"""
Type annotations for pipes service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pipes/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pipes.type_defs import AwsVpcConfigurationOutputTypeDef

    data: AwsVpcConfigurationOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AssignPublicIpType,
    BatchJobDependencyTypeType,
    BatchResourceRequirementTypeType,
    DynamoDBStreamStartPositionType,
    EcsResourceRequirementTypeType,
    EpochTimeUnitType,
    KinesisStreamStartPositionType,
    LaunchTypeType,
    LogLevelType,
    MeasureValueTypeType,
    MSKStartPositionType,
    PipeStateType,
    PipeTargetInvocationTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    RequestedPipeStateDescribeResponseType,
    RequestedPipeStateType,
    S3OutputFormatType,
    SelfManagedKafkaStartPositionType,
    TimeFieldTypeType,
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
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchContainerOverridesOutputTypeDef",
    "BatchContainerOverridesTypeDef",
    "BatchEnvironmentVariableTypeDef",
    "BatchJobDependencyTypeDef",
    "BatchResourceRequirementTypeDef",
    "BatchRetryStrategyTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CloudwatchLogsLogDestinationParametersTypeDef",
    "CloudwatchLogsLogDestinationTypeDef",
    "CreatePipeRequestTypeDef",
    "CreatePipeResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DeletePipeRequestTypeDef",
    "DeletePipeResponseTypeDef",
    "DescribePipeRequestTypeDef",
    "DescribePipeResponseTypeDef",
    "DimensionMappingTypeDef",
    "EcsContainerOverrideOutputTypeDef",
    "EcsContainerOverrideTypeDef",
    "EcsEnvironmentFileTypeDef",
    "EcsEnvironmentVariableTypeDef",
    "EcsEphemeralStorageTypeDef",
    "EcsInferenceAcceleratorOverrideTypeDef",
    "EcsResourceRequirementTypeDef",
    "EcsTaskOverrideOutputTypeDef",
    "EcsTaskOverrideTypeDef",
    "FilterCriteriaOutputTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriteriaUnionTypeDef",
    "FilterTypeDef",
    "FirehoseLogDestinationParametersTypeDef",
    "FirehoseLogDestinationTypeDef",
    "ListPipesRequestPaginateTypeDef",
    "ListPipesRequestTypeDef",
    "ListPipesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MQBrokerAccessCredentialsTypeDef",
    "MSKAccessCredentialsTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "MultiMeasureMappingOutputTypeDef",
    "MultiMeasureMappingTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PipeEnrichmentHttpParametersOutputTypeDef",
    "PipeEnrichmentHttpParametersTypeDef",
    "PipeEnrichmentParametersOutputTypeDef",
    "PipeEnrichmentParametersTypeDef",
    "PipeEnrichmentParametersUnionTypeDef",
    "PipeLogConfigurationParametersTypeDef",
    "PipeLogConfigurationTypeDef",
    "PipeSourceActiveMQBrokerParametersTypeDef",
    "PipeSourceDynamoDBStreamParametersTypeDef",
    "PipeSourceKinesisStreamParametersOutputTypeDef",
    "PipeSourceKinesisStreamParametersTypeDef",
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    "PipeSourceParametersOutputTypeDef",
    "PipeSourceParametersTypeDef",
    "PipeSourceParametersUnionTypeDef",
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersOutputTypeDef",
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    "PipeSourceSqsQueueParametersTypeDef",
    "PipeTargetBatchJobParametersOutputTypeDef",
    "PipeTargetBatchJobParametersTypeDef",
    "PipeTargetCloudWatchLogsParametersTypeDef",
    "PipeTargetEcsTaskParametersOutputTypeDef",
    "PipeTargetEcsTaskParametersTypeDef",
    "PipeTargetEventBridgeEventBusParametersOutputTypeDef",
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    "PipeTargetHttpParametersOutputTypeDef",
    "PipeTargetHttpParametersTypeDef",
    "PipeTargetKinesisStreamParametersTypeDef",
    "PipeTargetLambdaFunctionParametersTypeDef",
    "PipeTargetParametersOutputTypeDef",
    "PipeTargetParametersTypeDef",
    "PipeTargetParametersUnionTypeDef",
    "PipeTargetRedshiftDataParametersOutputTypeDef",
    "PipeTargetRedshiftDataParametersTypeDef",
    "PipeTargetSageMakerPipelineParametersOutputTypeDef",
    "PipeTargetSageMakerPipelineParametersTypeDef",
    "PipeTargetSqsQueueParametersTypeDef",
    "PipeTargetStateMachineParametersTypeDef",
    "PipeTargetTimestreamParametersOutputTypeDef",
    "PipeTargetTimestreamParametersTypeDef",
    "PipeTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogDestinationParametersTypeDef",
    "S3LogDestinationTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcOutputTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcUnionTypeDef",
    "SingleMeasureMappingTypeDef",
    "StartPipeRequestTypeDef",
    "StartPipeResponseTypeDef",
    "StopPipeRequestTypeDef",
    "StopPipeResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePipeRequestTypeDef",
    "UpdatePipeResponseTypeDef",
    "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    "UpdatePipeSourceParametersTypeDef",
    "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    "UpdatePipeSourceSqsQueueParametersTypeDef",
)

class AwsVpcConfigurationOutputTypeDef(TypedDict):
    Subnets: List[str]
    SecurityGroups: NotRequired[List[str]]
    AssignPublicIp: NotRequired[AssignPublicIpType]

class AwsVpcConfigurationTypeDef(TypedDict):
    Subnets: Sequence[str]
    SecurityGroups: NotRequired[Sequence[str]]
    AssignPublicIp: NotRequired[AssignPublicIpType]

class BatchArrayPropertiesTypeDef(TypedDict):
    Size: NotRequired[int]

class BatchEnvironmentVariableTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

BatchResourceRequirementTypeDef = TypedDict(
    "BatchResourceRequirementTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)
BatchJobDependencyTypeDef = TypedDict(
    "BatchJobDependencyTypeDef",
    {
        "JobId": NotRequired[str],
        "Type": NotRequired[BatchJobDependencyTypeType],
    },
)

class BatchRetryStrategyTypeDef(TypedDict):
    Attempts: NotRequired[int]

class CapacityProviderStrategyItemTypeDef(TypedDict):
    capacityProvider: str
    weight: NotRequired[int]
    base: NotRequired[int]

class CloudwatchLogsLogDestinationParametersTypeDef(TypedDict):
    LogGroupArn: str

class CloudwatchLogsLogDestinationTypeDef(TypedDict):
    LogGroupArn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeadLetterConfigTypeDef(TypedDict):
    Arn: NotRequired[str]

class DeletePipeRequestTypeDef(TypedDict):
    Name: str

class DescribePipeRequestTypeDef(TypedDict):
    Name: str

class DimensionMappingTypeDef(TypedDict):
    DimensionValue: str
    DimensionValueType: Literal["VARCHAR"]
    DimensionName: str

EcsEnvironmentFileTypeDef = TypedDict(
    "EcsEnvironmentFileTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)

class EcsEnvironmentVariableTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

EcsResourceRequirementTypeDef = TypedDict(
    "EcsResourceRequirementTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)

class EcsEphemeralStorageTypeDef(TypedDict):
    sizeInGiB: int

class EcsInferenceAcceleratorOverrideTypeDef(TypedDict):
    deviceName: NotRequired[str]
    deviceType: NotRequired[str]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": NotRequired[str],
    },
)

class FirehoseLogDestinationParametersTypeDef(TypedDict):
    DeliveryStreamArn: str

class FirehoseLogDestinationTypeDef(TypedDict):
    DeliveryStreamArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListPipesRequestTypeDef(TypedDict):
    NamePrefix: NotRequired[str]
    DesiredState: NotRequired[RequestedPipeStateType]
    CurrentState: NotRequired[PipeStateType]
    SourcePrefix: NotRequired[str]
    TargetPrefix: NotRequired[str]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class PipeTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    DesiredState: NotRequired[RequestedPipeStateType]
    CurrentState: NotRequired[PipeStateType]
    StateReason: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    Source: NotRequired[str]
    Target: NotRequired[str]
    Enrichment: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class MQBrokerAccessCredentialsTypeDef(TypedDict):
    BasicAuth: NotRequired[str]

class MSKAccessCredentialsTypeDef(TypedDict):
    SaslScram512Auth: NotRequired[str]
    ClientCertificateTlsAuth: NotRequired[str]

class MultiMeasureAttributeMappingTypeDef(TypedDict):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MultiMeasureAttributeName: str

class PipeEnrichmentHttpParametersOutputTypeDef(TypedDict):
    PathParameterValues: NotRequired[List[str]]
    HeaderParameters: NotRequired[Dict[str, str]]
    QueryStringParameters: NotRequired[Dict[str, str]]

class PipeEnrichmentHttpParametersTypeDef(TypedDict):
    PathParameterValues: NotRequired[Sequence[str]]
    HeaderParameters: NotRequired[Mapping[str, str]]
    QueryStringParameters: NotRequired[Mapping[str, str]]

class S3LogDestinationParametersTypeDef(TypedDict):
    BucketName: str
    BucketOwner: str
    OutputFormat: NotRequired[S3OutputFormatType]
    Prefix: NotRequired[str]

class S3LogDestinationTypeDef(TypedDict):
    BucketName: NotRequired[str]
    Prefix: NotRequired[str]
    BucketOwner: NotRequired[str]
    OutputFormat: NotRequired[S3OutputFormatType]

TimestampTypeDef = Union[datetime, str]

class PipeSourceSqsQueueParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class SelfManagedKafkaAccessConfigurationCredentialsTypeDef(TypedDict):
    BasicAuth: NotRequired[str]
    SaslScram512Auth: NotRequired[str]
    SaslScram256Auth: NotRequired[str]
    ClientCertificateTlsAuth: NotRequired[str]

class SelfManagedKafkaAccessConfigurationVpcOutputTypeDef(TypedDict):
    Subnets: NotRequired[List[str]]
    SecurityGroup: NotRequired[List[str]]

class SelfManagedKafkaAccessConfigurationVpcTypeDef(TypedDict):
    Subnets: NotRequired[Sequence[str]]
    SecurityGroup: NotRequired[Sequence[str]]

class PipeTargetCloudWatchLogsParametersTypeDef(TypedDict):
    LogStreamName: NotRequired[str]
    Timestamp: NotRequired[str]

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class PipeTargetEventBridgeEventBusParametersOutputTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    DetailType: NotRequired[str]
    Source: NotRequired[str]
    Resources: NotRequired[List[str]]
    Time: NotRequired[str]

class PipeTargetEventBridgeEventBusParametersTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    DetailType: NotRequired[str]
    Source: NotRequired[str]
    Resources: NotRequired[Sequence[str]]
    Time: NotRequired[str]

class PipeTargetHttpParametersOutputTypeDef(TypedDict):
    PathParameterValues: NotRequired[List[str]]
    HeaderParameters: NotRequired[Dict[str, str]]
    QueryStringParameters: NotRequired[Dict[str, str]]

class PipeTargetHttpParametersTypeDef(TypedDict):
    PathParameterValues: NotRequired[Sequence[str]]
    HeaderParameters: NotRequired[Mapping[str, str]]
    QueryStringParameters: NotRequired[Mapping[str, str]]

class PipeTargetKinesisStreamParametersTypeDef(TypedDict):
    PartitionKey: str

class PipeTargetLambdaFunctionParametersTypeDef(TypedDict):
    InvocationType: NotRequired[PipeTargetInvocationTypeType]

class PipeTargetRedshiftDataParametersOutputTypeDef(TypedDict):
    Database: str
    Sqls: List[str]
    SecretManagerArn: NotRequired[str]
    DbUser: NotRequired[str]
    StatementName: NotRequired[str]
    WithEvent: NotRequired[bool]

class PipeTargetSqsQueueParametersTypeDef(TypedDict):
    MessageGroupId: NotRequired[str]
    MessageDeduplicationId: NotRequired[str]

class PipeTargetStateMachineParametersTypeDef(TypedDict):
    InvocationType: NotRequired[PipeTargetInvocationTypeType]

class PipeTargetRedshiftDataParametersTypeDef(TypedDict):
    Database: str
    Sqls: Sequence[str]
    SecretManagerArn: NotRequired[str]
    DbUser: NotRequired[str]
    StatementName: NotRequired[str]
    WithEvent: NotRequired[bool]

class SageMakerPipelineParameterTypeDef(TypedDict):
    Name: str
    Value: str

class SingleMeasureMappingTypeDef(TypedDict):
    MeasureValue: str
    MeasureValueType: MeasureValueTypeType
    MeasureName: str

class StartPipeRequestTypeDef(TypedDict):
    Name: str

class StopPipeRequestTypeDef(TypedDict):
    Name: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePipeSourceSqsQueueParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class NetworkConfigurationOutputTypeDef(TypedDict):
    awsvpcConfiguration: NotRequired[AwsVpcConfigurationOutputTypeDef]

class NetworkConfigurationTypeDef(TypedDict):
    awsvpcConfiguration: NotRequired[AwsVpcConfigurationTypeDef]

class BatchContainerOverridesOutputTypeDef(TypedDict):
    Command: NotRequired[List[str]]
    Environment: NotRequired[List[BatchEnvironmentVariableTypeDef]]
    InstanceType: NotRequired[str]
    ResourceRequirements: NotRequired[List[BatchResourceRequirementTypeDef]]

class BatchContainerOverridesTypeDef(TypedDict):
    Command: NotRequired[Sequence[str]]
    Environment: NotRequired[Sequence[BatchEnvironmentVariableTypeDef]]
    InstanceType: NotRequired[str]
    ResourceRequirements: NotRequired[Sequence[BatchResourceRequirementTypeDef]]

class CreatePipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    DesiredState: RequestedPipeStateType
    CurrentState: PipeStateType
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PipeSourceDynamoDBStreamParametersTypeDef(TypedDict):
    StartingPosition: DynamoDBStreamStartPositionType
    BatchSize: NotRequired[int]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    OnPartialBatchItemFailure: NotRequired[Literal["AUTOMATIC_BISECT"]]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    MaximumRecordAgeInSeconds: NotRequired[int]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]

class PipeSourceKinesisStreamParametersOutputTypeDef(TypedDict):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: NotRequired[int]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    OnPartialBatchItemFailure: NotRequired[Literal["AUTOMATIC_BISECT"]]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    MaximumRecordAgeInSeconds: NotRequired[int]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]
    StartingPositionTimestamp: NotRequired[datetime]

class UpdatePipeSourceDynamoDBStreamParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    OnPartialBatchItemFailure: NotRequired[Literal["AUTOMATIC_BISECT"]]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    MaximumRecordAgeInSeconds: NotRequired[int]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]

class UpdatePipeSourceKinesisStreamParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    OnPartialBatchItemFailure: NotRequired[Literal["AUTOMATIC_BISECT"]]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    MaximumRecordAgeInSeconds: NotRequired[int]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]

class EcsContainerOverrideOutputTypeDef(TypedDict):
    Command: NotRequired[List[str]]
    Cpu: NotRequired[int]
    Environment: NotRequired[List[EcsEnvironmentVariableTypeDef]]
    EnvironmentFiles: NotRequired[List[EcsEnvironmentFileTypeDef]]
    Memory: NotRequired[int]
    MemoryReservation: NotRequired[int]
    Name: NotRequired[str]
    ResourceRequirements: NotRequired[List[EcsResourceRequirementTypeDef]]

class EcsContainerOverrideTypeDef(TypedDict):
    Command: NotRequired[Sequence[str]]
    Cpu: NotRequired[int]
    Environment: NotRequired[Sequence[EcsEnvironmentVariableTypeDef]]
    EnvironmentFiles: NotRequired[Sequence[EcsEnvironmentFileTypeDef]]
    Memory: NotRequired[int]
    MemoryReservation: NotRequired[int]
    Name: NotRequired[str]
    ResourceRequirements: NotRequired[Sequence[EcsResourceRequirementTypeDef]]

class FilterCriteriaOutputTypeDef(TypedDict):
    Filters: NotRequired[List[FilterTypeDef]]

class FilterCriteriaTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListPipesRequestPaginateTypeDef(TypedDict):
    NamePrefix: NotRequired[str]
    DesiredState: NotRequired[RequestedPipeStateType]
    CurrentState: NotRequired[PipeStateType]
    SourcePrefix: NotRequired[str]
    TargetPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPipesResponseTypeDef(TypedDict):
    Pipes: List[PipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PipeSourceActiveMQBrokerParametersTypeDef(TypedDict):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class PipeSourceRabbitMQBrokerParametersTypeDef(TypedDict):
    Credentials: MQBrokerAccessCredentialsTypeDef
    QueueName: str
    VirtualHost: NotRequired[str]
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class UpdatePipeSourceActiveMQBrokerParametersTypeDef(TypedDict):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class UpdatePipeSourceRabbitMQBrokerParametersTypeDef(TypedDict):
    Credentials: MQBrokerAccessCredentialsTypeDef
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class PipeSourceManagedStreamingKafkaParametersTypeDef(TypedDict):
    TopicName: str
    StartingPosition: NotRequired[MSKStartPositionType]
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    ConsumerGroupID: NotRequired[str]
    Credentials: NotRequired[MSKAccessCredentialsTypeDef]

class UpdatePipeSourceManagedStreamingKafkaParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    Credentials: NotRequired[MSKAccessCredentialsTypeDef]
    MaximumBatchingWindowInSeconds: NotRequired[int]

class MultiMeasureMappingOutputTypeDef(TypedDict):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]

class MultiMeasureMappingTypeDef(TypedDict):
    MultiMeasureName: str
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]

class PipeEnrichmentParametersOutputTypeDef(TypedDict):
    InputTemplate: NotRequired[str]
    HttpParameters: NotRequired[PipeEnrichmentHttpParametersOutputTypeDef]

class PipeEnrichmentParametersTypeDef(TypedDict):
    InputTemplate: NotRequired[str]
    HttpParameters: NotRequired[PipeEnrichmentHttpParametersTypeDef]

class PipeLogConfigurationParametersTypeDef(TypedDict):
    Level: LogLevelType
    S3LogDestination: NotRequired[S3LogDestinationParametersTypeDef]
    FirehoseLogDestination: NotRequired[FirehoseLogDestinationParametersTypeDef]
    CloudwatchLogsLogDestination: NotRequired[CloudwatchLogsLogDestinationParametersTypeDef]
    IncludeExecutionData: NotRequired[Sequence[Literal["ALL"]]]

class PipeLogConfigurationTypeDef(TypedDict):
    S3LogDestination: NotRequired[S3LogDestinationTypeDef]
    FirehoseLogDestination: NotRequired[FirehoseLogDestinationTypeDef]
    CloudwatchLogsLogDestination: NotRequired[CloudwatchLogsLogDestinationTypeDef]
    Level: NotRequired[LogLevelType]
    IncludeExecutionData: NotRequired[List[Literal["ALL"]]]

class PipeSourceKinesisStreamParametersTypeDef(TypedDict):
    StartingPosition: KinesisStreamStartPositionType
    BatchSize: NotRequired[int]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    OnPartialBatchItemFailure: NotRequired[Literal["AUTOMATIC_BISECT"]]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    MaximumRecordAgeInSeconds: NotRequired[int]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]
    StartingPositionTimestamp: NotRequired[TimestampTypeDef]

class PipeSourceSelfManagedKafkaParametersOutputTypeDef(TypedDict):
    TopicName: str
    StartingPosition: NotRequired[SelfManagedKafkaStartPositionType]
    AdditionalBootstrapServers: NotRequired[List[str]]
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    ConsumerGroupID: NotRequired[str]
    Credentials: NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef]
    ServerRootCaCertificate: NotRequired[str]
    Vpc: NotRequired[SelfManagedKafkaAccessConfigurationVpcOutputTypeDef]

class PipeSourceSelfManagedKafkaParametersTypeDef(TypedDict):
    TopicName: str
    StartingPosition: NotRequired[SelfManagedKafkaStartPositionType]
    AdditionalBootstrapServers: NotRequired[Sequence[str]]
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    ConsumerGroupID: NotRequired[str]
    Credentials: NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef]
    ServerRootCaCertificate: NotRequired[str]
    Vpc: NotRequired[SelfManagedKafkaAccessConfigurationVpcTypeDef]

SelfManagedKafkaAccessConfigurationVpcUnionTypeDef = Union[
    SelfManagedKafkaAccessConfigurationVpcTypeDef,
    SelfManagedKafkaAccessConfigurationVpcOutputTypeDef,
]

class PipeTargetSageMakerPipelineParametersOutputTypeDef(TypedDict):
    PipelineParameterList: NotRequired[List[SageMakerPipelineParameterTypeDef]]

class PipeTargetSageMakerPipelineParametersTypeDef(TypedDict):
    PipelineParameterList: NotRequired[Sequence[SageMakerPipelineParameterTypeDef]]

class PipeTargetBatchJobParametersOutputTypeDef(TypedDict):
    JobDefinition: str
    JobName: str
    ArrayProperties: NotRequired[BatchArrayPropertiesTypeDef]
    RetryStrategy: NotRequired[BatchRetryStrategyTypeDef]
    ContainerOverrides: NotRequired[BatchContainerOverridesOutputTypeDef]
    DependsOn: NotRequired[List[BatchJobDependencyTypeDef]]
    Parameters: NotRequired[Dict[str, str]]

class PipeTargetBatchJobParametersTypeDef(TypedDict):
    JobDefinition: str
    JobName: str
    ArrayProperties: NotRequired[BatchArrayPropertiesTypeDef]
    RetryStrategy: NotRequired[BatchRetryStrategyTypeDef]
    ContainerOverrides: NotRequired[BatchContainerOverridesTypeDef]
    DependsOn: NotRequired[Sequence[BatchJobDependencyTypeDef]]
    Parameters: NotRequired[Mapping[str, str]]

class EcsTaskOverrideOutputTypeDef(TypedDict):
    ContainerOverrides: NotRequired[List[EcsContainerOverrideOutputTypeDef]]
    Cpu: NotRequired[str]
    EphemeralStorage: NotRequired[EcsEphemeralStorageTypeDef]
    ExecutionRoleArn: NotRequired[str]
    InferenceAcceleratorOverrides: NotRequired[List[EcsInferenceAcceleratorOverrideTypeDef]]
    Memory: NotRequired[str]
    TaskRoleArn: NotRequired[str]

class EcsTaskOverrideTypeDef(TypedDict):
    ContainerOverrides: NotRequired[Sequence[EcsContainerOverrideTypeDef]]
    Cpu: NotRequired[str]
    EphemeralStorage: NotRequired[EcsEphemeralStorageTypeDef]
    ExecutionRoleArn: NotRequired[str]
    InferenceAcceleratorOverrides: NotRequired[Sequence[EcsInferenceAcceleratorOverrideTypeDef]]
    Memory: NotRequired[str]
    TaskRoleArn: NotRequired[str]

FilterCriteriaUnionTypeDef = Union[FilterCriteriaTypeDef, FilterCriteriaOutputTypeDef]

class PipeTargetTimestreamParametersOutputTypeDef(TypedDict):
    TimeValue: str
    VersionValue: str
    DimensionMappings: List[DimensionMappingTypeDef]
    EpochTimeUnit: NotRequired[EpochTimeUnitType]
    TimeFieldType: NotRequired[TimeFieldTypeType]
    TimestampFormat: NotRequired[str]
    SingleMeasureMappings: NotRequired[List[SingleMeasureMappingTypeDef]]
    MultiMeasureMappings: NotRequired[List[MultiMeasureMappingOutputTypeDef]]

class PipeTargetTimestreamParametersTypeDef(TypedDict):
    TimeValue: str
    VersionValue: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    EpochTimeUnit: NotRequired[EpochTimeUnitType]
    TimeFieldType: NotRequired[TimeFieldTypeType]
    TimestampFormat: NotRequired[str]
    SingleMeasureMappings: NotRequired[Sequence[SingleMeasureMappingTypeDef]]
    MultiMeasureMappings: NotRequired[Sequence[MultiMeasureMappingTypeDef]]

PipeEnrichmentParametersUnionTypeDef = Union[
    PipeEnrichmentParametersTypeDef, PipeEnrichmentParametersOutputTypeDef
]

class PipeSourceParametersOutputTypeDef(TypedDict):
    FilterCriteria: NotRequired[FilterCriteriaOutputTypeDef]
    KinesisStreamParameters: NotRequired[PipeSourceKinesisStreamParametersOutputTypeDef]
    DynamoDBStreamParameters: NotRequired[PipeSourceDynamoDBStreamParametersTypeDef]
    SqsQueueParameters: NotRequired[PipeSourceSqsQueueParametersTypeDef]
    ActiveMQBrokerParameters: NotRequired[PipeSourceActiveMQBrokerParametersTypeDef]
    RabbitMQBrokerParameters: NotRequired[PipeSourceRabbitMQBrokerParametersTypeDef]
    ManagedStreamingKafkaParameters: NotRequired[PipeSourceManagedStreamingKafkaParametersTypeDef]
    SelfManagedKafkaParameters: NotRequired[PipeSourceSelfManagedKafkaParametersOutputTypeDef]

class PipeSourceParametersTypeDef(TypedDict):
    FilterCriteria: NotRequired[FilterCriteriaTypeDef]
    KinesisStreamParameters: NotRequired[PipeSourceKinesisStreamParametersTypeDef]
    DynamoDBStreamParameters: NotRequired[PipeSourceDynamoDBStreamParametersTypeDef]
    SqsQueueParameters: NotRequired[PipeSourceSqsQueueParametersTypeDef]
    ActiveMQBrokerParameters: NotRequired[PipeSourceActiveMQBrokerParametersTypeDef]
    RabbitMQBrokerParameters: NotRequired[PipeSourceRabbitMQBrokerParametersTypeDef]
    ManagedStreamingKafkaParameters: NotRequired[PipeSourceManagedStreamingKafkaParametersTypeDef]
    SelfManagedKafkaParameters: NotRequired[PipeSourceSelfManagedKafkaParametersTypeDef]

class UpdatePipeSourceSelfManagedKafkaParametersTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    Credentials: NotRequired[SelfManagedKafkaAccessConfigurationCredentialsTypeDef]
    ServerRootCaCertificate: NotRequired[str]
    Vpc: NotRequired[SelfManagedKafkaAccessConfigurationVpcUnionTypeDef]

class PipeTargetEcsTaskParametersOutputTypeDef(TypedDict):
    TaskDefinitionArn: str
    TaskCount: NotRequired[int]
    LaunchType: NotRequired[LaunchTypeType]
    NetworkConfiguration: NotRequired[NetworkConfigurationOutputTypeDef]
    PlatformVersion: NotRequired[str]
    Group: NotRequired[str]
    CapacityProviderStrategy: NotRequired[List[CapacityProviderStrategyItemTypeDef]]
    EnableECSManagedTags: NotRequired[bool]
    EnableExecuteCommand: NotRequired[bool]
    PlacementConstraints: NotRequired[List[PlacementConstraintTypeDef]]
    PlacementStrategy: NotRequired[List[PlacementStrategyTypeDef]]
    PropagateTags: NotRequired[Literal["TASK_DEFINITION"]]
    ReferenceId: NotRequired[str]
    Overrides: NotRequired[EcsTaskOverrideOutputTypeDef]
    Tags: NotRequired[List[TagTypeDef]]

class PipeTargetEcsTaskParametersTypeDef(TypedDict):
    TaskDefinitionArn: str
    TaskCount: NotRequired[int]
    LaunchType: NotRequired[LaunchTypeType]
    NetworkConfiguration: NotRequired[NetworkConfigurationTypeDef]
    PlatformVersion: NotRequired[str]
    Group: NotRequired[str]
    CapacityProviderStrategy: NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]]
    EnableECSManagedTags: NotRequired[bool]
    EnableExecuteCommand: NotRequired[bool]
    PlacementConstraints: NotRequired[Sequence[PlacementConstraintTypeDef]]
    PlacementStrategy: NotRequired[Sequence[PlacementStrategyTypeDef]]
    PropagateTags: NotRequired[Literal["TASK_DEFINITION"]]
    ReferenceId: NotRequired[str]
    Overrides: NotRequired[EcsTaskOverrideTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

PipeSourceParametersUnionTypeDef = Union[
    PipeSourceParametersTypeDef, PipeSourceParametersOutputTypeDef
]

class UpdatePipeSourceParametersTypeDef(TypedDict):
    FilterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    KinesisStreamParameters: NotRequired[UpdatePipeSourceKinesisStreamParametersTypeDef]
    DynamoDBStreamParameters: NotRequired[UpdatePipeSourceDynamoDBStreamParametersTypeDef]
    SqsQueueParameters: NotRequired[UpdatePipeSourceSqsQueueParametersTypeDef]
    ActiveMQBrokerParameters: NotRequired[UpdatePipeSourceActiveMQBrokerParametersTypeDef]
    RabbitMQBrokerParameters: NotRequired[UpdatePipeSourceRabbitMQBrokerParametersTypeDef]
    ManagedStreamingKafkaParameters: NotRequired[
        UpdatePipeSourceManagedStreamingKafkaParametersTypeDef
    ]
    SelfManagedKafkaParameters: NotRequired[UpdatePipeSourceSelfManagedKafkaParametersTypeDef]

class PipeTargetParametersOutputTypeDef(TypedDict):
    InputTemplate: NotRequired[str]
    LambdaFunctionParameters: NotRequired[PipeTargetLambdaFunctionParametersTypeDef]
    StepFunctionStateMachineParameters: NotRequired[PipeTargetStateMachineParametersTypeDef]
    KinesisStreamParameters: NotRequired[PipeTargetKinesisStreamParametersTypeDef]
    EcsTaskParameters: NotRequired[PipeTargetEcsTaskParametersOutputTypeDef]
    BatchJobParameters: NotRequired[PipeTargetBatchJobParametersOutputTypeDef]
    SqsQueueParameters: NotRequired[PipeTargetSqsQueueParametersTypeDef]
    HttpParameters: NotRequired[PipeTargetHttpParametersOutputTypeDef]
    RedshiftDataParameters: NotRequired[PipeTargetRedshiftDataParametersOutputTypeDef]
    SageMakerPipelineParameters: NotRequired[PipeTargetSageMakerPipelineParametersOutputTypeDef]
    EventBridgeEventBusParameters: NotRequired[PipeTargetEventBridgeEventBusParametersOutputTypeDef]
    CloudWatchLogsParameters: NotRequired[PipeTargetCloudWatchLogsParametersTypeDef]
    TimestreamParameters: NotRequired[PipeTargetTimestreamParametersOutputTypeDef]

class PipeTargetParametersTypeDef(TypedDict):
    InputTemplate: NotRequired[str]
    LambdaFunctionParameters: NotRequired[PipeTargetLambdaFunctionParametersTypeDef]
    StepFunctionStateMachineParameters: NotRequired[PipeTargetStateMachineParametersTypeDef]
    KinesisStreamParameters: NotRequired[PipeTargetKinesisStreamParametersTypeDef]
    EcsTaskParameters: NotRequired[PipeTargetEcsTaskParametersTypeDef]
    BatchJobParameters: NotRequired[PipeTargetBatchJobParametersTypeDef]
    SqsQueueParameters: NotRequired[PipeTargetSqsQueueParametersTypeDef]
    HttpParameters: NotRequired[PipeTargetHttpParametersTypeDef]
    RedshiftDataParameters: NotRequired[PipeTargetRedshiftDataParametersTypeDef]
    SageMakerPipelineParameters: NotRequired[PipeTargetSageMakerPipelineParametersTypeDef]
    EventBridgeEventBusParameters: NotRequired[PipeTargetEventBridgeEventBusParametersTypeDef]
    CloudWatchLogsParameters: NotRequired[PipeTargetCloudWatchLogsParametersTypeDef]
    TimestreamParameters: NotRequired[PipeTargetTimestreamParametersTypeDef]

class DescribePipeResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    DesiredState: RequestedPipeStateDescribeResponseType
    CurrentState: PipeStateType
    StateReason: str
    Source: str
    SourceParameters: PipeSourceParametersOutputTypeDef
    Enrichment: str
    EnrichmentParameters: PipeEnrichmentParametersOutputTypeDef
    Target: str
    TargetParameters: PipeTargetParametersOutputTypeDef
    RoleArn: str
    Tags: Dict[str, str]
    CreationTime: datetime
    LastModifiedTime: datetime
    LogConfiguration: PipeLogConfigurationTypeDef
    KmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

PipeTargetParametersUnionTypeDef = Union[
    PipeTargetParametersTypeDef, PipeTargetParametersOutputTypeDef
]

class CreatePipeRequestTypeDef(TypedDict):
    Name: str
    Source: str
    Target: str
    RoleArn: str
    Description: NotRequired[str]
    DesiredState: NotRequired[RequestedPipeStateType]
    SourceParameters: NotRequired[PipeSourceParametersUnionTypeDef]
    Enrichment: NotRequired[str]
    EnrichmentParameters: NotRequired[PipeEnrichmentParametersUnionTypeDef]
    TargetParameters: NotRequired[PipeTargetParametersUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    LogConfiguration: NotRequired[PipeLogConfigurationParametersTypeDef]
    KmsKeyIdentifier: NotRequired[str]

class UpdatePipeRequestTypeDef(TypedDict):
    Name: str
    RoleArn: str
    Description: NotRequired[str]
    DesiredState: NotRequired[RequestedPipeStateType]
    SourceParameters: NotRequired[UpdatePipeSourceParametersTypeDef]
    Enrichment: NotRequired[str]
    EnrichmentParameters: NotRequired[PipeEnrichmentParametersUnionTypeDef]
    Target: NotRequired[str]
    TargetParameters: NotRequired[PipeTargetParametersUnionTypeDef]
    LogConfiguration: NotRequired[PipeLogConfigurationParametersTypeDef]
    KmsKeyIdentifier: NotRequired[str]
