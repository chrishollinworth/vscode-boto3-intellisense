"""
Main interface for efs service.

Usage::

    ```python
    import boto3
    from mypy_boto3_efs import (
        Client,
        DescribeAccessPointsPaginator,
        DescribeFileSystemsPaginator,
        DescribeMountTargetsPaginator,
        DescribeReplicationConfigurationsPaginator,
        DescribeTagsPaginator,
        EFSClient,
    )

    session = boto3.Session()

    client: EFSClient = boto3.client("efs")
    session_client: EFSClient = session.client("efs")

    describe_access_points_paginator: DescribeAccessPointsPaginator = client.get_paginator("describe_access_points")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_mount_targets_paginator: DescribeMountTargetsPaginator = client.get_paginator("describe_mount_targets")
    describe_replication_configurations_paginator: DescribeReplicationConfigurationsPaginator = client.get_paginator("describe_replication_configurations")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    ```
"""

from .client import EFSClient
from .paginator import (
    DescribeAccessPointsPaginator,
    DescribeFileSystemsPaginator,
    DescribeMountTargetsPaginator,
    DescribeReplicationConfigurationsPaginator,
    DescribeTagsPaginator,
)

Client = EFSClient

__all__ = (
    "Client",
    "DescribeAccessPointsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeMountTargetsPaginator",
    "DescribeReplicationConfigurationsPaginator",
    "DescribeTagsPaginator",
    "EFSClient",
)
