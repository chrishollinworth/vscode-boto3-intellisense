"""
Main interface for eks service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_eks import (
        AddonActiveWaiter,
        AddonDeletedWaiter,
        Client,
        ClusterActiveWaiter,
        ClusterDeletedWaiter,
        DescribeAddonVersionsPaginator,
        DescribeClusterVersionsPaginator,
        EKSClient,
        FargateProfileActiveWaiter,
        FargateProfileDeletedWaiter,
        ListAccessEntriesPaginator,
        ListAccessPoliciesPaginator,
        ListAddonsPaginator,
        ListAssociatedAccessPoliciesPaginator,
        ListClustersPaginator,
        ListEksAnywhereSubscriptionsPaginator,
        ListFargateProfilesPaginator,
        ListIdentityProviderConfigsPaginator,
        ListInsightsPaginator,
        ListNodegroupsPaginator,
        ListPodIdentityAssociationsPaginator,
        ListUpdatesPaginator,
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

    describe_addon_versions_paginator: DescribeAddonVersionsPaginator = client.get_paginator("describe_addon_versions")
    describe_cluster_versions_paginator: DescribeClusterVersionsPaginator = client.get_paginator("describe_cluster_versions")
    list_access_entries_paginator: ListAccessEntriesPaginator = client.get_paginator("list_access_entries")
    list_access_policies_paginator: ListAccessPoliciesPaginator = client.get_paginator("list_access_policies")
    list_addons_paginator: ListAddonsPaginator = client.get_paginator("list_addons")
    list_associated_access_policies_paginator: ListAssociatedAccessPoliciesPaginator = client.get_paginator("list_associated_access_policies")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_eks_anywhere_subscriptions_paginator: ListEksAnywhereSubscriptionsPaginator = client.get_paginator("list_eks_anywhere_subscriptions")
    list_fargate_profiles_paginator: ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
    list_identity_provider_configs_paginator: ListIdentityProviderConfigsPaginator = client.get_paginator("list_identity_provider_configs")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_nodegroups_paginator: ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
    list_pod_identity_associations_paginator: ListPodIdentityAssociationsPaginator = client.get_paginator("list_pod_identity_associations")
    list_updates_paginator: ListUpdatesPaginator = client.get_paginator("list_updates")
    ```
"""

from .client import EKSClient
from .paginator import (
    DescribeAddonVersionsPaginator,
    DescribeClusterVersionsPaginator,
    ListAccessEntriesPaginator,
    ListAccessPoliciesPaginator,
    ListAddonsPaginator,
    ListAssociatedAccessPoliciesPaginator,
    ListClustersPaginator,
    ListEksAnywhereSubscriptionsPaginator,
    ListFargateProfilesPaginator,
    ListIdentityProviderConfigsPaginator,
    ListInsightsPaginator,
    ListNodegroupsPaginator,
    ListPodIdentityAssociationsPaginator,
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
    "DescribeClusterVersionsPaginator",
    "EKSClient",
    "FargateProfileActiveWaiter",
    "FargateProfileDeletedWaiter",
    "ListAccessEntriesPaginator",
    "ListAccessPoliciesPaginator",
    "ListAddonsPaginator",
    "ListAssociatedAccessPoliciesPaginator",
    "ListClustersPaginator",
    "ListEksAnywhereSubscriptionsPaginator",
    "ListFargateProfilesPaginator",
    "ListIdentityProviderConfigsPaginator",
    "ListInsightsPaginator",
    "ListNodegroupsPaginator",
    "ListPodIdentityAssociationsPaginator",
    "ListUpdatesPaginator",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)
