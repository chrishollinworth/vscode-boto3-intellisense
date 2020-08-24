"""
Main interface for forecastquery service type definitions.

Usage::

    ```python
    from mypy_boto3_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("DataPointTypeDef", "ForecastTypeDef", "QueryForecastResponseTypeDef")

DataPointTypeDef = TypedDict("DataPointTypeDef", {"Timestamp": str, "Value": float}, total=False)

ForecastTypeDef = TypedDict(
    "ForecastTypeDef", {"Predictions": Dict[str, List["DataPointTypeDef"]]}, total=False
)

QueryForecastResponseTypeDef = TypedDict(
    "QueryForecastResponseTypeDef", {"Forecast": "ForecastTypeDef"}, total=False
)
