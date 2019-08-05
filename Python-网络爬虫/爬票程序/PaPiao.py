# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaPiao.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import  QPalette,QPixmap,QColor    # 导入QtGui模块

from PyQt5.QtGui import *    # 导入QtGui
from PyQt5.QtCore import Qt    # 导入Qt类
from PyQt5.QtWidgets import *    # 导入QtWidgets下所有类及方法
from query_request import *    # 导入用于查询的文件
from get_stations import *    # 导入get_stations文件

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 786)
        MainWindow.setMinimumSize(QtCore.QSize(960, 786))
        MainWindow.setMaximumSize(QtCore.QSize(960, 786))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 960, 141))
        self.label0.setText("")
        self.label0.setObjectName("label0")

        label0_img = QPixmap('train.png')    # 导入顶部位图
        self.label0.setPixmap(label0_img)    # 设置调色版

        self.frame0 = QtWidgets.QFrame(self.centralwidget)
        self.frame0.setGeometry(QtCore.QRect(0, 140, 960, 80))
        self.frame0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame0.setObjectName("frame0")

        self.frame0.setAutoFillBackground(True)    # 开启自动填充背景
        palette0 = QPalette()    # 调色板类
        palette0.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame0.setPalette(palette0)    # 设置调色板

        self.chufadi0 = QtWidgets.QLabel(self.frame0)
        self.chufadi0.setGeometry(QtCore.QRect(30, 25, 54, 20))
        self.chufadi0.setObjectName("chufadi0")
        self.chufadi1 = QtWidgets.QTextEdit(self.frame0)
        self.chufadi1.setGeometry(QtCore.QRect(90, 20, 104, 31))
        self.chufadi1.setObjectName("chufadi1")
        self.label_2 = QtWidgets.QLabel(self.frame0)
        self.label_2.setGeometry(QtCore.QRect(265, 250, 72, 15))
        self.label_2.setObjectName("label_2")
        self.chufari0 = QtWidgets.QLabel(self.frame0)
        self.chufari0.setGeometry(QtCore.QRect(440, 25, 54, 20))
        self.chufari0.setObjectName("chufari0")
        self.chaxun = QtWidgets.QPushButton(self.frame0)
        self.chaxun.setGeometry(QtCore.QRect(680, 20, 93, 28))
        self.chaxun.setObjectName("chaxun")
        self.mudidi1 = QtWidgets.QTextEdit(self.frame0)
        self.mudidi1.setGeometry(QtCore.QRect(300, 20, 104, 31))
        self.mudidi1.setObjectName("mudidi1")
        self.mididi0 = QtWidgets.QLabel(self.frame0)
        self.mididi0.setGeometry(QtCore.QRect(240, 25, 54, 20))
        self.mididi0.setObjectName("mididi0")
        self.chufari1 = QtWidgets.QTextEdit(self.frame0)
        self.chufari1.setGeometry(QtCore.QRect(500, 20, 104, 31))
        self.chufari1.setObjectName("chufari1")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(0, 220, 960, 40))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.checkBox0 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox0.setGeometry(QtCore.QRect(110, 10, 91, 19))
        self.checkBox0.setObjectName("checkBox0")
        self.checileixing = QtWidgets.QLabel(self.frame1)
        self.checileixing.setGeometry(QtCore.QRect(30, 13, 72, 15))
        self.checileixing.setObjectName("checileixing")
        self.checkBox1 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox1.setGeometry(QtCore.QRect(260, 10, 91, 19))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox2.setGeometry(QtCore.QRect(400, 10, 91, 19))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox3.setGeometry(QtCore.QRect(550, 10, 91, 19))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox4.setGeometry(QtCore.QRect(690, 10, 91, 19))
        self.checkBox4.setObjectName("checkBox4")
        
        self.frame1.setAutoFillBackground(True)    # 开启自动填充背景
        palette1 = QPalette()    # 调色板类
        palette1.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame1.setPalette(palette1)    # 设置调色板

        # self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text = QtWidgets.QTableView(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 330, 960, 457))
        self.text.setObjectName("text")
        
        self.model = QStandardItemModel()    # 创建存储数据模式
        # 根据空间自动改变宽度并且不可修改列宽度
        self.text.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头不可见
        self.text.horizontalHeader().setVisible(False)
        # 纵向表头不可见
        self.text.verticalHeader().setVisible(False)
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text.setFont(font)
        # 设置表格内容不可编辑
        self.text.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 垂直滚动条始终开启
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 260, 960, 70))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        label1_img = QPixmap('bg1.png')    # 导入顶部位图
        self.label1.setPixmap(label1_img)    # 设置调色版

    # 查询按钮的单击事件
    def on_click(self):
        get_from = self.chufadi1.toPlainText()    # 获取出发地
        get_to = self.mudidi1.toPlainText()    # 获取目的地
        get_date = self.chufari1.toPlainText()    # 获取出发日期
        # 判断车站文件是否存在
        if isStations() == True:
            stations = eval(read())    # 读取所有车站并转换为dic类型
            # 判读所有参数是否为空，出发地、目的地、出发日期
            if get_from != "" and get_to != "" and get_date != "":
                # 判断输入的车站名称是否存在，以及时间格式是否正确
                if get_from in stations and get_to in stations and is_valid_data(get_date):
                    # 获取输入的日期是当前年初到现在一共过了多少天
                    inputYearDay = time.strptime(get_date,"%Y-%m-%d").tm_yday
                    # 获取系统当前日期是当前年初到现在一共过了多少天
                    yearToday = time.localtime(time.time()).tm_yday
                    # 计算时间差，也就是输入的日期减掉系统当前的日期
                    timeDifference = inputYearDay - yearToday
                    # 判断时间差为0时证明查询当前的查票
                    # 以及29天以后的车票，12306官方要求只能查询30天以内的车票
                    if timeDifference >=0 and timeDifference <= 28:
                        from_station = stations[get_from]    # 在所有车站文件中找到对应的参数、出发地
                        to_station = stations[get_to]    # 目的地
                        data = query(get_date,from_station,to_station)    # 发送查询请求，并获取返回信息
                        self.checkBox_default()
                        if len(data) != 0:    # 判断返回的值是否为空
                        # 如果不为空的数据就将车票信息显示在表格中
                            self.displayTable(len(data),16,data)
                        else:
                            self.messageDialog('警告','没有返回的网络数据！')
                    else:
                        self.messageDialog('警告','超出查询日期的范围内，不可查询过去的以及29天以后的车票信息！')
                else:
                    self.messageDialog('警告','输入的站名不存在，或日期格式不正确！')
            else:
                self.messageDialog('警告','请填写车站名称！')
        else:
            self.messageDialog('警告','未下载车站查询文件！')

    # 高铁复选框事件处理
    def change_G(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            g_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_g_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 动车复选框事件处理
    def change_D(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            d_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_d_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 直达车复选框事件处理
    def change_Z(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            z_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_z_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 特快车复选框事件处理
    def change_T(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            t_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_t_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 快速复选框事件处理
    def change_K(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            k_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_k_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 将所有车次分类复选框取消勾选
    def checkBox_default(self):
        self.checkBox0.setChecked(False)
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)

    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialog(self,title,message):
        msg_box = QMessageBox(QMessageBox.Warning, title, message)
        msg_box.exec_()

    # 用于显示车次信息的表格
    # train参数为共有多少趟列车，该参数作为表格的行
    # info参数为每趟列车的具体信息，例如有座、无座、卧铺等。该参数作为表格的列
    def displayTable(self, train, info, data):
        self.model.clear()
        for row in range(train):
            for column in range(info):
                # 添加表格内容
                item = QStandardItem(data[row][column])
                # 向表格中添加具体内容
                self.model.setItem(row,column,item)
        # 设置表格存储数据的模式
        self.text.setModel(self.model)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手爬票"))
        self.chufadi0.setText(_translate("MainWindow", "出发地:"))
        self.label_2.setText(_translate("MainWindow", "目的地:"))
        self.chufari0.setText(_translate("MainWindow", "出发日:"))
        self.chaxun.setText(_translate("MainWindow", "查询"))
        self.mididi0.setText(_translate("MainWindow", "目的地:"))
        self.checkBox0.setText(_translate("MainWindow", "GC-高铁"))
        self.checileixing.setText(_translate("MainWindow", "车次类型:"))
        self.checkBox1.setText(_translate("MainWindow", "D-动车"))
        self.checkBox2.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox3.setText(_translate("MainWindow", "T-特快"))
        self.checkBox4.setText(_translate("MainWindow", "K-快速"))

        self.chufari1.setText(get_time())    # 出发日显示当天日期
        self.chaxun.clicked.connect(self.on_click)    # 查询按钮指定单击事件的方法
        self.checkBox0.stateChanged.connect(self.change_G)    # 高铁选择与取消事件
        self.checkBox1.stateChanged.connect(self.change_D)    # 动车选择与取消事件
        self.checkBox2.stateChanged.connect(self.change_Z)    # 直达车选择与取消事件
        self.checkBox3.stateChanged.connect(self.change_T)    # 特快车选择与取消事件
        self.checkBox4.stateChanged.connect(self.change_K)    # 快车选择与取消事件

import time
# 获取系统当前时间并转换请求数据所需要的格式
def get_time():
        # 获取当前时间戳
        now = int(time.time())
        # 转换为其它日期格式：如："%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d",timeStruct)
        return strTime
def is_valid_data(str):
    '''判断是否是一个有效日期字符串'''
    try:
        time.strptime(str,"%Y-%m-%d")
        return True
    except:
        return False


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)    # 实例化Qapplication类，作为GUI主程序的入口
    MainWindow = QtWidgets.QMainWindow()    # 创建QMainWindow
    ui = Ui_MainWindow()    # 实例UI类
    ui.setupUi(MainWindow)    # 设置窗体UI
    MainWindow.show()    # 显示窗体
    sys.exit(app.exec_())    # 当窗口创建完成以后，需要结束主循环


if __name__ == '__main__':
    if isStations() == False:    # 判断是否存在车站文件
        getStation()    # 下载文件
        show_MainWindow()    # 显示主窗体
    else:
        show_MainWindow()
