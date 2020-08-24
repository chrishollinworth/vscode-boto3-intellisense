# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for elasticache service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_elasticache import ElastiCacheClient
    from mypy_boto3_elasticache.waiter import (
        CacheClusterAvailableWaiter,
        CacheClusterDeletedWaiter,
        ReplicationGroupAvailableWaiter,
        ReplicationGroupDeletedWaiter,
    )

    client: ElastiCacheClient = boto3.client("elasticache")

    cache_cluster_available_waiter: CacheClusterAvailableWaiter = client.get_waiter("cache_cluster_available")
    cache_cluster_deleted_waiter: CacheClusterDeletedWaiter = client.get_waiter("cache_cluster_deleted")
    replication_group_available_waiter: ReplicationGroupAvailableWaiter = client.get_waiter("replication_group_available")
    replication_group_deleted_waiter: ReplicationGroupDeletedWaiter = client.get_waiter("replication_group_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_elasticache.type_defs import WaiterConfigTypeDef

__all__ = (
    "CacheClusterAvailableWaiter",
    "CacheClusterDeletedWaiter",
    "ReplicationGroupAvailableWaiter",
    "ReplicationGroupDeletedWaiter",
)


class CacheClusterAvailableWaiter(Boto3Waiter):
    """
    [Waiter.CacheClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)
    """

    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CacheClusterAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable.wait)
        """


class CacheClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.CacheClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)
    """

    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CacheClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted.wait)
        """


class ReplicationGroupAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationGroupAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)
    """

    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationGroupAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable.wait)
        """


class ReplicationGroupDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationGroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)
    """

    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationGroupDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted.wait)
        """
