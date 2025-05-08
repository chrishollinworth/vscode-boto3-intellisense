"""
Type annotations for license-manager-linux-subscriptions service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_license_manager_linux_subscriptions.client import LicenseManagerLinuxSubscriptionsClient
    from mypy_boto3_license_manager_linux_subscriptions.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListLinuxSubscriptionInstancesRequestPaginateTypeDef,
    ListLinuxSubscriptionInstancesResponseTypeDef,
    ListLinuxSubscriptionsRequestPaginateTypeDef,
    ListLinuxSubscriptionsResponseTypeDef,
    ListRegisteredSubscriptionProvidersRequestPaginateTypeDef,
    ListRegisteredSubscriptionProvidersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListLinuxSubscriptionInstancesPaginator",
    "ListLinuxSubscriptionsPaginator",
    "ListRegisteredSubscriptionProvidersPaginator",
)

if TYPE_CHECKING:
    _ListLinuxSubscriptionInstancesPaginatorBase = Paginator[
        ListLinuxSubscriptionInstancesResponseTypeDef
    ]
else:
    _ListLinuxSubscriptionInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListLinuxSubscriptionInstancesPaginator(_ListLinuxSubscriptionInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListLinuxSubscriptionInstances.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptionInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listlinuxsubscriptioninstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLinuxSubscriptionInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListLinuxSubscriptionInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListLinuxSubscriptionInstances.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptionInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listlinuxsubscriptioninstancespaginator)
        """

if TYPE_CHECKING:
    _ListLinuxSubscriptionsPaginatorBase = Paginator[ListLinuxSubscriptionsResponseTypeDef]
else:
    _ListLinuxSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLinuxSubscriptionsPaginator(_ListLinuxSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListLinuxSubscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listlinuxsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLinuxSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLinuxSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListLinuxSubscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listlinuxsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListRegisteredSubscriptionProvidersPaginatorBase = Paginator[
        ListRegisteredSubscriptionProvidersResponseTypeDef
    ]
else:
    _ListRegisteredSubscriptionProvidersPaginatorBase = Paginator  # type: ignore[assignment]

class ListRegisteredSubscriptionProvidersPaginator(
    _ListRegisteredSubscriptionProvidersPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListRegisteredSubscriptionProviders.html#LicenseManagerLinuxSubscriptions.Paginator.ListRegisteredSubscriptionProviders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listregisteredsubscriptionproviderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRegisteredSubscriptionProvidersRequestPaginateTypeDef]
    ) -> PageIterator[ListRegisteredSubscriptionProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions/paginator/ListRegisteredSubscriptionProviders.html#LicenseManagerLinuxSubscriptions.Paginator.ListRegisteredSubscriptionProviders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators/#listregisteredsubscriptionproviderspaginator)
        """
