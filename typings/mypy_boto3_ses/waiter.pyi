# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for ses service client waiters.

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

from mypy_boto3_ses.type_defs import WaiterConfigTypeDef

__all__ = ("IdentityExistsWaiter",)


class IdentityExistsWaiter(Boto3Waiter):
    """
    [Waiter.IdentityExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Waiter.IdentityExists)
    """

    def wait(self, Identities: List[str], WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [IdentityExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ses.html#SES.Waiter.IdentityExists.wait)
        """
