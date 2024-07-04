"""
Type annotations for mediapackagev2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mediapackagev2 import mediapackagev2Client
    from mypy_boto3_mediapackagev2.paginator import (
        ListChannelGroupsPaginator,
        ListChannelsPaginator,
        ListOriginEndpointsPaginator,
    )

    client: mediapackagev2Client = boto3.client("mediapackagev2")

    list_channel_groups_paginator: ListChannelGroupsPaginator = client.get_paginator("list_channel_groups")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListChannelGroupsResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListChannelGroupsPaginator", "ListChannelsPaginator", "ListOriginEndpointsPaginator")

class ListChannelGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannelGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelgroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannelGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelgroupspaginator)
        """

class ListChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelspaginator)
    """

    def paginate(
        self, *, ChannelGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listchannelspaginator)
        """

class ListOriginEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListOriginEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listoriginendpointspaginator)
    """

    def paginate(
        self,
        *,
        ChannelGroupName: str,
        ChannelName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOriginEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/mediapackagev2.html#mediapackagev2.Paginator.ListOriginEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/paginators.html#listoriginendpointspaginator)
        """
