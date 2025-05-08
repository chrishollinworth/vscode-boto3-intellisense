"""
Type annotations for appconfig service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import DeletionProtectionSettingsTypeDef

    data: DeletionProtectionSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ActionPointType,
    DeletionProtectionCheckType,
    DeploymentEventTypeType,
    DeploymentStateType,
    EnvironmentStateType,
    GrowthTypeType,
    ReplicateToType,
    TriggeredByType,
    ValidatorTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountSettingsTypeDef",
    "ActionInvocationTypeDef",
    "ActionTypeDef",
    "ApplicationResponseTypeDef",
    "ApplicationTypeDef",
    "ApplicationsTypeDef",
    "AppliedExtensionTypeDef",
    "BlobTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateConfigurationProfileRequestTypeDef",
    "CreateDeploymentStrategyRequestTypeDef",
    "CreateEnvironmentRequestTypeDef",
    "CreateExtensionAssociationRequestTypeDef",
    "CreateExtensionRequestTypeDef",
    "CreateHostedConfigurationVersionRequestTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteConfigurationProfileRequestTypeDef",
    "DeleteDeploymentStrategyRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DeleteExtensionAssociationRequestTypeDef",
    "DeleteExtensionRequestTypeDef",
    "DeleteHostedConfigurationVersionRequestTypeDef",
    "DeletionProtectionSettingsTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentStrategyResponseTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EnvironmentsTypeDef",
    "ExtensionAssociationSummaryTypeDef",
    "ExtensionAssociationTypeDef",
    "ExtensionAssociationsTypeDef",
    "ExtensionSummaryTypeDef",
    "ExtensionTypeDef",
    "ExtensionsTypeDef",
    "GetApplicationRequestTypeDef",
    "GetConfigurationProfileRequestTypeDef",
    "GetConfigurationRequestTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentRequestWaitTypeDef",
    "GetDeploymentStrategyRequestTypeDef",
    "GetEnvironmentRequestTypeDef",
    "GetEnvironmentRequestWaitTypeDef",
    "GetExtensionAssociationRequestTypeDef",
    "GetExtensionRequestTypeDef",
    "GetHostedConfigurationVersionRequestTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListConfigurationProfilesRequestPaginateTypeDef",
    "ListConfigurationProfilesRequestTypeDef",
    "ListDeploymentStrategiesRequestPaginateTypeDef",
    "ListDeploymentStrategiesRequestTypeDef",
    "ListDeploymentsRequestPaginateTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListEnvironmentsRequestPaginateTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListExtensionAssociationsRequestPaginateTypeDef",
    "ListExtensionAssociationsRequestTypeDef",
    "ListExtensionsRequestPaginateTypeDef",
    "ListExtensionsRequestTypeDef",
    "ListHostedConfigurationVersionsRequestPaginateTypeDef",
    "ListHostedConfigurationVersionsRequestTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "MonitorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestTypeDef",
    "StopDeploymentRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateConfigurationProfileRequestTypeDef",
    "UpdateDeploymentStrategyRequestTypeDef",
    "UpdateEnvironmentRequestTypeDef",
    "UpdateExtensionAssociationRequestTypeDef",
    "UpdateExtensionRequestTypeDef",
    "ValidateConfigurationRequestTypeDef",
    "ValidatorTypeDef",
    "WaiterConfigTypeDef",
)

class DeletionProtectionSettingsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    ProtectionPeriodInMinutes: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ActionInvocationTypeDef(TypedDict):
    ExtensionIdentifier: NotRequired[str]
    ActionName: NotRequired[str]
    Uri: NotRequired[str]
    RoleArn: NotRequired[str]
    ErrorMessage: NotRequired[str]
    ErrorCode: NotRequired[str]
    InvocationId: NotRequired[str]

class ActionTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Uri: NotRequired[str]
    RoleArn: NotRequired[str]

class ApplicationTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]

class AppliedExtensionTypeDef(TypedDict):
    ExtensionId: NotRequired[str]
    ExtensionAssociationId: NotRequired[str]
    VersionNumber: NotRequired[int]
    Parameters: NotRequired[Dict[str, str]]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "LocationUri": NotRequired[str],
        "ValidatorTypes": NotRequired[List[ValidatorTypeType]],
        "Type": NotRequired[str],
    },
)
ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)

class CreateApplicationRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateDeploymentStrategyRequestTypeDef(TypedDict):
    Name: str
    DeploymentDurationInMinutes: int
    GrowthFactor: float
    Description: NotRequired[str]
    FinalBakeTimeInMinutes: NotRequired[int]
    GrowthType: NotRequired[GrowthTypeType]
    ReplicateTo: NotRequired[ReplicateToType]
    Tags: NotRequired[Mapping[str, str]]

class MonitorTypeDef(TypedDict):
    AlarmArn: str
    AlarmRoleArn: NotRequired[str]

class CreateExtensionAssociationRequestTypeDef(TypedDict):
    ExtensionIdentifier: str
    ResourceIdentifier: str
    ExtensionVersionNumber: NotRequired[int]
    Parameters: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Mapping[str, str]]

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Description": NotRequired[str],
        "Required": NotRequired[bool],
        "Dynamic": NotRequired[bool],
    },
)

class DeleteApplicationRequestTypeDef(TypedDict):
    ApplicationId: str

class DeleteConfigurationProfileRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    DeletionProtectionCheck: NotRequired[DeletionProtectionCheckType]

class DeleteDeploymentStrategyRequestTypeDef(TypedDict):
    DeploymentStrategyId: str

class DeleteEnvironmentRequestTypeDef(TypedDict):
    EnvironmentId: str
    ApplicationId: str
    DeletionProtectionCheck: NotRequired[DeletionProtectionCheckType]

class DeleteExtensionAssociationRequestTypeDef(TypedDict):
    ExtensionAssociationId: str

class DeleteExtensionRequestTypeDef(TypedDict):
    ExtensionIdentifier: str
    VersionNumber: NotRequired[int]

class DeleteHostedConfigurationVersionRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int

class DeploymentStrategyTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    DeploymentDurationInMinutes: NotRequired[int]
    GrowthType: NotRequired[GrowthTypeType]
    GrowthFactor: NotRequired[float]
    FinalBakeTimeInMinutes: NotRequired[int]
    ReplicateTo: NotRequired[ReplicateToType]

class DeploymentSummaryTypeDef(TypedDict):
    DeploymentNumber: NotRequired[int]
    ConfigurationName: NotRequired[str]
    ConfigurationVersion: NotRequired[str]
    DeploymentDurationInMinutes: NotRequired[int]
    GrowthType: NotRequired[GrowthTypeType]
    GrowthFactor: NotRequired[float]
    FinalBakeTimeInMinutes: NotRequired[int]
    State: NotRequired[DeploymentStateType]
    PercentageComplete: NotRequired[float]
    StartedAt: NotRequired[datetime]
    CompletedAt: NotRequired[datetime]
    VersionLabel: NotRequired[str]

class ExtensionAssociationSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    ExtensionArn: NotRequired[str]
    ResourceArn: NotRequired[str]

class ExtensionSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    VersionNumber: NotRequired[int]
    Arn: NotRequired[str]
    Description: NotRequired[str]

class GetApplicationRequestTypeDef(TypedDict):
    ApplicationId: str

class GetConfigurationProfileRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str

class GetConfigurationRequestTypeDef(TypedDict):
    Application: str
    Environment: str
    Configuration: str
    ClientId: str
    ClientConfigurationVersion: NotRequired[str]

class GetDeploymentRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetDeploymentStrategyRequestTypeDef(TypedDict):
    DeploymentStrategyId: str

class GetEnvironmentRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str

class GetExtensionAssociationRequestTypeDef(TypedDict):
    ExtensionAssociationId: str

class GetExtensionRequestTypeDef(TypedDict):
    ExtensionIdentifier: str
    VersionNumber: NotRequired[int]

class GetHostedConfigurationVersionRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int

class HostedConfigurationVersionSummaryTypeDef(TypedDict):
    ApplicationId: NotRequired[str]
    ConfigurationProfileId: NotRequired[str]
    VersionNumber: NotRequired[int]
    Description: NotRequired[str]
    ContentType: NotRequired[str]
    VersionLabel: NotRequired[str]
    KmsKeyArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

ListConfigurationProfilesRequestTypeDef = TypedDict(
    "ListConfigurationProfilesRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class ListDeploymentStrategiesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDeploymentsRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEnvironmentsRequestTypeDef(TypedDict):
    ApplicationId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListExtensionAssociationsRequestTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    ExtensionIdentifier: NotRequired[str]
    ExtensionVersionNumber: NotRequired[int]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListExtensionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Name: NotRequired[str]

class ListHostedConfigurationVersionsRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    VersionLabel: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class StartDeploymentRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    KmsKeyIdentifier: NotRequired[str]
    DynamicExtensionParameters: NotRequired[Mapping[str, str]]

class StopDeploymentRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int
    AllowRevert: NotRequired[bool]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationRequestTypeDef(TypedDict):
    ApplicationId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateDeploymentStrategyRequestTypeDef(TypedDict):
    DeploymentStrategyId: str
    Description: NotRequired[str]
    DeploymentDurationInMinutes: NotRequired[int]
    FinalBakeTimeInMinutes: NotRequired[int]
    GrowthFactor: NotRequired[float]
    GrowthType: NotRequired[GrowthTypeType]

class UpdateExtensionAssociationRequestTypeDef(TypedDict):
    ExtensionAssociationId: str
    Parameters: NotRequired[Mapping[str, str]]

class ValidateConfigurationRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str

class UpdateAccountSettingsRequestTypeDef(TypedDict):
    DeletionProtection: NotRequired[DeletionProtectionSettingsTypeDef]

class AccountSettingsTypeDef(TypedDict):
    DeletionProtection: DeletionProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationResponseTypeDef(TypedDict):
    Id: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationTypeDef(TypedDict):
    Content: StreamingBody
    ConfigurationVersion: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentStrategyResponseTypeDef(TypedDict):
    Id: str
    Name: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    ReplicateTo: ReplicateToType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionAssociationTypeDef(TypedDict):
    Id: str
    ExtensionArn: str
    ResourceArn: str
    Arn: str
    Parameters: Dict[str, str]
    ExtensionVersionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class HostedConfigurationVersionTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    Content: StreamingBody
    ContentType: str
    VersionLabel: str
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTagsTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentEventTypeDef(TypedDict):
    EventType: NotRequired[DeploymentEventTypeType]
    TriggeredBy: NotRequired[TriggeredByType]
    Description: NotRequired[str]
    ActionInvocations: NotRequired[List[ActionInvocationTypeDef]]
    OccurredAt: NotRequired[datetime]

class ApplicationsTypeDef(TypedDict):
    Items: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateHostedConfigurationVersionRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    Content: BlobTypeDef
    ContentType: str
    Description: NotRequired[str]
    LatestVersionNumber: NotRequired[int]
    VersionLabel: NotRequired[str]

class ConfigurationProfilesTypeDef(TypedDict):
    Items: List[ConfigurationProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ConfigurationProfileTypeDef = TypedDict(
    "ConfigurationProfileTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List[ValidatorTypeDef],
        "Type": str,
        "KmsKeyArn": str,
        "KmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfigurationProfileRequestTypeDef = TypedDict(
    "CreateConfigurationProfileRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "LocationUri": str,
        "Description": NotRequired[str],
        "RetrievalRoleArn": NotRequired[str],
        "Validators": NotRequired[Sequence[ValidatorTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
        "KmsKeyIdentifier": NotRequired[str],
    },
)

class UpdateConfigurationProfileRequestTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    RetrievalRoleArn: NotRequired[str]
    Validators: NotRequired[Sequence[ValidatorTypeDef]]
    KmsKeyIdentifier: NotRequired[str]

class CreateEnvironmentRequestTypeDef(TypedDict):
    ApplicationId: str
    Name: str
    Description: NotRequired[str]
    Monitors: NotRequired[Sequence[MonitorTypeDef]]
    Tags: NotRequired[Mapping[str, str]]

class EnvironmentResponseTypeDef(TypedDict):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    State: EnvironmentStateType
    Monitors: List[MonitorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentTypeDef(TypedDict):
    ApplicationId: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[EnvironmentStateType]
    Monitors: NotRequired[List[MonitorTypeDef]]

class UpdateEnvironmentRequestTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Monitors: NotRequired[Sequence[MonitorTypeDef]]

class CreateExtensionRequestTypeDef(TypedDict):
    Name: str
    Actions: Mapping[ActionPointType, Sequence[ActionTypeDef]]
    Description: NotRequired[str]
    Parameters: NotRequired[Mapping[str, ParameterTypeDef]]
    Tags: NotRequired[Mapping[str, str]]
    LatestVersionNumber: NotRequired[int]

class ExtensionTypeDef(TypedDict):
    Id: str
    Name: str
    VersionNumber: int
    Arn: str
    Description: str
    Actions: Dict[ActionPointType, List[ActionTypeDef]]
    Parameters: Dict[str, ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExtensionRequestTypeDef(TypedDict):
    ExtensionIdentifier: str
    Description: NotRequired[str]
    Actions: NotRequired[Mapping[ActionPointType, Sequence[ActionTypeDef]]]
    Parameters: NotRequired[Mapping[str, ParameterTypeDef]]
    VersionNumber: NotRequired[int]

class DeploymentStrategiesTypeDef(TypedDict):
    Items: List[DeploymentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DeploymentsTypeDef(TypedDict):
    Items: List[DeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExtensionAssociationsTypeDef(TypedDict):
    Items: List[ExtensionAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExtensionsTypeDef(TypedDict):
    Items: List[ExtensionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDeploymentRequestWaitTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetEnvironmentRequestWaitTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class HostedConfigurationVersionsTypeDef(TypedDict):
    Items: List[HostedConfigurationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListConfigurationProfilesRequestPaginateTypeDef = TypedDict(
    "ListConfigurationProfilesRequestPaginateTypeDef",
    {
        "ApplicationId": str,
        "Type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListDeploymentStrategiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeploymentsRequestPaginateTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsRequestPaginateTypeDef(TypedDict):
    ApplicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExtensionAssociationsRequestPaginateTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    ExtensionIdentifier: NotRequired[str]
    ExtensionVersionNumber: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExtensionsRequestPaginateTypeDef(TypedDict):
    Name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHostedConfigurationVersionsRequestPaginateTypeDef(TypedDict):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionLabel: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DeploymentTypeDef(TypedDict):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    DeploymentNumber: int
    ConfigurationName: str
    ConfigurationLocationUri: str
    ConfigurationVersion: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    State: DeploymentStateType
    EventLog: List[DeploymentEventTypeDef]
    PercentageComplete: float
    StartedAt: datetime
    CompletedAt: datetime
    AppliedExtensions: List[AppliedExtensionTypeDef]
    KmsKeyArn: str
    KmsKeyIdentifier: str
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentsTypeDef(TypedDict):
    Items: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
