# 06 · 蛋白质：语言模型、结构预测与设计

[← 返回资源库](README.md)

## 课程与教程

| 资源 | 形式 | 说明 |
|---|---|---|
| ⭐ [EMBL-EBI《AlphaFold: A practical guide》](https://www.ebi.ac.uk/training/online/courses/alphafold/) | 🎓📹 | 与 Google DeepMind 联合开发，约 3 小时，Colab 实操；另有 [AlphaFold DB 导览](https://www.ebi.ac.uk/training/online/courses/navigating-alphafold-database/) |
| ⭐🆕 [A roadmap for AI-driven protein design](https://miangoaren.github.io/teaching/proteins) | 🎓📹 | 2026 年免费课程：10 讲、约 37 小时 YouTube 视频、800+ 页幻灯片（[Zenodo](https://doi.org/10.5281/zenodo.18498885)） |
| 🆕 [Rosetta Commons ML Protein Design Bootcamp](https://rosettacommons.org/2026/04/14/ml-protein-design-bootcamp-now-available-on-youtube/) | 📹 | 2025 年 11 月录制、2026 年 4 月上线 YouTube；AlphaFold、ESMFold、ProteinMPNN 等工具的入门实战 |
| ⭐ [The Illustrated AlphaFold](https://elanapearl.github.io/blog/2024/the-illustrated-alphafold/) | 博客 | 图解 AlphaFold3 的架构与信息流 |
| [ML for Protein Engineering 研讨会系列](https://www.ml4proteinengineering.com/) | 📹 | 双周学术讲座，YouTube 有往期录像 |
| ⭐ [ColabFold](https://github.com/sokrypton/ColabFold) | 💻 | 在 Colab 上免费跑结构预测 |
| [AlphaFold DB API 文档](https://alphafold.ebi.ac.uk/api-docs) | 📖 | 用程序批量获取预测结构。数据库已升级到 v6，部分接口字段有变化，见[变更说明](https://www.ebi.ac.uk/pdbe/news/breaking-changes-afdb-predictions-api) |
| ⭐ [ColabDesign](https://github.com/sokrypton/ColabDesign) | 💻 | Sergey Ovchinnikov 的蛋白设计 Notebook 合集 |
| [PDB-101](https://pdb101.rcsb.org/) | 📖 | 结构生物学基础 |
| [Machine-learning-guided directed evolution for protein engineering](https://arxiv.org/abs/1811.10775) | 📄 | Yang, Wu & Arnold 综述（Nature Methods 2019） |

## 蛋白质语言模型与表示

| 资源 | 要点 |
|---|---|
| ⭐ [ESM（Meta）](https://github.com/facebookresearch/esm) | ESM-2、ESMFold、ESM-1v、ESM-IF；最常用的蛋白语言模型 |
| ⭐ [ESM3 / ESM C（EvolutionaryScale）](https://github.com/evolutionaryscale/esm) | 序列、结构、功能多模态生成模型 |
| [ProtTrans](https://github.com/agemagician/ProtTrans) | ProtT5 等蛋白语言模型 |
| 🇨🇳 [SaProt（西湖大学）](https://github.com/westlake-repl/SaProt) | 引入结构词表的蛋白语言模型 |
| ⭐ [ProteinGym](https://proteingym.org/) | 突变效应预测的标准基准（深度突变扫描 + 临床数据） |

## 结构预测

| 模型 | 要点 | 链接 |
|---|---|---|
| AlphaFold2 | 2021，接近实验精度的单链结构预测 | [论文](https://doi.org/10.1038/s41586-021-03819-2) · [AlphaFold DB](https://alphafold.ebi.ac.uk/) |
| AlphaFold3 | 2024，蛋白-核酸-小分子复合物共折叠；学术用途可申请权重 | [论文](https://doi.org/10.1038/s41586-024-07487-w) · [代码](https://github.com/google-deepmind/alphafold3) · [AlphaFold Server](https://alphafoldserver.com/) |
| ⭐ Boltz-1 / Boltz-2 | 开源（MIT 许可），Boltz-2 同时预测结构与结合亲和力 | [代码](https://github.com/jwohlwend/boltz) |
| Chai-1 | 开源复合物结构预测 | [代码](https://github.com/chaidiscovery/chai-lab) |
| 🆕 OpenFold3 | AlphaFold3 的开源复现（Apache 2.0），2026 年 3 月重大更新并公开训练数据 | [代码](https://github.com/aqlaboratory/openfold-3) |
| BioEmu | 生成蛋白构象系综，弥补“单一静态结构”的局限 | [代码](https://github.com/microsoft/bioemu) |
| PoseBusters | 检查预测的蛋白-配体结构是否物理合理 | [代码](https://github.com/maabuu/posebusters) |

## 蛋白质设计

| 模型 | 要点 | 链接 |
|---|---|---|
| ⭐ ProteinMPNN | 反向折叠：给定骨架设计序列 | [论文](https://doi.org/10.1126/science.add2187) · [代码](https://github.com/dauparas/ProteinMPNN) |
| ⭐ RFdiffusion | 扩散模型生成蛋白骨架 | [论文](https://doi.org/10.1038/s41586-023-06415-8) · [代码](https://github.com/RosettaCommons/RFdiffusion) |
| 🆕 RFdiffusion3 | 2025 年 12 月在 foundry 中开源，全原子级设计 | [foundry](https://github.com/RosettaCommons/foundry) |
| BindCraft | 基于 AlphaFold2 反向传播的结合蛋白设计 | [代码](https://github.com/martinpacesa/BindCraft) |
| 🆕 BoltzGen | 开源（MIT）通用结合物设计：蛋白、纳米抗体、多肽 | [代码](https://github.com/HannesStark/boltzgen) |
| 🆕 RFD4-Proteina | 2026 年 10 月 UW IPD（Baker 实验室）与 NVIDIA 联合开源（BSD-3）的生物分子设计基础模型，基于流匹配 | [代码](https://github.com/RosettaCommons/RFD4-Proteina) |

## 负责任的研究

- [Responsible AI x Biodesign](https://responsiblebiodesign.ai/)：蛋白设计社区关于安全、开放与负责任开发的价值观与承诺。
