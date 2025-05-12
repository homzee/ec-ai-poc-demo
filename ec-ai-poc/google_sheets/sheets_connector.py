import os
import pandas as pd # type: ignore
import gspread # type: ignore
from oauth2client.service_account import ServiceAccountCredentials # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

def read_kpi_data():
    # Google Sheets 认证
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_path = os.getenv("GOOGLE_CREDS_JSON", "google_sheets/oauth_credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)

    sheet_id = os.getenv("GOOGLE_SHEETS_ID")
    sheet_range = os.getenv("SHEET_RANGE")

    spreadsheet = client.open_by_key(sheet_id)
    sheet = spreadsheet.worksheet(sheet_range.split("!")[0])
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df
