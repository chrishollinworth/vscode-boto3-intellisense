"""
Type annotations for drs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_drs.type_defs import AccountTypeDef

    data: AccountTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    DataReplicationErrorStringType,
    DataReplicationInitiationStepNameType,
    DataReplicationInitiationStepStatusType,
    DataReplicationStateType,
    EC2InstanceStateType,
    ExtensionStatusType,
    FailbackLaunchTypeType,
    FailbackReplicationErrorType,
    FailbackStateType,
    InitiatedByType,
    JobLogEventType,
    JobStatusType,
    JobTypeType,
    LastLaunchResultType,
    LastLaunchTypeType,
    LaunchActionCategoryType,
    LaunchActionParameterTypeType,
    LaunchActionRunStatusType,
    LaunchActionTypeType,
    LaunchDispositionType,
    LaunchStatusType,
    OriginEnvironmentType,
    PITPolicyRuleUnitsType,
    ProductCodeModeType,
    RecoveryInstanceDataReplicationInitiationStepNameType,
    RecoveryInstanceDataReplicationInitiationStepStatusType,
    RecoveryInstanceDataReplicationStateType,
    RecoveryResultType,
    RecoverySnapshotsOrderType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    ReplicationDirectionType,
    ReplicationStatusType,
    TargetInstanceTypeRightSizingMethodType,
    VolumeStatusType,
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
    "AccountTypeDef",
    "AssociateSourceNetworkStackRequestTypeDef",
    "AssociateSourceNetworkStackResponseTypeDef",
    "CPUTypeDef",
    "ConversionPropertiesTypeDef",
    "CreateExtendedSourceServerRequestTypeDef",
    "CreateExtendedSourceServerResponseTypeDef",
    "CreateLaunchConfigurationTemplateRequestTypeDef",
    "CreateLaunchConfigurationTemplateResponseTypeDef",
    "CreateReplicationConfigurationTemplateRequestTypeDef",
    "CreateSourceNetworkRequestTypeDef",
    "CreateSourceNetworkResponseTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteLaunchActionRequestTypeDef",
    "DeleteLaunchConfigurationTemplateRequestTypeDef",
    "DeleteRecoveryInstanceRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestTypeDef",
    "DeleteSourceNetworkRequestTypeDef",
    "DeleteSourceServerRequestTypeDef",
    "DescribeJobLogItemsRequestPaginateTypeDef",
    "DescribeJobLogItemsRequestTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestPaginateTypeDef",
    "DescribeJobsRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef",
    "DescribeLaunchConfigurationTemplatesRequestTypeDef",
    "DescribeLaunchConfigurationTemplatesResponseTypeDef",
    "DescribeRecoveryInstancesRequestFiltersTypeDef",
    "DescribeRecoveryInstancesRequestPaginateTypeDef",
    "DescribeRecoveryInstancesRequestTypeDef",
    "DescribeRecoveryInstancesResponseTypeDef",
    "DescribeRecoverySnapshotsRequestFiltersTypeDef",
    "DescribeRecoverySnapshotsRequestPaginateTypeDef",
    "DescribeRecoverySnapshotsRequestTypeDef",
    "DescribeRecoverySnapshotsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceNetworksRequestFiltersTypeDef",
    "DescribeSourceNetworksRequestPaginateTypeDef",
    "DescribeSourceNetworksRequestTypeDef",
    "DescribeSourceNetworksResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestPaginateTypeDef",
    "DescribeSourceServersRequestTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DisconnectRecoveryInstanceRequestTypeDef",
    "DisconnectSourceServerRequestTypeDef",
    "DiskTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventResourceDataTypeDef",
    "ExportSourceNetworkCfnTemplateRequestTypeDef",
    "ExportSourceNetworkCfnTemplateResponseTypeDef",
    "GetFailbackReplicationConfigurationRequestTypeDef",
    "GetFailbackReplicationConfigurationResponseTypeDef",
    "GetLaunchConfigurationRequestTypeDef",
    "GetReplicationConfigurationRequestTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
    "LaunchActionParameterTypeDef",
    "LaunchActionRunTypeDef",
    "LaunchActionTypeDef",
    "LaunchActionsRequestFiltersTypeDef",
    "LaunchActionsStatusTypeDef",
    "LaunchConfigurationTemplateTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchIntoInstancePropertiesTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastLaunchInitiatedTypeDef",
    "LifeCycleLastLaunchTypeDef",
    "LifeCycleTypeDef",
    "ListExtensibleSourceServersRequestPaginateTypeDef",
    "ListExtensibleSourceServersRequestTypeDef",
    "ListExtensibleSourceServersResponseTypeDef",
    "ListLaunchActionsRequestPaginateTypeDef",
    "ListLaunchActionsRequestTypeDef",
    "ListLaunchActionsResponseTypeDef",
    "ListStagingAccountsRequestPaginateTypeDef",
    "ListStagingAccountsRequestTypeDef",
    "ListStagingAccountsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PITPolicyRuleTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingResourceIDTypeDef",
    "ParticipatingResourceTypeDef",
    "ParticipatingServerTypeDef",
    "ProductCodeTypeDef",
    "PutLaunchActionRequestTypeDef",
    "PutLaunchActionResponseTypeDef",
    "RecoveryInstanceDataReplicationErrorTypeDef",
    "RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef",
    "RecoveryInstanceDataReplicationInfoTypeDef",
    "RecoveryInstanceDataReplicationInitiationStepTypeDef",
    "RecoveryInstanceDataReplicationInitiationTypeDef",
    "RecoveryInstanceDiskTypeDef",
    "RecoveryInstanceFailbackTypeDef",
    "RecoveryInstancePropertiesTypeDef",
    "RecoveryInstanceTypeDef",
    "RecoveryLifeCycleTypeDef",
    "RecoverySnapshotTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateResponseTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestTypeDef",
    "ReverseReplicationRequestTypeDef",
    "ReverseReplicationResponseTypeDef",
    "SourceCloudPropertiesTypeDef",
    "SourceNetworkDataTypeDef",
    "SourceNetworkTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerResponseTypeDef",
    "SourceServerTypeDef",
    "StagingAreaTypeDef",
    "StagingSourceServerTypeDef",
    "StartFailbackLaunchRequestTypeDef",
    "StartFailbackLaunchResponseTypeDef",
    "StartRecoveryRequestSourceServerTypeDef",
    "StartRecoveryRequestTypeDef",
    "StartRecoveryResponseTypeDef",
    "StartReplicationRequestTypeDef",
    "StartReplicationResponseTypeDef",
    "StartSourceNetworkRecoveryRequestNetworkEntryTypeDef",
    "StartSourceNetworkRecoveryRequestTypeDef",
    "StartSourceNetworkRecoveryResponseTypeDef",
    "StartSourceNetworkReplicationRequestTypeDef",
    "StartSourceNetworkReplicationResponseTypeDef",
    "StopFailbackRequestTypeDef",
    "StopReplicationRequestTypeDef",
    "StopReplicationResponseTypeDef",
    "StopSourceNetworkReplicationRequestTypeDef",
    "StopSourceNetworkReplicationResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TerminateRecoveryInstancesRequestTypeDef",
    "TerminateRecoveryInstancesResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFailbackReplicationConfigurationRequestTypeDef",
    "UpdateLaunchConfigurationRequestTypeDef",
    "UpdateLaunchConfigurationTemplateRequestTypeDef",
    "UpdateLaunchConfigurationTemplateResponseTypeDef",
    "UpdateReplicationConfigurationRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestTypeDef",
)

class AccountTypeDef(TypedDict):
    accountID: NotRequired[str]

class AssociateSourceNetworkStackRequestTypeDef(TypedDict):
    cfnStackName: str
    sourceNetworkID: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CPUTypeDef(TypedDict):
    cores: NotRequired[int]
    modelName: NotRequired[str]

class ProductCodeTypeDef(TypedDict):
    productCodeId: NotRequired[str]
    productCodeMode: NotRequired[ProductCodeModeType]

class CreateExtendedSourceServerRequestTypeDef(TypedDict):
    sourceServerArn: str
    tags: NotRequired[Mapping[str, str]]

class LicensingTypeDef(TypedDict):
    osByol: NotRequired[bool]

class PITPolicyRuleTypeDef(TypedDict):
    interval: int
    retentionDuration: int
    units: PITPolicyRuleUnitsType
    enabled: NotRequired[bool]
    ruleID: NotRequired[int]

class CreateSourceNetworkRequestTypeDef(TypedDict):
    originAccountID: str
    originRegion: str
    vpcID: str
    tags: NotRequired[Mapping[str, str]]

class DataReplicationErrorTypeDef(TypedDict):
    error: NotRequired[DataReplicationErrorStringType]
    rawError: NotRequired[str]

class DataReplicationInfoReplicatedDiskTypeDef(TypedDict):
    backloggedStorageBytes: NotRequired[int]
    deviceName: NotRequired[str]
    replicatedStorageBytes: NotRequired[int]
    rescannedStorageBytes: NotRequired[int]
    totalStorageBytes: NotRequired[int]
    volumeStatus: NotRequired[VolumeStatusType]

class DataReplicationInitiationStepTypeDef(TypedDict):
    name: NotRequired[DataReplicationInitiationStepNameType]
    status: NotRequired[DataReplicationInitiationStepStatusType]

class DeleteJobRequestTypeDef(TypedDict):
    jobID: str

class DeleteLaunchActionRequestTypeDef(TypedDict):
    actionId: str
    resourceId: str

class DeleteLaunchConfigurationTemplateRequestTypeDef(TypedDict):
    launchConfigurationTemplateID: str

class DeleteRecoveryInstanceRequestTypeDef(TypedDict):
    recoveryInstanceID: str

class DeleteReplicationConfigurationTemplateRequestTypeDef(TypedDict):
    replicationConfigurationTemplateID: str

class DeleteSourceNetworkRequestTypeDef(TypedDict):
    sourceNetworkID: str

class DeleteSourceServerRequestTypeDef(TypedDict):
    sourceServerID: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeJobLogItemsRequestTypeDef(TypedDict):
    jobID: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeJobsRequestFiltersTypeDef(TypedDict):
    fromDate: NotRequired[str]
    jobIDs: NotRequired[Sequence[str]]
    toDate: NotRequired[str]

class DescribeLaunchConfigurationTemplatesRequestTypeDef(TypedDict):
    launchConfigurationTemplateIDs: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeRecoveryInstancesRequestFiltersTypeDef(TypedDict):
    recoveryInstanceIDs: NotRequired[Sequence[str]]
    sourceServerIDs: NotRequired[Sequence[str]]

class DescribeRecoverySnapshotsRequestFiltersTypeDef(TypedDict):
    fromDateTime: NotRequired[str]
    toDateTime: NotRequired[str]

class RecoverySnapshotTypeDef(TypedDict):
    expectedTimestamp: str
    snapshotID: str
    sourceServerID: str
    ebsSnapshots: NotRequired[List[str]]
    timestamp: NotRequired[str]

class DescribeReplicationConfigurationTemplatesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    replicationConfigurationTemplateIDs: NotRequired[Sequence[str]]

class DescribeSourceNetworksRequestFiltersTypeDef(TypedDict):
    originAccountID: NotRequired[str]
    originRegion: NotRequired[str]
    sourceNetworkIDs: NotRequired[Sequence[str]]

class DescribeSourceServersRequestFiltersTypeDef(TypedDict):
    hardwareId: NotRequired[str]
    sourceServerIDs: NotRequired[Sequence[str]]
    stagingAccountIDs: NotRequired[Sequence[str]]

class DisconnectRecoveryInstanceRequestTypeDef(TypedDict):
    recoveryInstanceID: str

class DisconnectSourceServerRequestTypeDef(TypedDict):
    sourceServerID: str

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "bytes": NotRequired[int],
        "deviceName": NotRequired[str],
    },
)

class SourceNetworkDataTypeDef(TypedDict):
    sourceNetworkID: NotRequired[str]
    sourceVpc: NotRequired[str]
    stackName: NotRequired[str]
    targetVpc: NotRequired[str]

class ExportSourceNetworkCfnTemplateRequestTypeDef(TypedDict):
    sourceNetworkID: str

class GetFailbackReplicationConfigurationRequestTypeDef(TypedDict):
    recoveryInstanceID: str

class GetLaunchConfigurationRequestTypeDef(TypedDict):
    sourceServerID: str

class GetReplicationConfigurationRequestTypeDef(TypedDict):
    sourceServerID: str

class IdentificationHintsTypeDef(TypedDict):
    awsInstanceID: NotRequired[str]
    fqdn: NotRequired[str]
    hostname: NotRequired[str]
    vmWareUuid: NotRequired[str]

LaunchActionParameterTypeDef = TypedDict(
    "LaunchActionParameterTypeDef",
    {
        "type": NotRequired[LaunchActionParameterTypeType],
        "value": NotRequired[str],
    },
)

class LaunchActionsRequestFiltersTypeDef(TypedDict):
    actionIds: NotRequired[Sequence[str]]

class LaunchIntoInstancePropertiesTypeDef(TypedDict):
    launchIntoEC2InstanceID: NotRequired[str]

LifeCycleLastLaunchInitiatedTypeDef = TypedDict(
    "LifeCycleLastLaunchInitiatedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
        "jobID": NotRequired[str],
        "type": NotRequired[LastLaunchTypeType],
    },
)

class ListExtensibleSourceServersRequestTypeDef(TypedDict):
    stagingAccountID: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class StagingSourceServerTypeDef(TypedDict):
    arn: NotRequired[str]
    hostname: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListStagingAccountsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NetworkInterfaceTypeDef(TypedDict):
    ips: NotRequired[List[str]]
    isPrimary: NotRequired[bool]
    macAddress: NotRequired[str]

class OSTypeDef(TypedDict):
    fullString: NotRequired[str]

class ParticipatingResourceIDTypeDef(TypedDict):
    sourceNetworkID: NotRequired[str]

class RecoveryInstanceDataReplicationErrorTypeDef(TypedDict):
    error: NotRequired[FailbackReplicationErrorType]
    rawError: NotRequired[str]

class RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef(TypedDict):
    backloggedStorageBytes: NotRequired[int]
    deviceName: NotRequired[str]
    replicatedStorageBytes: NotRequired[int]
    rescannedStorageBytes: NotRequired[int]
    totalStorageBytes: NotRequired[int]

class RecoveryInstanceDataReplicationInitiationStepTypeDef(TypedDict):
    name: NotRequired[RecoveryInstanceDataReplicationInitiationStepNameType]
    status: NotRequired[RecoveryInstanceDataReplicationInitiationStepStatusType]

RecoveryInstanceDiskTypeDef = TypedDict(
    "RecoveryInstanceDiskTypeDef",
    {
        "bytes": NotRequired[int],
        "ebsVolumeID": NotRequired[str],
        "internalDeviceName": NotRequired[str],
    },
)

class RecoveryInstanceFailbackTypeDef(TypedDict):
    agentLastSeenByServiceDateTime: NotRequired[str]
    elapsedReplicationDuration: NotRequired[str]
    failbackClientID: NotRequired[str]
    failbackClientLastSeenByServiceDateTime: NotRequired[str]
    failbackInitiationTime: NotRequired[str]
    failbackJobID: NotRequired[str]
    failbackLaunchType: NotRequired[FailbackLaunchTypeType]
    failbackToOriginalServer: NotRequired[bool]
    firstByteDateTime: NotRequired[str]
    state: NotRequired[FailbackStateType]

class RecoveryLifeCycleTypeDef(TypedDict):
    apiCallDateTime: NotRequired[datetime]
    jobID: NotRequired[str]
    lastRecoveryResult: NotRequired[RecoveryResultType]

class ReplicationConfigurationReplicatedDiskTypeDef(TypedDict):
    deviceName: NotRequired[str]
    iops: NotRequired[int]
    isBootDisk: NotRequired[bool]
    optimizedStagingDiskType: NotRequired[ReplicationConfigurationReplicatedDiskStagingDiskTypeType]
    stagingDiskType: NotRequired[ReplicationConfigurationReplicatedDiskStagingDiskTypeType]
    throughput: NotRequired[int]

class RetryDataReplicationRequestTypeDef(TypedDict):
    sourceServerID: str

class ReverseReplicationRequestTypeDef(TypedDict):
    recoveryInstanceID: str

class SourceCloudPropertiesTypeDef(TypedDict):
    originAccountID: NotRequired[str]
    originAvailabilityZone: NotRequired[str]
    originRegion: NotRequired[str]
    sourceOutpostArn: NotRequired[str]

class StagingAreaTypeDef(TypedDict):
    errorMessage: NotRequired[str]
    stagingAccountID: NotRequired[str]
    stagingSourceServerArn: NotRequired[str]
    status: NotRequired[ExtensionStatusType]

class StartFailbackLaunchRequestTypeDef(TypedDict):
    recoveryInstanceIDs: Sequence[str]
    tags: NotRequired[Mapping[str, str]]

class StartRecoveryRequestSourceServerTypeDef(TypedDict):
    sourceServerID: str
    recoverySnapshotID: NotRequired[str]

class StartReplicationRequestTypeDef(TypedDict):
    sourceServerID: str

class StartSourceNetworkRecoveryRequestNetworkEntryTypeDef(TypedDict):
    sourceNetworkID: str
    cfnStackName: NotRequired[str]

class StartSourceNetworkReplicationRequestTypeDef(TypedDict):
    sourceNetworkID: str

class StopFailbackRequestTypeDef(TypedDict):
    recoveryInstanceID: str

class StopReplicationRequestTypeDef(TypedDict):
    sourceServerID: str

class StopSourceNetworkReplicationRequestTypeDef(TypedDict):
    sourceNetworkID: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateRecoveryInstancesRequestTypeDef(TypedDict):
    recoveryInstanceIDs: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateFailbackReplicationConfigurationRequestTypeDef(TypedDict):
    recoveryInstanceID: str
    bandwidthThrottling: NotRequired[int]
    name: NotRequired[str]
    usePrivateIP: NotRequired[bool]

class CreateSourceNetworkResponseTypeDef(TypedDict):
    sourceNetworkID: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSourceNetworkCfnTemplateResponseTypeDef(TypedDict):
    s3DestinationUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFailbackReplicationConfigurationResponseTypeDef(TypedDict):
    bandwidthThrottling: int
    name: str
    recoveryInstanceID: str
    usePrivateIP: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListStagingAccountsResponseTypeDef(TypedDict):
    accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReverseReplicationResponseTypeDef(TypedDict):
    reversedDirectionSourceServerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConversionPropertiesTypeDef(TypedDict):
    dataTimestamp: NotRequired[str]
    forceUefi: NotRequired[bool]
    rootVolumeName: NotRequired[str]
    volumeToConversionMap: NotRequired[Dict[str, Dict[str, str]]]
    volumeToProductCodes: NotRequired[Dict[str, List[ProductCodeTypeDef]]]
    volumeToVolumeSize: NotRequired[Dict[str, int]]

class CreateLaunchConfigurationTemplateRequestTypeDef(TypedDict):
    copyPrivateIp: NotRequired[bool]
    copyTags: NotRequired[bool]
    exportBucketArn: NotRequired[str]
    launchDisposition: NotRequired[LaunchDispositionType]
    launchIntoSourceInstance: NotRequired[bool]
    licensing: NotRequired[LicensingTypeDef]
    postLaunchEnabled: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]
    targetInstanceTypeRightSizingMethod: NotRequired[TargetInstanceTypeRightSizingMethodType]

class LaunchConfigurationTemplateTypeDef(TypedDict):
    arn: NotRequired[str]
    copyPrivateIp: NotRequired[bool]
    copyTags: NotRequired[bool]
    exportBucketArn: NotRequired[str]
    launchConfigurationTemplateID: NotRequired[str]
    launchDisposition: NotRequired[LaunchDispositionType]
    launchIntoSourceInstance: NotRequired[bool]
    licensing: NotRequired[LicensingTypeDef]
    postLaunchEnabled: NotRequired[bool]
    tags: NotRequired[Dict[str, str]]
    targetInstanceTypeRightSizingMethod: NotRequired[TargetInstanceTypeRightSizingMethodType]

class UpdateLaunchConfigurationTemplateRequestTypeDef(TypedDict):
    launchConfigurationTemplateID: str
    copyPrivateIp: NotRequired[bool]
    copyTags: NotRequired[bool]
    exportBucketArn: NotRequired[str]
    launchDisposition: NotRequired[LaunchDispositionType]
    launchIntoSourceInstance: NotRequired[bool]
    licensing: NotRequired[LicensingTypeDef]
    postLaunchEnabled: NotRequired[bool]
    targetInstanceTypeRightSizingMethod: NotRequired[TargetInstanceTypeRightSizingMethodType]

class CreateReplicationConfigurationTemplateRequestTypeDef(TypedDict):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    pitPolicy: Sequence[PITPolicyRuleTypeDef]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: Sequence[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Mapping[str, str]
    useDedicatedReplicationServer: bool
    autoReplicateNewDisks: NotRequired[bool]
    ebsEncryptionKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ReplicationConfigurationTemplateResponseTypeDef(TypedDict):
    arn: str
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    pitPolicy: List[PITPolicyRuleTypeDef]
    replicationConfigurationTemplateID: str
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    tags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationTemplateTypeDef(TypedDict):
    replicationConfigurationTemplateID: str
    arn: NotRequired[str]
    associateDefaultSecurityGroup: NotRequired[bool]
    autoReplicateNewDisks: NotRequired[bool]
    bandwidthThrottling: NotRequired[int]
    createPublicIP: NotRequired[bool]
    dataPlaneRouting: NotRequired[ReplicationConfigurationDataPlaneRoutingType]
    defaultLargeStagingDiskType: NotRequired[
        ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ]
    ebsEncryption: NotRequired[ReplicationConfigurationEbsEncryptionType]
    ebsEncryptionKeyArn: NotRequired[str]
    pitPolicy: NotRequired[List[PITPolicyRuleTypeDef]]
    replicationServerInstanceType: NotRequired[str]
    replicationServersSecurityGroupsIDs: NotRequired[List[str]]
    stagingAreaSubnetId: NotRequired[str]
    stagingAreaTags: NotRequired[Dict[str, str]]
    tags: NotRequired[Dict[str, str]]
    useDedicatedReplicationServer: NotRequired[bool]

class UpdateReplicationConfigurationTemplateRequestTypeDef(TypedDict):
    replicationConfigurationTemplateID: str
    arn: NotRequired[str]
    associateDefaultSecurityGroup: NotRequired[bool]
    autoReplicateNewDisks: NotRequired[bool]
    bandwidthThrottling: NotRequired[int]
    createPublicIP: NotRequired[bool]
    dataPlaneRouting: NotRequired[ReplicationConfigurationDataPlaneRoutingType]
    defaultLargeStagingDiskType: NotRequired[
        ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ]
    ebsEncryption: NotRequired[ReplicationConfigurationEbsEncryptionType]
    ebsEncryptionKeyArn: NotRequired[str]
    pitPolicy: NotRequired[Sequence[PITPolicyRuleTypeDef]]
    replicationServerInstanceType: NotRequired[str]
    replicationServersSecurityGroupsIDs: NotRequired[Sequence[str]]
    stagingAreaSubnetId: NotRequired[str]
    stagingAreaTags: NotRequired[Mapping[str, str]]
    useDedicatedReplicationServer: NotRequired[bool]

class DataReplicationInitiationTypeDef(TypedDict):
    nextAttemptDateTime: NotRequired[str]
    startDateTime: NotRequired[str]
    steps: NotRequired[List[DataReplicationInitiationStepTypeDef]]

class DescribeJobLogItemsRequestPaginateTypeDef(TypedDict):
    jobID: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef(TypedDict):
    launchConfigurationTemplateIDs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef(TypedDict):
    replicationConfigurationTemplateIDs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExtensibleSourceServersRequestPaginateTypeDef(TypedDict):
    stagingAccountID: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStagingAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeJobsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[DescribeJobsRequestFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeJobsRequestTypeDef(TypedDict):
    filters: NotRequired[DescribeJobsRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeRecoveryInstancesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[DescribeRecoveryInstancesRequestFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRecoveryInstancesRequestTypeDef(TypedDict):
    filters: NotRequired[DescribeRecoveryInstancesRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeRecoverySnapshotsRequestPaginateTypeDef(TypedDict):
    sourceServerID: str
    filters: NotRequired[DescribeRecoverySnapshotsRequestFiltersTypeDef]
    order: NotRequired[RecoverySnapshotsOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRecoverySnapshotsRequestTypeDef(TypedDict):
    sourceServerID: str
    filters: NotRequired[DescribeRecoverySnapshotsRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    order: NotRequired[RecoverySnapshotsOrderType]

class DescribeRecoverySnapshotsResponseTypeDef(TypedDict):
    items: List[RecoverySnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeSourceNetworksRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[DescribeSourceNetworksRequestFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSourceNetworksRequestTypeDef(TypedDict):
    filters: NotRequired[DescribeSourceNetworksRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeSourceServersRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[DescribeSourceServersRequestFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSourceServersRequestTypeDef(TypedDict):
    filters: NotRequired[DescribeSourceServersRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class EventResourceDataTypeDef(TypedDict):
    sourceNetworkData: NotRequired[SourceNetworkDataTypeDef]

LaunchActionTypeDef = TypedDict(
    "LaunchActionTypeDef",
    {
        "actionCode": NotRequired[str],
        "actionId": NotRequired[str],
        "actionVersion": NotRequired[str],
        "active": NotRequired[bool],
        "category": NotRequired[LaunchActionCategoryType],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "optional": NotRequired[bool],
        "order": NotRequired[int],
        "parameters": NotRequired[Dict[str, LaunchActionParameterTypeDef]],
        "type": NotRequired[LaunchActionTypeType],
    },
)

class PutLaunchActionRequestTypeDef(TypedDict):
    actionCode: str
    actionId: str
    actionVersion: str
    active: bool
    category: LaunchActionCategoryType
    description: str
    name: str
    optional: bool
    order: int
    resourceId: str
    parameters: NotRequired[Mapping[str, LaunchActionParameterTypeDef]]

PutLaunchActionResponseTypeDef = TypedDict(
    "PutLaunchActionResponseTypeDef",
    {
        "actionCode": str,
        "actionId": str,
        "actionVersion": str,
        "active": bool,
        "category": LaunchActionCategoryType,
        "description": str,
        "name": str,
        "optional": bool,
        "order": int,
        "parameters": Dict[str, LaunchActionParameterTypeDef],
        "resourceId": str,
        "type": LaunchActionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListLaunchActionsRequestPaginateTypeDef(TypedDict):
    resourceId: str
    filters: NotRequired[LaunchActionsRequestFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLaunchActionsRequestTypeDef(TypedDict):
    resourceId: str
    filters: NotRequired[LaunchActionsRequestFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class LaunchConfigurationTypeDef(TypedDict):
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    launchDisposition: LaunchDispositionType
    launchIntoInstanceProperties: LaunchIntoInstancePropertiesTypeDef
    licensing: LicensingTypeDef
    name: str
    postLaunchEnabled: bool
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchConfigurationRequestTypeDef(TypedDict):
    sourceServerID: str
    copyPrivateIp: NotRequired[bool]
    copyTags: NotRequired[bool]
    launchDisposition: NotRequired[LaunchDispositionType]
    launchIntoInstanceProperties: NotRequired[LaunchIntoInstancePropertiesTypeDef]
    licensing: NotRequired[LicensingTypeDef]
    name: NotRequired[str]
    postLaunchEnabled: NotRequired[bool]
    targetInstanceTypeRightSizingMethod: NotRequired[TargetInstanceTypeRightSizingMethodType]

class LifeCycleLastLaunchTypeDef(TypedDict):
    initiated: NotRequired[LifeCycleLastLaunchInitiatedTypeDef]
    status: NotRequired[LaunchStatusType]

class ListExtensibleSourceServersResponseTypeDef(TypedDict):
    items: List[StagingSourceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SourcePropertiesTypeDef(TypedDict):
    cpus: NotRequired[List[CPUTypeDef]]
    disks: NotRequired[List[DiskTypeDef]]
    identificationHints: NotRequired[IdentificationHintsTypeDef]
    lastUpdatedDateTime: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    os: NotRequired[OSTypeDef]
    ramBytes: NotRequired[int]
    recommendedInstanceType: NotRequired[str]
    supportsNitroInstances: NotRequired[bool]

class ParticipatingResourceTypeDef(TypedDict):
    launchStatus: NotRequired[LaunchStatusType]
    participatingResourceID: NotRequired[ParticipatingResourceIDTypeDef]

class RecoveryInstanceDataReplicationInitiationTypeDef(TypedDict):
    startDateTime: NotRequired[str]
    steps: NotRequired[List[RecoveryInstanceDataReplicationInitiationStepTypeDef]]

class RecoveryInstancePropertiesTypeDef(TypedDict):
    cpus: NotRequired[List[CPUTypeDef]]
    disks: NotRequired[List[RecoveryInstanceDiskTypeDef]]
    identificationHints: NotRequired[IdentificationHintsTypeDef]
    lastUpdatedDateTime: NotRequired[str]
    networkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    os: NotRequired[OSTypeDef]
    ramBytes: NotRequired[int]

class SourceNetworkTypeDef(TypedDict):
    arn: NotRequired[str]
    cfnStackName: NotRequired[str]
    lastRecovery: NotRequired[RecoveryLifeCycleTypeDef]
    launchedVpcID: NotRequired[str]
    replicationStatus: NotRequired[ReplicationStatusType]
    replicationStatusDetails: NotRequired[str]
    sourceAccountID: NotRequired[str]
    sourceNetworkID: NotRequired[str]
    sourceRegion: NotRequired[str]
    sourceVpcID: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ReplicationConfigurationTypeDef(TypedDict):
    associateDefaultSecurityGroup: bool
    autoReplicateNewDisks: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ebsEncryption: ReplicationConfigurationEbsEncryptionType
    ebsEncryptionKeyArn: str
    name: str
    pitPolicy: List[PITPolicyRuleTypeDef]
    replicatedDisks: List[ReplicationConfigurationReplicatedDiskTypeDef]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReplicationConfigurationRequestTypeDef(TypedDict):
    sourceServerID: str
    associateDefaultSecurityGroup: NotRequired[bool]
    autoReplicateNewDisks: NotRequired[bool]
    bandwidthThrottling: NotRequired[int]
    createPublicIP: NotRequired[bool]
    dataPlaneRouting: NotRequired[ReplicationConfigurationDataPlaneRoutingType]
    defaultLargeStagingDiskType: NotRequired[
        ReplicationConfigurationDefaultLargeStagingDiskTypeType
    ]
    ebsEncryption: NotRequired[ReplicationConfigurationEbsEncryptionType]
    ebsEncryptionKeyArn: NotRequired[str]
    name: NotRequired[str]
    pitPolicy: NotRequired[Sequence[PITPolicyRuleTypeDef]]
    replicatedDisks: NotRequired[Sequence[ReplicationConfigurationReplicatedDiskTypeDef]]
    replicationServerInstanceType: NotRequired[str]
    replicationServersSecurityGroupsIDs: NotRequired[Sequence[str]]
    stagingAreaSubnetId: NotRequired[str]
    stagingAreaTags: NotRequired[Mapping[str, str]]
    useDedicatedReplicationServer: NotRequired[bool]

class StartRecoveryRequestTypeDef(TypedDict):
    sourceServers: Sequence[StartRecoveryRequestSourceServerTypeDef]
    isDrill: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class StartSourceNetworkRecoveryRequestTypeDef(TypedDict):
    sourceNetworks: Sequence[StartSourceNetworkRecoveryRequestNetworkEntryTypeDef]
    deployAsNew: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class CreateLaunchConfigurationTemplateResponseTypeDef(TypedDict):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchConfigurationTemplatesResponseTypeDef(TypedDict):
    items: List[LaunchConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateLaunchConfigurationTemplateResponseTypeDef(TypedDict):
    launchConfigurationTemplate: LaunchConfigurationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationConfigurationTemplatesResponseTypeDef(TypedDict):
    items: List[ReplicationConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataReplicationInfoTypeDef(TypedDict):
    dataReplicationError: NotRequired[DataReplicationErrorTypeDef]
    dataReplicationInitiation: NotRequired[DataReplicationInitiationTypeDef]
    dataReplicationState: NotRequired[DataReplicationStateType]
    etaDateTime: NotRequired[str]
    lagDuration: NotRequired[str]
    replicatedDisks: NotRequired[List[DataReplicationInfoReplicatedDiskTypeDef]]
    stagingAvailabilityZone: NotRequired[str]
    stagingOutpostArn: NotRequired[str]

class JobLogEventDataTypeDef(TypedDict):
    conversionProperties: NotRequired[ConversionPropertiesTypeDef]
    conversionServerID: NotRequired[str]
    eventResourceData: NotRequired[EventResourceDataTypeDef]
    rawError: NotRequired[str]
    sourceServerID: NotRequired[str]
    targetInstanceID: NotRequired[str]

class LaunchActionRunTypeDef(TypedDict):
    action: NotRequired[LaunchActionTypeDef]
    failureReason: NotRequired[str]
    runId: NotRequired[str]
    status: NotRequired[LaunchActionRunStatusType]

class ListLaunchActionsResponseTypeDef(TypedDict):
    items: List[LaunchActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class LifeCycleTypeDef(TypedDict):
    addedToServiceDateTime: NotRequired[str]
    elapsedReplicationDuration: NotRequired[str]
    firstByteDateTime: NotRequired[str]
    lastLaunch: NotRequired[LifeCycleLastLaunchTypeDef]
    lastSeenByServiceDateTime: NotRequired[str]

class RecoveryInstanceDataReplicationInfoTypeDef(TypedDict):
    dataReplicationError: NotRequired[RecoveryInstanceDataReplicationErrorTypeDef]
    dataReplicationInitiation: NotRequired[RecoveryInstanceDataReplicationInitiationTypeDef]
    dataReplicationState: NotRequired[RecoveryInstanceDataReplicationStateType]
    etaDateTime: NotRequired[str]
    lagDuration: NotRequired[str]
    replicatedDisks: NotRequired[List[RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef]]
    stagingAvailabilityZone: NotRequired[str]
    stagingOutpostArn: NotRequired[str]

class DescribeSourceNetworksResponseTypeDef(TypedDict):
    items: List[SourceNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartSourceNetworkReplicationResponseTypeDef(TypedDict):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopSourceNetworkReplicationResponseTypeDef(TypedDict):
    sourceNetwork: SourceNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobLogTypeDef(TypedDict):
    event: NotRequired[JobLogEventType]
    eventData: NotRequired[JobLogEventDataTypeDef]
    logDateTime: NotRequired[str]

class LaunchActionsStatusTypeDef(TypedDict):
    runs: NotRequired[List[LaunchActionRunTypeDef]]
    ssmAgentDiscoveryDatetime: NotRequired[str]

class SourceServerResponseTypeDef(TypedDict):
    agentVersion: str
    arn: str
    dataReplicationInfo: DataReplicationInfoTypeDef
    lastLaunchResult: LastLaunchResultType
    lifeCycle: LifeCycleTypeDef
    recoveryInstanceId: str
    replicationDirection: ReplicationDirectionType
    reversedDirectionSourceServerArn: str
    sourceCloudProperties: SourceCloudPropertiesTypeDef
    sourceNetworkID: str
    sourceProperties: SourcePropertiesTypeDef
    sourceServerID: str
    stagingArea: StagingAreaTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceServerTypeDef(TypedDict):
    agentVersion: NotRequired[str]
    arn: NotRequired[str]
    dataReplicationInfo: NotRequired[DataReplicationInfoTypeDef]
    lastLaunchResult: NotRequired[LastLaunchResultType]
    lifeCycle: NotRequired[LifeCycleTypeDef]
    recoveryInstanceId: NotRequired[str]
    replicationDirection: NotRequired[ReplicationDirectionType]
    reversedDirectionSourceServerArn: NotRequired[str]
    sourceCloudProperties: NotRequired[SourceCloudPropertiesTypeDef]
    sourceNetworkID: NotRequired[str]
    sourceProperties: NotRequired[SourcePropertiesTypeDef]
    sourceServerID: NotRequired[str]
    stagingArea: NotRequired[StagingAreaTypeDef]
    tags: NotRequired[Dict[str, str]]

class RecoveryInstanceTypeDef(TypedDict):
    agentVersion: NotRequired[str]
    arn: NotRequired[str]
    dataReplicationInfo: NotRequired[RecoveryInstanceDataReplicationInfoTypeDef]
    ec2InstanceID: NotRequired[str]
    ec2InstanceState: NotRequired[EC2InstanceStateType]
    failback: NotRequired[RecoveryInstanceFailbackTypeDef]
    isDrill: NotRequired[bool]
    jobID: NotRequired[str]
    originAvailabilityZone: NotRequired[str]
    originEnvironment: NotRequired[OriginEnvironmentType]
    pointInTimeSnapshotDateTime: NotRequired[str]
    recoveryInstanceID: NotRequired[str]
    recoveryInstanceProperties: NotRequired[RecoveryInstancePropertiesTypeDef]
    sourceOutpostArn: NotRequired[str]
    sourceServerID: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class DescribeJobLogItemsResponseTypeDef(TypedDict):
    items: List[JobLogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ParticipatingServerTypeDef(TypedDict):
    launchActionsStatus: NotRequired[LaunchActionsStatusTypeDef]
    launchStatus: NotRequired[LaunchStatusType]
    recoveryInstanceID: NotRequired[str]
    sourceServerID: NotRequired[str]

class CreateExtendedSourceServerResponseTypeDef(TypedDict):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceServersResponseTypeDef(TypedDict):
    items: List[SourceServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartReplicationResponseTypeDef(TypedDict):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationResponseTypeDef(TypedDict):
    sourceServer: SourceServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecoveryInstancesResponseTypeDef(TypedDict):
    items: List[RecoveryInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "jobID": str,
        "arn": NotRequired[str],
        "creationDateTime": NotRequired[str],
        "endDateTime": NotRequired[str],
        "initiatedBy": NotRequired[InitiatedByType],
        "participatingResources": NotRequired[List[ParticipatingResourceTypeDef]],
        "participatingServers": NotRequired[List[ParticipatingServerTypeDef]],
        "status": NotRequired[JobStatusType],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[JobTypeType],
    },
)

class AssociateSourceNetworkStackResponseTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(TypedDict):
    items: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartFailbackLaunchResponseTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecoveryResponseTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSourceNetworkRecoveryResponseTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateRecoveryInstancesResponseTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
