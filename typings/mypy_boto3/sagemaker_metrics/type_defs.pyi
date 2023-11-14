"""
Type annotations for sagemaker-metrics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_metrics.type_defs import BatchPutMetricsErrorTypeDef

    data: BatchPutMetricsErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import PutMetricsErrorCodeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchPutMetricsErrorTypeDef",
    "BatchPutMetricsRequestRequestTypeDef",
    "BatchPutMetricsResponseTypeDef",
    "RawMetricDataTypeDef",
    "ResponseMetadataTypeDef",
)

BatchPutMetricsErrorTypeDef = TypedDict(
    "BatchPutMetricsErrorTypeDef",
    {
        "Code": PutMetricsErrorCodeType,
        "MetricIndex": int,
    },
    total=False,
)

BatchPutMetricsRequestRequestTypeDef = TypedDict(
    "BatchPutMetricsRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "MetricData": List["RawMetricDataTypeDef"],
    },
)

BatchPutMetricsResponseTypeDef = TypedDict(
    "BatchPutMetricsResponseTypeDef",
    {
        "Errors": List["BatchPutMetricsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRawMetricDataTypeDef = TypedDict(
    "_RequiredRawMetricDataTypeDef",
    {
        "MetricName": str,
        "Timestamp": Union[datetime, str],
        "Value": float,
    },
)
_OptionalRawMetricDataTypeDef = TypedDict(
    "_OptionalRawMetricDataTypeDef",
    {
        "Step": int,
    },
    total=False,
)

class RawMetricDataTypeDef(_RequiredRawMetricDataTypeDef, _OptionalRawMetricDataTypeDef):
    pass

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
