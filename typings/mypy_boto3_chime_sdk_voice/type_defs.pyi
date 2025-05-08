"""
Type annotations for chime-sdk-voice service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_voice/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chime_sdk_voice.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AlexaSkillStatusType,
    CallingNameStatusType,
    CallLegTypeType,
    CapabilityType,
    ContactCenterSystemTypeType,
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
    SessionBorderControllerTypeType,
    SipRuleTriggerTypeType,
    VoiceConnectorAwsRegionType,
    VoiceConnectorIntegrationTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddressTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "BatchDeletePhoneNumberRequestTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchUpdatePhoneNumberRequestTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "CallDetailsTypeDef",
    "CandidateAddressTypeDef",
    "CreatePhoneNumberOrderRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateSipMediaApplicationCallRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationRequestTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleRequestTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateVoiceConnectorGroupRequestTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorRequestTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CreateVoiceProfileDomainRequestTypeDef",
    "CreateVoiceProfileDomainResponseTypeDef",
    "CreateVoiceProfileRequestTypeDef",
    "CreateVoiceProfileResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeletePhoneNumberRequestTypeDef",
    "DeleteProxySessionRequestTypeDef",
    "DeleteSipMediaApplicationRequestTypeDef",
    "DeleteSipRuleRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestTypeDef",
    "DeleteVoiceConnectorRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestTypeDef",
    "DeleteVoiceProfileDomainRequestTypeDef",
    "DeleteVoiceProfileRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "EmergencyCallingConfigurationOutputTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EmergencyCallingConfigurationUnionTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExternalSystemsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetPhoneNumberOrderRequestTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberRequestTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionRequestTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef",
    "GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationRequestTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleRequestTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetSpeakerSearchTaskRequestTypeDef",
    "GetSpeakerSearchTaskResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef",
    "GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupRequestTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationRequestTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyRequestTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorRequestTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthRequestTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationRequestTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "GetVoiceProfileDomainRequestTypeDef",
    "GetVoiceProfileDomainResponseTypeDef",
    "GetVoiceProfileRequestTypeDef",
    "GetVoiceProfileResponseTypeDef",
    "GetVoiceToneAnalysisTaskRequestTypeDef",
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    "ListAvailableVoiceConnectorRegionsResponseTypeDef",
    "ListPhoneNumberOrdersRequestTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsRequestTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListSipMediaApplicationsRequestPaginateTypeDef",
    "ListSipMediaApplicationsRequestTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesRequestPaginateTypeDef",
    "ListSipRulesRequestTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVoiceConnectorGroupsRequestTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsRequestTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "ListVoiceProfileDomainsRequestTypeDef",
    "ListVoiceProfileDomainsResponseTypeDef",
    "ListVoiceProfilesRequestTypeDef",
    "ListVoiceProfilesResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "MediaInsightsConfigurationTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationOutputTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "OriginationUnionTypeDef",
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
    "PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef",
    "PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef",
    "PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyRequestTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestTypeDef",
    "PutVoiceConnectorTerminationRequestTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "SearchAvailablePhoneNumbersRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationOutputTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationTypeDef",
    "SipMediaApplicationAlexaSkillConfigurationUnionTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "SpeakerSearchDetailsTypeDef",
    "SpeakerSearchResultTypeDef",
    "SpeakerSearchTaskTypeDef",
    "StartSpeakerSearchTaskRequestTypeDef",
    "StartSpeakerSearchTaskResponseTypeDef",
    "StartVoiceToneAnalysisTaskRequestTypeDef",
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    "StopSpeakerSearchTaskRequestTypeDef",
    "StopVoiceToneAnalysisTaskRequestTypeDef",
    "StreamingConfigurationOutputTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingConfigurationUnionTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TerminationHealthTypeDef",
    "TerminationOutputTypeDef",
    "TerminationTypeDef",
    "TerminationUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateGlobalSettingsRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestTypeDef",
    "UpdateProxySessionRequestTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateSipMediaApplicationCallRequestTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationRequestTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleRequestTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateVoiceConnectorGroupRequestTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorRequestTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "UpdateVoiceProfileDomainRequestTypeDef",
    "UpdateVoiceProfileDomainResponseTypeDef",
    "UpdateVoiceProfileRequestTypeDef",
    "UpdateVoiceProfileResponseTypeDef",
    "ValidateE911AddressRequestTypeDef",
    "ValidateE911AddressResponseTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
    "VoiceProfileDomainSummaryTypeDef",
    "VoiceProfileDomainTypeDef",
    "VoiceProfileSummaryTypeDef",
    "VoiceProfileTypeDef",
    "VoiceToneAnalysisTaskTypeDef",
)

class AddressTypeDef(TypedDict):
    streetName: NotRequired[str]
    streetSuffix: NotRequired[str]
    postDirectional: NotRequired[str]
    preDirectional: NotRequired[str]
    streetNumber: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    postalCodePlus4: NotRequired[str]
    country: NotRequired[str]

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef(TypedDict):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: NotRequired[bool]

class PhoneNumberErrorTypeDef(TypedDict):
    PhoneNumberId: NotRequired[str]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: NotRequired[bool]

class BatchDeletePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberIds: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(TypedDict):
    PhoneNumberId: str
    ProductType: NotRequired[PhoneNumberProductTypeType]
    CallingName: NotRequired[str]
    Name: NotRequired[str]

class CallDetailsTypeDef(TypedDict):
    VoiceConnectorId: NotRequired[str]
    TransactionId: NotRequired[str]
    IsCaller: NotRequired[bool]

class CandidateAddressTypeDef(TypedDict):
    streetInfo: NotRequired[str]
    streetNumber: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postalCode: NotRequired[str]
    postalCodePlus4: NotRequired[str]
    country: NotRequired[str]

class CreatePhoneNumberOrderRequestTypeDef(TypedDict):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]
    Name: NotRequired[str]

class GeoMatchParamsTypeDef(TypedDict):
    Country: str
    AreaCode: str

class CreateSipMediaApplicationCallRequestTypeDef(TypedDict):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: NotRequired[Mapping[str, str]]
    ArgumentsMap: NotRequired[Mapping[str, str]]

class SipMediaApplicationCallTypeDef(TypedDict):
    TransactionId: NotRequired[str]

class SipMediaApplicationEndpointTypeDef(TypedDict):
    LambdaArn: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class SipRuleTargetApplicationTypeDef(TypedDict):
    SipMediaApplicationId: NotRequired[str]
    Priority: NotRequired[int]
    AwsRegion: NotRequired[str]

class VoiceConnectorItemTypeDef(TypedDict):
    VoiceConnectorId: str
    Priority: int

class VoiceConnectorTypeDef(TypedDict):
    VoiceConnectorId: NotRequired[str]
    AwsRegion: NotRequired[VoiceConnectorAwsRegionType]
    Name: NotRequired[str]
    OutboundHostName: NotRequired[str]
    RequireEncryption: NotRequired[bool]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    VoiceConnectorArn: NotRequired[str]
    IntegrationType: NotRequired[VoiceConnectorIntegrationTypeType]

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    KmsKeyArn: str

class CreateVoiceProfileRequestTypeDef(TypedDict):
    SpeakerSearchTaskId: str

class VoiceProfileTypeDef(TypedDict):
    VoiceProfileId: NotRequired[str]
    VoiceProfileArn: NotRequired[str]
    VoiceProfileDomainId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    ExpirationTimestamp: NotRequired[datetime]

class CredentialTypeDef(TypedDict):
    Username: NotRequired[str]
    Password: NotRequired[str]

class DNISEmergencyCallingConfigurationTypeDef(TypedDict):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: NotRequired[str]

class DeletePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class DeleteProxySessionRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    ProxySessionId: str

class DeleteSipMediaApplicationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str

class DeleteSipRuleRequestTypeDef(TypedDict):
    SipRuleId: str

class DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorGroupRequestTypeDef(TypedDict):
    VoiceConnectorGroupId: str

class DeleteVoiceConnectorOriginationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorProxyRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorStreamingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceConnectorTerminationCredentialsRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Usernames: Sequence[str]

class DeleteVoiceConnectorTerminationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class DeleteVoiceProfileDomainRequestTypeDef(TypedDict):
    VoiceProfileDomainId: str

class DeleteVoiceProfileRequestTypeDef(TypedDict):
    VoiceProfileId: str

class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef(TypedDict):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]

class DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]

class ExternalSystemsConfigurationTypeDef(TypedDict):
    SessionBorderControllerTypes: NotRequired[List[SessionBorderControllerTypeType]]
    ContactCenterSystemTypes: NotRequired[List[ContactCenterSystemTypeType]]

class VoiceConnectorSettingsTypeDef(TypedDict):
    CdrBucket: NotRequired[str]

class GetPhoneNumberOrderRequestTypeDef(TypedDict):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class GetProxySessionRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    ProxySessionId: str

class GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str

class SipMediaApplicationAlexaSkillConfigurationOutputTypeDef(TypedDict):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: List[str]

class GetSipMediaApplicationLoggingConfigurationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str

class SipMediaApplicationLoggingConfigurationTypeDef(TypedDict):
    EnableSipMediaApplicationMessageLogs: NotRequired[bool]

class GetSipMediaApplicationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str

class GetSipRuleRequestTypeDef(TypedDict):
    SipRuleId: str

class GetSpeakerSearchTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class GetVoiceConnectorGroupRequestTypeDef(TypedDict):
    VoiceConnectorGroupId: str

class GetVoiceConnectorLoggingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class LoggingConfigurationTypeDef(TypedDict):
    EnableSIPLogs: NotRequired[bool]
    EnableMediaMetricLogs: NotRequired[bool]

class GetVoiceConnectorOriginationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class GetVoiceConnectorProxyRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class ProxyTypeDef(TypedDict):
    DefaultSessionExpiryMinutes: NotRequired[int]
    Disabled: NotRequired[bool]
    FallBackPhoneNumber: NotRequired[str]
    PhoneNumberCountries: NotRequired[List[str]]

class GetVoiceConnectorRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class GetVoiceConnectorStreamingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class GetVoiceConnectorTerminationHealthRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class TerminationHealthTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]
    Source: NotRequired[str]

class GetVoiceConnectorTerminationRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class TerminationOutputTypeDef(TypedDict):
    CpsLimit: NotRequired[int]
    DefaultPhoneNumber: NotRequired[str]
    CallingRegions: NotRequired[List[str]]
    CidrAllowedList: NotRequired[List[str]]
    Disabled: NotRequired[bool]

class GetVoiceProfileDomainRequestTypeDef(TypedDict):
    VoiceProfileDomainId: str

class GetVoiceProfileRequestTypeDef(TypedDict):
    VoiceProfileId: str

class GetVoiceToneAnalysisTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str
    IsCaller: bool

class ListPhoneNumberOrdersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPhoneNumbersRequestTypeDef(TypedDict):
    Status: NotRequired[str]
    ProductType: NotRequired[PhoneNumberProductTypeType]
    FilterName: NotRequired[PhoneNumberAssociationNameType]
    FilterValue: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListProxySessionsRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Status: NotRequired[ProxySessionStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSipMediaApplicationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSipRulesRequestTypeDef(TypedDict):
    SipMediaApplicationId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSupportedPhoneNumberCountriesRequestTypeDef(TypedDict):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(TypedDict):
    CountryCode: NotRequired[str]
    SupportedPhoneNumberTypes: NotRequired[List[PhoneNumberTypeType]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class ListVoiceConnectorGroupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListVoiceConnectorTerminationCredentialsRequestTypeDef(TypedDict):
    VoiceConnectorId: str

class ListVoiceConnectorsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListVoiceProfileDomainsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class VoiceProfileDomainSummaryTypeDef(TypedDict):
    VoiceProfileDomainId: NotRequired[str]
    VoiceProfileDomainArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class ListVoiceProfilesRequestTypeDef(TypedDict):
    VoiceProfileDomainId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class VoiceProfileSummaryTypeDef(TypedDict):
    VoiceProfileId: NotRequired[str]
    VoiceProfileArn: NotRequired[str]
    VoiceProfileDomainId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    ExpirationTimestamp: NotRequired[datetime]

class MediaInsightsConfigurationTypeDef(TypedDict):
    Disabled: NotRequired[bool]
    ConfigurationArn: NotRequired[str]

class OrderedPhoneNumberTypeDef(TypedDict):
    E164PhoneNumber: NotRequired[str]
    Status: NotRequired[OrderedPhoneNumberStatusType]

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[OriginationRouteProtocolType],
        "Priority": NotRequired[int],
        "Weight": NotRequired[int],
    },
)

class ParticipantTypeDef(TypedDict):
    PhoneNumber: NotRequired[str]
    ProxyPhoneNumber: NotRequired[str]

class PhoneNumberAssociationTypeDef(TypedDict):
    Value: NotRequired[str]
    Name: NotRequired[PhoneNumberAssociationNameType]
    AssociatedTimestamp: NotRequired[datetime]

class PhoneNumberCapabilitiesTypeDef(TypedDict):
    InboundCall: NotRequired[bool]
    OutboundCall: NotRequired[bool]
    InboundSMS: NotRequired[bool]
    OutboundSMS: NotRequired[bool]
    InboundMMS: NotRequired[bool]
    OutboundMMS: NotRequired[bool]

class PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    SessionBorderControllerTypes: NotRequired[Sequence[SessionBorderControllerTypeType]]
    ContactCenterSystemTypes: NotRequired[Sequence[ContactCenterSystemTypeType]]

class PutVoiceConnectorProxyRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: NotRequired[str]
    Disabled: NotRequired[bool]

class RestorePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class SearchAvailablePhoneNumbersRequestTypeDef(TypedDict):
    AreaCode: NotRequired[str]
    City: NotRequired[str]
    Country: NotRequired[str]
    State: NotRequired[str]
    TollFreePrefix: NotRequired[str]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SipMediaApplicationAlexaSkillConfigurationTypeDef(TypedDict):
    AlexaSkillStatus: AlexaSkillStatusType
    AlexaSkillIds: Sequence[str]

class SpeakerSearchResultTypeDef(TypedDict):
    ConfidenceScore: NotRequired[float]
    VoiceProfileId: NotRequired[str]

class StartSpeakerSearchTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    TransactionId: str
    VoiceProfileDomainId: str
    ClientRequestToken: NotRequired[str]
    CallLeg: NotRequired[CallLegTypeType]

class StartVoiceToneAnalysisTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    TransactionId: str
    LanguageCode: Literal["en-US"]
    ClientRequestToken: NotRequired[str]

class StopSpeakerSearchTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    SpeakerSearchTaskId: str

class StopVoiceToneAnalysisTaskRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    VoiceToneAnalysisTaskId: str

class StreamingNotificationTargetTypeDef(TypedDict):
    NotificationTarget: NotRequired[NotificationTargetType]

class TerminationTypeDef(TypedDict):
    CpsLimit: NotRequired[int]
    DefaultPhoneNumber: NotRequired[str]
    CallingRegions: NotRequired[Sequence[str]]
    CidrAllowedList: NotRequired[Sequence[str]]
    Disabled: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdatePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str
    ProductType: NotRequired[PhoneNumberProductTypeType]
    CallingName: NotRequired[str]
    Name: NotRequired[str]

class UpdatePhoneNumberSettingsRequestTypeDef(TypedDict):
    CallingName: str

class UpdateProxySessionRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: NotRequired[int]

class UpdateSipMediaApplicationCallRequestTypeDef(TypedDict):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]

class UpdateVoiceConnectorRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool

class UpdateVoiceProfileDomainRequestTypeDef(TypedDict):
    VoiceProfileDomainId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateVoiceProfileRequestTypeDef(TypedDict):
    VoiceProfileId: str
    SpeakerSearchTaskId: str

class ValidateE911AddressRequestTypeDef(TypedDict):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str

class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(TypedDict):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(TypedDict):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableVoiceConnectorRegionsResponseTypeDef(TypedDict):
    VoiceConnectorRegions: List[VoiceConnectorAwsRegionType]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorTerminationCredentialsResponseTypeDef(TypedDict):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(TypedDict):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchUpdatePhoneNumberRequestTypeDef(TypedDict):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class VoiceToneAnalysisTaskTypeDef(TypedDict):
    VoiceToneAnalysisTaskId: NotRequired[str]
    VoiceToneAnalysisTaskStatus: NotRequired[str]
    CallDetails: NotRequired[CallDetailsTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    StartedTimestamp: NotRequired[datetime]
    StatusMessage: NotRequired[str]

class ValidateE911AddressResponseTypeDef(TypedDict):
    ValidationResult: int
    AddressExternalId: str
    Address: AddressTypeDef
    CandidateAddressList: List[CandidateAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProxySessionRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: NotRequired[str]
    ExpiryMinutes: NotRequired[int]
    NumberSelectionBehavior: NotRequired[NumberSelectionBehaviorType]
    GeoMatchLevel: NotRequired[GeoMatchLevelType]
    GeoMatchParams: NotRequired[GeoMatchParamsTypeDef]

class CreateSipMediaApplicationCallResponseTypeDef(TypedDict):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationCallResponseTypeDef(TypedDict):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SipMediaApplicationTypeDef(TypedDict):
    SipMediaApplicationId: NotRequired[str]
    AwsRegion: NotRequired[str]
    Name: NotRequired[str]
    Endpoints: NotRequired[List[SipMediaApplicationEndpointTypeDef]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    SipMediaApplicationArn: NotRequired[str]

class UpdateSipMediaApplicationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str
    Name: NotRequired[str]
    Endpoints: NotRequired[Sequence[SipMediaApplicationEndpointTypeDef]]

class CreateSipMediaApplicationRequestTypeDef(TypedDict):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpointTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateVoiceConnectorRequestTypeDef(TypedDict):
    Name: str
    RequireEncryption: bool
    AwsRegion: NotRequired[VoiceConnectorAwsRegionType]
    Tags: NotRequired[Sequence[TagTypeDef]]
    IntegrationType: NotRequired[VoiceConnectorIntegrationTypeType]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSipRuleRequestTypeDef(TypedDict):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    Disabled: NotRequired[bool]
    TargetApplications: NotRequired[Sequence[SipRuleTargetApplicationTypeDef]]

class SipRuleTypeDef(TypedDict):
    SipRuleId: NotRequired[str]
    Name: NotRequired[str]
    Disabled: NotRequired[bool]
    TriggerType: NotRequired[SipRuleTriggerTypeType]
    TriggerValue: NotRequired[str]
    TargetApplications: NotRequired[List[SipRuleTargetApplicationTypeDef]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class UpdateSipRuleRequestTypeDef(TypedDict):
    SipRuleId: str
    Name: str
    Disabled: NotRequired[bool]
    TargetApplications: NotRequired[Sequence[SipRuleTargetApplicationTypeDef]]

class CreateVoiceConnectorGroupRequestTypeDef(TypedDict):
    Name: str
    VoiceConnectorItems: NotRequired[Sequence[VoiceConnectorItemTypeDef]]

class UpdateVoiceConnectorGroupRequestTypeDef(TypedDict):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItemTypeDef]

class VoiceConnectorGroupTypeDef(TypedDict):
    VoiceConnectorGroupId: NotRequired[str]
    Name: NotRequired[str]
    VoiceConnectorItems: NotRequired[List[VoiceConnectorItemTypeDef]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    VoiceConnectorGroupArn: NotRequired[str]

class CreateVoiceConnectorResponseTypeDef(TypedDict):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorResponseTypeDef(TypedDict):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorsResponseTypeDef(TypedDict):
    VoiceConnectors: List[VoiceConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateVoiceConnectorResponseTypeDef(TypedDict):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainRequestTypeDef(TypedDict):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class VoiceProfileDomainTypeDef(TypedDict):
    VoiceProfileDomainId: NotRequired[str]
    VoiceProfileDomainArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    ServerSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class CreateVoiceProfileResponseTypeDef(TypedDict):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileResponseTypeDef(TypedDict):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileResponseTypeDef(TypedDict):
    VoiceProfile: VoiceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationCredentialsRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Credentials: NotRequired[Sequence[CredentialTypeDef]]

class EmergencyCallingConfigurationOutputTypeDef(TypedDict):
    DNIS: NotRequired[List[DNISEmergencyCallingConfigurationTypeDef]]

class EmergencyCallingConfigurationTypeDef(TypedDict):
    DNIS: NotRequired[Sequence[DNISEmergencyCallingConfigurationTypeDef]]

class GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef(TypedDict):
    ExternalSystemsConfiguration: ExternalSystemsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef(TypedDict):
    ExternalSystemsConfiguration: ExternalSystemsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsResponseTypeDef(TypedDict):
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestTypeDef(TypedDict):
    VoiceConnector: NotRequired[VoiceConnectorSettingsTypeDef]

class GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(TypedDict):
    SipMediaApplicationAlexaSkillConfiguration: (
        SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    )
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef(TypedDict):
    SipMediaApplicationAlexaSkillConfiguration: (
        SipMediaApplicationAlexaSkillConfigurationOutputTypeDef
    )
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(TypedDict):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationLoggingConfigurationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: NotRequired[
        SipMediaApplicationLoggingConfigurationTypeDef
    ]

class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(TypedDict):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorLoggingConfigurationResponseTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorLoggingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutVoiceConnectorLoggingConfigurationResponseTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorProxyResponseTypeDef(TypedDict):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorProxyResponseTypeDef(TypedDict):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationHealthResponseTypeDef(TypedDict):
    TerminationHealth: TerminationHealthTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationResponseTypeDef(TypedDict):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationResponseTypeDef(TypedDict):
    Termination: TerminationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSipRulesRequestPaginateTypeDef(TypedDict):
    SipMediaApplicationId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSupportedPhoneNumberCountriesResponseTypeDef(TypedDict):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceProfileDomainsResponseTypeDef(TypedDict):
    VoiceProfileDomains: List[VoiceProfileDomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListVoiceProfilesResponseTypeDef(TypedDict):
    VoiceProfiles: List[VoiceProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PhoneNumberOrderTypeDef(TypedDict):
    PhoneNumberOrderId: NotRequired[str]
    ProductType: NotRequired[PhoneNumberProductTypeType]
    Status: NotRequired[PhoneNumberOrderStatusType]
    OrderType: NotRequired[PhoneNumberOrderTypeType]
    OrderedPhoneNumbers: NotRequired[List[OrderedPhoneNumberTypeDef]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    FocDate: NotRequired[datetime]

class OriginationOutputTypeDef(TypedDict):
    Routes: NotRequired[List[OriginationRouteTypeDef]]
    Disabled: NotRequired[bool]

class OriginationTypeDef(TypedDict):
    Routes: NotRequired[Sequence[OriginationRouteTypeDef]]
    Disabled: NotRequired[bool]

class ProxySessionTypeDef(TypedDict):
    VoiceConnectorId: NotRequired[str]
    ProxySessionId: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[ProxySessionStatusType]
    ExpiryMinutes: NotRequired[int]
    Capabilities: NotRequired[List[CapabilityType]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    EndedTimestamp: NotRequired[datetime]
    Participants: NotRequired[List[ParticipantTypeDef]]
    NumberSelectionBehavior: NotRequired[NumberSelectionBehaviorType]
    GeoMatchLevel: NotRequired[GeoMatchLevelType]
    GeoMatchParams: NotRequired[GeoMatchParamsTypeDef]

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "E164PhoneNumber": NotRequired[str],
        "Country": NotRequired[str],
        "Type": NotRequired[PhoneNumberTypeType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberStatusType],
        "Capabilities": NotRequired[PhoneNumberCapabilitiesTypeDef],
        "Associations": NotRequired[List[PhoneNumberAssociationTypeDef]],
        "CallingName": NotRequired[str],
        "CallingNameStatus": NotRequired[CallingNameStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "DeletionTimestamp": NotRequired[datetime],
        "OrderId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
SipMediaApplicationAlexaSkillConfigurationUnionTypeDef = Union[
    SipMediaApplicationAlexaSkillConfigurationTypeDef,
    SipMediaApplicationAlexaSkillConfigurationOutputTypeDef,
]

class SpeakerSearchDetailsTypeDef(TypedDict):
    Results: NotRequired[List[SpeakerSearchResultTypeDef]]
    VoiceprintGenerationStatus: NotRequired[str]

class StreamingConfigurationOutputTypeDef(TypedDict):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: NotRequired[List[StreamingNotificationTargetTypeDef]]
    MediaInsightsConfiguration: NotRequired[MediaInsightsConfigurationTypeDef]

class StreamingConfigurationTypeDef(TypedDict):
    DataRetentionInHours: int
    Disabled: bool
    StreamingNotificationTargets: NotRequired[Sequence[StreamingNotificationTargetTypeDef]]
    MediaInsightsConfiguration: NotRequired[MediaInsightsConfigurationTypeDef]

TerminationUnionTypeDef = Union[TerminationTypeDef, TerminationOutputTypeDef]

class GetVoiceToneAnalysisTaskResponseTypeDef(TypedDict):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartVoiceToneAnalysisTaskResponseTypeDef(TypedDict):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationResponseTypeDef(TypedDict):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationResponseTypeDef(TypedDict):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsResponseTypeDef(TypedDict):
    SipMediaApplications: List[SipMediaApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSipMediaApplicationResponseTypeDef(TypedDict):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipRuleResponseTypeDef(TypedDict):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipRuleResponseTypeDef(TypedDict):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipRulesResponseTypeDef(TypedDict):
    SipRules: List[SipRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSipRuleResponseTypeDef(TypedDict):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceConnectorGroupResponseTypeDef(TypedDict):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorGroupResponseTypeDef(TypedDict):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorGroupsResponseTypeDef(TypedDict):
    VoiceConnectorGroups: List[VoiceConnectorGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateVoiceConnectorGroupResponseTypeDef(TypedDict):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceProfileDomainResponseTypeDef(TypedDict):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceProfileDomainResponseTypeDef(TypedDict):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceProfileDomainResponseTypeDef(TypedDict):
    VoiceProfileDomain: VoiceProfileDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(TypedDict):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(TypedDict):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EmergencyCallingConfigurationUnionTypeDef = Union[
    EmergencyCallingConfigurationTypeDef, EmergencyCallingConfigurationOutputTypeDef
]

class CreatePhoneNumberOrderResponseTypeDef(TypedDict):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(TypedDict):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(TypedDict):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetVoiceConnectorOriginationResponseTypeDef(TypedDict):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationResponseTypeDef(TypedDict):
    Origination: OriginationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OriginationUnionTypeDef = Union[OriginationTypeDef, OriginationOutputTypeDef]

class CreateProxySessionResponseTypeDef(TypedDict):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProxySessionResponseTypeDef(TypedDict):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProxySessionsResponseTypeDef(TypedDict):
    ProxySessions: List[ProxySessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateProxySessionResponseTypeDef(TypedDict):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(TypedDict):
    PhoneNumbers: List[PhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RestorePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef(TypedDict):
    SipMediaApplicationId: str
    SipMediaApplicationAlexaSkillConfiguration: NotRequired[
        SipMediaApplicationAlexaSkillConfigurationUnionTypeDef
    ]

class SpeakerSearchTaskTypeDef(TypedDict):
    SpeakerSearchTaskId: NotRequired[str]
    SpeakerSearchTaskStatus: NotRequired[str]
    CallDetails: NotRequired[CallDetailsTypeDef]
    SpeakerSearchDetails: NotRequired[SpeakerSearchDetailsTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]
    StartedTimestamp: NotRequired[datetime]
    StatusMessage: NotRequired[str]

class GetVoiceConnectorStreamingConfigurationResponseTypeDef(TypedDict):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationResponseTypeDef(TypedDict):
    StreamingConfiguration: StreamingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

StreamingConfigurationUnionTypeDef = Union[
    StreamingConfigurationTypeDef, StreamingConfigurationOutputTypeDef
]

class PutVoiceConnectorTerminationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Termination: TerminationUnionTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationUnionTypeDef

class PutVoiceConnectorOriginationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    Origination: OriginationUnionTypeDef

class GetSpeakerSearchTaskResponseTypeDef(TypedDict):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerSearchTaskResponseTypeDef(TypedDict):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationRequestTypeDef(TypedDict):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationUnionTypeDef
