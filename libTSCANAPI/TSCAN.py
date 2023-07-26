'''
Author: seven 865762826@qq.com
Date: 2023-07-26 14:25:45
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-26 16:40:19
FilePath: \libTSCANApi\libTSCANAPI\TSCAN.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from .TSStructure import *  
from .TSEnumdefine import * 
from .TSDirver import _os,dll,_curr_path,_arch,ascdll
import TSCommon
from ctypes import *

Is_initialize = False
def initialize_lib_tscan(AEnableFIFO: c_bool, AEnableError: c_bool,AUseHWTime:c_bool)->None:
    global Is_initialize
    Is_initialize = True
    TSCommon.initialize_lib_tscan(AEnableFIFO,AEnableError,AUseHWTime)

def finalize_lib_tscan()->None:
    global Is_initialize
    if Is_initialize:
        Is_initialize = False
        TSCommon.finalize_lib_tscan()

def tscan_register_event_connected(ACallBack:On_Connect_FUNC)->int:
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_register_event_connected(ACallBack)

def tscan_register_event_disconnected(ACallBack:On_disConnect_FUNC)->int:
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_register_event_disconnected(ACallBack)

def tscan_unregister_event_connected(ACallBack:On_Connect_FUNC)->int:
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_unregister_event_connected(ACallBack)

def tscan_unregister_event_disconnected(ACallBack:On_disConnect_FUNC)->int:
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_unregister_event_disconnected(ACallBack)

def tsapp_connect(ADeviceSerial:c_char_p,HWHandle:c_size_t):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_connect(ADeviceSerial,HWHandle)

def tsapp_disconnect_by_handle(HWHandle:c_size_t):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_disconnect_by_handle(HWHandle)

def tsapp_disconnect_all():
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_disconnect_all()

def tsapp_configure_baudrate_can(HWHandle: c_size_t, AChnIdx: TSCommon.CHANNEL_INDEX, ARateKbps: c_double,A120: TSCommon.A120):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_configure_baudrate_can(HWHandle,AChnIdx,ARateKbps,A120)

def tsapp_configure_baudrate_canfd(HWHandle: c_size_t, AChnIdx: CHANNEL_INDEX, ARateKbps: c_double,
ADataKbps: c_double,AControllerType: TLIBCANFDControllerType, AControllerMode: TLIBCANFDControllerMode,A120: A120):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_configure_baudrtsapp_configure_baudrate_canfdate_can(HWHandle,AChnIdx,ARateKbps,ADataKbps,AControllerType,AControllerMode,A120)

def tsapp_configure_baudrate_lin(HWHandle: c_size_t, AChnIdx: CHANNEL_INDEX, ARateKbps: c_double,LINPROTOCOL:LIN_PROTOCOL):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_configure_baudrate_lin(HWHandle,AChnIdx,ARateKbps,LINPROTOCOL)

def tslin_set_node_funtiontype(HWHandle: c_size_t, AChnIdx: CHANNEL_INDEX, AFunctionType: T_LIN_NODE_FUNCTION):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tslin_set_node_funtiontype(HWHandle,AChnIdx,AFunctionType)

def tscan_scan_devices(ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_scan_devices(ACount)

def tscan_get_device_info(ACountidx:s32,AFManufacturer:c_char_p,AFProduct:c_char_p,AFSerial:c_char_p):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tscan_get_device_info(ACountidx,AFManufacturer,AFProduct,AFSerial)

def tscan_unregister_pretx_events_all(HWHandle: c_size_t):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_unregister_pretx_events_all(HWHandle)

def tscan_set_auto_calc_bus_statistics(AEnable:c_bool):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_set_auto_calc_bus_statistics(AEnable)

def tscan_get_bus_status(HWHandle: c_size_t, AChnidx:s32,AIndex:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tscan_get_bus_status(HWHandle,AChnidx,AIndex)

def tscan_clear_can_bus_statistic():
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tscan_clear_can_bus_statistic()

def tsapp_transmit_can_async(HWHandle: c_size_t,Msg:PCAN or TLIBCAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_can_async(HWHandle,Msg)

def tsapp_transmit_can_sync(HWHandle: c_size_t,Msg:PCAN or TLIBCAN,ATimeout:u32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_can_sync(HWHandle,Msg,ATimeout)

def tsapp_add_cyclic_msg_can(HWHandle: c_size_t,Msg:PCAN or TLIBCAN,ATimeout:c_float):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_add_cyclic_msg_can(HWHandle,Msg,ATimeout)

def tsapp_delete_cyclic_msg_can(HWHandle: c_size_t,Msg:PCAN or TLIBCAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_delete_cyclic_msg_can(HWHandle,Msg)

def tsapp_transmit_canfd_async(HWHandle: c_size_t,Msg:PCANFD or TLIBCANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_canfd_async(HWHandle,Msg)

def tsapp_transmit_canfd_sync(HWHandle: c_size_t,Msg:PCANFD or TLIBCANFD,ATimeout:u32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_canfd_sync(HWHandle,Msg,ATimeout)

def tsapp_add_cyclic_msg_canfd(HWHandle: c_size_t,Msg:PCANFD or TLIBCANFD,ATimeout:c_float):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_add_cyclic_msg_canfd(HWHandle,Msg,ATimeout)

def tsapp_delete_cyclic_msg_canfd(HWHandle: c_size_t,Msg:PCANFD or TLIBCANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_delete_cyclic_msg_canfd(HWHandle,Msg)

def tsfifo_receive_can_msgs(HWHandle: c_size_t,Msgs:PCAN,MsgsCount:ps32,Chnidx:s32,IncludeTX: READ_TX_RX_DEF
):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_receive_can_msgs(HWHandle,Msgs,MsgsCount,Chnidx,IncludeTX)

def tsfifo_clear_can_receive_buffers(HWHandle:size_t,Chnidx:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_clear_can_receive_buffers(HWHandle,Chnidx)

def tsfifo_read_can_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_can_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_can_tx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_can_tx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_can_rx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_can_rx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsapp_register_pretx_event_can(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_can(HWHandle,ACallBack)

def tsapp_register_pretx_event_can_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_can_whandle(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_can(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_can(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_can_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_can_whandle(HWHandle,ACallBack)

def tsapp_register_event_can(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_can(HWHandle,ACallBack)

def tsapp_register_event_can_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_can_whandle(HWHandle,ACallBack)

def tsapp_unregister_event_can(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_can(HWHandle,ACallBack)

def tsapp_unregister_event_can_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CAN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_can_whandle(HWHandle,ACallBack)

def tsfifo_receive_canfd_msgs(HWHandle: c_size_t,Msgs:PCANFD,MsgsCount:ps32,Chnidx:s32,IncludeTX: READ_TX_RX_DEF
):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_receive_canfd_msgs(HWHandle,Msgs,MsgsCount,Chnidx,IncludeTX)

def tsfifo_clear_canfd_receive_buffers(HWHandle:size_t,Chnidx:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_clear_canfd_receive_buffers(HWHandle,Chnidx)

def tsfifo_read_canfd_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_canfd_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_canfd_tx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_canfd_tx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_canfd_rx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_canfd_rx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsapp_register_pretx_event_canfd(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_canfd(HWHandle,ACallBack)

def tsapp_register_pretx_event_canfd_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_canfd_whandle(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_canfd(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_canfd(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_canfd_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_canfd_whandle(HWHandle,ACallBack)

def tsapp_register_event_canfd(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_canfd(HWHandle,ACallBack)

def tsapp_register_event_canfd_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_canfd_whandle(HWHandle,ACallBack)

def tsapp_unregister_event_canfd(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_canfd(HWHandle,ACallBack)

def tsapp_unregister_event_canfd_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_CANFD_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_canfd_whandle(HWHandle,ACallBack)

def tsapp_transmit_lin_async(HWHandle: c_size_t,Msg:PLIN or TLIBLIN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_lin_async(HWHandle,Msg)

def tsapp_transmit_lin_sync(HWHandle: c_size_t,Msg:PLIN or TLIBLIN,ATimeout:u32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_lin_sync(HWHandle,Msg,ATimeout)


def tsfifo_receive_lin_msgs(HWHandle: c_size_t,Msgs:PLIN,MsgsCount:ps32,Chnidx:s32,IncludeTX: READ_TX_RX_DEF
):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_receive_lin_msgs(HWHandle,Msgs,MsgsCount,Chnidx,IncludeTX)

def tsfifo_clear_lin_receive_buffers(HWHandle:size_t,Chnidx:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_clear_lin_receive_buffers(HWHandle,Chnidx)

def tsfifo_read_lin_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_lin_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_lin_tx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_lin_tx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_lin_rx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_lin_rx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsapp_register_pretx_event_lin(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_lin(HWHandle,ACallBack)

def tsapp_register_pretx_event_lin_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_lin_whandle(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_lin(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_lin(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_lin_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_lin_whandle(HWHandle,ACallBack)

def tsapp_register_event_lin(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_lin(HWHandle,ACallBack)

def tsapp_register_event_lin_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_lin_whandle(HWHandle,ACallBack)

def tsapp_unregister_event_lin(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_lin(HWHandle,ACallBack)

def tsapp_unregister_event_lin_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_LIN_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_lin_whandle(HWHandle,ACallBack)


def tsapp_transmit_flexray_async(HWHandle: c_size_t,Msg:PFlexray or TLIBFlexray):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_flexray_async(HWHandle,Msg)

def tsapp_transmit_flexray_sync(HWHandle: c_size_t,Msg:PFlexray or TLIBFlexray,ATimeout:u32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return 	TSCommon.tsapp_transmit_flexray_sync(HWHandle,Msg,ATimeout)


def tsfifo_receive_flexray_msgs(HWHandle: c_size_t,Msgs:PFlexray,MsgsCount:ps32,Chnidx:s32,IncludeTX: READ_TX_RX_DEF
):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_receive_flexray_msgs(HWHandle,Msgs,MsgsCount,Chnidx,IncludeTX)

def tsfifo_clear_flexray_receive_buffers(HWHandle:size_t,Chnidx:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_clear_flexray_receive_buffers(HWHandle,Chnidx)

def tsfifo_read_flexray_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_flexray_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_flexray_tx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_flexray_tx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsfifo_read_flexray_rx_buffer_frame_count(HWHandle:size_t,Chnidx:s32,ACount:s32):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_read_flexray_rx_buffer_frame_count(HWHandle,Chnidx,ACount)

def tsapp_register_pretx_event_flexray(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_flexray(HWHandle,ACallBack)

def tsapp_register_pretx_event_flexray_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_pretx_event_flexray_whandle(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_flexray(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_flexray(HWHandle,ACallBack)

def tsapp_unregister_pretx_event_flexray_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_unregister_pretx_event_flexray_whandle(HWHandle,ACallBack)

def tsapp_register_event_flexray(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_flexray(HWHandle,ACallBack)

def tsapp_register_event_flexray_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_flexray_whandle(HWHandle,ACallBack)

def tsapp_unregister_event_flexray(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_flexray(HWHandle,ACallBack)

def tsapp_unregister_event_flexray_whandle(HWHandle:size_t,ACallBack:OnTx_RxFUNC_Flexray_WHandle):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsapp_register_event_flexray_whandle(HWHandle,ACallBack)




def tsfifo_add_flexray_pass_filter(HWHandle:size_t,AChnidx:s32,FSlotID:u16,FBaseCycle:u8,RepCycle:u8):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_add_flexray_pass_filter(HWHandle,AChnidx,FSlotID,FBaseCycle,RepCycle)

def tsfifo_delete_flexray_pass_filter(HWHandle:size_t,AChnidx:s32,FSlotID:u16,FBaseCycle:u8,RepCycle:u8):
    global Is_initialize
    if not Is_initialize:
        return 97
    return TSCommon.tsfifo_delete_flexray_pass_filter(HWHandle,AChnidx,FSlotID,FBaseCycle,RepCycle)

if 'windows' in _os.lower():
    def tsfifo_add_can_canfd_pass_filter(HWHandle:size_t,AChnidx:s32,FID:s32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsfifo_add_can_canfd_pass_filter(HWHandle,AChnidx,FID)

    def tsfifo_delete_can_canfd_pass_filter(HWHandle:size_t,AChnidx:s32,FID:s32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsfifo_delete_can_canfd_pass_filter(HWHandle,AChnidx,FID)

    def tsfifo_add_lin_pass_filter(HWHandle:size_t,AChnidx:s32,FID:u8):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsfifo_add_lin_pass_filter(HWHandle,AChnidx,FID)

    def tsfifo_delete_lin_pass_filter(HWHandle:size_t,AChnidx:s32,FID:u8):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsfifo_delete_lin_pass_filter(HWHandle,AChnidx,FID)
    
    def tsapp_configure_can_regs(HWHandle: c_size_t, AIdxChn: CHANNEL_INDEX, ABaudrateKbps: float, ASEG1: int,ASEG2: int, APrescaler: int,ASJ2: int, AOnlyListen: c_uint32, A120: A120):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsapp_configure_can_regs(HWHandle,AIdxChn,ABaudrateKbps,ASEG1,ASEG2,APrescaler,ASJ2,AOnlyListen,A120)
    
    def tsapp_configure_canfd_regs(HWHandle: c_size_t, AIdxChn: CHANNEL_INDEX, AArbBaudrateKbps: c_float, AArbSEG1: int,AArbSEG2: int,AArbPrescaler: int,AArbSJ2: int, ADataBaudrateKbps: c_float, ADataSEG1: int, ADataSEG2: int,ADataPrescaler: int,ADataSJ2: int, AControllerType: TLIBCANFDControllerType,AControllerMode: TLIBCANFDControllerMode,AInstallTermResistor120Ohm: A120):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsapp_configure_canfd_regs(HWHandle,AIdxChn,AArbBaudrateKbps,AArbSEG1,AArbSEG2,AArbPrescaler,AArbSJ2,ADataBaudrateKbps,ADataSEG1,ADataSEG2,ADataPrescaler,ADataSJ2,AControllerType,AControllerMode,AInstallTermResistor120Ohm)
    
    def tsdiag_can_create(HwHandle:size_t,pDiagModuleIndex: u8, AChnIndex: CHANNEL_INDEX, ASupportFDCAN: u8,AMaxDLC: u8,ARequestID: c_uint32, ARequestIDIsStd: bool, AResponseID: c_uint32, AResponseIDIsStd: bool,AFunctionID: c_uint32, AFunctionIDIsStd: bool):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_create(HwHandle,pDiagModuleIndex,AChnIndex,ASupportFDCAN,AMaxDLC,ARequestID,ARequestIDIsStd,AResponseID,AResponseIDIsStd,AFunctionID,AFunctionIDIsStd)
    
    def tsdiag_can_delete(pDiagModuleIndex: u8):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_delete(pDiagModuleIndex)
    
    def tsdiag_can_delete_all():
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_delete_all()
    
    def tstp_can_send_functional(pDiagModuleIndex: u8,data:pu8,datalen:s32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tstp_can_send_functional(pDiagModuleIndex,data,datalen)
    
    def tstp_can_send_request(pDiagModuleIndex: u8,data:pu8,datalen:s32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tstp_can_send_request(pDiagModuleIndex,data,datalen)
    
    def tstp_can_setstp_can_request_and_get_responsend_request(pDiagModuleIndex: u8,data:pu8,datalen:s32,resData:pu8,resDataLen:s32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tstp_can_request_and_get_response(pDiagModuleIndex,data,datalen,resData,resDataLen)
    
    def tsdiag_can_session_control(pDiagModuleIndex: u8,SubID:u8):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_session_control(pDiagModuleIndex,SubID)
    
    def tsdiag_can_routine_control(pDiagModuleIndex: c_int32,AARoutineControlType:c_uint8,ARoutintID:c_uint16):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_routine_control(pDiagModuleIndex,AARoutineControlType,ARoutintID)
    
    def tsdiag_can_communication_control(pDiagModuleIndex: u8,SubID:u8):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_communication_control(pDiagModuleIndex,SubID)
    
    def tsdiag_can_security_access_request_seed(pDiagModuleIndex: c_int32,ALevel:c_int32,ASeed:c_char_p,ASeedSize:c_int32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_security_access_request_seed(pDiagModuleIndex,ALevel,ASeed,ASeedSize)


    def tsdiag_can_security_access_send_key(pDiagModuleIndex: c_int32,ALevel:c_int32,AKey:c_char_p,AKeySize:c_int32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return tsdiag_can_security_access_send_key(pDiagModuleIndex,ALevel,AKey,AKeySize)
    
    def tsdiag_can_request_download(pDiagModuleIndex: c_int32,AMemAddr:c_uint32,AMemSize:c_uint32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_request_download(pDiagModuleIndex,AMemAddr,AMemSize)
    
    def tsdiag_can_request_upload(pDiagModuleIndex: c_int32,AMemAddr:c_uint32,AMemSize:c_uint32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_request_upload(pDiagModuleIndex,AMemAddr,AMemSize)
    
    
    def tsdiag_can_transfer_data(pDiagModuleIndex: c_int32,ASourceDatas:c_char_p,ASize:c_int32,AReqCase:c_int32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_transfer_data(pDiagModuleIndex,ASourceDatas,ASize,AReqCase)
    
    def tsdiag_can_request_transfer_exit(pDiagModuleIndex:c_int32):
        global Is_initialize
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_request_transfer_exit(pDiagModuleIndex)
    
    def tsdiag_can_write_data_by_identifier(pDiagModuleIndex: c_int32,ADataIdentifier:c_uint16,AWriteData:c_char_p,AWriteDataSize:c_int32):
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_write_data_by_identifier(pDiagModuleIndex,ADataIdentifier,AWriteData,AWriteDataSize)
    
    def tsdiag_can_read_data_by_identifier(pDiagModuleIndex: c_int32,ADataIdentifier:c_uint16,AReturnArray:c_char_p,AReturnArraySize:c_int32):
        if not Is_initialize:
            return 97
        return TSCommon.tsdiag_can_read_data_by_identifier(pDiagModuleIndex,ADataIdentifier,AReturnArray,AReturnArraySize)
else:
    def tslog_write_start(fileName:c_char_p,logHandle:c_void_p):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_start(fileName,logHandle)
    
    def tslog_write_end(logHandle:c_void_p):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_end(logHandle) 
    
    def tslog_write_flexray(logHandle:c_void_p,Msg:PFlexray or TLIBFlexray):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_flexray(logHandle,Msg) 
    
    def tslog_write_can(logHandle:c_void_p,Msg:PCAN or TLIBCAN):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_can(logHandle,Msg) 
    
    def tslog_write_canfd(logHandle:c_void_p,Msg:PCANFD or TLIBCANFD):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_canfd(logHandle,Msg) 
    
    def tslog_write_lin(logHandle:c_void_p,Msg:PLIN or TLIBLIN):
        if not Is_initialize:
            return 97
        return TSCommon.tslog_write_lin(logHandle,Msg) 