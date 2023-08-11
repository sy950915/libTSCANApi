from libTSCANAPI import *

initialize_lib_tscan(True,True,True)

hwHandle = size_t(0)

tsapp_connect(b'',hwHandle)

tsapp_configure_baudrate_canfd(hwHandle,0,500,2000,1,0,1)
# tsapp_configure_baudrate_canfd(hwHandle,1,500,2000,1,0,1)

udsHandle = u8(0)

'''

'''
tsdiag_can_create(hwHandle,udsHandle,0,0,8,0x123,1,0x456,1,0x789,1)

reqData = (u8*3)(0x22,0xf1,0x90)
AResdata = (u8*700)()
AResponseDataSize = s32(700)

tstp_can_request_and_get_response(udsHandle,reqData,3,AResdata,AResponseDataSize)




for i in range(0,AResponseDataSize.value):
    print(AResdata[i],end=" ")
print('')


# print(resData)

tsdiag_can_delete(udsHandle)

tsapp_disconnect_by_handle(hwHandle)

finalize_lib_tscan()