from .base import Base


class Resource(Base):
    def get_cells_by_range(self, cell_range):
        try:
            result = (
                self.sheets.values()
                .get(spreadsheetId=self.spreadsheet_id, range=cell_range)
                .execute()
            )
            values = result.get("values")
        except Exception:
            values = {}

        return values

    def update_cells_by_range(self, cell_range, value):
        result = (
            self.sheets.values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=cell_range,
                valueInputOption="RAW",
                body=value,
            )
            .execute()
        )

        return result["updatedCells"]

    def get_all_cells_in_column(self, column_id):
        cell_range_exclude_header = f"{column_id}2:{column_id}"

        column_values = self.get_cells_by_range(
            f"{self.SHEET_NAME}!{cell_range_exclude_header}"
        )
        value_list = [val[0] for val in column_values]

        return value_list

    def get_all_headers(self):
        header_values = self.get_cells_by_range(f"{self.SHEET_NAME}!1:1")

        return header_values[0]

    def find_row_number_by_value(self, column_id, value, **kwargs):
        value_list = self.get_all_cells_in_column(column_id)

        case_sensitive = kwargs.get("case_sensitive", True)
        if not case_sensitive:
            value_list = [val.lower() for val in value_list]

        try:
            value_index = value_list.index(value)
        except ValueError:
            raise ValueError("Value is not existed")

        excluded_header_row_number = 2
        value_row = value_index + excluded_header_row_number

        return value_row
