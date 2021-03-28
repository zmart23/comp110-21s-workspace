"""Utility functions for wrangling data."""

__author__ = "730317621"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


# def column_values(row: list[dict[str, str]], column: str) -> list[str]:
#     """Produce a list of all values in a single column whose name is the second parameter."""
#     column_val: list[str] = []
#     for line in row:
#         column_val.append(line[column])
#     return column_val


# def columnar(rowed: list[dict[str, str]]) -> dict[str, list[str]]:
#     """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
#     row_column: dict[str, list[str]] = {}
#     for row in rowed[0]:
#         row_column[row] = column_values(rowed, row)
#     return row_column


# def head(rowing: dict[str, list[str]], columning: int) -> dict[str, list[str]]:
#     rowing_columning: dict[str, list[str]] = {}
#     for column in rowing:
#         first_values: list[str] = []
#         for i in range(columning):
#             first_values.append(rowing[column][i])
#         rowing_columning[column] = first_values
#     return rowing_columning


# def select(ro: dict[str, list[str]], col: list[str]) -> dict[str, list[str]]:
#     ro_col: dict[str, list[str]] = {}
#     for column in col:
#         ro_col[column] = ro[column]
#     return ro_col