"""
Main interface for mediapackage-vod service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackage_vod import (
        Client,
        ListAssetsPaginator,
        ListPackagingConfigurationsPaginator,
        ListPackagingGroupsPaginator,
        MediaPackageVodClient,
    )

    session = boto3.Session()

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")
    session_client: MediaPackageVodClient = session.client("mediapackage-vod")

    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_packaging_configurations_paginator: ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
    list_packaging_groups_paginator: ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
    ```
"""
from mypy_boto3_mediapackage_vod.client import MediaPackageVodClient
from mypy_boto3_mediapackage_vod.paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)

Client = MediaPackageVodClient


__all__ = (
    "Client",
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
    "MediaPackageVodClient",
)
