from .base import Base


class Resource(Base):
    def get_specific_cell(self, column_name: str, cell_no: int) -> str:
        sheet_column = self.SHEET_COLUMNS[column_name]
        cell_range = f"{sheet_column}{cell_no}"

        values = self.__read_single_range(f"{self.SHEET_NAME}!{cell_range}")[0][0]

        return values

    def get_multiple_cell_ranges(self, column_name: str, cell_range: list) -> list:
        sheet_column = self.SHEET_COLUMNS[column_name]
        ranges = f"{sheet_column}{cell_range[0]}:{sheet_column}{cell_range[1]}"

        values = self.__read_multiple_ranges(f"{self.SHEET_NAME}!{ranges}")[0]["values"]

        return [val[0] for val in values]

    def get_all_cells_by_column_name(self, column_name: str) -> list:
        sheet_column = self.SHEET_COLUMNS[column_name]
        ranges = f"{sheet_column}2:{sheet_column}"

        values = self.__read_multiple_ranges(f"{self.SHEET_NAME}!{ranges}")[0]["values"]

        return [val[0] for val in values]

    def find_row_number_by_value(self, column_name: str, value: str, **kwargs) -> int:
        case_sensitive = kwargs.get("case_sensitive", True)
        value_list = self.get_all_cells_by_column(column_name)

        if not case_sensitive:
            value_list = [val.lower() for val in value_list]

        try:
            result_index = value_list.index(value)
        except ValueError:
            raise ValueError("Value is not existed")

        excluded_header_row_number = 2
        row_no = result_index + excluded_header_row_number

        return row_no

    def update_specific_cell(
        self, column_name: str, cell_no: int, new_value: str
    ) -> bool:
        sheet_column = self.SHEET_COLUMNS[column_name]
        cell_range = f"{sheet_column}{cell_no}"
        updated_value = {"values": [[new_value]]}

        result = self.__write_single_range(
            f"{self.SHEET_NAME}!{cell_range}", updated_value
        )
        return True if result else False

    def list_all_headers(self) -> list:
        ranges = "1:1"
        values = self.__read_multiple_ranges(f"{self.SHEET_NAME}!{ranges}")[0]["values"]

        return values[0]

    # private

    def __read_single_range(self, cell_range: str) -> list:
        try:
            result = (
                self.sheets.values()
                .get(spreadsheetId=self.spreadsheet_id, range=cell_range)
                .execute()
            )
            values = result.get("values", [])
        except Exception:
            values = []

        return values

    def __read_multiple_ranges(self, cell_range: str) -> list:
        try:
            result = (
                self.sheets.values()
                .batchGet(spreadsheetId=self.spreadsheet_id, ranges=cell_range)
                .execute()
            )
            values = result.get("valueRanges", [])
        except Exception:
            values = []

        return values

    def __write_single_range(self, cell_range: str, new_value: str) -> int:
        result = (
            self.sheets.values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=cell_range,
                valueInputOption="RAW",
                body=new_value,
            )
            .execute()
        )

        return result["updatedCells"]
