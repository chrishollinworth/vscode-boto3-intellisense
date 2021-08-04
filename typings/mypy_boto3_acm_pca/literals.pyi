"""
Type annotations for acm-pca service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/literals.html)

Usage::

    ```python
    from mypy_boto3_acm_pca.literals import AccessMethodTypeType

    data: AccessMethodTypeType = "CA_REPOSITORY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessMethodTypeType",
    "ActionTypeType",
    "AuditReportCreatedWaiterName",
    "AuditReportResponseFormatType",
    "AuditReportStatusType",
    "CertificateAuthorityCSRCreatedWaiterName",
    "CertificateAuthorityStatusType",
    "CertificateAuthorityTypeType",
    "CertificateIssuedWaiterName",
    "ExtendedKeyUsageTypeType",
    "FailureReasonType",
    "KeyAlgorithmType",
    "KeyStorageSecurityStandardType",
    "ListCertificateAuthoritiesPaginatorName",
    "ListPermissionsPaginatorName",
    "ListTagsPaginatorName",
    "PolicyQualifierIdType",
    "ResourceOwnerType",
    "RevocationReasonType",
    "S3ObjectAclType",
    "SigningAlgorithmType",
    "ValidityPeriodTypeType",
)

AccessMethodTypeType = Literal["CA_REPOSITORY", "RESOURCE_PKI_MANIFEST", "RESOURCE_PKI_NOTIFY"]
ActionTypeType = Literal["GetCertificate", "IssueCertificate", "ListPermissions"]
AuditReportCreatedWaiterName = Literal["audit_report_created"]
AuditReportResponseFormatType = Literal["CSV", "JSON"]
AuditReportStatusType = Literal["CREATING", "FAILED", "SUCCESS"]
CertificateAuthorityCSRCreatedWaiterName = Literal["certificate_authority_csr_created"]
CertificateAuthorityStatusType = Literal[
    "ACTIVE", "CREATING", "DELETED", "DISABLED", "EXPIRED", "FAILED", "PENDING_CERTIFICATE"
]
CertificateAuthorityTypeType = Literal["ROOT", "SUBORDINATE"]
CertificateIssuedWaiterName = Literal["certificate_issued"]
ExtendedKeyUsageTypeType = Literal[
    "CERTIFICATE_TRANSPARENCY",
    "CLIENT_AUTH",
    "CODE_SIGNING",
    "DOCUMENT_SIGNING",
    "EMAIL_PROTECTION",
    "OCSP_SIGNING",
    "SERVER_AUTH",
    "SMART_CARD_LOGIN",
    "TIME_STAMPING",
]
FailureReasonType = Literal["OTHER", "REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM"]
KeyAlgorithmType = Literal["EC_prime256v1", "EC_secp384r1", "RSA_2048", "RSA_4096"]
KeyStorageSecurityStandardType = Literal[
    "FIPS_140_2_LEVEL_2_OR_HIGHER", "FIPS_140_2_LEVEL_3_OR_HIGHER"
]
ListCertificateAuthoritiesPaginatorName = Literal["list_certificate_authorities"]
ListPermissionsPaginatorName = Literal["list_permissions"]
ListTagsPaginatorName = Literal["list_tags"]
PolicyQualifierIdType = Literal["CPS"]
ResourceOwnerType = Literal["OTHER_ACCOUNTS", "SELF"]
RevocationReasonType = Literal[
    "AFFILIATION_CHANGED",
    "A_A_COMPROMISE",
    "CERTIFICATE_AUTHORITY_COMPROMISE",
    "CESSATION_OF_OPERATION",
    "KEY_COMPROMISE",
    "PRIVILEGE_WITHDRAWN",
    "SUPERSEDED",
    "UNSPECIFIED",
]
S3ObjectAclType = Literal["BUCKET_OWNER_FULL_CONTROL", "PUBLIC_READ"]
SigningAlgorithmType = Literal[
    "SHA256WITHECDSA",
    "SHA256WITHRSA",
    "SHA384WITHECDSA",
    "SHA384WITHRSA",
    "SHA512WITHECDSA",
    "SHA512WITHRSA",
]
ValidityPeriodTypeType = Literal["ABSOLUTE", "DAYS", "END_DATE", "MONTHS", "YEARS"]
