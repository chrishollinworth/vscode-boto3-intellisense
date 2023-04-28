"""
Type annotations for license-manager-linux-subscriptions service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_license_manager_linux_subscriptions import LicenseManagerLinuxSubscriptionsClient
    from mypy_boto3_license_manager_linux_subscriptions.paginator import (
        ListLinuxSubscriptionInstancesPaginator,
        ListLinuxSubscriptionsPaginator,
    )

    client: LicenseManagerLinuxSubscriptionsClient = boto3.client("license-manager-linux-subscriptions")

    list_linux_subscription_instances_paginator: ListLinuxSubscriptionInstancesPaginator = client.get_paginator("list_linux_subscription_instances")
    list_linux_subscriptions_paginator: ListLinuxSubscriptionsPaginator = client.get_paginator("list_linux_subscriptions")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterTypeDef,
    ListLinuxSubscriptionInstancesResponseTypeDef,
    ListLinuxSubscriptionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListLinuxSubscriptionInstancesPaginator", "ListLinuxSubscriptionsPaginator")

class ListLinuxSubscriptionInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptionInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptioninstancespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLinuxSubscriptionInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptionInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptioninstancespaginator)
        """

class ListLinuxSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLinuxSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptionspaginator)
        """
