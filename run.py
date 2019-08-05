# 导入python 自带库
import json
import os
import time

import openpyxl
import pandas as pd
import requests
from ChinaArea.China_area import province_dict, cities_dict, city_code_dict
from Crawler.BaiduMapCrawler import BdMapCrawler
# 导入自定义模块
from Mainwindow.Mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from pandas import DataFrame
from qtpandas.models.DataFrameModel import DataFrameModel


class BaiduMapCrawler_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BaiduMapCrawler_main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("百度地图数据采集工具_by_夜雨微寒")
        self.setWindowIcon(QtGui.QIcon(r'./resource/image/spider3.png'))
        self.result = []

        '''初始化pandasqt'''
        widget = self.pandastablewidget
        # 设置qtpandas.DataFrameMode()
        self.model = DataFrameModel()
        widget.setViewModel(self.model)

        # 初始化省份
        self.comboBox_prov.clear()
        self.comboBox_prov.addItem('请选择')
        for k, v in province_dict.items():
            self.comboBox_prov.addItem(v, k)

    # 定义按下 开始抓取 按钮后的操作
    @pyqtSlot()
    def on_pushButton_crawl_clicked(self):
        self.crawl()

    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        self.result = []
        self.listWidget.clear()
        df = self.result_to_dataframe()
        self.model.setDataFrame(df)

    # 初始化城市
    @pyqtSlot(int)
    def on_comboBox_prov_activated(self, index):
        self.comboBox_city.addItem('请选择')
        key = int(self.comboBox_prov.itemData(index))
        self.comboBox_city.clear()
        city_info_dict = cities_dict[key]
        for k, v in city_info_dict.items():
            self.comboBox_city.addItem(v, k)

    def insert2list(self, crawl_result):
        for item in crawl_result:
            self.result.append(item)
        self.listWidget_show()

    # 将抓取的poi名称在listWidget中显示
    def listWidget_show(self):
        df = self.result_to_dataframe()
        self.model.setDataFrame(df)
        self.listWidget.clear()
        for item in self.result:
            self.listWidget.addItem(item[2])

    def show_crawl_progress(self, string):
        self.label_progress.setText(string)

    def display_poi_is_crawling(self, poi_str_lst):

        df = DataFrame(poi_str_lst, columns=['poi_name', '区域'])

        self.model.setDataFrame(df)

    def crawl(self):
        keyword = self.lineEdit_keyword.text().strip()
        province = self.comboBox_prov.currentText()
        print(province)
        city = self.comboBox_city.currentText()
        print(city)
        print(city, keyword)
        if keyword.replace(' ', '') == '':
            return
        # 获取百度地图城市代码
        try:
            citycode = city_code_dict[city]
        except BaseException:
            citycode = ''
        print(citycode)
        try:
            self.crawler = BdMapCrawler(keyword, province, city, citycode)
            self.crawler.finished_signal.connect(self.insert2list)
            self.crawler.page_done_signal.connect(self.show_crawl_progress)
            self.crawler.poi_is_crawling.connect(self.display_poi_is_crawling)
            self.crawler.start()
        except Exception as e:
            print(e)

    def result_to_dataframe(self):
        columns_name = [
            '省',
            '市',
            '百度商户名',
            '地址',
            '行业',
            '电话',
            '所属区域',
            '详细地址',
            '曾用名',
            '行业及代码',
            'aoi',
            '经纬度范围',
            '经度',
            '纬度']
        # 将列表数据转化为dataframe
        df = DataFrame(self.result, columns=columns_name)
        return df

    def write_to_excel(self, df):
        filename = time.strftime("%Y-%m-%d_%Hh_%Mm_%Ss") + '.xlsx'
        df.to_excel(filename, index=False)
        print("抓取数据已经写入到本地！")

    def openFile(self):
        DirName = QtWidgets.QFileDialog.getExistingDirectory(
            self.Filedialog, "浏览文件", "C:", QtWidgets.QFileDialog.ShowDirsOnly)
        self.DirlineEdit.setText(DirName)

    def saveFileToExcel(self):
        try:
            fileName = self.FilelineEdit.text()
            if fileName in ['', "文件名.xlsx"]:
                fileName = time.strftime("%Y-%m-%d_%Hh_%Mm_%Ss") + '采集结果.xlsx'

            fileName_path = self.DirlineEdit.text()
            fileName_path = os.path.join(fileName_path, fileName)
            print(fileName_path)

            if os.path.isfile(fileName_path):
                existMessage = QtWidgets.QMessageBox.warning(
                    self,
                    '文件已存在',
                    fileName + ' 已存在,是否覆盖该文件',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

                if existMessage == QtWidgets.QMessageBox.No:
                    return
            df = self.result_to_dataframe()
            df.to_excel(r'%s' % fileName_path, index=False)
            SucessMessage = QtWidgets.QMessageBox.information(self, '导出EXCEL', '导出成功', QtWidgets.QMessageBox.Yes)

            if SucessMessage == QtWidgets.QMessageBox.Yes: self.Filedialog.close()

        except Exception as e:
            QtWidgets.QMessageBox.information(self, '导出失败', '%s' % e, QtWidgets.QMessageBox.Yes)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bd_crawler = BaiduMapCrawler_main()
    bd_crawler.show()
    sys.exit(app.exec_())
