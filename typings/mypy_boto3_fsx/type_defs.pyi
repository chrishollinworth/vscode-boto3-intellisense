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
    DriveCacheTypeType,
    FileSystemLifecycleType,
    FileSystemMaintenanceOperationType,
    FileSystemTypeType,
    FilterNameType,
    LustreDeploymentTypeType,
    StatusType,
    StorageTypeType,
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
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestRequestTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryTaskRequestRequestTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupRequestRequestTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesRequestRequestTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DisassociateFileSystemAliasesRequestRequestTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
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

_RequiredCreateBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBackupRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalCreateBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBackupRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBackupRequestRequestTypeDef(
    _RequiredCreateBackupRequestRequestTypeDef, _OptionalCreateBackupRequestRequestTypeDef
):
    pass

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Type": Literal["EXPORT_TO_REPOSITORY"],
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
    },
    total=False,
)

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
    },
    total=False,
)

_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": Literal["EXPORT_TO_REPOSITORY"],
        "CreationTime": datetime,
        "FileSystemId": str,
    },
)
_OptionalDataRepositoryTaskTypeDef = TypedDict(
    "_OptionalDataRepositoryTaskTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "Paths": List[str],
        "FailureDetails": "DataRepositoryTaskFailureDetailsTypeDef",
        "Status": "DataRepositoryTaskStatusTypeDef",
        "Report": "CompletionReportTypeDef",
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
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
