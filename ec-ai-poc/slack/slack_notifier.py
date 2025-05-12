import os
import requests
from dotenv import load_dotenv

load_dotenv()

def post_to_slack(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Slack通知失败: {response.status_code} {response.text}")
