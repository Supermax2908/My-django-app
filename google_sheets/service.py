import os.path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

service_account_file_path = os.path.join(os.path.dirname(__file__), 'service-account.json')

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    service_account_file_path, scope
)


def get_google_sheets_client():
    return gspread.authorize(credentials)


def read_from_sheet(sheet_id, range):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(sheet_id)

    return spreadsheet.values_get(range)


def write_to_sheet(range, data):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    return spreadsheet.values_update(
        range,
        params={'valueInputOption': 'RAW'},
        body={'values': data}
    )


def bulk_write_to_sheet(sheet_id, data):
    client = get_google_sheets_client()
    spreadsheet = client.open_by_key(sheet_id)
    sheet = spreadsheet.sheet1

    # Write to multiple ranges
    request_data = []

    for range_name, values in data.items():
        request_data.append({
            'range': range_name,
            'majorDimension': 'ROWS',
            'values': values
        })

    return sheet.batch_update(request_data)