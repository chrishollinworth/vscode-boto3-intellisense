# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mediapackage service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediapackage import MediaPackageClient
    from mypy_boto3_mediapackage.paginator import (
        ListChannelsPaginator,
        ListHarvestJobsPaginator,
        ListOriginEndpointsPaginator,
    )

    client: MediaPackageClient = boto3.client("mediapackage")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_harvest_jobs_paginator: ListHarvestJobsPaginator = client.get_paginator("list_harvest_jobs")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediapackage.type_defs import (
    ListChannelsResponseTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListChannelsPaginator", "ListHarvestJobsPaginator", "ListOriginEndpointsPaginator")


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels.paginate)
        """


class ListHarvestJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListHarvestJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)
    """

    def paginate(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHarvestJobsResponseTypeDef]:
        """
        [ListHarvestJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs.paginate)
        """


class ListOriginEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListOriginEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)
    """

    def paginate(
        self, ChannelId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOriginEndpointsResponseTypeDef]:
        """
        [ListOriginEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints.paginate)
        """
