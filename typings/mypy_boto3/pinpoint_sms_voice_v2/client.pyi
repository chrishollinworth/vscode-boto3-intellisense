"""
Type annotations for pinpoint-sms-voice-v2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Client

    client: PinpointSMSVoiceV2Client = boto3.client("pinpoint-sms-voice-v2")
    ```
"""

import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    DestinationCountryParameterKeyType,
    EventTypeType,
    KeywordActionType,
    LanguageCodeType,
    MessageTypeType,
    NumberCapabilityType,
    RequestableNumberTypeType,
    VerificationChannelType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)
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
    ListRegistrationAssociationsPaginator,
)
from .type_defs import (
    AssociateOriginationIdentityResultTypeDef,
    AssociateProtectConfigurationResultTypeDef,
    CloudWatchLogsDestinationTypeDef,
    ConfigurationSetFilterTypeDef,
    CreateConfigurationSetResultTypeDef,
    CreateEventDestinationResultTypeDef,
    CreateOptOutListResultTypeDef,
    CreatePoolResultTypeDef,
    CreateProtectConfigurationResultTypeDef,
    CreateRegistrationAssociationResultTypeDef,
    CreateRegistrationAttachmentResultTypeDef,
    CreateRegistrationResultTypeDef,
    CreateRegistrationVersionResultTypeDef,
    CreateVerifiedDestinationNumberResultTypeDef,
    DeleteAccountDefaultProtectConfigurationResultTypeDef,
    DeleteConfigurationSetResultTypeDef,
    DeleteDefaultMessageTypeResultTypeDef,
    DeleteDefaultSenderIdResultTypeDef,
    DeleteEventDestinationResultTypeDef,
    DeleteKeywordResultTypeDef,
    DeleteMediaMessageSpendLimitOverrideResultTypeDef,
    DeleteOptedOutNumberResultTypeDef,
    DeleteOptOutListResultTypeDef,
    DeletePoolResultTypeDef,
    DeleteProtectConfigurationResultTypeDef,
    DeleteRegistrationAttachmentResultTypeDef,
    DeleteRegistrationFieldValueResultTypeDef,
    DeleteRegistrationResultTypeDef,
    DeleteTextMessageSpendLimitOverrideResultTypeDef,
    DeleteVerifiedDestinationNumberResultTypeDef,
    DeleteVoiceMessageSpendLimitOverrideResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAccountLimitsResultTypeDef,
    DescribeConfigurationSetsResultTypeDef,
    DescribeKeywordsResultTypeDef,
    DescribeOptedOutNumbersResultTypeDef,
    DescribeOptOutListsResultTypeDef,
    DescribePhoneNumbersResultTypeDef,
    DescribePoolsResultTypeDef,
    DescribeProtectConfigurationsResultTypeDef,
    DescribeRegistrationAttachmentsResultTypeDef,
    DescribeRegistrationFieldDefinitionsResultTypeDef,
    DescribeRegistrationFieldValuesResultTypeDef,
    DescribeRegistrationSectionDefinitionsResultTypeDef,
    DescribeRegistrationsResultTypeDef,
    DescribeRegistrationTypeDefinitionsResultTypeDef,
    DescribeRegistrationVersionsResultTypeDef,
    DescribeSenderIdsResultTypeDef,
    DescribeSpendLimitsResultTypeDef,
    DescribeVerifiedDestinationNumbersResultTypeDef,
    DisassociateOriginationIdentityResultTypeDef,
    DisassociateProtectConfigurationResultTypeDef,
    DiscardRegistrationVersionResultTypeDef,
    GetProtectConfigurationCountryRuleSetResultTypeDef,
    KeywordFilterTypeDef,
    KinesisFirehoseDestinationTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    ListRegistrationAssociationsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    OptedOutFilterTypeDef,
    PhoneNumberFilterTypeDef,
    PoolFilterTypeDef,
    PoolOriginationIdentitiesFilterTypeDef,
    ProtectConfigurationCountryRuleSetInformationTypeDef,
    ProtectConfigurationFilterTypeDef,
    PutKeywordResultTypeDef,
    PutOptedOutNumberResultTypeDef,
    PutRegistrationFieldValueResultTypeDef,
    RegistrationAssociationFilterTypeDef,
    RegistrationAttachmentFilterTypeDef,
    RegistrationFilterTypeDef,
    RegistrationTypeFilterTypeDef,
    RegistrationVersionFilterTypeDef,
    ReleasePhoneNumberResultTypeDef,
    ReleaseSenderIdResultTypeDef,
    RequestPhoneNumberResultTypeDef,
    RequestSenderIdResultTypeDef,
    SendDestinationNumberVerificationCodeResultTypeDef,
    SenderIdAndCountryTypeDef,
    SenderIdFilterTypeDef,
    SendMediaMessageResultTypeDef,
    SendTextMessageResultTypeDef,
    SendVoiceMessageResultTypeDef,
    SetAccountDefaultProtectConfigurationResultTypeDef,
    SetDefaultMessageTypeResultTypeDef,
    SetDefaultSenderIdResultTypeDef,
    SetMediaMessageSpendLimitOverrideResultTypeDef,
    SetTextMessageSpendLimitOverrideResultTypeDef,
    SetVoiceMessageSpendLimitOverrideResultTypeDef,
    SnsDestinationTypeDef,
    SubmitRegistrationVersionResultTypeDef,
    TagTypeDef,
    UpdateEventDestinationResultTypeDef,
    UpdatePhoneNumberResultTypeDef,
    UpdatePoolResultTypeDef,
    UpdateProtectConfigurationCountryRuleSetResultTypeDef,
    UpdateProtectConfigurationResultTypeDef,
    UpdateSenderIdResultTypeDef,
    VerifiedDestinationNumberFilterTypeDef,
    VerifyDestinationNumberResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PinpointSMSVoiceV2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceV2Client exceptions.
        """

    def associate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = None
    ) -> AssociateOriginationIdentityResultTypeDef:
        """
        Associates the specified origination identity with a pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.associate_origination_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#associate_origination_identity)
        """

    def associate_protect_configuration(
        self, *, ProtectConfigurationId: str, ConfigurationSetName: str
    ) -> AssociateProtectConfigurationResultTypeDef:
        """
        Associate a protect configuration with a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.associate_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#associate_protect_configuration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#close)
        """

    def create_configuration_set(
        self, *, ConfigurationSetName: str, Tags: List["TagTypeDef"] = None, ClientToken: str = None
    ) -> CreateConfigurationSetResultTypeDef:
        """
        Creates a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_configuration_set)
        """

    def create_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        MatchingEventTypes: List[EventTypeType],
        CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef" = None,
        KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef" = None,
        SnsDestination: "SnsDestinationTypeDef" = None,
        ClientToken: str = None
    ) -> CreateEventDestinationResultTypeDef:
        """
        Creates a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_event_destination)
        """

    def create_opt_out_list(
        self, *, OptOutListName: str, Tags: List["TagTypeDef"] = None, ClientToken: str = None
    ) -> CreateOptOutListResultTypeDef:
        """
        Creates a new opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_opt_out_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_opt_out_list)
        """

    def create_pool(
        self,
        *,
        OriginationIdentity: str,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreatePoolResultTypeDef:
        """
        Creates a new pool and associates the specified origination identity to the
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_pool)
        """

    def create_protect_configuration(
        self,
        *,
        ClientToken: str = None,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProtectConfigurationResultTypeDef:
        """
        Create a new protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_protect_configuration)
        """

    def create_registration(
        self, *, RegistrationType: str, Tags: List["TagTypeDef"] = None, ClientToken: str = None
    ) -> CreateRegistrationResultTypeDef:
        """
        Creates a new registration based on the **RegistrationType** field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_registration)
        """

    def create_registration_association(
        self, *, RegistrationId: str, ResourceId: str
    ) -> CreateRegistrationAssociationResultTypeDef:
        """
        Associate the registration with an origination identity such as a phone number
        or sender ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_registration_association)
        """

    def create_registration_attachment(
        self,
        *,
        AttachmentBody: Union[bytes, IO[bytes], StreamingBody] = None,
        AttachmentUrl: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateRegistrationAttachmentResultTypeDef:
        """
        Create a new registration attachment to use for uploading a file or a URL to a
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_registration_attachment)
        """

    def create_registration_version(
        self, *, RegistrationId: str
    ) -> CreateRegistrationVersionResultTypeDef:
        """
        Create a new version of the registration and increase the **VersionNumber**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_registration_version)
        """

    def create_verified_destination_number(
        self,
        *,
        DestinationPhoneNumber: str,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateVerifiedDestinationNumberResultTypeDef:
        """
        You can only send messages to verified destination numbers when your account is
        in the sandbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_verified_destination_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#create_verified_destination_number)
        """

    def delete_account_default_protect_configuration(
        self,
    ) -> DeleteAccountDefaultProtectConfigurationResultTypeDef:
        """
        Removes the current account default protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_account_default_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_account_default_protect_configuration)
        """

    def delete_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> DeleteConfigurationSetResultTypeDef:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_configuration_set)
        """

    def delete_default_message_type(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultMessageTypeResultTypeDef:
        """
        Deletes an existing default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_message_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_default_message_type)
        """

    def delete_default_sender_id(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultSenderIdResultTypeDef:
        """
        Deletes an existing default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_default_sender_id)
        """

    def delete_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> DeleteEventDestinationResultTypeDef:
        """
        Deletes an existing event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_event_destination)
        """

    def delete_keyword(
        self, *, OriginationIdentity: str, Keyword: str
    ) -> DeleteKeywordResultTypeDef:
        """
        Deletes an existing keyword from an origination phone number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_keyword)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_keyword)
        """

    def delete_media_message_spend_limit_override(
        self,
    ) -> DeleteMediaMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending multimedia
        messages (MMS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_media_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_media_message_spend_limit_override)
        """

    def delete_opt_out_list(self, *, OptOutListName: str) -> DeleteOptOutListResultTypeDef:
        """
        Deletes an existing opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opt_out_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_opt_out_list)
        """

    def delete_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> DeleteOptedOutNumberResultTypeDef:
        """
        Deletes an existing opted out destination phone number from the specified opt-
        out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opted_out_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_opted_out_number)
        """

    def delete_pool(self, *, PoolId: str) -> DeletePoolResultTypeDef:
        """
        Deletes an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_pool)
        """

    def delete_protect_configuration(
        self, *, ProtectConfigurationId: str
    ) -> DeleteProtectConfigurationResultTypeDef:
        """
        Permanently delete the protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_protect_configuration)
        """

    def delete_registration(self, *, RegistrationId: str) -> DeleteRegistrationResultTypeDef:
        """
        Permanently delete an existing registration from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_registration)
        """

    def delete_registration_attachment(
        self, *, RegistrationAttachmentId: str
    ) -> DeleteRegistrationAttachmentResultTypeDef:
        """
        Permanently delete the specified registration attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_registration_attachment)
        """

    def delete_registration_field_value(
        self, *, RegistrationId: str, FieldPath: str
    ) -> DeleteRegistrationFieldValueResultTypeDef:
        """
        Delete the value in a registration form field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration_field_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_registration_field_value)
        """

    def delete_text_message_spend_limit_override(
        self,
    ) -> DeleteTextMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_text_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_text_message_spend_limit_override)
        """

    def delete_verified_destination_number(
        self, *, VerifiedDestinationNumberId: str
    ) -> DeleteVerifiedDestinationNumberResultTypeDef:
        """
        Delete a verified destination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_verified_destination_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_verified_destination_number)
        """

    def delete_voice_message_spend_limit_override(
        self,
    ) -> DeleteVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account level monthly spend limit override for sending voice
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_voice_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#delete_voice_message_spend_limit_override)
        """

    def describe_account_attributes(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_account_attributes)
        """

    def describe_account_limits(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAccountLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint SMS Voice V2 resource quotas for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_account_limits)
        """

    def describe_configuration_sets(
        self,
        *,
        ConfigurationSetNames: List[str] = None,
        Filters: List["ConfigurationSetFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeConfigurationSetsResultTypeDef:
        """
        Describes the specified configuration sets or all in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_configuration_sets)
        """

    def describe_keywords(
        self,
        *,
        OriginationIdentity: str,
        Keywords: List[str] = None,
        Filters: List["KeywordFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeKeywordsResultTypeDef:
        """
        Describes the specified keywords or all keywords on your origination phone
        number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_keywords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_keywords)
        """

    def describe_opt_out_lists(
        self, *, OptOutListNames: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeOptOutListsResultTypeDef:
        """
        Describes the specified opt-out list or all opt-out lists in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opt_out_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_opt_out_lists)
        """

    def describe_opted_out_numbers(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: List[str] = None,
        Filters: List["OptedOutFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeOptedOutNumbersResultTypeDef:
        """
        Describes the specified opted out destination numbers or all opted out
        destination numbers in an opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opted_out_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_opted_out_numbers)
        """

    def describe_phone_numbers(
        self,
        *,
        PhoneNumberIds: List[str] = None,
        Filters: List["PhoneNumberFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribePhoneNumbersResultTypeDef:
        """
        Describes the specified origination phone number, or all the phone numbers in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_phone_numbers)
        """

    def describe_pools(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["PoolFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribePoolsResultTypeDef:
        """
        Retrieves the specified pools or all pools associated with your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_pools)
        """

    def describe_protect_configurations(
        self,
        *,
        ProtectConfigurationIds: List[str] = None,
        Filters: List["ProtectConfigurationFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeProtectConfigurationsResultTypeDef:
        """
        Retrieves the protect configurations that match any of filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_protect_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_protect_configurations)
        """

    def describe_registration_attachments(
        self,
        *,
        RegistrationAttachmentIds: List[str] = None,
        Filters: List["RegistrationAttachmentFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationAttachmentsResultTypeDef:
        """
        Retrieves the specified registration attachments or all registration attachments
        associated with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_attachments)
        """

    def describe_registration_field_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPath: str = None,
        FieldPaths: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationFieldDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type field definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_field_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_field_definitions)
        """

    def describe_registration_field_values(
        self,
        *,
        RegistrationId: str,
        VersionNumber: int = None,
        SectionPath: str = None,
        FieldPaths: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationFieldValuesResultTypeDef:
        """
        Retrieves the specified registration field values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_field_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_field_values)
        """

    def describe_registration_section_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPaths: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationSectionDefinitionsResultTypeDef:
        """
        Retrieves the specified registration section definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_section_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_section_definitions)
        """

    def describe_registration_type_definitions(
        self,
        *,
        RegistrationTypes: List[str] = None,
        Filters: List["RegistrationTypeFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationTypeDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_type_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_type_definitions)
        """

    def describe_registration_versions(
        self,
        *,
        RegistrationId: str,
        VersionNumbers: List[int] = None,
        Filters: List["RegistrationVersionFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationVersionsResultTypeDef:
        """
        Retrieves the specified registration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registration_versions)
        """

    def describe_registrations(
        self,
        *,
        RegistrationIds: List[str] = None,
        Filters: List["RegistrationFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRegistrationsResultTypeDef:
        """
        Retrieves the specified registrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_registrations)
        """

    def describe_sender_ids(
        self,
        *,
        SenderIds: List["SenderIdAndCountryTypeDef"] = None,
        Filters: List["SenderIdFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSenderIdsResultTypeDef:
        """
        Describes the specified SenderIds or all SenderIds associated with your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_sender_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_sender_ids)
        """

    def describe_spend_limits(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeSpendLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint monthly spend limits for sending voice and
        text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_spend_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_spend_limits)
        """

    def describe_verified_destination_numbers(
        self,
        *,
        VerifiedDestinationNumberIds: List[str] = None,
        DestinationPhoneNumbers: List[str] = None,
        Filters: List["VerifiedDestinationNumberFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeVerifiedDestinationNumbersResultTypeDef:
        """
        Retrieves the specified verified destiona numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_verified_destination_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#describe_verified_destination_numbers)
        """

    def disassociate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = None
    ) -> DisassociateOriginationIdentityResultTypeDef:
        """
        Removes the specified origination identity from an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.disassociate_origination_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#disassociate_origination_identity)
        """

    def disassociate_protect_configuration(
        self, *, ProtectConfigurationId: str, ConfigurationSetName: str
    ) -> DisassociateProtectConfigurationResultTypeDef:
        """
        Disassociate a protect configuration from a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.disassociate_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#disassociate_protect_configuration)
        """

    def discard_registration_version(
        self, *, RegistrationId: str
    ) -> DiscardRegistrationVersionResultTypeDef:
        """
        Discard the current version of the registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.discard_registration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#discard_registration_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#generate_presigned_url)
        """

    def get_protect_configuration_country_rule_set(
        self, *, ProtectConfigurationId: str, NumberCapability: NumberCapabilityType
    ) -> GetProtectConfigurationCountryRuleSetResultTypeDef:
        """
        Retrieve the CountryRuleSet for the specified NumberCapability from a protect
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_protect_configuration_country_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#get_protect_configuration_country_rule_set)
        """

    def list_pool_origination_identities(
        self,
        *,
        PoolId: str,
        Filters: List["PoolOriginationIdentitiesFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPoolOriginationIdentitiesResultTypeDef:
        """
        Lists all associated origination identities in your pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_pool_origination_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#list_pool_origination_identities)
        """

    def list_registration_associations(
        self,
        *,
        RegistrationId: str,
        Filters: List["RegistrationAssociationFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRegistrationAssociationsResultTypeDef:
        """
        Retreive all of the origination identies that are associated with a
        registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_registration_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#list_registration_associations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        List all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#list_tags_for_resource)
        """

    def put_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
        KeywordMessage: str,
        KeywordAction: KeywordActionType = None
    ) -> PutKeywordResultTypeDef:
        """
        Creates or updates a keyword configuration on an origination phone number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_keyword)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#put_keyword)
        """

    def put_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> PutOptedOutNumberResultTypeDef:
        """
        Creates an opted out destination phone number in the opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_opted_out_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#put_opted_out_number)
        """

    def put_registration_field_value(
        self,
        *,
        RegistrationId: str,
        FieldPath: str,
        SelectChoices: List[str] = None,
        TextValue: str = None,
        RegistrationAttachmentId: str = None
    ) -> PutRegistrationFieldValueResultTypeDef:
        """
        Creates or updates a field value for a registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_registration_field_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#put_registration_field_value)
        """

    def release_phone_number(self, *, PhoneNumberId: str) -> ReleasePhoneNumberResultTypeDef:
        """
        Releases an existing origination phone number in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#release_phone_number)
        """

    def release_sender_id(
        self, *, SenderId: str, IsoCountryCode: str
    ) -> ReleaseSenderIdResultTypeDef:
        """
        Releases an existing sender ID in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#release_sender_id)
        """

    def request_phone_number(
        self,
        *,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        NumberCapabilities: List[NumberCapabilityType],
        NumberType: RequestableNumberTypeType,
        OptOutListName: str = None,
        PoolId: str = None,
        RegistrationId: str = None,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> RequestPhoneNumberResultTypeDef:
        """
        Request an origination phone number for use in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#request_phone_number)
        """

    def request_sender_id(
        self,
        *,
        SenderId: str,
        IsoCountryCode: str,
        MessageTypes: List[MessageTypeType] = None,
        DeletionProtectionEnabled: bool = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> RequestSenderIdResultTypeDef:
        """
        Request a new sender ID that doesn't require registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#request_sender_id)
        """

    def send_destination_number_verification_code(
        self,
        *,
        VerifiedDestinationNumberId: str,
        VerificationChannel: VerificationChannelType,
        LanguageCode: LanguageCodeType = None,
        OriginationIdentity: str = None,
        ConfigurationSetName: str = None,
        Context: Dict[str, str] = None,
        DestinationCountryParameters: Dict[DestinationCountryParameterKeyType, str] = None
    ) -> SendDestinationNumberVerificationCodeResultTypeDef:
        """
        Before you can send test messages to a verified destination phone number you
        need to opt-in the verified destination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_destination_number_verification_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_destination_number_verification_code)
        """

    def send_media_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str = None,
        MediaUrls: List[str] = None,
        ConfigurationSetName: str = None,
        MaxPrice: str = None,
        TimeToLive: int = None,
        Context: Dict[str, str] = None,
        DryRun: bool = None,
        ProtectConfigurationId: str = None
    ) -> SendMediaMessageResultTypeDef:
        """
        Creates a new multimedia message (MMS) and sends it to a recipient's phone
        number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_media_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_media_message)
        """

    def send_text_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str = None,
        MessageBody: str = None,
        MessageType: MessageTypeType = None,
        Keyword: str = None,
        ConfigurationSetName: str = None,
        MaxPrice: str = None,
        TimeToLive: int = None,
        Context: Dict[str, str] = None,
        DestinationCountryParameters: Dict[DestinationCountryParameterKeyType, str] = None,
        DryRun: bool = None,
        ProtectConfigurationId: str = None
    ) -> SendTextMessageResultTypeDef:
        """
        Creates a new text message and sends it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_text_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_text_message)
        """

    def send_voice_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str = None,
        MessageBodyTextType: VoiceMessageBodyTextTypeType = None,
        VoiceId: VoiceIdType = None,
        ConfigurationSetName: str = None,
        MaxPricePerMinute: str = None,
        TimeToLive: int = None,
        Context: Dict[str, str] = None,
        DryRun: bool = None,
        ProtectConfigurationId: str = None
    ) -> SendVoiceMessageResultTypeDef:
        """
        Allows you to send a request that sends a voice message through Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_voice_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#send_voice_message)
        """

    def set_account_default_protect_configuration(
        self, *, ProtectConfigurationId: str
    ) -> SetAccountDefaultProtectConfigurationResultTypeDef:
        """
        Set a protect configuration as your account default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_account_default_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_account_default_protect_configuration)
        """

    def set_default_message_type(
        self, *, ConfigurationSetName: str, MessageType: MessageTypeType
    ) -> SetDefaultMessageTypeResultTypeDef:
        """
        Sets the default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_message_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_default_message_type)
        """

    def set_default_sender_id(
        self, *, ConfigurationSetName: str, SenderId: str
    ) -> SetDefaultSenderIdResultTypeDef:
        """
        Sets default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_default_sender_id)
        """

    def set_media_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetMediaMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending MMS messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_media_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_media_message_spend_limit_override)
        """

    def set_text_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetTextMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_text_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_text_message_spend_limit_override)
        """

    def set_voice_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending voice messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_voice_message_spend_limit_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#set_voice_message_spend_limit_override)
        """

    def submit_registration_version(
        self, *, RegistrationId: str
    ) -> SubmitRegistrationVersionResultTypeDef:
        """
        Submit the specified registration for review and approval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.submit_registration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#submit_registration_version)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or overwrites only the specified tags for the specified Amazon Pinpoint SMS
        Voice, version 2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the association of the specified tags from an Amazon Pinpoint SMS Voice
        V2 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#untag_resource)
        """

    def update_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        Enabled: bool = None,
        MatchingEventTypes: List[EventTypeType] = None,
        CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef" = None,
        KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef" = None,
        SnsDestination: "SnsDestinationTypeDef" = None
    ) -> UpdateEventDestinationResultTypeDef:
        """
        Updates an existing event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_event_destination)
        """

    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TwoWayEnabled: bool = None,
        TwoWayChannelArn: str = None,
        TwoWayChannelRole: str = None,
        SelfManagedOptOutsEnabled: bool = None,
        OptOutListName: str = None,
        DeletionProtectionEnabled: bool = None
    ) -> UpdatePhoneNumberResultTypeDef:
        """
        Updates the configuration of an existing origination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_phone_number)
        """

    def update_pool(
        self,
        *,
        PoolId: str,
        TwoWayEnabled: bool = None,
        TwoWayChannelArn: str = None,
        TwoWayChannelRole: str = None,
        SelfManagedOptOutsEnabled: bool = None,
        OptOutListName: str = None,
        SharedRoutesEnabled: bool = None,
        DeletionProtectionEnabled: bool = None
    ) -> UpdatePoolResultTypeDef:
        """
        Updates the configuration of an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_pool)
        """

    def update_protect_configuration(
        self, *, ProtectConfigurationId: str, DeletionProtectionEnabled: bool = None
    ) -> UpdateProtectConfigurationResultTypeDef:
        """
        Update the setting for an existing protect configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_protect_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_protect_configuration)
        """

    def update_protect_configuration_country_rule_set(
        self,
        *,
        ProtectConfigurationId: str,
        NumberCapability: NumberCapabilityType,
        CountryRuleSetUpdates: Dict[str, "ProtectConfigurationCountryRuleSetInformationTypeDef"]
    ) -> UpdateProtectConfigurationCountryRuleSetResultTypeDef:
        """
        Update a country rule set to `ALLOW` or `BLOCK` messages to be sent to the
        specified destination counties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_protect_configuration_country_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_protect_configuration_country_rule_set)
        """

    def update_sender_id(
        self, *, SenderId: str, IsoCountryCode: str, DeletionProtectionEnabled: bool = None
    ) -> UpdateSenderIdResultTypeDef:
        """
        Updates the configuration of an existing sender ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_sender_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#update_sender_id)
        """

    def verify_destination_number(
        self, *, VerifiedDestinationNumberId: str, VerificationCode: str
    ) -> VerifyDestinationNumberResultTypeDef:
        """
        Use the verification code that was received by the verified destination phone
        number to opt-in the verified destination phone number to receive more messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.verify_destination_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/client.html#verify_destination_number)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_attributes"]
    ) -> DescribeAccountAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountattributespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeAccountLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeaccountlimitspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_sets"]
    ) -> DescribeConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeConfigurationSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeconfigurationsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_keywords"]
    ) -> DescribeKeywordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeKeywords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describekeywordspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opt_out_lists"]
    ) -> DescribeOptOutListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptOutLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptoutlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opted_out_numbers"]
    ) -> DescribeOptedOutNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeOptedOutNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeoptedoutnumberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_phone_numbers"]
    ) -> DescribePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePhoneNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describephonenumberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_pools"]) -> DescribePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribePools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describepoolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_protect_configurations"]
    ) -> DescribeProtectConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeProtectConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeprotectconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_attachments"]
    ) -> DescribeRegistrationAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_field_definitions"]
    ) -> DescribeRegistrationFieldDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationFieldDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationfielddefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_field_values"]
    ) -> DescribeRegistrationFieldValuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationFieldValues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationfieldvaluespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_section_definitions"]
    ) -> DescribeRegistrationSectionDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationSectionDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationsectiondefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_type_definitions"]
    ) -> DescribeRegistrationTypeDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationTypeDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationtypedefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_versions"]
    ) -> DescribeRegistrationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrationVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registrations"]
    ) -> DescribeRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeRegistrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeregistrationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sender_ids"]
    ) -> DescribeSenderIdsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSenderIds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describesenderidspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spend_limits"]
    ) -> DescribeSpendLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeSpendLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describespendlimitspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_destination_numbers"]
    ) -> DescribeVerifiedDestinationNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.DescribeVerifiedDestinationNumbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#describeverifieddestinationnumberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pool_origination_identities"]
    ) -> ListPoolOriginationIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.ListPoolOriginationIdentities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#listpooloriginationidentitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_registration_associations"]
    ) -> ListRegistrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Paginator.ListRegistrationAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/paginators.html#listregistrationassociationspaginator)
        """
