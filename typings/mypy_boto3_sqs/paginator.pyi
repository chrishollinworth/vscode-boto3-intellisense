# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sqs service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sqs import SQSClient
    from mypy_boto3_sqs.paginator import (
        ListDeadLetterSourceQueuesPaginator,
        ListQueuesPaginator,
    )

    client: SQSClient = boto3.client("sqs")

    list_dead_letter_source_queues_paginator: ListDeadLetterSourceQueuesPaginator = client.get_paginator("list_dead_letter_source_queues")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sqs.type_defs import (
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueuesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDeadLetterSourceQueuesPaginator", "ListQueuesPaginator")


class ListDeadLetterSourceQueuesPaginator(Boto3Paginator):
    """
    [Paginator.ListDeadLetterSourceQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)
    """

    def paginate(
        self, QueueUrl: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeadLetterSourceQueuesResultTypeDef]:
        """
        [ListDeadLetterSourceQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListQueues)
    """

    def paginate(
        self, QueueNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResultTypeDef]:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListQueues.paginate)
        """
