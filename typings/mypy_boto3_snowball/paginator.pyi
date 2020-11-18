# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for snowball service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_snowball import SnowballClient
    from mypy_boto3_snowball.paginator import (
        DescribeAddressesPaginator,
        ListClusterJobsPaginator,
        ListClustersPaginator,
        ListCompatibleImagesPaginator,
        ListJobsPaginator,
    )

    client: SnowballClient = boto3.client("snowball")

    describe_addresses_paginator: DescribeAddressesPaginator = client.get_paginator("describe_addresses")
    list_cluster_jobs_paginator: ListClusterJobsPaginator = client.get_paginator("list_cluster_jobs")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compatible_images_paginator: ListCompatibleImagesPaginator = client.get_paginator("list_compatible_images")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_snowball.type_defs import (
    DescribeAddressesResultTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
)


class DescribeAddressesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddressesResultTypeDef]:
        """
        [DescribeAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses.paginate)
        """


class ListClusterJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterJobsResultTypeDef]:
        """
        [ListClusterJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResultTypeDef]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListClusters.paginate)
        """


class ListCompatibleImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCompatibleImagesResultTypeDef]:
        """
        [ListCompatibleImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListJobs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/snowball.html#Snowball.Paginator.ListJobs.paginate)
        """
