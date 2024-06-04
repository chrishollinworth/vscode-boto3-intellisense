"""
Type annotations for bedrock service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock.type_defs import AutomatedEvaluationConfigTypeDef

    data: AutomatedEvaluationConfigTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CommitmentDurationType,
    CustomizationTypeType,
    EvaluationJobStatusType,
    EvaluationJobTypeType,
    EvaluationTaskTypeType,
    FineTuningJobStatusType,
    FoundationModelLifecycleStatusType,
    GuardrailContentFilterTypeType,
    GuardrailFilterStrengthType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationActionType,
    GuardrailStatusType,
    InferenceTypeType,
    ModelCustomizationJobStatusType,
    ModelCustomizationType,
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
    "AutomatedEvaluationConfigTypeDef",
    "CloudWatchConfigTypeDef",
    "CreateEvaluationJobRequestRequestTypeDef",
    "CreateEvaluationJobResponseTypeDef",
    "CreateGuardrailRequestRequestTypeDef",
    "CreateGuardrailResponseTypeDef",
    "CreateGuardrailVersionRequestRequestTypeDef",
    "CreateGuardrailVersionResponseTypeDef",
    "CreateModelCustomizationJobRequestRequestTypeDef",
    "CreateModelCustomizationJobResponseTypeDef",
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    "CreateProvisionedModelThroughputResponseTypeDef",
    "CustomModelSummaryTypeDef",
    "DeleteCustomModelRequestRequestTypeDef",
    "DeleteGuardrailRequestRequestTypeDef",
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    "EvaluationBedrockModelTypeDef",
    "EvaluationConfigTypeDef",
    "EvaluationDatasetLocationTypeDef",
    "EvaluationDatasetMetricConfigTypeDef",
    "EvaluationDatasetTypeDef",
    "EvaluationInferenceConfigTypeDef",
    "EvaluationModelConfigTypeDef",
    "EvaluationOutputDataConfigTypeDef",
    "EvaluationSummaryTypeDef",
    "FoundationModelDetailsTypeDef",
    "FoundationModelLifecycleTypeDef",
    "FoundationModelSummaryTypeDef",
    "GetCustomModelRequestRequestTypeDef",
    "GetCustomModelResponseTypeDef",
    "GetEvaluationJobRequestRequestTypeDef",
    "GetEvaluationJobResponseTypeDef",
    "GetFoundationModelRequestRequestTypeDef",
    "GetFoundationModelResponseTypeDef",
    "GetGuardrailRequestRequestTypeDef",
    "GetGuardrailResponseTypeDef",
    "GetModelCustomizationJobRequestRequestTypeDef",
    "GetModelCustomizationJobResponseTypeDef",
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    "GetProvisionedModelThroughputResponseTypeDef",
    "GuardrailContentFilterConfigTypeDef",
    "GuardrailContentFilterTypeDef",
    "GuardrailContentPolicyConfigTypeDef",
    "GuardrailContentPolicyTypeDef",
    "GuardrailManagedWordsConfigTypeDef",
    "GuardrailManagedWordsTypeDef",
    "GuardrailPiiEntityConfigTypeDef",
    "GuardrailPiiEntityTypeDef",
    "GuardrailRegexConfigTypeDef",
    "GuardrailRegexTypeDef",
    "GuardrailSensitiveInformationPolicyConfigTypeDef",
    "GuardrailSensitiveInformationPolicyTypeDef",
    "GuardrailSummaryTypeDef",
    "GuardrailTopicConfigTypeDef",
    "GuardrailTopicPolicyConfigTypeDef",
    "GuardrailTopicPolicyTypeDef",
    "GuardrailTopicTypeDef",
    "GuardrailWordConfigTypeDef",
    "GuardrailWordPolicyConfigTypeDef",
    "GuardrailWordPolicyTypeDef",
    "GuardrailWordTypeDef",
    "HumanEvaluationConfigTypeDef",
    "HumanEvaluationCustomMetricTypeDef",
    "HumanWorkflowConfigTypeDef",
    "ListCustomModelsRequestRequestTypeDef",
    "ListCustomModelsResponseTypeDef",
    "ListEvaluationJobsRequestRequestTypeDef",
    "ListEvaluationJobsResponseTypeDef",
    "ListFoundationModelsRequestRequestTypeDef",
    "ListFoundationModelsResponseTypeDef",
    "ListGuardrailsRequestRequestTypeDef",
    "ListGuardrailsResponseTypeDef",
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
    "StopEvaluationJobRequestRequestTypeDef",
    "StopModelCustomizationJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrainingDataConfigTypeDef",
    "TrainingMetricsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGuardrailRequestRequestTypeDef",
    "UpdateGuardrailResponseTypeDef",
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    "ValidationDataConfigTypeDef",
    "ValidatorMetricTypeDef",
    "ValidatorTypeDef",
    "VpcConfigTypeDef",
)

AutomatedEvaluationConfigTypeDef = TypedDict(
    "AutomatedEvaluationConfigTypeDef",
    {
        "datasetMetricConfigs": List["EvaluationDatasetMetricConfigTypeDef"],
    },
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

_RequiredCreateEvaluationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEvaluationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "roleArn": str,
        "evaluationConfig": "EvaluationConfigTypeDef",
        "inferenceConfig": "EvaluationInferenceConfigTypeDef",
        "outputDataConfig": "EvaluationOutputDataConfigTypeDef",
    },
)
_OptionalCreateEvaluationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEvaluationJobRequestRequestTypeDef",
    {
        "jobDescription": str,
        "clientRequestToken": str,
        "customerEncryptionKeyId": str,
        "jobTags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEvaluationJobRequestRequestTypeDef(
    _RequiredCreateEvaluationJobRequestRequestTypeDef,
    _OptionalCreateEvaluationJobRequestRequestTypeDef,
):
    pass

CreateEvaluationJobResponseTypeDef = TypedDict(
    "CreateEvaluationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGuardrailRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGuardrailRequestRequestTypeDef",
    {
        "name": str,
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
    },
)
_OptionalCreateGuardrailRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGuardrailRequestRequestTypeDef",
    {
        "description": str,
        "topicPolicyConfig": "GuardrailTopicPolicyConfigTypeDef",
        "contentPolicyConfig": "GuardrailContentPolicyConfigTypeDef",
        "wordPolicyConfig": "GuardrailWordPolicyConfigTypeDef",
        "sensitiveInformationPolicyConfig": "GuardrailSensitiveInformationPolicyConfigTypeDef",
        "kmsKeyId": str,
        "tags": List["TagTypeDef"],
        "clientRequestToken": str,
    },
    total=False,
)

class CreateGuardrailRequestRequestTypeDef(
    _RequiredCreateGuardrailRequestRequestTypeDef, _OptionalCreateGuardrailRequestRequestTypeDef
):
    pass

CreateGuardrailResponseTypeDef = TypedDict(
    "CreateGuardrailResponseTypeDef",
    {
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGuardrailVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGuardrailVersionRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
    },
)
_OptionalCreateGuardrailVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGuardrailVersionRequestRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
    },
    total=False,
)

class CreateGuardrailVersionRequestRequestTypeDef(
    _RequiredCreateGuardrailVersionRequestRequestTypeDef,
    _OptionalCreateGuardrailVersionRequestRequestTypeDef,
):
    pass

CreateGuardrailVersionResponseTypeDef = TypedDict(
    "CreateGuardrailVersionResponseTypeDef",
    {
        "guardrailId": str,
        "version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "customizationType": CustomizationTypeType,
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

_RequiredCustomModelSummaryTypeDef = TypedDict(
    "_RequiredCustomModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "creationTime": datetime,
        "baseModelArn": str,
        "baseModelName": str,
    },
)
_OptionalCustomModelSummaryTypeDef = TypedDict(
    "_OptionalCustomModelSummaryTypeDef",
    {
        "customizationType": CustomizationTypeType,
    },
    total=False,
)

class CustomModelSummaryTypeDef(
    _RequiredCustomModelSummaryTypeDef, _OptionalCustomModelSummaryTypeDef
):
    pass

DeleteCustomModelRequestRequestTypeDef = TypedDict(
    "DeleteCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)

_RequiredDeleteGuardrailRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
    },
)
_OptionalDeleteGuardrailRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteGuardrailRequestRequestTypeDef",
    {
        "guardrailVersion": str,
    },
    total=False,
)

class DeleteGuardrailRequestRequestTypeDef(
    _RequiredDeleteGuardrailRequestRequestTypeDef, _OptionalDeleteGuardrailRequestRequestTypeDef
):
    pass

DeleteProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)

EvaluationBedrockModelTypeDef = TypedDict(
    "EvaluationBedrockModelTypeDef",
    {
        "modelIdentifier": str,
        "inferenceParams": str,
    },
)

EvaluationConfigTypeDef = TypedDict(
    "EvaluationConfigTypeDef",
    {
        "automated": "AutomatedEvaluationConfigTypeDef",
        "human": "HumanEvaluationConfigTypeDef",
    },
    total=False,
)

EvaluationDatasetLocationTypeDef = TypedDict(
    "EvaluationDatasetLocationTypeDef",
    {
        "s3Uri": str,
    },
    total=False,
)

EvaluationDatasetMetricConfigTypeDef = TypedDict(
    "EvaluationDatasetMetricConfigTypeDef",
    {
        "taskType": EvaluationTaskTypeType,
        "dataset": "EvaluationDatasetTypeDef",
        "metricNames": List[str],
    },
)

_RequiredEvaluationDatasetTypeDef = TypedDict(
    "_RequiredEvaluationDatasetTypeDef",
    {
        "name": str,
    },
)
_OptionalEvaluationDatasetTypeDef = TypedDict(
    "_OptionalEvaluationDatasetTypeDef",
    {
        "datasetLocation": "EvaluationDatasetLocationTypeDef",
    },
    total=False,
)

class EvaluationDatasetTypeDef(
    _RequiredEvaluationDatasetTypeDef, _OptionalEvaluationDatasetTypeDef
):
    pass

EvaluationInferenceConfigTypeDef = TypedDict(
    "EvaluationInferenceConfigTypeDef",
    {
        "models": List["EvaluationModelConfigTypeDef"],
    },
    total=False,
)

EvaluationModelConfigTypeDef = TypedDict(
    "EvaluationModelConfigTypeDef",
    {
        "bedrockModel": "EvaluationBedrockModelTypeDef",
    },
    total=False,
)

EvaluationOutputDataConfigTypeDef = TypedDict(
    "EvaluationOutputDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)

EvaluationSummaryTypeDef = TypedDict(
    "EvaluationSummaryTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "status": EvaluationJobStatusType,
        "creationTime": datetime,
        "jobType": EvaluationJobTypeType,
        "evaluationTaskTypes": List[EvaluationTaskTypeType],
        "modelIdentifiers": List[str],
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
        "customizationsSupported": List[ModelCustomizationType],
        "inferenceTypesSupported": List[InferenceTypeType],
        "modelLifecycle": "FoundationModelLifecycleTypeDef",
    },
    total=False,
)

class FoundationModelDetailsTypeDef(
    _RequiredFoundationModelDetailsTypeDef, _OptionalFoundationModelDetailsTypeDef
):
    pass

FoundationModelLifecycleTypeDef = TypedDict(
    "FoundationModelLifecycleTypeDef",
    {
        "status": FoundationModelLifecycleStatusType,
    },
)

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
        "customizationsSupported": List[ModelCustomizationType],
        "inferenceTypesSupported": List[InferenceTypeType],
        "modelLifecycle": "FoundationModelLifecycleTypeDef",
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
        "customizationType": CustomizationTypeType,
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

GetEvaluationJobRequestRequestTypeDef = TypedDict(
    "GetEvaluationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)

GetEvaluationJobResponseTypeDef = TypedDict(
    "GetEvaluationJobResponseTypeDef",
    {
        "jobName": str,
        "status": EvaluationJobStatusType,
        "jobArn": str,
        "jobDescription": str,
        "roleArn": str,
        "customerEncryptionKeyId": str,
        "jobType": EvaluationJobTypeType,
        "evaluationConfig": "EvaluationConfigTypeDef",
        "inferenceConfig": "EvaluationInferenceConfigTypeDef",
        "outputDataConfig": "EvaluationOutputDataConfigTypeDef",
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "failureMessages": List[str],
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

_RequiredGetGuardrailRequestRequestTypeDef = TypedDict(
    "_RequiredGetGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
    },
)
_OptionalGetGuardrailRequestRequestTypeDef = TypedDict(
    "_OptionalGetGuardrailRequestRequestTypeDef",
    {
        "guardrailVersion": str,
    },
    total=False,
)

class GetGuardrailRequestRequestTypeDef(
    _RequiredGetGuardrailRequestRequestTypeDef, _OptionalGetGuardrailRequestRequestTypeDef
):
    pass

GetGuardrailResponseTypeDef = TypedDict(
    "GetGuardrailResponseTypeDef",
    {
        "name": str,
        "description": str,
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "status": GuardrailStatusType,
        "topicPolicy": "GuardrailTopicPolicyTypeDef",
        "contentPolicy": "GuardrailContentPolicyTypeDef",
        "wordPolicy": "GuardrailWordPolicyTypeDef",
        "sensitiveInformationPolicy": "GuardrailSensitiveInformationPolicyTypeDef",
        "createdAt": datetime,
        "updatedAt": datetime,
        "statusReasons": List[str],
        "failureRecommendations": List[str],
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
        "kmsKeyArn": str,
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
        "customizationType": CustomizationTypeType,
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

GuardrailContentFilterConfigTypeDef = TypedDict(
    "GuardrailContentFilterConfigTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "inputStrength": GuardrailFilterStrengthType,
        "outputStrength": GuardrailFilterStrengthType,
    },
)

GuardrailContentFilterTypeDef = TypedDict(
    "GuardrailContentFilterTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "inputStrength": GuardrailFilterStrengthType,
        "outputStrength": GuardrailFilterStrengthType,
    },
)

GuardrailContentPolicyConfigTypeDef = TypedDict(
    "GuardrailContentPolicyConfigTypeDef",
    {
        "filtersConfig": List["GuardrailContentFilterConfigTypeDef"],
    },
)

GuardrailContentPolicyTypeDef = TypedDict(
    "GuardrailContentPolicyTypeDef",
    {
        "filters": List["GuardrailContentFilterTypeDef"],
    },
    total=False,
)

GuardrailManagedWordsConfigTypeDef = TypedDict(
    "GuardrailManagedWordsConfigTypeDef",
    {
        "type": Literal["PROFANITY"],
    },
)

GuardrailManagedWordsTypeDef = TypedDict(
    "GuardrailManagedWordsTypeDef",
    {
        "type": Literal["PROFANITY"],
    },
)

GuardrailPiiEntityConfigTypeDef = TypedDict(
    "GuardrailPiiEntityConfigTypeDef",
    {
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationActionType,
    },
)

GuardrailPiiEntityTypeDef = TypedDict(
    "GuardrailPiiEntityTypeDef",
    {
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationActionType,
    },
)

_RequiredGuardrailRegexConfigTypeDef = TypedDict(
    "_RequiredGuardrailRegexConfigTypeDef",
    {
        "name": str,
        "pattern": str,
        "action": GuardrailSensitiveInformationActionType,
    },
)
_OptionalGuardrailRegexConfigTypeDef = TypedDict(
    "_OptionalGuardrailRegexConfigTypeDef",
    {
        "description": str,
    },
    total=False,
)

class GuardrailRegexConfigTypeDef(
    _RequiredGuardrailRegexConfigTypeDef, _OptionalGuardrailRegexConfigTypeDef
):
    pass

_RequiredGuardrailRegexTypeDef = TypedDict(
    "_RequiredGuardrailRegexTypeDef",
    {
        "name": str,
        "pattern": str,
        "action": GuardrailSensitiveInformationActionType,
    },
)
_OptionalGuardrailRegexTypeDef = TypedDict(
    "_OptionalGuardrailRegexTypeDef",
    {
        "description": str,
    },
    total=False,
)

class GuardrailRegexTypeDef(_RequiredGuardrailRegexTypeDef, _OptionalGuardrailRegexTypeDef):
    pass

GuardrailSensitiveInformationPolicyConfigTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyConfigTypeDef",
    {
        "piiEntitiesConfig": List["GuardrailPiiEntityConfigTypeDef"],
        "regexesConfig": List["GuardrailRegexConfigTypeDef"],
    },
    total=False,
)

GuardrailSensitiveInformationPolicyTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyTypeDef",
    {
        "piiEntities": List["GuardrailPiiEntityTypeDef"],
        "regexes": List["GuardrailRegexTypeDef"],
    },
    total=False,
)

_RequiredGuardrailSummaryTypeDef = TypedDict(
    "_RequiredGuardrailSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": GuardrailStatusType,
        "name": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalGuardrailSummaryTypeDef = TypedDict(
    "_OptionalGuardrailSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class GuardrailSummaryTypeDef(_RequiredGuardrailSummaryTypeDef, _OptionalGuardrailSummaryTypeDef):
    pass

_RequiredGuardrailTopicConfigTypeDef = TypedDict(
    "_RequiredGuardrailTopicConfigTypeDef",
    {
        "name": str,
        "definition": str,
        "type": Literal["DENY"],
    },
)
_OptionalGuardrailTopicConfigTypeDef = TypedDict(
    "_OptionalGuardrailTopicConfigTypeDef",
    {
        "examples": List[str],
    },
    total=False,
)

class GuardrailTopicConfigTypeDef(
    _RequiredGuardrailTopicConfigTypeDef, _OptionalGuardrailTopicConfigTypeDef
):
    pass

GuardrailTopicPolicyConfigTypeDef = TypedDict(
    "GuardrailTopicPolicyConfigTypeDef",
    {
        "topicsConfig": List["GuardrailTopicConfigTypeDef"],
    },
)

GuardrailTopicPolicyTypeDef = TypedDict(
    "GuardrailTopicPolicyTypeDef",
    {
        "topics": List["GuardrailTopicTypeDef"],
    },
)

_RequiredGuardrailTopicTypeDef = TypedDict(
    "_RequiredGuardrailTopicTypeDef",
    {
        "name": str,
        "definition": str,
    },
)
_OptionalGuardrailTopicTypeDef = TypedDict(
    "_OptionalGuardrailTopicTypeDef",
    {
        "examples": List[str],
        "type": Literal["DENY"],
    },
    total=False,
)

class GuardrailTopicTypeDef(_RequiredGuardrailTopicTypeDef, _OptionalGuardrailTopicTypeDef):
    pass

GuardrailWordConfigTypeDef = TypedDict(
    "GuardrailWordConfigTypeDef",
    {
        "text": str,
    },
)

GuardrailWordPolicyConfigTypeDef = TypedDict(
    "GuardrailWordPolicyConfigTypeDef",
    {
        "wordsConfig": List["GuardrailWordConfigTypeDef"],
        "managedWordListsConfig": List["GuardrailManagedWordsConfigTypeDef"],
    },
    total=False,
)

GuardrailWordPolicyTypeDef = TypedDict(
    "GuardrailWordPolicyTypeDef",
    {
        "words": List["GuardrailWordTypeDef"],
        "managedWordLists": List["GuardrailManagedWordsTypeDef"],
    },
    total=False,
)

GuardrailWordTypeDef = TypedDict(
    "GuardrailWordTypeDef",
    {
        "text": str,
    },
)

_RequiredHumanEvaluationConfigTypeDef = TypedDict(
    "_RequiredHumanEvaluationConfigTypeDef",
    {
        "datasetMetricConfigs": List["EvaluationDatasetMetricConfigTypeDef"],
    },
)
_OptionalHumanEvaluationConfigTypeDef = TypedDict(
    "_OptionalHumanEvaluationConfigTypeDef",
    {
        "humanWorkflowConfig": "HumanWorkflowConfigTypeDef",
        "customMetrics": List["HumanEvaluationCustomMetricTypeDef"],
    },
    total=False,
)

class HumanEvaluationConfigTypeDef(
    _RequiredHumanEvaluationConfigTypeDef, _OptionalHumanEvaluationConfigTypeDef
):
    pass

_RequiredHumanEvaluationCustomMetricTypeDef = TypedDict(
    "_RequiredHumanEvaluationCustomMetricTypeDef",
    {
        "name": str,
        "ratingMethod": str,
    },
)
_OptionalHumanEvaluationCustomMetricTypeDef = TypedDict(
    "_OptionalHumanEvaluationCustomMetricTypeDef",
    {
        "description": str,
    },
    total=False,
)

class HumanEvaluationCustomMetricTypeDef(
    _RequiredHumanEvaluationCustomMetricTypeDef, _OptionalHumanEvaluationCustomMetricTypeDef
):
    pass

_RequiredHumanWorkflowConfigTypeDef = TypedDict(
    "_RequiredHumanWorkflowConfigTypeDef",
    {
        "flowDefinitionArn": str,
    },
)
_OptionalHumanWorkflowConfigTypeDef = TypedDict(
    "_OptionalHumanWorkflowConfigTypeDef",
    {
        "instructions": str,
    },
    total=False,
)

class HumanWorkflowConfigTypeDef(
    _RequiredHumanWorkflowConfigTypeDef, _OptionalHumanWorkflowConfigTypeDef
):
    pass

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

ListEvaluationJobsRequestRequestTypeDef = TypedDict(
    "ListEvaluationJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": Union[datetime, str],
        "creationTimeBefore": Union[datetime, str],
        "statusEquals": EvaluationJobStatusType,
        "nameContains": str,
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["CreationTime"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

ListEvaluationJobsResponseTypeDef = TypedDict(
    "ListEvaluationJobsResponseTypeDef",
    {
        "nextToken": str,
        "jobSummaries": List["EvaluationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFoundationModelsRequestRequestTypeDef = TypedDict(
    "ListFoundationModelsRequestRequestTypeDef",
    {
        "byProvider": str,
        "byCustomizationType": ModelCustomizationType,
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

ListGuardrailsRequestRequestTypeDef = TypedDict(
    "ListGuardrailsRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListGuardrailsResponseTypeDef = TypedDict(
    "ListGuardrailsResponseTypeDef",
    {
        "guardrails": List["GuardrailSummaryTypeDef"],
        "nextToken": str,
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
        "customizationType": CustomizationTypeType,
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

StopEvaluationJobRequestRequestTypeDef = TypedDict(
    "StopEvaluationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)

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

_RequiredUpdateGuardrailRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "name": str,
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
    },
)
_OptionalUpdateGuardrailRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGuardrailRequestRequestTypeDef",
    {
        "description": str,
        "topicPolicyConfig": "GuardrailTopicPolicyConfigTypeDef",
        "contentPolicyConfig": "GuardrailContentPolicyConfigTypeDef",
        "wordPolicyConfig": "GuardrailWordPolicyConfigTypeDef",
        "sensitiveInformationPolicyConfig": "GuardrailSensitiveInformationPolicyConfigTypeDef",
        "kmsKeyId": str,
    },
    total=False,
)

class UpdateGuardrailRequestRequestTypeDef(
    _RequiredUpdateGuardrailRequestRequestTypeDef, _OptionalUpdateGuardrailRequestRequestTypeDef
):
    pass

UpdateGuardrailResponseTypeDef = TypedDict(
    "UpdateGuardrailResponseTypeDef",
    {
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
