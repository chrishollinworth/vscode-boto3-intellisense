"""
Type annotations for kinesis service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kinesis.client import KinesisClient
    from mypy_boto3_kinesis.paginator import (
        DescribeStreamPaginator,
        ListShardsPaginator,
        ListStreamConsumersPaginator,
        ListStreamsPaginator,
    )

    session = Session()
    client: KinesisClient = session.client("kinesis")

    describe_stream_paginator: DescribeStreamPaginator = client.get_paginator("describe_stream")
    list_shards_paginator: ListShardsPaginator = client.get_paginator("list_shards")
    list_stream_consumers_paginator: ListStreamConsumersPaginator = client.get_paginator("list_stream_consumers")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeStreamInputPaginateTypeDef,
    DescribeStreamOutputTypeDef,
    ListShardsInputPaginateTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersInputPaginateTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsInputPaginateTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeStreamPaginator",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
)

if TYPE_CHECKING:
    _DescribeStreamPaginatorBase = Paginator[DescribeStreamOutputTypeDef]
else:
    _DescribeStreamPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStreamPaginator(_DescribeStreamPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/DescribeStream.html#Kinesis.Paginator.DescribeStream)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#describestreampaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStreamInputPaginateTypeDef]
    ) -> PageIterator[DescribeStreamOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/DescribeStream.html#Kinesis.Paginator.DescribeStream.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#describestreampaginator)
        """

if TYPE_CHECKING:
    _ListShardsPaginatorBase = Paginator[ListShardsOutputTypeDef]
else:
    _ListShardsPaginatorBase = Paginator  # type: ignore[assignment]

class ListShardsPaginator(_ListShardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListShards.html#Kinesis.Paginator.ListShards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#listshardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListShardsInputPaginateTypeDef]
    ) -> PageIterator[ListShardsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListShards.html#Kinesis.Paginator.ListShards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#listshardspaginator)
        """

if TYPE_CHECKING:
    _ListStreamConsumersPaginatorBase = Paginator[ListStreamConsumersOutputTypeDef]
else:
    _ListStreamConsumersPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamConsumersPaginator(_ListStreamConsumersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListStreamConsumers.html#Kinesis.Paginator.ListStreamConsumers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#liststreamconsumerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamConsumersInputPaginateTypeDef]
    ) -> PageIterator[ListStreamConsumersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListStreamConsumers.html#Kinesis.Paginator.ListStreamConsumers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#liststreamconsumerspaginator)
        """

if TYPE_CHECKING:
    _ListStreamsPaginatorBase = Paginator[ListStreamsOutputTypeDef]
else:
    _ListStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamsPaginator(_ListStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListStreams.html#Kinesis.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#liststreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamsInputPaginateTypeDef]
    ) -> PageIterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/paginator/ListStreams.html#Kinesis.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators/#liststreamspaginator)
        """
