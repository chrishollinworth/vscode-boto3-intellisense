"""
Type annotations for macie2 service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_macie2 import Macie2Client
    from mypy_boto3_macie2.waiter import (
        FindingRevealedWaiter,
    )

    client: Macie2Client = boto3.client("macie2")

    finding_revealed_waiter: FindingRevealedWaiter = client.get_waiter("finding_revealed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("FindingRevealedWaiter",)

class FindingRevealedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/macie2.html#Macie2.Waiter.FindingRevealed)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters.html#findingrevealedwaiter)
    """

    def wait(self, *, findingId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/macie2.html#Macie2.Waiter.FindingRevealed.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters.html#findingrevealedwaiter)
        """
