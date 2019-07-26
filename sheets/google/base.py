from .authorization import Authorization


class Base(Authorization):
    def __init__(self):
        self.credentials = self.CREDENTIALS
        self.spreadsheet_id = self.SPREADSHEET_ID
        self.sheets = self.authorize()
