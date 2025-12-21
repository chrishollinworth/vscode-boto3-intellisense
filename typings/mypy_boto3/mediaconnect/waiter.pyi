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
        InputActiveWaiter,
        InputDeletedWaiter,
        InputStandbyWaiter,
        OutputActiveWaiter,
        OutputDeletedWaiter,
        OutputRoutedWaiter,
        OutputStandbyWaiter,
    )

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")
    input_active_waiter: InputActiveWaiter = client.get_waiter("input_active")
    input_deleted_waiter: InputDeletedWaiter = client.get_waiter("input_deleted")
    input_standby_waiter: InputStandbyWaiter = client.get_waiter("input_standby")
    output_active_waiter: OutputActiveWaiter = client.get_waiter("output_active")
    output_deleted_waiter: OutputDeletedWaiter = client.get_waiter("output_deleted")
    output_routed_waiter: OutputRoutedWaiter = client.get_waiter("output_routed")
    output_standby_waiter: OutputStandbyWaiter = client.get_waiter("output_standby")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeFlowRequestWaitExtraExtraTypeDef,
    DescribeFlowRequestWaitExtraTypeDef,
    DescribeFlowRequestWaitTypeDef,
    GetRouterInputRequestWaitExtraExtraTypeDef,
    GetRouterInputRequestWaitExtraTypeDef,
    GetRouterInputRequestWaitTypeDef,
    GetRouterOutputRequestWaitExtraExtraExtraTypeDef,
    GetRouterOutputRequestWaitExtraExtraTypeDef,
    GetRouterOutputRequestWaitExtraTypeDef,
    GetRouterOutputRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "FlowActiveWaiter",
    "FlowDeletedWaiter",
    "FlowStandbyWaiter",
    "InputActiveWaiter",
    "InputDeletedWaiter",
    "InputStandbyWaiter",
    "OutputActiveWaiter",
    "OutputDeletedWaiter",
    "OutputRoutedWaiter",
    "OutputStandbyWaiter",
)

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

class InputActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputActive.html#MediaConnect.Waiter.InputActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterInputRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputActive.html#MediaConnect.Waiter.InputActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputactivewaiter)
        """

class InputDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputDeleted.html#MediaConnect.Waiter.InputDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterInputRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputDeleted.html#MediaConnect.Waiter.InputDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputdeletedwaiter)
        """

class InputStandbyWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputStandby.html#MediaConnect.Waiter.InputStandby)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputstandbywaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterInputRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/InputStandby.html#MediaConnect.Waiter.InputStandby.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#inputstandbywaiter)
        """

class OutputActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputActive.html#MediaConnect.Waiter.OutputActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterOutputRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputActive.html#MediaConnect.Waiter.OutputActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputactivewaiter)
        """

class OutputDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputDeleted.html#MediaConnect.Waiter.OutputDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterOutputRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputDeleted.html#MediaConnect.Waiter.OutputDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputdeletedwaiter)
        """

class OutputRoutedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputRouted.html#MediaConnect.Waiter.OutputRouted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputroutedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterOutputRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputRouted.html#MediaConnect.Waiter.OutputRouted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputroutedwaiter)
        """

class OutputStandbyWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputStandby.html#MediaConnect.Waiter.OutputStandby)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputstandbywaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRouterOutputRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect/waiter/OutputStandby.html#MediaConnect.Waiter.OutputStandby.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters/#outputstandbywaiter)
        """
