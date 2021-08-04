"""
Type annotations for opsworkscm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/literals.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.literals import BackupStatusType

    data: BackupStatusType = "DELETING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BackupStatusType",
    "BackupTypeType",
    "DescribeBackupsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeServersPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MaintenanceStatusType",
    "NodeAssociatedWaiterName",
    "NodeAssociationStatusType",
    "ServerStatusType",
)

BackupStatusType = Literal["DELETING", "FAILED", "IN_PROGRESS", "OK"]
BackupTypeType = Literal["AUTOMATED", "MANUAL"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeServersPaginatorName = Literal["describe_servers"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MaintenanceStatusType = Literal["FAILED", "SUCCESS"]
NodeAssociatedWaiterName = Literal["node_associated"]
NodeAssociationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ServerStatusType = Literal[
    "BACKING_UP",
    "CONNECTION_LOST",
    "CREATING",
    "DELETING",
    "FAILED",
    "HEALTHY",
    "MODIFYING",
    "RESTORING",
    "RUNNING",
    "SETUP",
    "TERMINATED",
    "UNDER_MAINTENANCE",
    "UNHEALTHY",
]
