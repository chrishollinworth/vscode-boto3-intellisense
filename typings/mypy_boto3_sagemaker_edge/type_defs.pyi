"""
Main interface for sagemaker-edge service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import EdgeMetricTypeDef

    data: EdgeMetricTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("EdgeMetricTypeDef", "GetDeviceRegistrationResultTypeDef", "ModelTypeDef")

EdgeMetricTypeDef = TypedDict(
    "EdgeMetricTypeDef",
    {"Dimension": str, "MetricName": str, "Value": float, "Timestamp": datetime},
    total=False,
)

GetDeviceRegistrationResultTypeDef = TypedDict(
    "GetDeviceRegistrationResultTypeDef", {"DeviceRegistration": str, "CacheTTL": str}, total=False
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "LatestSampleTime": datetime,
        "LatestInference": datetime,
        "ModelMetrics": List["EdgeMetricTypeDef"],
    },
    total=False,
)
