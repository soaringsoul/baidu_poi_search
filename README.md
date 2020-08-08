<img align="right" width="200" height="200" src="https://pic4.zhimg.com/v2-78d1472351272f41d8dd76a6d8a635c7_xll.jpg">

# 百度地图数据采集GUI工具
===========================================

[![image](https://img.shields.io/pypi/v/requests.svg)](https://pypi.org/project/requests/)
[![image](https://img.shields.io/pypi/l/requests.svg)](https://pypi.org/project/requests/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)




## 功能：
* 根据关键词（街道、酒店或其他标志性建筑物等），查询指定区域周边的商户、酒店、交通位置等兴趣点信息  

* 将采集结果以表格形式在界面实时呈现

* 将采集结果导出为Excel文件  

## 运行环境

python3.5

win10

## 2019补充说明

2016年写这个小项目时用的是python3.5,windows10环境。
现在，我用python3.6也可以正常运行。我把过程写在readme里了，我测试了下是没有问题的。



另外要特别说明的是当时写这个项目的目的主要是想体验下qtpandas的功能，其实这个工具并不实用，采集的数据维度少，而且也不全，个人感觉用来学习pyqt5还可以，真正用来采集数据是华而不实的。



如果真是需要采集百度兴趣点数据，可以clone我另外一个项目：https://github.com/xugongli/BaiduMapPoiSpider

这个是货真价实的数据采集工具，配置好ak，单日单进程 采集百万级数据是没有一点问题的。

这个采集程序已经为我之前的公司的多个数据调研项目提供了很多必要的数据支持。

建议大家使用。



## 使用

推荐使用virualenv 进行如下操作。

### 1 安装依赖库

* pip install -r  `requirements.txt`


### 2 安装qtpandas 1.0.4

qtpandas github地址：https://github.com/draperjames/qtpandas

> 之前写这个小程序时qtapndas有点问题，于是给qtpandas提交了这个问题的issue,

> 2018年8月，收到qtpandas作者回复，已经修复这个bug.
可以直接在github上搜索qtpandas，然后 ```pip install .```安装，或者```python setup.py```
> 注意还是要下载到本地安装，不要直接使用`pip install qtpandas `安装。



如果`git clone`较慢，这里提供一个百度云的下载链接:

> 链接：https://pan.baidu.com/s/157Dlar8HcBSLQlvwWtTD2A 
> 提取码：msud 



## 3 运行

1. 执行 python run.py，选择省、市，然后输入关键词，例：天津市 便利店

![Alt text](https://github.com/xugongli/GithubProjectImages/blob/master/PyQt5-BaiduMapCrawler_Images//run_main.gif)  


2. 导出抓取结果为excel表格  


![Alt text](https://github.com/xugongli/GithubProjectImages/blob/master/PyQt5-BaiduMapCrawler_Images//result_output.gif)  


3. 导出excel文件示例

![Alt text](https://github.com/xugongli/GithubProjectImages/blob/master/PyQt5-BaiduMapCrawler_Images//result.png)  



## 联系我

如果在使用过程中遇到无法解决的问题，你可以通过关注我的个人公众号找到我。

另外，也可以通过提交issue的方式提交问题。

![rewnwen_wechat](./images/rewnwen_wechat.png)




