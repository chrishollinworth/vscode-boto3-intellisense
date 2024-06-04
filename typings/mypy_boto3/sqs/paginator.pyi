"""
Type annotations for sqs service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html)

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

from .type_defs import (
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueuesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDeadLetterSourceQueuesPaginator", "ListQueuesPaginator")

class ListDeadLetterSourceQueuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listdeadlettersourcequeuespaginator)
    """

    def paginate(
        self, *, QueueUrl: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeadLetterSourceQueuesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listdeadlettersourcequeuespaginator)
        """

class ListQueuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sqs.html#SQS.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listqueuespaginator)
    """

    def paginate(
        self, *, QueueNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sqs.html#SQS.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listqueuespaginator)
        """
