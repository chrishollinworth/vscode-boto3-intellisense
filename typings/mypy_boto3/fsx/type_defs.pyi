"""
Type annotations for fsx service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AdministrativeActionTypeType,
    AliasLifecycleType,
    AutocommitPeriodTypeType,
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
    MetadataConfigurationModeType,
    OntapDeploymentTypeType,
    OntapVolumeTypeType,
    OpenZFSCopyStrategyType,
    OpenZFSDataCompressionTypeType,
    OpenZFSDeploymentTypeType,
    OpenZFSQuotaTypeType,
    OpenZFSReadCacheSizingModeType,
    PrivilegedDeleteType,
    ResourceTypeType,
    RestoreOpenZFSVolumeOptionType,
    RetentionPeriodTypeType,
    SecurityStyleType,
    SnaplockTypeType,
    SnapshotFilterNameType,
    SnapshotLifecycleType,
    StatusType,
    StorageTypeType,
    StorageVirtualMachineLifecycleType,
    StorageVirtualMachineRootVolumeSecurityStyleType,
    StorageVirtualMachineSubtypeType,
    TieringPolicyNameType,
    UpdateOpenZFSVolumeOptionType,
    VolumeFilterNameType,
    VolumeLifecycleType,
    VolumeStyleType,
    VolumeTypeType,
    WindowsAccessAuditLogLevelType,
    WindowsDeploymentTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionPaginatorTypeDef",
    "AdministrativeActionTypeDef",
    "AggregateConfigurationTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesRequestTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "AutoExportPolicyOutputTypeDef",
    "AutoExportPolicyTypeDef",
    "AutoImportPolicyOutputTypeDef",
    "AutoImportPolicyTypeDef",
    "AutocommitPeriodTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupPaginatorTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestTypeDef",
    "CopyBackupResponseTypeDef",
    "CopySnapshotAndUpdateVolumeRequestTypeDef",
    "CopySnapshotAndUpdateVolumeResponseTypeDef",
    "CreateAggregateConfigurationTypeDef",
    "CreateBackupRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryAssociationRequestTypeDef",
    "CreateDataRepositoryAssociationResponseTypeDef",
    "CreateDataRepositoryTaskRequestTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileCacheLustreConfigurationTypeDef",
    "CreateFileCacheRequestTypeDef",
    "CreateFileCacheResponseTypeDef",
    "CreateFileSystemFromBackupRequestTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemLustreMetadataConfigurationTypeDef",
    "CreateFileSystemOntapConfigurationTypeDef",
    "CreateFileSystemOpenZFSConfigurationTypeDef",
    "CreateFileSystemRequestTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "CreateOntapVolumeConfigurationTypeDef",
    "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
    "CreateOpenZFSVolumeConfigurationTypeDef",
    "CreateSnaplockConfigurationTypeDef",
    "CreateSnapshotRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateStorageVirtualMachineRequestTypeDef",
    "CreateStorageVirtualMachineResponseTypeDef",
    "CreateSvmActiveDirectoryConfigurationTypeDef",
    "CreateVolumeFromBackupRequestTypeDef",
    "CreateVolumeFromBackupResponseTypeDef",
    "CreateVolumeRequestTypeDef",
    "CreateVolumeResponseTypeDef",
    "DataRepositoryAssociationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteDataRepositoryAssociationRequestTypeDef",
    "DeleteDataRepositoryAssociationResponseTypeDef",
    "DeleteFileCacheRequestTypeDef",
    "DeleteFileCacheResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemOpenZFSConfigurationTypeDef",
    "DeleteFileSystemOpenZFSResponseTypeDef",
    "DeleteFileSystemRequestTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DeleteSnapshotRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteStorageVirtualMachineRequestTypeDef",
    "DeleteStorageVirtualMachineResponseTypeDef",
    "DeleteVolumeOntapConfigurationTypeDef",
    "DeleteVolumeOntapResponseTypeDef",
    "DeleteVolumeOpenZFSConfigurationTypeDef",
    "DeleteVolumeRequestTypeDef",
    "DeleteVolumeResponseTypeDef",
    "DescribeBackupsRequestPaginateTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponsePaginatorTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryAssociationsRequestTypeDef",
    "DescribeDataRepositoryAssociationsResponseTypeDef",
    "DescribeDataRepositoryTasksRequestTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileCachesRequestTypeDef",
    "DescribeFileCachesResponseTypeDef",
    "DescribeFileSystemAliasesRequestTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsRequestPaginateTypeDef",
    "DescribeFileSystemsRequestTypeDef",
    "DescribeFileSystemsResponsePaginatorTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeSharedVpcConfigurationResponseTypeDef",
    "DescribeSnapshotsRequestTypeDef",
    "DescribeSnapshotsResponseTypeDef",
    "DescribeStorageVirtualMachinesRequestPaginateTypeDef",
    "DescribeStorageVirtualMachinesRequestTypeDef",
    "DescribeStorageVirtualMachinesResponseTypeDef",
    "DescribeVolumesRequestPaginateTypeDef",
    "DescribeVolumesRequestTypeDef",
    "DescribeVolumesResponsePaginatorTypeDef",
    "DescribeVolumesResponseTypeDef",
    "DisassociateFileSystemAliasesRequestTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "DiskIopsConfigurationTypeDef",
    "DurationSinceLastAccessTypeDef",
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
    "FileSystemLustreMetadataConfigurationTypeDef",
    "FileSystemPaginatorTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "LifecycleTransitionReasonTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "LustreLogConfigurationTypeDef",
    "LustreLogCreateConfigurationTypeDef",
    "LustreRootSquashConfigurationOutputTypeDef",
    "LustreRootSquashConfigurationTypeDef",
    "LustreRootSquashConfigurationUnionTypeDef",
    "NFSDataRepositoryConfigurationTypeDef",
    "OntapFileSystemConfigurationTypeDef",
    "OntapVolumeConfigurationTypeDef",
    "OpenZFSClientConfigurationOutputTypeDef",
    "OpenZFSClientConfigurationTypeDef",
    "OpenZFSClientConfigurationUnionTypeDef",
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    "OpenZFSFileSystemConfigurationTypeDef",
    "OpenZFSNfsExportOutputTypeDef",
    "OpenZFSNfsExportTypeDef",
    "OpenZFSNfsExportUnionTypeDef",
    "OpenZFSOriginSnapshotConfigurationTypeDef",
    "OpenZFSReadCacheConfigurationTypeDef",
    "OpenZFSUserOrGroupQuotaTypeDef",
    "OpenZFSVolumeConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ReleaseConfigurationTypeDef",
    "ReleaseFileSystemNfsV3LocksRequestTypeDef",
    "ReleaseFileSystemNfsV3LocksResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreVolumeFromSnapshotRequestTypeDef",
    "RestoreVolumeFromSnapshotResponseTypeDef",
    "RetentionPeriodTypeDef",
    "S3DataRepositoryConfigurationOutputTypeDef",
    "S3DataRepositoryConfigurationTypeDef",
    "S3DataRepositoryConfigurationUnionTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "SnaplockConfigurationTypeDef",
    "SnaplockRetentionPeriodTypeDef",
    "SnapshotFilterTypeDef",
    "SnapshotPaginatorTypeDef",
    "SnapshotTypeDef",
    "StartMisconfiguredStateRecoveryRequestTypeDef",
    "StartMisconfiguredStateRecoveryResponseTypeDef",
    "StorageVirtualMachineFilterTypeDef",
    "StorageVirtualMachineTypeDef",
    "SvmActiveDirectoryConfigurationTypeDef",
    "SvmEndpointTypeDef",
    "SvmEndpointsTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TieringPolicyTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDataRepositoryAssociationRequestTypeDef",
    "UpdateDataRepositoryAssociationResponseTypeDef",
    "UpdateFileCacheLustreConfigurationTypeDef",
    "UpdateFileCacheRequestTypeDef",
    "UpdateFileCacheResponseTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemLustreMetadataConfigurationTypeDef",
    "UpdateFileSystemOntapConfigurationTypeDef",
    "UpdateFileSystemOpenZFSConfigurationTypeDef",
    "UpdateFileSystemRequestTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "UpdateOntapVolumeConfigurationTypeDef",
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    "UpdateSharedVpcConfigurationRequestTypeDef",
    "UpdateSharedVpcConfigurationResponseTypeDef",
    "UpdateSnaplockConfigurationTypeDef",
    "UpdateSnapshotRequestTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "UpdateStorageVirtualMachineRequestTypeDef",
    "UpdateStorageVirtualMachineResponseTypeDef",
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    "UpdateVolumeRequestTypeDef",
    "UpdateVolumeResponseTypeDef",
    "VolumeFilterTypeDef",
    "VolumePaginatorTypeDef",
    "VolumeTypeDef",
    "WindowsAuditLogConfigurationTypeDef",
    "WindowsAuditLogCreateConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)

class ActiveDirectoryBackupAttributesTypeDef(TypedDict):
    DomainName: NotRequired[str]
    ActiveDirectoryId: NotRequired[str]
    ResourceARN: NotRequired[str]

class AdministrativeActionFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class AggregateConfigurationTypeDef(TypedDict):
    Aggregates: NotRequired[List[str]]
    TotalConstituents: NotRequired[int]

class AliasTypeDef(TypedDict):
    Name: NotRequired[str]
    Lifecycle: NotRequired[AliasLifecycleType]

class AssociateFileSystemAliasesRequestTypeDef(TypedDict):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AutoExportPolicyOutputTypeDef(TypedDict):
    Events: NotRequired[List[EventTypeType]]

class AutoExportPolicyTypeDef(TypedDict):
    Events: NotRequired[Sequence[EventTypeType]]

class AutoImportPolicyOutputTypeDef(TypedDict):
    Events: NotRequired[List[EventTypeType]]

class AutoImportPolicyTypeDef(TypedDict):
    Events: NotRequired[Sequence[EventTypeType]]

AutocommitPeriodTypeDef = TypedDict(
    "AutocommitPeriodTypeDef",
    {
        "Type": AutocommitPeriodTypeType,
        "Value": NotRequired[int],
    },
)

class BackupFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CancelDataRepositoryTaskRequestTypeDef(TypedDict):
    TaskId: str

class CompletionReportTypeDef(TypedDict):
    Enabled: bool
    Path: NotRequired[str]
    Format: NotRequired[Literal["REPORT_CSV_20191124"]]
    Scope: NotRequired[Literal["FAILED_FILES_ONLY"]]

class CopySnapshotAndUpdateVolumeRequestTypeDef(TypedDict):
    VolumeId: str
    SourceSnapshotARN: str
    ClientRequestToken: NotRequired[str]
    CopyStrategy: NotRequired[OpenZFSCopyStrategyType]
    Options: NotRequired[Sequence[UpdateOpenZFSVolumeOptionType]]

class CreateAggregateConfigurationTypeDef(TypedDict):
    Aggregates: NotRequired[Sequence[str]]
    ConstituentsPerAggregate: NotRequired[int]

class FileCacheLustreMetadataConfigurationTypeDef(TypedDict):
    StorageCapacity: int

class CreateFileSystemLustreMetadataConfigurationTypeDef(TypedDict):
    Mode: MetadataConfigurationModeType
    Iops: NotRequired[int]

class LustreLogCreateConfigurationTypeDef(TypedDict):
    Level: LustreAccessAuditLogLevelType
    Destination: NotRequired[str]

class DiskIopsConfigurationTypeDef(TypedDict):
    Mode: NotRequired[DiskIopsConfigurationModeType]
    Iops: NotRequired[int]

class OpenZFSReadCacheConfigurationTypeDef(TypedDict):
    SizingMode: NotRequired[OpenZFSReadCacheSizingModeType]
    SizeGiB: NotRequired[int]

class SelfManagedActiveDirectoryConfigurationTypeDef(TypedDict):
    DomainName: str
    UserName: str
    Password: str
    DnsIps: Sequence[str]
    OrganizationalUnitDistinguishedName: NotRequired[str]
    FileSystemAdministratorsGroup: NotRequired[str]

class WindowsAuditLogCreateConfigurationTypeDef(TypedDict):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: NotRequired[str]

class TieringPolicyTypeDef(TypedDict):
    CoolingPeriod: NotRequired[int]
    Name: NotRequired[TieringPolicyNameType]

class CreateOpenZFSOriginSnapshotConfigurationTypeDef(TypedDict):
    SnapshotARN: str
    CopyStrategy: OpenZFSCopyStrategyType

OpenZFSUserOrGroupQuotaTypeDef = TypedDict(
    "OpenZFSUserOrGroupQuotaTypeDef",
    {
        "Type": OpenZFSQuotaTypeType,
        "Id": int,
        "StorageCapacityQuotaGiB": int,
    },
)

class DataRepositoryFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class DataRepositoryTaskFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class DataRepositoryTaskFilterTypeDef(TypedDict):
    Name: NotRequired[DataRepositoryTaskFilterNameType]
    Values: NotRequired[Sequence[str]]

class DataRepositoryTaskStatusTypeDef(TypedDict):
    TotalCount: NotRequired[int]
    SucceededCount: NotRequired[int]
    FailedCount: NotRequired[int]
    LastUpdatedTime: NotRequired[datetime]
    ReleasedCapacity: NotRequired[int]

class DeleteBackupRequestTypeDef(TypedDict):
    BackupId: str
    ClientRequestToken: NotRequired[str]

class DeleteDataRepositoryAssociationRequestTypeDef(TypedDict):
    AssociationId: str
    ClientRequestToken: NotRequired[str]
    DeleteDataInFileSystem: NotRequired[bool]

class DeleteFileCacheRequestTypeDef(TypedDict):
    FileCacheId: str
    ClientRequestToken: NotRequired[str]

class DeleteSnapshotRequestTypeDef(TypedDict):
    SnapshotId: str
    ClientRequestToken: NotRequired[str]

class DeleteStorageVirtualMachineRequestTypeDef(TypedDict):
    StorageVirtualMachineId: str
    ClientRequestToken: NotRequired[str]

class DeleteVolumeOpenZFSConfigurationTypeDef(TypedDict):
    Options: NotRequired[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]]

class FilterTypeDef(TypedDict):
    Name: NotRequired[FilterNameType]
    Values: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeFileCachesRequestTypeDef(TypedDict):
    FileCacheIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeFileSystemAliasesRequestTypeDef(TypedDict):
    FileSystemId: str
    ClientRequestToken: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeFileSystemsRequestTypeDef(TypedDict):
    FileSystemIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SnapshotFilterTypeDef(TypedDict):
    Name: NotRequired[SnapshotFilterNameType]
    Values: NotRequired[Sequence[str]]

class StorageVirtualMachineFilterTypeDef(TypedDict):
    Name: NotRequired[Literal["file-system-id"]]
    Values: NotRequired[Sequence[str]]

class VolumeFilterTypeDef(TypedDict):
    Name: NotRequired[VolumeFilterNameType]
    Values: NotRequired[Sequence[str]]

class DisassociateFileSystemAliasesRequestTypeDef(TypedDict):
    FileSystemId: str
    Aliases: Sequence[str]
    ClientRequestToken: NotRequired[str]

class DurationSinceLastAccessTypeDef(TypedDict):
    Unit: NotRequired[Literal["DAYS"]]
    Value: NotRequired[int]

class FileCacheFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class FileCacheNFSConfigurationTypeDef(TypedDict):
    Version: Literal["NFS3"]
    DnsIps: NotRequired[Sequence[str]]

class LustreLogConfigurationTypeDef(TypedDict):
    Level: LustreAccessAuditLogLevelType
    Destination: NotRequired[str]

class FileSystemEndpointTypeDef(TypedDict):
    DNSName: NotRequired[str]
    IpAddresses: NotRequired[List[str]]

class FileSystemFailureDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class FileSystemLustreMetadataConfigurationTypeDef(TypedDict):
    Mode: MetadataConfigurationModeType
    Iops: NotRequired[int]

class LifecycleTransitionReasonTypeDef(TypedDict):
    Message: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class LustreRootSquashConfigurationOutputTypeDef(TypedDict):
    RootSquash: NotRequired[str]
    NoSquashNids: NotRequired[List[str]]

class LustreRootSquashConfigurationTypeDef(TypedDict):
    RootSquash: NotRequired[str]
    NoSquashNids: NotRequired[Sequence[str]]

class OpenZFSClientConfigurationOutputTypeDef(TypedDict):
    Clients: str
    Options: List[str]

class OpenZFSClientConfigurationTypeDef(TypedDict):
    Clients: str
    Options: Sequence[str]

class OpenZFSOriginSnapshotConfigurationTypeDef(TypedDict):
    SnapshotARN: NotRequired[str]
    CopyStrategy: NotRequired[OpenZFSCopyStrategyType]

class ReleaseFileSystemNfsV3LocksRequestTypeDef(TypedDict):
    FileSystemId: str
    ClientRequestToken: NotRequired[str]

class RestoreVolumeFromSnapshotRequestTypeDef(TypedDict):
    VolumeId: str
    SnapshotId: str
    ClientRequestToken: NotRequired[str]
    Options: NotRequired[Sequence[RestoreOpenZFSVolumeOptionType]]

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "Type": RetentionPeriodTypeType,
        "Value": NotRequired[int],
    },
)

class SelfManagedActiveDirectoryAttributesTypeDef(TypedDict):
    DomainName: NotRequired[str]
    OrganizationalUnitDistinguishedName: NotRequired[str]
    FileSystemAdministratorsGroup: NotRequired[str]
    UserName: NotRequired[str]
    DnsIps: NotRequired[List[str]]

class SelfManagedActiveDirectoryConfigurationUpdatesTypeDef(TypedDict):
    UserName: NotRequired[str]
    Password: NotRequired[str]
    DnsIps: NotRequired[Sequence[str]]
    DomainName: NotRequired[str]
    OrganizationalUnitDistinguishedName: NotRequired[str]
    FileSystemAdministratorsGroup: NotRequired[str]

class StartMisconfiguredStateRecoveryRequestTypeDef(TypedDict):
    FileSystemId: str
    ClientRequestToken: NotRequired[str]

class SvmEndpointTypeDef(TypedDict):
    DNSName: NotRequired[str]
    IpAddresses: NotRequired[List[str]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateFileCacheLustreConfigurationTypeDef(TypedDict):
    WeeklyMaintenanceStartTime: NotRequired[str]

class UpdateFileSystemLustreMetadataConfigurationTypeDef(TypedDict):
    Iops: NotRequired[int]
    Mode: NotRequired[MetadataConfigurationModeType]

class UpdateSharedVpcConfigurationRequestTypeDef(TypedDict):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: NotRequired[str]
    ClientRequestToken: NotRequired[str]

class UpdateSnapshotRequestTypeDef(TypedDict):
    Name: str
    SnapshotId: str
    ClientRequestToken: NotRequired[str]

class WindowsAuditLogConfigurationTypeDef(TypedDict):
    FileAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    FileShareAccessAuditLogLevel: WindowsAccessAuditLogLevelType
    AuditLogDestination: NotRequired[str]

class AssociateFileSystemAliasesResponseTypeDef(TypedDict):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDataRepositoryTaskResponseTypeDef(TypedDict):
    Lifecycle: DataRepositoryTaskLifecycleType
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupResponseTypeDef(TypedDict):
    BackupId: str
    Lifecycle: BackupLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataRepositoryAssociationResponseTypeDef(TypedDict):
    AssociationId: str
    Lifecycle: DataRepositoryLifecycleType
    DeleteDataInFileSystem: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFileCacheResponseTypeDef(TypedDict):
    FileCacheId: str
    Lifecycle: FileCacheLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(TypedDict):
    SnapshotId: str
    Lifecycle: SnapshotLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStorageVirtualMachineResponseTypeDef(TypedDict):
    StorageVirtualMachineId: str
    Lifecycle: StorageVirtualMachineLifecycleType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileSystemAliasesResponseTypeDef(TypedDict):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSharedVpcConfigurationResponseTypeDef(TypedDict):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFileSystemAliasesResponseTypeDef(TypedDict):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSharedVpcConfigurationResponseTypeDef(TypedDict):
    EnableFsxRouteTableUpdatesFromParticipantAccounts: str
    ResponseMetadata: ResponseMetadataTypeDef

class NFSDataRepositoryConfigurationTypeDef(TypedDict):
    Version: Literal["NFS3"]
    DnsIps: NotRequired[List[str]]
    AutoExportPolicy: NotRequired[AutoExportPolicyOutputTypeDef]

class S3DataRepositoryConfigurationOutputTypeDef(TypedDict):
    AutoImportPolicy: NotRequired[AutoImportPolicyOutputTypeDef]
    AutoExportPolicy: NotRequired[AutoExportPolicyOutputTypeDef]

class S3DataRepositoryConfigurationTypeDef(TypedDict):
    AutoImportPolicy: NotRequired[AutoImportPolicyTypeDef]
    AutoExportPolicy: NotRequired[AutoExportPolicyTypeDef]

class CopyBackupRequestTypeDef(TypedDict):
    SourceBackupId: str
    ClientRequestToken: NotRequired[str]
    SourceRegion: NotRequired[str]
    KmsKeyId: NotRequired[str]
    CopyTags: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateBackupRequestTypeDef(TypedDict):
    FileSystemId: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    VolumeId: NotRequired[str]

class CreateSnapshotRequestTypeDef(TypedDict):
    Name: str
    VolumeId: str
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DeleteFileSystemLustreConfigurationTypeDef(TypedDict):
    SkipFinalBackup: NotRequired[bool]
    FinalBackupTags: NotRequired[Sequence[TagTypeDef]]

class DeleteFileSystemLustreResponseTypeDef(TypedDict):
    FinalBackupId: NotRequired[str]
    FinalBackupTags: NotRequired[List[TagTypeDef]]

class DeleteFileSystemOpenZFSConfigurationTypeDef(TypedDict):
    SkipFinalBackup: NotRequired[bool]
    FinalBackupTags: NotRequired[Sequence[TagTypeDef]]
    Options: NotRequired[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]]

class DeleteFileSystemOpenZFSResponseTypeDef(TypedDict):
    FinalBackupId: NotRequired[str]
    FinalBackupTags: NotRequired[List[TagTypeDef]]

class DeleteFileSystemWindowsConfigurationTypeDef(TypedDict):
    SkipFinalBackup: NotRequired[bool]
    FinalBackupTags: NotRequired[Sequence[TagTypeDef]]

class DeleteFileSystemWindowsResponseTypeDef(TypedDict):
    FinalBackupId: NotRequired[str]
    FinalBackupTags: NotRequired[List[TagTypeDef]]

class DeleteVolumeOntapConfigurationTypeDef(TypedDict):
    SkipFinalBackup: NotRequired[bool]
    FinalBackupTags: NotRequired[Sequence[TagTypeDef]]
    BypassSnaplockEnterpriseRetention: NotRequired[bool]

class DeleteVolumeOntapResponseTypeDef(TypedDict):
    FinalBackupId: NotRequired[str]
    FinalBackupTags: NotRequired[List[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFileCacheLustreConfigurationTypeDef(TypedDict):
    PerUnitStorageThroughput: int
    DeploymentType: Literal["CACHE_1"]
    MetadataConfiguration: FileCacheLustreMetadataConfigurationTypeDef
    WeeklyMaintenanceStartTime: NotRequired[str]

class CreateFileSystemOntapConfigurationTypeDef(TypedDict):
    DeploymentType: OntapDeploymentTypeType
    AutomaticBackupRetentionDays: NotRequired[int]
    DailyAutomaticBackupStartTime: NotRequired[str]
    EndpointIpAddressRange: NotRequired[str]
    FsxAdminPassword: NotRequired[str]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    PreferredSubnetId: NotRequired[str]
    RouteTableIds: NotRequired[Sequence[str]]
    ThroughputCapacity: NotRequired[int]
    WeeklyMaintenanceStartTime: NotRequired[str]
    HAPairs: NotRequired[int]
    ThroughputCapacityPerHAPair: NotRequired[int]

class UpdateFileSystemOntapConfigurationTypeDef(TypedDict):
    AutomaticBackupRetentionDays: NotRequired[int]
    DailyAutomaticBackupStartTime: NotRequired[str]
    FsxAdminPassword: NotRequired[str]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    ThroughputCapacity: NotRequired[int]
    AddRouteTableIds: NotRequired[Sequence[str]]
    RemoveRouteTableIds: NotRequired[Sequence[str]]
    ThroughputCapacityPerHAPair: NotRequired[int]
    HAPairs: NotRequired[int]

class OpenZFSFileSystemConfigurationTypeDef(TypedDict):
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    CopyTagsToVolumes: NotRequired[bool]
    DailyAutomaticBackupStartTime: NotRequired[str]
    DeploymentType: NotRequired[OpenZFSDeploymentTypeType]
    ThroughputCapacity: NotRequired[int]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    RootVolumeId: NotRequired[str]
    PreferredSubnetId: NotRequired[str]
    EndpointIpAddressRange: NotRequired[str]
    RouteTableIds: NotRequired[List[str]]
    EndpointIpAddress: NotRequired[str]
    ReadCacheConfiguration: NotRequired[OpenZFSReadCacheConfigurationTypeDef]

class UpdateFileSystemOpenZFSConfigurationTypeDef(TypedDict):
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    CopyTagsToVolumes: NotRequired[bool]
    DailyAutomaticBackupStartTime: NotRequired[str]
    ThroughputCapacity: NotRequired[int]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    AddRouteTableIds: NotRequired[Sequence[str]]
    RemoveRouteTableIds: NotRequired[Sequence[str]]
    ReadCacheConfiguration: NotRequired[OpenZFSReadCacheConfigurationTypeDef]

class CreateSvmActiveDirectoryConfigurationTypeDef(TypedDict):
    NetBiosName: str
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryConfigurationTypeDef
    ]

class CreateFileSystemWindowsConfigurationTypeDef(TypedDict):
    ThroughputCapacity: int
    ActiveDirectoryId: NotRequired[str]
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryConfigurationTypeDef
    ]
    DeploymentType: NotRequired[WindowsDeploymentTypeType]
    PreferredSubnetId: NotRequired[str]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    Aliases: NotRequired[Sequence[str]]
    AuditLogConfiguration: NotRequired[WindowsAuditLogCreateConfigurationTypeDef]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]

class DataRepositoryConfigurationTypeDef(TypedDict):
    Lifecycle: NotRequired[DataRepositoryLifecycleType]
    ImportPath: NotRequired[str]
    ExportPath: NotRequired[str]
    ImportedFileChunkSize: NotRequired[int]
    AutoImportPolicy: NotRequired[AutoImportPolicyTypeType]
    FailureDetails: NotRequired[DataRepositoryFailureDetailsTypeDef]

class DescribeDataRepositoryTasksRequestTypeDef(TypedDict):
    TaskIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[DataRepositoryTaskFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBackupsRequestTypeDef(TypedDict):
    BackupIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeDataRepositoryAssociationsRequestTypeDef(TypedDict):
    AssociationIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBackupsRequestPaginateTypeDef(TypedDict):
    BackupIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeFileSystemsRequestPaginateTypeDef(TypedDict):
    FileSystemIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSnapshotsRequestTypeDef(TypedDict):
    SnapshotIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[SnapshotFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    IncludeShared: NotRequired[bool]

class DescribeStorageVirtualMachinesRequestPaginateTypeDef(TypedDict):
    StorageVirtualMachineIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[StorageVirtualMachineFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStorageVirtualMachinesRequestTypeDef(TypedDict):
    StorageVirtualMachineIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[StorageVirtualMachineFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeVolumesRequestPaginateTypeDef(TypedDict):
    VolumeIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[VolumeFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeVolumesRequestTypeDef(TypedDict):
    VolumeIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[VolumeFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ReleaseConfigurationTypeDef(TypedDict):
    DurationSinceLastAccess: NotRequired[DurationSinceLastAccessTypeDef]

class FileCacheDataRepositoryAssociationTypeDef(TypedDict):
    FileCachePath: str
    DataRepositoryPath: str
    DataRepositorySubdirectories: NotRequired[Sequence[str]]
    NFS: NotRequired[FileCacheNFSConfigurationTypeDef]

class FileCacheLustreConfigurationTypeDef(TypedDict):
    PerUnitStorageThroughput: NotRequired[int]
    DeploymentType: NotRequired[Literal["CACHE_1"]]
    MountName: NotRequired[str]
    WeeklyMaintenanceStartTime: NotRequired[str]
    MetadataConfiguration: NotRequired[FileCacheLustreMetadataConfigurationTypeDef]
    LogConfiguration: NotRequired[LustreLogConfigurationTypeDef]

class FileSystemEndpointsTypeDef(TypedDict):
    Intercluster: NotRequired[FileSystemEndpointTypeDef]
    Management: NotRequired[FileSystemEndpointTypeDef]

class SnapshotPaginatorTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    SnapshotId: NotRequired[str]
    Name: NotRequired[str]
    VolumeId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Lifecycle: NotRequired[SnapshotLifecycleType]
    LifecycleTransitionReason: NotRequired[LifecycleTransitionReasonTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    AdministrativeActions: NotRequired[List[Dict[str, Any]]]

class SnapshotTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    SnapshotId: NotRequired[str]
    Name: NotRequired[str]
    VolumeId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Lifecycle: NotRequired[SnapshotLifecycleType]
    LifecycleTransitionReason: NotRequired[LifecycleTransitionReasonTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    AdministrativeActions: NotRequired[List[Dict[str, Any]]]

LustreRootSquashConfigurationUnionTypeDef = Union[
    LustreRootSquashConfigurationTypeDef, LustreRootSquashConfigurationOutputTypeDef
]

class OpenZFSNfsExportOutputTypeDef(TypedDict):
    ClientConfigurations: List[OpenZFSClientConfigurationOutputTypeDef]

OpenZFSClientConfigurationUnionTypeDef = Union[
    OpenZFSClientConfigurationTypeDef, OpenZFSClientConfigurationOutputTypeDef
]

class SnaplockRetentionPeriodTypeDef(TypedDict):
    DefaultRetention: RetentionPeriodTypeDef
    MinimumRetention: RetentionPeriodTypeDef
    MaximumRetention: RetentionPeriodTypeDef

class SvmActiveDirectoryConfigurationTypeDef(TypedDict):
    NetBiosName: NotRequired[str]
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryAttributesTypeDef
    ]

class UpdateFileSystemWindowsConfigurationTypeDef(TypedDict):
    WeeklyMaintenanceStartTime: NotRequired[str]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    ThroughputCapacity: NotRequired[int]
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryConfigurationUpdatesTypeDef
    ]
    AuditLogConfiguration: NotRequired[WindowsAuditLogCreateConfigurationTypeDef]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]

class UpdateSvmActiveDirectoryConfigurationTypeDef(TypedDict):
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryConfigurationUpdatesTypeDef
    ]
    NetBiosName: NotRequired[str]

class SvmEndpointsTypeDef(TypedDict):
    Iscsi: NotRequired[SvmEndpointTypeDef]
    Management: NotRequired[SvmEndpointTypeDef]
    Nfs: NotRequired[SvmEndpointTypeDef]
    Smb: NotRequired[SvmEndpointTypeDef]

class UpdateFileCacheRequestTypeDef(TypedDict):
    FileCacheId: str
    ClientRequestToken: NotRequired[str]
    LustreConfiguration: NotRequired[UpdateFileCacheLustreConfigurationTypeDef]

class WindowsFileSystemConfigurationTypeDef(TypedDict):
    ActiveDirectoryId: NotRequired[str]
    SelfManagedActiveDirectoryConfiguration: NotRequired[
        SelfManagedActiveDirectoryAttributesTypeDef
    ]
    DeploymentType: NotRequired[WindowsDeploymentTypeType]
    RemoteAdministrationEndpoint: NotRequired[str]
    PreferredSubnetId: NotRequired[str]
    PreferredFileServerIp: NotRequired[str]
    ThroughputCapacity: NotRequired[int]
    MaintenanceOperationsInProgress: NotRequired[List[FileSystemMaintenanceOperationType]]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    Aliases: NotRequired[List[AliasTypeDef]]
    AuditLogConfiguration: NotRequired[WindowsAuditLogConfigurationTypeDef]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]

class DataRepositoryAssociationTypeDef(TypedDict):
    AssociationId: NotRequired[str]
    ResourceARN: NotRequired[str]
    FileSystemId: NotRequired[str]
    Lifecycle: NotRequired[DataRepositoryLifecycleType]
    FailureDetails: NotRequired[DataRepositoryFailureDetailsTypeDef]
    FileSystemPath: NotRequired[str]
    DataRepositoryPath: NotRequired[str]
    BatchImportMetaDataOnCreate: NotRequired[bool]
    ImportedFileChunkSize: NotRequired[int]
    S3: NotRequired[S3DataRepositoryConfigurationOutputTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    CreationTime: NotRequired[datetime]
    FileCacheId: NotRequired[str]
    FileCachePath: NotRequired[str]
    DataRepositorySubdirectories: NotRequired[List[str]]
    NFS: NotRequired[NFSDataRepositoryConfigurationTypeDef]

S3DataRepositoryConfigurationUnionTypeDef = Union[
    S3DataRepositoryConfigurationTypeDef, S3DataRepositoryConfigurationOutputTypeDef
]

class DeleteFileSystemRequestTypeDef(TypedDict):
    FileSystemId: str
    ClientRequestToken: NotRequired[str]
    WindowsConfiguration: NotRequired[DeleteFileSystemWindowsConfigurationTypeDef]
    LustreConfiguration: NotRequired[DeleteFileSystemLustreConfigurationTypeDef]
    OpenZFSConfiguration: NotRequired[DeleteFileSystemOpenZFSConfigurationTypeDef]

class DeleteFileSystemResponseTypeDef(TypedDict):
    FileSystemId: str
    Lifecycle: FileSystemLifecycleType
    WindowsResponse: DeleteFileSystemWindowsResponseTypeDef
    LustreResponse: DeleteFileSystemLustreResponseTypeDef
    OpenZFSResponse: DeleteFileSystemOpenZFSResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVolumeRequestTypeDef(TypedDict):
    VolumeId: str
    ClientRequestToken: NotRequired[str]
    OntapConfiguration: NotRequired[DeleteVolumeOntapConfigurationTypeDef]
    OpenZFSConfiguration: NotRequired[DeleteVolumeOpenZFSConfigurationTypeDef]

class DeleteVolumeResponseTypeDef(TypedDict):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    OntapResponse: DeleteVolumeOntapResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageVirtualMachineRequestTypeDef(TypedDict):
    FileSystemId: str
    Name: str
    ActiveDirectoryConfiguration: NotRequired[CreateSvmActiveDirectoryConfigurationTypeDef]
    ClientRequestToken: NotRequired[str]
    SvmAdminPassword: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    RootVolumeSecurityStyle: NotRequired[StorageVirtualMachineRootVolumeSecurityStyleType]

class LustreFileSystemConfigurationTypeDef(TypedDict):
    WeeklyMaintenanceStartTime: NotRequired[str]
    DataRepositoryConfiguration: NotRequired[DataRepositoryConfigurationTypeDef]
    DeploymentType: NotRequired[LustreDeploymentTypeType]
    PerUnitStorageThroughput: NotRequired[int]
    MountName: NotRequired[str]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    DriveCacheType: NotRequired[DriveCacheTypeType]
    DataCompressionType: NotRequired[DataCompressionTypeType]
    LogConfiguration: NotRequired[LustreLogConfigurationTypeDef]
    RootSquashConfiguration: NotRequired[LustreRootSquashConfigurationOutputTypeDef]
    MetadataConfiguration: NotRequired[FileSystemLustreMetadataConfigurationTypeDef]
    EfaEnabled: NotRequired[bool]

CreateDataRepositoryTaskRequestTypeDef = TypedDict(
    "CreateDataRepositoryTaskRequestTypeDef",
    {
        "Type": DataRepositoryTaskTypeType,
        "FileSystemId": str,
        "Report": CompletionReportTypeDef,
        "Paths": NotRequired[Sequence[str]],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CapacityToRelease": NotRequired[int],
        "ReleaseConfiguration": NotRequired[ReleaseConfigurationTypeDef],
    },
)
DataRepositoryTaskTypeDef = TypedDict(
    "DataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": DataRepositoryTaskTypeType,
        "CreationTime": datetime,
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "FileSystemId": NotRequired[str],
        "Paths": NotRequired[List[str]],
        "FailureDetails": NotRequired[DataRepositoryTaskFailureDetailsTypeDef],
        "Status": NotRequired[DataRepositoryTaskStatusTypeDef],
        "Report": NotRequired[CompletionReportTypeDef],
        "CapacityToRelease": NotRequired[int],
        "FileCacheId": NotRequired[str],
        "ReleaseConfiguration": NotRequired[ReleaseConfigurationTypeDef],
    },
)

class CreateFileCacheRequestTypeDef(TypedDict):
    FileCacheType: Literal["LUSTRE"]
    FileCacheTypeVersion: str
    StorageCapacity: int
    SubnetIds: Sequence[str]
    ClientRequestToken: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    CopyTagsToDataRepositoryAssociations: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    LustreConfiguration: NotRequired[CreateFileCacheLustreConfigurationTypeDef]
    DataRepositoryAssociations: NotRequired[Sequence[FileCacheDataRepositoryAssociationTypeDef]]

class FileCacheCreatingTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    FileCacheId: NotRequired[str]
    FileCacheType: NotRequired[Literal["LUSTRE"]]
    FileCacheTypeVersion: NotRequired[str]
    Lifecycle: NotRequired[FileCacheLifecycleType]
    FailureDetails: NotRequired[FileCacheFailureDetailsTypeDef]
    StorageCapacity: NotRequired[int]
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    NetworkInterfaceIds: NotRequired[List[str]]
    DNSName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    CopyTagsToDataRepositoryAssociations: NotRequired[bool]
    LustreConfiguration: NotRequired[FileCacheLustreConfigurationTypeDef]
    DataRepositoryAssociationIds: NotRequired[List[str]]

class FileCacheTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    FileCacheId: NotRequired[str]
    FileCacheType: NotRequired[Literal["LUSTRE"]]
    FileCacheTypeVersion: NotRequired[str]
    Lifecycle: NotRequired[FileCacheLifecycleType]
    FailureDetails: NotRequired[FileCacheFailureDetailsTypeDef]
    StorageCapacity: NotRequired[int]
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    NetworkInterfaceIds: NotRequired[List[str]]
    DNSName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    ResourceARN: NotRequired[str]
    LustreConfiguration: NotRequired[FileCacheLustreConfigurationTypeDef]
    DataRepositoryAssociationIds: NotRequired[List[str]]

class OntapFileSystemConfigurationTypeDef(TypedDict):
    AutomaticBackupRetentionDays: NotRequired[int]
    DailyAutomaticBackupStartTime: NotRequired[str]
    DeploymentType: NotRequired[OntapDeploymentTypeType]
    EndpointIpAddressRange: NotRequired[str]
    Endpoints: NotRequired[FileSystemEndpointsTypeDef]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    PreferredSubnetId: NotRequired[str]
    RouteTableIds: NotRequired[List[str]]
    ThroughputCapacity: NotRequired[int]
    WeeklyMaintenanceStartTime: NotRequired[str]
    FsxAdminPassword: NotRequired[str]
    HAPairs: NotRequired[int]
    ThroughputCapacityPerHAPair: NotRequired[int]

class CreateSnapshotResponseTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsResponseTypeDef(TypedDict):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSnapshotResponseTypeDef(TypedDict):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemLustreConfigurationTypeDef(TypedDict):
    WeeklyMaintenanceStartTime: NotRequired[str]
    ImportPath: NotRequired[str]
    ExportPath: NotRequired[str]
    ImportedFileChunkSize: NotRequired[int]
    DeploymentType: NotRequired[LustreDeploymentTypeType]
    AutoImportPolicy: NotRequired[AutoImportPolicyTypeType]
    PerUnitStorageThroughput: NotRequired[int]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    DriveCacheType: NotRequired[DriveCacheTypeType]
    DataCompressionType: NotRequired[DataCompressionTypeType]
    EfaEnabled: NotRequired[bool]
    LogConfiguration: NotRequired[LustreLogCreateConfigurationTypeDef]
    RootSquashConfiguration: NotRequired[LustreRootSquashConfigurationUnionTypeDef]
    MetadataConfiguration: NotRequired[CreateFileSystemLustreMetadataConfigurationTypeDef]

class UpdateFileSystemLustreConfigurationTypeDef(TypedDict):
    WeeklyMaintenanceStartTime: NotRequired[str]
    DailyAutomaticBackupStartTime: NotRequired[str]
    AutomaticBackupRetentionDays: NotRequired[int]
    AutoImportPolicy: NotRequired[AutoImportPolicyTypeType]
    DataCompressionType: NotRequired[DataCompressionTypeType]
    LogConfiguration: NotRequired[LustreLogCreateConfigurationTypeDef]
    RootSquashConfiguration: NotRequired[LustreRootSquashConfigurationUnionTypeDef]
    PerUnitStorageThroughput: NotRequired[int]
    MetadataConfiguration: NotRequired[UpdateFileSystemLustreMetadataConfigurationTypeDef]

OpenZFSVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": NotRequired[str],
        "VolumePath": NotRequired[str],
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "CopyTagsToSnapshots": NotRequired[bool],
        "OriginSnapshot": NotRequired[OpenZFSOriginSnapshotConfigurationTypeDef],
        "ReadOnly": NotRequired[bool],
        "NfsExports": NotRequired[List[OpenZFSNfsExportOutputTypeDef]],
        "UserAndGroupQuotas": NotRequired[List[OpenZFSUserOrGroupQuotaTypeDef]],
        "RestoreToSnapshot": NotRequired[str],
        "DeleteIntermediateSnaphots": NotRequired[bool],
        "DeleteClonedVolumes": NotRequired[bool],
        "DeleteIntermediateData": NotRequired[bool],
        "SourceSnapshotARN": NotRequired[str],
        "DestinationSnapshot": NotRequired[str],
        "CopyStrategy": NotRequired[OpenZFSCopyStrategyType],
    },
)

class OpenZFSNfsExportTypeDef(TypedDict):
    ClientConfigurations: Sequence[OpenZFSClientConfigurationUnionTypeDef]

class CreateSnaplockConfigurationTypeDef(TypedDict):
    SnaplockType: SnaplockTypeType
    AuditLogVolume: NotRequired[bool]
    AutocommitPeriod: NotRequired[AutocommitPeriodTypeDef]
    PrivilegedDelete: NotRequired[PrivilegedDeleteType]
    RetentionPeriod: NotRequired[SnaplockRetentionPeriodTypeDef]
    VolumeAppendModeEnabled: NotRequired[bool]

class SnaplockConfigurationTypeDef(TypedDict):
    AuditLogVolume: NotRequired[bool]
    AutocommitPeriod: NotRequired[AutocommitPeriodTypeDef]
    PrivilegedDelete: NotRequired[PrivilegedDeleteType]
    RetentionPeriod: NotRequired[SnaplockRetentionPeriodTypeDef]
    SnaplockType: NotRequired[SnaplockTypeType]
    VolumeAppendModeEnabled: NotRequired[bool]

class UpdateSnaplockConfigurationTypeDef(TypedDict):
    AuditLogVolume: NotRequired[bool]
    AutocommitPeriod: NotRequired[AutocommitPeriodTypeDef]
    PrivilegedDelete: NotRequired[PrivilegedDeleteType]
    RetentionPeriod: NotRequired[SnaplockRetentionPeriodTypeDef]
    VolumeAppendModeEnabled: NotRequired[bool]

class UpdateStorageVirtualMachineRequestTypeDef(TypedDict):
    StorageVirtualMachineId: str
    ActiveDirectoryConfiguration: NotRequired[UpdateSvmActiveDirectoryConfigurationTypeDef]
    ClientRequestToken: NotRequired[str]
    SvmAdminPassword: NotRequired[str]

class StorageVirtualMachineTypeDef(TypedDict):
    ActiveDirectoryConfiguration: NotRequired[SvmActiveDirectoryConfigurationTypeDef]
    CreationTime: NotRequired[datetime]
    Endpoints: NotRequired[SvmEndpointsTypeDef]
    FileSystemId: NotRequired[str]
    Lifecycle: NotRequired[StorageVirtualMachineLifecycleType]
    Name: NotRequired[str]
    ResourceARN: NotRequired[str]
    StorageVirtualMachineId: NotRequired[str]
    Subtype: NotRequired[StorageVirtualMachineSubtypeType]
    UUID: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    LifecycleTransitionReason: NotRequired[LifecycleTransitionReasonTypeDef]
    RootVolumeSecurityStyle: NotRequired[StorageVirtualMachineRootVolumeSecurityStyleType]

class CreateDataRepositoryAssociationResponseTypeDef(TypedDict):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataRepositoryAssociationsResponseTypeDef(TypedDict):
    Associations: List[DataRepositoryAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateDataRepositoryAssociationResponseTypeDef(TypedDict):
    Association: DataRepositoryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataRepositoryAssociationRequestTypeDef(TypedDict):
    FileSystemId: str
    DataRepositoryPath: str
    FileSystemPath: NotRequired[str]
    BatchImportMetaDataOnCreate: NotRequired[bool]
    ImportedFileChunkSize: NotRequired[int]
    S3: NotRequired[S3DataRepositoryConfigurationUnionTypeDef]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateDataRepositoryAssociationRequestTypeDef(TypedDict):
    AssociationId: str
    ClientRequestToken: NotRequired[str]
    ImportedFileChunkSize: NotRequired[int]
    S3: NotRequired[S3DataRepositoryConfigurationUnionTypeDef]

class CreateDataRepositoryTaskResponseTypeDef(TypedDict):
    DataRepositoryTask: DataRepositoryTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataRepositoryTasksResponseTypeDef(TypedDict):
    DataRepositoryTasks: List[DataRepositoryTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateFileCacheResponseTypeDef(TypedDict):
    FileCache: FileCacheCreatingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileCachesResponseTypeDef(TypedDict):
    FileCaches: List[FileCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateFileCacheResponseTypeDef(TypedDict):
    FileCache: FileCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFileSystemRequestTypeDef(TypedDict):
    FileSystemId: str
    ClientRequestToken: NotRequired[str]
    StorageCapacity: NotRequired[int]
    WindowsConfiguration: NotRequired[UpdateFileSystemWindowsConfigurationTypeDef]
    LustreConfiguration: NotRequired[UpdateFileSystemLustreConfigurationTypeDef]
    OntapConfiguration: NotRequired[UpdateFileSystemOntapConfigurationTypeDef]
    OpenZFSConfiguration: NotRequired[UpdateFileSystemOpenZFSConfigurationTypeDef]
    StorageType: NotRequired[StorageTypeType]
    FileSystemTypeVersion: NotRequired[str]

OpenZFSNfsExportUnionTypeDef = Union[OpenZFSNfsExportTypeDef, OpenZFSNfsExportOutputTypeDef]

class CreateOntapVolumeConfigurationTypeDef(TypedDict):
    StorageVirtualMachineId: str
    JunctionPath: NotRequired[str]
    SecurityStyle: NotRequired[SecurityStyleType]
    SizeInMegabytes: NotRequired[int]
    StorageEfficiencyEnabled: NotRequired[bool]
    TieringPolicy: NotRequired[TieringPolicyTypeDef]
    OntapVolumeType: NotRequired[InputOntapVolumeTypeType]
    SnapshotPolicy: NotRequired[str]
    CopyTagsToBackups: NotRequired[bool]
    SnaplockConfiguration: NotRequired[CreateSnaplockConfigurationTypeDef]
    VolumeStyle: NotRequired[VolumeStyleType]
    AggregateConfiguration: NotRequired[CreateAggregateConfigurationTypeDef]
    SizeInBytes: NotRequired[int]

class OntapVolumeConfigurationTypeDef(TypedDict):
    FlexCacheEndpointType: NotRequired[FlexCacheEndpointTypeType]
    JunctionPath: NotRequired[str]
    SecurityStyle: NotRequired[SecurityStyleType]
    SizeInMegabytes: NotRequired[int]
    StorageEfficiencyEnabled: NotRequired[bool]
    StorageVirtualMachineId: NotRequired[str]
    StorageVirtualMachineRoot: NotRequired[bool]
    TieringPolicy: NotRequired[TieringPolicyTypeDef]
    UUID: NotRequired[str]
    OntapVolumeType: NotRequired[OntapVolumeTypeType]
    SnapshotPolicy: NotRequired[str]
    CopyTagsToBackups: NotRequired[bool]
    SnaplockConfiguration: NotRequired[SnaplockConfigurationTypeDef]
    VolumeStyle: NotRequired[VolumeStyleType]
    AggregateConfiguration: NotRequired[AggregateConfigurationTypeDef]
    SizeInBytes: NotRequired[int]

class UpdateOntapVolumeConfigurationTypeDef(TypedDict):
    JunctionPath: NotRequired[str]
    SecurityStyle: NotRequired[SecurityStyleType]
    SizeInMegabytes: NotRequired[int]
    StorageEfficiencyEnabled: NotRequired[bool]
    TieringPolicy: NotRequired[TieringPolicyTypeDef]
    SnapshotPolicy: NotRequired[str]
    CopyTagsToBackups: NotRequired[bool]
    SnaplockConfiguration: NotRequired[UpdateSnaplockConfigurationTypeDef]
    SizeInBytes: NotRequired[int]

class CreateStorageVirtualMachineResponseTypeDef(TypedDict):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorageVirtualMachinesResponseTypeDef(TypedDict):
    StorageVirtualMachines: List[StorageVirtualMachineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateStorageVirtualMachineResponseTypeDef(TypedDict):
    StorageVirtualMachine: StorageVirtualMachineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "CreateOpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": str,
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "CopyTagsToSnapshots": NotRequired[bool],
        "OriginSnapshot": NotRequired[CreateOpenZFSOriginSnapshotConfigurationTypeDef],
        "ReadOnly": NotRequired[bool],
        "NfsExports": NotRequired[Sequence[OpenZFSNfsExportUnionTypeDef]],
        "UserAndGroupQuotas": NotRequired[Sequence[OpenZFSUserOrGroupQuotaTypeDef]],
    },
)
OpenZFSCreateRootVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    {
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "NfsExports": NotRequired[Sequence[OpenZFSNfsExportUnionTypeDef]],
        "UserAndGroupQuotas": NotRequired[Sequence[OpenZFSUserOrGroupQuotaTypeDef]],
        "CopyTagsToSnapshots": NotRequired[bool],
        "ReadOnly": NotRequired[bool],
    },
)
UpdateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    {
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "NfsExports": NotRequired[Sequence[OpenZFSNfsExportUnionTypeDef]],
        "UserAndGroupQuotas": NotRequired[Sequence[OpenZFSUserOrGroupQuotaTypeDef]],
        "ReadOnly": NotRequired[bool],
    },
)

class CreateVolumeFromBackupRequestTypeDef(TypedDict):
    BackupId: str
    Name: str
    ClientRequestToken: NotRequired[str]
    OntapConfiguration: NotRequired[CreateOntapVolumeConfigurationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class VolumePaginatorTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    FileSystemId: NotRequired[str]
    Lifecycle: NotRequired[VolumeLifecycleType]
    Name: NotRequired[str]
    OntapConfiguration: NotRequired[OntapVolumeConfigurationTypeDef]
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[VolumeTypeType]
    LifecycleTransitionReason: NotRequired[LifecycleTransitionReasonTypeDef]
    AdministrativeActions: NotRequired[List[Dict[str, Any]]]
    OpenZFSConfiguration: NotRequired[OpenZFSVolumeConfigurationTypeDef]

class VolumeTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    FileSystemId: NotRequired[str]
    Lifecycle: NotRequired[VolumeLifecycleType]
    Name: NotRequired[str]
    OntapConfiguration: NotRequired[OntapVolumeConfigurationTypeDef]
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[VolumeTypeType]
    LifecycleTransitionReason: NotRequired[LifecycleTransitionReasonTypeDef]
    AdministrativeActions: NotRequired[List[Dict[str, Any]]]
    OpenZFSConfiguration: NotRequired[OpenZFSVolumeConfigurationTypeDef]

class CreateVolumeRequestTypeDef(TypedDict):
    VolumeType: VolumeTypeType
    Name: str
    ClientRequestToken: NotRequired[str]
    OntapConfiguration: NotRequired[CreateOntapVolumeConfigurationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    OpenZFSConfiguration: NotRequired[CreateOpenZFSVolumeConfigurationTypeDef]

class CreateFileSystemOpenZFSConfigurationTypeDef(TypedDict):
    DeploymentType: OpenZFSDeploymentTypeType
    ThroughputCapacity: int
    AutomaticBackupRetentionDays: NotRequired[int]
    CopyTagsToBackups: NotRequired[bool]
    CopyTagsToVolumes: NotRequired[bool]
    DailyAutomaticBackupStartTime: NotRequired[str]
    WeeklyMaintenanceStartTime: NotRequired[str]
    DiskIopsConfiguration: NotRequired[DiskIopsConfigurationTypeDef]
    RootVolumeConfiguration: NotRequired[OpenZFSCreateRootVolumeConfigurationTypeDef]
    PreferredSubnetId: NotRequired[str]
    EndpointIpAddressRange: NotRequired[str]
    RouteTableIds: NotRequired[Sequence[str]]
    ReadCacheConfiguration: NotRequired[OpenZFSReadCacheConfigurationTypeDef]

class UpdateVolumeRequestTypeDef(TypedDict):
    VolumeId: str
    ClientRequestToken: NotRequired[str]
    OntapConfiguration: NotRequired[UpdateOntapVolumeConfigurationTypeDef]
    Name: NotRequired[str]
    OpenZFSConfiguration: NotRequired[UpdateOpenZFSVolumeConfigurationTypeDef]

class AdministrativeActionPaginatorTypeDef(TypedDict):
    AdministrativeActionType: NotRequired[AdministrativeActionTypeType]
    ProgressPercent: NotRequired[int]
    RequestTime: NotRequired[datetime]
    Status: NotRequired[StatusType]
    TargetFileSystemValues: NotRequired[Dict[str, Any]]
    FailureDetails: NotRequired[AdministrativeActionFailureDetailsTypeDef]
    TargetVolumeValues: NotRequired[VolumePaginatorTypeDef]
    TargetSnapshotValues: NotRequired[SnapshotPaginatorTypeDef]
    TotalTransferBytes: NotRequired[int]
    RemainingTransferBytes: NotRequired[int]

class DescribeVolumesResponsePaginatorTypeDef(TypedDict):
    Volumes: List[VolumePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AdministrativeActionTypeDef(TypedDict):
    AdministrativeActionType: NotRequired[AdministrativeActionTypeType]
    ProgressPercent: NotRequired[int]
    RequestTime: NotRequired[datetime]
    Status: NotRequired[StatusType]
    TargetFileSystemValues: NotRequired[Dict[str, Any]]
    FailureDetails: NotRequired[AdministrativeActionFailureDetailsTypeDef]
    TargetVolumeValues: NotRequired[VolumeTypeDef]
    TargetSnapshotValues: NotRequired[SnapshotTypeDef]
    TotalTransferBytes: NotRequired[int]
    RemainingTransferBytes: NotRequired[int]

class CreateVolumeFromBackupResponseTypeDef(TypedDict):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVolumeResponseTypeDef(TypedDict):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumesResponseTypeDef(TypedDict):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateVolumeResponseTypeDef(TypedDict):
    Volume: VolumeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemFromBackupRequestTypeDef(TypedDict):
    BackupId: str
    SubnetIds: Sequence[str]
    ClientRequestToken: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    WindowsConfiguration: NotRequired[CreateFileSystemWindowsConfigurationTypeDef]
    LustreConfiguration: NotRequired[CreateFileSystemLustreConfigurationTypeDef]
    StorageType: NotRequired[StorageTypeType]
    KmsKeyId: NotRequired[str]
    FileSystemTypeVersion: NotRequired[str]
    OpenZFSConfiguration: NotRequired[CreateFileSystemOpenZFSConfigurationTypeDef]
    StorageCapacity: NotRequired[int]

class CreateFileSystemRequestTypeDef(TypedDict):
    FileSystemType: FileSystemTypeType
    SubnetIds: Sequence[str]
    ClientRequestToken: NotRequired[str]
    StorageCapacity: NotRequired[int]
    StorageType: NotRequired[StorageTypeType]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    WindowsConfiguration: NotRequired[CreateFileSystemWindowsConfigurationTypeDef]
    LustreConfiguration: NotRequired[CreateFileSystemLustreConfigurationTypeDef]
    OntapConfiguration: NotRequired[CreateFileSystemOntapConfigurationTypeDef]
    FileSystemTypeVersion: NotRequired[str]
    OpenZFSConfiguration: NotRequired[CreateFileSystemOpenZFSConfigurationTypeDef]

class FileSystemPaginatorTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    FileSystemId: NotRequired[str]
    FileSystemType: NotRequired[FileSystemTypeType]
    Lifecycle: NotRequired[FileSystemLifecycleType]
    FailureDetails: NotRequired[FileSystemFailureDetailsTypeDef]
    StorageCapacity: NotRequired[int]
    StorageType: NotRequired[StorageTypeType]
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    NetworkInterfaceIds: NotRequired[List[str]]
    DNSName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    WindowsConfiguration: NotRequired[WindowsFileSystemConfigurationTypeDef]
    LustreConfiguration: NotRequired[LustreFileSystemConfigurationTypeDef]
    AdministrativeActions: NotRequired[List[AdministrativeActionPaginatorTypeDef]]
    OntapConfiguration: NotRequired[OntapFileSystemConfigurationTypeDef]
    FileSystemTypeVersion: NotRequired[str]
    OpenZFSConfiguration: NotRequired[OpenZFSFileSystemConfigurationTypeDef]

class CopySnapshotAndUpdateVolumeResponseTypeDef(TypedDict):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    FileSystemId: NotRequired[str]
    FileSystemType: NotRequired[FileSystemTypeType]
    Lifecycle: NotRequired[FileSystemLifecycleType]
    FailureDetails: NotRequired[FileSystemFailureDetailsTypeDef]
    StorageCapacity: NotRequired[int]
    StorageType: NotRequired[StorageTypeType]
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    NetworkInterfaceIds: NotRequired[List[str]]
    DNSName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    WindowsConfiguration: NotRequired[WindowsFileSystemConfigurationTypeDef]
    LustreConfiguration: NotRequired[LustreFileSystemConfigurationTypeDef]
    AdministrativeActions: NotRequired[List[AdministrativeActionTypeDef]]
    OntapConfiguration: NotRequired[OntapFileSystemConfigurationTypeDef]
    FileSystemTypeVersion: NotRequired[str]
    OpenZFSConfiguration: NotRequired[OpenZFSFileSystemConfigurationTypeDef]

class RestoreVolumeFromSnapshotResponseTypeDef(TypedDict):
    VolumeId: str
    Lifecycle: VolumeLifecycleType
    AdministrativeActions: List[AdministrativeActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

BackupPaginatorTypeDef = TypedDict(
    "BackupPaginatorTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": FileSystemPaginatorTypeDef,
        "FailureDetails": NotRequired[BackupFailureDetailsTypeDef],
        "ProgressPercent": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "DirectoryInformation": NotRequired[ActiveDirectoryBackupAttributesTypeDef],
        "OwnerId": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "SourceBackupRegion": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "Volume": NotRequired[VolumePaginatorTypeDef],
        "SizeInBytes": NotRequired[int],
    },
)

class DescribeFileSystemsResponsePaginatorTypeDef(TypedDict):
    FileSystems: List[FileSystemPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": FileSystemTypeDef,
        "FailureDetails": NotRequired[BackupFailureDetailsTypeDef],
        "ProgressPercent": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "DirectoryInformation": NotRequired[ActiveDirectoryBackupAttributesTypeDef],
        "OwnerId": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "SourceBackupRegion": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "Volume": NotRequired[VolumeTypeDef],
        "SizeInBytes": NotRequired[int],
    },
)

class CreateFileSystemFromBackupResponseTypeDef(TypedDict):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemResponseTypeDef(TypedDict):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFileSystemsResponseTypeDef(TypedDict):
    FileSystems: List[FileSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ReleaseFileSystemNfsV3LocksResponseTypeDef(TypedDict):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMisconfiguredStateRecoveryResponseTypeDef(TypedDict):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFileSystemResponseTypeDef(TypedDict):
    FileSystem: FileSystemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponsePaginatorTypeDef(TypedDict):
    Backups: List[BackupPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CopyBackupResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(TypedDict):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
