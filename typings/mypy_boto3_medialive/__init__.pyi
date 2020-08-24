"""
Main interface for medialive service.

Usage::

    ```python
    import boto3
    from mypy_boto3_medialive import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        ChannelRunningWaiter,
        ChannelStoppedWaiter,
        Client,
        DescribeSchedulePaginator,
        InputAttachedWaiter,
        InputDeletedWaiter,
        InputDetachedWaiter,
        ListChannelsPaginator,
        ListInputDevicesPaginator,
        ListInputSecurityGroupsPaginator,
        ListInputsPaginator,
        ListMultiplexProgramsPaginator,
        ListMultiplexesPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        MediaLiveClient,
        MultiplexCreatedWaiter,
        MultiplexDeletedWaiter,
        MultiplexRunningWaiter,
        MultiplexStoppedWaiter,
    )

    session = boto3.Session()

    client: MediaLiveClient = boto3.client("medialive")
    session_client: MediaLiveClient = session.client("medialive")

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

    describe_schedule_paginator: DescribeSchedulePaginator = client.get_paginator("describe_schedule")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_input_devices_paginator: ListInputDevicesPaginator = client.get_paginator("list_input_devices")
    list_input_security_groups_paginator: ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
    list_inputs_paginator: ListInputsPaginator = client.get_paginator("list_inputs")
    list_multiplex_programs_paginator: ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
    list_multiplexes_paginator: ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""
from mypy_boto3_medialive.client import MediaLiveClient
from mypy_boto3_medialive.paginator import (
    DescribeSchedulePaginator,
    ListChannelsPaginator,
    ListInputDevicesPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
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

Client = MediaLiveClient


__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "Client",
    "DescribeSchedulePaginator",
    "InputAttachedWaiter",
    "InputDeletedWaiter",
    "InputDetachedWaiter",
    "ListChannelsPaginator",
    "ListInputDevicesPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "MediaLiveClient",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
)
