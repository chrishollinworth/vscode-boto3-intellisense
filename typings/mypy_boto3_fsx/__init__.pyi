"""
Main interface for fsx service.

Usage::

    ```python
    import boto3
    from mypy_boto3_fsx import (
        Client,
        DescribeBackupsPaginator,
        DescribeFileSystemsPaginator,
        DescribeStorageVirtualMachinesPaginator,
        DescribeVolumesPaginator,
        FSxClient,
        ListTagsForResourcePaginator,
    )

    session = boto3.Session()

    client: FSxClient = boto3.client("fsx")
    session_client: FSxClient = session.client("fsx")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_storage_virtual_machines_paginator: DescribeStorageVirtualMachinesPaginator = client.get_paginator("describe_storage_virtual_machines")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import FSxClient
from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    DescribeStorageVirtualMachinesPaginator,
    DescribeVolumesPaginator,
    ListTagsForResourcePaginator,
)

Client = FSxClient

__all__ = (
    "Client",
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeStorageVirtualMachinesPaginator",
    "DescribeVolumesPaginator",
    "FSxClient",
    "ListTagsForResourcePaginator",
)
