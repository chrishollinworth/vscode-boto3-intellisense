"""
Type annotations for personalize service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_personalize.client import PersonalizeClient

    session = Session()
    client: PersonalizeClient = session.client("personalize")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
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
    ListSolutionsPaginator,
    ListSolutionVersionsPaginator,
)
from .type_defs import (
    CreateBatchInferenceJobRequestTypeDef,
    CreateBatchInferenceJobResponseTypeDef,
    CreateBatchSegmentJobRequestTypeDef,
    CreateBatchSegmentJobResponseTypeDef,
    CreateCampaignRequestTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDataDeletionJobRequestTypeDef,
    CreateDataDeletionJobResponseTypeDef,
    CreateDatasetExportJobRequestTypeDef,
    CreateDatasetExportJobResponseTypeDef,
    CreateDatasetGroupRequestTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobRequestTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateEventTrackerRequestTypeDef,
    CreateEventTrackerResponseTypeDef,
    CreateFilterRequestTypeDef,
    CreateFilterResponseTypeDef,
    CreateMetricAttributionRequestTypeDef,
    CreateMetricAttributionResponseTypeDef,
    CreateRecommenderRequestTypeDef,
    CreateRecommenderResponseTypeDef,
    CreateSchemaRequestTypeDef,
    CreateSchemaResponseTypeDef,
    CreateSolutionRequestTypeDef,
    CreateSolutionResponseTypeDef,
    CreateSolutionVersionRequestTypeDef,
    CreateSolutionVersionResponseTypeDef,
    DeleteCampaignRequestTypeDef,
    DeleteDatasetGroupRequestTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteEventTrackerRequestTypeDef,
    DeleteFilterRequestTypeDef,
    DeleteMetricAttributionRequestTypeDef,
    DeleteRecommenderRequestTypeDef,
    DeleteSchemaRequestTypeDef,
    DeleteSolutionRequestTypeDef,
    DescribeAlgorithmRequestTypeDef,
    DescribeAlgorithmResponseTypeDef,
    DescribeBatchInferenceJobRequestTypeDef,
    DescribeBatchInferenceJobResponseTypeDef,
    DescribeBatchSegmentJobRequestTypeDef,
    DescribeBatchSegmentJobResponseTypeDef,
    DescribeCampaignRequestTypeDef,
    DescribeCampaignResponseTypeDef,
    DescribeDataDeletionJobRequestTypeDef,
    DescribeDataDeletionJobResponseTypeDef,
    DescribeDatasetExportJobRequestTypeDef,
    DescribeDatasetExportJobResponseTypeDef,
    DescribeDatasetGroupRequestTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobRequestTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeEventTrackerRequestTypeDef,
    DescribeEventTrackerResponseTypeDef,
    DescribeFeatureTransformationRequestTypeDef,
    DescribeFeatureTransformationResponseTypeDef,
    DescribeFilterRequestTypeDef,
    DescribeFilterResponseTypeDef,
    DescribeMetricAttributionRequestTypeDef,
    DescribeMetricAttributionResponseTypeDef,
    DescribeRecipeRequestTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeRecommenderRequestTypeDef,
    DescribeRecommenderResponseTypeDef,
    DescribeSchemaRequestTypeDef,
    DescribeSchemaResponseTypeDef,
    DescribeSolutionRequestTypeDef,
    DescribeSolutionResponseTypeDef,
    DescribeSolutionVersionRequestTypeDef,
    DescribeSolutionVersionResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetSolutionMetricsRequestTypeDef,
    GetSolutionMetricsResponseTypeDef,
    ListBatchInferenceJobsRequestTypeDef,
    ListBatchInferenceJobsResponseTypeDef,
    ListBatchSegmentJobsRequestTypeDef,
    ListBatchSegmentJobsResponseTypeDef,
    ListCampaignsRequestTypeDef,
    ListCampaignsResponseTypeDef,
    ListDataDeletionJobsRequestTypeDef,
    ListDataDeletionJobsResponseTypeDef,
    ListDatasetExportJobsRequestTypeDef,
    ListDatasetExportJobsResponseTypeDef,
    ListDatasetGroupsRequestTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsRequestTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersRequestTypeDef,
    ListEventTrackersResponseTypeDef,
    ListFiltersRequestTypeDef,
    ListFiltersResponseTypeDef,
    ListMetricAttributionMetricsRequestTypeDef,
    ListMetricAttributionMetricsResponseTypeDef,
    ListMetricAttributionsRequestTypeDef,
    ListMetricAttributionsResponseTypeDef,
    ListRecipesRequestTypeDef,
    ListRecipesResponseTypeDef,
    ListRecommendersRequestTypeDef,
    ListRecommendersResponseTypeDef,
    ListSchemasRequestTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionsRequestTypeDef,
    ListSolutionsResponseTypeDef,
    ListSolutionVersionsRequestTypeDef,
    ListSolutionVersionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartRecommenderRequestTypeDef,
    StartRecommenderResponseTypeDef,
    StopRecommenderRequestTypeDef,
    StopRecommenderResponseTypeDef,
    StopSolutionVersionCreationRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCampaignRequestTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateDatasetRequestTypeDef,
    UpdateDatasetResponseTypeDef,
    UpdateMetricAttributionRequestTypeDef,
    UpdateMetricAttributionResponseTypeDef,
    UpdateRecommenderRequestTypeDef,
    UpdateRecommenderResponseTypeDef,
    UpdateSolutionRequestTypeDef,
    UpdateSolutionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("PersonalizeClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class PersonalizeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#generate_presigned_url)
        """

    def create_batch_inference_job(
        self, **kwargs: Unpack[CreateBatchInferenceJobRequestTypeDef]
    ) -> CreateBatchInferenceJobResponseTypeDef:
        """
        Generates batch recommendations based on a list of items or users stored in
        Amazon S3 and exports the recommendations to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_batch_inference_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_batch_inference_job)
        """

    def create_batch_segment_job(
        self, **kwargs: Unpack[CreateBatchSegmentJobRequestTypeDef]
    ) -> CreateBatchSegmentJobResponseTypeDef:
        """
        Creates a batch segment job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_batch_segment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_batch_segment_job)
        """

    def create_campaign(
        self, **kwargs: Unpack[CreateCampaignRequestTypeDef]
    ) -> CreateCampaignResponseTypeDef:
        """
        You incur campaign costs while it is active.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_campaign)
        """

    def create_data_deletion_job(
        self, **kwargs: Unpack[CreateDataDeletionJobRequestTypeDef]
    ) -> CreateDataDeletionJobResponseTypeDef:
        """
        Creates a batch job that deletes all references to specific users from an
        Amazon Personalize dataset group in batches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_data_deletion_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_data_deletion_job)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates an empty dataset and adds it to the specified dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_dataset)
        """

    def create_dataset_export_job(
        self, **kwargs: Unpack[CreateDatasetExportJobRequestTypeDef]
    ) -> CreateDatasetExportJobResponseTypeDef:
        """
        Creates a job that exports data from your dataset to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_dataset_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_dataset_export_job)
        """

    def create_dataset_group(
        self, **kwargs: Unpack[CreateDatasetGroupRequestTypeDef]
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        Creates an empty dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_dataset_group)
        """

    def create_dataset_import_job(
        self, **kwargs: Unpack[CreateDatasetImportJobRequestTypeDef]
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Creates a job that imports training data from your data source (an Amazon S3
        bucket) to an Amazon Personalize dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_dataset_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_dataset_import_job)
        """

    def create_event_tracker(
        self, **kwargs: Unpack[CreateEventTrackerRequestTypeDef]
    ) -> CreateEventTrackerResponseTypeDef:
        """
        Creates an event tracker that you use when adding event data to a specified
        dataset group using the <a
        href="https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html">PutEvents</a>
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_event_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_event_tracker)
        """

    def create_filter(
        self, **kwargs: Unpack[CreateFilterRequestTypeDef]
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a recommendation filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_filter)
        """

    def create_metric_attribution(
        self, **kwargs: Unpack[CreateMetricAttributionRequestTypeDef]
    ) -> CreateMetricAttributionResponseTypeDef:
        """
        Creates a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_metric_attribution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_metric_attribution)
        """

    def create_recommender(
        self, **kwargs: Unpack[CreateRecommenderRequestTypeDef]
    ) -> CreateRecommenderResponseTypeDef:
        """
        Creates a recommender with the recipe (a Domain dataset group use case) you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_recommender)
        """

    def create_schema(
        self, **kwargs: Unpack[CreateSchemaRequestTypeDef]
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates an Amazon Personalize schema from the specified schema string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_schema)
        """

    def create_solution(
        self, **kwargs: Unpack[CreateSolutionRequestTypeDef]
    ) -> CreateSolutionResponseTypeDef:
        """
        By default, all new solutions use automatic training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_solution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_solution)
        """

    def create_solution_version(
        self, **kwargs: Unpack[CreateSolutionVersionRequestTypeDef]
    ) -> CreateSolutionVersionResponseTypeDef:
        """
        Trains or retrains an active solution in a Custom dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/create_solution_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#create_solution_version)
        """

    def delete_campaign(
        self, **kwargs: Unpack[DeleteCampaignRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a campaign by deleting the solution deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_campaign)
        """

    def delete_dataset(
        self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_dataset)
        """

    def delete_dataset_group(
        self, **kwargs: Unpack[DeleteDatasetGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_dataset_group)
        """

    def delete_event_tracker(
        self, **kwargs: Unpack[DeleteEventTrackerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the event tracker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_event_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_event_tracker)
        """

    def delete_filter(
        self, **kwargs: Unpack[DeleteFilterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_filter)
        """

    def delete_metric_attribution(
        self, **kwargs: Unpack[DeleteMetricAttributionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_metric_attribution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_metric_attribution)
        """

    def delete_recommender(
        self, **kwargs: Unpack[DeleteRecommenderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deactivates and removes a recommender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_recommender)
        """

    def delete_schema(
        self, **kwargs: Unpack[DeleteSchemaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_schema)
        """

    def delete_solution(
        self, **kwargs: Unpack[DeleteSolutionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all versions of a solution and the <code>Solution</code> object itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/delete_solution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#delete_solution)
        """

    def describe_algorithm(
        self, **kwargs: Unpack[DescribeAlgorithmRequestTypeDef]
    ) -> DescribeAlgorithmResponseTypeDef:
        """
        Describes the given algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_algorithm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_algorithm)
        """

    def describe_batch_inference_job(
        self, **kwargs: Unpack[DescribeBatchInferenceJobRequestTypeDef]
    ) -> DescribeBatchInferenceJobResponseTypeDef:
        """
        Gets the properties of a batch inference job including name, Amazon Resource
        Name (ARN), status, input and output configurations, and the ARN of the
        solution version used to generate the recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_batch_inference_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_batch_inference_job)
        """

    def describe_batch_segment_job(
        self, **kwargs: Unpack[DescribeBatchSegmentJobRequestTypeDef]
    ) -> DescribeBatchSegmentJobResponseTypeDef:
        """
        Gets the properties of a batch segment job including name, Amazon Resource Name
        (ARN), status, input and output configurations, and the ARN of the solution
        version used to generate segments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_batch_segment_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_batch_segment_job)
        """

    def describe_campaign(
        self, **kwargs: Unpack[DescribeCampaignRequestTypeDef]
    ) -> DescribeCampaignResponseTypeDef:
        """
        Describes the given campaign, including its status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_campaign)
        """

    def describe_data_deletion_job(
        self, **kwargs: Unpack[DescribeDataDeletionJobRequestTypeDef]
    ) -> DescribeDataDeletionJobResponseTypeDef:
        """
        Describes the data deletion job created by <a
        href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataDeletionJob.html">CreateDataDeletionJob</a>,
        including the job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_data_deletion_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_data_deletion_job)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Describes the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_dataset)
        """

    def describe_dataset_export_job(
        self, **kwargs: Unpack[DescribeDatasetExportJobRequestTypeDef]
    ) -> DescribeDatasetExportJobResponseTypeDef:
        """
        Describes the dataset export job created by <a
        href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html">CreateDatasetExportJob</a>,
        including the export job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_dataset_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_dataset_export_job)
        """

    def describe_dataset_group(
        self, **kwargs: Unpack[DescribeDatasetGroupRequestTypeDef]
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes the given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, **kwargs: Unpack[DescribeDatasetImportJobRequestTypeDef]
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes the dataset import job created by <a
        href="https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>,
        including the import job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_dataset_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_dataset_import_job)
        """

    def describe_event_tracker(
        self, **kwargs: Unpack[DescribeEventTrackerRequestTypeDef]
    ) -> DescribeEventTrackerResponseTypeDef:
        """
        Describes an event tracker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_event_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_event_tracker)
        """

    def describe_feature_transformation(
        self, **kwargs: Unpack[DescribeFeatureTransformationRequestTypeDef]
    ) -> DescribeFeatureTransformationResponseTypeDef:
        """
        Describes the given feature transformation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_feature_transformation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_feature_transformation)
        """

    def describe_filter(
        self, **kwargs: Unpack[DescribeFilterRequestTypeDef]
    ) -> DescribeFilterResponseTypeDef:
        """
        Describes a filter's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_filter)
        """

    def describe_metric_attribution(
        self, **kwargs: Unpack[DescribeMetricAttributionRequestTypeDef]
    ) -> DescribeMetricAttributionResponseTypeDef:
        """
        Describes a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_metric_attribution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_metric_attribution)
        """

    def describe_recipe(
        self, **kwargs: Unpack[DescribeRecipeRequestTypeDef]
    ) -> DescribeRecipeResponseTypeDef:
        """
        Describes a recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_recipe.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_recipe)
        """

    def describe_recommender(
        self, **kwargs: Unpack[DescribeRecommenderRequestTypeDef]
    ) -> DescribeRecommenderResponseTypeDef:
        """
        Describes the given recommender, including its status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_recommender)
        """

    def describe_schema(
        self, **kwargs: Unpack[DescribeSchemaRequestTypeDef]
    ) -> DescribeSchemaResponseTypeDef:
        """
        Describes a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_schema)
        """

    def describe_solution(
        self, **kwargs: Unpack[DescribeSolutionRequestTypeDef]
    ) -> DescribeSolutionResponseTypeDef:
        """
        Describes a solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_solution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_solution)
        """

    def describe_solution_version(
        self, **kwargs: Unpack[DescribeSolutionVersionRequestTypeDef]
    ) -> DescribeSolutionVersionResponseTypeDef:
        """
        Describes a specific version of a solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/describe_solution_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#describe_solution_version)
        """

    def get_solution_metrics(
        self, **kwargs: Unpack[GetSolutionMetricsRequestTypeDef]
    ) -> GetSolutionMetricsResponseTypeDef:
        """
        Gets the metrics for the specified solution version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_solution_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_solution_metrics)
        """

    def list_batch_inference_jobs(
        self, **kwargs: Unpack[ListBatchInferenceJobsRequestTypeDef]
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        Gets a list of the batch inference jobs that have been performed off of a
        solution version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_batch_inference_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_batch_inference_jobs)
        """

    def list_batch_segment_jobs(
        self, **kwargs: Unpack[ListBatchSegmentJobsRequestTypeDef]
    ) -> ListBatchSegmentJobsResponseTypeDef:
        """
        Gets a list of the batch segment jobs that have been performed off of a
        solution version that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_batch_segment_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_batch_segment_jobs)
        """

    def list_campaigns(
        self, **kwargs: Unpack[ListCampaignsRequestTypeDef]
    ) -> ListCampaignsResponseTypeDef:
        """
        Returns a list of campaigns that use the given solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_campaigns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_campaigns)
        """

    def list_data_deletion_jobs(
        self, **kwargs: Unpack[ListDataDeletionJobsRequestTypeDef]
    ) -> ListDataDeletionJobsResponseTypeDef:
        """
        Returns a list of data deletion jobs for a dataset group ordered by creation
        time, with the most recent first.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_data_deletion_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_data_deletion_jobs)
        """

    def list_dataset_export_jobs(
        self, **kwargs: Unpack[ListDatasetExportJobsRequestTypeDef]
    ) -> ListDatasetExportJobsResponseTypeDef:
        """
        Returns a list of dataset export jobs that use the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_dataset_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_dataset_export_jobs)
        """

    def list_dataset_groups(
        self, **kwargs: Unpack[ListDatasetGroupsRequestTypeDef]
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_dataset_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, **kwargs: Unpack[ListDatasetImportJobsRequestTypeDef]
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        Returns a list of dataset import jobs that use the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_dataset_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_dataset_import_jobs)
        """

    def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns the list of datasets contained in the given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_datasets)
        """

    def list_event_trackers(
        self, **kwargs: Unpack[ListEventTrackersRequestTypeDef]
    ) -> ListEventTrackersResponseTypeDef:
        """
        Returns the list of event trackers associated with the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_event_trackers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_event_trackers)
        """

    def list_filters(
        self, **kwargs: Unpack[ListFiltersRequestTypeDef]
    ) -> ListFiltersResponseTypeDef:
        """
        Lists all filters that belong to a given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_filters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_filters)
        """

    def list_metric_attribution_metrics(
        self, **kwargs: Unpack[ListMetricAttributionMetricsRequestTypeDef]
    ) -> ListMetricAttributionMetricsResponseTypeDef:
        """
        Lists the metrics for the metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_metric_attribution_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_metric_attribution_metrics)
        """

    def list_metric_attributions(
        self, **kwargs: Unpack[ListMetricAttributionsRequestTypeDef]
    ) -> ListMetricAttributionsResponseTypeDef:
        """
        Lists metric attributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_metric_attributions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_metric_attributions)
        """

    def list_recipes(
        self, **kwargs: Unpack[ListRecipesRequestTypeDef]
    ) -> ListRecipesResponseTypeDef:
        """
        Returns a list of available recipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_recipes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_recipes)
        """

    def list_recommenders(
        self, **kwargs: Unpack[ListRecommendersRequestTypeDef]
    ) -> ListRecommendersResponseTypeDef:
        """
        Returns a list of recommenders in a given Domain dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_recommenders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_recommenders)
        """

    def list_schemas(
        self, **kwargs: Unpack[ListSchemasRequestTypeDef]
    ) -> ListSchemasResponseTypeDef:
        """
        Returns the list of schemas associated with the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_schemas)
        """

    def list_solution_versions(
        self, **kwargs: Unpack[ListSolutionVersionsRequestTypeDef]
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        Returns a list of solution versions for the given solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_solution_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_solution_versions)
        """

    def list_solutions(
        self, **kwargs: Unpack[ListSolutionsRequestTypeDef]
    ) -> ListSolutionsResponseTypeDef:
        """
        Returns a list of solutions in a given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_solutions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_solutions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Get a list of <a
        href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a>
        attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#list_tags_for_resource)
        """

    def start_recommender(
        self, **kwargs: Unpack[StartRecommenderRequestTypeDef]
    ) -> StartRecommenderResponseTypeDef:
        """
        Starts a recommender that is INACTIVE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/start_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#start_recommender)
        """

    def stop_recommender(
        self, **kwargs: Unpack[StopRecommenderRequestTypeDef]
    ) -> StopRecommenderResponseTypeDef:
        """
        Stops a recommender that is ACTIVE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/stop_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#stop_recommender)
        """

    def stop_solution_version_creation(
        self, **kwargs: Unpack[StopSolutionVersionCreationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops creating a solution version that is in a state of CREATE_PENDING or
        CREATE IN_PROGRESS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/stop_solution_version_creation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#stop_solution_version_creation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add a list of tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags that are attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#untag_resource)
        """

    def update_campaign(
        self, **kwargs: Unpack[UpdateCampaignRequestTypeDef]
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates a campaign to deploy a retrained solution version with an existing
        campaign, change your campaign's <code>minProvisionedTPS</code>, or modify your
        campaign's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/update_campaign.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#update_campaign)
        """

    def update_dataset(
        self, **kwargs: Unpack[UpdateDatasetRequestTypeDef]
    ) -> UpdateDatasetResponseTypeDef:
        """
        Update a dataset to replace its schema with a new or existing one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/update_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#update_dataset)
        """

    def update_metric_attribution(
        self, **kwargs: Unpack[UpdateMetricAttributionRequestTypeDef]
    ) -> UpdateMetricAttributionResponseTypeDef:
        """
        Updates a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/update_metric_attribution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#update_metric_attribution)
        """

    def update_recommender(
        self, **kwargs: Unpack[UpdateRecommenderRequestTypeDef]
    ) -> UpdateRecommenderResponseTypeDef:
        """
        Updates the recommender to modify the recommender configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/update_recommender.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#update_recommender)
        """

    def update_solution(
        self, **kwargs: Unpack[UpdateSolutionRequestTypeDef]
    ) -> UpdateSolutionResponseTypeDef:
        """
        Updates an Amazon Personalize solution to use a different automatic training
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/update_solution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#update_solution)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_batch_inference_jobs"]
    ) -> ListBatchInferenceJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_batch_segment_jobs"]
    ) -> ListBatchSegmentJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_campaigns"]
    ) -> ListCampaignsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_export_jobs"]
    ) -> ListDatasetExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datasets"]
    ) -> ListDatasetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_trackers"]
    ) -> ListEventTrackersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_filters"]
    ) -> ListFiltersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metric_attribution_metrics"]
    ) -> ListMetricAttributionMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metric_attributions"]
    ) -> ListMetricAttributionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recipes"]
    ) -> ListRecipesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommenders"]
    ) -> ListRecommendersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schemas"]
    ) -> ListSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_solution_versions"]
    ) -> ListSolutionVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_solutions"]
    ) -> ListSolutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize/client/#get_paginator)
        """
