"""
Type annotations for glacier service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html)

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

from .type_defs import WaiterConfigTypeDef

__all__ = ("VaultExistsWaiter", "VaultNotExistsWaiter")

class VaultExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/glacier.html#Glacier.Waiter.VaultExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultexistswaiter)
    """

    def wait(
        self, *, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/glacier.html#Glacier.Waiter.VaultExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultexistswaiter)
        """

class VaultNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultnotexistswaiter)
    """

    def wait(
        self, *, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/glacier.html#Glacier.Waiter.VaultNotExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultnotexistswaiter)
        """
