"""
Main interface for redshift-serverless service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_redshift_serverless import (
        Client,
        ListCustomDomainAssociationsPaginator,
        ListEndpointAccessPaginator,
        ListManagedWorkgroupsPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListReservationOfferingsPaginator,
        ListReservationsPaginator,
        ListScheduledActionsPaginator,
        ListSnapshotCopyConfigurationsPaginator,
        ListSnapshotsPaginator,
        ListTableRestoreStatusPaginator,
        ListTracksPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
        RedshiftServerlessClient,
    )

    session = Session()
    client: RedshiftServerlessClient = session.client("redshift-serverless")

    list_custom_domain_associations_paginator: ListCustomDomainAssociationsPaginator = client.get_paginator("list_custom_domain_associations")
    list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
    list_managed_workgroups_paginator: ListManagedWorkgroupsPaginator = client.get_paginator("list_managed_workgroups")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
    list_reservation_offerings_paginator: ListReservationOfferingsPaginator = client.get_paginator("list_reservation_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    list_scheduled_actions_paginator: ListScheduledActionsPaginator = client.get_paginator("list_scheduled_actions")
    list_snapshot_copy_configurations_paginator: ListSnapshotCopyConfigurationsPaginator = client.get_paginator("list_snapshot_copy_configurations")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_table_restore_status_paginator: ListTableRestoreStatusPaginator = client.get_paginator("list_table_restore_status")
    list_tracks_paginator: ListTracksPaginator = client.get_paginator("list_tracks")
    list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
    list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""

from .client import RedshiftServerlessClient
from .paginator import (
    ListCustomDomainAssociationsPaginator,
    ListEndpointAccessPaginator,
    ListManagedWorkgroupsPaginator,
    ListNamespacesPaginator,
    ListRecoveryPointsPaginator,
    ListReservationOfferingsPaginator,
    ListReservationsPaginator,
    ListScheduledActionsPaginator,
    ListSnapshotCopyConfigurationsPaginator,
    ListSnapshotsPaginator,
    ListTableRestoreStatusPaginator,
    ListTracksPaginator,
    ListUsageLimitsPaginator,
    ListWorkgroupsPaginator,
)

Client = RedshiftServerlessClient

__all__ = (
    "Client",
    "ListCustomDomainAssociationsPaginator",
    "ListEndpointAccessPaginator",
    "ListManagedWorkgroupsPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListReservationOfferingsPaginator",
    "ListReservationsPaginator",
    "ListScheduledActionsPaginator",
    "ListSnapshotCopyConfigurationsPaginator",
    "ListSnapshotsPaginator",
    "ListTableRestoreStatusPaginator",
    "ListTracksPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
    "RedshiftServerlessClient",
)
