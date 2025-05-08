"""
Type annotations for pinpoint-sms-voice-v2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

    session = Session()
    client: PinpointSMSVoiceV2Client = session.client("pinpoint-sms-voice-v2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeProtectConfigurationsPaginator,
    DescribeRegistrationAttachmentsPaginator,
    DescribeRegistrationFieldDefinitionsPaginator,
    DescribeRegistrationFieldValuesPaginator,
    DescribeRegistrationSectionDefinitionsPaginator,
    DescribeRegistrationsPaginator,
    DescribeRegistrationTypeDefinitionsPaginator,
    DescribeRegistrationVersionsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    DescribeVerifiedDestinationNumbersPaginator,
    ListPoolOriginationIdentitiesPaginator,
    ListProtectConfigurationRuleSetNumberOverridesPaginator,
    ListRegistrationAssociationsPaginator,
)
from .type_defs import (
    AssociateOriginationIdentityRequestTypeDef,
    AssociateOriginationIdentityResultTypeDef,
    AssociateProtectConfigurationRequestTypeDef,
    AssociateProtectConfigurationResultTypeDef,
    CreateConfigurationSetRequestTypeDef,
    CreateConfigurationSetResultTypeDef,
    CreateEventDestinationRequestTypeDef,
    CreateEventDestinationResultTypeDef,
    CreateOptOutListRequestTypeDef,
    CreateOptOutListResultTypeDef,
    CreatePoolRequestTypeDef,
    CreatePoolResultTypeDef,
    CreateProtectConfigurationRequestTypeDef,
    CreateProtectConfigurationResultTypeDef,
    CreateRegistrationAssociationRequestTypeDef,
    CreateRegistrationAssociationResultTypeDef,
    CreateRegistrationAttachmentRequestTypeDef,
    CreateRegistrationAttachmentResultTypeDef,
    CreateRegistrationRequestTypeDef,
    CreateRegistrationResultTypeDef,
    CreateRegistrationVersionRequestTypeDef,
    CreateRegistrationVersionResultTypeDef,
    CreateVerifiedDestinationNumberRequestTypeDef,
    CreateVerifiedDestinationNumberResultTypeDef,
    DeleteAccountDefaultProtectConfigurationResultTypeDef,
    DeleteConfigurationSetRequestTypeDef,
    DeleteConfigurationSetResultTypeDef,
    DeleteDefaultMessageTypeRequestTypeDef,
    DeleteDefaultMessageTypeResultTypeDef,
    DeleteDefaultSenderIdRequestTypeDef,
    DeleteDefaultSenderIdResultTypeDef,
    DeleteEventDestinationRequestTypeDef,
    DeleteEventDestinationResultTypeDef,
    DeleteKeywordRequestTypeDef,
    DeleteKeywordResultTypeDef,
    DeleteMediaMessageSpendLimitOverrideResultTypeDef,
    DeleteOptedOutNumberRequestTypeDef,
    DeleteOptedOutNumberResultTypeDef,
    DeleteOptOutListRequestTypeDef,
    DeleteOptOutListResultTypeDef,
    DeletePoolRequestTypeDef,
    DeletePoolResultTypeDef,
    DeleteProtectConfigurationRequestTypeDef,
    DeleteProtectConfigurationResultTypeDef,
    DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef,
    DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef,
    DeleteRegistrationAttachmentRequestTypeDef,
    DeleteRegistrationAttachmentResultTypeDef,
    DeleteRegistrationFieldValueRequestTypeDef,
    DeleteRegistrationFieldValueResultTypeDef,
    DeleteRegistrationRequestTypeDef,
    DeleteRegistrationResultTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteResourcePolicyResultTypeDef,
    DeleteTextMessageSpendLimitOverrideResultTypeDef,
    DeleteVerifiedDestinationNumberRequestTypeDef,
    DeleteVerifiedDestinationNumberResultTypeDef,
    DeleteVoiceMessageSpendLimitOverrideResultTypeDef,
    DescribeAccountAttributesRequestTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAccountLimitsRequestTypeDef,
    DescribeAccountLimitsResultTypeDef,
    DescribeConfigurationSetsRequestTypeDef,
    DescribeConfigurationSetsResultTypeDef,
    DescribeKeywordsRequestTypeDef,
    DescribeKeywordsResultTypeDef,
    DescribeOptedOutNumbersRequestTypeDef,
    DescribeOptedOutNumbersResultTypeDef,
    DescribeOptOutListsRequestTypeDef,
    DescribeOptOutListsResultTypeDef,
    DescribePhoneNumbersRequestTypeDef,
    DescribePhoneNumbersResultTypeDef,
    DescribePoolsRequestTypeDef,
    DescribePoolsResultTypeDef,
    DescribeProtectConfigurationsRequestTypeDef,
    DescribeProtectConfigurationsResultTypeDef,
    DescribeRegistrationAttachmentsRequestTypeDef,
    DescribeRegistrationAttachmentsResultTypeDef,
    DescribeRegistrationFieldDefinitionsRequestTypeDef,
    DescribeRegistrationFieldDefinitionsResultTypeDef,
    DescribeRegistrationFieldValuesRequestTypeDef,
    DescribeRegistrationFieldValuesResultTypeDef,
    DescribeRegistrationSectionDefinitionsRequestTypeDef,
    DescribeRegistrationSectionDefinitionsResultTypeDef,
    DescribeRegistrationsRequestTypeDef,
    DescribeRegistrationsResultTypeDef,
    DescribeRegistrationTypeDefinitionsRequestTypeDef,
    DescribeRegistrationTypeDefinitionsResultTypeDef,
    DescribeRegistrationVersionsRequestTypeDef,
    DescribeRegistrationVersionsResultTypeDef,
    DescribeSenderIdsRequestTypeDef,
    DescribeSenderIdsResultTypeDef,
    DescribeSpendLimitsRequestTypeDef,
    DescribeSpendLimitsResultTypeDef,
    DescribeVerifiedDestinationNumbersRequestTypeDef,
    DescribeVerifiedDestinationNumbersResultTypeDef,
    DisassociateOriginationIdentityRequestTypeDef,
    DisassociateOriginationIdentityResultTypeDef,
    DisassociateProtectConfigurationRequestTypeDef,
    DisassociateProtectConfigurationResultTypeDef,
    DiscardRegistrationVersionRequestTypeDef,
    DiscardRegistrationVersionResultTypeDef,
    GetProtectConfigurationCountryRuleSetRequestTypeDef,
    GetProtectConfigurationCountryRuleSetResultTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResultTypeDef,
    ListPoolOriginationIdentitiesRequestTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef,
    ListProtectConfigurationRuleSetNumberOverridesResultTypeDef,
    ListRegistrationAssociationsRequestTypeDef,
    ListRegistrationAssociationsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PutKeywordRequestTypeDef,
    PutKeywordResultTypeDef,
    PutMessageFeedbackRequestTypeDef,
    PutMessageFeedbackResultTypeDef,
    PutOptedOutNumberRequestTypeDef,
    PutOptedOutNumberResultTypeDef,
    PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef,
    PutProtectConfigurationRuleSetNumberOverrideResultTypeDef,
    PutRegistrationFieldValueRequestTypeDef,
    PutRegistrationFieldValueResultTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResultTypeDef,
    ReleasePhoneNumberRequestTypeDef,
    ReleasePhoneNumberResultTypeDef,
    ReleaseSenderIdRequestTypeDef,
    ReleaseSenderIdResultTypeDef,
    RequestPhoneNumberRequestTypeDef,
    RequestPhoneNumberResultTypeDef,
    RequestSenderIdRequestTypeDef,
    RequestSenderIdResultTypeDef,
    SendDestinationNumberVerificationCodeRequestTypeDef,
    SendDestinationNumberVerificationCodeResultTypeDef,
    SendMediaMessageRequestTypeDef,
    SendMediaMessageResultTypeDef,
    SendTextMessageRequestTypeDef,
    SendTextMessageResultTypeDef,
    SendVoiceMessageRequestTypeDef,
    SendVoiceMessageResultTypeDef,
    SetAccountDefaultProtectConfigurationRequestTypeDef,
    SetAccountDefaultProtectConfigurationResultTypeDef,
    SetDefaultMessageFeedbackEnabledRequestTypeDef,
    SetDefaultMessageFeedbackEnabledResultTypeDef,
    SetDefaultMessageTypeRequestTypeDef,
    SetDefaultMessageTypeResultTypeDef,
    SetDefaultSenderIdRequestTypeDef,
    SetDefaultSenderIdResultTypeDef,
    SetMediaMessageSpendLimitOverrideRequestTypeDef,
    SetMediaMessageSpendLimitOverrideResultTypeDef,
    SetTextMessageSpendLimitOverrideRequestTypeDef,
    SetTextMessageSpendLimitOverrideResultTypeDef,
    SetVoiceMessageSpendLimitOverrideRequestTypeDef,
    SetVoiceMessageSpendLimitOverrideResultTypeDef,
    SubmitRegistrationVersionRequestTypeDef,
    SubmitRegistrationVersionResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateEventDestinationRequestTypeDef,
    UpdateEventDestinationResultTypeDef,
    UpdatePhoneNumberRequestTypeDef,
    UpdatePhoneNumberResultTypeDef,
    UpdatePoolRequestTypeDef,
    UpdatePoolResultTypeDef,
    UpdateProtectConfigurationCountryRuleSetRequestTypeDef,
    UpdateProtectConfigurationCountryRuleSetResultTypeDef,
    UpdateProtectConfigurationRequestTypeDef,
    UpdateProtectConfigurationResultTypeDef,
    UpdateSenderIdRequestTypeDef,
    UpdateSenderIdResultTypeDef,
    VerifyDestinationNumberRequestTypeDef,
    VerifyDestinationNumberResultTypeDef,
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

__all__ = ("PinpointSMSVoiceV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PinpointSMSVoiceV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#generate_presigned_url)
        """

    def associate_origination_identity(
        self, **kwargs: Unpack[AssociateOriginationIdentityRequestTypeDef]
    ) -> AssociateOriginationIdentityResultTypeDef:
        """
        Associates the specified origination identity with a pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/associate_origination_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#associate_origination_identity)
        """

    def associate_protect_configuration(
        self, **kwargs: Unpack[AssociateProtectConfigurationRequestTypeDef]
    ) -> AssociateProtectConfigurationResultTypeDef:
        """
        Associate a protect configuration with a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/associate_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#associate_protect_configuration)
        """

    def create_configuration_set(
        self, **kwargs: Unpack[CreateConfigurationSetRequestTypeDef]
    ) -> CreateConfigurationSetResultTypeDef:
        """
        Creates a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_configuration_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_configuration_set)
        """

    def create_event_destination(
        self, **kwargs: Unpack[CreateEventDestinationRequestTypeDef]
    ) -> CreateEventDestinationResultTypeDef:
        """
        Creates a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_event_destination)
        """

    def create_opt_out_list(
        self, **kwargs: Unpack[CreateOptOutListRequestTypeDef]
    ) -> CreateOptOutListResultTypeDef:
        """
        Creates a new opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_opt_out_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_opt_out_list)
        """

    def create_pool(self, **kwargs: Unpack[CreatePoolRequestTypeDef]) -> CreatePoolResultTypeDef:
        """
        Creates a new pool and associates the specified origination identity to the
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_pool)
        """

    def create_protect_configuration(
        self, **kwargs: Unpack[CreateProtectConfigurationRequestTypeDef]
    ) -> CreateProtectConfigurationResultTypeDef:
        """
        Create a new protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_protect_configuration)
        """

    def create_registration(
        self, **kwargs: Unpack[CreateRegistrationRequestTypeDef]
    ) -> CreateRegistrationResultTypeDef:
        """
        Creates a new registration based on the <b>RegistrationType</b> field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_registration)
        """

    def create_registration_association(
        self, **kwargs: Unpack[CreateRegistrationAssociationRequestTypeDef]
    ) -> CreateRegistrationAssociationResultTypeDef:
        """
        Associate the registration with an origination identity such as a phone number
        or sender ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_registration_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_registration_association)
        """

    def create_registration_attachment(
        self, **kwargs: Unpack[CreateRegistrationAttachmentRequestTypeDef]
    ) -> CreateRegistrationAttachmentResultTypeDef:
        """
        Create a new registration attachment to use for uploading a file or a URL to a
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_registration_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_registration_attachment)
        """

    def create_registration_version(
        self, **kwargs: Unpack[CreateRegistrationVersionRequestTypeDef]
    ) -> CreateRegistrationVersionResultTypeDef:
        """
        Create a new version of the registration and increase the <b>VersionNumber</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_registration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_registration_version)
        """

    def create_verified_destination_number(
        self, **kwargs: Unpack[CreateVerifiedDestinationNumberRequestTypeDef]
    ) -> CreateVerifiedDestinationNumberResultTypeDef:
        """
        You can only send messages to verified destination numbers when your account is
        in the sandbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/create_verified_destination_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#create_verified_destination_number)
        """

    def delete_account_default_protect_configuration(
        self,
    ) -> DeleteAccountDefaultProtectConfigurationResultTypeDef:
        """
        Removes the current account default protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_account_default_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_account_default_protect_configuration)
        """

    def delete_configuration_set(
        self, **kwargs: Unpack[DeleteConfigurationSetRequestTypeDef]
    ) -> DeleteConfigurationSetResultTypeDef:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_configuration_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_configuration_set)
        """

    def delete_default_message_type(
        self, **kwargs: Unpack[DeleteDefaultMessageTypeRequestTypeDef]
    ) -> DeleteDefaultMessageTypeResultTypeDef:
        """
        Deletes an existing default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_default_message_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_default_message_type)
        """

    def delete_default_sender_id(
        self, **kwargs: Unpack[DeleteDefaultSenderIdRequestTypeDef]
    ) -> DeleteDefaultSenderIdResultTypeDef:
        """
        Deletes an existing default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_default_sender_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_default_sender_id)
        """

    def delete_event_destination(
        self, **kwargs: Unpack[DeleteEventDestinationRequestTypeDef]
    ) -> DeleteEventDestinationResultTypeDef:
        """
        Deletes an existing event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_event_destination)
        """

    def delete_keyword(
        self, **kwargs: Unpack[DeleteKeywordRequestTypeDef]
    ) -> DeleteKeywordResultTypeDef:
        """
        Deletes an existing keyword from an origination phone number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_keyword.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_keyword)
        """

    def delete_media_message_spend_limit_override(
        self,
    ) -> DeleteMediaMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending multimedia
        messages (MMS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_media_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_media_message_spend_limit_override)
        """

    def delete_opt_out_list(
        self, **kwargs: Unpack[DeleteOptOutListRequestTypeDef]
    ) -> DeleteOptOutListResultTypeDef:
        """
        Deletes an existing opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_opt_out_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_opt_out_list)
        """

    def delete_opted_out_number(
        self, **kwargs: Unpack[DeleteOptedOutNumberRequestTypeDef]
    ) -> DeleteOptedOutNumberResultTypeDef:
        """
        Deletes an existing opted out destination phone number from the specified
        opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_opted_out_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_opted_out_number)
        """

    def delete_pool(self, **kwargs: Unpack[DeletePoolRequestTypeDef]) -> DeletePoolResultTypeDef:
        """
        Deletes an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_pool)
        """

    def delete_protect_configuration(
        self, **kwargs: Unpack[DeleteProtectConfigurationRequestTypeDef]
    ) -> DeleteProtectConfigurationResultTypeDef:
        """
        Permanently delete the protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_protect_configuration)
        """

    def delete_protect_configuration_rule_set_number_override(
        self, **kwargs: Unpack[DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef]
    ) -> DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef:
        """
        Permanently delete the protect configuration rule set number override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_protect_configuration_rule_set_number_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_protect_configuration_rule_set_number_override)
        """

    def delete_registration(
        self, **kwargs: Unpack[DeleteRegistrationRequestTypeDef]
    ) -> DeleteRegistrationResultTypeDef:
        """
        Permanently delete an existing registration from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_registration)
        """

    def delete_registration_attachment(
        self, **kwargs: Unpack[DeleteRegistrationAttachmentRequestTypeDef]
    ) -> DeleteRegistrationAttachmentResultTypeDef:
        """
        Permanently delete the specified registration attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_registration_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_registration_attachment)
        """

    def delete_registration_field_value(
        self, **kwargs: Unpack[DeleteRegistrationFieldValueRequestTypeDef]
    ) -> DeleteRegistrationFieldValueResultTypeDef:
        """
        Delete the value in a registration form field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_registration_field_value.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_registration_field_value)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> DeleteResourcePolicyResultTypeDef:
        """
        Deletes the resource-based policy document attached to the AWS End User
        Messaging SMS and Voice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_resource_policy)
        """

    def delete_text_message_spend_limit_override(
        self,
    ) -> DeleteTextMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_text_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_text_message_spend_limit_override)
        """

    def delete_verified_destination_number(
        self, **kwargs: Unpack[DeleteVerifiedDestinationNumberRequestTypeDef]
    ) -> DeleteVerifiedDestinationNumberResultTypeDef:
        """
        Delete a verified destination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_verified_destination_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_verified_destination_number)
        """

    def delete_voice_message_spend_limit_override(
        self,
    ) -> DeleteVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account level monthly spend limit override for sending voice
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/delete_voice_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#delete_voice_message_spend_limit_override)
        """

    def describe_account_attributes(
        self, **kwargs: Unpack[DescribeAccountAttributesRequestTypeDef]
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_account_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_account_attributes)
        """

    def describe_account_limits(
        self, **kwargs: Unpack[DescribeAccountLimitsRequestTypeDef]
    ) -> DescribeAccountLimitsResultTypeDef:
        """
        Describes the current AWS End User Messaging SMS and Voice SMS Voice V2
        resource quotas for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_account_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_account_limits)
        """

    def describe_configuration_sets(
        self, **kwargs: Unpack[DescribeConfigurationSetsRequestTypeDef]
    ) -> DescribeConfigurationSetsResultTypeDef:
        """
        Describes the specified configuration sets or all in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_configuration_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_configuration_sets)
        """

    def describe_keywords(
        self, **kwargs: Unpack[DescribeKeywordsRequestTypeDef]
    ) -> DescribeKeywordsResultTypeDef:
        """
        Describes the specified keywords or all keywords on your origination phone
        number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_keywords.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_keywords)
        """

    def describe_opt_out_lists(
        self, **kwargs: Unpack[DescribeOptOutListsRequestTypeDef]
    ) -> DescribeOptOutListsResultTypeDef:
        """
        Describes the specified opt-out list or all opt-out lists in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_opt_out_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_opt_out_lists)
        """

    def describe_opted_out_numbers(
        self, **kwargs: Unpack[DescribeOptedOutNumbersRequestTypeDef]
    ) -> DescribeOptedOutNumbersResultTypeDef:
        """
        Describes the specified opted out destination numbers or all opted out
        destination numbers in an opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_opted_out_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_opted_out_numbers)
        """

    def describe_phone_numbers(
        self, **kwargs: Unpack[DescribePhoneNumbersRequestTypeDef]
    ) -> DescribePhoneNumbersResultTypeDef:
        """
        Describes the specified origination phone number, or all the phone numbers in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_phone_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_phone_numbers)
        """

    def describe_pools(
        self, **kwargs: Unpack[DescribePoolsRequestTypeDef]
    ) -> DescribePoolsResultTypeDef:
        """
        Retrieves the specified pools or all pools associated with your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_pools)
        """

    def describe_protect_configurations(
        self, **kwargs: Unpack[DescribeProtectConfigurationsRequestTypeDef]
    ) -> DescribeProtectConfigurationsResultTypeDef:
        """
        Retrieves the protect configurations that match any of filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_protect_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_protect_configurations)
        """

    def describe_registration_attachments(
        self, **kwargs: Unpack[DescribeRegistrationAttachmentsRequestTypeDef]
    ) -> DescribeRegistrationAttachmentsResultTypeDef:
        """
        Retrieves the specified registration attachments or all registration
        attachments associated with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_attachments)
        """

    def describe_registration_field_definitions(
        self, **kwargs: Unpack[DescribeRegistrationFieldDefinitionsRequestTypeDef]
    ) -> DescribeRegistrationFieldDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type field definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_field_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_field_definitions)
        """

    def describe_registration_field_values(
        self, **kwargs: Unpack[DescribeRegistrationFieldValuesRequestTypeDef]
    ) -> DescribeRegistrationFieldValuesResultTypeDef:
        """
        Retrieves the specified registration field values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_field_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_field_values)
        """

    def describe_registration_section_definitions(
        self, **kwargs: Unpack[DescribeRegistrationSectionDefinitionsRequestTypeDef]
    ) -> DescribeRegistrationSectionDefinitionsResultTypeDef:
        """
        Retrieves the specified registration section definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_section_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_section_definitions)
        """

    def describe_registration_type_definitions(
        self, **kwargs: Unpack[DescribeRegistrationTypeDefinitionsRequestTypeDef]
    ) -> DescribeRegistrationTypeDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_type_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_type_definitions)
        """

    def describe_registration_versions(
        self, **kwargs: Unpack[DescribeRegistrationVersionsRequestTypeDef]
    ) -> DescribeRegistrationVersionsResultTypeDef:
        """
        Retrieves the specified registration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registration_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registration_versions)
        """

    def describe_registrations(
        self, **kwargs: Unpack[DescribeRegistrationsRequestTypeDef]
    ) -> DescribeRegistrationsResultTypeDef:
        """
        Retrieves the specified registrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_registrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_registrations)
        """

    def describe_sender_ids(
        self, **kwargs: Unpack[DescribeSenderIdsRequestTypeDef]
    ) -> DescribeSenderIdsResultTypeDef:
        """
        Describes the specified SenderIds or all SenderIds associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_sender_ids.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_sender_ids)
        """

    def describe_spend_limits(
        self, **kwargs: Unpack[DescribeSpendLimitsRequestTypeDef]
    ) -> DescribeSpendLimitsResultTypeDef:
        """
        Describes the current monthly spend limits for sending voice and text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_spend_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_spend_limits)
        """

    def describe_verified_destination_numbers(
        self, **kwargs: Unpack[DescribeVerifiedDestinationNumbersRequestTypeDef]
    ) -> DescribeVerifiedDestinationNumbersResultTypeDef:
        """
        Retrieves the specified verified destination numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/describe_verified_destination_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#describe_verified_destination_numbers)
        """

    def disassociate_origination_identity(
        self, **kwargs: Unpack[DisassociateOriginationIdentityRequestTypeDef]
    ) -> DisassociateOriginationIdentityResultTypeDef:
        """
        Removes the specified origination identity from an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/disassociate_origination_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#disassociate_origination_identity)
        """

    def disassociate_protect_configuration(
        self, **kwargs: Unpack[DisassociateProtectConfigurationRequestTypeDef]
    ) -> DisassociateProtectConfigurationResultTypeDef:
        """
        Disassociate a protect configuration from a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/disassociate_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#disassociate_protect_configuration)
        """

    def discard_registration_version(
        self, **kwargs: Unpack[DiscardRegistrationVersionRequestTypeDef]
    ) -> DiscardRegistrationVersionResultTypeDef:
        """
        Discard the current version of the registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/discard_registration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#discard_registration_version)
        """

    def get_protect_configuration_country_rule_set(
        self, **kwargs: Unpack[GetProtectConfigurationCountryRuleSetRequestTypeDef]
    ) -> GetProtectConfigurationCountryRuleSetResultTypeDef:
        """
        Retrieve the CountryRuleSet for the specified NumberCapability from a protect
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_protect_configuration_country_rule_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_protect_configuration_country_rule_set)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResultTypeDef:
        """
        Retrieves the JSON text of the resource-based policy document attached to the
        AWS End User Messaging SMS and Voice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_resource_policy)
        """

    def list_pool_origination_identities(
        self, **kwargs: Unpack[ListPoolOriginationIdentitiesRequestTypeDef]
    ) -> ListPoolOriginationIdentitiesResultTypeDef:
        """
        Lists all associated origination identities in your pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/list_pool_origination_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#list_pool_origination_identities)
        """

    def list_protect_configuration_rule_set_number_overrides(
        self, **kwargs: Unpack[ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef]
    ) -> ListProtectConfigurationRuleSetNumberOverridesResultTypeDef:
        """
        Retrieve all of the protect configuration rule set number overrides that match
        the filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/list_protect_configuration_rule_set_number_overrides.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#list_protect_configuration_rule_set_number_overrides)
        """

    def list_registration_associations(
        self, **kwargs: Unpack[ListRegistrationAssociationsRequestTypeDef]
    ) -> ListRegistrationAssociationsResultTypeDef:
        """
        Retrieve all of the origination identities that are associated with a
        registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/list_registration_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#list_registration_associations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        List all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#list_tags_for_resource)
        """

    def put_keyword(self, **kwargs: Unpack[PutKeywordRequestTypeDef]) -> PutKeywordResultTypeDef:
        """
        Creates or updates a keyword configuration on an origination phone number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_keyword.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_keyword)
        """

    def put_message_feedback(
        self, **kwargs: Unpack[PutMessageFeedbackRequestTypeDef]
    ) -> PutMessageFeedbackResultTypeDef:
        """
        Set the MessageFeedbackStatus as <code>RECEIVED</code> or <code>FAILED</code>
        for the passed in MessageId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_message_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_message_feedback)
        """

    def put_opted_out_number(
        self, **kwargs: Unpack[PutOptedOutNumberRequestTypeDef]
    ) -> PutOptedOutNumberResultTypeDef:
        """
        Creates an opted out destination phone number in the opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_opted_out_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_opted_out_number)
        """

    def put_protect_configuration_rule_set_number_override(
        self, **kwargs: Unpack[PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef]
    ) -> PutProtectConfigurationRuleSetNumberOverrideResultTypeDef:
        """
        Create or update a phone number rule override and associate it with a protect
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_protect_configuration_rule_set_number_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_protect_configuration_rule_set_number_override)
        """

    def put_registration_field_value(
        self, **kwargs: Unpack[PutRegistrationFieldValueRequestTypeDef]
    ) -> PutRegistrationFieldValueResultTypeDef:
        """
        Creates or updates a field value for a registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_registration_field_value.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_registration_field_value)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResultTypeDef:
        """
        Attaches a resource-based policy to a AWS End User Messaging SMS and Voice
        resource(phone number, sender Id, phone poll, or opt-out list) that is used for
        sharing the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#put_resource_policy)
        """

    def release_phone_number(
        self, **kwargs: Unpack[ReleasePhoneNumberRequestTypeDef]
    ) -> ReleasePhoneNumberResultTypeDef:
        """
        Releases an existing origination phone number in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/release_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#release_phone_number)
        """

    def release_sender_id(
        self, **kwargs: Unpack[ReleaseSenderIdRequestTypeDef]
    ) -> ReleaseSenderIdResultTypeDef:
        """
        Releases an existing sender ID in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/release_sender_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#release_sender_id)
        """

    def request_phone_number(
        self, **kwargs: Unpack[RequestPhoneNumberRequestTypeDef]
    ) -> RequestPhoneNumberResultTypeDef:
        """
        Request an origination phone number for use in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/request_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#request_phone_number)
        """

    def request_sender_id(
        self, **kwargs: Unpack[RequestSenderIdRequestTypeDef]
    ) -> RequestSenderIdResultTypeDef:
        """
        Request a new sender ID that doesn't require registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/request_sender_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#request_sender_id)
        """

    def send_destination_number_verification_code(
        self, **kwargs: Unpack[SendDestinationNumberVerificationCodeRequestTypeDef]
    ) -> SendDestinationNumberVerificationCodeResultTypeDef:
        """
        Before you can send test messages to a verified destination phone number you
        need to opt-in the verified destination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/send_destination_number_verification_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#send_destination_number_verification_code)
        """

    def send_media_message(
        self, **kwargs: Unpack[SendMediaMessageRequestTypeDef]
    ) -> SendMediaMessageResultTypeDef:
        """
        Creates a new multimedia message (MMS) and sends it to a recipient's phone
        number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/send_media_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#send_media_message)
        """

    def send_text_message(
        self, **kwargs: Unpack[SendTextMessageRequestTypeDef]
    ) -> SendTextMessageResultTypeDef:
        """
        Creates a new text message and sends it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/send_text_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#send_text_message)
        """

    def send_voice_message(
        self, **kwargs: Unpack[SendVoiceMessageRequestTypeDef]
    ) -> SendVoiceMessageResultTypeDef:
        """
        Allows you to send a request that sends a voice message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/send_voice_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#send_voice_message)
        """

    def set_account_default_protect_configuration(
        self, **kwargs: Unpack[SetAccountDefaultProtectConfigurationRequestTypeDef]
    ) -> SetAccountDefaultProtectConfigurationResultTypeDef:
        """
        Set a protect configuration as your account default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_account_default_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_account_default_protect_configuration)
        """

    def set_default_message_feedback_enabled(
        self, **kwargs: Unpack[SetDefaultMessageFeedbackEnabledRequestTypeDef]
    ) -> SetDefaultMessageFeedbackEnabledResultTypeDef:
        """
        Sets a configuration set's default for message feedback.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_default_message_feedback_enabled.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_default_message_feedback_enabled)
        """

    def set_default_message_type(
        self, **kwargs: Unpack[SetDefaultMessageTypeRequestTypeDef]
    ) -> SetDefaultMessageTypeResultTypeDef:
        """
        Sets the default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_default_message_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_default_message_type)
        """

    def set_default_sender_id(
        self, **kwargs: Unpack[SetDefaultSenderIdRequestTypeDef]
    ) -> SetDefaultSenderIdResultTypeDef:
        """
        Sets default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_default_sender_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_default_sender_id)
        """

    def set_media_message_spend_limit_override(
        self, **kwargs: Unpack[SetMediaMessageSpendLimitOverrideRequestTypeDef]
    ) -> SetMediaMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending MMS messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_media_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_media_message_spend_limit_override)
        """

    def set_text_message_spend_limit_override(
        self, **kwargs: Unpack[SetTextMessageSpendLimitOverrideRequestTypeDef]
    ) -> SetTextMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_text_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_text_message_spend_limit_override)
        """

    def set_voice_message_spend_limit_override(
        self, **kwargs: Unpack[SetVoiceMessageSpendLimitOverrideRequestTypeDef]
    ) -> SetVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending voice messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/set_voice_message_spend_limit_override.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#set_voice_message_spend_limit_override)
        """

    def submit_registration_version(
        self, **kwargs: Unpack[SubmitRegistrationVersionRequestTypeDef]
    ) -> SubmitRegistrationVersionResultTypeDef:
        """
        Submit the specified registration for review and approval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/submit_registration_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#submit_registration_version)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites only the specified tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the association of the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#untag_resource)
        """

    def update_event_destination(
        self, **kwargs: Unpack[UpdateEventDestinationRequestTypeDef]
    ) -> UpdateEventDestinationResultTypeDef:
        """
        Updates an existing event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_event_destination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_event_destination)
        """

    def update_phone_number(
        self, **kwargs: Unpack[UpdatePhoneNumberRequestTypeDef]
    ) -> UpdatePhoneNumberResultTypeDef:
        """
        Updates the configuration of an existing origination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_phone_number)
        """

    def update_pool(self, **kwargs: Unpack[UpdatePoolRequestTypeDef]) -> UpdatePoolResultTypeDef:
        """
        Updates the configuration of an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_pool)
        """

    def update_protect_configuration(
        self, **kwargs: Unpack[UpdateProtectConfigurationRequestTypeDef]
    ) -> UpdateProtectConfigurationResultTypeDef:
        """
        Update the setting for an existing protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_protect_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_protect_configuration)
        """

    def update_protect_configuration_country_rule_set(
        self, **kwargs: Unpack[UpdateProtectConfigurationCountryRuleSetRequestTypeDef]
    ) -> UpdateProtectConfigurationCountryRuleSetResultTypeDef:
        """
        Update a country rule set to <code>ALLOW</code>, <code>BLOCK</code>,
        <code>MONITOR</code>, or <code>FILTER</code> messages to be sent to the
        specified destination counties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_protect_configuration_country_rule_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_protect_configuration_country_rule_set)
        """

    def update_sender_id(
        self, **kwargs: Unpack[UpdateSenderIdRequestTypeDef]
    ) -> UpdateSenderIdResultTypeDef:
        """
        Updates the configuration of an existing sender ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/update_sender_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#update_sender_id)
        """

    def verify_destination_number(
        self, **kwargs: Unpack[VerifyDestinationNumberRequestTypeDef]
    ) -> VerifyDestinationNumberResultTypeDef:
        """
        Use the verification code that was received by the verified destination phone
        number to opt-in the verified destination phone number to receive more
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/verify_destination_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#verify_destination_number)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_account_attributes"]
    ) -> DescribeAccountAttributesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_configuration_sets"]
    ) -> DescribeConfigurationSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_keywords"]
    ) -> DescribeKeywordsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_opt_out_lists"]
    ) -> DescribeOptOutListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_opted_out_numbers"]
    ) -> DescribeOptedOutNumbersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_phone_numbers"]
    ) -> DescribePhoneNumbersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_pools"]
    ) -> DescribePoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_protect_configurations"]
    ) -> DescribeProtectConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_attachments"]
    ) -> DescribeRegistrationAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_field_definitions"]
    ) -> DescribeRegistrationFieldDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_field_values"]
    ) -> DescribeRegistrationFieldValuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_section_definitions"]
    ) -> DescribeRegistrationSectionDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_type_definitions"]
    ) -> DescribeRegistrationTypeDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registration_versions"]
    ) -> DescribeRegistrationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_registrations"]
    ) -> DescribeRegistrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_sender_ids"]
    ) -> DescribeSenderIdsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_spend_limits"]
    ) -> DescribeSpendLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_destination_numbers"]
    ) -> DescribeVerifiedDestinationNumbersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pool_origination_identities"]
    ) -> ListPoolOriginationIdentitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protect_configuration_rule_set_number_overrides"]
    ) -> ListProtectConfigurationRuleSetNumberOverridesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_registration_associations"]
    ) -> ListRegistrationAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client/#get_paginator)
        """
