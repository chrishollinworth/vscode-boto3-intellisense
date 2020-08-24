# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_fsx.paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_fsx.type_defs import (
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
    DescribeFileSystemsResponseTypeDef,
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


class Exceptions:
    ActiveDirectoryError: Type[Boto3ClientError]
    BackupInProgress: Type[Boto3ClientError]
    BackupNotFound: Type[Boto3ClientError]
    BackupRestoring: Type[Boto3ClientError]
    BadRequest: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DataRepositoryTaskEnded: Type[Boto3ClientError]
    DataRepositoryTaskExecuting: Type[Boto3ClientError]
    DataRepositoryTaskNotFound: Type[Boto3ClientError]
    FileSystemNotFound: Type[Boto3ClientError]
    IncompatibleParameterError: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    InvalidExportPath: Type[Boto3ClientError]
    InvalidImportPath: Type[Boto3ClientError]
    InvalidNetworkSettings: Type[Boto3ClientError]
    InvalidPerUnitStorageThroughput: Type[Boto3ClientError]
    MissingFileSystemConfiguration: Type[Boto3ClientError]
    NotServiceResourceError: Type[Boto3ClientError]
    ResourceDoesNotSupportTagging: Type[Boto3ClientError]
    ResourceNotFound: Type[Boto3ClientError]
    ServiceLimitExceeded: Type[Boto3ClientError]
    UnsupportedOperation: Type[Boto3ClientError]


class FSxClient:
    """
    [FSx.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.can_paginate)
        """

    def cancel_data_repository_task(self, TaskId: str) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        [Client.cancel_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        """

    def create_backup(
        self, FileSystemId: str, ClientRequestToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.create_backup)
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
        [Client.create_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.create_data_repository_task)
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
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.create_file_system)
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
        [Client.create_file_system_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        """

    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.delete_backup)
        """

    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: DeleteFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: DeleteFileSystemLustreConfigurationTypeDef = None,
    ) -> DeleteFileSystemResponseTypeDef:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.delete_file_system)
        """

    def describe_backups(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.describe_backups)
        """

    def describe_data_repository_tasks(
        self,
        TaskIds: List[str] = None,
        Filters: List[DataRepositoryTaskFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeDataRepositoryTasksResponseTypeDef:
        """
        [Client.describe_data_repository_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        """

    def describe_file_systems(
        self, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.describe_file_systems)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.untag_resource)
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
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Client.update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
