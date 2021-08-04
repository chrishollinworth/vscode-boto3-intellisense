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

from .literals import FileSystemTypeType, StorageTypeType
from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFileSystemAliasesResponseTypeDef,
    CancelDataRepositoryTaskResponseTypeDef,
    CompletionReportTypeDef,
    CopyBackupResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateDataRepositoryTaskResponseTypeDef,
    CreateFileSystemFromBackupResponseTypeDef,
    CreateFileSystemLustreConfigurationTypeDef,
    CreateFileSystemResponseTypeDef,
    CreateFileSystemWindowsConfigurationTypeDef,
    DataRepositoryTaskFilterTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteFileSystemLustreConfigurationTypeDef,
    DeleteFileSystemResponseTypeDef,
    DeleteFileSystemWindowsConfigurationTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeDataRepositoryTasksResponseTypeDef,
    DescribeFileSystemAliasesResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DisassociateFileSystemAliasesResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateFileSystemLustreConfigurationTypeDef,
    UpdateFileSystemResponseTypeDef,
    UpdateFileSystemWindowsConfigurationTypeDef,
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
    DataRepositoryTaskEnded: Type[BotocoreClientError]
    DataRepositoryTaskExecuting: Type[BotocoreClientError]
    DataRepositoryTaskNotFound: Type[BotocoreClientError]
    FileSystemNotFound: Type[BotocoreClientError]
    IncompatibleParameterError: Type[BotocoreClientError]
    IncompatibleRegionForMultiAZ: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidDestinationKmsKey: Type[BotocoreClientError]
    InvalidExportPath: Type[BotocoreClientError]
    InvalidImportPath: Type[BotocoreClientError]
    InvalidNetworkSettings: Type[BotocoreClientError]
    InvalidPerUnitStorageThroughput: Type[BotocoreClientError]
    InvalidRegion: Type[BotocoreClientError]
    InvalidSourceKmsKey: Type[BotocoreClientError]
    MissingFileSystemConfiguration: Type[BotocoreClientError]
    NotServiceResourceError: Type[BotocoreClientError]
    ResourceDoesNotSupportTagging: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceLimitExceeded: Type[BotocoreClientError]
    SourceBackupUnavailable: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]

class FSxClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.associate_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#associate_file_system_aliases)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#can_paginate)
        """
    def cancel_data_repository_task(
        self, *, TaskId: str
    ) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        Cancels an existing Amazon FSx for Lustre data repository task if that task is
        in either the `PENDING` or `EXECUTING` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#cancel_data_repository_task)
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
        Copies an existing backup within the same AWS account to another Region (cross-
        Region copy) or within the same Region (in-Region copy).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.copy_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#copy_backup)
        """
    def create_backup(
        self, *, FileSystemId: str, ClientRequestToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        Creates a backup of an existing Amazon FSx file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.create_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_backup)
        """
    def create_data_repository_task(
        self,
        *,
        Type: Literal["EXPORT_TO_REPOSITORY"],
        FileSystemId: str,
        Report: "CompletionReportTypeDef",
        Paths: List[str] = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataRepositoryTaskResponseTypeDef:
        """
        Creates an Amazon FSx for Lustre data repository task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.create_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_data_repository_task)
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
        LustreConfiguration: "CreateFileSystemLustreConfigurationTypeDef" = None
    ) -> CreateFileSystemResponseTypeDef:
        """
        Creates a new, empty Amazon FSx file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.create_file_system)
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
        KmsKeyId: str = None
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx file system from an existing Amazon FSx backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_system_from_backup)
        """
    def delete_backup(
        self, *, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        Deletes an Amazon FSx backup, deleting its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_backup)
        """
    def delete_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: "DeleteFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "DeleteFileSystemLustreConfigurationTypeDef" = None
    ) -> DeleteFileSystemResponseTypeDef:
        """
        Deletes a file system, deleting its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.delete_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_file_system)
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
        Returns the description of specific Amazon FSx backups, if a `BackupIds` value
        is provided for that backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.describe_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_backups)
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
        Returns the description of specific Amazon FSx for Lustre data repository tasks,
        if one or more `TaskIds` values are provided in the request, or if filters are
        used in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_data_repository_tasks)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.describe_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_system_aliases)
        """
    def describe_file_systems(
        self, *, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx file systems, if a
        `FileSystemIds` value is provided for that file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.describe_file_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_systems)
        """
    def disassociate_file_system_aliases(
        self, *, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> DisassociateFileSystemAliasesResponseTypeDef:
        """
        Use this action to disassociate, or remove, one or more Domain Name Service
        (DNS) aliases from an Amazon FSx for Windows File Server file system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.disassociate_file_system_aliases)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#generate_presigned_url)
        """
    def list_tags_for_resource(
        self, *, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for an Amazon FSx file systems and backups in the case of Amazon FSx
        for Windows File Server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        This action removes a tag from an Amazon FSx resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#untag_resource)
        """
    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        StorageCapacity: int = None,
        WindowsConfiguration: "UpdateFileSystemWindowsConfigurationTypeDef" = None,
        LustreConfiguration: "UpdateFileSystemLustreConfigurationTypeDef" = None
    ) -> UpdateFileSystemResponseTypeDef:
        """
        Use this operation to update the configuration of an existing Amazon FSx file
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Client.update_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_file_system)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describebackupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describefilesystemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#listtagsforresourcepaginator)
        """
