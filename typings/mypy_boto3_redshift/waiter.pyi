# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for redshift service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_redshift import RedshiftClient
    from mypy_boto3_redshift.waiter import (
        ClusterAvailableWaiter,
        ClusterDeletedWaiter,
        ClusterRestoredWaiter,
        SnapshotAvailableWaiter,
    )

    client: RedshiftClient = boto3.client("redshift")

    cluster_available_waiter: ClusterAvailableWaiter = client.get_waiter("cluster_available")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    cluster_restored_waiter: ClusterRestoredWaiter = client.get_waiter("cluster_restored")
    snapshot_available_waiter: SnapshotAvailableWaiter = client.get_waiter("snapshot_available")
    ```
"""
from datetime import datetime
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_redshift.type_defs import SnapshotSortingEntityTypeDef, WaiterConfigTypeDef

__all__ = (
    "ClusterAvailableWaiter",
    "ClusterDeletedWaiter",
    "ClusterRestoredWaiter",
    "SnapshotAvailableWaiter",
)


class ClusterAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)
    """

    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ClusterAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)
    """

    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted.wait)
        """


class ClusterRestoredWaiter(Boto3Waiter):
    """
    [Waiter.ClusterRestored documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)
    """

    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ClusterRestored.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.ClusterRestored.wait)
        """


class SnapshotAvailableWaiter(Boto3Waiter):
    """
    [Waiter.SnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)
    """

    def wait(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SnapshotAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable.wait)
        """
