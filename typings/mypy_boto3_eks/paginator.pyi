"""
Type annotations for eks service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_eks.client import EKSClient
    from mypy_boto3_eks.paginator import (
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

    session = Session()
    client: EKSClient = session.client("eks")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAddonVersionsRequestPaginateTypeDef,
    DescribeAddonVersionsResponseTypeDef,
    DescribeClusterVersionsRequestPaginateTypeDef,
    DescribeClusterVersionsResponseTypeDef,
    ListAccessEntriesRequestPaginateTypeDef,
    ListAccessEntriesResponseTypeDef,
    ListAccessPoliciesRequestPaginateTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAddonsRequestPaginateTypeDef,
    ListAddonsResponseTypeDef,
    ListAssociatedAccessPoliciesRequestPaginateTypeDef,
    ListAssociatedAccessPoliciesResponseTypeDef,
    ListClustersRequestPaginateTypeDef,
    ListClustersResponseTypeDef,
    ListEksAnywhereSubscriptionsRequestPaginateTypeDef,
    ListEksAnywhereSubscriptionsResponseTypeDef,
    ListFargateProfilesRequestPaginateTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsRequestPaginateTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListInsightsRequestPaginateTypeDef,
    ListInsightsResponseTypeDef,
    ListNodegroupsRequestPaginateTypeDef,
    ListNodegroupsResponseTypeDef,
    ListPodIdentityAssociationsRequestPaginateTypeDef,
    ListPodIdentityAssociationsResponseTypeDef,
    ListUpdatesRequestPaginateTypeDef,
    ListUpdatesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAddonVersionsPaginator",
    "DescribeClusterVersionsPaginator",
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
)

if TYPE_CHECKING:
    _DescribeAddonVersionsPaginatorBase = Paginator[DescribeAddonVersionsResponseTypeDef]
else:
    _DescribeAddonVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAddonVersionsPaginator(_DescribeAddonVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/DescribeAddonVersions.html#EKS.Paginator.DescribeAddonVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#describeaddonversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAddonVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAddonVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/DescribeAddonVersions.html#EKS.Paginator.DescribeAddonVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#describeaddonversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterVersionsPaginatorBase = Paginator[DescribeClusterVersionsResponseTypeDef]
else:
    _DescribeClusterVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterVersionsPaginator(_DescribeClusterVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/DescribeClusterVersions.html#EKS.Paginator.DescribeClusterVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#describeclusterversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClusterVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/DescribeClusterVersions.html#EKS.Paginator.DescribeClusterVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#describeclusterversionspaginator)
        """

if TYPE_CHECKING:
    _ListAccessEntriesPaginatorBase = Paginator[ListAccessEntriesResponseTypeDef]
else:
    _ListAccessEntriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessEntriesPaginator(_ListAccessEntriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAccessEntries.html#EKS.Paginator.ListAccessEntries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaccessentriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessEntriesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAccessEntries.html#EKS.Paginator.ListAccessEntries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaccessentriespaginator)
        """

if TYPE_CHECKING:
    _ListAccessPoliciesPaginatorBase = Paginator[ListAccessPoliciesResponseTypeDef]
else:
    _ListAccessPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPoliciesPaginator(_ListAccessPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAccessPolicies.html#EKS.Paginator.ListAccessPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaccesspoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAccessPolicies.html#EKS.Paginator.ListAccessPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaccesspoliciespaginator)
        """

if TYPE_CHECKING:
    _ListAddonsPaginatorBase = Paginator[ListAddonsResponseTypeDef]
else:
    _ListAddonsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAddonsPaginator(_ListAddonsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAddons.html#EKS.Paginator.ListAddons)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaddonspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAddonsRequestPaginateTypeDef]
    ) -> PageIterator[ListAddonsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAddons.html#EKS.Paginator.ListAddons.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listaddonspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedAccessPoliciesPaginatorBase = Paginator[
        ListAssociatedAccessPoliciesResponseTypeDef
    ]
else:
    _ListAssociatedAccessPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedAccessPoliciesPaginator(_ListAssociatedAccessPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAssociatedAccessPolicies.html#EKS.Paginator.ListAssociatedAccessPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listassociatedaccesspoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedAccessPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedAccessPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListAssociatedAccessPolicies.html#EKS.Paginator.ListAssociatedAccessPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listassociatedaccesspoliciespaginator)
        """

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersResponseTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListClusters.html#EKS.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListClusters.html#EKS.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListEksAnywhereSubscriptionsPaginatorBase = Paginator[
        ListEksAnywhereSubscriptionsResponseTypeDef
    ]
else:
    _ListEksAnywhereSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEksAnywhereSubscriptionsPaginator(_ListEksAnywhereSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListEksAnywhereSubscriptions.html#EKS.Paginator.ListEksAnywhereSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listeksanywheresubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEksAnywhereSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListEksAnywhereSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListEksAnywhereSubscriptions.html#EKS.Paginator.ListEksAnywhereSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listeksanywheresubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListFargateProfilesPaginatorBase = Paginator[ListFargateProfilesResponseTypeDef]
else:
    _ListFargateProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFargateProfilesPaginator(_ListFargateProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListFargateProfiles.html#EKS.Paginator.ListFargateProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listfargateprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFargateProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListFargateProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListFargateProfiles.html#EKS.Paginator.ListFargateProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listfargateprofilespaginator)
        """

if TYPE_CHECKING:
    _ListIdentityProviderConfigsPaginatorBase = Paginator[
        ListIdentityProviderConfigsResponseTypeDef
    ]
else:
    _ListIdentityProviderConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentityProviderConfigsPaginator(_ListIdentityProviderConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListIdentityProviderConfigs.html#EKS.Paginator.ListIdentityProviderConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listidentityproviderconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentityProviderConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListIdentityProviderConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListIdentityProviderConfigs.html#EKS.Paginator.ListIdentityProviderConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listidentityproviderconfigspaginator)
        """

if TYPE_CHECKING:
    _ListInsightsPaginatorBase = Paginator[ListInsightsResponseTypeDef]
else:
    _ListInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInsightsPaginator(_ListInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListInsights.html#EKS.Paginator.ListInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInsightsRequestPaginateTypeDef]
    ) -> PageIterator[ListInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListInsights.html#EKS.Paginator.ListInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listinsightspaginator)
        """

if TYPE_CHECKING:
    _ListNodegroupsPaginatorBase = Paginator[ListNodegroupsResponseTypeDef]
else:
    _ListNodegroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNodegroupsPaginator(_ListNodegroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListNodegroups.html#EKS.Paginator.ListNodegroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listnodegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNodegroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListNodegroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListNodegroups.html#EKS.Paginator.ListNodegroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listnodegroupspaginator)
        """

if TYPE_CHECKING:
    _ListPodIdentityAssociationsPaginatorBase = Paginator[
        ListPodIdentityAssociationsResponseTypeDef
    ]
else:
    _ListPodIdentityAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPodIdentityAssociationsPaginator(_ListPodIdentityAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListPodIdentityAssociations.html#EKS.Paginator.ListPodIdentityAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listpodidentityassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPodIdentityAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListPodIdentityAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListPodIdentityAssociations.html#EKS.Paginator.ListPodIdentityAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listpodidentityassociationspaginator)
        """

if TYPE_CHECKING:
    _ListUpdatesPaginatorBase = Paginator[ListUpdatesResponseTypeDef]
else:
    _ListUpdatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListUpdatesPaginator(_ListUpdatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListUpdates.html#EKS.Paginator.ListUpdates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listupdatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUpdatesRequestPaginateTypeDef]
    ) -> PageIterator[ListUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/paginator/ListUpdates.html#EKS.Paginator.ListUpdates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators/#listupdatespaginator)
        """
