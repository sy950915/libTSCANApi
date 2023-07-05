'''
Author: seven 865762826@qq.com
Date: 2023-06-11 13:29:24
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-05 02:54:10
'''
import queue
import time
from typing import Optional
import typing
from .TSDB import *
from .TSCommon import *
class TSMasterDevice():
    # HwHandle = size_t(0)
    # configs = {}
    # __hw_isconnect = False
    # include_own_message = False
    # __include_error_message = False
    # msg_list = queue.Queue(maxsize=100000)
    error_code = {1: "Index out of range",
                2: "Connect failed",
                3: "Device not found",
                4: "Error code not valid",
                5: "HID device already connected",
                6: "HID write data failed",
                7: "HID read data failed",
                8: "HID TX buffer overrun",
                9: "HID TX buffer too large",
                10: "HID RX packet report ID invalid",
                11: "HID RX packet length invalid",
                12: "Internal test failed",
                13: "RX packet lost",
                14: "SetupDiGetDeviceInterfaceDetai",
                15: "Create file failed",
                16: "CreateFile failed for read handle",
                17: "CreateFile failed for write handle",
                18: "HidD_SetNumInputBuffers",
                19: "HidD_GetPreparsedData",
                20: "HidP_GetCaps",
                21: "WriteFile",
                22: "GetOverlappedResult",
                23: "HidD_SetFeature",
                24: "HidD_GetFeature",
                25: "Send Feature Report DeviceIoContro",
                26: "Send Feature Report GetOverLappedResult",
                27: "HidD_GetManufacturerString",
                28: "HidD_GetProductString",
                29: "HidD_GetSerialNumberString",
                30: "HidD_GetIndexedString",
                31: "Transmit timed out",
                32: "HW DFU flash write failed",
                33: "HW DFU write without erase",
                34: "HW DFU crc check error",
                35: "HW DFU reset before crc check success",
                36: "HW packet identifier invalid",
                37: "HW packet length invalid",
                38: "HW internal test failed",
                39: "HW rx from pc packet lost",
                40: "HW tx to pc buffer overrun",
                41: "HW API parameter invalid",
                42: "DFU file load failed",
                43: "DFU header write failed",
                44: "Read status timed out",
                45: "Callback already exists",
                46: "Callback not exists",
                47: "File corrupted or not recognized",
                48: "Database unique id not found",
                49: "Software API parameter invalid",
                50: "Software API generic timed out",
                51: "Software API set hw config. failed",
                52: "Index out of bounds",
                53: "RX wait timed out",
                54: "Get I/O failed",
                55: "Set I/O failed",
                56: "An active replay is already running",
                57: "Instance not exists",
                58: "CAN message transmit failed",
                59: "No response from hardware",
                60: "CAN message not found",
                61: "User CAN receive buffer empty",
                62: "CAN total receive count <> desired count",
                63: "LIN config failed",
                64: "LIN frame number out of range",
                65: "LDF config failed",
                66: "LDF config cmd error",
                67: "TSMaster envrionment not ready",
                68: "reserved failed",
                69: "XL driver error",
                70: "index out of range",
                71: "string length out of range",
                72: "key is not initialized",
                73: "key is wrong",
                74: "write not permitted",
                75: "16 bytes multiple",
                76: "LIN channel out of range",
                77: "DLL not ready",
                78: "Feature not supported",
                79: "common service error",
                80: "read parameter overflow",
                81: "Invalid application channel mapping",
                82: "libTSMaster generic operation failed",
                83: "item already exists",
                84: "item not found",
                85: "logical channel invalid",
                86: "file not exists",
                87: "no init access, cannot set baudrate",
                88: "the channel is inactive",
                89: "the channel is not created",
                90: "length of the appname is out of range",
                91: "project is modified",
                92: "signal not found in database",
                93: "message not found in database",
                94: "TSMaster is not installed",
                95: "Library load failed",
                96: "Library function not found",
                97: 'cannot find libTSMaster.dll, use \"set_libtsmaster_location\" to set its location before calling initialize_lib_tsmaster',
                98: "PCAN generic operation error",
                99: "Kvaser generic operation error",
                100: "ZLG generic operation error",
                101: "ICS generic operation error",
                102: "TC1005 generic operation error",
                104: "Incorrect system variable type",
                105: "Message not existing, update failed",
                106: "Specified baudrate not available",
                107: "Device does not support sync. transmit",
                108: "Wait time not satisfied",
                109: "Cannot operate while app is connected",
                110: "Create file failed",
                111: "Execute python failed",
                112: "Current multiplexed signal is not active",
                113: "Get handle by logic channel failed",
                114: "Cannot operate while application is Connected, please stop application first",
                115: "File load failed",
                116: "Read LIN Data Failed",
                117: "FIFO not enabled",
                118: "Invalid handle",
                119: "Read file error",
                120: "Read to EOF",
                121: "Configuration not saved",
                122: "IP port open failed",
                123: "TCP connect failed",
                124: "Directory not exists",
                125: "Current library not supported",
                126: "Test is not running",
                127: "Server response not received",
                128: "Create directory failed",
                129: "Invalid argument type",
                130: "Read Data Package from Device Failed",
                131: "Precise replay is running",
                132: "Replay map is already",
                133: "User cancel input",
                134: "API check result is negative",
                135: "CANable generic error",
                136: "Wait criteria not satisfied",
                137: "Operation requires application connected",
                138: "Project path is used by another application",
                139: "Timeout for the sender to transmit data to the receiver",
                140: "Timeout for the receiver to transmit flow control to the sender",
                141: "Timeout for the sender to send first data frame after receiving FC frame",
                142: "Timeout for the receiver to receiving first CF frame after sending FC frame",
                143: "Serial Number Error",
                144: "Invalid flow status of the flow control frame",
                145: "Unexpected Protocol Data Unit",
                146: "Wait counter of the FC frame out of the maxWFT",
                147: "Buffer of the receiver is overflow",
                148: "TP Module is busy",
                149: "There is error from CAN Driver",
                150: "Handle of the TP Module is not exist",
                151: "UDS event buffer is full",
                152: "Handle pool is full, can not add new UDS module",
                153: "Pointer of UDS module is null",
                154: "UDS message is invalid",
                155: "No uds data received",
                156: "Handle of uds is not existing",
                157: "UDS module is not ready",
                158: "Transmit uds frame data failed",
                159: "This uds Service is not supported",
                160: "Time out to send uds request",
                161: "Time out to get uds response",
                162: "Get uds negative response",
                163: "Get uds negative response with expected NRC",
                164: "Get uds negative response with unexpected NRC",
                165: "UDS can tool is not ready",
                166: "UDS data is out of range",
                167: "Get unexpected UDS frame",
                168: "Receive unexpected positive response frame",
                169: "Receive positive response with wrong data",
                170: "Failed to get positive response",
                171: "Reserved UDS Error Code",
                172: "Receive negative response with unexpected NRC",
                173: "UDS service is busy",
                174: "Request download service must be performed before transfer data",
                175: "Length of the uds reponse is wrong",
                176: "Verdict value smaller than specification",
                177: "Verdict value greater than specification",
                178: "Verdict check failed",
                179: "Automation module not loaded, please load it first",
                180: "Panel not found",
                181: "Control not found in panel",
                182: "Panel not loaded, please load it first",
                183: "STIM signal not found",
                184: "Automation sub module not available",
                185: "Automation variant group not found",
                186: "Control not found in panel",
                187: "Panel control does not support this property",
                188: "RBS engine is not running",
                189: "This message does not support PDU container",
                190: "Data not available",
                191: "J1939 not supported",
                192: "Another J1939 PDU is already being transmitted",
                193: "Transmit J1939 PDU failed due to protocol error",
                194: "Transmit J1939 PDU failed due to node inactive",
                195: "API is called without license support",
                196: "Signal range check violation",
                197: "DataLogger read category failed",
                198: "Check Flash Bootloader Version Failed",
                199: "Log file not created",
                200: "Module is being edited by user",
                201: "The Logger device is busy, can not operation at the same time",
                202: "Master node transmit diagnostic package timeout",
                203: "Master node transmit frame failed",
                204: "Master node receive diagnostic package timeout",
                205: "Master node receive frame failed",
                206: "Internal time runs out before reception is completed ",
                207: "Master node received no response ",
                208: "Serial Number Error when receiving multi frames",
                209: "Slave node transmit diagnostic package timeout",
                210: "Slave node receive diagnostic pacakge timeout",
                211: "Slave node transmit frames error",
                212: "Slave node receive frames error",
                }
    def __init__(self, configs: typing.List[dict], hwserial: bytes = b'',
                is_include_tx: bool = False,
                dbc: bytes = b'',
                filters:typing.List[dict]=[]):
        initialize_lib_tscan(True,True,False)
        self.HwHandle = size_t(0)
        self.__hw_isconnect = False
        self.filters = filters
        self.include_own_message = is_include_tx
        self.configs = configs
        self.hwserial = hwserial
        self.dbc = dbc
        self.db = TSDB()
        if isinstance(hwserial, str):
            self.hwserial = hwserial.encode('utf8')
        self.connect()
    def connect(self):
        ret = tsapp_connect(self.hwserial, self.HwHandle)
        if ret == 0 or ret == 5:
            self.__hw_isconnect = True
            for filter in self.filters:
                AChannel = filter.get('channel',0)
                AId = filter.get('id',0x1)
                is_std = filter.get('is_std',True)
                tsfifo_add_can_canfd_pass_filter(self.HwHandle,AChannel,AId,is_std)
            for index, congfig in enumerate(self.configs):
                FChannel = congfig.get('FChannel',index)
                Rate_baudrate = congfig.get('rate_baudrate',500)
                data_baudrate = congfig.get('data_baudrate',2000)
                enable_120hm = congfig.get('enable_120hm',True)
                is_fd = congfig.get('is_fd',True)
                if is_fd:
                    tsapp_configure_baudrate_canfd(self.HwHandle, FChannel , Rate_baudrate,
                                                data_baudrate,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,enable_120hm)
                else:
                    tsapp_configure_baudrate_can(self.HwHandle, FChannel, Rate_baudrate,enable_120hm)
            # self.ONRxTx_Event = OnTx_RxFUNC_CANFD(self.on_tx_rx_event)
            # tsapp_register_event_canfd(self.HwHandle, self.ONRxTx_Event)
            # self.start_recv_time = time.perf_counter()
            if self.dbc!=b'':
                self.load_dbc(self.dbc)
        else:
            self.__hw_isconnect = False
            raise "HW CONNECT FAILED"
    def load_dbc(self, dbc):
        self.db.load_dbc(dbc)
    def unload_dbc_all(self):
        self.db.dbc_list_by_id.clear()
        self.db.dbc_list_by_name.clear()
    def set_singal_value(self, msg, singaldict:dict):
        return self.db.set_signal_value(msg, singaldict)
    def get_signal_value(self, msg, signal_name):
        return self.db.get_signal_value(msg, signal_name)
    def send_msg(self, msg, timeout: Optional[float] = 0.1, sync: bool = False, is_cyclic: bool = False):
        # timeout = timeout * 1000
        if self.__hw_isconnect:
            if isinstance(msg, TLIBCAN):
                if is_cyclic:
                    # '''timeout is cyclic time when is_cyclic is ture'''
                    tsapp_add_cyclic_msg_can(
                        self.HwHandle, msg, timeout * 1000)
                else:
                    if sync:
                        tsapp_transmit_can_sync(
                            self.HwHandle, msg, timeout * 1000)
                    else:
                        tsapp_transmit_can_async(self.HwHandle, msg)
            elif isinstance(msg, TLIBCANFD):
                if is_cyclic:
                    '''timeout is cyclic time when is_cyclic is ture'''
                    tsapp_add_cyclic_msg_canfd(
                        self.HwHandle, msg, timeout * 1000)
                else:
                    if sync:
                        tsapp_transmit_canfd_sync(
                            self.HwHandle, msg, timeout * 1000)
                    else:
                        tsapp_transmit_canfd_async(self.HwHandle, msg)
            elif isinstance(msg, Message):
                msg = msg_convert_tosun(msg)
                self.send_msg(msg, timeout, sync, is_cyclic)
            else:
                print("UNKOWN TYRE")
        else:
            raise "HW CONNECT FAILED"

    def recv(self, channel = 0,timeout: Optional[float] = 0.1) -> Message or None:
        start_time = time.perf_counter()
        while time.perf_counter() - start_time<= timeout:
            ACANFD = (TLIBCANFD*1)()
            buffersize = c_int32(1)
            tsfifo_receive_canfd_msgs(self.HwHandle,ACANFD,buffersize,channel,1 if self.include_own_message else 0)
            if buffersize.value==1:
                return tosun_convert_msg(ACANFD[0])
        return None
        # return self.msg_list.get() if not self.msg_list.empty() else None

    # def on_tx_rx_event(self, ACAN):
    #     if self.start_receive:
    #         msg_channel = self.filter.get('msg_channel',None)
    #         msg_id = self.filter.get('msg_id',None)
    #         # pass_no = self.filter.get('pass',True)
    #         if msg_channel != None and ACAN.contents.FIdxChn != msg_channel:
    #             return
    #         if msg_id != None and ACAN.contents.FIdentifier != msg_id:
    #             return
    #         if ACAN.contents.FProperties == 0x80:
    #             msg = Message(timestamp= float(ACAN.contents.FTimeUs) / 1000000,
    #                         arbitration_id=0xFFFFFFFF,
    #                         is_error_frame=True, data=[0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
    #             if self.__include_error_message:
    #                 if self.msg_list.full():
    #                     self.msg_list.get()
    #                 self.msg_list.put(msg)
    #         elif ACAN.contents.FProperties & 1 == 1:
    #             if self.include_own_message:
    #                 msg = tosun_convert_msg(ACAN.contents)
    #                 if self.msg_list.full():
    #                     self.msg_list.get()
    #                 self.msg_list.put(msg)
    #         else:
    #             msg = tosun_convert_msg(ACAN.contents)
    #             if self.msg_list.full():
    #                 self.msg_list.get()
    #             self.msg_list.put(msg)

    def tsdiag_can_create(self, pDiagModuleIndex: c_int32, AChnIndex: CHANNEL_INDEX, ASupportFDCAN: u8,
                        AMaxDLC: u8,
                        ARequestID: c_uint32, ARequestIDIsStd: bool, AResponseID: c_uint32, AResponseIDIsStd: bool,
                        AFunctionID: c_uint32, AFunctionIDIsStd: bool, timeout=0.1):
        self.timeout = c_int32(int(timeout * 1000))
        try:
            dlc = self.DLC_DATA_BYTE_CNT.index(AMaxDLC)
        except:
            dlc = AMaxDLC
        r = tsdiag_can_create(self.HwHandle,pDiagModuleIndex, AChnIndex, ASupportFDCAN, dlc, ARequestID,
                                ARequestIDIsStd,
                                AResponseID, AResponseIDIsStd, AFunctionID, AFunctionIDIsStd)
        return r

    def tsdiag_can_delete(self, pDiagModuleIndex: c_int32):
        r = tsdiag_can_delete(pDiagModuleIndex)
        return r

    def tstp_can_request_and_get_response(self, pDiagModuleIndex: c_int32, AReqDataArray, max_len=4095):
        if not isinstance(AReqDataArray, bytes):
            AReqDataArray = bytes(AReqDataArray)
        AResdata = create_string_buffer(max_len)
        AResponseDataSize = c_uint32(len(AResdata))

        r = tstp_can_request_and_get_response(pDiagModuleIndex, c_char_p(AReqDataArray), len(AReqDataArray),
                                                AResdata, byref(AResponseDataSize), self.timeout)
        return r, bytes(AResdata[:AResponseDataSize.value])

    def tstp_can_send_functional(self, pDiagModuleIndex: c_int32, AReqDataArray: bytearray):
        r = tstp_can_send_functional(pDiagModuleIndex, c_char_p(AReqDataArray), len(AReqDataArray),
                                        self.timeout)
        return r

    def tscan_get_error_description(self, ACode):
        return self.error_code[ACode]

    def shut_down(self):
        tsapp_disconnect_by_handle(self.HwHandle)
