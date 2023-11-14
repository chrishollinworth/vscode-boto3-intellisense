"""
Main interface for eks service.

Usage::

    ```python
    import boto3
    from mypy_boto3_eks import (
        AddonActiveWaiter,
        AddonDeletedWaiter,
        Client,
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        DescribeAddonVersionsPaginator,
        EKSClient,
        FargateProfileActiveWaiter,
        FargateProfileDeletedWaiter,
        ListAddonsPaginator,
        ListClustersPaginator,
        ListFargateProfilesPaginator,
        ListIdentityProviderConfigsPaginator,
        ListNodegroupsPaginator,
        ListUpdatesPaginator,
        NodegroupActiveWaiter,
        NodegroupDeletedWaiter,
    )

    session = boto3.Session()

    client: EKSClient = boto3.client("eks")
    session_client: EKSClient = session.client("eks")

    addon_active_waiter: AddonActiveWaiter = client.get_waiter("addon_active")
    addon_deleted_waiter: AddonDeletedWaiter = client.get_waiter("addon_deleted")
    cluster_active_waiter: ClusterActiveWaiter = client.get_waiter("cluster_active")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    fargate_profile_active_waiter: FargateProfileActiveWaiter = client.get_waiter("fargate_profile_active")
    fargate_profile_deleted_waiter: FargateProfileDeletedWaiter = client.get_waiter("fargate_profile_deleted")
    nodegroup_active_waiter: NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
    nodegroup_deleted_waiter: NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")

    describe_addon_versions_paginator: DescribeAddonVersionsPaginator = client.get_paginator("describe_addon_versions")
    list_addons_paginator: ListAddonsPaginator = client.get_paginator("list_addons")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_fargate_profiles_paginator: ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
    list_identity_provider_configs_paginator: ListIdentityProviderConfigsPaginator = client.get_paginator("list_identity_provider_configs")
    list_nodegroups_paginator: ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
    list_updates_paginator: ListUpdatesPaginator = client.get_paginator("list_updates")
    ```
"""
from .client import EKSClient
from .paginator import (
    DescribeAddonVersionsPaginator,
    ListAddonsPaginator,
    ListClustersPaginator,
    ListFargateProfilesPaginator,
    ListIdentityProviderConfigsPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from .waiter import (
    AddonActiveWaiter,
    AddonDeletedWaiter,
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    FargateProfileActiveWaiter,
    FargateProfileDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
)

Client = EKSClient

__all__ = (
    "AddonActiveWaiter",
    "AddonDeletedWaiter",
    "Client",
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "DescribeAddonVersionsPaginator",
    "EKSClient",
    "FargateProfileActiveWaiter",
    "FargateProfileDeletedWaiter",
    "ListAddonsPaginator",
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListIdentityProviderConfigsPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)
