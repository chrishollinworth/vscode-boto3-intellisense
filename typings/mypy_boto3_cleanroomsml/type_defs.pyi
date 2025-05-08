"""
Type annotations for cleanroomsml service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cleanroomsml.type_defs import S3ConfigMapTypeDef

    data: S3ConfigMapTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AudienceExportJobStatusType,
    AudienceGenerationJobStatusType,
    AudienceModelStatusType,
    AudienceSizeTypeType,
    ColumnTypeType,
    InferenceInstanceTypeType,
    InstanceTypeType,
    LogsStatusType,
    MetricsStatusType,
    MLInputChannelStatusType,
    NoiseLevelTypeType,
    PolicyExistenceConditionType,
    SharedAudienceMetricsType,
    TagOnCreatePolicyType,
    TrainedModelExportFileTypeType,
    TrainedModelExportJobStatusType,
    TrainedModelInferenceJobStatusType,
    TrainedModelStatusType,
    WorkerComputeTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AudienceDestinationTypeDef",
    "AudienceExportJobSummaryTypeDef",
    "AudienceGenerationJobDataSourceOutputTypeDef",
    "AudienceGenerationJobDataSourceTypeDef",
    "AudienceGenerationJobDataSourceUnionTypeDef",
    "AudienceGenerationJobSummaryTypeDef",
    "AudienceModelSummaryTypeDef",
    "AudienceQualityMetricsTypeDef",
    "AudienceSizeConfigOutputTypeDef",
    "AudienceSizeConfigTypeDef",
    "AudienceSizeConfigUnionTypeDef",
    "AudienceSizeTypeDef",
    "CancelTrainedModelInferenceJobRequestTypeDef",
    "CancelTrainedModelRequestTypeDef",
    "CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef",
    "CollaborationMLInputChannelSummaryTypeDef",
    "CollaborationTrainedModelExportJobSummaryTypeDef",
    "CollaborationTrainedModelInferenceJobSummaryTypeDef",
    "CollaborationTrainedModelSummaryTypeDef",
    "ColumnSchemaOutputTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnSchemaUnionTypeDef",
    "ComputeConfigurationTypeDef",
    "ConfiguredAudienceModelOutputConfigTypeDef",
    "ConfiguredAudienceModelSummaryTypeDef",
    "ConfiguredModelAlgorithmAssociationSummaryTypeDef",
    "ConfiguredModelAlgorithmSummaryTypeDef",
    "ContainerConfigOutputTypeDef",
    "ContainerConfigTypeDef",
    "ContainerConfigUnionTypeDef",
    "CreateAudienceModelRequestTypeDef",
    "CreateAudienceModelResponseTypeDef",
    "CreateConfiguredAudienceModelRequestTypeDef",
    "CreateConfiguredAudienceModelResponseTypeDef",
    "CreateConfiguredModelAlgorithmAssociationRequestTypeDef",
    "CreateConfiguredModelAlgorithmAssociationResponseTypeDef",
    "CreateConfiguredModelAlgorithmRequestTypeDef",
    "CreateConfiguredModelAlgorithmResponseTypeDef",
    "CreateMLInputChannelRequestTypeDef",
    "CreateMLInputChannelResponseTypeDef",
    "CreateTrainedModelRequestTypeDef",
    "CreateTrainedModelResponseTypeDef",
    "CreateTrainingDatasetRequestTypeDef",
    "CreateTrainingDatasetResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetInputConfigOutputTypeDef",
    "DatasetInputConfigTypeDef",
    "DatasetInputConfigUnionTypeDef",
    "DatasetOutputTypeDef",
    "DatasetTypeDef",
    "DatasetUnionTypeDef",
    "DeleteAudienceGenerationJobRequestTypeDef",
    "DeleteAudienceModelRequestTypeDef",
    "DeleteConfiguredAudienceModelPolicyRequestTypeDef",
    "DeleteConfiguredAudienceModelRequestTypeDef",
    "DeleteConfiguredModelAlgorithmAssociationRequestTypeDef",
    "DeleteConfiguredModelAlgorithmRequestTypeDef",
    "DeleteMLConfigurationRequestTypeDef",
    "DeleteMLInputChannelDataRequestTypeDef",
    "DeleteTrainedModelOutputRequestTypeDef",
    "DeleteTrainingDatasetRequestTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAudienceGenerationJobRequestTypeDef",
    "GetAudienceGenerationJobResponseTypeDef",
    "GetAudienceModelRequestTypeDef",
    "GetAudienceModelResponseTypeDef",
    "GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef",
    "GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef",
    "GetCollaborationMLInputChannelRequestTypeDef",
    "GetCollaborationMLInputChannelResponseTypeDef",
    "GetCollaborationTrainedModelRequestTypeDef",
    "GetCollaborationTrainedModelResponseTypeDef",
    "GetConfiguredAudienceModelPolicyRequestTypeDef",
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    "GetConfiguredAudienceModelRequestTypeDef",
    "GetConfiguredAudienceModelResponseTypeDef",
    "GetConfiguredModelAlgorithmAssociationRequestTypeDef",
    "GetConfiguredModelAlgorithmAssociationResponseTypeDef",
    "GetConfiguredModelAlgorithmRequestTypeDef",
    "GetConfiguredModelAlgorithmResponseTypeDef",
    "GetMLConfigurationRequestTypeDef",
    "GetMLConfigurationResponseTypeDef",
    "GetMLInputChannelRequestTypeDef",
    "GetMLInputChannelResponseTypeDef",
    "GetTrainedModelInferenceJobRequestTypeDef",
    "GetTrainedModelInferenceJobResponseTypeDef",
    "GetTrainedModelRequestTypeDef",
    "GetTrainedModelResponseTypeDef",
    "GetTrainingDatasetRequestTypeDef",
    "GetTrainingDatasetResponseTypeDef",
    "GlueDataSourceTypeDef",
    "InferenceContainerConfigTypeDef",
    "InferenceContainerExecutionParametersTypeDef",
    "InferenceOutputConfigurationOutputTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "InferenceOutputConfigurationUnionTypeDef",
    "InferenceReceiverMemberTypeDef",
    "InferenceResourceConfigTypeDef",
    "InputChannelDataSourceOutputTypeDef",
    "InputChannelDataSourceTypeDef",
    "InputChannelOutputTypeDef",
    "InputChannelTypeDef",
    "InputChannelUnionTypeDef",
    "ListAudienceExportJobsRequestPaginateTypeDef",
    "ListAudienceExportJobsRequestTypeDef",
    "ListAudienceExportJobsResponseTypeDef",
    "ListAudienceGenerationJobsRequestPaginateTypeDef",
    "ListAudienceGenerationJobsRequestTypeDef",
    "ListAudienceGenerationJobsResponseTypeDef",
    "ListAudienceModelsRequestPaginateTypeDef",
    "ListAudienceModelsRequestTypeDef",
    "ListAudienceModelsResponseTypeDef",
    "ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef",
    "ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef",
    "ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef",
    "ListCollaborationMLInputChannelsRequestPaginateTypeDef",
    "ListCollaborationMLInputChannelsRequestTypeDef",
    "ListCollaborationMLInputChannelsResponseTypeDef",
    "ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef",
    "ListCollaborationTrainedModelExportJobsRequestTypeDef",
    "ListCollaborationTrainedModelExportJobsResponseTypeDef",
    "ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef",
    "ListCollaborationTrainedModelInferenceJobsRequestTypeDef",
    "ListCollaborationTrainedModelInferenceJobsResponseTypeDef",
    "ListCollaborationTrainedModelsRequestPaginateTypeDef",
    "ListCollaborationTrainedModelsRequestTypeDef",
    "ListCollaborationTrainedModelsResponseTypeDef",
    "ListConfiguredAudienceModelsRequestPaginateTypeDef",
    "ListConfiguredAudienceModelsRequestTypeDef",
    "ListConfiguredAudienceModelsResponseTypeDef",
    "ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef",
    "ListConfiguredModelAlgorithmAssociationsRequestTypeDef",
    "ListConfiguredModelAlgorithmAssociationsResponseTypeDef",
    "ListConfiguredModelAlgorithmsRequestPaginateTypeDef",
    "ListConfiguredModelAlgorithmsRequestTypeDef",
    "ListConfiguredModelAlgorithmsResponseTypeDef",
    "ListMLInputChannelsRequestPaginateTypeDef",
    "ListMLInputChannelsRequestTypeDef",
    "ListMLInputChannelsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrainedModelInferenceJobsRequestPaginateTypeDef",
    "ListTrainedModelInferenceJobsRequestTypeDef",
    "ListTrainedModelInferenceJobsResponseTypeDef",
    "ListTrainedModelsRequestPaginateTypeDef",
    "ListTrainedModelsRequestTypeDef",
    "ListTrainedModelsResponseTypeDef",
    "ListTrainingDatasetsRequestPaginateTypeDef",
    "ListTrainingDatasetsRequestTypeDef",
    "ListTrainingDatasetsResponseTypeDef",
    "LogsConfigurationPolicyOutputTypeDef",
    "LogsConfigurationPolicyTypeDef",
    "MLInputChannelSummaryTypeDef",
    "MLOutputConfigurationTypeDef",
    "MetricDefinitionTypeDef",
    "MetricsConfigurationPolicyTypeDef",
    "ModelInferenceDataSourceTypeDef",
    "ModelTrainingDataChannelTypeDef",
    "PaginatorConfigTypeDef",
    "PrivacyConfigurationOutputTypeDef",
    "PrivacyConfigurationPoliciesOutputTypeDef",
    "PrivacyConfigurationPoliciesTypeDef",
    "PrivacyConfigurationTypeDef",
    "PrivacyConfigurationUnionTypeDef",
    "ProtectedQueryInputParametersOutputTypeDef",
    "ProtectedQueryInputParametersTypeDef",
    "ProtectedQuerySQLParametersOutputTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "PutConfiguredAudienceModelPolicyRequestTypeDef",
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    "PutMLConfigurationRequestTypeDef",
    "RelevanceMetricTypeDef",
    "ResourceConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigMapTypeDef",
    "StartAudienceExportJobRequestTypeDef",
    "StartAudienceGenerationJobRequestTypeDef",
    "StartAudienceGenerationJobResponseTypeDef",
    "StartTrainedModelExportJobRequestTypeDef",
    "StartTrainedModelInferenceJobRequestTypeDef",
    "StartTrainedModelInferenceJobResponseTypeDef",
    "StatusDetailsTypeDef",
    "StoppingConditionTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "TrainedModelExportOutputConfigurationOutputTypeDef",
    "TrainedModelExportOutputConfigurationTypeDef",
    "TrainedModelExportOutputConfigurationUnionTypeDef",
    "TrainedModelExportReceiverMemberTypeDef",
    "TrainedModelExportsConfigurationPolicyOutputTypeDef",
    "TrainedModelExportsConfigurationPolicyTypeDef",
    "TrainedModelExportsMaxSizeTypeDef",
    "TrainedModelInferenceJobSummaryTypeDef",
    "TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef",
    "TrainedModelInferenceJobsConfigurationPolicyTypeDef",
    "TrainedModelInferenceMaxOutputSizeTypeDef",
    "TrainedModelSummaryTypeDef",
    "TrainedModelsConfigurationPolicyOutputTypeDef",
    "TrainedModelsConfigurationPolicyTypeDef",
    "TrainingDatasetSummaryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConfiguredAudienceModelRequestTypeDef",
    "UpdateConfiguredAudienceModelResponseTypeDef",
    "WorkerComputeConfigurationTypeDef",
)

class S3ConfigMapTypeDef(TypedDict):
    s3Uri: str

AudienceSizeTypeDef = TypedDict(
    "AudienceSizeTypeDef",
    {
        "type": AudienceSizeTypeType,
        "value": int,
    },
)

class StatusDetailsTypeDef(TypedDict):
    statusCode: NotRequired[str]
    message: NotRequired[str]

class ProtectedQuerySQLParametersOutputTypeDef(TypedDict):
    queryString: NotRequired[str]
    analysisTemplateArn: NotRequired[str]
    parameters: NotRequired[Dict[str, str]]

class ProtectedQuerySQLParametersTypeDef(TypedDict):
    queryString: NotRequired[str]
    analysisTemplateArn: NotRequired[str]
    parameters: NotRequired[Mapping[str, str]]

class AudienceGenerationJobSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    status: AudienceGenerationJobStatusType
    configuredAudienceModelArn: str
    description: NotRequired[str]
    collaborationId: NotRequired[str]
    startedBy: NotRequired[str]

class AudienceModelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    description: NotRequired[str]

class AudienceSizeConfigOutputTypeDef(TypedDict):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: List[int]

class AudienceSizeConfigTypeDef(TypedDict):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: Sequence[int]

class CancelTrainedModelInferenceJobRequestTypeDef(TypedDict):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str

class CancelTrainedModelRequestTypeDef(TypedDict):
    membershipIdentifier: str
    trainedModelArn: str

class CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    creatorAccountId: str
    description: NotRequired[str]

class CollaborationMLInputChannelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    mlInputChannelArn: str
    status: MLInputChannelStatusType
    creatorAccountId: str
    description: NotRequired[str]

class CollaborationTrainedModelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainedModelArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    status: TrainedModelStatusType
    configuredModelAlgorithmAssociationArn: str
    creatorAccountId: str
    description: NotRequired[str]

class ColumnSchemaOutputTypeDef(TypedDict):
    columnName: str
    columnTypes: List[ColumnTypeType]

class ColumnSchemaTypeDef(TypedDict):
    columnName: str
    columnTypes: Sequence[ColumnTypeType]

WorkerComputeConfigurationTypeDef = TypedDict(
    "WorkerComputeConfigurationTypeDef",
    {
        "type": NotRequired[WorkerComputeTypeType],
        "number": NotRequired[int],
    },
)

class ConfiguredModelAlgorithmAssociationSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    configuredModelAlgorithmArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    description: NotRequired[str]

class ConfiguredModelAlgorithmSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    description: NotRequired[str]

class MetricDefinitionTypeDef(TypedDict):
    name: str
    regex: str

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class InferenceContainerConfigTypeDef(TypedDict):
    imageUri: str

class ModelTrainingDataChannelTypeDef(TypedDict):
    mlInputChannelArn: str
    channelName: str

class ResourceConfigTypeDef(TypedDict):
    instanceType: InstanceTypeType
    volumeSizeInGB: int
    instanceCount: NotRequired[int]

class StoppingConditionTypeDef(TypedDict):
    maxRuntimeInSeconds: NotRequired[int]

class GlueDataSourceTypeDef(TypedDict):
    tableName: str
    databaseName: str
    catalogId: NotRequired[str]

class DeleteAudienceGenerationJobRequestTypeDef(TypedDict):
    audienceGenerationJobArn: str

class DeleteAudienceModelRequestTypeDef(TypedDict):
    audienceModelArn: str

class DeleteConfiguredAudienceModelPolicyRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str

class DeleteConfiguredAudienceModelRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str

class DeleteConfiguredModelAlgorithmAssociationRequestTypeDef(TypedDict):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str

class DeleteConfiguredModelAlgorithmRequestTypeDef(TypedDict):
    configuredModelAlgorithmArn: str

class DeleteMLConfigurationRequestTypeDef(TypedDict):
    membershipIdentifier: str

class DeleteMLInputChannelDataRequestTypeDef(TypedDict):
    mlInputChannelArn: str
    membershipIdentifier: str

class DeleteTrainedModelOutputRequestTypeDef(TypedDict):
    trainedModelArn: str
    membershipIdentifier: str

class DeleteTrainingDatasetRequestTypeDef(TypedDict):
    trainingDatasetArn: str

class GetAudienceGenerationJobRequestTypeDef(TypedDict):
    audienceGenerationJobArn: str

class GetAudienceModelRequestTypeDef(TypedDict):
    audienceModelArn: str

class GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef(TypedDict):
    configuredModelAlgorithmAssociationArn: str
    collaborationIdentifier: str

class GetCollaborationMLInputChannelRequestTypeDef(TypedDict):
    mlInputChannelArn: str
    collaborationIdentifier: str

class GetCollaborationTrainedModelRequestTypeDef(TypedDict):
    trainedModelArn: str
    collaborationIdentifier: str

class GetConfiguredAudienceModelPolicyRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str

class GetConfiguredAudienceModelRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str

class GetConfiguredModelAlgorithmAssociationRequestTypeDef(TypedDict):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str

class GetConfiguredModelAlgorithmRequestTypeDef(TypedDict):
    configuredModelAlgorithmArn: str

class GetMLConfigurationRequestTypeDef(TypedDict):
    membershipIdentifier: str

class GetMLInputChannelRequestTypeDef(TypedDict):
    mlInputChannelArn: str
    membershipIdentifier: str

class GetTrainedModelInferenceJobRequestTypeDef(TypedDict):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str

class InferenceContainerExecutionParametersTypeDef(TypedDict):
    maxPayloadInMB: NotRequired[int]

class InferenceResourceConfigTypeDef(TypedDict):
    instanceType: InferenceInstanceTypeType
    instanceCount: NotRequired[int]

class ModelInferenceDataSourceTypeDef(TypedDict):
    mlInputChannelArn: str

class GetTrainedModelRequestTypeDef(TypedDict):
    trainedModelArn: str
    membershipIdentifier: str

class GetTrainingDatasetRequestTypeDef(TypedDict):
    trainingDatasetArn: str

class InferenceReceiverMemberTypeDef(TypedDict):
    accountId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAudienceExportJobsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    audienceGenerationJobArn: NotRequired[str]

class ListAudienceGenerationJobsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    configuredAudienceModelArn: NotRequired[str]
    collaborationId: NotRequired[str]

class ListAudienceModelsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationMLInputChannelsRequestTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationTrainedModelExportJobsRequestTypeDef(TypedDict):
    collaborationIdentifier: str
    trainedModelArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListCollaborationTrainedModelInferenceJobsRequestTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    trainedModelArn: NotRequired[str]

class ListCollaborationTrainedModelsRequestTypeDef(TypedDict):
    collaborationIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListConfiguredAudienceModelsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListConfiguredModelAlgorithmAssociationsRequestTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListConfiguredModelAlgorithmsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMLInputChannelsRequestTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MLInputChannelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    mlInputChannelArn: str
    status: MLInputChannelStatusType
    protectedQueryIdentifier: NotRequired[str]
    description: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTrainedModelInferenceJobsRequestTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    trainedModelArn: NotRequired[str]

class ListTrainedModelsRequestTypeDef(TypedDict):
    membershipIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TrainedModelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainedModelArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    status: TrainedModelStatusType
    configuredModelAlgorithmAssociationArn: str
    description: NotRequired[str]

class ListTrainingDatasetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TrainingDatasetSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    status: Literal["ACTIVE"]
    description: NotRequired[str]

class LogsConfigurationPolicyOutputTypeDef(TypedDict):
    allowedAccountIds: List[str]
    filterPattern: NotRequired[str]

class LogsConfigurationPolicyTypeDef(TypedDict):
    allowedAccountIds: Sequence[str]
    filterPattern: NotRequired[str]

class MetricsConfigurationPolicyTypeDef(TypedDict):
    noiseLevel: NoiseLevelTypeType

class PutConfiguredAudienceModelPolicyRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    previousPolicyHash: NotRequired[str]
    policyExistenceCondition: NotRequired[PolicyExistenceConditionType]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TrainedModelExportReceiverMemberTypeDef(TypedDict):
    accountId: str

class TrainedModelExportsMaxSizeTypeDef(TypedDict):
    unit: Literal["GB"]
    value: float

class TrainedModelInferenceMaxOutputSizeTypeDef(TypedDict):
    unit: Literal["GB"]
    value: float

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class AudienceDestinationTypeDef(TypedDict):
    s3Destination: S3ConfigMapTypeDef

class DestinationTypeDef(TypedDict):
    s3Destination: S3ConfigMapTypeDef

class RelevanceMetricTypeDef(TypedDict):
    audienceSize: AudienceSizeTypeDef
    score: NotRequired[float]

class StartAudienceExportJobRequestTypeDef(TypedDict):
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    description: NotRequired[str]

class AudienceExportJobSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    status: AudienceExportJobStatusType
    description: NotRequired[str]
    statusDetails: NotRequired[StatusDetailsTypeDef]
    outputLocation: NotRequired[str]

AudienceSizeConfigUnionTypeDef = Union[AudienceSizeConfigTypeDef, AudienceSizeConfigOutputTypeDef]
ColumnSchemaUnionTypeDef = Union[ColumnSchemaTypeDef, ColumnSchemaOutputTypeDef]

class ComputeConfigurationTypeDef(TypedDict):
    worker: NotRequired[WorkerComputeConfigurationTypeDef]

class ContainerConfigOutputTypeDef(TypedDict):
    imageUri: str
    entrypoint: NotRequired[List[str]]
    arguments: NotRequired[List[str]]
    metricDefinitions: NotRequired[List[MetricDefinitionTypeDef]]

class ContainerConfigTypeDef(TypedDict):
    imageUri: str
    entrypoint: NotRequired[Sequence[str]]
    arguments: NotRequired[Sequence[str]]
    metricDefinitions: NotRequired[Sequence[MetricDefinitionTypeDef]]

class CreateAudienceModelRequestTypeDef(TypedDict):
    name: str
    trainingDatasetArn: str
    trainingDataStartTime: NotRequired[TimestampTypeDef]
    trainingDataEndTime: NotRequired[TimestampTypeDef]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    description: NotRequired[str]

class CreateAudienceModelResponseTypeDef(TypedDict):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredAudienceModelResponseTypeDef(TypedDict):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredModelAlgorithmAssociationResponseTypeDef(TypedDict):
    configuredModelAlgorithmAssociationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredModelAlgorithmResponseTypeDef(TypedDict):
    configuredModelAlgorithmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLInputChannelResponseTypeDef(TypedDict):
    mlInputChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainedModelResponseTypeDef(TypedDict):
    trainedModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingDatasetResponseTypeDef(TypedDict):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAudienceModelResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainingDataStartTime: datetime
    trainingDataEndTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    statusDetails: StatusDetailsTypeDef
    kmsKeyArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationMLInputChannelResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    membershipIdentifier: str
    collaborationIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetailsTypeDef
    retentionInDays: int
    numberOfRecords: int
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredAudienceModelPolicyResponseTypeDef(TypedDict):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAudienceGenerationJobsResponseTypeDef(TypedDict):
    audienceGenerationJobs: List[AudienceGenerationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAudienceModelsResponseTypeDef(TypedDict):
    audienceModels: List[AudienceModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef(TypedDict):
    collaborationConfiguredModelAlgorithmAssociations: List[
        CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCollaborationMLInputChannelsResponseTypeDef(TypedDict):
    collaborationMLInputChannelsList: List[CollaborationMLInputChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCollaborationTrainedModelsResponseTypeDef(TypedDict):
    collaborationTrainedModels: List[CollaborationTrainedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListConfiguredModelAlgorithmAssociationsResponseTypeDef(TypedDict):
    configuredModelAlgorithmAssociations: List[ConfiguredModelAlgorithmAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListConfiguredModelAlgorithmsResponseTypeDef(TypedDict):
    configuredModelAlgorithms: List[ConfiguredModelAlgorithmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfiguredAudienceModelPolicyResponseTypeDef(TypedDict):
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAudienceGenerationJobResponseTypeDef(TypedDict):
    audienceGenerationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTrainedModelInferenceJobResponseTypeDef(TypedDict):
    trainedModelInferenceJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelResponseTypeDef(TypedDict):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainedModelRequestTypeDef(TypedDict):
    membershipIdentifier: str
    name: str
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    dataChannels: Sequence[ModelTrainingDataChannelTypeDef]
    hyperparameters: NotRequired[Mapping[str, str]]
    environment: NotRequired[Mapping[str, str]]
    stoppingCondition: NotRequired[StoppingConditionTypeDef]
    description: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class GetCollaborationTrainedModelResponseTypeDef(TypedDict):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetailsTypeDef
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    stoppingCondition: StoppingConditionTypeDef
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    trainingContainerImageDigest: str
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrainedModelResponseTypeDef(TypedDict):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetailsTypeDef
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    stoppingCondition: StoppingConditionTypeDef
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    trainingContainerImageDigest: str
    createTime: datetime
    updateTime: datetime
    hyperparameters: Dict[str, str]
    environment: Dict[str, str]
    kmsKeyArn: str
    tags: Dict[str, str]
    dataChannels: List[ModelTrainingDataChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceTypeDef(TypedDict):
    glueDataSource: GlueDataSourceTypeDef

class InferenceOutputConfigurationOutputTypeDef(TypedDict):
    members: List[InferenceReceiverMemberTypeDef]
    accept: NotRequired[str]

class InferenceOutputConfigurationTypeDef(TypedDict):
    members: Sequence[InferenceReceiverMemberTypeDef]
    accept: NotRequired[str]

class ListAudienceExportJobsRequestPaginateTypeDef(TypedDict):
    audienceGenerationJobArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAudienceGenerationJobsRequestPaginateTypeDef(TypedDict):
    configuredAudienceModelArn: NotRequired[str]
    collaborationId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAudienceModelsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationMLInputChannelsRequestPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    trainedModelArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    trainedModelArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollaborationTrainedModelsRequestPaginateTypeDef(TypedDict):
    collaborationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredAudienceModelsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfiguredModelAlgorithmsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMLInputChannelsRequestPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrainedModelInferenceJobsRequestPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    trainedModelArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrainedModelsRequestPaginateTypeDef(TypedDict):
    membershipIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrainingDatasetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMLInputChannelsResponseTypeDef(TypedDict):
    mlInputChannelsList: List[MLInputChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTrainedModelsResponseTypeDef(TypedDict):
    trainedModels: List[TrainedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTrainingDatasetsResponseTypeDef(TypedDict):
    trainingDatasets: List[TrainingDatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TrainedModelsConfigurationPolicyOutputTypeDef(TypedDict):
    containerLogs: NotRequired[List[LogsConfigurationPolicyOutputTypeDef]]
    containerMetrics: NotRequired[MetricsConfigurationPolicyTypeDef]

class TrainedModelsConfigurationPolicyTypeDef(TypedDict):
    containerLogs: NotRequired[Sequence[LogsConfigurationPolicyTypeDef]]
    containerMetrics: NotRequired[MetricsConfigurationPolicyTypeDef]

class TrainedModelExportOutputConfigurationOutputTypeDef(TypedDict):
    members: List[TrainedModelExportReceiverMemberTypeDef]

class TrainedModelExportOutputConfigurationTypeDef(TypedDict):
    members: Sequence[TrainedModelExportReceiverMemberTypeDef]

class TrainedModelExportsConfigurationPolicyOutputTypeDef(TypedDict):
    maxSize: TrainedModelExportsMaxSizeTypeDef
    filesToExport: List[TrainedModelExportFileTypeType]

class TrainedModelExportsConfigurationPolicyTypeDef(TypedDict):
    maxSize: TrainedModelExportsMaxSizeTypeDef
    filesToExport: Sequence[TrainedModelExportFileTypeType]

class TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef(TypedDict):
    containerLogs: NotRequired[List[LogsConfigurationPolicyOutputTypeDef]]
    maxOutputSize: NotRequired[TrainedModelInferenceMaxOutputSizeTypeDef]

class TrainedModelInferenceJobsConfigurationPolicyTypeDef(TypedDict):
    containerLogs: NotRequired[Sequence[LogsConfigurationPolicyTypeDef]]
    maxOutputSize: NotRequired[TrainedModelInferenceMaxOutputSizeTypeDef]

class ConfiguredAudienceModelOutputConfigTypeDef(TypedDict):
    destination: AudienceDestinationTypeDef
    roleArn: str

class MLOutputConfigurationTypeDef(TypedDict):
    roleArn: str
    destination: NotRequired[DestinationTypeDef]

class AudienceQualityMetricsTypeDef(TypedDict):
    relevanceMetrics: List[RelevanceMetricTypeDef]
    recallMetric: NotRequired[float]

class ListAudienceExportJobsResponseTypeDef(TypedDict):
    audienceExportJobs: List[AudienceExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AudienceGenerationJobDataSourceOutputTypeDef(TypedDict):
    roleArn: str
    dataSource: NotRequired[S3ConfigMapTypeDef]
    sqlParameters: NotRequired[ProtectedQuerySQLParametersOutputTypeDef]
    sqlComputeConfiguration: NotRequired[ComputeConfigurationTypeDef]

class AudienceGenerationJobDataSourceTypeDef(TypedDict):
    roleArn: str
    dataSource: NotRequired[S3ConfigMapTypeDef]
    sqlParameters: NotRequired[ProtectedQuerySQLParametersTypeDef]
    sqlComputeConfiguration: NotRequired[ComputeConfigurationTypeDef]

class ProtectedQueryInputParametersOutputTypeDef(TypedDict):
    sqlParameters: ProtectedQuerySQLParametersOutputTypeDef
    computeConfiguration: NotRequired[ComputeConfigurationTypeDef]

class ProtectedQueryInputParametersTypeDef(TypedDict):
    sqlParameters: ProtectedQuerySQLParametersTypeDef
    computeConfiguration: NotRequired[ComputeConfigurationTypeDef]

class GetConfiguredModelAlgorithmResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    trainingContainerConfig: ContainerConfigOutputTypeDef
    inferenceContainerConfig: InferenceContainerConfigTypeDef
    roleArn: str
    description: str
    tags: Dict[str, str]
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

ContainerConfigUnionTypeDef = Union[ContainerConfigTypeDef, ContainerConfigOutputTypeDef]

class DatasetInputConfigOutputTypeDef(TypedDict):
    schema: List[ColumnSchemaOutputTypeDef]
    dataSource: DataSourceTypeDef

class DatasetInputConfigTypeDef(TypedDict):
    schema: Sequence[ColumnSchemaUnionTypeDef]
    dataSource: DataSourceTypeDef

class CollaborationTrainedModelInferenceJobSummaryTypeDef(TypedDict):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    name: str
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    configuredModelAlgorithmAssociationArn: NotRequired[str]
    description: NotRequired[str]
    metricsStatus: NotRequired[MetricsStatusType]
    metricsStatusDetails: NotRequired[str]
    logsStatus: NotRequired[LogsStatusType]
    logsStatusDetails: NotRequired[str]

class GetTrainedModelInferenceJobResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainedModelInferenceJobArn: str
    configuredModelAlgorithmAssociationArn: str
    name: str
    status: TrainedModelInferenceJobStatusType
    trainedModelArn: str
    resourceConfig: InferenceResourceConfigTypeDef
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    membershipIdentifier: str
    dataSource: ModelInferenceDataSourceTypeDef
    containerExecutionParameters: InferenceContainerExecutionParametersTypeDef
    statusDetails: StatusDetailsTypeDef
    description: str
    inferenceContainerImageDigest: str
    environment: Dict[str, str]
    kmsKeyArn: str
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TrainedModelInferenceJobSummaryTypeDef(TypedDict):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    name: str
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: NotRequired[str]
    description: NotRequired[str]
    metricsStatus: NotRequired[MetricsStatusType]
    metricsStatusDetails: NotRequired[str]
    logsStatus: NotRequired[LogsStatusType]
    logsStatusDetails: NotRequired[str]

InferenceOutputConfigurationUnionTypeDef = Union[
    InferenceOutputConfigurationTypeDef, InferenceOutputConfigurationOutputTypeDef
]

class CollaborationTrainedModelExportJobSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    name: str
    outputConfiguration: TrainedModelExportOutputConfigurationOutputTypeDef
    status: TrainedModelExportJobStatusType
    creatorAccountId: str
    trainedModelArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    statusDetails: NotRequired[StatusDetailsTypeDef]
    description: NotRequired[str]

TrainedModelExportOutputConfigurationUnionTypeDef = Union[
    TrainedModelExportOutputConfigurationTypeDef, TrainedModelExportOutputConfigurationOutputTypeDef
]

class PrivacyConfigurationPoliciesOutputTypeDef(TypedDict):
    trainedModels: NotRequired[TrainedModelsConfigurationPolicyOutputTypeDef]
    trainedModelExports: NotRequired[TrainedModelExportsConfigurationPolicyOutputTypeDef]
    trainedModelInferenceJobs: NotRequired[
        TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef
    ]

class PrivacyConfigurationPoliciesTypeDef(TypedDict):
    trainedModels: NotRequired[TrainedModelsConfigurationPolicyTypeDef]
    trainedModelExports: NotRequired[TrainedModelExportsConfigurationPolicyTypeDef]
    trainedModelInferenceJobs: NotRequired[TrainedModelInferenceJobsConfigurationPolicyTypeDef]

class ConfiguredAudienceModelSummaryTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    configuredAudienceModelArn: str
    status: Literal["ACTIVE"]
    description: NotRequired[str]

class CreateConfiguredAudienceModelRequestTypeDef(TypedDict):
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    sharedAudienceMetrics: Sequence[SharedAudienceMetricsType]
    description: NotRequired[str]
    minMatchingSeedSize: NotRequired[int]
    audienceSizeConfig: NotRequired[AudienceSizeConfigUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    childResourceTagOnCreatePolicy: NotRequired[TagOnCreatePolicyType]

class GetConfiguredAudienceModelResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredAudienceModelArn: str
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    description: str
    status: Literal["ACTIVE"]
    sharedAudienceMetrics: List[SharedAudienceMetricsType]
    minMatchingSeedSize: int
    audienceSizeConfig: AudienceSizeConfigOutputTypeDef
    tags: Dict[str, str]
    childResourceTagOnCreatePolicy: TagOnCreatePolicyType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelRequestTypeDef(TypedDict):
    configuredAudienceModelArn: str
    outputConfig: NotRequired[ConfiguredAudienceModelOutputConfigTypeDef]
    audienceModelArn: NotRequired[str]
    sharedAudienceMetrics: NotRequired[Sequence[SharedAudienceMetricsType]]
    minMatchingSeedSize: NotRequired[int]
    audienceSizeConfig: NotRequired[AudienceSizeConfigUnionTypeDef]
    description: NotRequired[str]

class GetMLConfigurationResponseTypeDef(TypedDict):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfigurationTypeDef
    createTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutMLConfigurationRequestTypeDef(TypedDict):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfigurationTypeDef

class GetAudienceGenerationJobResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    description: str
    status: AudienceGenerationJobStatusType
    statusDetails: StatusDetailsTypeDef
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceOutputTypeDef
    includeSeedInOutput: bool
    collaborationId: str
    metrics: AudienceQualityMetricsTypeDef
    startedBy: str
    tags: Dict[str, str]
    protectedQueryIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

AudienceGenerationJobDataSourceUnionTypeDef = Union[
    AudienceGenerationJobDataSourceTypeDef, AudienceGenerationJobDataSourceOutputTypeDef
]

class InputChannelDataSourceOutputTypeDef(TypedDict):
    protectedQueryInputParameters: NotRequired[ProtectedQueryInputParametersOutputTypeDef]

class InputChannelDataSourceTypeDef(TypedDict):
    protectedQueryInputParameters: NotRequired[ProtectedQueryInputParametersTypeDef]

class CreateConfiguredModelAlgorithmRequestTypeDef(TypedDict):
    name: str
    roleArn: str
    description: NotRequired[str]
    trainingContainerConfig: NotRequired[ContainerConfigUnionTypeDef]
    inferenceContainerConfig: NotRequired[InferenceContainerConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]

DatasetOutputTypeDef = TypedDict(
    "DatasetOutputTypeDef",
    {
        "type": Literal["INTERACTIONS"],
        "inputConfig": DatasetInputConfigOutputTypeDef,
    },
)
DatasetInputConfigUnionTypeDef = Union[DatasetInputConfigTypeDef, DatasetInputConfigOutputTypeDef]

class ListCollaborationTrainedModelInferenceJobsResponseTypeDef(TypedDict):
    collaborationTrainedModelInferenceJobs: List[
        CollaborationTrainedModelInferenceJobSummaryTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTrainedModelInferenceJobsResponseTypeDef(TypedDict):
    trainedModelInferenceJobs: List[TrainedModelInferenceJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartTrainedModelInferenceJobRequestTypeDef(TypedDict):
    membershipIdentifier: str
    name: str
    trainedModelArn: str
    resourceConfig: InferenceResourceConfigTypeDef
    outputConfiguration: InferenceOutputConfigurationUnionTypeDef
    dataSource: ModelInferenceDataSourceTypeDef
    configuredModelAlgorithmAssociationArn: NotRequired[str]
    description: NotRequired[str]
    containerExecutionParameters: NotRequired[InferenceContainerExecutionParametersTypeDef]
    environment: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ListCollaborationTrainedModelExportJobsResponseTypeDef(TypedDict):
    collaborationTrainedModelExportJobs: List[CollaborationTrainedModelExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartTrainedModelExportJobRequestTypeDef(TypedDict):
    name: str
    trainedModelArn: str
    membershipIdentifier: str
    outputConfiguration: TrainedModelExportOutputConfigurationUnionTypeDef
    description: NotRequired[str]

class PrivacyConfigurationOutputTypeDef(TypedDict):
    policies: PrivacyConfigurationPoliciesOutputTypeDef

class PrivacyConfigurationTypeDef(TypedDict):
    policies: PrivacyConfigurationPoliciesTypeDef

class ListConfiguredAudienceModelsResponseTypeDef(TypedDict):
    configuredAudienceModels: List[ConfiguredAudienceModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartAudienceGenerationJobRequestTypeDef(TypedDict):
    name: str
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceUnionTypeDef
    includeSeedInOutput: NotRequired[bool]
    collaborationId: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class InputChannelOutputTypeDef(TypedDict):
    dataSource: InputChannelDataSourceOutputTypeDef
    roleArn: str

class InputChannelTypeDef(TypedDict):
    dataSource: InputChannelDataSourceTypeDef
    roleArn: str

class GetTrainingDatasetResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    trainingData: List[DatasetOutputTypeDef]
    status: Literal["ACTIVE"]
    roleArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "type": Literal["INTERACTIONS"],
        "inputConfig": DatasetInputConfigUnionTypeDef,
    },
)

class GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: str
    creatorAccountId: str
    privacyConfiguration: PrivacyConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredModelAlgorithmAssociationResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    privacyConfiguration: PrivacyConfigurationOutputTypeDef
    description: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

PrivacyConfigurationUnionTypeDef = Union[
    PrivacyConfigurationTypeDef, PrivacyConfigurationOutputTypeDef
]

class GetMLInputChannelResponseTypeDef(TypedDict):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    inputChannel: InputChannelOutputTypeDef
    protectedQueryIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetailsTypeDef
    retentionInDays: int
    numberOfRecords: int
    numberOfFiles: float
    sizeInGb: float
    description: str
    kmsKeyArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

InputChannelUnionTypeDef = Union[InputChannelTypeDef, InputChannelOutputTypeDef]
DatasetUnionTypeDef = Union[DatasetTypeDef, DatasetOutputTypeDef]

class CreateConfiguredModelAlgorithmAssociationRequestTypeDef(TypedDict):
    membershipIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: NotRequired[str]
    privacyConfiguration: NotRequired[PrivacyConfigurationUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class CreateMLInputChannelRequestTypeDef(TypedDict):
    membershipIdentifier: str
    configuredModelAlgorithmAssociations: Sequence[str]
    inputChannel: InputChannelUnionTypeDef
    name: str
    retentionInDays: int
    description: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateTrainingDatasetRequestTypeDef(TypedDict):
    name: str
    roleArn: str
    trainingData: Sequence[DatasetUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    description: NotRequired[str]
