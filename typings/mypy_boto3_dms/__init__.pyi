"""
Main interface for dms service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dms import (
        Client,
        DatabaseMigrationServiceClient,
        DescribeCertificatesPaginator,
        DescribeConnectionsPaginator,
        DescribeEndpointTypesPaginator,
        DescribeEndpointsPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeOrderableReplicationInstancesPaginator,
        DescribeReplicationInstancesPaginator,
        DescribeReplicationSubnetGroupsPaginator,
        DescribeReplicationTaskAssessmentResultsPaginator,
        DescribeReplicationTasksPaginator,
        DescribeSchemasPaginator,
        DescribeTableStatisticsPaginator,
        EndpointDeletedWaiter,
        ReplicationInstanceAvailableWaiter,
        ReplicationInstanceDeletedWaiter,
        ReplicationTaskDeletedWaiter,
        ReplicationTaskReadyWaiter,
        ReplicationTaskRunningWaiter,
        ReplicationTaskStoppedWaiter,
        TestConnectionSucceedsWaiter,
    )

    session = boto3.Session()

    client: DatabaseMigrationServiceClient = boto3.client("dms")
    session_client: DatabaseMigrationServiceClient = session.client("dms")

    endpoint_deleted_waiter: EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
    replication_instance_available_waiter: ReplicationInstanceAvailableWaiter = client.get_waiter("replication_instance_available")
    replication_instance_deleted_waiter: ReplicationInstanceDeletedWaiter = client.get_waiter("replication_instance_deleted")
    replication_task_deleted_waiter: ReplicationTaskDeletedWaiter = client.get_waiter("replication_task_deleted")
    replication_task_ready_waiter: ReplicationTaskReadyWaiter = client.get_waiter("replication_task_ready")
    replication_task_running_waiter: ReplicationTaskRunningWaiter = client.get_waiter("replication_task_running")
    replication_task_stopped_waiter: ReplicationTaskStoppedWaiter = client.get_waiter("replication_task_stopped")
    test_connection_succeeds_waiter: TestConnectionSucceedsWaiter = client.get_waiter("test_connection_succeeds")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_connections_paginator: DescribeConnectionsPaginator = client.get_paginator("describe_connections")
    describe_endpoint_types_paginator: DescribeEndpointTypesPaginator = client.get_paginator("describe_endpoint_types")
    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_orderable_replication_instances_paginator: DescribeOrderableReplicationInstancesPaginator = client.get_paginator("describe_orderable_replication_instances")
    describe_replication_instances_paginator: DescribeReplicationInstancesPaginator = client.get_paginator("describe_replication_instances")
    describe_replication_subnet_groups_paginator: DescribeReplicationSubnetGroupsPaginator = client.get_paginator("describe_replication_subnet_groups")
    describe_replication_task_assessment_results_paginator: DescribeReplicationTaskAssessmentResultsPaginator = client.get_paginator("describe_replication_task_assessment_results")
    describe_replication_tasks_paginator: DescribeReplicationTasksPaginator = client.get_paginator("describe_replication_tasks")
    describe_schemas_paginator: DescribeSchemasPaginator = client.get_paginator("describe_schemas")
    describe_table_statistics_paginator: DescribeTableStatisticsPaginator = client.get_paginator("describe_table_statistics")
    ```
"""
from mypy_boto3_dms.client import DatabaseMigrationServiceClient
from mypy_boto3_dms.paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
    DescribeEndpointsPaginator,
    DescribeEndpointTypesPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeOrderableReplicationInstancesPaginator,
    DescribeReplicationInstancesPaginator,
    DescribeReplicationSubnetGroupsPaginator,
    DescribeReplicationTaskAssessmentResultsPaginator,
    DescribeReplicationTasksPaginator,
    DescribeSchemasPaginator,
    DescribeTableStatisticsPaginator,
)
from mypy_boto3_dms.waiter import (
    EndpointDeletedWaiter,
    ReplicationInstanceAvailableWaiter,
    ReplicationInstanceDeletedWaiter,
    ReplicationTaskDeletedWaiter,
    ReplicationTaskReadyWaiter,
    ReplicationTaskRunningWaiter,
    ReplicationTaskStoppedWaiter,
    TestConnectionSucceedsWaiter,
)

Client = DatabaseMigrationServiceClient


__all__ = (
    "Client",
    "DatabaseMigrationServiceClient",
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)
