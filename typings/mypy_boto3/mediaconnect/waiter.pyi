"""
Type annotations for mediaconnect service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediaconnect.client import MediaConnectClient
    from mypy_boto3_mediaconnect.waiter import (
        FlowActiveWaiter,
        FlowDeletedWaiter,
        FlowStandbyWaiter,
    )

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeFlowRequestWaitExtraExtraTypeDef,
    DescribeFlowRequestWaitExtraTypeDef,
    DescribeFlowRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("FlowActiveWaiter", "FlowDeletedWaiter", "FlowStandbyWaiter")

class FlowActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowActive.html#MediaConnect.Waiter.FlowActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFlowRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowActive.html#MediaConnect.Waiter.FlowActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowactivewaiter)
        """

class FlowDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowDeleted.html#MediaConnect.Waiter.FlowDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFlowRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowDeleted.html#MediaConnect.Waiter.FlowDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowdeletedwaiter)
        """

class FlowStandbyWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowStandby.html#MediaConnect.Waiter.FlowStandby)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowstandbywaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFlowRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/FlowStandby.html#MediaConnect.Waiter.FlowStandby.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#flowstandbywaiter)
        """
