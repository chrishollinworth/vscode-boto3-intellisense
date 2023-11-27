"""
Type annotations for memorydb service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_memorydb import MemoryDBClient
    from mypy_boto3_memorydb.paginator import (
        DescribeACLsPaginator,
        DescribeClustersPaginator,
        DescribeEngineVersionsPaginator,
        DescribeEventsPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeReservedNodesPaginator,
        DescribeReservedNodesOfferingsPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeSubnetGroupsPaginator,
        DescribeUsersPaginator,
    )

    client: MemoryDBClient = boto3.client("memorydb")

    describe_acls_paginator: DescribeACLsPaginator = client.get_paginator("describe_acls")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_engine_versions_paginator: DescribeEngineVersionsPaginator = client.get_paginator("describe_engine_versions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_reserved_nodes_offerings_paginator: DescribeReservedNodesOfferingsPaginator = client.get_paginator("describe_reserved_nodes_offerings")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ServiceUpdateStatusType, SourceTypeType
from .type_defs import (
    DescribeACLsResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeReservedNodesOfferingsResponseTypeDef,
    DescribeReservedNodesResponseTypeDef,
    DescribeServiceUpdatesResponseTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    DescribeUsersResponseTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeACLsPaginator",
    "DescribeClustersPaginator",
    "DescribeEngineVersionsPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeReservedNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSubnetGroupsPaginator",
    "DescribeUsersPaginator",
)

class DescribeACLsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeACLs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeaclspaginator)
    """

    def paginate(
        self, *, ACLName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeACLsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeACLs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeaclspaginator)
        """

class DescribeClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeclusterspaginator)
    """

    def paginate(
        self,
        *,
        ClusterName: str = None,
        ShowShardDetails: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeclusterspaginator)
        """

class DescribeEngineVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEngineVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeengineversionspaginator)
    """

    def paginate(
        self,
        *,
        EngineVersion: str = None,
        ParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEngineVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeengineversionspaginator)
        """

class DescribeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeeventspaginator)
    """

    def paginate(
        self,
        *,
        SourceName: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeeventspaginator)
        """

class DescribeParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameterGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeparametergroupspaginator)
    """

    def paginate(
        self, *, ParameterGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParameterGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameterGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeparametergroupspaginator)
        """

class DescribeParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeparameterspaginator)
    """

    def paginate(
        self, *, ParameterGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParametersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeparameterspaginator)
        """

class DescribeReservedNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describereservednodespaginator)
    """

    def paginate(
        self,
        *,
        ReservationId: str = None,
        ReservedNodesOfferingId: str = None,
        NodeType: str = None,
        Duration: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describereservednodespaginator)
        """

class DescribeReservedNodesOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodesOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describereservednodesofferingspaginator)
    """

    def paginate(
        self,
        *,
        ReservedNodesOfferingId: str = None,
        NodeType: str = None,
        Duration: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedNodesOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodesOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describereservednodesofferingspaginator)
        """

class DescribeServiceUpdatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeServiceUpdates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeserviceupdatespaginator)
    """

    def paginate(
        self,
        *,
        ServiceUpdateName: str = None,
        ClusterNames: List[str] = None,
        Status: List[ServiceUpdateStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeServiceUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeServiceUpdates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeserviceupdatespaginator)
        """

class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describesnapshotspaginator)
    """

    def paginate(
        self,
        *,
        ClusterName: str = None,
        SnapshotName: str = None,
        Source: str = None,
        ShowDetail: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describesnapshotspaginator)
        """

class DescribeSubnetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSubnetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describesubnetgroupspaginator)
    """

    def paginate(
        self, *, SubnetGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubnetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describesubnetgroupspaginator)
        """

class DescribeUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeuserspaginator)
    """

    def paginate(
        self,
        *,
        UserName: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/memorydb.html#MemoryDB.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators.html#describeuserspaginator)
        """
