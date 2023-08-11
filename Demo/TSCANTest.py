'''
Author: seven 865762826@qq.com
Date: 2023-08-08 17:24:46
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-08-10 16:48:57
FilePath: \libTSCANApi\Demo\TSCANTest.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from libTSCANAPI import *
import threading


class TSCANTest(threading.Thread):
    
    def __init__(self,chnidx,HwHandle):
        threading.Thread.__init__(self,daemon=True)
        self.HwHandle = HwHandle
        # initialize_lib_tscan(True,True,False)
        # tsapp_connect("",self.HwHandle)
        self.chnidx = chnidx
        self.onpretx = OnTx_RxFUNC_CANFD_WHandle(self.pre_txcan)
        self.quit_thread = True
        # initialize_lib_tscan(True,True,False)
        # tsapp_connect(b"",self.HwHandle)
        print("=========================1============================")
        tsapp_register_event_canfd_whandle(self.HwHandle,self.onpretx)
        print("=========================2============================")
        tsapp_configure_baudrate_canfd(self.HwHandle,self.chnidx,500,2000,1,0,True)
    def pre_txcan(self,obj,msg):
        return
    
    def run(self):
        
        for i in range(100):
            msg = TLIBCANFD(self.chnidx,15,i,1,3,[1,2,3,4,5,6,7])
            # tsapp_transmit_canfd_async(self.HwHandle,msg)
            print(1111111111111111111111111111111111111111111)
            tsapp_add_cyclic_msg_canfd(self.HwHandle,msg,100)
            print(2222222222222222222222222222222222222222222)
            del msg
        # while self.quit_thread:
        #     time.sleep(1)
    def stop_thread(self):
        self.quit_thread = False
    
if __name__ == "__main__":
    HwHandle = size_t(0)
    initialize_lib_tscan(True,True,False)
    for i in range(10):
        tsapp_connect(b"",HwHandle)
        for i in range(12):
            print(f"-----------------{i}---------------------------")
            TSCANMsg = TSCANTest(i,HwHandle)
            TSCANMsg.start() 
            time.sleep(1)
        tsapp_disconnect_by_handle(HwHandle)
        time.sleep(3)
    while True:
        time.sleep(0.1)
# from TSMasterAPI import *
# import threading

# def pre_txcan(obj,msg):
#         return

# class TSCANTest(threading.Thread):
    
#     def __init__(self,chnidx,HwHandle = 0):
#         threading.Thread.__init__(self,daemon=True)
#         self.HwHandle = HwHandle
#         self.obj = s32(0) 
#         # initialize_lib_tscan(True,True,False)
#         # tsapp_connect("",self.HwHandle)
#         self.chnidx = chnidx
#         self.onpretx = OnTx_RxFUNC_CANFD(pre_txcan)
#         self.quit_thread = True
#         # initialize_lib_tscan(True,True,False)
#         # tsapp_connect(b"",self.HwHandle)
#         print("=========================1============================")
#         tsapp_register_event_canfd(self.obj,self.onpretx)
#         print("=========================2============================")
#         # tsapp_configure_baudrate_canfd(self.chnidx,500,2000,1,0,True)

    
#     def run(self):
#         for i in range(100):
#             msg = TLIBCANFD(self.chnidx,8,i,1,3,[1,2,3,4,5,6,7])
#             print("1111111111111111111111111111111111111111\n")
#             tsapp_add_cyclic_msg_canfd(msg,100)
#             print("2222222222222222222222222222222222222222\n")
#             del msg
#         while self.quit_thread:
#             time.sleep(1)
#     def stop_thread(self):
#         self.quit_thread = False
    
# if __name__ == "__main__":
    
#     initialize_lib_tsmaster(b"TSMaster")
#     tsapp_connect()
#     for i in range(12):
#         print(f"-----------------{i}---------------------------")
#         TSCANMsg = TSCANTest(i)
#         TSCANMsg.start() 
#         time.sleep(2)
#     while True:
#         key = input("input q to quit\n")
#         if key == "q":
#             break

