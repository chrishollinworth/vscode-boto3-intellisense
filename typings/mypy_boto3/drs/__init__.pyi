"""
Main interface for drs service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_drs import (
        Client,
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeLaunchConfigurationTemplatesPaginator,
        DescribeRecoveryInstancesPaginator,
        DescribeRecoverySnapshotsPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceNetworksPaginator,
        DescribeSourceServersPaginator,
        DrsClient,
        ListExtensibleSourceServersPaginator,
        ListLaunchActionsPaginator,
        ListStagingAccountsPaginator,
    )

    session = Session()
    client: DrsClient = session.client("drs")

    describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
    describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
    describe_launch_configuration_templates_paginator: DescribeLaunchConfigurationTemplatesPaginator = client.get_paginator("describe_launch_configuration_templates")
    describe_recovery_instances_paginator: DescribeRecoveryInstancesPaginator = client.get_paginator("describe_recovery_instances")
    describe_recovery_snapshots_paginator: DescribeRecoverySnapshotsPaginator = client.get_paginator("describe_recovery_snapshots")
    describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
    describe_source_networks_paginator: DescribeSourceNetworksPaginator = client.get_paginator("describe_source_networks")
    describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
    list_extensible_source_servers_paginator: ListExtensibleSourceServersPaginator = client.get_paginator("list_extensible_source_servers")
    list_launch_actions_paginator: ListLaunchActionsPaginator = client.get_paginator("list_launch_actions")
    list_staging_accounts_paginator: ListStagingAccountsPaginator = client.get_paginator("list_staging_accounts")
    ```
"""

from .client import DrsClient
from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeLaunchConfigurationTemplatesPaginator,
    DescribeRecoveryInstancesPaginator,
    DescribeRecoverySnapshotsPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceNetworksPaginator,
    DescribeSourceServersPaginator,
    ListExtensibleSourceServersPaginator,
    ListLaunchActionsPaginator,
    ListStagingAccountsPaginator,
)

Client = DrsClient

__all__ = (
    "Client",
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeLaunchConfigurationTemplatesPaginator",
    "DescribeRecoveryInstancesPaginator",
    "DescribeRecoverySnapshotsPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceNetworksPaginator",
    "DescribeSourceServersPaginator",
    "DrsClient",
    "ListExtensibleSourceServersPaginator",
    "ListLaunchActionsPaginator",
    "ListStagingAccountsPaginator",
)
