"""
Type annotations for chime-sdk-voice service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_voice import ChimeSDKVoiceClient

    client: ChimeSDKVoiceClient = boto3.client("chime-sdk-voice")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CapabilityType,
    GeoMatchLevelType,
    NumberSelectionBehaviorType,
    PhoneNumberAssociationNameType,
    PhoneNumberProductTypeType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    SipRuleTriggerTypeType,
    VoiceConnectorAwsRegionType,
)
from .paginator import ListSipMediaApplicationsPaginator, ListSipRulesPaginator
from .type_defs import (
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateProxySessionResponseTypeDef,
    CreateSipMediaApplicationCallResponseTypeDef,
    CreateSipMediaApplicationResponseTypeDef,
    CreateSipRuleResponseTypeDef,
    CreateVoiceConnectorGroupResponseTypeDef,
    CreateVoiceConnectorResponseTypeDef,
    CreateVoiceProfileDomainResponseTypeDef,
    CreateVoiceProfileResponseTypeDef,
    CredentialTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    EmergencyCallingConfigurationTypeDef,
    GeoMatchParamsTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetProxySessionResponseTypeDef,
    GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef,
    GetSipMediaApplicationLoggingConfigurationResponseTypeDef,
    GetSipMediaApplicationResponseTypeDef,
    GetSipRuleResponseTypeDef,
    GetSpeakerSearchTaskResponseTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorProxyResponseTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    GetVoiceProfileDomainResponseTypeDef,
    GetVoiceProfileResponseTypeDef,
    GetVoiceToneAnalysisTaskResponseTypeDef,
    ListAvailableVoiceConnectorRegionsResponseTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListProxySessionsResponseTypeDef,
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesResponseTypeDef,
    ListSupportedPhoneNumberCountriesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
    ListVoiceProfileDomainsResponseTypeDef,
    ListVoiceProfilesResponseTypeDef,
    LoggingConfigurationTypeDef,
    OriginationTypeDef,
    PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef,
    PutSipMediaApplicationLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorOriginationResponseTypeDef,
    PutVoiceConnectorProxyResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseTypeDef,
    PutVoiceConnectorTerminationResponseTypeDef,
    RestorePhoneNumberResponseTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SipMediaApplicationAlexaSkillConfigurationTypeDef,
    SipMediaApplicationEndpointTypeDef,
    SipMediaApplicationLoggingConfigurationTypeDef,
    SipRuleTargetApplicationTypeDef,
    StartSpeakerSearchTaskResponseTypeDef,
    StartVoiceToneAnalysisTaskResponseTypeDef,
    StreamingConfigurationTypeDef,
    TagTypeDef,
    TerminationTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdateProxySessionResponseTypeDef,
    UpdateSipMediaApplicationCallResponseTypeDef,
    UpdateSipMediaApplicationResponseTypeDef,
    UpdateSipRuleResponseTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
    UpdateVoiceProfileDomainResponseTypeDef,
    UpdateVoiceProfileResponseTypeDef,
    ValidateE911AddressResponseTypeDef,
    VoiceConnectorItemTypeDef,
    VoiceConnectorSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ChimeSDKVoiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]

class ChimeSDKVoiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKVoiceClient exceptions.
        """
    def associate_phone_numbers_with_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str], ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.associate_phone_numbers_with_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#associate_phone_numbers_with_voice_connector)
        """
    def associate_phone_numbers_with_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str],
        ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime SDK Voice Connector
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.associate_phone_numbers_with_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#associate_phone_numbers_with_voice_connector_group)
        """
    def batch_delete_phone_number(
        self, *, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        Moves phone numbers into the **Deletion queue**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.batch_delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#batch_delete_phone_number)
        """
    def batch_update_phone_number(
        self, *, UpdatePhoneNumberRequestItems: List["UpdatePhoneNumberRequestItemTypeDef"]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        Updates one or more phone numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.batch_update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#batch_update_phone_number)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#close)
        """
    def create_phone_number_order(
        self, *, ProductType: PhoneNumberProductTypeType, E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        Creates an order for phone numbers to be provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_phone_number_order)
        """
    def create_proxy_session(
        self,
        *,
        VoiceConnectorId: str,
        ParticipantPhoneNumbers: List[str],
        Capabilities: List[CapabilityType],
        Name: str = None,
        ExpiryMinutes: int = None,
        NumberSelectionBehavior: NumberSelectionBehaviorType = None,
        GeoMatchLevel: GeoMatchLevelType = None,
        GeoMatchParams: "GeoMatchParamsTypeDef" = None
    ) -> CreateProxySessionResponseTypeDef:
        """
        Creates a proxy session for the specified Amazon Chime SDK Voice Connector for
        the specified participant phone numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_proxy_session)
        """
    def create_sip_media_application(
        self,
        *,
        AwsRegion: str,
        Name: str,
        Endpoints: List["SipMediaApplicationEndpointTypeDef"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateSipMediaApplicationResponseTypeDef:
        """
        Creates a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_sip_media_application)
        """
    def create_sip_media_application_call(
        self,
        *,
        FromPhoneNumber: str,
        ToPhoneNumber: str,
        SipMediaApplicationId: str,
        SipHeaders: Dict[str, str] = None,
        ArgumentsMap: Dict[str, str] = None
    ) -> CreateSipMediaApplicationCallResponseTypeDef:
        """
        Creates an outbound call to a phone number from the phone number specified in
        the request, and it invokes the endpoint of the specified
        `sipMediaApplicationId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_media_application_call)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_sip_media_application_call)
        """
    def create_sip_rule(
        self,
        *,
        Name: str,
        TriggerType: SipRuleTriggerTypeType,
        TriggerValue: str,
        Disabled: bool = None,
        TargetApplications: List["SipRuleTargetApplicationTypeDef"] = None
    ) -> CreateSipRuleResponseTypeDef:
        """
        Creates a SIP rule, which can be used to run a SIP media application as a target
        for a specific trigger type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_sip_rule)
        """
    def create_voice_connector(
        self,
        *,
        Name: str,
        RequireEncryption: bool,
        AwsRegion: VoiceConnectorAwsRegionType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        Creates an Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_connector)
        """
    def create_voice_connector_group(
        self, *, Name: str, VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        Creates an Amazon Chime SDK Voice Connector group under the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_connector_group)
        """
    def create_voice_profile(
        self, *, SpeakerSearchTaskId: str
    ) -> CreateVoiceProfileResponseTypeDef:
        """
        Creates a voice profile, which consists of an enrolled user and their latest
        voice print.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_profile)
        """
    def create_voice_profile_domain(
        self,
        *,
        Name: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        Description: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateVoiceProfileDomainResponseTypeDef:
        """
        Creates a voice profile domain, a collection of voice profiles, their voice
        prints, and encrypted enrollment audio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_profile_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_profile_domain)
        """
    def delete_phone_number(self, *, PhoneNumberId: str) -> None:
        """
        Moves the specified phone number into the **Deletion queue**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_phone_number)
        """
    def delete_proxy_session(self, *, VoiceConnectorId: str, ProxySessionId: str) -> None:
        """
        Deletes the specified proxy session from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_proxy_session)
        """
    def delete_sip_media_application(self, *, SipMediaApplicationId: str) -> None:
        """
        Deletes a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_sip_media_application)
        """
    def delete_sip_rule(self, *, SipRuleId: str) -> None:
        """
        Deletes a SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_sip_rule)
        """
    def delete_voice_connector(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes an Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector)
        """
    def delete_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> None:
        """
        Deletes the emergency calling details from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_emergency_calling_configuration)
        """
    def delete_voice_connector_group(self, *, VoiceConnectorGroupId: str) -> None:
        """
        Deletes an Amazon Chime SDK Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_group)
        """
    def delete_voice_connector_origination(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the origination settings for the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_origination)
        """
    def delete_voice_connector_proxy(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the proxy configuration from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_proxy)
        """
    def delete_voice_connector_streaming_configuration(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes a Voice Connector's streaming configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_streaming_configuration)
        """
    def delete_voice_connector_termination(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the termination settings for the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_termination)
        """
    def delete_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Usernames: List[str]
    ) -> None:
        """
        Deletes the specified SIP credentials used by your equipment to authenticate
        during call termination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_termination_credentials)
        """
    def delete_voice_profile(self, *, VoiceProfileId: str) -> None:
        """
        Deletes a voice profile, including its voice print and enrollment data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_profile)
        """
    def delete_voice_profile_domain(self, *, VoiceProfileDomainId: str) -> None:
        """
        Deletes all voice profiles in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_profile_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_profile_domain)
        """
    def disassociate_phone_numbers_from_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.disassociate_phone_numbers_from_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#disassociate_phone_numbers_from_voice_connector)
        """
    def disassociate_phone_numbers_from_voice_connector_group(
        self, *, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime SDK
        Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.disassociate_phone_numbers_from_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#disassociate_phone_numbers_from_voice_connector_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#generate_presigned_url)
        """
    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        Retrieves the global settings for the Amazon Chime SDK Voice Connectors in an
        AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_global_settings)
        """
    def get_phone_number(self, *, PhoneNumberId: str) -> GetPhoneNumberResponseTypeDef:
        """
        Retrieves details for the specified phone number ID, such as associations,
        capabilities, and product type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number)
        """
    def get_phone_number_order(
        self, *, PhoneNumberOrderId: str
    ) -> GetPhoneNumberOrderResponseTypeDef:
        """
        Retrieves details for the specified phone number order, such as the order
        creation timestamp, phone numbers in E.164 format, product type, and order
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number_order)
        """
    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        Retrieves the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number_settings)
        """
    def get_proxy_session(
        self, *, VoiceConnectorId: str, ProxySessionId: str
    ) -> GetProxySessionResponseTypeDef:
        """
        Retrieves the specified proxy session details for the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_proxy_session)
        """
    def get_sip_media_application(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationResponseTypeDef:
        """
        Retrieves the information for a SIP media application, including name, AWS
        Region, and endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application)
        """
    def get_sip_media_application_alexa_skill_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        Gets the Alexa Skill configuration for the SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application_alexa_skill_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application_alexa_skill_configuration)
        """
    def get_sip_media_application_logging_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        Retrieves the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application_logging_configuration)
        """
    def get_sip_rule(self, *, SipRuleId: str) -> GetSipRuleResponseTypeDef:
        """
        Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and
        target endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_rule)
        """
    def get_speaker_search_task(
        self, *, VoiceConnectorId: str, SpeakerSearchTaskId: str
    ) -> GetSpeakerSearchTaskResponseTypeDef:
        """
        Retrieves the details of the specified speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_speaker_search_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_speaker_search_task)
        """
    def get_voice_connector(self, *, VoiceConnectorId: str) -> GetVoiceConnectorResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime SDK Voice Connector, such as
        timestamps,name, outbound host, and encryption requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector)
        """
    def get_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        Retrieves the emergency calling configuration details for the specified Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_emergency_calling_configuration)
        """
    def get_voice_connector_group(
        self, *, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime SDK Voice Connector group, such
        as timestamps,name, and associated `VoiceConnectorItems`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_group)
        """
    def get_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Retrieves the logging configuration settings for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_logging_configuration)
        """
    def get_voice_connector_origination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        Retrieves the origination settings for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_origination)
        """
    def get_voice_connector_proxy(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorProxyResponseTypeDef:
        """
        Retrieves the proxy configuration details for the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_proxy)
        """
    def get_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Retrieves the streaming configuration details for the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_streaming_configuration)
        """
    def get_voice_connector_termination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        Retrieves the termination setting details for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_termination)
        """
    def get_voice_connector_termination_health(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        Retrieves information about the last time a `SIP OPTIONS` ping was received from
        your SIP infrastructure for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_termination_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_termination_health)
        """
    def get_voice_profile(self, *, VoiceProfileId: str) -> GetVoiceProfileResponseTypeDef:
        """
        Retrieves the details of the specified voice profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_profile)
        """
    def get_voice_profile_domain(
        self, *, VoiceProfileDomainId: str
    ) -> GetVoiceProfileDomainResponseTypeDef:
        """
        Retrieves the details of the specified voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_profile_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_profile_domain)
        """
    def get_voice_tone_analysis_task(
        self, *, VoiceConnectorId: str, VoiceToneAnalysisTaskId: str, IsCaller: bool
    ) -> GetVoiceToneAnalysisTaskResponseTypeDef:
        """
        Retrieves the details of a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_tone_analysis_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_tone_analysis_task)
        """
    def list_available_voice_connector_regions(
        self,
    ) -> ListAvailableVoiceConnectorRegionsResponseTypeDef:
        """
        Lists the available AWS Regions in which you can create an Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_available_voice_connector_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_available_voice_connector_regions)
        """
    def list_phone_number_orders(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        Lists the phone numbers for an administrator's Amazon Chime SDK account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_phone_number_orders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_phone_number_orders)
        """
    def list_phone_numbers(
        self,
        *,
        Status: str = None,
        ProductType: PhoneNumberProductTypeType = None,
        FilterName: PhoneNumberAssociationNameType = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Lists the phone numbers for the specified Amazon Chime SDK account, Amazon Chime
        SDK user, Amazon Chime SDK Voice Connector, or Amazon Chime SDK Voice Connector
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_phone_numbers)
        """
    def list_proxy_sessions(
        self,
        *,
        VoiceConnectorId: str,
        Status: ProxySessionStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProxySessionsResponseTypeDef:
        """
        Lists the proxy sessions for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_proxy_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_proxy_sessions)
        """
    def list_sip_media_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSipMediaApplicationsResponseTypeDef:
        """
        Lists the SIP media applications under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_sip_media_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_sip_media_applications)
        """
    def list_sip_rules(
        self, *, SipMediaApplicationId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSipRulesResponseTypeDef:
        """
        Lists the SIP rules under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_sip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_sip_rules)
        """
    def list_supported_phone_number_countries(
        self, *, ProductType: PhoneNumberProductTypeType
    ) -> ListSupportedPhoneNumberCountriesResponseTypeDef:
        """
        Lists the countries that you can order phone numbers from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_supported_phone_number_countries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_supported_phone_number_countries)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags in a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_tags_for_resource)
        """
    def list_voice_connector_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        Lists the Amazon Chime SDK Voice Connector groups in the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connector_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connector_groups)
        """
    def list_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        Lists the SIP credentials for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connector_termination_credentials)
        """
    def list_voice_connectors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        Lists the Amazon Chime SDK Voice Connectors in the administrators AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connectors)
        """
    def list_voice_profile_domains(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceProfileDomainsResponseTypeDef:
        """
        Lists the specified voice profile domains in the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_profile_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_profile_domains)
        """
    def list_voice_profiles(
        self, *, VoiceProfileDomainId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceProfilesResponseTypeDef:
        """
        Lists the voice profiles in a voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_profiles)
        """
    def put_sip_media_application_alexa_skill_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationAlexaSkillConfiguration: "SipMediaApplicationAlexaSkillConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        Updates the Alexa Skill configuration for the SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_sip_media_application_alexa_skill_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_sip_media_application_alexa_skill_configuration)
        """
    def put_sip_media_application_logging_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        Updates the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_sip_media_application_logging_configuration)
        """
    def put_voice_connector_emergency_calling_configuration(
        self,
        *,
        VoiceConnectorId: str,
        EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's emergency calling configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_emergency_calling_configuration)
        """
    def put_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_logging_configuration)
        """
    def put_voice_connector_origination(
        self, *, VoiceConnectorId: str, Origination: "OriginationTypeDef"
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        Updates a Voice Connector's origination settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_origination)
        """
    def put_voice_connector_proxy(
        self,
        *,
        VoiceConnectorId: str,
        DefaultSessionExpiryMinutes: int,
        PhoneNumberPoolCountries: List[str],
        FallBackPhoneNumber: str = None,
        Disabled: bool = None
    ) -> PutVoiceConnectorProxyResponseTypeDef:
        """
        Puts the specified proxy configuration to the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_proxy)
        """
    def put_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str, StreamingConfiguration: "StreamingConfigurationTypeDef"
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's streaming configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_streaming_configuration)
        """
    def put_voice_connector_termination(
        self, *, VoiceConnectorId: str, Termination: "TerminationTypeDef"
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        Updates a Voice Connector's termination settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_termination)
        """
    def put_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Credentials: List["CredentialTypeDef"] = None
    ) -> None:
        """
        Updates a Voice Connector's termination credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_termination_credentials)
        """
    def restore_phone_number(self, *, PhoneNumberId: str) -> RestorePhoneNumberResponseTypeDef:
        """
        Restores a deleted phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.restore_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#restore_phone_number)
        """
    def search_available_phone_numbers(
        self,
        *,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        PhoneNumberType: PhoneNumberTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches the provisioned phone numbers in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.search_available_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#search_available_phone_numbers)
        """
    def start_speaker_search_task(
        self,
        *,
        VoiceConnectorId: str,
        TransactionId: str,
        VoiceProfileDomainId: str,
        ClientRequestToken: str = None
    ) -> StartSpeakerSearchTaskResponseTypeDef:
        """
        Starts a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.start_speaker_search_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#start_speaker_search_task)
        """
    def start_voice_tone_analysis_task(
        self,
        *,
        VoiceConnectorId: str,
        TransactionId: str,
        LanguageCode: Literal["en-US"],
        ClientRequestToken: str = None
    ) -> StartVoiceToneAnalysisTaskResponseTypeDef:
        """
        Starts a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.start_voice_tone_analysis_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#start_voice_tone_analysis_task)
        """
    def stop_speaker_search_task(self, *, VoiceConnectorId: str, SpeakerSearchTaskId: str) -> None:
        """
        Stops a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.stop_speaker_search_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#stop_speaker_search_task)
        """
    def stop_voice_tone_analysis_task(
        self, *, VoiceConnectorId: str, VoiceToneAnalysisTaskId: str
    ) -> None:
        """
        Stops a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.stop_voice_tone_analysis_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#stop_voice_tone_analysis_task)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#untag_resource)
        """
    def update_global_settings(
        self, *, VoiceConnector: "VoiceConnectorSettingsTypeDef" = None
    ) -> None:
        """
        Updates global settings for the Amazon Chime SDK Voice Connectors in an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_global_settings)
        """
    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        ProductType: PhoneNumberProductTypeType = None,
        CallingName: str = None
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number details, such as product type or calling name, for the
        specified phone number ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_phone_number)
        """
    def update_phone_number_settings(self, *, CallingName: str) -> None:
        """
        Updates the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_phone_number_settings)
        """
    def update_proxy_session(
        self,
        *,
        VoiceConnectorId: str,
        ProxySessionId: str,
        Capabilities: List[CapabilityType],
        ExpiryMinutes: int = None
    ) -> UpdateProxySessionResponseTypeDef:
        """
        Updates the specified proxy session details, such as voice or SMS capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_proxy_session)
        """
    def update_sip_media_application(
        self,
        *,
        SipMediaApplicationId: str,
        Name: str = None,
        Endpoints: List["SipMediaApplicationEndpointTypeDef"] = None
    ) -> UpdateSipMediaApplicationResponseTypeDef:
        """
        Updates the details of the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_sip_media_application)
        """
    def update_sip_media_application_call(
        self, *, SipMediaApplicationId: str, TransactionId: str, Arguments: Dict[str, str]
    ) -> UpdateSipMediaApplicationCallResponseTypeDef:
        """
        Invokes the AWS Lambda function associated with the SIP media application and
        transaction ID in an update request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_media_application_call)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_sip_media_application_call)
        """
    def update_sip_rule(
        self,
        *,
        SipRuleId: str,
        Name: str,
        Disabled: bool = None,
        TargetApplications: List["SipRuleTargetApplicationTypeDef"] = None
    ) -> UpdateSipRuleResponseTypeDef:
        """
        Updates the details of the specified SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_sip_rule)
        """
    def update_voice_connector(
        self, *, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        Updates the details for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_voice_connector)
        """
    def update_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List["VoiceConnectorItemTypeDef"]
    ) -> UpdateVoiceConnectorGroupResponseTypeDef:
        """
        Updates the settings for the specified Amazon Chime SDK Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_voice_connector_group)
        """
    def update_voice_profile(
        self, *, VoiceProfileId: str, SpeakerSearchTaskId: str
    ) -> UpdateVoiceProfileResponseTypeDef:
        """
        Updates the specified voice profile’s voice print and refreshes its expiration
        timestamp.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_voice_profile)
        """
    def update_voice_profile_domain(
        self, *, VoiceProfileDomainId: str, Name: str = None, Description: str = None
    ) -> UpdateVoiceProfileDomainResponseTypeDef:
        """
        Updates the settings for the specified voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_profile_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_voice_profile_domain)
        """
    def validate_e911_address(
        self,
        *,
        AwsAccountId: str,
        StreetNumber: str,
        StreetInfo: str,
        City: str,
        State: str,
        Country: str,
        PostalCode: str
    ) -> ValidateE911AddressResponseTypeDef:
        """
        Validates an address to be used for 911 calls made with Amazon Chime SDK Voice
        Connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.validate_e911_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#validate_e911_address)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sip_media_applications"]
    ) -> ListSipMediaApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipMediaApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsipmediaapplicationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_sip_rules"]) -> ListSipRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsiprulespaginator)
        """
