"""
Type annotations for fsx service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_fsx.client import FSxClient

    session = Session()
    client: FSxClient = session.client("fsx")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    DescribeStorageVirtualMachinesPaginator,
    DescribeVolumesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFileSystemAliasesRequestTypeDef,
    AssociateFileSystemAliasesResponseTypeDef,
    CancelDataRepositoryTaskRequestTypeDef,
    CancelDataRepositoryTaskResponseTypeDef,
    CopyBackupRequestTypeDef,
    CopyBackupResponseTypeDef,
    CopySnapshotAndUpdateVolumeRequestTypeDef,
    CopySnapshotAndUpdateVolumeResponseTypeDef,
    CreateBackupRequestTypeDef,
    CreateBackupResponseTypeDef,
    CreateDataRepositoryAssociationRequestTypeDef,
    CreateDataRepositoryAssociationResponseTypeDef,
    CreateDataRepositoryTaskRequestTypeDef,
    CreateDataRepositoryTaskResponseTypeDef,
    CreateFileCacheRequestTypeDef,
    CreateFileCacheResponseTypeDef,
    CreateFileSystemFromBackupRequestTypeDef,
    CreateFileSystemFromBackupResponseTypeDef,
    CreateFileSystemRequestTypeDef,
    CreateFileSystemResponseTypeDef,
    CreateSnapshotRequestTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateStorageVirtualMachineRequestTypeDef,
    CreateStorageVirtualMachineResponseTypeDef,
    CreateVolumeFromBackupRequestTypeDef,
    CreateVolumeFromBackupResponseTypeDef,
    CreateVolumeRequestTypeDef,
    CreateVolumeResponseTypeDef,
    DeleteBackupRequestTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteDataRepositoryAssociationRequestTypeDef,
    DeleteDataRepositoryAssociationResponseTypeDef,
    DeleteFileCacheRequestTypeDef,
    DeleteFileCacheResponseTypeDef,
    DeleteFileSystemRequestTypeDef,
    DeleteFileSystemResponseTypeDef,
    DeleteSnapshotRequestTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteStorageVirtualMachineRequestTypeDef,
    DeleteStorageVirtualMachineResponseTypeDef,
    DeleteVolumeRequestTypeDef,
    DeleteVolumeResponseTypeDef,
    DescribeBackupsRequestTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeDataRepositoryAssociationsRequestTypeDef,
    DescribeDataRepositoryAssociationsResponseTypeDef,
    DescribeDataRepositoryTasksRequestTypeDef,
    DescribeDataRepositoryTasksResponseTypeDef,
    DescribeFileCachesRequestTypeDef,
    DescribeFileCachesResponseTypeDef,
    DescribeFileSystemAliasesRequestTypeDef,
    DescribeFileSystemAliasesResponseTypeDef,
    DescribeFileSystemsRequestTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeSharedVpcConfigurationResponseTypeDef,
    DescribeSnapshotsRequestTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeStorageVirtualMachinesRequestTypeDef,
    DescribeStorageVirtualMachinesResponseTypeDef,
    DescribeVolumesRequestTypeDef,
    DescribeVolumesResponseTypeDef,
    DisassociateFileSystemAliasesRequestTypeDef,
    DisassociateFileSystemAliasesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ReleaseFileSystemNfsV3LocksRequestTypeDef,
    ReleaseFileSystemNfsV3LocksResponseTypeDef,
    RestoreVolumeFromSnapshotRequestTypeDef,
    RestoreVolumeFromSnapshotResponseTypeDef,
    StartMisconfiguredStateRecoveryRequestTypeDef,
    StartMisconfiguredStateRecoveryResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDataRepositoryAssociationRequestTypeDef,
    UpdateDataRepositoryAssociationResponseTypeDef,
    UpdateFileCacheRequestTypeDef,
    UpdateFileCacheResponseTypeDef,
    UpdateFileSystemRequestTypeDef,
    UpdateFileSystemResponseTypeDef,
    UpdateSharedVpcConfigurationRequestTypeDef,
    UpdateSharedVpcConfigurationResponseTypeDef,
    UpdateSnapshotRequestTypeDef,
    UpdateSnapshotResponseTypeDef,
    UpdateStorageVirtualMachineRequestTypeDef,
    UpdateStorageVirtualMachineResponseTypeDef,
    UpdateVolumeRequestTypeDef,
    UpdateVolumeResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("FSxClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FSxClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#generate_presigned_url)
        """

    def associate_file_system_aliases(
        self, **kwargs: Unpack[AssociateFileSystemAliasesRequestTypeDef]
    ) -> AssociateFileSystemAliasesResponseTypeDef:
        """
        Use this action to associate one or more Domain Name Server (DNS) aliases with
        an existing Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/associate_file_system_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#associate_file_system_aliases)
        """

    def cancel_data_repository_task(
        self, **kwargs: Unpack[CancelDataRepositoryTaskRequestTypeDef]
    ) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        Cancels an existing Amazon FSx for Lustre data repository task if that task is
        in either the <code>PENDING</code> or <code>EXECUTING</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/cancel_data_repository_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#cancel_data_repository_task)
        """

    def copy_backup(self, **kwargs: Unpack[CopyBackupRequestTypeDef]) -> CopyBackupResponseTypeDef:
        """
        Copies an existing backup within the same Amazon Web Services account to
        another Amazon Web Services Region (cross-Region copy) or within the same
        Amazon Web Services Region (in-Region copy).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/copy_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#copy_backup)
        """

    def copy_snapshot_and_update_volume(
        self, **kwargs: Unpack[CopySnapshotAndUpdateVolumeRequestTypeDef]
    ) -> CopySnapshotAndUpdateVolumeResponseTypeDef:
        """
        Updates an existing volume by using a snapshot from another Amazon FSx for
        OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/copy_snapshot_and_update_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#copy_snapshot_and_update_volume)
        """

    def create_backup(
        self, **kwargs: Unpack[CreateBackupRequestTypeDef]
    ) -> CreateBackupResponseTypeDef:
        """
        Creates a backup of an existing Amazon FSx for Windows File Server file system,
        Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or
        Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_backup)
        """

    def create_data_repository_association(
        self, **kwargs: Unpack[CreateDataRepositoryAssociationRequestTypeDef]
    ) -> CreateDataRepositoryAssociationResponseTypeDef:
        """
        Creates an Amazon FSx for Lustre data repository association (DRA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_data_repository_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_data_repository_association)
        """

    def create_data_repository_task(
        self, **kwargs: Unpack[CreateDataRepositoryTaskRequestTypeDef]
    ) -> CreateDataRepositoryTaskResponseTypeDef:
        """
        Creates an Amazon FSx for Lustre data repository task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_data_repository_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_data_repository_task)
        """

    def create_file_cache(
        self, **kwargs: Unpack[CreateFileCacheRequestTypeDef]
    ) -> CreateFileCacheResponseTypeDef:
        """
        Creates a new Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_file_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_file_cache)
        """

    def create_file_system(
        self, **kwargs: Unpack[CreateFileSystemRequestTypeDef]
    ) -> CreateFileSystemResponseTypeDef:
        """
        Creates a new, empty Amazon FSx file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_file_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_file_system)
        """

    def create_file_system_from_backup(
        self, **kwargs: Unpack[CreateFileSystemFromBackupRequestTypeDef]
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx for Lustre, Amazon FSx for Windows File Server, or
        Amazon FSx for OpenZFS file system from an existing Amazon FSx backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_file_system_from_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_file_system_from_backup)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestTypeDef]
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a snapshot of an existing Amazon FSx for OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_snapshot)
        """

    def create_storage_virtual_machine(
        self, **kwargs: Unpack[CreateStorageVirtualMachineRequestTypeDef]
    ) -> CreateStorageVirtualMachineResponseTypeDef:
        """
        Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_storage_virtual_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_storage_virtual_machine)
        """

    def create_volume(
        self, **kwargs: Unpack[CreateVolumeRequestTypeDef]
    ) -> CreateVolumeResponseTypeDef:
        """
        Creates an FSx for ONTAP or Amazon FSx for OpenZFS storage volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_volume)
        """

    def create_volume_from_backup(
        self, **kwargs: Unpack[CreateVolumeFromBackupRequestTypeDef]
    ) -> CreateVolumeFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx
        volume backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/create_volume_from_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#create_volume_from_backup)
        """

    def delete_backup(
        self, **kwargs: Unpack[DeleteBackupRequestTypeDef]
    ) -> DeleteBackupResponseTypeDef:
        """
        Deletes an Amazon FSx backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_backup)
        """

    def delete_data_repository_association(
        self, **kwargs: Unpack[DeleteDataRepositoryAssociationRequestTypeDef]
    ) -> DeleteDataRepositoryAssociationResponseTypeDef:
        """
        Deletes a data repository association on an Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_data_repository_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_data_repository_association)
        """

    def delete_file_cache(
        self, **kwargs: Unpack[DeleteFileCacheRequestTypeDef]
    ) -> DeleteFileCacheResponseTypeDef:
        """
        Deletes an Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_file_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_file_cache)
        """

    def delete_file_system(
        self, **kwargs: Unpack[DeleteFileSystemRequestTypeDef]
    ) -> DeleteFileSystemResponseTypeDef:
        """
        Deletes a file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_file_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_file_system)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestTypeDef]
    ) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes an Amazon FSx for OpenZFS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_snapshot)
        """

    def delete_storage_virtual_machine(
        self, **kwargs: Unpack[DeleteStorageVirtualMachineRequestTypeDef]
    ) -> DeleteStorageVirtualMachineResponseTypeDef:
        """
        Deletes an existing Amazon FSx for ONTAP storage virtual machine (SVM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_storage_virtual_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_storage_virtual_machine)
        """

    def delete_volume(
        self, **kwargs: Unpack[DeleteVolumeRequestTypeDef]
    ) -> DeleteVolumeResponseTypeDef:
        """
        Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/delete_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#delete_volume)
        """

    def describe_backups(
        self, **kwargs: Unpack[DescribeBackupsRequestTypeDef]
    ) -> DescribeBackupsResponseTypeDef:
        """
        Returns the description of a specific Amazon FSx backup, if a
        <code>BackupIds</code> value is provided for that backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_backups)
        """

    def describe_data_repository_associations(
        self, **kwargs: Unpack[DescribeDataRepositoryAssociationsRequestTypeDef]
    ) -> DescribeDataRepositoryAssociationsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for Lustre or Amazon File Cache
        data repository associations, if one or more <code>AssociationIds</code> values
        are provided in the request, or if filters are used in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_data_repository_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_data_repository_associations)
        """

    def describe_data_repository_tasks(
        self, **kwargs: Unpack[DescribeDataRepositoryTasksRequestTypeDef]
    ) -> DescribeDataRepositoryTasksResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for Lustre or Amazon File Cache
        data repository tasks, if one or more <code>TaskIds</code> values are provided
        in the request, or if filters are used in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_data_repository_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_data_repository_tasks)
        """

    def describe_file_caches(
        self, **kwargs: Unpack[DescribeFileCachesRequestTypeDef]
    ) -> DescribeFileCachesResponseTypeDef:
        """
        Returns the description of a specific Amazon File Cache resource, if a
        <code>FileCacheIds</code> value is provided for that cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_file_caches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_file_caches)
        """

    def describe_file_system_aliases(
        self, **kwargs: Unpack[DescribeFileSystemAliasesRequestTypeDef]
    ) -> DescribeFileSystemAliasesResponseTypeDef:
        """
        Returns the DNS aliases that are associated with the specified Amazon FSx for
        Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_file_system_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_file_system_aliases)
        """

    def describe_file_systems(
        self, **kwargs: Unpack[DescribeFileSystemsRequestTypeDef]
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx file systems, if a
        <code>FileSystemIds</code> value is provided for that file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_file_systems.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_file_systems)
        """

    def describe_shared_vpc_configuration(self) -> DescribeSharedVpcConfigurationResponseTypeDef:
        """
        Indicates whether participant accounts in your organization can create Amazon
        FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a
        virtual private cloud (VPC) owner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_shared_vpc_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_shared_vpc_configuration)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsRequestTypeDef]
    ) -> DescribeSnapshotsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for OpenZFS snapshots, if a
        <code>SnapshotIds</code> value is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_snapshots)
        """

    def describe_storage_virtual_machines(
        self, **kwargs: Unpack[DescribeStorageVirtualMachinesRequestTypeDef]
    ) -> DescribeStorageVirtualMachinesResponseTypeDef:
        """
        Describes one or more Amazon FSx for NetApp ONTAP storage virtual machines
        (SVMs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_storage_virtual_machines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_storage_virtual_machines)
        """

    def describe_volumes(
        self, **kwargs: Unpack[DescribeVolumesRequestTypeDef]
    ) -> DescribeVolumesResponseTypeDef:
        """
        Describes one or more Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS
        volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/describe_volumes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#describe_volumes)
        """

    def disassociate_file_system_aliases(
        self, **kwargs: Unpack[DisassociateFileSystemAliasesRequestTypeDef]
    ) -> DisassociateFileSystemAliasesResponseTypeDef:
        """
        Use this action to disassociate, or remove, one or more Domain Name Service
        (DNS) aliases from an Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/disassociate_file_system_aliases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#disassociate_file_system_aliases)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for Amazon FSx resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#list_tags_for_resource)
        """

    def release_file_system_nfs_v3_locks(
        self, **kwargs: Unpack[ReleaseFileSystemNfsV3LocksRequestTypeDef]
    ) -> ReleaseFileSystemNfsV3LocksResponseTypeDef:
        """
        Releases the file system lock from an Amazon FSx for OpenZFS file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/release_file_system_nfs_v3_locks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#release_file_system_nfs_v3_locks)
        """

    def restore_volume_from_snapshot(
        self, **kwargs: Unpack[RestoreVolumeFromSnapshotRequestTypeDef]
    ) -> RestoreVolumeFromSnapshotResponseTypeDef:
        """
        Returns an Amazon FSx for OpenZFS volume to the state saved by the specified
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/restore_volume_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#restore_volume_from_snapshot)
        """

    def start_misconfigured_state_recovery(
        self, **kwargs: Unpack[StartMisconfiguredStateRecoveryRequestTypeDef]
    ) -> StartMisconfiguredStateRecoveryResponseTypeDef:
        """
        After performing steps to repair the Active Directory configuration of an FSx
        for Windows File Server file system, use this action to initiate the process of
        Amazon FSx attempting to reconnect to the file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/start_misconfigured_state_recovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#start_misconfigured_state_recovery)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        This action removes a tag from an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#untag_resource)
        """

    def update_data_repository_association(
        self, **kwargs: Unpack[UpdateDataRepositoryAssociationRequestTypeDef]
    ) -> UpdateDataRepositoryAssociationResponseTypeDef:
        """
        Updates the configuration of an existing data repository association on an
        Amazon FSx for Lustre file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_data_repository_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_data_repository_association)
        """

    def update_file_cache(
        self, **kwargs: Unpack[UpdateFileCacheRequestTypeDef]
    ) -> UpdateFileCacheResponseTypeDef:
        """
        Updates the configuration of an existing Amazon File Cache resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_file_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_file_cache)
        """

    def update_file_system(
        self, **kwargs: Unpack[UpdateFileSystemRequestTypeDef]
    ) -> UpdateFileSystemResponseTypeDef:
        """
        Use this operation to update the configuration of an existing Amazon FSx file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_file_system.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_file_system)
        """

    def update_shared_vpc_configuration(
        self, **kwargs: Unpack[UpdateSharedVpcConfigurationRequestTypeDef]
    ) -> UpdateSharedVpcConfigurationResponseTypeDef:
        """
        Configures whether participant accounts in your organization can create Amazon
        FSx for NetApp ONTAP Multi-AZ file systems in subnets that are shared by a
        virtual private cloud (VPC) owner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_shared_vpc_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_shared_vpc_configuration)
        """

    def update_snapshot(
        self, **kwargs: Unpack[UpdateSnapshotRequestTypeDef]
    ) -> UpdateSnapshotResponseTypeDef:
        """
        Updates the name of an Amazon FSx for OpenZFS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_snapshot)
        """

    def update_storage_virtual_machine(
        self, **kwargs: Unpack[UpdateStorageVirtualMachineRequestTypeDef]
    ) -> UpdateStorageVirtualMachineResponseTypeDef:
        """
        Updates an FSx for ONTAP storage virtual machine (SVM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_storage_virtual_machine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_storage_virtual_machine)
        """

    def update_volume(
        self, **kwargs: Unpack[UpdateVolumeRequestTypeDef]
    ) -> UpdateVolumeResponseTypeDef:
        """
        Updates the configuration of an Amazon FSx for NetApp ONTAP or Amazon FSx for
        OpenZFS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/update_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#update_volume)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_storage_virtual_machines"]
    ) -> DescribeStorageVirtualMachinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/client/#get_paginator)
        """
