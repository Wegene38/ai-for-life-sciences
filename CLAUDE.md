# 维护手册：每日自动更新

本仓库属于 GitHub 用户 **Wegene38**，每天北京时间早上由 Claude Code 定时任务写一篇新的学习笔记。本文件是每日更新的操作手册，请严格按流程执行。人类读者看 [README.md](README.md) 即可。

## 基本约定

| 项目 | 约定 |
|---|---|
| 读者 | 计算生物学背景、想系统学习 AI 的研究者（会编程和生物，不一定熟悉深度学习） |
| 语言 | 简体中文；术语第一次出现时附英文，如“注意力机制（attention）”；代码注释可用中文，图表标签用英文（Colab 默认没有中文字体） |
| 时区 | Asia/Shanghai。今天的日期：`TZ=Asia/Shanghai date +%F`；星期：`TZ=Asia/Shanghai date +%u`（1 = 周一） |
| 提交作者 | `Wegene38 <338052809+Wegene38@users.noreply.github.com>`，用 `git commit --author=...` 指定 |
| 分支 | 直接提交到 `main` |
| 文件命名 | 笔记放在 `daily/YYYY-MM/dayNNN-YYYY-MM-DD.md`，NNN 是三位 Day 编号（Day 1000 起用四位） |

## 每日流程

### 1. 同步与幂等检查

```bash
git pull --rebase origin main
TODAY=$(TZ=Asia/Shanghai date +%F)
ls daily/*/day*-"$TODAY".md 2>/dev/null
```

如果已经有今天日期的笔记，说明今天已经更新过：**不要再写新笔记**，汇报“今天已更新”后结束。

### 2. 确定今天的课

- 在 [SYLLABUS.md](SYLLABUS.md) 中找到第一个“笔记”列为 ⏳ 的行：`grep -nE '^\| [0-9]{3,4} \|.*⏳' SYLLABUS.md | head -1`（只匹配表格行）。这一行给出 Day 编号、主题、学习要点与资源，所在小节标题给出阶段和周次。
- 如果 Day 编号是 7 的倍数，这是“周复盘”日，按下文“周复盘日的写法”来写。
- 如果没有 ⏳ 行，说明进入了阶段 6，按下文“阶段 6：持续进阶”先排课，再写笔记。

### 3. 调研与核实（必须做）

- **先查本仓库**：优先使用 [resources/](resources/README.md) 中已核实的资源，并精确到章节、视频集数或 Notebook。
- **外部链接要核实**：用 WebSearch 确认每个要引用的链接仍然存在、免费、内容正确。GitHub 仓库可以这样验证（返回 200 即存在）：
  ```bash
  curl -s -o /dev/null -w '%{http_code}\n' https://raw.githubusercontent.com/<owner>/<repo>/HEAD/README.md
  ```
- **网络限制**：本运行环境只放行少数域名（GitHub、PyPI 等），WebFetch 打不开大多数网站，这**不代表**链接失效，不要因此删改链接。WebSearch 可以正常使用。
- **今日前沿**：找 1–3 条最近 14 天内、与今天主题相关或在本领域很重要的新进展（论文、模型、数据集、课程、竞赛）。每条都要有可靠来源（官方博客、论文页、期刊、GitHub）。找不到可靠来源就写“今日无”，宁缺毋滥。

### 4. 写笔记

复制 [daily/TEMPLATE.md](daily/TEMPLATE.md) 到 `daily/YYYY-MM/dayNNN-YYYY-MM-DD.md`，保留模板中的所有 `##` 小节标题（校验脚本会检查）。质量要求：

- **核心概念**：800–1500 字，用自己的话讲清楚“是什么、为什么、怎么用、局限是什么”；可以用公式（`$...$`）、表格或 mermaid 图。结合生物学例子讲，不要只讲通用 AI 知识。
- **今日资源**：2–4 个，精确到章节 / 视频 / Notebook，每个给出建议时长；平日总时长约 1.5 小时，周复盘约 2–3 小时。
- **动手练习**：给出可运行的 Python 代码（Colab 优先）或明确的操作步骤，附期望输出，最后加一个“进阶”小任务。代码要尽量在本环境实际跑一遍：PyPI 可以访问，能 `pip install`；数据下载通常会被网络拦截，可以用合成数据或 mock 测试代码逻辑。
- **自测题**：3–5 道，答案放在 `<details>` 里。
- **准确性**：不得编造论文、作者、数字、链接。引用论文写“第一作者 et al. 年份，期刊或预印本”并附链接；拿不准就不写。
- **版权**：用自己的话总结，不要大段复制原文。
- 导航行：“上一篇”链接到前一天的笔记，路径统一写成 `../YYYY-MM/dayNNN-YYYY-MM-DD.md`；“下一篇”写 `下一篇：（明天更新）`。

### 5. 更新索引（每一项都要做）

1. **SYLLABUS.md**：把今天那一行的 `⏳` 换成 `[✅](daily/YYYY-MM/dayNNN-YYYY-MM-DD.md)`。
2. **前一篇笔记**：把 `下一篇：（明天更新）` 换成 `下一篇：[Day NNN](../YYYY-MM/dayNNN-YYYY-MM-DD.md)`。
3. **daily/README.md**：在对应月份表格的第一行插入今天的记录（日期 | Day 链接 | 阶段 | 主题）。新的月份就在页面最上方（第一个月份小节之前）新建“## YYYY 年 M 月”小节和表头。
4. **README.md**：
   - `<!-- LATEST:START -->` 与 `<!-- LATEST:END -->` 之间：把今天的记录插到表格第一行，最多保留 7 行。
   - `<!-- PROGRESS:START -->` 区块：两个徽章（笔记数 `daily%20notes-N`；日期 `updated-YYYY--MM--DD`，注意日期中的横线要写两个），以及“已更新 **N** 天 · 核心课程进度 min(N,182) / 182 · 当前阶段”。
5. **frontier/YYYY-MM.md**：把今日前沿条目追加到“每日条目”表格末尾（“今日无”则跳过）。新的月份就新建文件（参照已有月份文件的格式），并在 [frontier/README.md](frontier/README.md) 的月度表格第一行加入链接。

### 6. 校验

```bash
python3 scripts/validate.py
```

必须输出“✅ 校验通过”。不通过就按提示修好，再跑一遍。

### 7. 每周维护（只在周复盘日做）

- 浏览本周主题对应的 `resources/*.md`，补充确实有价值、已核实的新免费资源，标注 🆕；发现失效链接（WebSearch 也找不到，或 GitHub 返回 404）就修正或删除。
- 在 [CHANGELOG.md](CHANGELOG.md) 顶部记一条。

### 8. 提交与推送

```bash
git add -A
git commit --author="Wegene38 <338052809+Wegene38@users.noreply.github.com>" -m "docs(daily): Day NNN · 主题"
git push origin main
```

- 网络错误时按 2、4、8、16 秒间隔重试，最多 4 次。
- 如果因为远端有新提交被拒绝，先 `git pull --rebase origin main`，重新校验，再推送。
- 推送成功后用 2–3 句话汇报：Day 编号与主题、文件路径、今日前沿条数、是否有异常。

## 周复盘日的写法

Day 编号为 7 的倍数时，仍用同一模板，内容侧重如下：

- **核心概念**：本周知识地图——用要点回顾本周 6 天的内容，每点链接回当天笔记，并指出这些知识之间的联系。
- **动手练习**：本周小项目（见 [projects/README.md](projects/README.md)）：目标、数据、分步骤指引、评估方式、参考实现思路。
- **自测题**：从本周 6 篇笔记中挑 5 道最重要的题重做，再加 1 道综合题。

## 阶段 6：持续进阶（Day 183 起）

当 SYLLABUS.md 中没有 ⏳ 行时：

1. 在 SYLLABUS.md 末尾“阶段 6”表格中，追加接下来 7 天的计划（Day 编号接着往下排，“笔记”列为 ⏳）。按星期轮换主题：周一 基因组 / RNA，周二 蛋白质结构与设计，周三 小分子与药物，周四 单细胞与多组学，周五 影像与多模态，周六 LLM / 智能体 / 方法论，周日 本周前沿汇总与复盘。
2. 每天的主题是“精读一篇近 3 个月内的重要论文”或“上手一个新工具”，选题前用 WebSearch 核实。
3. 笔记照常使用模板；阶段写“阶段 6「持续进阶」”；核心课程进度保持 182 / 182。

## 禁止事项

- 不要删除文件，不要 `git push --force`，不要改写 git 历史。
- 不要改动历史笔记的主体内容。发现明显错误可以修正，但要在 CHANGELOG.md 记录。
- 不要收录必须付费才能学习的资源（免费旁听、免费注册的可以收录，但要注明）。
- 不要在仓库中写入任何密钥、私人邮箱或其他隐私信息。
- 不要修改本文件和 scripts/validate.py，除非流程本身有问题；修改时要在 CHANGELOG.md 说明原因。
