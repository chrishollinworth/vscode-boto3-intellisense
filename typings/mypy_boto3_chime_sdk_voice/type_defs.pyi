"""
Type annotations for chime-sdk-voice service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_voice.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AlexaSkillStatusType,
    CallingNameStatusType,
    CapabilityType,
    ErrorCodeType,
    GeoMatchLevelType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberOrderTypeType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    SipRuleTriggerTypeType,
    VoiceConnectorAwsRegionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddressTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "CandidateAddressTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleRequestRequestTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    "DeleteSipRuleRequestRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    "DeleteVoiceConnectorRequestRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorRequestRequestTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleRequestRequestTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "ValidateE911AddressRequestRequestTypeDef",
    "ValidateE911AddressResponseTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "streetName": str,
        "streetSuffix": str,
        "postDirectional": str,
        "preDirectional": str,
        "streetNumber": str,
        "city": str,
        "state": str,
        "postalCode": str,
        "postalCodePlus4": str,
        "country": str,
    },
    total=False,
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef,
):
    pass

AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": List[str],
    },
)

BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": List["UpdatePhoneNumberRequestItemTypeDef"],
    },
)

BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CandidateAddressTypeDef = TypedDict(
    "CandidateAddressTypeDef",
    {
        "streetInfo": str,
        "streetNumber": str,
        "city": str,
        "state": str,
        "postalCode": str,
        "postalCodePlus4": str,
        "country": str,
    },
    total=False,
)

CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": List[str],
    },
)

CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": List[str],
        "Capabilities": List[CapabilityType],
    },
)
_OptionalCreateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProxySessionRequestRequestTypeDef",
    {
        "Name": str,
        "ExpiryMinutes": int,
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)

class CreateProxySessionRequestRequestTypeDef(
    _RequiredCreateProxySessionRequestRequestTypeDef,
    _OptionalCreateProxySessionRequestRequestTypeDef,
):
    pass

CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
    },
)
_OptionalCreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipHeaders": Dict[str, str],
        "ArgumentsMap": Dict[str, str],
    },
    total=False,
)

class CreateSipMediaApplicationCallRequestRequestTypeDef(
    _RequiredCreateSipMediaApplicationCallRequestRequestTypeDef,
    _OptionalCreateSipMediaApplicationCallRequestRequestTypeDef,
):
    pass

CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
)

CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
    },
)
_OptionalCreateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
    total=False,
)

class CreateSipRuleRequestRequestTypeDef(
    _RequiredCreateSipRuleRequestRequestTypeDef, _OptionalCreateSipRuleRequestRequestTypeDef
):
    pass

CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
    total=False,
)

class CreateVoiceConnectorGroupRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorGroupRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorGroupRequestRequestTypeDef,
):
    pass

CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
    },
)
_OptionalCreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorRequestRequestTypeDef",
    {
        "AwsRegion": VoiceConnectorAwsRegionType,
    },
    total=False,
)

class CreateVoiceConnectorRequestRequestTypeDef(
    _RequiredCreateVoiceConnectorRequestRequestTypeDef,
    _OptionalCreateVoiceConnectorRequestRequestTypeDef,
):
    pass

CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

_RequiredDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
    },
)
_OptionalDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationTypeDef",
    {
        "TestPhoneNumber": str,
    },
    total=False,
)

class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef,
    _OptionalDNISEmergencyCallingConfigurationTypeDef,
):
    pass

DeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DeleteProxySessionRequestRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

DeleteSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

DeleteSipRuleRequestRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

DeleteVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": List[str],
    },
)

DeleteVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": List["DNISEmergencyCallingConfigurationTypeDef"],
    },
    total=False,
)

GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)

GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionRequestRequestTypeDef = TypedDict(
    "GetProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": "SipMediaApplicationAlexaSkillConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipRuleRequestRequestTypeDef = TypedDict(
    "GetSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationHealthRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": "TerminationHealthTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableVoiceConnectorRegionsResponseTypeDef = TypedDict(
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    {
        "VoiceConnectorRegions": List[VoiceConnectorAwsRegionType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List["PhoneNumberOrderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "Status": str,
        "ProductType": PhoneNumberProductTypeType,
        "FilterName": PhoneNumberAssociationNameType,
        "FilterValue": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProxySessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProxySessionsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalListProxySessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProxySessionsRequestRequestTypeDef",
    {
        "Status": ProxySessionStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProxySessionsRequestRequestTypeDef(
    _RequiredListProxySessionsRequestRequestTypeDef, _OptionalListProxySessionsRequestRequestTypeDef
):
    pass

ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {
        "ProxySessions": List["ProxySessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipMediaApplicationsRequestRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {
        "SipMediaApplications": List["SipMediaApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipRulesRequestRequestTypeDef = TypedDict(
    "ListSipRulesRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {
        "SipRules": List["SipRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedPhoneNumberCountriesRequestRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)

ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List["PhoneNumberCountryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorGroupsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List["VoiceConnectorGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List["VoiceConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": bool,
    },
    total=False,
)

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": str,
        "Status": OrderedPhoneNumberStatusType,
    },
    total=False,
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocolType,
        "Priority": int,
        "Weight": int,
    },
    total=False,
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": List["OriginationRouteTypeDef"],
        "Disabled": bool,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": str,
        "ProxyPhoneNumber": str,
    },
    total=False,
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": str,
        "Name": PhoneNumberAssociationNameType,
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": str,
        "SupportedPhoneNumberTypes": List[PhoneNumberTypeType],
    },
    total=False,
)

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberOrderStatusType,
        "OrderType": PhoneNumberOrderTypeType,
        "OrderedPhoneNumbers": List["OrderedPhoneNumberTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Country": str,
        "Type": PhoneNumberTypeType,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberStatusType,
        "Capabilities": "PhoneNumberCapabilitiesTypeDef",
        "Associations": List["PhoneNumberAssociationTypeDef"],
        "CallingName": str,
        "CallingNameStatus": CallingNameStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
        "OrderId": str,
    },
    total=False,
)

ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Name": str,
        "Status": ProxySessionStatusType,
        "ExpiryMinutes": int,
        "Capabilities": List[CapabilityType],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "EndedTimestamp": datetime,
        "Participants": List["ParticipantTypeDef"],
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)

ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": int,
        "Disabled": bool,
        "FallBackPhoneNumber": str,
        "PhoneNumberCountries": List[str],
    },
    total=False,
)

_RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    },
    total=False,
)

class PutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef(
    _RequiredPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef,
    _OptionalPutSipMediaApplicationAlexaSkillConfigurationRequestRequestTypeDef,
):
    pass

PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    {
        "SipMediaApplicationAlexaSkillConfiguration": "SipMediaApplicationAlexaSkillConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
    },
    total=False,
)

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(
    _RequiredPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
    _OptionalPutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef,
):
    pass

PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": "OriginationTypeDef",
    },
)

PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": List[str],
    },
)
_OptionalPutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "FallBackPhoneNumber": str,
        "Disabled": bool,
    },
    total=False,
)

class PutVoiceConnectorProxyRequestRequestTypeDef(
    _RequiredPutVoiceConnectorProxyRequestRequestTypeDef,
    _OptionalPutVoiceConnectorProxyRequestRequestTypeDef,
):
    pass

PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "Credentials": List["CredentialTypeDef"],
    },
    total=False,
)

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(
    _RequiredPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
    _OptionalPutVoiceConnectorTerminationCredentialsRequestRequestTypeDef,
):
    pass

PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": "TerminationTypeDef",
    },
)

PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "AreaCode": str,
        "City": str,
        "Country": str,
        "State": str,
        "TollFreePrefix": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SipMediaApplicationAlexaSkillConfigurationTypeDef = TypedDict(
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    {
        "AlexaSkillStatus": AlexaSkillStatusType,
        "AlexaSkillIds": List[str],
    },
)

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": str,
    },
    total=False,
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": str,
    },
    total=False,
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": bool,
    },
    total=False,
)

SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "Priority": int,
        "AwsRegion": str,
    },
    total=False,
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": bool,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredStreamingConfigurationTypeDef = TypedDict(
    "_RequiredStreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": bool,
    },
)
_OptionalStreamingConfigurationTypeDef = TypedDict(
    "_OptionalStreamingConfigurationTypeDef",
    {
        "StreamingNotificationTargets": List["StreamingNotificationTargetTypeDef"],
    },
    total=False,
)

class StreamingConfigurationTypeDef(
    _RequiredStreamingConfigurationTypeDef, _OptionalStreamingConfigurationTypeDef
):
    pass

StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
    total=False,
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": datetime,
        "Source": str,
    },
    total=False,
)

TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
    },
    total=False,
)

_RequiredUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestItemTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, _OptionalUpdatePhoneNumberRequestItemTypeDef
):
    pass

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePhoneNumberSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    {
        "CallingName": str,
    },
)

_RequiredUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": List[CapabilityType],
    },
)
_OptionalUpdateProxySessionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProxySessionRequestRequestTypeDef",
    {
        "ExpiryMinutes": int,
    },
    total=False,
)

class UpdateProxySessionRequestRequestTypeDef(
    _RequiredUpdateProxySessionRequestRequestTypeDef,
    _OptionalUpdateProxySessionRequestRequestTypeDef,
):
    pass

UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Dict[str, str],
    },
)

UpdateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalUpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
    total=False,
)

class UpdateSipMediaApplicationRequestRequestTypeDef(
    _RequiredUpdateSipMediaApplicationRequestRequestTypeDef,
    _OptionalUpdateSipMediaApplicationRequestRequestTypeDef,
):
    pass

UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
    },
)
_OptionalUpdateSipRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSipRuleRequestRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
    total=False,
)

class UpdateSipRuleRequestRequestTypeDef(
    _RequiredUpdateSipRuleRequestRequestTypeDef, _OptionalUpdateSipRuleRequestRequestTypeDef
):
    pass

UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
)

UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)

UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateE911AddressRequestRequestTypeDef = TypedDict(
    "ValidateE911AddressRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "StreetNumber": str,
        "StreetInfo": str,
        "City": str,
        "State": str,
        "Country": str,
        "PostalCode": str,
    },
)

ValidateE911AddressResponseTypeDef = TypedDict(
    "ValidateE911AddressResponseTypeDef",
    {
        "ValidationResult": int,
        "AddressExternalId": str,
        "Address": "AddressTypeDef",
        "CandidateAddressList": List["CandidateAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "VoiceConnectorGroupArn": str,
    },
    total=False,
)

VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": VoiceConnectorAwsRegionType,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "VoiceConnectorArn": str,
    },
    total=False,
)
