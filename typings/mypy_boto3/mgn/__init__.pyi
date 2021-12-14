"""
Main interface for mgn service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mgn import (
        Client,
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceServersPaginator,
        DescribeVcenterClientsPaginator,
        mgnClient,
    )

    session = boto3.Session()

    client: mgnClient = boto3.client("mgn")
    session_client: mgnClient = session.client("mgn")

    describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
    describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
    describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
    describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
    describe_vcenter_clients_paginator: DescribeVcenterClientsPaginator = client.get_paginator("describe_vcenter_clients")
    ```
"""
from .client import mgnClient
from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceServersPaginator,
    DescribeVcenterClientsPaginator,
)

Client = mgnClient

__all__ = (
    "Client",
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceServersPaginator",
    "DescribeVcenterClientsPaginator",
    "mgnClient",
)
