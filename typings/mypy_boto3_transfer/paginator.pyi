"""
Type annotations for transfer service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_transfer.client import TransferClient
    from mypy_boto3_transfer.paginator import (
        ListAccessesPaginator,
        ListAgreementsPaginator,
        ListCertificatesPaginator,
        ListConnectorsPaginator,
        ListExecutionsPaginator,
        ListFileTransferResultsPaginator,
        ListProfilesPaginator,
        ListSecurityPoliciesPaginator,
        ListServersPaginator,
        ListTagsForResourcePaginator,
        ListUsersPaginator,
        ListWebAppsPaginator,
        ListWorkflowsPaginator,
    )

    session = Session()
    client: TransferClient = session.client("transfer")

    list_accesses_paginator: ListAccessesPaginator = client.get_paginator("list_accesses")
    list_agreements_paginator: ListAgreementsPaginator = client.get_paginator("list_agreements")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_file_transfer_results_paginator: ListFileTransferResultsPaginator = client.get_paginator("list_file_transfer_results")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_security_policies_paginator: ListSecurityPoliciesPaginator = client.get_paginator("list_security_policies")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_web_apps_paginator: ListWebAppsPaginator = client.get_paginator("list_web_apps")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccessesRequestPaginateTypeDef,
    ListAccessesResponseTypeDef,
    ListAgreementsRequestPaginateTypeDef,
    ListAgreementsResponseTypeDef,
    ListCertificatesRequestPaginateTypeDef,
    ListCertificatesResponseTypeDef,
    ListConnectorsRequestPaginateTypeDef,
    ListConnectorsResponseTypeDef,
    ListExecutionsRequestPaginateTypeDef,
    ListExecutionsResponseTypeDef,
    ListFileTransferResultsRequestPaginateTypeDef,
    ListFileTransferResultsResponseTypeDef,
    ListProfilesRequestPaginateTypeDef,
    ListProfilesResponseTypeDef,
    ListSecurityPoliciesRequestPaginateTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersRequestPaginateTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
    ListWebAppsRequestPaginateTypeDef,
    ListWebAppsResponseTypeDef,
    ListWorkflowsRequestPaginateTypeDef,
    ListWorkflowsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAccessesPaginator",
    "ListAgreementsPaginator",
    "ListCertificatesPaginator",
    "ListConnectorsPaginator",
    "ListExecutionsPaginator",
    "ListFileTransferResultsPaginator",
    "ListProfilesPaginator",
    "ListSecurityPoliciesPaginator",
    "ListServersPaginator",
    "ListTagsForResourcePaginator",
    "ListUsersPaginator",
    "ListWebAppsPaginator",
    "ListWorkflowsPaginator",
)

if TYPE_CHECKING:
    _ListAccessesPaginatorBase = Paginator[ListAccessesResponseTypeDef]
else:
    _ListAccessesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessesPaginator(_ListAccessesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListAccesses.html#Transfer.Paginator.ListAccesses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listaccessespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListAccesses.html#Transfer.Paginator.ListAccesses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listaccessespaginator)
        """

if TYPE_CHECKING:
    _ListAgreementsPaginatorBase = Paginator[ListAgreementsResponseTypeDef]
else:
    _ListAgreementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgreementsPaginator(_ListAgreementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListAgreements.html#Transfer.Paginator.ListAgreements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listagreementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgreementsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgreementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListAgreements.html#Transfer.Paginator.ListAgreements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listagreementspaginator)
        """

if TYPE_CHECKING:
    _ListCertificatesPaginatorBase = Paginator[ListCertificatesResponseTypeDef]
else:
    _ListCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCertificatesPaginator(_ListCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListCertificates.html#Transfer.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listcertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCertificatesRequestPaginateTypeDef]
    ) -> PageIterator[ListCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListCertificates.html#Transfer.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listcertificatespaginator)
        """

if TYPE_CHECKING:
    _ListConnectorsPaginatorBase = Paginator[ListConnectorsResponseTypeDef]
else:
    _ListConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectorsPaginator(_ListConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListConnectors.html#Transfer.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListConnectors.html#Transfer.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listconnectorspaginator)
        """

if TYPE_CHECKING:
    _ListExecutionsPaginatorBase = Paginator[ListExecutionsResponseTypeDef]
else:
    _ListExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExecutionsPaginator(_ListExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListExecutions.html#Transfer.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListExecutions.html#Transfer.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListFileTransferResultsPaginatorBase = Paginator[ListFileTransferResultsResponseTypeDef]
else:
    _ListFileTransferResultsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFileTransferResultsPaginator(_ListFileTransferResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListFileTransferResults.html#Transfer.Paginator.ListFileTransferResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listfiletransferresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFileTransferResultsRequestPaginateTypeDef]
    ) -> PageIterator[ListFileTransferResultsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListFileTransferResults.html#Transfer.Paginator.ListFileTransferResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listfiletransferresultspaginator)
        """

if TYPE_CHECKING:
    _ListProfilesPaginatorBase = Paginator[ListProfilesResponseTypeDef]
else:
    _ListProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfilesPaginator(_ListProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListProfiles.html#Transfer.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListProfiles.html#Transfer.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listprofilespaginator)
        """

if TYPE_CHECKING:
    _ListSecurityPoliciesPaginatorBase = Paginator[ListSecurityPoliciesResponseTypeDef]
else:
    _ListSecurityPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityPoliciesPaginator(_ListSecurityPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListSecurityPolicies.html#Transfer.Paginator.ListSecurityPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listsecuritypoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListSecurityPolicies.html#Transfer.Paginator.ListSecurityPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listsecuritypoliciespaginator)
        """

if TYPE_CHECKING:
    _ListServersPaginatorBase = Paginator[ListServersResponseTypeDef]
else:
    _ListServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListServersPaginator(_ListServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListServers.html#Transfer.Paginator.ListServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServersRequestPaginateTypeDef]
    ) -> PageIterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListServers.html#Transfer.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listserverspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListTagsForResource.html#Transfer.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListTagsForResource.html#Transfer.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListUsers.html#Transfer.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListUsers.html#Transfer.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listuserspaginator)
        """

if TYPE_CHECKING:
    _ListWebAppsPaginatorBase = Paginator[ListWebAppsResponseTypeDef]
else:
    _ListWebAppsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWebAppsPaginator(_ListWebAppsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListWebApps.html#Transfer.Paginator.ListWebApps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listwebappspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWebAppsRequestPaginateTypeDef]
    ) -> PageIterator[ListWebAppsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListWebApps.html#Transfer.Paginator.ListWebApps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listwebappspaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListWorkflows.html#Transfer.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer/paginator/ListWorkflows.html#Transfer.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators/#listworkflowspaginator)
        """
