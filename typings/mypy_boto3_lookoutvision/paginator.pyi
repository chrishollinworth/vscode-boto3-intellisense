"""
Main interface for lookoutvision service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_lookoutvision import LookoutforVisionClient
    from mypy_boto3_lookoutvision.paginator import (
        ListDatasetEntriesPaginator,
        ListModelsPaginator,
        ListProjectsPaginator,
    )

    client: LookoutforVisionClient = boto3.client("lookoutvision")

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
    [Paginator.ListDatasetEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries)
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
        [ListDatasetEntries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListDatasetEntries.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels)
    """

    def paginate(
        self, ProjectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListModelsResponseTypeDef]:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListModels.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/lookoutvision.html#LookoutforVision.Paginator.ListProjects.paginate)
        """
