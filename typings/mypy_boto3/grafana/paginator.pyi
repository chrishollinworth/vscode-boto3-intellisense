"""
Type annotations for grafana service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_grafana.client import ManagedGrafanaClient
    from mypy_boto3_grafana.paginator import (
        ListPermissionsPaginator,
        ListVersionsPaginator,
        ListWorkspaceServiceAccountTokensPaginator,
        ListWorkspaceServiceAccountsPaginator,
        ListWorkspacesPaginator,
    )

    session = Session()
    client: ManagedGrafanaClient = session.client("grafana")

    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_versions_paginator: ListVersionsPaginator = client.get_paginator("list_versions")
    list_workspace_service_account_tokens_paginator: ListWorkspaceServiceAccountTokensPaginator = client.get_paginator("list_workspace_service_account_tokens")
    list_workspace_service_accounts_paginator: ListWorkspaceServiceAccountsPaginator = client.get_paginator("list_workspace_service_accounts")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListPermissionsRequestPaginateTypeDef,
    ListPermissionsResponseTypeDef,
    ListVersionsRequestPaginateTypeDef,
    ListVersionsResponseTypeDef,
    ListWorkspaceServiceAccountsRequestPaginateTypeDef,
    ListWorkspaceServiceAccountsResponseTypeDef,
    ListWorkspaceServiceAccountTokensRequestPaginateTypeDef,
    ListWorkspaceServiceAccountTokensResponseTypeDef,
    ListWorkspacesRequestPaginateTypeDef,
    ListWorkspacesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListPermissionsPaginator",
    "ListVersionsPaginator",
    "ListWorkspaceServiceAccountTokensPaginator",
    "ListWorkspaceServiceAccountsPaginator",
    "ListWorkspacesPaginator",
)

if TYPE_CHECKING:
    _ListPermissionsPaginatorBase = Paginator[ListPermissionsResponseTypeDef]
else:
    _ListPermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPermissionsPaginator(_ListPermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListPermissions.html#ManagedGrafana.Paginator.ListPermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listpermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPermissionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListPermissions.html#ManagedGrafana.Paginator.ListPermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listpermissionspaginator)
        """

if TYPE_CHECKING:
    _ListVersionsPaginatorBase = Paginator[ListVersionsResponseTypeDef]
else:
    _ListVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVersionsPaginator(_ListVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListVersions.html#ManagedGrafana.Paginator.ListVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListVersions.html#ManagedGrafana.Paginator.ListVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listversionspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspaceServiceAccountTokensPaginatorBase = Paginator[
        ListWorkspaceServiceAccountTokensResponseTypeDef
    ]
else:
    _ListWorkspaceServiceAccountTokensPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspaceServiceAccountTokensPaginator(_ListWorkspaceServiceAccountTokensPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaceServiceAccountTokens.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccountTokens)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspaceserviceaccounttokenspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspaceServiceAccountTokensRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspaceServiceAccountTokensResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaceServiceAccountTokens.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccountTokens.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspaceserviceaccounttokenspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspaceServiceAccountsPaginatorBase = Paginator[
        ListWorkspaceServiceAccountsResponseTypeDef
    ]
else:
    _ListWorkspaceServiceAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspaceServiceAccountsPaginator(_ListWorkspaceServiceAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaceServiceAccounts.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspaceserviceaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspaceServiceAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspaceServiceAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaceServiceAccounts.html#ManagedGrafana.Paginator.ListWorkspaceServiceAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspaceserviceaccountspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspacesPaginatorBase = Paginator[ListWorkspacesResponseTypeDef]
else:
    _ListWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspacesPaginator(_ListWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaces.html#ManagedGrafana.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/paginator/ListWorkspaces.html#ManagedGrafana.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators/#listworkspacespaginator)
        """
