'''
Author: seven 865762826@qq.com
Date: 2023-07-20 20:17:42
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-29 21:56:11
FilePath: /libTSCANApi/Demo/tosun_test(1).py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 多进程 test
# from ecu_simulator.sdk.driver.tosun.libTSCANAPI import *
# from ecu_simulator.sdk.driver.tosun import libTSCANAPI
from multiprocessing import Process
from threading import Thread
from time import sleep


def test_func1():
    from libTSCANAPI.TSCommon import (
        initialize_lib_tscan,
        tsapp_connect,
        size_t,
        finalize_lib_tscan,
    )

    ADeviceHandle1 = size_t(0)
    can = b"609C84C2E4BAF720"
    initialize_lib_tscan(True, True, False)  # 函数初始化
    print("fun1 start")
    tsapp_connect(can, ADeviceHandle1)
    print("fun1 end")
    sleep(2)
    finalize_lib_tscan()
    sleep(3)


def test_func2():
    from libTSCANAPI import (
        initialize_lib_tscan,
        tsapp_connect,
        size_t,
        finalize_lib_tscan,
    )

    print("start connect")
    ADeviceHandle2 = size_t(0)
    fr = b"6416653F83D1"
    initialize_lib_tscan(True, True, False)  # 函数初始化
    print("33333333333333333333333333333333333333333")
    sleep(3)
    tsapp_connect(fr, ADeviceHandle2)
    print("end connect")

    # print("5555555555555555555555555555555555")
    # finalize_lib_tscan()
    # print("666666666666666666666666666666666666666666666")
    print("start disconnect")
    finalize_lib_tscan()
    print("end disconnect")
    sleep(3)

if __name__ == "__main__":

    thread1 = Thread(target=test_func1, name="can", daemon=True)
    process2 = Process(target=test_func2, name="fr", daemon=True)
    thread1.start()
    process2.start()  

    sleep(10)

    process3 = Process(target=test_func2, name="fr3", daemon=True)
    process3.start()
    print("999999999999999999999999999999999999999999999999999999")

    sleep(10)
