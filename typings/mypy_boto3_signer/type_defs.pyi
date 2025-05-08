"""
Type annotations for signer service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionRequestTypeDef

    data: AddProfilePermissionRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionAlgorithmType,
    HashAlgorithmType,
    ImageFormatType,
    SigningProfileStatusType,
    SigningStatusType,
    ValidityTypeType,
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
    "AddProfilePermissionRequestTypeDef",
    "AddProfilePermissionResponseTypeDef",
    "BlobTypeDef",
    "CancelSigningProfileRequestTypeDef",
    "DescribeSigningJobRequestTypeDef",
    "DescribeSigningJobRequestWaitTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetRevocationStatusRequestTypeDef",
    "GetRevocationStatusResponseTypeDef",
    "GetSigningPlatformRequestTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileRequestTypeDef",
    "GetSigningProfileResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsRequestTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsRequestPaginateTypeDef",
    "ListSigningJobsRequestTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsRequestPaginateTypeDef",
    "ListSigningPlatformsRequestTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesRequestPaginateTypeDef",
    "ListSigningProfilesRequestTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileRequestTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionRequestTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSignatureRequestTypeDef",
    "RevokeSigningProfileRequestTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SignPayloadRequestTypeDef",
    "SignPayloadResponseTypeDef",
    "SignatureValidityPeriodTypeDef",
    "SignedObjectTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningJobRevocationRecordTypeDef",
    "SigningJobTypeDef",
    "SigningMaterialTypeDef",
    "SigningPlatformOverridesTypeDef",
    "SigningPlatformTypeDef",
    "SigningProfileRevocationRecordTypeDef",
    "SigningProfileTypeDef",
    "SourceTypeDef",
    "StartSigningJobRequestTypeDef",
    "StartSigningJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "WaiterConfigTypeDef",
)

class AddProfilePermissionRequestTypeDef(TypedDict):
    profileName: str
    action: str
    principal: str
    statementId: str
    profileVersion: NotRequired[str]
    revisionId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelSigningProfileRequestTypeDef(TypedDict):
    profileName: str

class DescribeSigningJobRequestTypeDef(TypedDict):
    jobId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class SigningJobRevocationRecordTypeDef(TypedDict):
    reason: NotRequired[str]
    revokedAt: NotRequired[datetime]
    revokedBy: NotRequired[str]

class SigningMaterialTypeDef(TypedDict):
    certificateArn: str

class S3DestinationTypeDef(TypedDict):
    bucketName: NotRequired[str]
    prefix: NotRequired[str]

class EncryptionAlgorithmOptionsTypeDef(TypedDict):
    allowedValues: List[EncryptionAlgorithmType]
    defaultValue: EncryptionAlgorithmType

TimestampTypeDef = Union[datetime, str]

class GetSigningPlatformRequestTypeDef(TypedDict):
    platformId: str

class SigningImageFormatTypeDef(TypedDict):
    supportedFormats: List[ImageFormatType]
    defaultFormat: ImageFormatType

class GetSigningProfileRequestTypeDef(TypedDict):
    profileName: str
    profileOwner: NotRequired[str]

SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef",
    {
        "value": NotRequired[int],
        "type": NotRequired[ValidityTypeType],
    },
)

class SigningProfileRevocationRecordTypeDef(TypedDict):
    revocationEffectiveFrom: NotRequired[datetime]
    revokedAt: NotRequired[datetime]
    revokedBy: NotRequired[str]

class HashAlgorithmOptionsTypeDef(TypedDict):
    allowedValues: List[HashAlgorithmType]
    defaultValue: HashAlgorithmType

class ListProfilePermissionsRequestTypeDef(TypedDict):
    profileName: str
    nextToken: NotRequired[str]

class PermissionTypeDef(TypedDict):
    action: NotRequired[str]
    principal: NotRequired[str]
    statementId: NotRequired[str]
    profileVersion: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSigningPlatformsRequestTypeDef(TypedDict):
    category: NotRequired[str]
    partner: NotRequired[str]
    target: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSigningProfilesRequestTypeDef(TypedDict):
    includeCanceled: NotRequired[bool]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    platformId: NotRequired[str]
    statuses: NotRequired[Sequence[SigningProfileStatusType]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RemoveProfilePermissionRequestTypeDef(TypedDict):
    profileName: str
    revisionId: str
    statementId: str

class RevokeSignatureRequestTypeDef(TypedDict):
    jobId: str
    reason: str
    jobOwner: NotRequired[str]

class S3SignedObjectTypeDef(TypedDict):
    bucketName: NotRequired[str]
    key: NotRequired[str]

class S3SourceTypeDef(TypedDict):
    bucketName: str
    key: str
    version: str

class SigningConfigurationOverridesTypeDef(TypedDict):
    encryptionAlgorithm: NotRequired[EncryptionAlgorithmType]
    hashAlgorithm: NotRequired[HashAlgorithmType]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class AddProfilePermissionResponseTypeDef(TypedDict):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRevocationStatusResponseTypeDef(TypedDict):
    revokedEntities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSigningProfileResponseTypeDef(TypedDict):
    arn: str
    profileVersion: str
    profileVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveProfilePermissionResponseTypeDef(TypedDict):
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadResponseTypeDef(TypedDict):
    jobId: str
    jobOwner: str
    metadata: Dict[str, str]
    signature: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class StartSigningJobResponseTypeDef(TypedDict):
    jobId: str
    jobOwner: str
    ResponseMetadata: ResponseMetadataTypeDef

class SignPayloadRequestTypeDef(TypedDict):
    profileName: str
    payload: BlobTypeDef
    payloadFormat: str
    profileOwner: NotRequired[str]

class DescribeSigningJobRequestWaitTypeDef(TypedDict):
    jobId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DestinationTypeDef(TypedDict):
    s3: NotRequired[S3DestinationTypeDef]

class GetRevocationStatusRequestTypeDef(TypedDict):
    signatureTimestamp: TimestampTypeDef
    platformId: str
    profileVersionArn: str
    jobArn: str
    certificateHashes: Sequence[str]

class ListSigningJobsRequestTypeDef(TypedDict):
    status: NotRequired[SigningStatusType]
    platformId: NotRequired[str]
    requestedBy: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    isRevoked: NotRequired[bool]
    signatureExpiresBefore: NotRequired[TimestampTypeDef]
    signatureExpiresAfter: NotRequired[TimestampTypeDef]
    jobInvoker: NotRequired[str]

class RevokeSigningProfileRequestTypeDef(TypedDict):
    profileName: str
    profileVersion: str
    reason: str
    effectiveTime: TimestampTypeDef

class SigningProfileTypeDef(TypedDict):
    profileName: NotRequired[str]
    profileVersion: NotRequired[str]
    profileVersionArn: NotRequired[str]
    signingMaterial: NotRequired[SigningMaterialTypeDef]
    signatureValidityPeriod: NotRequired[SignatureValidityPeriodTypeDef]
    platformId: NotRequired[str]
    platformDisplayName: NotRequired[str]
    signingParameters: NotRequired[Dict[str, str]]
    status: NotRequired[SigningProfileStatusType]
    arn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class SigningConfigurationTypeDef(TypedDict):
    encryptionAlgorithmOptions: EncryptionAlgorithmOptionsTypeDef
    hashAlgorithmOptions: HashAlgorithmOptionsTypeDef

class ListProfilePermissionsResponseTypeDef(TypedDict):
    revisionId: str
    policySizeBytes: int
    permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSigningJobsRequestPaginateTypeDef(TypedDict):
    status: NotRequired[SigningStatusType]
    platformId: NotRequired[str]
    requestedBy: NotRequired[str]
    isRevoked: NotRequired[bool]
    signatureExpiresBefore: NotRequired[TimestampTypeDef]
    signatureExpiresAfter: NotRequired[TimestampTypeDef]
    jobInvoker: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSigningPlatformsRequestPaginateTypeDef(TypedDict):
    category: NotRequired[str]
    partner: NotRequired[str]
    target: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSigningProfilesRequestPaginateTypeDef(TypedDict):
    includeCanceled: NotRequired[bool]
    platformId: NotRequired[str]
    statuses: NotRequired[Sequence[SigningProfileStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SignedObjectTypeDef(TypedDict):
    s3: NotRequired[S3SignedObjectTypeDef]

class SourceTypeDef(TypedDict):
    s3: NotRequired[S3SourceTypeDef]

class SigningPlatformOverridesTypeDef(TypedDict):
    signingConfiguration: NotRequired[SigningConfigurationOverridesTypeDef]
    signingImageFormat: NotRequired[ImageFormatType]

class ListSigningProfilesResponseTypeDef(TypedDict):
    profiles: List[SigningProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetSigningPlatformResponseTypeDef(TypedDict):
    platformId: str
    displayName: str
    partner: str
    target: str
    category: Literal["AWSIoT"]
    signingConfiguration: SigningConfigurationTypeDef
    signingImageFormat: SigningImageFormatTypeDef
    maxSizeInMB: int
    revocationSupported: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SigningPlatformTypeDef(TypedDict):
    platformId: NotRequired[str]
    displayName: NotRequired[str]
    partner: NotRequired[str]
    target: NotRequired[str]
    category: NotRequired[Literal["AWSIoT"]]
    signingConfiguration: NotRequired[SigningConfigurationTypeDef]
    signingImageFormat: NotRequired[SigningImageFormatTypeDef]
    maxSizeInMB: NotRequired[int]
    revocationSupported: NotRequired[bool]

class SigningJobTypeDef(TypedDict):
    jobId: NotRequired[str]
    source: NotRequired[SourceTypeDef]
    signedObject: NotRequired[SignedObjectTypeDef]
    signingMaterial: NotRequired[SigningMaterialTypeDef]
    createdAt: NotRequired[datetime]
    status: NotRequired[SigningStatusType]
    isRevoked: NotRequired[bool]
    profileName: NotRequired[str]
    profileVersion: NotRequired[str]
    platformId: NotRequired[str]
    platformDisplayName: NotRequired[str]
    signatureExpiresAt: NotRequired[datetime]
    jobOwner: NotRequired[str]
    jobInvoker: NotRequired[str]

class StartSigningJobRequestTypeDef(TypedDict):
    source: SourceTypeDef
    destination: DestinationTypeDef
    profileName: str
    clientRequestToken: str
    profileOwner: NotRequired[str]

class DescribeSigningJobResponseTypeDef(TypedDict):
    jobId: str
    source: SourceTypeDef
    signingMaterial: SigningMaterialTypeDef
    platformId: str
    platformDisplayName: str
    profileName: str
    profileVersion: str
    overrides: SigningPlatformOverridesTypeDef
    signingParameters: Dict[str, str]
    createdAt: datetime
    completedAt: datetime
    signatureExpiresAt: datetime
    requestedBy: str
    status: SigningStatusType
    statusReason: str
    revocationRecord: SigningJobRevocationRecordTypeDef
    signedObject: SignedObjectTypeDef
    jobOwner: str
    jobInvoker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSigningProfileResponseTypeDef(TypedDict):
    profileName: str
    profileVersion: str
    profileVersionArn: str
    revocationRecord: SigningProfileRevocationRecordTypeDef
    signingMaterial: SigningMaterialTypeDef
    platformId: str
    platformDisplayName: str
    signatureValidityPeriod: SignatureValidityPeriodTypeDef
    overrides: SigningPlatformOverridesTypeDef
    signingParameters: Dict[str, str]
    status: SigningProfileStatusType
    statusReason: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSigningProfileRequestTypeDef(TypedDict):
    profileName: str
    platformId: str
    signingMaterial: NotRequired[SigningMaterialTypeDef]
    signatureValidityPeriod: NotRequired[SignatureValidityPeriodTypeDef]
    overrides: NotRequired[SigningPlatformOverridesTypeDef]
    signingParameters: NotRequired[Mapping[str, str]]
    tags: NotRequired[Mapping[str, str]]

class ListSigningPlatformsResponseTypeDef(TypedDict):
    platforms: List[SigningPlatformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSigningJobsResponseTypeDef(TypedDict):
    jobs: List[SigningJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
