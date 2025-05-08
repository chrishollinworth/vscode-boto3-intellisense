"""
Type annotations for mq service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mq.client import MQClient
    from mypy_boto3_mq.paginator import (
        ListBrokersPaginator,
    )

    session = Session()
    client: MQClient = session.client("mq")

    list_brokers_paginator: ListBrokersPaginator = client.get_paginator("list_brokers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListBrokersRequestPaginateTypeDef, ListBrokersResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListBrokersPaginator",)

if TYPE_CHECKING:
    _ListBrokersPaginatorBase = Paginator[ListBrokersResponseTypeDef]
else:
    _ListBrokersPaginatorBase = Paginator  # type: ignore[assignment]

class ListBrokersPaginator(_ListBrokersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/paginator/ListBrokers.html#MQ.Paginator.ListBrokers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators/#listbrokerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBrokersRequestPaginateTypeDef]
    ) -> PageIterator[ListBrokersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq/paginator/ListBrokers.html#MQ.Paginator.ListBrokers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/paginators/#listbrokerspaginator)
        """
