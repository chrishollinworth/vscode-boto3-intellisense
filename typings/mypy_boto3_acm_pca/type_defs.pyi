"""
Main interface for acm-pca service type definitions.

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef

    data: ASN1SubjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityTypeDef",
    "CrlConfigurationTypeDef",
    "CsrExtensionsTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameTypeDef",
    "KeyUsageTypeDef",
    "OtherNameTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "QualifierTypeDef",
    "RevocationConfigurationTypeDef",
    "TagTypeDef",
    "ApiPassthroughTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "IssueCertificateResponseTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
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
    {"AccessMethod": "AccessMethodTypeDef", "AccessLocation": "GeneralNameTypeDef"},
)

AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": str,
        "AccessMethodType": Literal[
            "CA_REPOSITORY", "RESOURCE_PKI_MANIFEST", "RESOURCE_PKI_NOTIFY"
        ],
    },
    total=False,
)

_RequiredCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_RequiredCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": Literal["RSA_2048", "RSA_4096", "EC_prime256v1", "EC_secp384r1"],
        "SigningAlgorithm": Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        "Subject": "ASN1SubjectTypeDef",
    },
)
_OptionalCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_OptionalCertificateAuthorityConfigurationTypeDef",
    {"CsrExtensions": "CsrExtensionsTypeDef"},
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
        "Type": Literal["ROOT", "SUBORDINATE"],
        "Serial": str,
        "Status": Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": Literal["REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM", "OTHER"],
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "RestorableUntil": datetime,
    },
    total=False,
)

_RequiredCrlConfigurationTypeDef = TypedDict("_RequiredCrlConfigurationTypeDef", {"Enabled": bool})
_OptionalCrlConfigurationTypeDef = TypedDict(
    "_OptionalCrlConfigurationTypeDef",
    {"ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class CrlConfigurationTypeDef(_RequiredCrlConfigurationTypeDef, _OptionalCrlConfigurationTypeDef):
    pass


CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {"KeyUsage": "KeyUsageTypeDef", "SubjectInformationAccess": List["AccessDescriptionTypeDef"]},
    total=False,
)

_RequiredEdiPartyNameTypeDef = TypedDict("_RequiredEdiPartyNameTypeDef", {"PartyName": str})
_OptionalEdiPartyNameTypeDef = TypedDict(
    "_OptionalEdiPartyNameTypeDef", {"NameAssigner": str}, total=False
)


class EdiPartyNameTypeDef(_RequiredEdiPartyNameTypeDef, _OptionalEdiPartyNameTypeDef):
    pass


ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": Literal[
            "SERVER_AUTH",
            "CLIENT_AUTH",
            "CODE_SIGNING",
            "EMAIL_PROTECTION",
            "TIME_STAMPING",
            "OCSP_SIGNING",
            "SMART_CARD_LOGIN",
            "DOCUMENT_SIGNING",
            "CERTIFICATE_TRANSPARENCY",
        ],
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

OtherNameTypeDef = TypedDict("OtherNameTypeDef", {"TypeId": str, "Value": str})

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[Literal["IssueCertificate", "GetCertificate", "ListPermissions"]],
        "Policy": str,
    },
    total=False,
)

_RequiredPolicyInformationTypeDef = TypedDict(
    "_RequiredPolicyInformationTypeDef", {"CertPolicyId": str}
)
_OptionalPolicyInformationTypeDef = TypedDict(
    "_OptionalPolicyInformationTypeDef",
    {"PolicyQualifiers": List["PolicyQualifierInfoTypeDef"]},
    total=False,
)


class PolicyInformationTypeDef(
    _RequiredPolicyInformationTypeDef, _OptionalPolicyInformationTypeDef
):
    pass


PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {"PolicyQualifierId": Literal["CPS"], "Qualifier": "QualifierTypeDef"},
)

QualifierTypeDef = TypedDict("QualifierTypeDef", {"CpsUri": str})

RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef", {"CrlConfiguration": "CrlConfigurationTypeDef"}, total=False
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {"Extensions": "ExtensionsTypeDef", "Subject": "ASN1SubjectTypeDef"},
    total=False,
)

CreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    {"AuditReportId": str, "S3Key": str},
    total=False,
)

CreateCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseTypeDef", {"CertificateAuthorityArn": str}, total=False
)

DescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": Literal["CREATING", "SUCCESS", "FAILED"],
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
    },
    total=False,
)

DescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseTypeDef",
    {"CertificateAuthority": "CertificateAuthorityTypeDef"},
    total=False,
)

GetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)

GetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseTypeDef", {"Csr": str}, total=False
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef", {"Certificate": str, "CertificateChain": str}, total=False
)

GetPolicyResponseTypeDef = TypedDict("GetPolicyResponseTypeDef", {"Policy": str}, total=False)

IssueCertificateResponseTypeDef = TypedDict(
    "IssueCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

ListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseTypeDef",
    {"CertificateAuthorities": List["CertificateAuthorityTypeDef"], "NextToken": str},
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {"Permissions": List["PermissionTypeDef"], "NextToken": str},
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": List["TagTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {"Value": int, "Type": Literal["END_DATE", "ABSOLUTE", "DAYS", "MONTHS", "YEARS"]},
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
