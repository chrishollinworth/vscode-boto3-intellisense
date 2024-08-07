"""
Type annotations for personalize service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_personalize import PersonalizeClient
    from mypy_boto3_personalize.paginator import (
        ListBatchInferenceJobsPaginator,
        ListBatchSegmentJobsPaginator,
        ListCampaignsPaginator,
        ListDatasetExportJobsPaginator,
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListEventTrackersPaginator,
        ListFiltersPaginator,
        ListMetricAttributionMetricsPaginator,
        ListMetricAttributionsPaginator,
        ListRecipesPaginator,
        ListRecommendersPaginator,
        ListSchemasPaginator,
        ListSolutionVersionsPaginator,
        ListSolutionsPaginator,
    )

    client: PersonalizeClient = boto3.client("personalize")

    list_batch_inference_jobs_paginator: ListBatchInferenceJobsPaginator = client.get_paginator("list_batch_inference_jobs")
    list_batch_segment_jobs_paginator: ListBatchSegmentJobsPaginator = client.get_paginator("list_batch_segment_jobs")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_dataset_export_jobs_paginator: ListDatasetExportJobsPaginator = client.get_paginator("list_dataset_export_jobs")
    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_event_trackers_paginator: ListEventTrackersPaginator = client.get_paginator("list_event_trackers")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_metric_attribution_metrics_paginator: ListMetricAttributionMetricsPaginator = client.get_paginator("list_metric_attribution_metrics")
    list_metric_attributions_paginator: ListMetricAttributionsPaginator = client.get_paginator("list_metric_attributions")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_recommenders_paginator: ListRecommendersPaginator = client.get_paginator("list_recommenders")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_solution_versions_paginator: ListSolutionVersionsPaginator = client.get_paginator("list_solution_versions")
    list_solutions_paginator: ListSolutionsPaginator = client.get_paginator("list_solutions")
    ```
"""

import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import DomainType
from .type_defs import (
    ListBatchInferenceJobsResponseTypeDef,
    ListBatchSegmentJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetExportJobsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListMetricAttributionMetricsResponseTypeDef,
    ListMetricAttributionsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecommendersResponseTypeDef,
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
    "ListBatchSegmentJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetExportJobsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListFiltersPaginator",
    "ListMetricAttributionMetricsPaginator",
    "ListMetricAttributionsPaginator",
    "ListRecipesPaginator",
    "ListRecommendersPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
)

class ListBatchInferenceJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchinferencejobspaginator)
    """

    def paginate(
        self, *, solutionVersionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchInferenceJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchinferencejobspaginator)
        """

class ListBatchSegmentJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListBatchSegmentJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchsegmentjobspaginator)
    """

    def paginate(
        self, *, solutionVersionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchSegmentJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListBatchSegmentJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchsegmentjobspaginator)
        """

class ListCampaignsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listcampaignspaginator)
    """

    def paginate(
        self, *, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listcampaignspaginator)
        """

class ListDatasetExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetexportjobspaginator)
    """

    def paginate(
        self, *, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetexportjobspaginator)
        """

class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetgroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetgroupspaginator)
        """

class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetimportjobspaginator)
    """

    def paginate(
        self, *, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetimportjobspaginator)
        """

class ListDatasetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetspaginator)
        """

class ListEventTrackersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listeventtrackerspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventTrackersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listeventtrackerspaginator)
        """

class ListFiltersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListFilters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listfilterspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListFilters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listfilterspaginator)
        """

class ListMetricAttributionMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributionMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionmetricspaginator)
    """

    def paginate(
        self, *, metricAttributionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMetricAttributionMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributionMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionmetricspaginator)
        """

class ListMetricAttributionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMetricAttributionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionspaginator)
        """

class ListRecipesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecipespaginator)
    """

    def paginate(
        self,
        *,
        recipeProvider: Literal["SERVICE"] = None,
        domain: DomainType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListRecipes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecipespaginator)
        """

class ListRecommendersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListRecommenders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecommenderspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListRecommenders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecommenderspaginator)
        """

class ListSchemasPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listschemaspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listschemaspaginator)
        """

class ListSolutionVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionversionspaginator)
    """

    def paginate(
        self, *, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionversionspaginator)
        """

class ListSolutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionspaginator)
    """

    def paginate(
        self, *, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/personalize.html#Personalize.Paginator.ListSolutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionspaginator)
        """
