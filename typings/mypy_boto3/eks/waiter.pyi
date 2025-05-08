"""
Type annotations for eks service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_eks.client import EKSClient
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

    session = Session()
    client: EKSClient = session.client("eks")

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

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeAddonRequestWaitExtraTypeDef,
    DescribeAddonRequestWaitTypeDef,
    DescribeClusterRequestWaitExtraTypeDef,
    DescribeClusterRequestWaitTypeDef,
    DescribeFargateProfileRequestWaitExtraTypeDef,
    DescribeFargateProfileRequestWaitTypeDef,
    DescribeNodegroupRequestWaitExtraTypeDef,
    DescribeNodegroupRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

class AddonActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/AddonActive.html#EKS.Waiter.AddonActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#addonactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAddonRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/AddonActive.html#EKS.Waiter.AddonActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#addonactivewaiter)
        """

class AddonDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/AddonDeleted.html#EKS.Waiter.AddonDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#addondeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAddonRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/AddonDeleted.html#EKS.Waiter.AddonDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#addondeletedwaiter)
        """

class ClusterActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/ClusterActive.html#EKS.Waiter.ClusterActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#clusteractivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/ClusterActive.html#EKS.Waiter.ClusterActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#clusteractivewaiter)
        """

class ClusterDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/ClusterDeleted.html#EKS.Waiter.ClusterDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#clusterdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/ClusterDeleted.html#EKS.Waiter.ClusterDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#clusterdeletedwaiter)
        """

class FargateProfileActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/FargateProfileActive.html#EKS.Waiter.FargateProfileActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#fargateprofileactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFargateProfileRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/FargateProfileActive.html#EKS.Waiter.FargateProfileActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#fargateprofileactivewaiter)
        """

class FargateProfileDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/FargateProfileDeleted.html#EKS.Waiter.FargateProfileDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#fargateprofiledeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFargateProfileRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/FargateProfileDeleted.html#EKS.Waiter.FargateProfileDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#fargateprofiledeletedwaiter)
        """

class NodegroupActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/NodegroupActive.html#EKS.Waiter.NodegroupActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#nodegroupactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNodegroupRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/NodegroupActive.html#EKS.Waiter.NodegroupActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#nodegroupactivewaiter)
        """

class NodegroupDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/NodegroupDeleted.html#EKS.Waiter.NodegroupDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#nodegroupdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNodegroupRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/waiter/NodegroupDeleted.html#EKS.Waiter.NodegroupDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters/#nodegroupdeletedwaiter)
        """
