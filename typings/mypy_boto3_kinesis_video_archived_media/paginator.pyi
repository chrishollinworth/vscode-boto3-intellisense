"""
Type annotations for kinesis-video-archived-media service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
    from mypy_boto3_kinesis_video_archived_media.paginator import (
        GetImagesPaginator,
        ListFragmentsPaginator,
    )

    session = Session()
    client: KinesisVideoArchivedMediaClient = session.client("kinesis-video-archived-media")

    get_images_paginator: GetImagesPaginator = client.get_paginator("get_images")
    list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetImagesInputPaginateTypeDef,
    GetImagesOutputTypeDef,
    ListFragmentsInputPaginateTypeDef,
    ListFragmentsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetImagesPaginator", "ListFragmentsPaginator")

if TYPE_CHECKING:
    _GetImagesPaginatorBase = Paginator[GetImagesOutputTypeDef]
else:
    _GetImagesPaginatorBase = Paginator  # type: ignore[assignment]

class GetImagesPaginator(_GetImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media/paginator/GetImages.html#KinesisVideoArchivedMedia.Paginator.GetImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators/#getimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetImagesInputPaginateTypeDef]
    ) -> PageIterator[GetImagesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media/paginator/GetImages.html#KinesisVideoArchivedMedia.Paginator.GetImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators/#getimagespaginator)
        """

if TYPE_CHECKING:
    _ListFragmentsPaginatorBase = Paginator[ListFragmentsOutputTypeDef]
else:
    _ListFragmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFragmentsPaginator(_ListFragmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media/paginator/ListFragments.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators/#listfragmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFragmentsInputPaginateTypeDef]
    ) -> PageIterator[ListFragmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media/paginator/ListFragments.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators/#listfragmentspaginator)
        """
