# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for personalize service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_personalize import PersonalizeClient
    from mypy_boto3_personalize.paginator import (
        ListBatchInferenceJobsPaginator,
        ListCampaignsPaginator,
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListEventTrackersPaginator,
        ListRecipesPaginator,
        ListSchemasPaginator,
        ListSolutionVersionsPaginator,
        ListSolutionsPaginator,
    )

    client: PersonalizeClient = boto3.client("personalize")

    list_batch_inference_jobs_paginator: ListBatchInferenceJobsPaginator = client.get_paginator("list_batch_inference_jobs")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_event_trackers_paginator: ListEventTrackersPaginator = client.get_paginator("list_event_trackers")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_solution_versions_paginator: ListSolutionVersionsPaginator = client.get_paginator("list_solution_versions")
    list_solutions_paginator: ListSolutionsPaginator = client.get_paginator("list_solutions")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_personalize.type_defs import (
    ListBatchInferenceJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionsResponseTypeDef,
    ListSolutionVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
)


class ListBatchInferenceJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
    """

    def paginate(
        self, solutionVersionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchInferenceJobsResponseTypeDef]:
        """
        [ListBatchInferenceJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        """


class ListCampaignsPaginator(Boto3Paginator):
    """
    [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
    """

    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        """
        [ListCampaigns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListCampaigns.paginate)
        """


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
    """

    def paginate(
        self, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListDatasets.paginate)
        """


class ListEventTrackersPaginator(Boto3Paginator):
    """
    [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventTrackersResponseTypeDef]:
        """
        [ListEventTrackers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers.paginate)
        """


class ListRecipesPaginator(Boto3Paginator):
    """
    [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
    """

    def paginate(
        self,
        recipeProvider: Literal["SERVICE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRecipesResponseTypeDef]:
        """
        [ListRecipes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListRecipes.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSchemas.paginate)
        """


class ListSolutionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
    """

    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionVersionsResponseTypeDef]:
        """
        [ListSolutionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions.paginate)
        """


class ListSolutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionsResponseTypeDef]:
        """
        [ListSolutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/personalize.html#Personalize.Paginator.ListSolutions.paginate)
        """
