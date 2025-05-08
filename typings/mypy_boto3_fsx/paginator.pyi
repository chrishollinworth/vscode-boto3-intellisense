"""
Type annotations for fsx service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_fsx.client import FSxClient
    from mypy_boto3_fsx.paginator import (
        DescribeBackupsPaginator,
        DescribeFileSystemsPaginator,
        DescribeStorageVirtualMachinesPaginator,
        DescribeVolumesPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: FSxClient = session.client("fsx")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_storage_virtual_machines_paginator: DescribeStorageVirtualMachinesPaginator = client.get_paginator("describe_storage_virtual_machines")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBackupsRequestPaginateTypeDef,
    DescribeBackupsResponsePaginatorTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeFileSystemsRequestPaginateTypeDef,
    DescribeFileSystemsResponsePaginatorTypeDef,
    DescribeStorageVirtualMachinesRequestPaginateTypeDef,
    DescribeStorageVirtualMachinesResponseTypeDef,
    DescribeVolumesRequestPaginateTypeDef,
    DescribeVolumesResponsePaginatorTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeStorageVirtualMachinesPaginator",
    "DescribeVolumesPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _DescribeBackupsPaginatorBase = Paginator[DescribeBackupsResponseTypeDef]
else:
    _DescribeBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBackupsPaginator(_DescribeBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeBackups.html#FSx.Paginator.DescribeBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describebackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBackupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBackupsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeBackups.html#FSx.Paginator.DescribeBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describebackupspaginator)
        """

if TYPE_CHECKING:
    _DescribeFileSystemsPaginatorBase = Paginator[DescribeFileSystemsResponsePaginatorTypeDef]
else:
    _DescribeFileSystemsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFileSystemsPaginator(_DescribeFileSystemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeFileSystems.html#FSx.Paginator.DescribeFileSystems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describefilesystemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFileSystemsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFileSystemsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeFileSystems.html#FSx.Paginator.DescribeFileSystems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describefilesystemspaginator)
        """

if TYPE_CHECKING:
    _DescribeStorageVirtualMachinesPaginatorBase = Paginator[
        DescribeStorageVirtualMachinesResponseTypeDef
    ]
else:
    _DescribeStorageVirtualMachinesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStorageVirtualMachinesPaginator(_DescribeStorageVirtualMachinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeStorageVirtualMachines.html#FSx.Paginator.DescribeStorageVirtualMachines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describestoragevirtualmachinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStorageVirtualMachinesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStorageVirtualMachinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeStorageVirtualMachines.html#FSx.Paginator.DescribeStorageVirtualMachines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describestoragevirtualmachinespaginator)
        """

if TYPE_CHECKING:
    _DescribeVolumesPaginatorBase = Paginator[DescribeVolumesResponsePaginatorTypeDef]
else:
    _DescribeVolumesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVolumesPaginator(_DescribeVolumesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeVolumes.html#FSx.Paginator.DescribeVolumes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describevolumespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVolumesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/DescribeVolumes.html#FSx.Paginator.DescribeVolumes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#describevolumespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/ListTagsForResource.html#FSx.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx/paginator/ListTagsForResource.html#FSx.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators/#listtagsforresourcepaginator)
        """
