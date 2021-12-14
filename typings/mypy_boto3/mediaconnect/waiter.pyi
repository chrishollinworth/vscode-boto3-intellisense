"""
Type annotations for mediaconnect service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mediaconnect import MediaConnectClient
    from mypy_boto3_mediaconnect.waiter import (
        FlowActiveWaiter,
        FlowDeletedWaiter,
        FlowStandbyWaiter,
    )

    client: MediaConnectClient = boto3.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("FlowActiveWaiter", "FlowDeletedWaiter", "FlowStandbyWaiter")

class FlowActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowActive)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowactivewaiter)
    """

    def wait(self, *, FlowArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowActive.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowactivewaiter)
        """

class FlowDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowdeletedwaiter)
    """

    def wait(self, *, FlowArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowdeletedwaiter)
        """

class FlowStandbyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowStandby)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowstandbywaiter)
    """

    def wait(self, *, FlowArn: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/mediaconnect.html#MediaConnect.Waiter.FlowStandby.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/waiters.html#flowstandbywaiter)
        """
