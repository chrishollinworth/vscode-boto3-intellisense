"""
Type annotations for sagemaker-edge service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import ChecksumTypeDef

    data: ChecksumTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import DeploymentStatusType, FailureHandlingPolicyType, ModelStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChecksumTypeDef",
    "DefinitionTypeDef",
    "DeploymentModelTypeDef",
    "DeploymentResultTypeDef",
    "EdgeDeploymentTypeDef",
    "EdgeMetricTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDeploymentsResultTypeDef",
    "GetDeviceRegistrationRequestRequestTypeDef",
    "GetDeviceRegistrationResultTypeDef",
    "ModelTypeDef",
    "ResponseMetadataTypeDef",
    "SendHeartbeatRequestRequestTypeDef",
)

ChecksumTypeDef = TypedDict(
    "ChecksumTypeDef",
    {
        "Type": Literal["SHA1"],
        "Sum": str,
    },
    total=False,
)

DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "ModelHandle": str,
        "S3Url": str,
        "Checksum": "ChecksumTypeDef",
        "State": ModelStateType,
    },
    total=False,
)

DeploymentModelTypeDef = TypedDict(
    "DeploymentModelTypeDef",
    {
        "ModelHandle": str,
        "ModelName": str,
        "ModelVersion": str,
        "DesiredState": ModelStateType,
        "State": ModelStateType,
        "Status": DeploymentStatusType,
        "StatusReason": str,
        "RollbackFailureReason": str,
    },
    total=False,
)

DeploymentResultTypeDef = TypedDict(
    "DeploymentResultTypeDef",
    {
        "DeploymentName": str,
        "DeploymentStatus": str,
        "DeploymentStatusMessage": str,
        "DeploymentStartTime": Union[datetime, str],
        "DeploymentEndTime": Union[datetime, str],
        "DeploymentModels": List["DeploymentModelTypeDef"],
    },
    total=False,
)

EdgeDeploymentTypeDef = TypedDict(
    "EdgeDeploymentTypeDef",
    {
        "DeploymentName": str,
        "Type": Literal["Model"],
        "FailureHandlingPolicy": FailureHandlingPolicyType,
        "Definitions": List["DefinitionTypeDef"],
    },
    total=False,
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

GetDeploymentsRequestRequestTypeDef = TypedDict(
    "GetDeploymentsRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)

GetDeploymentsResultTypeDef = TypedDict(
    "GetDeploymentsResultTypeDef",
    {
        "Deployments": List["EdgeDeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "DeploymentResult": "DeploymentResultTypeDef",
    },
    total=False,
)

class SendHeartbeatRequestRequestTypeDef(
    _RequiredSendHeartbeatRequestRequestTypeDef, _OptionalSendHeartbeatRequestRequestTypeDef
):
    pass
