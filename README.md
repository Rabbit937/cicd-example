# cicd-example

一个示例项目，演示如何使用 GitHub Actions 进行 CI/CD。

## 项目结构

- `main.py`: 主程序文件
- `test_main.py`: 测试文件
- `pyproject.toml`: 项目配置和依赖

## GitHub Actions 工作流

在 `.github/workflows/test.yml` 中定义了 CI 工作流，包括：

1. 在多个 Python 版本 (3.10, 3.11, 3.12) 上运行测试
2. 代码质量检查 (linting 和 formatting)

工作流会在每次推送到 main 分支或创建 pull request 时触发。

## 如何运行测试

```bash
# 安装依赖 (使用 uv)
uv sync

# 运行测试
uv run pytest
```