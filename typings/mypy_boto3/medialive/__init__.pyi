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
        ListCloudWatchAlarmTemplateGroupsPaginator,
        ListCloudWatchAlarmTemplatesPaginator,
        ListEventBridgeRuleTemplateGroupsPaginator,
        ListEventBridgeRuleTemplatesPaginator,
        ListInputDeviceTransfersPaginator,
        ListInputDevicesPaginator,
        ListInputSecurityGroupsPaginator,
        ListInputsPaginator,
        ListMultiplexProgramsPaginator,
        ListMultiplexesPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        ListSignalMapsPaginator,
        MediaLiveClient,
        MultiplexCreatedWaiter,
        MultiplexDeletedWaiter,
        MultiplexRunningWaiter,
        MultiplexStoppedWaiter,
        SignalMapCreatedWaiter,
        SignalMapMonitorDeletedWaiter,
        SignalMapMonitorDeployedWaiter,
        SignalMapUpdatedWaiter,
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
    signal_map_created_waiter: SignalMapCreatedWaiter = client.get_waiter("signal_map_created")
    signal_map_monitor_deleted_waiter: SignalMapMonitorDeletedWaiter = client.get_waiter("signal_map_monitor_deleted")
    signal_map_monitor_deployed_waiter: SignalMapMonitorDeployedWaiter = client.get_waiter("signal_map_monitor_deployed")
    signal_map_updated_waiter: SignalMapUpdatedWaiter = client.get_waiter("signal_map_updated")

    describe_schedule_paginator: DescribeSchedulePaginator = client.get_paginator("describe_schedule")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_cloud_watch_alarm_template_groups_paginator: ListCloudWatchAlarmTemplateGroupsPaginator = client.get_paginator("list_cloud_watch_alarm_template_groups")
    list_cloud_watch_alarm_templates_paginator: ListCloudWatchAlarmTemplatesPaginator = client.get_paginator("list_cloud_watch_alarm_templates")
    list_event_bridge_rule_template_groups_paginator: ListEventBridgeRuleTemplateGroupsPaginator = client.get_paginator("list_event_bridge_rule_template_groups")
    list_event_bridge_rule_templates_paginator: ListEventBridgeRuleTemplatesPaginator = client.get_paginator("list_event_bridge_rule_templates")
    list_input_device_transfers_paginator: ListInputDeviceTransfersPaginator = client.get_paginator("list_input_device_transfers")
    list_input_devices_paginator: ListInputDevicesPaginator = client.get_paginator("list_input_devices")
    list_input_security_groups_paginator: ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
    list_inputs_paginator: ListInputsPaginator = client.get_paginator("list_inputs")
    list_multiplex_programs_paginator: ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
    list_multiplexes_paginator: ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    list_signal_maps_paginator: ListSignalMapsPaginator = client.get_paginator("list_signal_maps")
    ```
"""

from .client import MediaLiveClient
from .paginator import (
    DescribeSchedulePaginator,
    ListChannelsPaginator,
    ListCloudWatchAlarmTemplateGroupsPaginator,
    ListCloudWatchAlarmTemplatesPaginator,
    ListEventBridgeRuleTemplateGroupsPaginator,
    ListEventBridgeRuleTemplatesPaginator,
    ListInputDevicesPaginator,
    ListInputDeviceTransfersPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
    ListSignalMapsPaginator,
)
from .waiter import (
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
    SignalMapCreatedWaiter,
    SignalMapMonitorDeletedWaiter,
    SignalMapMonitorDeployedWaiter,
    SignalMapUpdatedWaiter,
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
    "ListCloudWatchAlarmTemplateGroupsPaginator",
    "ListCloudWatchAlarmTemplatesPaginator",
    "ListEventBridgeRuleTemplateGroupsPaginator",
    "ListEventBridgeRuleTemplatesPaginator",
    "ListInputDeviceTransfersPaginator",
    "ListInputDevicesPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "ListSignalMapsPaginator",
    "MediaLiveClient",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
    "SignalMapCreatedWaiter",
    "SignalMapMonitorDeletedWaiter",
    "SignalMapMonitorDeployedWaiter",
    "SignalMapUpdatedWaiter",
)
