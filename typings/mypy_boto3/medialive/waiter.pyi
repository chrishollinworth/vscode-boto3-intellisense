"""
Type annotations for medialive service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_medialive import MediaLiveClient
    from mypy_boto3_medialive.waiter import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        ChannelRunningWaiter,
        ChannelStoppedWaiter,
        InputAttachedWaiter,
        InputDeletedWaiter,
        InputDetachedWaiter,
        MultiplexCreatedWaiter,
        MultiplexDeletedWaiter,
        MultiplexRunningWaiter,
        MultiplexStoppedWaiter,
    )

    client: MediaLiveClient = boto3.client("medialive")

    channel_created_waiter: ChannelCreatedWaiter = client.get_waiter("channel_created")
    channel_deleted_waiter: ChannelDeletedWaiter = client.get_waiter("channel_deleted")
    channel_running_waiter: ChannelRunningWaiter = client.get_waiter("channel_running")
    channel_stopped_waiter: ChannelStoppedWaiter = client.get_waiter("channel_stopped")
    input_attached_waiter: InputAttachedWaiter = client.get_waiter("input_attached")
    input_deleted_waiter: InputDeletedWaiter = client.get_waiter("input_deleted")
    input_detached_waiter: InputDetachedWaiter = client.get_waiter("input_detached")
    multiplex_created_waiter: MultiplexCreatedWaiter = client.get_waiter("multiplex_created")
    multiplex_deleted_waiter: MultiplexDeletedWaiter = client.get_waiter("multiplex_deleted")
    multiplex_running_waiter: MultiplexRunningWaiter = client.get_waiter("multiplex_running")
    multiplex_stopped_waiter: MultiplexStoppedWaiter = client.get_waiter("multiplex_stopped")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "InputAttachedWaiter",
    "InputDeletedWaiter",
    "InputDetachedWaiter",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
)

class ChannelCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelcreatedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelcreatedwaiter)
        """

class ChannelDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channeldeletedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channeldeletedwaiter)
        """

class ChannelRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelrunningwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelrunningwaiter)
        """

class ChannelStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelstoppedwaiter)
    """

    def wait(self, *, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelstoppedwaiter)
        """

class InputAttachedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputAttached)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputattachedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputAttached.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputattachedwaiter)
        """

class InputDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdeletedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdeletedwaiter)
        """

class InputDetachedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputDetached)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdetachedwaiter)
    """

    def wait(self, *, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.InputDetached.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdetachedwaiter)
        """

class MultiplexCreatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexcreatedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexcreatedwaiter)
        """

class MultiplexDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexdeletedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexdeletedwaiter)
        """

class MultiplexRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexrunningwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexrunningwaiter)
        """

class MultiplexStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexstoppedwaiter)
    """

    def wait(self, *, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexstoppedwaiter)
        """
