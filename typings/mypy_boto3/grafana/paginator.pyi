"""
Type annotations for grafana service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_grafana import ManagedGrafanaClient
    from mypy_boto3_grafana.paginator import (
        ListPermissionsPaginator,
        ListVersionsPaginator,
        ListWorkspaceServiceAccountTokensPaginator,
        ListWorkspaceServiceAccountsPaginator,
        ListWorkspacesPaginator,
    )

    client: ManagedGrafanaClient = boto3.client("grafana")

    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_versions_paginator: ListVersionsPaginator = client.get_paginator("list_versions")
    list_workspace_service_account_tokens_paginator: ListWorkspaceServiceAccountTokensPaginator = client.get_paginator("list_workspace_service_account_tokens")
    list_workspace_service_accounts_paginator: ListWorkspaceServiceAccountsPaginator = client.get_paginator("list_workspace_service_accounts")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import UserTypeType
from .type_defs import (
    ListPermissionsResponseTypeDef,
    ListVersionsResponseTypeDef,
    ListWorkspaceServiceAccountsResponseTypeDef,
    ListWorkspaceServiceAccountTokensResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListPermissionsPaginator",
    "ListVersionsPaginator",
    "ListWorkspaceServiceAccountTokensPaginator",
    "ListWorkspaceServiceAccountsPaginator",
    "ListWorkspacesPaginator",
)

class ListPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listpermissionspaginator)
    """

    def paginate(
        self,
        *,
        workspaceId: str,
        groupId: str = None,
        userId: str = None,
        userType: UserTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listpermissionspaginator)
        """

class ListVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listversionspaginator)
    """

    def paginate(
        self, *, workspaceId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listversionspaginator)
        """

class ListWorkspaceServiceAccountTokensPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccountTokens)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspaceserviceaccounttokenspaginator)
    """

    def paginate(
        self,
        *,
        serviceAccountId: str,
        workspaceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspaceServiceAccountTokensResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccountTokens.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspaceserviceaccounttokenspaginator)
        """

class ListWorkspaceServiceAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspaceserviceaccountspaginator)
    """

    def paginate(
        self, *, workspaceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspaceServiceAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspaceserviceaccountspaginator)
        """

class ListWorkspacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspacespaginator)
        """
