"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import CancelQueryRequestRequestTypeDef

    data: CancelQueryRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ScalarTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ColumnInfoTypeDef",
    "DatumTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "EndpointTypeDef",
    "PaginatorConfigTypeDef",
    "QueryRequestRequestTypeDef",
    "QueryResponseTypeDef",
    "QueryStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TypeTypeDef",
)

CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "CancellationMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredColumnInfoTypeDef = TypedDict(
    "_RequiredColumnInfoTypeDef",
    {
        "Type": Dict[str, Any],
    },
)
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "ScalarValue": str,
        "TimeSeriesValue": List[Dict[str, Any]],
        "ArrayValue": List[Dict[str, Any]],
        "RowValue": Dict[str, Any],
        "NullValue": bool,
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredQueryRequestRequestTypeDef = TypedDict(
    "_RequiredQueryRequestRequestTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalQueryRequestRequestTypeDef = TypedDict(
    "_OptionalQueryRequestRequestTypeDef",
    {
        "ClientToken": str,
        "NextToken": str,
        "MaxRows": int,
    },
    total=False,
)

class QueryRequestRequestTypeDef(
    _RequiredQueryRequestRequestTypeDef, _OptionalQueryRequestRequestTypeDef
):
    pass

QueryResponseTypeDef = TypedDict(
    "QueryResponseTypeDef",
    {
        "QueryId": str,
        "NextToken": str,
        "Rows": List["RowTypeDef"],
        "ColumnInfo": List["ColumnInfoTypeDef"],
        "QueryStatus": "QueryStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {
        "ProgressPercentage": float,
        "CumulativeBytesScanned": int,
        "CumulativeBytesMetered": int,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List[Dict[str, Any]],
    },
)

TimeSeriesDataPointTypeDef = TypedDict(
    "TimeSeriesDataPointTypeDef",
    {
        "Time": str,
        "Value": "DatumTypeDef",
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "ScalarType": ScalarTypeType,
        "ArrayColumnInfo": Dict[str, Any],
        "TimeSeriesMeasureValueColumnInfo": Dict[str, Any],
        "RowColumnInfo": List[Dict[str, Any]],
    },
    total=False,
)
