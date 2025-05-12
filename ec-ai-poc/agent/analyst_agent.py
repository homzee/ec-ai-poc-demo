
import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import requests
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def assign_roi_grade(roi):
    if roi >= 0.012:
        return "A", "🔥 推广强化"
    elif roi >= 0.008:
        return "B", "✅ 维持"
    elif roi >= 0.005:
        return "C", "⚠️ 页面优化"
    else:
        return "D", "❗ 紧急改善"

def generate_analysis(df):
    # 计算 ROI
    df["ROI"] = df["Conversions"] / df["Clicks"]
    df[["等级", "建议标签"]] = df["ROI"].apply(lambda x: pd.Series(assign_roi_grade(x)))
    df_sorted = df.sort_values("ROI", ascending=False)
    table_str = df_sorted[["Product", "Sales", "Clicks", "Conversions", "ROI", "等级", "建议标签"]].to_markdown(index=False)

    # GPT Prompt
    prompt = f"""
以下是电商平台各产品的 KPI 数据及 ROI 分析等级与建议标签（已排序）：

{table_str}

请你作为一位资深电商运营分析师，综合数据与等级标签：
1. 总结 A/B/C/D 等级分别代表什么样的产品情况
2. 请挑出 ROI 最低的 1~2 个产品，并给出改善建议（如优化页面、重新定价、调整广告策略等）
3. 对整体表现作出简洁总结

请用简洁中文回答。
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位经验丰富的电商数据分析师。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        summary = response.choices[0].message.content
    except Exception as e:
        summary = f"❗ GPT 分析失败：{str(e)}"

    # 汇总文本
    slack_text = (
        "*📊 ROI评分与策略标签分析表格:*"
        f"```{table_str}```"
        "*🧠 OpenAI 分析摘要:*"
        f"{summary}"
    )

    # 推送到 Slack
    requests.post(SLACK_WEBHOOK_URL, json={"text": slack_text})

    # 保存为 Markdown 报告
    os.makedirs("logs", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"logs/kpi_report_{today}.md", "w", encoding="utf-8") as f:
        f.write(f"# KPI 分析报告 - {today}")
        f.write(f"## 表格分析```{table_str}```")
        f.write(f"## OpenAI 分析摘要{summary}")

    return summary
