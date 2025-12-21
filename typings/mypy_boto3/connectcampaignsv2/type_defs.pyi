"""
Type annotations for connectcampaignsv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaignsv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_connectcampaignsv2.type_defs import AnswerMachineDetectionConfigTypeDef

    data: AnswerMachineDetectionConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    CampaignDeletionPolicyType,
    CampaignStateType,
    ChannelSubtypeType,
    CommunicationTimeConfigTypeType,
    DayOfWeekType,
    EventTypeType,
    ExternalCampaignTypeType,
    FailureCodeType,
    GetCampaignStateBatchFailureCodeType,
    InstanceLimitsHandlingType,
    InstanceOnboardingJobFailureCodeType,
    InstanceOnboardingJobStatusCodeType,
    LocalTimeZoneDetectionTypeType,
    ProfileOutboundRequestFailureCodeType,
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
    "AnswerMachineDetectionConfigTypeDef",
    "CampaignFiltersTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "ChannelSubtypeConfigOutputTypeDef",
    "ChannelSubtypeConfigTypeDef",
    "ChannelSubtypeConfigUnionTypeDef",
    "ChannelSubtypeParametersTypeDef",
    "CommunicationLimitTypeDef",
    "CommunicationLimitsConfigOutputTypeDef",
    "CommunicationLimitsConfigTypeDef",
    "CommunicationLimitsConfigUnionTypeDef",
    "CommunicationLimitsOutputTypeDef",
    "CommunicationLimitsTypeDef",
    "CommunicationTimeConfigOutputTypeDef",
    "CommunicationTimeConfigTypeDef",
    "CommunicationTimeConfigUnionTypeDef",
    "CreateCampaignRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CustomerProfilesIntegrationConfigTypeDef",
    "CustomerProfilesIntegrationIdentifierTypeDef",
    "CustomerProfilesIntegrationSummaryTypeDef",
    "DeleteCampaignChannelSubtypeConfigRequestTypeDef",
    "DeleteCampaignCommunicationLimitsRequestTypeDef",
    "DeleteCampaignCommunicationTimeRequestTypeDef",
    "DeleteCampaignRequestTypeDef",
    "DeleteConnectInstanceConfigRequestTypeDef",
    "DeleteConnectInstanceIntegrationRequestTypeDef",
    "DeleteInstanceOnboardingJobRequestTypeDef",
    "DescribeCampaignRequestTypeDef",
    "DescribeCampaignResponseTypeDef",
    "EmailChannelSubtypeConfigOutputTypeDef",
    "EmailChannelSubtypeConfigTypeDef",
    "EmailChannelSubtypeParametersTypeDef",
    "EmailOutboundConfigTypeDef",
    "EmailOutboundModeOutputTypeDef",
    "EmailOutboundModeTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigTypeDef",
    "EventTriggerTypeDef",
    "FailedCampaignStateResponseTypeDef",
    "FailedProfileOutboundRequestTypeDef",
    "FailedRequestTypeDef",
    "GetCampaignStateBatchRequestTypeDef",
    "GetCampaignStateBatchResponseTypeDef",
    "GetCampaignStateRequestTypeDef",
    "GetCampaignStateResponseTypeDef",
    "GetConnectInstanceConfigRequestTypeDef",
    "GetConnectInstanceConfigResponseTypeDef",
    "GetInstanceCommunicationLimitsRequestTypeDef",
    "GetInstanceCommunicationLimitsResponseTypeDef",
    "GetInstanceOnboardingJobStatusRequestTypeDef",
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    "InstanceCommunicationLimitsConfigOutputTypeDef",
    "InstanceCommunicationLimitsConfigTypeDef",
    "InstanceCommunicationLimitsConfigUnionTypeDef",
    "InstanceConfigTypeDef",
    "InstanceIdFilterTypeDef",
    "InstanceOnboardingJobStatusTypeDef",
    "IntegrationConfigTypeDef",
    "IntegrationIdentifierTypeDef",
    "IntegrationSummaryTypeDef",
    "LambdaIntegrationConfigTypeDef",
    "LambdaIntegrationIdentifierTypeDef",
    "LambdaIntegrationSummaryTypeDef",
    "ListCampaignsRequestPaginateTypeDef",
    "ListCampaignsRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListConnectInstanceIntegrationsRequestPaginateTypeDef",
    "ListConnectInstanceIntegrationsRequestTypeDef",
    "ListConnectInstanceIntegrationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalTimeZoneConfigOutputTypeDef",
    "LocalTimeZoneConfigTypeDef",
    "OpenHoursOutputTypeDef",
    "OpenHoursTypeDef",
    "OutboundRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PauseCampaignRequestTypeDef",
    "PredictiveConfigTypeDef",
    "PreviewConfigOutputTypeDef",
    "PreviewConfigTypeDef",
    "ProfileOutboundRequestTypeDef",
    "ProgressiveConfigTypeDef",
    "PutConnectInstanceIntegrationRequestTypeDef",
    "PutInstanceCommunicationLimitsRequestTypeDef",
    "PutOutboundRequestBatchRequestTypeDef",
    "PutOutboundRequestBatchResponseTypeDef",
    "PutProfileOutboundRequestBatchRequestTypeDef",
    "PutProfileOutboundRequestBatchResponseTypeDef",
    "QConnectIntegrationConfigTypeDef",
    "QConnectIntegrationIdentifierTypeDef",
    "QConnectIntegrationSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RestrictedPeriodTypeDef",
    "RestrictedPeriodsOutputTypeDef",
    "RestrictedPeriodsTypeDef",
    "ResumeCampaignRequestTypeDef",
    "ScheduleOutputTypeDef",
    "ScheduleTypeDef",
    "ScheduleUnionTypeDef",
    "SmsChannelSubtypeConfigOutputTypeDef",
    "SmsChannelSubtypeConfigTypeDef",
    "SmsChannelSubtypeParametersTypeDef",
    "SmsOutboundConfigTypeDef",
    "SmsOutboundModeOutputTypeDef",
    "SmsOutboundModeTypeDef",
    "SourceTypeDef",
    "StartCampaignRequestTypeDef",
    "StartInstanceOnboardingJobRequestTypeDef",
    "StartInstanceOnboardingJobResponseTypeDef",
    "StopCampaignRequestTypeDef",
    "SuccessfulCampaignStateResponseTypeDef",
    "SuccessfulProfileOutboundRequestTypeDef",
    "SuccessfulRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TelephonyChannelSubtypeConfigOutputTypeDef",
    "TelephonyChannelSubtypeConfigTypeDef",
    "TelephonyChannelSubtypeParametersTypeDef",
    "TelephonyOutboundConfigTypeDef",
    "TelephonyOutboundModeOutputTypeDef",
    "TelephonyOutboundModeTypeDef",
    "TimeRangeTypeDef",
    "TimeWindowOutputTypeDef",
    "TimeWindowTypeDef",
    "TimeoutConfigTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCampaignChannelSubtypeConfigRequestTypeDef",
    "UpdateCampaignCommunicationLimitsRequestTypeDef",
    "UpdateCampaignCommunicationTimeRequestTypeDef",
    "UpdateCampaignFlowAssociationRequestTypeDef",
    "UpdateCampaignNameRequestTypeDef",
    "UpdateCampaignScheduleRequestTypeDef",
    "UpdateCampaignSourceRequestTypeDef",
    "WhatsAppChannelSubtypeConfigOutputTypeDef",
    "WhatsAppChannelSubtypeConfigTypeDef",
    "WhatsAppChannelSubtypeParametersTypeDef",
    "WhatsAppOutboundConfigTypeDef",
    "WhatsAppOutboundModeOutputTypeDef",
    "WhatsAppOutboundModeTypeDef",
)

class AnswerMachineDetectionConfigTypeDef(TypedDict):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: NotRequired[bool]

InstanceIdFilterTypeDef = TypedDict(
    "InstanceIdFilterTypeDef",
    {
        "value": str,
        "operator": Literal["Eq"],
    },
)

class ScheduleOutputTypeDef(TypedDict):
    startTime: datetime
    endTime: datetime
    refreshFrequency: NotRequired[str]

class EmailChannelSubtypeParametersTypeDef(TypedDict):
    destinationEmailAddress: str
    templateParameters: Mapping[str, str]
    connectSourceEmailAddress: NotRequired[str]
    templateArn: NotRequired[str]

class SmsChannelSubtypeParametersTypeDef(TypedDict):
    destinationPhoneNumber: str
    templateParameters: Mapping[str, str]
    connectSourcePhoneNumberArn: NotRequired[str]
    templateArn: NotRequired[str]

class WhatsAppChannelSubtypeParametersTypeDef(TypedDict):
    destinationPhoneNumber: str
    templateParameters: Mapping[str, str]
    connectSourcePhoneNumberArn: NotRequired[str]
    templateArn: NotRequired[str]

class CommunicationLimitTypeDef(TypedDict):
    maxCountPerRecipient: int
    frequency: int
    unit: Literal["DAY"]

class LocalTimeZoneConfigOutputTypeDef(TypedDict):
    defaultTimeZone: NotRequired[str]
    localTimeZoneDetection: NotRequired[List[LocalTimeZoneDetectionTypeType]]

class LocalTimeZoneConfigTypeDef(TypedDict):
    defaultTimeZone: NotRequired[str]
    localTimeZoneDetection: NotRequired[Sequence[LocalTimeZoneDetectionTypeType]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CustomerProfilesIntegrationConfigTypeDef(TypedDict):
    domainArn: str
    objectTypeNames: Mapping[EventTypeType, str]

class CustomerProfilesIntegrationIdentifierTypeDef(TypedDict):
    domainArn: str

class CustomerProfilesIntegrationSummaryTypeDef(TypedDict):
    domainArn: str
    objectTypeNames: Dict[EventTypeType, str]

DeleteCampaignChannelSubtypeConfigRequestTypeDef = TypedDict(
    "DeleteCampaignChannelSubtypeConfigRequestTypeDef",
    {
        "id": str,
        "channelSubtype": ChannelSubtypeType,
    },
)
DeleteCampaignCommunicationLimitsRequestTypeDef = TypedDict(
    "DeleteCampaignCommunicationLimitsRequestTypeDef",
    {
        "id": str,
        "config": Literal["ALL_CHANNEL_SUBTYPES"],
    },
)
DeleteCampaignCommunicationTimeRequestTypeDef = TypedDict(
    "DeleteCampaignCommunicationTimeRequestTypeDef",
    {
        "id": str,
        "config": CommunicationTimeConfigTypeType,
    },
)
DeleteCampaignRequestTypeDef = TypedDict(
    "DeleteCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteConnectInstanceConfigRequestTypeDef(TypedDict):
    connectInstanceId: str
    campaignDeletionPolicy: NotRequired[CampaignDeletionPolicyType]

class DeleteInstanceOnboardingJobRequestTypeDef(TypedDict):
    connectInstanceId: str

DescribeCampaignRequestTypeDef = TypedDict(
    "DescribeCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class EmailOutboundConfigTypeDef(TypedDict):
    connectSourceEmailAddress: str
    wisdomTemplateArn: str
    sourceEmailAddressDisplayName: NotRequired[str]

class EmailOutboundModeOutputTypeDef(TypedDict):
    agentless: NotRequired[Dict[str, Any]]

class EmailOutboundModeTypeDef(TypedDict):
    agentless: NotRequired[Mapping[str, Any]]

class EncryptionConfigTypeDef(TypedDict):
    enabled: bool
    encryptionType: NotRequired[Literal["KMS"]]
    keyArn: NotRequired[str]

class EventTriggerTypeDef(TypedDict):
    customerProfilesDomainArn: NotRequired[str]

class FailedCampaignStateResponseTypeDef(TypedDict):
    campaignId: NotRequired[str]
    failureCode: NotRequired[GetCampaignStateBatchFailureCodeType]

FailedProfileOutboundRequestTypeDef = TypedDict(
    "FailedProfileOutboundRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
        "failureCode": NotRequired[ProfileOutboundRequestFailureCodeType],
    },
)
FailedRequestTypeDef = TypedDict(
    "FailedRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
        "failureCode": NotRequired[FailureCodeType],
    },
)

class GetCampaignStateBatchRequestTypeDef(TypedDict):
    campaignIds: Sequence[str]

class SuccessfulCampaignStateResponseTypeDef(TypedDict):
    campaignId: NotRequired[str]
    state: NotRequired[CampaignStateType]

GetCampaignStateRequestTypeDef = TypedDict(
    "GetCampaignStateRequestTypeDef",
    {
        "id": str,
    },
)

class GetConnectInstanceConfigRequestTypeDef(TypedDict):
    connectInstanceId: str

class GetInstanceCommunicationLimitsRequestTypeDef(TypedDict):
    connectInstanceId: str

class GetInstanceOnboardingJobStatusRequestTypeDef(TypedDict):
    connectInstanceId: str

class InstanceOnboardingJobStatusTypeDef(TypedDict):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: NotRequired[InstanceOnboardingJobFailureCodeType]

class LambdaIntegrationConfigTypeDef(TypedDict):
    functionArn: str

class QConnectIntegrationConfigTypeDef(TypedDict):
    knowledgeBaseArn: str

class LambdaIntegrationIdentifierTypeDef(TypedDict):
    functionArn: str

class QConnectIntegrationIdentifierTypeDef(TypedDict):
    knowledgeBaseArn: str

class LambdaIntegrationSummaryTypeDef(TypedDict):
    functionArn: str

class QConnectIntegrationSummaryTypeDef(TypedDict):
    knowledgeBaseArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConnectInstanceIntegrationsRequestTypeDef(TypedDict):
    connectInstanceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    arn: str

class TimeRangeTypeDef(TypedDict):
    startTime: str
    endTime: str

TimestampTypeDef = Union[datetime, str]
PauseCampaignRequestTypeDef = TypedDict(
    "PauseCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class PredictiveConfigTypeDef(TypedDict):
    bandwidthAllocation: float

class TimeoutConfigTypeDef(TypedDict):
    durationInSeconds: int

class ProgressiveConfigTypeDef(TypedDict):
    bandwidthAllocation: float

SuccessfulRequestTypeDef = TypedDict(
    "SuccessfulRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
    },
)
SuccessfulProfileOutboundRequestTypeDef = TypedDict(
    "SuccessfulProfileOutboundRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
    },
)

class RestrictedPeriodTypeDef(TypedDict):
    startDate: str
    endDate: str
    name: NotRequired[str]

ResumeCampaignRequestTypeDef = TypedDict(
    "ResumeCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class SmsOutboundConfigTypeDef(TypedDict):
    connectSourcePhoneNumberArn: str
    wisdomTemplateArn: str

class SmsOutboundModeOutputTypeDef(TypedDict):
    agentless: NotRequired[Dict[str, Any]]

class SmsOutboundModeTypeDef(TypedDict):
    agentless: NotRequired[Mapping[str, Any]]

StartCampaignRequestTypeDef = TypedDict(
    "StartCampaignRequestTypeDef",
    {
        "id": str,
    },
)
StopCampaignRequestTypeDef = TypedDict(
    "StopCampaignRequestTypeDef",
    {
        "id": str,
    },
)

class TagResourceRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    arn: str
    tagKeys: Sequence[str]

UpdateCampaignFlowAssociationRequestTypeDef = TypedDict(
    "UpdateCampaignFlowAssociationRequestTypeDef",
    {
        "id": str,
        "connectCampaignFlowArn": str,
    },
)
UpdateCampaignNameRequestTypeDef = TypedDict(
    "UpdateCampaignNameRequestTypeDef",
    {
        "id": str,
        "name": str,
    },
)

class WhatsAppOutboundConfigTypeDef(TypedDict):
    connectSourcePhoneNumberArn: str
    wisdomTemplateArn: str

class WhatsAppOutboundModeOutputTypeDef(TypedDict):
    agentless: NotRequired[Dict[str, Any]]

class WhatsAppOutboundModeTypeDef(TypedDict):
    agentless: NotRequired[Mapping[str, Any]]

class TelephonyChannelSubtypeParametersTypeDef(TypedDict):
    destinationPhoneNumber: str
    attributes: Mapping[str, str]
    connectSourcePhoneNumber: NotRequired[str]
    answerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]
    ringTimeout: NotRequired[int]

class TelephonyOutboundConfigTypeDef(TypedDict):
    connectContactFlowId: str
    connectSourcePhoneNumber: NotRequired[str]
    answerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]
    ringTimeout: NotRequired[int]

class CampaignFiltersTypeDef(TypedDict):
    instanceIdFilter: NotRequired[InstanceIdFilterTypeDef]

CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "channelSubtypes": List[ChannelSubtypeType],
        "type": NotRequired[ExternalCampaignTypeType],
        "schedule": NotRequired[ScheduleOutputTypeDef],
        "connectCampaignFlowArn": NotRequired[str],
    },
)

class CommunicationLimitsOutputTypeDef(TypedDict):
    communicationLimitsList: NotRequired[List[CommunicationLimitTypeDef]]

class CommunicationLimitsTypeDef(TypedDict):
    communicationLimitsList: NotRequired[Sequence[CommunicationLimitTypeDef]]

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignStateResponseTypeDef(TypedDict):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmailChannelSubtypeConfigOutputTypeDef(TypedDict):
    outboundMode: EmailOutboundModeOutputTypeDef
    defaultOutboundConfig: EmailOutboundConfigTypeDef
    capacity: NotRequired[float]

class EmailChannelSubtypeConfigTypeDef(TypedDict):
    outboundMode: EmailOutboundModeTypeDef
    defaultOutboundConfig: EmailOutboundConfigTypeDef
    capacity: NotRequired[float]

class InstanceConfigTypeDef(TypedDict):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef

class StartInstanceOnboardingJobRequestTypeDef(TypedDict):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef

class SourceTypeDef(TypedDict):
    customerProfilesSegmentArn: NotRequired[str]
    eventTrigger: NotRequired[EventTriggerTypeDef]

class GetCampaignStateBatchResponseTypeDef(TypedDict):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceOnboardingJobStatusResponseTypeDef(TypedDict):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceOnboardingJobResponseTypeDef(TypedDict):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

IntegrationConfigTypeDef = TypedDict(
    "IntegrationConfigTypeDef",
    {
        "customerProfiles": NotRequired[CustomerProfilesIntegrationConfigTypeDef],
        "qConnect": NotRequired[QConnectIntegrationConfigTypeDef],
        "lambda": NotRequired[LambdaIntegrationConfigTypeDef],
    },
)
IntegrationIdentifierTypeDef = TypedDict(
    "IntegrationIdentifierTypeDef",
    {
        "customerProfiles": NotRequired[CustomerProfilesIntegrationIdentifierTypeDef],
        "qConnect": NotRequired[QConnectIntegrationIdentifierTypeDef],
        "lambda": NotRequired[LambdaIntegrationIdentifierTypeDef],
    },
)
IntegrationSummaryTypeDef = TypedDict(
    "IntegrationSummaryTypeDef",
    {
        "customerProfiles": NotRequired[CustomerProfilesIntegrationSummaryTypeDef],
        "qConnect": NotRequired[QConnectIntegrationSummaryTypeDef],
        "lambda": NotRequired[LambdaIntegrationSummaryTypeDef],
    },
)

class ListConnectInstanceIntegrationsRequestPaginateTypeDef(TypedDict):
    connectInstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class OpenHoursOutputTypeDef(TypedDict):
    dailyHours: NotRequired[Dict[DayOfWeekType, List[TimeRangeTypeDef]]]

class OpenHoursTypeDef(TypedDict):
    dailyHours: NotRequired[Mapping[DayOfWeekType, Sequence[TimeRangeTypeDef]]]

class ProfileOutboundRequestTypeDef(TypedDict):
    clientToken: str
    profileId: str
    expirationTime: NotRequired[TimestampTypeDef]

class ScheduleTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    refreshFrequency: NotRequired[str]

class PreviewConfigOutputTypeDef(TypedDict):
    bandwidthAllocation: float
    timeoutConfig: TimeoutConfigTypeDef
    agentActions: NotRequired[List[Literal["DISCARD"]]]

class PreviewConfigTypeDef(TypedDict):
    bandwidthAllocation: float
    timeoutConfig: TimeoutConfigTypeDef
    agentActions: NotRequired[Sequence[Literal["DISCARD"]]]

class PutOutboundRequestBatchResponseTypeDef(TypedDict):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileOutboundRequestBatchResponseTypeDef(TypedDict):
    successfulRequests: List[SuccessfulProfileOutboundRequestTypeDef]
    failedRequests: List[FailedProfileOutboundRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestrictedPeriodsOutputTypeDef(TypedDict):
    restrictedPeriodList: NotRequired[List[RestrictedPeriodTypeDef]]

class RestrictedPeriodsTypeDef(TypedDict):
    restrictedPeriodList: NotRequired[Sequence[RestrictedPeriodTypeDef]]

class SmsChannelSubtypeConfigOutputTypeDef(TypedDict):
    outboundMode: SmsOutboundModeOutputTypeDef
    defaultOutboundConfig: SmsOutboundConfigTypeDef
    capacity: NotRequired[float]

class SmsChannelSubtypeConfigTypeDef(TypedDict):
    outboundMode: SmsOutboundModeTypeDef
    defaultOutboundConfig: SmsOutboundConfigTypeDef
    capacity: NotRequired[float]

class WhatsAppChannelSubtypeConfigOutputTypeDef(TypedDict):
    outboundMode: WhatsAppOutboundModeOutputTypeDef
    defaultOutboundConfig: WhatsAppOutboundConfigTypeDef
    capacity: NotRequired[float]

class WhatsAppChannelSubtypeConfigTypeDef(TypedDict):
    outboundMode: WhatsAppOutboundModeTypeDef
    defaultOutboundConfig: WhatsAppOutboundConfigTypeDef
    capacity: NotRequired[float]

class ChannelSubtypeParametersTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeParametersTypeDef]
    sms: NotRequired[SmsChannelSubtypeParametersTypeDef]
    email: NotRequired[EmailChannelSubtypeParametersTypeDef]
    whatsApp: NotRequired[WhatsAppChannelSubtypeParametersTypeDef]

class ListCampaignsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[CampaignFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCampaignsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[CampaignFiltersTypeDef]

class ListCampaignsResponseTypeDef(TypedDict):
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CommunicationLimitsConfigOutputTypeDef(TypedDict):
    allChannelSubtypes: NotRequired[CommunicationLimitsOutputTypeDef]
    instanceLimitsHandling: NotRequired[InstanceLimitsHandlingType]

class InstanceCommunicationLimitsConfigOutputTypeDef(TypedDict):
    allChannelSubtypes: NotRequired[CommunicationLimitsOutputTypeDef]

class CommunicationLimitsConfigTypeDef(TypedDict):
    allChannelSubtypes: NotRequired[CommunicationLimitsTypeDef]
    instanceLimitsHandling: NotRequired[InstanceLimitsHandlingType]

class InstanceCommunicationLimitsConfigTypeDef(TypedDict):
    allChannelSubtypes: NotRequired[CommunicationLimitsTypeDef]

class GetConnectInstanceConfigResponseTypeDef(TypedDict):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

UpdateCampaignSourceRequestTypeDef = TypedDict(
    "UpdateCampaignSourceRequestTypeDef",
    {
        "id": str,
        "source": SourceTypeDef,
    },
)

class PutConnectInstanceIntegrationRequestTypeDef(TypedDict):
    connectInstanceId: str
    integrationConfig: IntegrationConfigTypeDef

class DeleteConnectInstanceIntegrationRequestTypeDef(TypedDict):
    connectInstanceId: str
    integrationIdentifier: IntegrationIdentifierTypeDef

class ListConnectInstanceIntegrationsResponseTypeDef(TypedDict):
    integrationSummaryList: List[IntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

PutProfileOutboundRequestBatchRequestTypeDef = TypedDict(
    "PutProfileOutboundRequestBatchRequestTypeDef",
    {
        "id": str,
        "profileOutboundRequests": Sequence[ProfileOutboundRequestTypeDef],
    },
)
ScheduleUnionTypeDef = Union[ScheduleTypeDef, ScheduleOutputTypeDef]

class TelephonyOutboundModeOutputTypeDef(TypedDict):
    progressive: NotRequired[ProgressiveConfigTypeDef]
    predictive: NotRequired[PredictiveConfigTypeDef]
    agentless: NotRequired[Dict[str, Any]]
    preview: NotRequired[PreviewConfigOutputTypeDef]

class TelephonyOutboundModeTypeDef(TypedDict):
    progressive: NotRequired[ProgressiveConfigTypeDef]
    predictive: NotRequired[PredictiveConfigTypeDef]
    agentless: NotRequired[Mapping[str, Any]]
    preview: NotRequired[PreviewConfigTypeDef]

class TimeWindowOutputTypeDef(TypedDict):
    openHours: OpenHoursOutputTypeDef
    restrictedPeriods: NotRequired[RestrictedPeriodsOutputTypeDef]

class TimeWindowTypeDef(TypedDict):
    openHours: OpenHoursTypeDef
    restrictedPeriods: NotRequired[RestrictedPeriodsTypeDef]

class OutboundRequestTypeDef(TypedDict):
    clientToken: str
    expirationTime: TimestampTypeDef
    channelSubtypeParameters: ChannelSubtypeParametersTypeDef

class GetInstanceCommunicationLimitsResponseTypeDef(TypedDict):
    communicationLimitsConfig: InstanceCommunicationLimitsConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CommunicationLimitsConfigUnionTypeDef = Union[
    CommunicationLimitsConfigTypeDef, CommunicationLimitsConfigOutputTypeDef
]
InstanceCommunicationLimitsConfigUnionTypeDef = Union[
    InstanceCommunicationLimitsConfigTypeDef, InstanceCommunicationLimitsConfigOutputTypeDef
]
UpdateCampaignScheduleRequestTypeDef = TypedDict(
    "UpdateCampaignScheduleRequestTypeDef",
    {
        "id": str,
        "schedule": ScheduleUnionTypeDef,
    },
)

class TelephonyChannelSubtypeConfigOutputTypeDef(TypedDict):
    outboundMode: TelephonyOutboundModeOutputTypeDef
    defaultOutboundConfig: TelephonyOutboundConfigTypeDef
    capacity: NotRequired[float]
    connectQueueId: NotRequired[str]

class TelephonyChannelSubtypeConfigTypeDef(TypedDict):
    outboundMode: TelephonyOutboundModeTypeDef
    defaultOutboundConfig: TelephonyOutboundConfigTypeDef
    capacity: NotRequired[float]
    connectQueueId: NotRequired[str]

class CommunicationTimeConfigOutputTypeDef(TypedDict):
    localTimeZoneConfig: LocalTimeZoneConfigOutputTypeDef
    telephony: NotRequired[TimeWindowOutputTypeDef]
    sms: NotRequired[TimeWindowOutputTypeDef]
    email: NotRequired[TimeWindowOutputTypeDef]
    whatsApp: NotRequired[TimeWindowOutputTypeDef]

class CommunicationTimeConfigTypeDef(TypedDict):
    localTimeZoneConfig: LocalTimeZoneConfigTypeDef
    telephony: NotRequired[TimeWindowTypeDef]
    sms: NotRequired[TimeWindowTypeDef]
    email: NotRequired[TimeWindowTypeDef]
    whatsApp: NotRequired[TimeWindowTypeDef]

PutOutboundRequestBatchRequestTypeDef = TypedDict(
    "PutOutboundRequestBatchRequestTypeDef",
    {
        "id": str,
        "outboundRequests": Sequence[OutboundRequestTypeDef],
    },
)
UpdateCampaignCommunicationLimitsRequestTypeDef = TypedDict(
    "UpdateCampaignCommunicationLimitsRequestTypeDef",
    {
        "id": str,
        "communicationLimitsOverride": CommunicationLimitsConfigUnionTypeDef,
    },
)

class PutInstanceCommunicationLimitsRequestTypeDef(TypedDict):
    connectInstanceId: str
    communicationLimitsConfig: InstanceCommunicationLimitsConfigUnionTypeDef

class ChannelSubtypeConfigOutputTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeConfigOutputTypeDef]
    sms: NotRequired[SmsChannelSubtypeConfigOutputTypeDef]
    email: NotRequired[EmailChannelSubtypeConfigOutputTypeDef]
    whatsApp: NotRequired[WhatsAppChannelSubtypeConfigOutputTypeDef]

class ChannelSubtypeConfigTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeConfigTypeDef]
    sms: NotRequired[SmsChannelSubtypeConfigTypeDef]
    email: NotRequired[EmailChannelSubtypeConfigTypeDef]
    whatsApp: NotRequired[WhatsAppChannelSubtypeConfigTypeDef]

CommunicationTimeConfigUnionTypeDef = Union[
    CommunicationTimeConfigTypeDef, CommunicationTimeConfigOutputTypeDef
]
CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "channelSubtypeConfig": NotRequired[ChannelSubtypeConfigOutputTypeDef],
        "type": NotRequired[ExternalCampaignTypeType],
        "source": NotRequired[SourceTypeDef],
        "connectCampaignFlowArn": NotRequired[str],
        "schedule": NotRequired[ScheduleOutputTypeDef],
        "communicationTimeConfig": NotRequired[CommunicationTimeConfigOutputTypeDef],
        "communicationLimitsOverride": NotRequired[CommunicationLimitsConfigOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
ChannelSubtypeConfigUnionTypeDef = Union[
    ChannelSubtypeConfigTypeDef, ChannelSubtypeConfigOutputTypeDef
]
UpdateCampaignCommunicationTimeRequestTypeDef = TypedDict(
    "UpdateCampaignCommunicationTimeRequestTypeDef",
    {
        "id": str,
        "communicationTimeConfig": CommunicationTimeConfigUnionTypeDef,
    },
)

class DescribeCampaignResponseTypeDef(TypedDict):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateCampaignRequestTypeDef = TypedDict(
    "CreateCampaignRequestTypeDef",
    {
        "name": str,
        "connectInstanceId": str,
        "channelSubtypeConfig": NotRequired[ChannelSubtypeConfigUnionTypeDef],
        "type": NotRequired[ExternalCampaignTypeType],
        "source": NotRequired[SourceTypeDef],
        "connectCampaignFlowArn": NotRequired[str],
        "schedule": NotRequired[ScheduleUnionTypeDef],
        "communicationTimeConfig": NotRequired[CommunicationTimeConfigUnionTypeDef],
        "communicationLimitsOverride": NotRequired[CommunicationLimitsConfigUnionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateCampaignChannelSubtypeConfigRequestTypeDef = TypedDict(
    "UpdateCampaignChannelSubtypeConfigRequestTypeDef",
    {
        "id": str,
        "channelSubtypeConfig": ChannelSubtypeConfigUnionTypeDef,
    },
)
