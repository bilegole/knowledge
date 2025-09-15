# 快速开始

本指南将帮助你在本地预览与构建本 Wiki。你也可以从 [首页](../index.md) 进入浏览内容。

## 安装依赖

- 需要 Python 3.8+。
- 安装 MkDocs 与主题：

```powershell
pip install mkdocs mkdocs-material
```

## 本地预览

在仓库根目录执行：

```powershell
mkdocs serve
```

然后打开浏览器访问 http://127.0.0.1:8000/。

## 构建静态站点

在仓库根目录执行：

```powershell
mkdocs build
```

生成的静态网站位于 `site/` 目录。将该目录内容部署至任意静态托管（如 GitHub Pages、Netlify 等）即可对外提供访问。

## 组织内容

- 所有 Markdown 文档放在 `docs/` 目录下；
- 需要出现在导航中的页面，在 `mkdocs.yml` 的 `nav` 中配置；
- 静态资源（图片、附件）建议放置在 `docs/assets/` 下，并使用相对路径引用。

更多建议与说明可查看项目 [README](../../README.md)。

## 常见问题

- 如果 `mkdocs` 命令无法识别，请确认 Python 的 Scripts 目录已加入 PATH，或者使用 `python -m mkdocs serve` 运行。
- 新人常见问题汇总见：[新人 FAQ](faq.md)。
- 不熟悉的缩写与名词见：[术语表](terminology.md)。
