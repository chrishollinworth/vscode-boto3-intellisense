"""
Main interface for eks service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_eks import EKSClient
    from mypy_boto3_eks.waiter import (
        AddonActiveWaiter,
        AddonDeletedWaiter,
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        NodegroupActiveWaiter,
        NodegroupDeletedWaiter,
    )

    client: EKSClient = boto3.client("eks")

    addon_active_waiter: AddonActiveWaiter = client.get_waiter("addon_active")
    addon_deleted_waiter: AddonDeletedWaiter = client.get_waiter("addon_deleted")
    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    nodegroup_active_waiter: NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
    nodegroup_deleted_waiter: NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_eks.type_defs import WaiterConfigTypeDef

__all__ = (
    "AddonActiveWaiter",
    "AddonDeletedWaiter",
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)


class AddonActiveWaiter(Boto3Waiter):
    """
    [Waiter.AddonActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.AddonActive)
    """

    def wait(
        self, clusterName: str, addonName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [AddonActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.AddonActive.wait)
        """


class AddonDeletedWaiter(Boto3Waiter):
    """
    [Waiter.AddonDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.AddonDeleted)
    """

    def wait(
        self, clusterName: str, addonName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [AddonDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.AddonDeleted.wait)
        """


class ClusterActiveWaiter(Boto3Waiter):
    """
    [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.ClusterActive)
    """

    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.ClusterActive.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
    """

    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.ClusterDeleted.wait)
        """


class NodegroupActiveWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.NodegroupActive)
    """

    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.NodegroupActive.wait)
        """


class NodegroupDeletedWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
    """

    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Waiter.NodegroupDeleted.wait)
        """
