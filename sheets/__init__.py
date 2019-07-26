import os

from .google.authorization import Authorization
from .google.base import Base
from .google.resource import Resource


class GoogleSheets(Resource):
    CREDENTIALS = os.getenv("CREDENTIALS")
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
