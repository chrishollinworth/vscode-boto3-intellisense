"""
Type annotations for connectcases service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_connectcases import ConnectCasesClient
    from mypy_boto3_connectcases.paginator import (
        SearchCasesPaginator,
        SearchRelatedItemsPaginator,
    )

    client: ConnectCasesClient = boto3.client("connectcases")

    search_cases_paginator: SearchCasesPaginator = client.get_paginator("search_cases")
    search_related_items_paginator: SearchRelatedItemsPaginator = client.get_paginator("search_related_items")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    CaseFilterTypeDef,
    FieldIdentifierTypeDef,
    PaginatorConfigTypeDef,
    RelatedItemTypeFilterTypeDef,
    SearchCasesResponseTypeDef,
    SearchRelatedItemsResponseTypeDef,
    SortTypeDef,
)

__all__ = ("SearchCasesPaginator", "SearchRelatedItemsPaginator")

class SearchCasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/connectcases.html#ConnectCases.Paginator.SearchCases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchcasespaginator)
    """

    def paginate(
        self,
        *,
        domainId: str,
        fields: List["FieldIdentifierTypeDef"] = None,
        filter: "CaseFilterTypeDef" = None,
        searchTerm: str = None,
        sorts: List["SortTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/connectcases.html#ConnectCases.Paginator.SearchCases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchcasespaginator)
        """

class SearchRelatedItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/connectcases.html#ConnectCases.Paginator.SearchRelatedItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchrelateditemspaginator)
    """

    def paginate(
        self,
        *,
        caseId: str,
        domainId: str,
        filters: List["RelatedItemTypeFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/connectcases.html#ConnectCases.Paginator.SearchRelatedItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/paginators.html#searchrelateditemspaginator)
        """
