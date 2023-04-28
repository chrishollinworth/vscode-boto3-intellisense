"""
Type annotations for eks service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_eks import EKSClient
    from mypy_boto3_eks.paginator import (
        DescribeAddonVersionsPaginator,
        ListAddonsPaginator,
        ListClustersPaginator,
        ListFargateProfilesPaginator,
        ListIdentityProviderConfigsPaginator,
        ListNodegroupsPaginator,
        ListUpdatesPaginator,
    )

    client: EKSClient = boto3.client("eks")

    describe_addon_versions_paginator: DescribeAddonVersionsPaginator = client.get_paginator("describe_addon_versions")
    list_addons_paginator: ListAddonsPaginator = client.get_paginator("list_addons")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_fargate_profiles_paginator: ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
    list_identity_provider_configs_paginator: ListIdentityProviderConfigsPaginator = client.get_paginator("list_identity_provider_configs")
    list_nodegroups_paginator: ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
    list_updates_paginator: ListUpdatesPaginator = client.get_paginator("list_updates")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeAddonVersionsResponseTypeDef,
    ListAddonsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListUpdatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAddonVersionsPaginator",
    "ListAddonsPaginator",
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListIdentityProviderConfigsPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
)

class DescribeAddonVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#describeaddonversionspaginator)
    """

    def paginate(
        self,
        *,
        kubernetesVersion: str = None,
        addonName: str = None,
        types: List[str] = None,
        publishers: List[str] = None,
        owners: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddonVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#describeaddonversionspaginator)
        """

class ListAddonsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListAddons)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaddonspaginator)
    """

    def paginate(
        self, *, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAddonsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListAddons.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaddonspaginator)
        """

class ListClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listclusterspaginator)
    """

    def paginate(
        self, *, include: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listclusterspaginator)
        """

class ListFargateProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listfargateprofilespaginator)
    """

    def paginate(
        self, *, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFargateProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListFargateProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listfargateprofilespaginator)
        """

class ListIdentityProviderConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListIdentityProviderConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listidentityproviderconfigspaginator)
    """

    def paginate(
        self, *, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityProviderConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListIdentityProviderConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listidentityproviderconfigspaginator)
        """

class ListNodegroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListNodegroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listnodegroupspaginator)
    """

    def paginate(
        self, *, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNodegroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListNodegroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listnodegroupspaginator)
        """

class ListUpdatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListUpdates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listupdatespaginator)
    """

    def paginate(
        self,
        *,
        name: str,
        nodegroupName: str = None,
        addonName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/eks.html#EKS.Paginator.ListUpdates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listupdatespaginator)
        """
