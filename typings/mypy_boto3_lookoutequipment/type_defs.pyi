"""
Type annotations for lookoutequipment service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.type_defs import CategoricalValuesTypeDef

    data: CategoricalValuesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DatasetStatusType,
    DataUploadFrequencyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    LabelRatingType,
    LatestInferenceResultType,
    ModelStatusType,
    MonotonicityType,
    StatisticalIssueStatusType,
    TargetSamplingRateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CategoricalValuesTypeDef",
    "CountPercentTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateInferenceSchedulerRequestRequestTypeDef",
    "CreateInferenceSchedulerResponseTypeDef",
    "CreateLabelGroupRequestRequestTypeDef",
    "CreateLabelGroupResponseTypeDef",
    "CreateLabelRequestRequestTypeDef",
    "CreateLabelResponseTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelResponseTypeDef",
    "DataIngestionJobSummaryTypeDef",
    "DataPreProcessingConfigurationTypeDef",
    "DataQualitySummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteInferenceSchedulerRequestRequestTypeDef",
    "DeleteLabelGroupRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DescribeDataIngestionJobRequestRequestTypeDef",
    "DescribeDataIngestionJobResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeInferenceSchedulerRequestRequestTypeDef",
    "DescribeInferenceSchedulerResponseTypeDef",
    "DescribeLabelGroupRequestRequestTypeDef",
    "DescribeLabelGroupResponseTypeDef",
    "DescribeLabelRequestRequestTypeDef",
    "DescribeLabelResponseTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "DuplicateTimestampsTypeDef",
    "InferenceEventSummaryTypeDef",
    "InferenceExecutionSummaryTypeDef",
    "InferenceInputConfigurationTypeDef",
    "InferenceInputNameConfigurationTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "InferenceS3InputConfigurationTypeDef",
    "InferenceS3OutputConfigurationTypeDef",
    "InferenceSchedulerSummaryTypeDef",
    "IngestedFilesSummaryTypeDef",
    "IngestionInputConfigurationTypeDef",
    "IngestionS3InputConfigurationTypeDef",
    "InsufficientSensorDataTypeDef",
    "InvalidSensorDataTypeDef",
    "LabelGroupSummaryTypeDef",
    "LabelSummaryTypeDef",
    "LabelsInputConfigurationTypeDef",
    "LabelsS3InputConfigurationTypeDef",
    "LargeTimestampGapsTypeDef",
    "ListDataIngestionJobsRequestRequestTypeDef",
    "ListDataIngestionJobsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListInferenceEventsRequestRequestTypeDef",
    "ListInferenceEventsResponseTypeDef",
    "ListInferenceExecutionsRequestRequestTypeDef",
    "ListInferenceExecutionsResponseTypeDef",
    "ListInferenceSchedulersRequestRequestTypeDef",
    "ListInferenceSchedulersResponseTypeDef",
    "ListLabelGroupsRequestRequestTypeDef",
    "ListLabelGroupsResponseTypeDef",
    "ListLabelsRequestRequestTypeDef",
    "ListLabelsResponseTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListSensorStatisticsRequestRequestTypeDef",
    "ListSensorStatisticsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissingCompleteSensorDataTypeDef",
    "MissingSensorDataTypeDef",
    "ModelSummaryTypeDef",
    "MonotonicValuesTypeDef",
    "MultipleOperatingModesTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SensorStatisticsSummaryTypeDef",
    "SensorsWithShortDateRangeTypeDef",
    "StartDataIngestionJobRequestRequestTypeDef",
    "StartDataIngestionJobResponseTypeDef",
    "StartInferenceSchedulerRequestRequestTypeDef",
    "StartInferenceSchedulerResponseTypeDef",
    "StopInferenceSchedulerRequestRequestTypeDef",
    "StopInferenceSchedulerResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UnsupportedTimestampsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateInferenceSchedulerRequestRequestTypeDef",
    "UpdateLabelGroupRequestRequestTypeDef",
)

_RequiredCategoricalValuesTypeDef = TypedDict(
    "_RequiredCategoricalValuesTypeDef",
    {
        "Status": StatisticalIssueStatusType,
    },
)
_OptionalCategoricalValuesTypeDef = TypedDict(
    "_OptionalCategoricalValuesTypeDef",
    {
        "NumberOfCategory": int,
    },
    total=False,
)

class CategoricalValuesTypeDef(
    _RequiredCategoricalValuesTypeDef, _OptionalCategoricalValuesTypeDef
):
    pass

CountPercentTypeDef = TypedDict(
    "CountPercentTypeDef",
    {
        "Count": int,
        "Percentage": float,
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
        "ClientToken": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "DatasetSchema": "DatasetSchemaTypeDef",
        "ServerSideKmsKeyId": str,
        "Tags": List["TagTypeDef"],
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
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceSchedulerRequestRequestTypeDef",
    {
        "ModelName": str,
        "InferenceSchedulerName": str,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceSchedulerRequestRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "ServerSideKmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInferenceSchedulerRequestRequestTypeDef(
    _RequiredCreateInferenceSchedulerRequestRequestTypeDef,
    _OptionalCreateInferenceSchedulerRequestRequestTypeDef,
):
    pass

CreateInferenceSchedulerResponseTypeDef = TypedDict(
    "CreateInferenceSchedulerResponseTypeDef",
    {
        "InferenceSchedulerArn": str,
        "InferenceSchedulerName": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLabelGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLabelGroupRequestRequestTypeDef",
    {
        "LabelGroupName": str,
        "ClientToken": str,
    },
)
_OptionalCreateLabelGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLabelGroupRequestRequestTypeDef",
    {
        "FaultCodes": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateLabelGroupRequestRequestTypeDef(
    _RequiredCreateLabelGroupRequestRequestTypeDef, _OptionalCreateLabelGroupRequestRequestTypeDef
):
    pass

CreateLabelGroupResponseTypeDef = TypedDict(
    "CreateLabelGroupResponseTypeDef",
    {
        "LabelGroupName": str,
        "LabelGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLabelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLabelRequestRequestTypeDef",
    {
        "LabelGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Rating": LabelRatingType,
        "ClientToken": str,
    },
)
_OptionalCreateLabelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLabelRequestRequestTypeDef",
    {
        "FaultCode": str,
        "Notes": str,
        "Equipment": str,
    },
    total=False,
)

class CreateLabelRequestRequestTypeDef(
    _RequiredCreateLabelRequestRequestTypeDef, _OptionalCreateLabelRequestRequestTypeDef
):
    pass

CreateLabelResponseTypeDef = TypedDict(
    "CreateLabelResponseTypeDef",
    {
        "LabelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "ModelName": str,
        "DatasetName": str,
        "ClientToken": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "DatasetSchema": "DatasetSchemaTypeDef",
        "LabelsInputConfiguration": "LabelsInputConfigurationTypeDef",
        "TrainingDataStartTime": Union[datetime, str],
        "TrainingDataEndTime": Union[datetime, str],
        "EvaluationDataStartTime": Union[datetime, str],
        "EvaluationDataEndTime": Union[datetime, str],
        "RoleArn": str,
        "DataPreProcessingConfiguration": "DataPreProcessingConfigurationTypeDef",
        "ServerSideKmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "OffCondition": str,
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ModelArn": str,
        "Status": ModelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataIngestionJobSummaryTypeDef = TypedDict(
    "DataIngestionJobSummaryTypeDef",
    {
        "JobId": str,
        "DatasetName": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "Status": IngestionJobStatusType,
    },
    total=False,
)

DataPreProcessingConfigurationTypeDef = TypedDict(
    "DataPreProcessingConfigurationTypeDef",
    {
        "TargetSamplingRate": TargetSamplingRateType,
    },
    total=False,
)

DataQualitySummaryTypeDef = TypedDict(
    "DataQualitySummaryTypeDef",
    {
        "InsufficientSensorData": "InsufficientSensorDataTypeDef",
        "MissingSensorData": "MissingSensorDataTypeDef",
        "InvalidSensorData": "InvalidSensorDataTypeDef",
        "UnsupportedTimestamps": "UnsupportedTimestampsTypeDef",
        "DuplicateTimestamps": "DuplicateTimestampsTypeDef",
    },
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "InlineDataSchema": str,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DeleteInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "DeleteInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DeleteLabelGroupRequestRequestTypeDef = TypedDict(
    "DeleteLabelGroupRequestRequestTypeDef",
    {
        "LabelGroupName": str,
    },
)

DeleteLabelRequestRequestTypeDef = TypedDict(
    "DeleteLabelRequestRequestTypeDef",
    {
        "LabelGroupName": str,
        "LabelId": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeDataIngestionJobRequestRequestTypeDef = TypedDict(
    "DescribeDataIngestionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDataIngestionJobResponseTypeDef = TypedDict(
    "DescribeDataIngestionJobResponseTypeDef",
    {
        "JobId": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "RoleArn": str,
        "CreatedAt": datetime,
        "Status": IngestionJobStatusType,
        "FailedReason": str,
        "DataQualitySummary": "DataQualitySummaryTypeDef",
        "IngestedFilesSummary": "IngestedFilesSummaryTypeDef",
        "StatusDetail": str,
        "IngestedDataSize": int,
        "DataStartTime": datetime,
        "DataEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Status": DatasetStatusType,
        "Schema": str,
        "ServerSideKmsKeyId": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "DataQualitySummary": "DataQualitySummaryTypeDef",
        "IngestedFilesSummary": "IngestedFilesSummaryTypeDef",
        "RoleArn": str,
        "DataStartTime": datetime,
        "DataEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "DescribeInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DescribeInferenceSchedulerResponseTypeDef = TypedDict(
    "DescribeInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
        "ServerSideKmsKeyId": str,
        "LatestInferenceResult": LatestInferenceResultType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLabelGroupRequestRequestTypeDef = TypedDict(
    "DescribeLabelGroupRequestRequestTypeDef",
    {
        "LabelGroupName": str,
    },
)

DescribeLabelGroupResponseTypeDef = TypedDict(
    "DescribeLabelGroupResponseTypeDef",
    {
        "LabelGroupName": str,
        "LabelGroupArn": str,
        "FaultCodes": List[str],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLabelRequestRequestTypeDef = TypedDict(
    "DescribeLabelRequestRequestTypeDef",
    {
        "LabelGroupName": str,
        "LabelId": str,
    },
)

DescribeLabelResponseTypeDef = TypedDict(
    "DescribeLabelResponseTypeDef",
    {
        "LabelGroupName": str,
        "LabelGroupArn": str,
        "LabelId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Rating": LabelRatingType,
        "FaultCode": str,
        "Notes": str,
        "Equipment": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelRequestRequestTypeDef = TypedDict(
    "DescribeModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Schema": str,
        "LabelsInputConfiguration": "LabelsInputConfigurationTypeDef",
        "TrainingDataStartTime": datetime,
        "TrainingDataEndTime": datetime,
        "EvaluationDataStartTime": datetime,
        "EvaluationDataEndTime": datetime,
        "RoleArn": str,
        "DataPreProcessingConfiguration": "DataPreProcessingConfigurationTypeDef",
        "Status": ModelStatusType,
        "TrainingExecutionStartTime": datetime,
        "TrainingExecutionEndTime": datetime,
        "FailedReason": str,
        "ModelMetrics": str,
        "LastUpdatedTime": datetime,
        "CreatedAt": datetime,
        "ServerSideKmsKeyId": str,
        "OffCondition": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DuplicateTimestampsTypeDef = TypedDict(
    "DuplicateTimestampsTypeDef",
    {
        "TotalNumberOfDuplicateTimestamps": int,
    },
)

InferenceEventSummaryTypeDef = TypedDict(
    "InferenceEventSummaryTypeDef",
    {
        "InferenceSchedulerArn": str,
        "InferenceSchedulerName": str,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "Diagnostics": str,
        "EventDurationInSeconds": int,
    },
    total=False,
)

InferenceExecutionSummaryTypeDef = TypedDict(
    "InferenceExecutionSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "ScheduledStartTime": datetime,
        "DataStartTime": datetime,
        "DataEndTime": datetime,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "CustomerResultObject": "S3ObjectTypeDef",
        "Status": InferenceExecutionStatusType,
        "FailedReason": str,
    },
    total=False,
)

InferenceInputConfigurationTypeDef = TypedDict(
    "InferenceInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "InferenceS3InputConfigurationTypeDef",
        "InputTimeZoneOffset": str,
        "InferenceInputNameConfiguration": "InferenceInputNameConfigurationTypeDef",
    },
    total=False,
)

InferenceInputNameConfigurationTypeDef = TypedDict(
    "InferenceInputNameConfigurationTypeDef",
    {
        "TimestampFormat": str,
        "ComponentTimestampDelimiter": str,
    },
    total=False,
)

_RequiredInferenceOutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceOutputConfigurationTypeDef",
    {
        "S3OutputConfiguration": "InferenceS3OutputConfigurationTypeDef",
    },
)
_OptionalInferenceOutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceOutputConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class InferenceOutputConfigurationTypeDef(
    _RequiredInferenceOutputConfigurationTypeDef, _OptionalInferenceOutputConfigurationTypeDef
):
    pass

_RequiredInferenceS3InputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3InputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class InferenceS3InputConfigurationTypeDef(
    _RequiredInferenceS3InputConfigurationTypeDef, _OptionalInferenceS3InputConfigurationTypeDef
):
    pass

_RequiredInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3OutputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3OutputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class InferenceS3OutputConfigurationTypeDef(
    _RequiredInferenceS3OutputConfigurationTypeDef, _OptionalInferenceS3OutputConfigurationTypeDef
):
    pass

InferenceSchedulerSummaryTypeDef = TypedDict(
    "InferenceSchedulerSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "LatestInferenceResult": LatestInferenceResultType,
    },
    total=False,
)

_RequiredIngestedFilesSummaryTypeDef = TypedDict(
    "_RequiredIngestedFilesSummaryTypeDef",
    {
        "TotalNumberOfFiles": int,
        "IngestedNumberOfFiles": int,
    },
)
_OptionalIngestedFilesSummaryTypeDef = TypedDict(
    "_OptionalIngestedFilesSummaryTypeDef",
    {
        "DiscardedFiles": List["S3ObjectTypeDef"],
    },
    total=False,
)

class IngestedFilesSummaryTypeDef(
    _RequiredIngestedFilesSummaryTypeDef, _OptionalIngestedFilesSummaryTypeDef
):
    pass

IngestionInputConfigurationTypeDef = TypedDict(
    "IngestionInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "IngestionS3InputConfigurationTypeDef",
    },
)

_RequiredIngestionS3InputConfigurationTypeDef = TypedDict(
    "_RequiredIngestionS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalIngestionS3InputConfigurationTypeDef = TypedDict(
    "_OptionalIngestionS3InputConfigurationTypeDef",
    {
        "Prefix": str,
        "KeyPattern": str,
    },
    total=False,
)

class IngestionS3InputConfigurationTypeDef(
    _RequiredIngestionS3InputConfigurationTypeDef, _OptionalIngestionS3InputConfigurationTypeDef
):
    pass

InsufficientSensorDataTypeDef = TypedDict(
    "InsufficientSensorDataTypeDef",
    {
        "MissingCompleteSensorData": "MissingCompleteSensorDataTypeDef",
        "SensorsWithShortDateRange": "SensorsWithShortDateRangeTypeDef",
    },
)

InvalidSensorDataTypeDef = TypedDict(
    "InvalidSensorDataTypeDef",
    {
        "AffectedSensorCount": int,
        "TotalNumberOfInvalidValues": int,
    },
)

LabelGroupSummaryTypeDef = TypedDict(
    "LabelGroupSummaryTypeDef",
    {
        "LabelGroupName": str,
        "LabelGroupArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "LabelGroupName": str,
        "LabelId": str,
        "LabelGroupArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Rating": LabelRatingType,
        "FaultCode": str,
        "Equipment": str,
        "CreatedAt": datetime,
    },
    total=False,
)

LabelsInputConfigurationTypeDef = TypedDict(
    "LabelsInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "LabelsS3InputConfigurationTypeDef",
        "LabelGroupName": str,
    },
    total=False,
)

_RequiredLabelsS3InputConfigurationTypeDef = TypedDict(
    "_RequiredLabelsS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalLabelsS3InputConfigurationTypeDef = TypedDict(
    "_OptionalLabelsS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class LabelsS3InputConfigurationTypeDef(
    _RequiredLabelsS3InputConfigurationTypeDef, _OptionalLabelsS3InputConfigurationTypeDef
):
    pass

_RequiredLargeTimestampGapsTypeDef = TypedDict(
    "_RequiredLargeTimestampGapsTypeDef",
    {
        "Status": StatisticalIssueStatusType,
    },
)
_OptionalLargeTimestampGapsTypeDef = TypedDict(
    "_OptionalLargeTimestampGapsTypeDef",
    {
        "NumberOfLargeTimestampGaps": int,
        "MaxTimestampGapInDays": int,
    },
    total=False,
)

class LargeTimestampGapsTypeDef(
    _RequiredLargeTimestampGapsTypeDef, _OptionalLargeTimestampGapsTypeDef
):
    pass

ListDataIngestionJobsRequestRequestTypeDef = TypedDict(
    "ListDataIngestionJobsRequestRequestTypeDef",
    {
        "DatasetName": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": IngestionJobStatusType,
    },
    total=False,
)

ListDataIngestionJobsResponseTypeDef = TypedDict(
    "ListDataIngestionJobsResponseTypeDef",
    {
        "NextToken": str,
        "DataIngestionJobSummaries": List["DataIngestionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "NextToken": str,
        "DatasetSummaries": List["DatasetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInferenceEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListInferenceEventsRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
        "IntervalStartTime": Union[datetime, str],
        "IntervalEndTime": Union[datetime, str],
    },
)
_OptionalListInferenceEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListInferenceEventsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInferenceEventsRequestRequestTypeDef(
    _RequiredListInferenceEventsRequestRequestTypeDef,
    _OptionalListInferenceEventsRequestRequestTypeDef,
):
    pass

ListInferenceEventsResponseTypeDef = TypedDict(
    "ListInferenceEventsResponseTypeDef",
    {
        "NextToken": str,
        "InferenceEventSummaries": List["InferenceEventSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInferenceExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListInferenceExecutionsRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalListInferenceExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListInferenceExecutionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DataStartTimeAfter": Union[datetime, str],
        "DataEndTimeBefore": Union[datetime, str],
        "Status": InferenceExecutionStatusType,
    },
    total=False,
)

class ListInferenceExecutionsRequestRequestTypeDef(
    _RequiredListInferenceExecutionsRequestRequestTypeDef,
    _OptionalListInferenceExecutionsRequestRequestTypeDef,
):
    pass

ListInferenceExecutionsResponseTypeDef = TypedDict(
    "ListInferenceExecutionsResponseTypeDef",
    {
        "NextToken": str,
        "InferenceExecutionSummaries": List["InferenceExecutionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInferenceSchedulersRequestRequestTypeDef = TypedDict(
    "ListInferenceSchedulersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "InferenceSchedulerNameBeginsWith": str,
        "ModelName": str,
    },
    total=False,
)

ListInferenceSchedulersResponseTypeDef = TypedDict(
    "ListInferenceSchedulersResponseTypeDef",
    {
        "NextToken": str,
        "InferenceSchedulerSummaries": List["InferenceSchedulerSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLabelGroupsRequestRequestTypeDef = TypedDict(
    "ListLabelGroupsRequestRequestTypeDef",
    {
        "LabelGroupNameBeginsWith": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLabelGroupsResponseTypeDef = TypedDict(
    "ListLabelGroupsResponseTypeDef",
    {
        "NextToken": str,
        "LabelGroupSummaries": List["LabelGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLabelsRequestRequestTypeDef = TypedDict(
    "_RequiredListLabelsRequestRequestTypeDef",
    {
        "LabelGroupName": str,
    },
)
_OptionalListLabelsRequestRequestTypeDef = TypedDict(
    "_OptionalListLabelsRequestRequestTypeDef",
    {
        "IntervalStartTime": Union[datetime, str],
        "IntervalEndTime": Union[datetime, str],
        "FaultCode": str,
        "Equipment": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLabelsRequestRequestTypeDef(
    _RequiredListLabelsRequestRequestTypeDef, _OptionalListLabelsRequestRequestTypeDef
):
    pass

ListLabelsResponseTypeDef = TypedDict(
    "ListLabelsResponseTypeDef",
    {
        "NextToken": str,
        "LabelSummaries": List["LabelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsRequestRequestTypeDef = TypedDict(
    "ListModelsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": ModelStatusType,
        "ModelNameBeginsWith": str,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {
        "NextToken": str,
        "ModelSummaries": List["ModelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSensorStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredListSensorStatisticsRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
)
_OptionalListSensorStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalListSensorStatisticsRequestRequestTypeDef",
    {
        "IngestionJobId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSensorStatisticsRequestRequestTypeDef(
    _RequiredListSensorStatisticsRequestRequestTypeDef,
    _OptionalListSensorStatisticsRequestRequestTypeDef,
):
    pass

ListSensorStatisticsResponseTypeDef = TypedDict(
    "ListSensorStatisticsResponseTypeDef",
    {
        "SensorStatisticsSummaries": List["SensorStatisticsSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MissingCompleteSensorDataTypeDef = TypedDict(
    "MissingCompleteSensorDataTypeDef",
    {
        "AffectedSensorCount": int,
    },
)

MissingSensorDataTypeDef = TypedDict(
    "MissingSensorDataTypeDef",
    {
        "AffectedSensorCount": int,
        "TotalNumberOfMissingValues": int,
    },
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Status": ModelStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

_RequiredMonotonicValuesTypeDef = TypedDict(
    "_RequiredMonotonicValuesTypeDef",
    {
        "Status": StatisticalIssueStatusType,
    },
)
_OptionalMonotonicValuesTypeDef = TypedDict(
    "_OptionalMonotonicValuesTypeDef",
    {
        "Monotonicity": MonotonicityType,
    },
    total=False,
)

class MonotonicValuesTypeDef(_RequiredMonotonicValuesTypeDef, _OptionalMonotonicValuesTypeDef):
    pass

MultipleOperatingModesTypeDef = TypedDict(
    "MultipleOperatingModesTypeDef",
    {
        "Status": StatisticalIssueStatusType,
    },
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

SensorStatisticsSummaryTypeDef = TypedDict(
    "SensorStatisticsSummaryTypeDef",
    {
        "ComponentName": str,
        "SensorName": str,
        "DataExists": bool,
        "MissingValues": "CountPercentTypeDef",
        "InvalidValues": "CountPercentTypeDef",
        "InvalidDateEntries": "CountPercentTypeDef",
        "DuplicateTimestamps": "CountPercentTypeDef",
        "CategoricalValues": "CategoricalValuesTypeDef",
        "MultipleOperatingModes": "MultipleOperatingModesTypeDef",
        "LargeTimestampGaps": "LargeTimestampGapsTypeDef",
        "MonotonicValues": "MonotonicValuesTypeDef",
        "DataStartTime": datetime,
        "DataEndTime": datetime,
    },
    total=False,
)

SensorsWithShortDateRangeTypeDef = TypedDict(
    "SensorsWithShortDateRangeTypeDef",
    {
        "AffectedSensorCount": int,
    },
)

StartDataIngestionJobRequestRequestTypeDef = TypedDict(
    "StartDataIngestionJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "RoleArn": str,
        "ClientToken": str,
    },
)

StartDataIngestionJobResponseTypeDef = TypedDict(
    "StartDataIngestionJobResponseTypeDef",
    {
        "JobId": str,
        "Status": IngestionJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "StartInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

StartInferenceSchedulerResponseTypeDef = TypedDict(
    "StartInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "StopInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

StopInferenceSchedulerResponseTypeDef = TypedDict(
    "StopInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UnsupportedTimestampsTypeDef = TypedDict(
    "UnsupportedTimestampsTypeDef",
    {
        "TotalNumberOfUnsupportedTimestamps": int,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalUpdateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInferenceSchedulerRequestRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
    },
    total=False,
)

class UpdateInferenceSchedulerRequestRequestTypeDef(
    _RequiredUpdateInferenceSchedulerRequestRequestTypeDef,
    _OptionalUpdateInferenceSchedulerRequestRequestTypeDef,
):
    pass

_RequiredUpdateLabelGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLabelGroupRequestRequestTypeDef",
    {
        "LabelGroupName": str,
    },
)
_OptionalUpdateLabelGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLabelGroupRequestRequestTypeDef",
    {
        "FaultCodes": List[str],
    },
    total=False,
)

class UpdateLabelGroupRequestRequestTypeDef(
    _RequiredUpdateLabelGroupRequestRequestTypeDef, _OptionalUpdateLabelGroupRequestRequestTypeDef
):
    pass
