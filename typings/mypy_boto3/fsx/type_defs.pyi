"""
Type annotations for fsx service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdministrativeActionTypeType,
    AliasLifecycleType,
    AutoImportPolicyTypeType,
    BackupLifecycleType,
    BackupTypeType,
    DataCompressionTypeType,
    DataRepositoryLifecycleType,
    DataRepositoryTaskFilterNameType,
    DataRepositoryTaskLifecycleType,
    DataRepositoryTaskTypeType,
    DiskIopsConfigurationModeType,
    DriveCacheTypeType,
    EventTypeType,
    FileCacheLifecycleType,
    FileSystemLifecycleType,
    FileSystemMaintenanceOperationType,
    FileSystemTypeType,
    FilterNameType,
    FlexCacheEndpointTypeType,
    InputOntapVolumeTypeType,
    LustreAccessAuditLogLevelType,
    LustreDeploymentTypeType,
    OntapDeploymentTypeType,
    OntapVolumeTypeType,
    OpenZFSCopyStrategyType,
    OpenZFSDataCompressionTypeType,
    OpenZFSDeploymentTypeType,
    OpenZFSQuotaTypeType,
    ResourceTypeType,
    RestoreOpenZFSVolumeOptionType,
    SecurityStyleType,
    SnapshotFilterNameType,
    SnapshotLifecycleType,
    StatusType,
    StorageTypeType,
    StorageVirtualMachineLifecycleType,
    StorageVirtualMachineRootVolumeSecurityStyleType,
    StorageVirtualMachineSubtypeType,
    TieringPolicyNameType,
    VolumeFilterNameType,
    VolumeLifecycleType,
    VolumeTypeType,
    WindowsAccessAuditLogLevelType,
    WindowsDeploymentTypeType,
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
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesRequestRequestTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "AutoExportPolicyTypeDef",
    "AutoImportPolicyTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestRequestTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryAssociationRequestRequestTypeDef",
    "CreateDataRepositoryAssociationResponseTypeDef",
    "CreateDataRepositoryTaskRequestRequestTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileCacheLustreConfigurationTypeDef",
    "CreateFileCacheRequestRequestTypeDef",
    "CreateFileCacheResponseTypeDef",
    "CreateFileSystemFromBackupRequestRequestTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemOntapConfigurationTypeDef",
    "CreateFileSystemOpenZFSConfigurationTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "CreateOntapVolumeConfigurationTypeDef",
    "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
    "CreateOpenZFSVolumeConfigurationTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateStorageVirtualMachineRequestRequestTypeDef",
    "CreateStorageVirtualMachineResponseTypeDef",
    "CreateSvmActiveDirectoryConfigurationTypeDef",
    "CreateVolumeFromBackupRequestRequestTypeDef",
    "CreateVolumeFromBackupResponseTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeResponseTypeDef",
    "DataRepositoryAssociationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteDataRepositoryAssociationRequestRequestTypeDef",
    "DeleteDataRepositoryAssociationResponseTypeDef",
    "DeleteFileCacheRequestRequestTypeDef",
    "DeleteFileCacheResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemOpenZFSConfigurationTypeDef",
    "DeleteFileSystemOpenZFSResponseTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteStorageVirtualMachineRequestRequestTypeDef",
    "DeleteStorageVirtualMachineResponseTypeDef",
    "DeleteVolumeOntapConfigurationTypeDef",
    "DeleteVolumeOntapResponseTypeDef",
    "DeleteVolumeOpenZFSConfigurationTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryAssociationsRequestRequestTypeDef",
    "DescribeDataRepositoryAssociationsResponseTypeDef",
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileCachesRequestRequestTypeDef",
    "DescribeFileCachesResponseTypeDef",
    "DescribeFileSystemAliasesRequestRequestTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResponseTypeDef",
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    "DescribeStorageVirtualMachinesResponseTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResponseTypeDef",
    "DisassociateFileSystemAliasesRequestRequestTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "DiskIopsConfigurationTypeDef",
    "FileCacheCreatingTypeDef",
    "FileCacheDataRepositoryAssociationTypeDef",
    "FileCacheFailureDetailsTypeDef",
    "FileCacheLustreConfigurationTypeDef",
    "FileCacheLustreMetadataConfigurationTypeDef",
    "FileCacheNFSConfigurationTypeDef",
    "FileCacheTypeDef",
    "FileSystemEndpointTypeDef",
    "FileSystemEndpointsTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "LifecycleTransitionReasonTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "LustreLogConfigurationTypeDef",
    "LustreLogCreateConfigurationTypeDef",
    "LustreRootSquashConfigurationTypeDef",
    "NFSDataRepositoryConfigurationTypeDef",
    "OntapFileSystemConfigurationTypeDef",
    "OntapVolumeConfigurationTypeDef",
    "OpenZFSClientConfigurationTypeDef",
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    "OpenZFSFileSystemConfigurationTypeDef",
    "OpenZFSNfsExportTypeDef",
    "OpenZFSOriginSnapshotConfigurationTypeDef",
    "OpenZFSUserOrGroupQuotaTypeDef",
    "OpenZFSVolumeConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ReleaseFileSystemNfsV3LocksRequestRequestTypeDef",
    "ReleaseFileSystemNfsV3LocksResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreVolumeFromSnapshotRequestRequestTypeDef",
    "RestoreVolumeFromSnapshotResponseTypeDef",
    "S3DataRepositoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "SnapshotFilterTypeDef",
    "SnapshotTypeDef",
    "StorageVirtualMachineFilterTypeDef",
    "StorageVirtualMachineTypeDef",
    "SvmActiveDirectoryConfigurationTypeDef",
    "SvmEndpointTypeDef",
    "SvmEndpointsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TieringPolicyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataRepositoryAssociationRequestRequestTypeDef",
    "UpdateDataRepositoryAssociationResponseTypeDef",
    "UpdateFileCacheLustreConfigurationTypeDef",
    "UpdateFileCacheRequestRequestTypeDef",
    "UpdateFileCacheResponseTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemOntapConfigurationTypeDef",
    "UpdateFileSystemOpenZFSConfigurationTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "UpdateOntapVolumeConfigurationTypeDef",
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "UpdateStorageVirtualMachineRequestRequestTypeDef",
    "UpdateStorageVirtualMachineResponseTypeDef",
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    "UpdateVolumeRequestRequestTypeDef",
    "UpdateVolumeResponseTypeDef",
    "VolumeFilterTypeDef",
    "VolumeTypeDef",
    "WindowsAuditLogConfigurationTypeDef",
    "WindowsAuditLogCreateConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {
        "DomainName": str,
        "ActiveDirectoryId": str,
        "ResourceARN": str,
    },
    total=False,
)

AdministrativeActionFailureDetailsTypeDef = TypedDict(
    "AdministrativeActionFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

AdministrativeActionTypeDef = TypedDict(
    "AdministrativeActionTypeDef",
    {
        "AdministrativeActionType": AdministrativeActionTypeType,
        "ProgressPercent": int,
        "RequestTime": datetime,
        "Status": StatusType,
        "TargetFileSystemValues": Dict[str, Any],
        "FailureDetails": "AdministrativeActionFailureDetailsTypeDef",
        "TargetVolumeValues": Dict[str, Any],
        "TargetSnapshotValues": Dict[str, Any],
    },
    total=False,
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": str,
        "Lifecycle": AliasLifecycleType,
    },
    total=False,
)

_RequiredAssociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": List[str],
    },
)
_OptionalAssociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class AssociateFileSystemAliasesRequestRequestTypeDef(
    _RequiredAssociateFileSystemAliasesRequestRequestTypeDef,
    _OptionalAssociateFileSystemAliasesRequestRequestTypeDef,
):
    pass

AssociateFileSystemAliasesResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoExportPolicyTypeDef = TypedDict(
    "AutoExportPolicyTypeDef",
    {
        "Events": List[EventTypeType],
    },
    total=False,
)

AutoImportPolicyTypeDef = TypedDict(
    "AutoImportPolicyTypeDef",
    {
        "Events": List[EventTypeType],
    },
    total=False,
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": "FileSystemTypeDef",
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": "BackupFailureDetailsTypeDef",
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "DirectoryInformation": "ActiveDirectoryBackupAttributesTypeDef",
        "OwnerId": str,
        "SourceBackupId": str,
        "SourceBackupRegion": str,
        "ResourceType": ResourceTypeType,
        "Volume": "VolumeTypeDef",
    },
    total=False,
)

class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass

CancelDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)

CancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseTypeDef",
    {
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "TaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompletionReportTypeDef = TypedDict(
    "_RequiredCompletionReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCompletionReportTypeDef = TypedDict(
    "_OptionalCompletionReportTypeDef",
    {
        "Path": str,
        "Format": Literal["REPORT_CSV_20191124"],
        "Scope": Literal["FAILED_FILES_ONLY"],
    },
    total=False,
)

class CompletionReportTypeDef(_RequiredCompletionReportTypeDef, _OptionalCompletionReportTypeDef):
    pass

_RequiredCopyBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCopyBackupRequestRequestTypeDef",
    {
        "SourceBackupId": str,
    },
)
_OptionalCopyBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCopyBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SourceRegion": str,
        "KmsKeyId": str,
        "CopyTags": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyBackupRequestRequestTypeDef(
    _RequiredCopyBackupRequestRequestTypeDef, _OptionalCopyBackupRequestRequestTypeDef
):
    pass

CopyBackupResponseTypeDef = TypedDict(
    "CopyBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackupRequestRequestTypeDef = TypedDict(
    "CreateBackupRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
        "VolumeId": str,
    },
    total=False,
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "DataRepositoryPath": str,
    },
)
_OptionalCreateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "FileSystemPath": str,
        "BatchImportMetaDataOnCreate": bool,
        "ImportedFileChunkSize": int,
        "S3": "S3DataRepositoryConfigurationTypeDef",
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataRepositoryAssociationRequestRequestTypeDef(
    _RequiredCreateDataRepositoryAssociationRequestRequestTypeDef,
    _OptionalCreateDataRepositoryAssociationRequestRequestTypeDef,
):
    pass

CreateDataRepositoryAssociationResponseTypeDef = TypedDict(
    "CreateDataRepositoryAssociationResponseTypeDef",
    {
        "Association": "DataRepositoryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Type": DataRepositoryTaskTypeType,
        "FileSystemId": str,
        "Report": "CompletionReportTypeDef",
    },
)
_OptionalCreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Paths": List[str],
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
        "CapacityToRelease": int,
    },
    total=False,
)

class CreateDataRepositoryTaskRequestRequestTypeDef(
    _RequiredCreateDataRepositoryTaskRequestRequestTypeDef,
    _OptionalCreateDataRepositoryTaskRequestRequestTypeDef,
):
    pass

CreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseTypeDef",
    {
        "DataRepositoryTask": "DataRepositoryTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileCacheLustreConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileCacheLustreConfigurationTypeDef",
    {
        "PerUnitStorageThroughput": int,
        "DeploymentType": Literal["CACHE_1"],
        "MetadataConfiguration": "FileCacheLustreMetadataConfigurationTypeDef",
    },
)
_OptionalCreateFileCacheLustreConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileCacheLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

class CreateFileCacheLustreConfigurationTypeDef(
    _RequiredCreateFileCacheLustreConfigurationTypeDef,
    _OptionalCreateFileCacheLustreConfigurationTypeDef,
):
    pass

_RequiredCreateFileCacheRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileCacheRequestRequestTypeDef",
    {
        "FileCacheType": Literal["LUSTRE"],
        "FileCacheTypeVersion": str,
        "StorageCapacity": int,
        "SubnetIds": List[str],
    },
)
_OptionalCreateFileCacheRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileCacheRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "CopyTagsToDataRepositoryAssociations": bool,
        "KmsKeyId": str,
        "LustreConfiguration": "CreateFileCacheLustreConfigurationTypeDef",
        "DataRepositoryAssociations": List["FileCacheDataRepositoryAssociationTypeDef"],
    },
    total=False,
)

class CreateFileCacheRequestRequestTypeDef(
    _RequiredCreateFileCacheRequestRequestTypeDef, _OptionalCreateFileCacheRequestRequestTypeDef
):
    pass

CreateFileCacheResponseTypeDef = TypedDict(
    "CreateFileCacheResponseTypeDef",
    {
        "FileCache": "FileCacheCreatingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemFromBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateFileSystemFromBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemFromBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
        "StorageType": StorageTypeType,
        "KmsKeyId": str,
        "FileSystemTypeVersion": str,
        "OpenZFSConfiguration": "CreateFileSystemOpenZFSConfigurationTypeDef",
        "StorageCapacity": int,
    },
    total=False,
)

class CreateFileSystemFromBackupRequestRequestTypeDef(
    _RequiredCreateFileSystemFromBackupRequestRequestTypeDef,
    _OptionalCreateFileSystemFromBackupRequestRequestTypeDef,
):
    pass

CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "DeploymentType": LustreDeploymentTypeType,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "PerUnitStorageThroughput": int,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
        "LogConfiguration": "LustreLogCreateConfigurationTypeDef",
        "RootSquashConfiguration": "LustreRootSquashConfigurationTypeDef",
    },
    total=False,
)

_RequiredCreateFileSystemOntapConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemOntapConfigurationTypeDef",
    {
        "DeploymentType": OntapDeploymentTypeType,
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemOntapConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemOntapConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "EndpointIpAddressRange": str,
        "FsxAdminPassword": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "PreferredSubnetId": str,
        "RouteTableIds": List[str],
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

class CreateFileSystemOntapConfigurationTypeDef(
    _RequiredCreateFileSystemOntapConfigurationTypeDef,
    _OptionalCreateFileSystemOntapConfigurationTypeDef,
):
    pass

_RequiredCreateFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemOpenZFSConfigurationTypeDef",
    {
        "DeploymentType": OpenZFSDeploymentTypeType,
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemOpenZFSConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "CopyTagsToVolumes": bool,
        "DailyAutomaticBackupStartTime": str,
        "WeeklyMaintenanceStartTime": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "RootVolumeConfiguration": "OpenZFSCreateRootVolumeConfigurationTypeDef",
    },
    total=False,
)

class CreateFileSystemOpenZFSConfigurationTypeDef(
    _RequiredCreateFileSystemOpenZFSConfigurationTypeDef,
    _OptionalCreateFileSystemOpenZFSConfigurationTypeDef,
):
    pass

_RequiredCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemRequestRequestTypeDef",
    {
        "FileSystemType": FileSystemTypeType,
        "StorageCapacity": int,
        "SubnetIds": List[str],
    },
)
_OptionalCreateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageType": StorageTypeType,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
        "OntapConfiguration": "CreateFileSystemOntapConfigurationTypeDef",
        "FileSystemTypeVersion": str,
        "OpenZFSConfiguration": "CreateFileSystemOpenZFSConfigurationTypeDef",
    },
    total=False,
)

class CreateFileSystemRequestRequestTypeDef(
    _RequiredCreateFileSystemRequestRequestTypeDef, _OptionalCreateFileSystemRequestRequestTypeDef
):
    pass

CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "PreferredSubnetId": str,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List[str],
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)

class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalCreateFileSystemWindowsConfigurationTypeDef,
):
    pass

_RequiredCreateOntapVolumeConfigurationTypeDef = TypedDict(
    "_RequiredCreateOntapVolumeConfigurationTypeDef",
    {
        "SizeInMegabytes": int,
        "StorageVirtualMachineId": str,
    },
)
_OptionalCreateOntapVolumeConfigurationTypeDef = TypedDict(
    "_OptionalCreateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": str,
        "SecurityStyle": SecurityStyleType,
        "StorageEfficiencyEnabled": bool,
        "TieringPolicy": "TieringPolicyTypeDef",
        "OntapVolumeType": InputOntapVolumeTypeType,
        "SnapshotPolicy": str,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

class CreateOntapVolumeConfigurationTypeDef(
    _RequiredCreateOntapVolumeConfigurationTypeDef, _OptionalCreateOntapVolumeConfigurationTypeDef
):
    pass

CreateOpenZFSOriginSnapshotConfigurationTypeDef = TypedDict(
    "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
    {
        "SnapshotARN": str,
        "CopyStrategy": OpenZFSCopyStrategyType,
    },
)

_RequiredCreateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "_RequiredCreateOpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": str,
    },
)
_OptionalCreateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "_OptionalCreateOpenZFSVolumeConfigurationTypeDef",
    {
        "StorageCapacityReservationGiB": int,
        "StorageCapacityQuotaGiB": int,
        "RecordSizeKiB": int,
        "DataCompressionType": OpenZFSDataCompressionTypeType,
        "CopyTagsToSnapshots": bool,
        "OriginSnapshot": "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
        "ReadOnly": bool,
        "NfsExports": List["OpenZFSNfsExportTypeDef"],
        "UserAndGroupQuotas": List["OpenZFSUserOrGroupQuotaTypeDef"],
    },
    total=False,
)

class CreateOpenZFSVolumeConfigurationTypeDef(
    _RequiredCreateOpenZFSVolumeConfigurationTypeDef,
    _OptionalCreateOpenZFSVolumeConfigurationTypeDef,
):
    pass

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "Name": str,
        "VolumeId": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStorageVirtualMachineRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Name": str,
    },
)
_OptionalCreateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStorageVirtualMachineRequestRequestTypeDef",
    {
        "ActiveDirectoryConfiguration": "CreateSvmActiveDirectoryConfigurationTypeDef",
        "ClientRequestToken": str,
        "SvmAdminPassword": str,
        "Tags": List["TagTypeDef"],
        "RootVolumeSecurityStyle": StorageVirtualMachineRootVolumeSecurityStyleType,
    },
    total=False,
)

class CreateStorageVirtualMachineRequestRequestTypeDef(
    _RequiredCreateStorageVirtualMachineRequestRequestTypeDef,
    _OptionalCreateStorageVirtualMachineRequestRequestTypeDef,
):
    pass

CreateStorageVirtualMachineResponseTypeDef = TypedDict(
    "CreateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredCreateSvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": str,
    },
)
_OptionalCreateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalCreateSvmActiveDirectoryConfigurationTypeDef",
    {
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
    },
    total=False,
)

class CreateSvmActiveDirectoryConfigurationTypeDef(
    _RequiredCreateSvmActiveDirectoryConfigurationTypeDef,
    _OptionalCreateSvmActiveDirectoryConfigurationTypeDef,
):
    pass

_RequiredCreateVolumeFromBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "Name": str,
    },
)
_OptionalCreateVolumeFromBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeFromBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "CreateOntapVolumeConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVolumeFromBackupRequestRequestTypeDef(
    _RequiredCreateVolumeFromBackupRequestRequestTypeDef,
    _OptionalCreateVolumeFromBackupRequestRequestTypeDef,
):
    pass

CreateVolumeFromBackupResponseTypeDef = TypedDict(
    "CreateVolumeFromBackupResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestRequestTypeDef",
    {
        "VolumeType": VolumeTypeType,
        "Name": str,
    },
)
_OptionalCreateVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "CreateOntapVolumeConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "OpenZFSConfiguration": "CreateOpenZFSVolumeConfigurationTypeDef",
    },
    total=False,
)

class CreateVolumeRequestRequestTypeDef(
    _RequiredCreateVolumeRequestRequestTypeDef, _OptionalCreateVolumeRequestRequestTypeDef
):
    pass

CreateVolumeResponseTypeDef = TypedDict(
    "CreateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRepositoryAssociationTypeDef = TypedDict(
    "DataRepositoryAssociationTypeDef",
    {
        "AssociationId": str,
        "ResourceARN": str,
        "FileSystemId": str,
        "Lifecycle": DataRepositoryLifecycleType,
        "FailureDetails": "DataRepositoryFailureDetailsTypeDef",
        "FileSystemPath": str,
        "DataRepositoryPath": str,
        "BatchImportMetaDataOnCreate": bool,
        "ImportedFileChunkSize": int,
        "S3": "S3DataRepositoryConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "CreationTime": datetime,
        "FileCacheId": str,
        "FileCachePath": str,
        "DataRepositorySubdirectories": List[str],
        "NFS": "NFSDataRepositoryConfigurationTypeDef",
    },
    total=False,
)

DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {
        "Lifecycle": DataRepositoryLifecycleType,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "FailureDetails": "DataRepositoryFailureDetailsTypeDef",
    },
    total=False,
)

DataRepositoryFailureDetailsTypeDef = TypedDict(
    "DataRepositoryFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "DataRepositoryTaskFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFilterTypeDef = TypedDict(
    "DataRepositoryTaskFilterTypeDef",
    {
        "Name": DataRepositoryTaskFilterNameType,
        "Values": List[str],
    },
    total=False,
)

DataRepositoryTaskStatusTypeDef = TypedDict(
    "DataRepositoryTaskStatusTypeDef",
    {
        "TotalCount": int,
        "SucceededCount": int,
        "FailedCount": int,
        "LastUpdatedTime": datetime,
        "ReleasedCapacity": int,
    },
    total=False,
)

_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": DataRepositoryTaskTypeType,
        "CreationTime": datetime,
    },
)
_OptionalDataRepositoryTaskTypeDef = TypedDict(
    "_OptionalDataRepositoryTaskTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "FileSystemId": str,
        "Paths": List[str],
        "FailureDetails": "DataRepositoryTaskFailureDetailsTypeDef",
        "Status": "DataRepositoryTaskStatusTypeDef",
        "Report": "CompletionReportTypeDef",
        "CapacityToRelease": int,
        "FileCacheId": str,
    },
    total=False,
)

class DataRepositoryTaskTypeDef(
    _RequiredDataRepositoryTaskTypeDef, _OptionalDataRepositoryTaskTypeDef
):
    pass

_RequiredDeleteBackupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
_OptionalDeleteBackupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteBackupRequestRequestTypeDef(
    _RequiredDeleteBackupRequestRequestTypeDef, _OptionalDeleteBackupRequestRequestTypeDef
):
    pass

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDataRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDeleteDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDataRepositoryAssociationRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "DeleteDataInFileSystem": bool,
    },
    total=False,
)

class DeleteDataRepositoryAssociationRequestRequestTypeDef(
    _RequiredDeleteDataRepositoryAssociationRequestRequestTypeDef,
    _OptionalDeleteDataRepositoryAssociationRequestRequestTypeDef,
):
    pass

DeleteDataRepositoryAssociationResponseTypeDef = TypedDict(
    "DeleteDataRepositoryAssociationResponseTypeDef",
    {
        "AssociationId": str,
        "Lifecycle": DataRepositoryLifecycleType,
        "DeleteDataInFileSystem": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFileCacheRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFileCacheRequestRequestTypeDef",
    {
        "FileCacheId": str,
    },
)
_OptionalDeleteFileCacheRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFileCacheRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteFileCacheRequestRequestTypeDef(
    _RequiredDeleteFileCacheRequestRequestTypeDef, _OptionalDeleteFileCacheRequestRequestTypeDef
):
    pass

DeleteFileCacheResponseTypeDef = TypedDict(
    "DeleteFileCacheResponseTypeDef",
    {
        "FileCacheId": str,
        "Lifecycle": FileCacheLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemLustreConfigurationTypeDef = TypedDict(
    "DeleteFileSystemLustreConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemLustreResponseTypeDef = TypedDict(
    "DeleteFileSystemLustreResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "DeleteFileSystemOpenZFSConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
        "Options": List[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]],
    },
    total=False,
)

DeleteFileSystemOpenZFSResponseTypeDef = TypedDict(
    "DeleteFileSystemOpenZFSResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDeleteFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "WindowsConfiguration": "DeleteFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "DeleteFileSystemLustreConfigurationTypeDef",
        "OpenZFSConfiguration": "DeleteFileSystemOpenZFSConfigurationTypeDef",
    },
    total=False,
)

class DeleteFileSystemRequestRequestTypeDef(
    _RequiredDeleteFileSystemRequestRequestTypeDef, _OptionalDeleteFileSystemRequestRequestTypeDef
):
    pass

DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycleType,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
        "OpenZFSResponse": "DeleteFileSystemOpenZFSResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalDeleteSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSnapshotRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteSnapshotRequestRequestTypeDef(
    _RequiredDeleteSnapshotRequestRequestTypeDef, _OptionalDeleteSnapshotRequestRequestTypeDef
):
    pass

DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "SnapshotId": str,
        "Lifecycle": SnapshotLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
    },
)
_OptionalDeleteStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStorageVirtualMachineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteStorageVirtualMachineRequestRequestTypeDef(
    _RequiredDeleteStorageVirtualMachineRequestRequestTypeDef,
    _OptionalDeleteStorageVirtualMachineRequestRequestTypeDef,
):
    pass

DeleteStorageVirtualMachineResponseTypeDef = TypedDict(
    "DeleteStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachineId": str,
        "Lifecycle": StorageVirtualMachineLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeOntapConfigurationTypeDef = TypedDict(
    "DeleteVolumeOntapConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteVolumeOntapResponseTypeDef = TypedDict(
    "DeleteVolumeOntapResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteVolumeOpenZFSConfigurationTypeDef = TypedDict(
    "DeleteVolumeOpenZFSConfigurationTypeDef",
    {
        "Options": List[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]],
    },
    total=False,
)

_RequiredDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "DeleteVolumeOntapConfigurationTypeDef",
        "OpenZFSConfiguration": "DeleteVolumeOpenZFSConfigurationTypeDef",
    },
    total=False,
)

class DeleteVolumeRequestRequestTypeDef(
    _RequiredDeleteVolumeRequestRequestTypeDef, _OptionalDeleteVolumeRequestRequestTypeDef
):
    pass

DeleteVolumeResponseTypeDef = TypedDict(
    "DeleteVolumeResponseTypeDef",
    {
        "VolumeId": str,
        "Lifecycle": VolumeLifecycleType,
        "OntapResponse": "DeleteVolumeOntapResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeDataRepositoryAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDataRepositoryAssociationsResponseTypeDef = TypedDict(
    "DescribeDataRepositoryAssociationsResponseTypeDef",
    {
        "Associations": List["DataRepositoryAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryTasksRequestRequestTypeDef = TypedDict(
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    {
        "TaskIds": List[str],
        "Filters": List["DataRepositoryTaskFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseTypeDef",
    {
        "DataRepositoryTasks": List["DataRepositoryTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileCachesRequestRequestTypeDef = TypedDict(
    "DescribeFileCachesRequestRequestTypeDef",
    {
        "FileCacheIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFileCachesResponseTypeDef = TypedDict(
    "DescribeFileCachesResponseTypeDef",
    {
        "FileCaches": List["FileCacheTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeFileSystemAliasesRequestRequestTypeDef(
    _RequiredDescribeFileSystemAliasesRequestRequestTypeDef,
    _OptionalDescribeFileSystemAliasesRequestRequestTypeDef,
):
    pass

DescribeFileSystemAliasesResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "FileSystemIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "FileSystems": List["FileSystemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "SnapshotIds": List[str],
        "Filters": List["SnapshotFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeSnapshotsResponseTypeDef = TypedDict(
    "DescribeSnapshotsResponseTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageVirtualMachinesRequestRequestTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    {
        "StorageVirtualMachineIds": List[str],
        "Filters": List["StorageVirtualMachineFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeStorageVirtualMachinesResponseTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesResponseTypeDef",
    {
        "StorageVirtualMachines": List["StorageVirtualMachineTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "VolumeIds": List[str],
        "Filters": List["VolumeFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVolumesResponseTypeDef = TypedDict(
    "DescribeVolumesResponseTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": List[str],
    },
)
_OptionalDisassociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateFileSystemAliasesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DisassociateFileSystemAliasesRequestRequestTypeDef(
    _RequiredDisassociateFileSystemAliasesRequestRequestTypeDef,
    _OptionalDisassociateFileSystemAliasesRequestRequestTypeDef,
):
    pass

DisassociateFileSystemAliasesResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskIopsConfigurationTypeDef = TypedDict(
    "DiskIopsConfigurationTypeDef",
    {
        "Mode": DiskIopsConfigurationModeType,
        "Iops": int,
    },
    total=False,
)

FileCacheCreatingTypeDef = TypedDict(
    "FileCacheCreatingTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileCacheId": str,
        "FileCacheType": Literal["LUSTRE"],
        "FileCacheTypeVersion": str,
        "Lifecycle": FileCacheLifecycleType,
        "FailureDetails": "FileCacheFailureDetailsTypeDef",
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "CopyTagsToDataRepositoryAssociations": bool,
        "LustreConfiguration": "FileCacheLustreConfigurationTypeDef",
        "DataRepositoryAssociationIds": List[str],
    },
    total=False,
)

_RequiredFileCacheDataRepositoryAssociationTypeDef = TypedDict(
    "_RequiredFileCacheDataRepositoryAssociationTypeDef",
    {
        "FileCachePath": str,
        "DataRepositoryPath": str,
    },
)
_OptionalFileCacheDataRepositoryAssociationTypeDef = TypedDict(
    "_OptionalFileCacheDataRepositoryAssociationTypeDef",
    {
        "DataRepositorySubdirectories": List[str],
        "NFS": "FileCacheNFSConfigurationTypeDef",
    },
    total=False,
)

class FileCacheDataRepositoryAssociationTypeDef(
    _RequiredFileCacheDataRepositoryAssociationTypeDef,
    _OptionalFileCacheDataRepositoryAssociationTypeDef,
):
    pass

FileCacheFailureDetailsTypeDef = TypedDict(
    "FileCacheFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

FileCacheLustreConfigurationTypeDef = TypedDict(
    "FileCacheLustreConfigurationTypeDef",
    {
        "PerUnitStorageThroughput": int,
        "DeploymentType": Literal["CACHE_1"],
        "MountName": str,
        "WeeklyMaintenanceStartTime": str,
        "MetadataConfiguration": "FileCacheLustreMetadataConfigurationTypeDef",
        "LogConfiguration": "LustreLogConfigurationTypeDef",
    },
    total=False,
)

FileCacheLustreMetadataConfigurationTypeDef = TypedDict(
    "FileCacheLustreMetadataConfigurationTypeDef",
    {
        "StorageCapacity": int,
    },
)

_RequiredFileCacheNFSConfigurationTypeDef = TypedDict(
    "_RequiredFileCacheNFSConfigurationTypeDef",
    {
        "Version": Literal["NFS3"],
    },
)
_OptionalFileCacheNFSConfigurationTypeDef = TypedDict(
    "_OptionalFileCacheNFSConfigurationTypeDef",
    {
        "DnsIps": List[str],
    },
    total=False,
)

class FileCacheNFSConfigurationTypeDef(
    _RequiredFileCacheNFSConfigurationTypeDef, _OptionalFileCacheNFSConfigurationTypeDef
):
    pass

FileCacheTypeDef = TypedDict(
    "FileCacheTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileCacheId": str,
        "FileCacheType": Literal["LUSTRE"],
        "FileCacheTypeVersion": str,
        "Lifecycle": FileCacheLifecycleType,
        "FailureDetails": "FileCacheFailureDetailsTypeDef",
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "LustreConfiguration": "FileCacheLustreConfigurationTypeDef",
        "DataRepositoryAssociationIds": List[str],
    },
    total=False,
)

FileSystemEndpointTypeDef = TypedDict(
    "FileSystemEndpointTypeDef",
    {
        "DNSName": str,
        "IpAddresses": List[str],
    },
    total=False,
)

FileSystemEndpointsTypeDef = TypedDict(
    "FileSystemEndpointsTypeDef",
    {
        "Intercluster": "FileSystemEndpointTypeDef",
        "Management": "FileSystemEndpointTypeDef",
    },
    total=False,
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": FileSystemTypeType,
        "Lifecycle": FileSystemLifecycleType,
        "FailureDetails": "FileSystemFailureDetailsTypeDef",
        "StorageCapacity": int,
        "StorageType": StorageTypeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "WindowsFileSystemConfigurationTypeDef",
        "LustreConfiguration": "LustreFileSystemConfigurationTypeDef",
        "AdministrativeActions": List[Dict[str, Any]],
        "OntapConfiguration": "OntapFileSystemConfigurationTypeDef",
        "FileSystemTypeVersion": str,
        "OpenZFSConfiguration": "OpenZFSFileSystemConfigurationTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": FilterNameType,
        "Values": List[str],
    },
    total=False,
)

LifecycleTransitionReasonTypeDef = TypedDict(
    "LifecycleTransitionReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": "DataRepositoryConfigurationTypeDef",
        "DeploymentType": LustreDeploymentTypeType,
        "PerUnitStorageThroughput": int,
        "MountName": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
        "LogConfiguration": "LustreLogConfigurationTypeDef",
        "RootSquashConfiguration": "LustreRootSquashConfigurationTypeDef",
    },
    total=False,
)

_RequiredLustreLogConfigurationTypeDef = TypedDict(
    "_RequiredLustreLogConfigurationTypeDef",
    {
        "Level": LustreAccessAuditLogLevelType,
    },
)
_OptionalLustreLogConfigurationTypeDef = TypedDict(
    "_OptionalLustreLogConfigurationTypeDef",
    {
        "Destination": str,
    },
    total=False,
)

class LustreLogConfigurationTypeDef(
    _RequiredLustreLogConfigurationTypeDef, _OptionalLustreLogConfigurationTypeDef
):
    pass

_RequiredLustreLogCreateConfigurationTypeDef = TypedDict(
    "_RequiredLustreLogCreateConfigurationTypeDef",
    {
        "Level": LustreAccessAuditLogLevelType,
    },
)
_OptionalLustreLogCreateConfigurationTypeDef = TypedDict(
    "_OptionalLustreLogCreateConfigurationTypeDef",
    {
        "Destination": str,
    },
    total=False,
)

class LustreLogCreateConfigurationTypeDef(
    _RequiredLustreLogCreateConfigurationTypeDef, _OptionalLustreLogCreateConfigurationTypeDef
):
    pass

LustreRootSquashConfigurationTypeDef = TypedDict(
    "LustreRootSquashConfigurationTypeDef",
    {
        "RootSquash": str,
        "NoSquashNids": List[str],
    },
    total=False,
)

_RequiredNFSDataRepositoryConfigurationTypeDef = TypedDict(
    "_RequiredNFSDataRepositoryConfigurationTypeDef",
    {
        "Version": Literal["NFS3"],
    },
)
_OptionalNFSDataRepositoryConfigurationTypeDef = TypedDict(
    "_OptionalNFSDataRepositoryConfigurationTypeDef",
    {
        "DnsIps": List[str],
        "AutoExportPolicy": "AutoExportPolicyTypeDef",
    },
    total=False,
)

class NFSDataRepositoryConfigurationTypeDef(
    _RequiredNFSDataRepositoryConfigurationTypeDef, _OptionalNFSDataRepositoryConfigurationTypeDef
):
    pass

OntapFileSystemConfigurationTypeDef = TypedDict(
    "OntapFileSystemConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "DeploymentType": OntapDeploymentTypeType,
        "EndpointIpAddressRange": str,
        "Endpoints": "FileSystemEndpointsTypeDef",
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "PreferredSubnetId": str,
        "RouteTableIds": List[str],
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

OntapVolumeConfigurationTypeDef = TypedDict(
    "OntapVolumeConfigurationTypeDef",
    {
        "FlexCacheEndpointType": FlexCacheEndpointTypeType,
        "JunctionPath": str,
        "SecurityStyle": SecurityStyleType,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "StorageVirtualMachineId": str,
        "StorageVirtualMachineRoot": bool,
        "TieringPolicy": "TieringPolicyTypeDef",
        "UUID": str,
        "OntapVolumeType": OntapVolumeTypeType,
        "SnapshotPolicy": str,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

OpenZFSClientConfigurationTypeDef = TypedDict(
    "OpenZFSClientConfigurationTypeDef",
    {
        "Clients": str,
        "Options": List[str],
    },
)

OpenZFSCreateRootVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    {
        "RecordSizeKiB": int,
        "DataCompressionType": OpenZFSDataCompressionTypeType,
        "NfsExports": List["OpenZFSNfsExportTypeDef"],
        "UserAndGroupQuotas": List["OpenZFSUserOrGroupQuotaTypeDef"],
        "CopyTagsToSnapshots": bool,
        "ReadOnly": bool,
    },
    total=False,
)

OpenZFSFileSystemConfigurationTypeDef = TypedDict(
    "OpenZFSFileSystemConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "CopyTagsToVolumes": bool,
        "DailyAutomaticBackupStartTime": str,
        "DeploymentType": OpenZFSDeploymentTypeType,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "RootVolumeId": str,
    },
    total=False,
)

OpenZFSNfsExportTypeDef = TypedDict(
    "OpenZFSNfsExportTypeDef",
    {
        "ClientConfigurations": List["OpenZFSClientConfigurationTypeDef"],
    },
)

OpenZFSOriginSnapshotConfigurationTypeDef = TypedDict(
    "OpenZFSOriginSnapshotConfigurationTypeDef",
    {
        "SnapshotARN": str,
        "CopyStrategy": OpenZFSCopyStrategyType,
    },
    total=False,
)

OpenZFSUserOrGroupQuotaTypeDef = TypedDict(
    "OpenZFSUserOrGroupQuotaTypeDef",
    {
        "Type": OpenZFSQuotaTypeType,
        "Id": int,
        "StorageCapacityQuotaGiB": int,
    },
)

OpenZFSVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": str,
        "VolumePath": str,
        "StorageCapacityReservationGiB": int,
        "StorageCapacityQuotaGiB": int,
        "RecordSizeKiB": int,
        "DataCompressionType": OpenZFSDataCompressionTypeType,
        "CopyTagsToSnapshots": bool,
        "OriginSnapshot": "OpenZFSOriginSnapshotConfigurationTypeDef",
        "ReadOnly": bool,
        "NfsExports": List["OpenZFSNfsExportTypeDef"],
        "UserAndGroupQuotas": List["OpenZFSUserOrGroupQuotaTypeDef"],
        "RestoreToSnapshot": str,
        "DeleteIntermediateSnaphots": bool,
        "DeleteClonedVolumes": bool,
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

_RequiredReleaseFileSystemNfsV3LocksRequestRequestTypeDef = TypedDict(
    "_RequiredReleaseFileSystemNfsV3LocksRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalReleaseFileSystemNfsV3LocksRequestRequestTypeDef = TypedDict(
    "_OptionalReleaseFileSystemNfsV3LocksRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class ReleaseFileSystemNfsV3LocksRequestRequestTypeDef(
    _RequiredReleaseFileSystemNfsV3LocksRequestRequestTypeDef,
    _OptionalReleaseFileSystemNfsV3LocksRequestRequestTypeDef,
):
    pass

ReleaseFileSystemNfsV3LocksResponseTypeDef = TypedDict(
    "ReleaseFileSystemNfsV3LocksResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
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

_RequiredRestoreVolumeFromSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreVolumeFromSnapshotRequestRequestTypeDef",
    {
        "VolumeId": str,
        "SnapshotId": str,
    },
)
_OptionalRestoreVolumeFromSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreVolumeFromSnapshotRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Options": List[RestoreOpenZFSVolumeOptionType],
    },
    total=False,
)

class RestoreVolumeFromSnapshotRequestRequestTypeDef(
    _RequiredRestoreVolumeFromSnapshotRequestRequestTypeDef,
    _OptionalRestoreVolumeFromSnapshotRequestRequestTypeDef,
):
    pass

RestoreVolumeFromSnapshotResponseTypeDef = TypedDict(
    "RestoreVolumeFromSnapshotResponseTypeDef",
    {
        "VolumeId": str,
        "Lifecycle": VolumeLifecycleType,
        "AdministrativeActions": List["AdministrativeActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3DataRepositoryConfigurationTypeDef = TypedDict(
    "S3DataRepositoryConfigurationTypeDef",
    {
        "AutoImportPolicy": "AutoImportPolicyTypeDef",
        "AutoExportPolicy": "AutoExportPolicyTypeDef",
    },
    total=False,
)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

_RequiredSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
)
_OptionalSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
    },
    total=False,
)

class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalSelfManagedActiveDirectoryConfigurationTypeDef,
):
    pass

SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)

SnapshotFilterTypeDef = TypedDict(
    "SnapshotFilterTypeDef",
    {
        "Name": SnapshotFilterNameType,
        "Values": List[str],
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "ResourceARN": str,
        "SnapshotId": str,
        "Name": str,
        "VolumeId": str,
        "CreationTime": datetime,
        "Lifecycle": SnapshotLifecycleType,
        "LifecycleTransitionReason": "LifecycleTransitionReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "AdministrativeActions": List["AdministrativeActionTypeDef"],
    },
    total=False,
)

StorageVirtualMachineFilterTypeDef = TypedDict(
    "StorageVirtualMachineFilterTypeDef",
    {
        "Name": Literal["file-system-id"],
        "Values": List[str],
    },
    total=False,
)

StorageVirtualMachineTypeDef = TypedDict(
    "StorageVirtualMachineTypeDef",
    {
        "ActiveDirectoryConfiguration": "SvmActiveDirectoryConfigurationTypeDef",
        "CreationTime": datetime,
        "Endpoints": "SvmEndpointsTypeDef",
        "FileSystemId": str,
        "Lifecycle": StorageVirtualMachineLifecycleType,
        "Name": str,
        "ResourceARN": str,
        "StorageVirtualMachineId": str,
        "Subtype": StorageVirtualMachineSubtypeType,
        "UUID": str,
        "Tags": List["TagTypeDef"],
        "LifecycleTransitionReason": "LifecycleTransitionReasonTypeDef",
        "RootVolumeSecurityStyle": StorageVirtualMachineRootVolumeSecurityStyleType,
    },
    total=False,
)

SvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "SvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
    },
    total=False,
)

SvmEndpointTypeDef = TypedDict(
    "SvmEndpointTypeDef",
    {
        "DNSName": str,
        "IpAddresses": List[str],
    },
    total=False,
)

SvmEndpointsTypeDef = TypedDict(
    "SvmEndpointsTypeDef",
    {
        "Iscsi": "SvmEndpointTypeDef",
        "Management": "SvmEndpointTypeDef",
        "Nfs": "SvmEndpointTypeDef",
        "Smb": "SvmEndpointTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TieringPolicyTypeDef = TypedDict(
    "TieringPolicyTypeDef",
    {
        "CoolingPeriod": int,
        "Name": TieringPolicyNameType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalUpdateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ImportedFileChunkSize": int,
        "S3": "S3DataRepositoryConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataRepositoryAssociationRequestRequestTypeDef(
    _RequiredUpdateDataRepositoryAssociationRequestRequestTypeDef,
    _OptionalUpdateDataRepositoryAssociationRequestRequestTypeDef,
):
    pass

UpdateDataRepositoryAssociationResponseTypeDef = TypedDict(
    "UpdateDataRepositoryAssociationResponseTypeDef",
    {
        "Association": "DataRepositoryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileCacheLustreConfigurationTypeDef = TypedDict(
    "UpdateFileCacheLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
    },
    total=False,
)

_RequiredUpdateFileCacheRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFileCacheRequestRequestTypeDef",
    {
        "FileCacheId": str,
    },
)
_OptionalUpdateFileCacheRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFileCacheRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "LustreConfiguration": "UpdateFileCacheLustreConfigurationTypeDef",
    },
    total=False,
)

class UpdateFileCacheRequestRequestTypeDef(
    _RequiredUpdateFileCacheRequestRequestTypeDef, _OptionalUpdateFileCacheRequestRequestTypeDef
):
    pass

UpdateFileCacheResponseTypeDef = TypedDict(
    "UpdateFileCacheResponseTypeDef",
    {
        "FileCache": "FileCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "DataCompressionType": DataCompressionTypeType,
        "LogConfiguration": "LustreLogCreateConfigurationTypeDef",
        "RootSquashConfiguration": "LustreRootSquashConfigurationTypeDef",
    },
    total=False,
)

UpdateFileSystemOntapConfigurationTypeDef = TypedDict(
    "UpdateFileSystemOntapConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "DailyAutomaticBackupStartTime": str,
        "FsxAdminPassword": str,
        "WeeklyMaintenanceStartTime": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
        "ThroughputCapacity": int,
        "AddRouteTableIds": List[str],
        "RemoveRouteTableIds": List[str],
    },
    total=False,
)

UpdateFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "UpdateFileSystemOpenZFSConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "CopyTagsToVolumes": bool,
        "DailyAutomaticBackupStartTime": str,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DiskIopsConfiguration": "DiskIopsConfigurationTypeDef",
    },
    total=False,
)

_RequiredUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalUpdateFileSystemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageCapacity": int,
        "WindowsConfiguration": "UpdateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "UpdateFileSystemLustreConfigurationTypeDef",
        "OntapConfiguration": "UpdateFileSystemOntapConfigurationTypeDef",
        "OpenZFSConfiguration": "UpdateFileSystemOpenZFSConfigurationTypeDef",
    },
    total=False,
)

class UpdateFileSystemRequestRequestTypeDef(
    _RequiredUpdateFileSystemRequestRequestTypeDef, _OptionalUpdateFileSystemRequestRequestTypeDef
):
    pass

UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "ThroughputCapacity": int,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)

UpdateOntapVolumeConfigurationTypeDef = TypedDict(
    "UpdateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": str,
        "SecurityStyle": SecurityStyleType,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "TieringPolicy": "TieringPolicyTypeDef",
        "SnapshotPolicy": str,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

UpdateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    {
        "StorageCapacityReservationGiB": int,
        "StorageCapacityQuotaGiB": int,
        "RecordSizeKiB": int,
        "DataCompressionType": OpenZFSDataCompressionTypeType,
        "NfsExports": List["OpenZFSNfsExportTypeDef"],
        "UserAndGroupQuotas": List["OpenZFSUserOrGroupQuotaTypeDef"],
        "ReadOnly": bool,
    },
    total=False,
)

_RequiredUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSnapshotRequestRequestTypeDef",
    {
        "Name": str,
        "SnapshotId": str,
    },
)
_OptionalUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSnapshotRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class UpdateSnapshotRequestRequestTypeDef(
    _RequiredUpdateSnapshotRequestRequestTypeDef, _OptionalUpdateSnapshotRequestRequestTypeDef
):
    pass

UpdateSnapshotResponseTypeDef = TypedDict(
    "UpdateSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
    },
)
_OptionalUpdateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageVirtualMachineRequestRequestTypeDef",
    {
        "ActiveDirectoryConfiguration": "UpdateSvmActiveDirectoryConfigurationTypeDef",
        "ClientRequestToken": str,
        "SvmAdminPassword": str,
    },
    total=False,
)

class UpdateStorageVirtualMachineRequestRequestTypeDef(
    _RequiredUpdateStorageVirtualMachineRequestRequestTypeDef,
    _OptionalUpdateStorageVirtualMachineRequestRequestTypeDef,
):
    pass

UpdateStorageVirtualMachineResponseTypeDef = TypedDict(
    "UpdateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    {
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    },
    total=False,
)

_RequiredUpdateVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalUpdateVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVolumeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "OntapConfiguration": "UpdateOntapVolumeConfigurationTypeDef",
        "Name": str,
        "OpenZFSConfiguration": "UpdateOpenZFSVolumeConfigurationTypeDef",
    },
    total=False,
)

class UpdateVolumeRequestRequestTypeDef(
    _RequiredUpdateVolumeRequestRequestTypeDef, _OptionalUpdateVolumeRequestRequestTypeDef
):
    pass

UpdateVolumeResponseTypeDef = TypedDict(
    "UpdateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeFilterTypeDef = TypedDict(
    "VolumeFilterTypeDef",
    {
        "Name": VolumeFilterNameType,
        "Values": List[str],
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "CreationTime": datetime,
        "FileSystemId": str,
        "Lifecycle": VolumeLifecycleType,
        "Name": str,
        "OntapConfiguration": "OntapVolumeConfigurationTypeDef",
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "VolumeId": str,
        "VolumeType": VolumeTypeType,
        "LifecycleTransitionReason": "LifecycleTransitionReasonTypeDef",
        "AdministrativeActions": List["AdministrativeActionTypeDef"],
        "OpenZFSConfiguration": "OpenZFSVolumeConfigurationTypeDef",
    },
    total=False,
)

_RequiredWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)

class WindowsAuditLogConfigurationTypeDef(
    _RequiredWindowsAuditLogConfigurationTypeDef, _OptionalWindowsAuditLogConfigurationTypeDef
):
    pass

_RequiredWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogCreateConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogCreateConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)

class WindowsAuditLogCreateConfigurationTypeDef(
    _RequiredWindowsAuditLogCreateConfigurationTypeDef,
    _OptionalWindowsAuditLogCreateConfigurationTypeDef,
):
    pass

WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[FileSystemMaintenanceOperationType],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List["AliasTypeDef"],
        "AuditLogConfiguration": "WindowsAuditLogConfigurationTypeDef",
    },
    total=False,
)
