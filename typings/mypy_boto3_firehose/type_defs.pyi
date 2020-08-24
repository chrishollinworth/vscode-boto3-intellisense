"""
Main interface for firehose service type definitions.

Usage::

    ```python
    from mypy_boto3_firehose.type_defs import BufferingHintsTypeDef

    data: BufferingHintsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BufferingHintsTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "CopyCommandTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DeserializerTypeDef",
    "DestinationDescriptionTypeDef",
    "ElasticsearchBufferingHintsTypeDef",
    "ElasticsearchDestinationDescriptionTypeDef",
    "ElasticsearchRetryOptionsTypeDef",
    "EncryptionConfigurationTypeDef",
    "ExtendedS3DestinationDescriptionTypeDef",
    "FailureDescriptionTypeDef",
    "HiveJsonSerDeTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "InputFormatConfigurationTypeDef",
    "KMSEncryptionConfigTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "OpenXJsonSerDeTypeDef",
    "OrcSerDeTypeDef",
    "OutputFormatConfigurationTypeDef",
    "ParquetSerDeTypeDef",
    "ProcessingConfigurationTypeDef",
    "ProcessorParameterTypeDef",
    "ProcessorTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "RedshiftDestinationDescriptionTypeDef",
    "RedshiftRetryOptionsTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationDescriptionTypeDef",
    "S3DestinationUpdateTypeDef",
    "SchemaConfigurationTypeDef",
    "SerializerTypeDef",
    "SourceDescriptionTypeDef",
    "SplunkDestinationDescriptionTypeDef",
    "SplunkRetryOptionsTypeDef",
    "TagTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
    "ElasticsearchDestinationConfigurationTypeDef",
    "ElasticsearchDestinationUpdateTypeDef",
    "ExtendedS3DestinationConfigurationTypeDef",
    "ExtendedS3DestinationUpdateTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "PutRecordBatchOutputTypeDef",
    "PutRecordOutputTypeDef",
    "RecordTypeDef",
    "RedshiftDestinationConfigurationTypeDef",
    "RedshiftDestinationUpdateTypeDef",
    "SplunkDestinationConfigurationTypeDef",
    "SplunkDestinationUpdateTypeDef",
)

BufferingHintsTypeDef = TypedDict(
    "BufferingHintsTypeDef", {"SizeInMBs": int, "IntervalInSeconds": int}, total=False
)

CloudWatchLoggingOptionsTypeDef = TypedDict(
    "CloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

_RequiredCopyCommandTypeDef = TypedDict("_RequiredCopyCommandTypeDef", {"DataTableName": str})
_OptionalCopyCommandTypeDef = TypedDict(
    "_OptionalCopyCommandTypeDef", {"DataTableColumns": str, "CopyOptions": str}, total=False
)


class CopyCommandTypeDef(_RequiredCopyCommandTypeDef, _OptionalCopyCommandTypeDef):
    pass


DataFormatConversionConfigurationTypeDef = TypedDict(
    "DataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": "SchemaConfigurationTypeDef",
        "InputFormatConfiguration": "InputFormatConfigurationTypeDef",
        "OutputFormatConfiguration": "OutputFormatConfigurationTypeDef",
        "Enabled": bool,
    },
    total=False,
)

_RequiredDeliveryStreamDescriptionTypeDef = TypedDict(
    "_RequiredDeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": Literal[
            "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED", "ACTIVE"
        ],
        "DeliveryStreamType": Literal["DirectPut", "KinesisStreamAsSource"],
        "VersionId": str,
        "Destinations": List["DestinationDescriptionTypeDef"],
        "HasMoreDestinations": bool,
    },
)
_OptionalDeliveryStreamDescriptionTypeDef = TypedDict(
    "_OptionalDeliveryStreamDescriptionTypeDef",
    {
        "FailureDescription": "FailureDescriptionTypeDef",
        "DeliveryStreamEncryptionConfiguration": "DeliveryStreamEncryptionConfigurationTypeDef",
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Source": "SourceDescriptionTypeDef",
    },
    total=False,
)


class DeliveryStreamDescriptionTypeDef(
    _RequiredDeliveryStreamDescriptionTypeDef, _OptionalDeliveryStreamDescriptionTypeDef
):
    pass


DeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "DeliveryStreamEncryptionConfigurationTypeDef",
    {
        "KeyARN": str,
        "KeyType": Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"],
        "Status": Literal[
            "ENABLED", "ENABLING", "ENABLING_FAILED", "DISABLED", "DISABLING", "DISABLING_FAILED"
        ],
        "FailureDescription": "FailureDescriptionTypeDef",
    },
    total=False,
)

DeserializerTypeDef = TypedDict(
    "DeserializerTypeDef",
    {"OpenXJsonSerDe": "OpenXJsonSerDeTypeDef", "HiveJsonSerDe": "HiveJsonSerDeTypeDef"},
    total=False,
)

_RequiredDestinationDescriptionTypeDef = TypedDict(
    "_RequiredDestinationDescriptionTypeDef", {"DestinationId": str}
)
_OptionalDestinationDescriptionTypeDef = TypedDict(
    "_OptionalDestinationDescriptionTypeDef",
    {
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ExtendedS3DestinationDescription": "ExtendedS3DestinationDescriptionTypeDef",
        "RedshiftDestinationDescription": "RedshiftDestinationDescriptionTypeDef",
        "ElasticsearchDestinationDescription": "ElasticsearchDestinationDescriptionTypeDef",
        "SplunkDestinationDescription": "SplunkDestinationDescriptionTypeDef",
        "HttpEndpointDestinationDescription": "HttpEndpointDestinationDescriptionTypeDef",
    },
    total=False,
)


class DestinationDescriptionTypeDef(
    _RequiredDestinationDescriptionTypeDef, _OptionalDestinationDescriptionTypeDef
):
    pass


ElasticsearchBufferingHintsTypeDef = TypedDict(
    "ElasticsearchBufferingHintsTypeDef", {"IntervalInSeconds": int, "SizeInMBs": int}, total=False
)

ElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "ElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedDocumentsOnly", "AllDocuments"],
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
    },
    total=False,
)

ElasticsearchRetryOptionsTypeDef = TypedDict(
    "ElasticsearchRetryOptionsTypeDef", {"DurationInSeconds": int}, total=False
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": Literal["NoEncryption"],
        "KMSEncryptionConfig": "KMSEncryptionConfigTypeDef",
    },
    total=False,
)

_RequiredExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)
_OptionalExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_OptionalExtendedS3DestinationDescriptionTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupDescription": "S3DestinationDescriptionTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
    },
    total=False,
)


class ExtendedS3DestinationDescriptionTypeDef(
    _RequiredExtendedS3DestinationDescriptionTypeDef,
    _OptionalExtendedS3DestinationDescriptionTypeDef,
):
    pass


FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef",
    {
        "Type": Literal[
            "RETIRE_KMS_GRANT_FAILED",
            "CREATE_KMS_GRANT_FAILED",
            "KMS_ACCESS_DENIED",
            "DISABLED_KMS_KEY",
            "INVALID_KMS_KEY",
            "KMS_KEY_NOT_FOUND",
            "KMS_OPT_IN_REQUIRED",
            "CREATE_ENI_FAILED",
            "DELETE_ENI_FAILED",
            "SUBNET_NOT_FOUND",
            "SECURITY_GROUP_NOT_FOUND",
            "ENI_ACCESS_DENIED",
            "SUBNET_ACCESS_DENIED",
            "SECURITY_GROUP_ACCESS_DENIED",
            "UNKNOWN_ERROR",
        ],
        "Details": str,
    },
)

HiveJsonSerDeTypeDef = TypedDict(
    "HiveJsonSerDeTypeDef", {"TimestampFormats": List[str]}, total=False
)

HttpEndpointBufferingHintsTypeDef = TypedDict(
    "HttpEndpointBufferingHintsTypeDef", {"SizeInMBs": int, "IntervalInSeconds": int}, total=False
)

HttpEndpointCommonAttributeTypeDef = TypedDict(
    "HttpEndpointCommonAttributeTypeDef", {"AttributeName": str, "AttributeValue": str}
)

_RequiredHttpEndpointConfigurationTypeDef = TypedDict(
    "_RequiredHttpEndpointConfigurationTypeDef", {"Url": str}
)
_OptionalHttpEndpointConfigurationTypeDef = TypedDict(
    "_OptionalHttpEndpointConfigurationTypeDef", {"Name": str, "AccessKey": str}, total=False
)


class HttpEndpointConfigurationTypeDef(
    _RequiredHttpEndpointConfigurationTypeDef, _OptionalHttpEndpointConfigurationTypeDef
):
    pass


HttpEndpointDescriptionTypeDef = TypedDict(
    "HttpEndpointDescriptionTypeDef", {"Url": str, "Name": str}, total=False
)

HttpEndpointDestinationDescriptionTypeDef = TypedDict(
    "HttpEndpointDestinationDescriptionTypeDef",
    {
        "EndpointConfiguration": "HttpEndpointDescriptionTypeDef",
        "BufferingHints": "HttpEndpointBufferingHintsTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "RequestConfiguration": "HttpEndpointRequestConfigurationTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RoleARN": str,
        "RetryOptions": "HttpEndpointRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedDataOnly", "AllData"],
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
    },
    total=False,
)

HttpEndpointRequestConfigurationTypeDef = TypedDict(
    "HttpEndpointRequestConfigurationTypeDef",
    {
        "ContentEncoding": Literal["NONE", "GZIP"],
        "CommonAttributes": List["HttpEndpointCommonAttributeTypeDef"],
    },
    total=False,
)

HttpEndpointRetryOptionsTypeDef = TypedDict(
    "HttpEndpointRetryOptionsTypeDef", {"DurationInSeconds": int}, total=False
)

InputFormatConfigurationTypeDef = TypedDict(
    "InputFormatConfigurationTypeDef", {"Deserializer": "DeserializerTypeDef"}, total=False
)

KMSEncryptionConfigTypeDef = TypedDict("KMSEncryptionConfigTypeDef", {"AWSKMSKeyARN": str})

KinesisStreamSourceDescriptionTypeDef = TypedDict(
    "KinesisStreamSourceDescriptionTypeDef",
    {"KinesisStreamARN": str, "RoleARN": str, "DeliveryStartTimestamp": datetime},
    total=False,
)

OpenXJsonSerDeTypeDef = TypedDict(
    "OpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)

OrcSerDeTypeDef = TypedDict(
    "OrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": Literal["NONE", "ZLIB", "SNAPPY"],
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": Literal["V0_11", "V0_12"],
    },
    total=False,
)

OutputFormatConfigurationTypeDef = TypedDict(
    "OutputFormatConfigurationTypeDef", {"Serializer": "SerializerTypeDef"}, total=False
)

ParquetSerDeTypeDef = TypedDict(
    "ParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": Literal["UNCOMPRESSED", "GZIP", "SNAPPY"],
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": Literal["V1", "V2"],
    },
    total=False,
)

ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {"Enabled": bool, "Processors": List["ProcessorTypeDef"]},
    total=False,
)

ProcessorParameterTypeDef = TypedDict(
    "ProcessorParameterTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
)

_RequiredProcessorTypeDef = TypedDict("_RequiredProcessorTypeDef", {"Type": Literal["Lambda"]})
_OptionalProcessorTypeDef = TypedDict(
    "_OptionalProcessorTypeDef", {"Parameters": List["ProcessorParameterTypeDef"]}, total=False
)


class ProcessorTypeDef(_RequiredProcessorTypeDef, _OptionalProcessorTypeDef):
    pass


PutRecordBatchResponseEntryTypeDef = TypedDict(
    "PutRecordBatchResponseEntryTypeDef",
    {"RecordId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_RequiredRedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "Username": str,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
    },
)
_OptionalRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_OptionalRedshiftDestinationDescriptionTypeDef",
    {
        "RetryOptions": "RedshiftRetryOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupDescription": "S3DestinationDescriptionTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)


class RedshiftDestinationDescriptionTypeDef(
    _RequiredRedshiftDestinationDescriptionTypeDef, _OptionalRedshiftDestinationDescriptionTypeDef
):
    pass


RedshiftRetryOptionsTypeDef = TypedDict(
    "RedshiftRetryOptionsTypeDef", {"DurationInSeconds": int}, total=False
)

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef", {"RoleARN": str, "BucketARN": str}
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)


class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass


_RequiredS3DestinationDescriptionTypeDef = TypedDict(
    "_RequiredS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)
_OptionalS3DestinationDescriptionTypeDef = TypedDict(
    "_OptionalS3DestinationDescriptionTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)


class S3DestinationDescriptionTypeDef(
    _RequiredS3DestinationDescriptionTypeDef, _OptionalS3DestinationDescriptionTypeDef
):
    pass


S3DestinationUpdateTypeDef = TypedDict(
    "S3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)

SchemaConfigurationTypeDef = TypedDict(
    "SchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

SerializerTypeDef = TypedDict(
    "SerializerTypeDef",
    {"ParquetSerDe": "ParquetSerDeTypeDef", "OrcSerDe": "OrcSerDeTypeDef"},
    total=False,
)

SourceDescriptionTypeDef = TypedDict(
    "SourceDescriptionTypeDef",
    {"KinesisStreamSourceDescription": "KinesisStreamSourceDescriptionTypeDef"},
    total=False,
)

SplunkDestinationDescriptionTypeDef = TypedDict(
    "SplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)

SplunkRetryOptionsTypeDef = TypedDict(
    "SplunkRetryOptionsTypeDef", {"DurationInSeconds": int}, total=False
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {"SubnetIds": List[str], "RoleARN": str, "SecurityGroupIds": List[str], "VpcId": str},
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {"SubnetIds": List[str], "RoleARN": str, "SecurityGroupIds": List[str]},
)

CreateDeliveryStreamOutputTypeDef = TypedDict(
    "CreateDeliveryStreamOutputTypeDef", {"DeliveryStreamARN": str}, total=False
)

_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef",
    {"KeyType": Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]},
)
_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef", {"KeyARN": str}, total=False
)


class DeliveryStreamEncryptionConfigurationInputTypeDef(
    _RequiredDeliveryStreamEncryptionConfigurationInputTypeDef,
    _OptionalDeliveryStreamEncryptionConfigurationInputTypeDef,
):
    pass


DescribeDeliveryStreamOutputTypeDef = TypedDict(
    "DescribeDeliveryStreamOutputTypeDef",
    {"DeliveryStreamDescription": "DeliveryStreamDescriptionTypeDef"},
)

_RequiredElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_RequiredElasticsearchDestinationConfigurationTypeDef",
    {"RoleARN": str, "IndexName": str, "S3Configuration": "S3DestinationConfigurationTypeDef"},
)
_OptionalElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_OptionalElasticsearchDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedDocumentsOnly", "AllDocuments"],
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)


class ElasticsearchDestinationConfigurationTypeDef(
    _RequiredElasticsearchDestinationConfigurationTypeDef,
    _OptionalElasticsearchDestinationConfigurationTypeDef,
):
    pass


ElasticsearchDestinationUpdateTypeDef = TypedDict(
    "ElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)

_RequiredExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationConfigurationTypeDef", {"RoleARN": str, "BucketARN": str}
)
_OptionalExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalExtendedS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupConfiguration": "S3DestinationConfigurationTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
    },
    total=False,
)


class ExtendedS3DestinationConfigurationTypeDef(
    _RequiredExtendedS3DestinationConfigurationTypeDef,
    _OptionalExtendedS3DestinationConfigurationTypeDef,
):
    pass


ExtendedS3DestinationUpdateTypeDef = TypedDict(
    "ExtendedS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy", "HADOOP_SNAPPY"],
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupUpdate": "S3DestinationUpdateTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
    },
    total=False,
)

_RequiredHttpEndpointDestinationConfigurationTypeDef = TypedDict(
    "_RequiredHttpEndpointDestinationConfigurationTypeDef",
    {
        "EndpointConfiguration": "HttpEndpointConfigurationTypeDef",
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalHttpEndpointDestinationConfigurationTypeDef = TypedDict(
    "_OptionalHttpEndpointDestinationConfigurationTypeDef",
    {
        "BufferingHints": "HttpEndpointBufferingHintsTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "RequestConfiguration": "HttpEndpointRequestConfigurationTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RoleARN": str,
        "RetryOptions": "HttpEndpointRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedDataOnly", "AllData"],
    },
    total=False,
)


class HttpEndpointDestinationConfigurationTypeDef(
    _RequiredHttpEndpointDestinationConfigurationTypeDef,
    _OptionalHttpEndpointDestinationConfigurationTypeDef,
):
    pass


HttpEndpointDestinationUpdateTypeDef = TypedDict(
    "HttpEndpointDestinationUpdateTypeDef",
    {
        "EndpointConfiguration": "HttpEndpointConfigurationTypeDef",
        "BufferingHints": "HttpEndpointBufferingHintsTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "RequestConfiguration": "HttpEndpointRequestConfigurationTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RoleARN": str,
        "RetryOptions": "HttpEndpointRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedDataOnly", "AllData"],
        "S3Update": "S3DestinationUpdateTypeDef",
    },
    total=False,
)

KinesisStreamSourceConfigurationTypeDef = TypedDict(
    "KinesisStreamSourceConfigurationTypeDef", {"KinesisStreamARN": str, "RoleARN": str}
)

ListDeliveryStreamsOutputTypeDef = TypedDict(
    "ListDeliveryStreamsOutputTypeDef",
    {"DeliveryStreamNames": List[str], "HasMoreDeliveryStreams": bool},
)

ListTagsForDeliveryStreamOutputTypeDef = TypedDict(
    "ListTagsForDeliveryStreamOutputTypeDef", {"Tags": List["TagTypeDef"], "HasMoreTags": bool}
)

_RequiredPutRecordBatchOutputTypeDef = TypedDict(
    "_RequiredPutRecordBatchOutputTypeDef",
    {"FailedPutCount": int, "RequestResponses": List["PutRecordBatchResponseEntryTypeDef"]},
)
_OptionalPutRecordBatchOutputTypeDef = TypedDict(
    "_OptionalPutRecordBatchOutputTypeDef", {"Encrypted": bool}, total=False
)


class PutRecordBatchOutputTypeDef(
    _RequiredPutRecordBatchOutputTypeDef, _OptionalPutRecordBatchOutputTypeDef
):
    pass


_RequiredPutRecordOutputTypeDef = TypedDict("_RequiredPutRecordOutputTypeDef", {"RecordId": str})
_OptionalPutRecordOutputTypeDef = TypedDict(
    "_OptionalPutRecordOutputTypeDef", {"Encrypted": bool}, total=False
)


class PutRecordOutputTypeDef(_RequiredPutRecordOutputTypeDef, _OptionalPutRecordOutputTypeDef):
    pass


RecordTypeDef = TypedDict("RecordTypeDef", {"Data": bytes})

_RequiredRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_RequiredRedshiftDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "Username": str,
        "Password": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_OptionalRedshiftDestinationConfigurationTypeDef",
    {
        "RetryOptions": "RedshiftRetryOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupConfiguration": "S3DestinationConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)


class RedshiftDestinationConfigurationTypeDef(
    _RequiredRedshiftDestinationConfigurationTypeDef,
    _OptionalRedshiftDestinationConfigurationTypeDef,
):
    pass


RedshiftDestinationUpdateTypeDef = TypedDict(
    "RedshiftDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "Username": str,
        "Password": str,
        "RetryOptions": "RedshiftRetryOptionsTypeDef",
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupUpdate": "S3DestinationUpdateTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)

_RequiredSplunkDestinationConfigurationTypeDef = TypedDict(
    "_RequiredSplunkDestinationConfigurationTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalSplunkDestinationConfigurationTypeDef = TypedDict(
    "_OptionalSplunkDestinationConfigurationTypeDef",
    {
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)


class SplunkDestinationConfigurationTypeDef(
    _RequiredSplunkDestinationConfigurationTypeDef, _OptionalSplunkDestinationConfigurationTypeDef
):
    pass


SplunkDestinationUpdateTypeDef = TypedDict(
    "SplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)
