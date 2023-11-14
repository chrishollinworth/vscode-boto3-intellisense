"""
Type annotations for personalize service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize.type_defs import AlgorithmImageTypeDef

    data: AlgorithmImageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DomainType,
    ImportModeType,
    IngestionModeType,
    ObjectiveSensitivityType,
    TrainingModeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlgorithmImageTypeDef",
    "AlgorithmTypeDef",
    "AutoMLConfigTypeDef",
    "AutoMLResultTypeDef",
    "BatchInferenceJobConfigTypeDef",
    "BatchInferenceJobInputTypeDef",
    "BatchInferenceJobOutputTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "BatchInferenceJobTypeDef",
    "BatchSegmentJobInputTypeDef",
    "BatchSegmentJobOutputTypeDef",
    "BatchSegmentJobSummaryTypeDef",
    "BatchSegmentJobTypeDef",
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "CreateBatchInferenceJobRequestRequestTypeDef",
    "CreateBatchInferenceJobResponseTypeDef",
    "CreateBatchSegmentJobRequestRequestTypeDef",
    "CreateBatchSegmentJobResponseTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDatasetExportJobRequestRequestTypeDef",
    "CreateDatasetExportJobResponseTypeDef",
    "CreateDatasetGroupRequestRequestTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobRequestRequestTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateEventTrackerRequestRequestTypeDef",
    "CreateEventTrackerResponseTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateMetricAttributionRequestRequestTypeDef",
    "CreateMetricAttributionResponseTypeDef",
    "CreateRecommenderRequestRequestTypeDef",
    "CreateRecommenderResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateSolutionRequestRequestTypeDef",
    "CreateSolutionResponseTypeDef",
    "CreateSolutionVersionRequestRequestTypeDef",
    "CreateSolutionVersionResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetExportJobOutputTypeDef",
    "DatasetExportJobSummaryTypeDef",
    "DatasetExportJobTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetGroupTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetImportJobTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTypeDef",
    "DatasetUpdateSummaryTypeDef",
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteEventTrackerRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteMetricAttributionRequestRequestTypeDef",
    "DeleteRecommenderRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSolutionRequestRequestTypeDef",
    "DescribeAlgorithmRequestRequestTypeDef",
    "DescribeAlgorithmResponseTypeDef",
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    "DescribeBatchInferenceJobResponseTypeDef",
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    "DescribeBatchSegmentJobResponseTypeDef",
    "DescribeCampaignRequestRequestTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DescribeDatasetExportJobRequestRequestTypeDef",
    "DescribeDatasetExportJobResponseTypeDef",
    "DescribeDatasetGroupRequestRequestTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobRequestRequestTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeEventTrackerRequestRequestTypeDef",
    "DescribeEventTrackerResponseTypeDef",
    "DescribeFeatureTransformationRequestRequestTypeDef",
    "DescribeFeatureTransformationResponseTypeDef",
    "DescribeFilterRequestRequestTypeDef",
    "DescribeFilterResponseTypeDef",
    "DescribeMetricAttributionRequestRequestTypeDef",
    "DescribeMetricAttributionResponseTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeRecommenderRequestRequestTypeDef",
    "DescribeRecommenderResponseTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DescribeSolutionRequestRequestTypeDef",
    "DescribeSolutionResponseTypeDef",
    "DescribeSolutionVersionRequestRequestTypeDef",
    "DescribeSolutionVersionResponseTypeDef",
    "EventTrackerSummaryTypeDef",
    "EventTrackerTypeDef",
    "FeatureTransformationTypeDef",
    "FilterSummaryTypeDef",
    "FilterTypeDef",
    "GetSolutionMetricsRequestRequestTypeDef",
    "GetSolutionMetricsResponseTypeDef",
    "HPOConfigTypeDef",
    "HPOObjectiveTypeDef",
    "HPOResourceConfigTypeDef",
    "HyperParameterRangesTypeDef",
    "IntegerHyperParameterRangeTypeDef",
    "ListBatchInferenceJobsRequestRequestTypeDef",
    "ListBatchInferenceJobsResponseTypeDef",
    "ListBatchSegmentJobsRequestRequestTypeDef",
    "ListBatchSegmentJobsResponseTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListDatasetExportJobsRequestRequestTypeDef",
    "ListDatasetExportJobsResponseTypeDef",
    "ListDatasetGroupsRequestRequestTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsRequestRequestTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListEventTrackersRequestRequestTypeDef",
    "ListEventTrackersResponseTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListMetricAttributionMetricsRequestRequestTypeDef",
    "ListMetricAttributionMetricsResponseTypeDef",
    "ListMetricAttributionsRequestRequestTypeDef",
    "ListMetricAttributionsResponseTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListRecommendersRequestRequestTypeDef",
    "ListRecommendersResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSolutionVersionsRequestRequestTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "ListSolutionsRequestRequestTypeDef",
    "ListSolutionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricAttributeTypeDef",
    "MetricAttributionOutputTypeDef",
    "MetricAttributionSummaryTypeDef",
    "MetricAttributionTypeDef",
    "OptimizationObjectiveTypeDef",
    "PaginatorConfigTypeDef",
    "RecipeSummaryTypeDef",
    "RecipeTypeDef",
    "RecommenderConfigTypeDef",
    "RecommenderSummaryTypeDef",
    "RecommenderTypeDef",
    "RecommenderUpdateSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataConfigTypeDef",
    "SolutionConfigTypeDef",
    "SolutionSummaryTypeDef",
    "SolutionTypeDef",
    "SolutionVersionSummaryTypeDef",
    "SolutionVersionTypeDef",
    "StartRecommenderRequestRequestTypeDef",
    "StartRecommenderResponseTypeDef",
    "StopRecommenderRequestRequestTypeDef",
    "StopRecommenderResponseTypeDef",
    "StopSolutionVersionCreationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrainingDataConfigTypeDef",
    "TunedHPOParamsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateMetricAttributionRequestRequestTypeDef",
    "UpdateMetricAttributionResponseTypeDef",
    "UpdateRecommenderRequestRequestTypeDef",
    "UpdateRecommenderResponseTypeDef",
)

_RequiredAlgorithmImageTypeDef = TypedDict(
    "_RequiredAlgorithmImageTypeDef",
    {
        "dockerURI": str,
    },
)
_OptionalAlgorithmImageTypeDef = TypedDict(
    "_OptionalAlgorithmImageTypeDef",
    {
        "name": str,
    },
    total=False,
)

class AlgorithmImageTypeDef(_RequiredAlgorithmImageTypeDef, _OptionalAlgorithmImageTypeDef):
    pass

AlgorithmTypeDef = TypedDict(
    "AlgorithmTypeDef",
    {
        "name": str,
        "algorithmArn": str,
        "algorithmImage": "AlgorithmImageTypeDef",
        "defaultHyperParameters": Dict[str, str],
        "defaultHyperParameterRanges": "DefaultHyperParameterRangesTypeDef",
        "defaultResourceConfig": Dict[str, str],
        "trainingInputMode": str,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

AutoMLConfigTypeDef = TypedDict(
    "AutoMLConfigTypeDef",
    {
        "metricName": str,
        "recipeList": List[str],
    },
    total=False,
)

AutoMLResultTypeDef = TypedDict(
    "AutoMLResultTypeDef",
    {
        "bestRecipeArn": str,
    },
    total=False,
)

BatchInferenceJobConfigTypeDef = TypedDict(
    "BatchInferenceJobConfigTypeDef",
    {
        "itemExplorationConfig": Dict[str, str],
    },
    total=False,
)

BatchInferenceJobInputTypeDef = TypedDict(
    "BatchInferenceJobInputTypeDef",
    {
        "s3DataSource": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobOutputTypeDef = TypedDict(
    "BatchInferenceJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobSummaryTypeDef = TypedDict(
    "BatchInferenceJobSummaryTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "solutionVersionArn": str,
    },
    total=False,
)

BatchInferenceJobTypeDef = TypedDict(
    "BatchInferenceJobTypeDef",
    {
        "jobName": str,
        "batchInferenceJobArn": str,
        "filterArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": "BatchInferenceJobInputTypeDef",
        "jobOutput": "BatchInferenceJobOutputTypeDef",
        "batchInferenceJobConfig": "BatchInferenceJobConfigTypeDef",
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BatchSegmentJobInputTypeDef = TypedDict(
    "BatchSegmentJobInputTypeDef",
    {
        "s3DataSource": "S3DataConfigTypeDef",
    },
)

BatchSegmentJobOutputTypeDef = TypedDict(
    "BatchSegmentJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

BatchSegmentJobSummaryTypeDef = TypedDict(
    "BatchSegmentJobSummaryTypeDef",
    {
        "batchSegmentJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "solutionVersionArn": str,
    },
    total=False,
)

BatchSegmentJobTypeDef = TypedDict(
    "BatchSegmentJobTypeDef",
    {
        "jobName": str,
        "batchSegmentJobArn": str,
        "filterArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": "BatchSegmentJobInputTypeDef",
        "jobOutput": "BatchSegmentJobOutputTypeDef",
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

CampaignConfigTypeDef = TypedDict(
    "CampaignConfigTypeDef",
    {
        "itemExplorationConfig": Dict[str, str],
    },
    total=False,
)

CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestCampaignUpdate": "CampaignUpdateSummaryTypeDef",
    },
    total=False,
)

CampaignUpdateSummaryTypeDef = TypedDict(
    "CampaignUpdateSummaryTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

CategoricalHyperParameterRangeTypeDef = TypedDict(
    "CategoricalHyperParameterRangeTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

ContinuousHyperParameterRangeTypeDef = TypedDict(
    "ContinuousHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": float,
        "maxValue": float,
    },
    total=False,
)

_RequiredCreateBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchInferenceJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": "BatchInferenceJobInputTypeDef",
        "jobOutput": "BatchInferenceJobOutputTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchInferenceJobRequestRequestTypeDef",
    {
        "filterArn": str,
        "numResults": int,
        "batchInferenceJobConfig": "BatchInferenceJobConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBatchInferenceJobRequestRequestTypeDef(
    _RequiredCreateBatchInferenceJobRequestRequestTypeDef,
    _OptionalCreateBatchInferenceJobRequestRequestTypeDef,
):
    pass

CreateBatchInferenceJobResponseTypeDef = TypedDict(
    "CreateBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchSegmentJobRequestRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": "BatchSegmentJobInputTypeDef",
        "jobOutput": "BatchSegmentJobOutputTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchSegmentJobRequestRequestTypeDef",
    {
        "filterArn": str,
        "numResults": int,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBatchSegmentJobRequestRequestTypeDef(
    _RequiredCreateBatchSegmentJobRequestRequestTypeDef,
    _OptionalCreateBatchSegmentJobRequestRequestTypeDef,
):
    pass

CreateBatchSegmentJobResponseTypeDef = TypedDict(
    "CreateBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "solutionVersionArn": str,
    },
)
_OptionalCreateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestRequestTypeDef",
    {
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCampaignRequestRequestTypeDef(
    _RequiredCreateCampaignRequestRequestTypeDef, _OptionalCreateCampaignRequestRequestTypeDef
):
    pass

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetExportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "roleArn": str,
        "jobOutput": "DatasetExportJobOutputTypeDef",
    },
)
_OptionalCreateDatasetExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetExportJobRequestRequestTypeDef",
    {
        "ingestionMode": IngestionModeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatasetExportJobRequestRequestTypeDef(
    _RequiredCreateDatasetExportJobRequestRequestTypeDef,
    _OptionalCreateDatasetExportJobRequestRequestTypeDef,
):
    pass

CreateDatasetExportJobResponseTypeDef = TypedDict(
    "CreateDatasetExportJobResponseTypeDef",
    {
        "datasetExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetGroupRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetGroupRequestRequestTypeDef",
    {
        "roleArn": str,
        "kmsKeyArn": str,
        "domain": DomainType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatasetGroupRequestRequestTypeDef(
    _RequiredCreateDatasetGroupRequestRequestTypeDef,
    _OptionalCreateDatasetGroupRequestRequestTypeDef,
):
    pass

CreateDatasetGroupResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseTypeDef",
    {
        "datasetGroupArn": str,
        "domain": DomainType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetImportJobRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "importMode": ImportModeType,
        "publishAttributionMetricsToS3": bool,
    },
    total=False,
)

class CreateDatasetImportJobRequestRequestTypeDef(
    _RequiredCreateDatasetImportJobRequestRequestTypeDef,
    _OptionalCreateDatasetImportJobRequestRequestTypeDef,
):
    pass

CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "datasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventTrackerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventTrackerRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)
_OptionalCreateEventTrackerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventTrackerRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEventTrackerRequestRequestTypeDef(
    _RequiredCreateEventTrackerRequestRequestTypeDef,
    _OptionalCreateEventTrackerRequestRequestTypeDef,
):
    pass

CreateEventTrackerResponseTypeDef = TypedDict(
    "CreateEventTrackerResponseTypeDef",
    {
        "eventTrackerArn": str,
        "trackingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFilterRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "filterExpression": str,
    },
)
_OptionalCreateFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFilterRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFilterRequestRequestTypeDef(
    _RequiredCreateFilterRequestRequestTypeDef, _OptionalCreateFilterRequestRequestTypeDef
):
    pass

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "filterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMetricAttributionRequestRequestTypeDef = TypedDict(
    "CreateMetricAttributionRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "metrics": List["MetricAttributeTypeDef"],
        "metricsOutputConfig": "MetricAttributionOutputTypeDef",
    },
)

CreateMetricAttributionResponseTypeDef = TypedDict(
    "CreateMetricAttributionResponseTypeDef",
    {
        "metricAttributionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecommenderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecommenderRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "recipeArn": str,
    },
)
_OptionalCreateRecommenderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecommenderRequestRequestTypeDef",
    {
        "recommenderConfig": "RecommenderConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRecommenderRequestRequestTypeDef(
    _RequiredCreateRecommenderRequestRequestTypeDef, _OptionalCreateRecommenderRequestRequestTypeDef
):
    pass

CreateRecommenderResponseTypeDef = TypedDict(
    "CreateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaRequestRequestTypeDef",
    {
        "name": str,
        "schema": str,
    },
)
_OptionalCreateSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaRequestRequestTypeDef",
    {
        "domain": DomainType,
    },
    total=False,
)

class CreateSchemaRequestRequestTypeDef(
    _RequiredCreateSchemaRequestRequestTypeDef, _OptionalCreateSchemaRequestRequestTypeDef
):
    pass

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "schemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSolutionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSolutionRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)
_OptionalCreateSolutionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSolutionRequestRequestTypeDef",
    {
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "solutionConfig": "SolutionConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSolutionRequestRequestTypeDef(
    _RequiredCreateSolutionRequestRequestTypeDef, _OptionalCreateSolutionRequestRequestTypeDef
):
    pass

CreateSolutionResponseTypeDef = TypedDict(
    "CreateSolutionResponseTypeDef",
    {
        "solutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSolutionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSolutionVersionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)
_OptionalCreateSolutionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSolutionVersionRequestRequestTypeDef",
    {
        "name": str,
        "trainingMode": TrainingModeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSolutionVersionRequestRequestTypeDef(
    _RequiredCreateSolutionVersionRequestRequestTypeDef,
    _OptionalCreateSolutionVersionRequestRequestTypeDef,
):
    pass

CreateSolutionVersionResponseTypeDef = TypedDict(
    "CreateSolutionVersionResponseTypeDef",
    {
        "solutionVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataLocation": str,
    },
    total=False,
)

DatasetExportJobOutputTypeDef = TypedDict(
    "DatasetExportJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

DatasetExportJobSummaryTypeDef = TypedDict(
    "DatasetExportJobSummaryTypeDef",
    {
        "datasetExportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetExportJobTypeDef = TypedDict(
    "DatasetExportJobTypeDef",
    {
        "jobName": str,
        "datasetExportJobArn": str,
        "datasetArn": str,
        "ingestionMode": IngestionModeType,
        "roleArn": str,
        "status": str,
        "jobOutput": "DatasetExportJobOutputTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "domain": DomainType,
    },
    total=False,
)

DatasetGroupTypeDef = TypedDict(
    "DatasetGroupTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "roleArn": str,
        "kmsKeyArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "domain": DomainType,
    },
    total=False,
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "importMode": ImportModeType,
    },
    total=False,
)

DatasetImportJobTypeDef = TypedDict(
    "DatasetImportJobTypeDef",
    {
        "jobName": str,
        "datasetImportJobArn": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "importMode": ImportModeType,
        "publishAttributionMetricsToS3": bool,
    },
    total=False,
)

DatasetSchemaSummaryTypeDef = TypedDict(
    "DatasetSchemaSummaryTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "domain": DomainType,
    },
    total=False,
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "schema": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "domain": DomainType,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "schemaArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestDatasetUpdate": "DatasetUpdateSummaryTypeDef",
    },
    total=False,
)

DatasetUpdateSummaryTypeDef = TypedDict(
    "DatasetUpdateSummaryTypeDef",
    {
        "schemaArn": str,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DefaultCategoricalHyperParameterRangeTypeDef = TypedDict(
    "DefaultCategoricalHyperParameterRangeTypeDef",
    {
        "name": str,
        "values": List[str],
        "isTunable": bool,
    },
    total=False,
)

DefaultContinuousHyperParameterRangeTypeDef = TypedDict(
    "DefaultContinuousHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": float,
        "maxValue": float,
        "isTunable": bool,
    },
    total=False,
)

DefaultHyperParameterRangesTypeDef = TypedDict(
    "DefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List["DefaultIntegerHyperParameterRangeTypeDef"],
        "continuousHyperParameterRanges": List["DefaultContinuousHyperParameterRangeTypeDef"],
        "categoricalHyperParameterRanges": List["DefaultCategoricalHyperParameterRangeTypeDef"],
    },
    total=False,
)

DefaultIntegerHyperParameterRangeTypeDef = TypedDict(
    "DefaultIntegerHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": int,
        "maxValue": int,
        "isTunable": bool,
    },
    total=False,
)

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DeleteDatasetGroupRequestRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DeleteEventTrackerRequestRequestTypeDef = TypedDict(
    "DeleteEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)

DeleteMetricAttributionRequestRequestTypeDef = TypedDict(
    "DeleteMetricAttributionRequestRequestTypeDef",
    {
        "metricAttributionArn": str,
    },
)

DeleteRecommenderRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DeleteSolutionRequestRequestTypeDef = TypedDict(
    "DeleteSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeAlgorithmRequestRequestTypeDef = TypedDict(
    "DescribeAlgorithmRequestRequestTypeDef",
    {
        "algorithmArn": str,
    },
)

DescribeAlgorithmResponseTypeDef = TypedDict(
    "DescribeAlgorithmResponseTypeDef",
    {
        "algorithm": "AlgorithmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    {
        "batchInferenceJobArn": str,
    },
)

DescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "DescribeBatchInferenceJobResponseTypeDef",
    {
        "batchInferenceJob": "BatchInferenceJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchSegmentJobRequestRequestTypeDef = TypedDict(
    "DescribeBatchSegmentJobRequestRequestTypeDef",
    {
        "batchSegmentJobArn": str,
    },
)

DescribeBatchSegmentJobResponseTypeDef = TypedDict(
    "DescribeBatchSegmentJobResponseTypeDef",
    {
        "batchSegmentJob": "BatchSegmentJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCampaignRequestRequestTypeDef = TypedDict(
    "DescribeCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DescribeCampaignResponseTypeDef = TypedDict(
    "DescribeCampaignResponseTypeDef",
    {
        "campaign": "CampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetExportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetExportJobRequestRequestTypeDef",
    {
        "datasetExportJobArn": str,
    },
)

DescribeDatasetExportJobResponseTypeDef = TypedDict(
    "DescribeDatasetExportJobResponseTypeDef",
    {
        "datasetExportJob": "DatasetExportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetGroupRequestRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DescribeDatasetGroupResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseTypeDef",
    {
        "datasetGroup": "DatasetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestRequestTypeDef",
    {
        "datasetImportJobArn": str,
    },
)

DescribeDatasetImportJobResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseTypeDef",
    {
        "datasetImportJob": "DatasetImportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTrackerRequestRequestTypeDef = TypedDict(
    "DescribeEventTrackerRequestRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DescribeEventTrackerResponseTypeDef = TypedDict(
    "DescribeEventTrackerResponseTypeDef",
    {
        "eventTracker": "EventTrackerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeatureTransformationRequestRequestTypeDef = TypedDict(
    "DescribeFeatureTransformationRequestRequestTypeDef",
    {
        "featureTransformationArn": str,
    },
)

DescribeFeatureTransformationResponseTypeDef = TypedDict(
    "DescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": "FeatureTransformationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFilterRequestRequestTypeDef = TypedDict(
    "DescribeFilterRequestRequestTypeDef",
    {
        "filterArn": str,
    },
)

DescribeFilterResponseTypeDef = TypedDict(
    "DescribeFilterResponseTypeDef",
    {
        "filter": "FilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricAttributionRequestRequestTypeDef = TypedDict(
    "DescribeMetricAttributionRequestRequestTypeDef",
    {
        "metricAttributionArn": str,
    },
)

DescribeMetricAttributionResponseTypeDef = TypedDict(
    "DescribeMetricAttributionResponseTypeDef",
    {
        "metricAttribution": "MetricAttributionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "recipeArn": str,
    },
)

DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "recipe": "RecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecommenderRequestRequestTypeDef = TypedDict(
    "DescribeRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

DescribeRecommenderResponseTypeDef = TypedDict(
    "DescribeRecommenderResponseTypeDef",
    {
        "recommender": "RecommenderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchemaRequestRequestTypeDef = TypedDict(
    "DescribeSchemaRequestRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "schema": "DatasetSchemaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionRequestRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeSolutionResponseTypeDef = TypedDict(
    "DescribeSolutionResponseTypeDef",
    {
        "solution": "SolutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionVersionRequestRequestTypeDef = TypedDict(
    "DescribeSolutionVersionRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

DescribeSolutionVersionResponseTypeDef = TypedDict(
    "DescribeSolutionVersionResponseTypeDef",
    {
        "solutionVersion": "SolutionVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTrackerSummaryTypeDef = TypedDict(
    "EventTrackerSummaryTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

EventTrackerTypeDef = TypedDict(
    "EventTrackerTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "accountId": str,
        "trackingId": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

FeatureTransformationTypeDef = TypedDict(
    "FeatureTransformationTypeDef",
    {
        "name": str,
        "featureTransformationArn": str,
        "defaultParameters": Dict[str, str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
    },
    total=False,
)

FilterSummaryTypeDef = TypedDict(
    "FilterSummaryTypeDef",
    {
        "name": str,
        "filterArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "datasetGroupArn": str,
        "failureReason": str,
        "status": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "filterArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "datasetGroupArn": str,
        "failureReason": str,
        "filterExpression": str,
        "status": str,
    },
    total=False,
)

GetSolutionMetricsRequestRequestTypeDef = TypedDict(
    "GetSolutionMetricsRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

GetSolutionMetricsResponseTypeDef = TypedDict(
    "GetSolutionMetricsResponseTypeDef",
    {
        "solutionVersionArn": str,
        "metrics": Dict[str, float],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HPOConfigTypeDef = TypedDict(
    "HPOConfigTypeDef",
    {
        "hpoObjective": "HPOObjectiveTypeDef",
        "hpoResourceConfig": "HPOResourceConfigTypeDef",
        "algorithmHyperParameterRanges": "HyperParameterRangesTypeDef",
    },
    total=False,
)

HPOObjectiveTypeDef = TypedDict(
    "HPOObjectiveTypeDef",
    {
        "type": str,
        "metricName": str,
        "metricRegex": str,
    },
    total=False,
)

HPOResourceConfigTypeDef = TypedDict(
    "HPOResourceConfigTypeDef",
    {
        "maxNumberOfTrainingJobs": str,
        "maxParallelTrainingJobs": str,
    },
    total=False,
)

HyperParameterRangesTypeDef = TypedDict(
    "HyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List["IntegerHyperParameterRangeTypeDef"],
        "continuousHyperParameterRanges": List["ContinuousHyperParameterRangeTypeDef"],
        "categoricalHyperParameterRanges": List["CategoricalHyperParameterRangeTypeDef"],
    },
    total=False,
)

IntegerHyperParameterRangeTypeDef = TypedDict(
    "IntegerHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": int,
        "maxValue": int,
    },
    total=False,
)

ListBatchInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListBatchInferenceJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListBatchInferenceJobsResponseTypeDef = TypedDict(
    "ListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List["BatchInferenceJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBatchSegmentJobsRequestRequestTypeDef = TypedDict(
    "ListBatchSegmentJobsRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListBatchSegmentJobsResponseTypeDef = TypedDict(
    "ListBatchSegmentJobsResponseTypeDef",
    {
        "batchSegmentJobs": List["BatchSegmentJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "solutionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaigns": List["CampaignSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetExportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetExportJobsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetExportJobsResponseTypeDef = TypedDict(
    "ListDatasetExportJobsResponseTypeDef",
    {
        "datasetExportJobs": List["DatasetExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetGroupsRequestRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {
        "datasetGroups": List["DatasetGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetImportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List["DatasetImportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventTrackersRequestRequestTypeDef = TypedDict(
    "ListEventTrackersRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEventTrackersResponseTypeDef = TypedDict(
    "ListEventTrackersResponseTypeDef",
    {
        "eventTrackers": List["EventTrackerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "Filters": List["FilterSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricAttributionMetricsRequestRequestTypeDef = TypedDict(
    "ListMetricAttributionMetricsRequestRequestTypeDef",
    {
        "metricAttributionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListMetricAttributionMetricsResponseTypeDef = TypedDict(
    "ListMetricAttributionMetricsResponseTypeDef",
    {
        "metrics": List["MetricAttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricAttributionsRequestRequestTypeDef = TypedDict(
    "ListMetricAttributionsRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListMetricAttributionsResponseTypeDef = TypedDict(
    "ListMetricAttributionsResponseTypeDef",
    {
        "metricAttributions": List["MetricAttributionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "recipeProvider": Literal["SERVICE"],
        "nextToken": str,
        "maxResults": int,
        "domain": DomainType,
    },
    total=False,
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "recipes": List["RecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendersRequestRequestTypeDef = TypedDict(
    "ListRecommendersRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRecommendersResponseTypeDef = TypedDict(
    "ListRecommendersResponseTypeDef",
    {
        "recommenders": List["RecommenderSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "schemas": List["DatasetSchemaSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionVersionsRequestRequestTypeDef = TypedDict(
    "ListSolutionVersionsRequestRequestTypeDef",
    {
        "solutionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSolutionVersionsResponseTypeDef = TypedDict(
    "ListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List["SolutionVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionsRequestRequestTypeDef = TypedDict(
    "ListSolutionsRequestRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSolutionsResponseTypeDef = TypedDict(
    "ListSolutionsResponseTypeDef",
    {
        "solutions": List["SolutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricAttributeTypeDef = TypedDict(
    "MetricAttributeTypeDef",
    {
        "eventType": str,
        "metricName": str,
        "expression": str,
    },
)

_RequiredMetricAttributionOutputTypeDef = TypedDict(
    "_RequiredMetricAttributionOutputTypeDef",
    {
        "roleArn": str,
    },
)
_OptionalMetricAttributionOutputTypeDef = TypedDict(
    "_OptionalMetricAttributionOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
    total=False,
)

class MetricAttributionOutputTypeDef(
    _RequiredMetricAttributionOutputTypeDef, _OptionalMetricAttributionOutputTypeDef
):
    pass

MetricAttributionSummaryTypeDef = TypedDict(
    "MetricAttributionSummaryTypeDef",
    {
        "name": str,
        "metricAttributionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

MetricAttributionTypeDef = TypedDict(
    "MetricAttributionTypeDef",
    {
        "name": str,
        "metricAttributionArn": str,
        "datasetGroupArn": str,
        "metricsOutputConfig": "MetricAttributionOutputTypeDef",
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

OptimizationObjectiveTypeDef = TypedDict(
    "OptimizationObjectiveTypeDef",
    {
        "itemAttribute": str,
        "objectiveSensitivity": ObjectiveSensitivityType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RecipeSummaryTypeDef = TypedDict(
    "RecipeSummaryTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "domain": DomainType,
    },
    total=False,
)

RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "algorithmArn": str,
        "featureTransformationArn": str,
        "status": str,
        "description": str,
        "creationDateTime": datetime,
        "recipeType": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

RecommenderConfigTypeDef = TypedDict(
    "RecommenderConfigTypeDef",
    {
        "itemExplorationConfig": Dict[str, str],
        "minRecommendationRequestsPerSecond": int,
        "trainingDataConfig": "TrainingDataConfigTypeDef",
    },
    total=False,
)

RecommenderSummaryTypeDef = TypedDict(
    "RecommenderSummaryTypeDef",
    {
        "name": str,
        "recommenderArn": str,
        "datasetGroupArn": str,
        "recipeArn": str,
        "recommenderConfig": "RecommenderConfigTypeDef",
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

RecommenderTypeDef = TypedDict(
    "RecommenderTypeDef",
    {
        "recommenderArn": str,
        "datasetGroupArn": str,
        "name": str,
        "recipeArn": str,
        "recommenderConfig": "RecommenderConfigTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
        "failureReason": str,
        "latestRecommenderUpdate": "RecommenderUpdateSummaryTypeDef",
        "modelMetrics": Dict[str, float],
    },
    total=False,
)

RecommenderUpdateSummaryTypeDef = TypedDict(
    "RecommenderUpdateSummaryTypeDef",
    {
        "recommenderConfig": "RecommenderConfigTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
        "failureReason": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3DataConfigTypeDef = TypedDict(
    "_RequiredS3DataConfigTypeDef",
    {
        "path": str,
    },
)
_OptionalS3DataConfigTypeDef = TypedDict(
    "_OptionalS3DataConfigTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

class S3DataConfigTypeDef(_RequiredS3DataConfigTypeDef, _OptionalS3DataConfigTypeDef):
    pass

SolutionConfigTypeDef = TypedDict(
    "SolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": "HPOConfigTypeDef",
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": "AutoMLConfigTypeDef",
        "optimizationObjective": "OptimizationObjectiveTypeDef",
        "trainingDataConfig": "TrainingDataConfigTypeDef",
    },
    total=False,
)

SolutionSummaryTypeDef = TypedDict(
    "SolutionSummaryTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "recipeArn": str,
    },
    total=False,
)

SolutionTypeDef = TypedDict(
    "SolutionTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "datasetGroupArn": str,
        "eventType": str,
        "solutionConfig": "SolutionConfigTypeDef",
        "autoMLResult": "AutoMLResultTypeDef",
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestSolutionVersion": "SolutionVersionSummaryTypeDef",
    },
    total=False,
)

SolutionVersionSummaryTypeDef = TypedDict(
    "SolutionVersionSummaryTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

SolutionVersionTypeDef = TypedDict(
    "SolutionVersionTypeDef",
    {
        "name": str,
        "solutionVersionArn": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "datasetGroupArn": str,
        "solutionConfig": "SolutionConfigTypeDef",
        "trainingHours": float,
        "trainingMode": TrainingModeType,
        "tunedHPOParams": "TunedHPOParamsTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

StartRecommenderRequestRequestTypeDef = TypedDict(
    "StartRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

StartRecommenderResponseTypeDef = TypedDict(
    "StartRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRecommenderRequestRequestTypeDef = TypedDict(
    "StopRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
    },
)

StopRecommenderResponseTypeDef = TypedDict(
    "StopRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSolutionVersionCreationRequestRequestTypeDef = TypedDict(
    "StopSolutionVersionCreationRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "tagKey": str,
        "tagValue": str,
    },
)

TrainingDataConfigTypeDef = TypedDict(
    "TrainingDataConfigTypeDef",
    {
        "excludedDatasetColumns": Dict[str, List[str]],
    },
    total=False,
)

TunedHPOParamsTypeDef = TypedDict(
    "TunedHPOParamsTypeDef",
    {
        "algorithmHyperParameters": Dict[str, str],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)
_OptionalUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
    },
    total=False,
)

class UpdateCampaignRequestRequestTypeDef(
    _RequiredUpdateCampaignRequestRequestTypeDef, _OptionalUpdateCampaignRequestRequestTypeDef
):
    pass

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetArn": str,
        "schemaArn": str,
    },
)

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMetricAttributionRequestRequestTypeDef = TypedDict(
    "UpdateMetricAttributionRequestRequestTypeDef",
    {
        "addMetrics": List["MetricAttributeTypeDef"],
        "removeMetrics": List[str],
        "metricsOutputConfig": "MetricAttributionOutputTypeDef",
        "metricAttributionArn": str,
    },
    total=False,
)

UpdateMetricAttributionResponseTypeDef = TypedDict(
    "UpdateMetricAttributionResponseTypeDef",
    {
        "metricAttributionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderRequestRequestTypeDef",
    {
        "recommenderArn": str,
        "recommenderConfig": "RecommenderConfigTypeDef",
    },
)

UpdateRecommenderResponseTypeDef = TypedDict(
    "UpdateRecommenderResponseTypeDef",
    {
        "recommenderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
