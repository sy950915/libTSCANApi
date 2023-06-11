# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\IDE\libTSCANApi\Demo\libTSCAN_PyDemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_scanDevices = QtWidgets.QPushButton(self.groupBox)
        self.btn_scanDevices.setObjectName("btn_scanDevices")
        self.verticalLayout_6.addWidget(self.btn_scanDevices)
        self.btn_connect = QtWidgets.QPushButton(self.groupBox)
        self.btn_connect.setObjectName("btn_connect")
        self.verticalLayout_6.addWidget(self.btn_connect)
        self.btn_disconnect = QtWidgets.QPushButton(self.groupBox)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.verticalLayout_6.addWidget(self.btn_disconnect)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.cbb_Devices = QtWidgets.QComboBox(self.groupBox)
        self.cbb_Devices.setObjectName("cbb_Devices")
        self.horizontalLayout_5.addWidget(self.cbb_Devices)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.tb_Handle = QtWidgets.QLineEdit(self.groupBox)
        self.tb_Handle.setObjectName("tb_Handle")
        self.horizontalLayout_6.addWidget(self.tb_Handle)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_getInfo = QtWidgets.QPushButton(self.groupBox)
        self.btn_getInfo.setObjectName("btn_getInfo")
        self.horizontalLayout.addWidget(self.btn_getInfo)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.le_AFManufacturer = QtWidgets.QLineEdit(self.groupBox)
        self.le_AFManufacturer.setObjectName("le_AFManufacturer")
        self.verticalLayout_3.addWidget(self.le_AFManufacturer)
        self.le_AFProduct = QtWidgets.QLineEdit(self.groupBox)
        self.le_AFProduct.setObjectName("le_AFProduct")
        self.verticalLayout_3.addWidget(self.le_AFProduct)
        self.le_AFSerial = QtWidgets.QLineEdit(self.groupBox)
        self.le_AFSerial.setObjectName("le_AFSerial")
        self.verticalLayout_3.addWidget(self.le_AFSerial)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_connectFunc = QtWidgets.QPushButton(self.groupBox)
        self.btn_connectFunc.setObjectName("btn_connectFunc")
        self.gridLayout.addWidget(self.btn_connectFunc, 0, 0, 1, 1)
        self.btn_unconnectFunc = QtWidgets.QPushButton(self.groupBox)
        self.btn_unconnectFunc.setObjectName("btn_unconnectFunc")
        self.gridLayout.addWidget(self.btn_unconnectFunc, 0, 1, 1, 1)
        self.btn_disconnectFunc = QtWidgets.QPushButton(self.groupBox)
        self.btn_disconnectFunc.setObjectName("btn_disconnectFunc")
        self.gridLayout.addWidget(self.btn_disconnectFunc, 1, 0, 1, 1)
        self.btn_undisconnectFunc = QtWidgets.QPushButton(self.groupBox)
        self.btn_undisconnectFunc.setObjectName("btn_undisconnectFunc")
        self.gridLayout.addWidget(self.btn_undisconnectFunc, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_enableBusMsg = QtWidgets.QPushButton(self.groupBox)
        self.btn_enableBusMsg.setObjectName("btn_enableBusMsg")
        self.verticalLayout_4.addWidget(self.btn_enableBusMsg)
        self.btn_getBusMsg = QtWidgets.QPushButton(self.groupBox)
        self.btn_getBusMsg.setObjectName("btn_getBusMsg")
        self.verticalLayout_4.addWidget(self.btn_getBusMsg)
        self.btn_ClearBusMsg = QtWidgets.QPushButton(self.groupBox)
        self.btn_ClearBusMsg.setObjectName("btn_ClearBusMsg")
        self.verticalLayout_4.addWidget(self.btn_ClearBusMsg)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbb_BusMsgType = QtWidgets.QComboBox(self.groupBox)
        self.cbb_BusMsgType.setObjectName("cbb_BusMsgType")
        self.horizontalLayout_2.addWidget(self.cbb_BusMsgType)
        self.lb_BusMsg = QtWidgets.QLabel(self.groupBox)
        self.lb_BusMsg.setMaximumSize(QtCore.QSize(20, 16777215))
        self.lb_BusMsg.setObjectName("lb_BusMsg")
        self.horizontalLayout_2.addWidget(self.lb_BusMsg)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tv_MsgData = QtWidgets.QTableView(self.groupBox_2)
        self.tv_MsgData.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tv_MsgData.setAcceptDrops(False)
        self.tv_MsgData.setObjectName("tv_MsgData")
        self.verticalLayout_2.addWidget(self.tv_MsgData)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "主功能区"))
        self.label.setText(_translate("MainWindow", "扫描设备"))
        self.label_2.setText(_translate("MainWindow", "连接设备"))
        self.label_3.setText(_translate("MainWindow", "断开设备"))
        self.btn_scanDevices.setText(_translate("MainWindow", "扫描设备"))
        self.btn_connect.setText(_translate("MainWindow", "连接设备"))
        self.btn_disconnect.setText(_translate("MainWindow", "断开设备"))
        self.label_6.setText(_translate("MainWindow", "设备列表"))
        self.label_4.setText(_translate("MainWindow", "设备句柄"))
        self.btn_getInfo.setText(_translate("MainWindow", "获取设备信息"))
        self.btn_connectFunc.setText(_translate("MainWindow", "注册连接成功回调函数"))
        self.btn_unconnectFunc.setText(_translate("MainWindow", "注销连接成功回调函数"))
        self.btn_disconnectFunc.setText(_translate("MainWindow", "注册断开连接成功回调函数"))
        self.btn_undisconnectFunc.setText(_translate("MainWindow", "注销断开连接成功回调函数"))
        self.btn_enableBusMsg.setText(_translate("MainWindow", "启动总线信息统计"))
        self.btn_getBusMsg.setText(_translate("MainWindow", "读取统计信息"))
        self.btn_ClearBusMsg.setText(_translate("MainWindow", "清除统计信息"))
        self.lb_BusMsg.setText(_translate("MainWindow", "0%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "设备管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "CAN API"))
        self.groupBox_2.setTitle(_translate("MainWindow", "报文信息"))
