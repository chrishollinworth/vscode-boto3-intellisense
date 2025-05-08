"""
Type annotations for ssm-contacts service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_contacts.client import SSMContactsClient

    session = Session()
    client: SSMContactsClient = session.client("ssm-contacts")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListContactChannelsPaginator,
    ListContactsPaginator,
    ListEngagementsPaginator,
    ListPageReceiptsPaginator,
    ListPageResolutionsPaginator,
    ListPagesByContactPaginator,
    ListPagesByEngagementPaginator,
    ListPreviewRotationShiftsPaginator,
    ListRotationOverridesPaginator,
    ListRotationShiftsPaginator,
    ListRotationsPaginator,
)
from .type_defs import (
    AcceptPageRequestTypeDef,
    ActivateContactChannelRequestTypeDef,
    CreateContactChannelRequestTypeDef,
    CreateContactChannelResultTypeDef,
    CreateContactRequestTypeDef,
    CreateContactResultTypeDef,
    CreateRotationOverrideRequestTypeDef,
    CreateRotationOverrideResultTypeDef,
    CreateRotationRequestTypeDef,
    CreateRotationResultTypeDef,
    DeactivateContactChannelRequestTypeDef,
    DeleteContactChannelRequestTypeDef,
    DeleteContactRequestTypeDef,
    DeleteRotationOverrideRequestTypeDef,
    DeleteRotationRequestTypeDef,
    DescribeEngagementRequestTypeDef,
    DescribeEngagementResultTypeDef,
    DescribePageRequestTypeDef,
    DescribePageResultTypeDef,
    GetContactChannelRequestTypeDef,
    GetContactChannelResultTypeDef,
    GetContactPolicyRequestTypeDef,
    GetContactPolicyResultTypeDef,
    GetContactRequestTypeDef,
    GetContactResultTypeDef,
    GetRotationOverrideRequestTypeDef,
    GetRotationOverrideResultTypeDef,
    GetRotationRequestTypeDef,
    GetRotationResultTypeDef,
    ListContactChannelsRequestTypeDef,
    ListContactChannelsResultTypeDef,
    ListContactsRequestTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsRequestTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsRequestTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPageResolutionsRequestTypeDef,
    ListPageResolutionsResultTypeDef,
    ListPagesByContactRequestTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementRequestTypeDef,
    ListPagesByEngagementResultTypeDef,
    ListPreviewRotationShiftsRequestTypeDef,
    ListPreviewRotationShiftsResultTypeDef,
    ListRotationOverridesRequestTypeDef,
    ListRotationOverridesResultTypeDef,
    ListRotationShiftsRequestTypeDef,
    ListRotationShiftsResultTypeDef,
    ListRotationsRequestTypeDef,
    ListRotationsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PutContactPolicyRequestTypeDef,
    SendActivationCodeRequestTypeDef,
    StartEngagementRequestTypeDef,
    StartEngagementResultTypeDef,
    StopEngagementRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateContactChannelRequestTypeDef,
    UpdateContactRequestTypeDef,
    UpdateRotationRequestTypeDef,
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

__all__ = ("SSMContactsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DataEncryptionException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SSMContactsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSMContactsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#generate_presigned_url)
        """

    def accept_page(self, **kwargs: Unpack[AcceptPageRequestTypeDef]) -> Dict[str, Any]:
        """
        Used to acknowledge an engagement to a contact channel during an incident.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/accept_page.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#accept_page)
        """

    def activate_contact_channel(
        self, **kwargs: Unpack[ActivateContactChannelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Activates a contact's contact channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/activate_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#activate_contact_channel)
        """

    def create_contact(
        self, **kwargs: Unpack[CreateContactRequestTypeDef]
    ) -> CreateContactResultTypeDef:
        """
        Contacts are either the contacts that Incident Manager engages during an
        incident or the escalation plans that Incident Manager uses to engage contacts
        in phases during an incident.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/create_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#create_contact)
        """

    def create_contact_channel(
        self, **kwargs: Unpack[CreateContactChannelRequestTypeDef]
    ) -> CreateContactChannelResultTypeDef:
        """
        A contact channel is the method that Incident Manager uses to engage your
        contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/create_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#create_contact_channel)
        """

    def create_rotation(
        self, **kwargs: Unpack[CreateRotationRequestTypeDef]
    ) -> CreateRotationResultTypeDef:
        """
        Creates a rotation in an on-call schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/create_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#create_rotation)
        """

    def create_rotation_override(
        self, **kwargs: Unpack[CreateRotationOverrideRequestTypeDef]
    ) -> CreateRotationOverrideResultTypeDef:
        """
        Creates an override for a rotation in an on-call schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/create_rotation_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#create_rotation_override)
        """

    def deactivate_contact_channel(
        self, **kwargs: Unpack[DeactivateContactChannelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        To no longer receive Incident Manager engagements to a contact channel, you can
        deactivate the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/deactivate_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#deactivate_contact_channel)
        """

    def delete_contact(self, **kwargs: Unpack[DeleteContactRequestTypeDef]) -> Dict[str, Any]:
        """
        To remove a contact from Incident Manager, you can delete the contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/delete_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#delete_contact)
        """

    def delete_contact_channel(
        self, **kwargs: Unpack[DeleteContactChannelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        To no longer receive engagements on a contact channel, you can delete the
        channel from a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/delete_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#delete_contact_channel)
        """

    def delete_rotation(self, **kwargs: Unpack[DeleteRotationRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a rotation from the system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/delete_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#delete_rotation)
        """

    def delete_rotation_override(
        self, **kwargs: Unpack[DeleteRotationOverrideRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing override for an on-call rotation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/delete_rotation_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#delete_rotation_override)
        """

    def describe_engagement(
        self, **kwargs: Unpack[DescribeEngagementRequestTypeDef]
    ) -> DescribeEngagementResultTypeDef:
        """
        Incident Manager uses engagements to engage contacts and escalation plans
        during an incident.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/describe_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#describe_engagement)
        """

    def describe_page(
        self, **kwargs: Unpack[DescribePageRequestTypeDef]
    ) -> DescribePageResultTypeDef:
        """
        Lists details of the engagement to a contact channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/describe_page.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#describe_page)
        """

    def get_contact(self, **kwargs: Unpack[GetContactRequestTypeDef]) -> GetContactResultTypeDef:
        """
        Retrieves information about the specified contact or escalation plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_contact)
        """

    def get_contact_channel(
        self, **kwargs: Unpack[GetContactChannelRequestTypeDef]
    ) -> GetContactChannelResultTypeDef:
        """
        List details about a specific contact channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_contact_channel)
        """

    def get_contact_policy(
        self, **kwargs: Unpack[GetContactPolicyRequestTypeDef]
    ) -> GetContactPolicyResultTypeDef:
        """
        Retrieves the resource policies attached to the specified contact or escalation
        plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_contact_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_contact_policy)
        """

    def get_rotation(self, **kwargs: Unpack[GetRotationRequestTypeDef]) -> GetRotationResultTypeDef:
        """
        Retrieves information about an on-call rotation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_rotation)
        """

    def get_rotation_override(
        self, **kwargs: Unpack[GetRotationOverrideRequestTypeDef]
    ) -> GetRotationOverrideResultTypeDef:
        """
        Retrieves information about an override to an on-call rotation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_rotation_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_rotation_override)
        """

    def list_contact_channels(
        self, **kwargs: Unpack[ListContactChannelsRequestTypeDef]
    ) -> ListContactChannelsResultTypeDef:
        """
        Lists all contact channels for the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_contact_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_contact_channels)
        """

    def list_contacts(
        self, **kwargs: Unpack[ListContactsRequestTypeDef]
    ) -> ListContactsResultTypeDef:
        """
        Lists all contacts and escalation plans in Incident Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_contacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_contacts)
        """

    def list_engagements(
        self, **kwargs: Unpack[ListEngagementsRequestTypeDef]
    ) -> ListEngagementsResultTypeDef:
        """
        Lists all engagements that have happened in an incident.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_engagements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_engagements)
        """

    def list_page_receipts(
        self, **kwargs: Unpack[ListPageReceiptsRequestTypeDef]
    ) -> ListPageReceiptsResultTypeDef:
        """
        Lists all of the engagements to contact channels that have been acknowledged.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_page_receipts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_page_receipts)
        """

    def list_page_resolutions(
        self, **kwargs: Unpack[ListPageResolutionsRequestTypeDef]
    ) -> ListPageResolutionsResultTypeDef:
        """
        Returns the resolution path of an engagement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_page_resolutions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_page_resolutions)
        """

    def list_pages_by_contact(
        self, **kwargs: Unpack[ListPagesByContactRequestTypeDef]
    ) -> ListPagesByContactResultTypeDef:
        """
        Lists the engagements to a contact's contact channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_pages_by_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_pages_by_contact)
        """

    def list_pages_by_engagement(
        self, **kwargs: Unpack[ListPagesByEngagementRequestTypeDef]
    ) -> ListPagesByEngagementResultTypeDef:
        """
        Lists the engagements to contact channels that occurred by engaging a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_pages_by_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_pages_by_engagement)
        """

    def list_preview_rotation_shifts(
        self, **kwargs: Unpack[ListPreviewRotationShiftsRequestTypeDef]
    ) -> ListPreviewRotationShiftsResultTypeDef:
        """
        Returns a list of shifts based on rotation configuration parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_preview_rotation_shifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_preview_rotation_shifts)
        """

    def list_rotation_overrides(
        self, **kwargs: Unpack[ListRotationOverridesRequestTypeDef]
    ) -> ListRotationOverridesResultTypeDef:
        """
        Retrieves a list of overrides currently specified for an on-call rotation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_rotation_overrides.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_rotation_overrides)
        """

    def list_rotation_shifts(
        self, **kwargs: Unpack[ListRotationShiftsRequestTypeDef]
    ) -> ListRotationShiftsResultTypeDef:
        """
        Returns a list of shifts generated by an existing rotation in the system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_rotation_shifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_rotation_shifts)
        """

    def list_rotations(
        self, **kwargs: Unpack[ListRotationsRequestTypeDef]
    ) -> ListRotationsResultTypeDef:
        """
        Retrieves a list of on-call rotations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_rotations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_rotations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Lists the tags of an escalation plan or contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#list_tags_for_resource)
        """

    def put_contact_policy(
        self, **kwargs: Unpack[PutContactPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds a resource policy to the specified contact or escalation plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/put_contact_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#put_contact_policy)
        """

    def send_activation_code(
        self, **kwargs: Unpack[SendActivationCodeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends an activation code to a contact channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/send_activation_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#send_activation_code)
        """

    def start_engagement(
        self, **kwargs: Unpack[StartEngagementRequestTypeDef]
    ) -> StartEngagementResultTypeDef:
        """
        Starts an engagement to a contact or escalation plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/start_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#start_engagement)
        """

    def stop_engagement(self, **kwargs: Unpack[StopEngagementRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops an engagement before it finishes the final stage of the escalation plan
        or engagement plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/stop_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#stop_engagement)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a contact or escalation plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#untag_resource)
        """

    def update_contact(self, **kwargs: Unpack[UpdateContactRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the contact or escalation plan specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/update_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#update_contact)
        """

    def update_contact_channel(
        self, **kwargs: Unpack[UpdateContactChannelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a contact's contact channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/update_contact_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#update_contact_channel)
        """

    def update_rotation(self, **kwargs: Unpack[UpdateRotationRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the information specified for an on-call rotation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/update_rotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#update_rotation)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contact_channels"]
    ) -> ListContactChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contacts"]
    ) -> ListContactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_engagements"]
    ) -> ListEngagementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_page_receipts"]
    ) -> ListPageReceiptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_page_resolutions"]
    ) -> ListPageResolutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pages_by_contact"]
    ) -> ListPagesByContactPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pages_by_engagement"]
    ) -> ListPagesByEngagementPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_preview_rotation_shifts"]
    ) -> ListPreviewRotationShiftsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rotation_overrides"]
    ) -> ListRotationOverridesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rotation_shifts"]
    ) -> ListRotationShiftsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rotations"]
    ) -> ListRotationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/client/#get_paginator)
        """
