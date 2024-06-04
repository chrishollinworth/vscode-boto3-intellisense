"""
Type annotations for pipes service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pipes.type_defs import AwsVpcConfigurationTypeDef

    data: AwsVpcConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchContainerOverridesTypeDef",
    "BatchEnvironmentVariableTypeDef",
    "BatchJobDependencyTypeDef",
    "BatchResourceRequirementTypeDef",
    "BatchRetryStrategyTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CloudwatchLogsLogDestinationParametersTypeDef",
    "CloudwatchLogsLogDestinationTypeDef",
    "CreatePipeRequestRequestTypeDef",
    "CreatePipeResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DeletePipeRequestRequestTypeDef",
    "DeletePipeResponseTypeDef",
    "DescribePipeRequestRequestTypeDef",
    "DescribePipeResponseTypeDef",
    "DimensionMappingTypeDef",
    "EcsContainerOverrideTypeDef",
    "EcsEnvironmentFileTypeDef",
    "EcsEnvironmentVariableTypeDef",
    "EcsEphemeralStorageTypeDef",
    "EcsInferenceAcceleratorOverrideTypeDef",
    "EcsResourceRequirementTypeDef",
    "EcsTaskOverrideTypeDef",
    "FilterCriteriaTypeDef",
    "FilterTypeDef",
    "FirehoseLogDestinationParametersTypeDef",
    "FirehoseLogDestinationTypeDef",
    "ListPipesRequestRequestTypeDef",
    "ListPipesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MQBrokerAccessCredentialsTypeDef",
    "MSKAccessCredentialsTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "MultiMeasureMappingTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PipeEnrichmentHttpParametersTypeDef",
    "PipeEnrichmentParametersTypeDef",
    "PipeLogConfigurationParametersTypeDef",
    "PipeLogConfigurationTypeDef",
    "PipeSourceActiveMQBrokerParametersTypeDef",
    "PipeSourceDynamoDBStreamParametersTypeDef",
    "PipeSourceKinesisStreamParametersTypeDef",
    "PipeSourceManagedStreamingKafkaParametersTypeDef",
    "PipeSourceParametersTypeDef",
    "PipeSourceRabbitMQBrokerParametersTypeDef",
    "PipeSourceSelfManagedKafkaParametersTypeDef",
    "PipeSourceSqsQueueParametersTypeDef",
    "PipeTargetBatchJobParametersTypeDef",
    "PipeTargetCloudWatchLogsParametersTypeDef",
    "PipeTargetEcsTaskParametersTypeDef",
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    "PipeTargetHttpParametersTypeDef",
    "PipeTargetKinesisStreamParametersTypeDef",
    "PipeTargetLambdaFunctionParametersTypeDef",
    "PipeTargetParametersTypeDef",
    "PipeTargetRedshiftDataParametersTypeDef",
    "PipeTargetSageMakerPipelineParametersTypeDef",
    "PipeTargetSqsQueueParametersTypeDef",
    "PipeTargetStateMachineParametersTypeDef",
    "PipeTargetTimestreamParametersTypeDef",
    "PipeTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogDestinationParametersTypeDef",
    "S3LogDestinationTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    "SingleMeasureMappingTypeDef",
    "StartPipeRequestRequestTypeDef",
    "StartPipeResponseTypeDef",
    "StopPipeRequestRequestTypeDef",
    "StopPipeResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePipeRequestRequestTypeDef",
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

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "Subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "SecurityGroups": List[str],
        "AssignPublicIp": AssignPublicIpType,
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": int,
    },
    total=False,
)

BatchContainerOverridesTypeDef = TypedDict(
    "BatchContainerOverridesTypeDef",
    {
        "Command": List[str],
        "Environment": List["BatchEnvironmentVariableTypeDef"],
        "InstanceType": str,
        "ResourceRequirements": List["BatchResourceRequirementTypeDef"],
    },
    total=False,
)

BatchEnvironmentVariableTypeDef = TypedDict(
    "BatchEnvironmentVariableTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

BatchJobDependencyTypeDef = TypedDict(
    "BatchJobDependencyTypeDef",
    {
        "JobId": str,
        "Type": BatchJobDependencyTypeType,
    },
    total=False,
)

BatchResourceRequirementTypeDef = TypedDict(
    "BatchResourceRequirementTypeDef",
    {
        "Type": BatchResourceRequirementTypeType,
        "Value": str,
    },
)

BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": int,
    },
    total=False,
)

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

CloudwatchLogsLogDestinationParametersTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationParametersTypeDef",
    {
        "LogGroupArn": str,
    },
)

CloudwatchLogsLogDestinationTypeDef = TypedDict(
    "CloudwatchLogsLogDestinationTypeDef",
    {
        "LogGroupArn": str,
    },
    total=False,
)

_RequiredCreatePipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "Source": str,
        "Target": str,
        "RoleArn": str,
    },
)
_OptionalCreatePipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipeRequestRequestTypeDef",
    {
        "Description": str,
        "DesiredState": RequestedPipeStateType,
        "SourceParameters": "PipeSourceParametersTypeDef",
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "TargetParameters": "PipeTargetParametersTypeDef",
        "Tags": Dict[str, str],
        "LogConfiguration": "PipeLogConfigurationParametersTypeDef",
    },
    total=False,
)

class CreatePipeRequestRequestTypeDef(
    _RequiredCreatePipeRequestRequestTypeDef, _OptionalCreatePipeRequestRequestTypeDef
):
    pass

CreatePipeResponseTypeDef = TypedDict(
    "CreatePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DeletePipeRequestRequestTypeDef = TypedDict(
    "DeletePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeletePipeResponseTypeDef = TypedDict(
    "DeletePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipeRequestRequestTypeDef = TypedDict(
    "DescribePipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePipeResponseTypeDef = TypedDict(
    "DescribePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "CurrentState": PipeStateType,
        "StateReason": str,
        "Source": str,
        "SourceParameters": "PipeSourceParametersTypeDef",
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "Target": str,
        "TargetParameters": "PipeTargetParametersTypeDef",
        "RoleArn": str,
        "Tags": Dict[str, str],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LogConfiguration": "PipeLogConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "DimensionValue": str,
        "DimensionValueType": Literal["VARCHAR"],
        "DimensionName": str,
    },
)

EcsContainerOverrideTypeDef = TypedDict(
    "EcsContainerOverrideTypeDef",
    {
        "Command": List[str],
        "Cpu": int,
        "Environment": List["EcsEnvironmentVariableTypeDef"],
        "EnvironmentFiles": List["EcsEnvironmentFileTypeDef"],
        "Memory": int,
        "MemoryReservation": int,
        "Name": str,
        "ResourceRequirements": List["EcsResourceRequirementTypeDef"],
    },
    total=False,
)

EcsEnvironmentFileTypeDef = TypedDict(
    "EcsEnvironmentFileTypeDef",
    {
        "type": Literal["s3"],
        "value": str,
    },
)

EcsEnvironmentVariableTypeDef = TypedDict(
    "EcsEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

EcsEphemeralStorageTypeDef = TypedDict(
    "EcsEphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

EcsInferenceAcceleratorOverrideTypeDef = TypedDict(
    "EcsInferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

EcsResourceRequirementTypeDef = TypedDict(
    "EcsResourceRequirementTypeDef",
    {
        "type": EcsResourceRequirementTypeType,
        "value": str,
    },
)

EcsTaskOverrideTypeDef = TypedDict(
    "EcsTaskOverrideTypeDef",
    {
        "ContainerOverrides": List["EcsContainerOverrideTypeDef"],
        "Cpu": str,
        "EphemeralStorage": "EcsEphemeralStorageTypeDef",
        "ExecutionRoleArn": str,
        "InferenceAcceleratorOverrides": List["EcsInferenceAcceleratorOverrideTypeDef"],
        "Memory": str,
        "TaskRoleArn": str,
    },
    total=False,
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": str,
    },
    total=False,
)

FirehoseLogDestinationParametersTypeDef = TypedDict(
    "FirehoseLogDestinationParametersTypeDef",
    {
        "DeliveryStreamArn": str,
    },
)

FirehoseLogDestinationTypeDef = TypedDict(
    "FirehoseLogDestinationTypeDef",
    {
        "DeliveryStreamArn": str,
    },
    total=False,
)

ListPipesRequestRequestTypeDef = TypedDict(
    "ListPipesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "SourcePrefix": str,
        "TargetPrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListPipesResponseTypeDef = TypedDict(
    "ListPipesResponseTypeDef",
    {
        "Pipes": List["PipeTypeDef"],
        "NextToken": str,
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

MQBrokerAccessCredentialsTypeDef = TypedDict(
    "MQBrokerAccessCredentialsTypeDef",
    {
        "BasicAuth": str,
    },
    total=False,
)

MSKAccessCredentialsTypeDef = TypedDict(
    "MSKAccessCredentialsTypeDef",
    {
        "SaslScram512Auth": str,
        "ClientCertificateTlsAuth": str,
    },
    total=False,
)

MultiMeasureAttributeMappingTypeDef = TypedDict(
    "MultiMeasureAttributeMappingTypeDef",
    {
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "MultiMeasureAttributeName": str,
    },
)

MultiMeasureMappingTypeDef = TypedDict(
    "MultiMeasureMappingTypeDef",
    {
        "MultiMeasureName": str,
        "MultiMeasureAttributeMappings": List["MultiMeasureAttributeMappingTypeDef"],
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": "AwsVpcConfigurationTypeDef",
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

PipeEnrichmentHttpParametersTypeDef = TypedDict(
    "PipeEnrichmentHttpParametersTypeDef",
    {
        "PathParameterValues": List[str],
        "HeaderParameters": Dict[str, str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

PipeEnrichmentParametersTypeDef = TypedDict(
    "PipeEnrichmentParametersTypeDef",
    {
        "InputTemplate": str,
        "HttpParameters": "PipeEnrichmentHttpParametersTypeDef",
    },
    total=False,
)

_RequiredPipeLogConfigurationParametersTypeDef = TypedDict(
    "_RequiredPipeLogConfigurationParametersTypeDef",
    {
        "Level": LogLevelType,
    },
)
_OptionalPipeLogConfigurationParametersTypeDef = TypedDict(
    "_OptionalPipeLogConfigurationParametersTypeDef",
    {
        "S3LogDestination": "S3LogDestinationParametersTypeDef",
        "FirehoseLogDestination": "FirehoseLogDestinationParametersTypeDef",
        "CloudwatchLogsLogDestination": "CloudwatchLogsLogDestinationParametersTypeDef",
        "IncludeExecutionData": List[Literal["ALL"]],
    },
    total=False,
)

class PipeLogConfigurationParametersTypeDef(
    _RequiredPipeLogConfigurationParametersTypeDef, _OptionalPipeLogConfigurationParametersTypeDef
):
    pass

PipeLogConfigurationTypeDef = TypedDict(
    "PipeLogConfigurationTypeDef",
    {
        "S3LogDestination": "S3LogDestinationTypeDef",
        "FirehoseLogDestination": "FirehoseLogDestinationTypeDef",
        "CloudwatchLogsLogDestination": "CloudwatchLogsLogDestinationTypeDef",
        "Level": LogLevelType,
        "IncludeExecutionData": List[Literal["ALL"]],
    },
    total=False,
)

_RequiredPipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_RequiredPipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": "MQBrokerAccessCredentialsTypeDef",
        "QueueName": str,
    },
)
_OptionalPipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_OptionalPipeSourceActiveMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class PipeSourceActiveMQBrokerParametersTypeDef(
    _RequiredPipeSourceActiveMQBrokerParametersTypeDef,
    _OptionalPipeSourceActiveMQBrokerParametersTypeDef,
):
    pass

_RequiredPipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "_RequiredPipeSourceDynamoDBStreamParametersTypeDef",
    {
        "StartingPosition": DynamoDBStreamStartPositionType,
    },
)
_OptionalPipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "_OptionalPipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
    },
    total=False,
)

class PipeSourceDynamoDBStreamParametersTypeDef(
    _RequiredPipeSourceDynamoDBStreamParametersTypeDef,
    _OptionalPipeSourceDynamoDBStreamParametersTypeDef,
):
    pass

_RequiredPipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "_RequiredPipeSourceKinesisStreamParametersTypeDef",
    {
        "StartingPosition": KinesisStreamStartPositionType,
    },
)
_OptionalPipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "_OptionalPipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
        "StartingPositionTimestamp": Union[datetime, str],
    },
    total=False,
)

class PipeSourceKinesisStreamParametersTypeDef(
    _RequiredPipeSourceKinesisStreamParametersTypeDef,
    _OptionalPipeSourceKinesisStreamParametersTypeDef,
):
    pass

_RequiredPipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "_RequiredPipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "_OptionalPipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "StartingPosition": MSKStartPositionType,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ConsumerGroupID": str,
        "Credentials": "MSKAccessCredentialsTypeDef",
    },
    total=False,
)

class PipeSourceManagedStreamingKafkaParametersTypeDef(
    _RequiredPipeSourceManagedStreamingKafkaParametersTypeDef,
    _OptionalPipeSourceManagedStreamingKafkaParametersTypeDef,
):
    pass

PipeSourceParametersTypeDef = TypedDict(
    "PipeSourceParametersTypeDef",
    {
        "FilterCriteria": "FilterCriteriaTypeDef",
        "KinesisStreamParameters": "PipeSourceKinesisStreamParametersTypeDef",
        "DynamoDBStreamParameters": "PipeSourceDynamoDBStreamParametersTypeDef",
        "SqsQueueParameters": "PipeSourceSqsQueueParametersTypeDef",
        "ActiveMQBrokerParameters": "PipeSourceActiveMQBrokerParametersTypeDef",
        "RabbitMQBrokerParameters": "PipeSourceRabbitMQBrokerParametersTypeDef",
        "ManagedStreamingKafkaParameters": "PipeSourceManagedStreamingKafkaParametersTypeDef",
        "SelfManagedKafkaParameters": "PipeSourceSelfManagedKafkaParametersTypeDef",
    },
    total=False,
)

_RequiredPipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_RequiredPipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": "MQBrokerAccessCredentialsTypeDef",
        "QueueName": str,
    },
)
_OptionalPipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_OptionalPipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "VirtualHost": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class PipeSourceRabbitMQBrokerParametersTypeDef(
    _RequiredPipeSourceRabbitMQBrokerParametersTypeDef,
    _OptionalPipeSourceRabbitMQBrokerParametersTypeDef,
):
    pass

_RequiredPipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "_RequiredPipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "TopicName": str,
    },
)
_OptionalPipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "_OptionalPipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "StartingPosition": SelfManagedKafkaStartPositionType,
        "AdditionalBootstrapServers": List[str],
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ConsumerGroupID": str,
        "Credentials": "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
        "ServerRootCaCertificate": str,
        "Vpc": "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    },
    total=False,
)

class PipeSourceSelfManagedKafkaParametersTypeDef(
    _RequiredPipeSourceSelfManagedKafkaParametersTypeDef,
    _OptionalPipeSourceSelfManagedKafkaParametersTypeDef,
):
    pass

PipeSourceSqsQueueParametersTypeDef = TypedDict(
    "PipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

_RequiredPipeTargetBatchJobParametersTypeDef = TypedDict(
    "_RequiredPipeTargetBatchJobParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalPipeTargetBatchJobParametersTypeDef = TypedDict(
    "_OptionalPipeTargetBatchJobParametersTypeDef",
    {
        "ArrayProperties": "BatchArrayPropertiesTypeDef",
        "RetryStrategy": "BatchRetryStrategyTypeDef",
        "ContainerOverrides": "BatchContainerOverridesTypeDef",
        "DependsOn": List["BatchJobDependencyTypeDef"],
        "Parameters": Dict[str, str],
    },
    total=False,
)

class PipeTargetBatchJobParametersTypeDef(
    _RequiredPipeTargetBatchJobParametersTypeDef, _OptionalPipeTargetBatchJobParametersTypeDef
):
    pass

PipeTargetCloudWatchLogsParametersTypeDef = TypedDict(
    "PipeTargetCloudWatchLogsParametersTypeDef",
    {
        "LogStreamName": str,
        "Timestamp": str,
    },
    total=False,
)

_RequiredPipeTargetEcsTaskParametersTypeDef = TypedDict(
    "_RequiredPipeTargetEcsTaskParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalPipeTargetEcsTaskParametersTypeDef = TypedDict(
    "_OptionalPipeTargetEcsTaskParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PlatformVersion": str,
        "Group": str,
        "CapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "PlacementConstraints": List["PlacementConstraintTypeDef"],
        "PlacementStrategy": List["PlacementStrategyTypeDef"],
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Overrides": "EcsTaskOverrideTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PipeTargetEcsTaskParametersTypeDef(
    _RequiredPipeTargetEcsTaskParametersTypeDef, _OptionalPipeTargetEcsTaskParametersTypeDef
):
    pass

PipeTargetEventBridgeEventBusParametersTypeDef = TypedDict(
    "PipeTargetEventBridgeEventBusParametersTypeDef",
    {
        "EndpointId": str,
        "DetailType": str,
        "Source": str,
        "Resources": List[str],
        "Time": str,
    },
    total=False,
)

PipeTargetHttpParametersTypeDef = TypedDict(
    "PipeTargetHttpParametersTypeDef",
    {
        "PathParameterValues": List[str],
        "HeaderParameters": Dict[str, str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

PipeTargetKinesisStreamParametersTypeDef = TypedDict(
    "PipeTargetKinesisStreamParametersTypeDef",
    {
        "PartitionKey": str,
    },
)

PipeTargetLambdaFunctionParametersTypeDef = TypedDict(
    "PipeTargetLambdaFunctionParametersTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
)

PipeTargetParametersTypeDef = TypedDict(
    "PipeTargetParametersTypeDef",
    {
        "InputTemplate": str,
        "LambdaFunctionParameters": "PipeTargetLambdaFunctionParametersTypeDef",
        "StepFunctionStateMachineParameters": "PipeTargetStateMachineParametersTypeDef",
        "KinesisStreamParameters": "PipeTargetKinesisStreamParametersTypeDef",
        "EcsTaskParameters": "PipeTargetEcsTaskParametersTypeDef",
        "BatchJobParameters": "PipeTargetBatchJobParametersTypeDef",
        "SqsQueueParameters": "PipeTargetSqsQueueParametersTypeDef",
        "HttpParameters": "PipeTargetHttpParametersTypeDef",
        "RedshiftDataParameters": "PipeTargetRedshiftDataParametersTypeDef",
        "SageMakerPipelineParameters": "PipeTargetSageMakerPipelineParametersTypeDef",
        "EventBridgeEventBusParameters": "PipeTargetEventBridgeEventBusParametersTypeDef",
        "CloudWatchLogsParameters": "PipeTargetCloudWatchLogsParametersTypeDef",
        "TimestreamParameters": "PipeTargetTimestreamParametersTypeDef",
    },
    total=False,
)

_RequiredPipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredPipeTargetRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sqls": List[str],
    },
)
_OptionalPipeTargetRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalPipeTargetRedshiftDataParametersTypeDef",
    {
        "SecretManagerArn": str,
        "DbUser": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class PipeTargetRedshiftDataParametersTypeDef(
    _RequiredPipeTargetRedshiftDataParametersTypeDef,
    _OptionalPipeTargetRedshiftDataParametersTypeDef,
):
    pass

PipeTargetSageMakerPipelineParametersTypeDef = TypedDict(
    "PipeTargetSageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": List["SageMakerPipelineParameterTypeDef"],
    },
    total=False,
)

PipeTargetSqsQueueParametersTypeDef = TypedDict(
    "PipeTargetSqsQueueParametersTypeDef",
    {
        "MessageGroupId": str,
        "MessageDeduplicationId": str,
    },
    total=False,
)

PipeTargetStateMachineParametersTypeDef = TypedDict(
    "PipeTargetStateMachineParametersTypeDef",
    {
        "InvocationType": PipeTargetInvocationTypeType,
    },
    total=False,
)

_RequiredPipeTargetTimestreamParametersTypeDef = TypedDict(
    "_RequiredPipeTargetTimestreamParametersTypeDef",
    {
        "TimeValue": str,
        "VersionValue": str,
        "DimensionMappings": List["DimensionMappingTypeDef"],
    },
)
_OptionalPipeTargetTimestreamParametersTypeDef = TypedDict(
    "_OptionalPipeTargetTimestreamParametersTypeDef",
    {
        "EpochTimeUnit": EpochTimeUnitType,
        "TimeFieldType": TimeFieldTypeType,
        "TimestampFormat": str,
        "SingleMeasureMappings": List["SingleMeasureMappingTypeDef"],
        "MultiMeasureMappings": List["MultiMeasureMappingTypeDef"],
    },
    total=False,
)

class PipeTargetTimestreamParametersTypeDef(
    _RequiredPipeTargetTimestreamParametersTypeDef, _OptionalPipeTargetTimestreamParametersTypeDef
):
    pass

PipeTypeDef = TypedDict(
    "PipeTypeDef",
    {
        "Name": str,
        "Arn": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Source": str,
        "Target": str,
        "Enrichment": str,
    },
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
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

_RequiredS3LogDestinationParametersTypeDef = TypedDict(
    "_RequiredS3LogDestinationParametersTypeDef",
    {
        "BucketName": str,
        "BucketOwner": str,
    },
)
_OptionalS3LogDestinationParametersTypeDef = TypedDict(
    "_OptionalS3LogDestinationParametersTypeDef",
    {
        "OutputFormat": S3OutputFormatType,
        "Prefix": str,
    },
    total=False,
)

class S3LogDestinationParametersTypeDef(
    _RequiredS3LogDestinationParametersTypeDef, _OptionalS3LogDestinationParametersTypeDef
):
    pass

S3LogDestinationTypeDef = TypedDict(
    "S3LogDestinationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "BucketOwner": str,
        "OutputFormat": S3OutputFormatType,
    },
    total=False,
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SelfManagedKafkaAccessConfigurationCredentialsTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    {
        "BasicAuth": str,
        "SaslScram512Auth": str,
        "SaslScram256Auth": str,
        "ClientCertificateTlsAuth": str,
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationVpcTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroup": List[str],
    },
    total=False,
)

SingleMeasureMappingTypeDef = TypedDict(
    "SingleMeasureMappingTypeDef",
    {
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": str,
    },
)

StartPipeRequestRequestTypeDef = TypedDict(
    "StartPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartPipeResponseTypeDef = TypedDict(
    "StartPipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPipeRequestRequestTypeDef = TypedDict(
    "StopPipeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopPipeResponseTypeDef = TypedDict(
    "StopPipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdatePipeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipeRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalUpdatePipeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipeRequestRequestTypeDef",
    {
        "Description": str,
        "DesiredState": RequestedPipeStateType,
        "SourceParameters": "UpdatePipeSourceParametersTypeDef",
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "Target": str,
        "TargetParameters": "PipeTargetParametersTypeDef",
        "LogConfiguration": "PipeLogConfigurationParametersTypeDef",
    },
    total=False,
)

class UpdatePipeRequestRequestTypeDef(
    _RequiredUpdatePipeRequestRequestTypeDef, _OptionalUpdatePipeRequestRequestTypeDef
):
    pass

UpdatePipeResponseTypeDef = TypedDict(
    "UpdatePipeResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "DesiredState": RequestedPipeStateType,
        "CurrentState": PipeStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "Credentials": "MQBrokerAccessCredentialsTypeDef",
    },
)
_OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef = TypedDict(
    "_OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class UpdatePipeSourceActiveMQBrokerParametersTypeDef(
    _RequiredUpdatePipeSourceActiveMQBrokerParametersTypeDef,
    _OptionalUpdatePipeSourceActiveMQBrokerParametersTypeDef,
):
    pass

UpdatePipeSourceDynamoDBStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
    },
    total=False,
)

UpdatePipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
    },
    total=False,
)

UpdatePipeSourceManagedStreamingKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
    {
        "BatchSize": int,
        "Credentials": "MSKAccessCredentialsTypeDef",
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

UpdatePipeSourceParametersTypeDef = TypedDict(
    "UpdatePipeSourceParametersTypeDef",
    {
        "FilterCriteria": "FilterCriteriaTypeDef",
        "KinesisStreamParameters": "UpdatePipeSourceKinesisStreamParametersTypeDef",
        "DynamoDBStreamParameters": "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
        "SqsQueueParameters": "UpdatePipeSourceSqsQueueParametersTypeDef",
        "ActiveMQBrokerParameters": "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
        "RabbitMQBrokerParameters": "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
        "ManagedStreamingKafkaParameters": "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
        "SelfManagedKafkaParameters": "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    },
    total=False,
)

_RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "Credentials": "MQBrokerAccessCredentialsTypeDef",
    },
)
_OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef = TypedDict(
    "_OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)

class UpdatePipeSourceRabbitMQBrokerParametersTypeDef(
    _RequiredUpdatePipeSourceRabbitMQBrokerParametersTypeDef,
    _OptionalUpdatePipeSourceRabbitMQBrokerParametersTypeDef,
):
    pass

UpdatePipeSourceSelfManagedKafkaParametersTypeDef = TypedDict(
    "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "Credentials": "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
        "ServerRootCaCertificate": str,
        "Vpc": "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    },
    total=False,
)

UpdatePipeSourceSqsQueueParametersTypeDef = TypedDict(
    "UpdatePipeSourceSqsQueueParametersTypeDef",
    {
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
    },
    total=False,
)
