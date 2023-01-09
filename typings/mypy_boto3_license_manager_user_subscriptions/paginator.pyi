"""
Type annotations for license-manager-user-subscriptions service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_license_manager_user_subscriptions import LicenseManagerUserSubscriptionsClient
    from mypy_boto3_license_manager_user_subscriptions.paginator import (
        ListIdentityProvidersPaginator,
        ListInstancesPaginator,
        ListProductSubscriptionsPaginator,
        ListUserAssociationsPaginator,
    )

    client: LicenseManagerUserSubscriptionsClient = boto3.client("license-manager-user-subscriptions")

    list_identity_providers_paginator: ListIdentityProvidersPaginator = client.get_paginator("list_identity_providers")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_product_subscriptions_paginator: ListProductSubscriptionsPaginator = client.get_paginator("list_product_subscriptions")
    list_user_associations_paginator: ListUserAssociationsPaginator = client.get_paginator("list_user_associations")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterTypeDef,
    IdentityProviderTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListProductSubscriptionsResponseTypeDef,
    ListUserAssociationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListIdentityProvidersPaginator",
    "ListInstancesPaginator",
    "ListProductSubscriptionsPaginator",
    "ListUserAssociationsPaginator",
)

class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListIdentityProviders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listidentityproviderspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListIdentityProviders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listidentityproviderspaginator)
        """

class ListInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listinstancespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listinstancespaginator)
        """

class ListProductSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListProductSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listproductsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        Product: str,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProductSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListProductSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listproductsubscriptionspaginator)
        """

class ListUserAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListUserAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listuserassociationspaginator)
    """

    def paginate(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        InstanceId: str,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListUserAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listuserassociationspaginator)
        """
