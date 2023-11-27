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
    KinesisStreamStartPositionType,
    LaunchTypeType,
    LogLevelType,
    MSKStartPositionType,
    PipeStateType,
    PipeTargetInvocationTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    RequestedPipeStateDescribeResponseType,
    RequestedPipeStateType,
    S3OutputFormatType,
    SelfManagedKafkaStartPositionType,
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
    "PipeTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogDestinationParametersTypeDef",
    "S3LogDestinationTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
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
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": List[str],
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
        "base": int,
        "weight": int,
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
        "RoleArn": str,
        "Source": str,
        "Target": str,
    },
)
_OptionalCreatePipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipeRequestRequestTypeDef",
    {
        "Description": str,
        "DesiredState": RequestedPipeStateType,
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "LogConfiguration": "PipeLogConfigurationParametersTypeDef",
        "SourceParameters": "PipeSourceParametersTypeDef",
        "Tags": Dict[str, str],
        "TargetParameters": "PipeTargetParametersTypeDef",
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "LastModifiedTime": datetime,
        "Name": str,
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "Description": str,
        "DesiredState": RequestedPipeStateDescribeResponseType,
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "LastModifiedTime": datetime,
        "LogConfiguration": "PipeLogConfigurationTypeDef",
        "Name": str,
        "RoleArn": str,
        "Source": str,
        "SourceParameters": "PipeSourceParametersTypeDef",
        "StateReason": str,
        "Tags": Dict[str, str],
        "Target": str,
        "TargetParameters": "PipeTargetParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "Limit": int,
        "NamePrefix": str,
        "NextToken": str,
        "SourcePrefix": str,
        "TargetPrefix": str,
    },
    total=False,
)

ListPipesResponseTypeDef = TypedDict(
    "ListPipesResponseTypeDef",
    {
        "NextToken": str,
        "Pipes": List["PipeTypeDef"],
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
        "ClientCertificateTlsAuth": str,
        "SaslScram512Auth": str,
    },
    total=False,
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
        "HeaderParameters": Dict[str, str],
        "PathParameterValues": List[str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

PipeEnrichmentParametersTypeDef = TypedDict(
    "PipeEnrichmentParametersTypeDef",
    {
        "HttpParameters": "PipeEnrichmentHttpParametersTypeDef",
        "InputTemplate": str,
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
        "CloudwatchLogsLogDestination": "CloudwatchLogsLogDestinationParametersTypeDef",
        "FirehoseLogDestination": "FirehoseLogDestinationParametersTypeDef",
        "IncludeExecutionData": List[Literal["ALL"]],
        "S3LogDestination": "S3LogDestinationParametersTypeDef",
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
        "CloudwatchLogsLogDestination": "CloudwatchLogsLogDestinationTypeDef",
        "FirehoseLogDestination": "FirehoseLogDestinationTypeDef",
        "IncludeExecutionData": List[Literal["ALL"]],
        "Level": LogLevelType,
        "S3LogDestination": "S3LogDestinationTypeDef",
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
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
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
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
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
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": "MSKAccessCredentialsTypeDef",
        "MaximumBatchingWindowInSeconds": int,
        "StartingPosition": MSKStartPositionType,
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
        "ActiveMQBrokerParameters": "PipeSourceActiveMQBrokerParametersTypeDef",
        "DynamoDBStreamParameters": "PipeSourceDynamoDBStreamParametersTypeDef",
        "FilterCriteria": "FilterCriteriaTypeDef",
        "KinesisStreamParameters": "PipeSourceKinesisStreamParametersTypeDef",
        "ManagedStreamingKafkaParameters": "PipeSourceManagedStreamingKafkaParametersTypeDef",
        "RabbitMQBrokerParameters": "PipeSourceRabbitMQBrokerParametersTypeDef",
        "SelfManagedKafkaParameters": "PipeSourceSelfManagedKafkaParametersTypeDef",
        "SqsQueueParameters": "PipeSourceSqsQueueParametersTypeDef",
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
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "VirtualHost": str,
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
        "AdditionalBootstrapServers": List[str],
        "BatchSize": int,
        "ConsumerGroupID": str,
        "Credentials": "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
        "MaximumBatchingWindowInSeconds": int,
        "ServerRootCaCertificate": str,
        "StartingPosition": SelfManagedKafkaStartPositionType,
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
        "ContainerOverrides": "BatchContainerOverridesTypeDef",
        "DependsOn": List["BatchJobDependencyTypeDef"],
        "Parameters": Dict[str, str],
        "RetryStrategy": "BatchRetryStrategyTypeDef",
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
        "CapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "Overrides": "EcsTaskOverrideTypeDef",
        "PlacementConstraints": List["PlacementConstraintTypeDef"],
        "PlacementStrategy": List["PlacementStrategyTypeDef"],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List["TagTypeDef"],
        "TaskCount": int,
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
        "DetailType": str,
        "EndpointId": str,
        "Resources": List[str],
        "Source": str,
        "Time": str,
    },
    total=False,
)

PipeTargetHttpParametersTypeDef = TypedDict(
    "PipeTargetHttpParametersTypeDef",
    {
        "HeaderParameters": Dict[str, str],
        "PathParameterValues": List[str],
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
        "BatchJobParameters": "PipeTargetBatchJobParametersTypeDef",
        "CloudWatchLogsParameters": "PipeTargetCloudWatchLogsParametersTypeDef",
        "EcsTaskParameters": "PipeTargetEcsTaskParametersTypeDef",
        "EventBridgeEventBusParameters": "PipeTargetEventBridgeEventBusParametersTypeDef",
        "HttpParameters": "PipeTargetHttpParametersTypeDef",
        "InputTemplate": str,
        "KinesisStreamParameters": "PipeTargetKinesisStreamParametersTypeDef",
        "LambdaFunctionParameters": "PipeTargetLambdaFunctionParametersTypeDef",
        "RedshiftDataParameters": "PipeTargetRedshiftDataParametersTypeDef",
        "SageMakerPipelineParameters": "PipeTargetSageMakerPipelineParametersTypeDef",
        "SqsQueueParameters": "PipeTargetSqsQueueParametersTypeDef",
        "StepFunctionStateMachineParameters": "PipeTargetStateMachineParametersTypeDef",
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
        "DbUser": str,
        "SecretManagerArn": str,
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
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
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

PipeTypeDef = TypedDict(
    "PipeTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "Enrichment": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "Source": str,
        "StateReason": str,
        "Target": str,
    },
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "expression": str,
        "type": PlacementConstraintTypeType,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": str,
        "type": PlacementStrategyTypeType,
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
        "BucketOwner": str,
        "OutputFormat": S3OutputFormatType,
        "Prefix": str,
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
        "ClientCertificateTlsAuth": str,
        "SaslScram256Auth": str,
        "SaslScram512Auth": str,
    },
    total=False,
)

SelfManagedKafkaAccessConfigurationVpcTypeDef = TypedDict(
    "SelfManagedKafkaAccessConfigurationVpcTypeDef",
    {
        "SecurityGroup": List[str],
        "Subnets": List[str],
    },
    total=False,
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
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
        "Enrichment": str,
        "EnrichmentParameters": "PipeEnrichmentParametersTypeDef",
        "LogConfiguration": "PipeLogConfigurationParametersTypeDef",
        "SourceParameters": "UpdatePipeSourceParametersTypeDef",
        "Target": str,
        "TargetParameters": "PipeTargetParametersTypeDef",
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
        "CreationTime": datetime,
        "CurrentState": PipeStateType,
        "DesiredState": RequestedPipeStateType,
        "LastModifiedTime": datetime,
        "Name": str,
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
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
        "ParallelizationFactor": int,
    },
    total=False,
)

UpdatePipeSourceKinesisStreamParametersTypeDef = TypedDict(
    "UpdatePipeSourceKinesisStreamParametersTypeDef",
    {
        "BatchSize": int,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "MaximumBatchingWindowInSeconds": int,
        "MaximumRecordAgeInSeconds": int,
        "MaximumRetryAttempts": int,
        "OnPartialBatchItemFailure": Literal["AUTOMATIC_BISECT"],
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
        "ActiveMQBrokerParameters": "UpdatePipeSourceActiveMQBrokerParametersTypeDef",
        "DynamoDBStreamParameters": "UpdatePipeSourceDynamoDBStreamParametersTypeDef",
        "FilterCriteria": "FilterCriteriaTypeDef",
        "KinesisStreamParameters": "UpdatePipeSourceKinesisStreamParametersTypeDef",
        "ManagedStreamingKafkaParameters": "UpdatePipeSourceManagedStreamingKafkaParametersTypeDef",
        "RabbitMQBrokerParameters": "UpdatePipeSourceRabbitMQBrokerParametersTypeDef",
        "SelfManagedKafkaParameters": "UpdatePipeSourceSelfManagedKafkaParametersTypeDef",
        "SqsQueueParameters": "UpdatePipeSourceSqsQueueParametersTypeDef",
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
        "Credentials": "SelfManagedKafkaAccessConfigurationCredentialsTypeDef",
        "MaximumBatchingWindowInSeconds": int,
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
