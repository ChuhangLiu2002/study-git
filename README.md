# study-git

这是一个用于学习和练习 Git 操作的仓库 📚

## 仓库作用

- 熟悉 Git 基础命令 🧩
- 练习文件的添加、提交和版本管理 ✍️
- 学习将本地代码推送到 GitHub ☁️
- 记录 Git 学习过程中的示例代码和笔记 🚀

## 常用操作

```bash
git status
git add .
git commit -m "描述本次修改"
git push
```

持续练习，逐步掌握 Git 工作流程 💪

## 常规 Git 操作

| 命令 | 作用 |
| --- | --- |
| `git init` | 初始化本地 Git 仓库 |
| `git clone <地址>` | 克隆远程仓库 |
| `git status` | 查看文件状态 |
| `git add <文件>` | 将文件加入暂存区 |
| `git add .` | 将所有修改加入暂存区 |
| `git commit -m "说明"` | 提交暂存区内容 |
| `git log` | 查看提交历史 |
| `git diff` | 查看文件修改内容 |
| `git branch` | 查看本地分支 |
| `git branch <分支名>` | 创建新分支 |
| `git switch <分支名>` | 切换分支 |
| `git switch -c <分支名>` | 创建并切换到新分支 |
| `git merge <分支名>` | 合并指定分支 |
| `git remote -v` | 查看远程仓库地址 |
| `git remote add origin <地址>` | 添加远程仓库 |
| `git fetch` | 获取远程更新，但不合并 |
| `git pull` | 获取并合并远程更新 |
| `git push` | 推送本地提交到远程仓库 |
| `git stash` | 临时保存当前修改 |
| `git stash pop` | 恢复临时保存的修改 |
| `git restore <文件>` | 撤销工作区修改 |
| `git revert <提交 ID>` | 创建新提交来撤销指定提交 |
| `git tag <标签名>` | 创建版本标签 |

## 日常工作流

```bash
git status                  # 查看当前状态
git add .                   # 添加所有修改
git commit -m "更新代码"     # 提交修改
git pull                    # 获取远程最新代码
git push                    # 推送本地提交
```

注意：`git reset` 可能会丢失提交或修改，使用前请确认目标 ⚠️