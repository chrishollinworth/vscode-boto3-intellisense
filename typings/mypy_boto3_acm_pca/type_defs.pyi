"""
Type annotations for acm-pca service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import CustomAttributeTypeDef

    data: CustomAttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    CertificateAuthorityUsageModeType,
    CrlTypeType,
    ExtendedKeyUsageTypeType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    S3ObjectAclType,
    SigningAlgorithmType,
    ValidityPeriodTypeType,
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
    "ASN1SubjectOutputTypeDef",
    "ASN1SubjectTypeDef",
    "ASN1SubjectUnionTypeDef",
    "AccessDescriptionOutputTypeDef",
    "AccessDescriptionTypeDef",
    "AccessMethodTypeDef",
    "ApiPassthroughTypeDef",
    "BlobTypeDef",
    "CertificateAuthorityConfigurationOutputTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityConfigurationUnionTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityAuditReportRequestTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityRequestTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "CreatePermissionRequestTypeDef",
    "CrlConfigurationTypeDef",
    "CrlDistributionPointExtensionConfigurationTypeDef",
    "CsrExtensionsOutputTypeDef",
    "CsrExtensionsTypeDef",
    "CustomAttributeTypeDef",
    "CustomExtensionTypeDef",
    "DeleteCertificateAuthorityRequestTypeDef",
    "DeletePermissionRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestWaitTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "DescribeCertificateAuthorityRequestTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "EdiPartyNameTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameOutputTypeDef",
    "GeneralNameTypeDef",
    "GeneralNameUnionTypeDef",
    "GetCertificateAuthorityCertificateRequestTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrRequestTypeDef",
    "GetCertificateAuthorityCsrRequestWaitTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateRequestTypeDef",
    "GetCertificateRequestWaitTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "ImportCertificateAuthorityCertificateRequestTypeDef",
    "IssueCertificateRequestTypeDef",
    "IssueCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificateAuthoritiesRequestPaginateTypeDef",
    "ListCertificateAuthoritiesRequestTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
    "ListPermissionsRequestPaginateTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsRequestPaginateTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseTypeDef",
    "OcspConfigurationTypeDef",
    "OtherNameTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "PutPolicyRequestTypeDef",
    "QualifierTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCertificateAuthorityRequestTypeDef",
    "RevocationConfigurationTypeDef",
    "RevokeCertificateRequestTypeDef",
    "TagCertificateAuthorityRequestTypeDef",
    "TagTypeDef",
    "UntagCertificateAuthorityRequestTypeDef",
    "UpdateCertificateAuthorityRequestTypeDef",
    "ValidityTypeDef",
    "WaiterConfigTypeDef",
)

class CustomAttributeTypeDef(TypedDict):
    ObjectIdentifier: str
    Value: str

class AccessMethodTypeDef(TypedDict):
    CustomObjectIdentifier: NotRequired[str]
    AccessMethodType: NotRequired[AccessMethodTypeType]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CreateCertificateAuthorityAuditReportRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    S3BucketName: str
    AuditReportResponseFormat: AuditReportResponseFormatType

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class CreatePermissionRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Principal: str
    Actions: Sequence[ActionTypeType]
    SourceAccount: NotRequired[str]

class CrlDistributionPointExtensionConfigurationTypeDef(TypedDict):
    OmitExtension: bool

class KeyUsageTypeDef(TypedDict):
    DigitalSignature: NotRequired[bool]
    NonRepudiation: NotRequired[bool]
    KeyEncipherment: NotRequired[bool]
    DataEncipherment: NotRequired[bool]
    KeyAgreement: NotRequired[bool]
    KeyCertSign: NotRequired[bool]
    CRLSign: NotRequired[bool]
    EncipherOnly: NotRequired[bool]
    DecipherOnly: NotRequired[bool]

class CustomExtensionTypeDef(TypedDict):
    ObjectIdentifier: str
    Value: str
    Critical: NotRequired[bool]

class DeleteCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    PermanentDeletionTimeInDays: NotRequired[int]

class DeletePermissionRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Principal: str
    SourceAccount: NotRequired[str]

class DeletePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DescribeCertificateAuthorityAuditReportRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    AuditReportId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str

class EdiPartyNameTypeDef(TypedDict):
    PartyName: str
    NameAssigner: NotRequired[str]

class ExtendedKeyUsageTypeDef(TypedDict):
    ExtendedKeyUsageType: NotRequired[ExtendedKeyUsageTypeType]
    ExtendedKeyUsageObjectIdentifier: NotRequired[str]

class OtherNameTypeDef(TypedDict):
    TypeId: str
    Value: str

class GetCertificateAuthorityCertificateRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str

class GetCertificateAuthorityCsrRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str

class GetCertificateRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    CertificateArn: str

class GetPolicyRequestTypeDef(TypedDict):
    ResourceArn: str

ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCertificateAuthoritiesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceOwner: NotRequired[ResourceOwnerType]

class ListPermissionsRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PermissionTypeDef(TypedDict):
    CertificateAuthorityArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Principal: NotRequired[str]
    SourceAccount: NotRequired[str]
    Actions: NotRequired[List[ActionTypeType]]
    Policy: NotRequired[str]

class ListTagsRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class OcspConfigurationTypeDef(TypedDict):
    Enabled: bool
    OcspCustomCname: NotRequired[str]

class QualifierTypeDef(TypedDict):
    CpsUri: str

class PutPolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class RestoreCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str

class RevokeCertificateRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    CertificateSerial: str
    RevocationReason: RevocationReasonType

class ASN1SubjectOutputTypeDef(TypedDict):
    Country: NotRequired[str]
    Organization: NotRequired[str]
    OrganizationalUnit: NotRequired[str]
    DistinguishedNameQualifier: NotRequired[str]
    State: NotRequired[str]
    CommonName: NotRequired[str]
    SerialNumber: NotRequired[str]
    Locality: NotRequired[str]
    Title: NotRequired[str]
    Surname: NotRequired[str]
    GivenName: NotRequired[str]
    Initials: NotRequired[str]
    Pseudonym: NotRequired[str]
    GenerationQualifier: NotRequired[str]
    CustomAttributes: NotRequired[List[CustomAttributeTypeDef]]

class ASN1SubjectTypeDef(TypedDict):
    Country: NotRequired[str]
    Organization: NotRequired[str]
    OrganizationalUnit: NotRequired[str]
    DistinguishedNameQualifier: NotRequired[str]
    State: NotRequired[str]
    CommonName: NotRequired[str]
    SerialNumber: NotRequired[str]
    Locality: NotRequired[str]
    Title: NotRequired[str]
    Surname: NotRequired[str]
    GivenName: NotRequired[str]
    Initials: NotRequired[str]
    Pseudonym: NotRequired[str]
    GenerationQualifier: NotRequired[str]
    CustomAttributes: NotRequired[Sequence[CustomAttributeTypeDef]]

class ImportCertificateAuthorityCertificateRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Certificate: BlobTypeDef
    CertificateChain: NotRequired[BlobTypeDef]

class CreateCertificateAuthorityAuditReportResponseTypeDef(TypedDict):
    AuditReportId: str
    S3Key: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateAuthorityResponseTypeDef(TypedDict):
    CertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateAuthorityAuditReportResponseTypeDef(TypedDict):
    AuditReportStatus: AuditReportStatusType
    S3BucketName: str
    S3Key: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCertificateResponseTypeDef(TypedDict):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCsrResponseTypeDef(TypedDict):
    Csr: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateResponseTypeDef(TypedDict):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class IssueCertificateResponseTypeDef(TypedDict):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class UntagCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class CrlConfigurationTypeDef(TypedDict):
    Enabled: bool
    ExpirationInDays: NotRequired[int]
    CustomCname: NotRequired[str]
    S3BucketName: NotRequired[str]
    S3ObjectAcl: NotRequired[S3ObjectAclType]
    CrlDistributionPointExtensionConfiguration: NotRequired[
        CrlDistributionPointExtensionConfigurationTypeDef
    ]
    CrlType: NotRequired[CrlTypeType]
    CustomPath: NotRequired[str]

class DescribeCertificateAuthorityAuditReportRequestWaitTypeDef(TypedDict):
    CertificateAuthorityArn: str
    AuditReportId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetCertificateAuthorityCsrRequestWaitTypeDef(TypedDict):
    CertificateAuthorityArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetCertificateRequestWaitTypeDef(TypedDict):
    CertificateAuthorityArn: str
    CertificateArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class ListCertificateAuthoritiesRequestPaginateTypeDef(TypedDict):
    ResourceOwner: NotRequired[ResourceOwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPermissionsRequestPaginateTypeDef(TypedDict):
    CertificateAuthorityArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsRequestPaginateTypeDef(TypedDict):
    CertificateAuthorityArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPermissionsResponseTypeDef(TypedDict):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PolicyQualifierInfoTypeDef(TypedDict):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: QualifierTypeDef

class GeneralNameOutputTypeDef(TypedDict):
    OtherName: NotRequired[OtherNameTypeDef]
    Rfc822Name: NotRequired[str]
    DnsName: NotRequired[str]
    DirectoryName: NotRequired[ASN1SubjectOutputTypeDef]
    EdiPartyName: NotRequired[EdiPartyNameTypeDef]
    UniformResourceIdentifier: NotRequired[str]
    IpAddress: NotRequired[str]
    RegisteredId: NotRequired[str]

ASN1SubjectUnionTypeDef = Union[ASN1SubjectTypeDef, ASN1SubjectOutputTypeDef]

class RevocationConfigurationTypeDef(TypedDict):
    CrlConfiguration: NotRequired[CrlConfigurationTypeDef]
    OcspConfiguration: NotRequired[OcspConfigurationTypeDef]

class PolicyInformationTypeDef(TypedDict):
    CertPolicyId: str
    PolicyQualifiers: NotRequired[Sequence[PolicyQualifierInfoTypeDef]]

class AccessDescriptionOutputTypeDef(TypedDict):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameOutputTypeDef

class GeneralNameTypeDef(TypedDict):
    OtherName: NotRequired[OtherNameTypeDef]
    Rfc822Name: NotRequired[str]
    DnsName: NotRequired[str]
    DirectoryName: NotRequired[ASN1SubjectUnionTypeDef]
    EdiPartyName: NotRequired[EdiPartyNameTypeDef]
    UniformResourceIdentifier: NotRequired[str]
    IpAddress: NotRequired[str]
    RegisteredId: NotRequired[str]

class UpdateCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    RevocationConfiguration: NotRequired[RevocationConfigurationTypeDef]
    Status: NotRequired[CertificateAuthorityStatusType]

class CsrExtensionsOutputTypeDef(TypedDict):
    KeyUsage: NotRequired[KeyUsageTypeDef]
    SubjectInformationAccess: NotRequired[List[AccessDescriptionOutputTypeDef]]

class AccessDescriptionTypeDef(TypedDict):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameTypeDef

GeneralNameUnionTypeDef = Union[GeneralNameTypeDef, GeneralNameOutputTypeDef]

class CertificateAuthorityConfigurationOutputTypeDef(TypedDict):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutputTypeDef
    CsrExtensions: NotRequired[CsrExtensionsOutputTypeDef]

class CsrExtensionsTypeDef(TypedDict):
    KeyUsage: NotRequired[KeyUsageTypeDef]
    SubjectInformationAccess: NotRequired[Sequence[AccessDescriptionTypeDef]]

class ExtensionsTypeDef(TypedDict):
    CertificatePolicies: NotRequired[Sequence[PolicyInformationTypeDef]]
    ExtendedKeyUsage: NotRequired[Sequence[ExtendedKeyUsageTypeDef]]
    KeyUsage: NotRequired[KeyUsageTypeDef]
    SubjectAlternativeNames: NotRequired[Sequence[GeneralNameUnionTypeDef]]
    CustomExtensions: NotRequired[Sequence[CustomExtensionTypeDef]]

CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastStateChangeAt": NotRequired[datetime],
        "Type": NotRequired[CertificateAuthorityTypeType],
        "Serial": NotRequired[str],
        "Status": NotRequired[CertificateAuthorityStatusType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "FailureReason": NotRequired[FailureReasonType],
        "CertificateAuthorityConfiguration": NotRequired[
            CertificateAuthorityConfigurationOutputTypeDef
        ],
        "RevocationConfiguration": NotRequired[RevocationConfigurationTypeDef],
        "RestorableUntil": NotRequired[datetime],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
        "UsageMode": NotRequired[CertificateAuthorityUsageModeType],
    },
)

class CertificateAuthorityConfigurationTypeDef(TypedDict):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectTypeDef
    CsrExtensions: NotRequired[CsrExtensionsTypeDef]

class ApiPassthroughTypeDef(TypedDict):
    Extensions: NotRequired[ExtensionsTypeDef]
    Subject: NotRequired[ASN1SubjectUnionTypeDef]

class DescribeCertificateAuthorityResponseTypeDef(TypedDict):
    CertificateAuthority: CertificateAuthorityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificateAuthoritiesResponseTypeDef(TypedDict):
    CertificateAuthorities: List[CertificateAuthorityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CertificateAuthorityConfigurationUnionTypeDef = Union[
    CertificateAuthorityConfigurationTypeDef, CertificateAuthorityConfigurationOutputTypeDef
]

class IssueCertificateRequestTypeDef(TypedDict):
    CertificateAuthorityArn: str
    Csr: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmType
    Validity: ValidityTypeDef
    ApiPassthrough: NotRequired[ApiPassthroughTypeDef]
    TemplateArn: NotRequired[str]
    ValidityNotBefore: NotRequired[ValidityTypeDef]
    IdempotencyToken: NotRequired[str]

class CreateCertificateAuthorityRequestTypeDef(TypedDict):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationUnionTypeDef
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: NotRequired[RevocationConfigurationTypeDef]
    IdempotencyToken: NotRequired[str]
    KeyStorageSecurityStandard: NotRequired[KeyStorageSecurityStandardType]
    Tags: NotRequired[Sequence[TagTypeDef]]
    UsageMode: NotRequired[CertificateAuthorityUsageModeType]
