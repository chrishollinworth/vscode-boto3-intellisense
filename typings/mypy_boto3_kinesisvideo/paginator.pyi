# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for kinesisvideo service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesisvideo import KinesisVideoClient
    from mypy_boto3_kinesisvideo.paginator import (
        ListSignalingChannelsPaginator,
        ListStreamsPaginator,
    )

    client: KinesisVideoClient = boto3.client("kinesisvideo")

    list_signaling_channels_paginator: ListSignalingChannelsPaginator = client.get_paginator("list_signaling_channels")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_kinesisvideo.type_defs import (
    ChannelNameConditionTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
    StreamNameConditionTypeDef,
)

__all__ = ("ListSignalingChannelsPaginator", "ListStreamsPaginator")


class ListSignalingChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListSignalingChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
    """

    def paginate(
        self,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSignalingChannelsOutputTypeDef]:
        """
        [ListSignalingChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
    """

    def paginate(
        self,
        StreamNameCondition: StreamNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStreamsOutputTypeDef]:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams.paginate)
        """
