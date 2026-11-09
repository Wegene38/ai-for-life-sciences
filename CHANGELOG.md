# 更新日志

每日笔记的更新记录见 git 历史和 [daily/README.md](daily/README.md)。这里记录资源库、路线和维护流程的变化。

## 2026-11-10

- 第 1 周资源维护：
  - [01 编程与数学基础](resources/01-programming-math.md)：补充 Missing Semester 2026 新版、《Pro Git》中文版、The Linux Command Line，以及两篇 Ten Simple Rules（用好 Git 与 GitHub、生物学家学编程）。
  - [12 工具与算力](resources/12-tools-compute.md)：补充 Bioconda、nbstripout、Jupytext、GitHub CLI、清华 TUNA 镜像，以及 Anaconda `defaults` 频道的条款说明。
  - [13 前沿追踪与社区](resources/13-frontier-community.md)：新增“读论文与学习方法”小节。
  - [06 蛋白质](resources/06-proteins.md)：新增 RFD4-Proteina，以及 AlphaFold DB API 文档和 v6 接口变更提示。
  - [07 小分子与药物发现](resources/07-drug-discovery.md)：新增 CheMeleon。
- AlphaFold DB 已升级到 v6，接口中 `entryId` 改名为 `modelEntityId`、不再提供 PAE 图片；Day 001 与 Day 007 的代码使用的 `pdbUrl` 字段仍然存在。

## 2026-11-05

- 修正 [CLAUDE.md](CLAUDE.md) 第 2 步查找下一课的命令：原来的 `grep '⏳'` 会先匹配到课程表开头说明文字里的 ⏳，现在只匹配表格行。

## 2026-11-04

- 建库：26 周学习路线（[ROADMAP.md](ROADMAP.md)）、182 天逐日课程表（[SYLLABUS.md](SYLLABUS.md)）、14 个分类资源文件（[resources/](resources/README.md)）、实战项目清单（[projects/](projects/README.md)）、前沿速递（[frontier/](frontier/README.md)）。
- 资源核实：所有 GitHub 仓库链接都确认存在；其他链接通过网络搜索交叉核实。
- 发布 [Day 001](daily/2026-11/day001-2026-11-04.md)；开启每日自动更新（北京时间早上），流程见 [CLAUDE.md](CLAUDE.md)，校验脚本见 [scripts/validate.py](scripts/validate.py)。
