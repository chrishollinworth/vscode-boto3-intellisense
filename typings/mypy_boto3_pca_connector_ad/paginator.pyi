"""
Type annotations for pca-connector-ad service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_pca_connector_ad.client import PcaConnectorAdClient
    from mypy_boto3_pca_connector_ad.paginator import (
        ListConnectorsPaginator,
        ListDirectoryRegistrationsPaginator,
        ListServicePrincipalNamesPaginator,
        ListTemplateGroupAccessControlEntriesPaginator,
        ListTemplatesPaginator,
    )

    session = Session()
    client: PcaConnectorAdClient = session.client("pca-connector-ad")

    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_directory_registrations_paginator: ListDirectoryRegistrationsPaginator = client.get_paginator("list_directory_registrations")
    list_service_principal_names_paginator: ListServicePrincipalNamesPaginator = client.get_paginator("list_service_principal_names")
    list_template_group_access_control_entries_paginator: ListTemplateGroupAccessControlEntriesPaginator = client.get_paginator("list_template_group_access_control_entries")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConnectorsRequestPaginateTypeDef,
    ListConnectorsResponseTypeDef,
    ListDirectoryRegistrationsRequestPaginateTypeDef,
    ListDirectoryRegistrationsResponseTypeDef,
    ListServicePrincipalNamesRequestPaginateTypeDef,
    ListServicePrincipalNamesResponseTypeDef,
    ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef,
    ListTemplateGroupAccessControlEntriesResponseTypeDef,
    ListTemplatesRequestPaginateTypeDef,
    ListTemplatesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListConnectorsPaginator",
    "ListDirectoryRegistrationsPaginator",
    "ListServicePrincipalNamesPaginator",
    "ListTemplateGroupAccessControlEntriesPaginator",
    "ListTemplatesPaginator",
)

if TYPE_CHECKING:
    _ListConnectorsPaginatorBase = Paginator[ListConnectorsResponseTypeDef]
else:
    _ListConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorsPaginator(_ListConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListConnectors.html#PcaConnectorAd.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListConnectors.html#PcaConnectorAd.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listconnectorspaginator)
        """

if TYPE_CHECKING:
    _ListDirectoryRegistrationsPaginatorBase = Paginator[ListDirectoryRegistrationsResponseTypeDef]
else:
    _ListDirectoryRegistrationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDirectoryRegistrationsPaginator(_ListDirectoryRegistrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListDirectoryRegistrations.html#PcaConnectorAd.Paginator.ListDirectoryRegistrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listdirectoryregistrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDirectoryRegistrationsRequestPaginateTypeDef]
    ) -> PageIterator[ListDirectoryRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListDirectoryRegistrations.html#PcaConnectorAd.Paginator.ListDirectoryRegistrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listdirectoryregistrationspaginator)
        """

if TYPE_CHECKING:
    _ListServicePrincipalNamesPaginatorBase = Paginator[ListServicePrincipalNamesResponseTypeDef]
else:
    _ListServicePrincipalNamesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicePrincipalNamesPaginator(_ListServicePrincipalNamesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListServicePrincipalNames.html#PcaConnectorAd.Paginator.ListServicePrincipalNames)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listserviceprincipalnamespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicePrincipalNamesRequestPaginateTypeDef]
    ) -> PageIterator[ListServicePrincipalNamesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListServicePrincipalNames.html#PcaConnectorAd.Paginator.ListServicePrincipalNames.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listserviceprincipalnamespaginator)
        """

if TYPE_CHECKING:
    _ListTemplateGroupAccessControlEntriesPaginatorBase = Paginator[
        ListTemplateGroupAccessControlEntriesResponseTypeDef
    ]
else:
    _ListTemplateGroupAccessControlEntriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplateGroupAccessControlEntriesPaginator(
    _ListTemplateGroupAccessControlEntriesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListTemplateGroupAccessControlEntries.html#PcaConnectorAd.Paginator.ListTemplateGroupAccessControlEntries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listtemplategroupaccesscontrolentriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef]
    ) -> PageIterator[ListTemplateGroupAccessControlEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListTemplateGroupAccessControlEntries.html#PcaConnectorAd.Paginator.ListTemplateGroupAccessControlEntries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listtemplategroupaccesscontrolentriespaginator)
        """

if TYPE_CHECKING:
    _ListTemplatesPaginatorBase = Paginator[ListTemplatesResponseTypeDef]
else:
    _ListTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTemplatesPaginator(_ListTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListTemplates.html#PcaConnectorAd.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad/paginator/ListTemplates.html#PcaConnectorAd.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators/#listtemplatespaginator)
        """
