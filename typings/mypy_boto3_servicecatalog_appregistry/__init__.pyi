"""
Main interface for servicecatalog-appregistry service.

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog_appregistry import (
        Client,
        ListApplicationsPaginator,
        ListAssociatedAttributeGroupsPaginator,
        ListAssociatedResourcesPaginator,
        ListAttributeGroupsPaginator,
        ServiceCatalogAppRegistryClient,
    )

    session = boto3.Session()

    client: ServiceCatalogAppRegistryClient = boto3.client("servicecatalog-appregistry")
    session_client: ServiceCatalogAppRegistryClient = session.client("servicecatalog-appregistry")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_associated_attribute_groups_paginator: ListAssociatedAttributeGroupsPaginator = client.get_paginator("list_associated_attribute_groups")
    list_associated_resources_paginator: ListAssociatedResourcesPaginator = client.get_paginator("list_associated_resources")
    list_attribute_groups_paginator: ListAttributeGroupsPaginator = client.get_paginator("list_attribute_groups")
    ```
"""
from mypy_boto3_servicecatalog_appregistry.client import ServiceCatalogAppRegistryClient
from mypy_boto3_servicecatalog_appregistry.paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsPaginator,
)

Client = ServiceCatalogAppRegistryClient


__all__ = (
    "Client",
    "ListApplicationsPaginator",
    "ListAssociatedAttributeGroupsPaginator",
    "ListAssociatedResourcesPaginator",
    "ListAttributeGroupsPaginator",
    "ServiceCatalogAppRegistryClient",
)
