"""
Type annotations for firehose service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_firehose/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_firehose.type_defs import AmazonOpenSearchServerlessBufferingHintsTypeDef

    data: AmazonOpenSearchServerlessBufferingHintsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AmazonOpenSearchServerlessS3BackupModeType,
    AmazonopensearchserviceIndexRotationPeriodType,
    AmazonopensearchserviceS3BackupModeType,
    CompressionFormatType,
    ConnectivityType,
    ContentEncodingType,
    DatabaseTypeType,
    DefaultDocumentIdFormatType,
    DeliveryStreamEncryptionStatusType,
    DeliveryStreamFailureTypeType,
    DeliveryStreamStatusType,
    DeliveryStreamTypeType,
    ElasticsearchIndexRotationPeriodType,
    ElasticsearchS3BackupModeType,
    HECEndpointTypeType,
    HttpEndpointS3BackupModeType,
    IcebergS3BackupModeType,
    KeyTypeType,
    OrcCompressionType,
    OrcFormatVersionType,
    ParquetCompressionType,
    ParquetWriterVersionType,
    ProcessorParameterNameType,
    ProcessorTypeType,
    RedshiftS3BackupModeType,
    S3BackupModeType,
    SnapshotRequestedByType,
    SnapshotStatusType,
    SnowflakeDataLoadingOptionType,
    SnowflakeS3BackupModeType,
    SplunkS3BackupModeType,
    SSLModeType,
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
    "BlobTypeDef",
    "BufferingHintsTypeDef",
    "CatalogConfigurationTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "CopyCommandTypeDef",
    "CreateDeliveryStreamInputTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "DataFormatConversionConfigurationOutputTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "DataFormatConversionConfigurationUnionTypeDef",
    "DatabaseColumnListOutputTypeDef",
    "DatabaseColumnListTypeDef",
    "DatabaseColumnListUnionTypeDef",
    "DatabaseListOutputTypeDef",
    "DatabaseListTypeDef",
    "DatabaseListUnionTypeDef",
    "DatabaseSnapshotInfoTypeDef",
    "DatabaseSourceAuthenticationConfigurationTypeDef",
    "DatabaseSourceConfigurationTypeDef",
    "DatabaseSourceDescriptionTypeDef",
    "DatabaseSourceVPCConfigurationTypeDef",
    "DatabaseTableListOutputTypeDef",
    "DatabaseTableListTypeDef",
    "DatabaseTableListUnionTypeDef",
    "DeleteDeliveryStreamInputTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DescribeDeliveryStreamInputTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
    "DeserializerOutputTypeDef",
    "DeserializerTypeDef",
    "DeserializerUnionTypeDef",
    "DestinationDescriptionTypeDef",
    "DestinationTableConfigurationOutputTypeDef",
    "DestinationTableConfigurationTypeDef",
    "DestinationTableConfigurationUnionTypeDef",
    "DirectPutSourceConfigurationTypeDef",
    "DirectPutSourceDescriptionTypeDef",
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
    "HiveJsonSerDeOutputTypeDef",
    "HiveJsonSerDeTypeDef",
    "HiveJsonSerDeUnionTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "HttpEndpointRequestConfigurationOutputTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "HttpEndpointRequestConfigurationUnionTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "IcebergDestinationConfigurationTypeDef",
    "IcebergDestinationDescriptionTypeDef",
    "IcebergDestinationUpdateTypeDef",
    "InputFormatConfigurationOutputTypeDef",
    "InputFormatConfigurationTypeDef",
    "InputFormatConfigurationUnionTypeDef",
    "KMSEncryptionConfigTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "ListDeliveryStreamsInputTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamInputTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "MSKSourceConfigurationTypeDef",
    "MSKSourceDescriptionTypeDef",
    "OpenXJsonSerDeOutputTypeDef",
    "OpenXJsonSerDeTypeDef",
    "OpenXJsonSerDeUnionTypeDef",
    "OrcSerDeOutputTypeDef",
    "OrcSerDeTypeDef",
    "OrcSerDeUnionTypeDef",
    "OutputFormatConfigurationOutputTypeDef",
    "OutputFormatConfigurationTypeDef",
    "OutputFormatConfigurationUnionTypeDef",
    "ParquetSerDeTypeDef",
    "PartitionFieldTypeDef",
    "PartitionSpecOutputTypeDef",
    "PartitionSpecTypeDef",
    "PartitionSpecUnionTypeDef",
    "ProcessingConfigurationOutputTypeDef",
    "ProcessingConfigurationTypeDef",
    "ProcessingConfigurationUnionTypeDef",
    "ProcessorOutputTypeDef",
    "ProcessorParameterTypeDef",
    "ProcessorTypeDef",
    "ProcessorUnionTypeDef",
    "PutRecordBatchInputTypeDef",
    "PutRecordBatchOutputTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "PutRecordInputTypeDef",
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
    "SchemaEvolutionConfigurationTypeDef",
    "SecretsManagerConfigurationTypeDef",
    "SerializerOutputTypeDef",
    "SerializerTypeDef",
    "SerializerUnionTypeDef",
    "SnowflakeBufferingHintsTypeDef",
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
    "StartDeliveryStreamEncryptionInputTypeDef",
    "StopDeliveryStreamEncryptionInputTypeDef",
    "TableCreationConfigurationTypeDef",
    "TagDeliveryStreamInputTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagDeliveryStreamInputTypeDef",
    "UpdateDestinationInputTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
)

class AmazonOpenSearchServerlessBufferingHintsTypeDef(TypedDict):
    IntervalInSeconds: NotRequired[int]
    SizeInMBs: NotRequired[int]

class AmazonOpenSearchServerlessRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class CloudWatchLoggingOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    LogGroupName: NotRequired[str]
    LogStreamName: NotRequired[str]

class VpcConfigurationTypeDef(TypedDict):
    SubnetIds: Sequence[str]
    RoleARN: str
    SecurityGroupIds: Sequence[str]

class VpcConfigurationDescriptionTypeDef(TypedDict):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
    VpcId: str

class AmazonopensearchserviceBufferingHintsTypeDef(TypedDict):
    IntervalInSeconds: NotRequired[int]
    SizeInMBs: NotRequired[int]

class AmazonopensearchserviceRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class DocumentIdOptionsTypeDef(TypedDict):
    DefaultDocumentIdFormat: DefaultDocumentIdFormatType

class AuthenticationConfigurationTypeDef(TypedDict):
    RoleARN: str
    Connectivity: ConnectivityType

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BufferingHintsTypeDef(TypedDict):
    SizeInMBs: NotRequired[int]
    IntervalInSeconds: NotRequired[int]

class CatalogConfigurationTypeDef(TypedDict):
    CatalogARN: NotRequired[str]
    WarehouseLocation: NotRequired[str]

class CopyCommandTypeDef(TypedDict):
    DataTableName: str
    DataTableColumns: NotRequired[str]
    CopyOptions: NotRequired[str]

class DeliveryStreamEncryptionConfigurationInputTypeDef(TypedDict):
    KeyType: KeyTypeType
    KeyARN: NotRequired[str]

class DirectPutSourceConfigurationTypeDef(TypedDict):
    ThroughputHintInMBs: int

class KinesisStreamSourceConfigurationTypeDef(TypedDict):
    KinesisStreamARN: str
    RoleARN: str

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SchemaConfigurationTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    CatalogId: NotRequired[str]
    DatabaseName: NotRequired[str]
    TableName: NotRequired[str]
    Region: NotRequired[str]
    VersionId: NotRequired[str]

class DatabaseColumnListOutputTypeDef(TypedDict):
    Include: NotRequired[List[str]]
    Exclude: NotRequired[List[str]]

class DatabaseColumnListTypeDef(TypedDict):
    Include: NotRequired[Sequence[str]]
    Exclude: NotRequired[Sequence[str]]

class DatabaseListOutputTypeDef(TypedDict):
    Include: NotRequired[List[str]]
    Exclude: NotRequired[List[str]]

class DatabaseListTypeDef(TypedDict):
    Include: NotRequired[Sequence[str]]
    Exclude: NotRequired[Sequence[str]]

FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef",
    {
        "Type": DeliveryStreamFailureTypeType,
        "Details": str,
    },
)

class SecretsManagerConfigurationTypeDef(TypedDict):
    Enabled: bool
    SecretARN: NotRequired[str]
    RoleARN: NotRequired[str]

class DatabaseSourceVPCConfigurationTypeDef(TypedDict):
    VpcEndpointServiceName: str

class DatabaseTableListOutputTypeDef(TypedDict):
    Include: NotRequired[List[str]]
    Exclude: NotRequired[List[str]]

class DatabaseTableListTypeDef(TypedDict):
    Include: NotRequired[Sequence[str]]
    Exclude: NotRequired[Sequence[str]]

class DeleteDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    AllowForceDelete: NotRequired[bool]

class DescribeDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    Limit: NotRequired[int]
    ExclusiveStartDestinationId: NotRequired[str]

class HiveJsonSerDeOutputTypeDef(TypedDict):
    TimestampFormats: NotRequired[List[str]]

class OpenXJsonSerDeOutputTypeDef(TypedDict):
    ConvertDotsInJsonKeysToUnderscores: NotRequired[bool]
    CaseInsensitive: NotRequired[bool]
    ColumnToJsonKeyMappings: NotRequired[Dict[str, str]]

class DirectPutSourceDescriptionTypeDef(TypedDict):
    ThroughputHintInMBs: NotRequired[int]

class RetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class ElasticsearchBufferingHintsTypeDef(TypedDict):
    IntervalInSeconds: NotRequired[int]
    SizeInMBs: NotRequired[int]

class ElasticsearchRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class KMSEncryptionConfigTypeDef(TypedDict):
    AWSKMSKeyARN: str

class HiveJsonSerDeTypeDef(TypedDict):
    TimestampFormats: NotRequired[Sequence[str]]

class HttpEndpointBufferingHintsTypeDef(TypedDict):
    SizeInMBs: NotRequired[int]
    IntervalInSeconds: NotRequired[int]

class HttpEndpointCommonAttributeTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: str

class HttpEndpointConfigurationTypeDef(TypedDict):
    Url: str
    Name: NotRequired[str]
    AccessKey: NotRequired[str]

class HttpEndpointDescriptionTypeDef(TypedDict):
    Url: NotRequired[str]
    Name: NotRequired[str]

class HttpEndpointRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class SchemaEvolutionConfigurationTypeDef(TypedDict):
    Enabled: bool

class TableCreationConfigurationTypeDef(TypedDict):
    Enabled: bool

class KinesisStreamSourceDescriptionTypeDef(TypedDict):
    KinesisStreamARN: NotRequired[str]
    RoleARN: NotRequired[str]
    DeliveryStartTimestamp: NotRequired[datetime]

class ListDeliveryStreamsInputTypeDef(TypedDict):
    Limit: NotRequired[int]
    DeliveryStreamType: NotRequired[DeliveryStreamTypeType]
    ExclusiveStartDeliveryStreamName: NotRequired[str]

class ListTagsForDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    ExclusiveStartTagKey: NotRequired[str]
    Limit: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class OpenXJsonSerDeTypeDef(TypedDict):
    ConvertDotsInJsonKeysToUnderscores: NotRequired[bool]
    CaseInsensitive: NotRequired[bool]
    ColumnToJsonKeyMappings: NotRequired[Mapping[str, str]]

class OrcSerDeOutputTypeDef(TypedDict):
    StripeSizeBytes: NotRequired[int]
    BlockSizeBytes: NotRequired[int]
    RowIndexStride: NotRequired[int]
    EnablePadding: NotRequired[bool]
    PaddingTolerance: NotRequired[float]
    Compression: NotRequired[OrcCompressionType]
    BloomFilterColumns: NotRequired[List[str]]
    BloomFilterFalsePositiveProbability: NotRequired[float]
    DictionaryKeyThreshold: NotRequired[float]
    FormatVersion: NotRequired[OrcFormatVersionType]

class OrcSerDeTypeDef(TypedDict):
    StripeSizeBytes: NotRequired[int]
    BlockSizeBytes: NotRequired[int]
    RowIndexStride: NotRequired[int]
    EnablePadding: NotRequired[bool]
    PaddingTolerance: NotRequired[float]
    Compression: NotRequired[OrcCompressionType]
    BloomFilterColumns: NotRequired[Sequence[str]]
    BloomFilterFalsePositiveProbability: NotRequired[float]
    DictionaryKeyThreshold: NotRequired[float]
    FormatVersion: NotRequired[OrcFormatVersionType]

class ParquetSerDeTypeDef(TypedDict):
    BlockSizeBytes: NotRequired[int]
    PageSizeBytes: NotRequired[int]
    Compression: NotRequired[ParquetCompressionType]
    EnableDictionaryCompression: NotRequired[bool]
    MaxPaddingBytes: NotRequired[int]
    WriterVersion: NotRequired[ParquetWriterVersionType]

class PartitionFieldTypeDef(TypedDict):
    SourceName: str

class ProcessorParameterTypeDef(TypedDict):
    ParameterName: ProcessorParameterNameType
    ParameterValue: str

class PutRecordBatchResponseEntryTypeDef(TypedDict):
    RecordId: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class RedshiftRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class SnowflakeBufferingHintsTypeDef(TypedDict):
    SizeInMBs: NotRequired[int]
    IntervalInSeconds: NotRequired[int]

class SnowflakeRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class SnowflakeRoleConfigurationTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    SnowflakeRole: NotRequired[str]

class SnowflakeVpcConfigurationTypeDef(TypedDict):
    PrivateLinkVpceId: str

class SplunkBufferingHintsTypeDef(TypedDict):
    IntervalInSeconds: NotRequired[int]
    SizeInMBs: NotRequired[int]

class SplunkRetryOptionsTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class StopDeliveryStreamEncryptionInputTypeDef(TypedDict):
    DeliveryStreamName: str

class UntagDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    TagKeys: Sequence[str]

class MSKSourceDescriptionTypeDef(TypedDict):
    MSKClusterARN: NotRequired[str]
    TopicName: NotRequired[str]
    AuthenticationConfiguration: NotRequired[AuthenticationConfigurationTypeDef]
    DeliveryStartTimestamp: NotRequired[datetime]
    ReadFromTimestamp: NotRequired[datetime]

class RecordTypeDef(TypedDict):
    Data: BlobTypeDef

class StartDeliveryStreamEncryptionInputTypeDef(TypedDict):
    DeliveryStreamName: str
    DeliveryStreamEncryptionConfigurationInput: NotRequired[
        DeliveryStreamEncryptionConfigurationInputTypeDef
    ]

class TagDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    Tags: Sequence[TagTypeDef]

class CreateDeliveryStreamOutputTypeDef(TypedDict):
    DeliveryStreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeliveryStreamsOutputTypeDef(TypedDict):
    DeliveryStreamNames: List[str]
    HasMoreDeliveryStreams: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDeliveryStreamOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordOutputTypeDef(TypedDict):
    RecordId: str
    Encrypted: bool
    ResponseMetadata: ResponseMetadataTypeDef

DatabaseColumnListUnionTypeDef = Union[DatabaseColumnListTypeDef, DatabaseColumnListOutputTypeDef]
DatabaseListUnionTypeDef = Union[DatabaseListTypeDef, DatabaseListOutputTypeDef]

class DatabaseSnapshotInfoTypeDef(TypedDict):
    Id: str
    Table: str
    RequestTimestamp: datetime
    RequestedBy: SnapshotRequestedByType
    Status: SnapshotStatusType
    FailureDescription: NotRequired[FailureDescriptionTypeDef]

class DeliveryStreamEncryptionConfigurationTypeDef(TypedDict):
    KeyARN: NotRequired[str]
    KeyType: NotRequired[KeyTypeType]
    Status: NotRequired[DeliveryStreamEncryptionStatusType]
    FailureDescription: NotRequired[FailureDescriptionTypeDef]

class DatabaseSourceAuthenticationConfigurationTypeDef(TypedDict):
    SecretsManagerConfiguration: SecretsManagerConfigurationTypeDef

DatabaseTableListUnionTypeDef = Union[DatabaseTableListTypeDef, DatabaseTableListOutputTypeDef]

class DeserializerOutputTypeDef(TypedDict):
    OpenXJsonSerDe: NotRequired[OpenXJsonSerDeOutputTypeDef]
    HiveJsonSerDe: NotRequired[HiveJsonSerDeOutputTypeDef]

class DynamicPartitioningConfigurationTypeDef(TypedDict):
    RetryOptions: NotRequired[RetryOptionsTypeDef]
    Enabled: NotRequired[bool]

class EncryptionConfigurationTypeDef(TypedDict):
    NoEncryptionConfig: NotRequired[Literal["NoEncryption"]]
    KMSEncryptionConfig: NotRequired[KMSEncryptionConfigTypeDef]

HiveJsonSerDeUnionTypeDef = Union[HiveJsonSerDeTypeDef, HiveJsonSerDeOutputTypeDef]

class HttpEndpointRequestConfigurationOutputTypeDef(TypedDict):
    ContentEncoding: NotRequired[ContentEncodingType]
    CommonAttributes: NotRequired[List[HttpEndpointCommonAttributeTypeDef]]

class HttpEndpointRequestConfigurationTypeDef(TypedDict):
    ContentEncoding: NotRequired[ContentEncodingType]
    CommonAttributes: NotRequired[Sequence[HttpEndpointCommonAttributeTypeDef]]

class MSKSourceConfigurationTypeDef(TypedDict):
    MSKClusterARN: str
    TopicName: str
    AuthenticationConfiguration: AuthenticationConfigurationTypeDef
    ReadFromTimestamp: NotRequired[TimestampTypeDef]

OpenXJsonSerDeUnionTypeDef = Union[OpenXJsonSerDeTypeDef, OpenXJsonSerDeOutputTypeDef]
OrcSerDeUnionTypeDef = Union[OrcSerDeTypeDef, OrcSerDeOutputTypeDef]

class SerializerOutputTypeDef(TypedDict):
    ParquetSerDe: NotRequired[ParquetSerDeTypeDef]
    OrcSerDe: NotRequired[OrcSerDeOutputTypeDef]

class PartitionSpecOutputTypeDef(TypedDict):
    Identity: NotRequired[List[PartitionFieldTypeDef]]

class PartitionSpecTypeDef(TypedDict):
    Identity: NotRequired[Sequence[PartitionFieldTypeDef]]

ProcessorOutputTypeDef = TypedDict(
    "ProcessorOutputTypeDef",
    {
        "Type": ProcessorTypeType,
        "Parameters": NotRequired[List[ProcessorParameterTypeDef]],
    },
)
ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Type": ProcessorTypeType,
        "Parameters": NotRequired[Sequence[ProcessorParameterTypeDef]],
    },
)

class PutRecordBatchOutputTypeDef(TypedDict):
    FailedPutCount: int
    Encrypted: bool
    RequestResponses: List[PutRecordBatchResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordBatchInputTypeDef(TypedDict):
    DeliveryStreamName: str
    Records: Sequence[RecordTypeDef]

class PutRecordInputTypeDef(TypedDict):
    DeliveryStreamName: str
    Record: RecordTypeDef

DatabaseSourceDescriptionTypeDef = TypedDict(
    "DatabaseSourceDescriptionTypeDef",
    {
        "Type": NotRequired[DatabaseTypeType],
        "Endpoint": NotRequired[str],
        "Port": NotRequired[int],
        "SSLMode": NotRequired[SSLModeType],
        "Databases": NotRequired[DatabaseListOutputTypeDef],
        "Tables": NotRequired[DatabaseTableListOutputTypeDef],
        "Columns": NotRequired[DatabaseColumnListOutputTypeDef],
        "SurrogateKeys": NotRequired[List[str]],
        "SnapshotWatermarkTable": NotRequired[str],
        "SnapshotInfo": NotRequired[List[DatabaseSnapshotInfoTypeDef]],
        "DatabaseSourceAuthenticationConfiguration": NotRequired[
            DatabaseSourceAuthenticationConfigurationTypeDef
        ],
        "DatabaseSourceVPCConfiguration": NotRequired[DatabaseSourceVPCConfigurationTypeDef],
    },
)
DatabaseSourceConfigurationTypeDef = TypedDict(
    "DatabaseSourceConfigurationTypeDef",
    {
        "Type": DatabaseTypeType,
        "Endpoint": str,
        "Port": int,
        "Databases": DatabaseListUnionTypeDef,
        "Tables": DatabaseTableListUnionTypeDef,
        "SnapshotWatermarkTable": str,
        "DatabaseSourceAuthenticationConfiguration": DatabaseSourceAuthenticationConfigurationTypeDef,
        "DatabaseSourceVPCConfiguration": DatabaseSourceVPCConfigurationTypeDef,
        "SSLMode": NotRequired[SSLModeType],
        "Columns": NotRequired[DatabaseColumnListUnionTypeDef],
        "SurrogateKeys": NotRequired[Sequence[str]],
    },
)

class InputFormatConfigurationOutputTypeDef(TypedDict):
    Deserializer: NotRequired[DeserializerOutputTypeDef]

class S3DestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CompressionFormat: NotRequired[CompressionFormatType]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]

class S3DestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHintsTypeDef
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]

class S3DestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    BucketARN: NotRequired[str]
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CompressionFormat: NotRequired[CompressionFormatType]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]

HttpEndpointRequestConfigurationUnionTypeDef = Union[
    HttpEndpointRequestConfigurationTypeDef, HttpEndpointRequestConfigurationOutputTypeDef
]

class DeserializerTypeDef(TypedDict):
    OpenXJsonSerDe: NotRequired[OpenXJsonSerDeUnionTypeDef]
    HiveJsonSerDe: NotRequired[HiveJsonSerDeUnionTypeDef]

class SerializerTypeDef(TypedDict):
    ParquetSerDe: NotRequired[ParquetSerDeTypeDef]
    OrcSerDe: NotRequired[OrcSerDeUnionTypeDef]

class OutputFormatConfigurationOutputTypeDef(TypedDict):
    Serializer: NotRequired[SerializerOutputTypeDef]

class DestinationTableConfigurationOutputTypeDef(TypedDict):
    DestinationTableName: str
    DestinationDatabaseName: str
    UniqueKeys: NotRequired[List[str]]
    PartitionSpec: NotRequired[PartitionSpecOutputTypeDef]
    S3ErrorOutputPrefix: NotRequired[str]

PartitionSpecUnionTypeDef = Union[PartitionSpecTypeDef, PartitionSpecOutputTypeDef]

class ProcessingConfigurationOutputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Processors: NotRequired[List[ProcessorOutputTypeDef]]

ProcessorUnionTypeDef = Union[ProcessorTypeDef, ProcessorOutputTypeDef]

class SourceDescriptionTypeDef(TypedDict):
    DirectPutSourceDescription: NotRequired[DirectPutSourceDescriptionTypeDef]
    KinesisStreamSourceDescription: NotRequired[KinesisStreamSourceDescriptionTypeDef]
    MSKSourceDescription: NotRequired[MSKSourceDescriptionTypeDef]
    DatabaseSourceDescription: NotRequired[DatabaseSourceDescriptionTypeDef]

DeserializerUnionTypeDef = Union[DeserializerTypeDef, DeserializerOutputTypeDef]
SerializerUnionTypeDef = Union[SerializerTypeDef, SerializerOutputTypeDef]

class DataFormatConversionConfigurationOutputTypeDef(TypedDict):
    SchemaConfiguration: NotRequired[SchemaConfigurationTypeDef]
    InputFormatConfiguration: NotRequired[InputFormatConfigurationOutputTypeDef]
    OutputFormatConfiguration: NotRequired[OutputFormatConfigurationOutputTypeDef]
    Enabled: NotRequired[bool]

class DestinationTableConfigurationTypeDef(TypedDict):
    DestinationTableName: str
    DestinationDatabaseName: str
    UniqueKeys: NotRequired[Sequence[str]]
    PartitionSpec: NotRequired[PartitionSpecUnionTypeDef]
    S3ErrorOutputPrefix: NotRequired[str]

class AmazonOpenSearchServerlessDestinationDescriptionTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    CollectionEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    BufferingHints: NotRequired[AmazonOpenSearchServerlessBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonOpenSearchServerlessRetryOptionsTypeDef]
    S3BackupMode: NotRequired[AmazonOpenSearchServerlessS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfigurationDescription: NotRequired[VpcConfigurationDescriptionTypeDef]

class AmazonopensearchserviceDestinationDescriptionTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[AmazonopensearchserviceIndexRotationPeriodType]
    BufferingHints: NotRequired[AmazonopensearchserviceBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonopensearchserviceRetryOptionsTypeDef]
    S3BackupMode: NotRequired[AmazonopensearchserviceS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfigurationDescription: NotRequired[VpcConfigurationDescriptionTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class ElasticsearchDestinationDescriptionTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[ElasticsearchIndexRotationPeriodType]
    BufferingHints: NotRequired[ElasticsearchBufferingHintsTypeDef]
    RetryOptions: NotRequired[ElasticsearchRetryOptionsTypeDef]
    S3BackupMode: NotRequired[ElasticsearchS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfigurationDescription: NotRequired[VpcConfigurationDescriptionTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class HttpEndpointDestinationDescriptionTypeDef(TypedDict):
    EndpointConfiguration: NotRequired[HttpEndpointDescriptionTypeDef]
    BufferingHints: NotRequired[HttpEndpointBufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    RequestConfiguration: NotRequired[HttpEndpointRequestConfigurationOutputTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    RoleARN: NotRequired[str]
    RetryOptions: NotRequired[HttpEndpointRetryOptionsTypeDef]
    S3BackupMode: NotRequired[HttpEndpointS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class IcebergDestinationDescriptionTypeDef(TypedDict):
    DestinationTableConfigurationList: NotRequired[List[DestinationTableConfigurationOutputTypeDef]]
    SchemaEvolutionConfiguration: NotRequired[SchemaEvolutionConfigurationTypeDef]
    TableCreationConfiguration: NotRequired[TableCreationConfigurationTypeDef]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    S3BackupMode: NotRequired[IcebergS3BackupModeType]
    RetryOptions: NotRequired[RetryOptionsTypeDef]
    RoleARN: NotRequired[str]
    AppendOnly: NotRequired[bool]
    CatalogConfiguration: NotRequired[CatalogConfigurationTypeDef]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]

class RedshiftDestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommandTypeDef
    S3DestinationDescription: S3DestinationDescriptionTypeDef
    Username: NotRequired[str]
    RetryOptions: NotRequired[RedshiftRetryOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    S3BackupMode: NotRequired[RedshiftS3BackupModeType]
    S3BackupDescription: NotRequired[S3DestinationDescriptionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class SnowflakeDestinationDescriptionTypeDef(TypedDict):
    AccountUrl: NotRequired[str]
    User: NotRequired[str]
    Database: NotRequired[str]
    Schema: NotRequired[str]
    Table: NotRequired[str]
    SnowflakeRoleConfiguration: NotRequired[SnowflakeRoleConfigurationTypeDef]
    DataLoadingOption: NotRequired[SnowflakeDataLoadingOptionType]
    MetaDataColumnName: NotRequired[str]
    ContentColumnName: NotRequired[str]
    SnowflakeVpcConfiguration: NotRequired[SnowflakeVpcConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    RoleARN: NotRequired[str]
    RetryOptions: NotRequired[SnowflakeRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SnowflakeS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]
    BufferingHints: NotRequired[SnowflakeBufferingHintsTypeDef]

class SplunkDestinationDescriptionTypeDef(TypedDict):
    HECEndpoint: NotRequired[str]
    HECEndpointType: NotRequired[HECEndpointTypeType]
    HECToken: NotRequired[str]
    HECAcknowledgmentTimeoutInSeconds: NotRequired[int]
    RetryOptions: NotRequired[SplunkRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SplunkS3BackupModeType]
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    BufferingHints: NotRequired[SplunkBufferingHintsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class ProcessingConfigurationTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Processors: NotRequired[Sequence[ProcessorUnionTypeDef]]

class InputFormatConfigurationTypeDef(TypedDict):
    Deserializer: NotRequired[DeserializerUnionTypeDef]

class OutputFormatConfigurationTypeDef(TypedDict):
    Serializer: NotRequired[SerializerUnionTypeDef]

class ExtendedS3DestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    BufferingHints: BufferingHintsTypeDef
    CompressionFormat: CompressionFormatType
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationOutputTypeDef]
    S3BackupMode: NotRequired[S3BackupModeType]
    S3BackupDescription: NotRequired[S3DestinationDescriptionTypeDef]
    DataFormatConversionConfiguration: NotRequired[DataFormatConversionConfigurationOutputTypeDef]
    DynamicPartitioningConfiguration: NotRequired[DynamicPartitioningConfigurationTypeDef]
    FileExtension: NotRequired[str]
    CustomTimeZone: NotRequired[str]

DestinationTableConfigurationUnionTypeDef = Union[
    DestinationTableConfigurationTypeDef, DestinationTableConfigurationOutputTypeDef
]
ProcessingConfigurationUnionTypeDef = Union[
    ProcessingConfigurationTypeDef, ProcessingConfigurationOutputTypeDef
]
InputFormatConfigurationUnionTypeDef = Union[
    InputFormatConfigurationTypeDef, InputFormatConfigurationOutputTypeDef
]
OutputFormatConfigurationUnionTypeDef = Union[
    OutputFormatConfigurationTypeDef, OutputFormatConfigurationOutputTypeDef
]

class DestinationDescriptionTypeDef(TypedDict):
    DestinationId: str
    S3DestinationDescription: NotRequired[S3DestinationDescriptionTypeDef]
    ExtendedS3DestinationDescription: NotRequired[ExtendedS3DestinationDescriptionTypeDef]
    RedshiftDestinationDescription: NotRequired[RedshiftDestinationDescriptionTypeDef]
    ElasticsearchDestinationDescription: NotRequired[ElasticsearchDestinationDescriptionTypeDef]
    AmazonopensearchserviceDestinationDescription: NotRequired[
        AmazonopensearchserviceDestinationDescriptionTypeDef
    ]
    SplunkDestinationDescription: NotRequired[SplunkDestinationDescriptionTypeDef]
    HttpEndpointDestinationDescription: NotRequired[HttpEndpointDestinationDescriptionTypeDef]
    SnowflakeDestinationDescription: NotRequired[SnowflakeDestinationDescriptionTypeDef]
    AmazonOpenSearchServerlessDestinationDescription: NotRequired[
        AmazonOpenSearchServerlessDestinationDescriptionTypeDef
    ]
    IcebergDestinationDescription: NotRequired[IcebergDestinationDescriptionTypeDef]

class AmazonOpenSearchServerlessDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    CollectionEndpoint: NotRequired[str]
    BufferingHints: NotRequired[AmazonOpenSearchServerlessBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonOpenSearchServerlessRetryOptionsTypeDef]
    S3BackupMode: NotRequired[AmazonOpenSearchServerlessS3BackupModeType]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfiguration: NotRequired[VpcConfigurationTypeDef]

class AmazonOpenSearchServerlessDestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    CollectionEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    BufferingHints: NotRequired[AmazonOpenSearchServerlessBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonOpenSearchServerlessRetryOptionsTypeDef]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]

class AmazonopensearchserviceDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[AmazonopensearchserviceIndexRotationPeriodType]
    BufferingHints: NotRequired[AmazonopensearchserviceBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonopensearchserviceRetryOptionsTypeDef]
    S3BackupMode: NotRequired[AmazonopensearchserviceS3BackupModeType]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class AmazonopensearchserviceDestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[AmazonopensearchserviceIndexRotationPeriodType]
    BufferingHints: NotRequired[AmazonopensearchserviceBufferingHintsTypeDef]
    RetryOptions: NotRequired[AmazonopensearchserviceRetryOptionsTypeDef]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class ElasticsearchDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    IndexName: str
    S3Configuration: S3DestinationConfigurationTypeDef
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[ElasticsearchIndexRotationPeriodType]
    BufferingHints: NotRequired[ElasticsearchBufferingHintsTypeDef]
    RetryOptions: NotRequired[ElasticsearchRetryOptionsTypeDef]
    S3BackupMode: NotRequired[ElasticsearchS3BackupModeType]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    VpcConfiguration: NotRequired[VpcConfigurationTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class ElasticsearchDestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    DomainARN: NotRequired[str]
    ClusterEndpoint: NotRequired[str]
    IndexName: NotRequired[str]
    TypeName: NotRequired[str]
    IndexRotationPeriod: NotRequired[ElasticsearchIndexRotationPeriodType]
    BufferingHints: NotRequired[ElasticsearchBufferingHintsTypeDef]
    RetryOptions: NotRequired[ElasticsearchRetryOptionsTypeDef]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    DocumentIdOptions: NotRequired[DocumentIdOptionsTypeDef]

class HttpEndpointDestinationConfigurationTypeDef(TypedDict):
    EndpointConfiguration: HttpEndpointConfigurationTypeDef
    S3Configuration: S3DestinationConfigurationTypeDef
    BufferingHints: NotRequired[HttpEndpointBufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    RequestConfiguration: NotRequired[HttpEndpointRequestConfigurationUnionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    RoleARN: NotRequired[str]
    RetryOptions: NotRequired[HttpEndpointRetryOptionsTypeDef]
    S3BackupMode: NotRequired[HttpEndpointS3BackupModeType]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class HttpEndpointDestinationUpdateTypeDef(TypedDict):
    EndpointConfiguration: NotRequired[HttpEndpointConfigurationTypeDef]
    BufferingHints: NotRequired[HttpEndpointBufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    RequestConfiguration: NotRequired[HttpEndpointRequestConfigurationUnionTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    RoleARN: NotRequired[str]
    RetryOptions: NotRequired[HttpEndpointRetryOptionsTypeDef]
    S3BackupMode: NotRequired[HttpEndpointS3BackupModeType]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class IcebergDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    CatalogConfiguration: CatalogConfigurationTypeDef
    S3Configuration: S3DestinationConfigurationTypeDef
    DestinationTableConfigurationList: NotRequired[
        Sequence[DestinationTableConfigurationUnionTypeDef]
    ]
    SchemaEvolutionConfiguration: NotRequired[SchemaEvolutionConfigurationTypeDef]
    TableCreationConfiguration: NotRequired[TableCreationConfigurationTypeDef]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[IcebergS3BackupModeType]
    RetryOptions: NotRequired[RetryOptionsTypeDef]
    AppendOnly: NotRequired[bool]

class IcebergDestinationUpdateTypeDef(TypedDict):
    DestinationTableConfigurationList: NotRequired[
        Sequence[DestinationTableConfigurationUnionTypeDef]
    ]
    SchemaEvolutionConfiguration: NotRequired[SchemaEvolutionConfigurationTypeDef]
    TableCreationConfiguration: NotRequired[TableCreationConfigurationTypeDef]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[IcebergS3BackupModeType]
    RetryOptions: NotRequired[RetryOptionsTypeDef]
    RoleARN: NotRequired[str]
    AppendOnly: NotRequired[bool]
    CatalogConfiguration: NotRequired[CatalogConfigurationTypeDef]
    S3Configuration: NotRequired[S3DestinationConfigurationTypeDef]

class RedshiftDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: CopyCommandTypeDef
    S3Configuration: S3DestinationConfigurationTypeDef
    Username: NotRequired[str]
    Password: NotRequired[str]
    RetryOptions: NotRequired[RedshiftRetryOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[RedshiftS3BackupModeType]
    S3BackupConfiguration: NotRequired[S3DestinationConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class RedshiftDestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    ClusterJDBCURL: NotRequired[str]
    CopyCommand: NotRequired[CopyCommandTypeDef]
    Username: NotRequired[str]
    Password: NotRequired[str]
    RetryOptions: NotRequired[RedshiftRetryOptionsTypeDef]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[RedshiftS3BackupModeType]
    S3BackupUpdate: NotRequired[S3DestinationUpdateTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class SnowflakeDestinationConfigurationTypeDef(TypedDict):
    AccountUrl: str
    Database: str
    Schema: str
    Table: str
    RoleARN: str
    S3Configuration: S3DestinationConfigurationTypeDef
    PrivateKey: NotRequired[str]
    KeyPassphrase: NotRequired[str]
    User: NotRequired[str]
    SnowflakeRoleConfiguration: NotRequired[SnowflakeRoleConfigurationTypeDef]
    DataLoadingOption: NotRequired[SnowflakeDataLoadingOptionType]
    MetaDataColumnName: NotRequired[str]
    ContentColumnName: NotRequired[str]
    SnowflakeVpcConfiguration: NotRequired[SnowflakeVpcConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    RetryOptions: NotRequired[SnowflakeRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SnowflakeS3BackupModeType]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]
    BufferingHints: NotRequired[SnowflakeBufferingHintsTypeDef]

class SnowflakeDestinationUpdateTypeDef(TypedDict):
    AccountUrl: NotRequired[str]
    PrivateKey: NotRequired[str]
    KeyPassphrase: NotRequired[str]
    User: NotRequired[str]
    Database: NotRequired[str]
    Schema: NotRequired[str]
    Table: NotRequired[str]
    SnowflakeRoleConfiguration: NotRequired[SnowflakeRoleConfigurationTypeDef]
    DataLoadingOption: NotRequired[SnowflakeDataLoadingOptionType]
    MetaDataColumnName: NotRequired[str]
    ContentColumnName: NotRequired[str]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    RoleARN: NotRequired[str]
    RetryOptions: NotRequired[SnowflakeRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SnowflakeS3BackupModeType]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]
    BufferingHints: NotRequired[SnowflakeBufferingHintsTypeDef]

class SplunkDestinationConfigurationTypeDef(TypedDict):
    HECEndpoint: str
    HECEndpointType: HECEndpointTypeType
    S3Configuration: S3DestinationConfigurationTypeDef
    HECToken: NotRequired[str]
    HECAcknowledgmentTimeoutInSeconds: NotRequired[int]
    RetryOptions: NotRequired[SplunkRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SplunkS3BackupModeType]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    BufferingHints: NotRequired[SplunkBufferingHintsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class SplunkDestinationUpdateTypeDef(TypedDict):
    HECEndpoint: NotRequired[str]
    HECEndpointType: NotRequired[HECEndpointTypeType]
    HECToken: NotRequired[str]
    HECAcknowledgmentTimeoutInSeconds: NotRequired[int]
    RetryOptions: NotRequired[SplunkRetryOptionsTypeDef]
    S3BackupMode: NotRequired[SplunkS3BackupModeType]
    S3Update: NotRequired[S3DestinationUpdateTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    BufferingHints: NotRequired[SplunkBufferingHintsTypeDef]
    SecretsManagerConfiguration: NotRequired[SecretsManagerConfigurationTypeDef]

class DataFormatConversionConfigurationTypeDef(TypedDict):
    SchemaConfiguration: NotRequired[SchemaConfigurationTypeDef]
    InputFormatConfiguration: NotRequired[InputFormatConfigurationUnionTypeDef]
    OutputFormatConfiguration: NotRequired[OutputFormatConfigurationUnionTypeDef]
    Enabled: NotRequired[bool]

class DeliveryStreamDescriptionTypeDef(TypedDict):
    DeliveryStreamName: str
    DeliveryStreamARN: str
    DeliveryStreamStatus: DeliveryStreamStatusType
    DeliveryStreamType: DeliveryStreamTypeType
    VersionId: str
    Destinations: List[DestinationDescriptionTypeDef]
    HasMoreDestinations: bool
    FailureDescription: NotRequired[FailureDescriptionTypeDef]
    DeliveryStreamEncryptionConfiguration: NotRequired[DeliveryStreamEncryptionConfigurationTypeDef]
    CreateTimestamp: NotRequired[datetime]
    LastUpdateTimestamp: NotRequired[datetime]
    Source: NotRequired[SourceDescriptionTypeDef]

DataFormatConversionConfigurationUnionTypeDef = Union[
    DataFormatConversionConfigurationTypeDef, DataFormatConversionConfigurationOutputTypeDef
]

class DescribeDeliveryStreamOutputTypeDef(TypedDict):
    DeliveryStreamDescription: DeliveryStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExtendedS3DestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CompressionFormat: NotRequired[CompressionFormatType]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[S3BackupModeType]
    S3BackupConfiguration: NotRequired[S3DestinationConfigurationTypeDef]
    DataFormatConversionConfiguration: NotRequired[DataFormatConversionConfigurationUnionTypeDef]
    DynamicPartitioningConfiguration: NotRequired[DynamicPartitioningConfigurationTypeDef]
    FileExtension: NotRequired[str]
    CustomTimeZone: NotRequired[str]

class ExtendedS3DestinationUpdateTypeDef(TypedDict):
    RoleARN: NotRequired[str]
    BucketARN: NotRequired[str]
    Prefix: NotRequired[str]
    ErrorOutputPrefix: NotRequired[str]
    BufferingHints: NotRequired[BufferingHintsTypeDef]
    CompressionFormat: NotRequired[CompressionFormatType]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    CloudWatchLoggingOptions: NotRequired[CloudWatchLoggingOptionsTypeDef]
    ProcessingConfiguration: NotRequired[ProcessingConfigurationUnionTypeDef]
    S3BackupMode: NotRequired[S3BackupModeType]
    S3BackupUpdate: NotRequired[S3DestinationUpdateTypeDef]
    DataFormatConversionConfiguration: NotRequired[DataFormatConversionConfigurationUnionTypeDef]
    DynamicPartitioningConfiguration: NotRequired[DynamicPartitioningConfigurationTypeDef]
    FileExtension: NotRequired[str]
    CustomTimeZone: NotRequired[str]

class CreateDeliveryStreamInputTypeDef(TypedDict):
    DeliveryStreamName: str
    DeliveryStreamType: NotRequired[DeliveryStreamTypeType]
    DirectPutSourceConfiguration: NotRequired[DirectPutSourceConfigurationTypeDef]
    KinesisStreamSourceConfiguration: NotRequired[KinesisStreamSourceConfigurationTypeDef]
    DeliveryStreamEncryptionConfigurationInput: NotRequired[
        DeliveryStreamEncryptionConfigurationInputTypeDef
    ]
    S3DestinationConfiguration: NotRequired[S3DestinationConfigurationTypeDef]
    ExtendedS3DestinationConfiguration: NotRequired[ExtendedS3DestinationConfigurationTypeDef]
    RedshiftDestinationConfiguration: NotRequired[RedshiftDestinationConfigurationTypeDef]
    ElasticsearchDestinationConfiguration: NotRequired[ElasticsearchDestinationConfigurationTypeDef]
    AmazonopensearchserviceDestinationConfiguration: NotRequired[
        AmazonopensearchserviceDestinationConfigurationTypeDef
    ]
    SplunkDestinationConfiguration: NotRequired[SplunkDestinationConfigurationTypeDef]
    HttpEndpointDestinationConfiguration: NotRequired[HttpEndpointDestinationConfigurationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    AmazonOpenSearchServerlessDestinationConfiguration: NotRequired[
        AmazonOpenSearchServerlessDestinationConfigurationTypeDef
    ]
    MSKSourceConfiguration: NotRequired[MSKSourceConfigurationTypeDef]
    SnowflakeDestinationConfiguration: NotRequired[SnowflakeDestinationConfigurationTypeDef]
    IcebergDestinationConfiguration: NotRequired[IcebergDestinationConfigurationTypeDef]
    DatabaseSourceConfiguration: NotRequired[DatabaseSourceConfigurationTypeDef]

class UpdateDestinationInputTypeDef(TypedDict):
    DeliveryStreamName: str
    CurrentDeliveryStreamVersionId: str
    DestinationId: str
    S3DestinationUpdate: NotRequired[S3DestinationUpdateTypeDef]
    ExtendedS3DestinationUpdate: NotRequired[ExtendedS3DestinationUpdateTypeDef]
    RedshiftDestinationUpdate: NotRequired[RedshiftDestinationUpdateTypeDef]
    ElasticsearchDestinationUpdate: NotRequired[ElasticsearchDestinationUpdateTypeDef]
    AmazonopensearchserviceDestinationUpdate: NotRequired[
        AmazonopensearchserviceDestinationUpdateTypeDef
    ]
    SplunkDestinationUpdate: NotRequired[SplunkDestinationUpdateTypeDef]
    HttpEndpointDestinationUpdate: NotRequired[HttpEndpointDestinationUpdateTypeDef]
    AmazonOpenSearchServerlessDestinationUpdate: NotRequired[
        AmazonOpenSearchServerlessDestinationUpdateTypeDef
    ]
    SnowflakeDestinationUpdate: NotRequired[SnowflakeDestinationUpdateTypeDef]
    IcebergDestinationUpdate: NotRequired[IcebergDestinationUpdateTypeDef]
