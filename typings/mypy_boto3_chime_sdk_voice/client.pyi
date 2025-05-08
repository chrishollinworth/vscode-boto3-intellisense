"""
Type annotations for chime-sdk-voice service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_voice.client import ChimeSDKVoiceClient

    session = Session()
    client: ChimeSDKVoiceClient = session.client("chime-sdk-voice")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListSipMediaApplicationsPaginator, ListSipRulesPaginator
from .type_defs import (
    AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    BatchDeletePhoneNumberRequestTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchUpdatePhoneNumberRequestTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    CreatePhoneNumberOrderRequestTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateProxySessionRequestTypeDef,
    CreateProxySessionResponseTypeDef,
    CreateSipMediaApplicationCallRequestTypeDef,
    CreateSipMediaApplicationCallResponseTypeDef,
    CreateSipMediaApplicationRequestTypeDef,
    CreateSipMediaApplicationResponseTypeDef,
    CreateSipRuleRequestTypeDef,
    CreateSipRuleResponseTypeDef,
    CreateVoiceConnectorGroupRequestTypeDef,
    CreateVoiceConnectorGroupResponseTypeDef,
    CreateVoiceConnectorRequestTypeDef,
    CreateVoiceConnectorResponseTypeDef,
    CreateVoiceProfileDomainRequestTypeDef,
    CreateVoiceProfileDomainResponseTypeDef,
    CreateVoiceProfileRequestTypeDef,
    CreateVoiceProfileResponseTypeDef,
    DeletePhoneNumberRequestTypeDef,
    DeleteProxySessionRequestTypeDef,
    DeleteSipMediaApplicationRequestTypeDef,
    DeleteSipRuleRequestTypeDef,
    DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef,
    DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef,
    DeleteVoiceConnectorGroupRequestTypeDef,
    DeleteVoiceConnectorOriginationRequestTypeDef,
    DeleteVoiceConnectorProxyRequestTypeDef,
    DeleteVoiceConnectorRequestTypeDef,
    DeleteVoiceConnectorStreamingConfigurationRequestTypeDef,
    DeleteVoiceConnectorTerminationCredentialsRequestTypeDef,
    DeleteVoiceConnectorTerminationRequestTypeDef,
    DeleteVoiceProfileDomainRequestTypeDef,
    DeleteVoiceProfileRequestTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetPhoneNumberOrderRequestTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberRequestTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetProxySessionRequestTypeDef,
    GetProxySessionResponseTypeDef,
    GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef,
    GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef,
    GetSipMediaApplicationLoggingConfigurationRequestTypeDef,
    GetSipMediaApplicationLoggingConfigurationResponseTypeDef,
    GetSipMediaApplicationRequestTypeDef,
    GetSipMediaApplicationResponseTypeDef,
    GetSipRuleRequestTypeDef,
    GetSipRuleResponseTypeDef,
    GetSpeakerSearchTaskRequestTypeDef,
    GetSpeakerSearchTaskResponseTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef,
    GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef,
    GetVoiceConnectorGroupRequestTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationRequestTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationRequestTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorProxyRequestTypeDef,
    GetVoiceConnectorProxyResponseTypeDef,
    GetVoiceConnectorRequestTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationRequestTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthRequestTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationRequestTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    GetVoiceProfileDomainRequestTypeDef,
    GetVoiceProfileDomainResponseTypeDef,
    GetVoiceProfileRequestTypeDef,
    GetVoiceProfileResponseTypeDef,
    GetVoiceToneAnalysisTaskRequestTypeDef,
    GetVoiceToneAnalysisTaskResponseTypeDef,
    ListAvailableVoiceConnectorRegionsResponseTypeDef,
    ListPhoneNumberOrdersRequestTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersRequestTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListProxySessionsRequestTypeDef,
    ListProxySessionsResponseTypeDef,
    ListSipMediaApplicationsRequestTypeDef,
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesRequestTypeDef,
    ListSipRulesResponseTypeDef,
    ListSupportedPhoneNumberCountriesRequestTypeDef,
    ListSupportedPhoneNumberCountriesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVoiceConnectorGroupsRequestTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorsRequestTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsRequestTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
    ListVoiceProfileDomainsRequestTypeDef,
    ListVoiceProfileDomainsResponseTypeDef,
    ListVoiceProfilesRequestTypeDef,
    ListVoiceProfilesResponseTypeDef,
    PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef,
    PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef,
    PutSipMediaApplicationLoggingConfigurationRequestTypeDef,
    PutSipMediaApplicationLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef,
    PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationRequestTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorOriginationRequestTypeDef,
    PutVoiceConnectorOriginationResponseTypeDef,
    PutVoiceConnectorProxyRequestTypeDef,
    PutVoiceConnectorProxyResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationRequestTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseTypeDef,
    PutVoiceConnectorTerminationCredentialsRequestTypeDef,
    PutVoiceConnectorTerminationRequestTypeDef,
    PutVoiceConnectorTerminationResponseTypeDef,
    RestorePhoneNumberRequestTypeDef,
    RestorePhoneNumberResponseTypeDef,
    SearchAvailablePhoneNumbersRequestTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    StartSpeakerSearchTaskRequestTypeDef,
    StartSpeakerSearchTaskResponseTypeDef,
    StartVoiceToneAnalysisTaskRequestTypeDef,
    StartVoiceToneAnalysisTaskResponseTypeDef,
    StopSpeakerSearchTaskRequestTypeDef,
    StopVoiceToneAnalysisTaskRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateGlobalSettingsRequestTypeDef,
    UpdatePhoneNumberRequestTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdatePhoneNumberSettingsRequestTypeDef,
    UpdateProxySessionRequestTypeDef,
    UpdateProxySessionResponseTypeDef,
    UpdateSipMediaApplicationCallRequestTypeDef,
    UpdateSipMediaApplicationCallResponseTypeDef,
    UpdateSipMediaApplicationRequestTypeDef,
    UpdateSipMediaApplicationResponseTypeDef,
    UpdateSipRuleRequestTypeDef,
    UpdateSipRuleResponseTypeDef,
    UpdateVoiceConnectorGroupRequestTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorRequestTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
    UpdateVoiceProfileDomainRequestTypeDef,
    UpdateVoiceProfileDomainResponseTypeDef,
    UpdateVoiceProfileRequestTypeDef,
    UpdateVoiceProfileResponseTypeDef,
    ValidateE911AddressRequestTypeDef,
    ValidateE911AddressResponseTypeDef,
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

__all__ = ("ChimeSDKVoiceClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKVoiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#generate_presigned_url)
        """

    def associate_phone_numbers_with_voice_connector(
        self, **kwargs: Unpack[AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef]
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/associate_phone_numbers_with_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#associate_phone_numbers_with_voice_connector)
        """

    def associate_phone_numbers_with_voice_connector_group(
        self, **kwargs: Unpack[AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef]
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime SDK Voice Connector
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/associate_phone_numbers_with_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#associate_phone_numbers_with_voice_connector_group)
        """

    def batch_delete_phone_number(
        self, **kwargs: Unpack[BatchDeletePhoneNumberRequestTypeDef]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        Moves phone numbers into the <b>Deletion queue</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/batch_delete_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#batch_delete_phone_number)
        """

    def batch_update_phone_number(
        self, **kwargs: Unpack[BatchUpdatePhoneNumberRequestTypeDef]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number product types, calling names, or phone number names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/batch_update_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#batch_update_phone_number)
        """

    def create_phone_number_order(
        self, **kwargs: Unpack[CreatePhoneNumberOrderRequestTypeDef]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        Creates an order for phone numbers to be provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_phone_number_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_phone_number_order)
        """

    def create_proxy_session(
        self, **kwargs: Unpack[CreateProxySessionRequestTypeDef]
    ) -> CreateProxySessionResponseTypeDef:
        """
        Creates a proxy session for the specified Amazon Chime SDK Voice Connector for
        the specified participant phone numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_proxy_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_proxy_session)
        """

    def create_sip_media_application(
        self, **kwargs: Unpack[CreateSipMediaApplicationRequestTypeDef]
    ) -> CreateSipMediaApplicationResponseTypeDef:
        """
        Creates a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_sip_media_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_sip_media_application)
        """

    def create_sip_media_application_call(
        self, **kwargs: Unpack[CreateSipMediaApplicationCallRequestTypeDef]
    ) -> CreateSipMediaApplicationCallResponseTypeDef:
        """
        Creates an outbound call to a phone number from the phone number specified in
        the request, and it invokes the endpoint of the specified
        <code>sipMediaApplicationId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_sip_media_application_call.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_sip_media_application_call)
        """

    def create_sip_rule(
        self, **kwargs: Unpack[CreateSipRuleRequestTypeDef]
    ) -> CreateSipRuleResponseTypeDef:
        """
        Creates a SIP rule, which can be used to run a SIP media application as a
        target for a specific trigger type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_sip_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_sip_rule)
        """

    def create_voice_connector(
        self, **kwargs: Unpack[CreateVoiceConnectorRequestTypeDef]
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        Creates an Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_voice_connector)
        """

    def create_voice_connector_group(
        self, **kwargs: Unpack[CreateVoiceConnectorGroupRequestTypeDef]
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        Creates an Amazon Chime SDK Voice Connector group under the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_voice_connector_group)
        """

    def create_voice_profile(
        self, **kwargs: Unpack[CreateVoiceProfileRequestTypeDef]
    ) -> CreateVoiceProfileResponseTypeDef:
        """
        Creates a voice profile, which consists of an enrolled user and their latest
        voice print.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_voice_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_voice_profile)
        """

    def create_voice_profile_domain(
        self, **kwargs: Unpack[CreateVoiceProfileDomainRequestTypeDef]
    ) -> CreateVoiceProfileDomainResponseTypeDef:
        """
        Creates a voice profile domain, a collection of voice profiles, their voice
        prints, and encrypted enrollment audio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/create_voice_profile_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#create_voice_profile_domain)
        """

    def delete_phone_number(
        self, **kwargs: Unpack[DeletePhoneNumberRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Moves the specified phone number into the <b>Deletion queue</b>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_phone_number)
        """

    def delete_proxy_session(
        self, **kwargs: Unpack[DeleteProxySessionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified proxy session from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_proxy_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_proxy_session)
        """

    def delete_sip_media_application(
        self, **kwargs: Unpack[DeleteSipMediaApplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_sip_media_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_sip_media_application)
        """

    def delete_sip_rule(
        self, **kwargs: Unpack[DeleteSipRuleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_sip_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_sip_rule)
        """

    def delete_voice_connector(
        self, **kwargs: Unpack[DeleteVoiceConnectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector)
        """

    def delete_voice_connector_emergency_calling_configuration(
        self, **kwargs: Unpack[DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the emergency calling details from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_emergency_calling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_emergency_calling_configuration)
        """

    def delete_voice_connector_external_systems_configuration(
        self, **kwargs: Unpack[DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the external systems configuration for a Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_external_systems_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_external_systems_configuration)
        """

    def delete_voice_connector_group(
        self, **kwargs: Unpack[DeleteVoiceConnectorGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Chime SDK Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_group)
        """

    def delete_voice_connector_origination(
        self, **kwargs: Unpack[DeleteVoiceConnectorOriginationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the origination settings for the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_origination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_origination)
        """

    def delete_voice_connector_proxy(
        self, **kwargs: Unpack[DeleteVoiceConnectorProxyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the proxy configuration from the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_proxy)
        """

    def delete_voice_connector_streaming_configuration(
        self, **kwargs: Unpack[DeleteVoiceConnectorStreamingConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Voice Connector's streaming configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_streaming_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_streaming_configuration)
        """

    def delete_voice_connector_termination(
        self, **kwargs: Unpack[DeleteVoiceConnectorTerminationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the termination settings for the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_termination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_termination)
        """

    def delete_voice_connector_termination_credentials(
        self, **kwargs: Unpack[DeleteVoiceConnectorTerminationCredentialsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified SIP credentials used by your equipment to authenticate
        during call termination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_connector_termination_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_connector_termination_credentials)
        """

    def delete_voice_profile(
        self, **kwargs: Unpack[DeleteVoiceProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a voice profile, including its voice print and enrollment data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_profile)
        """

    def delete_voice_profile_domain(
        self, **kwargs: Unpack[DeleteVoiceProfileDomainRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes all voice profiles in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/delete_voice_profile_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#delete_voice_profile_domain)
        """

    def disassociate_phone_numbers_from_voice_connector(
        self, **kwargs: Unpack[DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/disassociate_phone_numbers_from_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#disassociate_phone_numbers_from_voice_connector)
        """

    def disassociate_phone_numbers_from_voice_connector_group(
        self, **kwargs: Unpack[DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime SDK
        Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/disassociate_phone_numbers_from_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#disassociate_phone_numbers_from_voice_connector_group)
        """

    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        Retrieves the global settings for the Amazon Chime SDK Voice Connectors in an
        AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_global_settings)
        """

    def get_phone_number(
        self, **kwargs: Unpack[GetPhoneNumberRequestTypeDef]
    ) -> GetPhoneNumberResponseTypeDef:
        """
        Retrieves details for the specified phone number ID, such as associations,
        capabilities, and product type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_phone_number)
        """

    def get_phone_number_order(
        self, **kwargs: Unpack[GetPhoneNumberOrderRequestTypeDef]
    ) -> GetPhoneNumberOrderResponseTypeDef:
        """
        Retrieves details for the specified phone number order, such as the order
        creation timestamp, phone numbers in E.164 format, product type, and order
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_phone_number_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_phone_number_order)
        """

    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        Retrieves the phone number settings for the administrator's AWS account, such
        as the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_phone_number_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_phone_number_settings)
        """

    def get_proxy_session(
        self, **kwargs: Unpack[GetProxySessionRequestTypeDef]
    ) -> GetProxySessionResponseTypeDef:
        """
        Retrieves the specified proxy session details for the specified Amazon Chime
        SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_proxy_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_proxy_session)
        """

    def get_sip_media_application(
        self, **kwargs: Unpack[GetSipMediaApplicationRequestTypeDef]
    ) -> GetSipMediaApplicationResponseTypeDef:
        """
        Retrieves the information for a SIP media application, including name, AWS
        Region, and endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_sip_media_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_sip_media_application)
        """

    def get_sip_media_application_alexa_skill_configuration(
        self, **kwargs: Unpack[GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef]
    ) -> GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        Gets the Alexa Skill configuration for the SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_sip_media_application_alexa_skill_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_sip_media_application_alexa_skill_configuration)
        """

    def get_sip_media_application_logging_configuration(
        self, **kwargs: Unpack[GetSipMediaApplicationLoggingConfigurationRequestTypeDef]
    ) -> GetSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        Retrieves the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_sip_media_application_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_sip_media_application_logging_configuration)
        """

    def get_sip_rule(self, **kwargs: Unpack[GetSipRuleRequestTypeDef]) -> GetSipRuleResponseTypeDef:
        """
        Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and
        target endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_sip_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_sip_rule)
        """

    def get_speaker_search_task(
        self, **kwargs: Unpack[GetSpeakerSearchTaskRequestTypeDef]
    ) -> GetSpeakerSearchTaskResponseTypeDef:
        """
        Retrieves the details of the specified speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_speaker_search_task)
        """

    def get_voice_connector(
        self, **kwargs: Unpack[GetVoiceConnectorRequestTypeDef]
    ) -> GetVoiceConnectorResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime SDK Voice Connector, such as
        timestamps,name, outbound host, and encryption requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector)
        """

    def get_voice_connector_emergency_calling_configuration(
        self, **kwargs: Unpack[GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef]
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        Retrieves the emergency calling configuration details for the specified Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_emergency_calling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_emergency_calling_configuration)
        """

    def get_voice_connector_external_systems_configuration(
        self, **kwargs: Unpack[GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef]
    ) -> GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef:
        """
        Gets information about an external systems configuration for a Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_external_systems_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_external_systems_configuration)
        """

    def get_voice_connector_group(
        self, **kwargs: Unpack[GetVoiceConnectorGroupRequestTypeDef]
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime SDK Voice Connector group,
        such as timestamps,name, and associated <code>VoiceConnectorItems</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_group)
        """

    def get_voice_connector_logging_configuration(
        self, **kwargs: Unpack[GetVoiceConnectorLoggingConfigurationRequestTypeDef]
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Retrieves the logging configuration settings for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_logging_configuration)
        """

    def get_voice_connector_origination(
        self, **kwargs: Unpack[GetVoiceConnectorOriginationRequestTypeDef]
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        Retrieves the origination settings for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_origination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_origination)
        """

    def get_voice_connector_proxy(
        self, **kwargs: Unpack[GetVoiceConnectorProxyRequestTypeDef]
    ) -> GetVoiceConnectorProxyResponseTypeDef:
        """
        Retrieves the proxy configuration details for the specified Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_proxy)
        """

    def get_voice_connector_streaming_configuration(
        self, **kwargs: Unpack[GetVoiceConnectorStreamingConfigurationRequestTypeDef]
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Retrieves the streaming configuration details for the specified Amazon Chime
        SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_streaming_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_streaming_configuration)
        """

    def get_voice_connector_termination(
        self, **kwargs: Unpack[GetVoiceConnectorTerminationRequestTypeDef]
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        Retrieves the termination setting details for the specified Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_termination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_termination)
        """

    def get_voice_connector_termination_health(
        self, **kwargs: Unpack[GetVoiceConnectorTerminationHealthRequestTypeDef]
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        Retrieves information about the last time a <code>SIP OPTIONS</code> ping was
        received from your SIP infrastructure for the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_connector_termination_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_connector_termination_health)
        """

    def get_voice_profile(
        self, **kwargs: Unpack[GetVoiceProfileRequestTypeDef]
    ) -> GetVoiceProfileResponseTypeDef:
        """
        Retrieves the details of the specified voice profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_profile)
        """

    def get_voice_profile_domain(
        self, **kwargs: Unpack[GetVoiceProfileDomainRequestTypeDef]
    ) -> GetVoiceProfileDomainResponseTypeDef:
        """
        Retrieves the details of the specified voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_profile_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_profile_domain)
        """

    def get_voice_tone_analysis_task(
        self, **kwargs: Unpack[GetVoiceToneAnalysisTaskRequestTypeDef]
    ) -> GetVoiceToneAnalysisTaskResponseTypeDef:
        """
        Retrieves the details of a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_voice_tone_analysis_task)
        """

    def list_available_voice_connector_regions(
        self,
    ) -> ListAvailableVoiceConnectorRegionsResponseTypeDef:
        """
        Lists the available AWS Regions in which you can create an Amazon Chime SDK
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_available_voice_connector_regions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_available_voice_connector_regions)
        """

    def list_phone_number_orders(
        self, **kwargs: Unpack[ListPhoneNumberOrdersRequestTypeDef]
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        Lists the phone numbers for an administrator's Amazon Chime SDK account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_phone_number_orders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_phone_number_orders)
        """

    def list_phone_numbers(
        self, **kwargs: Unpack[ListPhoneNumbersRequestTypeDef]
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Lists the phone numbers for the specified Amazon Chime SDK account, Amazon
        Chime SDK user, Amazon Chime SDK Voice Connector, or Amazon Chime SDK Voice
        Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_phone_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_phone_numbers)
        """

    def list_proxy_sessions(
        self, **kwargs: Unpack[ListProxySessionsRequestTypeDef]
    ) -> ListProxySessionsResponseTypeDef:
        """
        Lists the proxy sessions for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_proxy_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_proxy_sessions)
        """

    def list_sip_media_applications(
        self, **kwargs: Unpack[ListSipMediaApplicationsRequestTypeDef]
    ) -> ListSipMediaApplicationsResponseTypeDef:
        """
        Lists the SIP media applications under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_sip_media_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_sip_media_applications)
        """

    def list_sip_rules(
        self, **kwargs: Unpack[ListSipRulesRequestTypeDef]
    ) -> ListSipRulesResponseTypeDef:
        """
        Lists the SIP rules under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_sip_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_sip_rules)
        """

    def list_supported_phone_number_countries(
        self, **kwargs: Unpack[ListSupportedPhoneNumberCountriesRequestTypeDef]
    ) -> ListSupportedPhoneNumberCountriesResponseTypeDef:
        """
        Lists the countries that you can order phone numbers from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_supported_phone_number_countries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_supported_phone_number_countries)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags in a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_tags_for_resource)
        """

    def list_voice_connector_groups(
        self, **kwargs: Unpack[ListVoiceConnectorGroupsRequestTypeDef]
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        Lists the Amazon Chime SDK Voice Connector groups in the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_voice_connector_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_voice_connector_groups)
        """

    def list_voice_connector_termination_credentials(
        self, **kwargs: Unpack[ListVoiceConnectorTerminationCredentialsRequestTypeDef]
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        Lists the SIP credentials for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_voice_connector_termination_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_voice_connector_termination_credentials)
        """

    def list_voice_connectors(
        self, **kwargs: Unpack[ListVoiceConnectorsRequestTypeDef]
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        Lists the Amazon Chime SDK Voice Connectors in the administrators AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_voice_connectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_voice_connectors)
        """

    def list_voice_profile_domains(
        self, **kwargs: Unpack[ListVoiceProfileDomainsRequestTypeDef]
    ) -> ListVoiceProfileDomainsResponseTypeDef:
        """
        Lists the specified voice profile domains in the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_voice_profile_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_voice_profile_domains)
        """

    def list_voice_profiles(
        self, **kwargs: Unpack[ListVoiceProfilesRequestTypeDef]
    ) -> ListVoiceProfilesResponseTypeDef:
        """
        Lists the voice profiles in a voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/list_voice_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#list_voice_profiles)
        """

    def put_sip_media_application_alexa_skill_configuration(
        self, **kwargs: Unpack[PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef]
    ) -> PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        Updates the Alexa Skill configuration for the SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_sip_media_application_alexa_skill_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_sip_media_application_alexa_skill_configuration)
        """

    def put_sip_media_application_logging_configuration(
        self, **kwargs: Unpack[PutSipMediaApplicationLoggingConfigurationRequestTypeDef]
    ) -> PutSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        Updates the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_sip_media_application_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_sip_media_application_logging_configuration)
        """

    def put_voice_connector_emergency_calling_configuration(
        self, **kwargs: Unpack[PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef]
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's emergency calling configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_emergency_calling_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_emergency_calling_configuration)
        """

    def put_voice_connector_external_systems_configuration(
        self, **kwargs: Unpack[PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef]
    ) -> PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef:
        """
        Adds an external systems configuration to a Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_external_systems_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_external_systems_configuration)
        """

    def put_voice_connector_logging_configuration(
        self, **kwargs: Unpack[PutVoiceConnectorLoggingConfigurationRequestTypeDef]
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_logging_configuration)
        """

    def put_voice_connector_origination(
        self, **kwargs: Unpack[PutVoiceConnectorOriginationRequestTypeDef]
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        Updates a Voice Connector's origination settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_origination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_origination)
        """

    def put_voice_connector_proxy(
        self, **kwargs: Unpack[PutVoiceConnectorProxyRequestTypeDef]
    ) -> PutVoiceConnectorProxyResponseTypeDef:
        """
        Puts the specified proxy configuration to the specified Amazon Chime SDK Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_proxy)
        """

    def put_voice_connector_streaming_configuration(
        self, **kwargs: Unpack[PutVoiceConnectorStreamingConfigurationRequestTypeDef]
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        Updates a Voice Connector's streaming configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_streaming_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_streaming_configuration)
        """

    def put_voice_connector_termination(
        self, **kwargs: Unpack[PutVoiceConnectorTerminationRequestTypeDef]
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        Updates a Voice Connector's termination settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_termination.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_termination)
        """

    def put_voice_connector_termination_credentials(
        self, **kwargs: Unpack[PutVoiceConnectorTerminationCredentialsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a Voice Connector's termination credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/put_voice_connector_termination_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#put_voice_connector_termination_credentials)
        """

    def restore_phone_number(
        self, **kwargs: Unpack[RestorePhoneNumberRequestTypeDef]
    ) -> RestorePhoneNumberResponseTypeDef:
        """
        Restores a deleted phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/restore_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#restore_phone_number)
        """

    def search_available_phone_numbers(
        self, **kwargs: Unpack[SearchAvailablePhoneNumbersRequestTypeDef]
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches the provisioned phone numbers in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/search_available_phone_numbers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#search_available_phone_numbers)
        """

    def start_speaker_search_task(
        self, **kwargs: Unpack[StartSpeakerSearchTaskRequestTypeDef]
    ) -> StartSpeakerSearchTaskResponseTypeDef:
        """
        Starts a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/start_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#start_speaker_search_task)
        """

    def start_voice_tone_analysis_task(
        self, **kwargs: Unpack[StartVoiceToneAnalysisTaskRequestTypeDef]
    ) -> StartVoiceToneAnalysisTaskResponseTypeDef:
        """
        Starts a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/start_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#start_voice_tone_analysis_task)
        """

    def stop_speaker_search_task(
        self, **kwargs: Unpack[StopSpeakerSearchTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a speaker search task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/stop_speaker_search_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#stop_speaker_search_task)
        """

    def stop_voice_tone_analysis_task(
        self, **kwargs: Unpack[StopVoiceToneAnalysisTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a voice tone analysis task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/stop_voice_tone_analysis_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#stop_voice_tone_analysis_task)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#untag_resource)
        """

    def update_global_settings(
        self, **kwargs: Unpack[UpdateGlobalSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates global settings for the Amazon Chime SDK Voice Connectors in an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_global_settings)
        """

    def update_phone_number(
        self, **kwargs: Unpack[UpdatePhoneNumberRequestTypeDef]
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates phone number details, such as product type, calling name, or phone
        number name for the specified phone number ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_phone_number.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_phone_number)
        """

    def update_phone_number_settings(
        self, **kwargs: Unpack[UpdatePhoneNumberSettingsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_phone_number_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_phone_number_settings)
        """

    def update_proxy_session(
        self, **kwargs: Unpack[UpdateProxySessionRequestTypeDef]
    ) -> UpdateProxySessionResponseTypeDef:
        """
        Updates the specified proxy session details, such as voice or SMS capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_proxy_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_proxy_session)
        """

    def update_sip_media_application(
        self, **kwargs: Unpack[UpdateSipMediaApplicationRequestTypeDef]
    ) -> UpdateSipMediaApplicationResponseTypeDef:
        """
        Updates the details of the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_sip_media_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_sip_media_application)
        """

    def update_sip_media_application_call(
        self, **kwargs: Unpack[UpdateSipMediaApplicationCallRequestTypeDef]
    ) -> UpdateSipMediaApplicationCallResponseTypeDef:
        """
        Invokes the AWS Lambda function associated with the SIP media application and
        transaction ID in an update request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_sip_media_application_call.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_sip_media_application_call)
        """

    def update_sip_rule(
        self, **kwargs: Unpack[UpdateSipRuleRequestTypeDef]
    ) -> UpdateSipRuleResponseTypeDef:
        """
        Updates the details of the specified SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_sip_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_sip_rule)
        """

    def update_voice_connector(
        self, **kwargs: Unpack[UpdateVoiceConnectorRequestTypeDef]
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        Updates the details for the specified Amazon Chime SDK Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_voice_connector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_voice_connector)
        """

    def update_voice_connector_group(
        self, **kwargs: Unpack[UpdateVoiceConnectorGroupRequestTypeDef]
    ) -> UpdateVoiceConnectorGroupResponseTypeDef:
        """
        Updates the settings for the specified Amazon Chime SDK Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_voice_connector_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_voice_connector_group)
        """

    def update_voice_profile(
        self, **kwargs: Unpack[UpdateVoiceProfileRequestTypeDef]
    ) -> UpdateVoiceProfileResponseTypeDef:
        """
        Updates the specified voice profile's voice print and refreshes its expiration
        timestamp.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_voice_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_voice_profile)
        """

    def update_voice_profile_domain(
        self, **kwargs: Unpack[UpdateVoiceProfileDomainRequestTypeDef]
    ) -> UpdateVoiceProfileDomainResponseTypeDef:
        """
        Updates the settings for the specified voice profile domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/update_voice_profile_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#update_voice_profile_domain)
        """

    def validate_e911_address(
        self, **kwargs: Unpack[ValidateE911AddressRequestTypeDef]
    ) -> ValidateE911AddressResponseTypeDef:
        """
        Validates an address to be used for 911 calls made with Amazon Chime SDK Voice
        Connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/validate_e911_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#validate_e911_address)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sip_media_applications"]
    ) -> ListSipMediaApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sip_rules"]
    ) -> ListSipRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client/#get_paginator)
        """
