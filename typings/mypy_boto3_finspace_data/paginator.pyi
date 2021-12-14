"""
Type annotations for finspace-data service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_finspace_data import FinSpaceDataClient
    from mypy_boto3_finspace_data.paginator import (
        ListChangesetsPaginator,
        ListDataViewsPaginator,
        ListDatasetsPaginator,
    )

    client: FinSpaceDataClient = boto3.client("finspace-data")

    list_changesets_paginator: ListChangesetsPaginator = client.get_paginator("list_changesets")
    list_data_views_paginator: ListDataViewsPaginator = client.get_paginator("list_data_views")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListChangesetsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListDataViewsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListChangesetsPaginator", "ListDataViewsPaginator", "ListDatasetsPaginator")

class ListChangesetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListChangesets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listchangesetspaginator)
    """

    def paginate(
        self, *, datasetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChangesetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListChangesets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listchangesetspaginator)
        """

class ListDataViewsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDataViews)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdataviewspaginator)
    """

    def paginate(
        self, *, datasetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataViewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDataViews.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdataviewspaginator)
        """

class ListDatasetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/finspace-data.html#FinSpaceData.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/paginators.html#listdatasetspaginator)
        """
