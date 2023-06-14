'''
Author: seven 865762826@qq.com
Date: 2023-06-12 09:57:16
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-14 17:27:16
FilePath: \libTSCANApi\Demo\libTSCANAPI_Demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Ui_libTSCAN_PyDemo import Ui_MainWindow
from libTSCANAPI import *




class ViewType:
    CallBackType = 0
    FifoType = 1


def str2List(strData):
    strData = strData.replace('  ', ' ')
    strData = strData.split(' ')
    DataList = [(int(x,16)&0xff) for x in strData if x.isdigit()]
    return DataList


class MyWindows(QMainWindow, Ui_MainWindow):
    # itmes = ["CAN总线负载率", "CAN总线峰值负载率", "", "", "", "", "", "","", "", "", ""]
    try:
        HwHandle = size_t(0)
        Is_Connect = False
        Is_enable_bus = False
        __ShowMsgCount = 100
        def __init__(self):
            super(MyWindows, self).__init__()
            self.setupUi(self)
            # self.cbb_BusMsgType.addItems(self.itmes)
            self.initUI()

        def tvAddRaw(self,Msg):
            Times = str(float(Msg.FTimeUs)/1000000.0)
            CHN = str(Msg.FIdxChn)
            if isinstance(Msg,TLIBLIN):
                ID = f"0x{Msg.FIdentifier:02x}"
            elif (Msg.FProperties >> 2 & 1) == 1:
                ID = f"0x{Msg.FIdentifier:08x}x"
            else:
                ID = f"0x{Msg.FIdentifier:03x}"
            Dir = 'TX' if (Msg.FProperties & 1) == 1 else 'RX' 
            DLC = str(Msg.FDLC)
            data_strings = []
            for i in range(DLC_DATA_BYTE_CNT[Msg.FDLC]):
                data_strings.append(f"{Msg.FData[i]:02x}")
            Data = f"{' '.join(data_strings)}"
            if isinstance(Msg,TLIBCAN):
                Type = "CAN"
            elif isinstance(Msg,TLIBCANFD):
                Type = "CANFD" if Msg.FFDProperties&1 else "CAN"
            elif isinstance(Msg,TLIBLIN):
                Type = "LIN"
            else:
                Type = "None"
            return [QStandardItem(Times),
                    QStandardItem(CHN),
                    QStandardItem(ID),
                    QStandardItem(Type),
                    QStandardItem(Dir),
                    QStandardItem(DLC),
                    QStandardItem(Data)
                            ]

        def initUI(self):
            self.model = QStandardItemModel(0, 7)
            self.model.setHorizontalHeaderLabels(['times', 'CHN','ID', 'Type','Dir','DLC','Data'])
            self.tv_MsgData.setModel(self.model)
            
            # self.tv_MsgData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
            
            self.tv_MsgData.setColumnWidth(0,120)
            self.tv_MsgData.setColumnWidth(1,40)
            self.tv_MsgData.setColumnWidth(2,120)
            self.tv_MsgData.setColumnWidth(3,80)
            self.tv_MsgData.setColumnWidth(4,40)
            self.tv_MsgData.setColumnWidth(5,40)
            self.tv_MsgData.setColumnWidth(6,1000)
            self.tv_MsgData.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中整行
            self.tv_MsgData.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中一行
            self.tv_MsgData.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
            
            def clearModel():
                self.model.removeRows(0,self.model.rowCount())
                
            self.actionClear.triggered.connect(clearModel) 

            def addItem(Msg) :
                if self.model.rowCount()>=self.__ShowMsgCount:
                    self.model.removeRow(0)
                self.model.appendRow(self.tvAddRaw(Msg))
                self.tv_MsgData.scrollToBottom()
            self.btn_addFilter.clicked.connect(addItem)  

            def scanDevices():
                ADevCount = s32(0)
                tscan_scan_devices(ADevCount)
                for i in range(ADevCount.value):
                    self.cbb_Devices.addItem(str(i)) 
            self.btn_scanDevices.clicked.connect(scanDevices)  # 开始扫描设备数量

            def connect_device():
                if self.cbb_Devices.currentIndex() == -1: return 	# 如果没有选择设备，则不执行操作
                AFManufacturer = c_char_p()
                AFProduct = c_char_p()
                AFSerial = c_char_p()
                tscan_get_device_info(self.cbb_Devices.currentIndex(),AFManufacturer,AFProduct,AFSerial)  # 获取设备信息(选择要连接的设备   0)
                ret = tsapp_connect(AFSerial,self.HwHandle)  # 连接设备(选择要连接的设备   0)
                if ret == 0 or ret == 5:
                    self.Is_Connect = True  # 连接设备成功后，显示连接状态   1)开始计时
                    self.tb_Handle.setText(str(self.HwHandle.value))  # 显示设备号码(选择要连接的设备   0)
            self.btn_connect.clicked.connect(connect_device)  # Connect button clicked. 创建TCP连接函数, 并连接

            def disconnect_device():
                if self.Is_Connect: 
                    tsapp_disconnect_by_handle(self.HwHandle)  # Disconnect device. (选择要断开的设备)
            self.btn_disconnect.clicked.connect(disconnect_device)  # Disconnect button clicked. 断开连接函数    

            def get_Devices_Info():
                if self.cbb_Devices.currentIndex() == -1: return
                AFManufacturer = c_char_p()
                AFProduct = c_char_p()
                AFSerial = c_char_p()
                tscan_get_device_info(self.cbb_Devices.currentIndex(),AFManufacturer,AFProduct,AFSerial)
                self.le_AFManufacturer.setText(AFManufacturer.value.decode('utf8')) # Display device serial number. 获取设备名称   1
                self.le_AFProduct.setText(AFProduct.value.decode('utf8'))  # Display device manufacturer. 获取设备品牌   2
                self.le_AFSerial.setText(AFSerial.value.decode('utf8'))  # Display device serial number. 获取设备 serial number   3
            self.btn_getInfo.clicked.connect(get_Devices_Info)  # Get device info. 获取设备信息函数  
            
            def on_connect_event(obj):   
                self.statusBar.showMessage("connected successed") 
                
            def on_disconnect_event(obj): 	
                self.statusBar.showMessage("disconnected successed")

            OC = On_Connect_FUNC(on_connect_event)
            def OnConnect():
                tscan_register_event_connected(OC)
            ODC = On_Connect_FUNC(on_disconnect_event) 
            def OnDisconnect():
                tscan_register_event_disconnected(ODC)
            def UnOnConnect():
                tscan_unregister_event_connected(OC)
            def UnOnDisconnect():
                tscan_unregister_event_disconnected(ODC)
            self.btn_connectFunc.clicked.connect(OnConnect)  # Connect button clicked. 连接函数    
            self.btn_disconnectFunc.clicked.connect(OnDisconnect)  # Disconnect button clicked. 断开连接函数
            self.btn_unconnectFunc.clicked.connect(UnOnConnect)  # Unconnect button clicked. 注销连接函数
            self.btn_undisconnectFunc.clicked.connect(UnOnDisconnect)

            def enable_bus_statistics():
                self.Is_enable_bus = not self.Is_enable_bus
                tscan_set_auto_calc_bus_statistics(self.Is_enable_bus)
            self.btn_enableBusMsg.clicked.connect(enable_bus_statistics)  # Enable/disable busy statistics. 开/关闭busy statistics   1

            def calc_bus_statistics():
                if self.Is_enable_bus:
                    busMsg = tscan_get_bus_status(self.HwHandle,0,self.cbb_BusMsgType.currentIndex())
                    self.lb_BusMsg.setText("%f"% (busMsg))   # Display the message. 显示
            self.btn_getBusMsg.clicked.connect(calc_bus_statistics)  # Enable/disable busy statistics. 计算bus statistics   2

            def clear_bus_statistic():
                if self.Is_enable_bus:
                    tscan_clear_can_bus_statistic()
                    self.statusBar.showMessage("clear successed")
            self.btn_ClearBusMsg.clicked.connect(clear_bus_statistic)  # Enable/disable busy statistics. 清空bus statistics   3

            # CAN API 
            def OnCanTypeChange(index):
                if index == 0:
                    self.cbb_data.setEnabled(False)
                elif index == 1:
                    self.cbb_data.setEnabled(True)
            self.cbb_canType.currentIndexChanged.connect(OnCanTypeChange)  # Select the type of the can. 选择can的类型   1
            
            def set_config():
                if self.cbb_canType.currentIndex() == 0: 
                    tsapp_configure_baudrate_can(self.HwHandle,self.cbb_channelList.currentIndex(),int(self.cbb_rate.currentText()),self.cb_enableBtv.isChecked())  # Select the channel and baudrate. 设)
                elif self.cbb_canType.currentIndex() == 1:
                    tsapp_configure_baudrate_canfd(self.HwHandle,self.cbb_channelList.currentIndex(),int(self.cbb_rate.currentText()),int(self.cbb_data.currentText()),TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,self.cb_enableBtv.isChecked())
            self.btn_downloadCAN.clicked.connect(set_config)  # Select the type of the can. 选择can的类型   2 描述
            
            def __CreateMsg(is_lin =False):
                FPro = 1
                
                FId = 0x12
                if is_lin:
                    str_id = self.tb_linId.text().strip().replace("0x",'')
                    if str_id.isdigit():
                        FId = int(str_id,16)
                    data = str2List(self.tb_LINMsgData.text())
                    FPro = 1 if self.rb_LINSend.isChecked() else 0 
                    Msg = TLIBLIN(FIdxChn=self.cbb_LINchannelList.currentIndex(),FIdentifier=FId,FProperties=FPro,FData=data)
                    return Msg
                else:
                    str_id= self.tb_canId.text().strip().replace("0x",'')
                    data = str2List(self.tb_CANMsgData.text())
                if str_id.isdigit():
                    FId = int(str_id,16)
                if self.rb_remMsg.isChecked():
                    FPro |= 0x2
                if self.rb_extendMsg.isChecked():
                    FPro |= 0x4
                if self.rb_canfdMode.isChecked():
                    FFPro = 1
                    if self.cb_enableRbs.isChecked():
                        FFPro |= 0x2
                    Msg = TLIBCANFD(FIdxChn=self.cbb_channelList.currentIndex(),FDLC=self.cbb_canDLC.currentIndex(),FIdentifier=FId,FData = data,FProperties=FPro,FFDProperties=FFPro) 
                else:
                    Msg = TLIBCAN(FIdxChn=self.cbb_channelList.currentIndex(),FDLC=self.cbb_canDLC.currentIndex(),FIdentifier=FId,FData = data,FProperties=FPro)
                return Msg
            
            def __SendMsg(msg,is_cyclic=False,is_asnyc=True,is_send=True):
                timeout = 100
                ATimeout = self.tb_CycliTime.text().strip()
                if ATimeout.isdigit():
                    timeout = int(ATimeout,16)
                if isinstance(msg,TLIBCANFD):
                    if not is_send:
                        return tsapp_delete_cyclic_msg_canfd(self.HwHandle,msg)
                    if is_cyclic:
                        return tsapp_add_cyclic_msg_canfd(self.HwHandle,msg,timeout)
                    if is_asnyc:
                        return tsapp_transmit_canfd_async(self.HwHandle,msg)
                    else:
                        return tsapp_transmit_canfd_sync(self.HwHandle,msg,timeout)
                elif isinstance(msg,TLIBCAN):
                    if not is_send:
                        return tsapp_delete_cyclic_msg_can(self.HwHandle,msg)
                    if is_cyclic:
                        return tsapp_add_cyclic_msg_can(self.HwHandle,msg,timeout)
                    if is_asnyc:
                        return tsapp_transmit_can_async(self.HwHandle,msg)
                    else:
                        return tsapp_transmit_can_sync(self.HwHandle,msg,timeout)
                elif isinstance(msg,TLIBLIN):
                    # if not is_send:
                    #     return tsapp_delete_cyclic_msg_canfd(self.HwHandle,msg)
                    if is_asnyc:
                        return tsapp_transmit_lin_async(self.HwHandle,msg)
                    else:
                        return tsapp_transmit_lin_sync(self.HwHandle,msg,timeout)
                else:
                    return -1
            # def 
            def asyncSendMsg():
                __SendMsg(__CreateMsg())
            self.btn_asyncSendMsg.clicked.connect(asyncSendMsg)  # Select the type of the can. 选择can的类型   3描述描

            def syncSendMsg():
                __SendMsg(__CreateMsg(),is_asnyc=False)
            self.btn_SyncSendMsg.clicked.connect(syncSendMsg)  # Select the type of the can. 选择can的类型   3描述描

            def CyclicSendMsg():
                __SendMsg(__CreateMsg(),is_cyclic=True)
            self.btn_cyclicMsg.clicked.connect(CyclicSendMsg)

            def CyclicStopSendMsg():
                __SendMsg(__CreateMsg(),is_send=False)
            self.btn_stopCyclicMsg.clicked.connect(CyclicStopSendMsg)
            
            def __is_start_viewMsg(viewType:ViewType = ViewType.CallBackType,is_lin=False):
                if is_lin:
                    return self.cb_LINMsgShow.isChecked()
                if not self.cb_MsgShow.isChecked():
                    return False
                if viewType == ViewType.CallBackType:
                    if self.rb_CallBack.isChecked():
                        return True
                    return False
                elif viewType == ViewType.FifoType:
                    if self.rb_tsFifo.isChecked():
                        return True
                    return False
                else: return False
            # on msg event
            def On_CANFD_Event(ACANFD):
                if not __is_start_viewMsg():
                    return
                if not ACANFD.contents.FProperties&0x80:
                    
                    addItem(ACANFD.contents)
            def On_CAN_Event(ACAN):
                if not __is_start_viewMsg():
                    return
                if not ACAN.contents.FProperties&0x80:
                    addItem(ACAN.contents)
            ONCANFDEVENT = OnTx_RxFUNC_CANFD(On_CANFD_Event)
            def RegCANFDEvent():
                tsapp_register_event_canfd(self.HwHandle,ONCANFDEVENT)
            self.btn_regCANFDCallBack.clicked.connect(RegCANFDEvent)

            def UnRegCANFDEvent():
                tsapp_unregister_event_canfd(self.HwHandle,ONCANFDEVENT)
            self.btn_unregCANFDCallBack.clicked.connect(UnRegCANFDEvent)
            
            ONCANEVENT = OnTx_RxFUNC_CAN(On_CAN_Event)
            def RegCANEvent():
                tsapp_register_event_can(self.HwHandle,ONCANEVENT)
            self.btn_regCANCallBack.clicked.connect(RegCANEvent)
            
            def UnRegCANEvent():
                tsapp_unregister_event_can(self.HwHandle,ONCANEVENT)
            self.btn_unregCANCallBack.clicked.connect(UnRegCANEvent)

            def fifo_recv(MsgType:MSGType,Chnidx:s32=0,includeTx:bool = False,is_read:bool =True):
                if MsgType == MSGType.CANMSG:
                    if is_read:
                        TCANBuffer = (TLIBCAN*100)()
                        BufferSize = 100 #buffersize 就是TCANBuffer的长度
                        return tsfifo_receive_can_msgs(self.HwHandle,Chnidx,TCANBuffer,BufferSize,includeTx) #buffersize 是该次读取的报文数量
                    return tsfifo_clear_can_receive_buffers(self.HwHandle,Chnidx)
                elif MsgType == MSGType.CANFDMSG:
                    if is_read:
                        TCANFDBuffer = (TLIBCANFD*100)()
                        BufferSize = 100 #buffersize 就是TLIBCANFD的长度
                        tsfifo_receive_canfd_msgs(self.HwHandle,Chnidx,TCANFDBuffer,BufferSize,includeTx) #buffersize 是该次读取的报文数量
                    return tsfifo_clear_canfd_receive_buffers(self.HwHandle,Chnidx)
                elif MsgType == MSGType.LINMSG:
                    if is_read:
                        TLINBuffer = (TLIBLIN*100)()
                        BufferSize = 100 #buffersize 就是TLINBuffer的长度
                        tsfifo_receive_lin_msgs(self.HwHandle,Chnidx,TCANFDBuffer,TLINBuffer,includeTx) #buffersize 是该次读取的报文数量
                    return tsfifo_clear_lin_receive_buffers(self.HwHandle,Chnidx)
                elif MsgType == MSGType.FlexrayMSG:
                    if is_read: 
                        TFlexrayBuffer = (TLIBLIN*100)()
                        BufferSize = 100 #buffersize 就是TFlexrayBuffer的长度
                        tsfifo_receive_flexray_msgs(self.HwHandle,Chnidx,TFlexrayBuffer,TLINBuffer,includeTx) #buffersize 是该次读取的报文数量
                    return tsfifo_clear_flexray_receive_buffers(self.HwHandle,Chnidx)
            
            def ReadRXFDMsg():
                fifo_recv(MSGType.CANFDMSG)
            self.btn_FifoRecvCANFDRxMsg.clicked.connect(ReadRXFDMsg)

            def ReadTXRXFDMsg():
                fifo_recv(MSGType.CANFDMSG,includeTx=True)
            self.btn_FifoRecvCANFDMsg.clicked.connect(ReadTXRXFDMsg)

            def ReadRXCANMsg():
                fifo_recv(MSGType.CANMSG)
            self.btn_FifoRecvCANRxMsg.clicked.connect(ReadRXCANMsg)

            def ReadTXRXCANMsg():
                fifo_recv(MSGType.CANMSG,includeTx=True)
            self.btn_FifoRecvCANMsg.clicked.connect(ReadTXRXCANMsg)

            def ClearFDMsg():
                if 0 == fifo_recv(MSGType.CANFDMSG,is_read=False):
                    self.statusBar.showMessage("FDMsg clear successed")
            self.btn_FifoClearCANFDMsg.clicked.connect(ClearFDMsg)

            def ClearCANMsg():
                if 0 == fifo_recv(MSGType.CANMSG,is_read=False):
                    self.statusBar.showMessage("CANMsg clear successed")
            self.btn_FifoClearCANMsg.clicked.connect(ClearCANMsg)

            self.CAN_Db = TSDB() 
            # CAN DataBase 
            def click_find_file_path():
            # 设置文件扩展名过滤，同一个类型的不同格式如xlsx和xls 用空格隔开
                filename, filetype = QFileDialog.getOpenFileName(self, "选取数据库文件",filter=
                                                        "DBC(*.dbc);;xml(*.xml)")
                if filename != "": 
                    if filetype =="DBC(*.dbc)":
                        ret = self.CAN_Db.load_dbc(filename)
                        if ret[0] == 0:
                            self.statusBar.showMessage("load "+filename+ " successed")
                        else:
                            self.statusBar.showMessage(ret[1])
            self.btn_laodDBC.clicked.connect(click_find_file_path)

            # LIN API 
            def configLin():
                if 0 ==tsapp_configure_baudrate_lin(self.HwHandle,self.cbb_LINchannelList.currentIndex(),float(self.cbb_linBtv.currentText()),self.cbb_linP.currentIndex()):
                    tslin_set_node_funtiontype(self.HwHandle,self.cbb_LINchannelList.currentIndex(),self.cbb_linType.currentIndex())
            self.btn_downloadLIN.clicked.connect(configLin)

            # 异步发送
            def Async_sendLinMsg():
                __SendMsg(__CreateMsg(True))
            self.btn_asyncSendLINMsg.clicked.connect(Async_sendLinMsg)
            
            # 同步发送
            def sync_sendLinMsg():
                __SendMsg(__CreateMsg(True),is_asnyc=False)
            self.btn_SyncSendLINMsg.clicked.connect(sync_sendLinMsg)

            def on_lin_event(ALIN):
                if not __is_start_viewMsg(is_lin=True): return
                addItem(ALIN.contents)
            ONLIN = OnTx_RxFUNC_LIN(on_lin_event)
            def reg_linEvent():
                tsapp_register_event_lin(self.HwHandle,ONLIN)
            self.btn_regLINCallBack.clicked.connect(reg_linEvent)
            def unreg_linEvent():
                tsapp_unregister_event_lin(self.HwHandle,ONLIN)
            self.btn_unregLINCallBack.clicked.connect(unreg_linEvent)
            def recvLINMsgs():
                fifo_recv(MSGType.LINMSG)
            self.btn_FifoRecvLINRxMsg.clicked.connect(recvLINMsgs)
            def recvTxRxMsgs():
                fifo_recv(MSGType.LINMSG,includeTx=True)
            self.btn_FifoRecvLINMsg.clicked.connect(recvTxRxMsgs)
            def clearLINMsgs():
                fifo_recv(MSGType.LINMSG,is_read=False)
            self.btn_FifoClearLINMsg.clicked.connect(clearLINMsgs)

    except:
        pass
            
            

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序

    window = MyWindows()

    window.show()

    sys.exit(app.exec_())  # 程序执行循环
