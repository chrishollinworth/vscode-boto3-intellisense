"""
Main interface for neptune service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_neptune import (
        Client,
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
        DescribeDBClusterEndpointsPaginator,
        DescribeDBClusterParameterGroupsPaginator,
        DescribeDBClusterParametersPaginator,
        DescribeDBClusterSnapshotsPaginator,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBParameterGroupsPaginator,
        DescribeDBParametersPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeGlobalClustersPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DescribePendingMaintenanceActionsPaginator,
        NeptuneClient,
    )

    session = Session()
    client: NeptuneClient = session.client("neptune")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")

    describe_db_cluster_endpoints_paginator: DescribeDBClusterEndpointsPaginator = client.get_paginator("describe_db_cluster_endpoints")
    describe_db_cluster_parameter_groups_paginator: DescribeDBClusterParameterGroupsPaginator = client.get_paginator("describe_db_cluster_parameter_groups")
    describe_db_cluster_parameters_paginator: DescribeDBClusterParametersPaginator = client.get_paginator("describe_db_cluster_parameters")
    describe_db_cluster_snapshots_paginator: DescribeDBClusterSnapshotsPaginator = client.get_paginator("describe_db_cluster_snapshots")
    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_parameter_groups_paginator: DescribeDBParameterGroupsPaginator = client.get_paginator("describe_db_parameter_groups")
    describe_db_parameters_paginator: DescribeDBParametersPaginator = client.get_paginator("describe_db_parameters")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_global_clusters_paginator: DescribeGlobalClustersPaginator = client.get_paginator("describe_global_clusters")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
    describe_pending_maintenance_actions_paginator: DescribePendingMaintenanceActionsPaginator = client.get_paginator("describe_pending_maintenance_actions")
    ```
"""

from .client import NeptuneClient
from .paginator import (
    DescribeDBClusterEndpointsPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeGlobalClustersPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
)
from .waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

Client = NeptuneClient

__all__ = (
    "Client",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
    "NeptuneClient",
)
