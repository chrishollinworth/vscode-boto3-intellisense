"""
Type annotations for transfer service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_transfer import TransferClient
    from mypy_boto3_transfer.waiter import (
        ServerOfflineWaiter,
        ServerOnlineWaiter,
    )

    client: TransferClient = boto3.client("transfer")

    server_offline_waiter: ServerOfflineWaiter = client.get_waiter("server_offline")
    server_online_waiter: ServerOnlineWaiter = client.get_waiter("server_online")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ServerOfflineWaiter", "ServerOnlineWaiter")

class ServerOfflineWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/transfer.html#Transfer.Waiter.ServerOffline)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serverofflinewaiter)
    """

    def wait(self, *, ServerId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/transfer.html#Transfer.Waiter.ServerOffline.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serverofflinewaiter)
        """

class ServerOnlineWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/transfer.html#Transfer.Waiter.ServerOnline)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serveronlinewaiter)
    """

    def wait(self, *, ServerId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/transfer.html#Transfer.Waiter.ServerOnline.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/waiters.html#serveronlinewaiter)
        """
