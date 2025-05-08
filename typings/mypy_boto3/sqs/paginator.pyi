"""
Type annotations for sqs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sqs.client import SQSClient
    from mypy_boto3_sqs.paginator import (
        ListDeadLetterSourceQueuesPaginator,
        ListQueuesPaginator,
    )

    session = Session()
    client: SQSClient = session.client("sqs")

    list_dead_letter_source_queues_paginator: ListDeadLetterSourceQueuesPaginator = client.get_paginator("list_dead_letter_source_queues")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDeadLetterSourceQueuesRequestPaginateTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueuesRequestPaginateTypeDef,
    ListQueuesResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListDeadLetterSourceQueuesPaginator", "ListQueuesPaginator")

if TYPE_CHECKING:
    _ListDeadLetterSourceQueuesPaginatorBase = Paginator[ListDeadLetterSourceQueuesResultTypeDef]
else:
    _ListDeadLetterSourceQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeadLetterSourceQueuesPaginator(_ListDeadLetterSourceQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/paginator/ListDeadLetterSourceQueues.html#SQS.Paginator.ListDeadLetterSourceQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators/#listdeadlettersourcequeuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeadLetterSourceQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListDeadLetterSourceQueuesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/paginator/ListDeadLetterSourceQueues.html#SQS.Paginator.ListDeadLetterSourceQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators/#listdeadlettersourcequeuespaginator)
        """

if TYPE_CHECKING:
    _ListQueuesPaginatorBase = Paginator[ListQueuesResultTypeDef]
else:
    _ListQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueuesPaginator(_ListQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/paginator/ListQueues.html#SQS.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators/#listqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListQueuesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/paginator/ListQueues.html#SQS.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators/#listqueuespaginator)
        """
