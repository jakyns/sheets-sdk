# Sheets SDK

## Dependencies

- Python 3.6 or higher
- [Pipfile](https://github.com/pypa/pipfile)
- [Google Cloud Account](https://cloud.google.com)

# Google Sheets

## Configuration

- APIs & Services (Google Cloud)
  - Enable Google Sheets API.
  - Create service account.
  - Add role as at least `Project -> Editor`.

- Google Sheets
  - Add service account for granting access to any sheet you want 

## Installation

Copy environment file `.env.xxx` to  `.env` according to your environment and add necessary values below.

```sh
SPREADSHEET_ID=
GOOGLE_SERVICE_ACCOUNT=
```

Initiate virtual environment and generate Pipfile and Pipfile.lock by running:

```sh
pipenv lock
```

Install dependencies and get into virtual environment.

```sh
pipenv install && pipenv shell
```

Pipenv will automatically loads environment varibles from `.env` variables, 
if they exist.

## Usage

For basic usage, you can use the module in your application by importing the
`sheets` module.

```python
>>> import sheets
```

Define example class that want to integrate with Google Sheets API.

```python
>>> class SampleSheet(sheets.GoogleSheets):
>>>    SHEET_NAME = "Sheet1"
>>>    SHEET_COLUMNS = {"name": "A", "code": "B"}
>>>
>>> sample_sheet = SampleSheet()
```

After credentials and constants are set, you can play with Google Sheets API. 

### List all headers

```python
>>> sample_sheet.get_all_headers()
["name", "code"]
```

### Get specific cell

```python
>>> column_name = "name"
>>> cell_no = 2
>>>
>>> sample_sheet.get_specific_cell(column_name, cell_no)
["A2"]
```

### Get multiple cells range

```python
>>> column_name = "name"
>>> cell_range = [2, 3]
>>>
>>> sample_sheet.get_multiple_cell_ranges(column_name, cell_range)
["A2", "A3"]
```

### Get all cells by column name

```python
>>> column_name = "code"
>>>
>>> sample_sheet.get_all_cells_by_column_name(column_name)
["B2", "B3"]
```

### Find row number by value

```python
>>> column_name = "code"
>>> value = "A2"
>>>
>>> sample_sheet.find_row_number_by_value(column_name, value)
2
```

### Update specific cell

```python
>>> column_name = "name"
>>> cell_no = 2
>>> new_value = "AA2"
>>>
>>> sample_sheet.update_specific_cell(column_name, cell_no, new_value)
True
```

### Append new rows

```python
>>> new_values = [["1", "A4"], ["2", "A5"]]
>>>
>>> sample_sheet.append_new_rows(new_values)
True
```
