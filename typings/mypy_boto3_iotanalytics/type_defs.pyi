"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef

    data: AddAttributesActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "CancelPipelineReprocessingRequestRequestTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetContentRequestRequestTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "CreateDatastoreResponseTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "DatasetActionTypeDef",
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
    "DatastorePartitionsTypeDef",
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteDatasetContentRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDatastoreRequestRequestTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DescribePipelineResponseTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestRequestTypeDef",
    "GetDatasetContentResponseTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDatasetContentsRequestRequestTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListDatastoresResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "MessageTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "ParquetConfigurationTypeDef",
    "PartitionTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RunPipelineActivityRequestRequestTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SampleChannelDataRequestRequestTypeDef",
    "SampleChannelDataResponseTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "StartPipelineReprocessingRequestRequestTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimestampPartitionTypeDef",
    "TriggeringDatasetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatastoreRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
)

_RequiredAddAttributesActivityTypeDef = TypedDict(
    "_RequiredAddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
    },
)
_OptionalAddAttributesActivityTypeDef = TypedDict(
    "_OptionalAddAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class AddAttributesActivityTypeDef(
    _RequiredAddAttributesActivityTypeDef, _OptionalAddAttributesActivityTypeDef
):
    pass

BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "channelName": str,
        "messages": List["MessageTypeDef"],
    },
)

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "CancelPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "reprocessingId": str,
    },
)

_RequiredChannelActivityTypeDef = TypedDict(
    "_RequiredChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
    },
)
_OptionalChannelActivityTypeDef = TypedDict(
    "_OptionalChannelActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class ChannelActivityTypeDef(_RequiredChannelActivityTypeDef, _OptionalChannelActivityTypeDef):
    pass

ChannelMessagesTypeDef = TypedDict(
    "ChannelMessagesTypeDef",
    {
        "s3Paths": List[str],
    },
    total=False,
)

ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef",
    {
        "size": "EstimatedResourceSizeTypeDef",
    },
    total=False,
)

ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedChannelS3StorageSummaryTypeDef",
    },
    total=False,
)

ChannelStorageTypeDef = TypedDict(
    "ChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedChannelS3StorageTypeDef",
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": str,
        "channelStorage": "ChannelStorageSummaryTypeDef",
        "status": ChannelStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "name": str,
        "storage": "ChannelStorageTypeDef",
        "arn": str,
        "status": ChannelStatusType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

_RequiredContainerDatasetActionTypeDef = TypedDict(
    "_RequiredContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": "ResourceConfigurationTypeDef",
    },
)
_OptionalContainerDatasetActionTypeDef = TypedDict(
    "_OptionalContainerDatasetActionTypeDef",
    {
        "variables": List["VariableTypeDef"],
    },
    total=False,
)

class ContainerDatasetActionTypeDef(
    _RequiredContainerDatasetActionTypeDef, _OptionalContainerDatasetActionTypeDef
):
    pass

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "channelStorage": "ChannelStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalCreateDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)

class CreateDatasetContentRequestRequestTypeDef(
    _RequiredCreateDatasetContentRequestRequestTypeDef,
    _OptionalCreateDatasetContentRequestRequestTypeDef,
):
    pass

CreateDatasetContentResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseTypeDef",
    {
        "versionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": List["DatasetActionTypeDef"],
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "lateDataRules": List["LateDataRuleTypeDef"],
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
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalCreateDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatastoreRequestRequestTypeDef",
    {
        "datastoreStorage": "DatastoreStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
        "tags": List["TagTypeDef"],
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)

class CreateDatastoreRequestRequestTypeDef(
    _RequiredCreateDatastoreRequestRequestTypeDef, _OptionalCreateDatastoreRequestRequestTypeDef
):
    pass

CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": List["PipelineActivityTypeDef"],
    },
)
_OptionalCreatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePipelineRequestRequestTypeDef(
    _RequiredCreatePipelineRequestRequestTypeDef, _OptionalCreatePipelineRequestRequestTypeDef
):
    pass

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedChannelS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedChannelS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class CustomerManagedChannelS3StorageTypeDef(
    _RequiredCustomerManagedChannelS3StorageTypeDef, _OptionalCustomerManagedChannelS3StorageTypeDef
):
    pass

CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
    },
)
_OptionalCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedDatastoreS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class CustomerManagedDatastoreS3StorageTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalCustomerManagedDatastoreS3StorageTypeDef,
):
    pass

DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {
        "actionName": str,
        "actionType": DatasetActionTypeType,
    },
    total=False,
)

DatasetActionTypeDef = TypedDict(
    "DatasetActionTypeDef",
    {
        "actionName": str,
        "queryAction": "SqlQueryDatasetActionTypeDef",
        "containerAction": "ContainerDatasetActionTypeDef",
    },
    total=False,
)

DatasetContentDeliveryDestinationTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": "IotEventsDestinationConfigurationTypeDef",
        "s3DestinationConfiguration": "S3DestinationConfigurationTypeDef",
    },
    total=False,
)

_RequiredDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_RequiredDatasetContentDeliveryRuleTypeDef",
    {
        "destination": "DatasetContentDeliveryDestinationTypeDef",
    },
)
_OptionalDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_OptionalDatasetContentDeliveryRuleTypeDef",
    {
        "entryName": str,
    },
    total=False,
)

class DatasetContentDeliveryRuleTypeDef(
    _RequiredDatasetContentDeliveryRuleTypeDef, _OptionalDatasetContentDeliveryRuleTypeDef
):
    pass

DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {
        "state": DatasetContentStateType,
        "reason": str,
    },
    total=False,
)

DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": str,
        "status": "DatasetContentStatusTypeDef",
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)

DatasetContentVersionValueTypeDef = TypedDict(
    "DatasetContentVersionValueTypeDef",
    {
        "datasetName": str,
    },
)

DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef",
    {
        "entryName": str,
        "dataURI": str,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": str,
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List["DatasetTriggerTypeDef"],
        "actions": List["DatasetActionSummaryTypeDef"],
    },
    total=False,
)

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {
        "schedule": "ScheduleTypeDef",
        "dataset": "TriggeringDatasetTypeDef",
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": str,
        "arn": str,
        "actions": List["DatasetActionTypeDef"],
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "status": DatasetStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)

DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)

DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    {
        "customerManagedS3Storage": "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    },
    total=False,
)

DatastoreIotSiteWiseMultiLayerStorageTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    },
)

DatastorePartitionTypeDef = TypedDict(
    "DatastorePartitionTypeDef",
    {
        "attributePartition": "PartitionTypeDef",
        "timestampPartition": "TimestampPartitionTypeDef",
    },
    total=False,
)

DatastorePartitionsTypeDef = TypedDict(
    "DatastorePartitionsTypeDef",
    {
        "partitions": List["DatastorePartitionTypeDef"],
    },
    total=False,
)

DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef",
    {
        "size": "EstimatedResourceSizeTypeDef",
    },
    total=False,
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageSummaryTypeDef",
        "iotSiteWiseMultiLayerStorage": "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    },
    total=False,
)

DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageTypeDef",
        "iotSiteWiseMultiLayerStorage": "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    },
    total=False,
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": "DatastoreStorageSummaryTypeDef",
        "status": DatastoreStatusType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatType": FileFormatTypeType,
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)

DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": str,
        "storage": "DatastoreStorageTypeDef",
        "arn": str,
        "status": DatastoreStatusType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
        "datastorePartitions": "DatastorePartitionsTypeDef",
    },
    total=False,
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)

_RequiredDeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalDeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)

class DeleteDatasetContentRequestRequestTypeDef(
    _RequiredDeleteDatasetContentRequestRequestTypeDef,
    _OptionalDeleteDatasetContentRequestRequestTypeDef,
):
    pass

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef",
    {
        "timeoutInMinutes": int,
    },
)

DeltaTimeTypeDef = TypedDict(
    "DeltaTimeTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)

_RequiredDescribeChannelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalDescribeChannelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelRequestRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)

class DescribeChannelRequestRequestTypeDef(
    _RequiredDescribeChannelRequestRequestTypeDef, _OptionalDescribeChannelRequestRequestTypeDef
):
    pass

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "statistics": "ChannelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalDescribeDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDatastoreRequestRequestTypeDef",
    {
        "includeStatistics": bool,
    },
    total=False,
)

class DescribeDatastoreRequestRequestTypeDef(
    _RequiredDescribeDatastoreRequestRequestTypeDef, _OptionalDescribeDatastoreRequestRequestTypeDef
):
    pass

DescribeDatastoreResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseTypeDef",
    {
        "datastore": "DatastoreTypeDef",
        "statistics": "DatastoreStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class DeviceRegistryEnrichActivityTypeDef(
    _RequiredDeviceRegistryEnrichActivityTypeDef, _OptionalDeviceRegistryEnrichActivityTypeDef
):
    pass

_RequiredDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
    },
)
_OptionalDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class DeviceShadowEnrichActivityTypeDef(
    _RequiredDeviceShadowEnrichActivityTypeDef, _OptionalDeviceShadowEnrichActivityTypeDef
):
    pass

EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {
        "estimatedSizeInBytes": float,
        "estimatedOn": datetime,
    },
    total=False,
)

FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {
        "jsonConfiguration": Dict[str, Any],
        "parquetConfiguration": "ParquetConfigurationTypeDef",
    },
    total=False,
)

_RequiredFilterActivityTypeDef = TypedDict(
    "_RequiredFilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
    },
)
_OptionalFilterActivityTypeDef = TypedDict(
    "_OptionalFilterActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class FilterActivityTypeDef(_RequiredFilterActivityTypeDef, _OptionalFilterActivityTypeDef):
    pass

_RequiredGetDatasetContentRequestRequestTypeDef = TypedDict(
    "_RequiredGetDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalGetDatasetContentRequestRequestTypeDef = TypedDict(
    "_OptionalGetDatasetContentRequestRequestTypeDef",
    {
        "versionId": str,
    },
    total=False,
)

class GetDatasetContentRequestRequestTypeDef(
    _RequiredGetDatasetContentRequestRequestTypeDef, _OptionalGetDatasetContentRequestRequestTypeDef
):
    pass

GetDatasetContentResponseTypeDef = TypedDict(
    "GetDatasetContentResponseTypeDef",
    {
        "entries": List["DatasetEntryTypeDef"],
        "timestamp": datetime,
        "status": "DatasetContentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)

IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
    },
)
_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "keyPrefix": str,
    },
    total=False,
)

class IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef(
    _RequiredIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalIotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
):
    pass

_RequiredLambdaActivityTypeDef = TypedDict(
    "_RequiredLambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
    },
)
_OptionalLambdaActivityTypeDef = TypedDict(
    "_OptionalLambdaActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class LambdaActivityTypeDef(_RequiredLambdaActivityTypeDef, _OptionalLambdaActivityTypeDef):
    pass

LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": "DeltaTimeSessionWindowConfigurationTypeDef",
    },
    total=False,
)

_RequiredLateDataRuleTypeDef = TypedDict(
    "_RequiredLateDataRuleTypeDef",
    {
        "ruleConfiguration": "LateDataRuleConfigurationTypeDef",
    },
)
_OptionalLateDataRuleTypeDef = TypedDict(
    "_OptionalLateDataRuleTypeDef",
    {
        "ruleName": str,
    },
    total=False,
)

class LateDataRuleTypeDef(_RequiredLateDataRuleTypeDef, _OptionalLateDataRuleTypeDef):
    pass

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channelSummaries": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatasetContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetContentsRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
_OptionalListDatasetContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetContentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "scheduledOnOrAfter": Union[datetime, str],
        "scheduledBefore": Union[datetime, str],
    },
    total=False,
)

class ListDatasetContentsRequestRequestTypeDef(
    _RequiredListDatasetContentsRequestRequestTypeDef,
    _OptionalListDatasetContentsRequestRequestTypeDef,
):
    pass

ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List["DatasetContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasetSummaries": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List["DatastoreSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List["PipelineSummaryTypeDef"],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)

_RequiredMathActivityTypeDef = TypedDict(
    "_RequiredMathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
    },
)
_OptionalMathActivityTypeDef = TypedDict(
    "_OptionalMathActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class MathActivityTypeDef(_RequiredMathActivityTypeDef, _OptionalMathActivityTypeDef):
    pass

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)

OutputFileUriValueTypeDef = TypedDict(
    "OutputFileUriValueTypeDef",
    {
        "fileName": str,
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

ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef",
    {
        "schemaDefinition": "SchemaDefinitionTypeDef",
    },
    total=False,
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "attributeName": str,
    },
)

PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": "ChannelActivityTypeDef",
        "lambda": "LambdaActivityTypeDef",
        "datastore": "DatastoreActivityTypeDef",
        "addAttributes": "AddAttributesActivityTypeDef",
        "removeAttributes": "RemoveAttributesActivityTypeDef",
        "selectAttributes": "SelectAttributesActivityTypeDef",
        "filter": "FilterActivityTypeDef",
        "math": "MathActivityTypeDef",
        "deviceRegistryEnrich": "DeviceRegistryEnrichActivityTypeDef",
        "deviceShadowEnrich": "DeviceShadowEnrichActivityTypeDef",
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List["ReprocessingSummaryTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List["PipelineActivityTypeDef"],
        "reprocessingSummaries": List["ReprocessingSummaryTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "deltaTime": "DeltaTimeTypeDef",
    },
    total=False,
)

_RequiredRemoveAttributesActivityTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalRemoveAttributesActivityTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class RemoveAttributesActivityTypeDef(
    _RequiredRemoveAttributesActivityTypeDef, _OptionalRemoveAttributesActivityTypeDef
):
    pass

ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": str,
        "status": ReprocessingStatusType,
        "creationTime": datetime,
    },
    total=False,
)

ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "unlimited": bool,
        "numberOfDays": int,
    },
    total=False,
)

RunPipelineActivityRequestRequestTypeDef = TypedDict(
    "RunPipelineActivityRequestRequestTypeDef",
    {
        "pipelineActivity": "PipelineActivityTypeDef",
        "payloads": List[Union[bytes, IO[bytes], StreamingBody]],
    },
)

RunPipelineActivityResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseTypeDef",
    {
        "payloads": List[bytes],
        "logResult": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "glueConfiguration": "GlueConfigurationTypeDef",
    },
    total=False,
)

class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass

_RequiredSampleChannelDataRequestRequestTypeDef = TypedDict(
    "_RequiredSampleChannelDataRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalSampleChannelDataRequestRequestTypeDef = TypedDict(
    "_OptionalSampleChannelDataRequestRequestTypeDef",
    {
        "maxMessages": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
    total=False,
)

class SampleChannelDataRequestRequestTypeDef(
    _RequiredSampleChannelDataRequestRequestTypeDef, _OptionalSampleChannelDataRequestRequestTypeDef
):
    pass

SampleChannelDataResponseTypeDef = TypedDict(
    "SampleChannelDataResponseTypeDef",
    {
        "payloads": List[bytes],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "expression": str,
    },
    total=False,
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": List["ColumnTypeDef"],
    },
    total=False,
)

_RequiredSelectAttributesActivityTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": List[str],
    },
)
_OptionalSelectAttributesActivityTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityTypeDef",
    {
        "next": str,
    },
    total=False,
)

class SelectAttributesActivityTypeDef(
    _RequiredSelectAttributesActivityTypeDef, _OptionalSelectAttributesActivityTypeDef
):
    pass

_RequiredSqlQueryDatasetActionTypeDef = TypedDict(
    "_RequiredSqlQueryDatasetActionTypeDef",
    {
        "sqlQuery": str,
    },
)
_OptionalSqlQueryDatasetActionTypeDef = TypedDict(
    "_OptionalSqlQueryDatasetActionTypeDef",
    {
        "filters": List["QueryFilterTypeDef"],
    },
    total=False,
)

class SqlQueryDatasetActionTypeDef(
    _RequiredSqlQueryDatasetActionTypeDef, _OptionalSqlQueryDatasetActionTypeDef
):
    pass

_RequiredStartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "_RequiredStartPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalStartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "_OptionalStartPipelineReprocessingRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "channelMessages": "ChannelMessagesTypeDef",
    },
    total=False,
)

class StartPipelineReprocessingRequestRequestTypeDef(
    _RequiredStartPipelineReprocessingRequestRequestTypeDef,
    _OptionalStartPipelineReprocessingRequestRequestTypeDef,
):
    pass

StartPipelineReprocessingResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseTypeDef",
    {
        "reprocessingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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

_RequiredTimestampPartitionTypeDef = TypedDict(
    "_RequiredTimestampPartitionTypeDef",
    {
        "attributeName": str,
    },
)
_OptionalTimestampPartitionTypeDef = TypedDict(
    "_OptionalTimestampPartitionTypeDef",
    {
        "timestampFormat": str,
    },
    total=False,
)

class TimestampPartitionTypeDef(
    _RequiredTimestampPartitionTypeDef, _OptionalTimestampPartitionTypeDef
):
    pass

TriggeringDatasetTypeDef = TypedDict(
    "TriggeringDatasetTypeDef",
    {
        "name": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "channelStorage": "ChannelStorageTypeDef",
        "retentionPeriod": "RetentionPeriodTypeDef",
    },
    total=False,
)

class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass

_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": List["DatasetActionTypeDef"],
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "triggers": List["DatasetTriggerTypeDef"],
        "contentDeliveryRules": List["DatasetContentDeliveryRuleTypeDef"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)

class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass

_RequiredUpdateDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
_OptionalUpdateDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatastoreRequestRequestTypeDef",
    {
        "retentionPeriod": "RetentionPeriodTypeDef",
        "datastoreStorage": "DatastoreStorageTypeDef",
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
    },
    total=False,
)

class UpdateDatastoreRequestRequestTypeDef(
    _RequiredUpdateDatastoreRequestRequestTypeDef, _OptionalUpdateDatastoreRequestRequestTypeDef
):
    pass

UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": List["PipelineActivityTypeDef"],
    },
)

_RequiredVariableTypeDef = TypedDict(
    "_RequiredVariableTypeDef",
    {
        "name": str,
    },
)
_OptionalVariableTypeDef = TypedDict(
    "_OptionalVariableTypeDef",
    {
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": "DatasetContentVersionValueTypeDef",
        "outputFileUriValue": "OutputFileUriValueTypeDef",
    },
    total=False,
)

class VariableTypeDef(_RequiredVariableTypeDef, _OptionalVariableTypeDef):
    pass

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "unlimited": bool,
        "maxVersions": int,
    },
    total=False,
)
