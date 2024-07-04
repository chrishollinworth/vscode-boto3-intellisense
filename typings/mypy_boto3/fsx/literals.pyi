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
    "AutocommitPeriodTypeType",
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
    "MetadataConfigurationModeType",
    "NfsVersionType",
    "OntapDeploymentTypeType",
    "OntapVolumeTypeType",
    "OpenZFSCopyStrategyType",
    "OpenZFSDataCompressionTypeType",
    "OpenZFSDeploymentTypeType",
    "OpenZFSQuotaTypeType",
    "PrivilegedDeleteType",
    "ReportFormatType",
    "ReportScopeType",
    "ResourceTypeType",
    "RestoreOpenZFSVolumeOptionType",
    "RetentionPeriodTypeType",
    "SecurityStyleType",
    "SnaplockTypeType",
    "SnapshotFilterNameType",
    "SnapshotLifecycleType",
    "StatusType",
    "StorageTypeType",
    "StorageVirtualMachineFilterNameType",
    "StorageVirtualMachineLifecycleType",
    "StorageVirtualMachineRootVolumeSecurityStyleType",
    "StorageVirtualMachineSubtypeType",
    "TieringPolicyNameType",
    "UnitType",
    "UpdateOpenZFSVolumeOptionType",
    "VolumeFilterNameType",
    "VolumeLifecycleType",
    "VolumeStyleType",
    "VolumeTypeType",
    "WindowsAccessAuditLogLevelType",
    "WindowsDeploymentTypeType",
)

AdministrativeActionTypeType = Literal[
    "FILE_SYSTEM_ALIAS_ASSOCIATION",
    "FILE_SYSTEM_ALIAS_DISASSOCIATION",
    "FILE_SYSTEM_UPDATE",
    "IOPS_OPTIMIZATION",
    "MISCONFIGURED_STATE_RECOVERY",
    "RELEASE_NFS_V3_LOCKS",
    "SNAPSHOT_UPDATE",
    "STORAGE_OPTIMIZATION",
    "STORAGE_TYPE_OPTIMIZATION",
    "THROUGHPUT_OPTIMIZATION",
    "VOLUME_INITIALIZE_WITH_SNAPSHOT",
    "VOLUME_RESTORE",
    "VOLUME_UPDATE",
    "VOLUME_UPDATE_WITH_SNAPSHOT",
]
AliasLifecycleType = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyTypeType = Literal["NEW", "NEW_CHANGED", "NEW_CHANGED_DELETED", "NONE"]
AutocommitPeriodTypeType = Literal["DAYS", "HOURS", "MINUTES", "MONTHS", "NONE", "YEARS"]
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
MetadataConfigurationModeType = Literal["AUTOMATIC", "USER_PROVISIONED"]
NfsVersionType = Literal["NFS3"]
OntapDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
OntapVolumeTypeType = Literal["DP", "LS", "RW"]
OpenZFSCopyStrategyType = Literal["CLONE", "FULL_COPY", "INCREMENTAL_COPY"]
OpenZFSDataCompressionTypeType = Literal["LZ4", "NONE", "ZSTD"]
OpenZFSDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
OpenZFSQuotaTypeType = Literal["GROUP", "USER"]
PrivilegedDeleteType = Literal["DISABLED", "ENABLED", "PERMANENTLY_DISABLED"]
ReportFormatType = Literal["REPORT_CSV_20191124"]
ReportScopeType = Literal["FAILED_FILES_ONLY"]
ResourceTypeType = Literal["FILE_SYSTEM", "VOLUME"]
RestoreOpenZFSVolumeOptionType = Literal["DELETE_CLONED_VOLUMES", "DELETE_INTERMEDIATE_SNAPSHOTS"]
RetentionPeriodTypeType = Literal[
    "DAYS", "HOURS", "INFINITE", "MINUTES", "MONTHS", "SECONDS", "UNSPECIFIED", "YEARS"
]
SecurityStyleType = Literal["MIXED", "NTFS", "UNIX"]
SnaplockTypeType = Literal["COMPLIANCE", "ENTERPRISE"]
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
UnitType = Literal["DAYS"]
UpdateOpenZFSVolumeOptionType = Literal[
    "DELETE_CLONED_VOLUMES", "DELETE_INTERMEDIATE_DATA", "DELETE_INTERMEDIATE_SNAPSHOTS"
]
VolumeFilterNameType = Literal["file-system-id", "storage-virtual-machine-id"]
VolumeLifecycleType = Literal[
    "AVAILABLE", "CREATED", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "PENDING"
]
VolumeStyleType = Literal["FLEXGROUP", "FLEXVOL"]
VolumeTypeType = Literal["ONTAP", "OPENZFS"]
WindowsAccessAuditLogLevelType = Literal[
    "DISABLED", "FAILURE_ONLY", "SUCCESS_AND_FAILURE", "SUCCESS_ONLY"
]
WindowsDeploymentTypeType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
