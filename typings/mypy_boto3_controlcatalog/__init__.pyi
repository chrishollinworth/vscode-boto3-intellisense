"""
Main interface for controlcatalog service.

Usage::

    ```python
    import boto3
    from mypy_boto3_controlcatalog import (
        Client,
        ControlCatalogClient,
        ListCommonControlsPaginator,
        ListDomainsPaginator,
        ListObjectivesPaginator,
    )

    session = boto3.Session()

    client: ControlCatalogClient = boto3.client("controlcatalog")
    session_client: ControlCatalogClient = session.client("controlcatalog")

    list_common_controls_paginator: ListCommonControlsPaginator = client.get_paginator("list_common_controls")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_objectives_paginator: ListObjectivesPaginator = client.get_paginator("list_objectives")
    ```
"""

from .client import ControlCatalogClient
from .paginator import ListCommonControlsPaginator, ListDomainsPaginator, ListObjectivesPaginator

Client = ControlCatalogClient

__all__ = (
    "Client",
    "ControlCatalogClient",
    "ListCommonControlsPaginator",
    "ListDomainsPaginator",
    "ListObjectivesPaginator",
)
