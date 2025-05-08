"""
Type annotations for amp service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_amp.client import PrometheusServiceClient
    from mypy_boto3_amp.paginator import (
        ListRuleGroupsNamespacesPaginator,
        ListScrapersPaginator,
        ListWorkspacesPaginator,
    )

    session = Session()
    client: PrometheusServiceClient = session.client("amp")

    list_rule_groups_namespaces_paginator: ListRuleGroupsNamespacesPaginator = client.get_paginator("list_rule_groups_namespaces")
    list_scrapers_paginator: ListScrapersPaginator = client.get_paginator("list_scrapers")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListRuleGroupsNamespacesRequestPaginateTypeDef,
    ListRuleGroupsNamespacesResponseTypeDef,
    ListScrapersRequestPaginateTypeDef,
    ListScrapersResponseTypeDef,
    ListWorkspacesRequestPaginateTypeDef,
    ListWorkspacesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRuleGroupsNamespacesPaginator", "ListScrapersPaginator", "ListWorkspacesPaginator")

if TYPE_CHECKING:
    _ListRuleGroupsNamespacesPaginatorBase = Paginator[ListRuleGroupsNamespacesResponseTypeDef]
else:
    _ListRuleGroupsNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRuleGroupsNamespacesPaginator(_ListRuleGroupsNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListRuleGroupsNamespaces.html#PrometheusService.Paginator.ListRuleGroupsNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listrulegroupsnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRuleGroupsNamespacesRequestPaginateTypeDef]
    ) -> PageIterator[ListRuleGroupsNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListRuleGroupsNamespaces.html#PrometheusService.Paginator.ListRuleGroupsNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listrulegroupsnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListScrapersPaginatorBase = Paginator[ListScrapersResponseTypeDef]
else:
    _ListScrapersPaginatorBase = Paginator  # type: ignore[assignment]

class ListScrapersPaginator(_ListScrapersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListScrapers.html#PrometheusService.Paginator.ListScrapers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listscraperspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScrapersRequestPaginateTypeDef]
    ) -> PageIterator[ListScrapersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListScrapers.html#PrometheusService.Paginator.ListScrapers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listscraperspaginator)
        """

if TYPE_CHECKING:
    _ListWorkspacesPaginatorBase = Paginator[ListWorkspacesResponseTypeDef]
else:
    _ListWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkspacesPaginator(_ListWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListWorkspaces.html#PrometheusService.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp/paginator/ListWorkspaces.html#PrometheusService.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators/#listworkspacespaginator)
        """
