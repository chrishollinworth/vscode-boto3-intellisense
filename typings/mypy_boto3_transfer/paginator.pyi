"""
Type annotations for transfer service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_transfer import TransferClient
    from mypy_boto3_transfer.paginator import (
        ListAccessesPaginator,
        ListAgreementsPaginator,
        ListCertificatesPaginator,
        ListConnectorsPaginator,
        ListExecutionsPaginator,
        ListProfilesPaginator,
        ListSecurityPoliciesPaginator,
        ListServersPaginator,
        ListTagsForResourcePaginator,
        ListUsersPaginator,
        ListWorkflowsPaginator,
    )

    client: TransferClient = boto3.client("transfer")

    list_accesses_paginator: ListAccessesPaginator = client.get_paginator("list_accesses")
    list_agreements_paginator: ListAgreementsPaginator = client.get_paginator("list_agreements")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_connectors_paginator: ListConnectorsPaginator = client.get_paginator("list_connectors")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_security_policies_paginator: ListSecurityPoliciesPaginator = client.get_paginator("list_security_policies")
    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ProfileTypeType
from .type_defs import (
    ListAccessesResponseTypeDef,
    ListAgreementsResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListExecutionsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAccessesPaginator",
    "ListAgreementsPaginator",
    "ListCertificatesPaginator",
    "ListConnectorsPaginator",
    "ListExecutionsPaginator",
    "ListProfilesPaginator",
    "ListSecurityPoliciesPaginator",
    "ListServersPaginator",
    "ListTagsForResourcePaginator",
    "ListUsersPaginator",
    "ListWorkflowsPaginator",
)

class ListAccessesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAccesses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listaccessespaginator)
    """

    def paginate(
        self, *, ServerId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAccesses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listaccessespaginator)
        """

class ListAgreementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAgreements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listagreementspaginator)
    """

    def paginate(
        self, *, ServerId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgreementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListAgreements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listagreementspaginator)
        """

class ListCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listcertificatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listcertificatespaginator)
        """

class ListConnectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListConnectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listconnectorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListConnectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listconnectorspaginator)
        """

class ListExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listexecutionspaginator)
    """

    def paginate(
        self, *, WorkflowId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listexecutionspaginator)
        """

class ListProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listprofilespaginator)
    """

    def paginate(
        self,
        *,
        ProfileType: ProfileTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listprofilespaginator)
        """

class ListSecurityPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListSecurityPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listsecuritypoliciespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListSecurityPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listsecuritypoliciespaginator)
        """

class ListServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listtagsforresourcepaginator)
        """

class ListUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listuserspaginator)
    """

    def paginate(
        self, *, ServerId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listuserspaginator)
        """

class ListWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listworkflowspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/transfer.html#Transfer.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listworkflowspaginator)
        """
