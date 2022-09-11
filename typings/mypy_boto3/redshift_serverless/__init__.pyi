"""
Main interface for redshift-serverless service.

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift_serverless import (
        Client,
        ListEndpointAccessPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListSnapshotsPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
        RedshiftServerlessClient,
    )

    session = boto3.Session()

    client: RedshiftServerlessClient = boto3.client("redshift-serverless")
    session_client: RedshiftServerlessClient = session.client("redshift-serverless")

    list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
    list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""
from .client import RedshiftServerlessClient
from .paginator import (
    ListEndpointAccessPaginator,
    ListNamespacesPaginator,
    ListRecoveryPointsPaginator,
    ListSnapshotsPaginator,
    ListUsageLimitsPaginator,
    ListWorkgroupsPaginator,
)

Client = RedshiftServerlessClient

__all__ = (
    "Client",
    "ListEndpointAccessPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListSnapshotsPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
    "RedshiftServerlessClient",
)