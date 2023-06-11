import os
import cantools
from can.message import Message as Message
from .TSStructure import TLIBCAN,TLIBCANFD,DLC_DATA_BYTE_CNT

def tosun_convert_msg(msg):
    """
    TLIBCAN  TLIBCANFD msg convert to can.Message
    Easy python-can to use
    """
    if isinstance(msg, TLIBCAN):
        return Message(
            timestamp= float(msg.FTimeUs) / 1000000,
            arbitration_id=msg.FIdentifier,
            is_extended_id=msg.FProperties & 0x04,
            is_remote_frame=msg.FProperties & 0x02,
            is_error_frame=msg.FProperties & 0x80,
            channel=msg.FIdxChn,
            dlc=msg.FDLC,
            data=bytes(msg.FData),
            is_fd=False,
            is_rx=False if msg.FProperties & 0x01 else True,
        )
    elif isinstance(msg, TLIBCANFD):
        return Message(
            timestamp= float(msg.FTimeUs) / 1000000,
            arbitration_id=msg.FIdentifier,
            is_extended_id=msg.FProperties & 0x04,
            is_remote_frame=msg.FProperties & 0x02,
            channel=msg.FIdxChn,
            dlc=DLC_DATA_BYTE_CNT[msg.FDLC],
            data=bytes(msg.FData),
            is_fd=msg.FFDProperties & 0x01,
            is_rx=False if msg.FProperties & 0x01 else True,
            bitrate_switch=msg.FFDProperties & 0x02,
            error_state_indicator=msg.FFDProperties & 0x04,
            is_error_frame=msg.FProperties & 0x80
        )
    elif isinstance(msg, Message):
        return msg
    else:
        raise (f'Unknown message type: {type(msg)}')

def msg_convert_tosun(msg):
    """
    can.Message convert to  TLIBCAN  TLIBCANFD msg 
    Easy python-can to use
    """
    if isinstance(msg, TLIBCAN):
        return msg
    elif isinstance(msg, TLIBCANFD):
        return msg
    elif isinstance(msg, Message):
        if msg.is_fd:
            result = TLIBCANFD()
            result.FFDProperties = 0x01 | (0x02 if msg.bitrate_switch else 0x00) | \
                (0x04 if msg.error_state_indicator else 0x00)
        else:
            result = TLIBCAN()
        result.FIdxChn = msg.channel
        result.FProperties = 0x01 | (0x00 if msg.is_rx else 0x01) | \
            (0x02 if msg.is_remote_frame else 0x00) | \
            (0x04 if msg.is_extended_id else 0x00)
        try:
            result.FDLC = DLC_DATA_BYTE_CNT.index(msg.dlc)
        except:
            if msg.dlc < 0x10:
                result.FDLC = msg.dlc
            else:
                print("Message DLC input error")

        result.FIdentifier = msg.arbitration_id
        result.FTimeUs = int(msg.timestamp)
        for index, item in enumerate(msg.data):
            result.FData[index] = item
        return result
    else:
        raise (f'Unknown message type: {type(msg)}')

class TSDB():
    dbc_list_by_name = {}
    dbc_signal_list = {}
    filenames = []
    dbc_list_by_id = {}

    def __init__(self, dbcfile=''):
        if dbcfile !='':
            self.load_dbc(dbcfile)

    def load_dbc(self, dbcfile):
        '''return db index'''
        if dbcfile != '':
            data_path, filename = os.path.split(dbcfile)
            if filename not in self.filenames:
                self.filenames.append(filename)
            else:
                print(filename, " already exists")
                return
            try:
                db = cantools.db.load_file(dbcfile)
                for msg in db.messages:
                    if (msg.name not in self.dbc_list_by_name) and (msg.frame_id not in self.dbc_list_by_id):
                        self.dbc_list_by_name[msg.name] = msg
                        self.dbc_list_by_id[msg.frame_id] = msg
                        self.dbc_signal_list[msg.name] = msg.signals
                    else:
                        print(msg.name, ' already exists')

            except Exception as e:
                print(e)

    def __change_signal_value(self, msg, signal_dict: dict):
        try:
            msg_data_dict = self.dbc_list_by_id[msg.arbitration_id].decode(
                data=msg.data)
            for key in signal_dict:
                if key in msg_data_dict:
                    msg_data_dict[key] = signal_dict[key]
                else:
                    print('signal not exist')
                    return msg
            msg.data = self.dbc_list_by_id[msg.arbitration_id].encode(
                msg_data_dict)
            return msg
        except Exception as e:
            print(e)

    def set_signal_value(self, msg:TLIBCAN or TLIBCANFD or Message, signal_dict: dict):
        msg = tosun_convert_msg(msg)
        if msg.arbitration_id in self.dbc_list_by_id:
            return msg_convert_tosun(self.__change_signal_value(msg, signal_dict))

    def get_signal_value(self, msg, signalname):
        try:
            if isinstance(msg, Message):
                signaldict = self.dbc_list_by_id[msg.arbitration_id].decode(
                    data=msg.data)

            elif isinstance(msg, TLIBCAN) or isinstance(msg, TLIBCANFD):
                signaldict = self.dbc_list_by_id[msg.FIdentifier].decode(
                    data=bytes(msg.FData))
            else:
                signaldict = {}
            if signalname:
                if signalname in signaldict:
                    return signaldict[signalname]
                else:
                    print("signal not exist")
                    return None
            else:
                return signaldict
        except Exception as e:
            print(e)