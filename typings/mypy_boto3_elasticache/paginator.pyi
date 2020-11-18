# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for elasticache service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_elasticache import ElastiCacheClient
    from mypy_boto3_elasticache.paginator import (
        DescribeCacheClustersPaginator,
        DescribeCacheEngineVersionsPaginator,
        DescribeCacheParameterGroupsPaginator,
        DescribeCacheParametersPaginator,
        DescribeCacheSecurityGroupsPaginator,
        DescribeCacheSubnetGroupsPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventsPaginator,
        DescribeGlobalReplicationGroupsPaginator,
        DescribeReplicationGroupsPaginator,
        DescribeReservedCacheNodesPaginator,
        DescribeReservedCacheNodesOfferingsPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeUpdateActionsPaginator,
        DescribeUserGroupsPaginator,
        DescribeUsersPaginator,
    )

    client: ElastiCacheClient = boto3.client("elasticache")

    describe_cache_clusters_paginator: DescribeCacheClustersPaginator = client.get_paginator("describe_cache_clusters")
    describe_cache_engine_versions_paginator: DescribeCacheEngineVersionsPaginator = client.get_paginator("describe_cache_engine_versions")
    describe_cache_parameter_groups_paginator: DescribeCacheParameterGroupsPaginator = client.get_paginator("describe_cache_parameter_groups")
    describe_cache_parameters_paginator: DescribeCacheParametersPaginator = client.get_paginator("describe_cache_parameters")
    describe_cache_security_groups_paginator: DescribeCacheSecurityGroupsPaginator = client.get_paginator("describe_cache_security_groups")
    describe_cache_subnet_groups_paginator: DescribeCacheSubnetGroupsPaginator = client.get_paginator("describe_cache_subnet_groups")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_global_replication_groups_paginator: DescribeGlobalReplicationGroupsPaginator = client.get_paginator("describe_global_replication_groups")
    describe_replication_groups_paginator: DescribeReplicationGroupsPaginator = client.get_paginator("describe_replication_groups")
    describe_reserved_cache_nodes_paginator: DescribeReservedCacheNodesPaginator = client.get_paginator("describe_reserved_cache_nodes")
    describe_reserved_cache_nodes_offerings_paginator: DescribeReservedCacheNodesOfferingsPaginator = client.get_paginator("describe_reserved_cache_nodes_offerings")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_update_actions_paginator: DescribeUpdateActionsPaginator = client.get_paginator("describe_update_actions")
    describe_user_groups_paginator: DescribeUserGroupsPaginator = client.get_paginator("describe_user_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_elasticache.type_defs import (
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeGlobalReplicationGroupsResultTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    DescribeUserGroupsResultTypeDef,
    DescribeUsersResultTypeDef,
    EventsMessageTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ServiceUpdatesMessageTypeDef,
    TimeRangeFilterTypeDef,
    UpdateActionsMessageTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCacheClustersPaginator",
    "DescribeCacheEngineVersionsPaginator",
    "DescribeCacheParameterGroupsPaginator",
    "DescribeCacheParametersPaginator",
    "DescribeCacheSecurityGroupsPaginator",
    "DescribeCacheSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalReplicationGroupsPaginator",
    "DescribeReplicationGroupsPaginator",
    "DescribeReservedCacheNodesPaginator",
    "DescribeReservedCacheNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeUpdateActionsPaginator",
    "DescribeUserGroupsPaginator",
    "DescribeUsersPaginator",
)


class DescribeCacheClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)
    """

    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheClusterMessageTypeDef]:
        """
        [DescribeCacheClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters.paginate)
        """


class DescribeCacheEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
    """

    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheEngineVersionMessageTypeDef]:
        """
        [DescribeCacheEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions.paginate)
        """


class DescribeCacheParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
    """

    def paginate(
        self, CacheParameterGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheParameterGroupsMessageTypeDef]:
        """
        [DescribeCacheParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups.paginate)
        """


class DescribeCacheParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)
    """

    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CacheParameterGroupDetailsTypeDef]:
        """
        [DescribeCacheParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters.paginate)
        """


class DescribeCacheSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
    """

    def paginate(
        self, CacheSecurityGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSecurityGroupMessageTypeDef]:
        """
        [DescribeCacheSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups.paginate)
        """


class DescribeCacheSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
    """

    def paginate(
        self, CacheSubnetGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSubnetGroupMessageTypeDef]:
        """
        [DescribeCacheSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
    """

    def paginate(
        self, CacheParameterGroupFamily: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
            "user",
            "user-group",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents.paginate)
        """


class DescribeGlobalReplicationGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)
    """

    def paginate(
        self,
        GlobalReplicationGroupId: str = None,
        ShowMemberInfo: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeGlobalReplicationGroupsResultTypeDef]:
        """
        [DescribeGlobalReplicationGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups.paginate)
        """


class DescribeReplicationGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)
    """

    def paginate(
        self, ReplicationGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReplicationGroupMessageTypeDef]:
        """
        [DescribeReplicationGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups.paginate)
        """


class DescribeReservedCacheNodesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedCacheNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
    """

    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedCacheNodeMessageTypeDef]:
        """
        [DescribeReservedCacheNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes.paginate)
        """


class DescribeReservedCacheNodesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedCacheNodesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
    """

    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedCacheNodesOfferingMessageTypeDef]:
        """
        [DescribeReservedCacheNodesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings.paginate)
        """


class DescribeServiceUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServiceUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)
    """

    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ServiceUpdatesMessageTypeDef]:
        """
        [DescribeServiceUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)
    """

    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSnapshotsListMessageTypeDef]:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots.paginate)
        """


class DescribeUpdateActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUpdateActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)
    """

    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
        UpdateActionStatus: List[
            Literal[
                "not-applied",
                "waiting-to-start",
                "in-progress",
                "stopping",
                "stopped",
                "complete",
                "scheduling",
                "scheduled",
                "not-applicable",
            ]
        ] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[UpdateActionsMessageTypeDef]:
        """
        [DescribeUpdateActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions.paginate)
        """


class DescribeUserGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUserGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups)
    """

    def paginate(
        self, UserGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUserGroupsResultTypeDef]:
        """
        [DescribeUserGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers)
    """

    def paginate(
        self,
        Engine: str = None,
        UserId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeUsersResultTypeDef]:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers.paginate)
        """
