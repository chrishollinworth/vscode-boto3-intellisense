"""
Main interface for route53-recovery-control-config service.

Usage::

    ```python
    import boto3
    from mypy_boto3_route53_recovery_control_config import (
        Client,
        ClusterCreatedWaiter,
        ClusterDeletedWaiter,
        ControlPanelCreatedWaiter,
        ControlPanelDeletedWaiter,
        Route53RecoveryControlConfigClient,
        RoutingControlCreatedWaiter,
        RoutingControlDeletedWaiter,
    )

    session = boto3.Session()

    client: Route53RecoveryControlConfigClient = boto3.client("route53-recovery-control-config")
    session_client: Route53RecoveryControlConfigClient = session.client("route53-recovery-control-config")

    cluster_created_waiter: ClusterCreatedWaiter = client.get_waiter("cluster_created")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    control_panel_created_waiter: ControlPanelCreatedWaiter = client.get_waiter("control_panel_created")
    control_panel_deleted_waiter: ControlPanelDeletedWaiter = client.get_waiter("control_panel_deleted")
    routing_control_created_waiter: RoutingControlCreatedWaiter = client.get_waiter("routing_control_created")
    routing_control_deleted_waiter: RoutingControlDeletedWaiter = client.get_waiter("routing_control_deleted")
    ```
"""
from .client import Route53RecoveryControlConfigClient
from .waiter import (
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    ControlPanelCreatedWaiter,
    ControlPanelDeletedWaiter,
    RoutingControlCreatedWaiter,
    RoutingControlDeletedWaiter,
)

Client = Route53RecoveryControlConfigClient

__all__ = (
    "Client",
    "ClusterCreatedWaiter",
    "ClusterDeletedWaiter",
    "ControlPanelCreatedWaiter",
    "ControlPanelDeletedWaiter",
    "Route53RecoveryControlConfigClient",
    "RoutingControlCreatedWaiter",
    "RoutingControlDeletedWaiter",
)
