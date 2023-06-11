from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Ui_libTSCAN_PyDemo import Ui_MainWindow
from libTSCANAPI import *

class MyWindows(QMainWindow, Ui_MainWindow):
    itmes = ["CAN总线负载率", "CAN总线峰值负载率", "标准数据帧帧率", "所有标准数据帧个数", "扩展数据帧帧率", "所有扩展数据帧个数", "标准远程帧帧率", "所有标准远程帧个数","扩展远程帧帧率", "所有扩展远程帧个数", "错误帧帧率", "所有错误帧个数"]
    HwHandle = size_t(0)
    Is_Connect = False
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)
        self.cbb_BusMsgType.addItems(self.itmes)
        self.initUI()

    def initUI(self):
        def scanDevices():
            ADevCount = s32(0)
            tscan_scan_devices(ADevCount)
            for i in range(ADevCount.value):
                self.cbb_Devices.addItem(str(i)) 
        self.btn_scanDevices.clicked.connect(scanDevices)  # 开始扫描设备数量

        def connect_device():
            if self.cbb_Devices.currentIndex() == -1: return 	# 如果没有选择设备，则不执行操作
            AFManufacturer = b''
            AFProduct = b''
            AFSerial = b''
            tscan_get_device_info(self.cbb_Devices.currentIndex(),AFManufacturer,AFProduct,AFSerial)  # 获取设备信息(选择要连接的设备   0)
            ret = tsapp_connect(AFSerial,self.HwHandle)  # 连接设备(选择要连接的设备   0)
            if ret == 0 or ret == 5:
                self.Is_Connect = True  # 连接设备成功后，显示连接状态   1)开始计时
                self.tb_Handle.setText(str(self.HwHandle))  # 显示设备号码(选择要连接的设备   0)
        self.btn_connect.clicked.connect(connect_device)  # Connect button clicked. 创建TCP连接函数, 并连接

        def disconnect_device():
            if self.Is_Connect: 
                tsapp_disconnect_by_handle(self.HwHandle)  # Disconnect device. (选择要连接的设
        self.btn_disconnect.clicked.connect(disconnect_device)  # Disconnect button clicked. 断开连接函数    

        def get_Devices_Info():
            AFManufacturer = c_char_p()
            AFProduct = c_char_p()
            AFSerial = c_char_p()
            tscan_get_device_info(self.cbb_Devices.currentIndex(),AFManufacturer,AFProduct,AFSerial)
            self.le_AFManufacturer.setText(str(AFManufacturer.value))  # Display device serial number. 获取设备名称   1
            self.le_AFProduct.setText(str(AFProduct.value))  # Display device manufacturer. 获取设备品牌   2
            self.le_AFSerial.setText(str(AFSerial.value))  # Display device serial number. 获取设备 serial number   3
        self.btn_getInfo.clicked.connect(get_Devices_Info)  # Get device info. 获取设备信息函数  
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序

    window = MyWindows()

    window.show()

    sys.exit(app.exec_())  # 程序执行循环
