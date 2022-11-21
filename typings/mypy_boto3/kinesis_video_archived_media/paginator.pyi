"""
Type annotations for kinesis-video-archived-media service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesis_video_archived_media import KinesisVideoArchivedMediaClient
    from mypy_boto3_kinesis_video_archived_media.paginator import (
        GetImagesPaginator,
        ListFragmentsPaginator,
    )

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")

    get_images_paginator: GetImagesPaginator = client.get_paginator("get_images")
    list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import FormatType, ImageSelectorTypeType
from .type_defs import (
    FragmentSelectorTypeDef,
    GetImagesOutputTypeDef,
    ListFragmentsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GetImagesPaginator", "ListFragmentsPaginator")

class GetImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.GetImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#getimagespaginator)
    """

    def paginate(
        self,
        *,
        ImageSelectorType: ImageSelectorTypeType,
        StartTimestamp: Union[datetime, str],
        EndTimestamp: Union[datetime, str],
        SamplingInterval: int,
        Format: FormatType,
        StreamName: str = None,
        StreamARN: str = None,
        FormatConfig: Dict[Literal["JPEGQuality"], str] = None,
        WidthPixels: int = None,
        HeightPixels: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetImagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.GetImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#getimagespaginator)
        """

class ListFragmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#listfragmentspaginator)
    """

    def paginate(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        FragmentSelector: "FragmentSelectorTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFragmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#listfragmentspaginator)
        """
