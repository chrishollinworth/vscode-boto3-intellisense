# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for appstream service client waiters.

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

from mypy_boto3_appstream.type_defs import WaiterConfigTypeDef

__all__ = ("FleetStartedWaiter", "FleetStoppedWaiter")


class FleetStartedWaiter(Boto3Waiter):
    """
    [Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
    """

    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [FleetStarted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStarted.wait)
        """


class FleetStoppedWaiter(Boto3Waiter):
    """
    [Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
    """

    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [FleetStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStopped.wait)
        """
