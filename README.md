# 我的应用 (my-app)

基于 Streamlit 的 AI 应用项目。

## 项目简介

这是一个使用 Streamlit 框架开发的 Web 应用，主要功能是加载和运行 AI 智能代理。

## 技术栈

- **Streamlit** - Web 应用框架
- **Python** - 编程语言
- **AI Agent** - 智能代理功能

## 项目结构

```
my-app/
├── .devcontainer/          # 开发容器配置
│   └── devcontainer.json
├── .env                    # 环境变量配置
├── .vscode/                # VS Code 配置
│   └── settings.json
└── app/
    ├── 2.py                # 主应用程序（包含 AI Agent 加载逻辑）
    └── requirements.txt    # 项目依赖
```

## 快速开始

### 环境要求

- Python 3.8+

### 安装依赖

```bash
cd app
pip install -r requirements.txt
```

### 运行应用

```bash
streamlit run app/2.py
```

或

```bash
cd app
streamlit run 2.py
```

应用将在浏览器中打开，通常访问地址为 `http://localhost:8501`。

## 配置说明

### 环境变量

在 `.env` 文件中配置必要的环境变量，具体内容根据 AI Agent 的需求进行设置。

### 开发容器

项目包含 `.devcontainer` 配置，支持使用 VS Code 的 Remote - Containers 插件进行容器化开发。

## 依赖说明

主要依赖见 `app/requirements.txt`，包括：
- streamlit
- 其他 AI 相关依赖（根据实际需求）

## 许可证

请查看项目根目录下的 LICENSE 文件了解具体的许可证信息。

## 作者

luoyong0129

---

如有问题或建议，欢迎提交 Issue 或 Pull Request。
