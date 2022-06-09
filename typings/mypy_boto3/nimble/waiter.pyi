"""
Type annotations for nimble service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_nimble import NimbleStudioClient
    from mypy_boto3_nimble.waiter import (
        LaunchProfileDeletedWaiter,
        LaunchProfileReadyWaiter,
        StreamingImageDeletedWaiter,
        StreamingImageReadyWaiter,
        StreamingSessionDeletedWaiter,
        StreamingSessionReadyWaiter,
        StreamingSessionStoppedWaiter,
        StreamingSessionStreamReadyWaiter,
        StudioComponentDeletedWaiter,
        StudioComponentReadyWaiter,
        StudioDeletedWaiter,
        StudioReadyWaiter,
    )

    client: NimbleStudioClient = boto3.client("nimble")

    launch_profile_deleted_waiter: LaunchProfileDeletedWaiter = client.get_waiter("launch_profile_deleted")
    launch_profile_ready_waiter: LaunchProfileReadyWaiter = client.get_waiter("launch_profile_ready")
    streaming_image_deleted_waiter: StreamingImageDeletedWaiter = client.get_waiter("streaming_image_deleted")
    streaming_image_ready_waiter: StreamingImageReadyWaiter = client.get_waiter("streaming_image_ready")
    streaming_session_deleted_waiter: StreamingSessionDeletedWaiter = client.get_waiter("streaming_session_deleted")
    streaming_session_ready_waiter: StreamingSessionReadyWaiter = client.get_waiter("streaming_session_ready")
    streaming_session_stopped_waiter: StreamingSessionStoppedWaiter = client.get_waiter("streaming_session_stopped")
    streaming_session_stream_ready_waiter: StreamingSessionStreamReadyWaiter = client.get_waiter("streaming_session_stream_ready")
    studio_component_deleted_waiter: StudioComponentDeletedWaiter = client.get_waiter("studio_component_deleted")
    studio_component_ready_waiter: StudioComponentReadyWaiter = client.get_waiter("studio_component_ready")
    studio_deleted_waiter: StudioDeletedWaiter = client.get_waiter("studio_deleted")
    studio_ready_waiter: StudioReadyWaiter = client.get_waiter("studio_ready")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "LaunchProfileDeletedWaiter",
    "LaunchProfileReadyWaiter",
    "StreamingImageDeletedWaiter",
    "StreamingImageReadyWaiter",
    "StreamingSessionDeletedWaiter",
    "StreamingSessionReadyWaiter",
    "StreamingSessionStoppedWaiter",
    "StreamingSessionStreamReadyWaiter",
    "StudioComponentDeletedWaiter",
    "StudioComponentReadyWaiter",
    "StudioDeletedWaiter",
    "StudioReadyWaiter",
)

class LaunchProfileDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofiledeletedwaiter)
    """

    def wait(
        self, *, launchProfileId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofiledeletedwaiter)
        """

class LaunchProfileReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofilereadywaiter)
    """

    def wait(
        self, *, launchProfileId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofilereadywaiter)
        """

class StreamingImageDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagedeletedwaiter)
    """

    def wait(
        self, *, streamingImageId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagedeletedwaiter)
        """

class StreamingImageReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagereadywaiter)
    """

    def wait(
        self, *, streamingImageId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagereadywaiter)
        """

class StreamingSessionDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessiondeletedwaiter)
    """

    def wait(
        self, *, sessionId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessiondeletedwaiter)
        """

class StreamingSessionReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionreadywaiter)
    """

    def wait(
        self, *, sessionId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionreadywaiter)
        """

class StreamingSessionStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStopped)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstoppedwaiter)
    """

    def wait(
        self, *, sessionId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStopped.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstoppedwaiter)
        """

class StreamingSessionStreamReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStreamReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstreamreadywaiter)
    """

    def wait(
        self,
        *,
        sessionId: str,
        streamId: str,
        studioId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStreamReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstreamreadywaiter)
        """

class StudioComponentDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentdeletedwaiter)
    """

    def wait(
        self, *, studioComponentId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentdeletedwaiter)
        """

class StudioComponentReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentreadywaiter)
    """

    def wait(
        self, *, studioComponentId: str, studioId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentreadywaiter)
        """

class StudioDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiodeletedwaiter)
    """

    def wait(self, *, studioId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiodeletedwaiter)
        """

class StudioReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioReady)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studioreadywaiter)
    """

    def wait(self, *, studioId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/nimble.html#NimbleStudio.Waiter.StudioReady.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studioreadywaiter)
        """
