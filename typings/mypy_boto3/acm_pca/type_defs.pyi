"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef

    data: ASN1SubjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ASN1SubjectTypeDef",
    "AccessDescriptionTypeDef",
    "AccessMethodTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityRequestRequestTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CrlConfigurationTypeDef",
    "CsrExtensionsTypeDef",
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameTypeDef",
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    "IssueCertificateRequestRequestTypeDef",
    "IssueCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "OtherNameTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "QualifierTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    "RevocationConfigurationTypeDef",
    "RevokeCertificateRequestRequestTypeDef",
    "TagCertificateAuthorityRequestRequestTypeDef",
    "TagTypeDef",
    "UntagCertificateAuthorityRequestRequestTypeDef",
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    "ValidityTypeDef",
    "WaiterConfigTypeDef",
)

ASN1SubjectTypeDef = TypedDict(
    "ASN1SubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

AccessDescriptionTypeDef = TypedDict(
    "AccessDescriptionTypeDef",
    {
        "AccessMethod": "AccessMethodTypeDef",
        "AccessLocation": "GeneralNameTypeDef",
    },
)

AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": str,
        "AccessMethodType": AccessMethodTypeType,
    },
    total=False,
)

ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {
        "Extensions": "ExtensionsTypeDef",
        "Subject": "ASN1SubjectTypeDef",
    },
    total=False,
)

_RequiredCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_RequiredCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": "ASN1SubjectTypeDef",
    },
)
_OptionalCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_OptionalCertificateAuthorityConfigurationTypeDef",
    {
        "CsrExtensions": "CsrExtensionsTypeDef",
    },
    total=False,
)

class CertificateAuthorityConfigurationTypeDef(
    _RequiredCertificateAuthorityConfigurationTypeDef,
    _OptionalCertificateAuthorityConfigurationTypeDef,
):
    pass

CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": str,
        "OwnerAccount": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": CertificateAuthorityTypeType,
        "Serial": str,
        "Status": CertificateAuthorityStatusType,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": FailureReasonType,
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "RestorableUntil": datetime,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
    },
    total=False,
)

CreateCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "S3BucketName": str,
        "AuditReportResponseFormat": AuditReportResponseFormatType,
    },
)

CreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportId": str,
        "S3Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "CertificateAuthorityType": CertificateAuthorityTypeType,
    },
)
_OptionalCreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateAuthorityRequestRequestTypeDef",
    {
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "IdempotencyToken": str,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCertificateAuthorityRequestRequestTypeDef(
    _RequiredCreateCertificateAuthorityRequestRequestTypeDef,
    _OptionalCreateCertificateAuthorityRequestRequestTypeDef,
):
    pass

CreateCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "Actions": List[ActionTypeType],
    },
)
_OptionalCreatePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionRequestRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)

class CreatePermissionRequestRequestTypeDef(
    _RequiredCreatePermissionRequestRequestTypeDef, _OptionalCreatePermissionRequestRequestTypeDef
):
    pass

_RequiredCrlConfigurationTypeDef = TypedDict(
    "_RequiredCrlConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCrlConfigurationTypeDef = TypedDict(
    "_OptionalCrlConfigurationTypeDef",
    {
        "ExpirationInDays": int,
        "CustomCname": str,
        "S3BucketName": str,
        "S3ObjectAcl": S3ObjectAclType,
    },
    total=False,
)

class CrlConfigurationTypeDef(_RequiredCrlConfigurationTypeDef, _OptionalCrlConfigurationTypeDef):
    pass

CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {
        "KeyUsage": "KeyUsageTypeDef",
        "SubjectInformationAccess": List["AccessDescriptionTypeDef"],
    },
    total=False,
)

_RequiredDeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalDeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "PermanentDeletionTimeInDays": int,
    },
    total=False,
)

class DeleteCertificateAuthorityRequestRequestTypeDef(
    _RequiredDeleteCertificateAuthorityRequestRequestTypeDef,
    _OptionalDeleteCertificateAuthorityRequestRequestTypeDef,
):
    pass

_RequiredDeletePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
    },
)
_OptionalDeletePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionRequestRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)

class DeletePermissionRequestRequestTypeDef(
    _RequiredDeletePermissionRequestRequestTypeDef, _OptionalDeletePermissionRequestRequestTypeDef
):
    pass

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)

DescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": AuditReportStatusType,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

DescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthority": "CertificateAuthorityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEdiPartyNameTypeDef = TypedDict(
    "_RequiredEdiPartyNameTypeDef",
    {
        "PartyName": str,
    },
)
_OptionalEdiPartyNameTypeDef = TypedDict(
    "_OptionalEdiPartyNameTypeDef",
    {
        "NameAssigner": str,
    },
    total=False,
)

class EdiPartyNameTypeDef(_RequiredEdiPartyNameTypeDef, _OptionalEdiPartyNameTypeDef):
    pass

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": ExtendedKeyUsageTypeType,
        "ExtendedKeyUsageObjectIdentifier": str,
    },
    total=False,
)

ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "CertificatePolicies": List["PolicyInformationTypeDef"],
        "ExtendedKeyUsage": List["ExtendedKeyUsageTypeDef"],
        "KeyUsage": "KeyUsageTypeDef",
        "SubjectAlternativeNames": List["GeneralNameTypeDef"],
    },
    total=False,
)

GeneralNameTypeDef = TypedDict(
    "GeneralNameTypeDef",
    {
        "OtherName": "OtherNameTypeDef",
        "Rfc822Name": str,
        "DnsName": str,
        "DirectoryName": "ASN1SubjectTypeDef",
        "EdiPartyName": "EdiPartyNameTypeDef",
        "UniformResourceIdentifier": str,
        "IpAddress": str,
        "RegisteredId": str,
    },
    total=False,
)

GetCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateAuthorityCsrRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseTypeDef",
    {
        "Csr": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
    },
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Certificate": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateChain": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class ImportCertificateAuthorityCertificateRequestRequestTypeDef(
    _RequiredImportCertificateAuthorityCertificateRequestRequestTypeDef,
    _OptionalImportCertificateAuthorityCertificateRequestRequestTypeDef,
):
    pass

_RequiredIssueCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredIssueCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Csr": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmType,
        "Validity": "ValidityTypeDef",
    },
)
_OptionalIssueCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalIssueCertificateRequestRequestTypeDef",
    {
        "ApiPassthrough": "ApiPassthroughTypeDef",
        "TemplateArn": str,
        "ValidityNotBefore": "ValidityTypeDef",
        "IdempotencyToken": str,
    },
    total=False,
)

class IssueCertificateRequestRequestTypeDef(
    _RequiredIssueCertificateRequestRequestTypeDef, _OptionalIssueCertificateRequestRequestTypeDef
):
    pass

IssueCertificateResponseTypeDef = TypedDict(
    "IssueCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "DigitalSignature": bool,
        "NonRepudiation": bool,
        "KeyEncipherment": bool,
        "DataEncipherment": bool,
        "KeyAgreement": bool,
        "KeyCertSign": bool,
        "CRLSign": bool,
        "EncipherOnly": bool,
        "DecipherOnly": bool,
    },
    total=False,
)

ListCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResourceOwner": ResourceOwnerType,
    },
    total=False,
)

ListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List["CertificateAuthorityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPermissionsRequestRequestTypeDef(
    _RequiredListPermissionsRequestRequestTypeDef, _OptionalListPermissionsRequestRequestTypeDef
):
    pass

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OtherNameTypeDef = TypedDict(
    "OtherNameTypeDef",
    {
        "TypeId": str,
        "Value": str,
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
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[ActionTypeType],
        "Policy": str,
    },
    total=False,
)

_RequiredPolicyInformationTypeDef = TypedDict(
    "_RequiredPolicyInformationTypeDef",
    {
        "CertPolicyId": str,
    },
)
_OptionalPolicyInformationTypeDef = TypedDict(
    "_OptionalPolicyInformationTypeDef",
    {
        "PolicyQualifiers": List["PolicyQualifierInfoTypeDef"],
    },
    total=False,
)

class PolicyInformationTypeDef(
    _RequiredPolicyInformationTypeDef, _OptionalPolicyInformationTypeDef
):
    pass

PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {
        "PolicyQualifierId": Literal["CPS"],
        "Qualifier": "QualifierTypeDef",
    },
)

PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

QualifierTypeDef = TypedDict(
    "QualifierTypeDef",
    {
        "CpsUri": str,
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

RestoreCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef",
    {
        "CrlConfiguration": "CrlConfigurationTypeDef",
    },
    total=False,
)

RevokeCertificateRequestRequestTypeDef = TypedDict(
    "RevokeCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateSerial": str,
        "RevocationReason": RevocationReasonType,
    },
)

TagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "TagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

UntagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UntagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredUpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalUpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "Status": CertificateAuthorityStatusType,
    },
    total=False,
)

class UpdateCertificateAuthorityRequestRequestTypeDef(
    _RequiredUpdateCertificateAuthorityRequestRequestTypeDef,
    _OptionalUpdateCertificateAuthorityRequestRequestTypeDef,
):
    pass

ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
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
