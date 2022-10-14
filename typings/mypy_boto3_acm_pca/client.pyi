"""
Type annotations for acm-pca service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_acm_pca import ACMPCAClient

    client: ACMPCAClient = boto3.client("acm-pca")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ActionTypeType,
    AuditReportResponseFormatType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    SigningAlgorithmType,
)
from .paginator import (
    ListCertificateAuthoritiesPaginator,
    ListPermissionsPaginator,
    ListTagsPaginator,
)
from .type_defs import (
    ApiPassthroughTypeDef,
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
from .waiter import (
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

class ACMPCAClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ACMPCAClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#close)
        """
    def create_certificate_authority(
        self,
        *,
        CertificateAuthorityConfiguration: "CertificateAuthorityConfigurationTypeDef",
        CertificateAuthorityType: CertificateAuthorityTypeType,
        RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
        IdempotencyToken: str = None,
        KeyStorageSecurityStandard: KeyStorageSecurityStandardType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCertificateAuthorityResponseTypeDef:
        """
        Creates a root or subordinate private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#create_certificate_authority)
        """
    def create_certificate_authority_audit_report(
        self,
        *,
        CertificateAuthorityArn: str,
        S3BucketName: str,
        AuditReportResponseFormat: AuditReportResponseFormatType
    ) -> CreateCertificateAuthorityAuditReportResponseTypeDef:
        """
        Creates an audit report that lists every time that your CA private key is used.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority_audit_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#create_certificate_authority_audit_report)
        """
    def create_permission(
        self,
        *,
        CertificateAuthorityArn: str,
        Principal: str,
        Actions: List[ActionTypeType],
        SourceAccount: str = None
    ) -> None:
        """
        Grants one or more permissions on a private CA to the Certificate Manager (ACM)
        service principal (`acm.amazonaws.com` ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.create_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#create_permission)
        """
    def delete_certificate_authority(
        self, *, CertificateAuthorityArn: str, PermanentDeletionTimeInDays: int = None
    ) -> None:
        """
        Deletes a private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.delete_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#delete_certificate_authority)
        """
    def delete_permission(
        self, *, CertificateAuthorityArn: str, Principal: str, SourceAccount: str = None
    ) -> None:
        """
        Revokes permissions on a private CA granted to the Certificate Manager (ACM)
        service principal (acm.amazonaws.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.delete_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#delete_permission)
        """
    def delete_policy(self, *, ResourceArn: str) -> None:
        """
        Deletes the resource-based policy attached to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#delete_policy)
        """
    def describe_certificate_authority(
        self, *, CertificateAuthorityArn: str
    ) -> DescribeCertificateAuthorityResponseTypeDef:
        """
        Lists information about your private certificate authority (CA) or one that has
        been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#describe_certificate_authority)
        """
    def describe_certificate_authority_audit_report(
        self, *, CertificateAuthorityArn: str, AuditReportId: str
    ) -> DescribeCertificateAuthorityAuditReportResponseTypeDef:
        """
        Lists information about a specific audit report created by calling the
        `CreateCertificateAuthorityAuditReport <https://docs.aws.amazon.com/acm-
        pca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html>`__
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority_audit_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#describe_certificate_authority_audit_report)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#generate_presigned_url)
        """
    def get_certificate(
        self, *, CertificateAuthorityArn: str, CertificateArn: str
    ) -> GetCertificateResponseTypeDef:
        """
        Retrieves a certificate from your private CA or one that has been shared with
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.get_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#get_certificate)
        """
    def get_certificate_authority_certificate(
        self, *, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCertificateResponseTypeDef:
        """
        Retrieves the certificate and certificate chain for your private certificate
        authority (CA) or one that has been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#get_certificate_authority_certificate)
        """
    def get_certificate_authority_csr(
        self, *, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCsrResponseTypeDef:
        """
        Retrieves the certificate signing request (CSR) for your private certificate
        authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_csr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#get_certificate_authority_csr)
        """
    def get_policy(self, *, ResourceArn: str) -> GetPolicyResponseTypeDef:
        """
        Retrieves the resource-based policy attached to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#get_policy)
        """
    def import_certificate_authority_certificate(
        self,
        *,
        CertificateAuthorityArn: str,
        Certificate: Union[bytes, IO[bytes], StreamingBody],
        CertificateChain: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> None:
        """
        Imports a signed private CA certificate into ACM Private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.import_certificate_authority_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#import_certificate_authority_certificate)
        """
    def issue_certificate(
        self,
        *,
        CertificateAuthorityArn: str,
        Csr: Union[bytes, IO[bytes], StreamingBody],
        SigningAlgorithm: SigningAlgorithmType,
        Validity: "ValidityTypeDef",
        ApiPassthrough: "ApiPassthroughTypeDef" = None,
        TemplateArn: str = None,
        ValidityNotBefore: "ValidityTypeDef" = None,
        IdempotencyToken: str = None
    ) -> IssueCertificateResponseTypeDef:
        """
        Uses your private certificate authority (CA), or one that has been shared with
        you, to issue a client certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.issue_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#issue_certificate)
        """
    def list_certificate_authorities(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        ResourceOwner: ResourceOwnerType = None
    ) -> ListCertificateAuthoritiesResponseTypeDef:
        """
        Lists the private certificate authorities that you created by using the
        `CreateCertificateAuthority <https://docs.aws.amazon.com/acm-
        pca/latest/APIReference/API_CreateCertificateAuthority.html>`__ action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.list_certificate_authorities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#list_certificate_authorities)
        """
    def list_permissions(
        self, *, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionsResponseTypeDef:
        """
        List all permissions on a private CA, if any, granted to the Certificate Manager
        (ACM) service principal (acm.amazonaws.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.list_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#list_permissions)
        """
    def list_tags(
        self, *, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        Lists the tags, if any, that are associated with your private CA or one that has
        been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#list_tags)
        """
    def put_policy(self, *, ResourceArn: str, Policy: str) -> None:
        """
        Attaches a resource-based policy to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.put_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#put_policy)
        """
    def restore_certificate_authority(self, *, CertificateAuthorityArn: str) -> None:
        """
        Restores a certificate authority (CA) that is in the `DELETED` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.restore_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#restore_certificate_authority)
        """
    def revoke_certificate(
        self,
        *,
        CertificateAuthorityArn: str,
        CertificateSerial: str,
        RevocationReason: RevocationReasonType
    ) -> None:
        """
        Revokes a certificate that was issued inside ACM Private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.revoke_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#revoke_certificate)
        """
    def tag_certificate_authority(
        self, *, CertificateAuthorityArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        Adds one or more tags to your private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.tag_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#tag_certificate_authority)
        """
    def untag_certificate_authority(
        self, *, CertificateAuthorityArn: str, Tags: List["TagTypeDef"]
    ) -> None:
        """
        Remove one or more tags from your private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.untag_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#untag_certificate_authority)
        """
    def update_certificate_authority(
        self,
        *,
        CertificateAuthorityArn: str,
        RevocationConfiguration: "RevocationConfigurationTypeDef" = None,
        Status: CertificateAuthorityStatusType = None
    ) -> None:
        """
        Updates the status or configuration of a private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Client.update_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client.html#update_certificate_authority)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificate_authorities"]
    ) -> ListCertificateAuthoritiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listcertificateauthoritiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listpermissionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listtagspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["audit_report_created"]) -> AuditReportCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/waiters.html#auditreportcreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["certificate_authority_csr_created"]
    ) -> CertificateAuthorityCSRCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/waiters.html#certificateauthoritycsrcreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["certificate_issued"]) -> CertificateIssuedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/waiters.html#certificateissuedwaiter)
        """
