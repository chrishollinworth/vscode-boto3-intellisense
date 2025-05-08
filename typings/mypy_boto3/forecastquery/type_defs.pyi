"""
Type annotations for forecastquery service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping
else:
    from typing import Dict, List, Mapping
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DataPointTypeDef",
    "ForecastTypeDef",
    "QueryForecastRequestTypeDef",
    "QueryForecastResponseTypeDef",
    "QueryWhatIfForecastRequestTypeDef",
    "QueryWhatIfForecastResponseTypeDef",
    "ResponseMetadataTypeDef",
)

class DataPointTypeDef(TypedDict):
    Timestamp: NotRequired[str]
    Value: NotRequired[float]

class QueryForecastRequestTypeDef(TypedDict):
    ForecastArn: str
    Filters: Mapping[str, str]
    StartDate: NotRequired[str]
    EndDate: NotRequired[str]
    NextToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class QueryWhatIfForecastRequestTypeDef(TypedDict):
    WhatIfForecastArn: str
    Filters: Mapping[str, str]
    StartDate: NotRequired[str]
    EndDate: NotRequired[str]
    NextToken: NotRequired[str]

class ForecastTypeDef(TypedDict):
    Predictions: NotRequired[Dict[str, List[DataPointTypeDef]]]

class QueryForecastResponseTypeDef(TypedDict):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryWhatIfForecastResponseTypeDef(TypedDict):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
