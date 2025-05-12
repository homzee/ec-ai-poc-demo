import schedule # type: ignore
import time
import subprocess
from datetime import datetime

def run_analysis():
    print(f"[{datetime.now()}] Running KPI analysis...")
    subprocess.run(["python", "app.py"])

# 每天早上9:00自动运行
schedule.every().day.at("16:19").do(run_analysis)

print("✅ 自动调度已启动，等待每日 09:00 执行任务...")
while True:
    schedule.run_pending()
    time.sleep(60)
