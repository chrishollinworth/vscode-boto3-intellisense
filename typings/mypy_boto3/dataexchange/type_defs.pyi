"""
Type annotations for dataexchange service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import AcceptDataGrantRequestTypeDef

    data: AcceptDataGrantRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AcceptanceStateFilterValueType,
    AssetTypeType,
    CodeType,
    DataGrantAcceptanceStateType,
    GrantDistributionScopeType,
    JobErrorLimitNameType,
    JobErrorResourceTypesType,
    LFPermissionType,
    LFResourceTypeType,
    NotificationTypeType,
    OriginType,
    SchemaChangeTypeType,
    ServerSideEncryptionTypesType,
    StateType,
    TableTagPolicyLFPermissionType,
    TypeType,
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
    "AcceptDataGrantRequestTypeDef",
    "AcceptDataGrantResponseTypeDef",
    "ActionTypeDef",
    "ApiGatewayApiAssetTypeDef",
    "AssetDestinationEntryTypeDef",
    "AssetDetailsTypeDef",
    "AssetEntryTypeDef",
    "AssetSourceEntryTypeDef",
    "AutoExportRevisionDestinationEntryTypeDef",
    "AutoExportRevisionToS3RequestDetailsTypeDef",
    "CancelJobRequestTypeDef",
    "CreateDataGrantRequestTypeDef",
    "CreateDataGrantResponseTypeDef",
    "CreateDataSetRequestTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateEventActionRequestTypeDef",
    "CreateEventActionResponseTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateRevisionRequestTypeDef",
    "CreateRevisionResponseTypeDef",
    "CreateS3DataAccessFromS3BucketRequestDetailsTypeDef",
    "CreateS3DataAccessFromS3BucketResponseDetailsTypeDef",
    "DataGrantSummaryEntryTypeDef",
    "DataSetEntryTypeDef",
    "DataUpdateRequestDetailsTypeDef",
    "DatabaseLFTagPolicyAndPermissionsOutputTypeDef",
    "DatabaseLFTagPolicyAndPermissionsTypeDef",
    "DatabaseLFTagPolicyAndPermissionsUnionTypeDef",
    "DatabaseLFTagPolicyTypeDef",
    "DeleteAssetRequestTypeDef",
    "DeleteDataGrantRequestTypeDef",
    "DeleteDataSetRequestTypeDef",
    "DeleteEventActionRequestTypeDef",
    "DeleteRevisionRequestTypeDef",
    "DeprecationRequestDetailsTypeDef",
    "DetailsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventActionEntryTypeDef",
    "EventTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "ExportRevisionsToS3RequestDetailsTypeDef",
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "GetAssetRequestTypeDef",
    "GetAssetResponseTypeDef",
    "GetDataGrantRequestTypeDef",
    "GetDataGrantResponseTypeDef",
    "GetDataSetRequestTypeDef",
    "GetDataSetResponseTypeDef",
    "GetEventActionRequestTypeDef",
    "GetEventActionResponseTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetReceivedDataGrantRequestTypeDef",
    "GetReceivedDataGrantResponseTypeDef",
    "GetRevisionRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "ImportAssetFromApiGatewayApiRequestDetailsTypeDef",
    "ImportAssetFromApiGatewayApiResponseDetailsTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef",
    "ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef",
    "ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "JobEntryTypeDef",
    "JobErrorTypeDef",
    "KmsKeyToGrantTypeDef",
    "LFResourceDetailsTypeDef",
    "LFTagOutputTypeDef",
    "LFTagPolicyDetailsTypeDef",
    "LFTagTypeDef",
    "LFTagUnionTypeDef",
    "LakeFormationDataPermissionAssetTypeDef",
    "LakeFormationDataPermissionDetailsTypeDef",
    "LakeFormationTagPolicyDetailsTypeDef",
    "ListDataGrantsRequestPaginateTypeDef",
    "ListDataGrantsRequestTypeDef",
    "ListDataGrantsResponseTypeDef",
    "ListDataSetRevisionsRequestPaginateTypeDef",
    "ListDataSetRevisionsRequestTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListDataSetsRequestPaginateTypeDef",
    "ListDataSetsRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListEventActionsRequestPaginateTypeDef",
    "ListEventActionsRequestTypeDef",
    "ListEventActionsResponseTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListReceivedDataGrantsRequestPaginateTypeDef",
    "ListReceivedDataGrantsRequestTypeDef",
    "ListReceivedDataGrantsResponseTypeDef",
    "ListRevisionAssetsRequestPaginateTypeDef",
    "ListRevisionAssetsRequestTypeDef",
    "ListRevisionAssetsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotificationDetailsTypeDef",
    "OriginDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ReceivedDataGrantSummariesEntryTypeDef",
    "RedshiftDataShareAssetSourceEntryTypeDef",
    "RedshiftDataShareAssetTypeDef",
    "RedshiftDataShareDetailsTypeDef",
    "RequestDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionDestinationEntryTypeDef",
    "RevisionEntryTypeDef",
    "RevisionPublishedTypeDef",
    "RevokeRevisionRequestTypeDef",
    "RevokeRevisionResponseTypeDef",
    "S3DataAccessAssetSourceEntryOutputTypeDef",
    "S3DataAccessAssetSourceEntryTypeDef",
    "S3DataAccessAssetSourceEntryUnionTypeDef",
    "S3DataAccessAssetTypeDef",
    "S3DataAccessDetailsTypeDef",
    "S3SnapshotAssetTypeDef",
    "SchemaChangeDetailsTypeDef",
    "SchemaChangeRequestDetailsTypeDef",
    "ScopeDetailsTypeDef",
    "SendApiAssetRequestTypeDef",
    "SendApiAssetResponseTypeDef",
    "SendDataSetNotificationRequestTypeDef",
    "StartJobRequestTypeDef",
    "TableLFTagPolicyAndPermissionsOutputTypeDef",
    "TableLFTagPolicyAndPermissionsTypeDef",
    "TableLFTagPolicyAndPermissionsUnionTypeDef",
    "TableLFTagPolicyTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAssetRequestTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDataSetRequestTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateEventActionRequestTypeDef",
    "UpdateEventActionResponseTypeDef",
    "UpdateRevisionRequestTypeDef",
    "UpdateRevisionResponseTypeDef",
)

class AcceptDataGrantRequestTypeDef(TypedDict):
    DataGrantArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ApiGatewayApiAssetTypeDef(TypedDict):
    ApiDescription: NotRequired[str]
    ApiEndpoint: NotRequired[str]
    ApiId: NotRequired[str]
    ApiKey: NotRequired[str]
    ApiName: NotRequired[str]
    ApiSpecificationDownloadUrl: NotRequired[str]
    ApiSpecificationDownloadUrlExpiresAt: NotRequired[datetime]
    ProtocolType: NotRequired[Literal["REST"]]
    Stage: NotRequired[str]

class AssetDestinationEntryTypeDef(TypedDict):
    AssetId: str
    Bucket: str
    Key: NotRequired[str]

class RedshiftDataShareAssetTypeDef(TypedDict):
    Arn: str

class S3SnapshotAssetTypeDef(TypedDict):
    Size: float

class AssetSourceEntryTypeDef(TypedDict):
    Bucket: str
    Key: str

class AutoExportRevisionDestinationEntryTypeDef(TypedDict):
    Bucket: str
    KeyPattern: NotRequired[str]

ExportServerSideEncryptionTypeDef = TypedDict(
    "ExportServerSideEncryptionTypeDef",
    {
        "Type": ServerSideEncryptionTypesType,
        "KmsKeyArn": NotRequired[str],
    },
)

class CancelJobRequestTypeDef(TypedDict):
    JobId: str

TimestampTypeDef = Union[datetime, str]

class CreateDataSetRequestTypeDef(TypedDict):
    AssetType: AssetTypeType
    Description: str
    Name: str
    Tags: NotRequired[Mapping[str, str]]

class OriginDetailsTypeDef(TypedDict):
    ProductId: NotRequired[str]
    DataGrantId: NotRequired[str]

class CreateRevisionRequestTypeDef(TypedDict):
    DataSetId: str
    Comment: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class DataGrantSummaryEntryTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    AcceptanceState: DataGrantAcceptanceStateType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    AcceptedAt: NotRequired[datetime]
    EndsAt: NotRequired[datetime]

class LFTagOutputTypeDef(TypedDict):
    TagKey: str
    TagValues: List[str]

class LFTagTypeDef(TypedDict):
    TagKey: str
    TagValues: Sequence[str]

class DeleteAssetRequestTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str

class DeleteDataGrantRequestTypeDef(TypedDict):
    DataGrantId: str

class DeleteDataSetRequestTypeDef(TypedDict):
    DataSetId: str

class DeleteEventActionRequestTypeDef(TypedDict):
    EventActionId: str

class DeleteRevisionRequestTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str

class ImportAssetFromSignedUrlJobErrorDetailsTypeDef(TypedDict):
    AssetName: str

class RevisionPublishedTypeDef(TypedDict):
    DataSetId: str

class ExportAssetToSignedUrlRequestDetailsTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str

class ExportAssetToSignedUrlResponseDetailsTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str
    SignedUrl: NotRequired[str]
    SignedUrlExpiresAt: NotRequired[datetime]

class RevisionDestinationEntryTypeDef(TypedDict):
    Bucket: str
    RevisionId: str
    KeyPattern: NotRequired[str]

class GetAssetRequestTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str

class GetDataGrantRequestTypeDef(TypedDict):
    DataGrantId: str

class GetDataSetRequestTypeDef(TypedDict):
    DataSetId: str

class GetEventActionRequestTypeDef(TypedDict):
    EventActionId: str

class GetJobRequestTypeDef(TypedDict):
    JobId: str

class GetReceivedDataGrantRequestTypeDef(TypedDict):
    DataGrantArn: str

class GetRevisionRequestTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str

class ImportAssetFromApiGatewayApiRequestDetailsTypeDef(TypedDict):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    DataSetId: str
    ProtocolType: Literal["REST"]
    RevisionId: str
    Stage: str
    ApiDescription: NotRequired[str]
    ApiKey: NotRequired[str]

class ImportAssetFromApiGatewayApiResponseDetailsTypeDef(TypedDict):
    ApiId: str
    ApiName: str
    ApiSpecificationMd5Hash: str
    ApiSpecificationUploadUrl: str
    ApiSpecificationUploadUrlExpiresAt: datetime
    DataSetId: str
    ProtocolType: Literal["REST"]
    RevisionId: str
    Stage: str
    ApiDescription: NotRequired[str]
    ApiKey: NotRequired[str]

class ImportAssetFromSignedUrlRequestDetailsTypeDef(TypedDict):
    AssetName: str
    DataSetId: str
    Md5Hash: str
    RevisionId: str

class ImportAssetFromSignedUrlResponseDetailsTypeDef(TypedDict):
    AssetName: str
    DataSetId: str
    RevisionId: str
    Md5Hash: NotRequired[str]
    SignedUrl: NotRequired[str]
    SignedUrlExpiresAt: NotRequired[datetime]

class RedshiftDataShareAssetSourceEntryTypeDef(TypedDict):
    DataShareArn: str

class KmsKeyToGrantTypeDef(TypedDict):
    KmsKeyArn: str

class LakeFormationTagPolicyDetailsTypeDef(TypedDict):
    Database: NotRequired[str]
    Table: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDataGrantsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDataSetRevisionsRequestTypeDef(TypedDict):
    DataSetId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RevisionEntryTypeDef(TypedDict):
    Arn: str
    CreatedAt: datetime
    DataSetId: str
    Id: str
    UpdatedAt: datetime
    Comment: NotRequired[str]
    Finalized: NotRequired[bool]
    SourceId: NotRequired[str]
    RevocationComment: NotRequired[str]
    Revoked: NotRequired[bool]
    RevokedAt: NotRequired[datetime]

class ListDataSetsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Origin: NotRequired[str]

class ListEventActionsRequestTypeDef(TypedDict):
    EventSourceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListJobsRequestTypeDef(TypedDict):
    DataSetId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    RevisionId: NotRequired[str]

class ListReceivedDataGrantsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AcceptanceState: NotRequired[Sequence[AcceptanceStateFilterValueType]]

class ReceivedDataGrantSummariesEntryTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    AcceptanceState: DataGrantAcceptanceStateType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    AcceptedAt: NotRequired[datetime]
    EndsAt: NotRequired[datetime]

class ListRevisionAssetsRequestTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RedshiftDataShareDetailsTypeDef(TypedDict):
    Arn: str
    Database: str
    Function: NotRequired[str]
    Table: NotRequired[str]
    Schema: NotRequired[str]
    View: NotRequired[str]

class RevokeRevisionRequestTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str
    RevocationComment: str

class S3DataAccessDetailsTypeDef(TypedDict):
    KeyPrefixes: NotRequired[Sequence[str]]
    Keys: NotRequired[Sequence[str]]

SchemaChangeDetailsTypeDef = TypedDict(
    "SchemaChangeDetailsTypeDef",
    {
        "Name": str,
        "Type": SchemaChangeTypeType,
        "Description": NotRequired[str],
    },
)

class SendApiAssetRequestTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str
    Body: NotRequired[str]
    QueryStringParameters: NotRequired[Mapping[str, str]]
    RequestHeaders: NotRequired[Mapping[str, str]]
    Method: NotRequired[str]
    Path: NotRequired[str]

class StartJobRequestTypeDef(TypedDict):
    JobId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAssetRequestTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    Name: str
    RevisionId: str

class UpdateDataSetRequestTypeDef(TypedDict):
    DataSetId: str
    Description: NotRequired[str]
    Name: NotRequired[str]

class UpdateRevisionRequestTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str
    Comment: NotRequired[str]
    Finalized: NotRequired[bool]

class AcceptDataGrantResponseTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataGrantResponseTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRevisionResponseTypeDef(TypedDict):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataGrantResponseTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    SourceDataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReceivedDataGrantResponseTypeDef(TypedDict):
    Name: str
    SenderPrincipal: str
    ReceiverPrincipal: str
    Description: str
    AcceptanceState: DataGrantAcceptanceStateType
    AcceptedAt: datetime
    EndsAt: datetime
    GrantDistributionScope: GrantDistributionScopeType
    DataSetId: str
    Id: str
    Arn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevisionResponseTypeDef(TypedDict):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeRevisionResponseTypeDef(TypedDict):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SendApiAssetResponseTypeDef(TypedDict):
    Body: str
    ResponseHeaders: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRevisionResponseTypeDef(TypedDict):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    UpdatedAt: datetime
    RevocationComment: str
    Revoked: bool
    RevokedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ImportAssetsFromS3RequestDetailsTypeDef(TypedDict):
    AssetSources: Sequence[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromS3ResponseDetailsTypeDef(TypedDict):
    AssetSources: List[AssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class AutoExportRevisionToS3RequestDetailsTypeDef(TypedDict):
    RevisionDestination: AutoExportRevisionDestinationEntryTypeDef
    Encryption: NotRequired[ExportServerSideEncryptionTypeDef]

class ExportAssetsToS3RequestDetailsTypeDef(TypedDict):
    AssetDestinations: Sequence[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: NotRequired[ExportServerSideEncryptionTypeDef]

class ExportAssetsToS3ResponseDetailsTypeDef(TypedDict):
    AssetDestinations: List[AssetDestinationEntryTypeDef]
    DataSetId: str
    RevisionId: str
    Encryption: NotRequired[ExportServerSideEncryptionTypeDef]

class CreateDataGrantRequestTypeDef(TypedDict):
    Name: str
    GrantDistributionScope: GrantDistributionScopeType
    ReceiverPrincipal: str
    SourceDataSetId: str
    EndsAt: NotRequired[TimestampTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class DataUpdateRequestDetailsTypeDef(TypedDict):
    DataUpdatedAt: NotRequired[TimestampTypeDef]

class DeprecationRequestDetailsTypeDef(TypedDict):
    DeprecationAt: TimestampTypeDef

class CreateDataSetResponseTypeDef(TypedDict):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DataSetEntryTypeDef(TypedDict):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    UpdatedAt: datetime
    OriginDetails: NotRequired[OriginDetailsTypeDef]
    SourceId: NotRequired[str]

class GetDataSetResponseTypeDef(TypedDict):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSetResponseTypeDef(TypedDict):
    Arn: str
    AssetType: AssetTypeType
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: OriginType
    OriginDetails: OriginDetailsTypeDef
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataGrantsResponseTypeDef(TypedDict):
    DataGrantSummaries: List[DataGrantSummaryEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DatabaseLFTagPolicyAndPermissionsOutputTypeDef(TypedDict):
    Expression: List[LFTagOutputTypeDef]
    Permissions: List[Literal["DESCRIBE"]]

class DatabaseLFTagPolicyTypeDef(TypedDict):
    Expression: List[LFTagOutputTypeDef]

class TableLFTagPolicyAndPermissionsOutputTypeDef(TypedDict):
    Expression: List[LFTagOutputTypeDef]
    Permissions: List[TableTagPolicyLFPermissionType]

class TableLFTagPolicyTypeDef(TypedDict):
    Expression: List[LFTagOutputTypeDef]

class DatabaseLFTagPolicyAndPermissionsTypeDef(TypedDict):
    Expression: Sequence[LFTagTypeDef]
    Permissions: Sequence[Literal["DESCRIBE"]]

LFTagUnionTypeDef = Union[LFTagTypeDef, LFTagOutputTypeDef]

class DetailsTypeDef(TypedDict):
    ImportAssetFromSignedUrlJobErrorDetails: NotRequired[
        ImportAssetFromSignedUrlJobErrorDetailsTypeDef
    ]
    ImportAssetsFromS3JobErrorDetails: NotRequired[List[AssetSourceEntryTypeDef]]

class EventTypeDef(TypedDict):
    RevisionPublished: NotRequired[RevisionPublishedTypeDef]

class ExportRevisionsToS3RequestDetailsTypeDef(TypedDict):
    DataSetId: str
    RevisionDestinations: Sequence[RevisionDestinationEntryTypeDef]
    Encryption: NotRequired[ExportServerSideEncryptionTypeDef]

class ExportRevisionsToS3ResponseDetailsTypeDef(TypedDict):
    DataSetId: str
    RevisionDestinations: List[RevisionDestinationEntryTypeDef]
    Encryption: NotRequired[ExportServerSideEncryptionTypeDef]
    EventActionArn: NotRequired[str]

class ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef(TypedDict):
    AssetSources: Sequence[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef(TypedDict):
    AssetSources: List[RedshiftDataShareAssetSourceEntryTypeDef]
    DataSetId: str
    RevisionId: str

class S3DataAccessAssetSourceEntryOutputTypeDef(TypedDict):
    Bucket: str
    KeyPrefixes: NotRequired[List[str]]
    Keys: NotRequired[List[str]]
    KmsKeysToGrant: NotRequired[List[KmsKeyToGrantTypeDef]]

class S3DataAccessAssetSourceEntryTypeDef(TypedDict):
    Bucket: str
    KeyPrefixes: NotRequired[Sequence[str]]
    Keys: NotRequired[Sequence[str]]
    KmsKeysToGrant: NotRequired[Sequence[KmsKeyToGrantTypeDef]]

class S3DataAccessAssetTypeDef(TypedDict):
    Bucket: str
    KeyPrefixes: NotRequired[List[str]]
    Keys: NotRequired[List[str]]
    S3AccessPointAlias: NotRequired[str]
    S3AccessPointArn: NotRequired[str]
    KmsKeysToGrant: NotRequired[List[KmsKeyToGrantTypeDef]]

class ListDataGrantsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetRevisionsRequestPaginateTypeDef(TypedDict):
    DataSetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetsRequestPaginateTypeDef(TypedDict):
    Origin: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventActionsRequestPaginateTypeDef(TypedDict):
    EventSourceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestPaginateTypeDef(TypedDict):
    DataSetId: NotRequired[str]
    RevisionId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReceivedDataGrantsRequestPaginateTypeDef(TypedDict):
    AcceptanceState: NotRequired[Sequence[AcceptanceStateFilterValueType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRevisionAssetsRequestPaginateTypeDef(TypedDict):
    DataSetId: str
    RevisionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSetRevisionsResponseTypeDef(TypedDict):
    Revisions: List[RevisionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReceivedDataGrantsResponseTypeDef(TypedDict):
    DataGrantSummaries: List[ReceivedDataGrantSummariesEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ScopeDetailsTypeDef(TypedDict):
    LakeFormationTagPolicies: NotRequired[Sequence[LakeFormationTagPolicyDetailsTypeDef]]
    RedshiftDataShares: NotRequired[Sequence[RedshiftDataShareDetailsTypeDef]]
    S3DataAccesses: NotRequired[Sequence[S3DataAccessDetailsTypeDef]]

class SchemaChangeRequestDetailsTypeDef(TypedDict):
    SchemaChangeAt: TimestampTypeDef
    Changes: NotRequired[Sequence[SchemaChangeDetailsTypeDef]]

class ActionTypeDef(TypedDict):
    ExportRevisionToS3: NotRequired[AutoExportRevisionToS3RequestDetailsTypeDef]

class ListDataSetsResponseTypeDef(TypedDict):
    DataSets: List[DataSetEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef(TypedDict):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: NotRequired[DatabaseLFTagPolicyAndPermissionsOutputTypeDef]
    Table: NotRequired[TableLFTagPolicyAndPermissionsOutputTypeDef]

class LFResourceDetailsTypeDef(TypedDict):
    Database: NotRequired[DatabaseLFTagPolicyTypeDef]
    Table: NotRequired[TableLFTagPolicyTypeDef]

DatabaseLFTagPolicyAndPermissionsUnionTypeDef = Union[
    DatabaseLFTagPolicyAndPermissionsTypeDef, DatabaseLFTagPolicyAndPermissionsOutputTypeDef
]

class TableLFTagPolicyAndPermissionsTypeDef(TypedDict):
    Expression: Sequence[LFTagUnionTypeDef]
    Permissions: Sequence[TableTagPolicyLFPermissionType]

class JobErrorTypeDef(TypedDict):
    Code: CodeType
    Message: str
    Details: NotRequired[DetailsTypeDef]
    LimitName: NotRequired[JobErrorLimitNameType]
    LimitValue: NotRequired[float]
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[JobErrorResourceTypesType]

class CreateS3DataAccessFromS3BucketResponseDetailsTypeDef(TypedDict):
    AssetSource: S3DataAccessAssetSourceEntryOutputTypeDef
    DataSetId: str
    RevisionId: str

S3DataAccessAssetSourceEntryUnionTypeDef = Union[
    S3DataAccessAssetSourceEntryTypeDef, S3DataAccessAssetSourceEntryOutputTypeDef
]

class NotificationDetailsTypeDef(TypedDict):
    DataUpdate: NotRequired[DataUpdateRequestDetailsTypeDef]
    Deprecation: NotRequired[DeprecationRequestDetailsTypeDef]
    SchemaChange: NotRequired[SchemaChangeRequestDetailsTypeDef]

class CreateEventActionRequestTypeDef(TypedDict):
    Action: ActionTypeDef
    Event: EventTypeDef

class CreateEventActionResponseTypeDef(TypedDict):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EventActionEntryTypeDef(TypedDict):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime

class GetEventActionResponseTypeDef(TypedDict):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventActionRequestTypeDef(TypedDict):
    EventActionId: str
    Action: NotRequired[ActionTypeDef]

class UpdateEventActionResponseTypeDef(TypedDict):
    Action: ActionTypeDef
    Arn: str
    CreatedAt: datetime
    Event: EventTypeDef
    Id: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LFTagPolicyDetailsTypeDef(TypedDict):
    CatalogId: str
    ResourceType: LFResourceTypeType
    ResourceDetails: LFResourceDetailsTypeDef

TableLFTagPolicyAndPermissionsUnionTypeDef = Union[
    TableLFTagPolicyAndPermissionsTypeDef, TableLFTagPolicyAndPermissionsOutputTypeDef
]

class ResponseDetailsTypeDef(TypedDict):
    ExportAssetToSignedUrl: NotRequired[ExportAssetToSignedUrlResponseDetailsTypeDef]
    ExportAssetsToS3: NotRequired[ExportAssetsToS3ResponseDetailsTypeDef]
    ExportRevisionsToS3: NotRequired[ExportRevisionsToS3ResponseDetailsTypeDef]
    ImportAssetFromSignedUrl: NotRequired[ImportAssetFromSignedUrlResponseDetailsTypeDef]
    ImportAssetsFromS3: NotRequired[ImportAssetsFromS3ResponseDetailsTypeDef]
    ImportAssetsFromRedshiftDataShares: NotRequired[
        ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef
    ]
    ImportAssetFromApiGatewayApi: NotRequired[ImportAssetFromApiGatewayApiResponseDetailsTypeDef]
    CreateS3DataAccessFromS3Bucket: NotRequired[
        CreateS3DataAccessFromS3BucketResponseDetailsTypeDef
    ]
    ImportAssetsFromLakeFormationTagPolicy: NotRequired[
        ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef
    ]

class CreateS3DataAccessFromS3BucketRequestDetailsTypeDef(TypedDict):
    AssetSource: S3DataAccessAssetSourceEntryUnionTypeDef
    DataSetId: str
    RevisionId: str

SendDataSetNotificationRequestTypeDef = TypedDict(
    "SendDataSetNotificationRequestTypeDef",
    {
        "DataSetId": str,
        "Type": NotificationTypeType,
        "Scope": NotRequired[ScopeDetailsTypeDef],
        "ClientToken": NotRequired[str],
        "Comment": NotRequired[str],
        "Details": NotRequired[NotificationDetailsTypeDef],
    },
)

class ListEventActionsResponseTypeDef(TypedDict):
    EventActions: List[EventActionEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LakeFormationDataPermissionDetailsTypeDef(TypedDict):
    LFTagPolicy: NotRequired[LFTagPolicyDetailsTypeDef]

class ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef(TypedDict):
    CatalogId: str
    RoleArn: str
    DataSetId: str
    RevisionId: str
    Database: NotRequired[DatabaseLFTagPolicyAndPermissionsUnionTypeDef]
    Table: NotRequired[TableLFTagPolicyAndPermissionsUnionTypeDef]

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Errors": List[JobErrorTypeDef],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Errors": List[JobErrorTypeDef],
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobEntryTypeDef = TypedDict(
    "JobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ResponseDetailsTypeDef,
        "Id": str,
        "State": StateType,
        "Type": TypeType,
        "UpdatedAt": datetime,
        "Errors": NotRequired[List[JobErrorTypeDef]],
    },
)

class LakeFormationDataPermissionAssetTypeDef(TypedDict):
    LakeFormationDataPermissionDetails: LakeFormationDataPermissionDetailsTypeDef
    LakeFormationDataPermissionType: Literal["LFTagPolicy"]
    Permissions: List[LFPermissionType]
    RoleArn: NotRequired[str]

class RequestDetailsTypeDef(TypedDict):
    ExportAssetToSignedUrl: NotRequired[ExportAssetToSignedUrlRequestDetailsTypeDef]
    ExportAssetsToS3: NotRequired[ExportAssetsToS3RequestDetailsTypeDef]
    ExportRevisionsToS3: NotRequired[ExportRevisionsToS3RequestDetailsTypeDef]
    ImportAssetFromSignedUrl: NotRequired[ImportAssetFromSignedUrlRequestDetailsTypeDef]
    ImportAssetsFromS3: NotRequired[ImportAssetsFromS3RequestDetailsTypeDef]
    ImportAssetsFromRedshiftDataShares: NotRequired[
        ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef
    ]
    ImportAssetFromApiGatewayApi: NotRequired[ImportAssetFromApiGatewayApiRequestDetailsTypeDef]
    CreateS3DataAccessFromS3Bucket: NotRequired[CreateS3DataAccessFromS3BucketRequestDetailsTypeDef]
    ImportAssetsFromLakeFormationTagPolicy: NotRequired[
        ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef
    ]

class ListJobsResponseTypeDef(TypedDict):
    Jobs: List[JobEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssetDetailsTypeDef(TypedDict):
    S3SnapshotAsset: NotRequired[S3SnapshotAssetTypeDef]
    RedshiftDataShareAsset: NotRequired[RedshiftDataShareAssetTypeDef]
    ApiGatewayApiAsset: NotRequired[ApiGatewayApiAssetTypeDef]
    S3DataAccessAsset: NotRequired[S3DataAccessAssetTypeDef]
    LakeFormationDataPermissionAsset: NotRequired[LakeFormationDataPermissionAssetTypeDef]

CreateJobRequestTypeDef = TypedDict(
    "CreateJobRequestTypeDef",
    {
        "Details": RequestDetailsTypeDef,
        "Type": TypeType,
    },
)

class AssetEntryTypeDef(TypedDict):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    UpdatedAt: datetime
    SourceId: NotRequired[str]

class GetAssetResponseTypeDef(TypedDict):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssetResponseTypeDef(TypedDict):
    Arn: str
    AssetDetails: AssetDetailsTypeDef
    AssetType: AssetTypeType
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListRevisionAssetsResponseTypeDef(TypedDict):
    Assets: List[AssetEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
