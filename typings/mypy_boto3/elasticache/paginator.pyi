"""
Type annotations for elasticache service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elasticache.client import ElastiCacheClient
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
        DescribeReservedCacheNodesOfferingsPaginator,
        DescribeReservedCacheNodesPaginator,
        DescribeServerlessCacheSnapshotsPaginator,
        DescribeServerlessCachesPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeUpdateActionsPaginator,
        DescribeUserGroupsPaginator,
        DescribeUsersPaginator,
    )

    session = Session()
    client: ElastiCacheClient = session.client("elasticache")

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
    describe_reserved_cache_nodes_offerings_paginator: DescribeReservedCacheNodesOfferingsPaginator = client.get_paginator("describe_reserved_cache_nodes_offerings")
    describe_reserved_cache_nodes_paginator: DescribeReservedCacheNodesPaginator = client.get_paginator("describe_reserved_cache_nodes")
    describe_serverless_cache_snapshots_paginator: DescribeServerlessCacheSnapshotsPaginator = client.get_paginator("describe_serverless_cache_snapshots")
    describe_serverless_caches_paginator: DescribeServerlessCachesPaginator = client.get_paginator("describe_serverless_caches")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_update_actions_paginator: DescribeUpdateActionsPaginator = client.get_paginator("describe_update_actions")
    describe_user_groups_paginator: DescribeUserGroupsPaginator = client.get_paginator("describe_user_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    DescribeCacheClustersMessagePaginateTypeDef,
    DescribeCacheEngineVersionsMessagePaginateTypeDef,
    DescribeCacheParameterGroupsMessagePaginateTypeDef,
    DescribeCacheParametersMessagePaginateTypeDef,
    DescribeCacheSecurityGroupsMessagePaginateTypeDef,
    DescribeCacheSubnetGroupsMessagePaginateTypeDef,
    DescribeEngineDefaultParametersMessagePaginateTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    DescribeGlobalReplicationGroupsMessagePaginateTypeDef,
    DescribeGlobalReplicationGroupsResultTypeDef,
    DescribeReplicationGroupsMessagePaginateTypeDef,
    DescribeReservedCacheNodesMessagePaginateTypeDef,
    DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef,
    DescribeServerlessCacheSnapshotsRequestPaginateTypeDef,
    DescribeServerlessCacheSnapshotsResponseTypeDef,
    DescribeServerlessCachesRequestPaginateTypeDef,
    DescribeServerlessCachesResponseTypeDef,
    DescribeServiceUpdatesMessagePaginateTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    DescribeSnapshotsMessagePaginateTypeDef,
    DescribeUpdateActionsMessagePaginateTypeDef,
    DescribeUserGroupsMessagePaginateTypeDef,
    DescribeUserGroupsResultTypeDef,
    DescribeUsersMessagePaginateTypeDef,
    DescribeUsersResultTypeDef,
    EventsMessageTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ServiceUpdatesMessageTypeDef,
    UpdateActionsMessageTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
    "DescribeReservedCacheNodesOfferingsPaginator",
    "DescribeReservedCacheNodesPaginator",
    "DescribeServerlessCacheSnapshotsPaginator",
    "DescribeServerlessCachesPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeUpdateActionsPaginator",
    "DescribeUserGroupsPaginator",
    "DescribeUsersPaginator",
)

if TYPE_CHECKING:
    _DescribeCacheClustersPaginatorBase = Paginator[CacheClusterMessageTypeDef]
else:
    _DescribeCacheClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheClustersPaginator(_DescribeCacheClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheClusters.html#ElastiCache.Paginator.DescribeCacheClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheClustersMessagePaginateTypeDef]
    ) -> PageIterator[CacheClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheClusters.html#ElastiCache.Paginator.DescribeCacheClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeCacheEngineVersionsPaginatorBase = Paginator[CacheEngineVersionMessageTypeDef]
else:
    _DescribeCacheEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheEngineVersionsPaginator(_DescribeCacheEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheEngineVersions.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheEngineVersionsMessagePaginateTypeDef]
    ) -> PageIterator[CacheEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheEngineVersions.html#ElastiCache.Paginator.DescribeCacheEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheengineversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeCacheParameterGroupsPaginatorBase = Paginator[CacheParameterGroupsMessageTypeDef]
else:
    _DescribeCacheParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheParameterGroupsPaginator(_DescribeCacheParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheParameterGroups.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[CacheParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheParameterGroups.html#ElastiCache.Paginator.DescribeCacheParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeCacheParametersPaginatorBase = Paginator[CacheParameterGroupDetailsTypeDef]
else:
    _DescribeCacheParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheParametersPaginator(_DescribeCacheParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheParameters.html#ElastiCache.Paginator.DescribeCacheParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheParametersMessagePaginateTypeDef]
    ) -> PageIterator[CacheParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheParameters.html#ElastiCache.Paginator.DescribeCacheParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecacheparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeCacheSecurityGroupsPaginatorBase = Paginator[CacheSecurityGroupMessageTypeDef]
else:
    _DescribeCacheSecurityGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheSecurityGroupsPaginator(_DescribeCacheSecurityGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheSecurityGroups.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecachesecuritygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheSecurityGroupsMessagePaginateTypeDef]
    ) -> PageIterator[CacheSecurityGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheSecurityGroups.html#ElastiCache.Paginator.DescribeCacheSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecachesecuritygroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeCacheSubnetGroupsPaginatorBase = Paginator[CacheSubnetGroupMessageTypeDef]
else:
    _DescribeCacheSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCacheSubnetGroupsPaginator(_DescribeCacheSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheSubnetGroups.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecachesubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[CacheSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeCacheSubnetGroups.html#ElastiCache.Paginator.DescribeCacheSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describecachesubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator[
        DescribeEngineDefaultParametersResultTypeDef
    ]
else:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEngineDefaultParametersPaginator(_DescribeEngineDefaultParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeEngineDefaultParameters.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeenginedefaultparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeEngineDefaultParameters.html#ElastiCache.Paginator.DescribeEngineDefaultParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeenginedefaultparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeEvents.html#ElastiCache.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeEvents.html#ElastiCache.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeGlobalReplicationGroupsPaginatorBase = Paginator[
        DescribeGlobalReplicationGroupsResultTypeDef
    ]
else:
    _DescribeGlobalReplicationGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGlobalReplicationGroupsPaginator(_DescribeGlobalReplicationGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeGlobalReplicationGroups.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeglobalreplicationgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGlobalReplicationGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeGlobalReplicationGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeGlobalReplicationGroups.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeglobalreplicationgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationGroupsPaginatorBase = Paginator[ReplicationGroupMessageTypeDef]
else:
    _DescribeReplicationGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationGroupsPaginator(_DescribeReplicationGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReplicationGroups.html#ElastiCache.Paginator.DescribeReplicationGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereplicationgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationGroupsMessagePaginateTypeDef]
    ) -> PageIterator[ReplicationGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReplicationGroups.html#ElastiCache.Paginator.DescribeReplicationGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereplicationgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedCacheNodesOfferingsPaginatorBase = Paginator[
        ReservedCacheNodesOfferingMessageTypeDef
    ]
else:
    _DescribeReservedCacheNodesOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedCacheNodesOfferingsPaginator(
    _DescribeReservedCacheNodesOfferingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReservedCacheNodesOfferings.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereservedcachenodesofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef]
    ) -> PageIterator[ReservedCacheNodesOfferingMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReservedCacheNodesOfferings.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereservedcachenodesofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedCacheNodesPaginatorBase = Paginator[ReservedCacheNodeMessageTypeDef]
else:
    _DescribeReservedCacheNodesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedCacheNodesPaginator(_DescribeReservedCacheNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReservedCacheNodes.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereservedcachenodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedCacheNodesMessagePaginateTypeDef]
    ) -> PageIterator[ReservedCacheNodeMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeReservedCacheNodes.html#ElastiCache.Paginator.DescribeReservedCacheNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describereservedcachenodespaginator)
        """

if TYPE_CHECKING:
    _DescribeServerlessCacheSnapshotsPaginatorBase = Paginator[
        DescribeServerlessCacheSnapshotsResponseTypeDef
    ]
else:
    _DescribeServerlessCacheSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServerlessCacheSnapshotsPaginator(_DescribeServerlessCacheSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServerlessCacheSnapshots.html#ElastiCache.Paginator.DescribeServerlessCacheSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserverlesscachesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServerlessCacheSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServerlessCacheSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServerlessCacheSnapshots.html#ElastiCache.Paginator.DescribeServerlessCacheSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserverlesscachesnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeServerlessCachesPaginatorBase = Paginator[DescribeServerlessCachesResponseTypeDef]
else:
    _DescribeServerlessCachesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServerlessCachesPaginator(_DescribeServerlessCachesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServerlessCaches.html#ElastiCache.Paginator.DescribeServerlessCaches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserverlesscachespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServerlessCachesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServerlessCachesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServerlessCaches.html#ElastiCache.Paginator.DescribeServerlessCaches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserverlesscachespaginator)
        """

if TYPE_CHECKING:
    _DescribeServiceUpdatesPaginatorBase = Paginator[ServiceUpdatesMessageTypeDef]
else:
    _DescribeServiceUpdatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServiceUpdatesPaginator(_DescribeServiceUpdatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServiceUpdates.html#ElastiCache.Paginator.DescribeServiceUpdates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserviceupdatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServiceUpdatesMessagePaginateTypeDef]
    ) -> PageIterator[ServiceUpdatesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeServiceUpdates.html#ElastiCache.Paginator.DescribeServiceUpdates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeserviceupdatespaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotsPaginatorBase = Paginator[DescribeSnapshotsListMessageTypeDef]
else:
    _DescribeSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotsPaginator(_DescribeSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeSnapshots.html#ElastiCache.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotsListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeSnapshots.html#ElastiCache.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describesnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeUpdateActionsPaginatorBase = Paginator[UpdateActionsMessageTypeDef]
else:
    _DescribeUpdateActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUpdateActionsPaginator(_DescribeUpdateActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUpdateActions.html#ElastiCache.Paginator.DescribeUpdateActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeupdateactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUpdateActionsMessagePaginateTypeDef]
    ) -> PageIterator[UpdateActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUpdateActions.html#ElastiCache.Paginator.DescribeUpdateActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeupdateactionspaginator)
        """

if TYPE_CHECKING:
    _DescribeUserGroupsPaginatorBase = Paginator[DescribeUserGroupsResultTypeDef]
else:
    _DescribeUserGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUserGroupsPaginator(_DescribeUserGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUserGroups.html#ElastiCache.Paginator.DescribeUserGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeusergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUserGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeUserGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUserGroups.html#ElastiCache.Paginator.DescribeUserGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeusergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeUsersPaginatorBase = Paginator[DescribeUsersResultTypeDef]
else:
    _DescribeUsersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUsersPaginator(_DescribeUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUsers.html#ElastiCache.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUsersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeUsersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/paginator/DescribeUsers.html#ElastiCache.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/paginators/#describeuserspaginator)
        """
