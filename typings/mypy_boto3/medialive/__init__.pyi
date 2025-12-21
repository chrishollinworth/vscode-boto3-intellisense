"""
Main interface for medialive service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_medialive import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        ChannelPlacementGroupAssignedWaiter,
        ChannelPlacementGroupDeletedWaiter,
        ChannelPlacementGroupUnassignedWaiter,
        ChannelRunningWaiter,
        ChannelStoppedWaiter,
        Client,
        ClusterCreatedWaiter,
        ClusterDeletedWaiter,
        DescribeSchedulePaginator,
        InputAttachedWaiter,
        InputDeletedWaiter,
        InputDetachedWaiter,
        ListAlertsPaginator,
        ListChannelPlacementGroupsPaginator,
        ListChannelsPaginator,
        ListCloudWatchAlarmTemplateGroupsPaginator,
        ListCloudWatchAlarmTemplatesPaginator,
        ListClusterAlertsPaginator,
        ListClustersPaginator,
        ListEventBridgeRuleTemplateGroupsPaginator,
        ListEventBridgeRuleTemplatesPaginator,
        ListInputDeviceTransfersPaginator,
        ListInputDevicesPaginator,
        ListInputSecurityGroupsPaginator,
        ListInputsPaginator,
        ListMultiplexAlertsPaginator,
        ListMultiplexProgramsPaginator,
        ListMultiplexesPaginator,
        ListNetworksPaginator,
        ListNodesPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        ListSdiSourcesPaginator,
        ListSignalMapsPaginator,
        MediaLiveClient,
        MultiplexCreatedWaiter,
        MultiplexDeletedWaiter,
        MultiplexRunningWaiter,
        MultiplexStoppedWaiter,
        NodeDeregisteredWaiter,
        NodeRegisteredWaiter,
        SignalMapCreatedWaiter,
        SignalMapMonitorDeletedWaiter,
        SignalMapMonitorDeployedWaiter,
        SignalMapUpdatedWaiter,
    )

    session = Session()
    client: MediaLiveClient = session.client("medialive")

    channel_created_waiter: ChannelCreatedWaiter = client.get_waiter("channel_created")
    channel_deleted_waiter: ChannelDeletedWaiter = client.get_waiter("channel_deleted")
    channel_placement_group_assigned_waiter: ChannelPlacementGroupAssignedWaiter = client.get_waiter("channel_placement_group_assigned")
    channel_placement_group_deleted_waiter: ChannelPlacementGroupDeletedWaiter = client.get_waiter("channel_placement_group_deleted")
    channel_placement_group_unassigned_waiter: ChannelPlacementGroupUnassignedWaiter = client.get_waiter("channel_placement_group_unassigned")
    channel_running_waiter: ChannelRunningWaiter = client.get_waiter("channel_running")
    channel_stopped_waiter: ChannelStoppedWaiter = client.get_waiter("channel_stopped")
    cluster_created_waiter: ClusterCreatedWaiter = client.get_waiter("cluster_created")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    input_attached_waiter: InputAttachedWaiter = client.get_waiter("input_attached")
    input_deleted_waiter: InputDeletedWaiter = client.get_waiter("input_deleted")
    input_detached_waiter: InputDetachedWaiter = client.get_waiter("input_detached")
    multiplex_created_waiter: MultiplexCreatedWaiter = client.get_waiter("multiplex_created")
    multiplex_deleted_waiter: MultiplexDeletedWaiter = client.get_waiter("multiplex_deleted")
    multiplex_running_waiter: MultiplexRunningWaiter = client.get_waiter("multiplex_running")
    multiplex_stopped_waiter: MultiplexStoppedWaiter = client.get_waiter("multiplex_stopped")
    node_deregistered_waiter: NodeDeregisteredWaiter = client.get_waiter("node_deregistered")
    node_registered_waiter: NodeRegisteredWaiter = client.get_waiter("node_registered")
    signal_map_created_waiter: SignalMapCreatedWaiter = client.get_waiter("signal_map_created")
    signal_map_monitor_deleted_waiter: SignalMapMonitorDeletedWaiter = client.get_waiter("signal_map_monitor_deleted")
    signal_map_monitor_deployed_waiter: SignalMapMonitorDeployedWaiter = client.get_waiter("signal_map_monitor_deployed")
    signal_map_updated_waiter: SignalMapUpdatedWaiter = client.get_waiter("signal_map_updated")

    describe_schedule_paginator: DescribeSchedulePaginator = client.get_paginator("describe_schedule")
    list_alerts_paginator: ListAlertsPaginator = client.get_paginator("list_alerts")
    list_channel_placement_groups_paginator: ListChannelPlacementGroupsPaginator = client.get_paginator("list_channel_placement_groups")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_cloud_watch_alarm_template_groups_paginator: ListCloudWatchAlarmTemplateGroupsPaginator = client.get_paginator("list_cloud_watch_alarm_template_groups")
    list_cloud_watch_alarm_templates_paginator: ListCloudWatchAlarmTemplatesPaginator = client.get_paginator("list_cloud_watch_alarm_templates")
    list_cluster_alerts_paginator: ListClusterAlertsPaginator = client.get_paginator("list_cluster_alerts")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_event_bridge_rule_template_groups_paginator: ListEventBridgeRuleTemplateGroupsPaginator = client.get_paginator("list_event_bridge_rule_template_groups")
    list_event_bridge_rule_templates_paginator: ListEventBridgeRuleTemplatesPaginator = client.get_paginator("list_event_bridge_rule_templates")
    list_input_device_transfers_paginator: ListInputDeviceTransfersPaginator = client.get_paginator("list_input_device_transfers")
    list_input_devices_paginator: ListInputDevicesPaginator = client.get_paginator("list_input_devices")
    list_input_security_groups_paginator: ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
    list_inputs_paginator: ListInputsPaginator = client.get_paginator("list_inputs")
    list_multiplex_alerts_paginator: ListMultiplexAlertsPaginator = client.get_paginator("list_multiplex_alerts")
    list_multiplex_programs_paginator: ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
    list_multiplexes_paginator: ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
    list_networks_paginator: ListNetworksPaginator = client.get_paginator("list_networks")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    list_sdi_sources_paginator: ListSdiSourcesPaginator = client.get_paginator("list_sdi_sources")
    list_signal_maps_paginator: ListSignalMapsPaginator = client.get_paginator("list_signal_maps")
    ```
"""

from .client import MediaLiveClient
from .paginator import (
    DescribeSchedulePaginator,
    ListAlertsPaginator,
    ListChannelPlacementGroupsPaginator,
    ListChannelsPaginator,
    ListCloudWatchAlarmTemplateGroupsPaginator,
    ListCloudWatchAlarmTemplatesPaginator,
    ListClusterAlertsPaginator,
    ListClustersPaginator,
    ListEventBridgeRuleTemplateGroupsPaginator,
    ListEventBridgeRuleTemplatesPaginator,
    ListInputDevicesPaginator,
    ListInputDeviceTransfersPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexAlertsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListNetworksPaginator,
    ListNodesPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
    ListSdiSourcesPaginator,
    ListSignalMapsPaginator,
)
from .waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    ChannelPlacementGroupAssignedWaiter,
    ChannelPlacementGroupDeletedWaiter,
    ChannelPlacementGroupUnassignedWaiter,
    ChannelRunningWaiter,
    ChannelStoppedWaiter,
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    InputAttachedWaiter,
    InputDeletedWaiter,
    InputDetachedWaiter,
    MultiplexCreatedWaiter,
    MultiplexDeletedWaiter,
    MultiplexRunningWaiter,
    MultiplexStoppedWaiter,
    NodeDeregisteredWaiter,
    NodeRegisteredWaiter,
    SignalMapCreatedWaiter,
    SignalMapMonitorDeletedWaiter,
    SignalMapMonitorDeployedWaiter,
    SignalMapUpdatedWaiter,
)

Client = MediaLiveClient

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelPlacementGroupAssignedWaiter",
    "ChannelPlacementGroupDeletedWaiter",
    "ChannelPlacementGroupUnassignedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "Client",
    "ClusterCreatedWaiter",
    "ClusterDeletedWaiter",
    "DescribeSchedulePaginator",
    "InputAttachedWaiter",
    "InputDeletedWaiter",
    "InputDetachedWaiter",
    "ListAlertsPaginator",
    "ListChannelPlacementGroupsPaginator",
    "ListChannelsPaginator",
    "ListCloudWatchAlarmTemplateGroupsPaginator",
    "ListCloudWatchAlarmTemplatesPaginator",
    "ListClusterAlertsPaginator",
    "ListClustersPaginator",
    "ListEventBridgeRuleTemplateGroupsPaginator",
    "ListEventBridgeRuleTemplatesPaginator",
    "ListInputDeviceTransfersPaginator",
    "ListInputDevicesPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexAlertsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListNetworksPaginator",
    "ListNodesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "ListSdiSourcesPaginator",
    "ListSignalMapsPaginator",
    "MediaLiveClient",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
    "NodeDeregisteredWaiter",
    "NodeRegisteredWaiter",
    "SignalMapCreatedWaiter",
    "SignalMapMonitorDeletedWaiter",
    "SignalMapMonitorDeployedWaiter",
    "SignalMapUpdatedWaiter",
)
