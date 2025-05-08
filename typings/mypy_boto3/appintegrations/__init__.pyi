"""
Main interface for appintegrations service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appintegrations import (
        AppIntegrationsServiceClient,
        Client,
        ListApplicationAssociationsPaginator,
        ListApplicationsPaginator,
        ListDataIntegrationAssociationsPaginator,
        ListDataIntegrationsPaginator,
        ListEventIntegrationAssociationsPaginator,
        ListEventIntegrationsPaginator,
    )

    session = Session()
    client: AppIntegrationsServiceClient = session.client("appintegrations")

    list_application_associations_paginator: ListApplicationAssociationsPaginator = client.get_paginator("list_application_associations")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_data_integration_associations_paginator: ListDataIntegrationAssociationsPaginator = client.get_paginator("list_data_integration_associations")
    list_data_integrations_paginator: ListDataIntegrationsPaginator = client.get_paginator("list_data_integrations")
    list_event_integration_associations_paginator: ListEventIntegrationAssociationsPaginator = client.get_paginator("list_event_integration_associations")
    list_event_integrations_paginator: ListEventIntegrationsPaginator = client.get_paginator("list_event_integrations")
    ```
"""

from .client import AppIntegrationsServiceClient
from .paginator import (
    ListApplicationAssociationsPaginator,
    ListApplicationsPaginator,
    ListDataIntegrationAssociationsPaginator,
    ListDataIntegrationsPaginator,
    ListEventIntegrationAssociationsPaginator,
    ListEventIntegrationsPaginator,
)

Client = AppIntegrationsServiceClient

__all__ = (
    "AppIntegrationsServiceClient",
    "Client",
    "ListApplicationAssociationsPaginator",
    "ListApplicationsPaginator",
    "ListDataIntegrationAssociationsPaginator",
    "ListDataIntegrationsPaginator",
    "ListEventIntegrationAssociationsPaginator",
    "ListEventIntegrationsPaginator",
)
