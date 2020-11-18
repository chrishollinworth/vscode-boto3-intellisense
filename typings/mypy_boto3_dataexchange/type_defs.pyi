"""
Main interface for dataexchange service type definitions.

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import AssetDestinationEntryTypeDef

    data: AssetDestinationEntryTypeDef = {...}
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
    "AssetDestinationEntryTypeDef",
    "AssetDetailsTypeDef",
    "AssetEntryTypeDef",
    "AssetSourceEntryTypeDef",
    "DataSetEntryTypeDef",
    "DetailsTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "JobEntryTypeDef",
    "JobErrorTypeDef",
    "OriginDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "RevisionEntryTypeDef",
    "S3SnapshotAssetTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateJobResponseTypeDef",
    "CreateRevisionResponseTypeDef",
    "GetAssetResponseTypeDef",
    "GetDataSetResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListRevisionAssetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RequestDetailsTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateRevisionResponseTypeDef",
)

_RequiredAssetDestinationEntryTypeDef = TypedDict(
    "_RequiredAssetDestinationEntryTypeDef", {"AssetId": str, "Bucket": str}
)
_OptionalAssetDestinationEntryTypeDef = TypedDict(
    "_OptionalAssetDestinationEntryTypeDef", {"Key": str}, total=False
)


class AssetDestinationEntryTypeDef(
    _RequiredAssetDestinationEntryTypeDef, _OptionalAssetDestinationEntryTypeDef
):
    pass


AssetDetailsTypeDef = TypedDict(
    "AssetDetailsTypeDef", {"S3SnapshotAsset": "S3SnapshotAssetTypeDef"}, total=False
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
_OptionalAssetEntryTypeDef = TypedDict("_OptionalAssetEntryTypeDef", {"SourceId": str}, total=False)


class AssetEntryTypeDef(_RequiredAssetEntryTypeDef, _OptionalAssetEntryTypeDef):
    pass


AssetSourceEntryTypeDef = TypedDict("AssetSourceEntryTypeDef", {"Bucket": str, "Key": str})

_RequiredDataSetEntryTypeDef = TypedDict(
    "_RequiredDataSetEntryTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "UpdatedAt": datetime,
    },
)
_OptionalDataSetEntryTypeDef = TypedDict(
    "_OptionalDataSetEntryTypeDef",
    {"OriginDetails": "OriginDetailsTypeDef", "SourceId": str},
    total=False,
)


class DataSetEntryTypeDef(_RequiredDataSetEntryTypeDef, _OptionalDataSetEntryTypeDef):
    pass


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
    {"AssetId": str, "DataSetId": str, "RevisionId": str},
)

_RequiredExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "_RequiredExportAssetToSignedUrlResponseDetailsTypeDef",
    {"AssetId": str, "DataSetId": str, "RevisionId": str},
)
_OptionalExportAssetToSignedUrlResponseDetailsTypeDef = TypedDict(
    "_OptionalExportAssetToSignedUrlResponseDetailsTypeDef",
    {"SignedUrl": str, "SignedUrlExpiresAt": datetime},
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
    {"Encryption": "ExportServerSideEncryptionTypeDef"},
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
    {"Encryption": "ExportServerSideEncryptionTypeDef"},
    total=False,
)


class ExportAssetsToS3ResponseDetailsTypeDef(
    _RequiredExportAssetsToS3ResponseDetailsTypeDef, _OptionalExportAssetsToS3ResponseDetailsTypeDef
):
    pass


_RequiredExportServerSideEncryptionTypeDef = TypedDict(
    "_RequiredExportServerSideEncryptionTypeDef", {"Type": Literal["aws:kms", "AES256"]}
)
_OptionalExportServerSideEncryptionTypeDef = TypedDict(
    "_OptionalExportServerSideEncryptionTypeDef", {"KmsKeyArn": str}, total=False
)


class ExportServerSideEncryptionTypeDef(
    _RequiredExportServerSideEncryptionTypeDef, _OptionalExportServerSideEncryptionTypeDef
):
    pass


ImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef", {"AssetName": str}
)

ImportAssetFromSignedUrlRequestDetailsTypeDef = TypedDict(
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    {"AssetName": str, "DataSetId": str, "Md5Hash": str, "RevisionId": str},
)

_RequiredImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "_RequiredImportAssetFromSignedUrlResponseDetailsTypeDef",
    {"AssetName": str, "DataSetId": str, "RevisionId": str},
)
_OptionalImportAssetFromSignedUrlResponseDetailsTypeDef = TypedDict(
    "_OptionalImportAssetFromSignedUrlResponseDetailsTypeDef",
    {"Md5Hash": str, "SignedUrl": str, "SignedUrlExpiresAt": datetime},
    total=False,
)


class ImportAssetFromSignedUrlResponseDetailsTypeDef(
    _RequiredImportAssetFromSignedUrlResponseDetailsTypeDef,
    _OptionalImportAssetFromSignedUrlResponseDetailsTypeDef,
):
    pass


ImportAssetsFromS3RequestDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3RequestDetailsTypeDef",
    {"AssetSources": List["AssetSourceEntryTypeDef"], "DataSetId": str, "RevisionId": str},
)

ImportAssetsFromS3ResponseDetailsTypeDef = TypedDict(
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    {"AssetSources": List["AssetSourceEntryTypeDef"], "DataSetId": str, "RevisionId": str},
)

_RequiredJobEntryTypeDef = TypedDict(
    "_RequiredJobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
)
_OptionalJobEntryTypeDef = TypedDict(
    "_OptionalJobEntryTypeDef", {"Errors": List["JobErrorTypeDef"]}, total=False
)


class JobEntryTypeDef(_RequiredJobEntryTypeDef, _OptionalJobEntryTypeDef):
    pass


_RequiredJobErrorTypeDef = TypedDict(
    "_RequiredJobErrorTypeDef",
    {
        "Code": Literal[
            "ACCESS_DENIED_EXCEPTION",
            "INTERNAL_SERVER_EXCEPTION",
            "MALWARE_DETECTED",
            "RESOURCE_NOT_FOUND_EXCEPTION",
            "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
            "VALIDATION_EXCEPTION",
            "MALWARE_SCAN_ENCRYPTED_FILE",
        ],
        "Message": str,
    },
)
_OptionalJobErrorTypeDef = TypedDict(
    "_OptionalJobErrorTypeDef",
    {
        "Details": "DetailsTypeDef",
        "LimitName": Literal["Assets per revision", "Asset size in GB"],
        "LimitValue": float,
        "ResourceId": str,
        "ResourceType": Literal["REVISION", "ASSET"],
    },
    total=False,
)


class JobErrorTypeDef(_RequiredJobErrorTypeDef, _OptionalJobErrorTypeDef):
    pass


OriginDetailsTypeDef = TypedDict("OriginDetailsTypeDef", {"ProductId": str})

ResponseDetailsTypeDef = TypedDict(
    "ResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": "ExportAssetToSignedUrlResponseDetailsTypeDef",
        "ExportAssetsToS3": "ExportAssetsToS3ResponseDetailsTypeDef",
        "ImportAssetFromSignedUrl": "ImportAssetFromSignedUrlResponseDetailsTypeDef",
        "ImportAssetsFromS3": "ImportAssetsFromS3ResponseDetailsTypeDef",
    },
    total=False,
)

_RequiredRevisionEntryTypeDef = TypedDict(
    "_RequiredRevisionEntryTypeDef",
    {"Arn": str, "CreatedAt": datetime, "DataSetId": str, "Id": str, "UpdatedAt": datetime},
)
_OptionalRevisionEntryTypeDef = TypedDict(
    "_OptionalRevisionEntryTypeDef",
    {"Comment": str, "Finalized": bool, "SourceId": str},
    total=False,
)


class RevisionEntryTypeDef(_RequiredRevisionEntryTypeDef, _OptionalRevisionEntryTypeDef):
    pass


S3SnapshotAssetTypeDef = TypedDict("S3SnapshotAssetTypeDef", {"Size": float})

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

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
    },
    total=False,
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
    },
    total=False,
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
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
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
    },
    total=False,
)

ListDataSetRevisionsResponseTypeDef = TypedDict(
    "ListDataSetRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List["RevisionEntryTypeDef"]},
    total=False,
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {"DataSets": List["DataSetEntryTypeDef"], "NextToken": str},
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef", {"Jobs": List["JobEntryTypeDef"], "NextToken": str}, total=False
)

ListRevisionAssetsResponseTypeDef = TypedDict(
    "ListRevisionAssetsResponseTypeDef",
    {"Assets": List["AssetEntryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RequestDetailsTypeDef = TypedDict(
    "RequestDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": "ExportAssetToSignedUrlRequestDetailsTypeDef",
        "ExportAssetsToS3": "ExportAssetsToS3RequestDetailsTypeDef",
        "ImportAssetFromSignedUrl": "ImportAssetFromSignedUrlRequestDetailsTypeDef",
        "ImportAssetsFromS3": "ImportAssetsFromS3RequestDetailsTypeDef",
    },
    total=False,
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
    },
    total=False,
)

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": Literal["S3_SNAPSHOT"],
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": "OriginDetailsTypeDef",
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

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
    },
    total=False,
)
