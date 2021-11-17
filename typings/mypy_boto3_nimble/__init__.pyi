"""
Main interface for nimble service.

Usage::

    ```python
    import boto3
    from mypy_boto3_nimble import (
        Client,
        LaunchProfileDeletedWaiter,
        LaunchProfileReadyWaiter,
        ListEulaAcceptancesPaginator,
        ListEulasPaginator,
        ListLaunchProfileMembersPaginator,
        ListLaunchProfilesPaginator,
        ListStreamingImagesPaginator,
        ListStreamingSessionsPaginator,
        ListStudioComponentsPaginator,
        ListStudioMembersPaginator,
        ListStudiosPaginator,
        NimbleStudioClient,
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

    session = boto3.Session()

    client: NimbleStudioClient = boto3.client("nimble")
    session_client: NimbleStudioClient = session.client("nimble")

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

    list_eula_acceptances_paginator: ListEulaAcceptancesPaginator = client.get_paginator("list_eula_acceptances")
    list_eulas_paginator: ListEulasPaginator = client.get_paginator("list_eulas")
    list_launch_profile_members_paginator: ListLaunchProfileMembersPaginator = client.get_paginator("list_launch_profile_members")
    list_launch_profiles_paginator: ListLaunchProfilesPaginator = client.get_paginator("list_launch_profiles")
    list_streaming_images_paginator: ListStreamingImagesPaginator = client.get_paginator("list_streaming_images")
    list_streaming_sessions_paginator: ListStreamingSessionsPaginator = client.get_paginator("list_streaming_sessions")
    list_studio_components_paginator: ListStudioComponentsPaginator = client.get_paginator("list_studio_components")
    list_studio_members_paginator: ListStudioMembersPaginator = client.get_paginator("list_studio_members")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""
from .client import NimbleStudioClient
from .paginator import (
    ListEulaAcceptancesPaginator,
    ListEulasPaginator,
    ListLaunchProfileMembersPaginator,
    ListLaunchProfilesPaginator,
    ListStreamingImagesPaginator,
    ListStreamingSessionsPaginator,
    ListStudioComponentsPaginator,
    ListStudioMembersPaginator,
    ListStudiosPaginator,
)
from .waiter import (
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

Client = NimbleStudioClient

__all__ = (
    "Client",
    "LaunchProfileDeletedWaiter",
    "LaunchProfileReadyWaiter",
    "ListEulaAcceptancesPaginator",
    "ListEulasPaginator",
    "ListLaunchProfileMembersPaginator",
    "ListLaunchProfilesPaginator",
    "ListStreamingImagesPaginator",
    "ListStreamingSessionsPaginator",
    "ListStudioComponentsPaginator",
    "ListStudioMembersPaginator",
    "ListStudiosPaginator",
    "NimbleStudioClient",
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
