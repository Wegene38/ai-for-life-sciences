#!/usr/bin/env python3
"""仓库结构校验。每天更新后运行：python3 scripts/validate.py，退出码为 0 才能提交。

检查项：
1. 所有 Markdown 里的相对链接都指向存在的文件；
2. 每日笔记的文件名、目录、标题和必需小节；
3. SYLLABUS.md 中已完成的 Day 与笔记文件一一对应，并且按顺序完成；
4. daily/README.md 收录了所有笔记；
5. README.md 的“最新笔记”、进度数字和徽章与实际一致；
6. 只有最新一篇笔记可以保留“下一篇：（明天更新）”。

只用标准库，不需要安装依赖。
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
NOTE_RE = re.compile(r"^day(\d{3,4})-(\d{4})-(\d{2})-(\d{2})\.md$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REQUIRED_SECTIONS = ["今日目标", "核心概念", "今日资源", "动手练习", "自测题", "今日前沿", "学习打卡"]
SKIP_LINK_CHECK = {"daily/TEMPLATE.md"}
PENDING_NEXT = "下一篇：（明天更新）"

errors = []


def err(msg):
    errors.append(msg)


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" not in p.parts:
            yield p


def strip_code(text):
    """去掉代码块和行内代码，避免把代码里的方括号当成链接。"""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check_links():
    for p in md_files():
        rel = p.relative_to(ROOT).as_posix()
        if rel in SKIP_LINK_CHECK:
            continue
        for target in LINK_RE.findall(strip_code(p.read_text(encoding="utf-8"))):
            if target.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # 页内锚点或外部链接（http、https、mailto）
            path = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if path and not (p.parent / path).exists():
                err(f"{rel}: 相对链接指向不存在的文件 -> {target}")


def collect_notes():
    notes = {}
    for p in sorted((ROOT / "daily").glob("*/*.md")):
        rel = p.relative_to(ROOT).as_posix()
        m = NOTE_RE.match(p.name)
        if not m:
            err(f"{rel}: 文件名应为 dayNNN-YYYY-MM-DD.md")
            continue
        day, y, mo, d = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        if p.parent.name != f"{y}-{mo}":
            err(f"{rel}: 应放在 daily/{y}-{mo}/ 目录下")
        if day in notes:
            err(f"Day {day:03d} 有两篇笔记：{notes[day]['rel']} 和 {rel}")
        notes[day] = {"path": p, "rel": rel, "date": f"{y}-{mo}-{d}"}
    return notes


def check_notes(notes):
    days = sorted(notes)
    if days and days != list(range(1, days[-1] + 1)):
        missing = sorted(set(range(1, days[-1] + 1)) - set(days))
        err(f"每日笔记编号不连续，缺少 Day：{missing}")
    dates = [notes[d]["date"] for d in days]
    if dates != sorted(dates) or len(set(dates)) != len(dates):
        err("笔记日期必须随 Day 编号严格递增（每天最多一篇）")
    for day in days:
        info = notes[day]
        text = info["path"].read_text(encoding="utf-8")
        lines = text.strip().splitlines()
        if not lines or not lines[0].startswith(f"# Day {day:03d}"):
            err(f"{info['rel']}: 第一行应以「# Day {day:03d}」开头")
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        for sec in REQUIRED_SECTIONS:
            if not any(sec in h for h in headings):
                err(f"{info['rel']}: 缺少小节「{sec}」")
        if day != days[-1] and PENDING_NEXT in text:
            err(f"{info['rel']}: 已有更新的笔记，“下一篇”应改成指向 Day {day + 1:03d} 的链接")


def check_syllabus(notes):
    rows = []
    for line in (ROOT / "SYLLABUS.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d{3,4})\s*\|(.*)\|\s*$", line)
        if m:
            rows.append((int(m.group(1)), m.group(2).split("|")[-1].strip()))
    nums = [d for d, _ in rows]
    if nums != sorted(set(nums)):
        err("SYLLABUS.md: Day 编号必须唯一且递增")
    done, seen_pending = set(), False
    for day, cell in rows:
        link = re.search(r"\]\((daily/[^)]+)\)", cell)
        if link:
            if seen_pending:
                err(f"SYLLABUS.md: Day {day:03d} 已完成，但前面还有未完成的 Day（必须按顺序更新）")
            done.add(day)
            if day not in notes:
                err(f"SYLLABUS.md: Day {day:03d} 标记为已完成，但找不到对应笔记")
            elif notes[day]["rel"] != link.group(1):
                err(f"SYLLABUS.md: Day {day:03d} 的链接应为 {notes[day]['rel']}")
        elif "⏳" in cell:
            seen_pending = True
        else:
            err(f"SYLLABUS.md: Day {day:03d} 的“笔记”列应为 ⏳ 或 [✅](daily/...)")
    unmarked = sorted(set(notes) - done)
    if unmarked:
        err(f"SYLLABUS.md: 这些 Day 已有笔记，但课程表中没有标记完成：{unmarked}")


def check_indexes(notes):
    index = (ROOT / "daily" / "README.md").read_text(encoding="utf-8")
    for info in notes.values():
        rel_from_daily = info["rel"].removeprefix("daily/")
        if f"]({rel_from_daily})" not in index:
            err(f"daily/README.md: 没有收录 {info['rel']}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    latest = re.search(r"<!-- LATEST:START -->(.*?)<!-- LATEST:END -->", readme, re.S)
    progress = re.search(r"<!-- PROGRESS:START -->(.*?)<!-- PROGRESS:END -->", readme, re.S)
    if not latest or not progress:
        err("README.md: 缺少 LATEST 或 PROGRESS 标记区块")
        return
    if notes:
        newest = notes[max(notes)]
        if f"]({newest['rel']})" not in latest.group(1):
            err(f"README.md: “最新笔记”里没有最新一篇 {newest['rel']}")
        rows = [line for line in latest.group(1).splitlines() if re.match(r"^\|\s*\d{4}-\d{2}-\d{2}", line)]
        if len(rows) > 7:
            err("README.md: “最新笔记”最多保留 7 行")
        date_badge = re.search(r"updated-(\d{4})--(\d{2})--(\d{2})", progress.group(1))
        if not date_badge or "-".join(date_badge.groups()) != newest["date"]:
            err(f"README.md: 更新日期徽章应为 {newest['date']}（写法：updated-{newest['date'].replace('-', '--')}）")
    count = len(notes)
    bold = re.findall(r"\*\*(\d+)\*\*", progress.group(1))
    if not bold or int(bold[0]) != count:
        err(f"README.md: 进度区块里第一个加粗数字应为已更新天数 **{count}**")
    count_badge = re.search(r"daily%20notes-(\d+)", progress.group(1))
    if not count_badge or int(count_badge.group(1)) != count:
        err(f"README.md: 笔记数徽章应为 daily%20notes-{count}")


def main():
    check_links()
    notes = collect_notes()
    check_notes(notes)
    check_syllabus(notes)
    check_indexes(notes)
    if errors:
        print(f"❌ 校验失败，共 {len(errors)} 个问题：")
        for e in errors:
            print("  -", e)
        return 1
    print(f"✅ 校验通过：{len(notes)} 篇每日笔记，课程表、索引与链接一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
