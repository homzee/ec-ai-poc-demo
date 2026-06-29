# 中亚 / Ozon 电商 AI 落地 Demo

公开演示地址：

https://homzee.github.io/ec-ai-poc-demo/

这是一个面向中亚与俄语区电商客户的 AI 落地 Demo，用于展示 SKU 利润测算、风险评分、俄语 Listing、图片合规检查、驳回处理、客服草稿、海外仓补货、智能定价和业务流程。

## 演示定位

第一期 PoC 先验证辅助决策与资料生成，不直接自动上架，不自动回复真实客户。后续可接入 Ozon/Kaspi API、Ollama/Qwen 本地模型、知识库、n8n 编排与通知审批。


## 继续开发交接

当前仓库保留三部分内容：

- `index.html`：面向客户演示的静态网页，可直接通过 GitHub Pages 或本地静态服务预览。
- `data/skus.json`：当前 Demo 的 SKU 示例数据源，用于驱动总览、库存、选品和 SKU 分析模块。
- `ec-ai-poc/`：早期 KPI/Slack PoC 代码，可作为后续自动化分析与通知模块的参考。

建议后续开发顺序：

1. 整理客户真实 SKU 表，沉淀成统一 CSV/JSON 数据源。
2. 将 `index.html` 中的示例 SKU、库存、评分和俄语文案改为数据驱动。（已先接入 `data/skus.json` 示例数据源）
3. 接入本地 Ollama/Qwen 生成 Listing、驳回处理建议和客服草稿。
4. 加入人工审核、通知审批和平台 API 对接，避免直接自动上架或自动回复真实客户。

本地预览：

```bash
python -m http.server 8765
```

然后打开 `http://localhost:8765/`。
