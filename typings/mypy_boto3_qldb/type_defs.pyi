"""
Type annotations for qldb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamRequestTypeDef

    data: CancelJournalKinesisStreamRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    EncryptionStatusType,
    ErrorCauseType,
    ExportStatusType,
    LedgerStateType,
    OutputFormatType,
    PermissionsModeType,
    S3ObjectEncryptionTypeType,
    StreamStatusType,
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
    "CancelJournalKinesisStreamRequestTypeDef",
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerRequestTypeDef",
    "CreateLedgerResponseTypeDef",
    "DeleteLedgerRequestTypeDef",
    "DescribeJournalKinesisStreamRequestTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportRequestTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerRequestTypeDef",
    "DescribeLedgerResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportJournalToS3RequestTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockRequestTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestRequestTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerEncryptionDescriptionTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerRequestTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerRequestTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsRequestTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersRequestTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisRequestTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLedgerPermissionsModeRequestTypeDef",
    "UpdateLedgerPermissionsModeResponseTypeDef",
    "UpdateLedgerRequestTypeDef",
    "UpdateLedgerResponseTypeDef",
    "ValueHolderTypeDef",
)

class CancelJournalKinesisStreamRequestTypeDef(TypedDict):
    LedgerName: str
    StreamId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateLedgerRequestTypeDef(TypedDict):
    Name: str
    PermissionsMode: PermissionsModeType
    Tags: NotRequired[Mapping[str, str]]
    DeletionProtection: NotRequired[bool]
    KmsKey: NotRequired[str]

class DeleteLedgerRequestTypeDef(TypedDict):
    Name: str

class DescribeJournalKinesisStreamRequestTypeDef(TypedDict):
    LedgerName: str
    StreamId: str

class DescribeJournalS3ExportRequestTypeDef(TypedDict):
    Name: str
    ExportId: str

class DescribeLedgerRequestTypeDef(TypedDict):
    Name: str

class LedgerEncryptionDescriptionTypeDef(TypedDict):
    KmsKeyArn: str
    EncryptionStatus: EncryptionStatusType
    InaccessibleKmsKeyDateTime: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class ValueHolderTypeDef(TypedDict):
    IonText: NotRequired[str]

class GetDigestRequestTypeDef(TypedDict):
    Name: str

class KinesisConfigurationTypeDef(TypedDict):
    StreamArn: str
    AggregationEnabled: NotRequired[bool]

class LedgerSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    State: NotRequired[LedgerStateType]
    CreationDateTime: NotRequired[datetime]

class ListJournalKinesisStreamsForLedgerRequestTypeDef(TypedDict):
    LedgerName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListJournalS3ExportsForLedgerRequestTypeDef(TypedDict):
    Name: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListJournalS3ExportsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLedgersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class S3EncryptionConfigurationTypeDef(TypedDict):
    ObjectEncryptionType: S3ObjectEncryptionTypeType
    KmsKeyArn: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateLedgerPermissionsModeRequestTypeDef(TypedDict):
    Name: str
    PermissionsMode: PermissionsModeType

class UpdateLedgerRequestTypeDef(TypedDict):
    Name: str
    DeletionProtection: NotRequired[bool]
    KmsKey: NotRequired[str]

class CancelJournalKinesisStreamResponseTypeDef(TypedDict):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLedgerResponseTypeDef(TypedDict):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportJournalToS3ResponseTypeDef(TypedDict):
    ExportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StreamJournalToKinesisResponseTypeDef(TypedDict):
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLedgerPermissionsModeResponseTypeDef(TypedDict):
    Name: str
    Arn: str
    PermissionsMode: PermissionsModeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLedgerResponseTypeDef(TypedDict):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    PermissionsMode: PermissionsModeType
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLedgerResponseTypeDef(TypedDict):
    Name: str
    Arn: str
    State: LedgerStateType
    CreationDateTime: datetime
    DeletionProtection: bool
    EncryptionDescription: LedgerEncryptionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlockRequestTypeDef(TypedDict):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DigestTipAddress: NotRequired[ValueHolderTypeDef]

class GetBlockResponseTypeDef(TypedDict):
    Block: ValueHolderTypeDef
    Proof: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDigestResponseTypeDef(TypedDict):
    Digest: bytes
    DigestTipAddress: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevisionRequestTypeDef(TypedDict):
    Name: str
    BlockAddress: ValueHolderTypeDef
    DocumentId: str
    DigestTipAddress: NotRequired[ValueHolderTypeDef]

class GetRevisionResponseTypeDef(TypedDict):
    Proof: ValueHolderTypeDef
    Revision: ValueHolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JournalKinesisStreamDescriptionTypeDef(TypedDict):
    LedgerName: str
    RoleArn: str
    StreamId: str
    Status: StreamStatusType
    KinesisConfiguration: KinesisConfigurationTypeDef
    StreamName: str
    CreationTime: NotRequired[datetime]
    InclusiveStartTime: NotRequired[datetime]
    ExclusiveEndTime: NotRequired[datetime]
    Arn: NotRequired[str]
    ErrorCause: NotRequired[ErrorCauseType]

class StreamJournalToKinesisRequestTypeDef(TypedDict):
    LedgerName: str
    RoleArn: str
    InclusiveStartTime: TimestampTypeDef
    KinesisConfiguration: KinesisConfigurationTypeDef
    StreamName: str
    Tags: NotRequired[Mapping[str, str]]
    ExclusiveEndTime: NotRequired[TimestampTypeDef]

class ListLedgersResponseTypeDef(TypedDict):
    Ledgers: List[LedgerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class S3ExportConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: S3EncryptionConfigurationTypeDef

class DescribeJournalKinesisStreamResponseTypeDef(TypedDict):
    Stream: JournalKinesisStreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJournalKinesisStreamsForLedgerResponseTypeDef(TypedDict):
    Streams: List[JournalKinesisStreamDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExportJournalToS3RequestTypeDef(TypedDict):
    Name: str
    InclusiveStartTime: TimestampTypeDef
    ExclusiveEndTime: TimestampTypeDef
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: NotRequired[OutputFormatType]

class JournalS3ExportDescriptionTypeDef(TypedDict):
    LedgerName: str
    ExportId: str
    ExportCreationTime: datetime
    Status: ExportStatusType
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    S3ExportConfiguration: S3ExportConfigurationTypeDef
    RoleArn: str
    OutputFormat: NotRequired[OutputFormatType]

class DescribeJournalS3ExportResponseTypeDef(TypedDict):
    ExportDescription: JournalS3ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJournalS3ExportsForLedgerResponseTypeDef(TypedDict):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListJournalS3ExportsResponseTypeDef(TypedDict):
    JournalS3Exports: List[JournalS3ExportDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
