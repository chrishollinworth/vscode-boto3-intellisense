# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for eks service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_eks import EKSClient
    from mypy_boto3_eks.waiter import (
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        NodegroupActiveWaiter,
        NodegroupDeletedWaiter,
    )

    client: EKSClient = boto3.client("eks")

    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    nodegroup_active_waiter: NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
    nodegroup_deleted_waiter: NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_eks.type_defs import WaiterConfigTypeDef

__all__ = (
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)


class ClusterActiveWaiter(Boto3Waiter):
    """
    [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterActive)
    """

    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterActive.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
    """

    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterDeleted.wait)
        """


class NodegroupActiveWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupActive)
    """

    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupActive.wait)
        """


class NodegroupDeletedWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
    """

    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupDeleted.wait)
        """
