# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for medialive service client waiters.

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

from mypy_boto3_medialive.type_defs import WaiterConfigTypeDef

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
    [Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
    """

    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated.wait)
        """


class ChannelDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
    """

    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted.wait)
        """


class ChannelRunningWaiter(Boto3Waiter):
    """
    [Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
    """

    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning.wait)
        """


class ChannelStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
    """

    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped.wait)
        """


class InputAttachedWaiter(Boto3Waiter):
    """
    [Waiter.InputAttached documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputAttached)
    """

    def wait(self, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InputAttached.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputAttached.wait)
        """


class InputDeletedWaiter(Boto3Waiter):
    """
    [Waiter.InputDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)
    """

    def wait(self, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InputDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDeleted.wait)
        """


class InputDetachedWaiter(Boto3Waiter):
    """
    [Waiter.InputDetached documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDetached)
    """

    def wait(self, InputId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InputDetached.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDetached.wait)
        """


class MultiplexCreatedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
    """

    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated.wait)
        """


class MultiplexDeletedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
    """

    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted.wait)
        """


class MultiplexRunningWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
    """

    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning.wait)
        """


class MultiplexStoppedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
    """

    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped.wait)
        """
