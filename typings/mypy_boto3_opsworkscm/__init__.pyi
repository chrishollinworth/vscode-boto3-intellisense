"""
Main interface for opsworkscm service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opsworkscm import (
        Client,
        DescribeBackupsPaginator,
        DescribeEventsPaginator,
        DescribeServersPaginator,
        ListTagsForResourcePaginator,
        NodeAssociatedWaiter,
        OpsWorksCMClient,
    )

    session = Session()
    client: OpsWorksCMClient = session.client("opsworkscm")

    node_associated_waiter: NodeAssociatedWaiter = client.get_waiter("node_associated")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_servers_paginator: DescribeServersPaginator = client.get_paginator("describe_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from .client import OpsWorksCMClient
from .paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from .waiter import NodeAssociatedWaiter

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
