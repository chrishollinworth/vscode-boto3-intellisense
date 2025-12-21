"""
Type annotations for keyspacesstreams service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_keyspacesstreams.client import KeyspacesStreamsClient
    from mypy_boto3_keyspacesstreams.paginator import (
        GetStreamPaginator,
        ListStreamsPaginator,
    )

    session = Session()
    client: KeyspacesStreamsClient = session.client("keyspacesstreams")

    get_stream_paginator: GetStreamPaginator = client.get_paginator("get_stream")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetStreamInputPaginateTypeDef,
    GetStreamOutputTypeDef,
    ListStreamsInputPaginateTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetStreamPaginator", "ListStreamsPaginator")

if TYPE_CHECKING:
    _GetStreamPaginatorBase = Paginator[GetStreamOutputTypeDef]
else:
    _GetStreamPaginatorBase = Paginator  # type: ignore[assignment]

class GetStreamPaginator(_GetStreamPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/paginator/GetStream.html#KeyspacesStreams.Paginator.GetStream)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/paginators/#getstreampaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetStreamInputPaginateTypeDef]
    ) -> PageIterator[GetStreamOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/paginator/GetStream.html#KeyspacesStreams.Paginator.GetStream.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/paginators/#getstreampaginator)
        """

if TYPE_CHECKING:
    _ListStreamsPaginatorBase = Paginator[ListStreamsOutputTypeDef]
else:
    _ListStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamsPaginator(_ListStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/paginator/ListStreams.html#KeyspacesStreams.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/paginators/#liststreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamsInputPaginateTypeDef]
    ) -> PageIterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/paginator/ListStreams.html#KeyspacesStreams.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/paginators/#liststreamspaginator)
        """
