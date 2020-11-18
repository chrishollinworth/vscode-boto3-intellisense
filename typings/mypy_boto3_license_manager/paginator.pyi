# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for license-manager service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_license_manager import LicenseManagerClient
    from mypy_boto3_license_manager.paginator import (
        ListAssociationsForLicenseConfigurationPaginator,
        ListLicenseConfigurationsPaginator,
        ListLicenseSpecificationsForResourcePaginator,
        ListResourceInventoryPaginator,
        ListUsageForLicenseConfigurationPaginator,
    )

    client: LicenseManagerClient = boto3.client("license-manager")

    list_associations_for_license_configuration_paginator: ListAssociationsForLicenseConfigurationPaginator = client.get_paginator("list_associations_for_license_configuration")
    list_license_configurations_paginator: ListLicenseConfigurationsPaginator = client.get_paginator("list_license_configurations")
    list_license_specifications_for_resource_paginator: ListLicenseSpecificationsForResourcePaginator = client.get_paginator("list_license_specifications_for_resource")
    list_resource_inventory_paginator: ListResourceInventoryPaginator = client.get_paginator("list_resource_inventory")
    list_usage_for_license_configuration_paginator: ListUsageForLicenseConfigurationPaginator = client.get_paginator("list_usage_for_license_configuration")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_license_manager.type_defs import (
    FilterTypeDef,
    InventoryFilterTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)


class ListAssociationsForLicenseConfigurationPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
    """

    def paginate(
        self, LicenseConfigurationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationsForLicenseConfigurationResponseTypeDef]:
        """
        [ListAssociationsForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration.paginate)
        """


class ListLicenseConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
    """

    def paginate(
        self,
        LicenseConfigurationArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLicenseConfigurationsResponseTypeDef]:
        """
        [ListLicenseConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations.paginate)
        """


class ListLicenseSpecificationsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLicenseSpecificationsForResourceResponseTypeDef]:
        """
        [ListLicenseSpecificationsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource.paginate)
        """


class ListResourceInventoryPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
    """

    def paginate(
        self,
        Filters: List[InventoryFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListResourceInventoryResponseTypeDef]:
        """
        [ListResourceInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory.paginate)
        """


class ListUsageForLicenseConfigurationPaginator(Boto3Paginator):
    """
    [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
    """

    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUsageForLicenseConfigurationResponseTypeDef]:
        """
        [ListUsageForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration.paginate)
        """
