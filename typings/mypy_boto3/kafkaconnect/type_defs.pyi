"""
Type annotations for kafkaconnect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kafkaconnect.type_defs import VpcDescriptionTypeDef

    data: VpcDescriptionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ConnectorOperationStateType,
    ConnectorOperationStepStateType,
    ConnectorOperationStepTypeType,
    ConnectorOperationTypeType,
    ConnectorStateType,
    CustomPluginContentTypeType,
    CustomPluginStateType,
    KafkaClusterClientAuthenticationTypeType,
    KafkaClusterEncryptionInTransitTypeType,
    WorkerConfigurationStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApacheKafkaClusterDescriptionTypeDef",
    "ApacheKafkaClusterTypeDef",
    "AutoScalingDescriptionTypeDef",
    "AutoScalingTypeDef",
    "AutoScalingUpdateTypeDef",
    "CapacityDescriptionTypeDef",
    "CapacityTypeDef",
    "CapacityUpdateTypeDef",
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    "CloudWatchLogsLogDeliveryTypeDef",
    "ConnectorOperationStepTypeDef",
    "ConnectorOperationSummaryTypeDef",
    "ConnectorSummaryTypeDef",
    "CreateConnectorRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateCustomPluginRequestTypeDef",
    "CreateCustomPluginResponseTypeDef",
    "CreateWorkerConfigurationRequestTypeDef",
    "CreateWorkerConfigurationResponseTypeDef",
    "CustomPluginDescriptionTypeDef",
    "CustomPluginFileDescriptionTypeDef",
    "CustomPluginLocationDescriptionTypeDef",
    "CustomPluginLocationTypeDef",
    "CustomPluginRevisionSummaryTypeDef",
    "CustomPluginSummaryTypeDef",
    "CustomPluginTypeDef",
    "DeleteConnectorRequestTypeDef",
    "DeleteConnectorResponseTypeDef",
    "DeleteCustomPluginRequestTypeDef",
    "DeleteCustomPluginResponseTypeDef",
    "DeleteWorkerConfigurationRequestTypeDef",
    "DeleteWorkerConfigurationResponseTypeDef",
    "DescribeConnectorOperationRequestTypeDef",
    "DescribeConnectorOperationResponseTypeDef",
    "DescribeConnectorRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeCustomPluginRequestTypeDef",
    "DescribeCustomPluginResponseTypeDef",
    "DescribeWorkerConfigurationRequestTypeDef",
    "DescribeWorkerConfigurationResponseTypeDef",
    "FirehoseLogDeliveryDescriptionTypeDef",
    "FirehoseLogDeliveryTypeDef",
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    "KafkaClusterClientAuthenticationTypeDef",
    "KafkaClusterDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitTypeDef",
    "KafkaClusterTypeDef",
    "ListConnectorOperationsRequestPaginateTypeDef",
    "ListConnectorOperationsRequestTypeDef",
    "ListConnectorOperationsResponseTypeDef",
    "ListConnectorsRequestPaginateTypeDef",
    "ListConnectorsRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListCustomPluginsRequestPaginateTypeDef",
    "ListCustomPluginsRequestTypeDef",
    "ListCustomPluginsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkerConfigurationsRequestPaginateTypeDef",
    "ListWorkerConfigurationsRequestTypeDef",
    "ListWorkerConfigurationsResponseTypeDef",
    "LogDeliveryDescriptionTypeDef",
    "LogDeliveryTypeDef",
    "PaginatorConfigTypeDef",
    "PluginDescriptionTypeDef",
    "PluginTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "ProvisionedCapacityTypeDef",
    "ProvisionedCapacityUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationDescriptionTypeDef",
    "S3LocationTypeDef",
    "S3LogDeliveryDescriptionTypeDef",
    "S3LogDeliveryTypeDef",
    "ScaleInPolicyDescriptionTypeDef",
    "ScaleInPolicyTypeDef",
    "ScaleInPolicyUpdateTypeDef",
    "ScaleOutPolicyDescriptionTypeDef",
    "ScaleOutPolicyTypeDef",
    "ScaleOutPolicyUpdateTypeDef",
    "StateDescriptionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectorRequestTypeDef",
    "UpdateConnectorResponseTypeDef",
    "VpcDescriptionTypeDef",
    "VpcTypeDef",
    "WorkerConfigurationDescriptionTypeDef",
    "WorkerConfigurationRevisionDescriptionTypeDef",
    "WorkerConfigurationRevisionSummaryTypeDef",
    "WorkerConfigurationSummaryTypeDef",
    "WorkerConfigurationTypeDef",
    "WorkerLogDeliveryDescriptionTypeDef",
    "WorkerLogDeliveryTypeDef",
    "WorkerSettingTypeDef",
)

class VpcDescriptionTypeDef(TypedDict):
    securityGroups: NotRequired[List[str]]
    subnets: NotRequired[List[str]]

class VpcTypeDef(TypedDict):
    subnets: Sequence[str]
    securityGroups: NotRequired[Sequence[str]]

class ScaleInPolicyDescriptionTypeDef(TypedDict):
    cpuUtilizationPercentage: NotRequired[int]

class ScaleOutPolicyDescriptionTypeDef(TypedDict):
    cpuUtilizationPercentage: NotRequired[int]

class ScaleInPolicyTypeDef(TypedDict):
    cpuUtilizationPercentage: int

class ScaleOutPolicyTypeDef(TypedDict):
    cpuUtilizationPercentage: int

class ScaleInPolicyUpdateTypeDef(TypedDict):
    cpuUtilizationPercentage: int

class ScaleOutPolicyUpdateTypeDef(TypedDict):
    cpuUtilizationPercentage: int

class ProvisionedCapacityDescriptionTypeDef(TypedDict):
    mcuCount: NotRequired[int]
    workerCount: NotRequired[int]

class ProvisionedCapacityTypeDef(TypedDict):
    mcuCount: int
    workerCount: int

class ProvisionedCapacityUpdateTypeDef(TypedDict):
    mcuCount: int
    workerCount: int

class CloudWatchLogsLogDeliveryDescriptionTypeDef(TypedDict):
    enabled: NotRequired[bool]
    logGroup: NotRequired[str]

class CloudWatchLogsLogDeliveryTypeDef(TypedDict):
    enabled: bool
    logGroup: NotRequired[str]

class ConnectorOperationStepTypeDef(TypedDict):
    stepType: NotRequired[ConnectorOperationStepTypeType]
    stepState: NotRequired[ConnectorOperationStepStateType]

class ConnectorOperationSummaryTypeDef(TypedDict):
    connectorOperationArn: NotRequired[str]
    connectorOperationType: NotRequired[ConnectorOperationTypeType]
    connectorOperationState: NotRequired[ConnectorOperationStateType]
    creationTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class KafkaClusterClientAuthenticationDescriptionTypeDef(TypedDict):
    authenticationType: NotRequired[KafkaClusterClientAuthenticationTypeType]

class KafkaClusterEncryptionInTransitDescriptionTypeDef(TypedDict):
    encryptionType: NotRequired[KafkaClusterEncryptionInTransitTypeType]

class WorkerConfigurationDescriptionTypeDef(TypedDict):
    revision: NotRequired[int]
    workerConfigurationArn: NotRequired[str]

class KafkaClusterClientAuthenticationTypeDef(TypedDict):
    authenticationType: KafkaClusterClientAuthenticationTypeType

class KafkaClusterEncryptionInTransitTypeDef(TypedDict):
    encryptionType: KafkaClusterEncryptionInTransitTypeType

class WorkerConfigurationTypeDef(TypedDict):
    revision: int
    workerConfigurationArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateWorkerConfigurationRequestTypeDef(TypedDict):
    name: str
    propertiesFileContent: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class WorkerConfigurationRevisionSummaryTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    description: NotRequired[str]
    revision: NotRequired[int]

class CustomPluginDescriptionTypeDef(TypedDict):
    customPluginArn: NotRequired[str]
    revision: NotRequired[int]

class CustomPluginFileDescriptionTypeDef(TypedDict):
    fileMd5: NotRequired[str]
    fileSize: NotRequired[int]

class S3LocationDescriptionTypeDef(TypedDict):
    bucketArn: NotRequired[str]
    fileKey: NotRequired[str]
    objectVersion: NotRequired[str]

class S3LocationTypeDef(TypedDict):
    bucketArn: str
    fileKey: str
    objectVersion: NotRequired[str]

class CustomPluginTypeDef(TypedDict):
    customPluginArn: str
    revision: int

class DeleteConnectorRequestTypeDef(TypedDict):
    connectorArn: str
    currentVersion: NotRequired[str]

class DeleteCustomPluginRequestTypeDef(TypedDict):
    customPluginArn: str

class DeleteWorkerConfigurationRequestTypeDef(TypedDict):
    workerConfigurationArn: str

class DescribeConnectorOperationRequestTypeDef(TypedDict):
    connectorOperationArn: str

class StateDescriptionTypeDef(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]

class DescribeConnectorRequestTypeDef(TypedDict):
    connectorArn: str

class DescribeCustomPluginRequestTypeDef(TypedDict):
    customPluginArn: str

class DescribeWorkerConfigurationRequestTypeDef(TypedDict):
    workerConfigurationArn: str

class WorkerConfigurationRevisionDescriptionTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    description: NotRequired[str]
    propertiesFileContent: NotRequired[str]
    revision: NotRequired[int]

class FirehoseLogDeliveryDescriptionTypeDef(TypedDict):
    deliveryStream: NotRequired[str]
    enabled: NotRequired[bool]

class FirehoseLogDeliveryTypeDef(TypedDict):
    enabled: bool
    deliveryStream: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConnectorOperationsRequestTypeDef(TypedDict):
    connectorArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListConnectorsRequestTypeDef(TypedDict):
    connectorNamePrefix: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCustomPluginsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    namePrefix: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListWorkerConfigurationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    namePrefix: NotRequired[str]

class S3LogDeliveryDescriptionTypeDef(TypedDict):
    bucket: NotRequired[str]
    enabled: NotRequired[bool]
    prefix: NotRequired[str]

class S3LogDeliveryTypeDef(TypedDict):
    enabled: bool
    bucket: NotRequired[str]
    prefix: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class ApacheKafkaClusterDescriptionTypeDef(TypedDict):
    bootstrapServers: NotRequired[str]
    vpc: NotRequired[VpcDescriptionTypeDef]

class ApacheKafkaClusterTypeDef(TypedDict):
    bootstrapServers: str
    vpc: VpcTypeDef

class AutoScalingDescriptionTypeDef(TypedDict):
    maxWorkerCount: NotRequired[int]
    mcuCount: NotRequired[int]
    minWorkerCount: NotRequired[int]
    scaleInPolicy: NotRequired[ScaleInPolicyDescriptionTypeDef]
    scaleOutPolicy: NotRequired[ScaleOutPolicyDescriptionTypeDef]

class AutoScalingTypeDef(TypedDict):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: NotRequired[ScaleInPolicyTypeDef]
    scaleOutPolicy: NotRequired[ScaleOutPolicyTypeDef]

class AutoScalingUpdateTypeDef(TypedDict):
    maxWorkerCount: int
    mcuCount: int
    minWorkerCount: int
    scaleInPolicy: ScaleInPolicyUpdateTypeDef
    scaleOutPolicy: ScaleOutPolicyUpdateTypeDef

class CreateConnectorResponseTypeDef(TypedDict):
    connectorArn: str
    connectorName: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomPluginResponseTypeDef(TypedDict):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    name: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectorResponseTypeDef(TypedDict):
    connectorArn: str
    connectorState: ConnectorStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomPluginResponseTypeDef(TypedDict):
    customPluginArn: str
    customPluginState: CustomPluginStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkerConfigurationResponseTypeDef(TypedDict):
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorOperationsResponseTypeDef(TypedDict):
    connectorOperations: List[ConnectorOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorResponseTypeDef(TypedDict):
    connectorArn: str
    connectorState: ConnectorStateType
    connectorOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkerConfigurationResponseTypeDef(TypedDict):
    creationTime: datetime
    latestRevision: WorkerConfigurationRevisionSummaryTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class WorkerConfigurationSummaryTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    description: NotRequired[str]
    latestRevision: NotRequired[WorkerConfigurationRevisionSummaryTypeDef]
    name: NotRequired[str]
    workerConfigurationArn: NotRequired[str]
    workerConfigurationState: NotRequired[WorkerConfigurationStateType]

class PluginDescriptionTypeDef(TypedDict):
    customPlugin: NotRequired[CustomPluginDescriptionTypeDef]

class CustomPluginLocationDescriptionTypeDef(TypedDict):
    s3Location: NotRequired[S3LocationDescriptionTypeDef]

class CustomPluginLocationTypeDef(TypedDict):
    s3Location: S3LocationTypeDef

class PluginTypeDef(TypedDict):
    customPlugin: CustomPluginTypeDef

class DescribeWorkerConfigurationResponseTypeDef(TypedDict):
    creationTime: datetime
    description: str
    latestRevision: WorkerConfigurationRevisionDescriptionTypeDef
    name: str
    workerConfigurationArn: str
    workerConfigurationState: WorkerConfigurationStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorOperationsRequestPaginateTypeDef(TypedDict):
    connectorArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectorsRequestPaginateTypeDef(TypedDict):
    connectorNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomPluginsRequestPaginateTypeDef(TypedDict):
    namePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkerConfigurationsRequestPaginateTypeDef(TypedDict):
    namePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class WorkerLogDeliveryDescriptionTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogsLogDeliveryDescriptionTypeDef]
    firehose: NotRequired[FirehoseLogDeliveryDescriptionTypeDef]
    s3: NotRequired[S3LogDeliveryDescriptionTypeDef]

class WorkerLogDeliveryTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogsLogDeliveryTypeDef]
    firehose: NotRequired[FirehoseLogDeliveryTypeDef]
    s3: NotRequired[S3LogDeliveryTypeDef]

class KafkaClusterDescriptionTypeDef(TypedDict):
    apacheKafkaCluster: NotRequired[ApacheKafkaClusterDescriptionTypeDef]

class KafkaClusterTypeDef(TypedDict):
    apacheKafkaCluster: ApacheKafkaClusterTypeDef

class CapacityDescriptionTypeDef(TypedDict):
    autoScaling: NotRequired[AutoScalingDescriptionTypeDef]
    provisionedCapacity: NotRequired[ProvisionedCapacityDescriptionTypeDef]

class CapacityTypeDef(TypedDict):
    autoScaling: NotRequired[AutoScalingTypeDef]
    provisionedCapacity: NotRequired[ProvisionedCapacityTypeDef]

class CapacityUpdateTypeDef(TypedDict):
    autoScaling: NotRequired[AutoScalingUpdateTypeDef]
    provisionedCapacity: NotRequired[ProvisionedCapacityUpdateTypeDef]

class ListWorkerConfigurationsResponseTypeDef(TypedDict):
    workerConfigurations: List[WorkerConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CustomPluginRevisionSummaryTypeDef(TypedDict):
    contentType: NotRequired[CustomPluginContentTypeType]
    creationTime: NotRequired[datetime]
    description: NotRequired[str]
    fileDescription: NotRequired[CustomPluginFileDescriptionTypeDef]
    location: NotRequired[CustomPluginLocationDescriptionTypeDef]
    revision: NotRequired[int]

class CreateCustomPluginRequestTypeDef(TypedDict):
    contentType: CustomPluginContentTypeType
    location: CustomPluginLocationTypeDef
    name: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class LogDeliveryDescriptionTypeDef(TypedDict):
    workerLogDelivery: NotRequired[WorkerLogDeliveryDescriptionTypeDef]

class LogDeliveryTypeDef(TypedDict):
    workerLogDelivery: WorkerLogDeliveryTypeDef

class WorkerSettingTypeDef(TypedDict):
    capacity: NotRequired[CapacityDescriptionTypeDef]

class UpdateConnectorRequestTypeDef(TypedDict):
    connectorArn: str
    currentVersion: str
    capacity: NotRequired[CapacityUpdateTypeDef]
    connectorConfiguration: NotRequired[Mapping[str, str]]

class CustomPluginSummaryTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    customPluginArn: NotRequired[str]
    customPluginState: NotRequired[CustomPluginStateType]
    description: NotRequired[str]
    latestRevision: NotRequired[CustomPluginRevisionSummaryTypeDef]
    name: NotRequired[str]

class DescribeCustomPluginResponseTypeDef(TypedDict):
    creationTime: datetime
    customPluginArn: str
    customPluginState: CustomPluginStateType
    description: str
    latestRevision: CustomPluginRevisionSummaryTypeDef
    name: str
    stateDescription: StateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorSummaryTypeDef(TypedDict):
    capacity: NotRequired[CapacityDescriptionTypeDef]
    connectorArn: NotRequired[str]
    connectorDescription: NotRequired[str]
    connectorName: NotRequired[str]
    connectorState: NotRequired[ConnectorStateType]
    creationTime: NotRequired[datetime]
    currentVersion: NotRequired[str]
    kafkaCluster: NotRequired[KafkaClusterDescriptionTypeDef]
    kafkaClusterClientAuthentication: NotRequired[
        KafkaClusterClientAuthenticationDescriptionTypeDef
    ]
    kafkaClusterEncryptionInTransit: NotRequired[KafkaClusterEncryptionInTransitDescriptionTypeDef]
    kafkaConnectVersion: NotRequired[str]
    logDelivery: NotRequired[LogDeliveryDescriptionTypeDef]
    plugins: NotRequired[List[PluginDescriptionTypeDef]]
    serviceExecutionRoleArn: NotRequired[str]
    workerConfiguration: NotRequired[WorkerConfigurationDescriptionTypeDef]

class DescribeConnectorResponseTypeDef(TypedDict):
    capacity: CapacityDescriptionTypeDef
    connectorArn: str
    connectorConfiguration: Dict[str, str]
    connectorDescription: str
    connectorName: str
    connectorState: ConnectorStateType
    creationTime: datetime
    currentVersion: str
    kafkaCluster: KafkaClusterDescriptionTypeDef
    kafkaClusterClientAuthentication: KafkaClusterClientAuthenticationDescriptionTypeDef
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransitDescriptionTypeDef
    kafkaConnectVersion: str
    logDelivery: LogDeliveryDescriptionTypeDef
    plugins: List[PluginDescriptionTypeDef]
    serviceExecutionRoleArn: str
    workerConfiguration: WorkerConfigurationDescriptionTypeDef
    stateDescription: StateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorRequestTypeDef(TypedDict):
    capacity: CapacityTypeDef
    connectorConfiguration: Mapping[str, str]
    connectorName: str
    kafkaCluster: KafkaClusterTypeDef
    kafkaClusterClientAuthentication: KafkaClusterClientAuthenticationTypeDef
    kafkaClusterEncryptionInTransit: KafkaClusterEncryptionInTransitTypeDef
    kafkaConnectVersion: str
    plugins: Sequence[PluginTypeDef]
    serviceExecutionRoleArn: str
    connectorDescription: NotRequired[str]
    logDelivery: NotRequired[LogDeliveryTypeDef]
    workerConfiguration: NotRequired[WorkerConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class DescribeConnectorOperationResponseTypeDef(TypedDict):
    connectorArn: str
    connectorOperationArn: str
    connectorOperationState: ConnectorOperationStateType
    connectorOperationType: ConnectorOperationTypeType
    operationSteps: List[ConnectorOperationStepTypeDef]
    originWorkerSetting: WorkerSettingTypeDef
    originConnectorConfiguration: Dict[str, str]
    targetWorkerSetting: WorkerSettingTypeDef
    targetConnectorConfiguration: Dict[str, str]
    errorInfo: StateDescriptionTypeDef
    creationTime: datetime
    endTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomPluginsResponseTypeDef(TypedDict):
    customPlugins: List[CustomPluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListConnectorsResponseTypeDef(TypedDict):
    connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
