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
    GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorProxyResponseTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    ListAvailableVoiceConnectorRegionsResponseTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListProxySessionsResponseTypeDef,
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesResponseTypeDef,
    ListSupportedPhoneNumberCountriesResponseTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
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
    SipMediaApplicationAlexaSkillConfigurationTypeDef,
    SipMediaApplicationEndpointTypeDef,
    SipMediaApplicationLoggingConfigurationTypeDef,
    SipRuleTargetApplicationTypeDef,
    StreamingConfigurationTypeDef,
    TerminationTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdateProxySessionResponseTypeDef,
    UpdateSipMediaApplicationCallResponseTypeDef,
    UpdateSipMediaApplicationResponseTypeDef,
    UpdateSipRuleResponseTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
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
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]

class ChimeSDKVoiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnector>`_ **Request
        Syntax** response = client.associate_phone_numbers_with_voice_connector(
        VoiceConnectorId='string', E164PhoneNumbers=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.associate_phone_numbers_with_voice_connector)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/AssociatePhoneNumbersWithVoiceConnectorGroup>`_ **Request
        Syntax** response = client.associate_phone_numbers_with_voice_connector_group(
        VoiceConnectorGroupId='string', E164Ph...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.associate_phone_numbers_with_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#associate_phone_numbers_with_voice_connector_group)
        """
    def batch_delete_phone_number(
        self, *, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/BatchDeletePhoneNumber>`_ **Request Syntax** response =
        client.batch_delete_phone_number( PhoneNumberIds=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.batch_delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#batch_delete_phone_number)
        """
    def batch_update_phone_number(
        self, *, UpdatePhoneNumberRequestItems: List["UpdatePhoneNumberRequestItemTypeDef"]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/BatchUpdatePhoneNumber>`_ **Request Syntax** response =
        client.batch_update_phone_number( UpdatePhoneNumberRequestItems=[ {
        'PhoneNumberId': 'string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.batch_update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#batch_update_phone_number)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#close)
        """
    def create_phone_number_order(
        self, *, ProductType: PhoneNumberProductTypeType, E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreatePhoneNumberOrder>`_ **Request Syntax** response =
        client.create_phone_number_order(
        ProductType='VoiceConnector'|'SipMediaApplicationDialIn', E164PhoneNumbers=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_phone_number_order)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateProxySession>`_ **Request Syntax** response =
        client.create_proxy_session( VoiceConnectorId='string',
        ParticipantPhoneNumbers=[ 'string', ], Name='...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_proxy_session)
        """
    def create_sip_media_application(
        self, *, AwsRegion: str, Name: str, Endpoints: List["SipMediaApplicationEndpointTypeDef"]
    ) -> CreateSipMediaApplicationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateSipMediaApplication>`_ **Request Syntax** response =
        client.create_sip_media_application( AwsRegion='string', Name='string',
        Endpoints=[ { ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_media_application)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateSipMediaApplicationCall>`_ **Request Syntax**
        response = client.create_sip_media_application_call( FromPhoneNumber='string',
        ToPhoneNumber='string', SipMediaApplic...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_media_application_call)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateSipRule>`_ **Request Syntax** response =
        client.create_sip_rule( Name='string',
        TriggerType='ToPhoneNumber'|'RequestUriHostname', TriggerValue='string', Disa...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_sip_rule)
        """
    def create_voice_connector(
        self, *, Name: str, RequireEncryption: bool, AwsRegion: VoiceConnectorAwsRegionType = None
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateVoiceConnector>`_ **Request Syntax** response =
        client.create_voice_connector( Name='string', AwsRegion='us-east-1'|'us-
        west-2'|'ca-central-1'|'eu-central-1'|'eu-west-1'...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_connector)
        """
    def create_voice_connector_group(
        self, *, Name: str, VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/CreateVoiceConnectorGroup>`_ **Request Syntax** response =
        client.create_voice_connector_group( Name='string', VoiceConnectorItems=[ {
        'VoiceConnectorI...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.create_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#create_voice_connector_group)
        """
    def delete_phone_number(self, *, PhoneNumberId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeletePhoneNumber>`_ **Request Syntax** response =
        client.delete_phone_number( PhoneNumberId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_phone_number)
        """
    def delete_proxy_session(self, *, VoiceConnectorId: str, ProxySessionId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteProxySession>`_ **Request Syntax** response =
        client.delete_proxy_session( VoiceConnectorId='string', ProxySessionId='string'
        ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_proxy_session)
        """
    def delete_sip_media_application(self, *, SipMediaApplicationId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteSipMediaApplication>`_ **Request Syntax** response =
        client.delete_sip_media_application( SipMediaApplicationId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_sip_media_application)
        """
    def delete_sip_rule(self, *, SipRuleId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteSipRule>`_ **Request Syntax** response =
        client.delete_sip_rule( SipRuleId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_sip_rule)
        """
    def delete_voice_connector(self, *, VoiceConnectorId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnector>`_ **Request Syntax** response =
        client.delete_voice_connector( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector)
        """
    def delete_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorEmergencyCallingConfiguration>`_
        **Request Syntax** response =
        client.delete_voice_connector_emergency_calling_configuration(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_emergency_calling_configuration)
        """
    def delete_voice_connector_group(self, *, VoiceConnectorGroupId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorGroup>`_ **Request Syntax** response =
        client.delete_voice_connector_group( VoiceConnectorGroupId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_group)
        """
    def delete_voice_connector_origination(self, *, VoiceConnectorId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorOrigination>`_ **Request Syntax**
        response = client.delete_voice_connector_origination( VoiceConnectorId='string'
        ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_origination)
        """
    def delete_voice_connector_proxy(self, *, VoiceConnectorId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorProxy>`_ **Request Syntax** response =
        client.delete_voice_connector_proxy( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_proxy)
        """
    def delete_voice_connector_streaming_configuration(self, *, VoiceConnectorId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorStreamingConfiguration>`_ **Request
        Syntax** response = client.delete_voice_connector_streaming_configuration(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_streaming_configuration)
        """
    def delete_voice_connector_termination(self, *, VoiceConnectorId: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorTermination>`_ **Request Syntax**
        response = client.delete_voice_connector_termination( VoiceConnectorId='string'
        ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_termination)
        """
    def delete_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Usernames: List[str]
    ) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DeleteVoiceConnectorTerminationCredentials>`_ **Request
        Syntax** response = client.delete_voice_connector_termination_credentials(
        VoiceConnectorId='string', Usernames=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.delete_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#delete_voice_connector_termination_credentials)
        """
    def disassociate_phone_numbers_from_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DisassociatePhoneNumbersFromVoiceConnector>`_ **Request
        Syntax** response = client.disassociate_phone_numbers_from_voice_connector(
        VoiceConnectorId='string', E164PhoneNumbers...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.disassociate_phone_numbers_from_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#disassociate_phone_numbers_from_voice_connector)
        """
    def disassociate_phone_numbers_from_voice_connector_group(
        self, *, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/DisassociatePhoneNumbersFromVoiceConnectorGroup>`_
        **Request Syntax** response =
        client.disassociate_phone_numbers_from_voice_connector_group(
        VoiceConnectorGroupId='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.disassociate_phone_numbers_from_voice_connector_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#generate_presigned_url)
        """
    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetGlobalSettings>`_ **Request Syntax** response =
        client.get_global_settings().

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_global_settings)
        """
    def get_phone_number(self, *, PhoneNumberId: str) -> GetPhoneNumberResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetPhoneNumber>`_ **Request Syntax** response =
        client.get_phone_number( PhoneNumberId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number)
        """
    def get_phone_number_order(
        self, *, PhoneNumberOrderId: str
    ) -> GetPhoneNumberOrderResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetPhoneNumberOrder>`_ **Request Syntax** response =
        client.get_phone_number_order( PhoneNumberOrderId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number_order)
        """
    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetPhoneNumberSettings>`_ **Request Syntax** response =
        client.get_phone_number_settings().

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_phone_number_settings)
        """
    def get_proxy_session(
        self, *, VoiceConnectorId: str, ProxySessionId: str
    ) -> GetProxySessionResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetProxySession>`_ **Request Syntax** response =
        client.get_proxy_session( VoiceConnectorId='string', ProxySessionId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_proxy_session)
        """
    def get_sip_media_application(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetSipMediaApplication>`_ **Request Syntax** response =
        client.get_sip_media_application( SipMediaApplicationId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application)
        """
    def get_sip_media_application_alexa_skill_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetSipMediaApplicationAlexaSkillConfiguration>`_ **Request
        Syntax** response = client.get_sip_media_application_alexa_skill_configuration(
        SipMediaApplicationId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application_alexa_skill_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application_alexa_skill_configuration)
        """
    def get_sip_media_application_logging_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetSipMediaApplicationLoggingConfiguration>`_ **Request
        Syntax** response = client.get_sip_media_application_logging_configuration(
        SipMediaApplicationId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_media_application_logging_configuration)
        """
    def get_sip_rule(self, *, SipRuleId: str) -> GetSipRuleResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetSipRule>`_ **Request Syntax** response =
        client.get_sip_rule( SipRuleId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_sip_rule)
        """
    def get_voice_connector(self, *, VoiceConnectorId: str) -> GetVoiceConnectorResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnector>`_ **Request Syntax** response =
        client.get_voice_connector( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector)
        """
    def get_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration>`_ **Request
        Syntax** response = client.get_voice_connector_emergency_calling_configuration(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_emergency_calling_configuration)
        """
    def get_voice_connector_group(
        self, *, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorGroup>`_ **Request Syntax** response =
        client.get_voice_connector_group( VoiceConnectorGroupId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_group)
        """
    def get_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorLoggingConfiguration>`_ **Request Syntax**
        response = client.get_voice_connector_logging_configuration(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_logging_configuration)
        """
    def get_voice_connector_origination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorOrigination>`_ **Request Syntax** response
        = client.get_voice_connector_origination( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_origination)
        """
    def get_voice_connector_proxy(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorProxyResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorProxy>`_ **Request Syntax** response =
        client.get_voice_connector_proxy( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_proxy)
        """
    def get_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorStreamingConfiguration>`_ **Request
        Syntax** response = client.get_voice_connector_streaming_configuration(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_streaming_configuration)
        """
    def get_voice_connector_termination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorTermination>`_ **Request Syntax** response
        = client.get_voice_connector_termination( VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_termination)
        """
    def get_voice_connector_termination_health(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/GetVoiceConnectorTerminationHealth>`_ **Request Syntax**
        response = client.get_voice_connector_termination_health(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.get_voice_connector_termination_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#get_voice_connector_termination_health)
        """
    def list_available_voice_connector_regions(
        self,
    ) -> ListAvailableVoiceConnectorRegionsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions>`_ **Request Syntax**
        response = client.list_available_voice_connector_regions().

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_available_voice_connector_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_available_voice_connector_regions)
        """
    def list_phone_number_orders(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListPhoneNumberOrders>`_ **Request Syntax** response =
        client.list_phone_number_orders( NextToken='string', MaxResults=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_phone_number_orders)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListPhoneNumbers>`_ **Request Syntax** response =
        client.list_phone_numbers( Status='string',
        ProductType='VoiceConnector'|'SipMediaApplicationDialIn', FilterName='Voice...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_phone_numbers)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListProxySessions>`_ **Request Syntax** response =
        client.list_proxy_sessions( VoiceConnectorId='string',
        Status='Open'|'InProgress'|'Closed', NextToken='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_proxy_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_proxy_sessions)
        """
    def list_sip_media_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSipMediaApplicationsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListSipMediaApplications>`_ **Request Syntax** response =
        client.list_sip_media_applications( MaxResults=123, NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_sip_media_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_sip_media_applications)
        """
    def list_sip_rules(
        self, *, SipMediaApplicationId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSipRulesResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListSipRules>`_ **Request Syntax** response =
        client.list_sip_rules( SipMediaApplicationId='string', MaxResults=123,
        NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_sip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_sip_rules)
        """
    def list_supported_phone_number_countries(
        self, *, ProductType: PhoneNumberProductTypeType
    ) -> ListSupportedPhoneNumberCountriesResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListSupportedPhoneNumberCountries>`_ **Request Syntax**
        response = client.list_supported_phone_number_countries(
        ProductType='VoiceConnector'|'SipMediaApplicationDialIn' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_supported_phone_number_countries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_supported_phone_number_countries)
        """
    def list_voice_connector_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListVoiceConnectorGroups>`_ **Request Syntax** response =
        client.list_voice_connector_groups( NextToken='string', MaxResults=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connector_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connector_groups)
        """
    def list_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListVoiceConnectorTerminationCredentials>`_ **Request
        Syntax** response = client.list_voice_connector_termination_credentials(
        VoiceConnectorId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connector_termination_credentials)
        """
    def list_voice_connectors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ListVoiceConnectors>`_ **Request Syntax** response =
        client.list_voice_connectors( NextToken='string', MaxResults=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.list_voice_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#list_voice_connectors)
        """
    def put_sip_media_application_alexa_skill_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationAlexaSkillConfiguration: "SipMediaApplicationAlexaSkillConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutSipMediaApplicationAlexaSkillConfiguration>`_ **Request
        Syntax** response = client.put_sip_media_application_alexa_skill_configuration(
        SipMediaApplicationId='string', SipM...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_sip_media_application_alexa_skill_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_sip_media_application_alexa_skill_configuration)
        """
    def put_sip_media_application_logging_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutSipMediaApplicationLoggingConfiguration>`_ **Request
        Syntax** response = client.put_sip_media_application_logging_configuration(
        SipMediaApplicationId='string', SipMediaApp...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_sip_media_application_logging_configuration)
        """
    def put_voice_connector_emergency_calling_configuration(
        self,
        *,
        VoiceConnectorId: str,
        EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorEmergencyCallingConfiguration>`_ **Request
        Syntax** response = client.put_voice_connector_emergency_calling_configuration(
        VoiceConnectorId='string', Emergenc...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_emergency_calling_configuration)
        """
    def put_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorLoggingConfiguration>`_ **Request Syntax**
        response = client.put_voice_connector_logging_configuration(
        VoiceConnectorId='string', LoggingConfiguration={ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_logging_configuration)
        """
    def put_voice_connector_origination(
        self, *, VoiceConnectorId: str, Origination: "OriginationTypeDef"
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorOrigination>`_ **Request Syntax** response
        = client.put_voice_connector_origination( VoiceConnectorId='string',
        Origination={ 'Routes': [ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_origination)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorProxy>`_ **Request Syntax** response =
        client.put_voice_connector_proxy( VoiceConnectorId='string',
        DefaultSessionExpiryMinutes=123, PhoneNumberPoolCoun...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_proxy)
        """
    def put_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str, StreamingConfiguration: "StreamingConfigurationTypeDef"
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration>`_ **Request
        Syntax** response = client.put_voice_connector_streaming_configuration(
        VoiceConnectorId='string', StreamingConfiguration=...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_streaming_configuration)
        """
    def put_voice_connector_termination(
        self, *, VoiceConnectorId: str, Termination: "TerminationTypeDef"
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorTermination>`_ **Request Syntax** response
        = client.put_voice_connector_termination( VoiceConnectorId='string',
        Termination={ 'CpsLimit': 123, ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_termination)
        """
    def put_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Credentials: List["CredentialTypeDef"] = None
    ) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/PutVoiceConnectorTerminationCredentials>`_ **Request
        Syntax** response = client.put_voice_connector_termination_credentials(
        VoiceConnectorId='string', Credentials=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.put_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#put_voice_connector_termination_credentials)
        """
    def restore_phone_number(self, *, PhoneNumberId: str) -> RestorePhoneNumberResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/RestorePhoneNumber>`_ **Request Syntax** response =
        client.restore_phone_number( PhoneNumberId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.restore_phone_number)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/SearchAvailablePhoneNumbers>`_ **Request Syntax** response
        = client.search_available_phone_numbers( AreaCode='string', City='string',
        Country='string', State='stri...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.search_available_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#search_available_phone_numbers)
        """
    def update_global_settings(
        self, *, VoiceConnector: "VoiceConnectorSettingsTypeDef" = None
    ) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateGlobalSettings>`_ **Request Syntax** response =
        client.update_global_settings( VoiceConnector={ 'CdrBucket': 'string' } ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_global_settings)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdatePhoneNumber>`_ **Request Syntax** response =
        client.update_phone_number( PhoneNumberId='string',
        ProductType='VoiceConnector'|'SipMediaApplicationDialIn', CallingN...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_phone_number)
        """
    def update_phone_number_settings(self, *, CallingName: str) -> None:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdatePhoneNumberSettings>`_ **Request Syntax** response =
        client.update_phone_number_settings( CallingName='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_phone_number_settings)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateProxySession>`_ **Request Syntax** response =
        client.update_proxy_session( VoiceConnectorId='string', ProxySessionId='string',
        Capabilities=[ 'Voice'|'SM...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_proxy_session)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateSipMediaApplication>`_ **Request Syntax** response =
        client.update_sip_media_application( SipMediaApplicationId='string',
        Name='string', Endpoints=[ { ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_sip_media_application)
        """
    def update_sip_media_application_call(
        self, *, SipMediaApplicationId: str, TransactionId: str, Arguments: Dict[str, str]
    ) -> UpdateSipMediaApplicationCallResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateSipMediaApplicationCall>`_ **Request Syntax**
        response = client.update_sip_media_application_call(
        SipMediaApplicationId='string', TransactionId='string', Argument...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_media_application_call)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateSipRule>`_ **Request Syntax** response =
        client.update_sip_rule( SipRuleId='string', Name='string', Disabled=True|False,
        TargetApplications=[ { ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_sip_rule)
        """
    def update_voice_connector(
        self, *, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateVoiceConnector>`_ **Request Syntax** response =
        client.update_voice_connector( VoiceConnectorId='string', Name='string',
        RequireEncryption=True|False ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_connector)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/UpdateVoiceConnectorGroup>`_ **Request Syntax** response =
        client.update_voice_connector_group( VoiceConnectorGroupId='string',
        Name='string', VoiceConnectorItems=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.update_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#update_voice_connector_group)
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
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chime-
        sdk-voice-2022-08-03/ValidateE911Address>`_ **Request Syntax** response =
        client.validate_e911_address( AwsAccountId='string', StreetNumber='string',
        StreetInfo='string', City='string'...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Client.validate_e911_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/client.html#validate_e911_address)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sip_media_applications"]
    ) -> ListSipMediaApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipMediaApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsipmediaapplicationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_sip_rules"]) -> ListSipRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/chime-sdk-voice.html#ChimeSDKVoice.Paginator.ListSipRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/paginators.html#listsiprulespaginator)
        """
