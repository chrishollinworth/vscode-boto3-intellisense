"""
Main interface for timestream-query service type definitions.

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import EndpointTypeDef

    data: EndpointTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EndpointTypeDef",
    "QueryStatusTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TypeTypeDef",
    "CancelQueryResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DatumTypeDef",
    "RowTypeDef",
    "ColumnInfoTypeDef",
    "PaginatorConfigTypeDef",
    "QueryResponseTypeDef",
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "CachePeriodInMinutes": int})

QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {"ProgressPercentage": float, "CumulativeBytesScanned": int, "CumulativeBytesMetered": int},
    total=False,
)

TimeSeriesDataPointTypeDef = TypedDict(
    "TimeSeriesDataPointTypeDef", {"Time": str, "Value": Dict[str, Any]}
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "ScalarType": Literal[
            "VARCHAR",
            "BOOLEAN",
            "BIGINT",
            "DOUBLE",
            "TIMESTAMP",
            "DATE",
            "TIME",
            "INTERVAL_DAY_TO_SECOND",
            "INTERVAL_YEAR_TO_MONTH",
            "UNKNOWN",
            "INTEGER",
        ],
        "ArrayColumnInfo": Dict[str, Any],
        "TimeSeriesMeasureValueColumnInfo": Dict[str, Any],
        "RowColumnInfo": List[Dict[str, Any]],
    },
    total=False,
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef", {"CancellationMessage": str}, total=False
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef", {"Endpoints": List["EndpointTypeDef"]}
)

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "ScalarValue": str,
        "TimeSeriesValue": List["TimeSeriesDataPointTypeDef"],
        "ArrayValue": List[Dict[str, Any]],
        "RowValue": Dict[str, Any],
        "NullValue": bool,
    },
    total=False,
)

RowTypeDef = TypedDict("RowTypeDef", {"Data": List[Dict[str, Any]]})

_RequiredColumnInfoTypeDef = TypedDict("_RequiredColumnInfoTypeDef", {"Type": "TypeTypeDef"})
_OptionalColumnInfoTypeDef = TypedDict("_OptionalColumnInfoTypeDef", {"Name": str}, total=False)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredQueryResponseTypeDef = TypedDict(
    "_RequiredQueryResponseTypeDef",
    {"QueryId": str, "Rows": List[Dict[str, Any]], "ColumnInfo": List[Dict[str, Any]]},
)
_OptionalQueryResponseTypeDef = TypedDict(
    "_OptionalQueryResponseTypeDef",
    {"NextToken": str, "QueryStatus": "QueryStatusTypeDef"},
    total=False,
)


class QueryResponseTypeDef(_RequiredQueryResponseTypeDef, _OptionalQueryResponseTypeDef):
    pass
