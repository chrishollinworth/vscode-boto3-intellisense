"""
Type annotations for license-manager service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_license_manager.client import LicenseManagerClient
    from mypy_boto3_license_manager.paginator import (
        ListAssociationsForLicenseConfigurationPaginator,
        ListLicenseConfigurationsPaginator,
        ListLicenseSpecificationsForResourcePaginator,
        ListResourceInventoryPaginator,
        ListUsageForLicenseConfigurationPaginator,
    )

    session = Session()
    client: LicenseManagerClient = session.client("license-manager")

    list_associations_for_license_configuration_paginator: ListAssociationsForLicenseConfigurationPaginator = client.get_paginator("list_associations_for_license_configuration")
    list_license_configurations_paginator: ListLicenseConfigurationsPaginator = client.get_paginator("list_license_configurations")
    list_license_specifications_for_resource_paginator: ListLicenseSpecificationsForResourcePaginator = client.get_paginator("list_license_specifications_for_resource")
    list_resource_inventory_paginator: ListResourceInventoryPaginator = client.get_paginator("list_resource_inventory")
    list_usage_for_license_configuration_paginator: ListUsageForLicenseConfigurationPaginator = client.get_paginator("list_usage_for_license_configuration")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssociationsForLicenseConfigurationRequestPaginateTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListLicenseConfigurationsRequestPaginateTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceRequestPaginateTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListResourceInventoryRequestPaginateTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListUsageForLicenseConfigurationRequestPaginateTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)

if TYPE_CHECKING:
    _ListAssociationsForLicenseConfigurationPaginatorBase = Paginator[
        ListAssociationsForLicenseConfigurationResponseTypeDef
    ]
else:
    _ListAssociationsForLicenseConfigurationPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociationsForLicenseConfigurationPaginator(
    _ListAssociationsForLicenseConfigurationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListAssociationsForLicenseConfiguration.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listassociationsforlicenseconfigurationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociationsForLicenseConfigurationRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociationsForLicenseConfigurationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListAssociationsForLicenseConfiguration.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listassociationsforlicenseconfigurationpaginator)
        """

if TYPE_CHECKING:
    _ListLicenseConfigurationsPaginatorBase = Paginator[ListLicenseConfigurationsResponseTypeDef]
else:
    _ListLicenseConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLicenseConfigurationsPaginator(_ListLicenseConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListLicenseConfigurations.html#LicenseManager.Paginator.ListLicenseConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listlicenseconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLicenseConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListLicenseConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListLicenseConfigurations.html#LicenseManager.Paginator.ListLicenseConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listlicenseconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListLicenseSpecificationsForResourcePaginatorBase = Paginator[
        ListLicenseSpecificationsForResourceResponseTypeDef
    ]
else:
    _ListLicenseSpecificationsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListLicenseSpecificationsForResourcePaginator(
    _ListLicenseSpecificationsForResourcePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListLicenseSpecificationsForResource.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listlicensespecificationsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLicenseSpecificationsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListLicenseSpecificationsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListLicenseSpecificationsForResource.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listlicensespecificationsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListResourceInventoryPaginatorBase = Paginator[ListResourceInventoryResponseTypeDef]
else:
    _ListResourceInventoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceInventoryPaginator(_ListResourceInventoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListResourceInventory.html#LicenseManager.Paginator.ListResourceInventory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listresourceinventorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceInventoryRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceInventoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListResourceInventory.html#LicenseManager.Paginator.ListResourceInventory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listresourceinventorypaginator)
        """

if TYPE_CHECKING:
    _ListUsageForLicenseConfigurationPaginatorBase = Paginator[
        ListUsageForLicenseConfigurationResponseTypeDef
    ]
else:
    _ListUsageForLicenseConfigurationPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsageForLicenseConfigurationPaginator(_ListUsageForLicenseConfigurationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListUsageForLicenseConfiguration.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listusageforlicenseconfigurationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsageForLicenseConfigurationRequestPaginateTypeDef]
    ) -> PageIterator[ListUsageForLicenseConfigurationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/paginator/ListUsageForLicenseConfiguration.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators/#listusageforlicenseconfigurationpaginator)
        """
