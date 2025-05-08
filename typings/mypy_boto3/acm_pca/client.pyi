"""
Type annotations for acm-pca service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_acm_pca.client import ACMPCAClient

    session = Session()
    client: ACMPCAClient = session.client("acm-pca")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCertificateAuthoritiesPaginator,
    ListPermissionsPaginator,
    ListTagsPaginator,
)
from .type_defs import (
    CreateCertificateAuthorityAuditReportRequestTypeDef,
    CreateCertificateAuthorityAuditReportResponseTypeDef,
    CreateCertificateAuthorityRequestTypeDef,
    CreateCertificateAuthorityResponseTypeDef,
    CreatePermissionRequestTypeDef,
    DeleteCertificateAuthorityRequestTypeDef,
    DeletePermissionRequestTypeDef,
    DeletePolicyRequestTypeDef,
    DescribeCertificateAuthorityAuditReportRequestTypeDef,
    DescribeCertificateAuthorityAuditReportResponseTypeDef,
    DescribeCertificateAuthorityRequestTypeDef,
    DescribeCertificateAuthorityResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCertificateAuthorityCertificateRequestTypeDef,
    GetCertificateAuthorityCertificateResponseTypeDef,
    GetCertificateAuthorityCsrRequestTypeDef,
    GetCertificateAuthorityCsrResponseTypeDef,
    GetCertificateRequestTypeDef,
    GetCertificateResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    ImportCertificateAuthorityCertificateRequestTypeDef,
    IssueCertificateRequestTypeDef,
    IssueCertificateResponseTypeDef,
    ListCertificateAuthoritiesRequestTypeDef,
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsRequestTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    PutPolicyRequestTypeDef,
    RestoreCertificateAuthorityRequestTypeDef,
    RevokeCertificateRequestTypeDef,
    TagCertificateAuthorityRequestTypeDef,
    UntagCertificateAuthorityRequestTypeDef,
    UpdateCertificateAuthorityRequestTypeDef,
)
from .waiter import (
    AuditReportCreatedWaiter,
    CertificateAuthorityCSRCreatedWaiter,
    CertificateIssuedWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ACMPCAClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ACMPCAClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html#ACMPCA.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#generate_presigned_url)
        """

    def create_certificate_authority(
        self, **kwargs: Unpack[CreateCertificateAuthorityRequestTypeDef]
    ) -> CreateCertificateAuthorityResponseTypeDef:
        """
        Creates a root or subordinate private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/create_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#create_certificate_authority)
        """

    def create_certificate_authority_audit_report(
        self, **kwargs: Unpack[CreateCertificateAuthorityAuditReportRequestTypeDef]
    ) -> CreateCertificateAuthorityAuditReportResponseTypeDef:
        """
        Creates an audit report that lists every time that your CA private key is used
        to issue a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/create_certificate_authority_audit_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#create_certificate_authority_audit_report)
        """

    def create_permission(
        self, **kwargs: Unpack[CreatePermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Grants one or more permissions on a private CA to the Certificate Manager (ACM)
        service principal (<code>acm.amazonaws.com</code>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/create_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#create_permission)
        """

    def delete_certificate_authority(
        self, **kwargs: Unpack[DeleteCertificateAuthorityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/delete_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#delete_certificate_authority)
        """

    def delete_permission(
        self, **kwargs: Unpack[DeletePermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Revokes permissions on a private CA granted to the Certificate Manager (ACM)
        service principal (acm.amazonaws.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/delete_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#delete_permission)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource-based policy attached to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#delete_policy)
        """

    def describe_certificate_authority(
        self, **kwargs: Unpack[DescribeCertificateAuthorityRequestTypeDef]
    ) -> DescribeCertificateAuthorityResponseTypeDef:
        """
        Lists information about your private certificate authority (CA) or one that has
        been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/describe_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#describe_certificate_authority)
        """

    def describe_certificate_authority_audit_report(
        self, **kwargs: Unpack[DescribeCertificateAuthorityAuditReportRequestTypeDef]
    ) -> DescribeCertificateAuthorityAuditReportResponseTypeDef:
        """
        Lists information about a specific audit report created by calling the <a
        href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a>
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/describe_certificate_authority_audit_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#describe_certificate_authority_audit_report)
        """

    def get_certificate(
        self, **kwargs: Unpack[GetCertificateRequestTypeDef]
    ) -> GetCertificateResponseTypeDef:
        """
        Retrieves a certificate from your private CA or one that has been shared with
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_certificate)
        """

    def get_certificate_authority_certificate(
        self, **kwargs: Unpack[GetCertificateAuthorityCertificateRequestTypeDef]
    ) -> GetCertificateAuthorityCertificateResponseTypeDef:
        """
        Retrieves the certificate and certificate chain for your private certificate
        authority (CA) or one that has been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_certificate_authority_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_certificate_authority_certificate)
        """

    def get_certificate_authority_csr(
        self, **kwargs: Unpack[GetCertificateAuthorityCsrRequestTypeDef]
    ) -> GetCertificateAuthorityCsrResponseTypeDef:
        """
        Retrieves the certificate signing request (CSR) for your private certificate
        authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_certificate_authority_csr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_certificate_authority_csr)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Retrieves the resource-based policy attached to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_policy)
        """

    def import_certificate_authority_certificate(
        self, **kwargs: Unpack[ImportCertificateAuthorityCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Imports a signed private CA certificate into Amazon Web Services Private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/import_certificate_authority_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#import_certificate_authority_certificate)
        """

    def issue_certificate(
        self, **kwargs: Unpack[IssueCertificateRequestTypeDef]
    ) -> IssueCertificateResponseTypeDef:
        """
        Uses your private certificate authority (CA), or one that has been shared with
        you, to issue a client certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/issue_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#issue_certificate)
        """

    def list_certificate_authorities(
        self, **kwargs: Unpack[ListCertificateAuthoritiesRequestTypeDef]
    ) -> ListCertificateAuthoritiesResponseTypeDef:
        """
        Lists the private certificate authorities that you created by using the <a
        href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/list_certificate_authorities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#list_certificate_authorities)
        """

    def list_permissions(
        self, **kwargs: Unpack[ListPermissionsRequestTypeDef]
    ) -> ListPermissionsResponseTypeDef:
        """
        List all permissions on a private CA, if any, granted to the Certificate
        Manager (ACM) service principal (acm.amazonaws.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/list_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#list_permissions)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Lists the tags, if any, that are associated with your private CA or one that
        has been shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#list_tags)
        """

    def put_policy(self, **kwargs: Unpack[PutPolicyRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a resource-based policy to a private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/put_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#put_policy)
        """

    def restore_certificate_authority(
        self, **kwargs: Unpack[RestoreCertificateAuthorityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Restores a certificate authority (CA) that is in the <code>DELETED</code> state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/restore_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#restore_certificate_authority)
        """

    def revoke_certificate(
        self, **kwargs: Unpack[RevokeCertificateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Revokes a certificate that was issued inside Amazon Web Services Private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/revoke_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#revoke_certificate)
        """

    def tag_certificate_authority(
        self, **kwargs: Unpack[TagCertificateAuthorityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to your private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/tag_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#tag_certificate_authority)
        """

    def untag_certificate_authority(
        self, **kwargs: Unpack[UntagCertificateAuthorityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove one or more tags from your private CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/untag_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#untag_certificate_authority)
        """

    def update_certificate_authority(
        self, **kwargs: Unpack[UpdateCertificateAuthorityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the status or configuration of a private certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/update_certificate_authority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#update_certificate_authority)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_certificate_authorities"]
    ) -> ListCertificateAuthoritiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags"]
    ) -> ListTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["audit_report_created"]
    ) -> AuditReportCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["certificate_authority_csr_created"]
    ) -> CertificateAuthorityCSRCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["certificate_issued"]
    ) -> CertificateIssuedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/client/#get_waiter)
        """
