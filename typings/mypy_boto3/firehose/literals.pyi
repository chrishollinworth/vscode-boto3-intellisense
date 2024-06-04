"""
Type annotations for firehose service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/literals.html)

Usage::

    ```python
    from mypy_boto3_firehose.literals import AmazonOpenSearchServerlessS3BackupModeType

    data: AmazonOpenSearchServerlessS3BackupModeType = "AllDocuments"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AmazonOpenSearchServerlessS3BackupModeType",
    "AmazonopensearchserviceIndexRotationPeriodType",
    "AmazonopensearchserviceS3BackupModeType",
    "CompressionFormatType",
    "ConnectivityType",
    "ContentEncodingType",
    "DefaultDocumentIdFormatType",
    "DeliveryStreamEncryptionStatusType",
    "DeliveryStreamFailureTypeType",
    "DeliveryStreamStatusType",
    "DeliveryStreamTypeType",
    "ElasticsearchIndexRotationPeriodType",
    "ElasticsearchS3BackupModeType",
    "HECEndpointTypeType",
    "HttpEndpointS3BackupModeType",
    "KeyTypeType",
    "NoEncryptionConfigType",
    "OrcCompressionType",
    "OrcFormatVersionType",
    "ParquetCompressionType",
    "ParquetWriterVersionType",
    "ProcessorParameterNameType",
    "ProcessorTypeType",
    "RedshiftS3BackupModeType",
    "S3BackupModeType",
    "SnowflakeDataLoadingOptionType",
    "SnowflakeS3BackupModeType",
    "SplunkS3BackupModeType",
)

AmazonOpenSearchServerlessS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
AmazonopensearchserviceIndexRotationPeriodType = Literal[
    "NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"
]
AmazonopensearchserviceS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
CompressionFormatType = Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
ConnectivityType = Literal["PRIVATE", "PUBLIC"]
ContentEncodingType = Literal["GZIP", "NONE"]
DefaultDocumentIdFormatType = Literal["FIREHOSE_DEFAULT", "NO_DOCUMENT_ID"]
DeliveryStreamEncryptionStatusType = Literal[
    "DISABLED", "DISABLING", "DISABLING_FAILED", "ENABLED", "ENABLING", "ENABLING_FAILED"
]
DeliveryStreamFailureTypeType = Literal[
    "CREATE_ENI_FAILED",
    "CREATE_KMS_GRANT_FAILED",
    "DELETE_ENI_FAILED",
    "DISABLED_KMS_KEY",
    "ENI_ACCESS_DENIED",
    "INVALID_KMS_KEY",
    "KMS_ACCESS_DENIED",
    "KMS_KEY_NOT_FOUND",
    "KMS_OPT_IN_REQUIRED",
    "RETIRE_KMS_GRANT_FAILED",
    "SECURITY_GROUP_ACCESS_DENIED",
    "SECURITY_GROUP_NOT_FOUND",
    "SUBNET_ACCESS_DENIED",
    "SUBNET_NOT_FOUND",
    "UNKNOWN_ERROR",
]
DeliveryStreamStatusType = Literal[
    "ACTIVE", "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED"
]
DeliveryStreamTypeType = Literal["DirectPut", "KinesisStreamAsSource", "MSKAsSource"]
ElasticsearchIndexRotationPeriodType = Literal[
    "NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"
]
ElasticsearchS3BackupModeType = Literal["AllDocuments", "FailedDocumentsOnly"]
HECEndpointTypeType = Literal["Event", "Raw"]
HttpEndpointS3BackupModeType = Literal["AllData", "FailedDataOnly"]
KeyTypeType = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
NoEncryptionConfigType = Literal["NoEncryption"]
OrcCompressionType = Literal["NONE", "SNAPPY", "ZLIB"]
OrcFormatVersionType = Literal["V0_11", "V0_12"]
ParquetCompressionType = Literal["GZIP", "SNAPPY", "UNCOMPRESSED"]
ParquetWriterVersionType = Literal["V1", "V2"]
ProcessorParameterNameType = Literal[
    "BufferIntervalInSeconds",
    "BufferSizeInMBs",
    "CompressionFormat",
    "DataMessageExtraction",
    "Delimiter",
    "JsonParsingEngine",
    "LambdaArn",
    "MetadataExtractionQuery",
    "NumberOfRetries",
    "RoleArn",
    "SubRecordType",
]
ProcessorTypeType = Literal[
    "AppendDelimiterToRecord",
    "CloudWatchLogProcessing",
    "Decompression",
    "Lambda",
    "MetadataExtraction",
    "RecordDeAggregation",
]
RedshiftS3BackupModeType = Literal["Disabled", "Enabled"]
S3BackupModeType = Literal["Disabled", "Enabled"]
SnowflakeDataLoadingOptionType = Literal[
    "JSON_MAPPING", "VARIANT_CONTENT_AND_METADATA_MAPPING", "VARIANT_CONTENT_MAPPING"
]
SnowflakeS3BackupModeType = Literal["AllData", "FailedDataOnly"]
SplunkS3BackupModeType = Literal["AllEvents", "FailedEventsOnly"]
