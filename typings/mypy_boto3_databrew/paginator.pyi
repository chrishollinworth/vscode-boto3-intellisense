"""
Main interface for databrew service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_databrew import GlueDataBrewClient
    from mypy_boto3_databrew.paginator import (
        ListDatasetsPaginator,
        ListJobRunsPaginator,
        ListJobsPaginator,
        ListProjectsPaginator,
        ListRecipeVersionsPaginator,
        ListRecipesPaginator,
        ListSchedulesPaginator,
    )

    client: GlueDataBrewClient = boto3.client("databrew")

    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_recipe_versions_paginator: ListRecipeVersionsPaginator = client.get_paginator("list_recipe_versions")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_schedules_paginator: ListSchedulesPaginator = client.get_paginator("list_schedules")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_databrew.type_defs import (
    ListDatasetsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListSchedulesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDatasetsPaginator",
    "ListJobRunsPaginator",
    "ListJobsPaginator",
    "ListProjectsPaginator",
    "ListRecipeVersionsPaginator",
    "ListRecipesPaginator",
    "ListSchedulesPaginator",
)


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets.paginate)
        """


class ListJobRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)
    """

    def paginate(
        self, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [ListJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)
    """

    def paginate(
        self,
        DatasetName: str = None,
        ProjectName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects.paginate)
        """


class ListRecipeVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListRecipeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)
    """

    def paginate(
        self, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipeVersionsResponseTypeDef]:
        """
        [ListRecipeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions.paginate)
        """


class ListRecipesPaginator(Boto3Paginator):
    """
    [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)
    """

    def paginate(
        self, RecipeVersion: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        """
        [ListRecipes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes.paginate)
        """


class ListSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)
    """

    def paginate(
        self, JobName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchedulesResponseTypeDef]:
        """
        [ListSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules.paginate)
        """
