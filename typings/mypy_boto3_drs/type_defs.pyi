"""
Type annotations for drs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_drs.type_defs import AccountTypeDef

    data: AccountTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountTypeDef",
    "AssociateSourceNetworkStackRequestRequestTypeDef",
    "AssociateSourceNetworkStackResponseTypeDef",
    "CPUTypeDef",
    "ConversionPropertiesTypeDef",
    "CreateExtendedSourceServerRequestRequestTypeDef",
    "CreateExtendedSourceServerResponseTypeDef",
    "CreateLaunchConfigurationTemplateRequestRequestTypeDef",
    "CreateLaunchConfigurationTemplateResponseTypeDef",
    "CreateReplicationConfigurationTemplateRequestRequestTypeDef",
    "CreateSourceNetworkRequestRequestTypeDef",
    "CreateSourceNetworkResponseTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteLaunchActionRequestRequestTypeDef",
    "DeleteLaunchConfigurationTemplateRequestRequestTypeDef",
    "DeleteRecoveryInstanceRequestRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    "DeleteSourceNetworkRequestRequestTypeDef",
    "DeleteSourceServerRequestRequestTypeDef",
    "DescribeJobLogItemsRequestRequestTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeLaunchConfigurationTemplatesRequestRequestTypeDef",
    "DescribeLaunchConfigurationTemplatesResponseTypeDef",
    "DescribeRecoveryInstancesRequestFiltersTypeDef",
    "DescribeRecoveryInstancesRequestRequestTypeDef",
    "DescribeRecoveryInstancesResponseTypeDef",
    "DescribeRecoverySnapshotsRequestFiltersTypeDef",
    "DescribeRecoverySnapshotsRequestRequestTypeDef",
    "DescribeRecoverySnapshotsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceNetworksRequestFiltersTypeDef",
    "DescribeSourceNetworksRequestRequestTypeDef",
    "DescribeSourceNetworksResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestRequestTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DisconnectRecoveryInstanceRequestRequestTypeDef",
    "DisconnectSourceServerRequestRequestTypeDef",
    "DiskTypeDef",
    "EventResourceDataTypeDef",
    "ExportSourceNetworkCfnTemplateRequestRequestTypeDef",
    "ExportSourceNetworkCfnTemplateResponseTypeDef",
    "GetFailbackReplicationConfigurationRequestRequestTypeDef",
    "GetFailbackReplicationConfigurationResponseTypeDef",
    "GetLaunchConfigurationRequestRequestTypeDef",
    "GetReplicationConfigurationRequestRequestTypeDef",
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
    "ListExtensibleSourceServersRequestRequestTypeDef",
    "ListExtensibleSourceServersResponseTypeDef",
    "ListLaunchActionsRequestRequestTypeDef",
    "ListLaunchActionsResponseTypeDef",
    "ListStagingAccountsRequestRequestTypeDef",
    "ListStagingAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PITPolicyRuleTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingResourceIDTypeDef",
    "ParticipatingResourceTypeDef",
    "ParticipatingServerTypeDef",
    "ProductCodeTypeDef",
    "PutLaunchActionRequestRequestTypeDef",
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
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestRequestTypeDef",
    "ReverseReplicationRequestRequestTypeDef",
    "ReverseReplicationResponseTypeDef",
    "SourceCloudPropertiesTypeDef",
    "SourceNetworkDataTypeDef",
    "SourceNetworkTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerResponseMetadataTypeDef",
    "SourceServerTypeDef",
    "StagingAreaTypeDef",
    "StagingSourceServerTypeDef",
    "StartFailbackLaunchRequestRequestTypeDef",
    "StartFailbackLaunchResponseTypeDef",
    "StartRecoveryRequestRequestTypeDef",
    "StartRecoveryRequestSourceServerTypeDef",
    "StartRecoveryResponseTypeDef",
    "StartReplicationRequestRequestTypeDef",
    "StartReplicationResponseTypeDef",
    "StartSourceNetworkRecoveryRequestNetworkEntryTypeDef",
    "StartSourceNetworkRecoveryRequestRequestTypeDef",
    "StartSourceNetworkRecoveryResponseTypeDef",
    "StartSourceNetworkReplicationRequestRequestTypeDef",
    "StartSourceNetworkReplicationResponseTypeDef",
    "StopFailbackRequestRequestTypeDef",
    "StopReplicationRequestRequestTypeDef",
    "StopReplicationResponseTypeDef",
    "StopSourceNetworkReplicationRequestRequestTypeDef",
    "StopSourceNetworkReplicationResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerminateRecoveryInstancesRequestRequestTypeDef",
    "TerminateRecoveryInstancesResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFailbackReplicationConfigurationRequestRequestTypeDef",
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    "UpdateLaunchConfigurationTemplateRequestRequestTypeDef",
    "UpdateLaunchConfigurationTemplateResponseTypeDef",
    "UpdateReplicationConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestRequestTypeDef",
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "accountID": str,
    },
    total=False,
)

AssociateSourceNetworkStackRequestRequestTypeDef = TypedDict(
    "AssociateSourceNetworkStackRequestRequestTypeDef",
    {
        "cfnStackName": str,
        "sourceNetworkID": str,
    },
)

AssociateSourceNetworkStackResponseTypeDef = TypedDict(
    "AssociateSourceNetworkStackResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "cores": int,
        "modelName": str,
    },
    total=False,
)

ConversionPropertiesTypeDef = TypedDict(
    "ConversionPropertiesTypeDef",
    {
        "dataTimestamp": str,
        "forceUefi": bool,
        "rootVolumeName": str,
        "volumeToConversionMap": Dict[str, Dict[str, str]],
        "volumeToProductCodes": Dict[str, List["ProductCodeTypeDef"]],
        "volumeToVolumeSize": Dict[str, int],
    },
    total=False,
)

_RequiredCreateExtendedSourceServerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExtendedSourceServerRequestRequestTypeDef",
    {
        "sourceServerArn": str,
    },
)
_OptionalCreateExtendedSourceServerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExtendedSourceServerRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateExtendedSourceServerRequestRequestTypeDef(
    _RequiredCreateExtendedSourceServerRequestRequestTypeDef,
    _OptionalCreateExtendedSourceServerRequestRequestTypeDef,
):
    pass

CreateExtendedSourceServerResponseTypeDef = TypedDict(
    "CreateExtendedSourceServerResponseTypeDef",
    {
        "sourceServer": "SourceServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "CreateLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "exportBucketArn": str,
        "launchDisposition": LaunchDispositionType,
        "launchIntoSourceInstance": bool,
        "licensing": "LicensingTypeDef",
        "postLaunchEnabled": bool,
        "tags": Dict[str, str],
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

CreateLaunchConfigurationTemplateResponseTypeDef = TypedDict(
    "CreateLaunchConfigurationTemplateResponseTypeDef",
    {
        "launchConfigurationTemplate": "LaunchConfigurationTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
)
_OptionalCreateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "autoReplicateNewDisks": bool,
        "ebsEncryptionKeyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateReplicationConfigurationTemplateRequestRequestTypeDef(
    _RequiredCreateReplicationConfigurationTemplateRequestRequestTypeDef,
    _OptionalCreateReplicationConfigurationTemplateRequestRequestTypeDef,
):
    pass

_RequiredCreateSourceNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSourceNetworkRequestRequestTypeDef",
    {
        "originAccountID": str,
        "originRegion": str,
        "vpcID": str,
    },
)
_OptionalCreateSourceNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSourceNetworkRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSourceNetworkRequestRequestTypeDef(
    _RequiredCreateSourceNetworkRequestRequestTypeDef,
    _OptionalCreateSourceNetworkRequestRequestTypeDef,
):
    pass

CreateSourceNetworkResponseTypeDef = TypedDict(
    "CreateSourceNetworkResponseTypeDef",
    {
        "sourceNetworkID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataReplicationErrorTypeDef = TypedDict(
    "DataReplicationErrorTypeDef",
    {
        "error": DataReplicationErrorStringType,
        "rawError": str,
    },
    total=False,
)

DataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "DataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": int,
        "deviceName": str,
        "replicatedStorageBytes": int,
        "rescannedStorageBytes": int,
        "totalStorageBytes": int,
        "volumeStatus": VolumeStatusType,
    },
    total=False,
)

DataReplicationInfoTypeDef = TypedDict(
    "DataReplicationInfoTypeDef",
    {
        "dataReplicationError": "DataReplicationErrorTypeDef",
        "dataReplicationInitiation": "DataReplicationInitiationTypeDef",
        "dataReplicationState": DataReplicationStateType,
        "etaDateTime": str,
        "lagDuration": str,
        "replicatedDisks": List["DataReplicationInfoReplicatedDiskTypeDef"],
        "stagingAvailabilityZone": str,
        "stagingOutpostArn": str,
    },
    total=False,
)

DataReplicationInitiationStepTypeDef = TypedDict(
    "DataReplicationInitiationStepTypeDef",
    {
        "name": DataReplicationInitiationStepNameType,
        "status": DataReplicationInitiationStepStatusType,
    },
    total=False,
)

DataReplicationInitiationTypeDef = TypedDict(
    "DataReplicationInitiationTypeDef",
    {
        "nextAttemptDateTime": str,
        "startDateTime": str,
        "steps": List["DataReplicationInitiationStepTypeDef"],
    },
    total=False,
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "jobID": str,
    },
)

DeleteLaunchActionRequestRequestTypeDef = TypedDict(
    "DeleteLaunchActionRequestRequestTypeDef",
    {
        "actionId": str,
        "resourceId": str,
    },
)

DeleteLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "launchConfigurationTemplateID": str,
    },
)

DeleteRecoveryInstanceRequestRequestTypeDef = TypedDict(
    "DeleteRecoveryInstanceRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

DeleteReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)

DeleteSourceNetworkRequestRequestTypeDef = TypedDict(
    "DeleteSourceNetworkRequestRequestTypeDef",
    {
        "sourceNetworkID": str,
    },
)

DeleteSourceServerRequestRequestTypeDef = TypedDict(
    "DeleteSourceServerRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

_RequiredDescribeJobLogItemsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeJobLogItemsRequestRequestTypeDef",
    {
        "jobID": str,
    },
)
_OptionalDescribeJobLogItemsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeJobLogItemsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class DescribeJobLogItemsRequestRequestTypeDef(
    _RequiredDescribeJobLogItemsRequestRequestTypeDef,
    _OptionalDescribeJobLogItemsRequestRequestTypeDef,
):
    pass

DescribeJobLogItemsResponseTypeDef = TypedDict(
    "DescribeJobLogItemsResponseTypeDef",
    {
        "items": List["JobLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestFiltersTypeDef = TypedDict(
    "DescribeJobsRequestFiltersTypeDef",
    {
        "fromDate": str,
        "jobIDs": List[str],
        "toDate": str,
    },
    total=False,
)

DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "filters": "DescribeJobsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "items": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchConfigurationTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeLaunchConfigurationTemplatesRequestRequestTypeDef",
    {
        "launchConfigurationTemplateIDs": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeLaunchConfigurationTemplatesResponseTypeDef = TypedDict(
    "DescribeLaunchConfigurationTemplatesResponseTypeDef",
    {
        "items": List["LaunchConfigurationTemplateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecoveryInstancesRequestFiltersTypeDef = TypedDict(
    "DescribeRecoveryInstancesRequestFiltersTypeDef",
    {
        "recoveryInstanceIDs": List[str],
        "sourceServerIDs": List[str],
    },
    total=False,
)

DescribeRecoveryInstancesRequestRequestTypeDef = TypedDict(
    "DescribeRecoveryInstancesRequestRequestTypeDef",
    {
        "filters": "DescribeRecoveryInstancesRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeRecoveryInstancesResponseTypeDef = TypedDict(
    "DescribeRecoveryInstancesResponseTypeDef",
    {
        "items": List["RecoveryInstanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecoverySnapshotsRequestFiltersTypeDef = TypedDict(
    "DescribeRecoverySnapshotsRequestFiltersTypeDef",
    {
        "fromDateTime": str,
        "toDateTime": str,
    },
    total=False,
)

_RequiredDescribeRecoverySnapshotsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRecoverySnapshotsRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalDescribeRecoverySnapshotsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRecoverySnapshotsRequestRequestTypeDef",
    {
        "filters": "DescribeRecoverySnapshotsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
        "order": RecoverySnapshotsOrderType,
    },
    total=False,
)

class DescribeRecoverySnapshotsRequestRequestTypeDef(
    _RequiredDescribeRecoverySnapshotsRequestRequestTypeDef,
    _OptionalDescribeRecoverySnapshotsRequestRequestTypeDef,
):
    pass

DescribeRecoverySnapshotsResponseTypeDef = TypedDict(
    "DescribeRecoverySnapshotsResponseTypeDef",
    {
        "items": List["RecoverySnapshotTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationConfigurationTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "replicationConfigurationTemplateIDs": List[str],
    },
    total=False,
)

DescribeReplicationConfigurationTemplatesResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    {
        "items": List["ReplicationConfigurationTemplateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSourceNetworksRequestFiltersTypeDef = TypedDict(
    "DescribeSourceNetworksRequestFiltersTypeDef",
    {
        "originAccountID": str,
        "originRegion": str,
        "sourceNetworkIDs": List[str],
    },
    total=False,
)

DescribeSourceNetworksRequestRequestTypeDef = TypedDict(
    "DescribeSourceNetworksRequestRequestTypeDef",
    {
        "filters": "DescribeSourceNetworksRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeSourceNetworksResponseTypeDef = TypedDict(
    "DescribeSourceNetworksResponseTypeDef",
    {
        "items": List["SourceNetworkTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSourceServersRequestFiltersTypeDef = TypedDict(
    "DescribeSourceServersRequestFiltersTypeDef",
    {
        "hardwareId": str,
        "sourceServerIDs": List[str],
        "stagingAccountIDs": List[str],
    },
    total=False,
)

DescribeSourceServersRequestRequestTypeDef = TypedDict(
    "DescribeSourceServersRequestRequestTypeDef",
    {
        "filters": "DescribeSourceServersRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeSourceServersResponseTypeDef = TypedDict(
    "DescribeSourceServersResponseTypeDef",
    {
        "items": List["SourceServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisconnectRecoveryInstanceRequestRequestTypeDef = TypedDict(
    "DisconnectRecoveryInstanceRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

DisconnectSourceServerRequestRequestTypeDef = TypedDict(
    "DisconnectSourceServerRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "bytes": int,
        "deviceName": str,
    },
    total=False,
)

EventResourceDataTypeDef = TypedDict(
    "EventResourceDataTypeDef",
    {
        "sourceNetworkData": "SourceNetworkDataTypeDef",
    },
    total=False,
)

ExportSourceNetworkCfnTemplateRequestRequestTypeDef = TypedDict(
    "ExportSourceNetworkCfnTemplateRequestRequestTypeDef",
    {
        "sourceNetworkID": str,
    },
)

ExportSourceNetworkCfnTemplateResponseTypeDef = TypedDict(
    "ExportSourceNetworkCfnTemplateResponseTypeDef",
    {
        "s3DestinationUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFailbackReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetFailbackReplicationConfigurationRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

GetFailbackReplicationConfigurationResponseTypeDef = TypedDict(
    "GetFailbackReplicationConfigurationResponseTypeDef",
    {
        "bandwidthThrottling": int,
        "name": str,
        "recoveryInstanceID": str,
        "usePrivateIP": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetLaunchConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

GetReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetReplicationConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

IdentificationHintsTypeDef = TypedDict(
    "IdentificationHintsTypeDef",
    {
        "awsInstanceID": str,
        "fqdn": str,
        "hostname": str,
        "vmWareUuid": str,
    },
    total=False,
)

JobLogEventDataTypeDef = TypedDict(
    "JobLogEventDataTypeDef",
    {
        "conversionProperties": "ConversionPropertiesTypeDef",
        "conversionServerID": str,
        "eventResourceData": "EventResourceDataTypeDef",
        "rawError": str,
        "sourceServerID": str,
        "targetInstanceID": str,
    },
    total=False,
)

JobLogTypeDef = TypedDict(
    "JobLogTypeDef",
    {
        "event": JobLogEventType,
        "eventData": "JobLogEventDataTypeDef",
        "logDateTime": str,
    },
    total=False,
)

_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef",
    {
        "jobID": str,
    },
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "arn": str,
        "creationDateTime": str,
        "endDateTime": str,
        "initiatedBy": InitiatedByType,
        "participatingResources": List["ParticipatingResourceTypeDef"],
        "participatingServers": List["ParticipatingServerTypeDef"],
        "status": JobStatusType,
        "tags": Dict[str, str],
        "type": JobTypeType,
    },
    total=False,
)

class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass

LaunchActionParameterTypeDef = TypedDict(
    "LaunchActionParameterTypeDef",
    {
        "type": LaunchActionParameterTypeType,
        "value": str,
    },
    total=False,
)

LaunchActionRunTypeDef = TypedDict(
    "LaunchActionRunTypeDef",
    {
        "action": "LaunchActionTypeDef",
        "failureReason": str,
        "runId": str,
        "status": LaunchActionRunStatusType,
    },
    total=False,
)

LaunchActionTypeDef = TypedDict(
    "LaunchActionTypeDef",
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
        "parameters": Dict[str, "LaunchActionParameterTypeDef"],
        "type": LaunchActionTypeType,
    },
    total=False,
)

LaunchActionsRequestFiltersTypeDef = TypedDict(
    "LaunchActionsRequestFiltersTypeDef",
    {
        "actionIds": List[str],
    },
    total=False,
)

LaunchActionsStatusTypeDef = TypedDict(
    "LaunchActionsStatusTypeDef",
    {
        "runs": List["LaunchActionRunTypeDef"],
        "ssmAgentDiscoveryDatetime": str,
    },
    total=False,
)

LaunchConfigurationTemplateTypeDef = TypedDict(
    "LaunchConfigurationTemplateTypeDef",
    {
        "arn": str,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "exportBucketArn": str,
        "launchConfigurationTemplateID": str,
        "launchDisposition": LaunchDispositionType,
        "launchIntoSourceInstance": bool,
        "licensing": "LicensingTypeDef",
        "postLaunchEnabled": bool,
        "tags": Dict[str, str],
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "launchDisposition": LaunchDispositionType,
        "launchIntoInstanceProperties": "LaunchIntoInstancePropertiesTypeDef",
        "licensing": "LicensingTypeDef",
        "name": str,
        "postLaunchEnabled": bool,
        "sourceServerID": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchIntoInstancePropertiesTypeDef = TypedDict(
    "LaunchIntoInstancePropertiesTypeDef",
    {
        "launchIntoEC2InstanceID": str,
    },
    total=False,
)

LicensingTypeDef = TypedDict(
    "LicensingTypeDef",
    {
        "osByol": bool,
    },
    total=False,
)

LifeCycleLastLaunchInitiatedTypeDef = TypedDict(
    "LifeCycleLastLaunchInitiatedTypeDef",
    {
        "apiCallDateTime": str,
        "jobID": str,
        "type": LastLaunchTypeType,
    },
    total=False,
)

LifeCycleLastLaunchTypeDef = TypedDict(
    "LifeCycleLastLaunchTypeDef",
    {
        "initiated": "LifeCycleLastLaunchInitiatedTypeDef",
        "status": LaunchStatusType,
    },
    total=False,
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": str,
        "elapsedReplicationDuration": str,
        "firstByteDateTime": str,
        "lastLaunch": "LifeCycleLastLaunchTypeDef",
        "lastSeenByServiceDateTime": str,
    },
    total=False,
)

_RequiredListExtensibleSourceServersRequestRequestTypeDef = TypedDict(
    "_RequiredListExtensibleSourceServersRequestRequestTypeDef",
    {
        "stagingAccountID": str,
    },
)
_OptionalListExtensibleSourceServersRequestRequestTypeDef = TypedDict(
    "_OptionalListExtensibleSourceServersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListExtensibleSourceServersRequestRequestTypeDef(
    _RequiredListExtensibleSourceServersRequestRequestTypeDef,
    _OptionalListExtensibleSourceServersRequestRequestTypeDef,
):
    pass

ListExtensibleSourceServersResponseTypeDef = TypedDict(
    "ListExtensibleSourceServersResponseTypeDef",
    {
        "items": List["StagingSourceServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLaunchActionsRequestRequestTypeDef",
    {
        "resourceId": str,
    },
)
_OptionalListLaunchActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLaunchActionsRequestRequestTypeDef",
    {
        "filters": "LaunchActionsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLaunchActionsRequestRequestTypeDef(
    _RequiredListLaunchActionsRequestRequestTypeDef, _OptionalListLaunchActionsRequestRequestTypeDef
):
    pass

ListLaunchActionsResponseTypeDef = TypedDict(
    "ListLaunchActionsResponseTypeDef",
    {
        "items": List["LaunchActionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStagingAccountsRequestRequestTypeDef = TypedDict(
    "ListStagingAccountsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStagingAccountsResponseTypeDef = TypedDict(
    "ListStagingAccountsResponseTypeDef",
    {
        "accounts": List["AccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "ips": List[str],
        "isPrimary": bool,
        "macAddress": str,
    },
    total=False,
)

OSTypeDef = TypedDict(
    "OSTypeDef",
    {
        "fullString": str,
    },
    total=False,
)

_RequiredPITPolicyRuleTypeDef = TypedDict(
    "_RequiredPITPolicyRuleTypeDef",
    {
        "interval": int,
        "retentionDuration": int,
        "units": PITPolicyRuleUnitsType,
    },
)
_OptionalPITPolicyRuleTypeDef = TypedDict(
    "_OptionalPITPolicyRuleTypeDef",
    {
        "enabled": bool,
        "ruleID": int,
    },
    total=False,
)

class PITPolicyRuleTypeDef(_RequiredPITPolicyRuleTypeDef, _OptionalPITPolicyRuleTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParticipatingResourceIDTypeDef = TypedDict(
    "ParticipatingResourceIDTypeDef",
    {
        "sourceNetworkID": str,
    },
    total=False,
)

ParticipatingResourceTypeDef = TypedDict(
    "ParticipatingResourceTypeDef",
    {
        "launchStatus": LaunchStatusType,
        "participatingResourceID": "ParticipatingResourceIDTypeDef",
    },
    total=False,
)

ParticipatingServerTypeDef = TypedDict(
    "ParticipatingServerTypeDef",
    {
        "launchActionsStatus": "LaunchActionsStatusTypeDef",
        "launchStatus": LaunchStatusType,
        "recoveryInstanceID": str,
        "sourceServerID": str,
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "productCodeId": str,
        "productCodeMode": ProductCodeModeType,
    },
    total=False,
)

_RequiredPutLaunchActionRequestRequestTypeDef = TypedDict(
    "_RequiredPutLaunchActionRequestRequestTypeDef",
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
        "resourceId": str,
    },
)
_OptionalPutLaunchActionRequestRequestTypeDef = TypedDict(
    "_OptionalPutLaunchActionRequestRequestTypeDef",
    {
        "parameters": Dict[str, "LaunchActionParameterTypeDef"],
    },
    total=False,
)

class PutLaunchActionRequestRequestTypeDef(
    _RequiredPutLaunchActionRequestRequestTypeDef, _OptionalPutLaunchActionRequestRequestTypeDef
):
    pass

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
        "parameters": Dict[str, "LaunchActionParameterTypeDef"],
        "resourceId": str,
        "type": LaunchActionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecoveryInstanceDataReplicationErrorTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationErrorTypeDef",
    {
        "error": FailbackReplicationErrorType,
        "rawError": str,
    },
    total=False,
)

RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": int,
        "deviceName": str,
        "replicatedStorageBytes": int,
        "rescannedStorageBytes": int,
        "totalStorageBytes": int,
    },
    total=False,
)

RecoveryInstanceDataReplicationInfoTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInfoTypeDef",
    {
        "dataReplicationError": "RecoveryInstanceDataReplicationErrorTypeDef",
        "dataReplicationInitiation": "RecoveryInstanceDataReplicationInitiationTypeDef",
        "dataReplicationState": RecoveryInstanceDataReplicationStateType,
        "etaDateTime": str,
        "lagDuration": str,
        "replicatedDisks": List["RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef"],
        "stagingAvailabilityZone": str,
        "stagingOutpostArn": str,
    },
    total=False,
)

RecoveryInstanceDataReplicationInitiationStepTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInitiationStepTypeDef",
    {
        "name": RecoveryInstanceDataReplicationInitiationStepNameType,
        "status": RecoveryInstanceDataReplicationInitiationStepStatusType,
    },
    total=False,
)

RecoveryInstanceDataReplicationInitiationTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInitiationTypeDef",
    {
        "startDateTime": str,
        "steps": List["RecoveryInstanceDataReplicationInitiationStepTypeDef"],
    },
    total=False,
)

RecoveryInstanceDiskTypeDef = TypedDict(
    "RecoveryInstanceDiskTypeDef",
    {
        "bytes": int,
        "ebsVolumeID": str,
        "internalDeviceName": str,
    },
    total=False,
)

RecoveryInstanceFailbackTypeDef = TypedDict(
    "RecoveryInstanceFailbackTypeDef",
    {
        "agentLastSeenByServiceDateTime": str,
        "elapsedReplicationDuration": str,
        "failbackClientID": str,
        "failbackClientLastSeenByServiceDateTime": str,
        "failbackInitiationTime": str,
        "failbackJobID": str,
        "failbackLaunchType": FailbackLaunchTypeType,
        "failbackToOriginalServer": bool,
        "firstByteDateTime": str,
        "state": FailbackStateType,
    },
    total=False,
)

RecoveryInstancePropertiesTypeDef = TypedDict(
    "RecoveryInstancePropertiesTypeDef",
    {
        "cpus": List["CPUTypeDef"],
        "disks": List["RecoveryInstanceDiskTypeDef"],
        "identificationHints": "IdentificationHintsTypeDef",
        "lastUpdatedDateTime": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "os": "OSTypeDef",
        "ramBytes": int,
    },
    total=False,
)

RecoveryInstanceTypeDef = TypedDict(
    "RecoveryInstanceTypeDef",
    {
        "agentVersion": str,
        "arn": str,
        "dataReplicationInfo": "RecoveryInstanceDataReplicationInfoTypeDef",
        "ec2InstanceID": str,
        "ec2InstanceState": EC2InstanceStateType,
        "failback": "RecoveryInstanceFailbackTypeDef",
        "isDrill": bool,
        "jobID": str,
        "originAvailabilityZone": str,
        "originEnvironment": OriginEnvironmentType,
        "pointInTimeSnapshotDateTime": str,
        "recoveryInstanceID": str,
        "recoveryInstanceProperties": "RecoveryInstancePropertiesTypeDef",
        "sourceOutpostArn": str,
        "sourceServerID": str,
        "tags": Dict[str, str],
    },
    total=False,
)

RecoveryLifeCycleTypeDef = TypedDict(
    "RecoveryLifeCycleTypeDef",
    {
        "apiCallDateTime": datetime,
        "jobID": str,
        "lastRecoveryResult": RecoveryResultType,
    },
    total=False,
)

_RequiredRecoverySnapshotTypeDef = TypedDict(
    "_RequiredRecoverySnapshotTypeDef",
    {
        "expectedTimestamp": str,
        "snapshotID": str,
        "sourceServerID": str,
    },
)
_OptionalRecoverySnapshotTypeDef = TypedDict(
    "_OptionalRecoverySnapshotTypeDef",
    {
        "ebsSnapshots": List[str],
        "timestamp": str,
    },
    total=False,
)

class RecoverySnapshotTypeDef(_RequiredRecoverySnapshotTypeDef, _OptionalRecoverySnapshotTypeDef):
    pass

ReplicationConfigurationReplicatedDiskTypeDef = TypedDict(
    "ReplicationConfigurationReplicatedDiskTypeDef",
    {
        "deviceName": str,
        "iops": int,
        "isBootDisk": bool,
        "optimizedStagingDiskType": ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
        "stagingDiskType": ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
        "throughput": int,
    },
    total=False,
)

ReplicationConfigurationTemplateResponseMetadataTypeDef = TypedDict(
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "autoReplicateNewDisks": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicationConfigurationTemplateID": str,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "tags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplicationConfigurationTemplateTypeDef = TypedDict(
    "_RequiredReplicationConfigurationTemplateTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)
_OptionalReplicationConfigurationTemplateTypeDef = TypedDict(
    "_OptionalReplicationConfigurationTemplateTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "autoReplicateNewDisks": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "tags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)

class ReplicationConfigurationTemplateTypeDef(
    _RequiredReplicationConfigurationTemplateTypeDef,
    _OptionalReplicationConfigurationTemplateTypeDef,
):
    pass

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "autoReplicateNewDisks": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "sourceServerID": str,
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RetryDataReplicationRequestRequestTypeDef = TypedDict(
    "RetryDataReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

ReverseReplicationRequestRequestTypeDef = TypedDict(
    "ReverseReplicationRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

ReverseReplicationResponseTypeDef = TypedDict(
    "ReverseReplicationResponseTypeDef",
    {
        "reversedDirectionSourceServerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceCloudPropertiesTypeDef = TypedDict(
    "SourceCloudPropertiesTypeDef",
    {
        "originAccountID": str,
        "originAvailabilityZone": str,
        "originRegion": str,
        "sourceOutpostArn": str,
    },
    total=False,
)

SourceNetworkDataTypeDef = TypedDict(
    "SourceNetworkDataTypeDef",
    {
        "sourceNetworkID": str,
        "sourceVpc": str,
        "stackName": str,
        "targetVpc": str,
    },
    total=False,
)

SourceNetworkTypeDef = TypedDict(
    "SourceNetworkTypeDef",
    {
        "arn": str,
        "cfnStackName": str,
        "lastRecovery": "RecoveryLifeCycleTypeDef",
        "launchedVpcID": str,
        "replicationStatus": ReplicationStatusType,
        "replicationStatusDetails": str,
        "sourceAccountID": str,
        "sourceNetworkID": str,
        "sourceRegion": str,
        "sourceVpcID": str,
        "tags": Dict[str, str],
    },
    total=False,
)

SourcePropertiesTypeDef = TypedDict(
    "SourcePropertiesTypeDef",
    {
        "cpus": List["CPUTypeDef"],
        "disks": List["DiskTypeDef"],
        "identificationHints": "IdentificationHintsTypeDef",
        "lastUpdatedDateTime": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "os": "OSTypeDef",
        "ramBytes": int,
        "recommendedInstanceType": str,
        "supportsNitroInstances": bool,
    },
    total=False,
)

SourceServerResponseMetadataTypeDef = TypedDict(
    "SourceServerResponseMetadataTypeDef",
    {
        "agentVersion": str,
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "lastLaunchResult": LastLaunchResultType,
        "lifeCycle": "LifeCycleTypeDef",
        "recoveryInstanceId": str,
        "replicationDirection": ReplicationDirectionType,
        "reversedDirectionSourceServerArn": str,
        "sourceCloudProperties": "SourceCloudPropertiesTypeDef",
        "sourceNetworkID": str,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "stagingArea": "StagingAreaTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceServerTypeDef = TypedDict(
    "SourceServerTypeDef",
    {
        "agentVersion": str,
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "lastLaunchResult": LastLaunchResultType,
        "lifeCycle": "LifeCycleTypeDef",
        "recoveryInstanceId": str,
        "replicationDirection": ReplicationDirectionType,
        "reversedDirectionSourceServerArn": str,
        "sourceCloudProperties": "SourceCloudPropertiesTypeDef",
        "sourceNetworkID": str,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "stagingArea": "StagingAreaTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

StagingAreaTypeDef = TypedDict(
    "StagingAreaTypeDef",
    {
        "errorMessage": str,
        "stagingAccountID": str,
        "stagingSourceServerArn": str,
        "status": ExtensionStatusType,
    },
    total=False,
)

StagingSourceServerTypeDef = TypedDict(
    "StagingSourceServerTypeDef",
    {
        "arn": str,
        "hostname": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredStartFailbackLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredStartFailbackLaunchRequestRequestTypeDef",
    {
        "recoveryInstanceIDs": List[str],
    },
)
_OptionalStartFailbackLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalStartFailbackLaunchRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class StartFailbackLaunchRequestRequestTypeDef(
    _RequiredStartFailbackLaunchRequestRequestTypeDef,
    _OptionalStartFailbackLaunchRequestRequestTypeDef,
):
    pass

StartFailbackLaunchResponseTypeDef = TypedDict(
    "StartFailbackLaunchResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRecoveryRequestRequestTypeDef = TypedDict(
    "_RequiredStartRecoveryRequestRequestTypeDef",
    {
        "sourceServers": List["StartRecoveryRequestSourceServerTypeDef"],
    },
)
_OptionalStartRecoveryRequestRequestTypeDef = TypedDict(
    "_OptionalStartRecoveryRequestRequestTypeDef",
    {
        "isDrill": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartRecoveryRequestRequestTypeDef(
    _RequiredStartRecoveryRequestRequestTypeDef, _OptionalStartRecoveryRequestRequestTypeDef
):
    pass

_RequiredStartRecoveryRequestSourceServerTypeDef = TypedDict(
    "_RequiredStartRecoveryRequestSourceServerTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalStartRecoveryRequestSourceServerTypeDef = TypedDict(
    "_OptionalStartRecoveryRequestSourceServerTypeDef",
    {
        "recoverySnapshotID": str,
    },
    total=False,
)

class StartRecoveryRequestSourceServerTypeDef(
    _RequiredStartRecoveryRequestSourceServerTypeDef,
    _OptionalStartRecoveryRequestSourceServerTypeDef,
):
    pass

StartRecoveryResponseTypeDef = TypedDict(
    "StartRecoveryResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationRequestRequestTypeDef = TypedDict(
    "StartReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

StartReplicationResponseTypeDef = TypedDict(
    "StartReplicationResponseTypeDef",
    {
        "sourceServer": "SourceServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSourceNetworkRecoveryRequestNetworkEntryTypeDef = TypedDict(
    "_RequiredStartSourceNetworkRecoveryRequestNetworkEntryTypeDef",
    {
        "sourceNetworkID": str,
    },
)
_OptionalStartSourceNetworkRecoveryRequestNetworkEntryTypeDef = TypedDict(
    "_OptionalStartSourceNetworkRecoveryRequestNetworkEntryTypeDef",
    {
        "cfnStackName": str,
    },
    total=False,
)

class StartSourceNetworkRecoveryRequestNetworkEntryTypeDef(
    _RequiredStartSourceNetworkRecoveryRequestNetworkEntryTypeDef,
    _OptionalStartSourceNetworkRecoveryRequestNetworkEntryTypeDef,
):
    pass

_RequiredStartSourceNetworkRecoveryRequestRequestTypeDef = TypedDict(
    "_RequiredStartSourceNetworkRecoveryRequestRequestTypeDef",
    {
        "sourceNetworks": List["StartSourceNetworkRecoveryRequestNetworkEntryTypeDef"],
    },
)
_OptionalStartSourceNetworkRecoveryRequestRequestTypeDef = TypedDict(
    "_OptionalStartSourceNetworkRecoveryRequestRequestTypeDef",
    {
        "deployAsNew": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartSourceNetworkRecoveryRequestRequestTypeDef(
    _RequiredStartSourceNetworkRecoveryRequestRequestTypeDef,
    _OptionalStartSourceNetworkRecoveryRequestRequestTypeDef,
):
    pass

StartSourceNetworkRecoveryResponseTypeDef = TypedDict(
    "StartSourceNetworkRecoveryResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSourceNetworkReplicationRequestRequestTypeDef = TypedDict(
    "StartSourceNetworkReplicationRequestRequestTypeDef",
    {
        "sourceNetworkID": str,
    },
)

StartSourceNetworkReplicationResponseTypeDef = TypedDict(
    "StartSourceNetworkReplicationResponseTypeDef",
    {
        "sourceNetwork": "SourceNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFailbackRequestRequestTypeDef = TypedDict(
    "StopFailbackRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

StopReplicationRequestRequestTypeDef = TypedDict(
    "StopReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

StopReplicationResponseTypeDef = TypedDict(
    "StopReplicationResponseTypeDef",
    {
        "sourceServer": "SourceServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSourceNetworkReplicationRequestRequestTypeDef = TypedDict(
    "StopSourceNetworkReplicationRequestRequestTypeDef",
    {
        "sourceNetworkID": str,
    },
)

StopSourceNetworkReplicationResponseTypeDef = TypedDict(
    "StopSourceNetworkReplicationResponseTypeDef",
    {
        "sourceNetwork": "SourceNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TerminateRecoveryInstancesRequestRequestTypeDef = TypedDict(
    "TerminateRecoveryInstancesRequestRequestTypeDef",
    {
        "recoveryInstanceIDs": List[str],
    },
)

TerminateRecoveryInstancesResponseTypeDef = TypedDict(
    "TerminateRecoveryInstancesResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateFailbackReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFailbackReplicationConfigurationRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)
_OptionalUpdateFailbackReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFailbackReplicationConfigurationRequestRequestTypeDef",
    {
        "bandwidthThrottling": int,
        "name": str,
        "usePrivateIP": bool,
    },
    total=False,
)

class UpdateFailbackReplicationConfigurationRequestRequestTypeDef(
    _RequiredUpdateFailbackReplicationConfigurationRequestRequestTypeDef,
    _OptionalUpdateFailbackReplicationConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalUpdateLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchConfigurationRequestRequestTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "launchDisposition": LaunchDispositionType,
        "launchIntoInstanceProperties": "LaunchIntoInstancePropertiesTypeDef",
        "licensing": "LicensingTypeDef",
        "name": str,
        "postLaunchEnabled": bool,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

class UpdateLaunchConfigurationRequestRequestTypeDef(
    _RequiredUpdateLaunchConfigurationRequestRequestTypeDef,
    _OptionalUpdateLaunchConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "launchConfigurationTemplateID": str,
    },
)
_OptionalUpdateLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "exportBucketArn": str,
        "launchDisposition": LaunchDispositionType,
        "launchIntoSourceInstance": bool,
        "licensing": "LicensingTypeDef",
        "postLaunchEnabled": bool,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(
    _RequiredUpdateLaunchConfigurationTemplateRequestRequestTypeDef,
    _OptionalUpdateLaunchConfigurationTemplateRequestRequestTypeDef,
):
    pass

UpdateLaunchConfigurationTemplateResponseTypeDef = TypedDict(
    "UpdateLaunchConfigurationTemplateResponseTypeDef",
    {
        "launchConfigurationTemplate": "LaunchConfigurationTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalUpdateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationConfigurationRequestRequestTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "autoReplicateNewDisks": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)

class UpdateReplicationConfigurationRequestRequestTypeDef(
    _RequiredUpdateReplicationConfigurationRequestRequestTypeDef,
    _OptionalUpdateReplicationConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)
_OptionalUpdateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "autoReplicateNewDisks": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "pitPolicy": List["PITPolicyRuleTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)

class UpdateReplicationConfigurationTemplateRequestRequestTypeDef(
    _RequiredUpdateReplicationConfigurationTemplateRequestRequestTypeDef,
    _OptionalUpdateReplicationConfigurationTemplateRequestRequestTypeDef,
):
    pass
