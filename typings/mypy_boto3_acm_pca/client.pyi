# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for acm-pca service client

Usage::

    ```python
    import boto3
    from mypy_boto3_acm_pca import ACMPCAClient

    client: ACMPCAClient = boto3.client("acm-pca")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_acm_pca.paginator import (
    ListCertificateAuthoritiesPaginator,
    ListPermissionsPaginator,
    ListTagsPaginator,
)
from mypy_boto3_acm_pca.type_defs import (
    CertificateAuthorityConfigurationTypeDef,
    CreateCertificateAuthorityAuditReportResponseTypeDef,
    CreateCertificateAuthorityResponseTypeDef,
    DescribeCertificateAuthorityAuditReportResponseTypeDef,
    DescribeCertificateAuthorityResponseTypeDef,
    GetCertificateAuthorityCertificateResponseTypeDef,
    GetCertificateAuthorityCsrResponseTypeDef,
    GetCertificateResponseTypeDef,
    GetPolicyResponseTypeDef,
    IssueCertificateResponseTypeDef,
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    RevocationConfigurationTypeDef,
    TagTypeDef,
    ValidityTypeDef,
)
from mypy_boto3_acm_pca.waiter import (
    AuditReportCreatedWaiter,
    CertificateAuthorityCSRCreatedWaiter,
    CertificateIssuedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ACMPCAClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    CertificateMismatchException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidArgsException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidPolicyException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LockoutPreventedException: Type[BotocoreClientError]
    MalformedCSRException: Type[BotocoreClientError]
    MalformedCertificateException: Type[BotocoreClientError]
    PermissionAlreadyExistsException: Type[BotocoreClientError]
    RequestAlreadyProcessedException: Type[BotocoreClientError]
    RequestFailedException: Type[BotocoreClientError]
    RequestInProgressException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class ACMPCAClient:
    """
    [ACMPCA.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.can_paginate)
        """

    def create_certificate_authority(
        self,
        CertificateAuthorityConfiguration: "CertificateAuthorityConfigurationTypeDef",
        CertificateAuthorityType: Literal["ROOT", "SUBORDINATE"],
        RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
        IdempotencyToken: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCertificateAuthorityResponseTypeDef:
        """
        [Client.create_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority)
        """

    def create_certificate_authority_audit_report(
        self,
        CertificateAuthorityArn: str,
        S3BucketName: str,
        AuditReportResponseFormat: Literal["JSON", "CSV"],
    ) -> CreateCertificateAuthorityAuditReportResponseTypeDef:
        """
        [Client.create_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority_audit_report)
        """

    def create_permission(
        self,
        CertificateAuthorityArn: str,
        Principal: str,
        Actions: List[Literal["IssueCertificate", "GetCertificate", "ListPermissions"]],
        SourceAccount: str = None,
    ) -> None:
        """
        [Client.create_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.create_permission)
        """

    def delete_certificate_authority(
        self, CertificateAuthorityArn: str, PermanentDeletionTimeInDays: int = None
    ) -> None:
        """
        [Client.delete_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.delete_certificate_authority)
        """

    def delete_permission(
        self, CertificateAuthorityArn: str, Principal: str, SourceAccount: str = None
    ) -> None:
        """
        [Client.delete_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.delete_permission)
        """

    def delete_policy(self, ResourceArn: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.delete_policy)
        """

    def describe_certificate_authority(
        self, CertificateAuthorityArn: str
    ) -> DescribeCertificateAuthorityResponseTypeDef:
        """
        [Client.describe_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority)
        """

    def describe_certificate_authority_audit_report(
        self, CertificateAuthorityArn: str, AuditReportId: str
    ) -> DescribeCertificateAuthorityAuditReportResponseTypeDef:
        """
        [Client.describe_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority_audit_report)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.generate_presigned_url)
        """

    def get_certificate(
        self, CertificateAuthorityArn: str, CertificateArn: str
    ) -> GetCertificateResponseTypeDef:
        """
        [Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.get_certificate)
        """

    def get_certificate_authority_certificate(
        self, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCertificateResponseTypeDef:
        """
        [Client.get_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_certificate)
        """

    def get_certificate_authority_csr(
        self, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCsrResponseTypeDef:
        """
        [Client.get_certificate_authority_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_csr)
        """

    def get_policy(self, ResourceArn: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.get_policy)
        """

    def import_certificate_authority_certificate(
        self,
        CertificateAuthorityArn: str,
        Certificate: Union[bytes, IO[bytes]],
        CertificateChain: Union[bytes, IO[bytes]] = None,
    ) -> None:
        """
        [Client.import_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.import_certificate_authority_certificate)
        """

    def issue_certificate(
        self,
        CertificateAuthorityArn: str,
        Csr: Union[bytes, IO[bytes]],
        SigningAlgorithm: Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        Validity: ValidityTypeDef,
        TemplateArn: str = None,
        IdempotencyToken: str = None,
    ) -> IssueCertificateResponseTypeDef:
        """
        [Client.issue_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.issue_certificate)
        """

    def list_certificate_authorities(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ResourceOwner: Literal["SELF", "OTHER_ACCOUNTS"] = None,
    ) -> ListCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.list_certificate_authorities)
        """

    def list_permissions(
        self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionsResponseTypeDef:
        """
        [Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.list_permissions)
        """

    def list_tags(
        self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.list_tags)
        """

    def put_policy(self, ResourceArn: str, Policy: str) -> None:
        """
        [Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.put_policy)
        """

    def restore_certificate_authority(self, CertificateAuthorityArn: str) -> None:
        """
        [Client.restore_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.restore_certificate_authority)
        """

    def revoke_certificate(
        self,
        CertificateAuthorityArn: str,
        CertificateSerial: str,
        RevocationReason: Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CERTIFICATE_AUTHORITY_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERSEDED",
            "CESSATION_OF_OPERATION",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
    ) -> None:
        """
        [Client.revoke_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.revoke_certificate)
        """

    def tag_certificate_authority(
        self, CertificateAuthorityArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        [Client.tag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.tag_certificate_authority)
        """

    def untag_certificate_authority(
        self, CertificateAuthorityArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        [Client.untag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.untag_certificate_authority)
        """

    def update_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
        Status: Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ] = None,
    ) -> None:
        """
        [Client.update_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Client.update_certificate_authority)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificate_authorities"]
    ) -> ListCertificateAuthoritiesPaginator:
        """
        [Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        [Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["audit_report_created"]) -> AuditReportCreatedWaiter:
        """
        [Waiter.AuditReportCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["certificate_authority_csr_created"]
    ) -> CertificateAuthorityCSRCreatedWaiter:
        """
        [Waiter.CertificateAuthorityCSRCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["certificate_issued"]) -> CertificateIssuedWaiter:
        """
        [Waiter.CertificateIssued documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)
        """
