# baidu_poi_search Roadmap

_English follows Chinese. English version below._

---

## 路线图（中文）

本路线图用于概述 `baidu_poi_search` 的演进方向，帮助使用者与贡献者理解项目未来的发展重点。时间节点为参考，实际进度会根据社区反馈和维护者时间适当调整。

### 1. 近期开发计划（0–6 个月）

- **稳定性与易用性**
  - 在更多 Python 3.x 版本和 Windows 版本上测试与验证
  - 改进错误提示与异常处理，减少查询过程中“黑盒”行为
  - 补充 README 中的常见问题（FAQ）与典型工作流示例
- **数据导出与清洗能力增强**
  - 优化导出 Excel 的字段与格式，使其更易于后续在 GIS 软件或 pandas 中处理
  - 增加可选字段（如分类标签、行政区划等），为后续 AI 处理打基础
- **教学与示例项目**
  - 增加面向高校课程和培训班的“实验手册级”示例（如城市 POI 分布分析案例）

### 2. 中期规划：面向 AI/LLM 的能力建设（6–18 个月）

在获取稳定的 API 额度（如 OpenAI API Credits）后，计划探索以下能力：

- **智能 POI 分类与标签补全**  
  将原始查询得到的 POI 描述（名称、地址、类别等）输入到大模型中，自动生成更加一致、细粒度的业态或功能标签，降低人工标注成本。

- **地理实体归一化与去重**  
  通过模型理解相近文本和地址描述，对多次查询或多数据源的 POI 进行合并与去重，提升数据质量，便于后续分析与可视化。

- **自动化空间数据质量评估**  
  利用模型识别缺失字段、异常坐标、疑似脏数据，并生成自然语言的质量报告与修正建议。

- **自然语言查询与工作流指导**  
  用户可以通过中文自然语言描述任务（例如：“帮我查询并导出广州天河区商场附近 1 公里范围内的咖啡店”），由系统将其翻译为具体的查询参数和操作步骤，降低使用门槛。

- **文档问答与新贡献者 Onboarding**  
  将 README、示例代码和 Issue 历史与大模型结合，提供问答式的上手指导，帮助新贡献者快速理解代码结构与开发流程。

### 3. 远期构想（18 个月以后）

- 与其他开源 GIS 工具（如 QGIS、geopandas 等）形成更紧密的工作流衔接
- 提供可选的 Web 前端或命令行界面，让不方便运行桌面 GUI 的用户也能使用
- 探索与更多地图 / POI 数据源的集成（在遵守各平台条款的前提下）

---

## Roadmap (English)

This roadmap outlines the future direction of `baidu_poi_search` and how it plans to better serve the open-source GIS and geospatial communities.

### 1. Short-term (0–6 months)

- **Stability & usability**
  - Test and validate the tool on more Python 3.x versions and Windows environments
  - Improve error handling and user-facing messages
  - Extend documentation with FAQs and step-by-step usage examples
- **Better export & cleaning capabilities**
  - Refine Excel export schemas to be more GIS/pandas friendly
  - Add optional fields (e.g., categories, administrative codes) to prepare for downstream AI processing
- **Teaching-oriented materials**
  - Provide example notebooks and case studies for university courses and trainings

### 2. Mid-term: AI/LLM-powered features (6–18 months)

When stable API credits (e.g., OpenAI API credits) are available, the project plans to experiment with:

- **Intelligent POI categorization & enrichment**  
  Use LLMs to normalize and enrich POI records with consistent, fine-grained business or functional categories.

- **Geographic entity normalization & deduplication**  
  Automatically merge and deduplicate POIs queried from multiple runs or sources by understanding textual similarity and spatial context.

- **Automated spatial data quality assessment**  
  Detect missing fields, suspicious coordinates, and potential outliers, and generate natural-language quality reports and cleaning suggestions.

- **Natural-language querying & workflow guidance**  
  Allow users to describe tasks in natural language (e.g., “query and export coffee shops within 1km of major malls in Tianhe, Guangzhou”) and have the system translate them into concrete parameters and operations.

- **AI-assisted documentation & onboarding**  
  Provide Q&A-style documentation and contributor onboarding by combining project docs, examples, and issue history with LLM-powered assistants.

### 3. Long-term (18+ months)

- Tighter integration with other open-source GIS tools (e.g., QGIS, geopandas)
- Optional web or CLI interfaces for users who cannot run the desktop GUI
- Potential support for additional map/POI providers (while respecting their terms of service)

---

This roadmap is intentionally flexible and will be updated based on community feedback and the maintainer's capacity.  
Suggestions and contributions are always welcome via GitHub Issues and Pull Requests.
