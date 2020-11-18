"""
Main interface for acm service type definitions.

Usage::

    ```python
    from mypy_boto3_acm.type_defs import CertificateDetailTypeDef

    data: CertificateDetailTypeDef = {...}
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
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DomainValidationTypeDef",
    "ExtendedKeyUsageTypeDef",
    "KeyUsageTypeDef",
    "RenewalSummaryTypeDef",
    "ResourceRecordTypeDef",
    "TagTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "ExportCertificateResponseTypeDef",
    "FiltersTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RequestCertificateResponseTypeDef",
    "WaiterConfigTypeDef",
)

CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
        "SubjectAlternativeNames": List[str],
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "Serial": str,
        "Subject": str,
        "Issuer": str,
        "CreatedAt": datetime,
        "IssuedAt": datetime,
        "ImportedAt": datetime,
        "Status": Literal[
            "PENDING_VALIDATION",
            "ISSUED",
            "INACTIVE",
            "EXPIRED",
            "VALIDATION_TIMED_OUT",
            "REVOKED",
            "FAILED",
        ],
        "RevokedAt": datetime,
        "RevocationReason": Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CA_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERCEDED",
            "CESSATION_OF_OPERATION",
            "CERTIFICATE_HOLD",
            "REMOVE_FROM_CRL",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "KeyAlgorithm": Literal[
            "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
        ],
        "SignatureAlgorithm": str,
        "InUseBy": List[str],
        "FailureReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "SLR_NOT_FOUND",
            "OTHER",
        ],
        "Type": Literal["IMPORTED", "AMAZON_ISSUED", "PRIVATE"],
        "RenewalSummary": "RenewalSummaryTypeDef",
        "KeyUsages": List["KeyUsageTypeDef"],
        "ExtendedKeyUsages": List["ExtendedKeyUsageTypeDef"],
        "CertificateAuthorityArn": str,
        "RenewalEligibility": Literal["ELIGIBLE", "INELIGIBLE"],
        "Options": "CertificateOptionsTypeDef",
    },
    total=False,
)

CertificateOptionsTypeDef = TypedDict(
    "CertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef", {"CertificateArn": str, "DomainName": str}, total=False
)

_RequiredDomainValidationTypeDef = TypedDict(
    "_RequiredDomainValidationTypeDef", {"DomainName": str}
)
_OptionalDomainValidationTypeDef = TypedDict(
    "_OptionalDomainValidationTypeDef",
    {
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": Literal["PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "ResourceRecord": "ResourceRecordTypeDef",
        "ValidationMethod": Literal["EMAIL", "DNS"],
    },
    total=False,
)


class DomainValidationTypeDef(_RequiredDomainValidationTypeDef, _OptionalDomainValidationTypeDef):
    pass


ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "Name": Literal[
            "TLS_WEB_SERVER_AUTHENTICATION",
            "TLS_WEB_CLIENT_AUTHENTICATION",
            "CODE_SIGNING",
            "EMAIL_PROTECTION",
            "TIME_STAMPING",
            "OCSP_SIGNING",
            "IPSEC_END_SYSTEM",
            "IPSEC_TUNNEL",
            "IPSEC_USER",
            "ANY",
            "NONE",
            "CUSTOM",
        ],
        "OID": str,
    },
    total=False,
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "Name": Literal[
            "DIGITAL_SIGNATURE",
            "NON_REPUDIATION",
            "KEY_ENCIPHERMENT",
            "DATA_ENCIPHERMENT",
            "KEY_AGREEMENT",
            "CERTIFICATE_SIGNING",
            "CRL_SIGNING",
            "ENCIPHER_ONLY",
            "DECIPHER_ONLY",
            "ANY",
            "CUSTOM",
        ]
    },
    total=False,
)

_RequiredRenewalSummaryTypeDef = TypedDict(
    "_RequiredRenewalSummaryTypeDef",
    {
        "RenewalStatus": Literal["PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "UpdatedAt": datetime,
    },
)
_OptionalRenewalSummaryTypeDef = TypedDict(
    "_OptionalRenewalSummaryTypeDef",
    {
        "RenewalStatusReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "SLR_NOT_FOUND",
            "OTHER",
        ]
    },
    total=False,
)


class RenewalSummaryTypeDef(_RequiredRenewalSummaryTypeDef, _OptionalRenewalSummaryTypeDef):
    pass


ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef", {"Name": str, "Type": Literal["CNAME"], "Value": str}
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef", {"Certificate": "CertificateDetailTypeDef"}, total=False
)

DomainValidationOptionTypeDef = TypedDict(
    "DomainValidationOptionTypeDef", {"DomainName": str, "ValidationDomain": str}
)

ExportCertificateResponseTypeDef = TypedDict(
    "ExportCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str, "PrivateKey": str},
    total=False,
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": List[
            Literal[
                "TLS_WEB_SERVER_AUTHENTICATION",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "CODE_SIGNING",
                "EMAIL_PROTECTION",
                "TIME_STAMPING",
                "OCSP_SIGNING",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "ANY",
                "NONE",
                "CUSTOM",
            ]
        ],
        "keyUsage": List[
            Literal[
                "DIGITAL_SIGNATURE",
                "NON_REPUDIATION",
                "KEY_ENCIPHERMENT",
                "DATA_ENCIPHERMENT",
                "KEY_AGREEMENT",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "ENCIPHER_ONLY",
                "DECIPHER_ONLY",
                "ANY",
                "CUSTOM",
            ]
        ],
        "keyTypes": List[
            Literal[
                "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
            ]
        ],
    },
    total=False,
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef", {"Certificate": str, "CertificateChain": str}, total=False
)

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {"NextToken": str, "CertificateSummaryList": List["CertificateSummaryTypeDef"]},
    total=False,
)

ListTagsForCertificateResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RequestCertificateResponseTypeDef = TypedDict(
    "RequestCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
