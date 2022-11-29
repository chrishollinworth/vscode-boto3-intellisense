"""
Type annotations for lakeformation service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_lakeformation import LakeFormationClient
    from mypy_boto3_lakeformation.paginator import (
        GetWorkUnitsPaginator,
        ListDataCellsFilterPaginator,
        ListLFTagsPaginator,
        SearchDatabasesByLFTagsPaginator,
        SearchTablesByLFTagsPaginator,
    )

    client: LakeFormationClient = boto3.client("lakeformation")

    get_work_units_paginator: GetWorkUnitsPaginator = client.get_paginator("get_work_units")
    list_data_cells_filter_paginator: ListDataCellsFilterPaginator = client.get_paginator("list_data_cells_filter")
    list_lf_tags_paginator: ListLFTagsPaginator = client.get_paginator("list_lf_tags")
    search_databases_by_lf_tags_paginator: SearchDatabasesByLFTagsPaginator = client.get_paginator("search_databases_by_lf_tags")
    search_tables_by_lf_tags_paginator: SearchTablesByLFTagsPaginator = client.get_paginator("search_tables_by_lf_tags")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ResourceShareTypeType
from .type_defs import (
    GetWorkUnitsResponseTypeDef,
    LFTagTypeDef,
    ListDataCellsFilterResponseTypeDef,
    ListLFTagsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
    TableResourceTypeDef,
)

__all__ = (
    "GetWorkUnitsPaginator",
    "ListDataCellsFilterPaginator",
    "ListLFTagsPaginator",
    "SearchDatabasesByLFTagsPaginator",
    "SearchTablesByLFTagsPaginator",
)

class GetWorkUnitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.GetWorkUnits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#getworkunitspaginator)
    """

    def paginate(
        self, *, QueryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetWorkUnitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.GetWorkUnits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#getworkunitspaginator)
        """

class ListDataCellsFilterPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.ListDataCellsFilter)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listdatacellsfilterpaginator)
    """

    def paginate(
        self,
        *,
        Table: "TableResourceTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataCellsFilterResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.ListDataCellsFilter.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listdatacellsfilterpaginator)
        """

class ListLFTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.ListLFTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listlftagspaginator)
    """

    def paginate(
        self,
        *,
        CatalogId: str = None,
        ResourceShareType: ResourceShareTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.ListLFTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#listlftagspaginator)
        """

class SearchDatabasesByLFTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.SearchDatabasesByLFTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchdatabasesbylftagspaginator)
    """

    def paginate(
        self,
        *,
        Expression: List["LFTagTypeDef"],
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDatabasesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.SearchDatabasesByLFTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchdatabasesbylftagspaginator)
        """

class SearchTablesByLFTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.SearchTablesByLFTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchtablesbylftagspaginator)
    """

    def paginate(
        self,
        *,
        Expression: List["LFTagTypeDef"],
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchTablesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/lakeformation.html#LakeFormation.Paginator.SearchTablesByLFTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators.html#searchtablesbylftagspaginator)
        """
