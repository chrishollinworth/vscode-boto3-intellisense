"""
Main interface for license-manager-linux-subscriptions service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_license_manager_linux_subscriptions import (
        Client,
        LicenseManagerLinuxSubscriptionsClient,
        ListLinuxSubscriptionInstancesPaginator,
        ListLinuxSubscriptionsPaginator,
        ListRegisteredSubscriptionProvidersPaginator,
    )

    session = Session()
    client: LicenseManagerLinuxSubscriptionsClient = session.client("license-manager-linux-subscriptions")

    list_linux_subscription_instances_paginator: ListLinuxSubscriptionInstancesPaginator = client.get_paginator("list_linux_subscription_instances")
    list_linux_subscriptions_paginator: ListLinuxSubscriptionsPaginator = client.get_paginator("list_linux_subscriptions")
    list_registered_subscription_providers_paginator: ListRegisteredSubscriptionProvidersPaginator = client.get_paginator("list_registered_subscription_providers")
    ```
"""

from .client import LicenseManagerLinuxSubscriptionsClient
from .paginator import (
    ListLinuxSubscriptionInstancesPaginator,
    ListLinuxSubscriptionsPaginator,
    ListRegisteredSubscriptionProvidersPaginator,
)

Client = LicenseManagerLinuxSubscriptionsClient

__all__ = (
    "Client",
    "LicenseManagerLinuxSubscriptionsClient",
    "ListLinuxSubscriptionInstancesPaginator",
    "ListLinuxSubscriptionsPaginator",
    "ListRegisteredSubscriptionProvidersPaginator",
)
