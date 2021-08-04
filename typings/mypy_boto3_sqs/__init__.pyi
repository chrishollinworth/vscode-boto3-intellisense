"""
Main interface for sqs service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sqs import (
        Client,
        ListDeadLetterSourceQueuesPaginator,
        ListQueuesPaginator,
        SQSClient,
        SQSServiceResource,
        ServiceResource,
    )

    session = boto3.Session()

    client: SQSClient = boto3.client("sqs")
    session_client: SQSClient = session.client("sqs")

    resource: SQSServiceResource = boto3.resource("sqs")
    session_resource: SQSServiceResource = session.resource("sqs")

    list_dead_letter_source_queues_paginator: ListDeadLetterSourceQueuesPaginator = client.get_paginator("list_dead_letter_source_queues")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""
from .client import SQSClient
from .paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from .service_resource import SQSServiceResource

Client = SQSClient

ServiceResource = SQSServiceResource

__all__ = (
    "Client",
    "ListDeadLetterSourceQueuesPaginator",
    "ListQueuesPaginator",
    "SQSClient",
    "SQSServiceResource",
    "ServiceResource",
)
