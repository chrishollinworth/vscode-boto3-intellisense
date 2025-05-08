"""
Type annotations for elasticache service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elasticache.client import ElastiCacheClient
    from mypy_boto3_elasticache.waiter import (
        CacheClusterAvailableWaiter,
        CacheClusterDeletedWaiter,
        ReplicationGroupAvailableWaiter,
        ReplicationGroupDeletedWaiter,
    )

    session = Session()
    client: ElastiCacheClient = session.client("elasticache")

    cache_cluster_available_waiter: CacheClusterAvailableWaiter = client.get_waiter("cache_cluster_available")
    cache_cluster_deleted_waiter: CacheClusterDeletedWaiter = client.get_waiter("cache_cluster_deleted")
    replication_group_available_waiter: ReplicationGroupAvailableWaiter = client.get_waiter("replication_group_available")
    replication_group_deleted_waiter: ReplicationGroupDeletedWaiter = client.get_waiter("replication_group_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeCacheClustersMessageWaitExtraTypeDef,
    DescribeCacheClustersMessageWaitTypeDef,
    DescribeReplicationGroupsMessageWaitExtraTypeDef,
    DescribeReplicationGroupsMessageWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "CacheClusterAvailableWaiter",
    "CacheClusterDeletedWaiter",
    "ReplicationGroupAvailableWaiter",
    "ReplicationGroupDeletedWaiter",
)

class CacheClusterAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/CacheClusterAvailable.html#ElastiCache.Waiter.CacheClusterAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#cacheclusteravailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheClustersMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/CacheClusterAvailable.html#ElastiCache.Waiter.CacheClusterAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#cacheclusteravailablewaiter)
        """

class CacheClusterDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/CacheClusterDeleted.html#ElastiCache.Waiter.CacheClusterDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#cacheclusterdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCacheClustersMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/CacheClusterDeleted.html#ElastiCache.Waiter.CacheClusterDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#cacheclusterdeletedwaiter)
        """

class ReplicationGroupAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/ReplicationGroupAvailable.html#ElastiCache.Waiter.ReplicationGroupAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#replicationgroupavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationGroupsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/ReplicationGroupAvailable.html#ElastiCache.Waiter.ReplicationGroupAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#replicationgroupavailablewaiter)
        """

class ReplicationGroupDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/ReplicationGroupDeleted.html#ElastiCache.Waiter.ReplicationGroupDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#replicationgroupdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationGroupsMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache/waiter/ReplicationGroupDeleted.html#ElastiCache.Waiter.ReplicationGroupDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/waiters/#replicationgroupdeletedwaiter)
        """
