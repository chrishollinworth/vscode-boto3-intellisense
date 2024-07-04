"""
Type annotations for appintegrations service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_appintegrations import AppIntegrationsServiceClient
    from mypy_boto3_appintegrations.paginator import (
        ListApplicationAssociationsPaginator,
        ListApplicationsPaginator,
        ListDataIntegrationAssociationsPaginator,
        ListDataIntegrationsPaginator,
        ListEventIntegrationAssociationsPaginator,
        ListEventIntegrationsPaginator,
    )

    client: AppIntegrationsServiceClient = boto3.client("appintegrations")

    list_application_associations_paginator: ListApplicationAssociationsPaginator = client.get_paginator("list_application_associations")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_data_integration_associations_paginator: ListDataIntegrationAssociationsPaginator = client.get_paginator("list_data_integration_associations")
    list_data_integrations_paginator: ListDataIntegrationsPaginator = client.get_paginator("list_data_integrations")
    list_event_integration_associations_paginator: ListEventIntegrationAssociationsPaginator = client.get_paginator("list_event_integration_associations")
    list_event_integrations_paginator: ListEventIntegrationsPaginator = client.get_paginator("list_event_integrations")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationAssociationsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListDataIntegrationAssociationsResponseTypeDef,
    ListDataIntegrationsResponseTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationAssociationsPaginator",
    "ListApplicationsPaginator",
    "ListDataIntegrationAssociationsPaginator",
    "ListDataIntegrationsPaginator",
    "ListEventIntegrationAssociationsPaginator",
    "ListEventIntegrationsPaginator",
)

class ListApplicationAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListApplicationAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listapplicationassociationspaginator)
    """

    def paginate(
        self, *, ApplicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListApplicationAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listapplicationassociationspaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listapplicationspaginator)
        """

class ListDataIntegrationAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListDataIntegrationAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listdataintegrationassociationspaginator)
    """

    def paginate(
        self, *, DataIntegrationIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListDataIntegrationAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listdataintegrationassociationspaginator)
        """

class ListDataIntegrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListDataIntegrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listdataintegrationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListDataIntegrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listdataintegrationspaginator)
        """

class ListEventIntegrationAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListEventIntegrationAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listeventintegrationassociationspaginator)
    """

    def paginate(
        self, *, EventIntegrationName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListEventIntegrationAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listeventintegrationassociationspaginator)
        """

class ListEventIntegrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListEventIntegrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listeventintegrationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/appintegrations.html#AppIntegrationsService.Paginator.ListEventIntegrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators.html#listeventintegrationspaginator)
        """
