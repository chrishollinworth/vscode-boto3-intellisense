"""
Type annotations for fsx service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_fsx import FSxClient
    from mypy_boto3_fsx.paginator import (
        DescribeBackupsPaginator,
        DescribeFileSystemsPaginator,
        DescribeStorageVirtualMachinesPaginator,
        DescribeVolumesPaginator,
        ListTagsForResourcePaginator,
    )

    client: FSxClient = boto3.client("fsx")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_storage_virtual_machines_paginator: DescribeStorageVirtualMachinesPaginator = client.get_paginator("describe_storage_virtual_machines")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DescribeStorageVirtualMachinesResponseTypeDef,
    DescribeVolumesResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    StorageVirtualMachineFilterTypeDef,
    VolumeFilterTypeDef,
)

__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeStorageVirtualMachinesPaginator",
    "DescribeVolumesPaginator",
    "ListTagsForResourcePaginator",
)

class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describebackupspaginator)
    """

    def paginate(
        self,
        *,
        BackupIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeBackups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describebackupspaginator)
        """

class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describefilesystemspaginator)
    """

    def paginate(
        self, *, FileSystemIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFileSystemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describefilesystemspaginator)
        """

class DescribeStorageVirtualMachinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeStorageVirtualMachines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describestoragevirtualmachinespaginator)
    """

    def paginate(
        self,
        *,
        StorageVirtualMachineIds: List[str] = None,
        Filters: List["StorageVirtualMachineFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStorageVirtualMachinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeStorageVirtualMachines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describestoragevirtualmachinespaginator)
        """

class DescribeVolumesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeVolumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describevolumespaginator)
    """

    def paginate(
        self,
        *,
        VolumeIds: List[str] = None,
        Filters: List["VolumeFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.DescribeVolumes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describevolumespaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/fsx.html#FSx.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#listtagsforresourcepaginator)
        """
