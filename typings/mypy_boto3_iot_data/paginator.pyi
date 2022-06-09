"""
Type annotations for iot-data service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iot_data import IoTDataPlaneClient
    from mypy_boto3_iot_data.paginator import (
        ListRetainedMessagesPaginator,
    )

    client: IoTDataPlaneClient = boto3.client("iot-data")

    list_retained_messages_paginator: ListRetainedMessagesPaginator = client.get_paginator("list_retained_messages")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListRetainedMessagesResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListRetainedMessagesPaginator",)

class ListRetainedMessagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot-data.html#IoTDataPlane.Paginator.ListRetainedMessages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators.html#listretainedmessagespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRetainedMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot-data.html#IoTDataPlane.Paginator.ListRetainedMessages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators.html#listretainedmessagespaginator)
        """
