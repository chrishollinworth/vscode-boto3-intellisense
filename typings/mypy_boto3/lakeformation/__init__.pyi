"""
Main interface for lakeformation service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lakeformation import (
        Client,
        GetWorkUnitsPaginator,
        LakeFormationClient,
        ListDataCellsFilterPaginator,
        ListLFTagsPaginator,
        SearchDatabasesByLFTagsPaginator,
        SearchTablesByLFTagsPaginator,
    )

    session = boto3.Session()

    client: LakeFormationClient = boto3.client("lakeformation")
    session_client: LakeFormationClient = session.client("lakeformation")

    get_work_units_paginator: GetWorkUnitsPaginator = client.get_paginator("get_work_units")
    list_data_cells_filter_paginator: ListDataCellsFilterPaginator = client.get_paginator("list_data_cells_filter")
    list_lf_tags_paginator: ListLFTagsPaginator = client.get_paginator("list_lf_tags")
    search_databases_by_lf_tags_paginator: SearchDatabasesByLFTagsPaginator = client.get_paginator("search_databases_by_lf_tags")
    search_tables_by_lf_tags_paginator: SearchTablesByLFTagsPaginator = client.get_paginator("search_tables_by_lf_tags")
    ```
"""
from .client import LakeFormationClient
from .paginator import (
    GetWorkUnitsPaginator,
    ListDataCellsFilterPaginator,
    ListLFTagsPaginator,
    SearchDatabasesByLFTagsPaginator,
    SearchTablesByLFTagsPaginator,
)

Client = LakeFormationClient

__all__ = (
    "Client",
    "GetWorkUnitsPaginator",
    "LakeFormationClient",
    "ListDataCellsFilterPaginator",
    "ListLFTagsPaginator",
    "SearchDatabasesByLFTagsPaginator",
    "SearchTablesByLFTagsPaginator",
)
