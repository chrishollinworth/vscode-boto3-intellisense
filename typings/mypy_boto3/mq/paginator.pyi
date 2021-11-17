"""
Type annotations for mq service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mq import MQClient
    from mypy_boto3_mq.paginator import (
        ListBrokersPaginator,
    )

    client: MQClient = boto3.client("mq")

    list_brokers_paginator: ListBrokersPaginator = client.get_paginator("list_brokers")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListBrokersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListBrokersPaginator",)

class ListBrokersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/mq.html#MQ.Paginator.ListBrokers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators.html#listbrokerspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBrokersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/mq.html#MQ.Paginator.ListBrokers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators.html#listbrokerspaginator)
        """
