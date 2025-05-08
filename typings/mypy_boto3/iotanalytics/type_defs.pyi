"""
Type annotations for iotanalytics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityOutputTypeDef

    data: AddAttributesActivityOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ComputeTypeType,
    DatasetActionTypeType,
    DatasetContentStateType,
    DatasetStatusType,
    DatastoreStatusType,
    FileFormatTypeType,
    ReprocessingStatusType,
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
    "AddAttributesActivityOutputTypeDef",
    "AddAttributesActivityTypeDef",
    "AddAttributesActivityUnionTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BlobTypeDef",
    "CancelPipelineReprocessingRequestTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageOutputTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelStorageUnionTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionOutputTypeDef",
    "ContainerDatasetActionTypeDef",
    "ContainerDatasetActionUnionTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetContentRequestTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreRequestTypeDef",
    "CreateDatastoreResponseTypeDef",
    "CreatePipelineRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionOutputTypeDef",
    "DatasetActionSummaryTypeDef",
    "DatasetActionTypeDef",
    "DatasetActionUnionTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentSummaryTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTriggerTypeDef",
    "DatasetTypeDef",
    "DatastoreActivityTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    "DatastorePartitionTypeDef",
    "DatastorePartitionsOutputTypeDef",
    "DatastorePartitionsTypeDef",
    "DatastorePartitionsUnionTypeDef",
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageOutputTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreStorageUnionTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteDatasetContentRequestTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatastoreRequestTypeDef",
    "DeletePipelineRequestTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDatastoreRequestTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePipelineRequestTypeDef",
    "DescribePipelineResponseTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationOutputTypeDef",
    "FileFormatConfigurationTypeDef",
    "FileFormatConfigurationUnionTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestTypeDef",
    "GetDatasetContentResponseTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "ListChannelsRequestPaginateTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDatasetContentsRequestPaginateTypeDef",
    "ListDatasetContentsRequestTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "ListDatasetsRequestPaginateTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDatastoresRequestPaginateTypeDef",
    "ListDatastoresRequestTypeDef",
    "ListDatastoresResponseTypeDef",
    "ListPipelinesRequestPaginateTypeDef",
    "ListPipelinesRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "MessageTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "ParquetConfigurationOutputTypeDef",
    "ParquetConfigurationTypeDef",
    "PartitionTypeDef",
    "PipelineActivityOutputTypeDef",
    "PipelineActivityTypeDef",
    "PipelineActivityUnionTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "PutLoggingOptionsRequestTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityOutputTypeDef",
    "RemoveAttributesActivityTypeDef",
    "RemoveAttributesActivityUnionTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RunPipelineActivityRequestTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SampleChannelDataRequestTypeDef",
    "SampleChannelDataResponseTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityOutputTypeDef",
    "SelectAttributesActivityTypeDef",
    "SelectAttributesActivityUnionTypeDef",
    "SqlQueryDatasetActionOutputTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "SqlQueryDatasetActionUnionTypeDef",
    "StartPipelineReprocessingRequestTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampPartitionTypeDef",
    "TimestampTypeDef",
    "TriggeringDatasetTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateDatasetRequestTypeDef",
    "UpdateDatastoreRequestTypeDef",
    "UpdatePipelineRequestTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
)

AddAttributesActivityOutputTypeDef = TypedDict(
    "AddAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
        "next": NotRequired[str],
    },
)
AddAttributesActivityTypeDef = TypedDict(
    "AddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Mapping[str, str],
        "next": NotRequired[str],
    },
)

class BatchPutMessageErrorEntryTypeDef(TypedDict):
    messageId: NotRequired[str]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelPipelineReprocessingRequestTypeDef(TypedDict):
    pipelineName: str
    reprocessingId: str

ChannelActivityTypeDef = TypedDict(
    "ChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
        "next": NotRequired[str],
    },
)

class ChannelMessagesTypeDef(TypedDict):
    s3Paths: NotRequired[Sequence[str]]

class EstimatedResourceSizeTypeDef(TypedDict):
    estimatedSizeInBytes: NotRequired[float]
    estimatedOn: NotRequired[datetime]

class CustomerManagedChannelS3StorageTypeDef(TypedDict):
    bucket: str
    roleArn: str
    keyPrefix: NotRequired[str]

class CustomerManagedChannelS3StorageSummaryTypeDef(TypedDict):
    bucket: NotRequired[str]
    keyPrefix: NotRequired[str]
    roleArn: NotRequired[str]

class RetentionPeriodTypeDef(TypedDict):
    unlimited: NotRequired[bool]
    numberOfDays: NotRequired[int]

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

class ResourceConfigurationTypeDef(TypedDict):
    computeType: ComputeTypeType
    volumeSizeInGB: int

class TagTypeDef(TypedDict):
    key: str
    value: str

class CreateDatasetContentRequestTypeDef(TypedDict):
    datasetName: str
    versionId: NotRequired[str]

class VersioningConfigurationTypeDef(TypedDict):
    unlimited: NotRequired[bool]
    maxVersions: NotRequired[int]

class CustomerManagedDatastoreS3StorageSummaryTypeDef(TypedDict):
    bucket: NotRequired[str]
    keyPrefix: NotRequired[str]
    roleArn: NotRequired[str]

class CustomerManagedDatastoreS3StorageTypeDef(TypedDict):
    bucket: str
    roleArn: str
    keyPrefix: NotRequired[str]

class DatasetActionSummaryTypeDef(TypedDict):
    actionName: NotRequired[str]
    actionType: NotRequired[DatasetActionTypeType]

class IotEventsDestinationConfigurationTypeDef(TypedDict):
    inputName: str
    roleArn: str

class DatasetContentStatusTypeDef(TypedDict):
    state: NotRequired[DatasetContentStateType]
    reason: NotRequired[str]

class DatasetContentVersionValueTypeDef(TypedDict):
    datasetName: str

class DatasetEntryTypeDef(TypedDict):
    entryName: NotRequired[str]
    dataURI: NotRequired[str]

class ScheduleTypeDef(TypedDict):
    expression: NotRequired[str]

class TriggeringDatasetTypeDef(TypedDict):
    name: str

class DatastoreActivityTypeDef(TypedDict):
    name: str
    datastoreName: str

class IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef(TypedDict):
    bucket: NotRequired[str]
    keyPrefix: NotRequired[str]

class IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef(TypedDict):
    bucket: str
    keyPrefix: NotRequired[str]

class PartitionTypeDef(TypedDict):
    attributeName: str

class TimestampPartitionTypeDef(TypedDict):
    attributeName: str
    timestampFormat: NotRequired[str]

class DeleteChannelRequestTypeDef(TypedDict):
    channelName: str

class DeleteDatasetContentRequestTypeDef(TypedDict):
    datasetName: str
    versionId: NotRequired[str]

class DeleteDatasetRequestTypeDef(TypedDict):
    datasetName: str

class DeleteDatastoreRequestTypeDef(TypedDict):
    datastoreName: str

class DeletePipelineRequestTypeDef(TypedDict):
    pipelineName: str

class DeltaTimeSessionWindowConfigurationTypeDef(TypedDict):
    timeoutInMinutes: int

class DeltaTimeTypeDef(TypedDict):
    offsetSeconds: int
    timeExpression: str

class DescribeChannelRequestTypeDef(TypedDict):
    channelName: str
    includeStatistics: NotRequired[bool]

class DescribeDatasetRequestTypeDef(TypedDict):
    datasetName: str

class DescribeDatastoreRequestTypeDef(TypedDict):
    datastoreName: str
    includeStatistics: NotRequired[bool]

class LoggingOptionsTypeDef(TypedDict):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool

class DescribePipelineRequestTypeDef(TypedDict):
    pipelineName: str

DeviceRegistryEnrichActivityTypeDef = TypedDict(
    "DeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)
DeviceShadowEnrichActivityTypeDef = TypedDict(
    "DeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)
FilterActivityTypeDef = TypedDict(
    "FilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
        "next": NotRequired[str],
    },
)

class GetDatasetContentRequestTypeDef(TypedDict):
    datasetName: str
    versionId: NotRequired[str]

class GlueConfigurationTypeDef(TypedDict):
    tableName: str
    databaseName: str

LambdaActivityTypeDef = TypedDict(
    "LambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
        "next": NotRequired[str],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChannelsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class ListDatasetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDatastoresRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPipelinesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

MathActivityTypeDef = TypedDict(
    "MathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
        "next": NotRequired[str],
    },
)

class OutputFileUriValueTypeDef(TypedDict):
    fileName: str

RemoveAttributesActivityOutputTypeDef = TypedDict(
    "RemoveAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
        "next": NotRequired[str],
    },
)
SelectAttributesActivityOutputTypeDef = TypedDict(
    "SelectAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
        "next": NotRequired[str],
    },
)
ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[ReprocessingStatusType],
        "creationTime": NotRequired[datetime],
    },
)
RemoveAttributesActivityTypeDef = TypedDict(
    "RemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)
SelectAttributesActivityTypeDef = TypedDict(
    "SelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

AddAttributesActivityUnionTypeDef = Union[
    AddAttributesActivityTypeDef, AddAttributesActivityOutputTypeDef
]

class BatchPutMessageResponseTypeDef(TypedDict):
    batchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetContentResponseTypeDef(TypedDict):
    versionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineResponseTypeDef(TypedDict):
    pipelineName: str
    pipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class RunPipelineActivityResponseTypeDef(TypedDict):
    payloads: List[bytes]
    logResult: str
    ResponseMetadata: ResponseMetadataTypeDef

class SampleChannelDataResponseTypeDef(TypedDict):
    payloads: List[bytes]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineReprocessingResponseTypeDef(TypedDict):
    reprocessingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(TypedDict):
    messageId: str
    payload: BlobTypeDef

class ChannelStatisticsTypeDef(TypedDict):
    size: NotRequired[EstimatedResourceSizeTypeDef]

class DatastoreStatisticsTypeDef(TypedDict):
    size: NotRequired[EstimatedResourceSizeTypeDef]

class ChannelStorageOutputTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Dict[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedChannelS3StorageTypeDef]

class ChannelStorageTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Mapping[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedChannelS3StorageTypeDef]

class ChannelStorageSummaryTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Dict[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedChannelS3StorageSummaryTypeDef]

class CreateChannelResponseTypeDef(TypedDict):
    channelName: str
    channelArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(TypedDict):
    datasetName: str
    datasetArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreResponseTypeDef(TypedDict):
    datastoreName: str
    datastoreArn: str
    retentionPeriod: RetentionPeriodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaDefinitionOutputTypeDef(TypedDict):
    columns: NotRequired[List[ColumnTypeDef]]

class SchemaDefinitionTypeDef(TypedDict):
    columns: NotRequired[Sequence[ColumnTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class DatasetContentSummaryTypeDef(TypedDict):
    version: NotRequired[str]
    status: NotRequired[DatasetContentStatusTypeDef]
    creationTime: NotRequired[datetime]
    scheduleTime: NotRequired[datetime]
    completionTime: NotRequired[datetime]

class GetDatasetContentResponseTypeDef(TypedDict):
    entries: List[DatasetEntryTypeDef]
    timestamp: datetime
    status: DatasetContentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetTriggerTypeDef(TypedDict):
    schedule: NotRequired[ScheduleTypeDef]
    dataset: NotRequired[TriggeringDatasetTypeDef]

class DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef(TypedDict):
    customerManagedS3Storage: NotRequired[
        IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef
    ]

class DatastoreIotSiteWiseMultiLayerStorageTypeDef(TypedDict):
    customerManagedS3Storage: IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef

class DatastorePartitionTypeDef(TypedDict):
    attributePartition: NotRequired[PartitionTypeDef]
    timestampPartition: NotRequired[TimestampPartitionTypeDef]

class LateDataRuleConfigurationTypeDef(TypedDict):
    deltaTimeSessionWindowConfiguration: NotRequired[DeltaTimeSessionWindowConfigurationTypeDef]

class QueryFilterTypeDef(TypedDict):
    deltaTime: NotRequired[DeltaTimeTypeDef]

class DescribeLoggingOptionsResponseTypeDef(TypedDict):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestTypeDef(TypedDict):
    loggingOptions: LoggingOptionsTypeDef

class S3DestinationConfigurationTypeDef(TypedDict):
    bucket: str
    key: str
    roleArn: str
    glueConfiguration: NotRequired[GlueConfigurationTypeDef]

class ListChannelsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatastoresRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPipelinesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetContentsRequestPaginateTypeDef(TypedDict):
    datasetName: str
    scheduledOnOrAfter: NotRequired[TimestampTypeDef]
    scheduledBefore: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetContentsRequestTypeDef(TypedDict):
    datasetName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    scheduledOnOrAfter: NotRequired[TimestampTypeDef]
    scheduledBefore: NotRequired[TimestampTypeDef]

class SampleChannelDataRequestTypeDef(TypedDict):
    channelName: str
    maxMessages: NotRequired[int]
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]

class StartPipelineReprocessingRequestTypeDef(TypedDict):
    pipelineName: str
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    channelMessages: NotRequired[ChannelMessagesTypeDef]

class VariableTypeDef(TypedDict):
    name: str
    stringValue: NotRequired[str]
    doubleValue: NotRequired[float]
    datasetContentVersionValue: NotRequired[DatasetContentVersionValueTypeDef]
    outputFileUriValue: NotRequired[OutputFileUriValueTypeDef]

PipelineActivityOutputTypeDef = TypedDict(
    "PipelineActivityOutputTypeDef",
    {
        "channel": NotRequired[ChannelActivityTypeDef],
        "lambda": NotRequired[LambdaActivityTypeDef],
        "datastore": NotRequired[DatastoreActivityTypeDef],
        "addAttributes": NotRequired[AddAttributesActivityOutputTypeDef],
        "removeAttributes": NotRequired[RemoveAttributesActivityOutputTypeDef],
        "selectAttributes": NotRequired[SelectAttributesActivityOutputTypeDef],
        "filter": NotRequired[FilterActivityTypeDef],
        "math": NotRequired[MathActivityTypeDef],
        "deviceRegistryEnrich": NotRequired[DeviceRegistryEnrichActivityTypeDef],
        "deviceShadowEnrich": NotRequired[DeviceShadowEnrichActivityTypeDef],
    },
)

class PipelineSummaryTypeDef(TypedDict):
    pipelineName: NotRequired[str]
    reprocessingSummaries: NotRequired[List[ReprocessingSummaryTypeDef]]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

RemoveAttributesActivityUnionTypeDef = Union[
    RemoveAttributesActivityTypeDef, RemoveAttributesActivityOutputTypeDef
]
SelectAttributesActivityUnionTypeDef = Union[
    SelectAttributesActivityTypeDef, SelectAttributesActivityOutputTypeDef
]

class BatchPutMessageRequestTypeDef(TypedDict):
    channelName: str
    messages: Sequence[MessageTypeDef]

class ChannelTypeDef(TypedDict):
    name: NotRequired[str]
    storage: NotRequired[ChannelStorageOutputTypeDef]
    arn: NotRequired[str]
    status: NotRequired[ChannelStatusType]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    lastMessageArrivalTime: NotRequired[datetime]

ChannelStorageUnionTypeDef = Union[ChannelStorageTypeDef, ChannelStorageOutputTypeDef]

class ChannelSummaryTypeDef(TypedDict):
    channelName: NotRequired[str]
    channelStorage: NotRequired[ChannelStorageSummaryTypeDef]
    status: NotRequired[ChannelStatusType]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    lastMessageArrivalTime: NotRequired[datetime]

class ParquetConfigurationOutputTypeDef(TypedDict):
    schemaDefinition: NotRequired[SchemaDefinitionOutputTypeDef]

class ParquetConfigurationTypeDef(TypedDict):
    schemaDefinition: NotRequired[SchemaDefinitionTypeDef]

class ListDatasetContentsResponseTypeDef(TypedDict):
    datasetContentSummaries: List[DatasetContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DatasetSummaryTypeDef(TypedDict):
    datasetName: NotRequired[str]
    status: NotRequired[DatasetStatusType]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    triggers: NotRequired[List[DatasetTriggerTypeDef]]
    actions: NotRequired[List[DatasetActionSummaryTypeDef]]

class DatastoreStorageSummaryTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Dict[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedDatastoreS3StorageSummaryTypeDef]
    iotSiteWiseMultiLayerStorage: NotRequired[DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef]

class DatastoreStorageOutputTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Dict[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedDatastoreS3StorageTypeDef]
    iotSiteWiseMultiLayerStorage: NotRequired[DatastoreIotSiteWiseMultiLayerStorageTypeDef]

class DatastoreStorageTypeDef(TypedDict):
    serviceManagedS3: NotRequired[Mapping[str, Any]]
    customerManagedS3: NotRequired[CustomerManagedDatastoreS3StorageTypeDef]
    iotSiteWiseMultiLayerStorage: NotRequired[DatastoreIotSiteWiseMultiLayerStorageTypeDef]

class DatastorePartitionsOutputTypeDef(TypedDict):
    partitions: NotRequired[List[DatastorePartitionTypeDef]]

class DatastorePartitionsTypeDef(TypedDict):
    partitions: NotRequired[Sequence[DatastorePartitionTypeDef]]

class LateDataRuleTypeDef(TypedDict):
    ruleConfiguration: LateDataRuleConfigurationTypeDef
    ruleName: NotRequired[str]

class SqlQueryDatasetActionOutputTypeDef(TypedDict):
    sqlQuery: str
    filters: NotRequired[List[QueryFilterTypeDef]]

class SqlQueryDatasetActionTypeDef(TypedDict):
    sqlQuery: str
    filters: NotRequired[Sequence[QueryFilterTypeDef]]

class DatasetContentDeliveryDestinationTypeDef(TypedDict):
    iotEventsDestinationConfiguration: NotRequired[IotEventsDestinationConfigurationTypeDef]
    s3DestinationConfiguration: NotRequired[S3DestinationConfigurationTypeDef]

class ContainerDatasetActionOutputTypeDef(TypedDict):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: NotRequired[List[VariableTypeDef]]

class ContainerDatasetActionTypeDef(TypedDict):
    image: str
    executionRoleArn: str
    resourceConfiguration: ResourceConfigurationTypeDef
    variables: NotRequired[Sequence[VariableTypeDef]]

class PipelineTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    activities: NotRequired[List[PipelineActivityOutputTypeDef]]
    reprocessingSummaries: NotRequired[List[ReprocessingSummaryTypeDef]]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]

class ListPipelinesResponseTypeDef(TypedDict):
    pipelineSummaries: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": NotRequired[ChannelActivityTypeDef],
        "lambda": NotRequired[LambdaActivityTypeDef],
        "datastore": NotRequired[DatastoreActivityTypeDef],
        "addAttributes": NotRequired[AddAttributesActivityUnionTypeDef],
        "removeAttributes": NotRequired[RemoveAttributesActivityUnionTypeDef],
        "selectAttributes": NotRequired[SelectAttributesActivityUnionTypeDef],
        "filter": NotRequired[FilterActivityTypeDef],
        "math": NotRequired[MathActivityTypeDef],
        "deviceRegistryEnrich": NotRequired[DeviceRegistryEnrichActivityTypeDef],
        "deviceShadowEnrich": NotRequired[DeviceShadowEnrichActivityTypeDef],
    },
)

class DescribeChannelResponseTypeDef(TypedDict):
    channel: ChannelTypeDef
    statistics: ChannelStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestTypeDef(TypedDict):
    channelName: str
    channelStorage: NotRequired[ChannelStorageUnionTypeDef]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateChannelRequestTypeDef(TypedDict):
    channelName: str
    channelStorage: NotRequired[ChannelStorageUnionTypeDef]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]

class ListChannelsResponseTypeDef(TypedDict):
    channelSummaries: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FileFormatConfigurationOutputTypeDef(TypedDict):
    jsonConfiguration: NotRequired[Dict[str, Any]]
    parquetConfiguration: NotRequired[ParquetConfigurationOutputTypeDef]

class FileFormatConfigurationTypeDef(TypedDict):
    jsonConfiguration: NotRequired[Mapping[str, Any]]
    parquetConfiguration: NotRequired[ParquetConfigurationTypeDef]

class ListDatasetsResponseTypeDef(TypedDict):
    datasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DatastoreStorageUnionTypeDef = Union[DatastoreStorageTypeDef, DatastoreStorageOutputTypeDef]

class DatastoreSummaryTypeDef(TypedDict):
    datastoreName: NotRequired[str]
    datastoreStorage: NotRequired[DatastoreStorageSummaryTypeDef]
    status: NotRequired[DatastoreStatusType]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    lastMessageArrivalTime: NotRequired[datetime]
    fileFormatType: NotRequired[FileFormatTypeType]
    datastorePartitions: NotRequired[DatastorePartitionsOutputTypeDef]

DatastorePartitionsUnionTypeDef = Union[
    DatastorePartitionsTypeDef, DatastorePartitionsOutputTypeDef
]
SqlQueryDatasetActionUnionTypeDef = Union[
    SqlQueryDatasetActionTypeDef, SqlQueryDatasetActionOutputTypeDef
]

class DatasetContentDeliveryRuleTypeDef(TypedDict):
    destination: DatasetContentDeliveryDestinationTypeDef
    entryName: NotRequired[str]

class DatasetActionOutputTypeDef(TypedDict):
    actionName: NotRequired[str]
    queryAction: NotRequired[SqlQueryDatasetActionOutputTypeDef]
    containerAction: NotRequired[ContainerDatasetActionOutputTypeDef]

ContainerDatasetActionUnionTypeDef = Union[
    ContainerDatasetActionTypeDef, ContainerDatasetActionOutputTypeDef
]

class DescribePipelineResponseTypeDef(TypedDict):
    pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

PipelineActivityUnionTypeDef = Union[PipelineActivityTypeDef, PipelineActivityOutputTypeDef]

class DatastoreTypeDef(TypedDict):
    name: NotRequired[str]
    storage: NotRequired[DatastoreStorageOutputTypeDef]
    arn: NotRequired[str]
    status: NotRequired[DatastoreStatusType]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    lastMessageArrivalTime: NotRequired[datetime]
    fileFormatConfiguration: NotRequired[FileFormatConfigurationOutputTypeDef]
    datastorePartitions: NotRequired[DatastorePartitionsOutputTypeDef]

FileFormatConfigurationUnionTypeDef = Union[
    FileFormatConfigurationTypeDef, FileFormatConfigurationOutputTypeDef
]

class ListDatastoresResponseTypeDef(TypedDict):
    datastoreSummaries: List[DatastoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DatasetTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    actions: NotRequired[List[DatasetActionOutputTypeDef]]
    triggers: NotRequired[List[DatasetTriggerTypeDef]]
    contentDeliveryRules: NotRequired[List[DatasetContentDeliveryRuleTypeDef]]
    status: NotRequired[DatasetStatusType]
    creationTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    versioningConfiguration: NotRequired[VersioningConfigurationTypeDef]
    lateDataRules: NotRequired[List[LateDataRuleTypeDef]]

class DatasetActionTypeDef(TypedDict):
    actionName: NotRequired[str]
    queryAction: NotRequired[SqlQueryDatasetActionUnionTypeDef]
    containerAction: NotRequired[ContainerDatasetActionUnionTypeDef]

class CreatePipelineRequestTypeDef(TypedDict):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnionTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

class RunPipelineActivityRequestTypeDef(TypedDict):
    pipelineActivity: PipelineActivityUnionTypeDef
    payloads: Sequence[BlobTypeDef]

class UpdatePipelineRequestTypeDef(TypedDict):
    pipelineName: str
    pipelineActivities: Sequence[PipelineActivityUnionTypeDef]

class DescribeDatastoreResponseTypeDef(TypedDict):
    datastore: DatastoreTypeDef
    statistics: DatastoreStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatastoreRequestTypeDef(TypedDict):
    datastoreName: str
    datastoreStorage: NotRequired[DatastoreStorageUnionTypeDef]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    fileFormatConfiguration: NotRequired[FileFormatConfigurationUnionTypeDef]
    datastorePartitions: NotRequired[DatastorePartitionsUnionTypeDef]

class UpdateDatastoreRequestTypeDef(TypedDict):
    datastoreName: str
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    datastoreStorage: NotRequired[DatastoreStorageUnionTypeDef]
    fileFormatConfiguration: NotRequired[FileFormatConfigurationUnionTypeDef]

class DescribeDatasetResponseTypeDef(TypedDict):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DatasetActionUnionTypeDef = Union[DatasetActionTypeDef, DatasetActionOutputTypeDef]

class CreateDatasetRequestTypeDef(TypedDict):
    datasetName: str
    actions: Sequence[DatasetActionUnionTypeDef]
    triggers: NotRequired[Sequence[DatasetTriggerTypeDef]]
    contentDeliveryRules: NotRequired[Sequence[DatasetContentDeliveryRuleTypeDef]]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    versioningConfiguration: NotRequired[VersioningConfigurationTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    lateDataRules: NotRequired[Sequence[LateDataRuleTypeDef]]

class UpdateDatasetRequestTypeDef(TypedDict):
    datasetName: str
    actions: Sequence[DatasetActionUnionTypeDef]
    triggers: NotRequired[Sequence[DatasetTriggerTypeDef]]
    contentDeliveryRules: NotRequired[Sequence[DatasetContentDeliveryRuleTypeDef]]
    retentionPeriod: NotRequired[RetentionPeriodTypeDef]
    versioningConfiguration: NotRequired[VersioningConfigurationTypeDef]
    lateDataRules: NotRequired[Sequence[LateDataRuleTypeDef]]
