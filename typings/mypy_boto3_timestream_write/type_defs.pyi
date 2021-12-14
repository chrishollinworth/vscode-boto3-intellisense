"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import CreateDatabaseRequestRequestTypeDef

    data: CreateDatabaseRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import MeasureValueTypeType, S3EncryptionOptionType, TableStatusType, TimeUnitType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateDatabaseRequestRequestTypeDef",
    "CreateDatabaseResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTableResponseTypeDef",
    "DatabaseTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DescribeDatabaseRequestRequestTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "DescribeTableResponseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MagneticStoreRejectedDataLocationTypeDef",
    "MagneticStoreWritePropertiesTypeDef",
    "MeasureValueTypeDef",
    "RecordTypeDef",
    "RecordsIngestedTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPropertiesTypeDef",
    "S3ConfigurationTypeDef",
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
