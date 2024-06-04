"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import BatchLoadProgressReportTypeDef

    data: BatchLoadProgressReportTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BatchLoadStatusType,
    MeasureValueTypeType,
    PartitionKeyEnforcementLevelType,
    PartitionKeyTypeType,
    S3EncryptionOptionType,
    ScalarMeasureValueTypeType,
    TableStatusType,
    TimeUnitType,
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
    "BatchLoadProgressReportTypeDef",
    "BatchLoadTaskDescriptionTypeDef",
    "BatchLoadTaskTypeDef",
    "CreateBatchLoadTaskRequestRequestTypeDef",
    "CreateBatchLoadTaskResponseTypeDef",
    "CreateDatabaseRequestRequestTypeDef",
    "CreateDatabaseResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTableResponseTypeDef",
    "CsvConfigurationTypeDef",
    "DataModelConfigurationTypeDef",
    "DataModelS3ConfigurationTypeDef",
    "DataModelTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceS3ConfigurationTypeDef",
    "DatabaseTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DescribeBatchLoadTaskRequestRequestTypeDef",
    "DescribeBatchLoadTaskResponseTypeDef",
    "DescribeDatabaseRequestRequestTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "DescribeTableResponseTypeDef",
    "DimensionMappingTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListBatchLoadTasksRequestRequestTypeDef",
    "ListBatchLoadTasksResponseTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MagneticStoreRejectedDataLocationTypeDef",
    "MagneticStoreWritePropertiesTypeDef",
    "MeasureValueTypeDef",
    "MixedMeasureMappingTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "MultiMeasureMappingsTypeDef",
    "PartitionKeyTypeDef",
    "RecordTypeDef",
    "RecordsIngestedTypeDef",
    "ReportConfigurationTypeDef",
    "ReportS3ConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeBatchLoadTaskRequestRequestTypeDef",
    "RetentionPropertiesTypeDef",
    "S3ConfigurationTypeDef",
    "SchemaTypeDef",
    "TableTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "UpdateTableResponseTypeDef",
    "WriteRecordsRequestRequestTypeDef",
    "WriteRecordsResponseTypeDef",
)

BatchLoadProgressReportTypeDef = TypedDict(
    "BatchLoadProgressReportTypeDef",
    {
        "RecordsProcessed": int,
        "RecordsIngested": int,
        "ParseFailures": int,
        "RecordIngestionFailures": int,
        "FileFailures": int,
        "BytesMetered": int,
    },
    total=False,
)

BatchLoadTaskDescriptionTypeDef = TypedDict(
    "BatchLoadTaskDescriptionTypeDef",
    {
        "TaskId": str,
        "ErrorMessage": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "ProgressReport": "BatchLoadProgressReportTypeDef",
        "ReportConfiguration": "ReportConfigurationTypeDef",
        "DataModelConfiguration": "DataModelConfigurationTypeDef",
        "TargetDatabaseName": str,
        "TargetTableName": str,
        "TaskStatus": BatchLoadStatusType,
        "RecordVersion": int,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "ResumableUntil": datetime,
    },
    total=False,
)

BatchLoadTaskTypeDef = TypedDict(
    "BatchLoadTaskTypeDef",
    {
        "TaskId": str,
        "TaskStatus": BatchLoadStatusType,
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "ResumableUntil": datetime,
    },
    total=False,
)

_RequiredCreateBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBatchLoadTaskRequestRequestTypeDef",
    {
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "ReportConfiguration": "ReportConfigurationTypeDef",
        "TargetDatabaseName": str,
        "TargetTableName": str,
    },
)
_OptionalCreateBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBatchLoadTaskRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DataModelConfiguration": "DataModelConfigurationTypeDef",
        "RecordVersion": int,
    },
    total=False,
)

class CreateBatchLoadTaskRequestRequestTypeDef(
    _RequiredCreateBatchLoadTaskRequestRequestTypeDef,
    _OptionalCreateBatchLoadTaskRequestRequestTypeDef,
):
    pass

CreateBatchLoadTaskResponseTypeDef = TypedDict(
    "CreateBatchLoadTaskResponseTypeDef",
    {
        "TaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalCreateDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatabaseRequestRequestTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatabaseRequestRequestTypeDef(
    _RequiredCreateDatabaseRequestRequestTypeDef, _OptionalCreateDatabaseRequestRequestTypeDef
):
    pass

CreateDatabaseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalCreateTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTableRequestRequestTypeDef",
    {
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
        "MagneticStoreWriteProperties": "MagneticStoreWritePropertiesTypeDef",
        "Schema": "SchemaTypeDef",
    },
    total=False,
)

class CreateTableRequestRequestTypeDef(
    _RequiredCreateTableRequestRequestTypeDef, _OptionalCreateTableRequestRequestTypeDef
):
    pass

CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvConfigurationTypeDef = TypedDict(
    "CsvConfigurationTypeDef",
    {
        "ColumnSeparator": str,
        "EscapeChar": str,
        "QuoteChar": str,
        "NullValue": str,
        "TrimWhiteSpace": bool,
    },
    total=False,
)

DataModelConfigurationTypeDef = TypedDict(
    "DataModelConfigurationTypeDef",
    {
        "DataModel": "DataModelTypeDef",
        "DataModelS3Configuration": "DataModelS3ConfigurationTypeDef",
    },
    total=False,
)

DataModelS3ConfigurationTypeDef = TypedDict(
    "DataModelS3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
    total=False,
)

_RequiredDataModelTypeDef = TypedDict(
    "_RequiredDataModelTypeDef",
    {
        "DimensionMappings": List["DimensionMappingTypeDef"],
    },
)
_OptionalDataModelTypeDef = TypedDict(
    "_OptionalDataModelTypeDef",
    {
        "TimeColumn": str,
        "TimeUnit": TimeUnitType,
        "MultiMeasureMappings": "MultiMeasureMappingsTypeDef",
        "MixedMeasureMappings": List["MixedMeasureMappingTypeDef"],
        "MeasureNameColumn": str,
    },
    total=False,
)

class DataModelTypeDef(_RequiredDataModelTypeDef, _OptionalDataModelTypeDef):
    pass

_RequiredDataSourceConfigurationTypeDef = TypedDict(
    "_RequiredDataSourceConfigurationTypeDef",
    {
        "DataSourceS3Configuration": "DataSourceS3ConfigurationTypeDef",
        "DataFormat": Literal["CSV"],
    },
)
_OptionalDataSourceConfigurationTypeDef = TypedDict(
    "_OptionalDataSourceConfigurationTypeDef",
    {
        "CsvConfiguration": "CsvConfigurationTypeDef",
    },
    total=False,
)

class DataSourceConfigurationTypeDef(
    _RequiredDataSourceConfigurationTypeDef, _OptionalDataSourceConfigurationTypeDef
):
    pass

_RequiredDataSourceS3ConfigurationTypeDef = TypedDict(
    "_RequiredDataSourceS3ConfigurationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalDataSourceS3ConfigurationTypeDef = TypedDict(
    "_OptionalDataSourceS3ConfigurationTypeDef",
    {
        "ObjectKeyPrefix": str,
    },
    total=False,
)

class DataSourceS3ConfigurationTypeDef(
    _RequiredDataSourceS3ConfigurationTypeDef, _OptionalDataSourceS3ConfigurationTypeDef
):
    pass

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Arn": str,
        "DatabaseName": str,
        "TableCount": int,
        "KmsKeyId": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DeleteDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "DescribeBatchLoadTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)

DescribeBatchLoadTaskResponseTypeDef = TypedDict(
    "DescribeBatchLoadTaskResponseTypeDef",
    {
        "BatchLoadTaskDescription": "BatchLoadTaskDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatabaseRequestRequestTypeDef = TypedDict(
    "DescribeDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DescribeDatabaseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableRequestRequestTypeDef = TypedDict(
    "DescribeTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "SourceColumn": str,
        "DestinationColumn": str,
    },
    total=False,
)

_RequiredDimensionTypeDef = TypedDict(
    "_RequiredDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalDimensionTypeDef = TypedDict(
    "_OptionalDimensionTypeDef",
    {
        "DimensionValueType": Literal["VARCHAR"],
    },
    total=False,
)

class DimensionTypeDef(_RequiredDimensionTypeDef, _OptionalDimensionTypeDef):
    pass

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

ListBatchLoadTasksRequestRequestTypeDef = TypedDict(
    "ListBatchLoadTasksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "TaskStatus": BatchLoadStatusType,
    },
    total=False,
)

ListBatchLoadTasksResponseTypeDef = TypedDict(
    "ListBatchLoadTasksResponseTypeDef",
    {
        "NextToken": str,
        "BatchLoadTasks": List["BatchLoadTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatabasesRequestRequestTypeDef = TypedDict(
    "ListDatabasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "Tables": List["TableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MagneticStoreRejectedDataLocationTypeDef = TypedDict(
    "MagneticStoreRejectedDataLocationTypeDef",
    {
        "S3Configuration": "S3ConfigurationTypeDef",
    },
    total=False,
)

_RequiredMagneticStoreWritePropertiesTypeDef = TypedDict(
    "_RequiredMagneticStoreWritePropertiesTypeDef",
    {
        "EnableMagneticStoreWrites": bool,
    },
)
_OptionalMagneticStoreWritePropertiesTypeDef = TypedDict(
    "_OptionalMagneticStoreWritePropertiesTypeDef",
    {
        "MagneticStoreRejectedDataLocation": "MagneticStoreRejectedDataLocationTypeDef",
    },
    total=False,
)

class MagneticStoreWritePropertiesTypeDef(
    _RequiredMagneticStoreWritePropertiesTypeDef, _OptionalMagneticStoreWritePropertiesTypeDef
):
    pass

MeasureValueTypeDef = TypedDict(
    "MeasureValueTypeDef",
    {
        "Name": str,
        "Value": str,
        "Type": MeasureValueTypeType,
    },
)

_RequiredMixedMeasureMappingTypeDef = TypedDict(
    "_RequiredMixedMeasureMappingTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
    },
)
_OptionalMixedMeasureMappingTypeDef = TypedDict(
    "_OptionalMixedMeasureMappingTypeDef",
    {
        "MeasureName": str,
        "SourceColumn": str,
        "TargetMeasureName": str,
        "MultiMeasureAttributeMappings": List["MultiMeasureAttributeMappingTypeDef"],
    },
    total=False,
)

class MixedMeasureMappingTypeDef(
    _RequiredMixedMeasureMappingTypeDef, _OptionalMixedMeasureMappingTypeDef
):
    pass

_RequiredMultiMeasureAttributeMappingTypeDef = TypedDict(
    "_RequiredMultiMeasureAttributeMappingTypeDef",
    {
        "SourceColumn": str,
    },
)
_OptionalMultiMeasureAttributeMappingTypeDef = TypedDict(
    "_OptionalMultiMeasureAttributeMappingTypeDef",
    {
        "TargetMultiMeasureAttributeName": str,
        "MeasureValueType": ScalarMeasureValueTypeType,
    },
    total=False,
)

class MultiMeasureAttributeMappingTypeDef(
    _RequiredMultiMeasureAttributeMappingTypeDef, _OptionalMultiMeasureAttributeMappingTypeDef
):
    pass

_RequiredMultiMeasureMappingsTypeDef = TypedDict(
    "_RequiredMultiMeasureMappingsTypeDef",
    {
        "MultiMeasureAttributeMappings": List["MultiMeasureAttributeMappingTypeDef"],
    },
)
_OptionalMultiMeasureMappingsTypeDef = TypedDict(
    "_OptionalMultiMeasureMappingsTypeDef",
    {
        "TargetMultiMeasureName": str,
    },
    total=False,
)

class MultiMeasureMappingsTypeDef(
    _RequiredMultiMeasureMappingsTypeDef, _OptionalMultiMeasureMappingsTypeDef
):
    pass

_RequiredPartitionKeyTypeDef = TypedDict(
    "_RequiredPartitionKeyTypeDef",
    {
        "Type": PartitionKeyTypeType,
    },
)
_OptionalPartitionKeyTypeDef = TypedDict(
    "_OptionalPartitionKeyTypeDef",
    {
        "Name": str,
        "EnforcementInRecord": PartitionKeyEnforcementLevelType,
    },
    total=False,
)

class PartitionKeyTypeDef(_RequiredPartitionKeyTypeDef, _OptionalPartitionKeyTypeDef):
    pass

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "MeasureName": str,
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "Time": str,
        "TimeUnit": TimeUnitType,
        "Version": int,
        "MeasureValues": List["MeasureValueTypeDef"],
    },
    total=False,
)

RecordsIngestedTypeDef = TypedDict(
    "RecordsIngestedTypeDef",
    {
        "Total": int,
        "MemoryStore": int,
        "MagneticStore": int,
    },
    total=False,
)

ReportConfigurationTypeDef = TypedDict(
    "ReportConfigurationTypeDef",
    {
        "ReportS3Configuration": "ReportS3ConfigurationTypeDef",
    },
    total=False,
)

_RequiredReportS3ConfigurationTypeDef = TypedDict(
    "_RequiredReportS3ConfigurationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalReportS3ConfigurationTypeDef = TypedDict(
    "_OptionalReportS3ConfigurationTypeDef",
    {
        "ObjectKeyPrefix": str,
        "EncryptionOption": S3EncryptionOptionType,
        "KmsKeyId": str,
    },
    total=False,
)

class ReportS3ConfigurationTypeDef(
    _RequiredReportS3ConfigurationTypeDef, _OptionalReportS3ConfigurationTypeDef
):
    pass

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

ResumeBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "ResumeBatchLoadTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)

RetentionPropertiesTypeDef = TypedDict(
    "RetentionPropertiesTypeDef",
    {
        "MemoryStoreRetentionPeriodInHours": int,
        "MagneticStoreRetentionPeriodInDays": int,
    },
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKeyPrefix": str,
        "EncryptionOption": S3EncryptionOptionType,
        "KmsKeyId": str,
    },
    total=False,
)

SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "CompositePartitionKey": List["PartitionKeyTypeDef"],
    },
    total=False,
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Arn": str,
        "TableName": str,
        "DatabaseName": str,
        "TableStatus": TableStatusType,
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "MagneticStoreWriteProperties": "MagneticStoreWritePropertiesTypeDef",
        "Schema": "SchemaTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
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
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": str,
    },
)

UpdateDatabaseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalUpdateTableRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTableRequestRequestTypeDef",
    {
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "MagneticStoreWriteProperties": "MagneticStoreWritePropertiesTypeDef",
        "Schema": "SchemaTypeDef",
    },
    total=False,
)

class UpdateTableRequestRequestTypeDef(
    _RequiredUpdateTableRequestRequestTypeDef, _OptionalUpdateTableRequestRequestTypeDef
):
    pass

UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWriteRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredWriteRecordsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Records": List["RecordTypeDef"],
    },
)
_OptionalWriteRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalWriteRecordsRequestRequestTypeDef",
    {
        "CommonAttributes": "RecordTypeDef",
    },
    total=False,
)

class WriteRecordsRequestRequestTypeDef(
    _RequiredWriteRecordsRequestRequestTypeDef, _OptionalWriteRecordsRequestRequestTypeDef
):
    pass

WriteRecordsResponseTypeDef = TypedDict(
    "WriteRecordsResponseTypeDef",
    {
        "RecordsIngested": "RecordsIngestedTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
