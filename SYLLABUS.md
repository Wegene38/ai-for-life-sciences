# 📅 逐日课程表（26 周 · 182 天）

每天一篇学习笔记，按本表顺序更新。“笔记”列为 ⏳ 表示尚未更新，✅ 链接到当天的笔记。

- **时间投入**：平日约 1.5 小时；每周第 7 天是“周复盘 + 小项目”，约 2–3 小时。
- **可以跳过**：已经掌握的内容直接跳过，见 [ROADMAP.md](ROADMAP.md#1-先做自评)。笔记会继续每天更新，可以当作资料库。
- **资源简称**：UDL = *Understanding Deep Learning*；d2l = 《动手学深度学习》中文版；ISLP = *An Introduction to Statistical Learning (Python)*；MML = *Mathematics for Machine Learning*；MSMB = *Modern Statistics for Modern Biology*；PDSH = *Python Data Science Handbook*。所有链接见 [resources/](resources/README.md)。

| 阶段 | 周次 | Day | 主题 |
|---|---|---|---|
| 0 · 启航 | 第 1 周 | 001–007 | 全景图、学习方法、开发环境 |
| 1 · 基础补齐 | 第 2–5 周 | 008–035 | Python 科学计算、数学、生命科学与生信速成 |
| 2 · 机器学习与深度学习核心 | 第 6–11 周 | 036–077 | 经典机器学习、神经网络、CNN、Transformer、GNN |
| 3 · 生成模型与大模型 | 第 12–13 周 | 078–091 | VAE、扩散、流匹配、LLM 与基础模型 |
| 4 · AI × 生命科学专题 | 第 14–24 周 | 092–168 | 基因组、蛋白质、药物发现、单细胞、影像、智能体 |
| 5 · 科研实战 | 第 25–26 周 | 169–182 | 科研严谨性、毕业项目、持续成长 |
| 6 · 持续进阶 | 第 27 周起 | 183– | 每天精读一篇近期论文或一个新工具 |

---

## 阶段 0 · 启航

### 第 1 周 · 全景图、学习方法与开发环境
> 本周目标：知道这个领域在做什么、自己要往哪走；搭好能跑代码的环境。

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 001 | 启航：AI × 生命科学全景图 | 模态 × 任务地图、2012–2026 里程碑；deep-review 综述、诺贝尔奖科普、AlphaFold DB | [✅](daily/2026-11/day001-2026-11-04.md) |
| 002 | 学习者自评与个人路线定制 | 技能自评表、两条入口路线、学习方法（主动回忆、间隔重复、费曼） | [✅](daily/2026-11/day002-2026-11-05.md) |
| 003 | 开发环境：Colab、Kaggle、conda、Jupyter | 免费 GPU 的用法与限制；本地 mamba 环境；国内访问提示 | [✅](daily/2026-11/day003-2026-11-06.md) |
| 004 | Git 与 GitHub：建立自己的学习仓库 | Software Carpentry Git；Missing Semester 版本控制一课 | [✅](daily/2026-11/day004-2026-11-07.md) |
| 005 | Linux 命令行与生信文件操作 | Software Carpentry Shell；Data Carpentry Shell for Genomics | [✅](daily/2026-11/day005-2026-11-08.md) |
| 006 | 如何读 AI × 生物论文、追踪文献 | Keshav《How to Read a Paper》；Ten simple rules for reading a scientific paper；Zotero + 预印本订阅 | [✅](daily/2026-11/day006-2026-11-09.md) |
| 007 | 🔁 周复盘 ①：第一个生物 AI Notebook | Biopython 解析序列 + 从 AlphaFold DB 取结构 + 画 pLDDT 曲线 | [✅](daily/2026-11/day007-2026-11-10.md) |

## 阶段 1 · 基础补齐

### 第 2 周 · Python 科学计算
> 主资源：[Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/)、[PDSH](https://jakevdp.github.io/PythonDataScienceHandbook/)、[Biopython](https://biopython.org/wiki/Documentation)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 008 | Python 核心语法速览 | 数据结构、函数、类、模块；Python 官方教程 3–9 章 | [✅](daily/2026-11/day008-2026-11-11.md) |
| 009 | NumPy：向量化与广播 | PDSH 第 2 章；用 one-hot 编码 DNA 序列 | [✅](daily/2026-11/day009-2026-11-12.md) |
| 010 | pandas：表格数据处理 | PDSH 第 3 章；以基因表达矩阵为例做筛选、分组、合并 | ⏳ |
| 011 | 可视化：matplotlib / seaborn | PDSH 第 4 章；火山图、热图、散点图的规范画法 | ⏳ |
| 012 | Biopython 与生物文件格式 | FASTA/FASTQ/GenBank/PDB 读写；Biopython Tutorial | ⏳ |
| 013 | 写可复现的科研代码 | 《Good enough practices in scientific computing》；项目结构、环境锁定、随机种子 | ⏳ |
| 014 | 🔁 周复盘 ②：分析一个公开表达数据集 | 读入 → 质控 → 归一化 → 差异表达初探 → 作图 | ⏳ |

### 第 3 周 · 数学 I：线性代数与优化
> 主资源：[3Blue1Brown 线性代数的本质](https://www.3blue1brown.com/topics/linear-algebra)、[MML](https://mml-book.github.io/)、[d2l](https://zh.d2l.ai/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 015 | 向量、矩阵与线性变换 | 3Blue1Brown 第 1–4 集；MML 第 2 章 | ⏳ |
| 016 | 特征分解与 SVD | 3Blue1Brown 特征向量一集；MML 第 4 章；MIT 18.06 选看 | ⏳ |
| 017 | PCA：原理与组学应用 | MML 第 10 章；MSMB 第 7 章；用 SVD 手写 PCA | ⏳ |
| 018 | 导数、梯度与链式法则 | 3Blue1Brown 微积分的本质；MML 第 5 章 | ⏳ |
| 019 | 优化：梯度下降与学习率 | MML 第 7 章；d2l 第 11 章 11.1–11.5 | ⏳ |
| 020 | 自动微分：从手推到 autograd | d2l 2.5；Karpathy micrograd（Zero to Hero 第 1 讲） | ⏳ |
| 021 | 🔁 周复盘 ③：从零实现 PCA 与线性回归 | 只用 NumPy；与 scikit-learn 结果对比 | ⏳ |

### 第 4 周 · 数学 II：概率统计与信息论
> 主资源：[Harvard Stat 110](https://stat110.hsites.harvard.edu/)、[MSMB](https://www.huber.embl.de/msmb/)、[ISLP](https://www.statlearning.com/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 022 | 概率基础与贝叶斯定理 | Stat 110 前几讲；Seeing Theory 交互演示 | ⏳ |
| 023 | 常见分布与生物计数数据 | 二项、泊松、负二项——为什么 RNA-seq 用负二项；MSMB 第 1–2 章 | ⏳ |
| 024 | 参数估计：MLE、MAP 与贝叶斯推断 | MML 第 8 章；Murphy《Probabilistic ML》第 4 章选读 | ⏳ |
| 025 | 假设检验、p 值与多重检验（FDR） | MSMB 第 6 章；ISLP 第 13 章 | ⏳ |
| 026 | 信息论：熵、交叉熵、KL 散度 | 损失函数从哪里来；Murphy《Probabilistic ML》信息论一章 | ⏳ |
| 027 | 偏差-方差、过拟合与模型选择 | ISLP 第 2、5 章 | ⏳ |
| 028 | 🔁 周复盘 ④：用模拟实验理解统计陷阱 | 模拟多重检验假阳性、小样本过拟合 | ⏳ |

### 第 5 周 · 生命科学与生物信息速成
> 主资源：[OpenStax Biology 2e](https://openstax.org/details/books/biology-2e)、[生物信息学：导论与方法（北大）](https://www.coursera.org/learn/sheng-wu-xin-xi-xue)、[Rosalind](https://rosalind.info/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 029 | 中心法则、基因组与基因调控 | OpenStax Biology 2e 分子生物学相关章节；MIT 7.00x 选看 | ⏳ |
| 030 | 测序技术与组学数据 | NGS、RNA-seq、ATAC-seq、单细胞测序；HBC Training 入门 | ⏳ |
| 031 | 蛋白质：序列、结构与功能 | 四级结构、折叠、结构域；PDB-101 | ⏳ |
| 032 | 小分子与药物研发流程 | 靶点 → 苗头 → 先导 → 候选；ADMET；TeachOpenCADD T001–T002 | ⏳ |
| 033 | 序列比对与进化：动态规划、BLAST、MSA | Bioinformatics Algorithms 第 5 章；北大生物信息学课程比对单元 | ⏳ |
| 034 | 核心数据库与文件格式 | NCBI/Ensembl/UniProt/PDB/ChEMBL/GEO；FASTA/BAM/VCF/mmCIF/SMILES/h5ad | ⏳ |
| 035 | 🔁 周复盘 ⑤：Rosalind 刷题 + 数据获取脚本 | 完成 5 道 Rosalind；写脚本从 UniProt/PDB/ChEMBL 取数据 | ⏳ |

## 阶段 2 · 机器学习与深度学习核心

### 第 6 周 · 机器学习 I：监督学习
> 主资源：[ISLP](https://www.statlearning.com/)、[scikit-learn 用户指南](https://scikit-learn.org/stable/user_guide.html)、[李宏毅机器学习 2021](https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.php)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 036 | 机器学习概览与数据划分 | 训练/验证/测试；Google ML Crash Course；ISLP 第 2 章 | ⏳ |
| 037 | 线性回归与正则化 | Ridge / Lasso / Elastic Net；ISLP 第 3、6 章 | ⏳ |
| 038 | 逻辑回归与分类评估 | 混淆矩阵、ROC-AUC、PR-AUC、类别不平衡；ISLP 第 4 章 | ⏳ |
| 039 | 交叉验证、超参数搜索与 Pipeline | ISLP 第 5 章；scikit-learn Pipeline 与 GridSearchCV | ⏳ |
| 040 | 生物数据的数据泄漏与合理划分 | 同源序列、分子骨架、时间、患者级划分；Chicco《Ten quick tips for ML in computational biology》 | ⏳ |
| 041 | 特征工程：k-mer、one-hot、分子指纹 | 序列与分子的经典特征；RDKit Morgan 指纹 | ⏳ |
| 042 | 🔁 周复盘 ⑥：表达谱肿瘤亚型分类 | 完整 scikit-learn 流程 + 合理的交叉验证 | ⏳ |

### 第 7 周 · 机器学习 II：树模型、核方法与无监督
> 主资源：[ISLP](https://www.statlearning.com/)、[Interpretable ML](https://christophm.github.io/interpretable-ml-book/)、[sc-best-practices](https://www.sc-best-practices.org/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 043 | 决策树、随机森林与梯度提升 | ISLP 第 8 章；XGBoost / LightGBM 实践要点 | ⏳ |
| 044 | 支持向量机与核方法 | ISLP 第 9 章；序列核、图核的思想 | ⏳ |
| 045 | 聚类：k-means、层次聚类、Leiden | ISLP 第 12 章；sc-best-practices 聚类一章 | ⏳ |
| 046 | 降维可视化：PCA、t-SNE、UMAP 的正确解读 | Chari & Pachter《The specious art of single-cell genomics》 | ⏳ |
| 047 | 可解释性：特征重要性、SHAP、部分依赖 | Molnar《Interpretable Machine Learning》 | ⏳ |
| 048 | 隐马尔可夫模型与序列标注 | Bioinformatics Algorithms 第 10 章；基因预测与 CpG 岛 | ⏳ |
| 049 | 🔁 周复盘 ⑦：完整 ML 小比赛 | EDA → 基线 → 调参 → 误差分析 → 报告 | ⏳ |

### 第 8 周 · 深度学习 I：神经网络与 PyTorch
> 主资源：[UDL](https://udlbook.github.io/udlbook/)、[d2l](https://zh.d2l.ai/)、[PyTorch Tutorials](https://pytorch.org/tutorials/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 050 | 从感知机到多层感知机 | UDL 第 3–4 章；d2l 第 4 章 4.1–4.3 | ⏳ |
| 051 | 反向传播与计算图 | UDL 第 7 章；d2l 4.7；3Blue1Brown 神经网络系列 | ⏳ |
| 052 | PyTorch 基础：Tensor、Dataset、训练循环 | PyTorch “Learn the Basics”；learnpytorch.io | ⏳ |
| 053 | 优化器与训练技巧 | SGD/动量/Adam、学习率调度、初始化；UDL 第 6 章；d2l 第 11 章 | ⏳ |
| 054 | 正则化与泛化 | Dropout、BatchNorm/LayerNorm、权重衰减、早停；UDL 第 9 章 | ⏳ |
| 055 | 深度学习实验管理与复现 | GPU、混合精度、日志、随机种子；Karpathy《A Recipe for Training Neural Networks》 | ⏳ |
| 056 | 🔁 周复盘 ⑧：PyTorch 从零写 MLP 预测分子性质 | 指纹 → MLP；与随机森林对比 | ⏳ |

### 第 9 周 · 深度学习 II：卷积网络与可解释性
> 主资源：[d2l](https://zh.d2l.ai/)、[UDL](https://udlbook.github.io/udlbook/)、[A primer on deep learning in genomics](https://github.com/abidlabs/deep-learning-genomics-primer)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 057 | 卷积神经网络原理 | 卷积、池化、感受野；d2l 第 6 章；CS231n 笔记 | ⏳ |
| 058 | 现代 CNN：ResNet、空洞卷积、U-Net | d2l 第 7 章；UDL 第 10–11 章 | ⏳ |
| 059 | 1D CNN 读 DNA：基序检测 | Zou et al. 2019 primer 及其 Colab | ⏳ |
| 060 | 解释深度模型：显著图、Integrated Gradients | Captum 教程；in silico 突变扫描 | ⏳ |
| 061 | 迁移学习与预训练模型微调 | d2l 13.2；冻结、微调、领域偏移 | ⏳ |
| 062 | 不确定性估计与校准 | 深度集成、MC Dropout、共形预测（Angelopoulos & Bates 教程） | ⏳ |
| 063 | 🔁 周复盘 ⑨：CNN 预测转录因子结合 | 训练、评估、可视化学到的基序 | ⏳ |

### 第 10 周 · 序列模型与 Transformer
> 主资源：[d2l](https://zh.d2l.ai/)、[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)、[Karpathy Zero to Hero](https://karpathy.ai/zero-to-hero.html)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 064 | 嵌入与表示学习 | one-hot → word2vec → 上下文嵌入；d2l 第 14 章 | ⏳ |
| 065 | RNN / LSTM 与序列建模的难点 | d2l 第 8–9 章（选读） | ⏳ |
| 066 | 注意力机制与 Transformer | d2l 第 10 章；The Illustrated Transformer | ⏳ |
| 067 | 从零实现一个小 Transformer | Karpathy “Let’s build GPT” 与 nanoGPT | ⏳ |
| 068 | 分词与预训练目标：MLM vs 自回归 | k-mer / BPE 分词（DNABERT-2）；Hugging Face LLM Course 分词章节 | ⏳ |
| 069 | 高效微调与长序列 | LoRA / PEFT；FlashAttention、Hyena、Mamba 简介 | ⏳ |
| 070 | 🔁 周复盘 ⑩：Transformer 做蛋白序列分类 | 小模型从零训练 vs 预训练嵌入 | ⏳ |

### 第 11 周 · 图神经网络与几何深度学习
> 主资源：[CS224W](https://web.stanford.edu/class/cs224w/)、[Geometric Deep Learning](https://geometricdeeplearning.com/)、[dmol.pub](https://dmol.pub/)、[PyG](https://pytorch-geometric.readthedocs.io/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 071 | 图与图学习任务 | 节点 / 边 / 图级任务；CS224W 前 3 讲；Distill GNN 入门 | ⏳ |
| 072 | 消息传递：GCN、GAT、GIN、MPNN | CS224W；PyG 文档 | ⏳ |
| 073 | 分子图与 PyG 实战 | dmol.pub 图神经网络一章；PyG 教程 | ⏳ |
| 074 | 对称性与等变性 | 为什么 3D 结构需要 E(3) 等变；Geometric Deep Learning 原书第 3–4 章 | ⏳ |
| 075 | 等变网络：EGNN 与 e3nn 入门 | dmol.pub 等变网络一章；e3nn 教程 | ⏳ |
| 076 | 生物网络与知识图谱 | 蛋白互作网络、链接预测；PrimeKG | ⏳ |
| 077 | 🔁 周复盘 ⑪：GNN 预测分子性质 | 骨架划分（scaffold split）下对比 GNN 与指纹模型 | ⏳ |

## 阶段 3 · 生成模型与大模型

### 第 12 周 · 生成模型
> 主资源：[MIT 6.S184（2026）](https://diffusion.csail.mit.edu/)、[UDL](https://udlbook.github.io/udlbook/)、[Lilian Weng 扩散模型博客](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 078 | 生成模型全景 | 自回归、VAE、GAN、流、扩散的比较；UDL 第 14 章 | ⏳ |
| 079 | 自编码器与 VAE | UDL 第 17 章；scVI 为什么是 VAE | ⏳ |
| 080 | 扩散模型 I：DDPM 与得分匹配 | MIT 6.S184 讲义；UDL 第 18 章 | ⏳ |
| 081 | 扩散模型 II：流匹配与条件生成 | MIT 6.S184；Meta《Flow Matching Guide and Code》；无分类器引导 | ⏳ |
| 082 | 离散数据生成：序列设计 | 自回归 vs 离散扩散；MIT 6.S184（2026）离散扩散一讲 | ⏳ |
| 083 | 如何评估生物生成模型 | 新颖性、多样性、可设计性、湿实验验证 | ⏳ |
| 084 | 🔁 周复盘 ⑫：从零实现 2D 流匹配 | 完成 MIT 6.S184 Lab 1–2 | ⏳ |

### 第 13 周 · 大语言模型与基础模型
> 主资源：[李宏毅机器学习 2025](https://speech.ee.ntu.edu.tw/~hylee/ml/2025-spring.php)、[Hugging Face LLM Course](https://huggingface.co/learn/llm-course)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 085 | LLM 如何训练：预训练、指令微调、RLHF | 李宏毅 ML 2025；Karpathy《Deep Dive into LLMs like ChatGPT》 | ⏳ |
| 086 | Hugging Face 生态实战 | Transformers、Datasets、Hub；LLM Course 前几章 | ⏳ |
| 087 | 嵌入、检索与 RAG | 搭一个文献问答原型；PaperQA 的思路 | ⏳ |
| 088 | 提示工程与工具调用 | Prompt Engineering Guide；结构化输出 | ⏳ |
| 089 | 生物学里的“基础模型”：机遇与局限 | Bommasani et al. 2021；单细胞基础模型零样本评测 | ⏳ |
| 090 | 读懂基准与排行榜 | ProteinGym、TDC、Polaris；基准过拟合与数据泄漏 | ⏳ |
| 091 | 🔁 周复盘 ⑬：读论文助手小工具 | 检索 + 摘要 + 引用核对 | ⏳ |

## 阶段 4 · AI × 生命科学专题

### 第 14 周 · 基因组学 I：调控序列模型
> 主资源：[MIT 6.874](https://mit6874.github.io/)、[CS273B 材料](https://github.com/kundajelab/cs273b)、[gReLU](https://github.com/Genentech/gReLU)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 092 | 调控基因组学与“序列 → 功能”问题 | MIT 6.874 调控基因组学讲座 | ⏳ |
| 093 | DeepSEA / Basset：CNN 预测染色质特征 | Zhou & Troyanskaya 2015；Kelley et al. 2016 | ⏳ |
| 094 | BPNet 与碱基分辨率模型 | Avsec et al. 2021：profile 预测与基序语法 | ⏳ |
| 095 | 变异效应预测 | 从序列模型到 eQTL / GWAS 位点解读 | ⏳ |
| 096 | 实战：用 gReLU 训练和解释模型 | gReLU 官方教程 | ⏳ |
| 097 | 从解释到发现：基序与增强子设计 | in silico 突变、TF-MoDISco 思路、序列设计 | ⏳ |
| 098 | 🔁 周复盘 ⑭：复现小型序列 → 功能模型 | 训练 + 突变扫描 + 基序可视化 | ⏳ |

### 第 15 周 · 基因组学 II：长程模型与 DNA 语言模型
> 主资源：[AlphaGenome](https://github.com/google-deepmind/alphagenome)、[Evo 2](https://github.com/ArcInstitute/evo2)、[Borzoi](https://github.com/calico/borzoi)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 099 | Enformer 与长程调控 | Avsec et al. 2021 Nature Methods | ⏳ |
| 100 | Borzoi 与 AlphaGenome | 从 RNA-seq 覆盖度到 1 Mb 多模态预测；AlphaGenome（Nature 2026） | ⏳ |
| 101 | DNA 语言模型 | DNABERT-2、Nucleotide Transformer、HyenaDNA、Caduceus | ⏳ |
| 102 | Evo 2：跨生命域的基因组基础模型 | Evo 2（Nature 2026）；生成式基因组设计 | ⏳ |
| 103 | 基因组模型评测 | BEND 基准；零样本变异效应 | ⏳ |
| 104 | RNA：剪接、结构与 RNA 模型 | SpliceAI；Stanford RNA 3D Folding 竞赛 | ⏳ |
| 105 | 🔁 周复盘 ⑮：变异效应打分实战 | AlphaGenome API 或开源 DNA 模型 | ⏳ |

### 第 16 周 · 蛋白质 I：表示学习与语言模型
> 主资源：[ESM](https://github.com/facebookresearch/esm)、[ESM3 / ESM C](https://github.com/evolutionaryscale/esm)、[ProteinGym](https://proteingym.org/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 106 | 蛋白质的计算表示 | 序列、MSA、结构、残基图 | ⏳ |
| 107 | 蛋白质语言模型：ESM-2 | Lin et al. 2023 Science；掩码语言模型学到了什么 | ⏳ |
| 108 | 实战：ESM 嵌入做性质预测 | 嵌入 + 轻量下游模型 | ⏳ |
| 109 | 零样本突变效应与 ProteinGym | ESM-1v 思路；深度突变扫描（DMS）基准 | ⏳ |
| 110 | ESM3 / ESM C 与多模态蛋白模型 | 序列 + 结构 + 功能联合建模；SaProt | ⏳ |
| 111 | 机器学习指导的蛋白质工程 | 主动学习、贝叶斯优化；Yang, Wu & Arnold 综述；ML4PE 讲座 | ⏳ |
| 112 | 🔁 周复盘 ⑯：ESM-2 零样本突变扫描 | 与公开 DMS 数据算 Spearman 相关 | ⏳ |

### 第 17 周 · 蛋白质 II：结构预测
> 主资源：[EMBL-EBI AlphaFold 课程](https://www.ebi.ac.uk/training/online/courses/alphafold/)、[ColabFold](https://github.com/sokrypton/ColabFold)、[Boltz](https://github.com/jwohlwend/boltz)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 113 | 结构预测简史：从同源建模到 AlphaFold | EMBL-EBI《AlphaFold: A practical guide》；CASP | ⏳ |
| 114 | AlphaFold2 架构精读 | Evoformer、结构模块、pLDDT / PAE；AF2 论文 | ⏳ |
| 115 | 实战：ColabFold 预测与置信度解读 | ColabFold Notebook | ⏳ |
| 116 | AlphaFold3 与共折叠 | 蛋白-核酸-小分子复合物；The Illustrated AlphaFold | ⏳ |
| 117 | 开源复现：Boltz-2、Chai-1、OpenFold3 | 结构 + 亲和力联合预测；许可证差异 | ⏳ |
| 118 | 结构预测的局限 | 构象动态（BioEmu）、无序区、记忆化、PoseBusters | ⏳ |
| 119 | 🔁 周复盘 ⑰：预测一个复合物并批判性评估 | Boltz-2 或 ColabFold | ⏳ |

### 第 18 周 · 蛋白质 III：蛋白质设计
> 主资源：[A roadmap for AI-driven protein design](https://miangoaren.github.io/teaching/proteins)、[ProteinMPNN](https://github.com/dauparas/ProteinMPNN)、[RFdiffusion](https://github.com/RosettaCommons/RFdiffusion)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 120 | 蛋白质设计范式：从理性设计到生成 | AI 蛋白设计课程第 1–2 讲；Rosetta Commons ML 设计训练营 | ⏳ |
| 121 | 反向折叠：ProteinMPNN | Dauparas et al. 2022 Science | ⏳ |
| 122 | 骨架生成：RFdiffusion 与 RFdiffusion3 | Watson et al. 2023 Nature；foundry 仓库 | ⏳ |
| 123 | 结合蛋白设计：BindCraft、BoltzGen | 幻觉（hallucination）与生成两条路线；ColabDesign | ⏳ |
| 124 | 设计的评估与筛选 | 自洽性、AF2 过滤、实验验证与设计竞赛 | ⏳ |
| 125 | 生物安全与负责任的设计 | Responsible AI x Biodesign 承诺 | ⏳ |
| 126 | 🔁 周复盘 ⑱：跑通一条小设计管线 | ProteinMPNN（可选 RFdiffusion → MPNN → 结构预测验证） | ⏳ |

### 第 19 周 · 小分子与药物发现 I：表示与性质预测
> 主资源：[TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/)、[dmol.pub](https://dmol.pub/)、[RDKit](https://www.rdkit.org/docs/GettingStartedInPython.html)、[TDC](https://tdcommons.ai/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 127 | 分子表示：SMILES、分子图、指纹、3D 构象 | dmol.pub；RDKit 入门 | ⏳ |
| 128 | RDKit 实战：描述符、子结构、相似性 | TeachOpenCADD T004 | ⏳ |
| 129 | 分子性质预测：从 QSAR 到 Chemprop | Chemprop 文档与示例 | ⏳ |
| 130 | 基准与数据划分 | MoleculeNet、TDC、Polaris；骨架划分与时间划分 | ⏳ |
| 131 | ADMET 预测与多任务学习 | TDC ADMET 基准组；ADMET-AI | ⏳ |
| 132 | 实用化学信息学 | 数据清洗、活性悬崖、适用域；Pat Walters 教程 | ⏳ |
| 133 | 🔁 周复盘 ⑲：指纹 + RF vs GNN | 在 TDC 或 Polaris 数据集上比较 | ⏳ |

### 第 20 周 · 药物发现 II：结构、生成与闭环
> 主资源：[TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/)、[DiffDock](https://github.com/gcorso/DiffDock)、[REINVENT4](https://github.com/MolecularAI/REINVENT4)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 134 | 基于结构的药物设计与分子对接 | TeachOpenCADD T015；AutoDock Vina 文档 | ⏳ |
| 135 | 深度学习对接与共折叠 | DiffDock；Boltz-2 亲和力；PoseBusters 的警示 | ⏳ |
| 136 | 分子生成：REINVENT 与 3D 生成 | REINVENT4；扩散 / 流模型生成分子 | ⏳ |
| 137 | 主动学习与“实验室在环” | 设计-制造-测试-学习（DMTL）循环 | ⏳ |
| 138 | 合成可及性与逆合成：AiZynthFinder | AiZynthFinder 文档 | ⏳ |
| 139 | 案例：AI 发现的药物走到哪一步了 | 成功、炒作与教训；Derek Lowe 博客 | ⏳ |
| 140 | 🔁 周复盘 ⑳：小型虚拟筛选管线 | 过滤 → 打分 → 排序 → 可视化 | ⏳ |

### 第 21 周 · 单细胞与多组学 I：分析基础
> 主资源：[sc-best-practices](https://www.sc-best-practices.org/)、[scanpy](https://scanpy.readthedocs.io/)、[scvi-tools](https://docs.scvi-tools.org/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 141 | 单细胞数据与 scverse 生态 | AnnData / h5ad；sc-best-practices 引言 | ⏳ |
| 142 | 预处理：质控、归一化、高变基因、降维 | sc-best-practices 预处理各章 | ⏳ |
| 143 | 聚类、注释与差异表达 | 伪批量（pseudobulk）差异分析 | ⏳ |
| 144 | 批次整合与 scVI / scANVI | scvi-tools 教程 | ⏳ |
| 145 | 轨迹推断与 RNA velocity | sc-best-practices 轨迹章节 | ⏳ |
| 146 | 空间转录组与多组学整合 | squidpy；MuData | ⏳ |
| 147 | 🔁 周复盘 ㉑：完整单细胞分析 + scVI 整合 | PBMC 数据集 | ⏳ |

### 第 22 周 · 单细胞 II：基础模型与虚拟细胞
> 主资源：[scGPT](https://github.com/bowang-lab/scGPT)、[Geneformer](https://huggingface.co/ctheodoris/Geneformer)、[Arc State](https://github.com/ArcInstitute/state)、[Virtual Cell Challenge](https://virtualcellchallenge.org/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 148 | 单细胞基础模型：Geneformer、scGPT、scFoundation、UCE | 预训练目标与表示方式的差异 | ⏳ |
| 149 | 实战：基础模型嵌入做细胞注释 | 与 PCA / 高变基因基线公平比较 | ⏳ |
| 150 | 扰动预测：Perturb-seq 与 GEARS | Roohani et al. GEARS | ⏳ |
| 151 | 虚拟细胞：State 与 Virtual Cell Challenge | State 论文；Cell-Eval 评测 | ⏳ |
| 152 | 大规模数据资源 | CELLxGENE Census、Human Cell Atlas、Tahoe-100M | ⏳ |
| 153 | 简单基线为何常常更强 | Ahlmann-Eltze et al. 2025；Kedzierska et al. 2025 | ⏳ |
| 154 | 🔁 周复盘 ㉒：扰动预测基线实验 | 均值 / 线性基线 vs 深度模型 | ⏳ |

### 第 23 周 · 生物医学影像
> 主资源：[BioImage Analysis Notebooks](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/)、[DL@MBL 练习](https://github.com/dl-janelia/DL-MBL-2024)、[Cellpose](https://www.cellpose.org/)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 155 | 生物图像分析基础与 napari | 图像格式、通道、尺度；BioImage Analysis Notebooks | ⏳ |
| 156 | 分割：U-Net、StarDist、Cellpose | DL@MBL U-Net 练习 | ⏳ |
| 157 | 去噪与恢复：自监督方法 | DL@MBL 去噪练习（Noise2Void 等） | ⏳ |
| 158 | bioimage.io 与通用分割模型 | BioImage Model Zoo；Cellpose 新版本 | ⏳ |
| 159 | 计算病理与医学影像 | 多示例学习（MIL）、病理基础模型 UNI；MONAI | ⏳ |
| 160 | 多模态：图像 + 组学 | Cell Painting（JUMP）、空间组学 | ⏳ |
| 161 | 🔁 周复盘 ㉓：Cellpose 分割 + 形态特征聚类 | — | ⏳ |

### 第 24 周 · LLM、智能体与 AI 科学家
> 主资源：[Biomni](https://github.com/snap-stanford/Biomni)、[PaperQA](https://github.com/Future-House/paper-qa)、[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 162 | 生物医学文本挖掘：从 BioBERT 到 LLM | 实体识别、关系抽取、文献综述自动化 | ⏳ |
| 163 | 科学智能体的结构 | 规划、工具、记忆、代码执行；HF Agents Course | ⏳ |
| 164 | Biomni：通用生物医学智能体 | Biomni 论文与代码 | ⏳ |
| 165 | 文献智能体：PaperQA | 检索、引用核对与综合 | ⏳ |
| 166 | 多智能体科研：Virtual Lab、AI 科学家 | Virtual Lab；Robin / Kosmos 等案例 | ⏳ |
| 167 | 风险与评估：幻觉、可复现性、生物安全 | LAB-Bench；BioReasoning Challenge | ⏳ |
| 168 | 🔁 周复盘 ㉔：搭一个小型科研智能体 | 文献检索 + UniProt / NCBI API 调用 | ⏳ |

## 阶段 5 · 科研实战

### 第 25 周 · 科研严谨性与毕业项目启动
> 主资源：[projects/README.md](projects/README.md)

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 169 | 如何选题 | 生物学意义 × 数据可得 × 可验证 | ⏳ |
| 170 | 基线优先、消融实验与统计检验 | 别让复杂模型输给简单基线 | ⏳ |
| 171 | 可复现研究与开放科学 | Sandve et al.《Ten simple rules for reproducible computational research》；模型卡 | ⏳ |
| 172 | 毕业项目①：问题定义、数据与基线 | — | ⏳ |
| 173 | 毕业项目②：模型迭代与误差分析 | — | ⏳ |
| 174 | 毕业项目③：生物学解读与可视化 | — | ⏳ |
| 175 | 🔁 周复盘 ㉕：项目中期自查 | 自查清单 | ⏳ |

### 第 26 周 · 毕业项目收尾与持续成长
| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
| 176 | 写作：技术报告、博客与论文 | 结构、图表、讲清贡献 | ⏳ |
| 177 | 开源发布：README、许可证、环境、模型卡 | — | ⏳ |
| 178 | 学术交流：会议、研讨会与投稿 | ISMB、RECOMB、MLCB、MLSB 等 | ⏳ |
| 179 | 建立自己的前沿追踪系统 | 每周信息流、读书会、竞赛 | ⏳ |
| 180 | 职业路径与作品集 | 学术界、药企 / 生物科技、AI 实验室 | ⏳ |
| 181 | 半年总复盘 | 知识地图自测与查漏补缺 | ⏳ |
| 182 | 🎓 结业：下一阶段规划 | 选择 1–2 个方向深入 | ⏳ |

## 阶段 6 · 持续进阶（Day 183 起）

182 天完成后，每天精读一篇近期重要论文或一个新工具，按周轮换主题：周一 基因组 / RNA，周二 蛋白质结构与设计，周三 小分子与药物，周四 单细胞与多组学，周五 影像与多模态，周六 LLM / 智能体 / 方法论，周日 本周前沿汇总。每周一提前排好未来 7 天的主题，追加到下表。

| Day | 主题 | 学习要点 / 资源 | 笔记 |
|---|---|---|---|
