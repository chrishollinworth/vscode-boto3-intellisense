"""
Type annotations for sagemaker-edge service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import EdgeMetricTypeDef

    data: EdgeMetricTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "EdgeMetricTypeDef",
    "GetDeviceRegistrationRequestRequestTypeDef",
    "GetDeviceRegistrationResultTypeDef",
    "ModelTypeDef",
    "ResponseMetadataTypeDef",
    "SendHeartbeatRequestRequestTypeDef",
)

EdgeMetricTypeDef = TypedDict(
    "EdgeMetricTypeDef",
    {
        "Dimension": str,
        "MetricName": str,
        "Value": float,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)

GetDeviceRegistrationRequestRequestTypeDef = TypedDict(
    "GetDeviceRegistrationRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)

GetDeviceRegistrationResultTypeDef = TypedDict(
    "GetDeviceRegistrationResultTypeDef",
    {
        "DeviceRegistration": str,
        "CacheTTL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "LatestSampleTime": Union[datetime, str],
        "LatestInference": Union[datetime, str],
        "ModelMetrics": List["EdgeMetricTypeDef"],
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

_RequiredSendHeartbeatRequestRequestTypeDef = TypedDict(
    "_RequiredSendHeartbeatRequestRequestTypeDef",
    {
        "AgentVersion": str,
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
_OptionalSendHeartbeatRequestRequestTypeDef = TypedDict(
    "_OptionalSendHeartbeatRequestRequestTypeDef",
    {
        "AgentMetrics": List["EdgeMetricTypeDef"],
        "Models": List["ModelTypeDef"],
    },
    total=False,
)

class SendHeartbeatRequestRequestTypeDef(
    _RequiredSendHeartbeatRequestRequestTypeDef, _OptionalSendHeartbeatRequestRequestTypeDef
):
    pass
