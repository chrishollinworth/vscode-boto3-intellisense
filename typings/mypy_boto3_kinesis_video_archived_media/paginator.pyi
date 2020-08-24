# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for kinesis-video-archived-media service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesis_video_archived_media import KinesisVideoArchivedMediaClient
    from mypy_boto3_kinesis_video_archived_media.paginator import (
        ListFragmentsPaginator,
    )

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")

    list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_kinesis_video_archived_media.type_defs import (
    FragmentSelectorTypeDef,
    ListFragmentsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListFragmentsPaginator",)


class ListFragmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
    """

    def paginate(
        self,
        StreamName: str,
        FragmentSelector: FragmentSelectorTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFragmentsOutputTypeDef]:
        """
        [ListFragments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        """
