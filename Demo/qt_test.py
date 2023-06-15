'''
Author: seven 865762826@qq.com
Date: 2023-06-15 12:59:16
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-06-15 12:59:27
FilePath: \libTSCANApi\Demo\qt_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
dict_1 = {'#01号车间': ['QJ_01_1', 'QJ_01_2', 'QJ_01_3', 'QJ_01_4', 'QJ_01_5', 'QJ_01_6', 'QJ_01_7', 'QJ_01_8', 'QJ_01_9', 'QJ_01_10'], '#02号车间': ['QJ_02_1', 'QJ_02_2', 'QJ_02_3', 'QJ_02_4', 'QJ_02_5', 'QJ_02_6', 'QJ_02_7', 'QJ_02_8', 'QJ_02_9', 'QJ_02_10'], '#03号车间': ['QJ_03_1', 'QJ_03_2', 'QJ_03_3', 'QJ_03_4', 'QJ_03_5', 'QJ_03_6', 'QJ_03_7', 'QJ_03_8', 'QJ_03_9', 'QJ_03_10']}
list_add= {}
list_add_clumon = []
class window(QWidget):
    def __init__(self):
        super(window,self).__init__()
        self.resize(800,800)
        self.setWindowTitle("wwww")
        self.verh = QHBoxLayout(self)
        self.treeView_add_fjg = QTreeWidget(self)
        self.treeView_add_fjg.setColumnCount(2)
        self.treeView_add_fjg.setHeaderLabels(["发酵罐","状态"])#设置标题
        self.treeView_add_fjg.setColumnWidth(0,150)#设置列宽
 
        self.root=QTreeWidgetItem(self.treeView_add_fjg)
        self.root.setText(0,"可用发酵罐")
        self.root.setIcon(0,QIcon("../image/add_one_f.png"))
        for i in dict_1.keys():
            child1 = QTreeWidgetItem(self.root)
            child1.setText(0,i)
            child1.setIcon(0,QIcon("../image/cj2.png"))
            child1.setText(1,str(len(dict_1[i]))+"个可使用")
            for j in dict_1[i]:
                self.child2 = QTreeWidgetItem(child1)
                self.child2.setText(0,str(j))
                self.child2.setIcon(0,QIcon("../image/image_fajiao.png"))
                self.child2.setText(1,"可使用")
                self.child2.setCheckState(0, not Qt.CheckState)
                # self.child2.checkState(0)
        self.treeView_add_fjg.expandAll()
        self.verh.addWidget(self.treeView_add_fjg)
        self.btns_add = QPushButton(self)
        self.btns_add.setText("增加")
        self.verh.addWidget(self.btns_add)
        self.btns_del = QPushButton(self)
        self.btns_del.setText("减少")
        self.verh.addWidget(self.btns_del)
 
        self.treeView_usable = QTreeWidget(self)
        self.verh.addWidget(self.treeView_usable)
 
        # self.treeView_add_fjg.clicked.connect(self.onclick)
        self.treeView_add_fjg.itemChanged.connect(self.onclick)
        self.btns_add.clicked.connect(self.add_fjg)
    def add_fjg(self):
        self.treeView_usable.clear()
        self.root_1 = QTreeWidgetItem(self.treeView_usable)
        self.root_1.setText(0, "已选择的发酵罐")
        self.root_1.setIcon(0, QIcon("../image/add_one_f.png"))
        self.treeView_usable.destroy()
        self.treeView_usable.setColumnCount(1)
        for i in list_add:
            child1 = QTreeWidgetItem(self.root_1)
            child1.setText(0, i)
            child1.setIcon(0, QIcon("../image/image_fajiao_add.png"))
            child1.setText(1, "已选择")
        self.treeView_usable.expandAll()
    def onclick(self,item,cloumn):
        if item.checkState(cloumn) == Qt.Checked:
            print("checked", item.text(0),item.text(1))
            list_add[item.text(0)]=item.text(0)
            list_add_clumon.append(self.treeView_add_fjg.currentColumn())
        if item.checkState(cloumn) == Qt.Unchecked:
            print("unchecked", item.text(0))
        print(list_add)
        print(list_add_clumon)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    fjg_gl = window()
    fjg_gl.show()
    sys.exit(app.exec_())
