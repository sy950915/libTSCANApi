import time
import queue
from .TSCommon import *

class TSUDS():
    msg_list = queue.Queue(maxsize=10000)
    def __init__(self, HwHandle, channel=0, dlc=8, request_id=0x1, respond_id=0x2, is_fd=False, is_std=True,
                fuction_id=0x3, timeout=0.1, bitrate_switch=False):
        self.HwHandle = HwHandle
        self.channel = channel
        try:
            self.dlc = DLC_DATA_BYTE_CNT.index(dlc)
        except:
            if dlc < 0x10:
                self.dlc = dlc
        self.is_fd = is_fd
        if not self.is_fd and self.dlc > 8:
            self.dlc = 8
        self.is_std = is_std
        self.bitrate_switch = bitrate_switch
        self.FFDProperties = 0x00 | (0x01 if self.is_fd else 0x00) | (
            0x02 if self.bitrate_switch else 0x00)
        self.FProperties = 0x01 | (0x04 if not self.is_std else 0x01)
        self.request_id = request_id
        self.respond_id = respond_id
        self.fuction_id = fuction_id
        self.timeout = timeout
        self.msg_data_size = DLC_DATA_BYTE_CNT[self.dlc]
        self.CANFDMsg = TLIBCANFD(FIdxChn=self.channel, FDLC=self.dlc, FIdentifier=self.request_id,
                                FFDProperties=self.FFDProperties, FProperties=self.FProperties,
                                FData=[0X30, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00])
        self.ONRxTx_Event = OnTx_RxFUNC_CANFD(self.on_tx_rx_event)
        tsapp_register_event_canfd(self.HwHandle, self.ONRxTx_Event)

    def on_tx_rx_event(self, ACAN):
        if ACAN.contents.FIdentifier == self.respond_id and ACAN.contents.FIdxChn == self.channel:
            msgdata = []
            for i in range(DLC_DATA_BYTE_CNT[ACAN.contents.FDLC]):
                msgdata.append(ACAN.contents.FData[i])
            self.msg_list.put(msgdata)

    def receive_can_Response(self):
        Datalist = []
        StartTime = time.perf_counter()
        FristDataLength = self.msg_data_size - 2
        DataLength = self.msg_data_size - 1
        while time.perf_counter() - StartTime < self.timeout:
            time.sleep(0.001)
            if not self.msg_list.empty():
                msgs = self.msg_list.get()
                N_PCItype = msgs[0] >> 4
                if 0 == N_PCItype:
                    if len(msgs) <= 8:
                        ResSize = (msgs[0] & 0xf)
                        if msgs[1] == 0x7f and msgs[3] == 0x78:
                            StartTime = time.perf_counter()
                            continue
                        for i in range(ResSize):
                            Datalist.append(msgs[i + 1])
                        return 0, Datalist
                    else:
                        ResSize = (msgs[1] & 0xff)
                        if msgs[2] == 0x7f and msgs[4] == 0x78:
                            StartTime = time.perf_counter()
                            continue
                        for i in range(ResSize):
                            Datalist.append(msgs[i + 2])
                        return 0, Datalist
                elif 1 == N_PCItype:
                    ResSize = (msgs[0] & 0xf) * 256 + msgs[1]
                    for i in range(len(msgs) - 2):
                        Datalist.append(msgs[i + 2])
                    if 0 == tsapp_transmit_canfd_async(self.HwHandle, self.CANFDMsg):
                        snCnt = 0x1
                        rxIndex = len(msgs) - 2
                        while rxIndex < ResSize and time.perf_counter() - StartTime < self.timeout:
                            if len(Datalist) == ResSize:
                                return 0, Datalist
                            elif not self.msg_list.empty():
                                msgs = self.msg_list.get()
                                N_PCItype = msgs[0] >> 4
                                if N_PCItype != 2:
                                    break
                                rxSN = msgs[0] & 0xf
                                if rxSN != snCnt & 0xf:
                                    break
                                snCnt += 1
                                if len(Datalist) != ResSize:
                                    if len(msgs) - 1 < ResSize - len(Datalist):
                                        for i in range(len(msgs) - 1):
                                            Datalist.append(msgs[i + 1])
                                        StartTime = time.perf_counter()
                                    else:
                                        for i in range(ResSize - len(Datalist)):
                                            Datalist.append(msgs[i + 1])
                                        StartTime = time.perf_counter()
                                    if len(Datalist) == ResSize:
                                        return 0, Datalist
                                else:
                                    return 0, Datalist
        return 161, Datalist

    def tstp_can_send_request(self, SendDatas):
        CANMsg = TLIBCANFD(FIdxChn=self.channel, FDLC=self.dlc, FIdentifier=self.request_id,
                        FFDProperties=self.FFDProperties, FProperties=self.FProperties,
                        )
        txIndex = self.msg_data_size - 2
        Datalengh = self.msg_data_size - 1
        MsgLen = len(SendDatas)
        if MsgLen <= Datalengh:
            if self.msg_data_size == self.dlc:
                CANMsg.FData[0] = MsgLen
                for i in range(MsgLen):
                    CANMsg.FData[i + 1] = SendDatas[i]
                return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
            else:
                if MsgLen <= Datalengh - 1:
                    for i in range(8, self.dlc):
                        if MsgLen < DLC_DATA_BYTE_CNT[i]:
                            CANMsg.FDLC = i
                            break
                    if CANMsg.FDLC == 8:
                        CANMsg.FData[0] = MsgLen
                        for i in range(MsgLen):
                            CANMsg.FData[i + 1] = SendDatas[i]
                        return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
                    else:
                        CANMsg.FData[0] = 0x00
                        CANMsg.FData[1] = MsgLen
                        for i in range(MsgLen):
                            CANMsg.FData[i + 2] = SendDatas[i]
                        return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
        CANMsg.FDLC = self.dlc
        CANMsg.FData[0] = 0x10 + (MsgLen >> 8 & 0xf)
        CANMsg.FData[1] = MsgLen & 0xff
        for i in range(txIndex):
            CANMsg.FData[i + 2] = SendDatas[i]
        if 0 == tsapp_transmit_canfd_async(self.HwHandle, CANMsg):
            Datalist = []
            snCnt = 1
            StartTime = time.perf_counter()
            while time.perf_counter() - StartTime < self.timeout:
                if not self.msg_list.empty():
                    msgs = self.msg_list.get()
                    if msgs[0] == 0x30:
                        while txIndex < MsgLen:
                            CANMsg.FData[0] = (0x20 | (snCnt & 0xf))
                            snCnt += 1
                            txLen = MsgLen - txIndex
                            if txLen > Datalengh:
                                txLen = Datalengh
                            else:
                                for i in range(txLen, Datalengh):
                                    CANMsg.FData[i + 1] = 0xAA
                            for i in range(txLen):
                                CANMsg.FData[i + 1] = SendDatas[i + txIndex]
                            if tsapp_transmit_canfd_async(self.HwHandle, CANMsg) != 0:
                                break
                            txIndex += txLen
                            if txIndex >= MsgLen:
                                return 0
                        return 161
            else:
                return 161

    def tstp_can_request_and_get_response(self, SendDatas):
        self.msg_list.queue.clear()
        ret = self.tstp_can_send_request(SendDatas)
        if ret == 0:
            ret, recv_data = self.receive_can_Response()
        else:
            return ret, []
        return ret, bytes(recv_data)

