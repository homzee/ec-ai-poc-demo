from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from google_sheets.sheets_connector import read_kpi_data
from agent.analyst_agent import generate_analysis
from slack.slack_notifier import post_to_slack

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Slack Approval Server is running"}

@app.post("/trigger")
def run_kpi_analysis(request: Request):
    try:
        df = read_kpi_data()
        summary = generate_analysis(df)
        post_to_slack(summary)
        return {"status": "success", "message": "KPI 分析已发送至 Slack"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/approve/{task_id}")
def approve_action(task_id: str):
    try:
        df = read_kpi_data()
        summary = generate_analysis(df)
        post_to_slack(f"✅ 审批已通过：{task_id}\n\n{summary}")
        with open(f"logs/{task_id}.md", "w", encoding="utf-8") as logf:
            logf.write(summary)
        return {"status": "approved", "message": f"任务 {task_id} 已执行并记录"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
