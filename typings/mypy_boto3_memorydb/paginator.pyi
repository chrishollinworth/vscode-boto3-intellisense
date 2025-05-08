"""
Type annotations for memorydb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_memorydb.client import MemoryDBClient
    from mypy_boto3_memorydb.paginator import (
        DescribeACLsPaginator,
        DescribeClustersPaginator,
        DescribeEngineVersionsPaginator,
        DescribeEventsPaginator,
        DescribeMultiRegionClustersPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeReservedNodesOfferingsPaginator,
        DescribeReservedNodesPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeSubnetGroupsPaginator,
        DescribeUsersPaginator,
    )

    session = Session()
    client: MemoryDBClient = session.client("memorydb")

    describe_acls_paginator: DescribeACLsPaginator = client.get_paginator("describe_acls")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_engine_versions_paginator: DescribeEngineVersionsPaginator = client.get_paginator("describe_engine_versions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_multi_region_clusters_paginator: DescribeMultiRegionClustersPaginator = client.get_paginator("describe_multi_region_clusters")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_reserved_nodes_offerings_paginator: DescribeReservedNodesOfferingsPaginator = client.get_paginator("describe_reserved_nodes_offerings")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeACLsRequestPaginateTypeDef,
    DescribeACLsResponseTypeDef,
    DescribeClustersRequestPaginateTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeEngineVersionsRequestPaginateTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventsRequestPaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeMultiRegionClustersRequestPaginateTypeDef,
    DescribeMultiRegionClustersResponseTypeDef,
    DescribeParameterGroupsRequestPaginateTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestPaginateTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeReservedNodesOfferingsRequestPaginateTypeDef,
    DescribeReservedNodesOfferingsResponseTypeDef,
    DescribeReservedNodesRequestPaginateTypeDef,
    DescribeReservedNodesResponseTypeDef,
    DescribeServiceUpdatesRequestPaginateTypeDef,
    DescribeServiceUpdatesResponseTypeDef,
    DescribeSnapshotsRequestPaginateTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeSubnetGroupsRequestPaginateTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    DescribeUsersRequestPaginateTypeDef,
    DescribeUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeACLsPaginator",
    "DescribeClustersPaginator",
    "DescribeEngineVersionsPaginator",
    "DescribeEventsPaginator",
    "DescribeMultiRegionClustersPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeReservedNodesOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSubnetGroupsPaginator",
    "DescribeUsersPaginator",
)

if TYPE_CHECKING:
    _DescribeACLsPaginatorBase = Paginator[DescribeACLsResponseTypeDef]
else:
    _DescribeACLsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeACLsPaginator(_DescribeACLsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeACLs.html#MemoryDB.Paginator.DescribeACLs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeaclspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeACLsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeACLsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeACLs.html#MemoryDB.Paginator.DescribeACLs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeaclspaginator)
        """

if TYPE_CHECKING:
    _DescribeClustersPaginatorBase = Paginator[DescribeClustersResponseTypeDef]
else:
    _DescribeClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClustersPaginator(_DescribeClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeClusters.html#MemoryDB.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeClusters.html#MemoryDB.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEngineVersionsPaginatorBase = Paginator[DescribeEngineVersionsResponseTypeDef]
else:
    _DescribeEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEngineVersionsPaginator(_DescribeEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeEngineVersions.html#MemoryDB.Paginator.DescribeEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEngineVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeEngineVersions.html#MemoryDB.Paginator.DescribeEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeengineversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[DescribeEventsResponseTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeEvents.html#MemoryDB.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeEvents.html#MemoryDB.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeMultiRegionClustersPaginatorBase = Paginator[
        DescribeMultiRegionClustersResponseTypeDef
    ]
else:
    _DescribeMultiRegionClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMultiRegionClustersPaginator(_DescribeMultiRegionClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeMultiRegionClusters.html#MemoryDB.Paginator.DescribeMultiRegionClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describemultiregionclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMultiRegionClustersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMultiRegionClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeMultiRegionClusters.html#MemoryDB.Paginator.DescribeMultiRegionClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describemultiregionclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeParameterGroupsPaginatorBase = Paginator[DescribeParameterGroupsResponseTypeDef]
else:
    _DescribeParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeParameterGroupsPaginator(_DescribeParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeParameterGroups.html#MemoryDB.Paginator.DescribeParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeParameterGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeParameterGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeParameterGroups.html#MemoryDB.Paginator.DescribeParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeParametersPaginatorBase = Paginator[DescribeParametersResponseTypeDef]
else:
    _DescribeParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeParametersPaginator(_DescribeParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeParameters.html#MemoryDB.Paginator.DescribeParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeParametersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeParametersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeParameters.html#MemoryDB.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedNodesOfferingsPaginatorBase = Paginator[
        DescribeReservedNodesOfferingsResponseTypeDef
    ]
else:
    _DescribeReservedNodesOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedNodesOfferingsPaginator(_DescribeReservedNodesOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeReservedNodesOfferings.html#MemoryDB.Paginator.DescribeReservedNodesOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodesofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedNodesOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedNodesOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeReservedNodesOfferings.html#MemoryDB.Paginator.DescribeReservedNodesOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodesofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedNodesPaginatorBase = Paginator[DescribeReservedNodesResponseTypeDef]
else:
    _DescribeReservedNodesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedNodesPaginator(_DescribeReservedNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeReservedNodes.html#MemoryDB.Paginator.DescribeReservedNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedNodesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeReservedNodes.html#MemoryDB.Paginator.DescribeReservedNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodespaginator)
        """

if TYPE_CHECKING:
    _DescribeServiceUpdatesPaginatorBase = Paginator[DescribeServiceUpdatesResponseTypeDef]
else:
    _DescribeServiceUpdatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServiceUpdatesPaginator(_DescribeServiceUpdatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeServiceUpdates.html#MemoryDB.Paginator.DescribeServiceUpdates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeserviceupdatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServiceUpdatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServiceUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeServiceUpdates.html#MemoryDB.Paginator.DescribeServiceUpdates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeserviceupdatespaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotsPaginatorBase = Paginator[DescribeSnapshotsResponseTypeDef]
else:
    _DescribeSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotsPaginator(_DescribeSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeSnapshots.html#MemoryDB.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeSnapshots.html#MemoryDB.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeSubnetGroupsPaginatorBase = Paginator[DescribeSubnetGroupsResponseTypeDef]
else:
    _DescribeSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSubnetGroupsPaginator(_DescribeSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeSubnetGroups.html#MemoryDB.Paginator.DescribeSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSubnetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeSubnetGroups.html#MemoryDB.Paginator.DescribeSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeUsersPaginatorBase = Paginator[DescribeUsersResponseTypeDef]
else:
    _DescribeUsersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUsersPaginator(_DescribeUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeUsers.html#MemoryDB.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUsersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/paginator/DescribeUsers.html#MemoryDB.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeuserspaginator)
        """
