"""
Type annotations for forecastquery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DataPointTypeDef",
    "ForecastTypeDef",
    "QueryForecastRequestRequestTypeDef",
    "QueryForecastResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": str,
        "Value": float,
    },
    total=False,
)

ForecastTypeDef = TypedDict(
    "ForecastTypeDef",
    {
        "Predictions": Dict[str, List["DataPointTypeDef"]],
    },
    total=False,
)

_RequiredQueryForecastRequestRequestTypeDef = TypedDict(
    "_RequiredQueryForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
        "Filters": Dict[str, str],
    },
)
_OptionalQueryForecastRequestRequestTypeDef = TypedDict(
    "_OptionalQueryForecastRequestRequestTypeDef",
    {
        "StartDate": str,
        "EndDate": str,
        "NextToken": str,
    },
    total=False,
)

class QueryForecastRequestRequestTypeDef(
    _RequiredQueryForecastRequestRequestTypeDef, _OptionalQueryForecastRequestRequestTypeDef
):
    pass

QueryForecastResponseTypeDef = TypedDict(
    "QueryForecastResponseTypeDef",
    {
        "Forecast": "ForecastTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
