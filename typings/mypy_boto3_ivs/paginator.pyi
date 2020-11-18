# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ivs service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ivs import IVSClient
    from mypy_boto3_ivs.paginator import (
        ListChannelsPaginator,
        ListPlaybackKeyPairsPaginator,
        ListStreamKeysPaginator,
        ListStreamsPaginator,
    )

    client: IVSClient = boto3.client("ivs")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_playback_key_pairs_paginator: ListPlaybackKeyPairsPaginator = client.get_paginator("list_playback_key_pairs")
    list_stream_keys_paginator: ListStreamKeysPaginator = client.get_paginator("list_stream_keys")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ivs.type_defs import (
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListChannelsPaginator",
    "ListPlaybackKeyPairsPaginator",
    "ListStreamKeysPaginator",
    "ListStreamsPaginator",
)


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListChannels)
    """

    def paginate(
        self, filterByName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListChannels.paginate)
        """


class ListPlaybackKeyPairsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlaybackKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaybackKeyPairsResponseTypeDef]:
        """
        [ListPlaybackKeyPairs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs.paginate)
        """


class ListStreamKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreamKeys)
    """

    def paginate(
        self, channelArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamKeysResponseTypeDef]:
        """
        [ListStreamKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreamKeys.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreams)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsResponseTypeDef]:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreams.paginate)
        """
