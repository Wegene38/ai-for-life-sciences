# 05 · 基因组学

[← 返回资源库](README.md)

核心问题：从 DNA / RNA 序列预测调控活性、基因表达、剪接和变异效应，并据此解释或设计序列。

## 课程与教程

| 资源 | 形式 | 说明 |
|---|---|---|
| ⭐ [A primer on deep learning in genomics](https://www.nature.com/articles/s41588-018-0295-5) + [Colab](https://github.com/abidlabs/deep-learning-genomics-primer) | 📄💻 | 用 CNN 从 DNA 序列预测结合位点的完整小例子 |
| ⭐ [MIT 6.874 调控基因组学相关讲座](https://mit6874.github.io/) | 🎓📹 | Kellis & Gifford |
| ⭐ [Stanford CS273B 材料](https://github.com/kundajelab/cs273b) | 💻 | Kundaje 组的调控基因组学深度学习 |
| ⭐ [gReLU（Genentech）](https://github.com/Genentech/gReLU) | 💻📖 | 训练、解释、设计 DNA 序列模型的一站式框架，带教程 |
| [Kipoi](https://github.com/kipoi/kipoi) | 💻 | 基因组学预训练模型仓库 |

## 代表模型

| 模型 | 年份 | 要点 | 链接 |
|---|---|---|---|
| DeepSEA | 2015 | CNN 从序列预测染色质特征与非编码变异效应 | [论文](https://doi.org/10.1038/nmeth.3547) |
| Basset | 2016 | CNN 预测染色质可及性 | [论文](https://doi.org/10.1101/gr.200535.115) |
| SpliceAI | 2019 | 从序列预测剪接位点 | [代码](https://github.com/Illumina/SpliceAI) |
| BPNet | 2021 | 碱基分辨率预测 TF 结合谱，学习基序语法 | [论文](https://doi.org/10.1038/s41588-021-00782-6) |
| Enformer | 2021 | Transformer 建模约 100 kb 远端调控 | [论文](https://doi.org/10.1038/s41592-021-01252-x) |
| Borzoi | 2025 | 从序列预测 RNA-seq 覆盖度 | [代码](https://github.com/calico/borzoi) |
| ⭐🆕 AlphaGenome | 2026 | 1 Mb 输入、碱基分辨率、同时预测表达、剪接、可及性等数千种性质；API 对非商业用途免费 | [Nature 论文](https://doi.org/10.1038/s41586-025-10014-0) · [API](https://github.com/google-deepmind/alphagenome) · [模型代码](https://github.com/google-deepmind/alphagenome_research) |
| DNABERT-2 | 2024 | BPE 分词的多物种 DNA 语言模型 | [代码](https://github.com/MAGICS-LAB/DNABERT_2) |
| Nucleotide Transformer | 2024 | 多物种 DNA 语言模型 | [代码](https://github.com/instadeepai/nucleotide-transformer) |
| HyenaDNA | 2023 | 长卷积实现百万碱基上下文 | [代码](https://github.com/HazyResearch/hyena-dna) |
| Caduceus | 2024 | 双向、反向互补等变的 DNA 模型 | [代码](https://github.com/kuleshov-group/caduceus) |
| ⭐🆕 Evo 2 | 2026 | 跨生命域训练的基因组基础模型，1 Mb 上下文，数据、代码、权重全部开源 | [Nature 论文](https://doi.org/10.1038/s41586-026-10176-5) · [代码](https://github.com/ArcInstitute/evo2) |

## 基准与竞赛

| 资源 | 说明 |
|---|---|
| [BEND](https://github.com/frederikkemarin/BEND) | DNA 语言模型基准 |
| [Stanford RNA 3D Folding（Kaggle）](https://www.kaggle.com/competitions/stanford-rna-3d-folding) | 从序列预测 RNA 三维结构；2026 年 1 月开启了难度更高的第二轮 |

## 拓展阅读

- [Ensembl](https://www.ensembl.org/)、[UCSC Genome Browser](https://genome.ucsc.edu/)、[ENCODE](https://www.encodeproject.org/)、[GTEx](https://gtexportal.org/)：训练和评估序列模型最常用的数据来源。
