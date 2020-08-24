"""
Main interface for eks service.

Usage::

    ```python
    import boto3
    from mypy_boto3_eks import (
        Client,
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        EKSClient,
        ListClustersPaginator,
        ListFargateProfilesPaginator,
        ListNodegroupsPaginator,
        ListUpdatesPaginator,
        NodegroupActiveWaiter,
        NodegroupDeletedWaiter,
    )

    session = boto3.Session()

    client: EKSClient = boto3.client("eks")
    session_client: EKSClient = session.client("eks")

    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    nodegroup_active_waiter: NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
    nodegroup_deleted_waiter: NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")

    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_fargate_profiles_paginator: ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
    list_nodegroups_paginator: ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
    list_updates_paginator: ListUpdatesPaginator = client.get_paginator("list_updates")
    ```
"""
from mypy_boto3_eks.client import EKSClient
from mypy_boto3_eks.paginator import (
    ListClustersPaginator,
    ListFargateProfilesPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from mypy_boto3_eks.waiter import (
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
)

Client = EKSClient


__all__ = (
    "Client",
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "EKSClient",
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)
