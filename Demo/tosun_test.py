'''
Author: seven 865762826@qq.com
Date: 2023-07-05 22:41:32
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-05 23:55:12
FilePath: /libTSCANApi/Demo/tosun_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from multiprocessing import Process
from time import sleep
import vthread

# @vthread.pool(2)
def test_func1():
    from libTSCANAPI import initialize_lib_tscan,tsapp_connect,size_t
    ADeviceHandle1 = size_t(0)
    can = b"6524670985BE"
    initialize_lib_tscan(True, True, False)  # 函数初始化
    print("11111111111111111111111111111111111")
    tsapp_connect(can, ADeviceHandle1)
    print("222222222222222222222222222222222222222")
    sleep(5)
    # libTSCANAPI.finalize_lib_tscan()
    


# @vthread.pool(2)
def test_func2():
    from libTSCANAPI import initialize_lib_tscan,tsapp_connect,size_t
    ADeviceHandle1 = size_t(0)
    can = b"E7CB383B263B8955"
    initialize_lib_tscan(True, True, False)  # 函数初始化
    print("3333333333333333333333333333333333333333")
    tsapp_connect(can, ADeviceHandle1)
    print("4444444444444444444444444444444444444444")
    sleep(5)
    # libTSCANAPI.finalize_lib_tscan()


if __name__ == "__main__":
    # worke dir: ecu_simulator/

    # ADeviceHandle1 = size_t(0)
    # initialize_lib_tscan(True, True, False)  # 函数初始化
    

    process1 = Process(target=test_func1)
    process2 = Process(target=test_func2)
    process1.start()
    process2.start()
    # test_func1()
    # test_func2()

    sleep(20)

