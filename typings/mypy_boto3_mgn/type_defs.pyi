"""
Type annotations for mgn service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mgn.type_defs import ApplicationAggregatedStatusTypeDef

    data: ApplicationAggregatedStatusTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ActionCategoryType,
    ApplicationHealthStatusType,
    ApplicationProgressStatusType,
    BootModeType,
    ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    DataReplicationErrorStringType,
    DataReplicationInitiationStepNameType,
    DataReplicationInitiationStepStatusType,
    DataReplicationStateType,
    ExportStatusType,
    FirstBootType,
    ImportErrorTypeType,
    ImportStatusType,
    InitiatedByType,
    JobLogEventType,
    JobStatusType,
    JobTypeType,
    LaunchDispositionType,
    LaunchStatusType,
    LifeCycleStateType,
    PostLaunchActionExecutionStatusType,
    PostLaunchActionsDeploymentTypeType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    ReplicationTypeType,
    SsmDocumentTypeType,
    TargetInstanceTypeRightSizingMethodType,
    VolumeTypeType,
    WaveHealthStatusType,
    WaveProgressStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationAggregatedStatusTypeDef",
    "ApplicationResponseMetadataTypeDef",
    "ApplicationTypeDef",
    "ArchiveApplicationRequestRequestTypeDef",
    "ArchiveWaveRequestRequestTypeDef",
    "AssociateApplicationsRequestRequestTypeDef",
    "AssociateSourceServersRequestRequestTypeDef",
    "CPUTypeDef",
    "ChangeServerLifeCycleStateRequestRequestTypeDef",
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateLaunchConfigurationTemplateRequestRequestTypeDef",
    "CreateReplicationConfigurationTemplateRequestRequestTypeDef",
    "CreateWaveRequestRequestTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteLaunchConfigurationTemplateRequestRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    "DeleteSourceServerRequestRequestTypeDef",
    "DeleteVcenterClientRequestRequestTypeDef",
    "DeleteWaveRequestRequestTypeDef",
    "DescribeJobLogItemsRequestRequestTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeLaunchConfigurationTemplatesRequestRequestTypeDef",
    "DescribeLaunchConfigurationTemplatesResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestRequestTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DescribeVcenterClientsRequestRequestTypeDef",
    "DescribeVcenterClientsResponseTypeDef",
    "DisassociateApplicationsRequestRequestTypeDef",
    "DisassociateSourceServersRequestRequestTypeDef",
    "DisconnectFromServiceRequestRequestTypeDef",
    "DiskTypeDef",
    "ExportErrorDataTypeDef",
    "ExportTaskErrorTypeDef",
    "ExportTaskSummaryTypeDef",
    "ExportTaskTypeDef",
    "FinalizeCutoverRequestRequestTypeDef",
    "GetLaunchConfigurationRequestRequestTypeDef",
    "GetReplicationConfigurationRequestRequestTypeDef",
    "IdentificationHintsTypeDef",
    "ImportErrorDataTypeDef",
    "ImportTaskErrorTypeDef",
    "ImportTaskSummaryApplicationsTypeDef",
    "ImportTaskSummaryServersTypeDef",
    "ImportTaskSummaryTypeDef",
    "ImportTaskSummaryWavesTypeDef",
    "ImportTaskTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobPostLaunchActionsLaunchStatusTypeDef",
    "JobTypeDef",
    "LaunchConfigurationTemplateResponseMetadataTypeDef",
    "LaunchConfigurationTemplateTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateDiskConfTypeDef",
    "LaunchedInstanceTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastCutoverFinalizedTypeDef",
    "LifeCycleLastCutoverInitiatedTypeDef",
    "LifeCycleLastCutoverRevertedTypeDef",
    "LifeCycleLastCutoverTypeDef",
    "LifeCycleLastTestFinalizedTypeDef",
    "LifeCycleLastTestInitiatedTypeDef",
    "LifeCycleLastTestRevertedTypeDef",
    "LifeCycleLastTestTypeDef",
    "LifeCycleTypeDef",
    "ListApplicationsRequestFiltersTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListExportErrorsRequestRequestTypeDef",
    "ListExportErrorsResponseTypeDef",
    "ListExportsRequestFiltersTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListExportsResponseTypeDef",
    "ListImportErrorsRequestRequestTypeDef",
    "ListImportErrorsResponseTypeDef",
    "ListImportsRequestFiltersTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListImportsResponseTypeDef",
    "ListSourceServerActionsRequestRequestTypeDef",
    "ListSourceServerActionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateActionsRequestRequestTypeDef",
    "ListTemplateActionsResponseTypeDef",
    "ListWavesRequestFiltersTypeDef",
    "ListWavesRequestRequestTypeDef",
    "ListWavesResponseTypeDef",
    "MarkAsArchivedRequestRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingServerTypeDef",
    "PostLaunchActionsStatusTypeDef",
    "PostLaunchActionsTypeDef",
    "PutSourceServerActionRequestRequestTypeDef",
    "PutTemplateActionRequestRequestTypeDef",
    "RemoveSourceServerActionRequestRequestTypeDef",
    "RemoveTemplateActionRequestRequestTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestRequestTypeDef",
    "S3BucketSourceTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerActionDocumentResponseMetadataTypeDef",
    "SourceServerActionDocumentTypeDef",
    "SourceServerActionsRequestFiltersTypeDef",
    "SourceServerResponseMetadataTypeDef",
    "SourceServerTypeDef",
    "SsmDocumentTypeDef",
    "SsmExternalParameterTypeDef",
    "SsmParameterStoreParameterTypeDef",
    "StartCutoverRequestRequestTypeDef",
    "StartCutoverResponseTypeDef",
    "StartExportRequestRequestTypeDef",
    "StartExportResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartReplicationRequestRequestTypeDef",
    "StartTestRequestRequestTypeDef",
    "StartTestResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateActionDocumentResponseMetadataTypeDef",
    "TemplateActionDocumentTypeDef",
    "TemplateActionsRequestFiltersTypeDef",
    "TerminateTargetInstancesRequestRequestTypeDef",
    "TerminateTargetInstancesResponseTypeDef",
    "UnarchiveApplicationRequestRequestTypeDef",
    "UnarchiveWaveRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    "UpdateLaunchConfigurationTemplateRequestRequestTypeDef",
    "UpdateReplicationConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestRequestTypeDef",
    "UpdateSourceServerReplicationTypeRequestRequestTypeDef",
    "UpdateWaveRequestRequestTypeDef",
    "VcenterClientTypeDef",
    "WaveAggregatedStatusTypeDef",
    "WaveResponseMetadataTypeDef",
    "WaveTypeDef",
)

ApplicationAggregatedStatusTypeDef = TypedDict(
    "ApplicationAggregatedStatusTypeDef",
    {
        "healthStatus": ApplicationHealthStatusType,
        "lastUpdateDateTime": str,
        "progressStatus": ApplicationProgressStatusType,
        "totalSourceServers": int,
    },
    total=False,
)

ApplicationResponseMetadataTypeDef = TypedDict(
    "ApplicationResponseMetadataTypeDef",
    {
        "applicationAggregatedStatus": "ApplicationAggregatedStatusTypeDef",
        "applicationID": str,
        "arn": str,
        "creationDateTime": str,
        "description": str,
        "isArchived": bool,
        "lastModifiedDateTime": str,
        "name": str,
        "tags": Dict[str, str],
        "waveID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "applicationAggregatedStatus": "ApplicationAggregatedStatusTypeDef",
        "applicationID": str,
        "arn": str,
        "creationDateTime": str,
        "description": str,
        "isArchived": bool,
        "lastModifiedDateTime": str,
        "name": str,
        "tags": Dict[str, str],
        "waveID": str,
    },
    total=False,
)

ArchiveApplicationRequestRequestTypeDef = TypedDict(
    "ArchiveApplicationRequestRequestTypeDef",
    {
        "applicationID": str,
    },
)

ArchiveWaveRequestRequestTypeDef = TypedDict(
    "ArchiveWaveRequestRequestTypeDef",
    {
        "waveID": str,
    },
)

AssociateApplicationsRequestRequestTypeDef = TypedDict(
    "AssociateApplicationsRequestRequestTypeDef",
    {
        "applicationIDs": List[str],
        "waveID": str,
    },
)

AssociateSourceServersRequestRequestTypeDef = TypedDict(
    "AssociateSourceServersRequestRequestTypeDef",
    {
        "applicationID": str,
        "sourceServerIDs": List[str],
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

ChangeServerLifeCycleStateRequestRequestTypeDef = TypedDict(
    "ChangeServerLifeCycleStateRequestRequestTypeDef",
    {
        "lifeCycle": "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
        "sourceServerID": str,
    },
)

ChangeServerLifeCycleStateSourceServerLifecycleTypeDef = TypedDict(
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    {
        "state": ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "CreateLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "associatePublicIpAddress": bool,
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "enableMapAutoTagging": bool,
        "largeVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
        "smallVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "smallVolumeMaxSize": int,
        "tags": Dict[str, str],
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
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

_RequiredCreateWaveRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWaveRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateWaveRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWaveRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateWaveRequestRequestTypeDef(
    _RequiredCreateWaveRequestRequestTypeDef, _OptionalCreateWaveRequestRequestTypeDef
):
    pass

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
        "lastSnapshotDateTime": str,
        "replicatedDisks": List["DataReplicationInfoReplicatedDiskTypeDef"],
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

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationID": str,
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "jobID": str,
    },
)

DeleteLaunchConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteLaunchConfigurationTemplateRequestRequestTypeDef",
    {
        "launchConfigurationTemplateID": str,
    },
)

DeleteReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)

DeleteSourceServerRequestRequestTypeDef = TypedDict(
    "DeleteSourceServerRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

DeleteVcenterClientRequestRequestTypeDef = TypedDict(
    "DeleteVcenterClientRequestRequestTypeDef",
    {
        "vcenterClientID": str,
    },
)

DeleteWaveRequestRequestTypeDef = TypedDict(
    "DeleteWaveRequestRequestTypeDef",
    {
        "waveID": str,
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

DescribeSourceServersRequestFiltersTypeDef = TypedDict(
    "DescribeSourceServersRequestFiltersTypeDef",
    {
        "applicationIDs": List[str],
        "isArchived": bool,
        "lifeCycleStates": List[LifeCycleStateType],
        "replicationTypes": List[ReplicationTypeType],
        "sourceServerIDs": List[str],
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

DescribeVcenterClientsRequestRequestTypeDef = TypedDict(
    "DescribeVcenterClientsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeVcenterClientsResponseTypeDef = TypedDict(
    "DescribeVcenterClientsResponseTypeDef",
    {
        "items": List["VcenterClientTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateApplicationsRequestRequestTypeDef = TypedDict(
    "DisassociateApplicationsRequestRequestTypeDef",
    {
        "applicationIDs": List[str],
        "waveID": str,
    },
)

DisassociateSourceServersRequestRequestTypeDef = TypedDict(
    "DisassociateSourceServersRequestRequestTypeDef",
    {
        "applicationID": str,
        "sourceServerIDs": List[str],
    },
)

DisconnectFromServiceRequestRequestTypeDef = TypedDict(
    "DisconnectFromServiceRequestRequestTypeDef",
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

ExportErrorDataTypeDef = TypedDict(
    "ExportErrorDataTypeDef",
    {
        "rawError": str,
    },
    total=False,
)

ExportTaskErrorTypeDef = TypedDict(
    "ExportTaskErrorTypeDef",
    {
        "errorData": "ExportErrorDataTypeDef",
        "errorDateTime": str,
    },
    total=False,
)

ExportTaskSummaryTypeDef = TypedDict(
    "ExportTaskSummaryTypeDef",
    {
        "applicationsCount": int,
        "serversCount": int,
        "wavesCount": int,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "creationDateTime": str,
        "endDateTime": str,
        "exportID": str,
        "progressPercentage": float,
        "s3Bucket": str,
        "s3BucketOwner": str,
        "s3Key": str,
        "status": ExportStatusType,
        "summary": "ExportTaskSummaryTypeDef",
    },
    total=False,
)

FinalizeCutoverRequestRequestTypeDef = TypedDict(
    "FinalizeCutoverRequestRequestTypeDef",
    {
        "sourceServerID": str,
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
        "vmPath": str,
        "vmWareUuid": str,
    },
    total=False,
)

ImportErrorDataTypeDef = TypedDict(
    "ImportErrorDataTypeDef",
    {
        "applicationID": str,
        "ec2LaunchTemplateID": str,
        "rawError": str,
        "rowNumber": int,
        "sourceServerID": str,
        "waveID": str,
    },
    total=False,
)

ImportTaskErrorTypeDef = TypedDict(
    "ImportTaskErrorTypeDef",
    {
        "errorData": "ImportErrorDataTypeDef",
        "errorDateTime": str,
        "errorType": ImportErrorTypeType,
    },
    total=False,
)

ImportTaskSummaryApplicationsTypeDef = TypedDict(
    "ImportTaskSummaryApplicationsTypeDef",
    {
        "createdCount": int,
        "modifiedCount": int,
    },
    total=False,
)

ImportTaskSummaryServersTypeDef = TypedDict(
    "ImportTaskSummaryServersTypeDef",
    {
        "createdCount": int,
        "modifiedCount": int,
    },
    total=False,
)

ImportTaskSummaryTypeDef = TypedDict(
    "ImportTaskSummaryTypeDef",
    {
        "applications": "ImportTaskSummaryApplicationsTypeDef",
        "servers": "ImportTaskSummaryServersTypeDef",
        "waves": "ImportTaskSummaryWavesTypeDef",
    },
    total=False,
)

ImportTaskSummaryWavesTypeDef = TypedDict(
    "ImportTaskSummaryWavesTypeDef",
    {
        "createdCount": int,
        "modifiedCount": int,
    },
    total=False,
)

ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "creationDateTime": str,
        "endDateTime": str,
        "importID": str,
        "progressPercentage": float,
        "s3BucketSource": "S3BucketSourceTypeDef",
        "status": ImportStatusType,
        "summary": "ImportTaskSummaryTypeDef",
    },
    total=False,
)

JobLogEventDataTypeDef = TypedDict(
    "JobLogEventDataTypeDef",
    {
        "conversionServerID": str,
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

JobPostLaunchActionsLaunchStatusTypeDef = TypedDict(
    "JobPostLaunchActionsLaunchStatusTypeDef",
    {
        "executionID": str,
        "executionStatus": PostLaunchActionExecutionStatusType,
        "failureReason": str,
        "ssmDocument": "SsmDocumentTypeDef",
        "ssmDocumentType": SsmDocumentTypeType,
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
        "participatingServers": List["ParticipatingServerTypeDef"],
        "status": JobStatusType,
        "tags": Dict[str, str],
        "type": JobTypeType,
    },
    total=False,
)

class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass

LaunchConfigurationTemplateResponseMetadataTypeDef = TypedDict(
    "LaunchConfigurationTemplateResponseMetadataTypeDef",
    {
        "arn": str,
        "associatePublicIpAddress": bool,
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "enableMapAutoTagging": bool,
        "largeVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "launchConfigurationTemplateID": str,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
        "smallVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "smallVolumeMaxSize": int,
        "tags": Dict[str, str],
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLaunchConfigurationTemplateTypeDef = TypedDict(
    "_RequiredLaunchConfigurationTemplateTypeDef",
    {
        "launchConfigurationTemplateID": str,
    },
)
_OptionalLaunchConfigurationTemplateTypeDef = TypedDict(
    "_OptionalLaunchConfigurationTemplateTypeDef",
    {
        "arn": str,
        "associatePublicIpAddress": bool,
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "enableMapAutoTagging": bool,
        "largeVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
        "smallVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "smallVolumeMaxSize": int,
        "tags": Dict[str, str],
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

class LaunchConfigurationTemplateTypeDef(
    _RequiredLaunchConfigurationTemplateTypeDef, _OptionalLaunchConfigurationTemplateTypeDef
):
    pass

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "enableMapAutoTagging": bool,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "name": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
        "sourceServerID": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchTemplateDiskConfTypeDef = TypedDict(
    "LaunchTemplateDiskConfTypeDef",
    {
        "iops": int,
        "throughput": int,
        "volumeType": VolumeTypeType,
    },
    total=False,
)

LaunchedInstanceTypeDef = TypedDict(
    "LaunchedInstanceTypeDef",
    {
        "ec2InstanceID": str,
        "firstBoot": FirstBootType,
        "jobID": str,
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

LifeCycleLastCutoverFinalizedTypeDef = TypedDict(
    "LifeCycleLastCutoverFinalizedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastCutoverInitiatedTypeDef = TypedDict(
    "LifeCycleLastCutoverInitiatedTypeDef",
    {
        "apiCallDateTime": str,
        "jobID": str,
    },
    total=False,
)

LifeCycleLastCutoverRevertedTypeDef = TypedDict(
    "LifeCycleLastCutoverRevertedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastCutoverTypeDef = TypedDict(
    "LifeCycleLastCutoverTypeDef",
    {
        "finalized": "LifeCycleLastCutoverFinalizedTypeDef",
        "initiated": "LifeCycleLastCutoverInitiatedTypeDef",
        "reverted": "LifeCycleLastCutoverRevertedTypeDef",
    },
    total=False,
)

LifeCycleLastTestFinalizedTypeDef = TypedDict(
    "LifeCycleLastTestFinalizedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastTestInitiatedTypeDef = TypedDict(
    "LifeCycleLastTestInitiatedTypeDef",
    {
        "apiCallDateTime": str,
        "jobID": str,
    },
    total=False,
)

LifeCycleLastTestRevertedTypeDef = TypedDict(
    "LifeCycleLastTestRevertedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastTestTypeDef = TypedDict(
    "LifeCycleLastTestTypeDef",
    {
        "finalized": "LifeCycleLastTestFinalizedTypeDef",
        "initiated": "LifeCycleLastTestInitiatedTypeDef",
        "reverted": "LifeCycleLastTestRevertedTypeDef",
    },
    total=False,
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": str,
        "elapsedReplicationDuration": str,
        "firstByteDateTime": str,
        "lastCutover": "LifeCycleLastCutoverTypeDef",
        "lastSeenByServiceDateTime": str,
        "lastTest": "LifeCycleLastTestTypeDef",
        "state": LifeCycleStateType,
    },
    total=False,
)

ListApplicationsRequestFiltersTypeDef = TypedDict(
    "ListApplicationsRequestFiltersTypeDef",
    {
        "applicationIDs": List[str],
        "isArchived": bool,
        "waveIDs": List[str],
    },
    total=False,
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "filters": "ListApplicationsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "items": List["ApplicationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExportErrorsRequestRequestTypeDef = TypedDict(
    "_RequiredListExportErrorsRequestRequestTypeDef",
    {
        "exportID": str,
    },
)
_OptionalListExportErrorsRequestRequestTypeDef = TypedDict(
    "_OptionalListExportErrorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListExportErrorsRequestRequestTypeDef(
    _RequiredListExportErrorsRequestRequestTypeDef, _OptionalListExportErrorsRequestRequestTypeDef
):
    pass

ListExportErrorsResponseTypeDef = TypedDict(
    "ListExportErrorsResponseTypeDef",
    {
        "items": List["ExportTaskErrorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsRequestFiltersTypeDef = TypedDict(
    "ListExportsRequestFiltersTypeDef",
    {
        "exportIDs": List[str],
    },
    total=False,
)

ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "filters": "ListExportsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "items": List["ExportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImportErrorsRequestRequestTypeDef = TypedDict(
    "_RequiredListImportErrorsRequestRequestTypeDef",
    {
        "importID": str,
    },
)
_OptionalListImportErrorsRequestRequestTypeDef = TypedDict(
    "_OptionalListImportErrorsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListImportErrorsRequestRequestTypeDef(
    _RequiredListImportErrorsRequestRequestTypeDef, _OptionalListImportErrorsRequestRequestTypeDef
):
    pass

ListImportErrorsResponseTypeDef = TypedDict(
    "ListImportErrorsResponseTypeDef",
    {
        "items": List["ImportTaskErrorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsRequestFiltersTypeDef = TypedDict(
    "ListImportsRequestFiltersTypeDef",
    {
        "importIDs": List[str],
    },
    total=False,
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "filters": "ListImportsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "items": List["ImportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSourceServerActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSourceServerActionsRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalListSourceServerActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSourceServerActionsRequestRequestTypeDef",
    {
        "filters": "SourceServerActionsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSourceServerActionsRequestRequestTypeDef(
    _RequiredListSourceServerActionsRequestRequestTypeDef,
    _OptionalListSourceServerActionsRequestRequestTypeDef,
):
    pass

ListSourceServerActionsResponseTypeDef = TypedDict(
    "ListSourceServerActionsResponseTypeDef",
    {
        "items": List["SourceServerActionDocumentTypeDef"],
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

_RequiredListTemplateActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateActionsRequestRequestTypeDef",
    {
        "launchConfigurationTemplateID": str,
    },
)
_OptionalListTemplateActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateActionsRequestRequestTypeDef",
    {
        "filters": "TemplateActionsRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTemplateActionsRequestRequestTypeDef(
    _RequiredListTemplateActionsRequestRequestTypeDef,
    _OptionalListTemplateActionsRequestRequestTypeDef,
):
    pass

ListTemplateActionsResponseTypeDef = TypedDict(
    "ListTemplateActionsResponseTypeDef",
    {
        "items": List["TemplateActionDocumentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWavesRequestFiltersTypeDef = TypedDict(
    "ListWavesRequestFiltersTypeDef",
    {
        "isArchived": bool,
        "waveIDs": List[str],
    },
    total=False,
)

ListWavesRequestRequestTypeDef = TypedDict(
    "ListWavesRequestRequestTypeDef",
    {
        "filters": "ListWavesRequestFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWavesResponseTypeDef = TypedDict(
    "ListWavesResponseTypeDef",
    {
        "items": List["WaveTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarkAsArchivedRequestRequestTypeDef = TypedDict(
    "MarkAsArchivedRequestRequestTypeDef",
    {
        "sourceServerID": str,
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredParticipatingServerTypeDef = TypedDict(
    "_RequiredParticipatingServerTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalParticipatingServerTypeDef = TypedDict(
    "_OptionalParticipatingServerTypeDef",
    {
        "launchStatus": LaunchStatusType,
        "launchedEc2InstanceID": str,
        "postLaunchActionsStatus": "PostLaunchActionsStatusTypeDef",
    },
    total=False,
)

class ParticipatingServerTypeDef(
    _RequiredParticipatingServerTypeDef, _OptionalParticipatingServerTypeDef
):
    pass

PostLaunchActionsStatusTypeDef = TypedDict(
    "PostLaunchActionsStatusTypeDef",
    {
        "postLaunchActionsLaunchStatusList": List["JobPostLaunchActionsLaunchStatusTypeDef"],
        "ssmAgentDiscoveryDatetime": str,
    },
    total=False,
)

PostLaunchActionsTypeDef = TypedDict(
    "PostLaunchActionsTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "deployment": PostLaunchActionsDeploymentTypeType,
        "s3LogBucket": str,
        "s3OutputKeyPrefix": str,
        "ssmDocuments": List["SsmDocumentTypeDef"],
    },
    total=False,
)

_RequiredPutSourceServerActionRequestRequestTypeDef = TypedDict(
    "_RequiredPutSourceServerActionRequestRequestTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "documentIdentifier": str,
        "order": int,
        "sourceServerID": str,
    },
)
_OptionalPutSourceServerActionRequestRequestTypeDef = TypedDict(
    "_OptionalPutSourceServerActionRequestRequestTypeDef",
    {
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
    },
    total=False,
)

class PutSourceServerActionRequestRequestTypeDef(
    _RequiredPutSourceServerActionRequestRequestTypeDef,
    _OptionalPutSourceServerActionRequestRequestTypeDef,
):
    pass

_RequiredPutTemplateActionRequestRequestTypeDef = TypedDict(
    "_RequiredPutTemplateActionRequestRequestTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "documentIdentifier": str,
        "launchConfigurationTemplateID": str,
        "order": int,
    },
)
_OptionalPutTemplateActionRequestRequestTypeDef = TypedDict(
    "_OptionalPutTemplateActionRequestRequestTypeDef",
    {
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "operatingSystem": str,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
    },
    total=False,
)

class PutTemplateActionRequestRequestTypeDef(
    _RequiredPutTemplateActionRequestRequestTypeDef, _OptionalPutTemplateActionRequestRequestTypeDef
):
    pass

RemoveSourceServerActionRequestRequestTypeDef = TypedDict(
    "RemoveSourceServerActionRequestRequestTypeDef",
    {
        "actionID": str,
        "sourceServerID": str,
    },
)

RemoveTemplateActionRequestRequestTypeDef = TypedDict(
    "RemoveTemplateActionRequestRequestTypeDef",
    {
        "actionID": str,
        "launchConfigurationTemplateID": str,
    },
)

ReplicationConfigurationReplicatedDiskTypeDef = TypedDict(
    "ReplicationConfigurationReplicatedDiskTypeDef",
    {
        "deviceName": str,
        "iops": int,
        "isBootDisk": bool,
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
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
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
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
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
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
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

_RequiredS3BucketSourceTypeDef = TypedDict(
    "_RequiredS3BucketSourceTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)
_OptionalS3BucketSourceTypeDef = TypedDict(
    "_OptionalS3BucketSourceTypeDef",
    {
        "s3BucketOwner": str,
    },
    total=False,
)

class S3BucketSourceTypeDef(_RequiredS3BucketSourceTypeDef, _OptionalS3BucketSourceTypeDef):
    pass

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
    },
    total=False,
)

SourceServerActionDocumentResponseMetadataTypeDef = TypedDict(
    "SourceServerActionDocumentResponseMetadataTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentIdentifier": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "order": int,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceServerActionDocumentTypeDef = TypedDict(
    "SourceServerActionDocumentTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentIdentifier": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "order": int,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
    },
    total=False,
)

SourceServerActionsRequestFiltersTypeDef = TypedDict(
    "SourceServerActionsRequestFiltersTypeDef",
    {
        "actionIDs": List[str],
    },
    total=False,
)

SourceServerResponseMetadataTypeDef = TypedDict(
    "SourceServerResponseMetadataTypeDef",
    {
        "applicationID": str,
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "fqdnForActionFramework": str,
        "isArchived": bool,
        "launchedInstance": "LaunchedInstanceTypeDef",
        "lifeCycle": "LifeCycleTypeDef",
        "replicationType": ReplicationTypeType,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
        "userProvidedID": str,
        "vcenterClientID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceServerTypeDef = TypedDict(
    "SourceServerTypeDef",
    {
        "applicationID": str,
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "fqdnForActionFramework": str,
        "isArchived": bool,
        "launchedInstance": "LaunchedInstanceTypeDef",
        "lifeCycle": "LifeCycleTypeDef",
        "replicationType": ReplicationTypeType,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
        "userProvidedID": str,
        "vcenterClientID": str,
    },
    total=False,
)

_RequiredSsmDocumentTypeDef = TypedDict(
    "_RequiredSsmDocumentTypeDef",
    {
        "actionName": str,
        "ssmDocumentName": str,
    },
)
_OptionalSsmDocumentTypeDef = TypedDict(
    "_OptionalSsmDocumentTypeDef",
    {
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
    },
    total=False,
)

class SsmDocumentTypeDef(_RequiredSsmDocumentTypeDef, _OptionalSsmDocumentTypeDef):
    pass

SsmExternalParameterTypeDef = TypedDict(
    "SsmExternalParameterTypeDef",
    {
        "dynamicPath": str,
    },
    total=False,
)

SsmParameterStoreParameterTypeDef = TypedDict(
    "SsmParameterStoreParameterTypeDef",
    {
        "parameterName": str,
        "parameterType": Literal["STRING"],
    },
)

_RequiredStartCutoverRequestRequestTypeDef = TypedDict(
    "_RequiredStartCutoverRequestRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalStartCutoverRequestRequestTypeDef = TypedDict(
    "_OptionalStartCutoverRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class StartCutoverRequestRequestTypeDef(
    _RequiredStartCutoverRequestRequestTypeDef, _OptionalStartCutoverRequestRequestTypeDef
):
    pass

StartCutoverResponseTypeDef = TypedDict(
    "StartCutoverResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartExportRequestRequestTypeDef = TypedDict(
    "_RequiredStartExportRequestRequestTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)
_OptionalStartExportRequestRequestTypeDef = TypedDict(
    "_OptionalStartExportRequestRequestTypeDef",
    {
        "s3BucketOwner": str,
    },
    total=False,
)

class StartExportRequestRequestTypeDef(
    _RequiredStartExportRequestRequestTypeDef, _OptionalStartExportRequestRequestTypeDef
):
    pass

StartExportResponseTypeDef = TypedDict(
    "StartExportResponseTypeDef",
    {
        "exportTask": "ExportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestRequestTypeDef",
    {
        "s3BucketSource": "S3BucketSourceTypeDef",
    },
)
_OptionalStartImportRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartImportRequestRequestTypeDef(
    _RequiredStartImportRequestRequestTypeDef, _OptionalStartImportRequestRequestTypeDef
):
    pass

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "importTask": "ImportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationRequestRequestTypeDef = TypedDict(
    "StartReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

_RequiredStartTestRequestRequestTypeDef = TypedDict(
    "_RequiredStartTestRequestRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalStartTestRequestRequestTypeDef = TypedDict(
    "_OptionalStartTestRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class StartTestRequestRequestTypeDef(
    _RequiredStartTestRequestRequestTypeDef, _OptionalStartTestRequestRequestTypeDef
):
    pass

StartTestResponseTypeDef = TypedDict(
    "StartTestResponseTypeDef",
    {
        "job": "JobTypeDef",
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

TemplateActionDocumentResponseMetadataTypeDef = TypedDict(
    "TemplateActionDocumentResponseMetadataTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentIdentifier": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "operatingSystem": str,
        "order": int,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TemplateActionDocumentTypeDef = TypedDict(
    "TemplateActionDocumentTypeDef",
    {
        "actionID": str,
        "actionName": str,
        "active": bool,
        "category": ActionCategoryType,
        "description": str,
        "documentIdentifier": str,
        "documentVersion": str,
        "externalParameters": Dict[str, "SsmExternalParameterTypeDef"],
        "mustSucceedForCutover": bool,
        "operatingSystem": str,
        "order": int,
        "parameters": Dict[str, List["SsmParameterStoreParameterTypeDef"]],
        "timeoutSeconds": int,
    },
    total=False,
)

TemplateActionsRequestFiltersTypeDef = TypedDict(
    "TemplateActionsRequestFiltersTypeDef",
    {
        "actionIDs": List[str],
    },
    total=False,
)

_RequiredTerminateTargetInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredTerminateTargetInstancesRequestRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalTerminateTargetInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalTerminateTargetInstancesRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TerminateTargetInstancesRequestRequestTypeDef(
    _RequiredTerminateTargetInstancesRequestRequestTypeDef,
    _OptionalTerminateTargetInstancesRequestRequestTypeDef,
):
    pass

TerminateTargetInstancesResponseTypeDef = TypedDict(
    "TerminateTargetInstancesResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnarchiveApplicationRequestRequestTypeDef = TypedDict(
    "UnarchiveApplicationRequestRequestTypeDef",
    {
        "applicationID": str,
    },
)

UnarchiveWaveRequestRequestTypeDef = TypedDict(
    "UnarchiveWaveRequestRequestTypeDef",
    {
        "waveID": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "applicationID": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
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
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "enableMapAutoTagging": bool,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "name": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
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
        "associatePublicIpAddress": bool,
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "enableMapAutoTagging": bool,
        "largeVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "mapAutoTaggingMpeID": str,
        "postLaunchActions": "PostLaunchActionsTypeDef",
        "smallVolumeConf": "LaunchTemplateDiskConfTypeDef",
        "smallVolumeMaxSize": int,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)

class UpdateLaunchConfigurationTemplateRequestRequestTypeDef(
    _RequiredUpdateLaunchConfigurationTemplateRequestRequestTypeDef,
    _OptionalUpdateLaunchConfigurationTemplateRequestRequestTypeDef,
):
    pass

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
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
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
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
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

UpdateSourceServerReplicationTypeRequestRequestTypeDef = TypedDict(
    "UpdateSourceServerReplicationTypeRequestRequestTypeDef",
    {
        "replicationType": ReplicationTypeType,
        "sourceServerID": str,
    },
)

_RequiredUpdateWaveRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWaveRequestRequestTypeDef",
    {
        "waveID": str,
    },
)
_OptionalUpdateWaveRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWaveRequestRequestTypeDef",
    {
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateWaveRequestRequestTypeDef(
    _RequiredUpdateWaveRequestRequestTypeDef, _OptionalUpdateWaveRequestRequestTypeDef
):
    pass

VcenterClientTypeDef = TypedDict(
    "VcenterClientTypeDef",
    {
        "arn": str,
        "datacenterName": str,
        "hostname": str,
        "lastSeenDatetime": str,
        "sourceServerTags": Dict[str, str],
        "tags": Dict[str, str],
        "vcenterClientID": str,
        "vcenterUUID": str,
    },
    total=False,
)

WaveAggregatedStatusTypeDef = TypedDict(
    "WaveAggregatedStatusTypeDef",
    {
        "healthStatus": WaveHealthStatusType,
        "lastUpdateDateTime": str,
        "progressStatus": WaveProgressStatusType,
        "replicationStartedDateTime": str,
        "totalApplications": int,
    },
    total=False,
)

WaveResponseMetadataTypeDef = TypedDict(
    "WaveResponseMetadataTypeDef",
    {
        "arn": str,
        "creationDateTime": str,
        "description": str,
        "isArchived": bool,
        "lastModifiedDateTime": str,
        "name": str,
        "tags": Dict[str, str],
        "waveAggregatedStatus": "WaveAggregatedStatusTypeDef",
        "waveID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaveTypeDef = TypedDict(
    "WaveTypeDef",
    {
        "arn": str,
        "creationDateTime": str,
        "description": str,
        "isArchived": bool,
        "lastModifiedDateTime": str,
        "name": str,
        "tags": Dict[str, str],
        "waveAggregatedStatus": "WaveAggregatedStatusTypeDef",
        "waveID": str,
    },
    total=False,
)
