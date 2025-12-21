"""
Type annotations for security-ir service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_security_ir.client import SecurityIncidentResponseClient

    session = Session()
    client: SecurityIncidentResponseClient = session.client("security-ir")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCaseEditsPaginator,
    ListCasesPaginator,
    ListCommentsPaginator,
    ListInvestigationsPaginator,
    ListMembershipsPaginator,
)
from .type_defs import (
    BatchGetMemberAccountDetailsRequestTypeDef,
    BatchGetMemberAccountDetailsResponseTypeDef,
    CancelMembershipRequestTypeDef,
    CancelMembershipResponseTypeDef,
    CloseCaseRequestTypeDef,
    CloseCaseResponseTypeDef,
    CreateCaseCommentRequestTypeDef,
    CreateCaseCommentResponseTypeDef,
    CreateCaseRequestTypeDef,
    CreateCaseResponseTypeDef,
    CreateMembershipRequestTypeDef,
    CreateMembershipResponseTypeDef,
    GetCaseAttachmentDownloadUrlRequestTypeDef,
    GetCaseAttachmentDownloadUrlResponseTypeDef,
    GetCaseAttachmentUploadUrlRequestTypeDef,
    GetCaseAttachmentUploadUrlResponseTypeDef,
    GetCaseRequestTypeDef,
    GetCaseResponseTypeDef,
    GetMembershipRequestTypeDef,
    GetMembershipResponseTypeDef,
    ListCaseEditsRequestTypeDef,
    ListCaseEditsResponseTypeDef,
    ListCasesRequestTypeDef,
    ListCasesResponseTypeDef,
    ListCommentsRequestTypeDef,
    ListCommentsResponseTypeDef,
    ListInvestigationsRequestTypeDef,
    ListInvestigationsResponseTypeDef,
    ListMembershipsRequestTypeDef,
    ListMembershipsResponseTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    SendFeedbackRequestTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateCaseCommentRequestTypeDef,
    UpdateCaseCommentResponseTypeDef,
    UpdateCaseRequestTypeDef,
    UpdateCaseStatusRequestTypeDef,
    UpdateCaseStatusResponseTypeDef,
    UpdateMembershipRequestTypeDef,
    UpdateResolverTypeRequestTypeDef,
    UpdateResolverTypeResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SecurityIncidentResponseClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    SecurityIncidentResponseNotActiveException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SecurityIncidentResponseClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir.html#SecurityIncidentResponse.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SecurityIncidentResponseClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir.html#SecurityIncidentResponse.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#generate_presigned_url)
        """

    def batch_get_member_account_details(
        self, **kwargs: Unpack[BatchGetMemberAccountDetailsRequestTypeDef]
    ) -> BatchGetMemberAccountDetailsResponseTypeDef:
        """
        Provides information on whether the supplied account IDs are associated with a
        membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/batch_get_member_account_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#batch_get_member_account_details)
        """

    def cancel_membership(
        self, **kwargs: Unpack[CancelMembershipRequestTypeDef]
    ) -> CancelMembershipResponseTypeDef:
        """
        Cancels an existing membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/cancel_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#cancel_membership)
        """

    def close_case(self, **kwargs: Unpack[CloseCaseRequestTypeDef]) -> CloseCaseResponseTypeDef:
        """
        Closes an existing case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/close_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#close_case)
        """

    def create_case(self, **kwargs: Unpack[CreateCaseRequestTypeDef]) -> CreateCaseResponseTypeDef:
        """
        Creates a new case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/create_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#create_case)
        """

    def create_case_comment(
        self, **kwargs: Unpack[CreateCaseCommentRequestTypeDef]
    ) -> CreateCaseCommentResponseTypeDef:
        """
        Adds a comment to an existing case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/create_case_comment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#create_case_comment)
        """

    def create_membership(
        self, **kwargs: Unpack[CreateMembershipRequestTypeDef]
    ) -> CreateMembershipResponseTypeDef:
        """
        Creates a new membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/create_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#create_membership)
        """

    def get_case(self, **kwargs: Unpack[GetCaseRequestTypeDef]) -> GetCaseResponseTypeDef:
        """
        Returns the attributes of a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_case)
        """

    def get_case_attachment_download_url(
        self, **kwargs: Unpack[GetCaseAttachmentDownloadUrlRequestTypeDef]
    ) -> GetCaseAttachmentDownloadUrlResponseTypeDef:
        """
        Returns a Pre-Signed URL for uploading attachments into a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_case_attachment_download_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_case_attachment_download_url)
        """

    def get_case_attachment_upload_url(
        self, **kwargs: Unpack[GetCaseAttachmentUploadUrlRequestTypeDef]
    ) -> GetCaseAttachmentUploadUrlResponseTypeDef:
        """
        Uploads an attachment to a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_case_attachment_upload_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_case_attachment_upload_url)
        """

    def get_membership(
        self, **kwargs: Unpack[GetMembershipRequestTypeDef]
    ) -> GetMembershipResponseTypeDef:
        """
        Returns the attributes of a membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_membership)
        """

    def list_case_edits(
        self, **kwargs: Unpack[ListCaseEditsRequestTypeDef]
    ) -> ListCaseEditsResponseTypeDef:
        """
        Views the case history for edits made to a designated case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_case_edits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_case_edits)
        """

    def list_cases(self, **kwargs: Unpack[ListCasesRequestTypeDef]) -> ListCasesResponseTypeDef:
        """
        Lists all cases the requester has access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_cases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_cases)
        """

    def list_comments(
        self, **kwargs: Unpack[ListCommentsRequestTypeDef]
    ) -> ListCommentsResponseTypeDef:
        """
        Returns comments for a designated case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_comments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_comments)
        """

    def list_investigations(
        self, **kwargs: Unpack[ListInvestigationsRequestTypeDef]
    ) -> ListInvestigationsResponseTypeDef:
        """
        Investigation performed by an agent for a security incident...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_investigations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_investigations)
        """

    def list_memberships(
        self, **kwargs: Unpack[ListMembershipsRequestTypeDef]
    ) -> ListMembershipsResponseTypeDef:
        """
        Returns the memberships that the calling principal can access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_memberships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_memberships)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns currently configured tags on a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#list_tags_for_resource)
        """

    def send_feedback(self, **kwargs: Unpack[SendFeedbackRequestTypeDef]) -> Dict[str, Any]:
        """
        Send feedback based on response investigation action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/send_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#send_feedback)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag(s) to a designated resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag(s) from a designate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#untag_resource)
        """

    def update_case(self, **kwargs: Unpack[UpdateCaseRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an existing case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/update_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#update_case)
        """

    def update_case_comment(
        self, **kwargs: Unpack[UpdateCaseCommentRequestTypeDef]
    ) -> UpdateCaseCommentResponseTypeDef:
        """
        Updates an existing case comment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/update_case_comment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#update_case_comment)
        """

    def update_case_status(
        self, **kwargs: Unpack[UpdateCaseStatusRequestTypeDef]
    ) -> UpdateCaseStatusResponseTypeDef:
        """
        Updates the state transitions for a designated cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/update_case_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#update_case_status)
        """

    def update_membership(self, **kwargs: Unpack[UpdateMembershipRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates membership configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/update_membership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#update_membership)
        """

    def update_resolver_type(
        self, **kwargs: Unpack[UpdateResolverTypeRequestTypeDef]
    ) -> UpdateResolverTypeResponseTypeDef:
        """
        Updates the resolver type for a case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/update_resolver_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#update_resolver_type)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_case_edits"]
    ) -> ListCaseEditsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cases"]
    ) -> ListCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_comments"]
    ) -> ListCommentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_investigations"]
    ) -> ListInvestigationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_memberships"]
    ) -> ListMembershipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/security-ir/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_security_ir/client/#get_paginator)
        """
