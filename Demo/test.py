'''
Author: seven 865762826@qq.com
Date: 2023-06-13 21:14:56
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-17 21:37:58
FilePath: \libTSCANApi\Demo\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# import can
# from ctypes import *
# configs = [{'FChannel': 0, 'rate_baudrate': 500,
# 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 1, 'rate_baudrate': 500,
# 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 2, 'rate_baudrate': 500,
# 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}, {'FChannel': 3, 'rate_baudrate': 500,
# 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}]

# hwhandle = can.Bus(bustype="libtosun", configs=configs, is_include_tx=True, hwserial=b"")

# msg = can.Message(channel=0,arbitration_id=0x1,is_extended_id=False, is_remote_frame=False, dlc=8, data=[1, 2, 3, 4, 5, 6, 7, 8])

# hwhandle.send(msg)

# hwhandle.recv(1)

import os
from ldfparser import *
currentpath = os.path.dirname(__file__) # get current path 定义为：/home/pi/ldf/ldf.
a = parse_ldf(currentpath+"/../DataBases/LINDemo.ldf")
for Frame in a.frames:
    print(Frame)
    for Signal in Frame.signal_map:
        print("    ",Signal[1].name,Signal[1].width,Signal[1].init_value)
print(a)