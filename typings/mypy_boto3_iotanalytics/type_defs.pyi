"""
Main interface for iotanalytics service type definitions.

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef

    data: AddAttributesActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    "ChannelActivityTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionTypeDef",
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
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationTypeDef",
    "FilterActivityTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "OutputFileUriValueTypeDef",
    "ParquetConfigurationTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "RetentionPeriodTypeDef",
    "S3DestinationConfigurationTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "TagTypeDef",
    "TriggeringDatasetTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
    "BatchPutMessageResponseTypeDef",
    "ChannelMessagesTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "CreatePipelineResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePipelineResponseTypeDef",
    "GetDatasetContentResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDatastoresResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "SampleChannelDataResponseTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
)

_RequiredAddAttributesActivityTypeDef = TypedDict(
    "_RequiredAddAttributesActivityTypeDef", {"name": str, "attributes": Dict[str, str]}
)
_OptionalAddAttributesActivityTypeDef = TypedDict(
    "_OptionalAddAttributesActivityTypeDef", {"next": str}, total=False
)


class AddAttributesActivityTypeDef(
    _RequiredAddAttributesActivityTypeDef, _OptionalAddAttributesActivityTypeDef
):
    pass


BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)

_RequiredChannelActivityTypeDef = TypedDict(
    "_RequiredChannelActivityTypeDef", {"name": str, "channelName": str}
)
_OptionalChannelActivityTypeDef = TypedDict(
    "_OptionalChannelActivityTypeDef", {"next": str}, total=False
)


class ChannelActivityTypeDef(_RequiredChannelActivityTypeDef, _OptionalChannelActivityTypeDef):
    pass


ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef", {"size": "EstimatedResourceSizeTypeDef"}, total=False
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
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
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
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
    },
    total=False,
)

ColumnTypeDef = TypedDict("ColumnTypeDef", {"name": str, "type": str})

_RequiredContainerDatasetActionTypeDef = TypedDict(
    "_RequiredContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": "ResourceConfigurationTypeDef",
    },
)
_OptionalContainerDatasetActionTypeDef = TypedDict(
    "_OptionalContainerDatasetActionTypeDef", {"variables": List["VariableTypeDef"]}, total=False
)


class ContainerDatasetActionTypeDef(
    _RequiredContainerDatasetActionTypeDef, _OptionalContainerDatasetActionTypeDef
):
    pass


CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

_RequiredCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedChannelS3StorageTypeDef", {"bucket": str, "roleArn": str}
)
_OptionalCustomerManagedChannelS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedChannelS3StorageTypeDef", {"keyPrefix": str}, total=False
)


class CustomerManagedChannelS3StorageTypeDef(
    _RequiredCustomerManagedChannelS3StorageTypeDef, _OptionalCustomerManagedChannelS3StorageTypeDef
):
    pass


CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

_RequiredCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_RequiredCustomerManagedDatastoreS3StorageTypeDef", {"bucket": str, "roleArn": str}
)
_OptionalCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "_OptionalCustomerManagedDatastoreS3StorageTypeDef", {"keyPrefix": str}, total=False
)


class CustomerManagedDatastoreS3StorageTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageTypeDef,
    _OptionalCustomerManagedDatastoreS3StorageTypeDef,
):
    pass


DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {"actionName": str, "actionType": Literal["QUERY", "CONTAINER"]},
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
    {"destination": "DatasetContentDeliveryDestinationTypeDef"},
)
_OptionalDatasetContentDeliveryRuleTypeDef = TypedDict(
    "_OptionalDatasetContentDeliveryRuleTypeDef", {"entryName": str}, total=False
)


class DatasetContentDeliveryRuleTypeDef(
    _RequiredDatasetContentDeliveryRuleTypeDef, _OptionalDatasetContentDeliveryRuleTypeDef
):
    pass


DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
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
    "DatasetContentVersionValueTypeDef", {"datasetName": str}
)

DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef", {"entryName": str, "dataURI": str}, total=False
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List["DatasetTriggerTypeDef"],
        "actions": List["DatasetActionSummaryTypeDef"],
    },
    total=False,
)

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {"schedule": "ScheduleTypeDef", "dataset": "TriggeringDatasetTypeDef"},
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
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "versioningConfiguration": "VersioningConfigurationTypeDef",
        "lateDataRules": List["LateDataRuleTypeDef"],
    },
    total=False,
)

DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef", {"name": str, "datastoreName": str}
)

DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef", {"size": "EstimatedResourceSizeTypeDef"}, total=False
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    },
    total=False,
)

DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": "CustomerManagedDatastoreS3StorageTypeDef",
    },
    total=False,
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": "DatastoreStorageSummaryTypeDef",
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatType": Literal["JSON", "PARQUET"],
    },
    total=False,
)

DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": str,
        "storage": "DatastoreStorageTypeDef",
        "arn": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": "RetentionPeriodTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "lastMessageArrivalTime": datetime,
        "fileFormatConfiguration": "FileFormatConfigurationTypeDef",
    },
    total=False,
)

DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef", {"timeoutInMinutes": int}
)

DeltaTimeTypeDef = TypedDict("DeltaTimeTypeDef", {"offsetSeconds": int, "timeExpression": str})

_RequiredDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityTypeDef", {"next": str}, total=False
)


class DeviceRegistryEnrichActivityTypeDef(
    _RequiredDeviceRegistryEnrichActivityTypeDef, _OptionalDeviceRegistryEnrichActivityTypeDef
):
    pass


_RequiredDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityTypeDef", {"next": str}, total=False
)


class DeviceShadowEnrichActivityTypeDef(
    _RequiredDeviceShadowEnrichActivityTypeDef, _OptionalDeviceShadowEnrichActivityTypeDef
):
    pass


EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)

FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {"jsonConfiguration": Dict[str, Any], "parquetConfiguration": "ParquetConfigurationTypeDef"},
    total=False,
)

_RequiredFilterActivityTypeDef = TypedDict(
    "_RequiredFilterActivityTypeDef", {"name": str, "filter": str}
)
_OptionalFilterActivityTypeDef = TypedDict(
    "_OptionalFilterActivityTypeDef", {"next": str}, total=False
)


class FilterActivityTypeDef(_RequiredFilterActivityTypeDef, _OptionalFilterActivityTypeDef):
    pass


GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef", {"tableName": str, "databaseName": str}
)

IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef", {"inputName": str, "roleArn": str}
)

_RequiredLambdaActivityTypeDef = TypedDict(
    "_RequiredLambdaActivityTypeDef", {"name": str, "lambdaName": str, "batchSize": int}
)
_OptionalLambdaActivityTypeDef = TypedDict(
    "_OptionalLambdaActivityTypeDef", {"next": str}, total=False
)


class LambdaActivityTypeDef(_RequiredLambdaActivityTypeDef, _OptionalLambdaActivityTypeDef):
    pass


LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {"deltaTimeSessionWindowConfiguration": "DeltaTimeSessionWindowConfigurationTypeDef"},
    total=False,
)

_RequiredLateDataRuleTypeDef = TypedDict(
    "_RequiredLateDataRuleTypeDef", {"ruleConfiguration": "LateDataRuleConfigurationTypeDef"}
)
_OptionalLateDataRuleTypeDef = TypedDict(
    "_OptionalLateDataRuleTypeDef", {"ruleName": str}, total=False
)


class LateDataRuleTypeDef(_RequiredLateDataRuleTypeDef, _OptionalLateDataRuleTypeDef):
    pass


LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef", {"roleArn": str, "level": Literal["ERROR"], "enabled": bool}
)

_RequiredMathActivityTypeDef = TypedDict(
    "_RequiredMathActivityTypeDef", {"name": str, "attribute": str, "math": str}
)
_OptionalMathActivityTypeDef = TypedDict("_OptionalMathActivityTypeDef", {"next": str}, total=False)


class MathActivityTypeDef(_RequiredMathActivityTypeDef, _OptionalMathActivityTypeDef):
    pass


OutputFileUriValueTypeDef = TypedDict("OutputFileUriValueTypeDef", {"fileName": str})

ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef", {"schemaDefinition": "SchemaDefinitionTypeDef"}, total=False
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

QueryFilterTypeDef = TypedDict("QueryFilterTypeDef", {"deltaTime": "DeltaTimeTypeDef"}, total=False)

_RequiredRemoveAttributesActivityTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityTypeDef", {"name": str, "attributes": List[str]}
)
_OptionalRemoveAttributesActivityTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityTypeDef", {"next": str}, total=False
)


class RemoveAttributesActivityTypeDef(
    _RequiredRemoveAttributesActivityTypeDef, _OptionalRemoveAttributesActivityTypeDef
):
    pass


ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)

ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
)

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef", {"unlimited": bool, "numberOfDays": int}, total=False
)

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef", {"bucket": str, "key": str, "roleArn": str}
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {"glueConfiguration": "GlueConfigurationTypeDef"},
    total=False,
)


class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass


ScheduleTypeDef = TypedDict("ScheduleTypeDef", {"expression": str}, total=False)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef", {"columns": List["ColumnTypeDef"]}, total=False
)

_RequiredSelectAttributesActivityTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityTypeDef", {"name": str, "attributes": List[str]}
)
_OptionalSelectAttributesActivityTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityTypeDef", {"next": str}, total=False
)


class SelectAttributesActivityTypeDef(
    _RequiredSelectAttributesActivityTypeDef, _OptionalSelectAttributesActivityTypeDef
):
    pass


_RequiredSqlQueryDatasetActionTypeDef = TypedDict(
    "_RequiredSqlQueryDatasetActionTypeDef", {"sqlQuery": str}
)
_OptionalSqlQueryDatasetActionTypeDef = TypedDict(
    "_OptionalSqlQueryDatasetActionTypeDef", {"filters": List["QueryFilterTypeDef"]}, total=False
)


class SqlQueryDatasetActionTypeDef(
    _RequiredSqlQueryDatasetActionTypeDef, _OptionalSqlQueryDatasetActionTypeDef
):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

TriggeringDatasetTypeDef = TypedDict("TriggeringDatasetTypeDef", {"name": str})

_RequiredVariableTypeDef = TypedDict("_RequiredVariableTypeDef", {"name": str})
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
    "VersioningConfigurationTypeDef", {"unlimited": bool, "maxVersions": int}, total=False
)

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {"batchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"]},
    total=False,
)

ChannelMessagesTypeDef = TypedDict("ChannelMessagesTypeDef", {"s3Paths": List[str]}, total=False)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {"channelName": str, "channelArn": str, "retentionPeriod": "RetentionPeriodTypeDef"},
    total=False,
)

CreateDatasetContentResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseTypeDef", {"versionId": str}, total=False
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {"datasetName": str, "datasetArn": str, "retentionPeriod": "RetentionPeriodTypeDef"},
    total=False,
)

CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {"datastoreName": str, "datastoreArn": str, "retentionPeriod": "RetentionPeriodTypeDef"},
    total=False,
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef", {"pipelineName": str, "pipelineArn": str}, total=False
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {"channel": "ChannelTypeDef", "statistics": "ChannelStatisticsTypeDef"},
    total=False,
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef", {"dataset": "DatasetTypeDef"}, total=False
)

DescribeDatastoreResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseTypeDef",
    {"datastore": "DatastoreTypeDef", "statistics": "DatastoreStatisticsTypeDef"},
    total=False,
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": "LoggingOptionsTypeDef"},
    total=False,
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef", {"pipeline": "PipelineTypeDef"}, total=False
)

GetDatasetContentResponseTypeDef = TypedDict(
    "GetDatasetContentResponseTypeDef",
    {
        "entries": List["DatasetEntryTypeDef"],
        "timestamp": datetime,
        "status": "DatasetContentStatusTypeDef",
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {"channelSummaries": List["ChannelSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {"datasetContentSummaries": List["DatasetContentSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {"datasetSummaries": List["DatasetSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {"datastoreSummaries": List["DatastoreSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {"pipelineSummaries": List["PipelineSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": List["TagTypeDef"]}, total=False
)

MessageTypeDef = TypedDict("MessageTypeDef", {"messageId": str, "payload": Union[bytes, IO[bytes]]})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RunPipelineActivityResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseTypeDef",
    {"payloads": List[Union[bytes, IO[bytes]]], "logResult": str},
    total=False,
)

SampleChannelDataResponseTypeDef = TypedDict(
    "SampleChannelDataResponseTypeDef", {"payloads": List[Union[bytes, IO[bytes]]]}, total=False
)

StartPipelineReprocessingResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseTypeDef", {"reprocessingId": str}, total=False
)
