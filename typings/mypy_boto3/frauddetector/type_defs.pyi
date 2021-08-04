"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef

    data: BatchCreateVariableErrorTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AsyncJobStatusType,
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    ModelEndpointStatusType,
    ModelInputDataFormatType,
    ModelOutputDataFormatType,
    ModelVersionStatusType,
    RuleExecutionModeType,
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
    "BatchCreateVariableErrorTypeDef",
    "BatchCreateVariableRequestRequestTypeDef",
    "BatchCreateVariableResultTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableRequestRequestTypeDef",
    "BatchGetVariableResultTypeDef",
    "BatchPredictionTypeDef",
    "CancelBatchPredictionJobRequestRequestTypeDef",
    "CreateBatchPredictionJobRequestRequestTypeDef",
    "CreateDetectorVersionRequestRequestTypeDef",
    "CreateDetectorVersionResultTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelVersionRequestRequestTypeDef",
    "CreateModelVersionResultTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResultTypeDef",
    "CreateVariableRequestRequestTypeDef",
    "DataValidationMetricsTypeDef",
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteDetectorVersionRequestRequestTypeDef",
    "DeleteEntityTypeRequestRequestTypeDef",
    "DeleteEventRequestRequestTypeDef",
    "DeleteEventTypeRequestRequestTypeDef",
    "DeleteExternalModelRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelVersionRequestRequestTypeDef",
    "DeleteOutcomeRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteVariableRequestRequestTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "DescribeDetectorResultTypeDef",
    "DescribeModelVersionsRequestRequestTypeDef",
    "DescribeModelVersionsResultTypeDef",
    "DetectorTypeDef",
    "DetectorVersionSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EventTypeTypeDef",
    "ExternalEventsDetailTypeDef",
    "ExternalModelTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "GetBatchPredictionJobsRequestRequestTypeDef",
    "GetBatchPredictionJobsResultTypeDef",
    "GetDetectorVersionRequestRequestTypeDef",
    "GetDetectorVersionResultTypeDef",
    "GetDetectorsRequestRequestTypeDef",
    "GetDetectorsResultTypeDef",
    "GetEntityTypesRequestRequestTypeDef",
    "GetEntityTypesResultTypeDef",
    "GetEventPredictionRequestRequestTypeDef",
    "GetEventPredictionResultTypeDef",
    "GetEventTypesRequestRequestTypeDef",
    "GetEventTypesResultTypeDef",
    "GetExternalModelsRequestRequestTypeDef",
    "GetExternalModelsResultTypeDef",
    "GetKMSEncryptionKeyResultTypeDef",
    "GetLabelsRequestRequestTypeDef",
    "GetLabelsResultTypeDef",
    "GetModelVersionRequestRequestTypeDef",
    "GetModelVersionResultTypeDef",
    "GetModelsRequestRequestTypeDef",
    "GetModelsResultTypeDef",
    "GetOutcomesRequestRequestTypeDef",
    "GetOutcomesResultTypeDef",
    "GetRulesRequestRequestTypeDef",
    "GetRulesResultTypeDef",
    "GetVariablesRequestRequestTypeDef",
    "GetVariablesResultTypeDef",
    "KMSKeyTypeDef",
    "LabelSchemaTypeDef",
    "LabelTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogitMetricTypeDef",
    "MetricDataPointTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationTypeDef",
    "ModelScoresTypeDef",
    "ModelTypeDef",
    "ModelVersionDetailTypeDef",
    "ModelVersionTypeDef",
    "OutcomeTypeDef",
    "PutDetectorRequestRequestTypeDef",
    "PutEntityTypeRequestRequestTypeDef",
    "PutEventTypeRequestRequestTypeDef",
    "PutExternalModelRequestRequestTypeDef",
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    "PutLabelRequestRequestTypeDef",
    "PutOutcomeRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDetailTypeDef",
    "RuleResultTypeDef",
    "RuleTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrainingDataSchemaTypeDef",
    "TrainingMetricsTypeDef",
    "TrainingResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    "UpdateDetectorVersionRequestRequestTypeDef",
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateModelVersionRequestRequestTypeDef",
    "UpdateModelVersionResultTypeDef",
    "UpdateModelVersionStatusRequestRequestTypeDef",
    "UpdateRuleMetadataRequestRequestTypeDef",
    "UpdateRuleVersionRequestRequestTypeDef",
    "UpdateRuleVersionResultTypeDef",
    "UpdateVariableRequestRequestTypeDef",
    "VariableEntryTypeDef",
    "VariableImportanceMetricsTypeDef",
    "VariableTypeDef",
)

BatchCreateVariableErrorTypeDef = TypedDict(
    "BatchCreateVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

_RequiredBatchCreateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateVariableRequestRequestTypeDef",
    {
        "variableEntries": List["VariableEntryTypeDef"],
    },
)
_OptionalBatchCreateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateVariableRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class BatchCreateVariableRequestRequestTypeDef(
    _RequiredBatchCreateVariableRequestRequestTypeDef,
    _OptionalBatchCreateVariableRequestRequestTypeDef,
):
    pass

BatchCreateVariableResultTypeDef = TypedDict(
    "BatchCreateVariableResultTypeDef",
    {
        "errors": List["BatchCreateVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetVariableErrorTypeDef = TypedDict(
    "BatchGetVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

BatchGetVariableRequestRequestTypeDef = TypedDict(
    "BatchGetVariableRequestRequestTypeDef",
    {
        "names": List[str],
    },
)

BatchGetVariableResultTypeDef = TypedDict(
    "BatchGetVariableResultTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "errors": List["BatchGetVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "jobId": str,
        "status": AsyncJobStatusType,
        "failureReason": str,
        "startTime": str,
        "completionTime": str,
        "lastHeartbeatTime": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "detectorVersion": str,
        "iamRoleArn": str,
        "arn": str,
        "processedRecordsCount": int,
        "totalRecordsCount": int,
    },
    total=False,
)

CancelBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CancelBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredCreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "iamRoleArn": str,
    },
)
_OptionalCreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchPredictionJobRequestRequestTypeDef",
    {
        "detectorVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBatchPredictionJobRequestRequestTypeDef(
    _RequiredCreateBatchPredictionJobRequestRequestTypeDef,
    _OptionalCreateBatchPredictionJobRequestRequestTypeDef,
):
    pass

_RequiredCreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "rules": List["RuleTypeDef"],
    },
)
_OptionalCreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorVersionRequestRequestTypeDef",
    {
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List["ModelVersionTypeDef"],
        "ruleExecutionMode": RuleExecutionModeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDetectorVersionRequestRequestTypeDef(
    _RequiredCreateDetectorVersionRequestRequestTypeDef,
    _OptionalCreateDetectorVersionRequestRequestTypeDef,
):
    pass

CreateDetectorVersionResultTypeDef = TypedDict(
    "CreateDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "eventTypeName": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

_RequiredCreateModelVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
    },
)
_OptionalCreateModelVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelVersionRequestRequestTypeDef",
    {
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelVersionRequestRequestTypeDef(
    _RequiredCreateModelVersionRequestRequestTypeDef,
    _OptionalCreateModelVersionRequestRequestTypeDef,
):
    pass

CreateModelVersionResultTypeDef = TypedDict(
    "CreateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "ruleId": str,
        "detectorId": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass

CreateRuleResultTypeDef = TypedDict(
    "CreateRuleResultTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVariableRequestRequestTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
    },
)
_OptionalCreateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVariableRequestRequestTypeDef",
    {
        "description": str,
        "variableType": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVariableRequestRequestTypeDef(
    _RequiredCreateVariableRequestRequestTypeDef, _OptionalCreateVariableRequestRequestTypeDef
):
    pass

DataValidationMetricsTypeDef = TypedDict(
    "DataValidationMetricsTypeDef",
    {
        "fileLevelMessages": List["FileValidationMessageTypeDef"],
        "fieldLevelMessages": List["FieldValidationMessageTypeDef"],
    },
    total=False,
)

DeleteBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)

DeleteDetectorVersionRequestRequestTypeDef = TypedDict(
    "DeleteDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

DeleteEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEventRequestRequestTypeDef = TypedDict(
    "DeleteEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)

DeleteEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteExternalModelRequestRequestTypeDef = TypedDict(
    "DeleteExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
    },
)

DeleteLabelRequestRequestTypeDef = TypedDict(
    "DeleteLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
    },
)

DeleteModelVersionRequestRequestTypeDef = TypedDict(
    "DeleteModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)

DeleteOutcomeRequestRequestTypeDef = TypedDict(
    "DeleteOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
    },
)

DeleteVariableRequestRequestTypeDef = TypedDict(
    "DeleteVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredDescribeDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalDescribeDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeDetectorRequestRequestTypeDef(
    _RequiredDescribeDetectorRequestRequestTypeDef, _OptionalDescribeDetectorRequestRequestTypeDef
):
    pass

DescribeDetectorResultTypeDef = TypedDict(
    "DescribeDetectorResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List["DetectorVersionSummaryTypeDef"],
        "nextToken": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelVersionsRequestRequestTypeDef = TypedDict(
    "DescribeModelVersionsRequestRequestTypeDef",
    {
        "modelId": str,
        "modelVersionNumber": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeModelVersionsResultTypeDef = TypedDict(
    "DescribeModelVersionsResultTypeDef",
    {
        "modelVersionDetails": List["ModelVersionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorId": str,
        "description": str,
        "eventTypeName": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

DetectorVersionSummaryTypeDef = TypedDict(
    "DetectorVersionSummaryTypeDef",
    {
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "description": str,
        "lastUpdatedTime": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)

EntityTypeTypeDef = TypedDict(
    "EntityTypeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "name": str,
        "description": str,
        "eventVariables": List[str],
        "labels": List[str],
        "entityTypes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

ExternalEventsDetailTypeDef = TypedDict(
    "ExternalEventsDetailTypeDef",
    {
        "dataLocation": str,
        "dataAccessRoleArn": str,
    },
)

ExternalModelTypeDef = TypedDict(
    "ExternalModelTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": "ModelInputConfigurationTypeDef",
        "outputConfiguration": "ModelOutputConfigurationTypeDef",
        "modelEndpointStatus": ModelEndpointStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {
        "fieldName": str,
        "identifier": str,
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef",
    {
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

GetBatchPredictionJobsRequestRequestTypeDef = TypedDict(
    "GetBatchPredictionJobsRequestRequestTypeDef",
    {
        "jobId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetBatchPredictionJobsResultTypeDef = TypedDict(
    "GetBatchPredictionJobsResultTypeDef",
    {
        "batchPredictions": List["BatchPredictionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorVersionRequestRequestTypeDef = TypedDict(
    "GetDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

GetDetectorVersionResultTypeDef = TypedDict(
    "GetDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List["ModelVersionTypeDef"],
        "rules": List["RuleTypeDef"],
        "status": DetectorVersionStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "ruleExecutionMode": RuleExecutionModeType,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorsRequestRequestTypeDef = TypedDict(
    "GetDetectorsRequestRequestTypeDef",
    {
        "detectorId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetDetectorsResultTypeDef = TypedDict(
    "GetDetectorsResultTypeDef",
    {
        "detectors": List["DetectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEntityTypesRequestRequestTypeDef = TypedDict(
    "GetEntityTypesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEntityTypesResultTypeDef = TypedDict(
    "GetEntityTypesResultTypeDef",
    {
        "entityTypes": List["EntityTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEventPredictionRequestRequestTypeDef = TypedDict(
    "_RequiredGetEventPredictionRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventId": str,
        "eventTypeName": str,
        "entities": List["EntityTypeDef"],
        "eventTimestamp": str,
        "eventVariables": Dict[str, str],
    },
)
_OptionalGetEventPredictionRequestRequestTypeDef = TypedDict(
    "_OptionalGetEventPredictionRequestRequestTypeDef",
    {
        "detectorVersionId": str,
        "externalModelEndpointDataBlobs": Dict[str, "ModelEndpointDataBlobTypeDef"],
    },
    total=False,
)

class GetEventPredictionRequestRequestTypeDef(
    _RequiredGetEventPredictionRequestRequestTypeDef,
    _OptionalGetEventPredictionRequestRequestTypeDef,
):
    pass

GetEventPredictionResultTypeDef = TypedDict(
    "GetEventPredictionResultTypeDef",
    {
        "modelScores": List["ModelScoresTypeDef"],
        "ruleResults": List["RuleResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventTypesRequestRequestTypeDef = TypedDict(
    "GetEventTypesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEventTypesResultTypeDef = TypedDict(
    "GetEventTypesResultTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExternalModelsRequestRequestTypeDef = TypedDict(
    "GetExternalModelsRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetExternalModelsResultTypeDef = TypedDict(
    "GetExternalModelsResultTypeDef",
    {
        "externalModels": List["ExternalModelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKMSEncryptionKeyResultTypeDef = TypedDict(
    "GetKMSEncryptionKeyResultTypeDef",
    {
        "kmsKey": "KMSKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLabelsRequestRequestTypeDef = TypedDict(
    "GetLabelsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetLabelsResultTypeDef = TypedDict(
    "GetLabelsResultTypeDef",
    {
        "labels": List["LabelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelVersionRequestRequestTypeDef = TypedDict(
    "GetModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)

GetModelVersionResultTypeDef = TypedDict(
    "GetModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "status": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetModelsResultTypeDef = TypedDict(
    "GetModelsResultTypeDef",
    {
        "nextToken": str,
        "models": List["ModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutcomesRequestRequestTypeDef = TypedDict(
    "GetOutcomesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetOutcomesResultTypeDef = TypedDict(
    "GetOutcomesResultTypeDef",
    {
        "outcomes": List["OutcomeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRulesRequestRequestTypeDef = TypedDict(
    "_RequiredGetRulesRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalGetRulesRequestRequestTypeDef = TypedDict(
    "_OptionalGetRulesRequestRequestTypeDef",
    {
        "ruleId": str,
        "ruleVersion": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetRulesRequestRequestTypeDef(
    _RequiredGetRulesRequestRequestTypeDef, _OptionalGetRulesRequestRequestTypeDef
):
    pass

GetRulesResultTypeDef = TypedDict(
    "GetRulesResultTypeDef",
    {
        "ruleDetails": List["RuleDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVariablesRequestRequestTypeDef = TypedDict(
    "GetVariablesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetVariablesResultTypeDef = TypedDict(
    "GetVariablesResultTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KMSKeyTypeDef = TypedDict(
    "KMSKeyTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
    total=False,
)

LabelSchemaTypeDef = TypedDict(
    "LabelSchemaTypeDef",
    {
        "labelMapper": Dict[str, List[str]],
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogitMetricTypeDef = TypedDict(
    "LogitMetricTypeDef",
    {
        "variableName": str,
        "variableType": str,
        "variableImportance": float,
    },
)

MetricDataPointTypeDef = TypedDict(
    "MetricDataPointTypeDef",
    {
        "fpr": float,
        "precision": float,
        "tpr": float,
        "threshold": float,
    },
    total=False,
)

ModelEndpointDataBlobTypeDef = TypedDict(
    "ModelEndpointDataBlobTypeDef",
    {
        "byteBuffer": Union[bytes, IO[bytes], StreamingBody],
        "contentType": str,
    },
    total=False,
)

_RequiredModelInputConfigurationTypeDef = TypedDict(
    "_RequiredModelInputConfigurationTypeDef",
    {
        "useEventVariables": bool,
    },
)
_OptionalModelInputConfigurationTypeDef = TypedDict(
    "_OptionalModelInputConfigurationTypeDef",
    {
        "eventTypeName": str,
        "format": ModelInputDataFormatType,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)

class ModelInputConfigurationTypeDef(
    _RequiredModelInputConfigurationTypeDef, _OptionalModelInputConfigurationTypeDef
):
    pass

_RequiredModelOutputConfigurationTypeDef = TypedDict(
    "_RequiredModelOutputConfigurationTypeDef",
    {
        "format": ModelOutputDataFormatType,
    },
)
_OptionalModelOutputConfigurationTypeDef = TypedDict(
    "_OptionalModelOutputConfigurationTypeDef",
    {
        "jsonKeyToVariableMap": Dict[str, str],
        "csvIndexToVariableMap": Dict[str, str],
    },
    total=False,
)

class ModelOutputConfigurationTypeDef(
    _RequiredModelOutputConfigurationTypeDef, _OptionalModelOutputConfigurationTypeDef
):
    pass

ModelScoresTypeDef = TypedDict(
    "ModelScoresTypeDef",
    {
        "modelVersion": "ModelVersionTypeDef",
        "scores": Dict[str, float],
    },
    total=False,
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "description": str,
        "eventTypeName": str,
        "createdTime": str,
        "lastUpdatedTime": str,
        "arn": str,
    },
    total=False,
)

ModelVersionDetailTypeDef = TypedDict(
    "ModelVersionDetailTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "trainingResult": "TrainingResultTypeDef",
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredModelVersionTypeDef = TypedDict(
    "_RequiredModelVersionTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)
_OptionalModelVersionTypeDef = TypedDict(
    "_OptionalModelVersionTypeDef",
    {
        "arn": str,
    },
    total=False,
)

class ModelVersionTypeDef(_RequiredModelVersionTypeDef, _OptionalModelVersionTypeDef):
    pass

OutcomeTypeDef = TypedDict(
    "OutcomeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredPutDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredPutDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventTypeName": str,
    },
)
_OptionalPutDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalPutDetectorRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutDetectorRequestRequestTypeDef(
    _RequiredPutDetectorRequestRequestTypeDef, _OptionalPutDetectorRequestRequestTypeDef
):
    pass

_RequiredPutEntityTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutEntityTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutEntityTypeRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutEntityTypeRequestRequestTypeDef(
    _RequiredPutEntityTypeRequestRequestTypeDef, _OptionalPutEntityTypeRequestRequestTypeDef
):
    pass

_RequiredPutEventTypeRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventTypeRequestRequestTypeDef",
    {
        "name": str,
        "eventVariables": List[str],
        "entityTypes": List[str],
    },
)
_OptionalPutEventTypeRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventTypeRequestRequestTypeDef",
    {
        "description": str,
        "labels": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutEventTypeRequestRequestTypeDef(
    _RequiredPutEventTypeRequestRequestTypeDef, _OptionalPutEventTypeRequestRequestTypeDef
):
    pass

_RequiredPutExternalModelRequestRequestTypeDef = TypedDict(
    "_RequiredPutExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": "ModelInputConfigurationTypeDef",
        "outputConfiguration": "ModelOutputConfigurationTypeDef",
        "modelEndpointStatus": ModelEndpointStatusType,
    },
)
_OptionalPutExternalModelRequestRequestTypeDef = TypedDict(
    "_OptionalPutExternalModelRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutExternalModelRequestRequestTypeDef(
    _RequiredPutExternalModelRequestRequestTypeDef, _OptionalPutExternalModelRequestRequestTypeDef
):
    pass

PutKMSEncryptionKeyRequestRequestTypeDef = TypedDict(
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
)

_RequiredPutLabelRequestRequestTypeDef = TypedDict(
    "_RequiredPutLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutLabelRequestRequestTypeDef = TypedDict(
    "_OptionalPutLabelRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutLabelRequestRequestTypeDef(
    _RequiredPutLabelRequestRequestTypeDef, _OptionalPutLabelRequestRequestTypeDef
):
    pass

_RequiredPutOutcomeRequestRequestTypeDef = TypedDict(
    "_RequiredPutOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutOutcomeRequestRequestTypeDef = TypedDict(
    "_OptionalPutOutcomeRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutOutcomeRequestRequestTypeDef(
    _RequiredPutOutcomeRequestRequestTypeDef, _OptionalPutOutcomeRequestRequestTypeDef
):
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

RuleDetailTypeDef = TypedDict(
    "RuleDetailTypeDef",
    {
        "ruleId": str,
        "description": str,
        "detectorId": str,
        "ruleVersion": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "ruleId": str,
        "outcomes": List[str],
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "detectorId": str,
        "ruleId": str,
        "ruleVersion": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TrainingDataSchemaTypeDef = TypedDict(
    "TrainingDataSchemaTypeDef",
    {
        "modelVariables": List[str],
        "labelSchema": "LabelSchemaTypeDef",
    },
)

TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "auc": float,
        "metricDataPoints": List["MetricDataPointTypeDef"],
    },
    total=False,
)

TrainingResultTypeDef = TypedDict(
    "TrainingResultTypeDef",
    {
        "dataValidationMetrics": "DataValidationMetricsTypeDef",
        "trainingMetrics": "TrainingMetricsTypeDef",
        "variableImportanceMetrics": "VariableImportanceMetricsTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

UpdateDetectorVersionMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
    },
)

_RequiredUpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "externalModelEndpoints": List[str],
        "rules": List["RuleTypeDef"],
    },
)
_OptionalUpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorVersionRequestRequestTypeDef",
    {
        "description": str,
        "modelVersions": List["ModelVersionTypeDef"],
        "ruleExecutionMode": RuleExecutionModeType,
    },
    total=False,
)

class UpdateDetectorVersionRequestRequestTypeDef(
    _RequiredUpdateDetectorVersionRequestRequestTypeDef,
    _OptionalUpdateDetectorVersionRequestRequestTypeDef,
):
    pass

UpdateDetectorVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
    },
)

_RequiredUpdateModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
    },
)
_OptionalUpdateModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateModelRequestRequestTypeDef(
    _RequiredUpdateModelRequestRequestTypeDef, _OptionalUpdateModelRequestRequestTypeDef
):
    pass

_RequiredUpdateModelVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "majorVersionNumber": str,
    },
)
_OptionalUpdateModelVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelVersionRequestRequestTypeDef",
    {
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class UpdateModelVersionRequestRequestTypeDef(
    _RequiredUpdateModelVersionRequestRequestTypeDef,
    _OptionalUpdateModelVersionRequestRequestTypeDef,
):
    pass

UpdateModelVersionResultTypeDef = TypedDict(
    "UpdateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateModelVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionStatusRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": ModelVersionStatusType,
    },
)

UpdateRuleMetadataRequestRequestTypeDef = TypedDict(
    "UpdateRuleMetadataRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "description": str,
    },
)

_RequiredUpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleVersionRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
    },
)
_OptionalUpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleVersionRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class UpdateRuleVersionRequestRequestTypeDef(
    _RequiredUpdateRuleVersionRequestRequestTypeDef, _OptionalUpdateRuleVersionRequestRequestTypeDef
):
    pass

UpdateRuleVersionResultTypeDef = TypedDict(
    "UpdateRuleVersionResultTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVariableRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateVariableRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVariableRequestRequestTypeDef",
    {
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)

class UpdateVariableRequestRequestTypeDef(
    _RequiredUpdateVariableRequestRequestTypeDef, _OptionalUpdateVariableRequestRequestTypeDef
):
    pass

VariableEntryTypeDef = TypedDict(
    "VariableEntryTypeDef",
    {
        "name": str,
        "dataType": str,
        "dataSource": str,
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)

VariableImportanceMetricsTypeDef = TypedDict(
    "VariableImportanceMetricsTypeDef",
    {
        "LogitMetrics": List["LogitMetricTypeDef"],
    },
    total=False,
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
        "description": str,
        "variableType": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)
