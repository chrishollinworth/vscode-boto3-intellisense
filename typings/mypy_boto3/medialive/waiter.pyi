"""
Type annotations for medialive service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_medialive.client import MediaLiveClient
    from mypy_boto3_medialive.waiter import (
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
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef,
    DescribeChannelPlacementGroupRequestWaitExtraTypeDef,
    DescribeChannelPlacementGroupRequestWaitTypeDef,
    DescribeChannelRequestWaitExtraExtraExtraTypeDef,
    DescribeChannelRequestWaitExtraExtraTypeDef,
    DescribeChannelRequestWaitExtraTypeDef,
    DescribeChannelRequestWaitTypeDef,
    DescribeClusterRequestWaitExtraTypeDef,
    DescribeClusterRequestWaitTypeDef,
    DescribeInputRequestWaitExtraExtraTypeDef,
    DescribeInputRequestWaitExtraTypeDef,
    DescribeInputRequestWaitTypeDef,
    DescribeMultiplexRequestWaitExtraExtraExtraTypeDef,
    DescribeMultiplexRequestWaitExtraExtraTypeDef,
    DescribeMultiplexRequestWaitExtraTypeDef,
    DescribeMultiplexRequestWaitTypeDef,
    DescribeNodeRequestWaitExtraTypeDef,
    DescribeNodeRequestWaitTypeDef,
    GetSignalMapRequestWaitExtraExtraExtraTypeDef,
    GetSignalMapRequestWaitExtraExtraTypeDef,
    GetSignalMapRequestWaitExtraTypeDef,
    GetSignalMapRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelPlacementGroupAssignedWaiter",
    "ChannelPlacementGroupDeletedWaiter",
    "ChannelPlacementGroupUnassignedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "ClusterCreatedWaiter",
    "ClusterDeletedWaiter",
    "InputAttachedWaiter",
    "InputDeletedWaiter",
    "InputDetachedWaiter",
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

class ChannelCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelCreated.html#MediaLive.Waiter.ChannelCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelCreated.html#MediaLive.Waiter.ChannelCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelcreatedwaiter)
        """

class ChannelDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelDeleted.html#MediaLive.Waiter.ChannelDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channeldeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelDeleted.html#MediaLive.Waiter.ChannelDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channeldeletedwaiter)
        """

class ChannelPlacementGroupAssignedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupAssigned.html#MediaLive.Waiter.ChannelPlacementGroupAssigned)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupassignedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelPlacementGroupRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupAssigned.html#MediaLive.Waiter.ChannelPlacementGroupAssigned.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupassignedwaiter)
        """

class ChannelPlacementGroupDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupDeleted.html#MediaLive.Waiter.ChannelPlacementGroupDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupDeleted.html#MediaLive.Waiter.ChannelPlacementGroupDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupdeletedwaiter)
        """

class ChannelPlacementGroupUnassignedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupUnassigned.html#MediaLive.Waiter.ChannelPlacementGroupUnassigned)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupunassignedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelPlacementGroupRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelPlacementGroupUnassigned.html#MediaLive.Waiter.ChannelPlacementGroupUnassigned.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelplacementgroupunassignedwaiter)
        """

class ChannelRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelRunning.html#MediaLive.Waiter.ChannelRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelrunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelRunning.html#MediaLive.Waiter.ChannelRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelrunningwaiter)
        """

class ChannelStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelStopped.html#MediaLive.Waiter.ChannelStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChannelRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ChannelStopped.html#MediaLive.Waiter.ChannelStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#channelstoppedwaiter)
        """

class ClusterCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ClusterCreated.html#MediaLive.Waiter.ClusterCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#clustercreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ClusterCreated.html#MediaLive.Waiter.ClusterCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#clustercreatedwaiter)
        """

class ClusterDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ClusterDeleted.html#MediaLive.Waiter.ClusterDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#clusterdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/ClusterDeleted.html#MediaLive.Waiter.ClusterDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#clusterdeletedwaiter)
        """

class InputAttachedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputAttached.html#MediaLive.Waiter.InputAttached)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputattachedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInputRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputAttached.html#MediaLive.Waiter.InputAttached.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputattachedwaiter)
        """

class InputDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputDeleted.html#MediaLive.Waiter.InputDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInputRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputDeleted.html#MediaLive.Waiter.InputDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputdeletedwaiter)
        """

class InputDetachedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputDetached.html#MediaLive.Waiter.InputDetached)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputdetachedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInputRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/InputDetached.html#MediaLive.Waiter.InputDetached.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#inputdetachedwaiter)
        """

class MultiplexCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexCreated.html#MediaLive.Waiter.MultiplexCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMultiplexRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexCreated.html#MediaLive.Waiter.MultiplexCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexcreatedwaiter)
        """

class MultiplexDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexDeleted.html#MediaLive.Waiter.MultiplexDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMultiplexRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexDeleted.html#MediaLive.Waiter.MultiplexDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexdeletedwaiter)
        """

class MultiplexRunningWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexRunning.html#MediaLive.Waiter.MultiplexRunning)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexrunningwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMultiplexRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexRunning.html#MediaLive.Waiter.MultiplexRunning.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexrunningwaiter)
        """

class MultiplexStoppedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexStopped.html#MediaLive.Waiter.MultiplexStopped)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexstoppedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMultiplexRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/MultiplexStopped.html#MediaLive.Waiter.MultiplexStopped.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#multiplexstoppedwaiter)
        """

class NodeDeregisteredWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/NodeDeregistered.html#MediaLive.Waiter.NodeDeregistered)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#nodederegisteredwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNodeRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/NodeDeregistered.html#MediaLive.Waiter.NodeDeregistered.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#nodederegisteredwaiter)
        """

class NodeRegisteredWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/NodeRegistered.html#MediaLive.Waiter.NodeRegistered)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#noderegisteredwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNodeRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/NodeRegistered.html#MediaLive.Waiter.NodeRegistered.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#noderegisteredwaiter)
        """

class SignalMapCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapCreated.html#MediaLive.Waiter.SignalMapCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSignalMapRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapCreated.html#MediaLive.Waiter.SignalMapCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapcreatedwaiter)
        """

class SignalMapMonitorDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapMonitorDeleted.html#MediaLive.Waiter.SignalMapMonitorDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapmonitordeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSignalMapRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapMonitorDeleted.html#MediaLive.Waiter.SignalMapMonitorDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapmonitordeletedwaiter)
        """

class SignalMapMonitorDeployedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapMonitorDeployed.html#MediaLive.Waiter.SignalMapMonitorDeployed)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapmonitordeployedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSignalMapRequestWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapMonitorDeployed.html#MediaLive.Waiter.SignalMapMonitorDeployed.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapmonitordeployedwaiter)
        """

class SignalMapUpdatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapUpdated.html#MediaLive.Waiter.SignalMapUpdated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapupdatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSignalMapRequestWaitExtraExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive/waiter/SignalMapUpdated.html#MediaLive.Waiter.SignalMapUpdated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters/#signalmapupdatedwaiter)
        """
