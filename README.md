# Google Sheets SDK

## Dependencies

- Python 3.6.x or higher
- [Pipfile](https://github.com/pypa/pipfile)
- [Google Cloud Account](https://cloud.google.com)

## Configuration

- APIs & Services (Google Cloud)
  - Enable Google Sheets API
  - Create service account key credential
  - Choose role as at least `Project -> Editor`

- Google Sheets
  - Add service account for granting access to any sheet you want 

## Installation

Copy environment file `.env.xxx` to  `.env` according to your environment and add necessary values below.

```sh
CREDENTIALS=
SPREADSHEET_ID=
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

```
>>> class SampleSheet(sheets.GoogleSheets):
>>>    SHEET_NAME = "Sheet1"
>>>    SHEET_COLUMNS = {"name": "A", "code": "B"}
>>>
>>> sample_sheet = SampleSheet()
```

After credentials and constants are set, you can play with Google Sheets API. 
For example, to get all data from column `name`:

```python
>>> sample_sheet.get_all_cells_in_column(sample_sheet.SHEET_COLUMNS["name"])
["A2", "A3"]
```

to get all headers:

```python
>>> sample_sheet.get_all_headers()
["name", "code"]
```

to map data with column `name` from cell `A2`

```python
>>> cell_range = "{}{}:{}{}".format(
>>>     sample_sheet.SHEET_COLUMNS["name"],
>>>     range[0],
>>>     sample_sheet.SHEET_COLUMNS["name"],
>>>     range[1],
>>> )
>>>
>>> name_list = sample_sheet.get_cells_by_range(
>>>     "{}!{}".format(sample_sheet.SHEET_NAME, cell_range)
>>> )
>>>
>>> dict(zip(sample_sheet.SHEET_COLUMNS.keys(), name_list[0]))
{"name": ["A2"]}
```

to get row number from value in column `name`

```python
>>> sample_sheet.get_row_number_by_value(
>>>     sample_sheet.SHEET_COLUMNS["name"], "A2"
>>> )
2
```

update specific cell to another value

```python
>>> sample_sheet.update_cells_by_range(
>>>     "{}!{}{}".format(
>>>         sample_sheet.SHEET_NAME, 
>>>         sample_sheet.SHEET_COLUMNS["name"],
>>>         range[0]
>>>     ),
>>>     {"values": [["AA"]]},
>>> )
1
```
