"""
Main interface for route53profiles service.

Usage::

    ```python
    import boto3
    from mypy_boto3_route53profiles import (
        Client,
        ListProfileAssociationsPaginator,
        ListProfileResourceAssociationsPaginator,
        ListProfilesPaginator,
        Route53ProfilesClient,
    )

    session = boto3.Session()

    client: Route53ProfilesClient = boto3.client("route53profiles")
    session_client: Route53ProfilesClient = session.client("route53profiles")

    list_profile_associations_paginator: ListProfileAssociationsPaginator = client.get_paginator("list_profile_associations")
    list_profile_resource_associations_paginator: ListProfileResourceAssociationsPaginator = client.get_paginator("list_profile_resource_associations")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    ```
"""

from .client import Route53ProfilesClient
from .paginator import (
    ListProfileAssociationsPaginator,
    ListProfileResourceAssociationsPaginator,
    ListProfilesPaginator,
)

Client = Route53ProfilesClient

__all__ = (
    "Client",
    "ListProfileAssociationsPaginator",
    "ListProfileResourceAssociationsPaginator",
    "ListProfilesPaginator",
    "Route53ProfilesClient",
)
