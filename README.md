<img align="right" width="200" height="200" src="https://pic4.zhimg.com/v2-78d1472351272f41d8dd76a6d8a635c7_xll.jpg">

# 百度地图数据查询GUI工具
===========================================

[![image](https://img.shields.io/pypi/v/requests.svg)](https://pypi.org/project/requests/)
[![image](https://img.shields.io/pypi/l/requests.svg)](https://pypi.org/project/requests/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)



## 项目简介

`baidu_poi_search` 是一个开源的地理空间数据查询与可视化工具，用于从百度地图批量查询兴趣点（POI）数据，并通过图形界面完成查询、浏览和导出工作。

项目最初于 2016 年开源，目前由 @soaringsoul 持续维护和改进，已经被部分高校课程、独立研究者和行业用户用于地理研究、选址分析和教学示例。

本项目采用开源许可，欢迎通过 Issue / Pull Request 参与共建。

## 面向人群与应用场景

* 地理信息系统（GIS）、城市研究、交通与规划等方向的研究者和学生
* 从事选址分析、商圈研究、位置情报（Location Intelligence）的数据分析师和工程师
* 希望在不过多编写代码的前提下完成 POI 数据查询与导出的业务人员和爱好者

## 功能：
* 根据关键词（街道、酒店或其他标志性建筑物等），查询指定区域周边的商户、酒店、交通位置等兴趣点信息  

* 将查询结果以表格形式在界面实时呈现

* 将查询结果导出为 Excel 文件，用于后续的数据分析或 GIS 处理  

## 运行环境

python3.5

win10

## 2019补充说明

2016年最初编写这个小项目时使用的是python3.5、Windows10环境。
目前在python3.6等3.x版本上也已验证可以正常运行，相关过程已经在本说明中给出，并经过实际测试。

本工具最初的出发点是结合qtpandas探索基于PyQt5的表格数据展示，因此在数据字段数量和查询规模上更适合教学、原型验证和中小规模的查询任务。
对于需要大规模、高并发查询百度兴趣点数据的同学，可以参考我维护的另一个项目：https://github.com/xugongli/BaiduMapPoiSpider

该查询程序在配置好AK后，单日单进程处理百万级查询数据没有问题，已经为多个真实的数据调研项目提供过生产级的数据支持。



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


2. 导出查询结果为excel表格  


![Alt text](https://github.com/xugongli/GithubProjectImages/blob/master/PyQt5-BaiduMapCrawler_Images//result_output.gif)  


3. 导出excel文件示例

![Alt text](https://github.com/xugongli/GithubProjectImages/blob/master/PyQt5-BaiduMapCrawler_Images//result.png)  


## 开源社区与项目状态

本项目自开源以来，已经收获了来自社区的 Star 和 Fork（具体数量以 GitHub 页面为准），并被多位开发者用于个人项目、教学示例以及企业内部工具。

仓库目前由 @soaringsoul 作为主要维护者，负责修复问题、改进易用性，并根据社区反馈持续更新。欢迎通过 Issue 提出建议或提交 Pull Request 参与贡献。

## 未来规划：AI 与智能 GIS 工作流

在不泄露用户隐私和密钥的前提下，计划逐步引入基于大语言模型的智能能力，帮助更多非专业开发者高效完成空间数据分析工作，包括但不限于：

* 智能 POI 分类与标签补全（如按业态、功能区等自动归类）
* 地理实体归一化与去重，提高多来源数据融合质量
* 自动化空间数据质量评估与异常检测
* 基于自然语言的查询与工作流指导（例如：“帮我查询并导出某城市商圈附近的咖啡店”）
* 面向新贡献者的智能文档问答与上手引导

如果你对这些方向感兴趣，欢迎在 Issue 中交流或参与实现。

## Project Overview (English)

`baidu_poi_search` is an open-source geospatial query tool that provides a graphical interface for querying, visualizing, and exporting Point-of-Interest (POI) data from Baidu Maps.

The project has been adopted by researchers, GIS practitioners, students, and industry users as part of broader geospatial data workflows, such as urban studies, location intelligence, and business site selection. The repository is actively maintained by the primary maintainer (@soaringsoul), who reviews community feedback, fixes issues, and improves usability.

With future integration of AI/LLM-based features – including intelligent POI categorization and enrichment, geographic entity normalization and deduplication, automated spatial data quality assessment, natural-language querying, and AI-assisted documentation – the project aims to make spatial data analysis more accessible to a wider audience and to strengthen the open-source ecosystem around spatial data tools.

## 联系我

如果在使用过程中遇到无法解决的问题，你可以通过关注我的个人公众号找到我。

另外，也可以通过提交issue的方式提交问题。

![rewnwen_wechat](./images/rewnwen_wechat.png)




