"""
Main interface for license-manager-user-subscriptions service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_license_manager_user_subscriptions import (
        Client,
        LicenseManagerUserSubscriptionsClient,
        ListIdentityProvidersPaginator,
        ListInstancesPaginator,
        ListLicenseServerEndpointsPaginator,
        ListProductSubscriptionsPaginator,
        ListUserAssociationsPaginator,
    )

    session = Session()
    client: LicenseManagerUserSubscriptionsClient = session.client("license-manager-user-subscriptions")

    list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_license_server_endpoints_paginator: ListLicenseServerEndpointsPaginator = client.get_paginator("list_license_server_endpoints")
    list_product_subscriptions_paginator: ListProductSubscriptionsPaginator = client.get_paginator("list_product_subscriptions")
    list_user_associations_paginator: ListUserAssociationsPaginator = client.get_paginator("list_user_associations")
    ```
"""

from .client import LicenseManagerUserSubscriptionsClient
from .paginator import (
    ListIdentityProvidersPaginator,
    ListInstancesPaginator,
    ListLicenseServerEndpointsPaginator,
    ListProductSubscriptionsPaginator,
    ListUserAssociationsPaginator,
)

Client = LicenseManagerUserSubscriptionsClient

__all__ = (
    "Client",
    "LicenseManagerUserSubscriptionsClient",
    "ListIdentityProvidersPaginator",
    "ListInstancesPaginator",
    "ListLicenseServerEndpointsPaginator",
    "ListProductSubscriptionsPaginator",
    "ListUserAssociationsPaginator",
)
