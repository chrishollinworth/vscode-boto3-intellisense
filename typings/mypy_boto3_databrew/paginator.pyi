"""
Type annotations for databrew service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html)

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
        ListRulesetsPaginator,
        ListSchedulesPaginator,
    )

    client: GlueDataBrewClient = boto3.client("databrew")

    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_recipe_versions_paginator: ListRecipeVersionsPaginator = client.get_paginator("list_recipe_versions")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_rulesets_paginator: ListRulesetsPaginator = client.get_paginator("list_rulesets")
    list_schedules_paginator: ListSchedulesPaginator = client.get_paginator("list_schedules")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListDatasetsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListRulesetsResponseTypeDef,
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
    "ListRulesetsPaginator",
    "ListSchedulesPaginator",
)

class ListDatasetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listdatasetspaginator)
        """

class ListJobRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobrunspaginator)
    """

    def paginate(
        self, *, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobrunspaginator)
        """

class ListJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobspaginator)
    """

    def paginate(
        self,
        *,
        DatasetName: str = None,
        ProjectName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobspaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listprojectspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listprojectspaginator)
        """

class ListRecipeVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipeversionspaginator)
    """

    def paginate(
        self, *, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipeversionspaginator)
        """

class ListRecipesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipespaginator)
    """

    def paginate(
        self, *, RecipeVersion: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipespaginator)
        """

class ListRulesetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRulesets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrulesetspaginator)
    """

    def paginate(
        self, *, TargetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListRulesets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrulesetspaginator)
        """

class ListSchedulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listschedulespaginator)
    """

    def paginate(
        self, *, JobName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchedulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listschedulespaginator)
        """
