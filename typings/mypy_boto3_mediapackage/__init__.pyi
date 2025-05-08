"""
Main interface for mediapackage service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackage import (
        Client,
        ListChannelsPaginator,
        ListHarvestJobsPaginator,
        ListOriginEndpointsPaginator,
        MediaPackageClient,
    )

    session = Session()
    client: MediaPackageClient = session.client("mediapackage")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_harvest_jobs_paginator: ListHarvestJobsPaginator = client.get_paginator("list_harvest_jobs")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from .client import MediaPackageClient
from .paginator import ListChannelsPaginator, ListHarvestJobsPaginator, ListOriginEndpointsPaginator

Client = MediaPackageClient

__all__ = (
    "Client",
    "ListChannelsPaginator",
    "ListHarvestJobsPaginator",
    "ListOriginEndpointsPaginator",
    "MediaPackageClient",
)
