"""
Type annotations for fsx service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/literals.html)

Usage::

    ```python
    from mypy_boto3_fsx.literals import AdministrativeActionTypeType

    data: AdministrativeActionTypeType = "FILE_SYSTEM_ALIAS_ASSOCIATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdministrativeActionTypeType",
    "AliasLifecycleType",
    "AutoImportPolicyTypeType",
    "BackupLifecycleType",
    "BackupTypeType",
    "DataCompressionTypeType",
    "DataRepositoryLifecycleType",
    "DataRepositoryTaskFilterNameType",
    "DataRepositoryTaskLifecycleType",
    "DataRepositoryTaskTypeType",
    "DescribeBackupsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DiskIopsConfigurationModeType",
    "DriveCacheTypeType",
    "FileSystemLifecycleType",
    "FileSystemMaintenanceOperationType",
    "FileSystemTypeType",
    "FilterNameType",
    "FlexCacheEndpointTypeType",
    "ListTagsForResourcePaginatorName",
    "LustreDeploymentTypeType",
    "OntapDeploymentTypeType",
    "OntapVolumeTypeType",
    "ReportFormatType",
    "ReportScopeType",
    "ResourceTypeType",
    "SecurityStyleType",
    "StatusType",
    "StorageTypeType",
    "StorageVirtualMachineFilterNameType",
    "StorageVirtualMachineLifecycleType",
    "StorageVirtualMachineRootVolumeSecurityStyleType",
    "StorageVirtualMachineSubtypeType",
    "TieringPolicyNameType",
    "VolumeFilterNameType",
    "VolumeLifecycleType",
    "VolumeTypeType",
    "WindowsAccessAuditLogLevelType",
    "WindowsDeploymentTypeType",
)

AdministrativeActionTypeType = Literal[
    "FILE_SYSTEM_ALIAS_ASSOCIATION",
    "FILE_SYSTEM_ALIAS_DISASSOCIATION",
    "FILE_SYSTEM_UPDATE",
    "STORAGE_OPTIMIZATION",
]
AliasLifecycleType = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyTypeType = Literal["NEW", "NEW_CHANGED", "NONE"]
BackupLifecycleType = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETED", "FAILED", "PENDING", "TRANSFERRING"
]
BackupTypeType = Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"]
DataCompressionTypeType = Literal["LZ4", "NONE"]
DataRepositoryLifecycleType = Literal[
    "AVAILABLE", "CREATING", "DELETING", "MISCONFIGURED", "UPDATING"
]
DataRepositoryTaskFilterNameType = Literal["file-system-id", "task-lifecycle"]
DataRepositoryTaskLifecycleType = Literal[
    "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
]
DataRepositoryTaskTypeType = Literal["EXPORT_TO_REPOSITORY"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DiskIopsConfigurationModeType = Literal["AUTOMATIC", "USER_PROVISIONED"]
DriveCacheTypeType = Literal["NONE", "READ"]
FileSystemLifecycleType = Literal[
    "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
]
FileSystemMaintenanceOperationType = Literal["BACKING_UP", "PATCHING"]
FileSystemTypeType = Literal["LUSTRE", "ONTAP", "WINDOWS"]
FilterNameType = Literal["backup-type", "file-system-id", "file-system-type", "volume-id"]
FlexCacheEndpointTypeType = Literal["CACHE", "NONE", "ORIGIN"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LustreDeploymentTypeType = Literal["PERSISTENT_1", "SCRATCH_1", "SCRATCH_2"]
OntapDeploymentTypeType = Literal["MULTI_AZ_1"]
OntapVolumeTypeType = Literal["DP", "LS", "RW"]
ReportFormatType = Literal["REPORT_CSV_20191124"]
ReportScopeType = Literal["FAILED_FILES_ONLY"]
ResourceTypeType = Literal["FILE_SYSTEM", "VOLUME"]
SecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
StatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "UPDATED_OPTIMIZING"]
StorageTypeType = Literal["HDD", "SSD"]
StorageVirtualMachineFilterNameType = Literal["file-system-id"]
StorageVirtualMachineLifecycleType = Literal[
    "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
StorageVirtualMachineRootVolumeSecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
StorageVirtualMachineSubtypeType = Literal[
    "DEFAULT", "DP_DESTINATION", "SYNC_DESTINATION", "SYNC_SOURCE"
]
TieringPolicyNameType = Literal["ALL", "AUTO", "NONE", "SNAPSHOT_ONLY"]
VolumeFilterNameType = Literal["file-system-id", "storage-virtual-machine-id"]
VolumeLifecycleType = Literal[
    "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
VolumeTypeType = Literal["ONTAP"]
WindowsAccessAuditLogLevelType = Literal[
    "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
]
WindowsDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
