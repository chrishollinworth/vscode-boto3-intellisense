"""
Main interface for opsworkscm service.

Usage::

    ```python
    import boto3
    from mypy_boto3_opsworkscm import (
        Client,
        DescribeBackupsPaginator,
        DescribeEventsPaginator,
        DescribeServersPaginator,
        ListTagsForResourcePaginator,
        NodeAssociatedWaiter,
        OpsWorksCMClient,
    )

    session = boto3.Session()

    client: OpsWorksCMClient = boto3.client("opsworkscm")
    session_client: OpsWorksCMClient = session.client("opsworkscm")

    node_associated_waiter: NodeAssociatedWaiter = client.get_waiter("node_associated")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_servers_paginator: DescribeServersPaginator = client.get_paginator("describe_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from mypy_boto3_opsworkscm.client import OpsWorksCMClient
from mypy_boto3_opsworkscm.paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_opsworkscm.waiter import NodeAssociatedWaiter

Client = OpsWorksCMClient


__all__ = (
    "Client",
    "DescribeBackupsPaginator",
    "DescribeEventsPaginator",
    "DescribeServersPaginator",
    "ListTagsForResourcePaginator",
    "NodeAssociatedWaiter",
    "OpsWorksCMClient",
)
