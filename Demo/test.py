import can
from ctypes import *
configs = [{'FChannel': 0, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 1, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 2, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 3, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}]

hwhandle = can.Bus(bustype="libtosun", configs=configs, is_include_tx=True, hwserial=b"")

msg = can.Message(channel=0,arbitration_id=0x1,is_extended_id=False, is_remote_frame=False, dlc=8, data=[1, 2, 3, 4, 5, 6, 7, 8])

hwhandle.send(msg)

hwhandle.recv(1)

