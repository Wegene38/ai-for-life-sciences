# 12 · 工具与算力

[← 返回资源库](README.md)

## 免费算力

| 平台 | 说明 |
|---|---|
| ⭐ [Google Colab](https://colab.research.google.com/) | 免费 GPU（有时长和资源限制），本课程练习默认环境 |
| ⭐ [Kaggle Notebooks](https://www.kaggle.com/code) | 每周有免费 GPU 配额（以官网为准），数据集丰富 |
| [Hugging Face Spaces](https://huggingface.co/spaces) | 托管与试用模型 Demo |
| [AlphaFold Server](https://alphafoldserver.com/) | 网页端免费运行 AlphaFold3（非商业用途，有每日配额） |
| 🇨🇳 [魔搭 ModelScope](https://modelscope.cn/) | 国内模型社区，提供 Notebook 算力（免费额度以官网为准） |
| 🇨🇳 [百度 AI Studio](https://aistudio.baidu.com/) | 国内在线 Notebook 与算力（免费额度以官网为准） |

## 国内学习者提示

- YouTube、Google Colab、Hugging Face 在部分网络环境下无法直接访问。很多课程在 B 站有官方或搬运版本（见 [14 中文资源汇总](14-chinese-resources.md)）。
- pip 与 conda 换源：参考清华 TUNA 的 [Anaconda 镜像帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)；pip 可运行 `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`。
- Hugging Face 模型可尝试社区镜像 [hf-mirror.com](https://hf-mirror.com/)（设置环境变量 `HF_ENDPOINT=https://hf-mirror.com`）。
- 没有 GPU 时：先用小数据、小模型在 CPU 上跑通逻辑，再迁移到 Kaggle / Colab / 国内平台。

## 核心软件库

| 类别 | 库 |
|---|---|
| 深度学习 | [PyTorch](https://pytorch.org/) · [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/) · [Hugging Face Transformers](https://huggingface.co/docs/transformers) · [PEFT](https://huggingface.co/docs/peft) |
| 图与几何 | [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/) · [e3nn](https://e3nn.org/) |
| 传统 ML | [scikit-learn](https://scikit-learn.org/) · [XGBoost](https://xgboost.readthedocs.io/) |
| 可解释性 | [Captum](https://captum.ai/) |
| 序列与结构 | [Biopython](https://biopython.org/) · [ESM](https://github.com/facebookresearch/esm) · [ColabFold](https://github.com/sokrypton/ColabFold) |
| 化学 | [RDKit](https://github.com/rdkit/rdkit) · [Chemprop](https://github.com/chemprop/chemprop) · [DeepChem](https://github.com/deepchem/deepchem) |
| 单细胞 | [scanpy](https://scanpy.readthedocs.io/) · [scvi-tools](https://docs.scvi-tools.org/) · [squidpy](https://squidpy.readthedocs.io/) |
| 影像 | [napari](https://napari.org/) · [Cellpose](https://www.cellpose.org/) · [MONAI](https://github.com/Project-MONAI/tutorials) |
| 分子模拟 | [OpenMM](https://openmm.org/) |
| 生信命令行工具 | [Bioconda](https://bioconda.github.io/)（samtools、bwa 等，支持 Linux 和 macOS） |
| Notebook 与版本控制 | [nbstripout](https://github.com/kynan/nbstripout)（提交时清除输出） · [Jupytext](https://github.com/mwouts/jupytext)（Notebook 与 .py 互相同步） |
| GitHub | [GitHub CLI](https://cli.github.com/)（`gh auth login` 登录、在命令行管理仓库） |
| 结构可视化 | [ChimeraX](https://www.cgl.ucsf.edu/chimerax/)（学术免费） · [py3Dmol](https://pypi.org/project/py3Dmol/)（Notebook 内 3D 显示） |

## 环境管理

- 推荐用 [Miniforge](https://github.com/conda-forge/miniforge)（自带 mamba）为每个项目建独立环境，导出 `environment.yml` 以便复现。
- Anaconda 官方的 `defaults` 频道受其服务条款约束，机构用户可能需要付费授权；Miniforge 默认只用社区维护的 conda-forge 频道。
