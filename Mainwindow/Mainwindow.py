# -*- coding: utf-8 -*-

import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import  QApplication
# Form implementation generated from reading ui file 'F:\PyQt5_Workstation\baidumap_crawler.ui'
#
# Created by: soaringsoul
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import (QAction, QMessageBox)


class WebView(QWebEngineView):
    def __init__(self, url='https://xugongli.github.io/'):
        super(WebView, self).__init__()
        self.load(QUrl(url))
        self.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 778)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        qss_file = open(os.getcwd() + '/resource/QSS/Mainwindow.qss').read()
        self.setStyleSheet(qss_file)
        self.aboutAct = QAction("&About", self,
                                statusTip="Show the application's About box",
                                triggered=self.about)
        # self.mainAct = QAction("回到主程序界面", self,
        #                         statusTip="Show the application's About box")

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_prov = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prov.sizePolicy().hasHeightForWidth())
        self.label_prov.setSizePolicy(sizePolicy)
        self.label_prov.setMinimumSize(QtCore.QSize(0, 0))
        self.label_prov.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_prov.setObjectName("label_prov")
        self.horizontalLayout.addWidget(self.label_prov)
        self.comboBox_prov = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_prov.sizePolicy().hasHeightForWidth())
        self.comboBox_prov.setSizePolicy(sizePolicy)
        self.comboBox_prov.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_prov.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.comboBox_prov.setObjectName("comboBox_prov")
        self.horizontalLayout.addWidget(self.comboBox_prov)
        self.label_city = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_city.sizePolicy().hasHeightForWidth())
        self.label_city.setSizePolicy(sizePolicy)
        self.label_city.setMinimumSize(QtCore.QSize(0, 0))
        self.label_city.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_city.setObjectName("label_city")
        self.horizontalLayout.addWidget(self.label_city)
        self.comboBox_city = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_city.sizePolicy().hasHeightForWidth())
        self.comboBox_city.setSizePolicy(sizePolicy)
        self.comboBox_city.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_city.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.comboBox_city.setObjectName("comboBox_city")
        self.horizontalLayout.addWidget(self.comboBox_city)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_keyword.sizePolicy().hasHeightForWidth())
        self.lineEdit_keyword.setSizePolicy(sizePolicy)
        self.lineEdit_keyword.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_keyword.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.horizontalLayout.addWidget(self.lineEdit_keyword)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pandastablewidget = DataTableWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pandastablewidget.sizePolicy().hasHeightForWidth())
        self.pandastablewidget.setSizePolicy(sizePolicy)
        self.pandastablewidget.setMinimumSize(QtCore.QSize(800, 600))
        self.pandastablewidget.setObjectName("pandastablewidget")
        self.verticalLayout_2.addWidget(self.pandastablewidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_display = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy)
        self.label_display.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_display.setObjectName("label_display")
        self.horizontalLayout_3.addWidget(self.label_display)
        self.label_progress = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_progress.sizePolicy().hasHeightForWidth())
        self.label_progress.setSizePolicy(sizePolicy)
        self.label_progress.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_progress.setText("")
        self.label_progress.setObjectName("label_progress")
        self.horizontalLayout_3.addWidget(self.label_progress)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_crawl = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_crawl.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.pushButton_crawl.setObjectName("pushButton_crawl")
        self.horizontalLayout_2.addWidget(self.pushButton_crawl)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_clear.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_clear.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_2.addWidget(self.pushButton_clear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1030, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.menu_3.addSeparator()
        self.menu_3.addSeparator()
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        outPutAction = QtWidgets.QAction(QtGui.QIcon(os.getcwd() + '/resource/spider.png'), '导出文件', self)
        outPutAction.triggered.connect(self.outPutFile)
        self.menu.addAction(outPutAction)
        self.menu_3.addAction(self.aboutAct)
        # self.menu_2.addAction(self.mainAct)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_prov.setText(_translate("MainWindow", "省    份"))
        self.label_city.setText(_translate("MainWindow", "城    市"))
        self.label.setText(_translate("MainWindow", "关键词"))
        self.label_display.setText(_translate("MainWindow", "采集进度"))
        self.pushButton_crawl.setText(_translate("MainWindow", "开始采集"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空结果"))
        self.menu.setTitle(_translate("MainWindow", "导出结果"))
        self.menu_3.setTitle(_translate("MainWindow", "关于我"))
        # self.menu_2.setTitle(_translate("MainWindow", "主程序"))

    def outPutFile(self):
        print('开始运行导出程序')
        try:
            self.Filedialog = QtWidgets.QDialog(self.centralWidget)
            self.Filedialog.setFixedSize(600, 150)
            self.Filedialog.setWindowTitle('导出EXCEL文件')
            self.Filedialog.setModal(True)

            self.Dirlabel = QtWidgets.QLabel(self.Filedialog)
            self.Dirlabel.move(20, 40)
            self.Dirlabel.setFixedSize(70, 30)
            self.Dirlabel.setText('文件位置: ')


            self.DirlineEdit = QtWidgets.QLineEdit(self.Filedialog)
            self.DirlineEdit.move(100, 40)
            self.DirlineEdit.setFixedSize(350, 30)
            self.DirlineEdit.setText(os.getcwd())

            self.Filelabel = QtWidgets.QLabel(self.Filedialog)
            self.Filelabel.move(20, 100)
            self.Filelabel.setFixedSize(70, 30)
            self.Filelabel.setText('文件名称: ')


            self.FilelineEdit = QtWidgets.QLineEdit(self.Filedialog)
            self.FilelineEdit.move(100, 100)
            self.FilelineEdit.setFixedSize(350, 30)
            self.FilelineEdit.setText("文件名.xlsx")

            self.YesButton = QtWidgets.QPushButton(self.Filedialog)
            self.YesButton.move(470, 100)
            self.YesButton.setFixedSize(100, 30)
            self.YesButton.setText('确定')
            self.YesButton.clicked.connect(self.saveFileToExcel)

            self.browlButton = QtWidgets.QPushButton(self.Filedialog)
            self.browlButton.move(470, 40)
            self.browlButton.setFixedSize(100, 30)
            self.browlButton.setText('浏览')
            self.browlButton.clicked.connect(self.openFile)

            self.Filedialog.show()
        except Exception as e:
            print(e)

    def about(self):
        self.webview = WebView()
        self.webview.load(QUrl("https://xugongli.github.io/"))
        self.setCentralWidget(self.webview)



from qtpandas.views.DataTableView import DataTableWidget

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
