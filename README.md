# Rebuild-n8n

> 🛠️ 一个基于 [n8n](https://n8n.io/) 的定制与重构版本。

![License](https://img.shields.io/github/license/AliverAnme/Rebuild-n8n)
![Languages](https://img.shields.io/github/languages/top/AliverAnme/Rebuild-n8n)
![Last Commit](https://img.shields.io/github/last-commit/AliverAnme/Rebuild-n8n)

---
## 使用

添加环境变量指明`N8N_DEFAULT_LOCALE=zh`

注：2.7.3可用AiBuilder

## 📌 简介

本项目在保留 n8n 核心能力的基础上，进行了以下改进：
✅ 中文化支持
⚠️ 本项目目前处于活跃开发阶段，尚未发布稳定版本。欢迎贡献！

## 🗂 目录结构

```
Rebuild-n8n/
├── .github/workflows/ # CI/CD 工作流
├── locales/ # 多语言资源（含简体中文）
├── patches/ # 对原版 n8n 的补丁文件
├── scripts/ # 构建与部署脚本
├── package.json # Node.js 依赖与脚本入口
├── LICENSE # MIT 许可证
└── README.md
```

## 🚀 快速开始

1. fork 本仓库

2. 自行设定仓库secrets

- GHCR_TOKEN, 需要仓库的读写权限
- OPENAI_API_KEY

3. 设定vars

- OPENAI_API_BASE
- OPENAI_API_CONCURRENT不设置默认为 2，请勿设置过高
- OPENAI_MODEL

4. 手动触发（支持自选 tag）或者等待自动运行，action 会将镜像推送到仓库拥有者的 ghcr 上，请自行调整可见性，并修改 docker 运行配置指向自己的 ghcr 镜像

本项目通过 locales/ 目录提供多语言支持。默认语言为简体中文（zh-CN）

可以自行添加 patch 到 patch 目录下

## 📄 许可证

本项目基于 MIT License 开源。
版权所有 (c) 2025 AliverAnme
详见 [LICENSE](./LICENSE) 文件。

🙏 致谢
感谢 [n8n 官方团队](https://n8n.io/) 
