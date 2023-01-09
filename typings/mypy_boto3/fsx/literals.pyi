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
    "DeleteFileSystemOpenZFSOptionType",
    "DeleteOpenZFSVolumeOptionType",
    "DescribeBackupsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DescribeStorageVirtualMachinesPaginatorName",
    "DescribeVolumesPaginatorName",
    "DiskIopsConfigurationModeType",
    "DriveCacheTypeType",
    "EventTypeType",
    "FileCacheLifecycleType",
    "FileCacheLustreDeploymentTypeType",
    "FileCacheTypeType",
    "FileSystemLifecycleType",
    "FileSystemMaintenanceOperationType",
    "FileSystemTypeType",
    "FilterNameType",
    "FlexCacheEndpointTypeType",
    "InputOntapVolumeTypeType",
    "ListTagsForResourcePaginatorName",
    "LustreAccessAuditLogLevelType",
    "LustreDeploymentTypeType",
    "NfsVersionType",
    "OntapDeploymentTypeType",
    "OntapVolumeTypeType",
    "OpenZFSCopyStrategyType",
    "OpenZFSDataCompressionTypeType",
    "OpenZFSDeploymentTypeType",
    "OpenZFSQuotaTypeType",
    "ReportFormatType",
    "ReportScopeType",
    "ResourceTypeType",
    "RestoreOpenZFSVolumeOptionType",
    "SecurityStyleType",
    "SnapshotFilterNameType",
    "SnapshotLifecycleType",
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
    "RELEASE_NFS_V3_LOCKS",
    "SNAPSHOT_UPDATE",
    "STORAGE_OPTIMIZATION",
    "VOLUME_RESTORE",
    "VOLUME_UPDATE",
]
AliasLifecycleType = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyTypeType = Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
BackupLifecycleType = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETED", "FAILED", "PENDING", "TRANSFERRING"
]
BackupTypeType = Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"]
DataCompressionTypeType = Literal["LZ4", "NONE"]
DataRepositoryLifecycleType = Literal[
    "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
]
DataRepositoryTaskFilterNameType = Literal[
    "data-repository-association-id", "file-cache-id", "file-system-id", "task-lifecycle"
]
DataRepositoryTaskLifecycleType = Literal[
    "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
]
DataRepositoryTaskTypeType = Literal[
    "AUTO_RELEASE_DATA",
    "EXPORT_TO_REPOSITORY",
    "IMPORT_METADATA_FROM_REPOSITORY",
    "RELEASE_DATA_FROM_FILESYSTEM",
]
DeleteFileSystemOpenZFSOptionType = Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]
DeleteOpenZFSVolumeOptionType = Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DescribeStorageVirtualMachinesPaginatorName = Literal["describe_storage_virtual_machines"]
DescribeVolumesPaginatorName = Literal["describe_volumes"]
DiskIopsConfigurationModeType = Literal["AUTOMATIC", "USER_PROVISIONED"]
DriveCacheTypeType = Literal["NONE", "READ"]
EventTypeType = Literal["CHANGED", "DELETED", "NEW"]
FileCacheLifecycleType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "UPDATING"]
FileCacheLustreDeploymentTypeType = Literal["CACHE_1"]
FileCacheTypeType = Literal["LUSTRE"]
FileSystemLifecycleType = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "MISCONFIGURED_UNAVAILABLE",
    "UPDATING",
]
FileSystemMaintenanceOperationType = Literal["BACKING_UP", "PATCHING"]
FileSystemTypeType = Literal["LUSTRE", "ONTAP", "OPENZFS", "WINDOWS"]
FilterNameType = Literal[
    "backup-type",
    "data-repository-type",
    "file-cache-id",
    "file-cache-type",
    "file-system-id",
    "file-system-type",
    "volume-id",
]
FlexCacheEndpointTypeType = Literal["CACHE", "NONE", "ORIGIN"]
InputOntapVolumeTypeType = Literal["DP", "RW"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LustreAccessAuditLogLevelType = Literal["DISABLED", "ERROR_ONLY", "WARN_ERROR", "WARN_ONLY"]
LustreDeploymentTypeType = Literal["PERSISTENT_1", "PERSISTENT_2", "SCRATCH_1", "SCRATCH_2"]
NfsVersionType = Literal["NFS3"]
OntapDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1"]
OntapVolumeTypeType = Literal["DP", "LS", "RW"]
OpenZFSCopyStrategyType = Literal["CLONE", "FULL_COPY"]
OpenZFSDataCompressionTypeType = Literal["LZ4", "NONE", "ZSTD"]
OpenZFSDeploymentTypeType = Literal["SINGLE_AZ_1", "SINGLE_AZ_2"]
OpenZFSQuotaTypeType = Literal["GROUP", "USER"]
ReportFormatType = Literal["REPORT_CSV_20191124"]
ReportScopeType = Literal["FAILED_FILES_ONLY"]
ResourceTypeType = Literal["FILE_SYSTEM", "VOLUME"]
RestoreOpenZFSVolumeOptionType = Literal["DELETE_CLONED_VOLUMES", "DELETE_INTERMEDIATE_SNAPSHOTS"]
SecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
SnapshotFilterNameType = Literal["file-system-id", "volume-id"]
SnapshotLifecycleType = Literal["AVAILABLE", "CREATING", "DELETING", "PENDING"]
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
    "AVAILABLE", "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
VolumeTypeType = Literal["ONTAP", "OPENZFS"]
WindowsAccessAuditLogLevelType = Literal[
    "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
]
WindowsDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
