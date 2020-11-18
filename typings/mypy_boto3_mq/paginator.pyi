# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mq service client paginators.

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

from mypy_boto3_mq.type_defs import ListBrokersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListBrokersPaginator",)


class ListBrokersPaginator(Boto3Paginator):
    """
    [Paginator.ListBrokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mq.html#MQ.Paginator.ListBrokers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBrokersResponseTypeDef]:
        """
        [ListBrokers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mq.html#MQ.Paginator.ListBrokers.paginate)
        """
