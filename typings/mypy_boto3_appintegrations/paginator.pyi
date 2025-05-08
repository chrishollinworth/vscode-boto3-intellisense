"""
Type annotations for appintegrations service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appintegrations.client import AppIntegrationsServiceClient
    from mypy_boto3_appintegrations.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationAssociationsRequestPaginateTypeDef,
    ListApplicationAssociationsResponseTypeDef,
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListDataIntegrationAssociationsRequestPaginateTypeDef,
    ListDataIntegrationAssociationsResponseTypeDef,
    ListDataIntegrationsRequestPaginateTypeDef,
    ListDataIntegrationsResponseTypeDef,
    ListEventIntegrationAssociationsRequestPaginateTypeDef,
    ListEventIntegrationAssociationsResponseTypeDef,
    ListEventIntegrationsRequestPaginateTypeDef,
    ListEventIntegrationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationAssociationsPaginator",
    "ListApplicationsPaginator",
    "ListDataIntegrationAssociationsPaginator",
    "ListDataIntegrationsPaginator",
    "ListEventIntegrationAssociationsPaginator",
    "ListEventIntegrationsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationAssociationsPaginatorBase = Paginator[
        ListApplicationAssociationsResponseTypeDef
    ]
else:
    _ListApplicationAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationAssociationsPaginator(_ListApplicationAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListApplicationAssociations.html#AppIntegrationsService.Paginator.ListApplicationAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listapplicationassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListApplicationAssociations.html#AppIntegrationsService.Paginator.ListApplicationAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listapplicationassociationspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListApplications.html#AppIntegrationsService.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListApplications.html#AppIntegrationsService.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListDataIntegrationAssociationsPaginatorBase = Paginator[
        ListDataIntegrationAssociationsResponseTypeDef
    ]
else:
    _ListDataIntegrationAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataIntegrationAssociationsPaginator(_ListDataIntegrationAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListDataIntegrationAssociations.html#AppIntegrationsService.Paginator.ListDataIntegrationAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listdataintegrationassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataIntegrationAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListDataIntegrationAssociations.html#AppIntegrationsService.Paginator.ListDataIntegrationAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listdataintegrationassociationspaginator)
        """

if TYPE_CHECKING:
    _ListDataIntegrationsPaginatorBase = Paginator[ListDataIntegrationsResponseTypeDef]
else:
    _ListDataIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataIntegrationsPaginator(_ListDataIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListDataIntegrations.html#AppIntegrationsService.Paginator.ListDataIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listdataintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataIntegrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListDataIntegrations.html#AppIntegrationsService.Paginator.ListDataIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listdataintegrationspaginator)
        """

if TYPE_CHECKING:
    _ListEventIntegrationAssociationsPaginatorBase = Paginator[
        ListEventIntegrationAssociationsResponseTypeDef
    ]
else:
    _ListEventIntegrationAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventIntegrationAssociationsPaginator(_ListEventIntegrationAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListEventIntegrationAssociations.html#AppIntegrationsService.Paginator.ListEventIntegrationAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listeventintegrationassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventIntegrationAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListEventIntegrationAssociations.html#AppIntegrationsService.Paginator.ListEventIntegrationAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listeventintegrationassociationspaginator)
        """

if TYPE_CHECKING:
    _ListEventIntegrationsPaginatorBase = Paginator[ListEventIntegrationsResponseTypeDef]
else:
    _ListEventIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventIntegrationsPaginator(_ListEventIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListEventIntegrations.html#AppIntegrationsService.Paginator.ListEventIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listeventintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventIntegrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations/paginator/ListEventIntegrations.html#AppIntegrationsService.Paginator.ListEventIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/paginators/#listeventintegrationspaginator)
        """
