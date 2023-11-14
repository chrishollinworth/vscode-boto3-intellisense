"""
Type annotations for groundstation service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_groundstation import GroundStationClient
    from mypy_boto3_groundstation.waiter import (
        ContactScheduledWaiter,
    )

    client: GroundStationClient = boto3.client("groundstation")

    contact_scheduled_waiter: ContactScheduledWaiter = client.get_waiter("contact_scheduled")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ContactScheduledWaiter",)

class ContactScheduledWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/groundstation.html#GroundStation.Waiter.ContactScheduled)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/waiters.html#contactscheduledwaiter)
    """

    def wait(self, *, contactId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/groundstation.html#GroundStation.Waiter.ContactScheduled.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/waiters.html#contactscheduledwaiter)
        """
