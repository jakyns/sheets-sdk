import json

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


class Authorization:
    def authorize(self):
        service_account_info = self.__load_credential()

        try:
            credentials = service_account.Credentials.from_service_account_info(
                service_account_info, scopes=SCOPES
            )
        except ValueError:
            raise ValueError("Permission denied")

        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()

        return sheet

    # private

    def __load_credential(self):
        credential_raw = self.CREDENTIALS

        if credential_raw is None:
            raise AttributeError("Credential is not set")

        return json.loads(credential_raw)
