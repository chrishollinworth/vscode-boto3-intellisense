"""
Type annotations for honeycode service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/literals.html)

Usage::

    ```python
    from mypy_boto3_honeycode.literals import ErrorCodeType

    data: ErrorCodeType = "ACCESS_DENIED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ErrorCodeType",
    "FormatType",
    "ImportDataCharacterEncodingType",
    "ImportSourceDataFormatType",
    "ListTableColumnsPaginatorName",
    "ListTableRowsPaginatorName",
    "ListTablesPaginatorName",
    "QueryTableRowsPaginatorName",
    "TableDataImportJobStatusType",
    "UpsertActionType",
)

ErrorCodeType = Literal[
    "ACCESS_DENIED",
    "FILE_EMPTY_ERROR",
    "FILE_NOT_FOUND_ERROR",
    "FILE_PARSING_ERROR",
    "FILE_SIZE_LIMIT_ERROR",
    "INVALID_FILE_TYPE_ERROR",
    "INVALID_IMPORT_OPTIONS_ERROR",
    "INVALID_TABLE_COLUMN_ID_ERROR",
    "INVALID_TABLE_ID_ERROR",
    "INVALID_URL_ERROR",
    "RESOURCE_NOT_FOUND_ERROR",
    "SYSTEM_LIMIT_ERROR",
    "TABLE_NOT_FOUND_ERROR",
    "UNKNOWN_ERROR",
]
FormatType = Literal[
    "ACCOUNTING",
    "AUTO",
    "CONTACT",
    "CURRENCY",
    "DATE",
    "DATE_TIME",
    "NUMBER",
    "PERCENTAGE",
    "ROWLINK",
    "ROWSET",
    "TEXT",
    "TIME",
]
ImportDataCharacterEncodingType = Literal[
    "ISO-8859-1", "US-ASCII", "UTF-16", "UTF-16BE", "UTF-16LE", "UTF-8"
]
ImportSourceDataFormatType = Literal["DELIMITED_TEXT"]
ListTableColumnsPaginatorName = Literal["list_table_columns"]
ListTableRowsPaginatorName = Literal["list_table_rows"]
ListTablesPaginatorName = Literal["list_tables"]
QueryTableRowsPaginatorName = Literal["query_table_rows"]
TableDataImportJobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"]
UpsertActionType = Literal["APPENDED", "UPDATED"]
