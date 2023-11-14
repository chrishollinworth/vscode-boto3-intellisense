"""
Type annotations for signer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/literals.html)

Usage::

    ```python
    from mypy_boto3_signer.literals import CategoryType

    data: CategoryType = "AWSIoT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CategoryType",
    "EncryptionAlgorithmType",
    "HashAlgorithmType",
    "ImageFormatType",
    "ListSigningJobsPaginatorName",
    "ListSigningPlatformsPaginatorName",
    "ListSigningProfilesPaginatorName",
    "SigningProfileStatusType",
    "SigningStatusType",
    "SuccessfulSigningJobWaiterName",
    "ValidityTypeType",
)

CategoryType = Literal["AWSIoT"]
EncryptionAlgorithmType = Literal["ECDSA", "RSA"]
HashAlgorithmType = Literal["SHA1", "SHA256"]
ImageFormatType = Literal["JSON", "JSONDetached", "JSONEmbedded"]
ListSigningJobsPaginatorName = Literal["list_signing_jobs"]
ListSigningPlatformsPaginatorName = Literal["list_signing_platforms"]
ListSigningProfilesPaginatorName = Literal["list_signing_profiles"]
SigningProfileStatusType = Literal["Active", "Canceled", "Revoked"]
SigningStatusType = Literal["Failed", "InProgress", "Succeeded"]
SuccessfulSigningJobWaiterName = Literal["successful_signing_job"]
ValidityTypeType = Literal["DAYS", "MONTHS", "YEARS"]
