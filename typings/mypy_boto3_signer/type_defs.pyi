"""
Main interface for signer service type definitions.

Usage::

    ```python
    from mypy_boto3_signer.type_defs import EncryptionAlgorithmOptionsTypeDef

    data: EncryptionAlgorithmOptionsTypeDef = {...}
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
    "EncryptionAlgorithmOptionsTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SignedObjectTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningJobTypeDef",
    "SigningMaterialTypeDef",
    "SigningPlatformOverridesTypeDef",
    "SigningPlatformTypeDef",
    "SigningProfileTypeDef",
    "SourceTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileResponseTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutSigningProfileResponseTypeDef",
    "StartSigningJobResponseTypeDef",
    "WaiterConfigTypeDef",
)

EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef", {"bucketName": str, "prefix": str}, total=False
)

S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef", {"bucketName": str, "key": str}, total=False
)

S3SourceTypeDef = TypedDict("S3SourceTypeDef", {"bucketName": str, "key": str, "version": str})

SignedObjectTypeDef = TypedDict("SignedObjectTypeDef", {"s3": "S3SignedObjectTypeDef"}, total=False)

SigningConfigurationOverridesTypeDef = TypedDict(
    "SigningConfigurationOverridesTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
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
        "supportedFormats": List[Literal["JSON", "JSONEmbedded", "JSONDetached"]],
        "defaultFormat": Literal["JSON", "JSONEmbedded", "JSONDetached"],
    },
)

SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "createdAt": datetime,
        "status": Literal["InProgress", "Failed", "Succeeded"],
    },
    total=False,
)

SigningMaterialTypeDef = TypedDict("SigningMaterialTypeDef", {"certificateArn": str})

SigningPlatformOverridesTypeDef = TypedDict(
    "SigningPlatformOverridesTypeDef",
    {
        "signingConfiguration": "SigningConfigurationOverridesTypeDef",
        "signingImageFormat": Literal["JSON", "JSONEmbedded", "JSONDetached"],
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
    },
    total=False,
)

SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": str,
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

SourceTypeDef = TypedDict("SourceTypeDef", {"s3": "S3SourceTypeDef"}, total=False)

DescribeSigningJobResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "profileName": str,
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "requestedBy": str,
        "status": Literal["InProgress", "Failed", "Succeeded"],
        "statusReason": str,
        "signedObject": "SignedObjectTypeDef",
    },
    total=False,
)

DestinationTypeDef = TypedDict("DestinationTypeDef", {"s3": "S3DestinationTypeDef"}, total=False)

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
    },
    total=False,
)

GetSigningProfileResponseTypeDef = TypedDict(
    "GetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {"jobs": List["SigningJobTypeDef"], "nextToken": str},
    total=False,
)

ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {"platforms": List["SigningPlatformTypeDef"], "nextToken": str},
    total=False,
)

ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {"profiles": List["SigningProfileTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutSigningProfileResponseTypeDef = TypedDict(
    "PutSigningProfileResponseTypeDef", {"arn": str}, total=False
)

StartSigningJobResponseTypeDef = TypedDict(
    "StartSigningJobResponseTypeDef", {"jobId": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
