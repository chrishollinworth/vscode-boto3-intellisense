"""
Type annotations for mediapackagev2 service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediapackagev2.client import Mediapackagev2Client
    from mypy_boto3_mediapackagev2.waiter import (
        HarvestJobFinishedWaiter,
    )

    session = Session()
    client: Mediapackagev2Client = session.client("mediapackagev2")

    harvest_job_finished_waiter: HarvestJobFinishedWaiter = client.get_waiter("harvest_job_finished")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetHarvestJobRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("HarvestJobFinishedWaiter",)

class HarvestJobFinishedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/waiter/HarvestJobFinished.html#Mediapackagev2.Waiter.HarvestJobFinished)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/waiters/#harvestjobfinishedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetHarvestJobRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackagev2/waiter/HarvestJobFinished.html#Mediapackagev2.Waiter.HarvestJobFinished.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/waiters/#harvestjobfinishedwaiter)
        """
