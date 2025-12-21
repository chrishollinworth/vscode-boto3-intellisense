"""
Type annotations for acm service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_acm.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    CertificateExportType,
    CertificateStatusType,
    CertificateTransparencyLoggingPreferenceType,
    CertificateTypeType,
    DomainStatusType,
    ExtendedKeyUsageNameType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyUsageNameType,
    RenewalEligibilityType,
    RenewalStatusType,
    RevocationReasonType,
    SortOrderType,
    ValidationMethodType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddTagsToCertificateRequestTypeDef",
    "BlobTypeDef",
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DeleteCertificateRequestTypeDef",
    "DescribeCertificateRequestTypeDef",
    "DescribeCertificateRequestWaitTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "DomainValidationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExportCertificateRequestTypeDef",
    "ExportCertificateResponseTypeDef",
    "ExtendedKeyUsageTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetCertificateRequestTypeDef",
    "GetCertificateResponseTypeDef",
    "HttpRedirectTypeDef",
    "ImportCertificateRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificatesRequestPaginateTypeDef",
    "ListCertificatesRequestTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateRequestTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountConfigurationRequestTypeDef",
    "RemoveTagsFromCertificateRequestTypeDef",
    "RenewCertificateRequestTypeDef",
    "RenewalSummaryTypeDef",
    "RequestCertificateRequestTypeDef",
    "RequestCertificateResponseTypeDef",
    "ResendValidationEmailRequestTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeCertificateRequestTypeDef",
    "RevokeCertificateResponseTypeDef",
    "TagTypeDef",
    "UpdateCertificateOptionsRequestTypeDef",
    "WaiterConfigTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CertificateOptionsTypeDef(TypedDict):
    CertificateTransparencyLoggingPreference: NotRequired[
        CertificateTransparencyLoggingPreferenceType
    ]
    Export: NotRequired[CertificateExportType]

class ExtendedKeyUsageTypeDef(TypedDict):
    Name: NotRequired[ExtendedKeyUsageNameType]
    OID: NotRequired[str]

class KeyUsageTypeDef(TypedDict):
    Name: NotRequired[KeyUsageNameType]

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
        "SubjectAlternativeNameSummaries": NotRequired[List[str]],
        "HasAdditionalSubjectAlternativeNames": NotRequired[bool],
        "Status": NotRequired[CertificateStatusType],
        "Type": NotRequired[CertificateTypeType],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
        "KeyUsages": NotRequired[List[KeyUsageNameType]],
        "ExtendedKeyUsages": NotRequired[List[ExtendedKeyUsageNameType]],
        "ExportOption": NotRequired[CertificateExportType],
        "InUse": NotRequired[bool],
        "Exported": NotRequired[bool],
        "RenewalEligibility": NotRequired[RenewalEligibilityType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "IssuedAt": NotRequired[datetime],
        "ImportedAt": NotRequired[datetime],
        "RevokedAt": NotRequired[datetime],
        "ManagedBy": NotRequired[Literal["CLOUDFRONT"]],
    },
)

class DeleteCertificateRequestTypeDef(TypedDict):
    CertificateArn: str

class DescribeCertificateRequestTypeDef(TypedDict):
    CertificateArn: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DomainValidationOptionTypeDef(TypedDict):
    DomainName: str
    ValidationDomain: str

class HttpRedirectTypeDef(TypedDict):
    RedirectFrom: NotRequired[str]
    RedirectTo: NotRequired[str]

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Name": str,
        "Type": Literal["CNAME"],
        "Value": str,
    },
)

class ExpiryEventsConfigurationTypeDef(TypedDict):
    DaysBeforeExpiry: NotRequired[int]

class FiltersTypeDef(TypedDict):
    extendedKeyUsage: NotRequired[Sequence[ExtendedKeyUsageNameType]]
    keyUsage: NotRequired[Sequence[KeyUsageNameType]]
    keyTypes: NotRequired[Sequence[KeyAlgorithmType]]
    exportOption: NotRequired[CertificateExportType]
    managedBy: NotRequired[Literal["CLOUDFRONT"]]

class GetCertificateRequestTypeDef(TypedDict):
    CertificateArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForCertificateRequestTypeDef(TypedDict):
    CertificateArn: str

class RenewCertificateRequestTypeDef(TypedDict):
    CertificateArn: str

class ResendValidationEmailRequestTypeDef(TypedDict):
    CertificateArn: str
    Domain: str
    ValidationDomain: str

class RevokeCertificateRequestTypeDef(TypedDict):
    CertificateArn: str
    RevocationReason: RevocationReasonType

class AddTagsToCertificateRequestTypeDef(TypedDict):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]

class RemoveTagsFromCertificateRequestTypeDef(TypedDict):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]

class ExportCertificateRequestTypeDef(TypedDict):
    CertificateArn: str
    Passphrase: BlobTypeDef

class ImportCertificateRequestTypeDef(TypedDict):
    Certificate: BlobTypeDef
    PrivateKey: BlobTypeDef
    CertificateArn: NotRequired[str]
    CertificateChain: NotRequired[BlobTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateCertificateOptionsRequestTypeDef(TypedDict):
    CertificateArn: str
    Options: CertificateOptionsTypeDef

class DescribeCertificateRequestWaitTypeDef(TypedDict):
    CertificateArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportCertificateResponseTypeDef(TypedDict):
    Certificate: str
    CertificateChain: str
    PrivateKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateResponseTypeDef(TypedDict):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(TypedDict):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesResponseTypeDef(TypedDict):
    CertificateSummaryList: List[CertificateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForCertificateResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestCertificateResponseTypeDef(TypedDict):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeCertificateResponseTypeDef(TypedDict):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestCertificateRequestTypeDef(TypedDict):
    DomainName: str
    ValidationMethod: NotRequired[ValidationMethodType]
    SubjectAlternativeNames: NotRequired[Sequence[str]]
    IdempotencyToken: NotRequired[str]
    DomainValidationOptions: NotRequired[Sequence[DomainValidationOptionTypeDef]]
    Options: NotRequired[CertificateOptionsTypeDef]
    CertificateAuthorityArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KeyAlgorithm: NotRequired[KeyAlgorithmType]
    ManagedBy: NotRequired[Literal["CLOUDFRONT"]]

class DomainValidationTypeDef(TypedDict):
    DomainName: str
    ValidationEmails: NotRequired[List[str]]
    ValidationDomain: NotRequired[str]
    ValidationStatus: NotRequired[DomainStatusType]
    ResourceRecord: NotRequired[ResourceRecordTypeDef]
    HttpRedirect: NotRequired[HttpRedirectTypeDef]
    ValidationMethod: NotRequired[ValidationMethodType]

class GetAccountConfigurationResponseTypeDef(TypedDict):
    ExpiryEvents: ExpiryEventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountConfigurationRequestTypeDef(TypedDict):
    IdempotencyToken: str
    ExpiryEvents: NotRequired[ExpiryEventsConfigurationTypeDef]

class ListCertificatesRequestTypeDef(TypedDict):
    CertificateStatuses: NotRequired[Sequence[CertificateStatusType]]
    Includes: NotRequired[FiltersTypeDef]
    NextToken: NotRequired[str]
    MaxItems: NotRequired[int]
    SortBy: NotRequired[Literal["CREATED_AT"]]
    SortOrder: NotRequired[SortOrderType]

class ListCertificatesRequestPaginateTypeDef(TypedDict):
    CertificateStatuses: NotRequired[Sequence[CertificateStatusType]]
    Includes: NotRequired[FiltersTypeDef]
    SortBy: NotRequired[Literal["CREATED_AT"]]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class RenewalSummaryTypeDef(TypedDict):
    RenewalStatus: RenewalStatusType
    DomainValidationOptions: List[DomainValidationTypeDef]
    UpdatedAt: datetime
    RenewalStatusReason: NotRequired[FailureReasonType]

CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "ManagedBy": NotRequired[Literal["CLOUDFRONT"]],
        "DomainValidationOptions": NotRequired[List[DomainValidationTypeDef]],
        "Serial": NotRequired[str],
        "Subject": NotRequired[str],
        "Issuer": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "IssuedAt": NotRequired[datetime],
        "ImportedAt": NotRequired[datetime],
        "Status": NotRequired[CertificateStatusType],
        "RevokedAt": NotRequired[datetime],
        "RevocationReason": NotRequired[RevocationReasonType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
        "SignatureAlgorithm": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "FailureReason": NotRequired[FailureReasonType],
        "Type": NotRequired[CertificateTypeType],
        "RenewalSummary": NotRequired[RenewalSummaryTypeDef],
        "KeyUsages": NotRequired[List[KeyUsageTypeDef]],
        "ExtendedKeyUsages": NotRequired[List[ExtendedKeyUsageTypeDef]],
        "CertificateAuthorityArn": NotRequired[str],
        "RenewalEligibility": NotRequired[RenewalEligibilityType],
        "Options": NotRequired[CertificateOptionsTypeDef],
    },
)

class DescribeCertificateResponseTypeDef(TypedDict):
    Certificate: CertificateDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
