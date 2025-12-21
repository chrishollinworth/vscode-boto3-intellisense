"""
Type annotations for connectcases service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_connectcases.client import ConnectCasesClient
    from mypy_boto3_connectcases.paginator import (
        ListCaseRulesPaginator,
        SearchAllRelatedItemsPaginator,
        SearchCasesPaginator,
        SearchRelatedItemsPaginator,
    )

    session = Session()
    client: ConnectCasesClient = session.client("connectcases")

    list_case_rules_paginator: ListCaseRulesPaginator = client.get_paginator("list_case_rules")
    search_all_related_items_paginator: SearchAllRelatedItemsPaginator = client.get_paginator("search_all_related_items")
    search_cases_paginator: SearchCasesPaginator = client.get_paginator("search_cases")
    search_related_items_paginator: SearchRelatedItemsPaginator = client.get_paginator("search_related_items")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCaseRulesRequestPaginateTypeDef,
    ListCaseRulesResponseTypeDef,
    SearchAllRelatedItemsRequestPaginateTypeDef,
    SearchAllRelatedItemsResponseTypeDef,
    SearchCasesRequestPaginateTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsRequestPaginateTypeDef,
    SearchRelatedItemsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCaseRulesPaginator",
    "SearchAllRelatedItemsPaginator",
    "SearchCasesPaginator",
    "SearchRelatedItemsPaginator",
)

if TYPE_CHECKING:
    _ListCaseRulesPaginatorBase = Paginator[ListCaseRulesResponseTypeDef]
else:
    _ListCaseRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCaseRulesPaginator(_ListCaseRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/ListCaseRules.html#ConnectCases.Paginator.ListCaseRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#listcaserulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCaseRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListCaseRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/ListCaseRules.html#ConnectCases.Paginator.ListCaseRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#listcaserulespaginator)
        """

if TYPE_CHECKING:
    _SearchAllRelatedItemsPaginatorBase = Paginator[SearchAllRelatedItemsResponseTypeDef]
else:
    _SearchAllRelatedItemsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchAllRelatedItemsPaginator(_SearchAllRelatedItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchAllRelatedItems.html#ConnectCases.Paginator.SearchAllRelatedItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchallrelateditemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchAllRelatedItemsRequestPaginateTypeDef]
    ) -> PageIterator[SearchAllRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchAllRelatedItems.html#ConnectCases.Paginator.SearchAllRelatedItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchallrelateditemspaginator)
        """

if TYPE_CHECKING:
    _SearchCasesPaginatorBase = Paginator[SearchCasesResponseTypeDef]
else:
    _SearchCasesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchCasesPaginator(_SearchCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchCases.html#ConnectCases.Paginator.SearchCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchCasesRequestPaginateTypeDef]
    ) -> PageIterator[SearchCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchCases.html#ConnectCases.Paginator.SearchCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchcasespaginator)
        """

if TYPE_CHECKING:
    _SearchRelatedItemsPaginatorBase = Paginator[SearchRelatedItemsResponseTypeDef]
else:
    _SearchRelatedItemsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchRelatedItemsPaginator(_SearchRelatedItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchRelatedItems.html#ConnectCases.Paginator.SearchRelatedItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchrelateditemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchRelatedItemsRequestPaginateTypeDef]
    ) -> PageIterator[SearchRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases/paginator/SearchRelatedItems.html#ConnectCases.Paginator.SearchRelatedItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators/#searchrelateditemspaginator)
        """
