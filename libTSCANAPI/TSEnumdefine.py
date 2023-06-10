'''
Author: seven 865762826@qq.com
Date: 2023-04-21 10:04:48
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-04-21 10:17:38
'''
from enum import IntEnum, IntFlag

class MSGType(IntEnum):
    CANMSG = 0
    CANFDMSG = 1
    LINMSG = 2
    FlexrayMSG = 3

class CHANNEL_INDEX(IntEnum):
    (CHN1, CHN2, CHN3, CHN4, CHN5, CHN6, CHN7, CHN8, CHN9, CHN10, CHN11, CHN12, CHN13, CHN14, CHN15, CHN16, CHN17,
        CHN18, CHN19, CHN20, CHN21, CHN22, CHN23, CHN24, CHN25, CHN26, CHN27, CHN28, CHN29, CHN30, CHN31, CHN32) = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29,
        30,
        31
    )

class TSTATISTICTYPE(IntEnum):
    IDX_CAN_STAT_BUSLOAD = 0
    IDX_CAN_STAT_PEAKLOAD =1
    IDX_CAN_STAT_STD_DATA_RATE=2
    IDX_CAN_STAT_STD_DATA_ALL=3
    IDX_CAN_STAT_EXT_DATA_RATE=4
    IDX_CAN_STAT_EXT_DATA_ALL=5
    IDX_CAN_STAT_STD_REMOTE_RATE=6
    IDX_CAN_STAT_STD_REMOTE_ALL=7
    IDX_CAN_STAT_EXT_REMOTE_RATE=8
    IDX_CAN_STAT_EXT_REMOTE_ALL=9
    IDX_CAN_STAT_ERR_FRAME_RATE=10
    IDX_CAN_STAT_ERR_FRAME_ALL=11
    
HW_dict = {
    "TS_UNKNOWN_DEVICE":0,
    "TSCAN_PRO":1,
    "TSCAN_Lite1" : 2,
    "TC1001" : 3,
    "TL1001" : 4,
    "TC1011" : 5,
    'TSInterface' : 6,
    'TC1002' : 7,
    'TC1014' : 8,
    'TSCANFD2517' : 9,
    'TC1026' : 10,
    'TC1016' : 11,
    'TC1012' : 12,
    'TC1013' : 13,
    'TLog1002' : 14,
    'TC1034' : 15,
}

class TLIB_TS_Device_Sub_Type(IntEnum):
    '''在通道映射时,该tsapp_set_mapping_verbose函数的参数5为TS_USB_DEVICE时 填入下列准确类型'''
    TS_UNKNOWN_DEVICE = 0
    TSCAN_PRO = 1
    TSCAN_Lite1 = 2
    TC1001 = 3
    TL1001 = 4
    TC1011 = 5
    TSInterface = 6
    TC1002 = 7
    TC1014 = 8
    TSCANFD2517 = 9
    TC1026 = 10
    TC1016 = 11
    TC1012 = 12
    TC1013 = 13
    TLog1002 = 14
    TC1034 = 15

class TLIBBusToolDeviceType(IntEnum):
    '''在通道映射时,该tsapp_set_mapping_verbose函数的参数5 填入准确类型'''
    BUS_UNKNOWN_TYPE = 0  
    TS_TCP_DEVICE = 1 #虚拟通道 TS Virtual Devices
    XL_USB_DEVICE = 2  #vector hardware devices
    TS_USB_DEVICE = 3  #TOSUN hardware devices
    PEAK_USB_DEVICE = 4 #PEAK hardware devices
    KVASER_USB_DEVICE = 5    #KVASER hardware devices
    RESERVED_DEVICE = 6 
    ICS_USB_DEVICE = 7   #ICS hardware devices
    TS_TC1005_DEVICE = 8 #TC1005 device

class TLIBApplicationChannelType(IntEnum):
    '''在通道映射时,该tsapp_set_mapping_verbose函数的参数2 填入准确类型'''
    APP_CAN = 0     #AppChannelType:CAN
    APP_LIN = 1     #AppChannelType:LIN
    APP_FlexRay = 2 #AppChannelType:FlexRay

class READ_TX_RX_DEF(IntEnum):
    '''在接收报文数据时 ONLY_RX_MESSAGES表示只获取接收报文 TX_RX_MESSAGES表示获取发送与接受报文,函数如下：
    tsfifo_receive_can_msgs  接收can报文
    tsfifo_receive_canfd_msgs 接收canfd报文 包括can报文
    tsfifo_receive_lin_msgs   接收lin报文
    tsfifo_receive_flexray_msgs 接受Flexray报文
    '''
    ONLY_RX_MESSAGES = 0
    TX_RX_MESSAGES = 1

class LIN_PROTOCOL(IntEnum):
    """设置LIN 版本协议
    使用函数：
    tsapp_configure_baudrate_lin
    """
    LIN_PROTOCOL_13 = 0  #lin 1.3
    LIN_PROTOCOL_20 = 1  #lin 2.0
    LIN_PROTOCOL_21 = 2  #lin 2.1
    LIN_PROTOCOL_J2602 = 3  #lin J2602

class T_LIN_NODE_FUNCTION(IntEnum):
    """设置LIN 主从节点
    使用函数：
    tslin_set_node_funtiontype
    需要注意,该函数需要在tsapp_connect 之后使用才能正常执行
    """
    T_MASTER_NODE = 0
    T_SLAVE_NODE = 1
    T_MONITOR_NODE = 2

class TLIBCANFDControllerType(IntEnum):
    """设置CANFD硬件 模式
    使用函数：
    tsapp_configure_baudrate_canfd
    tsapp_configure_canfd_regs
    """
    lfdtCAN = 0     #普通CAN    
    lfdtISOCAN = 1   #ISO CANFD
    lfdtNonISOCAN = 2  #Non-ISO CANFD

class TLIBCANFDControllerMode(IntEnum):
    """设置CANFD硬件 controller模式
    使用函数：
    tsapp_configure_baudrate_canfd
    tsapp_configure_canfd_regs
    """
    lfdmNormal = 0  #正常模式
    lfdmACKOff = 1  #关闭ACK模式
    lfdmRestricted = 2  #限制模式

class TSupportedObjType():
    """
    读取blf文件时,判断读取到的报文类型
    使用函数：
    tslog_blf_read_object
    """
    sotCAN = 0
    sotLIN = 1
    sotCANFD = 2
    sotRealtimeComment = 3
    sotUnknown = 0xFFFFFFF