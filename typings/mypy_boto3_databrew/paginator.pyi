"""
Type annotations for databrew service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_databrew.client import GlueDataBrewClient
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

    session = Session()
    client: GlueDataBrewClient = session.client("databrew")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListJobRunsRequestPaginateTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesRequestPaginateTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsRequestPaginateTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListRulesetsRequestPaginateTypeDef,
    ListRulesetsResponseTypeDef,
    ListSchedulesRequestPaginateTypeDef,
    ListSchedulesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListDatasets.html#GlueDataBrew.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListDatasets.html#GlueDataBrew.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListJobRunsPaginatorBase = Paginator[ListJobRunsResponseTypeDef]
else:
    _ListJobRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobRunsPaginator(_ListJobRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListJobRuns.html#GlueDataBrew.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listjobrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListJobRuns.html#GlueDataBrew.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listjobrunspaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListJobs.html#GlueDataBrew.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListJobs.html#GlueDataBrew.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResponseTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListProjects.html#GlueDataBrew.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListProjects.html#GlueDataBrew.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListRecipeVersionsPaginatorBase = Paginator[ListRecipeVersionsResponseTypeDef]
else:
    _ListRecipeVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecipeVersionsPaginator(_ListRecipeVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRecipeVersions.html#GlueDataBrew.Paginator.ListRecipeVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrecipeversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecipeVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecipeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRecipeVersions.html#GlueDataBrew.Paginator.ListRecipeVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrecipeversionspaginator)
        """

if TYPE_CHECKING:
    _ListRecipesPaginatorBase = Paginator[ListRecipesResponseTypeDef]
else:
    _ListRecipesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecipesPaginator(_ListRecipesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRecipes.html#GlueDataBrew.Paginator.ListRecipes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrecipespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecipesRequestPaginateTypeDef]
    ) -> PageIterator[ListRecipesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRecipes.html#GlueDataBrew.Paginator.ListRecipes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrecipespaginator)
        """

if TYPE_CHECKING:
    _ListRulesetsPaginatorBase = Paginator[ListRulesetsResponseTypeDef]
else:
    _ListRulesetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesetsPaginator(_ListRulesetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRulesets.html#GlueDataBrew.Paginator.ListRulesets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrulesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesetsRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListRulesets.html#GlueDataBrew.Paginator.ListRulesets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listrulesetspaginator)
        """

if TYPE_CHECKING:
    _ListSchedulesPaginatorBase = Paginator[ListSchedulesResponseTypeDef]
else:
    _ListSchedulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchedulesPaginator(_ListSchedulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListSchedules.html#GlueDataBrew.Paginator.ListSchedules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listschedulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchedulesRequestPaginateTypeDef]
    ) -> PageIterator[ListSchedulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew/paginator/ListSchedules.html#GlueDataBrew.Paginator.ListSchedules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators/#listschedulespaginator)
        """
