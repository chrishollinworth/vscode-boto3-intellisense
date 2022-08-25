"""
Type annotations for appstream service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_appstream import AppStreamClient
    from mypy_boto3_appstream.waiter import (
        FleetStartedWaiter,
        FleetStoppedWaiter,
    )

    client: AppStreamClient = boto3.client("appstream")

    fleet_started_waiter: FleetStartedWaiter = client.get_waiter("fleet_started")
    fleet_stopped_waiter: FleetStoppedWaiter = client.get_waiter("fleet_stopped")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("FleetStartedWaiter", "FleetStoppedWaiter")

class FleetStartedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstartedwaiter)
    """

    def wait(
        self,
        *,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/appstream.html#AppStream.Waiter.FleetStarted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstartedwaiter)
        """

class FleetStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstoppedwaiter)
    """

    def wait(
        self,
        *,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/appstream.html#AppStream.Waiter.FleetStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstoppedwaiter)
        """
