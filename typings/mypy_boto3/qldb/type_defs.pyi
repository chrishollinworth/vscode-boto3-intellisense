"""
Type annotations for qldb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamRequestRequestTypeDef

    data: CancelJournalKinesisStreamRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EncryptionStatusType,
    ErrorCauseType,
    ExportStatusType,
    LedgerStateType,
    PermissionsModeType,
    S3ObjectEncryptionTypeType,
    StreamStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerRequestRequestTypeDef",
    "CreateLedgerResponseTypeDef",
    "DeleteLedgerRequestRequestTypeDef",
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportRequestRequestTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerRequestRequestTypeDef",
    "DescribeLedgerResponseTypeDef",
    "ExportJournalToS3RequestRequestTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockRequestRequestTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestRequestRequestTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerEncryptionDescriptionTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerRequestRequestTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsRequestRequestTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersRequestRequestTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisRequestRequestTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    "UpdateLedgerPermissionsModeResponseTypeDef",
    "UpdateLedgerRequestRequestTypeDef",
    "UpdateLedgerResponseTypeDef",
    "ValueHolderTypeDef",
)

CancelJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

CancelJournalKinesisStreamResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLedgerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)
_OptionalCreateLedgerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLedgerRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "DeletionProtection": bool,
        "KmsKey": str,
    },
    total=False,
)

class CreateLedgerRequestRequestTypeDef(
    _RequiredCreateLedgerRequestRequestTypeDef, _OptionalCreateLedgerRequestRequestTypeDef
):
    pass

CreateLedgerResponseTypeDef = TypedDict(
    "CreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLedgerRequestRequestTypeDef = TypedDict(
    "DeleteLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

DescribeJournalKinesisStreamResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseTypeDef",
    {
        "Stream": "JournalKinesisStreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJournalS3ExportRequestRequestTypeDef = TypedDict(
    "DescribeJournalS3ExportRequestRequestTypeDef",
    {
        "Name": str,
        "ExportId": str,
    },
)

DescribeJournalS3ExportResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseTypeDef",
    {
        "ExportDescription": "JournalS3ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLedgerRequestRequestTypeDef = TypedDict(
    "DescribeLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeLedgerResponseTypeDef = TypedDict(
    "DescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "EncryptionDescription": "LedgerEncryptionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportJournalToS3RequestRequestTypeDef = TypedDict(
    "ExportJournalToS3RequestRequestTypeDef",
    {
        "Name": str,
        "InclusiveStartTime": Union[datetime, str],
        "ExclusiveEndTime": Union[datetime, str],
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
    },
)

ExportJournalToS3ResponseTypeDef = TypedDict(
    "ExportJournalToS3ResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBlockRequestRequestTypeDef = TypedDict(
    "_RequiredGetBlockRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
    },
)
_OptionalGetBlockRequestRequestTypeDef = TypedDict(
    "_OptionalGetBlockRequestRequestTypeDef",
    {
        "DigestTipAddress": "ValueHolderTypeDef",
    },
    total=False,
)

class GetBlockRequestRequestTypeDef(
    _RequiredGetBlockRequestRequestTypeDef, _OptionalGetBlockRequestRequestTypeDef
):
    pass

GetBlockResponseTypeDef = TypedDict(
    "GetBlockResponseTypeDef",
    {
        "Block": "ValueHolderTypeDef",
        "Proof": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDigestRequestRequestTypeDef = TypedDict(
    "GetDigestRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDigestResponseTypeDef = TypedDict(
    "GetDigestResponseTypeDef",
    {
        "Digest": bytes,
        "DigestTipAddress": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRevisionRequestRequestTypeDef = TypedDict(
    "_RequiredGetRevisionRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
        "DocumentId": str,
    },
)
_OptionalGetRevisionRequestRequestTypeDef = TypedDict(
    "_OptionalGetRevisionRequestRequestTypeDef",
    {
        "DigestTipAddress": "ValueHolderTypeDef",
    },
    total=False,
)

class GetRevisionRequestRequestTypeDef(
    _RequiredGetRevisionRequestRequestTypeDef, _OptionalGetRevisionRequestRequestTypeDef
):
    pass

GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Proof": "ValueHolderTypeDef",
        "Revision": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_RequiredJournalKinesisStreamDescriptionTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "StreamId": str,
        "Status": StreamStatusType,
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
    },
)
_OptionalJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_OptionalJournalKinesisStreamDescriptionTypeDef",
    {
        "CreationTime": datetime,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "Arn": str,
        "ErrorCause": ErrorCauseType,
    },
    total=False,
)

class JournalKinesisStreamDescriptionTypeDef(
    _RequiredJournalKinesisStreamDescriptionTypeDef, _OptionalJournalKinesisStreamDescriptionTypeDef
):
    pass

JournalS3ExportDescriptionTypeDef = TypedDict(
    "JournalS3ExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": ExportStatusType,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
    },
)

_RequiredKinesisConfigurationTypeDef = TypedDict(
    "_RequiredKinesisConfigurationTypeDef",
    {
        "StreamArn": str,
    },
)
_OptionalKinesisConfigurationTypeDef = TypedDict(
    "_OptionalKinesisConfigurationTypeDef",
    {
        "AggregationEnabled": bool,
    },
    total=False,
)

class KinesisConfigurationTypeDef(
    _RequiredKinesisConfigurationTypeDef, _OptionalKinesisConfigurationTypeDef
):
    pass

_RequiredLedgerEncryptionDescriptionTypeDef = TypedDict(
    "_RequiredLedgerEncryptionDescriptionTypeDef",
    {
        "KmsKeyArn": str,
        "EncryptionStatus": EncryptionStatusType,
    },
)
_OptionalLedgerEncryptionDescriptionTypeDef = TypedDict(
    "_OptionalLedgerEncryptionDescriptionTypeDef",
    {
        "InaccessibleKmsKeyDateTime": datetime,
    },
    total=False,
)

class LedgerEncryptionDescriptionTypeDef(
    _RequiredLedgerEncryptionDescriptionTypeDef, _OptionalLedgerEncryptionDescriptionTypeDef
):
    pass

LedgerSummaryTypeDef = TypedDict(
    "LedgerSummaryTypeDef",
    {
        "Name": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
    },
    total=False,
)

_RequiredListJournalKinesisStreamsForLedgerRequestRequestTypeDef = TypedDict(
    "_RequiredListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    {
        "LedgerName": str,
    },
)
_OptionalListJournalKinesisStreamsForLedgerRequestRequestTypeDef = TypedDict(
    "_OptionalListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListJournalKinesisStreamsForLedgerRequestRequestTypeDef(
    _RequiredListJournalKinesisStreamsForLedgerRequestRequestTypeDef,
    _OptionalListJournalKinesisStreamsForLedgerRequestRequestTypeDef,
):
    pass

ListJournalKinesisStreamsForLedgerResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    {
        "Streams": List["JournalKinesisStreamDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJournalS3ExportsForLedgerRequestRequestTypeDef = TypedDict(
    "_RequiredListJournalS3ExportsForLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJournalS3ExportsForLedgerRequestRequestTypeDef = TypedDict(
    "_OptionalListJournalS3ExportsForLedgerRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListJournalS3ExportsForLedgerRequestRequestTypeDef(
    _RequiredListJournalS3ExportsForLedgerRequestRequestTypeDef,
    _OptionalListJournalS3ExportsForLedgerRequestRequestTypeDef,
):
    pass

ListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJournalS3ExportsRequestRequestTypeDef = TypedDict(
    "ListJournalS3ExportsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListJournalS3ExportsResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLedgersRequestRequestTypeDef = TypedDict(
    "ListLedgersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLedgersResponseTypeDef = TypedDict(
    "ListLedgersResponseTypeDef",
    {
        "Ledgers": List["LedgerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredS3EncryptionConfigurationTypeDef = TypedDict(
    "_RequiredS3EncryptionConfigurationTypeDef",
    {
        "ObjectEncryptionType": S3ObjectEncryptionTypeType,
    },
)
_OptionalS3EncryptionConfigurationTypeDef = TypedDict(
    "_OptionalS3EncryptionConfigurationTypeDef",
    {
        "KmsKeyArn": str,
    },
    total=False,
)

class S3EncryptionConfigurationTypeDef(
    _RequiredS3EncryptionConfigurationTypeDef, _OptionalS3EncryptionConfigurationTypeDef
):
    pass

S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": "S3EncryptionConfigurationTypeDef",
    },
)

_RequiredStreamJournalToKinesisRequestRequestTypeDef = TypedDict(
    "_RequiredStreamJournalToKinesisRequestRequestTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "InclusiveStartTime": Union[datetime, str],
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
    },
)
_OptionalStreamJournalToKinesisRequestRequestTypeDef = TypedDict(
    "_OptionalStreamJournalToKinesisRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "ExclusiveEndTime": Union[datetime, str],
    },
    total=False,
)

class StreamJournalToKinesisRequestRequestTypeDef(
    _RequiredStreamJournalToKinesisRequestRequestTypeDef,
    _OptionalStreamJournalToKinesisRequestRequestTypeDef,
):
    pass

StreamJournalToKinesisResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateLedgerPermissionsModeRequestRequestTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)

UpdateLedgerPermissionsModeResponseTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "PermissionsMode": PermissionsModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLedgerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateLedgerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLedgerRequestRequestTypeDef",
    {
        "DeletionProtection": bool,
        "KmsKey": str,
    },
    total=False,
)

class UpdateLedgerRequestRequestTypeDef(
    _RequiredUpdateLedgerRequestRequestTypeDef, _OptionalUpdateLedgerRequestRequestTypeDef
):
    pass

UpdateLedgerResponseTypeDef = TypedDict(
    "UpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
        "EncryptionDescription": "LedgerEncryptionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonText": str,
    },
    total=False,
)
