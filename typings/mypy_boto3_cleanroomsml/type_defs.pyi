"""
Type annotations for cleanroomsml service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cleanroomsml.type_defs import AudienceDestinationTypeDef

    data: AudienceDestinationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AudienceExportJobStatusType,
    AudienceGenerationJobStatusType,
    AudienceModelStatusType,
    AudienceSizeTypeType,
    ColumnTypeType,
    PolicyExistenceConditionType,
    SharedAudienceMetricsType,
    TagOnCreatePolicyType,
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
    "AudienceDestinationTypeDef",
    "AudienceExportJobSummaryTypeDef",
    "AudienceGenerationJobDataSourceTypeDef",
    "AudienceGenerationJobSummaryTypeDef",
    "AudienceModelSummaryTypeDef",
    "AudienceQualityMetricsTypeDef",
    "AudienceSizeConfigTypeDef",
    "AudienceSizeTypeDef",
    "ColumnSchemaTypeDef",
    "ConfiguredAudienceModelOutputConfigTypeDef",
    "ConfiguredAudienceModelSummaryTypeDef",
    "CreateAudienceModelRequestRequestTypeDef",
    "CreateAudienceModelResponseTypeDef",
    "CreateConfiguredAudienceModelRequestRequestTypeDef",
    "CreateConfiguredAudienceModelResponseTypeDef",
    "CreateTrainingDatasetRequestRequestTypeDef",
    "CreateTrainingDatasetResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetInputConfigTypeDef",
    "DatasetTypeDef",
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    "DeleteAudienceModelRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    "DeleteTrainingDatasetRequestRequestTypeDef",
    "GetAudienceGenerationJobRequestRequestTypeDef",
    "GetAudienceGenerationJobResponseTypeDef",
    "GetAudienceModelRequestRequestTypeDef",
    "GetAudienceModelResponseTypeDef",
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    "GetConfiguredAudienceModelResponseTypeDef",
    "GetTrainingDatasetRequestRequestTypeDef",
    "GetTrainingDatasetResponseTypeDef",
    "GlueDataSourceTypeDef",
    "ListAudienceExportJobsRequestRequestTypeDef",
    "ListAudienceExportJobsResponseTypeDef",
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    "ListAudienceGenerationJobsResponseTypeDef",
    "ListAudienceModelsRequestRequestTypeDef",
    "ListAudienceModelsResponseTypeDef",
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
    "ListConfiguredAudienceModelsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrainingDatasetsRequestRequestTypeDef",
    "ListTrainingDatasetsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    "RelevanceMetricTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigMapTypeDef",
    "StartAudienceExportJobRequestRequestTypeDef",
    "StartAudienceGenerationJobRequestRequestTypeDef",
    "StartAudienceGenerationJobResponseTypeDef",
    "StatusDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TrainingDatasetSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConfiguredAudienceModelRequestRequestTypeDef",
    "UpdateConfiguredAudienceModelResponseTypeDef",
)

AudienceDestinationTypeDef = TypedDict(
    "AudienceDestinationTypeDef",
    {
        "s3Destination": "S3ConfigMapTypeDef",
    },
)

_RequiredAudienceExportJobSummaryTypeDef = TypedDict(
    "_RequiredAudienceExportJobSummaryTypeDef",
    {
        "audienceGenerationJobArn": str,
        "audienceSize": "AudienceSizeTypeDef",
        "createTime": datetime,
        "name": str,
        "status": AudienceExportJobStatusType,
        "updateTime": datetime,
    },
)
_OptionalAudienceExportJobSummaryTypeDef = TypedDict(
    "_OptionalAudienceExportJobSummaryTypeDef",
    {
        "description": str,
        "outputLocation": str,
        "statusDetails": "StatusDetailsTypeDef",
    },
    total=False,
)

class AudienceExportJobSummaryTypeDef(
    _RequiredAudienceExportJobSummaryTypeDef, _OptionalAudienceExportJobSummaryTypeDef
):
    pass

AudienceGenerationJobDataSourceTypeDef = TypedDict(
    "AudienceGenerationJobDataSourceTypeDef",
    {
        "dataSource": "S3ConfigMapTypeDef",
        "roleArn": str,
    },
)

_RequiredAudienceGenerationJobSummaryTypeDef = TypedDict(
    "_RequiredAudienceGenerationJobSummaryTypeDef",
    {
        "audienceGenerationJobArn": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "status": AudienceGenerationJobStatusType,
        "updateTime": datetime,
    },
)
_OptionalAudienceGenerationJobSummaryTypeDef = TypedDict(
    "_OptionalAudienceGenerationJobSummaryTypeDef",
    {
        "collaborationId": str,
        "description": str,
        "startedBy": str,
    },
    total=False,
)

class AudienceGenerationJobSummaryTypeDef(
    _RequiredAudienceGenerationJobSummaryTypeDef, _OptionalAudienceGenerationJobSummaryTypeDef
):
    pass

_RequiredAudienceModelSummaryTypeDef = TypedDict(
    "_RequiredAudienceModelSummaryTypeDef",
    {
        "audienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "status": AudienceModelStatusType,
        "trainingDatasetArn": str,
        "updateTime": datetime,
    },
)
_OptionalAudienceModelSummaryTypeDef = TypedDict(
    "_OptionalAudienceModelSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class AudienceModelSummaryTypeDef(
    _RequiredAudienceModelSummaryTypeDef, _OptionalAudienceModelSummaryTypeDef
):
    pass

_RequiredAudienceQualityMetricsTypeDef = TypedDict(
    "_RequiredAudienceQualityMetricsTypeDef",
    {
        "relevanceMetrics": List["RelevanceMetricTypeDef"],
    },
)
_OptionalAudienceQualityMetricsTypeDef = TypedDict(
    "_OptionalAudienceQualityMetricsTypeDef",
    {
        "recallMetric": float,
    },
    total=False,
)

class AudienceQualityMetricsTypeDef(
    _RequiredAudienceQualityMetricsTypeDef, _OptionalAudienceQualityMetricsTypeDef
):
    pass

AudienceSizeConfigTypeDef = TypedDict(
    "AudienceSizeConfigTypeDef",
    {
        "audienceSizeBins": List[int],
        "audienceSizeType": AudienceSizeTypeType,
    },
)

AudienceSizeTypeDef = TypedDict(
    "AudienceSizeTypeDef",
    {
        "type": AudienceSizeTypeType,
        "value": int,
    },
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "columnName": str,
        "columnTypes": List[ColumnTypeType],
    },
)

ConfiguredAudienceModelOutputConfigTypeDef = TypedDict(
    "ConfiguredAudienceModelOutputConfigTypeDef",
    {
        "destination": "AudienceDestinationTypeDef",
        "roleArn": str,
    },
)

_RequiredConfiguredAudienceModelSummaryTypeDef = TypedDict(
    "_RequiredConfiguredAudienceModelSummaryTypeDef",
    {
        "audienceModelArn": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "name": str,
        "outputConfig": "ConfiguredAudienceModelOutputConfigTypeDef",
        "status": Literal["ACTIVE"],
        "updateTime": datetime,
    },
)
_OptionalConfiguredAudienceModelSummaryTypeDef = TypedDict(
    "_OptionalConfiguredAudienceModelSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ConfiguredAudienceModelSummaryTypeDef(
    _RequiredConfiguredAudienceModelSummaryTypeDef, _OptionalConfiguredAudienceModelSummaryTypeDef
):
    pass

_RequiredCreateAudienceModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAudienceModelRequestRequestTypeDef",
    {
        "name": str,
        "trainingDatasetArn": str,
    },
)
_OptionalCreateAudienceModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAudienceModelRequestRequestTypeDef",
    {
        "description": str,
        "kmsKeyArn": str,
        "tags": Dict[str, str],
        "trainingDataEndTime": Union[datetime, str],
        "trainingDataStartTime": Union[datetime, str],
    },
    total=False,
)

class CreateAudienceModelRequestRequestTypeDef(
    _RequiredCreateAudienceModelRequestRequestTypeDef,
    _OptionalCreateAudienceModelRequestRequestTypeDef,
):
    pass

CreateAudienceModelResponseTypeDef = TypedDict(
    "CreateAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
        "name": str,
        "outputConfig": "ConfiguredAudienceModelOutputConfigTypeDef",
        "sharedAudienceMetrics": List[SharedAudienceMetricsType],
    },
)
_OptionalCreateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "audienceSizeConfig": "AudienceSizeConfigTypeDef",
        "childResourceTagOnCreatePolicy": TagOnCreatePolicyType,
        "description": str,
        "minMatchingSeedSize": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateConfiguredAudienceModelRequestRequestTypeDef(
    _RequiredCreateConfiguredAudienceModelRequestRequestTypeDef,
    _OptionalCreateConfiguredAudienceModelRequestRequestTypeDef,
):
    pass

CreateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "CreateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrainingDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrainingDatasetRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "trainingData": List["DatasetTypeDef"],
    },
)
_OptionalCreateTrainingDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrainingDatasetRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateTrainingDatasetRequestRequestTypeDef(
    _RequiredCreateTrainingDatasetRequestRequestTypeDef,
    _OptionalCreateTrainingDatasetRequestRequestTypeDef,
):
    pass

CreateTrainingDatasetResponseTypeDef = TypedDict(
    "CreateTrainingDatasetResponseTypeDef",
    {
        "trainingDatasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "glueDataSource": "GlueDataSourceTypeDef",
    },
)

DatasetInputConfigTypeDef = TypedDict(
    "DatasetInputConfigTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "schema": List["ColumnSchemaTypeDef"],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "inputConfig": "DatasetInputConfigTypeDef",
        "type": Literal["INTERACTIONS"],
    },
)

DeleteAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)

DeleteAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)

DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)

DeleteConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)

DeleteTrainingDatasetRequestRequestTypeDef = TypedDict(
    "DeleteTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
    },
)

GetAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "GetAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)

GetAudienceGenerationJobResponseTypeDef = TypedDict(
    "GetAudienceGenerationJobResponseTypeDef",
    {
        "audienceGenerationJobArn": str,
        "collaborationId": str,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "includeSeedInOutput": bool,
        "metrics": "AudienceQualityMetricsTypeDef",
        "name": str,
        "seedAudience": "AudienceGenerationJobDataSourceTypeDef",
        "startedBy": str,
        "status": AudienceGenerationJobStatusType,
        "statusDetails": "StatusDetailsTypeDef",
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAudienceModelRequestRequestTypeDef = TypedDict(
    "GetAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)

GetAudienceModelResponseTypeDef = TypedDict(
    "GetAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "kmsKeyArn": str,
        "name": str,
        "status": AudienceModelStatusType,
        "statusDetails": "StatusDetailsTypeDef",
        "tags": Dict[str, str],
        "trainingDataEndTime": datetime,
        "trainingDataStartTime": datetime,
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)

GetConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)

GetConfiguredAudienceModelResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "audienceSizeConfig": "AudienceSizeConfigTypeDef",
        "childResourceTagOnCreatePolicy": TagOnCreatePolicyType,
        "configuredAudienceModelArn": str,
        "createTime": datetime,
        "description": str,
        "minMatchingSeedSize": int,
        "name": str,
        "outputConfig": "ConfiguredAudienceModelOutputConfigTypeDef",
        "sharedAudienceMetrics": List[SharedAudienceMetricsType],
        "status": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrainingDatasetRequestRequestTypeDef = TypedDict(
    "GetTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
    },
)

GetTrainingDatasetResponseTypeDef = TypedDict(
    "GetTrainingDatasetResponseTypeDef",
    {
        "createTime": datetime,
        "description": str,
        "name": str,
        "roleArn": str,
        "status": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "trainingData": List["DatasetTypeDef"],
        "trainingDatasetArn": str,
        "updateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGlueDataSourceTypeDef = TypedDict(
    "_RequiredGlueDataSourceTypeDef",
    {
        "databaseName": str,
        "tableName": str,
    },
)
_OptionalGlueDataSourceTypeDef = TypedDict(
    "_OptionalGlueDataSourceTypeDef",
    {
        "catalogId": str,
    },
    total=False,
)

class GlueDataSourceTypeDef(_RequiredGlueDataSourceTypeDef, _OptionalGlueDataSourceTypeDef):
    pass

ListAudienceExportJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceExportJobsRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAudienceExportJobsResponseTypeDef = TypedDict(
    "ListAudienceExportJobsResponseTypeDef",
    {
        "audienceExportJobs": List["AudienceExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAudienceGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    {
        "collaborationId": str,
        "configuredAudienceModelArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAudienceGenerationJobsResponseTypeDef = TypedDict(
    "ListAudienceGenerationJobsResponseTypeDef",
    {
        "audienceGenerationJobs": List["AudienceGenerationJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListAudienceModelsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAudienceModelsResponseTypeDef = TypedDict(
    "ListAudienceModelsResponseTypeDef",
    {
        "audienceModels": List["AudienceModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfiguredAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListConfiguredAudienceModelsResponseTypeDef = TypedDict(
    "ListConfiguredAudienceModelsResponseTypeDef",
    {
        "configuredAudienceModels": List["ConfiguredAudienceModelSummaryTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrainingDatasetsRequestRequestTypeDef = TypedDict(
    "ListTrainingDatasetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTrainingDatasetsResponseTypeDef = TypedDict(
    "ListTrainingDatasetsResponseTypeDef",
    {
        "nextToken": str,
        "trainingDatasets": List["TrainingDatasetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPutConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
    },
)
_OptionalPutConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "policyExistenceCondition": PolicyExistenceConditionType,
        "previousPolicyHash": str,
    },
    total=False,
)

class PutConfiguredAudienceModelPolicyRequestRequestTypeDef(
    _RequiredPutConfiguredAudienceModelPolicyRequestRequestTypeDef,
    _OptionalPutConfiguredAudienceModelPolicyRequestRequestTypeDef,
):
    pass

PutConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRelevanceMetricTypeDef = TypedDict(
    "_RequiredRelevanceMetricTypeDef",
    {
        "audienceSize": "AudienceSizeTypeDef",
    },
)
_OptionalRelevanceMetricTypeDef = TypedDict(
    "_OptionalRelevanceMetricTypeDef",
    {
        "score": float,
    },
    total=False,
)

class RelevanceMetricTypeDef(_RequiredRelevanceMetricTypeDef, _OptionalRelevanceMetricTypeDef):
    pass

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

S3ConfigMapTypeDef = TypedDict(
    "S3ConfigMapTypeDef",
    {
        "s3Uri": str,
    },
)

_RequiredStartAudienceExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartAudienceExportJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
        "audienceSize": "AudienceSizeTypeDef",
        "name": str,
    },
)
_OptionalStartAudienceExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartAudienceExportJobRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StartAudienceExportJobRequestRequestTypeDef(
    _RequiredStartAudienceExportJobRequestRequestTypeDef,
    _OptionalStartAudienceExportJobRequestRequestTypeDef,
):
    pass

_RequiredStartAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartAudienceGenerationJobRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "name": str,
        "seedAudience": "AudienceGenerationJobDataSourceTypeDef",
    },
)
_OptionalStartAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartAudienceGenerationJobRequestRequestTypeDef",
    {
        "collaborationId": str,
        "description": str,
        "includeSeedInOutput": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartAudienceGenerationJobRequestRequestTypeDef(
    _RequiredStartAudienceGenerationJobRequestRequestTypeDef,
    _OptionalStartAudienceGenerationJobRequestRequestTypeDef,
):
    pass

StartAudienceGenerationJobResponseTypeDef = TypedDict(
    "StartAudienceGenerationJobResponseTypeDef",
    {
        "audienceGenerationJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatusDetailsTypeDef = TypedDict(
    "StatusDetailsTypeDef",
    {
        "message": str,
        "statusCode": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTrainingDatasetSummaryTypeDef = TypedDict(
    "_RequiredTrainingDatasetSummaryTypeDef",
    {
        "createTime": datetime,
        "name": str,
        "status": Literal["ACTIVE"],
        "trainingDatasetArn": str,
        "updateTime": datetime,
    },
)
_OptionalTrainingDatasetSummaryTypeDef = TypedDict(
    "_OptionalTrainingDatasetSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class TrainingDatasetSummaryTypeDef(
    _RequiredTrainingDatasetSummaryTypeDef, _OptionalTrainingDatasetSummaryTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
_OptionalUpdateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
        "audienceSizeConfig": "AudienceSizeConfigTypeDef",
        "description": str,
        "minMatchingSeedSize": int,
        "outputConfig": "ConfiguredAudienceModelOutputConfigTypeDef",
        "sharedAudienceMetrics": List[SharedAudienceMetricsType],
    },
    total=False,
)

class UpdateConfiguredAudienceModelRequestRequestTypeDef(
    _RequiredUpdateConfiguredAudienceModelRequestRequestTypeDef,
    _OptionalUpdateConfiguredAudienceModelRequestRequestTypeDef,
):
    pass

UpdateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
