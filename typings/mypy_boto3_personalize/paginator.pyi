"""
Type annotations for personalize service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_personalize.client import PersonalizeClient
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

    session = Session()
    client: PersonalizeClient = session.client("personalize")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBatchInferenceJobsRequestPaginateTypeDef,
    ListBatchInferenceJobsResponseTypeDef,
    ListBatchSegmentJobsRequestPaginateTypeDef,
    ListBatchSegmentJobsResponseTypeDef,
    ListCampaignsRequestPaginateTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetExportJobsRequestPaginateTypeDef,
    ListDatasetExportJobsResponseTypeDef,
    ListDatasetGroupsRequestPaginateTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsRequestPaginateTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersRequestPaginateTypeDef,
    ListEventTrackersResponseTypeDef,
    ListFiltersRequestPaginateTypeDef,
    ListFiltersResponseTypeDef,
    ListMetricAttributionMetricsRequestPaginateTypeDef,
    ListMetricAttributionMetricsResponseTypeDef,
    ListMetricAttributionsRequestPaginateTypeDef,
    ListMetricAttributionsResponseTypeDef,
    ListRecipesRequestPaginateTypeDef,
    ListRecipesResponseTypeDef,
    ListRecommendersRequestPaginateTypeDef,
    ListRecommendersResponseTypeDef,
    ListSchemasRequestPaginateTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionsRequestPaginateTypeDef,
    ListSolutionsResponseTypeDef,
    ListSolutionVersionsRequestPaginateTypeDef,
    ListSolutionVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListBatchInferenceJobsPaginatorBase = Paginator[ListBatchInferenceJobsResponseTypeDef]
else:
    _ListBatchInferenceJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBatchInferenceJobsPaginator(_ListBatchInferenceJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListBatchInferenceJobs.html#Personalize.Paginator.ListBatchInferenceJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listbatchinferencejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBatchInferenceJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListBatchInferenceJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListBatchInferenceJobs.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listbatchinferencejobspaginator)
        """

if TYPE_CHECKING:
    _ListBatchSegmentJobsPaginatorBase = Paginator[ListBatchSegmentJobsResponseTypeDef]
else:
    _ListBatchSegmentJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBatchSegmentJobsPaginator(_ListBatchSegmentJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListBatchSegmentJobs.html#Personalize.Paginator.ListBatchSegmentJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listbatchsegmentjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBatchSegmentJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListBatchSegmentJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListBatchSegmentJobs.html#Personalize.Paginator.ListBatchSegmentJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listbatchsegmentjobspaginator)
        """

if TYPE_CHECKING:
    _ListCampaignsPaginatorBase = Paginator[ListCampaignsResponseTypeDef]
else:
    _ListCampaignsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCampaignsPaginator(_ListCampaignsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListCampaigns.html#Personalize.Paginator.ListCampaigns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listcampaignspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCampaignsRequestPaginateTypeDef]
    ) -> PageIterator[ListCampaignsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListCampaigns.html#Personalize.Paginator.ListCampaigns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listcampaignspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetExportJobsPaginatorBase = Paginator[ListDatasetExportJobsResponseTypeDef]
else:
    _ListDatasetExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetExportJobsPaginator(_ListDatasetExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetExportJobs.html#Personalize.Paginator.ListDatasetExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetExportJobs.html#Personalize.Paginator.ListDatasetExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetGroupsPaginatorBase = Paginator[ListDatasetGroupsResponseTypeDef]
else:
    _ListDatasetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetGroupsPaginator(_ListDatasetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetGroups.html#Personalize.Paginator.ListDatasetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetGroups.html#Personalize.Paginator.ListDatasetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetgroupspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetImportJobsPaginatorBase = Paginator[ListDatasetImportJobsResponseTypeDef]
else:
    _ListDatasetImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetImportJobsPaginator(_ListDatasetImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetImportJobs.html#Personalize.Paginator.ListDatasetImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasetImportJobs.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasets.html#Personalize.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListDatasets.html#Personalize.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListEventTrackersPaginatorBase = Paginator[ListEventTrackersResponseTypeDef]
else:
    _ListEventTrackersPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventTrackersPaginator(_ListEventTrackersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListEventTrackers.html#Personalize.Paginator.ListEventTrackers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listeventtrackerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventTrackersRequestPaginateTypeDef]
    ) -> PageIterator[ListEventTrackersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListEventTrackers.html#Personalize.Paginator.ListEventTrackers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listeventtrackerspaginator)
        """

if TYPE_CHECKING:
    _ListFiltersPaginatorBase = Paginator[ListFiltersResponseTypeDef]
else:
    _ListFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class ListFiltersPaginator(_ListFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListFilters.html#Personalize.Paginator.ListFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFiltersRequestPaginateTypeDef]
    ) -> PageIterator[ListFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListFilters.html#Personalize.Paginator.ListFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listfilterspaginator)
        """

if TYPE_CHECKING:
    _ListMetricAttributionMetricsPaginatorBase = Paginator[
        ListMetricAttributionMetricsResponseTypeDef
    ]
else:
    _ListMetricAttributionMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMetricAttributionMetricsPaginator(_ListMetricAttributionMetricsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListMetricAttributionMetrics.html#Personalize.Paginator.ListMetricAttributionMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listmetricattributionmetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMetricAttributionMetricsRequestPaginateTypeDef]
    ) -> PageIterator[ListMetricAttributionMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListMetricAttributionMetrics.html#Personalize.Paginator.ListMetricAttributionMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listmetricattributionmetricspaginator)
        """

if TYPE_CHECKING:
    _ListMetricAttributionsPaginatorBase = Paginator[ListMetricAttributionsResponseTypeDef]
else:
    _ListMetricAttributionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMetricAttributionsPaginator(_ListMetricAttributionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListMetricAttributions.html#Personalize.Paginator.ListMetricAttributions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listmetricattributionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMetricAttributionsRequestPaginateTypeDef]
    ) -> PageIterator[ListMetricAttributionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListMetricAttributions.html#Personalize.Paginator.ListMetricAttributions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listmetricattributionspaginator)
        """

if TYPE_CHECKING:
    _ListRecipesPaginatorBase = Paginator[ListRecipesResponseTypeDef]
else:
    _ListRecipesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecipesPaginator(_ListRecipesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListRecipes.html#Personalize.Paginator.ListRecipes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listrecipespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecipesRequestPaginateTypeDef]
    ) -> PageIterator[ListRecipesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListRecipes.html#Personalize.Paginator.ListRecipes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listrecipespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendersPaginatorBase = Paginator[ListRecommendersResponseTypeDef]
else:
    _ListRecommendersPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendersPaginator(_ListRecommendersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListRecommenders.html#Personalize.Paginator.ListRecommenders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listrecommenderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendersRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListRecommenders.html#Personalize.Paginator.ListRecommenders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listrecommenderspaginator)
        """

if TYPE_CHECKING:
    _ListSchemasPaginatorBase = Paginator[ListSchemasResponseTypeDef]
else:
    _ListSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemasPaginator(_ListSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSchemas.html#Personalize.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemasRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSchemas.html#Personalize.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listschemaspaginator)
        """

if TYPE_CHECKING:
    _ListSolutionVersionsPaginatorBase = Paginator[ListSolutionVersionsResponseTypeDef]
else:
    _ListSolutionVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolutionVersionsPaginator(_ListSolutionVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSolutionVersions.html#Personalize.Paginator.ListSolutionVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listsolutionversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolutionVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSolutionVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSolutionVersions.html#Personalize.Paginator.ListSolutionVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listsolutionversionspaginator)
        """

if TYPE_CHECKING:
    _ListSolutionsPaginatorBase = Paginator[ListSolutionsResponseTypeDef]
else:
    _ListSolutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSolutionsPaginator(_ListSolutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSolutions.html#Personalize.Paginator.ListSolutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listsolutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSolutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSolutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/paginator/ListSolutions.html#Personalize.Paginator.ListSolutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators/#listsolutionspaginator)
        """
