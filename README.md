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

如果在使用过程中遇到无法解决的问题，你可以在这里找到我：[夜雨微寒的个人主页](https://xugongli.github.io/about/)；

另外，也可以通过提交issue的方式提交问题。




