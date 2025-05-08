"""
Main interface for license-manager service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_license_manager import (
        Client,
        LicenseManagerClient,
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

from .client import LicenseManagerClient
from .paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)

Client = LicenseManagerClient

__all__ = (
    "Client",
    "LicenseManagerClient",
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)
