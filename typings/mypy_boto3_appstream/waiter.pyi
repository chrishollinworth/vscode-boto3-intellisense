"""
Type annotations for appstream service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appstream.client import AppStreamClient
    from mypy_boto3_appstream.waiter import (
        FleetStartedWaiter,
        FleetStoppedWaiter,
    )

    session = Session()
    client: AppStreamClient = session.client("appstream")

    fleet_started_waiter: FleetStartedWaiter = client.get_waiter("fleet_started")
    fleet_stopped_waiter: FleetStoppedWaiter = client.get_waiter("fleet_stopped")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeFleetsRequestWaitExtraTypeDef, DescribeFleetsRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("FleetStartedWaiter", "FleetStoppedWaiter")

class FleetStartedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/waiter/FleetStarted.html#AppStream.Waiter.FleetStarted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters/#fleetstartedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFleetsRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/waiter/FleetStarted.html#AppStream.Waiter.FleetStarted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters/#fleetstartedwaiter)
        """

class FleetStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/waiter/FleetStopped.html#AppStream.Waiter.FleetStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters/#fleetstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFleetsRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream/waiter/FleetStopped.html#AppStream.Waiter.FleetStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters/#fleetstoppedwaiter)
        """
