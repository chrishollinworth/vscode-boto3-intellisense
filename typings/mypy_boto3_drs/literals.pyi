"""
Type annotations for drs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/literals.html)

Usage::

    ```python
    from mypy_boto3_drs.literals import DataReplicationErrorStringType

    data: DataReplicationErrorStringType = "AGENT_NOT_SEEN"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DataReplicationErrorStringType",
    "DataReplicationInitiationStepNameType",
    "DataReplicationInitiationStepStatusType",
    "DataReplicationStateType",
    "DescribeJobLogItemsPaginatorName",
    "DescribeJobsPaginatorName",
    "DescribeRecoveryInstancesPaginatorName",
    "DescribeRecoverySnapshotsPaginatorName",
    "DescribeReplicationConfigurationTemplatesPaginatorName",
    "DescribeSourceServersPaginatorName",
    "EC2InstanceStateType",
    "ExtensionStatusType",
    "FailbackLaunchTypeType",
    "FailbackReplicationErrorType",
    "FailbackStateType",
    "InitiatedByType",
    "JobLogEventType",
    "JobStatusType",
    "JobTypeType",
    "LastLaunchResultType",
    "LastLaunchTypeType",
    "LaunchDispositionType",
    "LaunchStatusType",
    "ListExtensibleSourceServersPaginatorName",
    "ListStagingAccountsPaginatorName",
    "OriginEnvironmentType",
    "PITPolicyRuleUnitsType",
    "RecoveryInstanceDataReplicationInitiationStepNameType",
    "RecoveryInstanceDataReplicationInitiationStepStatusType",
    "RecoveryInstanceDataReplicationStateType",
    "RecoverySnapshotsOrderType",
    "ReplicationConfigurationDataPlaneRoutingType",
    "ReplicationConfigurationDefaultLargeStagingDiskTypeType",
    "ReplicationConfigurationEbsEncryptionType",
    "ReplicationConfigurationReplicatedDiskStagingDiskTypeType",
    "ReplicationDirectionType",
    "TargetInstanceTypeRightSizingMethodType",
)

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
    "NOT_CONVERGING",
    "SNAPSHOTS_FAILURE",
    "UNSTABLE_NETWORK",
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
    "RESCAN",
    "STALLED",
    "STOPPED",
]
DescribeJobLogItemsPaginatorName = Literal["describe_job_log_items"]
DescribeJobsPaginatorName = Literal["describe_jobs"]
DescribeRecoveryInstancesPaginatorName = Literal["describe_recovery_instances"]
DescribeRecoverySnapshotsPaginatorName = Literal["describe_recovery_snapshots"]
DescribeReplicationConfigurationTemplatesPaginatorName = Literal[
    "describe_replication_configuration_templates"
]
DescribeSourceServersPaginatorName = Literal["describe_source_servers"]
EC2InstanceStateType = Literal[
    "NOT_FOUND", "PENDING", "RUNNING", "SHUTTING-DOWN", "STOPPED", "STOPPING", "TERMINATED"
]
ExtensionStatusType = Literal["EXTENDED", "EXTENSION_ERROR", "NOT_EXTENDED"]
FailbackLaunchTypeType = Literal["DRILL", "RECOVERY"]
FailbackReplicationErrorType = Literal[
    "AGENT_NOT_SEEN",
    "FAILBACK_CLIENT_NOT_SEEN",
    "FAILED_GETTING_REPLICATION_STATE",
    "FAILED_TO_ATTACH_STAGING_DISKS",
    "FAILED_TO_AUTHENTICATE_WITH_SERVICE",
    "FAILED_TO_BOOT_REPLICATION_SERVER",
    "FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE",
    "FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER",
    "FAILED_TO_CREATE_SECURITY_GROUP",
    "FAILED_TO_CREATE_STAGING_DISKS",
    "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE",
    "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT",
    "FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION",
    "FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION",
    "FAILED_TO_LAUNCH_REPLICATION_SERVER",
    "FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE",
    "FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT",
    "FAILED_TO_START_DATA_TRANSFER",
    "NOT_CONVERGING",
    "SNAPSHOTS_FAILURE",
    "UNSTABLE_NETWORK",
]
FailbackStateType = Literal[
    "FAILBACK_COMPLETED",
    "FAILBACK_ERROR",
    "FAILBACK_IN_PROGRESS",
    "FAILBACK_LAUNCH_STATE_NOT_AVAILABLE",
    "FAILBACK_NOT_READY_FOR_LAUNCH",
    "FAILBACK_NOT_STARTED",
    "FAILBACK_READY_FOR_LAUNCH",
]
InitiatedByType = Literal[
    "DIAGNOSTIC",
    "FAILBACK",
    "START_DRILL",
    "START_RECOVERY",
    "TARGET_ACCOUNT",
    "TERMINATE_RECOVERY_INSTANCES",
]
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
    "USING_PREVIOUS_SNAPSHOT_FAILED",
]
JobStatusType = Literal["COMPLETED", "PENDING", "STARTED"]
JobTypeType = Literal["CREATE_CONVERTED_SNAPSHOT", "LAUNCH", "TERMINATE"]
LastLaunchResultType = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCEEDED"]
LastLaunchTypeType = Literal["DRILL", "RECOVERY"]
LaunchDispositionType = Literal["STARTED", "STOPPED"]
LaunchStatusType = Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
ListExtensibleSourceServersPaginatorName = Literal["list_extensible_source_servers"]
ListStagingAccountsPaginatorName = Literal["list_staging_accounts"]
OriginEnvironmentType = Literal["AWS", "ON_PREMISES"]
PITPolicyRuleUnitsType = Literal["DAY", "HOUR", "MINUTE"]
RecoveryInstanceDataReplicationInitiationStepNameType = Literal[
    "ATTACH_STAGING_DISKS",
    "AUTHENTICATE_WITH_SERVICE",
    "BOOT_REPLICATION_SERVER",
    "COMPLETE_VOLUME_MAPPING",
    "CONFIGURE_REPLICATION_SOFTWARE",
    "CONNECT_AGENT_TO_REPLICATION_SERVER",
    "CREATE_SECURITY_GROUP",
    "CREATE_STAGING_DISKS",
    "DOWNLOAD_REPLICATION_SOFTWARE",
    "DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT",
    "ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION",
    "ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION",
    "LAUNCH_REPLICATION_SERVER",
    "LINK_FAILBACK_CLIENT_WITH_RECOVERY_INSTANCE",
    "PAIR_AGENT_WITH_REPLICATION_SOFTWARE",
    "PAIR_REPLICATION_SERVER_WITH_AGENT",
    "START_DATA_TRANSFER",
    "WAIT",
]
RecoveryInstanceDataReplicationInitiationStepStatusType = Literal[
    "FAILED", "IN_PROGRESS", "NOT_STARTED", "SKIPPED", "SUCCEEDED"
]
RecoveryInstanceDataReplicationStateType = Literal[
    "BACKLOG",
    "CONTINUOUS",
    "CREATING_SNAPSHOT",
    "DISCONNECTED",
    "INITIAL_SYNC",
    "INITIATING",
    "NOT_STARTED",
    "PAUSED",
    "REPLICATION_STATE_NOT_AVAILABLE",
    "RESCAN",
    "STALLED",
    "STOPPED",
]
RecoverySnapshotsOrderType = Literal["ASC", "DESC"]
ReplicationConfigurationDataPlaneRoutingType = Literal["PRIVATE_IP", "PUBLIC_IP"]
ReplicationConfigurationDefaultLargeStagingDiskTypeType = Literal["AUTO", "GP2", "GP3", "ST1"]
ReplicationConfigurationEbsEncryptionType = Literal["CUSTOM", "DEFAULT"]
ReplicationConfigurationReplicatedDiskStagingDiskTypeType = Literal[
    "AUTO", "GP2", "GP3", "IO1", "SC1", "ST1", "STANDARD"
]
ReplicationDirectionType = Literal["FAILBACK", "FAILOVER"]
TargetInstanceTypeRightSizingMethodType = Literal["BASIC", "NONE"]
