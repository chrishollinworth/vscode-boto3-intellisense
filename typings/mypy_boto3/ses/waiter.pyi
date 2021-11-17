"""
Type annotations for ses service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ses import SESClient
    from mypy_boto3_ses.waiter import (
        IdentityExistsWaiter,
    )

    client: SESClient = boto3.client("ses")

    identity_exists_waiter: IdentityExistsWaiter = client.get_waiter("identity_exists")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("IdentityExistsWaiter",)

class IdentityExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Waiter.IdentityExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/waiters.html#identityexistswaiter)
    """

    def wait(self, *, Identities: List[str], WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Waiter.IdentityExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/waiters.html#identityexistswaiter)
        """
