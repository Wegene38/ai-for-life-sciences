# 08 · 单细胞与多组学

[← 返回资源库](README.md)

## 分析基础

| 资源 | 形式 | 说明 |
|---|---|---|
| ⭐ [Single-cell Best Practices](https://www.sc-best-practices.org/) | 📖💻 | Theis 实验室主导的在线书（配套 Nat Rev Genet 2023），从质控到扰动建模、空间组学 |
| ⭐ [scanpy](https://scanpy.readthedocs.io/) | 📖💻 | Python 单细胞分析标准库，scverse 生态核心 |
| ⭐ [scvi-tools](https://docs.scvi-tools.org/) | 📖💻 | 概率深度生成模型（scVI、scANVI、totalVI 等） |
| [squidpy](https://squidpy.readthedocs.io/) | 📖💻 | 空间组学分析 |
| [Orchestrating Single-Cell Analysis with Bioconductor（OSCA）](https://bioconductor.org/books/release/OSCA/) | 📖 | R 语言单细胞分析在线书 |
| [HBC 单细胞培训材料](https://hbctraining.github.io/main/) | 📖💻 | 哈佛生信核心的实战课程 |
| [The specious art of single-cell genomics](https://doi.org/10.1371/journal.pcbi.1011288) | 📄 | Chari & Pachter 2023：t-SNE / UMAP 图不能随便解读 |

## 基础模型

| 模型 | 要点 | 链接 |
|---|---|---|
| Geneformer | 基于基因排序编码的预训练 Transformer | [Hugging Face](https://huggingface.co/ctheodoris/Geneformer) |
| scGPT | 生成式预训练单细胞模型 | [代码](https://github.com/bowang-lab/scGPT) |
| 🇨🇳 scFoundation | 大规模单细胞基础模型（百图生科、清华） | [代码](https://github.com/biomap-research/scFoundation) |
| UCE | 跨物种通用细胞嵌入 | [代码](https://github.com/snap-stanford/UCE) |
| 🆕 Tahoe-x1 | 基于大规模药物扰动单细胞数据训练的模型 | [代码](https://github.com/tahoebio/tahoe-x1) |

## 扰动预测与虚拟细胞

| 资源 | 说明 |
|---|---|
| GEARS | 结合基因关系图预测遗传扰动效应 · [代码](https://github.com/snap-stanford/GEARS) |
| ⭐🆕 State（Arc Institute） | 跨细胞环境预测扰动响应 · [代码](https://github.com/ArcInstitute/state) · [论文](https://doi.org/10.1101/2025.06.26.661135) |
| 🆕 Cell-Eval | Virtual Cell Challenge 使用的评测框架 · [代码](https://github.com/ArcInstitute/cell-eval) |
| ⭐🆕 [Virtual Cell Challenge](https://virtualcellchallenge.org/) | Arc Institute 主办；2026 年第二届聚焦跨细胞系泛化与零样本预测 · [Hugging Face 入门导读](https://huggingface.co/blog/virtual-cell-challenge) |
| [Open Problems in Single-Cell Analysis](https://openproblems.bio/) | 社区维护的单细胞任务基准 · [扰动预测任务](https://github.com/openproblems-bio/task_perturbation_prediction) |

## 冷静看待基础模型（必读）

- Kedzierska et al. 2025，[Zero-shot evaluation reveals limitations of single-cell foundation models](https://doi.org/10.1186/s13059-025-03574-x)（Genome Biology）：零样本场景下 scGPT、Geneformer 常不如高变基因等简单方法。
- Ahlmann-Eltze et al. 2025，[Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://doi.org/10.1038/s41592-025-02772-6)（Nature Methods）：扰动预测中，简单线性 / 加和基线与深度模型相当甚至更好。

## 数据资源

| 资源 | 说明 |
|---|---|
| ⭐ [CZ CELLxGENE](https://cellxgene.cziscience.com/) · [Census API](https://chanzuckerberg.github.io/cellxgene-census/) | 数千万细胞的标准化数据，可直接用 Python 查询 |
| [Human Cell Atlas Data Portal](https://data.humancellatlas.org/) | 人类细胞图谱 |
| [论文列表：深度学习单细胞](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) · [单细胞基础模型](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) | 按任务分类的论文导航 |
