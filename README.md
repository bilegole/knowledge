# EVE Knowledge Wiki

这是一个使用 Markdown 的 Wiki 项目骨架，基于 MkDocs 组织与预览。

## 快速开始

1. 安装 MkDocs（需要 Python 3.8+）
   - Windows PowerShell：
     - 如果未安装 Python，请先安装 https://www.python.org/downloads/
     - 安装 MkDocs：
       ```powershell
       pip3 install mkdocs mkdocs-material
       ```
2. 本地预览
   ```powershell
   mkdocs serve
   ```
   打开浏览器访问 http://127.0.0.1:8000/ 即可实时预览。

3. 生成静态站点
   ```powershell
   mkdocs build
   ```
   生成的静态文件位于 `site/` 目录，可部署到任意静态托管。

## 目录结构

```
.
├─ docs/                  # Markdown 文档存放处
│  ├─ index.md            # 首页（Wiki 入口）
│  └─ guide/
│     └─ getting-started.md
├─ mkdocs.yml             # MkDocs 配置
└─ .gitignore             # 忽略构建产物
```

## 内容约定

- 所有内容使用 Markdown（.md）编写。
- 建议使用相对路径引用图片，例如：`![](assets/img/xxx.png)`，并将资源放入 `docs/assets/`。
- 导航在 `mkdocs.yml` 的 `nav` 中配置。

## 发布建议

- GitHub Pages：
  - 在仓库 Settings → Pages 选择 `GitHub Actions`，并使用 MkDocs 官方模板工作流；
  - 或者将 `site/` 上传到任意静态站点。

## 协作

- 新建页面：在 `docs/` 下创建新的 `.md` 文件，并在 `mkdocs.yml` 的 `nav` 添加到导航。
- 约定 PR 模板：页面开头建议包含一级标题与简要说明。

Happy writing!