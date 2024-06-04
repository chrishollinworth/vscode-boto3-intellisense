"""
Main interface for appfabric service.

Usage::

    ```python
    import boto3
    from mypy_boto3_appfabric import (
        AppFabricClient,
        Client,
        ListAppAuthorizationsPaginator,
        ListAppBundlesPaginator,
        ListIngestionDestinationsPaginator,
        ListIngestionsPaginator,
    )

    session = boto3.Session()

    client: AppFabricClient = boto3.client("appfabric")
    session_client: AppFabricClient = session.client("appfabric")

    list_app_authorizations_paginator: ListAppAuthorizationsPaginator = client.get_paginator("list_app_authorizations")
    list_app_bundles_paginator: ListAppBundlesPaginator = client.get_paginator("list_app_bundles")
    list_ingestion_destinations_paginator: ListIngestionDestinationsPaginator = client.get_paginator("list_ingestion_destinations")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    ```
"""

from .client import AppFabricClient
from .paginator import (
    ListAppAuthorizationsPaginator,
    ListAppBundlesPaginator,
    ListIngestionDestinationsPaginator,
    ListIngestionsPaginator,
)

Client = AppFabricClient

__all__ = (
    "AppFabricClient",
    "Client",
    "ListAppAuthorizationsPaginator",
    "ListAppBundlesPaginator",
    "ListIngestionDestinationsPaginator",
    "ListIngestionsPaginator",
)
