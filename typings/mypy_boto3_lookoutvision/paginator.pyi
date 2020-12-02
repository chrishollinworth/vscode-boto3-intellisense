# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for lookoutvision service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_lookoutvision import LookoutForVisionClient
    from mypy_boto3_lookoutvision.paginator import (
        ListDatasetEntriesPaginator,
        ListModelsPaginator,
        ListProjectsPaginator,
    )

    client: LookoutForVisionClient = boto3.client("lookoutvision")

    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_lookoutvision.type_defs import (
    ListDatasetEntriesResponseTypeDef,
    ListModelsResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDatasetEntriesPaginator", "ListModelsPaginator", "ListProjectsPaginator")


class ListDatasetEntriesPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListDatasetEntries)
    """

    def paginate(
        self,
        ProjectName: str,
        DatasetType: str,
        Labeled: bool = None,
        AnomalyClass: str = None,
        BeforeCreationDate: datetime = None,
        AfterCreationDate: datetime = None,
        SourceRefContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDatasetEntriesResponseTypeDef]:
        """
        [ListDatasetEntries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListDatasetEntries.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListModels)
    """

    def paginate(
        self, ProjectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelsResponseTypeDef]:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListModels.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/lookoutvision.html#LookoutForVision.Paginator.ListProjects.paginate)
        """
