"""
Type annotations for transfer service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_transfer.client import TransferClient
    from mypy_boto3_transfer.waiter import (
        ServerOfflineWaiter,
        ServerOnlineWaiter,
    )

    session = Session()
    client: TransferClient = session.client("transfer")

    server_offline_waiter: ServerOfflineWaiter = client.get_waiter("server_offline")
    server_online_waiter: ServerOnlineWaiter = client.get_waiter("server_online")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeServerRequestWaitExtraTypeDef, DescribeServerRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ServerOfflineWaiter", "ServerOnlineWaiter")

class ServerOfflineWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/waiter/ServerOffline.html#Transfer.Waiter.ServerOffline)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters/#serverofflinewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServerRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/waiter/ServerOffline.html#Transfer.Waiter.ServerOffline.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters/#serverofflinewaiter)
        """

class ServerOnlineWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/waiter/ServerOnline.html#Transfer.Waiter.ServerOnline)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters/#serveronlinewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServerRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/waiter/ServerOnline.html#Transfer.Waiter.ServerOnline.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters/#serveronlinewaiter)
        """
