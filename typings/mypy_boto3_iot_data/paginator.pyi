"""
Type annotations for iot-data service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iot_data.client import IoTDataPlaneClient
    from mypy_boto3_iot_data.paginator import (
        ListRetainedMessagesPaginator,
    )

    session = Session()
    client: IoTDataPlaneClient = session.client("iot-data")

    list_retained_messages_paginator: ListRetainedMessagesPaginator = client.get_paginator("list_retained_messages")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListRetainedMessagesRequestPaginateTypeDef,
    ListRetainedMessagesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRetainedMessagesPaginator",)

if TYPE_CHECKING:
    _ListRetainedMessagesPaginatorBase = Paginator[ListRetainedMessagesResponseTypeDef]
else:
    _ListRetainedMessagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRetainedMessagesPaginator(_ListRetainedMessagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data/paginator/ListRetainedMessages.html#IoTDataPlane.Paginator.ListRetainedMessages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators/#listretainedmessagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRetainedMessagesRequestPaginateTypeDef]
    ) -> PageIterator[ListRetainedMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data/paginator/ListRetainedMessages.html#IoTDataPlane.Paginator.ListRetainedMessages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators/#listretainedmessagespaginator)
        """
