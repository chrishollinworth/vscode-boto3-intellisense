"""
Type annotations for firehose service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/type_defs.html)

Usage::

    ```python
    from mypy_boto3_firehose.type_defs import AmazonOpenSearchServerlessBufferingHintsTypeDef

    data: AmazonOpenSearchServerlessBufferingHintsTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AmazonOpenSearchServerlessS3BackupModeType,
    AmazonopensearchserviceIndexRotationPeriodType,
    AmazonopensearchserviceS3BackupModeType,
    CompressionFormatType,
    ConnectivityType,
    ContentEncodingType,
    DefaultDocumentIdFormatType,
    DeliveryStreamEncryptionStatusType,
    DeliveryStreamFailureTypeType,
    DeliveryStreamStatusType,
    DeliveryStreamTypeType,
    ElasticsearchIndexRotationPeriodType,
    ElasticsearchS3BackupModeType,
    HECEndpointTypeType,
    HttpEndpointS3BackupModeType,
    KeyTypeType,
    OrcCompressionType,
    OrcFormatVersionType,
    ParquetCompressionType,
    ParquetWriterVersionType,
    ProcessorParameterNameType,
    ProcessorTypeType,
    RedshiftS3BackupModeType,
    S3BackupModeType,
    SnowflakeDataLoadingOptionType,
    SnowflakeS3BackupModeType,
    SplunkS3BackupModeType,
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
    "AmazonOpenSearchServerlessBufferingHintsTypeDef",
    "AmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    "AmazonOpenSearchServerlessDestinationDescriptionTypeDef",
    "AmazonOpenSearchServerlessDestinationUpdateTypeDef",
    "AmazonOpenSearchServerlessRetryOptionsTypeDef",
    "AmazonopensearchserviceBufferingHintsTypeDef",
    "AmazonopensearchserviceDestinationConfigurationTypeDef",
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    "AmazonopensearchserviceRetryOptionsTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BufferingHintsTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "CopyCommandTypeDef",
    "CreateDeliveryStreamInputRequestTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "DeleteDeliveryStreamInputRequestTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DescribeDeliveryStreamInputRequestTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
    "DeserializerTypeDef",
    "DestinationDescriptionTypeDef",
    "DocumentIdOptionsTypeDef",
    "DynamicPartitioningConfigurationTypeDef",
    "ElasticsearchBufferingHintsTypeDef",
    "ElasticsearchDestinationConfigurationTypeDef",
    "ElasticsearchDestinationDescriptionTypeDef",
    "ElasticsearchDestinationUpdateTypeDef",
    "ElasticsearchRetryOptionsTypeDef",
    "EncryptionConfigurationTypeDef",
    "ExtendedS3DestinationConfigurationTypeDef",
    "ExtendedS3DestinationDescriptionTypeDef",
    "ExtendedS3DestinationUpdateTypeDef",
    "FailureDescriptionTypeDef",
    "HiveJsonSerDeTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "InputFormatConfigurationTypeDef",
    "KMSEncryptionConfigTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "ListDeliveryStreamsInputRequestTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamInputRequestTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "MSKSourceConfigurationTypeDef",
    "MSKSourceDescriptionTypeDef",
    "OpenXJsonSerDeTypeDef",
    "OrcSerDeTypeDef",
    "OutputFormatConfigurationTypeDef",
    "ParquetSerDeTypeDef",
    "ProcessingConfigurationTypeDef",
    "ProcessorParameterTypeDef",
    "ProcessorTypeDef",
    "PutRecordBatchInputRequestTypeDef",
    "PutRecordBatchOutputTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordOutputTypeDef",
    "RecordTypeDef",
    "RedshiftDestinationConfigurationTypeDef",
    "RedshiftDestinationDescriptionTypeDef",
    "RedshiftDestinationUpdateTypeDef",
    "RedshiftRetryOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "RetryOptionsTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationDescriptionTypeDef",
    "S3DestinationUpdateTypeDef",
    "SchemaConfigurationTypeDef",
    "SecretsManagerConfigurationTypeDef",
    "SerializerTypeDef",
    "SnowflakeDestinationConfigurationTypeDef",
    "SnowflakeDestinationDescriptionTypeDef",
    "SnowflakeDestinationUpdateTypeDef",
    "SnowflakeRetryOptionsTypeDef",
    "SnowflakeRoleConfigurationTypeDef",
    "SnowflakeVpcConfigurationTypeDef",
    "SourceDescriptionTypeDef",
    "SplunkBufferingHintsTypeDef",
    "SplunkDestinationConfigurationTypeDef",
    "SplunkDestinationDescriptionTypeDef",
    "SplunkDestinationUpdateTypeDef",
    "SplunkRetryOptionsTypeDef",
    "StartDeliveryStreamEncryptionInputRequestTypeDef",
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    "TagDeliveryStreamInputRequestTypeDef",
    "TagTypeDef",
    "UntagDeliveryStreamInputRequestTypeDef",
    "UpdateDestinationInputRequestTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
)

AmazonOpenSearchServerlessBufferingHintsTypeDef = TypedDict(
    "AmazonOpenSearchServerlessBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

_RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef = TypedDict(
    "_RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef = TypedDict(
    "_OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef",
    {
        "CollectionEndpoint": str,
        "BufferingHints": "AmazonOpenSearchServerlessBufferingHintsTypeDef",
        "RetryOptions": "AmazonOpenSearchServerlessRetryOptionsTypeDef",
        "S3BackupMode": AmazonOpenSearchServerlessS3BackupModeType,
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)

class AmazonOpenSearchServerlessDestinationConfigurationTypeDef(
    _RequiredAmazonOpenSearchServerlessDestinationConfigurationTypeDef,
    _OptionalAmazonOpenSearchServerlessDestinationConfigurationTypeDef,
):
    pass

AmazonOpenSearchServerlessDestinationDescriptionTypeDef = TypedDict(
    "AmazonOpenSearchServerlessDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "CollectionEndpoint": str,
        "IndexName": str,
        "BufferingHints": "AmazonOpenSearchServerlessBufferingHintsTypeDef",
        "RetryOptions": "AmazonOpenSearchServerlessRetryOptionsTypeDef",
        "S3BackupMode": AmazonOpenSearchServerlessS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
    },
    total=False,
)

AmazonOpenSearchServerlessDestinationUpdateTypeDef = TypedDict(
    "AmazonOpenSearchServerlessDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "CollectionEndpoint": str,
        "IndexName": str,
        "BufferingHints": "AmazonOpenSearchServerlessBufferingHintsTypeDef",
        "RetryOptions": "AmazonOpenSearchServerlessRetryOptionsTypeDef",
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
    },
    total=False,
)

AmazonOpenSearchServerlessRetryOptionsTypeDef = TypedDict(
    "AmazonOpenSearchServerlessRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

AmazonopensearchserviceBufferingHintsTypeDef = TypedDict(
    "AmazonopensearchserviceBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

_RequiredAmazonopensearchserviceDestinationConfigurationTypeDef = TypedDict(
    "_RequiredAmazonopensearchserviceDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalAmazonopensearchserviceDestinationConfigurationTypeDef = TypedDict(
    "_OptionalAmazonopensearchserviceDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": "AmazonopensearchserviceBufferingHintsTypeDef",
        "RetryOptions": "AmazonopensearchserviceRetryOptionsTypeDef",
        "S3BackupMode": AmazonopensearchserviceS3BackupModeType,
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

class AmazonopensearchserviceDestinationConfigurationTypeDef(
    _RequiredAmazonopensearchserviceDestinationConfigurationTypeDef,
    _OptionalAmazonopensearchserviceDestinationConfigurationTypeDef,
):
    pass

AmazonopensearchserviceDestinationDescriptionTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": "AmazonopensearchserviceBufferingHintsTypeDef",
        "RetryOptions": "AmazonopensearchserviceRetryOptionsTypeDef",
        "S3BackupMode": AmazonopensearchserviceS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

AmazonopensearchserviceDestinationUpdateTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": AmazonopensearchserviceIndexRotationPeriodType,
        "BufferingHints": "AmazonopensearchserviceBufferingHintsTypeDef",
        "RetryOptions": "AmazonopensearchserviceRetryOptionsTypeDef",
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

AmazonopensearchserviceRetryOptionsTypeDef = TypedDict(
    "AmazonopensearchserviceRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "RoleARN": str,
        "Connectivity": ConnectivityType,
    },
)

BufferingHintsTypeDef = TypedDict(
    "BufferingHintsTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

CloudWatchLoggingOptionsTypeDef = TypedDict(
    "CloudWatchLoggingOptionsTypeDef",
    {
        "Enabled": bool,
        "LogGroupName": str,
        "LogStreamName": str,
    },
    total=False,
)

_RequiredCopyCommandTypeDef = TypedDict(
    "_RequiredCopyCommandTypeDef",
    {
        "DataTableName": str,
    },
)
_OptionalCopyCommandTypeDef = TypedDict(
    "_OptionalCopyCommandTypeDef",
    {
        "DataTableColumns": str,
        "CopyOptions": str,
    },
    total=False,
)

class CopyCommandTypeDef(_RequiredCopyCommandTypeDef, _OptionalCopyCommandTypeDef):
    pass

_RequiredCreateDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalCreateDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamType": DeliveryStreamTypeType,
        "KinesisStreamSourceConfiguration": "KinesisStreamSourceConfigurationTypeDef",
        "DeliveryStreamEncryptionConfigurationInput": "DeliveryStreamEncryptionConfigurationInputTypeDef",
        "S3DestinationConfiguration": "S3DestinationConfigurationTypeDef",
        "ExtendedS3DestinationConfiguration": "ExtendedS3DestinationConfigurationTypeDef",
        "RedshiftDestinationConfiguration": "RedshiftDestinationConfigurationTypeDef",
        "ElasticsearchDestinationConfiguration": "ElasticsearchDestinationConfigurationTypeDef",
        "AmazonopensearchserviceDestinationConfiguration": "AmazonopensearchserviceDestinationConfigurationTypeDef",
        "SplunkDestinationConfiguration": "SplunkDestinationConfigurationTypeDef",
        "HttpEndpointDestinationConfiguration": "HttpEndpointDestinationConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "AmazonOpenSearchServerlessDestinationConfiguration": "AmazonOpenSearchServerlessDestinationConfigurationTypeDef",
        "MSKSourceConfiguration": "MSKSourceConfigurationTypeDef",
        "SnowflakeDestinationConfiguration": "SnowflakeDestinationConfigurationTypeDef",
    },
    total=False,
)

class CreateDeliveryStreamInputRequestTypeDef(
    _RequiredCreateDeliveryStreamInputRequestTypeDef,
    _OptionalCreateDeliveryStreamInputRequestTypeDef,
):
    pass

CreateDeliveryStreamOutputTypeDef = TypedDict(
    "CreateDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredDeleteDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalDeleteDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteDeliveryStreamInputRequestTypeDef",
    {
        "AllowForceDelete": bool,
    },
    total=False,
)

class DeleteDeliveryStreamInputRequestTypeDef(
    _RequiredDeleteDeliveryStreamInputRequestTypeDef,
    _OptionalDeleteDeliveryStreamInputRequestTypeDef,
):
    pass

_RequiredDeliveryStreamDescriptionTypeDef = TypedDict(
    "_RequiredDeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": DeliveryStreamStatusType,
        "DeliveryStreamType": DeliveryStreamTypeType,
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

_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_RequiredDeliveryStreamEncryptionConfigurationInputTypeDef",
    {
        "KeyType": KeyTypeType,
    },
)
_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "_OptionalDeliveryStreamEncryptionConfigurationInputTypeDef",
    {
        "KeyARN": str,
    },
    total=False,
)

class DeliveryStreamEncryptionConfigurationInputTypeDef(
    _RequiredDeliveryStreamEncryptionConfigurationInputTypeDef,
    _OptionalDeliveryStreamEncryptionConfigurationInputTypeDef,
):
    pass

DeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "DeliveryStreamEncryptionConfigurationTypeDef",
    {
        "KeyARN": str,
        "KeyType": KeyTypeType,
        "Status": DeliveryStreamEncryptionStatusType,
        "FailureDescription": "FailureDescriptionTypeDef",
    },
    total=False,
)

_RequiredDescribeDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredDescribeDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalDescribeDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalDescribeDeliveryStreamInputRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartDestinationId": str,
    },
    total=False,
)

class DescribeDeliveryStreamInputRequestTypeDef(
    _RequiredDescribeDeliveryStreamInputRequestTypeDef,
    _OptionalDescribeDeliveryStreamInputRequestTypeDef,
):
    pass

DescribeDeliveryStreamOutputTypeDef = TypedDict(
    "DescribeDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamDescription": "DeliveryStreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeserializerTypeDef = TypedDict(
    "DeserializerTypeDef",
    {
        "OpenXJsonSerDe": "OpenXJsonSerDeTypeDef",
        "HiveJsonSerDe": "HiveJsonSerDeTypeDef",
    },
    total=False,
)

_RequiredDestinationDescriptionTypeDef = TypedDict(
    "_RequiredDestinationDescriptionTypeDef",
    {
        "DestinationId": str,
    },
)
_OptionalDestinationDescriptionTypeDef = TypedDict(
    "_OptionalDestinationDescriptionTypeDef",
    {
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ExtendedS3DestinationDescription": "ExtendedS3DestinationDescriptionTypeDef",
        "RedshiftDestinationDescription": "RedshiftDestinationDescriptionTypeDef",
        "ElasticsearchDestinationDescription": "ElasticsearchDestinationDescriptionTypeDef",
        "AmazonopensearchserviceDestinationDescription": "AmazonopensearchserviceDestinationDescriptionTypeDef",
        "SplunkDestinationDescription": "SplunkDestinationDescriptionTypeDef",
        "HttpEndpointDestinationDescription": "HttpEndpointDestinationDescriptionTypeDef",
        "SnowflakeDestinationDescription": "SnowflakeDestinationDescriptionTypeDef",
        "AmazonOpenSearchServerlessDestinationDescription": "AmazonOpenSearchServerlessDestinationDescriptionTypeDef",
    },
    total=False,
)

class DestinationDescriptionTypeDef(
    _RequiredDestinationDescriptionTypeDef, _OptionalDestinationDescriptionTypeDef
):
    pass

DocumentIdOptionsTypeDef = TypedDict(
    "DocumentIdOptionsTypeDef",
    {
        "DefaultDocumentIdFormat": DefaultDocumentIdFormatType,
    },
)

DynamicPartitioningConfigurationTypeDef = TypedDict(
    "DynamicPartitioningConfigurationTypeDef",
    {
        "RetryOptions": "RetryOptionsTypeDef",
        "Enabled": bool,
    },
    total=False,
)

ElasticsearchBufferingHintsTypeDef = TypedDict(
    "ElasticsearchBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

_RequiredElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_RequiredElasticsearchDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_OptionalElasticsearchDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3BackupMode": ElasticsearchS3BackupModeType,
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

class ElasticsearchDestinationConfigurationTypeDef(
    _RequiredElasticsearchDestinationConfigurationTypeDef,
    _OptionalElasticsearchDestinationConfigurationTypeDef,
):
    pass

ElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "ElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3BackupMode": ElasticsearchS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

ElasticsearchDestinationUpdateTypeDef = TypedDict(
    "ElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": ElasticsearchIndexRotationPeriodType,
        "BufferingHints": "ElasticsearchBufferingHintsTypeDef",
        "RetryOptions": "ElasticsearchRetryOptionsTypeDef",
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "DocumentIdOptions": "DocumentIdOptionsTypeDef",
    },
    total=False,
)

ElasticsearchRetryOptionsTypeDef = TypedDict(
    "ElasticsearchRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": Literal["NoEncryption"],
        "KMSEncryptionConfig": "KMSEncryptionConfigTypeDef",
    },
    total=False,
)

_RequiredExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
    },
)
_OptionalExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalExtendedS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": S3BackupModeType,
        "S3BackupConfiguration": "S3DestinationConfigurationTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
        "DynamicPartitioningConfiguration": "DynamicPartitioningConfigurationTypeDef",
        "FileExtension": str,
        "CustomTimeZone": str,
    },
    total=False,
)

class ExtendedS3DestinationConfigurationTypeDef(
    _RequiredExtendedS3DestinationConfigurationTypeDef,
    _OptionalExtendedS3DestinationConfigurationTypeDef,
):
    pass

_RequiredExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "_RequiredExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": CompressionFormatType,
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
        "S3BackupMode": S3BackupModeType,
        "S3BackupDescription": "S3DestinationDescriptionTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
        "DynamicPartitioningConfiguration": "DynamicPartitioningConfigurationTypeDef",
        "FileExtension": str,
        "CustomTimeZone": str,
    },
    total=False,
)

class ExtendedS3DestinationDescriptionTypeDef(
    _RequiredExtendedS3DestinationDescriptionTypeDef,
    _OptionalExtendedS3DestinationDescriptionTypeDef,
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
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": S3BackupModeType,
        "S3BackupUpdate": "S3DestinationUpdateTypeDef",
        "DataFormatConversionConfiguration": "DataFormatConversionConfigurationTypeDef",
        "DynamicPartitioningConfiguration": "DynamicPartitioningConfigurationTypeDef",
        "FileExtension": str,
        "CustomTimeZone": str,
    },
    total=False,
)

FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef",
    {
        "Type": DeliveryStreamFailureTypeType,
        "Details": str,
    },
)

HiveJsonSerDeTypeDef = TypedDict(
    "HiveJsonSerDeTypeDef",
    {
        "TimestampFormats": List[str],
    },
    total=False,
)

HttpEndpointBufferingHintsTypeDef = TypedDict(
    "HttpEndpointBufferingHintsTypeDef",
    {
        "SizeInMBs": int,
        "IntervalInSeconds": int,
    },
    total=False,
)

HttpEndpointCommonAttributeTypeDef = TypedDict(
    "HttpEndpointCommonAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
)

_RequiredHttpEndpointConfigurationTypeDef = TypedDict(
    "_RequiredHttpEndpointConfigurationTypeDef",
    {
        "Url": str,
    },
)
_OptionalHttpEndpointConfigurationTypeDef = TypedDict(
    "_OptionalHttpEndpointConfigurationTypeDef",
    {
        "Name": str,
        "AccessKey": str,
    },
    total=False,
)

class HttpEndpointConfigurationTypeDef(
    _RequiredHttpEndpointConfigurationTypeDef, _OptionalHttpEndpointConfigurationTypeDef
):
    pass

HttpEndpointDescriptionTypeDef = TypedDict(
    "HttpEndpointDescriptionTypeDef",
    {
        "Url": str,
        "Name": str,
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
        "S3BackupMode": HttpEndpointS3BackupModeType,
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

class HttpEndpointDestinationConfigurationTypeDef(
    _RequiredHttpEndpointDestinationConfigurationTypeDef,
    _OptionalHttpEndpointDestinationConfigurationTypeDef,
):
    pass

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
        "S3BackupMode": HttpEndpointS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

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
        "S3BackupMode": HttpEndpointS3BackupModeType,
        "S3Update": "S3DestinationUpdateTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

HttpEndpointRequestConfigurationTypeDef = TypedDict(
    "HttpEndpointRequestConfigurationTypeDef",
    {
        "ContentEncoding": ContentEncodingType,
        "CommonAttributes": List["HttpEndpointCommonAttributeTypeDef"],
    },
    total=False,
)

HttpEndpointRetryOptionsTypeDef = TypedDict(
    "HttpEndpointRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

InputFormatConfigurationTypeDef = TypedDict(
    "InputFormatConfigurationTypeDef",
    {
        "Deserializer": "DeserializerTypeDef",
    },
    total=False,
)

KMSEncryptionConfigTypeDef = TypedDict(
    "KMSEncryptionConfigTypeDef",
    {
        "AWSKMSKeyARN": str,
    },
)

KinesisStreamSourceConfigurationTypeDef = TypedDict(
    "KinesisStreamSourceConfigurationTypeDef",
    {
        "KinesisStreamARN": str,
        "RoleARN": str,
    },
)

KinesisStreamSourceDescriptionTypeDef = TypedDict(
    "KinesisStreamSourceDescriptionTypeDef",
    {
        "KinesisStreamARN": str,
        "RoleARN": str,
        "DeliveryStartTimestamp": datetime,
    },
    total=False,
)

ListDeliveryStreamsInputRequestTypeDef = TypedDict(
    "ListDeliveryStreamsInputRequestTypeDef",
    {
        "Limit": int,
        "DeliveryStreamType": DeliveryStreamTypeType,
        "ExclusiveStartDeliveryStreamName": str,
    },
    total=False,
)

ListDeliveryStreamsOutputTypeDef = TypedDict(
    "ListDeliveryStreamsOutputTypeDef",
    {
        "DeliveryStreamNames": List[str],
        "HasMoreDeliveryStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForDeliveryStreamInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalListTagsForDeliveryStreamInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForDeliveryStreamInputRequestTypeDef",
    {
        "ExclusiveStartTagKey": str,
        "Limit": int,
    },
    total=False,
)

class ListTagsForDeliveryStreamInputRequestTypeDef(
    _RequiredListTagsForDeliveryStreamInputRequestTypeDef,
    _OptionalListTagsForDeliveryStreamInputRequestTypeDef,
):
    pass

ListTagsForDeliveryStreamOutputTypeDef = TypedDict(
    "ListTagsForDeliveryStreamOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MSKSourceConfigurationTypeDef = TypedDict(
    "MSKSourceConfigurationTypeDef",
    {
        "MSKClusterARN": str,
        "TopicName": str,
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
    },
)

MSKSourceDescriptionTypeDef = TypedDict(
    "MSKSourceDescriptionTypeDef",
    {
        "MSKClusterARN": str,
        "TopicName": str,
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
        "DeliveryStartTimestamp": datetime,
    },
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
        "Compression": OrcCompressionType,
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": OrcFormatVersionType,
    },
    total=False,
)

OutputFormatConfigurationTypeDef = TypedDict(
    "OutputFormatConfigurationTypeDef",
    {
        "Serializer": "SerializerTypeDef",
    },
    total=False,
)

ParquetSerDeTypeDef = TypedDict(
    "ParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": ParquetCompressionType,
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": ParquetWriterVersionType,
    },
    total=False,
)

ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List["ProcessorTypeDef"],
    },
    total=False,
)

ProcessorParameterTypeDef = TypedDict(
    "ProcessorParameterTypeDef",
    {
        "ParameterName": ProcessorParameterNameType,
        "ParameterValue": str,
    },
)

_RequiredProcessorTypeDef = TypedDict(
    "_RequiredProcessorTypeDef",
    {
        "Type": ProcessorTypeType,
    },
)
_OptionalProcessorTypeDef = TypedDict(
    "_OptionalProcessorTypeDef",
    {
        "Parameters": List["ProcessorParameterTypeDef"],
    },
    total=False,
)

class ProcessorTypeDef(_RequiredProcessorTypeDef, _OptionalProcessorTypeDef):
    pass

PutRecordBatchInputRequestTypeDef = TypedDict(
    "PutRecordBatchInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Records": List["RecordTypeDef"],
    },
)

PutRecordBatchOutputTypeDef = TypedDict(
    "PutRecordBatchOutputTypeDef",
    {
        "FailedPutCount": int,
        "Encrypted": bool,
        "RequestResponses": List["PutRecordBatchResponseEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordBatchResponseEntryTypeDef = TypedDict(
    "PutRecordBatchResponseEntryTypeDef",
    {
        "RecordId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutRecordInputRequestTypeDef = TypedDict(
    "PutRecordInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Record": "RecordTypeDef",
    },
)

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "RecordId": str,
        "Encrypted": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

_RequiredRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_RequiredRedshiftDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_OptionalRedshiftDestinationConfigurationTypeDef",
    {
        "Username": str,
        "Password": str,
        "RetryOptions": "RedshiftRetryOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupConfiguration": "S3DestinationConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

class RedshiftDestinationConfigurationTypeDef(
    _RequiredRedshiftDestinationConfigurationTypeDef,
    _OptionalRedshiftDestinationConfigurationTypeDef,
):
    pass

_RequiredRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_RequiredRedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
    },
)
_OptionalRedshiftDestinationDescriptionTypeDef = TypedDict(
    "_OptionalRedshiftDestinationDescriptionTypeDef",
    {
        "Username": str,
        "RetryOptions": "RedshiftRetryOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupDescription": "S3DestinationDescriptionTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

class RedshiftDestinationDescriptionTypeDef(
    _RequiredRedshiftDestinationDescriptionTypeDef, _OptionalRedshiftDestinationDescriptionTypeDef
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
        "S3BackupMode": RedshiftS3BackupModeType,
        "S3BackupUpdate": "S3DestinationUpdateTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

RedshiftRetryOptionsTypeDef = TypedDict(
    "RedshiftRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
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

RetryOptionsTypeDef = TypedDict(
    "RetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": CompressionFormatType,
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
        "CompressionFormat": CompressionFormatType,
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
        "CompressionFormat": CompressionFormatType,
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

_RequiredSecretsManagerConfigurationTypeDef = TypedDict(
    "_RequiredSecretsManagerConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalSecretsManagerConfigurationTypeDef = TypedDict(
    "_OptionalSecretsManagerConfigurationTypeDef",
    {
        "SecretARN": str,
        "RoleARN": str,
    },
    total=False,
)

class SecretsManagerConfigurationTypeDef(
    _RequiredSecretsManagerConfigurationTypeDef, _OptionalSecretsManagerConfigurationTypeDef
):
    pass

SerializerTypeDef = TypedDict(
    "SerializerTypeDef",
    {
        "ParquetSerDe": "ParquetSerDeTypeDef",
        "OrcSerDe": "OrcSerDeTypeDef",
    },
    total=False,
)

_RequiredSnowflakeDestinationConfigurationTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationConfigurationTypeDef",
    {
        "AccountUrl": str,
        "Database": str,
        "Schema": str,
        "Table": str,
        "RoleARN": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalSnowflakeDestinationConfigurationTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationConfigurationTypeDef",
    {
        "PrivateKey": str,
        "KeyPassphrase": str,
        "User": str,
        "SnowflakeRoleConfiguration": "SnowflakeRoleConfigurationTypeDef",
        "DataLoadingOption": SnowflakeDataLoadingOptionType,
        "MetaDataColumnName": str,
        "ContentColumnName": str,
        "SnowflakeVpcConfiguration": "SnowflakeVpcConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RetryOptions": "SnowflakeRetryOptionsTypeDef",
        "S3BackupMode": SnowflakeS3BackupModeType,
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

class SnowflakeDestinationConfigurationTypeDef(
    _RequiredSnowflakeDestinationConfigurationTypeDef,
    _OptionalSnowflakeDestinationConfigurationTypeDef,
):
    pass

SnowflakeDestinationDescriptionTypeDef = TypedDict(
    "SnowflakeDestinationDescriptionTypeDef",
    {
        "AccountUrl": str,
        "User": str,
        "Database": str,
        "Schema": str,
        "Table": str,
        "SnowflakeRoleConfiguration": "SnowflakeRoleConfigurationTypeDef",
        "DataLoadingOption": SnowflakeDataLoadingOptionType,
        "MetaDataColumnName": str,
        "ContentColumnName": str,
        "SnowflakeVpcConfiguration": "SnowflakeVpcConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RoleARN": str,
        "RetryOptions": "SnowflakeRetryOptionsTypeDef",
        "S3BackupMode": SnowflakeS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

SnowflakeDestinationUpdateTypeDef = TypedDict(
    "SnowflakeDestinationUpdateTypeDef",
    {
        "AccountUrl": str,
        "PrivateKey": str,
        "KeyPassphrase": str,
        "User": str,
        "Database": str,
        "Schema": str,
        "Table": str,
        "SnowflakeRoleConfiguration": "SnowflakeRoleConfigurationTypeDef",
        "DataLoadingOption": SnowflakeDataLoadingOptionType,
        "MetaDataColumnName": str,
        "ContentColumnName": str,
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "RoleARN": str,
        "RetryOptions": "SnowflakeRetryOptionsTypeDef",
        "S3BackupMode": SnowflakeS3BackupModeType,
        "S3Update": "S3DestinationUpdateTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

SnowflakeRetryOptionsTypeDef = TypedDict(
    "SnowflakeRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

SnowflakeRoleConfigurationTypeDef = TypedDict(
    "SnowflakeRoleConfigurationTypeDef",
    {
        "Enabled": bool,
        "SnowflakeRole": str,
    },
    total=False,
)

SnowflakeVpcConfigurationTypeDef = TypedDict(
    "SnowflakeVpcConfigurationTypeDef",
    {
        "PrivateLinkVpceId": str,
    },
)

SourceDescriptionTypeDef = TypedDict(
    "SourceDescriptionTypeDef",
    {
        "KinesisStreamSourceDescription": "KinesisStreamSourceDescriptionTypeDef",
        "MSKSourceDescription": "MSKSourceDescriptionTypeDef",
    },
    total=False,
)

SplunkBufferingHintsTypeDef = TypedDict(
    "SplunkBufferingHintsTypeDef",
    {
        "IntervalInSeconds": int,
        "SizeInMBs": int,
    },
    total=False,
)

_RequiredSplunkDestinationConfigurationTypeDef = TypedDict(
    "_RequiredSplunkDestinationConfigurationTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
    },
)
_OptionalSplunkDestinationConfigurationTypeDef = TypedDict(
    "_OptionalSplunkDestinationConfigurationTypeDef",
    {
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": SplunkS3BackupModeType,
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "BufferingHints": "SplunkBufferingHintsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

class SplunkDestinationConfigurationTypeDef(
    _RequiredSplunkDestinationConfigurationTypeDef, _OptionalSplunkDestinationConfigurationTypeDef
):
    pass

SplunkDestinationDescriptionTypeDef = TypedDict(
    "SplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": SplunkS3BackupModeType,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "BufferingHints": "SplunkBufferingHintsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

SplunkDestinationUpdateTypeDef = TypedDict(
    "SplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": "SplunkRetryOptionsTypeDef",
        "S3BackupMode": SplunkS3BackupModeType,
        "S3Update": "S3DestinationUpdateTypeDef",
        "ProcessingConfiguration": "ProcessingConfigurationTypeDef",
        "CloudWatchLoggingOptions": "CloudWatchLoggingOptionsTypeDef",
        "BufferingHints": "SplunkBufferingHintsTypeDef",
        "SecretsManagerConfiguration": "SecretsManagerConfigurationTypeDef",
    },
    total=False,
)

SplunkRetryOptionsTypeDef = TypedDict(
    "SplunkRetryOptionsTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

_RequiredStartDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStartDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)
_OptionalStartDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStartDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamEncryptionConfigurationInput": "DeliveryStreamEncryptionConfigurationInputTypeDef",
    },
    total=False,
)

class StartDeliveryStreamEncryptionInputRequestTypeDef(
    _RequiredStartDeliveryStreamEncryptionInputRequestTypeDef,
    _OptionalStartDeliveryStreamEncryptionInputRequestTypeDef,
):
    pass

StopDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)

TagDeliveryStreamInputRequestTypeDef = TypedDict(
    "TagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

UntagDeliveryStreamInputRequestTypeDef = TypedDict(
    "UntagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDestinationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDestinationInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "CurrentDeliveryStreamVersionId": str,
        "DestinationId": str,
    },
)
_OptionalUpdateDestinationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDestinationInputRequestTypeDef",
    {
        "S3DestinationUpdate": "S3DestinationUpdateTypeDef",
        "ExtendedS3DestinationUpdate": "ExtendedS3DestinationUpdateTypeDef",
        "RedshiftDestinationUpdate": "RedshiftDestinationUpdateTypeDef",
        "ElasticsearchDestinationUpdate": "ElasticsearchDestinationUpdateTypeDef",
        "AmazonopensearchserviceDestinationUpdate": "AmazonopensearchserviceDestinationUpdateTypeDef",
        "SplunkDestinationUpdate": "SplunkDestinationUpdateTypeDef",
        "HttpEndpointDestinationUpdate": "HttpEndpointDestinationUpdateTypeDef",
        "AmazonOpenSearchServerlessDestinationUpdate": "AmazonOpenSearchServerlessDestinationUpdateTypeDef",
        "SnowflakeDestinationUpdate": "SnowflakeDestinationUpdateTypeDef",
    },
    total=False,
)

class UpdateDestinationInputRequestTypeDef(
    _RequiredUpdateDestinationInputRequestTypeDef, _OptionalUpdateDestinationInputRequestTypeDef
):
    pass

VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "SubnetIds": List[str],
        "RoleARN": str,
        "SecurityGroupIds": List[str],
        "VpcId": str,
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": List[str],
        "RoleARN": str,
        "SecurityGroupIds": List[str],
    },
)
