# todo-cli_14

一个简洁、轻量的命令行待办事项（Todo）管理工具，使用 Python 编写，数据以 JSON 格式本地保存。

> 本项目为《开源文化运动》课程期末考核项目，项目名称后缀 `_14` 为学号后两位。

## 功能特性

- ✅ 添加待办事项，支持设置优先级（高 / 普通 / 低）
- 📋 列出所有待办事项，显示完成状态
- ✔️ 标记事项为已完成
- 🗑️ 删除指定事项
- 🧹 一键清空所有事项
- 💾 数据本地持久化（JSON）

## 环境要求

- Python 3.6 及以上版本

## 安装与使用

```bash
# 克隆仓库
git clone https://github.com/你的用户名/todo-cli_14.git
cd todo-cli_14

# 添加待办
python todo.py add "完成实验报告" 高

# 查看所有待办
python todo.py list

# 标记完成
python todo.py done 1

# 删除事项
python todo.py delete 1

# 清空
python todo.py clear
```

## 项目结构

```
todo-cli_14/
├── todo.py        # 主程序
├── todos.json     # 数据文件（运行后自动生成）
├── README.md      # 项目说明文档
├── LICENSE        # 开源许可证
└── .gitignore     # Git 忽略规则
```

## 分支管理

本项目遵循简单的 Git Flow 思想进行分支管理：

- `main`：主分支，保持稳定可发布
- `dev`：开发主分支
- `feature/*`：功能分支，如 `feature/add-priority`
- `fix/*`：缺陷修复分支，如 `fix/typo-in-readme`

开发流程：从 `dev` 切出 `feature` 分支 → 开发并提交 → 合并回 `dev` → 测试通过后合并到 `main`。

## 贡献指南

欢迎 Issue 与 Pull Request！

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交改动：`git commit -m "Add your feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 发起 Pull Request

## 许可证

本项目采用 [MIT License](LICENSE) 开源协议，详见 [LICENSE](LICENSE) 文件。

## 作者

周依诺  学号：2025131014
