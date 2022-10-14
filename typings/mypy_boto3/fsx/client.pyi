"""
Type annotations for fsx service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_fsx import FSxClient

    client: FSxClient = boto3.client("fsx")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DataRepositoryTaskTypeType,
    FileSystemTypeType,
    RestoreOpenZFSVolumeOptionType,
    StorageTypeType,
    StorageVirtualMachineRootVolumeSecurityStyleType,
    VolumeTypeType,
)
from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    DescribeStorageVirtualMachinesPaginator,
    DescribeVolumesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFileSystemAliasesResponseTypeDef,
    CancelDataRepositoryTaskResponseTypeDef,
    CompletionReportTypeDef,
    CopyBackupResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateDataRepositoryAssociationResponseTypeDef,
    CreateDataRepositoryTaskResponseTypeDef,
    CreateFileCacheLustreConfigurationTypeDef,
    CreateFileCacheResponseTypeDef,
    CreateFileSystemFromBackupResponseTypeDef,
    CreateFileSystemLustreConfigurationTypeDef,
    CreateFileSystemOntapConfigurationTypeDef,
    CreateFileSystemOpenZFSConfigurationTypeDef,
    CreateFileSystemResponseTypeDef,
    CreateFileSystemWindowsConfigurationTypeDef,
    CreateOntapVolumeConfigurationTypeDef,
    CreateOpenZFSVolumeConfigurationTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateStorageVirtualMachineResponseTypeDef,
    CreateSvmActiveDirectoryConfigurationTypeDef,
    CreateVolumeFromBackupResponseTypeDef,
    CreateVolumeResponseTypeDef,
    DataRepositoryTaskFilterTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteDataRepositoryAssociationResponseTypeDef,
    DeleteFileCacheResponseTypeDef,
    DeleteFileSystemLustreConfigurationTypeDef,
    DeleteFileSystemOpenZFSConfigurationTypeDef,
    DeleteFileSystemResponseTypeDef,
    DeleteFileSystemWindowsConfigurationTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteStorageVirtualMachineResponseTypeDef,
    DeleteVolumeOntapConfigurationTypeDef,
    DeleteVolumeOpenZFSConfigurationTypeDef,
    DeleteVolumeResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeDataRepositoryAssociationsResponseTypeDef,
    DescribeDataRepositoryTasksResponseTypeDef,
    DescribeFileCachesResponseTypeDef,
    DescribeFileSystemAliasesResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeStorageVirtualMachinesResponseTypeDef,
    DescribeVolumesResponseTypeDef,
    DisassociateFileSystemAliasesResponseTypeDef,
    FileCacheDataRepositoryAssociationTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    ReleaseFileSystemNfsV3LocksResponseTypeDef,
    RestoreVolumeFromSnapshotResponseTypeDef,
    S3DataRepositoryConfigurationTypeDef,
    SnapshotFilterTypeDef,
    StorageVirtualMachineFilterTypeDef,
    TagTypeDef,
    UpdateDataRepositoryAssociationResponseTypeDef,
    UpdateFileCacheLustreConfigurationTypeDef,
    UpdateFileCacheResponseTypeDef,
    UpdateFileSystemLustreConfigurationTypeDef,
    UpdateFileSystemOntapConfigurationTypeDef,
    UpdateFileSystemOpenZFSConfigurationTypeDef,
    UpdateFileSystemResponseTypeDef,
    UpdateFileSystemWindowsConfigurationTypeDef,
    UpdateOntapVolumeConfigurationTypeDef,
    UpdateOpenZFSVolumeConfigurationTypeDef,
    UpdateSnapshotResponseTypeDef,
    UpdateStorageVirtualMachineResponseTypeDef,
    UpdateSvmActiveDirectoryConfigurationTypeDef,
    UpdateVolumeResponseTypeDef,
    VolumeFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FSxClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActiveDirectoryError: Type[BotocoreClientError]
    BackupBeingCopied: Type[BotocoreClientError]
    BackupInProgress: Type[BotocoreClientError]
    BackupNotFound: Type[BotocoreClientError]
    BackupRestoring: Type[BotocoreClientError]
    BadRequest: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataRepositoryAssociationNotFound: Type[BotocoreClientError]
    DataRepositoryTaskEnded: Type[BotocoreClientError]
    DataRepositoryTaskExecuting: Type[BotocoreClientError]
    DataRepositoryTaskNotFound: Type[BotocoreClientError]
    FileCacheNotFound: Type[BotocoreClientError]
    FileSystemNotFound: Type[BotocoreClientError]
    IncompatibleParameterError: Type[BotocoreClientError]
    IncompatibleRegionForMultiAZ: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidDataRepositoryType: Type[BotocoreClientError]
    InvalidDestinationKmsKey: Type[BotocoreClientError]
    InvalidExportPath: Type[BotocoreClientError]
    InvalidImportPath: Type[BotocoreClientError]
    InvalidNetworkSettings: Type[BotocoreClientError]
    InvalidPerUnitStorageThroughput: Type[BotocoreClientError]
    InvalidRegion: Type[BotocoreClientError]
    InvalidSourceKmsKey: Type[BotocoreClientError]
    MissingFileCacheConfiguration: Type[BotocoreClientError]
    MissingFileSystemConfiguration: Type[BotocoreClientError]
    MissingVolumeConfiguration: Type[BotocoreClientError]
    NotServiceResourceError: Type[BotocoreClientError]
    ResourceDoesNotSupportTagging: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceLimitExceeded: Type[BotocoreClientError]
    SnapshotNotFound: Type[BotocoreClientError]
    SourceBackupUnavailable: Type[BotocoreClientError]
    StorageVirtualMachineNotFound: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]
    VolumeNotFound: Type[BotocoreClientError]

class FSxClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FSxClient exceptions.
        """
    def associate_file_system_aliases(
        self, *, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> AssociateFileSystemAliasesResponseTypeDef:
        """
        Use this action to associate one or more Domain Name Server (DNS) aliases with
        an existing Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.associate_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#associate_file_system_aliases)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#can_paginate)
        """
    def cancel_data_repository_task(
        self, *, TaskId: str
    ) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        Cancels an existing Amazon FSx for Lustre data repository task if that task is
        in either the `PENDING` or `EXECUTING` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#cancel_data_repository_task)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#close)
        """
    def copy_backup(
        self,
        *,
        SourceBackupId: str,
        ClientRequestToken: str = None,
        SourceRegion: str = None,
        KmsKeyId: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CopyBackupResponseTypeDef:
        """
        Copies an existing backup within the same Amazon Web Services account to another
        Amazon Web Services Region (cross-Region copy) or within the same Amazon Web
        Services Region (in-Region copy).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.copy_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#copy_backup)
        """
    def create_backup(
        self,
        *,
        FileSystemId: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
        VolumeId: str = None
    ) -> CreateBackupResponseTypeDef:
        """
        Creates a backup of an existing Amazon FSx for Windows File Server file system,
        Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon
        FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_backup)
        """
    def create_data_repository_association(
        self,
        *,
        FileSystemId: str,
        DataRepositoryPath: str,
        FileSystemPath: str = None,
        BatchImportMetaDataOnCreate: bool = None,
        ImportedFileChunkSize: int = None,
        S3: "S3DataRepositoryConfigurationTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataRepositoryAssociationResponseTypeDef:
        """
        Creates an Amazon FSx for Lustre data repository association (DRA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_data_repository_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_data_repository_association)
        """
    def create_data_repository_task(
        self,
        *,
        Type: DataRepositoryTaskTypeType,
        FileSystemId: str,
        Report: "CompletionReportTypeDef",
        Paths: List[str] = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
        CapacityToRelease: int = None
    ) -> CreateDataRepositoryTaskResponseTypeDef:
        """
        Creates an Amazon FSx for Lustre data repository task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_data_repository_task)
        """
    def create_file_cache(
        self,
        *,
        FileCacheType: Literal["LUSTRE"],
        FileCacheTypeVersion: str,
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        CopyTagsToDataRepositoryAssociations: bool = None,
        KmsKeyId: str = None,
        LustreConfiguration: "CreateFileCacheLustreConfigurationTypeDef" = None,
        DataRepositoryAssociations: List["FileCacheDataRepositoryAssociationTypeDef"] = None
    ) -> CreateFileCacheResponseTypeDef:
        """
        Creates a new Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_file_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_cache)
        """
    def create_file_system(
        self,
        *,
        FileSystemType: FileSystemTypeType,
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        StorageType: StorageTypeType = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: "CreateFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "CreateFileSystemLustreConfigurationTypeDef" = None,
        OntapConfiguration: "CreateFileSystemOntapConfigurationTypeDef" = None,
        FileSystemTypeVersion: str = None,
        OpenZFSConfiguration: "CreateFileSystemOpenZFSConfigurationTypeDef" = None
    ) -> CreateFileSystemResponseTypeDef:
        """
        Creates a new, empty Amazon FSx file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_system)
        """
    def create_file_system_from_backup(
        self,
        *,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        WindowsConfiguration: "CreateFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "CreateFileSystemLustreConfigurationTypeDef" = None,
        StorageType: StorageTypeType = None,
        KmsKeyId: str = None,
        FileSystemTypeVersion: str = None,
        OpenZFSConfiguration: "CreateFileSystemOpenZFSConfigurationTypeDef" = None,
        StorageCapacity: int = None
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx for Lustre, Amazon FSx for Windows File Server, or
        Amazon FSx for OpenZFS file system from an existing Amazon FSx backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_system_from_backup)
        """
    def create_snapshot(
        self,
        *,
        Name: str,
        VolumeId: str,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a snapshot of an existing Amazon FSx for OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_snapshot)
        """
    def create_storage_virtual_machine(
        self,
        *,
        FileSystemId: str,
        Name: str,
        ActiveDirectoryConfiguration: "CreateSvmActiveDirectoryConfigurationTypeDef" = None,
        ClientRequestToken: str = None,
        SvmAdminPassword: str = None,
        Tags: List["TagTypeDef"] = None,
        RootVolumeSecurityStyle: StorageVirtualMachineRootVolumeSecurityStyleType = None
    ) -> CreateStorageVirtualMachineResponseTypeDef:
        """
        Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_storage_virtual_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_storage_virtual_machine)
        """
    def create_volume(
        self,
        *,
        VolumeType: VolumeTypeType,
        Name: str,
        ClientRequestToken: str = None,
        OntapConfiguration: "CreateOntapVolumeConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        OpenZFSConfiguration: "CreateOpenZFSVolumeConfigurationTypeDef" = None
    ) -> CreateVolumeResponseTypeDef:
        """
        Creates an FSx for ONTAP or Amazon FSx for OpenZFS storage volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_volume)
        """
    def create_volume_from_backup(
        self,
        *,
        BackupId: str,
        Name: str,
        ClientRequestToken: str = None,
        OntapConfiguration: "CreateOntapVolumeConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateVolumeFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx
        volume backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.create_volume_from_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_volume_from_backup)
        """
    def delete_backup(
        self, *, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        Deletes an Amazon FSx backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_backup)
        """
    def delete_data_repository_association(
        self,
        *,
        AssociationId: str,
        ClientRequestToken: str = None,
        DeleteDataInFileSystem: bool = None
    ) -> DeleteDataRepositoryAssociationResponseTypeDef:
        """
        Deletes a data repository association on an Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_data_repository_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_data_repository_association)
        """
    def delete_file_cache(
        self, *, FileCacheId: str, ClientRequestToken: str = None
    ) -> DeleteFileCacheResponseTypeDef:
        """
        Deletes an Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_file_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_file_cache)
        """
    def delete_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: "DeleteFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "DeleteFileSystemLustreConfigurationTypeDef" = None,
        OpenZFSConfiguration: "DeleteFileSystemOpenZFSConfigurationTypeDef" = None
    ) -> DeleteFileSystemResponseTypeDef:
        """
        Deletes a file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_file_system)
        """
    def delete_snapshot(
        self, *, SnapshotId: str, ClientRequestToken: str = None
    ) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes an Amazon FSx for OpenZFS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_snapshot)
        """
    def delete_storage_virtual_machine(
        self, *, StorageVirtualMachineId: str, ClientRequestToken: str = None
    ) -> DeleteStorageVirtualMachineResponseTypeDef:
        """
        Deletes an existing Amazon FSx for ONTAP storage virtual machine (SVM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_storage_virtual_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_storage_virtual_machine)
        """
    def delete_volume(
        self,
        *,
        VolumeId: str,
        ClientRequestToken: str = None,
        OntapConfiguration: "DeleteVolumeOntapConfigurationTypeDef" = None,
        OpenZFSConfiguration: "DeleteVolumeOpenZFSConfigurationTypeDef" = None
    ) -> DeleteVolumeResponseTypeDef:
        """
        Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.delete_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_volume)
        """
    def describe_backups(
        self,
        *,
        BackupIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeBackupsResponseTypeDef:
        """
        Returns the description of a specific Amazon FSx backup, if a `BackupIds` value
        is provided for that backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_backups)
        """
    def describe_data_repository_associations(
        self,
        *,
        AssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDataRepositoryAssociationsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for Lustre or Amazon File Cache
        data repository associations, if one or more `AssociationIds` values are
        provided in the request, or if filters are used in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_data_repository_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_data_repository_associations)
        """
    def describe_data_repository_tasks(
        self,
        *,
        TaskIds: List[str] = None,
        Filters: List["DataRepositoryTaskFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDataRepositoryTasksResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for Lustre or Amazon File Cache
        data repository tasks, if one or more `TaskIds` values are provided in the
        request, or if filters are used in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_data_repository_tasks)
        """
    def describe_file_caches(
        self, *, FileCacheIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileCachesResponseTypeDef:
        """
        Returns the description of a specific Amazon File Cache resource, if a
        `FileCacheIds` value is provided for that cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_file_caches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_caches)
        """
    def describe_file_system_aliases(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFileSystemAliasesResponseTypeDef:
        """
        Returns the DNS aliases that are associated with the specified Amazon FSx for
        Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_system_aliases)
        """
    def describe_file_systems(
        self, *, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx file systems, if a
        `FileSystemIds` value is provided for that file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_file_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_systems)
        """
    def describe_snapshots(
        self,
        *,
        SnapshotIds: List[str] = None,
        Filters: List["SnapshotFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeSnapshotsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for OpenZFS snapshots, if a
        `SnapshotIds` value is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_snapshots)
        """
    def describe_storage_virtual_machines(
        self,
        *,
        StorageVirtualMachineIds: List[str] = None,
        Filters: List["StorageVirtualMachineFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeStorageVirtualMachinesResponseTypeDef:
        """
        Describes one or more Amazon FSx for NetApp ONTAP storage virtual machines
        (SVMs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_storage_virtual_machines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_storage_virtual_machines)
        """
    def describe_volumes(
        self,
        *,
        VolumeIds: List[str] = None,
        Filters: List["VolumeFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVolumesResponseTypeDef:
        """
        Describes one or more Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS
        volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.describe_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_volumes)
        """
    def disassociate_file_system_aliases(
        self, *, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> DisassociateFileSystemAliasesResponseTypeDef:
        """
        Use this action to disassociate, or remove, one or more Domain Name Service
        (DNS) aliases from an Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.disassociate_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#disassociate_file_system_aliases)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#generate_presigned_url)
        """
    def list_tags_for_resource(
        self, *, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for Amazon FSx resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#list_tags_for_resource)
        """
    def release_file_system_nfs_v3_locks(
        self, *, FileSystemId: str, ClientRequestToken: str = None
    ) -> ReleaseFileSystemNfsV3LocksResponseTypeDef:
        """
        Releases the file system lock from an Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.release_file_system_nfs_v3_locks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#release_file_system_nfs_v3_locks)
        """
    def restore_volume_from_snapshot(
        self,
        *,
        VolumeId: str,
        SnapshotId: str,
        ClientRequestToken: str = None,
        Options: List[RestoreOpenZFSVolumeOptionType] = None
    ) -> RestoreVolumeFromSnapshotResponseTypeDef:
        """
        Returns an Amazon FSx for OpenZFS volume to the state saved by the specified
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.restore_volume_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#restore_volume_from_snapshot)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        This action removes a tag from an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#untag_resource)
        """
    def update_data_repository_association(
        self,
        *,
        AssociationId: str,
        ClientRequestToken: str = None,
        ImportedFileChunkSize: int = None,
        S3: "S3DataRepositoryConfigurationTypeDef" = None
    ) -> UpdateDataRepositoryAssociationResponseTypeDef:
        """
        Updates the configuration of an existing data repository association on an
        Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_data_repository_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_data_repository_association)
        """
    def update_file_cache(
        self,
        *,
        FileCacheId: str,
        ClientRequestToken: str = None,
        LustreConfiguration: "UpdateFileCacheLustreConfigurationTypeDef" = None
    ) -> UpdateFileCacheResponseTypeDef:
        """
        Updates the configuration of an existing Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_file_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_file_cache)
        """
    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        StorageCapacity: int = None,
        WindowsConfiguration: "UpdateFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "UpdateFileSystemLustreConfigurationTypeDef" = None,
        OntapConfiguration: "UpdateFileSystemOntapConfigurationTypeDef" = None,
        OpenZFSConfiguration: "UpdateFileSystemOpenZFSConfigurationTypeDef" = None
    ) -> UpdateFileSystemResponseTypeDef:
        """
        Use this operation to update the configuration of an existing Amazon FSx file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_file_system)
        """
    def update_snapshot(
        self, *, Name: str, SnapshotId: str, ClientRequestToken: str = None
    ) -> UpdateSnapshotResponseTypeDef:
        """
        Updates the name of an Amazon FSx for OpenZFS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_snapshot)
        """
    def update_storage_virtual_machine(
        self,
        *,
        StorageVirtualMachineId: str,
        ActiveDirectoryConfiguration: "UpdateSvmActiveDirectoryConfigurationTypeDef" = None,
        ClientRequestToken: str = None,
        SvmAdminPassword: str = None
    ) -> UpdateStorageVirtualMachineResponseTypeDef:
        """
        Updates an Amazon FSx for ONTAP storage virtual machine (SVM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_storage_virtual_machine)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_storage_virtual_machine)
        """
    def update_volume(
        self,
        *,
        VolumeId: str,
        ClientRequestToken: str = None,
        OntapConfiguration: "UpdateOntapVolumeConfigurationTypeDef" = None,
        Name: str = None,
        OpenZFSConfiguration: "UpdateOpenZFSVolumeConfigurationTypeDef" = None
    ) -> UpdateVolumeResponseTypeDef:
        """
        Updates the configuration of an Amazon FSx for NetApp ONTAP or Amazon FSx for
        OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Client.update_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_volume)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describebackupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describefilesystemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_storage_virtual_machines"]
    ) -> DescribeStorageVirtualMachinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Paginator.DescribeStorageVirtualMachines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describestoragevirtualmachinespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Paginator.DescribeVolumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describevolumespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#listtagsforresourcepaginator)
        """
