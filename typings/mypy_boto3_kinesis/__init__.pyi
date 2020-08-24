"""
Main interface for kinesis service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis import (
        Client,
        DescribeStreamPaginator,
        KinesisClient,
        ListShardsPaginator,
        ListStreamConsumersPaginator,
        ListStreamsPaginator,
        StreamExistsWaiter,
        StreamNotExistsWaiter,
    )

    session = boto3.Session()

    client: KinesisClient = boto3.client("kinesis")
    session_client: KinesisClient = session.client("kinesis")

    stream_exists_waiter: StreamExistsWaiter = client.get_waiter("stream_exists")
    stream_not_exists_waiter: StreamNotExistsWaiter = client.get_waiter("stream_not_exists")

    describe_stream_paginator: DescribeStreamPaginator = client.get_paginator("describe_stream")
    list_shards_paginator: ListShardsPaginator = client.get_paginator("list_shards")
    list_stream_consumers_paginator: ListStreamConsumersPaginator = client.get_paginator("list_stream_consumers")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from mypy_boto3_kinesis.client import KinesisClient
from mypy_boto3_kinesis.paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_kinesis.waiter import StreamExistsWaiter, StreamNotExistsWaiter

Client = KinesisClient


__all__ = (
    "Client",
    "DescribeStreamPaginator",
    "KinesisClient",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
    "StreamExistsWaiter",
    "StreamNotExistsWaiter",
)
