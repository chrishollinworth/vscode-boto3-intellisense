"""
Type annotations for eks service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_eks import EKSClient
    from mypy_boto3_eks.waiter import (
        AddonActiveWaiter,
        AddonDeletedWaiter,
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        FargateProfileActiveWaiter,
        FargateProfileDeletedWaiter,
        NodegroupActiveWaiter,
        NodegroupDeletedWaiter,
    )

    client: EKSClient = boto3.client("eks")

    addon_active_waiter: AddonActiveWaiter = client.get_waiter("addon_active")
    addon_deleted_waiter: AddonDeletedWaiter = client.get_waiter("addon_deleted")
    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    fargate_profile_active_waiter: FargateProfileActiveWaiter = client.get_waiter("fargate_profile_active")
    fargate_profile_deleted_waiter: FargateProfileDeletedWaiter = client.get_waiter("fargate_profile_deleted")
    nodegroup_active_waiter: NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
    nodegroup_deleted_waiter: NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "AddonActiveWaiter",
    "AddonDeletedWaiter",
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "FargateProfileActiveWaiter",
    "FargateProfileDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)

class AddonActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.AddonActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addonactivewaiter)
    """

    def wait(
        self, *, clusterName: str, addonName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.AddonActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addonactivewaiter)
        """

class AddonDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.AddonDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addondeletedwaiter)
    """

    def wait(
        self, *, clusterName: str, addonName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.AddonDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addondeletedwaiter)
        """

class ClusterActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.ClusterActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusteractivewaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.ClusterActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusteractivewaiter)
        """

class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusterdeletedwaiter)
    """

    def wait(self, *, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.ClusterDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusterdeletedwaiter)
        """

class FargateProfileActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.FargateProfileActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofileactivewaiter)
    """

    def wait(
        self, *, clusterName: str, fargateProfileName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.FargateProfileActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofileactivewaiter)
        """

class FargateProfileDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.FargateProfileDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofiledeletedwaiter)
    """

    def wait(
        self, *, clusterName: str, fargateProfileName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.FargateProfileDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofiledeletedwaiter)
        """

class NodegroupActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.NodegroupActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupactivewaiter)
    """

    def wait(
        self, *, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.NodegroupActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupactivewaiter)
        """

class NodegroupDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupdeletedwaiter)
    """

    def wait(
        self, *, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/eks.html#EKS.Waiter.NodegroupDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupdeletedwaiter)
        """
