"""
Type annotations for pca-connector-ad service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_pca_connector_ad import PcaConnectorAdClient
    from mypy_boto3_pca_connector_ad.paginator import (
        ListConnectorsPaginator,
        ListDirectoryRegistrationsPaginator,
        ListServicePrincipalNamesPaginator,
        ListTemplateGroupAccessControlEntriesPaginator,
        ListTemplatesPaginator,
    )

    client: PcaConnectorAdClient = boto3.client("pca-connector-ad")

    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_directory_registrations_paginator: ListDirectoryRegistrationsPaginator = client.get_paginator("list_directory_registrations")
    list_service_principal_names_paginator: ListServicePrincipalNamesPaginator = client.get_paginator("list_service_principal_names")
    list_template_group_access_control_entries_paginator: ListTemplateGroupAccessControlEntriesPaginator = client.get_paginator("list_template_group_access_control_entries")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListConnectorsResponseTypeDef,
    ListDirectoryRegistrationsResponseTypeDef,
    ListServicePrincipalNamesResponseTypeDef,
    ListTemplateGroupAccessControlEntriesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListConnectorsPaginator",
    "ListDirectoryRegistrationsPaginator",
    "ListServicePrincipalNamesPaginator",
    "ListTemplateGroupAccessControlEntriesPaginator",
    "ListTemplatesPaginator",
)

class ListConnectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listconnectorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listconnectorspaginator)
        """

class ListDirectoryRegistrationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListDirectoryRegistrations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listdirectoryregistrationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDirectoryRegistrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListDirectoryRegistrations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listdirectoryregistrationspaginator)
        """

class ListServicePrincipalNamesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListServicePrincipalNames)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listserviceprincipalnamespaginator)
    """

    def paginate(
        self, *, DirectoryRegistrationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicePrincipalNamesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListServicePrincipalNames.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listserviceprincipalnamespaginator)
        """

class ListTemplateGroupAccessControlEntriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplateGroupAccessControlEntries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplategroupaccesscontrolentriespaginator)
    """

    def paginate(
        self, *, TemplateArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateGroupAccessControlEntriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplateGroupAccessControlEntries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplategroupaccesscontrolentriespaginator)
        """

class ListTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplatespaginator)
    """

    def paginate(
        self, *, ConnectorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/pca-connector-ad.html#PcaConnectorAd.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_ad/paginators.html#listtemplatespaginator)
        """
