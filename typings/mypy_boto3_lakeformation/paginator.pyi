"""
Type annotations for lakeformation service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lakeformation.client import LakeFormationClient
    from mypy_boto3_lakeformation.paginator import (
        GetWorkUnitsPaginator,
        ListDataCellsFilterPaginator,
        ListLFTagExpressionsPaginator,
        ListLFTagsPaginator,
        SearchDatabasesByLFTagsPaginator,
        SearchTablesByLFTagsPaginator,
    )

    session = Session()
    client: LakeFormationClient = session.client("lakeformation")

    get_work_units_paginator: GetWorkUnitsPaginator = client.get_paginator("get_work_units")
    list_data_cells_filter_paginator: ListDataCellsFilterPaginator = client.get_paginator("list_data_cells_filter")
    list_lf_tag_expressions_paginator: ListLFTagExpressionsPaginator = client.get_paginator("list_lf_tag_expressions")
    list_lf_tags_paginator: ListLFTagsPaginator = client.get_paginator("list_lf_tags")
    search_databases_by_lf_tags_paginator: SearchDatabasesByLFTagsPaginator = client.get_paginator("search_databases_by_lf_tags")
    search_tables_by_lf_tags_paginator: SearchTablesByLFTagsPaginator = client.get_paginator("search_tables_by_lf_tags")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetWorkUnitsRequestPaginateTypeDef,
    GetWorkUnitsResponseTypeDef,
    ListDataCellsFilterRequestPaginateTypeDef,
    ListDataCellsFilterResponseTypeDef,
    ListLFTagExpressionsRequestPaginateTypeDef,
    ListLFTagExpressionsResponseTypeDef,
    ListLFTagsRequestPaginateTypeDef,
    ListLFTagsResponseTypeDef,
    SearchDatabasesByLFTagsRequestPaginateTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsRequestPaginateTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetWorkUnitsPaginator",
    "ListDataCellsFilterPaginator",
    "ListLFTagExpressionsPaginator",
    "ListLFTagsPaginator",
    "SearchDatabasesByLFTagsPaginator",
    "SearchTablesByLFTagsPaginator",
)

if TYPE_CHECKING:
    _GetWorkUnitsPaginatorBase = Paginator[GetWorkUnitsResponseTypeDef]
else:
    _GetWorkUnitsPaginatorBase = Paginator  # type: ignore[assignment]

class GetWorkUnitsPaginator(_GetWorkUnitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/GetWorkUnits.html#LakeFormation.Paginator.GetWorkUnits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#getworkunitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetWorkUnitsRequestPaginateTypeDef]
    ) -> PageIterator[GetWorkUnitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/GetWorkUnits.html#LakeFormation.Paginator.GetWorkUnits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#getworkunitspaginator)
        """

if TYPE_CHECKING:
    _ListDataCellsFilterPaginatorBase = Paginator[ListDataCellsFilterResponseTypeDef]
else:
    _ListDataCellsFilterPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataCellsFilterPaginator(_ListDataCellsFilterPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListDataCellsFilter.html#LakeFormation.Paginator.ListDataCellsFilter)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listdatacellsfilterpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataCellsFilterRequestPaginateTypeDef]
    ) -> PageIterator[ListDataCellsFilterResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListDataCellsFilter.html#LakeFormation.Paginator.ListDataCellsFilter.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listdatacellsfilterpaginator)
        """

if TYPE_CHECKING:
    _ListLFTagExpressionsPaginatorBase = Paginator[ListLFTagExpressionsResponseTypeDef]
else:
    _ListLFTagExpressionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLFTagExpressionsPaginator(_ListLFTagExpressionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListLFTagExpressions.html#LakeFormation.Paginator.ListLFTagExpressions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagexpressionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLFTagExpressionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLFTagExpressionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListLFTagExpressions.html#LakeFormation.Paginator.ListLFTagExpressions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagexpressionspaginator)
        """

if TYPE_CHECKING:
    _ListLFTagsPaginatorBase = Paginator[ListLFTagsResponseTypeDef]
else:
    _ListLFTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLFTagsPaginator(_ListLFTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListLFTags.html#LakeFormation.Paginator.ListLFTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLFTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/ListLFTags.html#LakeFormation.Paginator.ListLFTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagspaginator)
        """

if TYPE_CHECKING:
    _SearchDatabasesByLFTagsPaginatorBase = Paginator[SearchDatabasesByLFTagsResponseTypeDef]
else:
    _SearchDatabasesByLFTagsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchDatabasesByLFTagsPaginator(_SearchDatabasesByLFTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/SearchDatabasesByLFTags.html#LakeFormation.Paginator.SearchDatabasesByLFTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchdatabasesbylftagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchDatabasesByLFTagsRequestPaginateTypeDef]
    ) -> PageIterator[SearchDatabasesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/SearchDatabasesByLFTags.html#LakeFormation.Paginator.SearchDatabasesByLFTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchdatabasesbylftagspaginator)
        """

if TYPE_CHECKING:
    _SearchTablesByLFTagsPaginatorBase = Paginator[SearchTablesByLFTagsResponseTypeDef]
else:
    _SearchTablesByLFTagsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchTablesByLFTagsPaginator(_SearchTablesByLFTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/SearchTablesByLFTags.html#LakeFormation.Paginator.SearchTablesByLFTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchtablesbylftagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchTablesByLFTagsRequestPaginateTypeDef]
    ) -> PageIterator[SearchTablesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation/paginator/SearchTablesByLFTags.html#LakeFormation.Paginator.SearchTablesByLFTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchtablesbylftagspaginator)
        """
