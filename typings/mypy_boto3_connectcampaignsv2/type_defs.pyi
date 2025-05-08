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
    FailureCodeType,
    GetCampaignStateBatchFailureCodeType,
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
    "GetInstanceOnboardingJobStatusRequestTypeDef",
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    "InstanceConfigTypeDef",
    "InstanceIdFilterTypeDef",
    "InstanceOnboardingJobStatusTypeDef",
    "IntegrationConfigTypeDef",
    "IntegrationIdentifierTypeDef",
    "IntegrationSummaryTypeDef",
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
    "ProfileOutboundRequestTypeDef",
    "ProgressiveConfigTypeDef",
    "PutConnectInstanceIntegrationRequestTypeDef",
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
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCampaignChannelSubtypeConfigRequestTypeDef",
    "UpdateCampaignCommunicationLimitsRequestTypeDef",
    "UpdateCampaignCommunicationTimeRequestTypeDef",
    "UpdateCampaignFlowAssociationRequestTypeDef",
    "UpdateCampaignNameRequestTypeDef",
    "UpdateCampaignScheduleRequestTypeDef",
    "UpdateCampaignSourceRequestTypeDef",
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

class GetInstanceOnboardingJobStatusRequestTypeDef(TypedDict):
    connectInstanceId: str

class InstanceOnboardingJobStatusTypeDef(TypedDict):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: NotRequired[InstanceOnboardingJobFailureCodeType]

class QConnectIntegrationConfigTypeDef(TypedDict):
    knowledgeBaseArn: str

class QConnectIntegrationIdentifierTypeDef(TypedDict):
    knowledgeBaseArn: str

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

class TelephonyChannelSubtypeParametersTypeDef(TypedDict):
    destinationPhoneNumber: str
    attributes: Mapping[str, str]
    connectSourcePhoneNumber: NotRequired[str]
    answerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]

class TelephonyOutboundConfigTypeDef(TypedDict):
    connectContactFlowId: str
    connectSourcePhoneNumber: NotRequired[str]
    answerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]

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

class IntegrationConfigTypeDef(TypedDict):
    customerProfiles: NotRequired[CustomerProfilesIntegrationConfigTypeDef]
    qConnect: NotRequired[QConnectIntegrationConfigTypeDef]

class IntegrationIdentifierTypeDef(TypedDict):
    customerProfiles: NotRequired[CustomerProfilesIntegrationIdentifierTypeDef]
    qConnect: NotRequired[QConnectIntegrationIdentifierTypeDef]

class IntegrationSummaryTypeDef(TypedDict):
    customerProfiles: NotRequired[CustomerProfilesIntegrationSummaryTypeDef]
    qConnect: NotRequired[QConnectIntegrationSummaryTypeDef]

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

class TelephonyOutboundModeOutputTypeDef(TypedDict):
    progressive: NotRequired[ProgressiveConfigTypeDef]
    predictive: NotRequired[PredictiveConfigTypeDef]
    agentless: NotRequired[Dict[str, Any]]

class TelephonyOutboundModeTypeDef(TypedDict):
    progressive: NotRequired[ProgressiveConfigTypeDef]
    predictive: NotRequired[PredictiveConfigTypeDef]
    agentless: NotRequired[Mapping[str, Any]]

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

class ChannelSubtypeParametersTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeParametersTypeDef]
    sms: NotRequired[SmsChannelSubtypeParametersTypeDef]
    email: NotRequired[EmailChannelSubtypeParametersTypeDef]

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

class CommunicationLimitsConfigTypeDef(TypedDict):
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

CommunicationLimitsConfigUnionTypeDef = Union[
    CommunicationLimitsConfigTypeDef, CommunicationLimitsConfigOutputTypeDef
]
UpdateCampaignScheduleRequestTypeDef = TypedDict(
    "UpdateCampaignScheduleRequestTypeDef",
    {
        "id": str,
        "schedule": ScheduleUnionTypeDef,
    },
)

class ChannelSubtypeConfigOutputTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeConfigOutputTypeDef]
    sms: NotRequired[SmsChannelSubtypeConfigOutputTypeDef]
    email: NotRequired[EmailChannelSubtypeConfigOutputTypeDef]

class ChannelSubtypeConfigTypeDef(TypedDict):
    telephony: NotRequired[TelephonyChannelSubtypeConfigTypeDef]
    sms: NotRequired[SmsChannelSubtypeConfigTypeDef]
    email: NotRequired[EmailChannelSubtypeConfigTypeDef]

class CommunicationTimeConfigOutputTypeDef(TypedDict):
    localTimeZoneConfig: LocalTimeZoneConfigOutputTypeDef
    telephony: NotRequired[TimeWindowOutputTypeDef]
    sms: NotRequired[TimeWindowOutputTypeDef]
    email: NotRequired[TimeWindowOutputTypeDef]

class CommunicationTimeConfigTypeDef(TypedDict):
    localTimeZoneConfig: LocalTimeZoneConfigTypeDef
    telephony: NotRequired[TimeWindowTypeDef]
    sms: NotRequired[TimeWindowTypeDef]
    email: NotRequired[TimeWindowTypeDef]

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
ChannelSubtypeConfigUnionTypeDef = Union[
    ChannelSubtypeConfigTypeDef, ChannelSubtypeConfigOutputTypeDef
]
CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "channelSubtypeConfig": ChannelSubtypeConfigOutputTypeDef,
        "source": NotRequired[SourceTypeDef],
        "connectCampaignFlowArn": NotRequired[str],
        "schedule": NotRequired[ScheduleOutputTypeDef],
        "communicationTimeConfig": NotRequired[CommunicationTimeConfigOutputTypeDef],
        "communicationLimitsOverride": NotRequired[CommunicationLimitsConfigOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
CommunicationTimeConfigUnionTypeDef = Union[
    CommunicationTimeConfigTypeDef, CommunicationTimeConfigOutputTypeDef
]
UpdateCampaignChannelSubtypeConfigRequestTypeDef = TypedDict(
    "UpdateCampaignChannelSubtypeConfigRequestTypeDef",
    {
        "id": str,
        "channelSubtypeConfig": ChannelSubtypeConfigUnionTypeDef,
    },
)

class DescribeCampaignResponseTypeDef(TypedDict):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCampaignRequestTypeDef(TypedDict):
    name: str
    connectInstanceId: str
    channelSubtypeConfig: ChannelSubtypeConfigUnionTypeDef
    source: NotRequired[SourceTypeDef]
    connectCampaignFlowArn: NotRequired[str]
    schedule: NotRequired[ScheduleUnionTypeDef]
    communicationTimeConfig: NotRequired[CommunicationTimeConfigUnionTypeDef]
    communicationLimitsOverride: NotRequired[CommunicationLimitsConfigUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

UpdateCampaignCommunicationTimeRequestTypeDef = TypedDict(
    "UpdateCampaignCommunicationTimeRequestTypeDef",
    {
        "id": str,
        "communicationTimeConfig": CommunicationTimeConfigUnionTypeDef,
    },
)
