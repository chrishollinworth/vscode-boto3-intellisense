"""
Type annotations for efs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/literals.html)

Usage::

    ```python
    from mypy_boto3_efs.literals import DescribeAccessPointsPaginatorName

    data: DescribeAccessPointsPaginatorName = "describe_access_points"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeAccessPointsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DescribeMountTargetsPaginatorName",
    "DescribeReplicationConfigurationsPaginatorName",
    "DescribeTagsPaginatorName",
    "LifeCycleStateType",
    "PerformanceModeType",
    "ReplicationOverwriteProtectionType",
    "ReplicationStatusType",
    "ResourceIdTypeType",
    "ResourceType",
    "StatusType",
    "ThroughputModeType",
    "TransitionToArchiveRulesType",
    "TransitionToIARulesType",
    "TransitionToPrimaryStorageClassRulesType",
)

DescribeAccessPointsPaginatorName = Literal["describe_access_points"]
DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DescribeMountTargetsPaginatorName = Literal["describe_mount_targets"]
DescribeReplicationConfigurationsPaginatorName = Literal["describe_replication_configurations"]
DescribeTagsPaginatorName = Literal["describe_tags"]
LifeCycleStateType = Literal["available", "creating", "deleted", "deleting", "error", "updating"]
PerformanceModeType = Literal["generalPurpose", "maxIO"]
ReplicationOverwriteProtectionType = Literal["DISABLED", "ENABLED", "REPLICATING"]
ReplicationStatusType = Literal["DELETING", "ENABLED", "ENABLING", "ERROR", "PAUSED", "PAUSING"]
ResourceIdTypeType = Literal["LONG_ID", "SHORT_ID"]
ResourceType = Literal["FILE_SYSTEM", "MOUNT_TARGET"]
StatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
ThroughputModeType = Literal["bursting", "elastic", "provisioned"]
TransitionToArchiveRulesType = Literal[
    "AFTER_14_DAYS",
    "AFTER_180_DAYS",
    "AFTER_1_DAY",
    "AFTER_270_DAYS",
    "AFTER_30_DAYS",
    "AFTER_365_DAYS",
    "AFTER_60_DAYS",
    "AFTER_7_DAYS",
    "AFTER_90_DAYS",
]
TransitionToIARulesType = Literal[
    "AFTER_14_DAYS",
    "AFTER_180_DAYS",
    "AFTER_1_DAY",
    "AFTER_270_DAYS",
    "AFTER_30_DAYS",
    "AFTER_365_DAYS",
    "AFTER_60_DAYS",
    "AFTER_7_DAYS",
    "AFTER_90_DAYS",
]
TransitionToPrimaryStorageClassRulesType = Literal["AFTER_1_ACCESS"]
