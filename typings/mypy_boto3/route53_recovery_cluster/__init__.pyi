"""
Main interface for route53-recovery-cluster service.

Usage::

    ```python
    import boto3
    from mypy_boto3_route53_recovery_cluster import (
        Client,
        ListRoutingControlsPaginator,
        Route53RecoveryClusterClient,
    )

    session = boto3.Session()

    client: Route53RecoveryClusterClient = boto3.client("route53-recovery-cluster")
    session_client: Route53RecoveryClusterClient = session.client("route53-recovery-cluster")

    list_routing_controls_paginator: ListRoutingControlsPaginator = client.get_paginator("list_routing_controls")
    ```
"""
from .client import Route53RecoveryClusterClient
from .paginator import ListRoutingControlsPaginator

Client = Route53RecoveryClusterClient

__all__ = ("Client", "ListRoutingControlsPaginator", "Route53RecoveryClusterClient")
