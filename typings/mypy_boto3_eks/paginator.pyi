"""
Main interface for eks service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_eks import EKSClient
    from mypy_boto3_eks.paginator import (
        DescribeAddonVersionsPaginator,
        ListAddonsPaginator,
        ListClustersPaginator,
        ListFargateProfilesPaginator,
        ListNodegroupsPaginator,
        ListUpdatesPaginator,
    )

    client: EKSClient = boto3.client("eks")

    describe_addon_versions_paginator: DescribeAddonVersionsPaginator = client.get_paginator("describe_addon_versions")
    list_addons_paginator: ListAddonsPaginator = client.get_paginator("list_addons")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_fargate_profiles_paginator: ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
    list_nodegroups_paginator: ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
    list_updates_paginator: ListUpdatesPaginator = client.get_paginator("list_updates")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_eks.type_defs import (
    DescribeAddonVersionsResponseTypeDef,
    ListAddonsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListUpdatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAddonVersionsPaginator",
    "ListAddonsPaginator",
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
)


class DescribeAddonVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAddonVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions)
    """

    def paginate(
        self,
        kubernetesVersion: str = None,
        addonName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAddonVersionsResponseTypeDef]:
        """
        [DescribeAddonVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions.paginate)
        """


class ListAddonsPaginator(Boto3Paginator):
    """
    [Paginator.ListAddons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListAddons)
    """

    def paginate(
        self, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAddonsResponseTypeDef]:
        """
        [ListAddons.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListAddons.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListClusters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListClusters.paginate)
        """


class ListFargateProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
    """

    def paginate(
        self, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFargateProfilesResponseTypeDef]:
        """
        [ListFargateProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListFargateProfiles.paginate)
        """


class ListNodegroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListNodegroups)
    """

    def paginate(
        self, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNodegroupsResponseTypeDef]:
        """
        [ListNodegroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListNodegroups.paginate)
        """


class ListUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListUpdates)
    """

    def paginate(
        self,
        name: str,
        nodegroupName: str = None,
        addonName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUpdatesResponseTypeDef]:
        """
        [ListUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/eks.html#EKS.Paginator.ListUpdates.paginate)
        """
