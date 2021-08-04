"""
Type annotations for dataexchange service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import AssetDestinationEntryTypeDef

    data: AssetDestinationEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CodeType,
    JobErrorLimitNameType,
    JobErrorResourceTypesType,
    OriginType,
    ServerSideEncryptionTypesType,
    StateType,
    TypeType,
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
    "AssetDestinationEntryTypeDef",
    "AssetDetailsTypeDef",
    "AssetEntryTypeDef",
    "AssetSourceEntryTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateRevisionRequestRequestTypeDef",
    "CreateRevisionResponseTypeDef",
    "DataSetEntryTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteRevisionRequestRequestTypeDef",
    "DetailsTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "ExportRevisionsToS3RequestDetailsTypeDef",
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "GetAssetRequestRequestTypeDef",
    "GetAssetResponseTypeDef",
    "GetDataSetRequestRequestTypeDef",
    "GetDataSetResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "JobEntryTypeDef",
    "JobErrorTypeDef",
    "ListDataSetRevisionsRequestRequestTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListRevisionAssetsRequestRequestTypeDef",
    "ListRevisionAssetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OriginDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "RequestDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionDestinationEntryTypeDef",
    "RevisionEntryTypeDef",
    "S3SnapshotAssetTypeDef",
    "StartJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateRevisionRequestRequestTypeDef",
    "UpdateRevisionResponseTypeDef",
)

_RequiredAssetDestinationEntryTypeDef = TypedDict(
    "_RequiredAssetDestinationEntryTypeDef",
    {
        "AssetId": str,
        "Bucket": str,
    },
)
_OptionalAssetDestinationEntryTypeDef = TypedDict(
    "_OptionalAssetDestinationEntryTypeDef",
    {
        "Key": str,
    },
    total=False,
)

class AssetDestinationEntryTypeDef(
    _RequiredAssetDestinationEntryTypeDef, _OptionalAssetDestinationEntryTypeDef
):
    pass

AssetDetailsTypeDef = TypedDict(
    "AssetDetailsTypeDef",
    {
        "S3SnapshotAsset": "S3SnapshotAssetTypeDef",
    },
    total=False,
)

_RequiredAssetEntryTypeDef = TypedDict(
    "_RequiredAssetEntryTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "UpdatedAt": datetime,
    },
)
_OptionalAssetEntryTypeDef = TypedDict(
    "_OptionalAssetEntryTypeDef",
    {
        "SourceId": str,
    },
    total=False,
)

class AssetEntryTypeDef(_RequiredAssetEntryTypeDef, _OptionalAssetEntryTypeDef):
    pass

AssetSourceEntryTypeDef = TypedDict(
    "AssetSourceEntryTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

_RequiredCreateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSetRequestRequestTypeDef",
    {
        "AssetType": Literal["S3_SNAPSHOT"],
        "Description": str,
        "Name": str,
    },
)
_OptionalCreateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSetRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDataSetRequestRequestTypeDef(
    _RequiredCreateDataSetRequestRequestTypeDef, _OptionalCreateDataSetRequestRequestTypeDef
):
    pass

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "Details": "RequestDetailsTypeDef",
        "Type": TypeType,
    },
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRevisionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)
_OptionalCreateRevisionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRevisionRequestRequestTypeDef",
    {
        "Comment": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRevisionRequestRequestTypeDef(
    _RequiredCreateRevisionRequestRequestTypeDef, _OptionalCreateRevisionRequestRequestTypeDef
):
    pass

CreateRevisionResponseTypeDef = TypedDict(
    "CreateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataSetEntryTypeDef = TypedDict(
    "_RequiredDataSetEntryTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "UpdatedAt": datetime,
    },
)
_OptionalDataSetEntryTypeDef = TypedDict(
    "_OptionalDataSetEntryTypeDef",
    {
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
    },
    total=False,
)

class DataSetEntryTypeDef(_RequiredDataSetEntryTypeDef, _OptionalDataSetEntryTypeDef):
    pass

DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)

DeleteRevisionRequestRequestTypeDef = TypedDict(
    "DeleteRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)

DetailsTypeDef = TypedDict(
    "DetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
        "ImportAssetsFromS3JobErrorDetails": List["AssetSourceEntryTypeDef"],
    },
    total=False,
)

ExportAssetToSignedUrlRequestDetailsTypeDef = TypedDict(
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

_RequiredExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "_RequiredExportAssetToSignedUrlResponseDetailsTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "_OptionalExportAssetToSignedUrlResponseDetailsTypeDef",
    {
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

class ExportAssetToSignedUrlResponseDetailsTypeDef(
    _RequiredExportAssetToSignedUrlResponseDetailsTypeDef,
    _OptionalExportAssetToSignedUrlResponseDetailsTypeDef,
):
    pass

_RequiredExportAssetsToS3RequestDetailsTypeDef = TypedDict(
    "_RequiredExportAssetsToS3RequestDetailsTypeDef",
    {
        "AssetDestinations": List["AssetDestinationEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalExportAssetsToS3RequestDetailsTypeDef = TypedDict(
    "_OptionalExportAssetsToS3RequestDetailsTypeDef",
    {
        "Encryption": "ExportServerSideEncryptionTypeDef",
    },
    total=False,
)

class ExportAssetsToS3RequestDetailsTypeDef(
    _RequiredExportAssetsToS3RequestDetailsTypeDef, _OptionalExportAssetsToS3RequestDetailsTypeDef
):
    pass

_RequiredExportAssetsToS3ResponseDetailsTypeDef = TypedDict(
    "_RequiredExportAssetsToS3ResponseDetailsTypeDef",
    {
        "AssetDestinations": List["AssetDestinationEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalExportAssetsToS3ResponseDetailsTypeDef = TypedDict(
    "_OptionalExportAssetsToS3ResponseDetailsTypeDef",
    {
        "Encryption": "ExportServerSideEncryptionTypeDef",
    },
    total=False,
)

class ExportAssetsToS3ResponseDetailsTypeDef(
    _RequiredExportAssetsToS3ResponseDetailsTypeDef, _OptionalExportAssetsToS3ResponseDetailsTypeDef
):
    pass

_RequiredExportRevisionsToS3RequestDetailsTypeDef = TypedDict(
    "_RequiredExportRevisionsToS3RequestDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": List["RevisionDestinationEntryTypeDef"],
    },
)
_OptionalExportRevisionsToS3RequestDetailsTypeDef = TypedDict(
    "_OptionalExportRevisionsToS3RequestDetailsTypeDef",
    {
        "Encryption": "ExportServerSideEncryptionTypeDef",
    },
    total=False,
)

class ExportRevisionsToS3RequestDetailsTypeDef(
    _RequiredExportRevisionsToS3RequestDetailsTypeDef,
    _OptionalExportRevisionsToS3RequestDetailsTypeDef,
):
    pass

_RequiredExportRevisionsToS3ResponseDetailsTypeDef = TypedDict(
    "_RequiredExportRevisionsToS3ResponseDetailsTypeDef",
    {
        "DataSetId": str,
        "RevisionDestinations": List["RevisionDestinationEntryTypeDef"],
    },
)
_OptionalExportRevisionsToS3ResponseDetailsTypeDef = TypedDict(
    "_OptionalExportRevisionsToS3ResponseDetailsTypeDef",
    {
        "Encryption": "ExportServerSideEncryptionTypeDef",
    },
    total=False,
)

class ExportRevisionsToS3ResponseDetailsTypeDef(
    _RequiredExportRevisionsToS3ResponseDetailsTypeDef,
    _OptionalExportRevisionsToS3ResponseDetailsTypeDef,
):
    pass

_RequiredExportServerSideEncryptionTypeDef = TypedDict(
    "_RequiredExportServerSideEncryptionTypeDef",
    {
        "Type": ServerSideEncryptionTypesType,
    },
)
_OptionalExportServerSideEncryptionTypeDef = TypedDict(
    "_OptionalExportServerSideEncryptionTypeDef",
    {
        "KmsKeyArn": str,
    },
    total=False,
)

class ExportServerSideEncryptionTypeDef(
    _RequiredExportServerSideEncryptionTypeDef, _OptionalExportServerSideEncryptionTypeDef
):
    pass

GetAssetRequestRequestTypeDef = TypedDict(
    "GetAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)

GetAssetResponseTypeDef = TypedDict(
    "GetAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSetRequestRequestTypeDef = TypedDict(
    "GetDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)

GetDataSetResponseTypeDef = TypedDict(
    "GetDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRevisionRequestRequestTypeDef = TypedDict(
    "GetRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)

GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {
        "AssetName": str,
    },
)

ImportAssetFromSignedUrlRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
    },
)

_RequiredImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "_RequiredImportAssetFromSignedUrlResponseDetailsTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "_OptionalImportAssetFromSignedUrlResponseDetailsTypeDef",
    {
        "Md5Hash": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

class ImportAssetFromSignedUrlResponseDetailsTypeDef(
    _RequiredImportAssetFromSignedUrlResponseDetailsTypeDef,
    _OptionalImportAssetFromSignedUrlResponseDetailsTypeDef,
):
    pass

ImportAssetsFromS3RequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3RequestDetailsTypeDef",
    {
        "AssetSources": List["AssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

ImportAssetsFromS3ResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    {
        "AssetSources": List["AssetSourceEntryTypeDef"],
        "DataSetId": str,
        "RevisionId": str,
    },
)

_RequiredJobEntryTypeDef = TypedDict(
    "_RequiredJobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
    },
)
_OptionalJobEntryTypeDef = TypedDict(
    "_OptionalJobEntryTypeDef",
    {
        "Errors": List["JobErrorTypeDef"],
    },
    total=False,
)

class JobEntryTypeDef(_RequiredJobEntryTypeDef, _OptionalJobEntryTypeDef):
    pass

_RequiredJobErrorTypeDef = TypedDict(
    "_RequiredJobErrorTypeDef",
    {
        "Code": CodeType,
        "Message": str,
    },
)
_OptionalJobErrorTypeDef = TypedDict(
    "_OptionalJobErrorTypeDef",
    {
        "Details": "DetailsTypeDef",
        "LimitName": JobErrorLimitNameType,
        "LimitValue": float,
        "ResourceId": str,
        "ResourceType": JobErrorResourceTypesType,
    },
    total=False,
)

class JobErrorTypeDef(_RequiredJobErrorTypeDef, _OptionalJobErrorTypeDef):
    pass

_RequiredListDataSetRevisionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSetRevisionsRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)
_OptionalListDataSetRevisionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSetRevisionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDataSetRevisionsRequestRequestTypeDef(
    _RequiredListDataSetRevisionsRequestRequestTypeDef,
    _OptionalListDataSetRevisionsRequestRequestTypeDef,
):
    pass

ListDataSetRevisionsResponseTypeDef = TypedDict(
    "ListDataSetRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List["RevisionEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSetsRequestRequestTypeDef = TypedDict(
    "ListDataSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Origin": str,
    },
    total=False,
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSets": List["DataSetEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "MaxResults": int,
        "NextToken": str,
        "RevisionId": str,
    },
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List["JobEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRevisionAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredListRevisionAssetsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalListRevisionAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalListRevisionAssetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRevisionAssetsRequestRequestTypeDef(
    _RequiredListRevisionAssetsRequestRequestTypeDef,
    _OptionalListRevisionAssetsRequestRequestTypeDef,
):
    pass

ListRevisionAssetsResponseTypeDef = TypedDict(
    "ListRevisionAssetsResponseTypeDef",
    {
        "Assets": List["AssetEntryTypeDef"],
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

OriginDetailsTypeDef = TypedDict(
    "OriginDetailsTypeDef",
    {
        "ProductId": str,
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

RequestDetailsTypeDef = TypedDict(
    "RequestDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": "ExportAssetToSignedUrlRequestDetailsTypeDef",
        "ExportAssetsToS3": "ExportAssetsToS3RequestDetailsTypeDef",
        "ExportRevisionsToS3": "ExportRevisionsToS3RequestDetailsTypeDef",
        "ImportAssetFromSignedUrl": "ImportAssetFromSignedUrlRequestDetailsTypeDef",
        "ImportAssetsFromS3": "ImportAssetsFromS3RequestDetailsTypeDef",
    },
    total=False,
)

ResponseDetailsTypeDef = TypedDict(
    "ResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": "ExportAssetToSignedUrlResponseDetailsTypeDef",
        "ExportAssetsToS3": "ExportAssetsToS3ResponseDetailsTypeDef",
        "ExportRevisionsToS3": "ExportRevisionsToS3ResponseDetailsTypeDef",
        "ImportAssetFromSignedUrl": "ImportAssetFromSignedUrlResponseDetailsTypeDef",
        "ImportAssetsFromS3": "ImportAssetsFromS3ResponseDetailsTypeDef",
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

_RequiredRevisionDestinationEntryTypeDef = TypedDict(
    "_RequiredRevisionDestinationEntryTypeDef",
    {
        "Bucket": str,
        "RevisionId": str,
    },
)
_OptionalRevisionDestinationEntryTypeDef = TypedDict(
    "_OptionalRevisionDestinationEntryTypeDef",
    {
        "KeyPattern": str,
    },
    total=False,
)

class RevisionDestinationEntryTypeDef(
    _RequiredRevisionDestinationEntryTypeDef, _OptionalRevisionDestinationEntryTypeDef
):
    pass

_RequiredRevisionEntryTypeDef = TypedDict(
    "_RequiredRevisionEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "UpdatedAt": datetime,
    },
)
_OptionalRevisionEntryTypeDef = TypedDict(
    "_OptionalRevisionEntryTypeDef",
    {
        "Comment": str,
        "Finalized": bool,
        "SourceId": str,
    },
    total=False,
)

class RevisionEntryTypeDef(_RequiredRevisionEntryTypeDef, _OptionalRevisionEntryTypeDef):
    pass

S3SnapshotAssetTypeDef = TypedDict(
    "S3SnapshotAssetTypeDef",
    {
        "Size": float,
    },
)

StartJobRequestRequestTypeDef = TypedDict(
    "StartJobRequestRequestTypeDef",
    {
        "JobId": str,
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

UpdateAssetRequestRequestTypeDef = TypedDict(
    "UpdateAssetRequestRequestTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "Name": str,
        "RevisionId": str,
    },
)

UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": "AssetDetailsTypeDef",
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetRequestRequestTypeDef",
    {
        "DataSetId": str,
    },
)
_OptionalUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetRequestRequestTypeDef",
    {
        "Description": str,
        "Name": str,
    },
    total=False,
)

class UpdateDataSetRequestRequestTypeDef(
    _RequiredUpdateDataSetRequestRequestTypeDef, _OptionalUpdateDataSetRequestRequestTypeDef
):
    pass

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": OriginType,
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRevisionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRevisionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "RevisionId": str,
    },
)
_OptionalUpdateRevisionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRevisionRequestRequestTypeDef",
    {
        "Comment": str,
        "Finalized": bool,
    },
    total=False,
)

class UpdateRevisionRequestRequestTypeDef(
    _RequiredUpdateRevisionRequestRequestTypeDef, _OptionalUpdateRevisionRequestRequestTypeDef
):
    pass

UpdateRevisionResponseTypeDef = TypedDict(
    "UpdateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
