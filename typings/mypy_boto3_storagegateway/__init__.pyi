"""
Main interface for storagegateway service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_storagegateway import (
        Client,
        DescribeTapeArchivesPaginator,
        DescribeTapeRecoveryPointsPaginator,
        DescribeTapesPaginator,
        DescribeVTLDevicesPaginator,
        ListCacheReportsPaginator,
        ListFileSharesPaginator,
        ListFileSystemAssociationsPaginator,
        ListGatewaysPaginator,
        ListTagsForResourcePaginator,
        ListTapePoolsPaginator,
        ListTapesPaginator,
        ListVolumesPaginator,
        StorageGatewayClient,
    )

    session = Session()
    client: StorageGatewayClient = session.client("storagegateway")

    describe_tape_archives_paginator: DescribeTapeArchivesPaginator = client.get_paginator("describe_tape_archives")
    describe_tape_recovery_points_paginator: DescribeTapeRecoveryPointsPaginator = client.get_paginator("describe_tape_recovery_points")
    describe_tapes_paginator: DescribeTapesPaginator = client.get_paginator("describe_tapes")
    describe_vtl_devices_paginator: DescribeVTLDevicesPaginator = client.get_paginator("describe_vtl_devices")
    list_cache_reports_paginator: ListCacheReportsPaginator = client.get_paginator("list_cache_reports")
    list_file_shares_paginator: ListFileSharesPaginator = client.get_paginator("list_file_shares")
    list_file_system_associations_paginator: ListFileSystemAssociationsPaginator = client.get_paginator("list_file_system_associations")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_tape_pools_paginator: ListTapePoolsPaginator = client.get_paginator("list_tape_pools")
    list_tapes_paginator: ListTapesPaginator = client.get_paginator("list_tapes")
    list_volumes_paginator: ListVolumesPaginator = client.get_paginator("list_volumes")
    ```
"""

from .client import StorageGatewayClient
from .paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListCacheReportsPaginator,
    ListFileSharesPaginator,
    ListFileSystemAssociationsPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapePoolsPaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)

Client = StorageGatewayClient

__all__ = (
    "Client",
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListCacheReportsPaginator",
    "ListFileSharesPaginator",
    "ListFileSystemAssociationsPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapePoolsPaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
    "StorageGatewayClient",
)
