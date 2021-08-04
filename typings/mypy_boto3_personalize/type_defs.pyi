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

from .literals import IngestionModeType, ObjectiveSensitivityType, TrainingModeType

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
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "CreateBatchInferenceJobRequestRequestTypeDef",
    "CreateBatchInferenceJobResponseTypeDef",
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
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteEventTrackerRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSolutionRequestRequestTypeDef",
    "DescribeAlgorithmRequestRequestTypeDef",
    "DescribeAlgorithmResponseTypeDef",
    "DescribeBatchInferenceJobRequestRequestTypeDef",
    "DescribeBatchInferenceJobResponseTypeDef",
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
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
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
    "ListRecipesRequestRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSolutionVersionsRequestRequestTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "ListSolutionsRequestRequestTypeDef",
    "ListSolutionsResponseTypeDef",
    "OptimizationObjectiveTypeDef",
    "PaginatorConfigTypeDef",
    "RecipeSummaryTypeDef",
    "RecipeTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataConfigTypeDef",
    "SolutionConfigTypeDef",
    "SolutionSummaryTypeDef",
    "SolutionTypeDef",
    "SolutionVersionSummaryTypeDef",
    "SolutionVersionTypeDef",
    "StopSolutionVersionCreationRequestRequestTypeDef",
    "TunedHPOParamsTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "CreateDatasetImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
    },
)

CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "datasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventTrackerRequestRequestTypeDef = TypedDict(
    "CreateEventTrackerRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)

CreateEventTrackerResponseTypeDef = TypedDict(
    "CreateEventTrackerResponseTypeDef",
    {
        "eventTrackerArn": str,
        "trackingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "filterExpression": str,
    },
)

CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "filterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "name": str,
        "schema": str,
    },
)

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
        "trainingMode": TrainingModeType,
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

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "recipeProvider": Literal["SERVICE"],
        "nextToken": str,
        "maxResults": int,
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

StopSolutionVersionCreationRequestRequestTypeDef = TypedDict(
    "StopSolutionVersionCreationRequestRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

TunedHPOParamsTypeDef = TypedDict(
    "TunedHPOParamsTypeDef",
    {
        "algorithmHyperParameters": Dict[str, str],
    },
    total=False,
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
