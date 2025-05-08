"""
Main interface for mediapackage-vod service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackage_vod import (
        Client,
        ListAssetsPaginator,
        ListPackagingConfigurationsPaginator,
        ListPackagingGroupsPaginator,
        MediaPackageVodClient,
    )

    session = Session()
    client: MediaPackageVodClient = session.client("mediapackage-vod")

    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_packaging_configurations_paginator: ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
    list_packaging_groups_paginator: ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
    ```
"""

from .client import MediaPackageVodClient
from .paginator import (
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
