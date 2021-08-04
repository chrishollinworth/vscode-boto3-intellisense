"""
Type annotations for signer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionRequestRequestTypeDef

    data: AddProfilePermissionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EncryptionAlgorithmType,
    HashAlgorithmType,
    ImageFormatType,
    SigningProfileStatusType,
    SigningStatusType,
    ValidityTypeType,
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
    "AddProfilePermissionRequestRequestTypeDef",
    "AddProfilePermissionResponseTypeDef",
    "CancelSigningProfileRequestRequestTypeDef",
    "DescribeSigningJobRequestRequestTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetSigningPlatformRequestRequestTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileRequestRequestTypeDef",
    "GetSigningProfileResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsRequestRequestTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsRequestRequestTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsRequestRequestTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesRequestRequestTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileRequestRequestTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionRequestRequestTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSignatureRequestRequestTypeDef",
    "RevokeSigningProfileRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
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
    "StartSigningJobRequestRequestTypeDef",
    "StartSigningJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddProfilePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredAddProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "action": str,
        "principal": str,
        "statementId": str,
    },
)
_OptionalAddProfilePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalAddProfilePermissionRequestRequestTypeDef",
    {
        "profileVersion": str,
        "revisionId": str,
    },
    total=False,
)

class AddProfilePermissionRequestRequestTypeDef(
    _RequiredAddProfilePermissionRequestRequestTypeDef,
    _OptionalAddProfilePermissionRequestRequestTypeDef,
):
    pass

AddProfilePermissionResponseTypeDef = TypedDict(
    "AddProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSigningProfileRequestRequestTypeDef = TypedDict(
    "CancelSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
    },
)

DescribeSigningJobRequestRequestTypeDef = TypedDict(
    "DescribeSigningJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeSigningJobResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "profileName": str,
        "profileVersion": str,
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "signatureExpiresAt": datetime,
        "requestedBy": str,
        "status": SigningStatusType,
        "statusReason": str,
        "revocationRecord": "SigningJobRevocationRecordTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "jobOwner": str,
        "jobInvoker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3": "S3DestinationTypeDef",
    },
    total=False,
)

EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[EncryptionAlgorithmType],
        "defaultValue": EncryptionAlgorithmType,
    },
)

GetSigningPlatformRequestRequestTypeDef = TypedDict(
    "GetSigningPlatformRequestRequestTypeDef",
    {
        "platformId": str,
    },
)

GetSigningPlatformResponseTypeDef = TypedDict(
    "GetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": "SigningConfigurationTypeDef",
        "signingImageFormat": "SigningImageFormatTypeDef",
        "maxSizeInMB": int,
        "revocationSupported": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSigningProfileRequestRequestTypeDef = TypedDict(
    "_RequiredGetSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
    },
)
_OptionalGetSigningProfileRequestRequestTypeDef = TypedDict(
    "_OptionalGetSigningProfileRequestRequestTypeDef",
    {
        "profileOwner": str,
    },
    total=False,
)

class GetSigningProfileRequestRequestTypeDef(
    _RequiredGetSigningProfileRequestRequestTypeDef, _OptionalGetSigningProfileRequestRequestTypeDef
):
    pass

GetSigningProfileResponseTypeDef = TypedDict(
    "GetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "revocationRecord": "SigningProfileRevocationRecordTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "statusReason": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[HashAlgorithmType],
        "defaultValue": HashAlgorithmType,
    },
)

_RequiredListProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProfilePermissionsRequestRequestTypeDef",
    {
        "profileName": str,
    },
)
_OptionalListProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProfilePermissionsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListProfilePermissionsRequestRequestTypeDef(
    _RequiredListProfilePermissionsRequestRequestTypeDef,
    _OptionalListProfilePermissionsRequestRequestTypeDef,
):
    pass

ListProfilePermissionsResponseTypeDef = TypedDict(
    "ListProfilePermissionsResponseTypeDef",
    {
        "revisionId": str,
        "policySizeBytes": int,
        "permissions": List["PermissionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningJobsRequestRequestTypeDef = TypedDict(
    "ListSigningJobsRequestRequestTypeDef",
    {
        "status": SigningStatusType,
        "platformId": str,
        "requestedBy": str,
        "maxResults": int,
        "nextToken": str,
        "isRevoked": bool,
        "signatureExpiresBefore": Union[datetime, str],
        "signatureExpiresAfter": Union[datetime, str],
        "jobInvoker": str,
    },
    total=False,
)

ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {
        "jobs": List["SigningJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningPlatformsRequestRequestTypeDef = TypedDict(
    "ListSigningPlatformsRequestRequestTypeDef",
    {
        "category": str,
        "partner": str,
        "target": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {
        "platforms": List["SigningPlatformTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningProfilesRequestRequestTypeDef = TypedDict(
    "ListSigningProfilesRequestRequestTypeDef",
    {
        "includeCanceled": bool,
        "maxResults": int,
        "nextToken": str,
        "platformId": str,
        "statuses": List[SigningProfileStatusType],
    },
    total=False,
)

ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {
        "profiles": List["SigningProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "action": str,
        "principal": str,
        "statementId": str,
        "profileVersion": str,
    },
    total=False,
)

_RequiredPutSigningProfileRequestRequestTypeDef = TypedDict(
    "_RequiredPutSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "platformId": str,
    },
)
_OptionalPutSigningProfileRequestRequestTypeDef = TypedDict(
    "_OptionalPutSigningProfileRequestRequestTypeDef",
    {
        "signingMaterial": "SigningMaterialTypeDef",
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class PutSigningProfileRequestRequestTypeDef(
    _RequiredPutSigningProfileRequestRequestTypeDef, _OptionalPutSigningProfileRequestRequestTypeDef
):
    pass

PutSigningProfileResponseTypeDef = TypedDict(
    "PutSigningProfileResponseTypeDef",
    {
        "arn": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveProfilePermissionRequestRequestTypeDef = TypedDict(
    "RemoveProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "revisionId": str,
        "statementId": str,
    },
)

RemoveProfilePermissionResponseTypeDef = TypedDict(
    "RemoveProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
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

_RequiredRevokeSignatureRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeSignatureRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)
_OptionalRevokeSignatureRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeSignatureRequestRequestTypeDef",
    {
        "jobOwner": str,
    },
    total=False,
)

class RevokeSignatureRequestRequestTypeDef(
    _RequiredRevokeSignatureRequestRequestTypeDef, _OptionalRevokeSignatureRequestRequestTypeDef
):
    pass

RevokeSigningProfileRequestRequestTypeDef = TypedDict(
    "RevokeSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "reason": str,
        "effectiveTime": Union[datetime, str],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": str,
        "prefix": str,
    },
    total=False,
)

S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
    total=False,
)

S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "bucketName": str,
        "key": str,
        "version": str,
    },
)

SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef",
    {
        "value": int,
        "type": ValidityTypeType,
    },
    total=False,
)

SignedObjectTypeDef = TypedDict(
    "SignedObjectTypeDef",
    {
        "s3": "S3SignedObjectTypeDef",
    },
    total=False,
)

SigningConfigurationOverridesTypeDef = TypedDict(
    "SigningConfigurationOverridesTypeDef",
    {
        "encryptionAlgorithm": EncryptionAlgorithmType,
        "hashAlgorithm": HashAlgorithmType,
    },
    total=False,
)

SigningConfigurationTypeDef = TypedDict(
    "SigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": "EncryptionAlgorithmOptionsTypeDef",
        "hashAlgorithmOptions": "HashAlgorithmOptionsTypeDef",
    },
)

SigningImageFormatTypeDef = TypedDict(
    "SigningImageFormatTypeDef",
    {
        "supportedFormats": List[ImageFormatType],
        "defaultFormat": ImageFormatType,
    },
)

SigningJobRevocationRecordTypeDef = TypedDict(
    "SigningJobRevocationRecordTypeDef",
    {
        "reason": str,
        "revokedAt": datetime,
        "revokedBy": str,
    },
    total=False,
)

SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "createdAt": datetime,
        "status": SigningStatusType,
        "isRevoked": bool,
        "profileName": str,
        "profileVersion": str,
        "platformId": str,
        "platformDisplayName": str,
        "signatureExpiresAt": datetime,
        "jobOwner": str,
        "jobInvoker": str,
    },
    total=False,
)

SigningMaterialTypeDef = TypedDict(
    "SigningMaterialTypeDef",
    {
        "certificateArn": str,
    },
)

SigningPlatformOverridesTypeDef = TypedDict(
    "SigningPlatformOverridesTypeDef",
    {
        "signingConfiguration": "SigningConfigurationOverridesTypeDef",
        "signingImageFormat": ImageFormatType,
    },
    total=False,
)

SigningPlatformTypeDef = TypedDict(
    "SigningPlatformTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": "SigningConfigurationTypeDef",
        "signingImageFormat": "SigningImageFormatTypeDef",
        "maxSizeInMB": int,
        "revocationSupported": bool,
    },
    total=False,
)

SigningProfileRevocationRecordTypeDef = TypedDict(
    "SigningProfileRevocationRecordTypeDef",
    {
        "revocationEffectiveFrom": datetime,
        "revokedAt": datetime,
        "revokedBy": str,
    },
    total=False,
)

SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "signingMaterial": "SigningMaterialTypeDef",
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3": "S3SourceTypeDef",
    },
    total=False,
)

_RequiredStartSigningJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartSigningJobRequestRequestTypeDef",
    {
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
        "profileName": str,
        "clientRequestToken": str,
    },
)
_OptionalStartSigningJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartSigningJobRequestRequestTypeDef",
    {
        "profileOwner": str,
    },
    total=False,
)

class StartSigningJobRequestRequestTypeDef(
    _RequiredStartSigningJobRequestRequestTypeDef, _OptionalStartSigningJobRequestRequestTypeDef
):
    pass

StartSigningJobResponseTypeDef = TypedDict(
    "StartSigningJobResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
