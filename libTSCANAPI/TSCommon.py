'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:59:15
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-10 22:32:02
'''

from .TSStructure import *  
from .TSEnumdefine import * 
from .TSDirver import _os,dll

# Common Functions



tscan_get_error_description = dll.tscan_get_error_description
tscan_get_error_description.argtypes = [s32,charpp]
tscan_get_error_description.restype  = TS_ReturnType 


def check_status_operation(result, function, arguments):
    """Check the status and raise """
    if result != 0:
        ret = c_char_p()
        tscan_get_error_description(result, ret)
        print("TSDriverOperationError: " + str(function.__name__) + "(" + str(arguments) + ") returned " + str(result) + ": " + str(ret.value))
    return result

# 初始化函数 API函数使用之前 必须调用该函数 否则无法正常使用 在工程起始时 调用
"""
    Initialization function 
    There is no need to call it now because I will automatically call it when the program loads
example:
    initialize_lib_tscan(true,true,false)
"""
initialize_lib_tscan = dll.initialize_lib_tscan
initialize_lib_tscan.argtypes = [c_bool,c_bool,c_bool]
initialize_lib_tscan.restype = None  

# 释放函数 与 initialize_lib_tsmaster 或者 initialize_lib_tsmaster_with_project 成对出现 在工程结束后 调用
"""
    Release function 
    There is no need to call now because I will automatically release it at the end of the program
"""
finalize_lib_tscan = dll.finalize_lib_tscan
finalize_lib_tscan.argtypes = []
finalize_lib_tscan.restype = None 


# 连接
"""
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
    Returns:
        r:error code
    
    example:
        AHandle = c_size_t(0)
        ACount = 0
        r = tsapp_connect(b"1234568798DFE",AHandle) or r = tsapp_connect(b"",AHandle) 
"""
tsapp_connect = dll.tscan_connect
tsapp_connect.argtypes = [c_char_p,psize_t]  
tsapp_connect.restype = TS_ReturnType
tsapp_connect.errcheck = check_status_operation

# only windows supported now
if 'windows' in _os.lower():
    # 设置当前硬件存在CAN的通道数量
    """
        Args:
            AHandle (c_size_t): tsapp_connect retrun handle
        Returns:
            r:error code
        
        example:
            AHandle = c_size_t(0)
            ACount = 0
            r = tsapp_connect(b"1234568798DFE",AHandle) or tsapp_connect("",AHandle) 
            if(r==0 or r==5):  #0 or 5 :connect success
                print(AHandle)
                r = tscan_get_can_channel_count(AHandle,ACount)
    """

    tscan_get_can_channel_count = dll.tscan_get_can_channel_count
    tscan_get_can_channel_count.argtypes = [size_t,ps32]
    tscan_get_can_channel_count.restype = TS_ReturnType
    tscan_get_can_channel_count.errcheck = check_status_operation


    # 设置当前硬件存在LIN的通道数量
    """
        Args:
            AHandle (c_size_t): tsapp_connect retrun handle
        Returns:
            r:error code
        
        example:
            AHandle = c_size_t(0)
            ACount = 0
            r = tsapp_connect(b"1234568798DFE",AHandle) or tsapp_connect("",AHandle) 
            if(r==0 or r==5):  #0 or 5 :connect success
                print(AHandle)
                r = tscan_get_lin_channel_count(AHandle,ACount)
    """
    tscan_get_lin_channel_count = dll.tscan_get_lin_channel_count
    tscan_get_lin_channel_count.argtypes = [size_t,ps32]
    tscan_get_lin_channel_count.restype = TS_ReturnType
    tscan_get_lin_channel_count.errcheck = check_status_operation


    # 设置当前硬件存在Flexray的通道数量
    """
        Args:
            AHandle (c_size_t): tsapp_connect retrun handle
        Returns:
            r:error code
        
        example:
            AHandle = c_size_t(0)
            ACount = 0
            r = tsapp_connect(b"1234568798DFE",AHandle) or tsapp_connect("",AHandle) 
            if(r==0 or r==5):  #0 or 5 :connect success
                print(AHandle)
                r = tscan_get_flexray_channel_count(AHandle,ACount)
    """
    tscan_get_flexray_channel_count = dll.tscan_get_flexray_channel_count
    tscan_get_flexray_channel_count.argtypes = [size_t,ps32]
    tscan_get_flexray_channel_count.restype = TS_ReturnType
    tscan_get_flexray_channel_count.errcheck = check_status_operation
    """
    configure can regs include baudrate and termination resistor
    Args:
        ADeviceHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (CHANNEL_INDEX): chn_index
        ABaudrateKbps (float): baudrate
        ASEG1 (int): Phase buffer section1
        ASEG2 (int): Phase buffer section2
        APrescaler (int): APrescaler
        ASJ2 (int): BTL count
        AOnlyListen (c_uint32): is only listen
        A120 (c_uint32): enable termination resistor 

    Returns:
        error code
    
    example:
        tsapp_configure_can_regs(handle, CHANNEL_INDEX.CHN1, 500, 63, 16, 1, 80, 0, A120.A120_ENABLE)
    """
    tsapp_configure_can_regs = dll.tscan_configure_can_regs
    tsapp_configure_can_regs.argtypes = [size_t,s32, c_float, s32,s32,s32,s32,c_bool, c_bool]
    tsapp_configure_can_regs.restype = TS_ReturnType
    tsapp_configure_can_regs.errcheck = check_status_operation

    """
    configure canfd regs include baudrate and termination resistor

    Args:
        ADeviceHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (CHANNEL_INDEX): chn_index
        AArbBaudrateKbps (float): Arbbaudrate
        AArbSEG1 (int): Arb Phase buffer section1
        AArbSEG2 (int): Arb Phase buffer section2
        AArbPrescaler (int): ArbPrescaler
        AArbSJ2 (int): Arb BTL count
        ADataBaudrateKbps (float): Databaudrate
        ADataSEG1 (int): Data Phase buffer section1
        ADataSEG2 (int): Data Phase buffer section2
        ADataPrescaler (int): Data Prescaler
        ADataSJ2 (int): Data BTL count
        AControllerType (TLIBCANFDControllerType): can isocanfd non-isocanfd
        AControllerMode (TLIBCANFDControllerMode): normol ackoff
        AInstallTermResistor120Ohm (c_bool): enable termination resistor 

    Returns:
        error code
    example:
        error = tsapp_canfd_config(handle, CHANNEL_INDEX.CHN1, 500, 63, 16, 1, 80, 2000,63,16,1,80,TLIBCANFDControllerType.lfdtCAN,TLIBCANFDControllerMode.lfdmNormal, A120.A120_ENABLE)
    """
    tsapp_configure_canfd_regs = dll.tscan_configure_canfd_regs
    tsapp_configure_canfd_regs.argtypes = [size_t,s32, c_float, s32,s32,s32,s32,c_float, s32,s32,s32,s32,s32,s32, c_bool]
    tsapp_configure_canfd_regs.restype = TS_ReturnType
    tsapp_configure_canfd_regs.errcheck = check_status_operation
# UDS诊断
# CAN
# 创建诊断服务
# only windows supported now
    __tsdiag_can_create_mod = dll.tsdiag_can_create
    __tsdiag_can_create_mod.argtypes = [pu8,s32,u8,u8,s32,c_bool,s32,c_bool,s32,c_bool]
    __tsdiag_can_create_mod.restype = TS_ReturnType
    __tsdiag_can_create_mod.errcheck = check_status_operation

    __tsdiag_can_attach_to_tscan_tool = dll.tsdiag_can_attach_to_tscan_tool
    __tsdiag_can_attach_to_tscan_tool.argtypes = [s32,size_t]
    __tsdiag_can_attach_to_tscan_tool.restype = TS_ReturnType
    __tsdiag_can_attach_to_tscan_tool.errcheck = check_status_operation

    def tsdiag_can_create(HwHandle,pDiagModuleIndex: c_int32, AChnIndex: CHANNEL_INDEX, ASupportFDCAN: u8,AMaxDLC: u8,ARequestID: c_uint32, ARequestIDIsStd: bool, AResponseID: c_uint32, AResponseIDIsStd: bool,AFunctionID: c_uint32, AFunctionIDIsStd: bool):
        """
            udsHandle = c_int8(0)
            ChnIndex = CHANNEL_INDEX.CHN1
            ASupportFD  = c_byte(1)
            AMaxdlc = c_byte(8)
            reqID = c_int32(0x7e0)
            ARequestIDIsStd = False
            resID = c_int32(0x7e3)
            resIsStd = False
            AFctID = c_int32(0x7df)
            fctIsStd = False
            tsdiag_can_create(HWHandle,udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
            """
        try:
            dlc = DLC_DATA_BYTE_CNT.index(AMaxDLC)
        except:
            dlc = AMaxDLC
        r = __tsdiag_can_create_mod(pDiagModuleIndex, AChnIndex, ASupportFDCAN, dlc, ARequestID,
                                    ARequestIDIsStd,
                                    AResponseID, AResponseIDIsStd, AFunctionID, AFunctionIDIsStd)
        r = __tsdiag_can_attach_to_tscan_tool(pDiagModuleIndex, HwHandle)
        return r


    # 删除指定诊断服务
    tsdiag_can_delete = dll.tsdiag_can_delete
    tsdiag_can_delete.argtypes = [u8]
    tsdiag_can_delete.restype = TS_ReturnType
    tsdiag_can_delete.errcheck = check_status_operation

    # 删除所有诊断服务
    tsdiag_can_delete_all = dll.tsdiag_can_delete_all
    tsdiag_can_delete_all.argtypes = []
    tsdiag_can_delete_all.restype = TS_ReturnType
    tsdiag_can_delete_all.errcheck = check_status_operation

    # 功能寻址 请求
    tstp_can_send_functional = dll.tstp_can_send_functional
    tstp_can_send_functional.argtypes = [u8,pu8,s32]
    tstp_can_send_functional.restype = TS_ReturnType
    tstp_can_send_functional.errcheck = check_status_operation

    # 请求id 发送数据
    tstp_can_send_request = dll.tstp_can_send_request
    tstp_can_send_request.argtypes = [u8,pu8,s32]
    tstp_can_send_request.restype = TS_ReturnType
    tstp_can_send_request.errcheck = check_status_operation

    # 请求并接收数据
    tstp_can_request_and_get_response = dll.tstp_can_request_and_get_response
    tstp_can_send_request.argtypes = [u8,pu8,s32,pu8,ps32]
    tstp_can_send_request.restype = TS_ReturnType
    tstp_can_send_request.errcheck = check_status_operation

    # 相关诊断服务
    # 10 服务
    tsdiag_can_session_control = dll.tsdiag_can_session_control
    tsdiag_can_session_control.argtypes = [u8,u8]
    tsdiag_can_session_control.restype = TS_ReturnType
    tsdiag_can_session_control.errcheck = check_status_operation

    # 31
    tsdiag_can_routine_control = dll.tsdiag_can_routine_control
    tsdiag_can_routine_control.argtypes = [u8,u8,u16]
    tsdiag_can_routine_control.restype = TS_ReturnType
    tsdiag_can_routine_control.errcheck = check_status_operation

    # 28
    tsdiag_can_communication_control = dll.tsdiag_can_communication_control
    tsdiag_can_communication_control.argtypes = [u8,u8]
    tsdiag_can_communication_control.restype = TS_ReturnType
    tsdiag_can_communication_control.errcheck = check_status_operation

    # 27 get seed
    tsdiag_can_security_access_request_seed = dll.tsdiag_can_security_access_request_seed
    tsdiag_can_security_access_request_seed.argtypes = [u8,s32,pu8,ps32]
    tsdiag_can_security_access_request_seed.restype = TS_ReturnType
    tsdiag_can_security_access_request_seed.errcheck = check_status_operation

    # 27 send key
    tsdiag_can_security_access_send_key = dll.tsdiag_can_security_access_send_key
    tsdiag_can_security_access_send_key.argtypes = [u8,s32,pu8,ps32]
    tsdiag_can_security_access_send_key.restype = TS_ReturnType
    tsdiag_can_security_access_send_key.errcheck = check_status_operation

    # 34
    tsdiag_can_request_download = dll.tsdiag_can_request_download
    tsdiag_can_request_download.argtypes = [u8,u32,u32]
    tsdiag_can_request_download.restype = TS_ReturnType
    tsdiag_can_request_download.errcheck = check_status_operation

    # 35
    tsdiag_can_request_upload = dll.tsdiag_can_request_upload
    tsdiag_can_request_upload.argtypes = [u8,s32,s32]
    tsdiag_can_request_upload.restype = TS_ReturnType
    tsdiag_can_request_upload.errcheck = check_status_operation

    # 36
    tsdiag_can_transfer_data = dll.tsdiag_can_transfer_data
    tsdiag_can_transfer_data.argtypes = [u8,pu8,s32,s32]
    tsdiag_can_transfer_data.restype = TS_ReturnType
    tsdiag_can_transfer_data.errcheck = check_status_operation

    # 37
    tsdiag_can_request_transfer_exit = dll.tsdiag_can_request_transfer_exit
    tsdiag_can_request_transfer_exit.argtypes = [u8]
    tsdiag_can_request_transfer_exit.restype = TS_ReturnType
    tsdiag_can_request_transfer_exit.errcheck = check_status_operation

    # 2E
    tsdiag_can_write_data_by_identifier = dll.tsdiag_can_write_data_by_identifier
    tsdiag_can_write_data_by_identifier.argtypes = [u8,u16,pu8,s32]
    tsdiag_can_write_data_by_identifier.restype = TS_ReturnType
    tsdiag_can_write_data_by_identifier.errcheck = check_status_operation

    # 22
    tsdiag_can_read_data_by_identifier = dll.tsdiag_can_read_data_by_identifier
    tsdiag_can_read_data_by_identifier.argtypes = [u8,u16,pu8,ps32]
    tsdiag_can_read_data_by_identifier.restype = TS_ReturnType
    tsdiag_can_read_data_by_identifier.errcheck = check_status_operation

    # LIN 诊断
    # 诊断请求
    tstp_lin_master_request = dll.tstp_lin_master_request
    tstp_lin_master_request.argtypes = [s32,u8,pu8,s32,s32]
    tstp_lin_master_request.restype = TS_ReturnType
    tstp_lin_master_request.errcheck = check_status_operation
    # 
    tstp_lin_master_request_intervalms = dll.tstp_lin_master_request_intervalms
    tstp_lin_master_request_intervalms.argtypes = [s32,u16]
    tstp_lin_master_request_intervalms.restype = TS_ReturnType
    tstp_lin_master_request_intervalms.errcheck = check_status_operation
    # 重启
    tstp_lin_reset = dll.tstp_lin_reset
    tstp_lin_reset.argtypes = [s32]
    tstp_lin_reset.restype = TS_ReturnType
    tstp_lin_reset.errcheck = check_status_operation

    # 从节点响应
    tstp_lin_slave_response_intervalms = dll.tstp_lin_slave_response_intervalms
    tstp_lin_slave_response_intervalms.argtypes = [s32,u16]
    tstp_lin_slave_response_intervalms.restype = TS_ReturnType
    tstp_lin_slave_response_intervalms.errcheck = check_status_operation

    # 22
    tsdiag_lin_read_data_by_identifier = dll.tsdiag_lin_read_data_by_identifier
    tsdiag_lin_read_data_by_identifier.argtypes = [s32,u8,u16,pu8,pu8,ps32,s32]
    tsdiag_lin_read_data_by_identifier.restype = TS_ReturnType
    tsdiag_lin_read_data_by_identifier.errcheck = check_status_operation

    # 2E
    tsdiag_lin_write_data_by_identifier = dll.tsdiag_lin_write_data_by_identifier
    tsdiag_lin_write_data_by_identifier.argtypes = [s32,u8,u16,pu8,s32,pu8,pu8,ps32,s32]
    tsdiag_lin_write_data_by_identifier.restype = TS_ReturnType
    tsdiag_lin_write_data_by_identifier.errcheck = check_status_operation

    # 10
    tsdiag_lin_session_control = dll.tsdiag_lin_session_control
    tsdiag_lin_session_control.argtypes = [s32,u8,u8,s32]
    tsdiag_lin_session_control.restype = TS_ReturnType
    tsdiag_lin_session_control.errcheck = check_status_operation

    # 
    tsdiag_lin_fault_memory_clear = dll.tsdiag_lin_fault_memory_clear
    tsdiag_lin_fault_memory_clear.argtypes = [s32,u8,u8,s32]
    tsdiag_lin_fault_memory_clear.restype = TS_ReturnType
    tsdiag_lin_fault_memory_clear.errcheck = check_status_operation

    # 
    tsdiag_lin_fault_memory_read = dll.tsdiag_lin_fault_memory_read
    tsdiag_lin_fault_memory_read.argtypes = [s32,u8,u8,s32]
    tsdiag_lin_fault_memory_read.restype = TS_ReturnType
    tsdiag_lin_fault_memory_read.errcheck = check_status_operation





# CAN 通道参数配置
"""
    set  AChnIdx can baudrate include termination resistor 

    Args:
        ADeviceHandle (c_size_t): tsapp_connect retrun handle
        AChnIdx (CHANNEL_INDEX): can channle index
        ARateKbps (c_double): baudrate
        A120 (A120): enable termination resistor 

    Returns:
        error code
    example:
        tsapp_configure_baudrate_can(handle,CHANNEL_INDEX.CHN1,500,A120.DEABLEA120)
"""
tsapp_configure_baudrate_can = dll.tscan_config_can_by_baudrate
tsapp_configure_baudrate_can.argtypes = [size_t,s32, c_double, c_bool]
tsapp_configure_baudrate_can.restype = TS_ReturnType
tsapp_configure_baudrate_can.errcheck = check_status_operation

# CANFD 通道参数配置
"""
set  AChnIdx canfd baudrate include termination resistor

Args:
    ADeviceHandle (c_size_t): tsapp_connect retrun handle
    AChnIdx (CHANNEL_INDEX): chn_index
    ARateKbps (c_double): Rate baudrate
    ADataKbps (c_double): data baudrate
    AControllerType (TLIBCANFDControllerType): can isocanfd non-isocanfd
    AControllerMode (TLIBCANFDControllerMode): normol ackoff 
    A120 (A120): enable termination resistor 
Returns:
    error code

example:
    tsapp_configure_baudrate_canfd(handle,CHANNEL_INDEX.CHN1,500,2000,TLIBCANFDControllerType.lfdtCAN,TLIBCANFDControllerMode.lfdmNormal,A120.A120_ENABLE)
"""
tsapp_configure_baudrate_canfd = dll.tscan_config_canfd_by_baudrate
tsapp_configure_baudrate_canfd.argtypes = [size_t,s32, c_double,c_double,s32,s32,c_bool]
tsapp_configure_baudrate_canfd.restype = TS_ReturnType
tsapp_configure_baudrate_canfd.errcheck = check_status_operation


# LIN 通道参数配置
"""
    set lin baudrate
    Args:
        ADeviceHandle (c_size_t): tsapp_connect retrun handle
        AChnIdx (CHANNEL_INDEX): lin chnidx
        ARateKbps (c_double): baudrate

    Returns:
        error code
    example:
        tsapp_configure_baudrate_lin(handle,0,c_double(19.2))
"""
tsapp_configure_baudrate_lin = dll.tslin_config_baudrate
tsapp_configure_baudrate_lin.argtypes = [size_t,s32, double, s32]
tsapp_configure_baudrate_lin.restype = TS_ReturnType
tsapp_configure_baudrate_lin.errcheck = check_status_operation


# 设置LIN模式
"""
set lin node funtiontype

Args:
    ADeviceHandle (c_size_t): tsapp_connect retrun handle
    AChnIdx (CHANNEL_INDEX): lin chnidx
    AFunctionType (T_LIN_NODE_FUNCTION): T_MASTER_NODE T_SLAVE_NODE
example:
    tsapp_set_node_funtiontype(handle,0,T_LIN_NODE_FUNCTION.T_MASTER_NODE)

Returns:
    error code
"""
tslin_set_node_funtiontype = dll.tslin_set_node_funtiontype
tslin_set_node_funtiontype.argtypes=[size_t,s32, u8]
tslin_set_node_funtiontype.restype = TS_ReturnType
tslin_set_node_funtiontype.errcheck = check_status_operation

# 获取在线硬件 参数必须为变量
"""
    Args:
        ADeviceCount (c_uint32): _description_ :get devices count 

    Returns:
        r:error_code ADeviceCount:get devices count
    example:
        ADeviceCount = c_uint32(0)
        r = tscan_scan_devices(ADeviceCount)
        if r==0:       #0 :get success   
            print(ADeviceCount)
"""
tscan_scan_devices = dll.tscan_scan_devices
tscan_scan_devices.argtypes=[ps32]
tscan_scan_devices.restype = TS_ReturnType
tscan_scan_devices.errcheck = check_status_operation

# 通过索引获取硬件（名称、描述和描述数据）
"""
    get hw info
    Args:
        ADeviceCount (c_uint32): hw_index 

    Returns:
        FManufacturer, FProduct, FSerial
    example:
        ADeviceCount = c_uint32(0)
        r = tscan_scan_devices(ADeviceCount)
        if r==0:       #0 :get success
            AFManufacturer = POINTER(POINTER(c_char))()
            AFProduct = POINTER(POINTER(c_char))()
            AFSerial = POINTER(POINTER(c_char))()
            for i in range(ADeviceCount):
                tscan_get_device_info(i,AFManufacturer,AFProduct,AFSerial)
                
"""
tscan_get_device_info = dll.tscan_get_device_info
tscan_get_device_info.argtypes=[size_t,charpp,charpp,charpp]
tscan_get_device_info.restype = TS_ReturnType
tscan_get_device_info.errcheck = check_status_operation


# 断开指定连接
"""
    disconnect by handle
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle

    Returns:
        error code
    
    example:
        tsapp_disconnect_by_handle(handle)
"""
tscan_disconnect_by_handle = dll.tscan_disconnect_by_handle
tscan_disconnect_by_handle.argtypes = [size_t]  
tscan_disconnect_by_handle.restype = TS_ReturnType
tscan_disconnect_by_handle.errcheck = check_status_operation
tscan_disconnect_by_handle

# 断开所有设备连接
""" tsapp_disconnect_all() """
tsapp_disconnect_all = dll.tscan_disconnect_all_devices
tsapp_disconnect_all.argtypes = []  
tsapp_disconnect_all.restype = TS_ReturnType
tsapp_disconnect_all.errcheck = check_status_operation
tsapp_disconnect_all

# 注销所有预发送事件
tscan_unregister_pretx_events_all = dll.tscan_unregister_pretx_events_all
tscan_unregister_pretx_events_all.argtypes = [size_t]  
tscan_unregister_pretx_events_all.restype = TS_ReturnType
tscan_unregister_pretx_events_all.errcheck = check_status_operation
tscan_unregister_pretx_events_all



# 是否使能总线数据统计
"""
    disconnect by handle
    Args:
        bRunning (c_bool): 是否启动

    Returns:
        void
    
    example:
        tscan_set_auto_calc_bus_statistics(true)
"""
tscan_set_auto_calc_bus_statistics = dll.tscan_set_auto_calc_bus_statistics
tscan_set_auto_calc_bus_statistics.argtypes = [c_bool]  
tscan_set_auto_calc_bus_statistics.restype = None

# 获取总线统计数据
"""
Args:
    AHandle:connect handle
    AChnBase0:hw channel
    AIndex:TSTATISTICTYPE get bus type
example:
    tscan_get_bus_status(Handle,0,TSTATISTICTYPE.IDX_CAN_STAT_BUSLOAD)
"""
tscan_get_bus_status = dll.tscan_get_bus_status
tscan_get_bus_status.argtypes = [size_t,s32,s32]  
tscan_get_bus_status.restype = double

# clear bus statistic
"""
example:
    tscan_clear_can_bus_statistic()
"""
tscan_clear_can_bus_statistic = dll.tscan_clear_can_bus_statistic
tscan_clear_can_bus_statistic.argtypes = [] 
tscan_clear_can_bus_statistic.restype = None


# TSCANAPI

# CAN报文发送

# 异步单帧发送CAN报文
"""
    sync send can msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCAN): can msg
    example:    
        msg = TLIBCAN(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_can_async(handle,msg)
    Returns:
        error code
    """
tsapp_transmit_can_async = dll.tscan_transmit_can_async
tsapp_transmit_can_async.argtypes = [size_t,PCAN]  
tsapp_transmit_can_async.restype = TS_ReturnType
tsapp_transmit_can_async.errcheck = check_status_operation

# 同步单帧发送CAN报文
"""
    sync send can msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCAN): can msg
        ATimeoutMS (c_uint32): timeout in ms

    Returns:
        error code
    example:
        msg = TLIBCAN(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_can_sync(handle,msg,100)
    """
tsapp_transmit_can_sync = dll.tscan_transmit_can_sync
tsapp_transmit_can_sync.argtypes = [size_t,PCAN,u32]  
tsapp_transmit_can_sync.restype = TS_ReturnType
tsapp_transmit_can_sync.errcheck = check_status_operation


# 增加周期发送CAN报文
"""
    cyclic send can msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCAN): can msg
        ATimeoutMS (c_int32): timeout in ms
    example:    
        msg = TLIBCAN(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tscan_add_cyclic_msg_can(handle,msg,c_float(100))
    Returns:
        error code
    """
tsapp_add_cyclic_msg_can = dll.tscan_add_cyclic_msg_can
tsapp_add_cyclic_msg_can.argtypes = [size_t,PCAN,c_float]  
tsapp_add_cyclic_msg_can.restype = TS_ReturnType
tsapp_add_cyclic_msg_can.errcheck = check_status_operation

# 删除周期发送CAN报文
"""
    delete cyclic send canfd msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCANFD): canfd msg
    example:    
        msg = TLIBCANFD(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_delete_cyclic_msg_can(handle,msg)
    Returns:
        error code
"""
tsapp_delete_cyclic_msg_can = dll.tscan_delete_cyclic_msg_can
tsapp_delete_cyclic_msg_can.argtypes = [size_t,PCAN]  
tsapp_delete_cyclic_msg_can.restype = TS_ReturnType
tsapp_delete_cyclic_msg_can.errcheck = check_status_operation

# 异步单帧发送CANFD报文
"""
    async send canfd msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCANFD): canfd msg
    example:    
        msg = TLIBCANFD(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_canfd_async(handle,msg)
    Returns:
        error code
    """
tsapp_transmit_canfd_async = dll.tscan_transmit_can_async
tsapp_transmit_canfd_async.argtypes = [size_t,PCANFD]  
tsapp_transmit_canfd_async.restype = TS_ReturnType
tsapp_transmit_canfd_async.errcheck = check_status_operation

# 同步单帧发送CANFD报文
"""
    sync send canfd msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCANFD): canfd msg
        ATimeoutMS (c_int32): timeout in ms
    example:    
        msg = TLIBCANFD(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_canfd_sync(handle,msg,100)
    Returns:
        error code
"""
tsapp_transmit_canfd_sync = dll.tscan_transmit_canfd_sync
tsapp_transmit_canfd_sync.argtypes = [size_t,PCANFD,u32]  
tsapp_transmit_canfd_sync.restype = TS_ReturnType
tsapp_transmit_canfd_sync.errcheck = check_status_operation

# 增加周期发送CANFD报文
"""
    cyclic send canfd msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCANFD): canfd msg
        ATimeoutMS (c_int32): timeout in ms
    example:    
        msg = TLIBCANFD(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_add_cyclic_msg_canfd(handle,msg,c_float(100))
    Returns:
        error code
    """
tsapp_add_cyclic_msg_canfd = dll.tscan_add_cyclic_msg_canfd
tsapp_add_cyclic_msg_canfd.argtypes = [size_t,PCANFD,c_float]  
tsapp_add_cyclic_msg_canfd.restype = TS_ReturnType
tsapp_add_cyclic_msg_canfd.errcheck = check_status_operation

# 删除周期发送CANFD报文
"""
    delete cyclic send canfd msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBCANFD): canfd msg
    example:    
        msg = TLIBCANFD(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_delete_cyclic_msg_canfd(handle,msg)
    Returns:
        error code
    """
tsapp_delete_cyclic_msg_canfd = dll.tscan_delete_cyclic_msg_canfd
tsapp_delete_cyclic_msg_canfd.argtypes = [size_t,PCANFD]  
tsapp_delete_cyclic_msg_canfd.restype = TS_ReturnType
tsapp_delete_cyclic_msg_canfd.errcheck = check_status_operation


# CAN报文接收
# 接收can 报文
"""
    receive can msgs

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ADataBuffers (TLIBCAN): can buffer 
        ADataBufferSize (c_int32): can buffer size
        chn (c_int32): can channel
        ARxTx (c_int8): include tx
    Returns:
        error_code TLIBCAN_buffer TLIBCAN_bufferSize
    example:    
        canbuffer = (TLIBCAN * 100)()
        size = c_int32(100)
        tsfifo_receive_can_msgs(handle, canbuffer, size, 0, 1)
        for i in canbuffer:
            string = ''
            for index in range(i.FActualPayloadLength):
                string += hex(i.FData[index]) + ' '
    """
tsfifo_receive_can_msgs = dll.tsfifo_receive_can_msgs
tsfifo_receive_can_msgs.argtypes = [size_t,PCAN,ps32,s32,s32]  
tsfifo_receive_can_msgs.restype = TS_ReturnType
tsfifo_receive_can_msgs.errcheck = check_status_operation

# 清除fifo中can报文数量
"""
    clear can receive buffers
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        CHN (CHANNEL_INDEX): can channel idnex

    Returns:
        error code
        
    example:
        tsfifo_clear_can_receive_buffers(handle,CHANNEL_INDEX.CHN1)
    """
tsfifo_clear_can_receive_buffers = dll.tsfifo_clear_can_receive_buffers
tsfifo_clear_can_receive_buffers.argtypes = [size_t]  
tsfifo_clear_can_receive_buffers.restype = TS_ReturnType
tsfifo_clear_can_receive_buffers.errcheck = check_status_operation

# 获取fifo 中can报文数量
"""
    get can buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_can_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_can_buffer_frame_count = dll.tsfifo_read_can_buffer_frame_count
tsfifo_read_can_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_can_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX can报文数量
"""
    get can buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_can_tx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_can_tx_buffer_frame_count = dll.tsfifo_read_can_tx_buffer_frame_count
tsfifo_read_can_tx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_can_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX can报文数量
"""
    get can buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_can_rx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_can_rx_buffer_frame_count = dll.tsfifo_read_can_rx_buffer_frame_count
tsfifo_read_can_rx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_can_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_can_rx_buffer_frame_count.errcheck = check_status_operation

# CAN 回调事件

# 注册预发送事件
"""
    register pre tx can event
    Sending a message will trigger and can modify the message data
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CAN): function

    Returns:
        error code
    example:
        def on_can(ACAN):
            ACAN.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ACAN.contents.FIdentifier == 1:
                ACAN.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_can_event = OnTx_RxFUNC_CAN(on_can)
        tsapp_register_event_can(Handle,on_can_event)
    """
tsapp_register_pretx_event_can = dll.tscan_register_pretx_event_can
tsapp_register_pretx_event_can.argtypes = [size_t,OnTx_RxFUNC_CAN]  
tsapp_register_pretx_event_can.restype = TS_ReturnType
tsapp_register_pretx_event_can.errcheck = check_status_operation

# 注销预发送事件
"""
    unregister pre tx can event
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CAN): function

    Returns:
        error code
    example:
        def on_can(ACAN):
            ACAN.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ACAN.contents.FIdentifier == 1:
                ACAN.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_can_event = OnTx_RxFUNC_CAN(on_can)
        tsapp_unregister_event_can(Handle,on_can_event)
    """
tsapp_unregister_pretx_event_can = dll.tscan_unregister_pretx_event_can
tsapp_unregister_pretx_event_can.argtypes = [size_t,OnTx_RxFUNC_CAN]  
tsapp_unregister_pretx_event_can.restype = TS_ReturnType
tsapp_unregister_pretx_event_can.errcheck = check_status_operation

# 注册rx_tx事件
"""
    register canfd event
    Triggered when there is message transmission on the bus
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_can(ACAN):
            print(ACAN.contents.FData[0])
            
        on_can_event = OnTx_RxFUNC_CANFD(on_can)
        tsapp_register_event_canfd(Handle,on_can_event)
    """
tsapp_register_event_can = dll.tscan_register_event_canfd
tsapp_register_event_can.argtypes = [size_t,OnTx_RxFUNC_CAN]  
tsapp_register_event_can.restype = TS_ReturnType
tsapp_register_event_can.errcheck = check_status_operation

# 注销rx_tx事件
"""
    unregister canfd event
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_can(ACAN):
            print(ACAN.contents.FData[0])
            
        on_can_event = OnTx_RxFUNC_CANFD(on_can)
        tsapp_unregister_event_canfd(Handle,on_can_event)
"""
tsapp_unregister_event_can = dll.tscan_unregister_event_canfd
tsapp_unregister_event_can.argtypes = [size_t,OnTx_RxFUNC_CAN]  
tsapp_unregister_event_can.restype = TS_ReturnType
tsapp_unregister_event_can.errcheck = check_status_operation


# 接收canfd 报文
"""
    receive canfd msgs

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ADataBuffers (TLIBCANFD): can buffer 
        ADataBufferSize (c_int32): can buffer size
        chn (c_int32): can channel
        ARxTx (c_int8): include tx
    Returns:
        error_code TLIBCANFD_buffer TLIBCANFD_bufferSize
    example:    
        canbuffer = (TLIBCANFD * 100)()
        size = c_int32(100)
        tsapp_receive_canfd_msgs(handle, canbuffer, size, 0, 1)
        for i in canbuffer:
            string = ''
            for index in range(i.FActualPayloadLength):
                string += hex(i.FData[index]) + ' '
"""
tsfifo_receive_canfd_msgs = dll.tsfifo_receive_canfd_msgs
tsfifo_receive_canfd_msgs.argtypes = [size_t,PCANFD,ps32,s32,s32]  
tsfifo_receive_canfd_msgs.restype = TS_ReturnType
tsfifo_receive_canfd_msgs.errcheck = check_status_operation

# 获取fifo 中can报文数量
"""
    get canfd buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_canfd_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_canfd_buffer_frame_count = dll.tsfifo_read_canfd_buffer_frame_count
tsfifo_read_canfd_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_canfd_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX can报文数量
"""
    get canfd buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_canfd_tx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_canfd_tx_buffer_frame_count = dll.tsfifo_read_canfd_tx_buffer_frame_count
tsfifo_read_canfd_tx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_canfd_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX can报文数量
"""
    get canfd buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): can channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_canfd_rx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_canfd_rx_buffer_frame_count = dll.tsfifo_read_canfd_rx_buffer_frame_count
tsfifo_read_canfd_rx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_canfd_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_canfd_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 canfd fifo
"""
    clear canfd receive buffers
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        CHN (CHANNEL_INDEX): canfd channel idnex

    Returns:
        error code
        
    example:
        tsfifo_clear_canfd_receive_buffers(handle,CHANNEL_INDEX.CHN1)
    """
tsfifo_clear_canfd_receive_buffers = dll.tsfifo_clear_canfd_receive_buffers
tsfifo_clear_canfd_receive_buffers.argtypes = [size_t,s32,ps32]  
tsfifo_clear_canfd_receive_buffers.restype = TS_ReturnType
tsfifo_clear_canfd_receive_buffers.errcheck = check_status_operation

# CANFD 回调事件
# 注册预发送事件
"""
    register pre tx can event
    Sending a message will trigger and can modify the message data
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_canfd(ACANFD):
            ACANFD.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ACANFD.contents.FIdentifier == 1:
                ACANFD.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_canfd_event = OnTx_RxFUNC_CANFD(on_canfd)
        tsapp_register_event_canfd(Handle,on_canfd_event)
    """
tsapp_register_pretx_event_canfd = dll.tscan_register_pretx_event_canfd
tsapp_register_pretx_event_canfd.argtypes = [size_t,OnTx_RxFUNC_CANFD]  
tsapp_register_pretx_event_canfd.restype = TS_ReturnType
tsapp_register_pretx_event_canfd.errcheck = check_status_operation

# 注销预发送事件
"""
    unregister pre tx can event
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_canfd(ACANFD):
            ACANFD.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ACANFD.contents.FIdentifier == 1:
                ACANFD.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_canfd_event = OnTx_RxFUNC_CANFD(on_canfd)
        tsapp_unregister_event_canfd(Handle,on_canfd_event)
    """
tsapp_unregister_pretx_event_canfd = dll.tscan_unregister_pretx_event_canfd
tsapp_unregister_pretx_event_canfd.argtypes = [size_t,OnTx_RxFUNC_CANFD]  
tsapp_unregister_pretx_event_canfd.restype = TS_ReturnType
tsapp_unregister_pretx_event_canfd.errcheck = check_status_operation

# 注册rx_tx事件
"""
    register canfd event
    Triggered when there is message transmission on the bus
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_canfd(ACANFD):
            print(ACANFD.contents.FData[0])
            
        on_canfd_event = OnTx_RxFUNC_CANFD(on_canfd)
        tsapp_register_event_canfd(Handle,on_canfd_event)
    """
tsapp_register_event_canfd = dll.tscan_register_event_canfd
tsapp_register_event_canfd.argtypes = [size_t,OnTx_RxFUNC_CANFD]  
tsapp_register_event_canfd.restype = TS_ReturnType
tsapp_register_event_canfd.errcheck = check_status_operation

# 注销rx_tx事件
"""
    unregister canfd event
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_CANFD): function

    Returns:
        error code
    example:
        def on_canfd(ACANFD):
            print(ACANFD.contents.FData[0])
            
        on_canfd_event = OnTx_RxFUNC_CANFD(on_canfd)
        tsapp_unregister_event_canfd(Handle,on_canfd_event)
"""
tsapp_unregister_event_canfd = dll.tscan_unregister_event_canfd
tsapp_unregister_event_canfd.argtypes = [size_t,OnTx_RxFUNC_CANFD]  
tsapp_unregister_event_canfd.restype = TS_ReturnType
tsapp_unregister_event_canfd.errcheck = check_status_operation

# LIN API
# LIN 发送报文
# 异步单帧发送LIN报文
"""
    async send lin msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBLIN): lin msg
    Returns:
        error code
    example:
        msg = TLIBLIN(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_lin_async(handle,msg)
    """
tsapp_transmit_lin_async = dll.tslin_transmit_lin_async
tsapp_transmit_lin_async.argtypes = [size_t,PLIN]  
tsapp_transmit_lin_async.restype = TS_ReturnType
tsapp_transmit_lin_async.errcheck = check_status_operation

# 同步单帧发送LIN报文
"""
    sync send lin msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        Msg (TLIBLIN): lin msg
        ATimeoutMS (c_int32): timeout in ms

    Returns:
        error code
    example:
        msg = TLIBLIN(FIdentifier = 1,FData=[1,2,3,4,5,6,7,8])
        tsapp_transmit_lin_sync(handle,msg,100)
    """
tsapp_transmit_lin_sync = dll.tslin_transmit_lin_sync
tsapp_transmit_lin_sync.argtypes = [size_t,PLIN,s32]  
tsapp_transmit_lin_sync.restype = TS_ReturnType
tsapp_transmit_lin_sync.errcheck = check_status_operation
# LIN报文接收

# 接收LIN 报文
"""
    receive lin msgs

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ADataBuffers (TLIBLIN): can buffer 
        ADataBufferSize (c_int32): can buffer size
        chn (c_int32): can channel
        ARxTx (c_int8): include tx
    Returns:
        error_code TLIBLIN_buffer TLIBLIN_bufferSize
    example:    
        linbuffer = (TLIBLIN * 100)()
        size = c_int32(100)
        tsapp_receive_lin_msgs(handle, linbuffer, size, 0, 1)
        for i in linbuffer:
            string = ''
            for index in range(i.FActualPayloadLength):
                string += hex(i.FData[index]) + ' '
            
    """
tsfifo_receive_lin_msgs = dll.tsfifo_receive_lin_msgs
tsfifo_receive_lin_msgs.argtypes = [size_t,PLIN,ps32,s32,s32]  
tsfifo_receive_lin_msgs.restype = TS_ReturnType
tsfifo_receive_lin_msgs.errcheck = check_status_operation

# 获取fifo 中lin报文数量
"""
    get lin buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): lin channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_lin_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_lin_buffer_frame_count = dll.tsfifo_read_lin_buffer_frame_count
tsfifo_read_lin_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_lin_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX lin报文数量
"""
    get lin buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): lin channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_lin_tx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_lin_tx_buffer_frame_count = dll.tsfifo_read_lin_tx_buffer_frame_count
tsfifo_read_lin_tx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_lin_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX lin报文数量
"""
    get lin buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): lin channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_lin_rx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_lin_rx_buffer_frame_count = dll.tsfifo_read_lin_rx_buffer_frame_count
tsfifo_read_lin_rx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_lin_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_lin_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 lin fifo
"""
    clear lin receive buffers
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        CHN (CHANNEL_INDEX): lin channel idnex

    Returns:
        error code
        
    example:
        tsfifo_clear_can_receive_buffers(handle,CHANNEL_INDEX.CHN1)
    """
tsfifo_clear_lin_receive_buffers = dll.tsfifo_clear_lin_receive_buffers
tsfifo_clear_lin_receive_buffers.argtypes = [size_t,s32]  
tsfifo_clear_lin_receive_buffers.restype = TS_ReturnType
tsfifo_clear_lin_receive_buffers.errcheck = check_status_operation

# LIN 回调事件
# 注册预发送事件
"""
    register pre tx can event
    Sending a message will trigger and can modify the message data
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_LIN): function

    Returns:
        error code
    example:
        def on_lin(ALIN):
            ALIN.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ALIN.contents.FIdentifier == 1:
                ALIN.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_lin_event = OnTx_RxFUNC_LIN(on_lin)
        tsapp_register_event_lin(Handle,on_lin_event)
    """
tsapp_register_pretx_event_lin = dll.tslin_register_pretx_event_lin
tsapp_register_pretx_event_lin.argtypes = [size_t,OnTx_RxFUNC_LIN]  
tsapp_register_pretx_event_lin.restype = TS_ReturnType
tsapp_register_pretx_event_lin.errcheck = check_status_operation

# 注销预发送事件
"""
    unregister pre tx can event
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_LIN): function

    Returns:
        error code
    example:
        def on_lin(ALIN):
            ALIN.contents.FData[0] = 1 #All message FData[0] will only be 1
            if ALIN.contents.FIdentifier == 1:
                ALIN.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_lin_event = OnTx_RxFUNC_LIN(on_lin)
        tsapp_unregister_event_lin(Handle,on_lin_event)
    """
tsapp_unregister_pretx_event_lin = dll.tslin_unregister_pretx_event_lin
tsapp_unregister_pretx_event_lin.argtypes = [size_t,OnTx_RxFUNC_LIN]  
tsapp_unregister_pretx_event_lin.restype = TS_ReturnType
tsapp_unregister_pretx_event_lin.errcheck = check_status_operation

# 注册rx_tx事件
"""
    register canfd event
    Triggered when there is message transmission on the bus
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_LIN): function

    Returns:
        error code
    example:
        def on_lin(ALIN):
            print(ALIN.contents.FData[0])
            
        on_lin_event = OnTx_RxFUNC_LIN(on_lin)
        tsapp_register_event_lin(Handle,on_lin_event)
    """
tsapp_register_event_lin = dll.tslin_register_event_lin
tsapp_register_event_lin.argtypes = [size_t,OnTx_RxFUNC_LIN]  
tsapp_register_event_lin.restype = TS_ReturnType
tsapp_register_event_lin.errcheck = check_status_operation

# 注销rx_tx事件
"""
    unregister canfd event
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_LIN): function

    Returns:
        error code
    example:
        def on_lin(ALIN):
            print(ALIN.contents.FData[0])
            
        on_lin_event = OnTx_RxFUNC_LIN(on_lin)
        tsapp_unregister_event_lin(Handle,on_lin_event)
"""
tsapp_unregister_event_lin = dll.tslin_unregister_event_lin
tsapp_unregister_event_lin.argtypes = [size_t,OnTx_RxFUNC_LIN]  
tsapp_unregister_event_lin.restype = TS_ReturnType
tsapp_unregister_event_lin.errcheck = check_status_operation

# flexray API

# 启动 flexray 网络
"""
    start flexray network
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ANodeIndex (c_int): flexray channel 
        ATimeoutMs (c_int): timeout in ms
    Returns:
        error code
    example:
        tsflexray_start_net(handle,0,1000)
    """
tsflexray_start_net = dll.tsflexray_start_net
tsflexray_start_net.argtypes = [size_t,s32,s32]  
tsflexray_start_net.restype = TS_ReturnType
tsflexray_start_net.errcheck = check_status_operation

# 停止 flexray 网络
"""
    stop flexray network

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ANodeIndex (c_int): flexray channel 
        ATimeoutMs (c_int): timeout in ms
    Returns:
        error code
    example:
        tsflexray_stop_net(handle,0,1000)
    """
tsflexray_stop_net = dll.tsflexray_stop_net
tsflexray_stop_net.argtypes = [size_t,s32,s32]  
tsflexray_stop_net.restype = TS_ReturnType
tsflexray_stop_net.errcheck = check_status_operation

# # 使能wakeup_pattern
# """
#     stop flexray network

#     Args:
#         AHandle (c_size_t): tsapp_connect retrun handle
#         ANodeIndex (c_int): flexray channel 
#         ATimeoutMs (c_int): timeout in ms
#     Returns:
#         error code
#     example:
#         tsflexray_wakeup_pattern(handle,0,1000)
#     """
# tsflexray_wakeup_pattern = dll.tsflexray_wakeup_pattern
# tsflexray_wakeup_pattern.argtypes = [size_t,s32,s32]  
# tsflexray_wakeup_pattern.restype = TS_ReturnType
# tsflexray_wakeup_pattern.errcheck = check_status_operation


tsflexray_set_controller_frametrigger = dll.tsflexray_set_controller_frametrigger
"""
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ANodeIndex (c_uint): flexray channle 0 or 1                    
        AControllerConfig (TLibFlexray_controller_config): Controller Config from database config
        AFrameLengthArray (bytearray): Frame Array
        AFrameNum (c_int):  Frame len
        AFrameTrigger (TLibTrigger_def): Triggers 
        AFrameTriggerNum (c_int): Triggers len
        ATimeoutMs (c_int): timeout

    Returns:
        error code
        
    example:
        self = TLibFlexray_controller_config(is_open_a=True, is_open_b=True, enable100_b=True, is_show_nullframe=False,
                                        is_Bridging=True)
        fr_trigger = (TLibTrigger_def * 3)()
        '''(1,0,1)'''
        fr_trigger[0].frame_idx = 0
        fr_trigger[0].slot_id = 35
        fr_trigger[0].cycle_code = 1
        fr_trigger[0].config_byte = 0x33
        fr_trigger[0].recv = 0
        '''(3,0,4)'''
        fr_trigger[1].frame_idx = 1
        fr_trigger[1].slot_id = 3
        fr_trigger[1].cycle_code = 4
        fr_trigger[1].config_byte = 0x03
        fr_trigger[1].recv = 0
        '''(3,3,4)'''
        fr_trigger[2].frame_idx = 2
        fr_trigger[2].slot_id = 3
        fr_trigger[2].cycle_code = 7
        fr_trigger[2].config_byte = 0x03
        fr_trigger[2].recv = 0
        FrameLengthArray = (c_int * 3)(32, 32, 32)
        ret = tsflexray_set_controller_frametrigger(handle, chn0, self, FrameLengthArray, 3, fr_trigger, 3, 1000)
    """
tsflexray_set_controller_frametrigger.argtypes = [size_t,s32,PLibFlexray_controller_config,ps32,s32,PLibTrigger_def,s32,s32]  
tsflexray_set_controller_frametrigger.restype = TS_ReturnType
tsflexray_set_controller_frametrigger.errcheck = check_status_operation

# flexray 发送
# 异步单帧发送flexray报文
"""
    async send flexray msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AData (TLIBFlexray): flexray msg

    Returns:
        error code
    example:
        flexray_1 = TLIBFlexray(FSlotId = 35,FChannelMask=1,FCycleNumber=1,FData=[1,2,3,4,5,6,7,8] )
        ret =  tsapp_transmit_flexray_async(handle, flexray_1) 
    """
tsapp_transmit_flexray_async = dll.tsflexray_transmit_async
tsapp_transmit_flexray_async.argtypes = [size_t,PFlexray]  
tsapp_transmit_flexray_async.restype = TS_ReturnType
tsapp_transmit_flexray_async.errcheck = check_status_operation

# 同步单帧发送flexray报文
"""
    async send flexray msg

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AData (TLIBFlexray): flexray msg
        ATimeoutMs (c_int32):timeout
    Returns:
        error code
    example:
        flexray_1 = TLIBFlexray(FSlotId = 35,FChannelMask=1,FCycleNumber=1,FData=[1,2,3,4,5,6,7,8] )
        ret =  tsflexray_transmit_sync(handle, flexray_1,c_int32(100)) 
    """
tsapp_transmit_flexray_sync = dll.tsflexray_transmit_sync
tsapp_transmit_flexray_sync.argtypes = [size_t,PFlexray,s32]  
tsapp_transmit_flexray_sync.restype = TS_ReturnType
tsapp_transmit_flexray_sync.errcheck = check_status_operation

# flexray报文接收
# 接收flexray 报文
"""
    receive flexray msgs

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ADataBuffers (TLIBFlexray): flexray buffer 
        ADataBufferSize (c_int32): flexray buffer size
        chn (c_int32): flexray channel
        ARxTx (c_int8): include tx

    Returns:
        error_code TLIBFlexray_buffer ADataBufferSize
    example:    
        flexray_2 = (TLIBFlexray * 100)()
        size = c_int32(100)
        tsfifo_receive_flexray_msgs(handle, flexray_2, size, 0, 1)
        for i in flexray_2:
            string = ''
            for index in range(i.FActualPayloadLength):
                string += hex(i.FData[index]) + ' '
            print(i.FTimeUs, ' ', i.FSlotId, ' ', i.FCycleNumber, ' ', ('tx' if i.FDir else 'rx'), "  ", string)
    """
tsfifo_receive_flexray_msgs = dll.tsfifo_receive_flexray_msgs
tsfifo_receive_flexray_msgs.argtypes = [size_t,PFlexray,ps32,s32,s32]  
tsfifo_receive_flexray_msgs.restype = TS_ReturnType
tsfifo_receive_flexray_msgs.errcheck = check_status_operation

# 获取fifo 中flexray报文数量
"""
    get flexray buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): flexray channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_flexray_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_flexray_buffer_frame_count = dll.tsfifo_read_flexray_buffer_frame_count
tsfifo_read_flexray_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_flexray_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中TX flexray报文数量
"""
    get flexray buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): flexray channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_flexray_tx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_flexray_tx_buffer_frame_count = dll.tsfifo_read_flexray_tx_buffer_frame_count
tsfifo_read_flexray_tx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_flexray_tx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_tx_buffer_frame_count.errcheck = check_status_operation

# 获取fifo 中RX flexray报文数量
"""
    get flexray buffer frame count

    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        AIdxChn (c_int32): flexray channel 
        ACount (c_int32): get count

    Returns:
        error code
    
    example:
        ACount = c_int32(0)
        tsfifo_read_flexray_rx_buffer_frame_count(AHandle,0,ACount)
        print(ACount)
    """
tsfifo_read_flexray_rx_buffer_frame_count = dll.tsfifo_read_flexray_rx_buffer_frame_count
tsfifo_read_flexray_rx_buffer_frame_count.argtypes = [size_t,s32,ps32]  
tsfifo_read_flexray_rx_buffer_frame_count.restype = TS_ReturnType
tsfifo_read_flexray_rx_buffer_frame_count.errcheck = check_status_operation

# 清空 flexray fifo
"""
    clear lin receive buffers
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        CHN (CHANNEL_INDEX): lin channel idnex

    Returns:
        error code
        
    example:
        tsfifo_clear_can_receive_buffers(handle,CHANNEL_INDEX.CHN1)
    """
tsfifo_clear_flexray_receive_buffers = dll.tsfifo_clear_flexray_receive_buffers
tsfifo_clear_flexray_receive_buffers.argtypes = [size_t,s32]  
tsfifo_clear_flexray_receive_buffers.restype = TS_ReturnType
tsfifo_clear_flexray_receive_buffers.errcheck = check_status_operation

# flexray 回调事件
# 注册预发送事件
"""
    register pre tx can event
    Sending a message will trigger and can modify the message data
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_Flexray): function

    Returns:
        error code
    example:
        def on_flexray(AFlexray):
            AFlexray.contents.FData[0] = 1 #All message FData[0] will only be 1
            if AFlexray.contents.FIdentifier == 1:
                AFlexray.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_flexray_event = OnTx_RxFUNC_Flexray(on_flexray)
        tsapp_register_event_flexray(Handle,on_flexray_event)
    """
tsapp_register_pretx_event_flexray = dll.tsflexray_register_pretx_event_flexray
tsapp_register_pretx_event_flexray.argtypes = [size_t,OnTx_RxFUNC_Flexray]  
tsapp_register_pretx_event_flexray.restype = TS_ReturnType
tsapp_register_pretx_event_flexray.errcheck = check_status_operation

# 注销预发送事件
"""
    unregister pre tx can event
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_Flexray): function

    Returns:
        error code
    example:
        def on_flexray(AFlexray):
            AFlexray.contents.FData[0] = 1 #All message FData[0] will only be 1
            if AFlexray.contents.FIdentifier == 1:
                AFlexray.contents.FData[0] = 2  #only id=1 can message FData[0] will  be 2
            
        on_flexray_event = OnTx_RxFUNC_Flexray(on_flexray)
        tsapp_unregister_pretx_event_flexray(Handle,on_flexray_event)
    """
tsapp_unregister_pretx_event_flexray = dll.tsflexray_unregister_pretx_event_flexray
tsapp_unregister_pretx_event_flexray.argtypes = [size_t,OnTx_RxFUNC_Flexray]  
tsapp_unregister_pretx_event_flexray.restype = TS_ReturnType
tsapp_unregister_pretx_event_flexray.errcheck = check_status_operation

# 注册rx_tx事件
"""
    register canfd event
    Triggered when there is message transmission on the bus
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_Flexray): function

    Returns:
        error code
    example:
        def on_flexray(AFlexray):
            print(AFlexray.contents.FData[0])
            
        on_flexray_event = OnTx_RxFUNC_Flexray(on_flexray)
        tsapp_register_event_flexray(Handle,on_flexray_event)
    """
tsapp_register_event_flexray = dll.tsflexray_register_event_flexray
tsapp_register_event_flexray.argtypes = [size_t,OnTx_RxFUNC_Flexray]  
tsapp_register_event_flexray.restype = TS_ReturnType
tsapp_register_event_flexray.errcheck = check_status_operation

# 注销rx_tx事件
"""
    unregister canfd event
    
    Args:
        AHandle (c_size_t): tsapp_connect retrun handle
        ACallback (OnTx_RxFUNC_Flexray): function

    Returns:
        error code
    example:
        def on_flexray(AFlexray):
            print(AFlexray.contents.FData[0])
            
        on_flexray_event = OnTx_RxFUNC_Flexray(on_flexray)
        tsapp_unregister_event_flexray(Handle,on_flexray_event)
"""
tsapp_unregister_event_flexray = dll.tsflexray_unregister_event_flexray
tsapp_unregister_event_flexray.argtypes = [size_t,OnTx_RxFUNC_Flexray]  
tsapp_unregister_event_flexray.restype = TS_ReturnType
tsapp_unregister_event_flexray.errcheck = check_status_operation


    