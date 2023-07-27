'''
Author: seven 865762826@qq.com
Date: 2023-07-03 11:00:13
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-27 05:20:43
FilePath: \TSMasterAPId:\Chat\QChat\WXWork\1688855494347287\Cache\File\2023-06\canDemo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from libTSCANAPI import *
import time

count = 0
def on_can_event(obj,ACANFD):
        if (ACANFD.contents.FProperties&1)==1:
            print('tx')
        else:
            print('rx')

ONCAN = OnTx_RxFUNC_CANFD_WHandle(on_can_event)

while True:
    count +=1
    print(f"--------- {count}--------------")
    initialize_lib_tscan(True,True,False)
    ACount = s32(0)
    tscan_scan_devices(ACount)

    for i in range(ACount.value):
        AFManufacturer=c_char_p()
        AFProduct=c_char_p()
        AFSerial=c_char_p()
        tscan_get_device_info(i,AFManufacturer,AFProduct,AFSerial)
        print(AFSerial.value)


    hwHandle = size_t(0)
    ret = tsapp_connect(b"",hwHandle)
    if 0!=ret and 5!=ret:
        print("connect error code = ",ret)
        time.sleep(1)
        break

    tsapp_register_event_canfd_whandle(hwHandle,ONCAN)

    # 波特率配置
    """
    0:  通道
    500: 仲裁段波特率
    2000: 数据段波特率
    最后一个参数为 是否激活终端电阻
    """



    tsapp_configure_baudrate_canfd(hwHandle,0,500,2000,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,True)

    tsapp_configure_baudrate_canfd(hwHandle,1,500,2000,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,True)

    ACAN = TLIBCANFD(0,8,0X1,1,0,[1,2,3,4,5,6,7,8])

    tsapp_transmit_canfd_async(hwHandle,ACAN)

    time.sleep(2)

    TCANBuffer = (TLIBCANFD*100)()
    BufferSize = s32(100)  #buffersize 就是TLINBuffer的长度

    tsfifo_receive_canfd_msgs(hwHandle,TCANBuffer,BufferSize,0,READ_TX_RX_DEF.ONLY_RX_MESSAGES) 

    tsapp_disconnect_by_handle(hwHandle)

    finalize_lib_tscan()

    time.sleep(5)

