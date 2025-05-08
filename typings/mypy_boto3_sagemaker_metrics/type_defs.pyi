"""
Type annotations for sagemaker-metrics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sagemaker_metrics.type_defs import MetricQueryTypeDef

    data: MetricQueryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    MetricQueryResultStatusType,
    MetricStatisticType,
    PeriodType,
    PutMetricsErrorCodeType,
    XAxisTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BatchGetMetricsRequestTypeDef",
    "BatchGetMetricsResponseTypeDef",
    "BatchPutMetricsErrorTypeDef",
    "BatchPutMetricsRequestTypeDef",
    "BatchPutMetricsResponseTypeDef",
    "MetricQueryResultTypeDef",
    "MetricQueryTypeDef",
    "RawMetricDataTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
)

class MetricQueryTypeDef(TypedDict):
    MetricName: str
    ResourceArn: str
    MetricStat: MetricStatisticType
    Period: PeriodType
    XAxisType: XAxisTypeType
    Start: NotRequired[int]
    End: NotRequired[int]

class MetricQueryResultTypeDef(TypedDict):
    Status: MetricQueryResultStatusType
    XAxisValues: List[int]
    MetricValues: List[float]
    Message: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchPutMetricsErrorTypeDef(TypedDict):
    Code: NotRequired[PutMetricsErrorCodeType]
    MetricIndex: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class BatchGetMetricsRequestTypeDef(TypedDict):
    MetricQueries: Sequence[MetricQueryTypeDef]

class BatchGetMetricsResponseTypeDef(TypedDict):
    MetricQueryResults: List[MetricQueryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutMetricsResponseTypeDef(TypedDict):
    Errors: List[BatchPutMetricsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RawMetricDataTypeDef(TypedDict):
    MetricName: str
    Timestamp: TimestampTypeDef
    Value: float
    Step: NotRequired[int]

class BatchPutMetricsRequestTypeDef(TypedDict):
    TrialComponentName: str
    MetricData: Sequence[RawMetricDataTypeDef]
