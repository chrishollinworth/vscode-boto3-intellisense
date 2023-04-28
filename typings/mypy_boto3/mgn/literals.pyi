"""
Type annotations for mgn service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/literals.html)

Usage::

    ```python
    from mypy_boto3_mgn.literals import ActionCategoryType

    data: ActionCategoryType = "BACKUP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionCategoryType",
    "ApplicationHealthStatusType",
    "ApplicationProgressStatusType",
    "BootModeType",
    "ChangeServerLifeCycleStateSourceServerLifecycleStateType",
    "DataReplicationErrorStringType",
    "DataReplicationInitiationStepNameType",
    "DataReplicationInitiationStepStatusType",
    "DataReplicationStateType",
    "DescribeJobLogItemsPaginatorName",
    "DescribeJobsPaginatorName",
    "DescribeLaunchConfigurationTemplatesPaginatorName",
    "DescribeReplicationConfigurationTemplatesPaginatorName",
    "DescribeSourceServersPaginatorName",
    "DescribeVcenterClientsPaginatorName",
    "ExportStatusType",
    "FirstBootType",
    "ImportErrorTypeType",
    "ImportStatusType",
    "InitiatedByType",
    "JobLogEventType",
    "JobStatusType",
    "JobTypeType",
    "LaunchDispositionType",
    "LaunchStatusType",
    "LifeCycleStateType",
    "ListApplicationsPaginatorName",
    "ListExportErrorsPaginatorName",
    "ListExportsPaginatorName",
    "ListImportErrorsPaginatorName",
    "ListImportsPaginatorName",
    "ListSourceServerActionsPaginatorName",
    "ListTemplateActionsPaginatorName",
    "ListWavesPaginatorName",
    "PostLaunchActionExecutionStatusType",
    "PostLaunchActionsDeploymentTypeType",
    "ReplicationConfigurationDataPlaneRoutingType",
    "ReplicationConfigurationDefaultLargeStagingDiskTypeType",
    "ReplicationConfigurationEbsEncryptionType",
    "ReplicationConfigurationReplicatedDiskStagingDiskTypeType",
    "ReplicationTypeType",
    "SsmDocumentTypeType",
    "SsmParameterStoreParameterTypeType",
    "TargetInstanceTypeRightSizingMethodType",
    "VolumeTypeType",
    "WaveHealthStatusType",
    "WaveProgressStatusType",
)

ActionCategoryType = Literal[
    "BACKUP",
    "CONFIGURATION",
    "DISASTER_RECOVERY",
    "LICENSE_AND_SUBSCRIPTION",
    "NETWORKING",
    "OBSERVABILITY",
    "OPERATING_SYSTEM",
    "OTHER",
    "SECURITY",
    "VALIDATION",
]
ApplicationHealthStatusType = Literal["ERROR", "HEALTHY", "LAGGING"]
ApplicationProgressStatusType = Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
BootModeType = Literal["LEGACY_BIOS", "UEFI"]
ChangeServerLifeCycleStateSourceServerLifecycleStateType = Literal[
    "CUTOVER", "READY_FOR_CUTOVER", "READY_FOR_TEST"
]
DataReplicationErrorStringType = Literal[
    "AGENT_NOT_SEEN",
    "FAILED_TO_ATTACH_STAGING_DISKS",
    "FAILED_TO_AUTHENTICATE_WITH_SERVICE",
    "FAILED_TO_BOOT_REPLICATION_SERVER",
    "FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER",
    "FAILED_TO_CREATE_SECURITY_GROUP",
    "FAILED_TO_CREATE_STAGING_DISKS",
    "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE",
    "FAILED_TO_LAUNCH_REPLICATION_SERVER",
    "FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT",
    "FAILED_TO_START_DATA_TRANSFER",
    "LAST_SNAPSHOT_JOB_FAILED",
    "NOT_CONVERGING",
    "SNAPSHOTS_FAILURE",
    "UNSTABLE_NETWORK",
    "UNSUPPORTED_VM_CONFIGURATION",
]
DataReplicationInitiationStepNameType = Literal[
    "ATTACH_STAGING_DISKS",
    "AUTHENTICATE_WITH_SERVICE",
    "BOOT_REPLICATION_SERVER",
    "CONNECT_AGENT_TO_REPLICATION_SERVER",
    "CREATE_SECURITY_GROUP",
    "CREATE_STAGING_DISKS",
    "DOWNLOAD_REPLICATION_SOFTWARE",
    "LAUNCH_REPLICATION_SERVER",
    "PAIR_REPLICATION_SERVER_WITH_AGENT",
    "START_DATA_TRANSFER",
    "WAIT",
]
DataReplicationInitiationStepStatusType = Literal[
    "FAILED", "IN_PROGRESS", "NOT_STARTED", "SKIPPED", "SUCCEEDED"
]
DataReplicationStateType = Literal[
    "BACKLOG",
    "CONTINUOUS",
    "CREATING_SNAPSHOT",
    "DISCONNECTED",
    "INITIAL_SYNC",
    "INITIATING",
    "PAUSED",
    "PENDING_SNAPSHOT_SHIPPING",
    "RESCAN",
    "SHIPPING_SNAPSHOT",
    "STALLED",
    "STOPPED",
]
DescribeJobLogItemsPaginatorName = Literal["describe_job_log_items"]
DescribeJobsPaginatorName = Literal["describe_jobs"]
DescribeLaunchConfigurationTemplatesPaginatorName = Literal[
    "describe_launch_configuration_templates"
]
DescribeReplicationConfigurationTemplatesPaginatorName = Literal[
    "describe_replication_configuration_templates"
]
DescribeSourceServersPaginatorName = Literal["describe_source_servers"]
DescribeVcenterClientsPaginatorName = Literal["describe_vcenter_clients"]
ExportStatusType = Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]
FirstBootType = Literal["STOPPED", "SUCCEEDED", "UNKNOWN", "WAITING"]
ImportErrorTypeType = Literal["PROCESSING_ERROR", "VALIDATION_ERROR"]
ImportStatusType = Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]
InitiatedByType = Literal["DIAGNOSTIC", "START_CUTOVER", "START_TEST", "TERMINATE"]
JobLogEventType = Literal[
    "CLEANUP_END",
    "CLEANUP_FAIL",
    "CLEANUP_START",
    "CONVERSION_END",
    "CONVERSION_FAIL",
    "CONVERSION_START",
    "JOB_CANCEL",
    "JOB_END",
    "JOB_START",
    "LAUNCH_FAILED",
    "LAUNCH_START",
    "SERVER_SKIPPED",
    "SNAPSHOT_END",
    "SNAPSHOT_FAIL",
    "SNAPSHOT_START",
    "USING_PREVIOUS_SNAPSHOT",
]
JobStatusType = Literal["COMPLETED", "PENDING", "STARTED"]
JobTypeType = Literal["LAUNCH", "TERMINATE"]
LaunchDispositionType = Literal["STARTED", "STOPPED"]
LaunchStatusType = Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
LifeCycleStateType = Literal[
    "CUTOVER",
    "CUTTING_OVER",
    "DISCONNECTED",
    "DISCOVERED",
    "NOT_READY",
    "PENDING_INSTALLATION",
    "READY_FOR_CUTOVER",
    "READY_FOR_TEST",
    "STOPPED",
    "TESTING",
]
ListApplicationsPaginatorName = Literal["list_applications"]
ListExportErrorsPaginatorName = Literal["list_export_errors"]
ListExportsPaginatorName = Literal["list_exports"]
ListImportErrorsPaginatorName = Literal["list_import_errors"]
ListImportsPaginatorName = Literal["list_imports"]
ListSourceServerActionsPaginatorName = Literal["list_source_server_actions"]
ListTemplateActionsPaginatorName = Literal["list_template_actions"]
ListWavesPaginatorName = Literal["list_waves"]
PostLaunchActionExecutionStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
PostLaunchActionsDeploymentTypeType = Literal["CUTOVER_ONLY", "TEST_AND_CUTOVER", "TEST_ONLY"]
ReplicationConfigurationDataPlaneRoutingType = Literal["PRIVATE_IP", "PUBLIC_IP"]
ReplicationConfigurationDefaultLargeStagingDiskTypeType = Literal["GP2", "GP3", "ST1"]
ReplicationConfigurationEbsEncryptionType = Literal["CUSTOM", "DEFAULT"]
ReplicationConfigurationReplicatedDiskStagingDiskTypeType = Literal[
    "AUTO", "GP2", "GP3", "IO1", "IO2", "SC1", "ST1", "STANDARD"
]
ReplicationTypeType = Literal["AGENT_BASED", "SNAPSHOT_SHIPPING"]
SsmDocumentTypeType = Literal["AUTOMATION", "COMMAND"]
SsmParameterStoreParameterTypeType = Literal["STRING"]
TargetInstanceTypeRightSizingMethodType = Literal["BASIC", "NONE"]
VolumeTypeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
WaveHealthStatusType = Literal["ERROR", "HEALTHY", "LAGGING"]
WaveProgressStatusType = Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
