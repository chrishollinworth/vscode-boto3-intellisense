# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for fsx service client

Usage::

    ```python
    import boto3
    from mypy_boto3_fsx import FSxClient

    client: FSxClient = boto3.client("fsx")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_fsx.paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_fsx.type_defs import (
    AssociateFileSystemAliasesResponseTypeDef,
    CancelDataRepositoryTaskResponseTypeDef,
    CompletionReportTypeDef,
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
    InternalServerError: Type[BotocoreClientError]
    InvalidExportPath: Type[BotocoreClientError]
    InvalidImportPath: Type[BotocoreClientError]
    InvalidNetworkSettings: Type[BotocoreClientError]
    InvalidPerUnitStorageThroughput: Type[BotocoreClientError]
    MissingFileSystemConfiguration: Type[BotocoreClientError]
    NotServiceResourceError: Type[BotocoreClientError]
    ResourceDoesNotSupportTagging: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceLimitExceeded: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class FSxClient:
    """
    [FSx.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_file_system_aliases(
        self, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> AssociateFileSystemAliasesResponseTypeDef:
        """
        [Client.associate_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.associate_file_system_aliases)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.can_paginate)
        """

    def cancel_data_repository_task(self, TaskId: str) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        [Client.cancel_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        """

    def create_backup(
        self, FileSystemId: str, ClientRequestToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.create_backup)
        """

    def create_data_repository_task(
        self,
        Type: Literal["EXPORT_TO_REPOSITORY"],
        FileSystemId: str,
        Report: "CompletionReportTypeDef",
        Paths: List[str] = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDataRepositoryTaskResponseTypeDef:
        """
        [Client.create_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.create_data_repository_task)
        """

    def create_file_system(
        self,
        FileSystemType: Literal["WINDOWS", "LUSTRE"],
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        StorageType: Literal["SSD", "HDD"] = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None,
    ) -> CreateFileSystemResponseTypeDef:
        """
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.create_file_system)
        """

    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None,
        StorageType: Literal["SSD", "HDD"] = None,
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        [Client.create_file_system_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        """

    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.delete_backup)
        """

    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: DeleteFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: DeleteFileSystemLustreConfigurationTypeDef = None,
    ) -> DeleteFileSystemResponseTypeDef:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.delete_file_system)
        """

    def describe_backups(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.describe_backups)
        """

    def describe_data_repository_tasks(
        self,
        TaskIds: List[str] = None,
        Filters: List[DataRepositoryTaskFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeDataRepositoryTasksResponseTypeDef:
        """
        [Client.describe_data_repository_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        """

    def describe_file_system_aliases(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeFileSystemAliasesResponseTypeDef:
        """
        [Client.describe_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.describe_file_system_aliases)
        """

    def describe_file_systems(
        self, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.describe_file_systems)
        """

    def disassociate_file_system_aliases(
        self, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> DisassociateFileSystemAliasesResponseTypeDef:
        """
        [Client.disassociate_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.disassociate_file_system_aliases)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.untag_resource)
        """

    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        StorageCapacity: int = None,
        WindowsConfiguration: UpdateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: UpdateFileSystemLustreConfigurationTypeDef = None,
    ) -> UpdateFileSystemResponseTypeDef:
        """
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Client.update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        """
