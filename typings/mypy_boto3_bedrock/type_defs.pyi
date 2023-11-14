"""
Type annotations for bedrock service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock.type_defs import CloudWatchConfigTypeDef

    data: CloudWatchConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CommitmentDurationType,
    FineTuningJobStatusType,
    InferenceTypeType,
    ModelCustomizationJobStatusType,
    ModelModalityType,
    ProvisionedModelStatusType,
    SortOrderType,
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
    "CloudWatchConfigTypeDef",
    "CreateModelCustomizationJobRequestRequestTypeDef",
    "CreateModelCustomizationJobResponseTypeDef",
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    "CreateProvisionedModelThroughputResponseTypeDef",
    "CustomModelSummaryTypeDef",
    "DeleteCustomModelRequestRequestTypeDef",
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    "FoundationModelDetailsTypeDef",
    "FoundationModelSummaryTypeDef",
    "GetCustomModelRequestRequestTypeDef",
    "GetCustomModelResponseTypeDef",
    "GetFoundationModelRequestRequestTypeDef",
    "GetFoundationModelResponseTypeDef",
    "GetModelCustomizationJobRequestRequestTypeDef",
    "GetModelCustomizationJobResponseTypeDef",
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    "GetProvisionedModelThroughputResponseTypeDef",
    "ListCustomModelsRequestRequestTypeDef",
    "ListCustomModelsResponseTypeDef",
    "ListFoundationModelsRequestRequestTypeDef",
    "ListFoundationModelsResponseTypeDef",
    "ListModelCustomizationJobsRequestRequestTypeDef",
    "ListModelCustomizationJobsResponseTypeDef",
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    "ListProvisionedModelThroughputsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingConfigTypeDef",
    "ModelCustomizationJobSummaryTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedModelSummaryTypeDef",
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "StopModelCustomizationJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrainingDataConfigTypeDef",
    "TrainingMetricsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    "ValidationDataConfigTypeDef",
    "ValidatorMetricTypeDef",
    "ValidatorTypeDef",
    "VpcConfigTypeDef",
)

_RequiredCloudWatchConfigTypeDef = TypedDict(
    "_RequiredCloudWatchConfigTypeDef",
    {
        "logGroupName": str,
        "roleArn": str,
    },
)
_OptionalCloudWatchConfigTypeDef = TypedDict(
    "_OptionalCloudWatchConfigTypeDef",
    {
        "largeDataDeliveryS3Config": "S3ConfigTypeDef",
    },
    total=False,
)

class CloudWatchConfigTypeDef(_RequiredCloudWatchConfigTypeDef, _OptionalCloudWatchConfigTypeDef):
    pass

_RequiredCreateModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelCustomizationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "customModelName": str,
        "roleArn": str,
        "baseModelIdentifier": str,
        "trainingDataConfig": "TrainingDataConfigTypeDef",
        "outputDataConfig": "OutputDataConfigTypeDef",
        "hyperParameters": Dict[str, str],
    },
)
_OptionalCreateModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelCustomizationJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "customModelKmsKeyId": str,
        "jobTags": List["TagTypeDef"],
        "customModelTags": List["TagTypeDef"],
        "validationDataConfig": "ValidationDataConfigTypeDef",
        "vpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

class CreateModelCustomizationJobRequestRequestTypeDef(
    _RequiredCreateModelCustomizationJobRequestRequestTypeDef,
    _OptionalCreateModelCustomizationJobRequestRequestTypeDef,
):
    pass

CreateModelCustomizationJobResponseTypeDef = TypedDict(
    "CreateModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "modelUnits": int,
        "provisionedModelName": str,
        "modelId": str,
    },
)
_OptionalCreateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "commitmentDuration": CommitmentDurationType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProvisionedModelThroughputRequestRequestTypeDef(
    _RequiredCreateProvisionedModelThroughputRequestRequestTypeDef,
    _OptionalCreateProvisionedModelThroughputRequestRequestTypeDef,
):
    pass

CreateProvisionedModelThroughputResponseTypeDef = TypedDict(
    "CreateProvisionedModelThroughputResponseTypeDef",
    {
        "provisionedModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomModelSummaryTypeDef = TypedDict(
    "CustomModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "creationTime": datetime,
        "baseModelArn": str,
        "baseModelName": str,
    },
)

DeleteCustomModelRequestRequestTypeDef = TypedDict(
    "DeleteCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)

DeleteProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)

_RequiredFoundationModelDetailsTypeDef = TypedDict(
    "_RequiredFoundationModelDetailsTypeDef",
    {
        "modelArn": str,
        "modelId": str,
    },
)
_OptionalFoundationModelDetailsTypeDef = TypedDict(
    "_OptionalFoundationModelDetailsTypeDef",
    {
        "modelName": str,
        "providerName": str,
        "inputModalities": List[ModelModalityType],
        "outputModalities": List[ModelModalityType],
        "responseStreamingSupported": bool,
        "customizationsSupported": List[Literal["FINE_TUNING"]],
        "inferenceTypesSupported": List[InferenceTypeType],
    },
    total=False,
)

class FoundationModelDetailsTypeDef(
    _RequiredFoundationModelDetailsTypeDef, _OptionalFoundationModelDetailsTypeDef
):
    pass

_RequiredFoundationModelSummaryTypeDef = TypedDict(
    "_RequiredFoundationModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelId": str,
    },
)
_OptionalFoundationModelSummaryTypeDef = TypedDict(
    "_OptionalFoundationModelSummaryTypeDef",
    {
        "modelName": str,
        "providerName": str,
        "inputModalities": List[ModelModalityType],
        "outputModalities": List[ModelModalityType],
        "responseStreamingSupported": bool,
        "customizationsSupported": List[Literal["FINE_TUNING"]],
        "inferenceTypesSupported": List[InferenceTypeType],
    },
    total=False,
)

class FoundationModelSummaryTypeDef(
    _RequiredFoundationModelSummaryTypeDef, _OptionalFoundationModelSummaryTypeDef
):
    pass

GetCustomModelRequestRequestTypeDef = TypedDict(
    "GetCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)

GetCustomModelResponseTypeDef = TypedDict(
    "GetCustomModelResponseTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "jobName": str,
        "jobArn": str,
        "baseModelArn": str,
        "modelKmsKeyArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": "TrainingDataConfigTypeDef",
        "validationDataConfig": "ValidationDataConfigTypeDef",
        "outputDataConfig": "OutputDataConfigTypeDef",
        "trainingMetrics": "TrainingMetricsTypeDef",
        "validationMetrics": List["ValidatorMetricTypeDef"],
        "creationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFoundationModelRequestRequestTypeDef = TypedDict(
    "GetFoundationModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)

GetFoundationModelResponseTypeDef = TypedDict(
    "GetFoundationModelResponseTypeDef",
    {
        "modelDetails": "FoundationModelDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "GetModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)

GetModelCustomizationJobResponseTypeDef = TypedDict(
    "GetModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "outputModelName": str,
        "outputModelArn": str,
        "clientRequestToken": str,
        "roleArn": str,
        "status": ModelCustomizationJobStatusType,
        "failureMessage": str,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "baseModelArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": "TrainingDataConfigTypeDef",
        "validationDataConfig": "ValidationDataConfigTypeDef",
        "outputDataConfig": "OutputDataConfigTypeDef",
        "outputModelKmsKeyArn": str,
        "trainingMetrics": "TrainingMetricsTypeDef",
        "validationMetrics": List["ValidatorMetricTypeDef"],
        "vpcConfig": "VpcConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelInvocationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    {
        "loggingConfig": "LoggingConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)

GetProvisionedModelThroughputResponseTypeDef = TypedDict(
    "GetProvisionedModelThroughputResponseTypeDef",
    {
        "modelUnits": int,
        "desiredModelUnits": int,
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "failureMessage": str,
        "commitmentDuration": CommitmentDurationType,
        "commitmentExpirationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomModelsRequestRequestTypeDef = TypedDict(
    "ListCustomModelsRequestRequestTypeDef",
    {
        "creationTimeBefore": Union[datetime, str],
        "creationTimeAfter": Union[datetime, str],
        "nameContains": str,
        "baseModelArnEquals": str,
        "foundationModelArnEquals": str,
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["CreationTime"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

ListCustomModelsResponseTypeDef = TypedDict(
    "ListCustomModelsResponseTypeDef",
    {
        "nextToken": str,
        "modelSummaries": List["CustomModelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFoundationModelsRequestRequestTypeDef = TypedDict(
    "ListFoundationModelsRequestRequestTypeDef",
    {
        "byProvider": str,
        "byCustomizationType": Literal["FINE_TUNING"],
        "byOutputModality": ModelModalityType,
        "byInferenceType": InferenceTypeType,
    },
    total=False,
)

ListFoundationModelsResponseTypeDef = TypedDict(
    "ListFoundationModelsResponseTypeDef",
    {
        "modelSummaries": List["FoundationModelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelCustomizationJobsRequestRequestTypeDef = TypedDict(
    "ListModelCustomizationJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": Union[datetime, str],
        "creationTimeBefore": Union[datetime, str],
        "statusEquals": FineTuningJobStatusType,
        "nameContains": str,
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["CreationTime"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

ListModelCustomizationJobsResponseTypeDef = TypedDict(
    "ListModelCustomizationJobsResponseTypeDef",
    {
        "nextToken": str,
        "modelCustomizationJobSummaries": List["ModelCustomizationJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedModelThroughputsRequestRequestTypeDef = TypedDict(
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    {
        "creationTimeAfter": Union[datetime, str],
        "creationTimeBefore": Union[datetime, str],
        "statusEquals": ProvisionedModelStatusType,
        "modelArnEquals": str,
        "nameContains": str,
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["CreationTime"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

ListProvisionedModelThroughputsResponseTypeDef = TypedDict(
    "ListProvisionedModelThroughputsResponseTypeDef",
    {
        "nextToken": str,
        "provisionedModelSummaries": List["ProvisionedModelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "cloudWatchConfig": "CloudWatchConfigTypeDef",
        "s3Config": "S3ConfigTypeDef",
        "textDataDeliveryEnabled": bool,
        "imageDataDeliveryEnabled": bool,
        "embeddingDataDeliveryEnabled": bool,
    },
    total=False,
)

_RequiredModelCustomizationJobSummaryTypeDef = TypedDict(
    "_RequiredModelCustomizationJobSummaryTypeDef",
    {
        "jobArn": str,
        "baseModelArn": str,
        "jobName": str,
        "status": ModelCustomizationJobStatusType,
        "creationTime": datetime,
    },
)
_OptionalModelCustomizationJobSummaryTypeDef = TypedDict(
    "_OptionalModelCustomizationJobSummaryTypeDef",
    {
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "customModelArn": str,
        "customModelName": str,
    },
    total=False,
)

class ModelCustomizationJobSummaryTypeDef(
    _RequiredModelCustomizationJobSummaryTypeDef, _OptionalModelCustomizationJobSummaryTypeDef
):
    pass

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "s3Uri": str,
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

_RequiredProvisionedModelSummaryTypeDef = TypedDict(
    "_RequiredProvisionedModelSummaryTypeDef",
    {
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "modelUnits": int,
        "desiredModelUnits": int,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
    },
)
_OptionalProvisionedModelSummaryTypeDef = TypedDict(
    "_OptionalProvisionedModelSummaryTypeDef",
    {
        "commitmentDuration": CommitmentDurationType,
        "commitmentExpirationTime": datetime,
    },
    total=False,
)

class ProvisionedModelSummaryTypeDef(
    _RequiredProvisionedModelSummaryTypeDef, _OptionalProvisionedModelSummaryTypeDef
):
    pass

PutModelInvocationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
    {
        "loggingConfig": "LoggingConfigTypeDef",
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

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

StopModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "StopModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
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

TrainingDataConfigTypeDef = TypedDict(
    "TrainingDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)

TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "trainingLoss": float,
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

_RequiredUpdateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)
_OptionalUpdateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "desiredProvisionedModelName": str,
        "desiredModelId": str,
    },
    total=False,
)

class UpdateProvisionedModelThroughputRequestRequestTypeDef(
    _RequiredUpdateProvisionedModelThroughputRequestRequestTypeDef,
    _OptionalUpdateProvisionedModelThroughputRequestRequestTypeDef,
):
    pass

ValidationDataConfigTypeDef = TypedDict(
    "ValidationDataConfigTypeDef",
    {
        "validators": List["ValidatorTypeDef"],
    },
)

ValidatorMetricTypeDef = TypedDict(
    "ValidatorMetricTypeDef",
    {
        "validationLoss": float,
    },
    total=False,
)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "s3Uri": str,
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
)
