"""
Type annotations for personalize service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize import PersonalizeClient

    client: PersonalizeClient = boto3.client("personalize")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import DomainType, ImportModeType, IngestionModeType, TrainingModeType
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
    BatchInferenceJobConfigTypeDef,
    BatchInferenceJobInputTypeDef,
    BatchInferenceJobOutputTypeDef,
    BatchSegmentJobInputTypeDef,
    BatchSegmentJobOutputTypeDef,
    CampaignConfigTypeDef,
    CreateBatchInferenceJobResponseTypeDef,
    CreateBatchSegmentJobResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDatasetExportJobResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateEventTrackerResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateMetricAttributionResponseTypeDef,
    CreateRecommenderResponseTypeDef,
    CreateSchemaResponseTypeDef,
    CreateSolutionResponseTypeDef,
    CreateSolutionVersionResponseTypeDef,
    DatasetExportJobOutputTypeDef,
    DataSourceTypeDef,
    DescribeAlgorithmResponseTypeDef,
    DescribeBatchInferenceJobResponseTypeDef,
    DescribeBatchSegmentJobResponseTypeDef,
    DescribeCampaignResponseTypeDef,
    DescribeDatasetExportJobResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeEventTrackerResponseTypeDef,
    DescribeFeatureTransformationResponseTypeDef,
    DescribeFilterResponseTypeDef,
    DescribeMetricAttributionResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeRecommenderResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    DescribeSolutionResponseTypeDef,
    DescribeSolutionVersionResponseTypeDef,
    GetSolutionMetricsResponseTypeDef,
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
    ListTagsForResourceResponseTypeDef,
    MetricAttributeTypeDef,
    MetricAttributionOutputTypeDef,
    RecommenderConfigTypeDef,
    SolutionConfigTypeDef,
    StartRecommenderResponseTypeDef,
    StopRecommenderResponseTypeDef,
    TagTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateMetricAttributionResponseTypeDef,
    UpdateRecommenderResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PersonalizeClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#close)
        """
    def create_batch_inference_job(
        self,
        *,
        jobName: str,
        solutionVersionArn: str,
        jobInput: "BatchInferenceJobInputTypeDef",
        jobOutput: "BatchInferenceJobOutputTypeDef",
        roleArn: str,
        filterArn: str = None,
        numResults: int = None,
        batchInferenceJobConfig: "BatchInferenceJobConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateBatchInferenceJobResponseTypeDef:
        """
        Creates a batch inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_batch_inference_job)
        """
    def create_batch_segment_job(
        self,
        *,
        jobName: str,
        solutionVersionArn: str,
        jobInput: "BatchSegmentJobInputTypeDef",
        jobOutput: "BatchSegmentJobOutputTypeDef",
        roleArn: str,
        filterArn: str = None,
        numResults: int = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateBatchSegmentJobResponseTypeDef:
        """
        Creates a batch segment job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_batch_segment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_batch_segment_job)
        """
    def create_campaign(
        self,
        *,
        name: str,
        solutionVersionArn: str,
        minProvisionedTPS: int = None,
        campaignConfig: "CampaignConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCampaignResponseTypeDef:
        """
        Creates a campaign that deploys a solution version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_campaign)
        """
    def create_dataset(
        self,
        *,
        name: str,
        schemaArn: str,
        datasetGroupArn: str,
        datasetType: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates an empty dataset and adds it to the specified dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset)
        """
    def create_dataset_export_job(
        self,
        *,
        jobName: str,
        datasetArn: str,
        roleArn: str,
        jobOutput: "DatasetExportJobOutputTypeDef",
        ingestionMode: IngestionModeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDatasetExportJobResponseTypeDef:
        """
        Creates a job that exports data from your dataset to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_dataset_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_export_job)
        """
    def create_dataset_group(
        self,
        *,
        name: str,
        roleArn: str = None,
        kmsKeyArn: str = None,
        domain: DomainType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        Creates an empty dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_group)
        """
    def create_dataset_import_job(
        self,
        *,
        jobName: str,
        datasetArn: str,
        dataSource: "DataSourceTypeDef",
        roleArn: str,
        tags: List["TagTypeDef"] = None,
        importMode: ImportModeType = None,
        publishAttributionMetricsToS3: bool = None
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Creates a job that imports training data from your data source (an Amazon S3
        bucket) to an Amazon Personalize dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_import_job)
        """
    def create_event_tracker(
        self, *, name: str, datasetGroupArn: str, tags: List["TagTypeDef"] = None
    ) -> CreateEventTrackerResponseTypeDef:
        """
        Creates an event tracker that you use when adding event data to a specified
        dataset group using the `PutEvents
        <https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html>`__
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_event_tracker)
        """
    def create_filter(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        filterExpression: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a recommendation filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_filter)
        """
    def create_metric_attribution(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        metrics: List["MetricAttributeTypeDef"],
        metricsOutputConfig: "MetricAttributionOutputTypeDef"
    ) -> CreateMetricAttributionResponseTypeDef:
        """
        Creates a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_metric_attribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_metric_attribution)
        """
    def create_recommender(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        recipeArn: str,
        recommenderConfig: "RecommenderConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRecommenderResponseTypeDef:
        """
        Creates a recommender with the recipe (a Domain dataset group use case) you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_recommender)
        """
    def create_schema(
        self, *, name: str, schema: str, domain: DomainType = None
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates an Amazon Personalize schema from the specified schema string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_schema)
        """
    def create_solution(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: "SolutionConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateSolutionResponseTypeDef:
        """
        Creates the configuration for training a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_solution)
        """
    def create_solution_version(
        self,
        *,
        solutionArn: str,
        name: str = None,
        trainingMode: TrainingModeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateSolutionVersionResponseTypeDef:
        """
        Trains or retrains an active solution in a Custom dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.create_solution_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_solution_version)
        """
    def delete_campaign(self, *, campaignArn: str) -> None:
        """
        Removes a campaign by deleting the solution deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_campaign)
        """
    def delete_dataset(self, *, datasetArn: str) -> None:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_dataset)
        """
    def delete_dataset_group(self, *, datasetGroupArn: str) -> None:
        """
        Deletes a dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_dataset_group)
        """
    def delete_event_tracker(self, *, eventTrackerArn: str) -> None:
        """
        Deletes the event tracker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_event_tracker)
        """
    def delete_filter(self, *, filterArn: str) -> None:
        """
        Deletes a filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_filter)
        """
    def delete_metric_attribution(self, *, metricAttributionArn: str) -> None:
        """
        Deletes a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_metric_attribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_metric_attribution)
        """
    def delete_recommender(self, *, recommenderArn: str) -> None:
        """
        Deactivates and removes a recommender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_recommender)
        """
    def delete_schema(self, *, schemaArn: str) -> None:
        """
        Deletes a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_schema)
        """
    def delete_solution(self, *, solutionArn: str) -> None:
        """
        Deletes all versions of a solution and the `Solution` object itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.delete_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_solution)
        """
    def describe_algorithm(self, *, algorithmArn: str) -> DescribeAlgorithmResponseTypeDef:
        """
        Describes the given algorithm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_algorithm)
        """
    def describe_batch_inference_job(
        self, *, batchInferenceJobArn: str
    ) -> DescribeBatchInferenceJobResponseTypeDef:
        """
        Gets the properties of a batch inference job including name, Amazon Resource
        Name (ARN), status, input and output configurations, and the ARN of the solution
        version used to generate the recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_batch_inference_job)
        """
    def describe_batch_segment_job(
        self, *, batchSegmentJobArn: str
    ) -> DescribeBatchSegmentJobResponseTypeDef:
        """
        Gets the properties of a batch segment job including name, Amazon Resource Name
        (ARN), status, input and output configurations, and the ARN of the solution
        version used to generate segments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_batch_segment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_batch_segment_job)
        """
    def describe_campaign(self, *, campaignArn: str) -> DescribeCampaignResponseTypeDef:
        """
        Describes the given campaign, including its status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_campaign)
        """
    def describe_dataset(self, *, datasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Describes the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset)
        """
    def describe_dataset_export_job(
        self, *, datasetExportJobArn: str
    ) -> DescribeDatasetExportJobResponseTypeDef:
        """
        Describes the dataset export job created by `CreateDatasetExportJob <https://doc
        s.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html>`__,
        including the export job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_dataset_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_export_job)
        """
    def describe_dataset_group(
        self, *, datasetGroupArn: str
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes the given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_group)
        """
    def describe_dataset_import_job(
        self, *, datasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes the dataset import job created by `CreateDatasetImportJob <https://doc
        s.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html>`__,
        including the import job status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_import_job)
        """
    def describe_event_tracker(
        self, *, eventTrackerArn: str
    ) -> DescribeEventTrackerResponseTypeDef:
        """
        Describes an event tracker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_event_tracker)
        """
    def describe_feature_transformation(
        self, *, featureTransformationArn: str
    ) -> DescribeFeatureTransformationResponseTypeDef:
        """
        Describes the given feature transformation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_feature_transformation)
        """
    def describe_filter(self, *, filterArn: str) -> DescribeFilterResponseTypeDef:
        """
        Describes a filter's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_filter)
        """
    def describe_metric_attribution(
        self, *, metricAttributionArn: str
    ) -> DescribeMetricAttributionResponseTypeDef:
        """
        Describes a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_metric_attribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_metric_attribution)
        """
    def describe_recipe(self, *, recipeArn: str) -> DescribeRecipeResponseTypeDef:
        """
        Describes a recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_recipe)
        """
    def describe_recommender(self, *, recommenderArn: str) -> DescribeRecommenderResponseTypeDef:
        """
        Describes the given recommender, including its status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_recommender)
        """
    def describe_schema(self, *, schemaArn: str) -> DescribeSchemaResponseTypeDef:
        """
        Describes a schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_schema)
        """
    def describe_solution(self, *, solutionArn: str) -> DescribeSolutionResponseTypeDef:
        """
        Describes a solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_solution)
        """
    def describe_solution_version(
        self, *, solutionVersionArn: str
    ) -> DescribeSolutionVersionResponseTypeDef:
        """
        Describes a specific version of a solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.describe_solution_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_solution_version)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#generate_presigned_url)
        """
    def get_solution_metrics(self, *, solutionVersionArn: str) -> GetSolutionMetricsResponseTypeDef:
        """
        Gets the metrics for the specified solution version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.get_solution_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#get_solution_metrics)
        """
    def list_batch_inference_jobs(
        self, *, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        Gets a list of the batch inference jobs that have been performed off of a
        solution version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_batch_inference_jobs)
        """
    def list_batch_segment_jobs(
        self, *, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBatchSegmentJobsResponseTypeDef:
        """
        Gets a list of the batch segment jobs that have been performed off of a solution
        version that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_batch_segment_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_batch_segment_jobs)
        """
    def list_campaigns(
        self, *, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListCampaignsResponseTypeDef:
        """
        Returns a list of campaigns that use the given solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_campaigns)
        """
    def list_dataset_export_jobs(
        self, *, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetExportJobsResponseTypeDef:
        """
        Returns a list of dataset export jobs that use the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_dataset_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_export_jobs)
        """
    def list_dataset_groups(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_dataset_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_groups)
        """
    def list_dataset_import_jobs(
        self, *, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        Returns a list of dataset import jobs that use the given dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_import_jobs)
        """
    def list_datasets(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns the list of datasets contained in the given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_datasets)
        """
    def list_event_trackers(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventTrackersResponseTypeDef:
        """
        Returns the list of event trackers associated with the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_event_trackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_event_trackers)
        """
    def list_filters(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListFiltersResponseTypeDef:
        """
        Lists all filters that belong to a given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_filters)
        """
    def list_metric_attribution_metrics(
        self, *, metricAttributionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListMetricAttributionMetricsResponseTypeDef:
        """
        Lists the metrics for the metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_metric_attribution_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_metric_attribution_metrics)
        """
    def list_metric_attributions(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListMetricAttributionsResponseTypeDef:
        """
        Lists metric attributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_metric_attributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_metric_attributions)
        """
    def list_recipes(
        self,
        *,
        recipeProvider: Literal["SERVICE"] = None,
        nextToken: str = None,
        maxResults: int = None,
        domain: DomainType = None
    ) -> ListRecipesResponseTypeDef:
        """
        Returns a list of available recipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_recipes)
        """
    def list_recommenders(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListRecommendersResponseTypeDef:
        """
        Returns a list of recommenders in a given Domain dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_recommenders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_recommenders)
        """
    def list_schemas(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListSchemasResponseTypeDef:
        """
        Returns the list of schemas associated with the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_schemas)
        """
    def list_solution_versions(
        self, *, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        Returns a list of solution versions for the given solution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_solution_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_solution_versions)
        """
    def list_solutions(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionsResponseTypeDef:
        """
        Returns a list of solutions that use the given dataset group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_solutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_solutions)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Get a list of `tags <https://docs.aws.amazon.com/personalize/latest/dev/tagging-
        resources.html>`__ attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_tags_for_resource)
        """
    def start_recommender(self, *, recommenderArn: str) -> StartRecommenderResponseTypeDef:
        """
        Starts a recommender that is INACTIVE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.start_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#start_recommender)
        """
    def stop_recommender(self, *, recommenderArn: str) -> StopRecommenderResponseTypeDef:
        """
        Stops a recommender that is ACTIVE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.stop_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#stop_recommender)
        """
    def stop_solution_version_creation(self, *, solutionVersionArn: str) -> None:
        """
        Stops creating a solution version that is in a state of CREATE_PENDING or CREATE
        IN_PROGRESS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.stop_solution_version_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#stop_solution_version_creation)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add a list of tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove `tags <https://docs.aws.amazon.com/personalize/latest/dev/tagging-
        resources.html>`__ that are attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#untag_resource)
        """
    def update_campaign(
        self,
        *,
        campaignArn: str,
        solutionVersionArn: str = None,
        minProvisionedTPS: int = None,
        campaignConfig: "CampaignConfigTypeDef" = None
    ) -> UpdateCampaignResponseTypeDef:
        """
        Updates a campaign by either deploying a new solution or changing the value of
        the campaign's `minProvisionedTPS` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.update_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#update_campaign)
        """
    def update_metric_attribution(
        self,
        *,
        addMetrics: List["MetricAttributeTypeDef"] = None,
        removeMetrics: List[str] = None,
        metricsOutputConfig: "MetricAttributionOutputTypeDef" = None,
        metricAttributionArn: str = None
    ) -> UpdateMetricAttributionResponseTypeDef:
        """
        Updates a metric attribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.update_metric_attribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#update_metric_attribution)
        """
    def update_recommender(
        self, *, recommenderArn: str, recommenderConfig: "RecommenderConfigTypeDef"
    ) -> UpdateRecommenderResponseTypeDef:
        """
        Updates the recommender to modify the recommender configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Client.update_recommender)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#update_recommender)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_inference_jobs"]
    ) -> ListBatchInferenceJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchinferencejobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_segment_jobs"]
    ) -> ListBatchSegmentJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListBatchSegmentJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchsegmentjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_campaigns"]) -> ListCampaignsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listcampaignspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_export_jobs"]
    ) -> ListDatasetExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetexportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetimportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_trackers"]
    ) -> ListEventTrackersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listeventtrackerspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listfilterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_metric_attribution_metrics"]
    ) -> ListMetricAttributionMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributionMetrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionmetricspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_metric_attributions"]
    ) -> ListMetricAttributionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListMetricAttributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listmetricattributionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecipespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommenders"]
    ) -> ListRecommendersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListRecommenders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecommenderspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listschemaspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_solution_versions"]
    ) -> ListSolutionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_solutions"]) -> ListSolutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionspaginator)
        """
