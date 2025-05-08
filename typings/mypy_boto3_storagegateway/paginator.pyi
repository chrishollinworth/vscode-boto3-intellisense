"""
Type annotations for storagegateway service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_storagegateway.client import StorageGatewayClient
    from mypy_boto3_storagegateway.paginator import (
        DescribeTapeArchivesPaginator,
        DescribeTapeRecoveryPointsPaginator,
        DescribeTapesPaginator,
        DescribeVTLDevicesPaginator,
        ListCacheReportsPaginator,
        ListFileSharesPaginator,
        ListFileSystemAssociationsPaginator,
        ListGatewaysPaginator,
        ListTagsForResourcePaginator,
        ListTapePoolsPaginator,
        ListTapesPaginator,
        ListVolumesPaginator,
    )

    session = Session()
    client: StorageGatewayClient = session.client("storagegateway")

    describe_tape_archives_paginator: DescribeTapeArchivesPaginator = client.get_paginator("describe_tape_archives")
    describe_tape_recovery_points_paginator: DescribeTapeRecoveryPointsPaginator = client.get_paginator("describe_tape_recovery_points")
    describe_tapes_paginator: DescribeTapesPaginator = client.get_paginator("describe_tapes")
    describe_vtl_devices_paginator: DescribeVTLDevicesPaginator = client.get_paginator("describe_vtl_devices")
    list_cache_reports_paginator: ListCacheReportsPaginator = client.get_paginator("list_cache_reports")
    list_file_shares_paginator: ListFileSharesPaginator = client.get_paginator("list_file_shares")
    list_file_system_associations_paginator: ListFileSystemAssociationsPaginator = client.get_paginator("list_file_system_associations")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_tape_pools_paginator: ListTapePoolsPaginator = client.get_paginator("list_tape_pools")
    list_tapes_paginator: ListTapesPaginator = client.get_paginator("list_tapes")
    list_volumes_paginator: ListVolumesPaginator = client.get_paginator("list_volumes")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeTapeArchivesInputPaginateTypeDef,
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsInputPaginateTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesInputPaginateTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeVTLDevicesInputPaginateTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    ListCacheReportsInputPaginateTypeDef,
    ListCacheReportsOutputTypeDef,
    ListFileSharesInputPaginateTypeDef,
    ListFileSharesOutputTypeDef,
    ListFileSystemAssociationsInputPaginateTypeDef,
    ListFileSystemAssociationsOutputTypeDef,
    ListGatewaysInputPaginateTypeDef,
    ListGatewaysOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapePoolsInputPaginateTypeDef,
    ListTapePoolsOutputTypeDef,
    ListTapesInputPaginateTypeDef,
    ListTapesOutputTypeDef,
    ListVolumesInputPaginateTypeDef,
    ListVolumesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListCacheReportsPaginator",
    "ListFileSharesPaginator",
    "ListFileSystemAssociationsPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapePoolsPaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)

if TYPE_CHECKING:
    _DescribeTapeArchivesPaginatorBase = Paginator[DescribeTapeArchivesOutputTypeDef]
else:
    _DescribeTapeArchivesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTapeArchivesPaginator(_DescribeTapeArchivesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapeArchives.html#StorageGateway.Paginator.DescribeTapeArchives)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetapearchivespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTapeArchivesInputPaginateTypeDef]
    ) -> PageIterator[DescribeTapeArchivesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapeArchives.html#StorageGateway.Paginator.DescribeTapeArchives.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetapearchivespaginator)
        """

if TYPE_CHECKING:
    _DescribeTapeRecoveryPointsPaginatorBase = Paginator[DescribeTapeRecoveryPointsOutputTypeDef]
else:
    _DescribeTapeRecoveryPointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTapeRecoveryPointsPaginator(_DescribeTapeRecoveryPointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapeRecoveryPoints.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetaperecoverypointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTapeRecoveryPointsInputPaginateTypeDef]
    ) -> PageIterator[DescribeTapeRecoveryPointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapeRecoveryPoints.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetaperecoverypointspaginator)
        """

if TYPE_CHECKING:
    _DescribeTapesPaginatorBase = Paginator[DescribeTapesOutputTypeDef]
else:
    _DescribeTapesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTapesPaginator(_DescribeTapesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapes.html#StorageGateway.Paginator.DescribeTapes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetapespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTapesInputPaginateTypeDef]
    ) -> PageIterator[DescribeTapesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeTapes.html#StorageGateway.Paginator.DescribeTapes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describetapespaginator)
        """

if TYPE_CHECKING:
    _DescribeVTLDevicesPaginatorBase = Paginator[DescribeVTLDevicesOutputTypeDef]
else:
    _DescribeVTLDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVTLDevicesPaginator(_DescribeVTLDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeVTLDevices.html#StorageGateway.Paginator.DescribeVTLDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describevtldevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVTLDevicesInputPaginateTypeDef]
    ) -> PageIterator[DescribeVTLDevicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/DescribeVTLDevices.html#StorageGateway.Paginator.DescribeVTLDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#describevtldevicespaginator)
        """

if TYPE_CHECKING:
    _ListCacheReportsPaginatorBase = Paginator[ListCacheReportsOutputTypeDef]
else:
    _ListCacheReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCacheReportsPaginator(_ListCacheReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListCacheReports.html#StorageGateway.Paginator.ListCacheReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listcachereportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCacheReportsInputPaginateTypeDef]
    ) -> PageIterator[ListCacheReportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListCacheReports.html#StorageGateway.Paginator.ListCacheReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listcachereportspaginator)
        """

if TYPE_CHECKING:
    _ListFileSharesPaginatorBase = Paginator[ListFileSharesOutputTypeDef]
else:
    _ListFileSharesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFileSharesPaginator(_ListFileSharesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListFileShares.html#StorageGateway.Paginator.ListFileShares)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listfilesharespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFileSharesInputPaginateTypeDef]
    ) -> PageIterator[ListFileSharesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListFileShares.html#StorageGateway.Paginator.ListFileShares.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listfilesharespaginator)
        """

if TYPE_CHECKING:
    _ListFileSystemAssociationsPaginatorBase = Paginator[ListFileSystemAssociationsOutputTypeDef]
else:
    _ListFileSystemAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFileSystemAssociationsPaginator(_ListFileSystemAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListFileSystemAssociations.html#StorageGateway.Paginator.ListFileSystemAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listfilesystemassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFileSystemAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListFileSystemAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListFileSystemAssociations.html#StorageGateway.Paginator.ListFileSystemAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listfilesystemassociationspaginator)
        """

if TYPE_CHECKING:
    _ListGatewaysPaginatorBase = Paginator[ListGatewaysOutputTypeDef]
else:
    _ListGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewaysPaginator(_ListGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListGateways.html#StorageGateway.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewaysInputPaginateTypeDef]
    ) -> PageIterator[ListGatewaysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListGateways.html#StorageGateway.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTagsForResource.html#StorageGateway.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTagsForResource.html#StorageGateway.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListTapePoolsPaginatorBase = Paginator[ListTapePoolsOutputTypeDef]
else:
    _ListTapePoolsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTapePoolsPaginator(_ListTapePoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTapePools.html#StorageGateway.Paginator.ListTapePools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtapepoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTapePoolsInputPaginateTypeDef]
    ) -> PageIterator[ListTapePoolsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTapePools.html#StorageGateway.Paginator.ListTapePools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtapepoolspaginator)
        """

if TYPE_CHECKING:
    _ListTapesPaginatorBase = Paginator[ListTapesOutputTypeDef]
else:
    _ListTapesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTapesPaginator(_ListTapesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTapes.html#StorageGateway.Paginator.ListTapes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtapespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTapesInputPaginateTypeDef]
    ) -> PageIterator[ListTapesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListTapes.html#StorageGateway.Paginator.ListTapes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listtapespaginator)
        """

if TYPE_CHECKING:
    _ListVolumesPaginatorBase = Paginator[ListVolumesOutputTypeDef]
else:
    _ListVolumesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVolumesPaginator(_ListVolumesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListVolumes.html#StorageGateway.Paginator.ListVolumes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listvolumespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVolumesInputPaginateTypeDef]
    ) -> PageIterator[ListVolumesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway/paginator/ListVolumes.html#StorageGateway.Paginator.ListVolumes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators/#listvolumespaginator)
        """
