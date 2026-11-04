# 更新日志

每日笔记的更新记录见 git 历史和 [daily/README.md](daily/README.md)。这里记录资源库、路线和维护流程的变化。

## 2026-11-05

- 修正 [CLAUDE.md](CLAUDE.md) 第 2 步查找下一课的命令：原来的 `grep '⏳'` 会先匹配到课程表开头说明文字里的 ⏳，现在只匹配表格行。

## 2026-11-04

- 建库：26 周学习路线（[ROADMAP.md](ROADMAP.md)）、182 天逐日课程表（[SYLLABUS.md](SYLLABUS.md)）、14 个分类资源文件（[resources/](resources/README.md)）、实战项目清单（[projects/](projects/README.md)）、前沿速递（[frontier/](frontier/README.md)）。
- 资源核实：所有 GitHub 仓库链接都确认存在；其他链接通过网络搜索交叉核实。
- 发布 [Day 001](daily/2026-11/day001-2026-11-04.md)；开启每日自动更新（北京时间早上），流程见 [CLAUDE.md](CLAUDE.md)，校验脚本见 [scripts/validate.py](scripts/validate.py)。
