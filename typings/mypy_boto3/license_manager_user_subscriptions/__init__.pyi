"""
Main interface for license-manager-user-subscriptions service.

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager_user_subscriptions import (
        Client,
        LicenseManagerUserSubscriptionsClient,
        ListIdentityProvidersPaginator,
        ListInstancesPaginator,
        ListProductSubscriptionsPaginator,
        ListUserAssociationsPaginator,
    )

    session = boto3.Session()

    client: LicenseManagerUserSubscriptionsClient = boto3.client("license-manager-user-subscriptions")
    session_client: LicenseManagerUserSubscriptionsClient = session.client("license-manager-user-subscriptions")

    list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_product_subscriptions_paginator: ListProductSubscriptionsPaginator = client.get_paginator("list_product_subscriptions")
    list_user_associations_paginator: ListUserAssociationsPaginator = client.get_paginator("list_user_associations")
    ```
"""
from .client import LicenseManagerUserSubscriptionsClient
from .paginator import (
    ListIdentityProvidersPaginator,
    ListInstancesPaginator,
    ListProductSubscriptionsPaginator,
    ListUserAssociationsPaginator,
)

Client = LicenseManagerUserSubscriptionsClient

__all__ = (
    "Client",
    "LicenseManagerUserSubscriptionsClient",
    "ListIdentityProvidersPaginator",
    "ListInstancesPaginator",
    "ListProductSubscriptionsPaginator",
    "ListUserAssociationsPaginator",
)
