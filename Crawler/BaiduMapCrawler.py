import time

import requests
from PyQt5 import QtCore


class BdMapCrawler(QtCore.QThread):

    finished_signal = QtCore.pyqtSignal(list)
    page_done_signal = QtCore.pyqtSignal(str)
    poi_is_crawling = QtCore.pyqtSignal(list)

    def __init__(self, keyword, province, city, citycode):
        super(BdMapCrawler, self).__init__()
        self.keyword = keyword
        self.province = province
        self.city = city
        self.citycode = citycode
        self.headers = {
            'Host': "map.baidu.com",
            "Connection": "keep-alive",
            "Cache - Control": "max - age = 0",
            "Upgrade - Insecure - Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }

    def run(self):
        print('run')
        try:
            self.result = []
            data_list = []
            page = 0
            keys = [
                'name',
                'addr',
                'std_tag',
                'tel',
                'area_name',
                'address_norm',
                'alias',
                'cla',
                'aoi',
                'geo',
                'x',
                'y']
            keys_add = [
                'area_name',
                'address_norm',
                'alias',
                'cla',
                'aoi',
                'geo',
                'x',
                'y']
            while True:
                try:
                    # data即为访问每个百度页面获取到的数据，是一个由字典对象组成的列表。
                    data = self.search(self.keyword, self.citycode, page)
                    # print(data)
                except BaseException:
                    break
                # 若data列表为空,中止程序。
                if not data:
                    break
                for line in data:
                    item = [self.province, self.city]
                    for key in keys:
                        try:
                            item.append(line[key])
                        except BaseException:
                            item.append('')
                    self.result.append(item)
                self.page_done_signal.emit(
                    '当前城市【%s】' %
                    self.city +
                    '正在抓取第--' +
                    str(page) +
                    '--页')
                page += 1
                time.sleep(0.5)
            # print(self.result)
            self.page_done_signal.emit('%s' % self.city + '获取数据成功!')
            self.finished_signal.emit(self.result)
        except Exception as e:
            print(e)

    def search(self, keyword, citycode, page):
        url = 'http://map.baidu.com/'
        pay_load = {
            'reqflag': 'pcmap',
            'qt': 's',
            'wd': '%s' % keyword,
            'l': '18',
            'sug': '0',
            'pn': '%s' % page,
            'nn': '%s' % (page * 10),
            'from': 'webmap',
            'wd2': '',
            'biz': '1',
            'c': '%s' % citycode,
            'ie': 'utf-8',
            'newmap': '1',
            'da_par': 'direct',
            'src': '0',
            'pcevaname': 'pc4.1',
            'da_src': 'searchBox.button'}

        res = requests.get(url, params=pay_load, headers=self.headers)
        # 解析请求结果
        data_json = res.json()
        data_pois = data_json['content']
        # 打印抓取到的百度地图pois数据
        df_lst = []
        for dict_here in data_pois:
            print_list = [
                dict_here['name'],
                dict_here['area_name']]
            poi_str = '获取数据ing：%s' % (print_list)
            print(poi_str)
            df_lst.append(print_list)
        self.poi_is_crawling.emit(df_lst)
        return data_pois
