# EC自動分析PoCシステム（フェーズ1対応）

本リポジトリは、Slackを起点としたAIドリブンEC分析PoCの構築成果物です。  
クラウドワークス掲載案件「Googleスプレッドシート連携 + AI施策提案 + Slack承認実装」に準拠しています。

## ✅ 主な機能

- Google SheetsのKPIデータ自動取得（OAuth認証）
- OpenAI GPT-3.5によるROIスコアリングと施策提案
- Slackへ要約 + 承認ボタン投稿
- /approve, /reject エンドポイントでワンクリック実装可能
- Markdownログ自動保存（logs/）
- Windows用batファイル付き：run_daily.bat

## 🚀 エンドポイント構成（FastAPI）

| メソッド | パス | 説明 |
|----------|------|------|
| GET | `/` | サーバ稼働確認 |
| POST | `/trigger` | 分析+Slack送信 |
| POST | `/approve` | ユーザーが承認した際の処理 |
| POST | `/reject` | ユーザーが却下した際の処理 |

## 🐳 Docker利用方法

```bash
docker build -t slack-approver .
docker run -d -p 8000:8000 --env-file .env slack-approver
```

## 📎 必要な環境変数（.env）

```dotenv
OPENAI_API_KEY=sk-xxxxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxxx
SLACK_APPROVAL_URL=http://localhost:8000
GOOGLE_SHEET_ID=スプレッドシートID
```
