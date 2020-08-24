# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for glacier service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_glacier import GlacierClient
    from mypy_boto3_glacier.waiter import (
        VaultExistsWaiter,
        VaultNotExistsWaiter,
    )

    client: GlacierClient = boto3.client("glacier")

    vault_exists_waiter: VaultExistsWaiter = client.get_waiter("vault_exists")
    vault_not_exists_waiter: VaultNotExistsWaiter = client.get_waiter("vault_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_glacier.type_defs import WaiterConfigTypeDef

__all__ = ("VaultExistsWaiter", "VaultNotExistsWaiter")


class VaultExistsWaiter(Boto3Waiter):
    """
    [Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultExists)
    """

    def wait(
        self, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [VaultExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultExists.wait)
        """


class VaultNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
    """

    def wait(
        self, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [VaultNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/glacier.html#Glacier.Waiter.VaultNotExists.wait)
        """
