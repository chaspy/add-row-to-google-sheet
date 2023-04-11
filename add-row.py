import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_service():
    creds = None
    if os.path.exists("service-account.json"):
        creds = service_account.Credentials.from_service_account_file(
            "service-account.json",
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )

    service = build("sheets", "v4", credentials=creds)
    return service

def add_row(sheet_id, range_name, data):
    service = get_service()
    body = {
        "range": range_name,
        "values": [data],
        "majorDimension": "ROWS",
    }
    result = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=sheet_id,
            range=range_name,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body,
        )
        .execute()
    )
    return result

if __name__ == "__main__":
    sheet_id = os.environ["SPREADSHEET_ID"]
    range_name = "Sheet1!A1:Z"  # 適切な範囲を指定してください

    # ここで、追加したいデータのリストを作成します。
    # 例: ["value1", "value2", "value3"]
    data = ["value1","value2","value3"]

    add_row(sheet_id, range_name, data)

