# 07 过程留痕

本阶段归档的是**接口文档的生成中间件**。

- `接口文档生成/`：`01~05` 接口抓包文档的分段草稿（`draft.xml`、`part2.xml`、`part3.xml`）、合并终稿（`full.xml`）、合并脚本（`merge.py`）与生成决策记录（`.presentation-decision.json`）
- `merge.py` 按 `draft.xml → part2.xml → part3.xml` 顺序拼接输出 `full.xml`，脚本内 `base` 为原始工作目录的绝对路径，仅作留痕，重新执行需改路径
