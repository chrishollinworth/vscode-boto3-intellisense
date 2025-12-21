"""
Type annotations for partnercentral-account service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_account.client import PartnerCentralAccountAPIClient

    session = Session()
    client: PartnerCentralAccountAPIClient = session.client("partnercentral-account")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListConnectionInvitationsPaginator,
    ListConnectionsPaginator,
    ListPartnersPaginator,
)
from .type_defs import (
    AcceptConnectionInvitationRequestTypeDef,
    AcceptConnectionInvitationResponseTypeDef,
    AssociateAwsTrainingCertificationEmailDomainRequestTypeDef,
    CancelConnectionInvitationRequestTypeDef,
    CancelConnectionInvitationResponseTypeDef,
    CancelConnectionRequestTypeDef,
    CancelConnectionResponseTypeDef,
    CancelProfileUpdateTaskRequestTypeDef,
    CancelProfileUpdateTaskResponseTypeDef,
    CreateConnectionInvitationRequestTypeDef,
    CreateConnectionInvitationResponseTypeDef,
    CreatePartnerRequestTypeDef,
    CreatePartnerResponseTypeDef,
    DisassociateAwsTrainingCertificationEmailDomainRequestTypeDef,
    GetAllianceLeadContactRequestTypeDef,
    GetAllianceLeadContactResponseTypeDef,
    GetConnectionInvitationRequestTypeDef,
    GetConnectionInvitationResponseTypeDef,
    GetConnectionPreferencesRequestTypeDef,
    GetConnectionPreferencesResponseTypeDef,
    GetConnectionRequestTypeDef,
    GetConnectionResponseTypeDef,
    GetPartnerRequestTypeDef,
    GetPartnerResponseTypeDef,
    GetProfileUpdateTaskRequestTypeDef,
    GetProfileUpdateTaskResponseTypeDef,
    GetProfileVisibilityRequestTypeDef,
    GetProfileVisibilityResponseTypeDef,
    GetVerificationRequestTypeDef,
    GetVerificationResponseTypeDef,
    ListConnectionInvitationsRequestTypeDef,
    ListConnectionInvitationsResponseTypeDef,
    ListConnectionsRequestTypeDef,
    ListConnectionsResponseTypeDef,
    ListPartnersRequestTypeDef,
    ListPartnersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutAllianceLeadContactRequestTypeDef,
    PutAllianceLeadContactResponseTypeDef,
    PutProfileVisibilityRequestTypeDef,
    PutProfileVisibilityResponseTypeDef,
    RejectConnectionInvitationRequestTypeDef,
    RejectConnectionInvitationResponseTypeDef,
    SendEmailVerificationCodeRequestTypeDef,
    StartProfileUpdateTaskRequestTypeDef,
    StartProfileUpdateTaskResponseTypeDef,
    StartVerificationRequestTypeDef,
    StartVerificationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateConnectionPreferencesRequestTypeDef,
    UpdateConnectionPreferencesResponseTypeDef,
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

__all__ = ("PartnerCentralAccountAPIClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PartnerCentralAccountAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account.html#PartnerCentralAccountAPI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PartnerCentralAccountAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account.html#PartnerCentralAccountAPI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#generate_presigned_url)
        """

    def accept_connection_invitation(
        self, **kwargs: Unpack[AcceptConnectionInvitationRequestTypeDef]
    ) -> AcceptConnectionInvitationResponseTypeDef:
        """
        Accepts a connection invitation from another partner, establishing a formal
        partnership connection between the two parties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/accept_connection_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#accept_connection_invitation)
        """

    def associate_aws_training_certification_email_domain(
        self, **kwargs: Unpack[AssociateAwsTrainingCertificationEmailDomainRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an email domain with AWS training and certification for the partner
        account, enabling automatic verification of employee certifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/associate_aws_training_certification_email_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#associate_aws_training_certification_email_domain)
        """

    def cancel_connection(
        self, **kwargs: Unpack[CancelConnectionRequestTypeDef]
    ) -> CancelConnectionResponseTypeDef:
        """
        Cancels an existing connection between partners, terminating the partnership
        relationship.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/cancel_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#cancel_connection)
        """

    def cancel_connection_invitation(
        self, **kwargs: Unpack[CancelConnectionInvitationRequestTypeDef]
    ) -> CancelConnectionInvitationResponseTypeDef:
        """
        Cancels a pending connection invitation before it has been accepted or rejected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/cancel_connection_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#cancel_connection_invitation)
        """

    def cancel_profile_update_task(
        self, **kwargs: Unpack[CancelProfileUpdateTaskRequestTypeDef]
    ) -> CancelProfileUpdateTaskResponseTypeDef:
        """
        Cancels an in-progress profile update task, stopping any pending changes to the
        partner profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/cancel_profile_update_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#cancel_profile_update_task)
        """

    def create_connection_invitation(
        self, **kwargs: Unpack[CreateConnectionInvitationRequestTypeDef]
    ) -> CreateConnectionInvitationResponseTypeDef:
        """
        Creates a new connection invitation to establish a partnership with another
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/create_connection_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#create_connection_invitation)
        """

    def create_partner(
        self, **kwargs: Unpack[CreatePartnerRequestTypeDef]
    ) -> CreatePartnerResponseTypeDef:
        """
        Creates a new partner account in the AWS Partner Network with the specified
        details and configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/create_partner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#create_partner)
        """

    def disassociate_aws_training_certification_email_domain(
        self, **kwargs: Unpack[DisassociateAwsTrainingCertificationEmailDomainRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the association between an email domain and AWS training and
        certification for the partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/disassociate_aws_training_certification_email_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#disassociate_aws_training_certification_email_domain)
        """

    def get_alliance_lead_contact(
        self, **kwargs: Unpack[GetAllianceLeadContactRequestTypeDef]
    ) -> GetAllianceLeadContactResponseTypeDef:
        """
        Retrieves the alliance lead contact information for a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_alliance_lead_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_alliance_lead_contact)
        """

    def get_connection(
        self, **kwargs: Unpack[GetConnectionRequestTypeDef]
    ) -> GetConnectionResponseTypeDef:
        """
        Retrieves detailed information about a specific connection between partners.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_connection)
        """

    def get_connection_invitation(
        self, **kwargs: Unpack[GetConnectionInvitationRequestTypeDef]
    ) -> GetConnectionInvitationResponseTypeDef:
        """
        Retrieves detailed information about a specific connection invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_connection_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_connection_invitation)
        """

    def get_connection_preferences(
        self, **kwargs: Unpack[GetConnectionPreferencesRequestTypeDef]
    ) -> GetConnectionPreferencesResponseTypeDef:
        """
        Retrieves the connection preferences for a partner account, including access
        settings and exclusions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_connection_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_connection_preferences)
        """

    def get_partner(self, **kwargs: Unpack[GetPartnerRequestTypeDef]) -> GetPartnerResponseTypeDef:
        """
        Retrieves detailed information about a specific partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_partner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_partner)
        """

    def get_profile_update_task(
        self, **kwargs: Unpack[GetProfileUpdateTaskRequestTypeDef]
    ) -> GetProfileUpdateTaskResponseTypeDef:
        """
        Retrieves information about a specific profile update task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_profile_update_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_profile_update_task)
        """

    def get_profile_visibility(
        self, **kwargs: Unpack[GetProfileVisibilityRequestTypeDef]
    ) -> GetProfileVisibilityResponseTypeDef:
        """
        Retrieves the visibility settings for a partner profile, determining who can
        see the profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_profile_visibility.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_profile_visibility)
        """

    def get_verification(
        self, **kwargs: Unpack[GetVerificationRequestTypeDef]
    ) -> GetVerificationResponseTypeDef:
        """
        Retrieves the current status and details of a verification process for a
        partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_verification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_verification)
        """

    def list_connection_invitations(
        self, **kwargs: Unpack[ListConnectionInvitationsRequestTypeDef]
    ) -> ListConnectionInvitationsResponseTypeDef:
        """
        Lists connection invitations for the partner account, with optional filtering
        by status, type, and other criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/list_connection_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#list_connection_invitations)
        """

    def list_connections(
        self, **kwargs: Unpack[ListConnectionsRequestTypeDef]
    ) -> ListConnectionsResponseTypeDef:
        """
        Lists active connections for the partner account, with optional filtering by
        connection type and participant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/list_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#list_connections)
        """

    def list_partners(
        self, **kwargs: Unpack[ListPartnersRequestTypeDef]
    ) -> ListPartnersResponseTypeDef:
        """
        Lists partner accounts in the catalog, providing a summary view of all partners.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/list_partners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#list_partners)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a specific AWS Partner Central Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#list_tags_for_resource)
        """

    def put_alliance_lead_contact(
        self, **kwargs: Unpack[PutAllianceLeadContactRequestTypeDef]
    ) -> PutAllianceLeadContactResponseTypeDef:
        """
        Creates or updates the alliance lead contact information for a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/put_alliance_lead_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#put_alliance_lead_contact)
        """

    def put_profile_visibility(
        self, **kwargs: Unpack[PutProfileVisibilityRequestTypeDef]
    ) -> PutProfileVisibilityResponseTypeDef:
        """
        Sets the visibility level for a partner profile, controlling who can view the
        profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/put_profile_visibility.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#put_profile_visibility)
        """

    def reject_connection_invitation(
        self, **kwargs: Unpack[RejectConnectionInvitationRequestTypeDef]
    ) -> RejectConnectionInvitationResponseTypeDef:
        """
        Rejects a connection invitation from another partner, declining the partnership
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/reject_connection_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#reject_connection_invitation)
        """

    def send_email_verification_code(
        self, **kwargs: Unpack[SendEmailVerificationCodeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends an email verification code to the specified email address for account
        verification purposes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/send_email_verification_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#send_email_verification_code)
        """

    def start_profile_update_task(
        self, **kwargs: Unpack[StartProfileUpdateTaskRequestTypeDef]
    ) -> StartProfileUpdateTaskResponseTypeDef:
        """
        Initiates a profile update task to modify partner profile information
        asynchronously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/start_profile_update_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#start_profile_update_task)
        """

    def start_verification(
        self, **kwargs: Unpack[StartVerificationRequestTypeDef]
    ) -> StartVerificationResponseTypeDef:
        """
        Initiates a new verification process for a partner account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/start_verification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#start_verification)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a specified AWS Partner Central Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes specified tags from an AWS Partner Central Account resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#untag_resource)
        """

    def update_connection_preferences(
        self, **kwargs: Unpack[UpdateConnectionPreferencesRequestTypeDef]
    ) -> UpdateConnectionPreferencesResponseTypeDef:
        """
        Updates the connection preferences for a partner account, modifying access
        settings and exclusions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/update_connection_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#update_connection_preferences)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connection_invitations"]
    ) -> ListConnectionInvitationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connections"]
    ) -> ListConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_partners"]
    ) -> ListPartnersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-account/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_account/client/#get_paginator)
        """
