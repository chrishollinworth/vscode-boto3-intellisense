"""
Type annotations for efs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/literals.html)

Usage::

    ```python
    from mypy_boto3_efs.literals import DescribeFileSystemsPaginatorName

    data: DescribeFileSystemsPaginatorName = "describe_file_systems"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeFileSystemsPaginatorName",
    "DescribeMountTargetsPaginatorName",
    "DescribeTagsPaginatorName",
    "LifeCycleStateType",
    "PerformanceModeType",
    "ResourceIdTypeType",
    "ResourceType",
    "StatusType",
    "ThroughputModeType",
    "TransitionToIARulesType",
)

DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DescribeMountTargetsPaginatorName = Literal["describe_mount_targets"]
DescribeTagsPaginatorName = Literal["describe_tags"]
LifeCycleStateType = Literal["available", "creating", "deleted", "deleting", "error", "updating"]
PerformanceModeType = Literal["generalPurpose", "maxIO"]
ResourceIdTypeType = Literal["LONG_ID", "SHORT_ID"]
ResourceType = Literal["FILE_SYSTEM", "MOUNT_TARGET"]
StatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
ThroughputModeType = Literal["bursting", "provisioned"]
TransitionToIARulesType = Literal[
    "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_7_DAYS", "AFTER_90_DAYS"
]
