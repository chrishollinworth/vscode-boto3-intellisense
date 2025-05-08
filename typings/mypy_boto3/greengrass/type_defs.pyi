"""
Type annotations for greengrass service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupRequestTypeDef

    data: AssociateRoleToGroupRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    BulkDeploymentStatusType,
    ConfigurationSyncStatusType,
    DeploymentTypeType,
    EncodingTypeType,
    FunctionIsolationModeType,
    LoggerComponentType,
    LoggerLevelType,
    LoggerTypeType,
    PermissionType,
    SoftwareToUpdateType,
    TelemetryType,
    UpdateAgentLogLevelType,
    UpdateTargetsArchitectureType,
    UpdateTargetsOperatingSystemType,
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
    "AssociateRoleToGroupRequestTypeDef",
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionOutputTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorDefinitionVersionUnionTypeDef",
    "ConnectorOutputTypeDef",
    "ConnectorTypeDef",
    "ConnectorUnionTypeDef",
    "CoreDefinitionVersionOutputTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreDefinitionVersionUnionTypeDef",
    "CoreTypeDef",
    "CreateConnectorDefinitionRequestTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionRequestTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionRequestTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionRequestTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionRequestTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionRequestTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionRequestTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionRequestTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityRequestTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionRequestTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionRequestTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionRequestTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionRequestTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionRequestTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobRequestTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionRequestTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionRequestTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DefinitionInformationTypeDef",
    "DeleteConnectorDefinitionRequestTypeDef",
    "DeleteCoreDefinitionRequestTypeDef",
    "DeleteDeviceDefinitionRequestTypeDef",
    "DeleteFunctionDefinitionRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteLoggerDefinitionRequestTypeDef",
    "DeleteResourceDefinitionRequestTypeDef",
    "DeleteSubscriptionDefinitionRequestTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionOutputTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceDefinitionVersionUnionTypeDef",
    "DeviceTypeDef",
    "DisassociateRoleFromGroupRequestTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentOutputTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationEnvironmentUnionTypeDef",
    "FunctionConfigurationOutputTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionConfigurationUnionTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionOutputTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionDefinitionVersionUnionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionOutputTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "FunctionUnionTypeDef",
    "GetAssociatedRoleRequestTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetBulkDeploymentStatusRequestTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetConnectivityInfoRequestTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetConnectorDefinitionRequestTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetConnectorDefinitionVersionRequestTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "GetCoreDefinitionRequestTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetCoreDefinitionVersionRequestTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "GetDeploymentStatusRequestTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "GetDeviceDefinitionRequestTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetDeviceDefinitionVersionRequestTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "GetFunctionDefinitionRequestTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetFunctionDefinitionVersionRequestTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "GetGroupCertificateAuthorityRequestTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationRequestTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetGroupVersionRequestTypeDef",
    "GetGroupVersionResponseTypeDef",
    "GetLoggerDefinitionRequestTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetLoggerDefinitionVersionRequestTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "GetResourceDefinitionRequestTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetResourceDefinitionVersionRequestTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionRequestTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "GetSubscriptionDefinitionVersionRequestTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "GetThingRuntimeConfigurationRequestTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "ListBulkDeploymentDetailedReportsRequestPaginateTypeDef",
    "ListBulkDeploymentDetailedReportsRequestTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "ListBulkDeploymentsRequestPaginateTypeDef",
    "ListBulkDeploymentsRequestTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "ListConnectorDefinitionVersionsRequestPaginateTypeDef",
    "ListConnectorDefinitionVersionsRequestTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListConnectorDefinitionsRequestPaginateTypeDef",
    "ListConnectorDefinitionsRequestTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsRequestPaginateTypeDef",
    "ListCoreDefinitionVersionsRequestTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsRequestPaginateTypeDef",
    "ListCoreDefinitionsRequestTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeploymentsRequestPaginateTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsRequestPaginateTypeDef",
    "ListDeviceDefinitionVersionsRequestTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsRequestPaginateTypeDef",
    "ListDeviceDefinitionsRequestTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsRequestPaginateTypeDef",
    "ListFunctionDefinitionVersionsRequestTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsRequestPaginateTypeDef",
    "ListFunctionDefinitionsRequestTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupCertificateAuthoritiesRequestTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupVersionsRequestPaginateTypeDef",
    "ListGroupVersionsRequestTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListGroupsRequestPaginateTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsRequestPaginateTypeDef",
    "ListLoggerDefinitionVersionsRequestTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsRequestPaginateTypeDef",
    "ListLoggerDefinitionsRequestTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsRequestPaginateTypeDef",
    "ListResourceDefinitionVersionsRequestTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsRequestPaginateTypeDef",
    "ListResourceDefinitionsRequestTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsRequestPaginateTypeDef",
    "ListSubscriptionDefinitionVersionsRequestTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsRequestPaginateTypeDef",
    "ListSubscriptionDefinitionsRequestTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionOutputTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerDefinitionVersionUnionTypeDef",
    "LoggerTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsRequestTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerOutputTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDataContainerUnionTypeDef",
    "ResourceDefinitionVersionOutputTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDefinitionVersionUnionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceOutputTypeDef",
    "ResourceTypeDef",
    "ResourceUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataOutputTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "SecretsManagerSecretResourceDataUnionTypeDef",
    "StartBulkDeploymentRequestTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "StopBulkDeploymentRequestTypeDef",
    "SubscriptionDefinitionVersionOutputTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionDefinitionVersionUnionTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectivityInfoRequestTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateConnectorDefinitionRequestTypeDef",
    "UpdateCoreDefinitionRequestTypeDef",
    "UpdateDeviceDefinitionRequestTypeDef",
    "UpdateFunctionDefinitionRequestTypeDef",
    "UpdateGroupCertificateConfigurationRequestTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateLoggerDefinitionRequestTypeDef",
    "UpdateResourceDefinitionRequestTypeDef",
    "UpdateSubscriptionDefinitionRequestTypeDef",
    "UpdateThingRuntimeConfigurationRequestTypeDef",
    "VersionInformationTypeDef",
)

class AssociateRoleToGroupRequestTypeDef(TypedDict):
    GroupId: str
    RoleArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateServiceRoleToAccountRequestTypeDef(TypedDict):
    RoleArn: str

class BulkDeploymentMetricsTypeDef(TypedDict):
    InvalidInputRecords: NotRequired[int]
    RecordsProcessed: NotRequired[int]
    RetryAttempts: NotRequired[int]

class ErrorDetailTypeDef(TypedDict):
    DetailedErrorCode: NotRequired[str]
    DetailedErrorMessage: NotRequired[str]

class BulkDeploymentTypeDef(TypedDict):
    BulkDeploymentArn: NotRequired[str]
    BulkDeploymentId: NotRequired[str]
    CreatedAt: NotRequired[str]

class ConnectivityInfoTypeDef(TypedDict):
    HostAddress: NotRequired[str]
    Id: NotRequired[str]
    Metadata: NotRequired[str]
    PortNumber: NotRequired[int]

class ConnectorOutputTypeDef(TypedDict):
    ConnectorArn: str
    Id: str
    Parameters: NotRequired[Dict[str, str]]

class ConnectorTypeDef(TypedDict):
    ConnectorArn: str
    Id: str
    Parameters: NotRequired[Mapping[str, str]]

class CoreTypeDef(TypedDict):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: NotRequired[bool]

class CreateDeploymentRequestTypeDef(TypedDict):
    DeploymentType: DeploymentTypeType
    GroupId: str
    AmznClientToken: NotRequired[str]
    DeploymentId: NotRequired[str]
    GroupVersionId: NotRequired[str]

class DeviceTypeDef(TypedDict):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: NotRequired[bool]

class CreateGroupCertificateAuthorityRequestTypeDef(TypedDict):
    GroupId: str
    AmznClientToken: NotRequired[str]

class GroupVersionTypeDef(TypedDict):
    ConnectorDefinitionVersionArn: NotRequired[str]
    CoreDefinitionVersionArn: NotRequired[str]
    DeviceDefinitionVersionArn: NotRequired[str]
    FunctionDefinitionVersionArn: NotRequired[str]
    LoggerDefinitionVersionArn: NotRequired[str]
    ResourceDefinitionVersionArn: NotRequired[str]
    SubscriptionDefinitionVersionArn: NotRequired[str]

class CreateGroupVersionRequestTypeDef(TypedDict):
    GroupId: str
    AmznClientToken: NotRequired[str]
    ConnectorDefinitionVersionArn: NotRequired[str]
    CoreDefinitionVersionArn: NotRequired[str]
    DeviceDefinitionVersionArn: NotRequired[str]
    FunctionDefinitionVersionArn: NotRequired[str]
    LoggerDefinitionVersionArn: NotRequired[str]
    ResourceDefinitionVersionArn: NotRequired[str]
    SubscriptionDefinitionVersionArn: NotRequired[str]

LoggerTypeDef = TypedDict(
    "LoggerTypeDef",
    {
        "Component": LoggerComponentType,
        "Id": str,
        "Level": LoggerLevelType,
        "Type": LoggerTypeType,
        "Space": NotRequired[int],
    },
)

class CreateSoftwareUpdateJobRequestTypeDef(TypedDict):
    S3UrlSignerRole: str
    SoftwareToUpdate: SoftwareToUpdateType
    UpdateTargets: Sequence[str]
    UpdateTargetsArchitecture: UpdateTargetsArchitectureType
    UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystemType
    AmznClientToken: NotRequired[str]
    UpdateAgentLogLevel: NotRequired[UpdateAgentLogLevelType]

class SubscriptionTypeDef(TypedDict):
    Id: str
    Source: str
    Subject: str
    Target: str

class DefinitionInformationTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreationTimestamp: NotRequired[str]
    Id: NotRequired[str]
    LastUpdatedTimestamp: NotRequired[str]
    LatestVersion: NotRequired[str]
    LatestVersionArn: NotRequired[str]
    Name: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class DeleteConnectorDefinitionRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str

class DeleteCoreDefinitionRequestTypeDef(TypedDict):
    CoreDefinitionId: str

class DeleteDeviceDefinitionRequestTypeDef(TypedDict):
    DeviceDefinitionId: str

class DeleteFunctionDefinitionRequestTypeDef(TypedDict):
    FunctionDefinitionId: str

class DeleteGroupRequestTypeDef(TypedDict):
    GroupId: str

class DeleteLoggerDefinitionRequestTypeDef(TypedDict):
    LoggerDefinitionId: str

class DeleteResourceDefinitionRequestTypeDef(TypedDict):
    ResourceDefinitionId: str

class DeleteSubscriptionDefinitionRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str

class DeploymentTypeDef(TypedDict):
    CreatedAt: NotRequired[str]
    DeploymentArn: NotRequired[str]
    DeploymentId: NotRequired[str]
    DeploymentType: NotRequired[DeploymentTypeType]
    GroupArn: NotRequired[str]

class DisassociateRoleFromGroupRequestTypeDef(TypedDict):
    GroupId: str

class ResourceAccessPolicyTypeDef(TypedDict):
    ResourceId: str
    Permission: NotRequired[PermissionType]

class FunctionRunAsConfigTypeDef(TypedDict):
    Gid: NotRequired[int]
    Uid: NotRequired[int]

class GetAssociatedRoleRequestTypeDef(TypedDict):
    GroupId: str

class GetBulkDeploymentStatusRequestTypeDef(TypedDict):
    BulkDeploymentId: str

class GetConnectivityInfoRequestTypeDef(TypedDict):
    ThingName: str

class GetConnectorDefinitionRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str

class GetConnectorDefinitionVersionRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str
    ConnectorDefinitionVersionId: str
    NextToken: NotRequired[str]

class GetCoreDefinitionRequestTypeDef(TypedDict):
    CoreDefinitionId: str

class GetCoreDefinitionVersionRequestTypeDef(TypedDict):
    CoreDefinitionId: str
    CoreDefinitionVersionId: str

class GetDeploymentStatusRequestTypeDef(TypedDict):
    DeploymentId: str
    GroupId: str

class GetDeviceDefinitionRequestTypeDef(TypedDict):
    DeviceDefinitionId: str

class GetDeviceDefinitionVersionRequestTypeDef(TypedDict):
    DeviceDefinitionId: str
    DeviceDefinitionVersionId: str
    NextToken: NotRequired[str]

class GetFunctionDefinitionRequestTypeDef(TypedDict):
    FunctionDefinitionId: str

class GetFunctionDefinitionVersionRequestTypeDef(TypedDict):
    FunctionDefinitionId: str
    FunctionDefinitionVersionId: str
    NextToken: NotRequired[str]

class GetGroupCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityId: str
    GroupId: str

class GetGroupCertificateConfigurationRequestTypeDef(TypedDict):
    GroupId: str

class GetGroupRequestTypeDef(TypedDict):
    GroupId: str

class GetGroupVersionRequestTypeDef(TypedDict):
    GroupId: str
    GroupVersionId: str

class GetLoggerDefinitionRequestTypeDef(TypedDict):
    LoggerDefinitionId: str

class GetLoggerDefinitionVersionRequestTypeDef(TypedDict):
    LoggerDefinitionId: str
    LoggerDefinitionVersionId: str
    NextToken: NotRequired[str]

class GetResourceDefinitionRequestTypeDef(TypedDict):
    ResourceDefinitionId: str

class GetResourceDefinitionVersionRequestTypeDef(TypedDict):
    ResourceDefinitionId: str
    ResourceDefinitionVersionId: str

class GetSubscriptionDefinitionRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str

class GetSubscriptionDefinitionVersionRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str
    SubscriptionDefinitionVersionId: str
    NextToken: NotRequired[str]

class GetThingRuntimeConfigurationRequestTypeDef(TypedDict):
    ThingName: str

class GroupCertificateAuthorityPropertiesTypeDef(TypedDict):
    GroupCertificateAuthorityArn: NotRequired[str]
    GroupCertificateAuthorityId: NotRequired[str]

class GroupInformationTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreationTimestamp: NotRequired[str]
    Id: NotRequired[str]
    LastUpdatedTimestamp: NotRequired[str]
    LatestVersion: NotRequired[str]
    LatestVersionArn: NotRequired[str]
    Name: NotRequired[str]

class GroupOwnerSettingTypeDef(TypedDict):
    AutoAddGroupOwner: NotRequired[bool]
    GroupOwner: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBulkDeploymentDetailedReportsRequestTypeDef(TypedDict):
    BulkDeploymentId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListBulkDeploymentsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListConnectorDefinitionVersionsRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class VersionInformationTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreationTimestamp: NotRequired[str]
    Id: NotRequired[str]
    Version: NotRequired[str]

class ListConnectorDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListCoreDefinitionVersionsRequestTypeDef(TypedDict):
    CoreDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListCoreDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListDeploymentsRequestTypeDef(TypedDict):
    GroupId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListDeviceDefinitionVersionsRequestTypeDef(TypedDict):
    DeviceDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListDeviceDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListFunctionDefinitionVersionsRequestTypeDef(TypedDict):
    FunctionDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListFunctionDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListGroupCertificateAuthoritiesRequestTypeDef(TypedDict):
    GroupId: str

class ListGroupVersionsRequestTypeDef(TypedDict):
    GroupId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListGroupsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListLoggerDefinitionVersionsRequestTypeDef(TypedDict):
    LoggerDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListLoggerDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListResourceDefinitionVersionsRequestTypeDef(TypedDict):
    ResourceDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListResourceDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListSubscriptionDefinitionVersionsRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListSubscriptionDefinitionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[str]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ResetDeploymentsRequestTypeDef(TypedDict):
    GroupId: str
    AmznClientToken: NotRequired[str]
    Force: NotRequired[bool]

class SecretsManagerSecretResourceDataOutputTypeDef(TypedDict):
    ARN: NotRequired[str]
    AdditionalStagingLabelsToDownload: NotRequired[List[str]]

class ResourceDownloadOwnerSettingTypeDef(TypedDict):
    GroupOwner: str
    GroupPermission: PermissionType

class TelemetryConfigurationTypeDef(TypedDict):
    Telemetry: TelemetryType
    ConfigurationSyncStatus: NotRequired[ConfigurationSyncStatusType]

class SecretsManagerSecretResourceDataTypeDef(TypedDict):
    ARN: NotRequired[str]
    AdditionalStagingLabelsToDownload: NotRequired[Sequence[str]]

class StartBulkDeploymentRequestTypeDef(TypedDict):
    ExecutionRoleArn: str
    InputFileUri: str
    AmznClientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class StopBulkDeploymentRequestTypeDef(TypedDict):
    BulkDeploymentId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    tags: NotRequired[Mapping[str, str]]

class TelemetryConfigurationUpdateTypeDef(TypedDict):
    Telemetry: TelemetryType

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectorDefinitionRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str
    Name: NotRequired[str]

class UpdateCoreDefinitionRequestTypeDef(TypedDict):
    CoreDefinitionId: str
    Name: NotRequired[str]

class UpdateDeviceDefinitionRequestTypeDef(TypedDict):
    DeviceDefinitionId: str
    Name: NotRequired[str]

class UpdateFunctionDefinitionRequestTypeDef(TypedDict):
    FunctionDefinitionId: str
    Name: NotRequired[str]

class UpdateGroupCertificateConfigurationRequestTypeDef(TypedDict):
    GroupId: str
    CertificateExpiryInMilliseconds: NotRequired[str]

class UpdateGroupRequestTypeDef(TypedDict):
    GroupId: str
    Name: NotRequired[str]

class UpdateLoggerDefinitionRequestTypeDef(TypedDict):
    LoggerDefinitionId: str
    Name: NotRequired[str]

class UpdateResourceDefinitionRequestTypeDef(TypedDict):
    ResourceDefinitionId: str
    Name: NotRequired[str]

class UpdateSubscriptionDefinitionRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str
    Name: NotRequired[str]

class AssociateRoleToGroupResponseTypeDef(TypedDict):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateServiceRoleToAccountResponseTypeDef(TypedDict):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(TypedDict):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupCertificateAuthorityResponseTypeDef(TypedDict):
    GroupCertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSoftwareUpdateJobResponseTypeDef(TypedDict):
    IotJobArn: str
    IotJobId: str
    PlatformSoftwareVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateRoleFromGroupResponseTypeDef(TypedDict):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(TypedDict):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedRoleResponseTypeDef(TypedDict):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateAuthorityResponseTypeDef(TypedDict):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str
    PemEncodedCertificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateConfigurationResponseTypeDef(TypedDict):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggerDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(TypedDict):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionDefinitionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetDeploymentsResponseTypeDef(TypedDict):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBulkDeploymentResponseTypeDef(TypedDict):
    BulkDeploymentArn: str
    BulkDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(TypedDict):
    Message: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupCertificateConfigurationResponseTypeDef(TypedDict):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BulkDeploymentResultTypeDef(TypedDict):
    CreatedAt: NotRequired[str]
    DeploymentArn: NotRequired[str]
    DeploymentId: NotRequired[str]
    DeploymentStatus: NotRequired[str]
    DeploymentType: NotRequired[DeploymentTypeType]
    ErrorDetails: NotRequired[List[ErrorDetailTypeDef]]
    ErrorMessage: NotRequired[str]
    GroupArn: NotRequired[str]

class GetBulkDeploymentStatusResponseTypeDef(TypedDict):
    BulkDeploymentMetrics: BulkDeploymentMetricsTypeDef
    BulkDeploymentStatus: BulkDeploymentStatusType
    CreatedAt: str
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentStatusResponseTypeDef(TypedDict):
    DeploymentStatus: str
    DeploymentType: DeploymentTypeType
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    UpdatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBulkDeploymentsResponseTypeDef(TypedDict):
    BulkDeployments: List[BulkDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetConnectivityInfoResponseTypeDef(TypedDict):
    ConnectivityInfo: List[ConnectivityInfoTypeDef]
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestTypeDef(TypedDict):
    ThingName: str
    ConnectivityInfo: NotRequired[Sequence[ConnectivityInfoTypeDef]]

class ConnectorDefinitionVersionOutputTypeDef(TypedDict):
    Connectors: NotRequired[List[ConnectorOutputTypeDef]]

class ConnectorDefinitionVersionTypeDef(TypedDict):
    Connectors: NotRequired[Sequence[ConnectorTypeDef]]

ConnectorUnionTypeDef = Union[ConnectorTypeDef, ConnectorOutputTypeDef]

class CoreDefinitionVersionOutputTypeDef(TypedDict):
    Cores: NotRequired[List[CoreTypeDef]]

class CoreDefinitionVersionTypeDef(TypedDict):
    Cores: NotRequired[Sequence[CoreTypeDef]]

class CreateCoreDefinitionVersionRequestTypeDef(TypedDict):
    CoreDefinitionId: str
    AmznClientToken: NotRequired[str]
    Cores: NotRequired[Sequence[CoreTypeDef]]

class CreateDeviceDefinitionVersionRequestTypeDef(TypedDict):
    DeviceDefinitionId: str
    AmznClientToken: NotRequired[str]
    Devices: NotRequired[Sequence[DeviceTypeDef]]

class DeviceDefinitionVersionOutputTypeDef(TypedDict):
    Devices: NotRequired[List[DeviceTypeDef]]

class DeviceDefinitionVersionTypeDef(TypedDict):
    Devices: NotRequired[Sequence[DeviceTypeDef]]

class CreateGroupRequestTypeDef(TypedDict):
    Name: str
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[GroupVersionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class GetGroupVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: GroupVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionRequestTypeDef(TypedDict):
    LoggerDefinitionId: str
    AmznClientToken: NotRequired[str]
    Loggers: NotRequired[Sequence[LoggerTypeDef]]

class LoggerDefinitionVersionOutputTypeDef(TypedDict):
    Loggers: NotRequired[List[LoggerTypeDef]]

class LoggerDefinitionVersionTypeDef(TypedDict):
    Loggers: NotRequired[Sequence[LoggerTypeDef]]

class CreateSubscriptionDefinitionVersionRequestTypeDef(TypedDict):
    SubscriptionDefinitionId: str
    AmznClientToken: NotRequired[str]
    Subscriptions: NotRequired[Sequence[SubscriptionTypeDef]]

class SubscriptionDefinitionVersionOutputTypeDef(TypedDict):
    Subscriptions: NotRequired[List[SubscriptionTypeDef]]

class SubscriptionDefinitionVersionTypeDef(TypedDict):
    Subscriptions: NotRequired[Sequence[SubscriptionTypeDef]]

class ListConnectorDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCoreDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDeviceDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFunctionDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLoggerDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSubscriptionDefinitionsResponseTypeDef(TypedDict):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDeploymentsResponseTypeDef(TypedDict):
    Deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FunctionDefaultExecutionConfigTypeDef(TypedDict):
    IsolationMode: NotRequired[FunctionIsolationModeType]
    RunAs: NotRequired[FunctionRunAsConfigTypeDef]

class FunctionExecutionConfigTypeDef(TypedDict):
    IsolationMode: NotRequired[FunctionIsolationModeType]
    RunAs: NotRequired[FunctionRunAsConfigTypeDef]

class ListGroupCertificateAuthoritiesResponseTypeDef(TypedDict):
    GroupCertificateAuthorities: List[GroupCertificateAuthorityPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LocalDeviceResourceDataTypeDef(TypedDict):
    GroupOwnerSetting: NotRequired[GroupOwnerSettingTypeDef]
    SourcePath: NotRequired[str]

class LocalVolumeResourceDataTypeDef(TypedDict):
    DestinationPath: NotRequired[str]
    GroupOwnerSetting: NotRequired[GroupOwnerSettingTypeDef]
    SourcePath: NotRequired[str]

class ListBulkDeploymentDetailedReportsRequestPaginateTypeDef(TypedDict):
    BulkDeploymentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBulkDeploymentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectorDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    ConnectorDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectorDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoreDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    CoreDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoreDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeploymentsRequestPaginateTypeDef(TypedDict):
    GroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeviceDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    DeviceDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeviceDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    FunctionDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupVersionsRequestPaginateTypeDef(TypedDict):
    GroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLoggerDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    LoggerDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLoggerDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    ResourceDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionDefinitionVersionsRequestPaginateTypeDef(TypedDict):
    SubscriptionDefinitionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscriptionDefinitionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectorDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCoreDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDeviceDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListFunctionDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLoggerDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSubscriptionDefinitionVersionsResponseTypeDef(TypedDict):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class S3MachineLearningModelResourceDataTypeDef(TypedDict):
    DestinationPath: NotRequired[str]
    OwnerSetting: NotRequired[ResourceDownloadOwnerSettingTypeDef]
    S3Uri: NotRequired[str]

class SageMakerMachineLearningModelResourceDataTypeDef(TypedDict):
    DestinationPath: NotRequired[str]
    OwnerSetting: NotRequired[ResourceDownloadOwnerSettingTypeDef]
    SageMakerJobArn: NotRequired[str]

class RuntimeConfigurationTypeDef(TypedDict):
    TelemetryConfiguration: NotRequired[TelemetryConfigurationTypeDef]

SecretsManagerSecretResourceDataUnionTypeDef = Union[
    SecretsManagerSecretResourceDataTypeDef, SecretsManagerSecretResourceDataOutputTypeDef
]

class UpdateThingRuntimeConfigurationRequestTypeDef(TypedDict):
    ThingName: str
    TelemetryConfiguration: NotRequired[TelemetryConfigurationUpdateTypeDef]

class ListBulkDeploymentDetailedReportsResponseTypeDef(TypedDict):
    Deployments: List[BulkDeploymentResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetConnectorDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: ConnectorDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ConnectorDefinitionVersionUnionTypeDef = Union[
    ConnectorDefinitionVersionTypeDef, ConnectorDefinitionVersionOutputTypeDef
]

class CreateConnectorDefinitionVersionRequestTypeDef(TypedDict):
    ConnectorDefinitionId: str
    AmznClientToken: NotRequired[str]
    Connectors: NotRequired[Sequence[ConnectorUnionTypeDef]]

class GetCoreDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: CoreDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CoreDefinitionVersionUnionTypeDef = Union[
    CoreDefinitionVersionTypeDef, CoreDefinitionVersionOutputTypeDef
]

class GetDeviceDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: DeviceDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

DeviceDefinitionVersionUnionTypeDef = Union[
    DeviceDefinitionVersionTypeDef, DeviceDefinitionVersionOutputTypeDef
]

class GetLoggerDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: LoggerDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

LoggerDefinitionVersionUnionTypeDef = Union[
    LoggerDefinitionVersionTypeDef, LoggerDefinitionVersionOutputTypeDef
]

class GetSubscriptionDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: SubscriptionDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

SubscriptionDefinitionVersionUnionTypeDef = Union[
    SubscriptionDefinitionVersionTypeDef, SubscriptionDefinitionVersionOutputTypeDef
]

class FunctionDefaultConfigTypeDef(TypedDict):
    Execution: NotRequired[FunctionDefaultExecutionConfigTypeDef]

class FunctionConfigurationEnvironmentOutputTypeDef(TypedDict):
    AccessSysfs: NotRequired[bool]
    Execution: NotRequired[FunctionExecutionConfigTypeDef]
    ResourceAccessPolicies: NotRequired[List[ResourceAccessPolicyTypeDef]]
    Variables: NotRequired[Dict[str, str]]

class FunctionConfigurationEnvironmentTypeDef(TypedDict):
    AccessSysfs: NotRequired[bool]
    Execution: NotRequired[FunctionExecutionConfigTypeDef]
    ResourceAccessPolicies: NotRequired[Sequence[ResourceAccessPolicyTypeDef]]
    Variables: NotRequired[Mapping[str, str]]

class ResourceDataContainerOutputTypeDef(TypedDict):
    LocalDeviceResourceData: NotRequired[LocalDeviceResourceDataTypeDef]
    LocalVolumeResourceData: NotRequired[LocalVolumeResourceDataTypeDef]
    S3MachineLearningModelResourceData: NotRequired[S3MachineLearningModelResourceDataTypeDef]
    SageMakerMachineLearningModelResourceData: NotRequired[
        SageMakerMachineLearningModelResourceDataTypeDef
    ]
    SecretsManagerSecretResourceData: NotRequired[SecretsManagerSecretResourceDataOutputTypeDef]

class GetThingRuntimeConfigurationResponseTypeDef(TypedDict):
    RuntimeConfiguration: RuntimeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDataContainerTypeDef(TypedDict):
    LocalDeviceResourceData: NotRequired[LocalDeviceResourceDataTypeDef]
    LocalVolumeResourceData: NotRequired[LocalVolumeResourceDataTypeDef]
    S3MachineLearningModelResourceData: NotRequired[S3MachineLearningModelResourceDataTypeDef]
    SageMakerMachineLearningModelResourceData: NotRequired[
        SageMakerMachineLearningModelResourceDataTypeDef
    ]
    SecretsManagerSecretResourceData: NotRequired[SecretsManagerSecretResourceDataUnionTypeDef]

class CreateConnectorDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[ConnectorDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateCoreDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[CoreDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateDeviceDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[DeviceDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateLoggerDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[LoggerDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateSubscriptionDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[SubscriptionDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class FunctionConfigurationOutputTypeDef(TypedDict):
    EncodingType: NotRequired[EncodingTypeType]
    Environment: NotRequired[FunctionConfigurationEnvironmentOutputTypeDef]
    ExecArgs: NotRequired[str]
    Executable: NotRequired[str]
    MemorySize: NotRequired[int]
    Pinned: NotRequired[bool]
    Timeout: NotRequired[int]
    FunctionRuntimeOverride: NotRequired[str]

FunctionConfigurationEnvironmentUnionTypeDef = Union[
    FunctionConfigurationEnvironmentTypeDef, FunctionConfigurationEnvironmentOutputTypeDef
]

class ResourceOutputTypeDef(TypedDict):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerOutputTypeDef

ResourceDataContainerUnionTypeDef = Union[
    ResourceDataContainerTypeDef, ResourceDataContainerOutputTypeDef
]

class FunctionOutputTypeDef(TypedDict):
    Id: str
    FunctionArn: NotRequired[str]
    FunctionConfiguration: NotRequired[FunctionConfigurationOutputTypeDef]

class FunctionConfigurationTypeDef(TypedDict):
    EncodingType: NotRequired[EncodingTypeType]
    Environment: NotRequired[FunctionConfigurationEnvironmentUnionTypeDef]
    ExecArgs: NotRequired[str]
    Executable: NotRequired[str]
    MemorySize: NotRequired[int]
    Pinned: NotRequired[bool]
    Timeout: NotRequired[int]
    FunctionRuntimeOverride: NotRequired[str]

class ResourceDefinitionVersionOutputTypeDef(TypedDict):
    Resources: NotRequired[List[ResourceOutputTypeDef]]

class ResourceTypeDef(TypedDict):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerUnionTypeDef

class FunctionDefinitionVersionOutputTypeDef(TypedDict):
    DefaultConfig: NotRequired[FunctionDefaultConfigTypeDef]
    Functions: NotRequired[List[FunctionOutputTypeDef]]

FunctionConfigurationUnionTypeDef = Union[
    FunctionConfigurationTypeDef, FunctionConfigurationOutputTypeDef
]

class GetResourceDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: ResourceDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDefinitionVersionTypeDef(TypedDict):
    Resources: NotRequired[Sequence[ResourceTypeDef]]

ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]

class GetFunctionDefinitionVersionResponseTypeDef(TypedDict):
    Arn: str
    CreationTimestamp: str
    Definition: FunctionDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FunctionTypeDef(TypedDict):
    Id: str
    FunctionArn: NotRequired[str]
    FunctionConfiguration: NotRequired[FunctionConfigurationUnionTypeDef]

ResourceDefinitionVersionUnionTypeDef = Union[
    ResourceDefinitionVersionTypeDef, ResourceDefinitionVersionOutputTypeDef
]

class CreateResourceDefinitionVersionRequestTypeDef(TypedDict):
    ResourceDefinitionId: str
    AmznClientToken: NotRequired[str]
    Resources: NotRequired[Sequence[ResourceUnionTypeDef]]

class FunctionDefinitionVersionTypeDef(TypedDict):
    DefaultConfig: NotRequired[FunctionDefaultConfigTypeDef]
    Functions: NotRequired[Sequence[FunctionTypeDef]]

FunctionUnionTypeDef = Union[FunctionTypeDef, FunctionOutputTypeDef]

class CreateResourceDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[ResourceDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

FunctionDefinitionVersionUnionTypeDef = Union[
    FunctionDefinitionVersionTypeDef, FunctionDefinitionVersionOutputTypeDef
]

class CreateFunctionDefinitionVersionRequestTypeDef(TypedDict):
    FunctionDefinitionId: str
    AmznClientToken: NotRequired[str]
    DefaultConfig: NotRequired[FunctionDefaultConfigTypeDef]
    Functions: NotRequired[Sequence[FunctionUnionTypeDef]]

class CreateFunctionDefinitionRequestTypeDef(TypedDict):
    AmznClientToken: NotRequired[str]
    InitialVersion: NotRequired[FunctionDefinitionVersionUnionTypeDef]
    Name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
