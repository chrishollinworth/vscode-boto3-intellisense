"""
Main interface for redshift service.

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift import (
        Client,
        ClusterAvailableWaiter,
        ClusterDeletedWaiter,
        ClusterRestoredWaiter,
        DescribeClusterDbRevisionsPaginator,
        DescribeClusterParameterGroupsPaginator,
        DescribeClusterParametersPaginator,
        DescribeClusterSecurityGroupsPaginator,
        DescribeClusterSnapshotsPaginator,
        DescribeClusterSubnetGroupsPaginator,
        DescribeClusterTracksPaginator,
        DescribeClusterVersionsPaginator,
        DescribeClustersPaginator,
        DescribeDefaultClusterParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeHsmClientCertificatesPaginator,
        DescribeHsmConfigurationsPaginator,
        DescribeNodeConfigurationOptionsPaginator,
        DescribeOrderableClusterOptionsPaginator,
        DescribeReservedNodeOfferingsPaginator,
        DescribeReservedNodesPaginator,
        DescribeScheduledActionsPaginator,
        DescribeSnapshotCopyGrantsPaginator,
        DescribeSnapshotSchedulesPaginator,
        DescribeTableRestoreStatusPaginator,
        DescribeTagsPaginator,
        DescribeUsageLimitsPaginator,
        GetReservedNodeExchangeOfferingsPaginator,
        RedshiftClient,
        SnapshotAvailableWaiter,
    )

    session = boto3.Session()

    client: RedshiftClient = boto3.client("redshift")
    session_client: RedshiftClient = session.client("redshift")

    cluster_available_waiter: ClusterAvailableWaiter = client.get_waiter("cluster_available")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    cluster_restored_waiter: ClusterRestoredWaiter = client.get_waiter("cluster_restored")
    snapshot_available_waiter: SnapshotAvailableWaiter = client.get_waiter("snapshot_available")

    describe_cluster_db_revisions_paginator: DescribeClusterDbRevisionsPaginator = client.get_paginator("describe_cluster_db_revisions")
    describe_cluster_parameter_groups_paginator: DescribeClusterParameterGroupsPaginator = client.get_paginator("describe_cluster_parameter_groups")
    describe_cluster_parameters_paginator: DescribeClusterParametersPaginator = client.get_paginator("describe_cluster_parameters")
    describe_cluster_security_groups_paginator: DescribeClusterSecurityGroupsPaginator = client.get_paginator("describe_cluster_security_groups")
    describe_cluster_snapshots_paginator: DescribeClusterSnapshotsPaginator = client.get_paginator("describe_cluster_snapshots")
    describe_cluster_subnet_groups_paginator: DescribeClusterSubnetGroupsPaginator = client.get_paginator("describe_cluster_subnet_groups")
    describe_cluster_tracks_paginator: DescribeClusterTracksPaginator = client.get_paginator("describe_cluster_tracks")
    describe_cluster_versions_paginator: DescribeClusterVersionsPaginator = client.get_paginator("describe_cluster_versions")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_default_cluster_parameters_paginator: DescribeDefaultClusterParametersPaginator = client.get_paginator("describe_default_cluster_parameters")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_hsm_client_certificates_paginator: DescribeHsmClientCertificatesPaginator = client.get_paginator("describe_hsm_client_certificates")
    describe_hsm_configurations_paginator: DescribeHsmConfigurationsPaginator = client.get_paginator("describe_hsm_configurations")
    describe_node_configuration_options_paginator: DescribeNodeConfigurationOptionsPaginator = client.get_paginator("describe_node_configuration_options")
    describe_orderable_cluster_options_paginator: DescribeOrderableClusterOptionsPaginator = client.get_paginator("describe_orderable_cluster_options")
    describe_reserved_node_offerings_paginator: DescribeReservedNodeOfferingsPaginator = client.get_paginator("describe_reserved_node_offerings")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    describe_snapshot_copy_grants_paginator: DescribeSnapshotCopyGrantsPaginator = client.get_paginator("describe_snapshot_copy_grants")
    describe_snapshot_schedules_paginator: DescribeSnapshotSchedulesPaginator = client.get_paginator("describe_snapshot_schedules")
    describe_table_restore_status_paginator: DescribeTableRestoreStatusPaginator = client.get_paginator("describe_table_restore_status")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_usage_limits_paginator: DescribeUsageLimitsPaginator = client.get_paginator("describe_usage_limits")
    get_reserved_node_exchange_offerings_paginator: GetReservedNodeExchangeOfferingsPaginator = client.get_paginator("get_reserved_node_exchange_offerings")
    ```
"""
from mypy_boto3_redshift.client import RedshiftClient
from mypy_boto3_redshift.paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClustersPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    DescribeUsageLimitsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
)
from mypy_boto3_redshift.waiter import (
    ClusterAvailableWaiter,
    ClusterDeletedWaiter,
    ClusterRestoredWaiter,
    SnapshotAvailableWaiter,
)

Client = RedshiftClient


__all__ = (
    "Client",
    "ClusterAvailableWaiter",
    "ClusterDeletedWaiter",
    "ClusterRestoredWaiter",
    "DescribeClusterDbRevisionsPaginator",
    "DescribeClusterParameterGroupsPaginator",
    "DescribeClusterParametersPaginator",
    "DescribeClusterSecurityGroupsPaginator",
    "DescribeClusterSnapshotsPaginator",
    "DescribeClusterSubnetGroupsPaginator",
    "DescribeClusterTracksPaginator",
    "DescribeClusterVersionsPaginator",
    "DescribeClustersPaginator",
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
    "DescribeReservedNodeOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeSnapshotCopyGrantsPaginator",
    "DescribeSnapshotSchedulesPaginator",
    "DescribeTableRestoreStatusPaginator",
    "DescribeTagsPaginator",
    "DescribeUsageLimitsPaginator",
    "GetReservedNodeExchangeOfferingsPaginator",
    "RedshiftClient",
    "SnapshotAvailableWaiter",
)
