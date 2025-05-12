import os
from dotenv import load_dotenv
from google_sheets.sheets_connector import read_kpi_data
from agent.analyst_agent import generate_analysis
from slack.slack_notifier import post_to_slack

load_dotenv()

def main():
    df = read_kpi_data()
    summary = generate_analysis(df)
    post_to_slack(summary)

if __name__ == '__main__':
    main()
