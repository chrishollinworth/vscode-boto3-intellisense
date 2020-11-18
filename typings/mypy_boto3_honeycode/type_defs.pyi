"""
Main interface for honeycode service type definitions.

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import ColumnMetadataTypeDef

    data: ColumnMetadataTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ColumnMetadataTypeDef",
    "DataItemTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "GetScreenDataResultTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "VariableValueTypeDef",
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "format": Literal[
            "AUTO",
            "NUMBER",
            "CURRENCY",
            "DATE",
            "TIME",
            "DATE_TIME",
            "PERCENTAGE",
            "TEXT",
            "ACCOUNTING",
            "CONTACT",
            "ROWLINK",
        ],
    },
)

DataItemTypeDef = TypedDict(
    "DataItemTypeDef",
    {
        "overrideFormat": Literal[
            "AUTO",
            "NUMBER",
            "CURRENCY",
            "DATE",
            "TIME",
            "DATE_TIME",
            "PERCENTAGE",
            "TEXT",
            "ACCOUNTING",
            "CONTACT",
            "ROWLINK",
        ],
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

_RequiredResultRowTypeDef = TypedDict(
    "_RequiredResultRowTypeDef", {"dataItems": List["DataItemTypeDef"]}
)
_OptionalResultRowTypeDef = TypedDict("_OptionalResultRowTypeDef", {"rowId": str}, total=False)


class ResultRowTypeDef(_RequiredResultRowTypeDef, _OptionalResultRowTypeDef):
    pass


ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef", {"headers": List["ColumnMetadataTypeDef"], "rows": List["ResultRowTypeDef"]}
)

_RequiredGetScreenDataResultTypeDef = TypedDict(
    "_RequiredGetScreenDataResultTypeDef",
    {"results": Dict[str, "ResultSetTypeDef"], "workbookCursor": int},
)
_OptionalGetScreenDataResultTypeDef = TypedDict(
    "_OptionalGetScreenDataResultTypeDef", {"nextToken": str}, total=False
)


class GetScreenDataResultTypeDef(
    _RequiredGetScreenDataResultTypeDef, _OptionalGetScreenDataResultTypeDef
):
    pass


InvokeScreenAutomationResultTypeDef = TypedDict(
    "InvokeScreenAutomationResultTypeDef", {"workbookCursor": int}
)

VariableValueTypeDef = TypedDict("VariableValueTypeDef", {"rawValue": str})
