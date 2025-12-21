"""
Main interface for fsx service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_fsx import (
        Client,
        DescribeBackupsPaginator,
        DescribeFileSystemsPaginator,
        DescribeS3AccessPointAttachmentsPaginator,
        DescribeSnapshotsPaginator,
        DescribeStorageVirtualMachinesPaginator,
        DescribeVolumesPaginator,
        FSxClient,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: FSxClient = session.client("fsx")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    describe_s3_access_point_attachments_paginator: DescribeS3AccessPointAttachmentsPaginator = client.get_paginator("describe_s3_access_point_attachments")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_storage_virtual_machines_paginator: DescribeStorageVirtualMachinesPaginator = client.get_paginator("describe_storage_virtual_machines")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from .client import FSxClient
from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    DescribeS3AccessPointAttachmentsPaginator,
    DescribeSnapshotsPaginator,
    DescribeStorageVirtualMachinesPaginator,
    DescribeVolumesPaginator,
    ListTagsForResourcePaginator,
)

Client = FSxClient

__all__ = (
    "Client",
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "DescribeS3AccessPointAttachmentsPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeStorageVirtualMachinesPaginator",
    "DescribeVolumesPaginator",
    "FSxClient",
    "ListTagsForResourcePaginator",
)
