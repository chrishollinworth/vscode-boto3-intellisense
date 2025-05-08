"""
Type annotations for redshift service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_redshift.client import RedshiftClient
    from mypy_boto3_redshift.waiter import (
        ClusterAvailableWaiter,
        ClusterDeletedWaiter,
        ClusterRestoredWaiter,
        SnapshotAvailableWaiter,
    )

    session = Session()
    client: RedshiftClient = session.client("redshift")

    cluster_available_waiter: ClusterAvailableWaiter = client.get_waiter("cluster_available")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    cluster_restored_waiter: ClusterRestoredWaiter = client.get_waiter("cluster_restored")
    snapshot_available_waiter: SnapshotAvailableWaiter = client.get_waiter("snapshot_available")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeClustersMessageWaitExtraExtraTypeDef,
    DescribeClustersMessageWaitExtraTypeDef,
    DescribeClustersMessageWaitTypeDef,
    DescribeClusterSnapshotsMessageWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ClusterAvailableWaiter",
    "ClusterDeletedWaiter",
    "ClusterRestoredWaiter",
    "SnapshotAvailableWaiter",
)

class ClusterAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterAvailable.html#Redshift.Waiter.ClusterAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusteravailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterAvailable.html#Redshift.Waiter.ClusterAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusteravailablewaiter)
        """

class ClusterDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterDeleted.html#Redshift.Waiter.ClusterDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusterdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterDeleted.html#Redshift.Waiter.ClusterDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusterdeletedwaiter)
        """

class ClusterRestoredWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterRestored.html#Redshift.Waiter.ClusterRestored)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusterrestoredwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersMessageWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/ClusterRestored.html#Redshift.Waiter.ClusterRestored.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#clusterrestoredwaiter)
        """

class SnapshotAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/SnapshotAvailable.html#Redshift.Waiter.SnapshotAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#snapshotavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterSnapshotsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/waiter/SnapshotAvailable.html#Redshift.Waiter.SnapshotAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters/#snapshotavailablewaiter)
        """
