"""
Type annotations for sms service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sms.type_defs import LaunchDetailsTypeDef

    data: LaunchDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
)

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
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobRequestTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "DeleteAppLaunchConfigurationRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteAppValidationConfigurationRequestTypeDef",
    "DeleteReplicationJobRequestTypeDef",
    "DisassociateConnectorRequestTypeDef",
    "GenerateChangeSetRequestTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateRequestTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationRequestTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationRequestTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppRequestTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationRequestTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputRequestTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsRequestPaginateTypeDef",
    "GetConnectorsRequestTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsRequestPaginateTypeDef",
    "GetReplicationJobsRequestTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsRequestPaginateTypeDef",
    "GetReplicationRunsRequestTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersRequestPaginateTypeDef",
    "GetServersRequestTypeDef",
    "GetServersResponseTypeDef",
    "ImportAppCatalogRequestTypeDef",
    "LaunchAppRequestTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsRequestPaginateTypeDef",
    "ListAppsRequestTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "NotifyAppValidationOutputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppLaunchConfigurationRequestTypeDef",
    "PutAppReplicationConfigurationRequestTypeDef",
    "PutAppValidationConfigurationRequestTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SSMOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "ServerGroupLaunchConfigurationOutputTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupLaunchConfigurationUnionTypeDef",
    "ServerGroupOutputTypeDef",
    "ServerGroupReplicationConfigurationOutputTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupReplicationConfigurationUnionTypeDef",
    "ServerGroupTypeDef",
    "ServerGroupUnionTypeDef",
    "ServerGroupValidationConfigurationOutputTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ServerGroupValidationConfigurationUnionTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationOutputTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerReplicationConfigurationUnionTypeDef",
    "ServerReplicationParametersOutputTypeDef",
    "ServerReplicationParametersTypeDef",
    "ServerReplicationParametersUnionTypeDef",
    "ServerTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "SourceTypeDef",
    "StartAppReplicationRequestTypeDef",
    "StartOnDemandAppReplicationRequestTypeDef",
    "StartOnDemandReplicationRunRequestTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "StopAppReplicationRequestTypeDef",
    "TagTypeDef",
    "TerminateAppRequestTypeDef",
    "TimestampTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateReplicationJobRequestTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
)

class LaunchDetailsTypeDef(TypedDict):
    latestLaunchTime: NotRequired[datetime]
    stackName: NotRequired[str]
    stackId: NotRequired[str]

class ConnectorTypeDef(TypedDict):
    connectorId: NotRequired[str]
    version: NotRequired[str]
    status: NotRequired[ConnectorStatusType]
    capabilityList: NotRequired[List[ConnectorCapabilityType]]
    vmManagerName: NotRequired[str]
    vmManagerType: NotRequired[VmManagerTypeType]
    vmManagerId: NotRequired[str]
    ipAddress: NotRequired[str]
    macAddress: NotRequired[str]
    associatedOn: NotRequired[datetime]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DeleteAppLaunchConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class DeleteAppReplicationConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class DeleteAppRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    forceStopAppReplication: NotRequired[bool]
    forceTerminateApp: NotRequired[bool]

class DeleteAppValidationConfigurationRequestTypeDef(TypedDict):
    appId: str

class DeleteReplicationJobRequestTypeDef(TypedDict):
    replicationJobId: str

class DisassociateConnectorRequestTypeDef(TypedDict):
    connectorId: str

class GenerateChangeSetRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    changesetFormat: NotRequired[OutputFormatType]

class S3LocationTypeDef(TypedDict):
    bucket: NotRequired[str]
    key: NotRequired[str]

class GenerateTemplateRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    templateFormat: NotRequired[OutputFormatType]

class GetAppLaunchConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class GetAppReplicationConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class GetAppRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class GetAppValidationConfigurationRequestTypeDef(TypedDict):
    appId: str

class GetAppValidationOutputRequestTypeDef(TypedDict):
    appId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetConnectorsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetReplicationJobsRequestTypeDef(TypedDict):
    replicationJobId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetReplicationRunsRequestTypeDef(TypedDict):
    replicationJobId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class VmServerAddressTypeDef(TypedDict):
    vmManagerId: NotRequired[str]
    vmId: NotRequired[str]

class ImportAppCatalogRequestTypeDef(TypedDict):
    roleName: NotRequired[str]

class LaunchAppRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class ListAppsRequestTypeDef(TypedDict):
    appIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class NotificationContextTypeDef(TypedDict):
    validationId: NotRequired[str]
    status: NotRequired[ValidationStatusType]
    statusMessage: NotRequired[str]

class ReplicationRunStageDetailsTypeDef(TypedDict):
    stage: NotRequired[str]
    stageProgress: NotRequired[str]

class ServerReplicationParametersOutputTypeDef(TypedDict):
    seedTime: NotRequired[datetime]
    frequency: NotRequired[int]
    runOnce: NotRequired[bool]
    licenseType: NotRequired[LicenseTypeType]
    numberOfRecentAmisToKeep: NotRequired[int]
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]

class StartAppReplicationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class StartOnDemandAppReplicationRequestTypeDef(TypedDict):
    appId: str
    description: NotRequired[str]

class StartOnDemandReplicationRunRequestTypeDef(TypedDict):
    replicationJobId: str
    description: NotRequired[str]

class StopAppReplicationRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class TerminateAppRequestTypeDef(TypedDict):
    appId: NotRequired[str]

class AppSummaryTypeDef(TypedDict):
    appId: NotRequired[str]
    importedAppId: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[AppStatusType]
    statusMessage: NotRequired[str]
    replicationConfigurationStatus: NotRequired[AppReplicationConfigurationStatusType]
    replicationStatus: NotRequired[AppReplicationStatusType]
    replicationStatusMessage: NotRequired[str]
    latestReplicationTime: NotRequired[datetime]
    launchConfigurationStatus: NotRequired[AppLaunchConfigurationStatusType]
    launchStatus: NotRequired[AppLaunchStatusType]
    launchStatusMessage: NotRequired[str]
    launchDetails: NotRequired[LaunchDetailsTypeDef]
    creationTime: NotRequired[datetime]
    lastModified: NotRequired[datetime]
    roleName: NotRequired[str]
    totalServerGroups: NotRequired[int]
    totalServers: NotRequired[int]

class CreateReplicationJobResponseTypeDef(TypedDict):
    replicationJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorsResponseTypeDef(TypedDict):
    connectorList: List[ConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartOnDemandReplicationRunResponseTypeDef(TypedDict):
    replicationRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationJobRequestTypeDef(TypedDict):
    serverId: str
    seedReplicationTime: TimestampTypeDef
    frequency: NotRequired[int]
    runOnce: NotRequired[bool]
    licenseType: NotRequired[LicenseTypeType]
    roleName: NotRequired[str]
    description: NotRequired[str]
    numberOfRecentAmisToKeep: NotRequired[int]
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]

class ServerReplicationParametersTypeDef(TypedDict):
    seedTime: NotRequired[TimestampTypeDef]
    frequency: NotRequired[int]
    runOnce: NotRequired[bool]
    licenseType: NotRequired[LicenseTypeType]
    numberOfRecentAmisToKeep: NotRequired[int]
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]

class UpdateReplicationJobRequestTypeDef(TypedDict):
    replicationJobId: str
    frequency: NotRequired[int]
    nextReplicationRunStartTime: NotRequired[TimestampTypeDef]
    licenseType: NotRequired[LicenseTypeType]
    roleName: NotRequired[str]
    description: NotRequired[str]
    numberOfRecentAmisToKeep: NotRequired[int]
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]

class GenerateChangeSetResponseTypeDef(TypedDict):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateTemplateResponseTypeDef(TypedDict):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SSMOutputTypeDef(TypedDict):
    s3Location: NotRequired[S3LocationTypeDef]

class SourceTypeDef(TypedDict):
    s3Location: NotRequired[S3LocationTypeDef]

class UserDataTypeDef(TypedDict):
    s3Location: NotRequired[S3LocationTypeDef]

class GetConnectorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetReplicationJobsRequestPaginateTypeDef(TypedDict):
    replicationJobId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetReplicationRunsRequestPaginateTypeDef(TypedDict):
    replicationJobId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAppsRequestPaginateTypeDef(TypedDict):
    appIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetServersRequestPaginateTypeDef(TypedDict):
    vmServerAddressList: NotRequired[Sequence[VmServerAddressTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetServersRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    vmServerAddressList: NotRequired[Sequence[VmServerAddressTypeDef]]

class VmServerTypeDef(TypedDict):
    vmServerAddress: NotRequired[VmServerAddressTypeDef]
    vmName: NotRequired[str]
    vmManagerName: NotRequired[str]
    vmManagerType: NotRequired[VmManagerTypeType]
    vmPath: NotRequired[str]

class NotifyAppValidationOutputRequestTypeDef(TypedDict):
    appId: str
    notificationContext: NotRequired[NotificationContextTypeDef]

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": NotRequired[str],
        "state": NotRequired[ReplicationRunStateType],
        "type": NotRequired[ReplicationRunTypeType],
        "stageDetails": NotRequired[ReplicationRunStageDetailsTypeDef],
        "statusMessage": NotRequired[str],
        "amiId": NotRequired[str],
        "scheduledStartTime": NotRequired[datetime],
        "completedTime": NotRequired[datetime],
        "description": NotRequired[str],
        "encrypted": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
    },
)

class ListAppsResponseTypeDef(TypedDict):
    apps: List[AppSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ServerReplicationParametersUnionTypeDef = Union[
    ServerReplicationParametersTypeDef, ServerReplicationParametersOutputTypeDef
]

class AppValidationOutputTypeDef(TypedDict):
    ssmOutput: NotRequired[SSMOutputTypeDef]

class SSMValidationParametersTypeDef(TypedDict):
    source: NotRequired[SourceTypeDef]
    instanceId: NotRequired[str]
    scriptType: NotRequired[ScriptTypeType]
    command: NotRequired[str]
    executionTimeoutSeconds: NotRequired[int]
    outputS3BucketName: NotRequired[str]

class UserDataValidationParametersTypeDef(TypedDict):
    source: NotRequired[SourceTypeDef]
    scriptType: NotRequired[ScriptTypeType]

class ServerTypeDef(TypedDict):
    serverId: NotRequired[str]
    serverType: NotRequired[Literal["VIRTUAL_MACHINE"]]
    vmServer: NotRequired[VmServerTypeDef]
    replicationJobId: NotRequired[str]
    replicationJobTerminated: NotRequired[bool]

class ReplicationJobTypeDef(TypedDict):
    replicationJobId: NotRequired[str]
    serverId: NotRequired[str]
    serverType: NotRequired[Literal["VIRTUAL_MACHINE"]]
    vmServer: NotRequired[VmServerTypeDef]
    seedReplicationTime: NotRequired[datetime]
    frequency: NotRequired[int]
    runOnce: NotRequired[bool]
    nextReplicationRunStartTime: NotRequired[datetime]
    licenseType: NotRequired[LicenseTypeType]
    roleName: NotRequired[str]
    latestAmiId: NotRequired[str]
    state: NotRequired[ReplicationJobStateType]
    statusMessage: NotRequired[str]
    description: NotRequired[str]
    numberOfRecentAmisToKeep: NotRequired[int]
    encrypted: NotRequired[bool]
    kmsKeyId: NotRequired[str]
    replicationRunList: NotRequired[List[ReplicationRunTypeDef]]

class AppValidationConfigurationTypeDef(TypedDict):
    validationId: NotRequired[str]
    name: NotRequired[str]
    appValidationStrategy: NotRequired[Literal["SSM"]]
    ssmValidationParameters: NotRequired[SSMValidationParametersTypeDef]

class GetServersResponseTypeDef(TypedDict):
    lastModifiedOn: datetime
    serverCatalogStatus: ServerCatalogStatusType
    serverList: List[ServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ServerGroupOutputTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    name: NotRequired[str]
    serverList: NotRequired[List[ServerTypeDef]]

class ServerGroupTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    name: NotRequired[str]
    serverList: NotRequired[Sequence[ServerTypeDef]]

class ServerLaunchConfigurationTypeDef(TypedDict):
    server: NotRequired[ServerTypeDef]
    logicalId: NotRequired[str]
    vpc: NotRequired[str]
    subnet: NotRequired[str]
    securityGroup: NotRequired[str]
    ec2KeyName: NotRequired[str]
    userData: NotRequired[UserDataTypeDef]
    instanceType: NotRequired[str]
    associatePublicIpAddress: NotRequired[bool]
    iamInstanceProfileName: NotRequired[str]
    configureScript: NotRequired[S3LocationTypeDef]
    configureScriptType: NotRequired[ScriptTypeType]

class ServerReplicationConfigurationOutputTypeDef(TypedDict):
    server: NotRequired[ServerTypeDef]
    serverReplicationParameters: NotRequired[ServerReplicationParametersOutputTypeDef]

class ServerReplicationConfigurationTypeDef(TypedDict):
    server: NotRequired[ServerTypeDef]
    serverReplicationParameters: NotRequired[ServerReplicationParametersUnionTypeDef]

class ServerValidationConfigurationTypeDef(TypedDict):
    server: NotRequired[ServerTypeDef]
    validationId: NotRequired[str]
    name: NotRequired[str]
    serverValidationStrategy: NotRequired[Literal["USERDATA"]]
    userDataValidationParameters: NotRequired[UserDataValidationParametersTypeDef]

class ServerValidationOutputTypeDef(TypedDict):
    server: NotRequired[ServerTypeDef]

class GetReplicationJobsResponseTypeDef(TypedDict):
    replicationJobList: List[ReplicationJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetReplicationRunsResponseTypeDef(TypedDict):
    replicationJob: ReplicationJobTypeDef
    replicationRunList: List[ReplicationRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAppResponseTypeDef(TypedDict):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppResponseTypeDef(TypedDict):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppResponseTypeDef(TypedDict):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ServerGroupUnionTypeDef = Union[ServerGroupTypeDef, ServerGroupOutputTypeDef]

class ServerGroupLaunchConfigurationOutputTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    launchOrder: NotRequired[int]
    serverLaunchConfigurations: NotRequired[List[ServerLaunchConfigurationTypeDef]]

class ServerGroupLaunchConfigurationTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    launchOrder: NotRequired[int]
    serverLaunchConfigurations: NotRequired[Sequence[ServerLaunchConfigurationTypeDef]]

class ServerGroupReplicationConfigurationOutputTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    serverReplicationConfigurations: NotRequired[List[ServerReplicationConfigurationOutputTypeDef]]

ServerReplicationConfigurationUnionTypeDef = Union[
    ServerReplicationConfigurationTypeDef, ServerReplicationConfigurationOutputTypeDef
]

class ServerGroupValidationConfigurationOutputTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    serverValidationConfigurations: NotRequired[List[ServerValidationConfigurationTypeDef]]

class ServerGroupValidationConfigurationTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    serverValidationConfigurations: NotRequired[Sequence[ServerValidationConfigurationTypeDef]]

class ValidationOutputTypeDef(TypedDict):
    validationId: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[ValidationStatusType]
    statusMessage: NotRequired[str]
    latestValidationTime: NotRequired[datetime]
    appValidationOutput: NotRequired[AppValidationOutputTypeDef]
    serverValidationOutput: NotRequired[ServerValidationOutputTypeDef]

class CreateAppRequestTypeDef(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    roleName: NotRequired[str]
    clientToken: NotRequired[str]
    serverGroups: NotRequired[Sequence[ServerGroupUnionTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateAppRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    roleName: NotRequired[str]
    serverGroups: NotRequired[Sequence[ServerGroupUnionTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class GetAppLaunchConfigurationResponseTypeDef(TypedDict):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List[ServerGroupLaunchConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ServerGroupLaunchConfigurationUnionTypeDef = Union[
    ServerGroupLaunchConfigurationTypeDef, ServerGroupLaunchConfigurationOutputTypeDef
]

class GetAppReplicationConfigurationResponseTypeDef(TypedDict):
    serverGroupReplicationConfigurations: List[ServerGroupReplicationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServerGroupReplicationConfigurationTypeDef(TypedDict):
    serverGroupId: NotRequired[str]
    serverReplicationConfigurations: NotRequired[
        Sequence[ServerReplicationConfigurationUnionTypeDef]
    ]

class GetAppValidationConfigurationResponseTypeDef(TypedDict):
    appValidationConfigurations: List[AppValidationConfigurationTypeDef]
    serverGroupValidationConfigurations: List[ServerGroupValidationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ServerGroupValidationConfigurationUnionTypeDef = Union[
    ServerGroupValidationConfigurationTypeDef, ServerGroupValidationConfigurationOutputTypeDef
]

class GetAppValidationOutputResponseTypeDef(TypedDict):
    validationOutputList: List[ValidationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppLaunchConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    roleName: NotRequired[str]
    autoLaunch: NotRequired[bool]
    serverGroupLaunchConfigurations: NotRequired[
        Sequence[ServerGroupLaunchConfigurationUnionTypeDef]
    ]

ServerGroupReplicationConfigurationUnionTypeDef = Union[
    ServerGroupReplicationConfigurationTypeDef, ServerGroupReplicationConfigurationOutputTypeDef
]

class PutAppValidationConfigurationRequestTypeDef(TypedDict):
    appId: str
    appValidationConfigurations: NotRequired[Sequence[AppValidationConfigurationTypeDef]]
    serverGroupValidationConfigurations: NotRequired[
        Sequence[ServerGroupValidationConfigurationUnionTypeDef]
    ]

class PutAppReplicationConfigurationRequestTypeDef(TypedDict):
    appId: NotRequired[str]
    serverGroupReplicationConfigurations: NotRequired[
        Sequence[ServerGroupReplicationConfigurationUnionTypeDef]
    ]
