# Contributing to baidu_poi_search

_English follows Chinese. English version below._

---

## 贡献指南（中文）

感谢你对 `baidu_poi_search` 的关注和支持！这是一个面向地理空间数据查询与教学场景的开源项目，欢迎任何形式的贡献。

### 适合的贡献方式

- **提交 Issue**  
  - 报告 Bug 或意外行为
  - 提出新功能 / 新场景建议
  - 改进文档、教程或示例
- **提交 Pull Request**  
  - 修复 Bug
  - 改进界面与用户体验
  - 增强数据导出、清洗与分析能力
  - 为未来的 AI/LLM 能力做准备（如添加数据字段、结构化元数据等）

### 开发环境准备

- 操作系统：推荐 Windows 10（与当前 GUI 体验保持一致）
- Python 版本：3.5 或 3.6+（建议使用虚拟环境 virtualenv 或 venv）
- 安装依赖：

```bash
pip install -r requirements.txt
```

如需修改界面逻辑或数据处理流程，建议先在本地以小规模数据进行测试。

### 提交代码前的检查

- 确保主要功能能够在本地正常运行（启动 GUI、完成一次 POI 查询并导出结果）。
- 如修改较多逻辑，请在 PR 描述中说明：
  - 修改目的
  - 关键变更点
  - 已经手动测试过的场景
- 避免提交包含个人密钥（如 Baidu AK）、临时数据或大型二进制文件。

### 与维护者沟通

本项目目前由 **@soaringsoul** 作为主要维护者：

- 推荐在 GitHub Issue 中讨论需求与设计方案；
- 也可以通过 README 中的公众号二维码与作者取得联系；
- 欢迎任何关于教学使用、科研使用或生产部署的经验分享。

---

## Contributing Guide (English)

Thank you for your interest in contributing to `baidu_poi_search`!  
This project focuses on geospatial Point-of-Interest (POI) querying and is widely used in teaching, research, and small-to-medium scale data workflows.

### How you can contribute

- **Open Issues**
  - Report bugs or unexpected behavior
  - Propose new features or usage scenarios
  - Suggest improvements to documentation, tutorials, or examples
- **Submit Pull Requests**
  - Fix bugs
  - Improve the GUI and user experience
  - Enhance data export, cleaning, and analysis capabilities
  - Prepare the codebase for future AI/LLM-powered features (e.g., richer schemas or metadata)

### Setting up a development environment

- OS: Windows 10 is recommended (to match the current GUI workflow)
- Python: 3.5 or 3.6+ (virtualenv or venv is recommended)
- Install dependencies:

```bash
pip install -r requirements.txt
```

Before sending a PR, please make sure that:

- The application can be launched successfully.
- At least one end-to-end flow (search POI + export to Excel) works on your machine.
- Your PR description clearly explains:
  - Why the change is needed
  - What has been modified
  - What you have tested

### Maintainer & communication

The repository is primarily maintained by **@soaringsoul**.

- For technical discussions, please use GitHub Issues or PR comments.
- You can also contact the maintainer via the WeChat public account shown in the README.
- Contributions from universities, researchers, and industry users are all welcome.

By participating in this project, you help make geospatial analysis and POI querying more accessible to a wider community.
