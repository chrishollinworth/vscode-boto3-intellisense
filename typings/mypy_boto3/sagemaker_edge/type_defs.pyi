"""
Type annotations for sagemaker-edge service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import ChecksumTypeDef

    data: ChecksumTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import DeploymentStatusType, FailureHandlingPolicyType, ModelStateType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ChecksumTypeDef",
    "DefinitionTypeDef",
    "DeploymentModelTypeDef",
    "DeploymentResultTypeDef",
    "EdgeDeploymentTypeDef",
    "EdgeMetricTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDeploymentsRequestTypeDef",
    "GetDeploymentsResultTypeDef",
    "GetDeviceRegistrationRequestTypeDef",
    "GetDeviceRegistrationResultTypeDef",
    "ModelTypeDef",
    "ResponseMetadataTypeDef",
    "SendHeartbeatRequestTypeDef",
    "TimestampTypeDef",
)

ChecksumTypeDef = TypedDict(
    "ChecksumTypeDef",
    {
        "Type": NotRequired[Literal["SHA1"]],
        "Sum": NotRequired[str],
    },
)

class DeploymentModelTypeDef(TypedDict):
    ModelHandle: NotRequired[str]
    ModelName: NotRequired[str]
    ModelVersion: NotRequired[str]
    DesiredState: NotRequired[ModelStateType]
    State: NotRequired[ModelStateType]
    Status: NotRequired[DeploymentStatusType]
    StatusReason: NotRequired[str]
    RollbackFailureReason: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetDeploymentsRequestTypeDef(TypedDict):
    DeviceName: str
    DeviceFleetName: str

class GetDeviceRegistrationRequestTypeDef(TypedDict):
    DeviceName: str
    DeviceFleetName: str

class DefinitionTypeDef(TypedDict):
    ModelHandle: NotRequired[str]
    S3Url: NotRequired[str]
    Checksum: NotRequired[ChecksumTypeDef]
    State: NotRequired[ModelStateType]

class DeploymentResultTypeDef(TypedDict):
    DeploymentName: NotRequired[str]
    DeploymentStatus: NotRequired[str]
    DeploymentStatusMessage: NotRequired[str]
    DeploymentStartTime: NotRequired[TimestampTypeDef]
    DeploymentEndTime: NotRequired[TimestampTypeDef]
    DeploymentModels: NotRequired[Sequence[DeploymentModelTypeDef]]

class EdgeMetricTypeDef(TypedDict):
    Dimension: NotRequired[str]
    MetricName: NotRequired[str]
    Value: NotRequired[float]
    Timestamp: NotRequired[TimestampTypeDef]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceRegistrationResultTypeDef(TypedDict):
    DeviceRegistration: str
    CacheTTL: str
    ResponseMetadata: ResponseMetadataTypeDef

EdgeDeploymentTypeDef = TypedDict(
    "EdgeDeploymentTypeDef",
    {
        "DeploymentName": NotRequired[str],
        "Type": NotRequired[Literal["Model"]],
        "FailureHandlingPolicy": NotRequired[FailureHandlingPolicyType],
        "Definitions": NotRequired[List[DefinitionTypeDef]],
    },
)

class ModelTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelVersion: NotRequired[str]
    LatestSampleTime: NotRequired[TimestampTypeDef]
    LatestInference: NotRequired[TimestampTypeDef]
    ModelMetrics: NotRequired[Sequence[EdgeMetricTypeDef]]

class GetDeploymentsResultTypeDef(TypedDict):
    Deployments: List[EdgeDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendHeartbeatRequestTypeDef(TypedDict):
    AgentVersion: str
    DeviceName: str
    DeviceFleetName: str
    AgentMetrics: NotRequired[Sequence[EdgeMetricTypeDef]]
    Models: NotRequired[Sequence[ModelTypeDef]]
    DeploymentResult: NotRequired[DeploymentResultTypeDef]
