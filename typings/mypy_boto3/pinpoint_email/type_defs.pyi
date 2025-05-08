"""
Type annotations for pinpoint-email service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    MailFromDomainStatusType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlacklistEntryTypeDef",
    "BlobTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDestinationUnionTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateDedicatedIpPoolRequestTypeDef",
    "CreateDeliverabilityTestReportRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityRequestTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteDedicatedIpPoolRequestTypeDef",
    "DeleteEmailIdentityRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionOutputTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainDeliverabilityTrackingOptionUnionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsRequestTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetRequestTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetDedicatedIpRequestTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsRequestPaginateTypeDef",
    "GetDedicatedIpsRequestTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportRequestTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignRequestTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportRequestTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityRequestTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "IdentityInfoTypeDef",
    "InboxPlacementTrackingOptionOutputTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "InboxPlacementTrackingOptionUnionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestPaginateTypeDef",
    "ListConfigurationSetsRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsRequestPaginateTypeDef",
    "ListDedicatedIpPoolsRequestTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsRequestPaginateTypeDef",
    "ListDeliverabilityTestReportsRequestTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesRequestPaginateTypeDef",
    "ListEmailIdentitiesRequestTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PaginatorConfigTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestTypeDef",
    "PutAccountSendingAttributesRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestTypeDef",
    "PutDedicatedIpInPoolRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestTypeDef",
    "RawMessageTypeDef",
    "ReputationOptionsOutputTypeDef",
    "ReputationOptionsTypeDef",
    "ReputationOptionsUnionTypeDef",
    "ResponseMetadataTypeDef",
    "SendEmailRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TimestampTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    "VolumeStatisticsTypeDef",
)

class BlacklistEntryTypeDef(TypedDict):
    RblName: NotRequired[str]
    ListingTime: NotRequired[datetime]
    Description: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ContentTypeDef(TypedDict):
    Data: str
    Charset: NotRequired[str]

class CloudWatchDimensionConfigurationTypeDef(TypedDict):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class DeliveryOptionsTypeDef(TypedDict):
    TlsPolicy: NotRequired[TlsPolicyType]
    SendingPoolName: NotRequired[str]

class SendingOptionsTypeDef(TypedDict):
    SendingEnabled: NotRequired[bool]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class TrackingOptionsTypeDef(TypedDict):
    CustomRedirectDomain: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DkimAttributesTypeDef(TypedDict):
    SigningEnabled: NotRequired[bool]
    Status: NotRequired[DkimStatusType]
    Tokens: NotRequired[List[str]]

class DomainIspPlacementTypeDef(TypedDict):
    IspName: NotRequired[str]
    InboxRawCount: NotRequired[int]
    SpamRawCount: NotRequired[int]
    InboxPercentage: NotRequired[float]
    SpamPercentage: NotRequired[float]

class VolumeStatisticsTypeDef(TypedDict):
    InboxRawCount: NotRequired[int]
    SpamRawCount: NotRequired[int]
    ProjectedInbox: NotRequired[int]
    ProjectedSpam: NotRequired[int]

class DedicatedIpTypeDef(TypedDict):
    Ip: str
    WarmupStatus: WarmupStatusType
    WarmupPercentage: int
    PoolName: NotRequired[str]

class DeleteConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteDedicatedIpPoolRequestTypeDef(TypedDict):
    PoolName: str

class DeleteEmailIdentityRequestTypeDef(TypedDict):
    EmailIdentity: str

class DeliverabilityTestReportTypeDef(TypedDict):
    ReportId: NotRequired[str]
    ReportName: NotRequired[str]
    Subject: NotRequired[str]
    FromEmailAddress: NotRequired[str]
    CreateDate: NotRequired[datetime]
    DeliverabilityTestStatus: NotRequired[DeliverabilityTestStatusType]

class DestinationTypeDef(TypedDict):
    ToAddresses: NotRequired[Sequence[str]]
    CcAddresses: NotRequired[Sequence[str]]
    BccAddresses: NotRequired[Sequence[str]]

class DomainDeliverabilityCampaignTypeDef(TypedDict):
    CampaignId: NotRequired[str]
    ImageUrl: NotRequired[str]
    Subject: NotRequired[str]
    FromAddress: NotRequired[str]
    SendingIps: NotRequired[List[str]]
    FirstSeenDateTime: NotRequired[datetime]
    LastSeenDateTime: NotRequired[datetime]
    InboxCount: NotRequired[int]
    SpamCount: NotRequired[int]
    ReadRate: NotRequired[float]
    DeleteRate: NotRequired[float]
    ReadDeleteRate: NotRequired[float]
    ProjectedVolume: NotRequired[int]
    Esps: NotRequired[List[str]]

class InboxPlacementTrackingOptionOutputTypeDef(TypedDict):
    Global: NotRequired[bool]
    TrackedIsps: NotRequired[List[str]]

TimestampTypeDef = Union[datetime, str]

class TemplateTypeDef(TypedDict):
    TemplateArn: NotRequired[str]
    TemplateData: NotRequired[str]

class KinesisFirehoseDestinationTypeDef(TypedDict):
    IamRoleArn: str
    DeliveryStreamArn: str

class PinpointDestinationTypeDef(TypedDict):
    ApplicationArn: NotRequired[str]

class SnsDestinationTypeDef(TypedDict):
    TopicArn: str

class SendQuotaTypeDef(TypedDict):
    Max24HourSend: NotRequired[float]
    MaxSendRate: NotRequired[float]
    SentLast24Hours: NotRequired[float]

class GetBlacklistReportsRequestTypeDef(TypedDict):
    BlacklistItemNames: Sequence[str]

class GetConfigurationSetEventDestinationsRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class GetConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class ReputationOptionsOutputTypeDef(TypedDict):
    ReputationMetricsEnabled: NotRequired[bool]
    LastFreshStart: NotRequired[datetime]

class GetDedicatedIpRequestTypeDef(TypedDict):
    Ip: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetDedicatedIpsRequestTypeDef(TypedDict):
    PoolName: NotRequired[str]
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class GetDeliverabilityTestReportRequestTypeDef(TypedDict):
    ReportId: str

class PlacementStatisticsTypeDef(TypedDict):
    InboxPercentage: NotRequired[float]
    SpamPercentage: NotRequired[float]
    MissingPercentage: NotRequired[float]
    SpfPercentage: NotRequired[float]
    DkimPercentage: NotRequired[float]

class GetDomainDeliverabilityCampaignRequestTypeDef(TypedDict):
    CampaignId: str

class GetEmailIdentityRequestTypeDef(TypedDict):
    EmailIdentity: str

class MailFromAttributesTypeDef(TypedDict):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatusType
    BehaviorOnMxFailure: BehaviorOnMxFailureType

class IdentityInfoTypeDef(TypedDict):
    IdentityType: NotRequired[IdentityTypeType]
    IdentityName: NotRequired[str]
    SendingEnabled: NotRequired[bool]

class InboxPlacementTrackingOptionTypeDef(TypedDict):
    Global: NotRequired[bool]
    TrackedIsps: NotRequired[Sequence[str]]

class ListConfigurationSetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListDedicatedIpPoolsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListDeliverabilityTestReportsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListEmailIdentitiesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class MessageTagTypeDef(TypedDict):
    Name: str
    Value: str

class PutAccountDedicatedIpWarmupAttributesRequestTypeDef(TypedDict):
    AutoWarmupEnabled: NotRequired[bool]

class PutAccountSendingAttributesRequestTypeDef(TypedDict):
    SendingEnabled: NotRequired[bool]

class PutConfigurationSetDeliveryOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    TlsPolicy: NotRequired[TlsPolicyType]
    SendingPoolName: NotRequired[str]

class PutConfigurationSetReputationOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    ReputationMetricsEnabled: NotRequired[bool]

class PutConfigurationSetSendingOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    SendingEnabled: NotRequired[bool]

class PutConfigurationSetTrackingOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    CustomRedirectDomain: NotRequired[str]

class PutDedicatedIpInPoolRequestTypeDef(TypedDict):
    Ip: str
    DestinationPoolName: str

class PutDedicatedIpWarmupAttributesRequestTypeDef(TypedDict):
    Ip: str
    WarmupPercentage: int

class PutEmailIdentityDkimAttributesRequestTypeDef(TypedDict):
    EmailIdentity: str
    SigningEnabled: NotRequired[bool]

class PutEmailIdentityFeedbackAttributesRequestTypeDef(TypedDict):
    EmailIdentity: str
    EmailForwardingEnabled: NotRequired[bool]

class PutEmailIdentityMailFromAttributesRequestTypeDef(TypedDict):
    EmailIdentity: str
    MailFromDomain: NotRequired[str]
    BehaviorOnMxFailure: NotRequired[BehaviorOnMxFailureType]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class RawMessageTypeDef(TypedDict):
    Data: BlobTypeDef

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": NotRequired[ContentTypeDef],
        "Html": NotRequired[ContentTypeDef],
    },
)

class CloudWatchDestinationOutputTypeDef(TypedDict):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]

class CloudWatchDestinationTypeDef(TypedDict):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateDedicatedIpPoolRequestTypeDef(TypedDict):
    PoolName: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateEmailIdentityRequestTypeDef(TypedDict):
    EmailIdentity: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateDeliverabilityTestReportResponseTypeDef(TypedDict):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlacklistReportsResponseTypeDef(TypedDict):
    BlacklistReport: Dict[str, List[BlacklistEntryTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(TypedDict):
    ConfigurationSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDedicatedIpPoolsResponseTypeDef(TypedDict):
    DedicatedIpPools: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailIdentityResponseTypeDef(TypedDict):
    IdentityType: IdentityTypeType
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DailyVolumeTypeDef(TypedDict):
    StartDate: NotRequired[datetime]
    VolumeStatistics: NotRequired[VolumeStatisticsTypeDef]
    DomainIspPlacements: NotRequired[List[DomainIspPlacementTypeDef]]

class OverallVolumeTypeDef(TypedDict):
    VolumeStatistics: NotRequired[VolumeStatisticsTypeDef]
    ReadRatePercent: NotRequired[float]
    DomainIspPlacements: NotRequired[List[DomainIspPlacementTypeDef]]

class GetDedicatedIpResponseTypeDef(TypedDict):
    DedicatedIp: DedicatedIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsResponseTypeDef(TypedDict):
    DedicatedIps: List[DedicatedIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDeliverabilityTestReportsResponseTypeDef(TypedDict):
    DeliverabilityTestReports: List[DeliverabilityTestReportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDomainDeliverabilityCampaignResponseTypeDef(TypedDict):
    DomainDeliverabilityCampaign: DomainDeliverabilityCampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainDeliverabilityCampaignsResponseTypeDef(TypedDict):
    DomainDeliverabilityCampaigns: List[DomainDeliverabilityCampaignTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DomainDeliverabilityTrackingOptionOutputTypeDef(TypedDict):
    Domain: NotRequired[str]
    SubscriptionStartDate: NotRequired[datetime]
    InboxPlacementTrackingOption: NotRequired[InboxPlacementTrackingOptionOutputTypeDef]

class GetDomainStatisticsReportRequestTypeDef(TypedDict):
    Domain: str
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef

class ListDomainDeliverabilityCampaignsRequestTypeDef(TypedDict):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef
    SubscribedDomain: str
    NextToken: NotRequired[str]
    PageSize: NotRequired[int]

class ReputationOptionsTypeDef(TypedDict):
    ReputationMetricsEnabled: NotRequired[bool]
    LastFreshStart: NotRequired[TimestampTypeDef]

class GetAccountResponseTypeDef(TypedDict):
    SendQuota: SendQuotaTypeDef
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationSetResponseTypeDef(TypedDict):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsOutputTypeDef
    SendingOptions: SendingOptionsTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDedicatedIpsRequestPaginateTypeDef(TypedDict):
    PoolName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfigurationSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDedicatedIpPoolsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeliverabilityTestReportsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEmailIdentitiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class IspPlacementTypeDef(TypedDict):
    IspName: NotRequired[str]
    PlacementStatistics: NotRequired[PlacementStatisticsTypeDef]

class GetEmailIdentityResponseTypeDef(TypedDict):
    IdentityType: IdentityTypeType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: DkimAttributesTypeDef
    MailFromAttributes: MailFromAttributesTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEmailIdentitiesResponseTypeDef(TypedDict):
    EmailIdentities: List[IdentityInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

InboxPlacementTrackingOptionUnionTypeDef = Union[
    InboxPlacementTrackingOptionTypeDef, InboxPlacementTrackingOptionOutputTypeDef
]

class MessageTypeDef(TypedDict):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class EventDestinationTypeDef(TypedDict):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: NotRequired[bool]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    CloudWatchDestination: NotRequired[CloudWatchDestinationOutputTypeDef]
    SnsDestination: NotRequired[SnsDestinationTypeDef]
    PinpointDestination: NotRequired[PinpointDestinationTypeDef]

CloudWatchDestinationUnionTypeDef = Union[
    CloudWatchDestinationTypeDef, CloudWatchDestinationOutputTypeDef
]

class GetDomainStatisticsReportResponseTypeDef(TypedDict):
    OverallVolume: OverallVolumeTypeDef
    DailyVolumes: List[DailyVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverabilityDashboardOptionsResponseTypeDef(TypedDict):
    DashboardEnabled: bool
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatusType
    ActiveSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    PendingExpirationSubscribedDomains: List[DomainDeliverabilityTrackingOptionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ReputationOptionsUnionTypeDef = Union[ReputationOptionsTypeDef, ReputationOptionsOutputTypeDef]

class GetDeliverabilityTestReportResponseTypeDef(TypedDict):
    DeliverabilityTestReport: DeliverabilityTestReportTypeDef
    OverallPlacement: PlacementStatisticsTypeDef
    IspPlacements: List[IspPlacementTypeDef]
    Message: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainDeliverabilityTrackingOptionTypeDef(TypedDict):
    Domain: NotRequired[str]
    SubscriptionStartDate: NotRequired[TimestampTypeDef]
    InboxPlacementTrackingOption: NotRequired[InboxPlacementTrackingOptionUnionTypeDef]

class EmailContentTypeDef(TypedDict):
    Simple: NotRequired[MessageTypeDef]
    Raw: NotRequired[RawMessageTypeDef]
    Template: NotRequired[TemplateTypeDef]

class GetConfigurationSetEventDestinationsResponseTypeDef(TypedDict):
    EventDestinations: List[EventDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventDestinationDefinitionTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    MatchingEventTypes: NotRequired[Sequence[EventTypeType]]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    CloudWatchDestination: NotRequired[CloudWatchDestinationUnionTypeDef]
    SnsDestination: NotRequired[SnsDestinationTypeDef]
    PinpointDestination: NotRequired[PinpointDestinationTypeDef]

class CreateConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    TrackingOptions: NotRequired[TrackingOptionsTypeDef]
    DeliveryOptions: NotRequired[DeliveryOptionsTypeDef]
    ReputationOptions: NotRequired[ReputationOptionsUnionTypeDef]
    SendingOptions: NotRequired[SendingOptionsTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

DomainDeliverabilityTrackingOptionUnionTypeDef = Union[
    DomainDeliverabilityTrackingOptionTypeDef, DomainDeliverabilityTrackingOptionOutputTypeDef
]

class CreateDeliverabilityTestReportRequestTypeDef(TypedDict):
    FromEmailAddress: str
    Content: EmailContentTypeDef
    ReportName: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class SendEmailRequestTypeDef(TypedDict):
    Destination: DestinationTypeDef
    Content: EmailContentTypeDef
    FromEmailAddress: NotRequired[str]
    ReplyToAddresses: NotRequired[Sequence[str]]
    FeedbackForwardingEmailAddress: NotRequired[str]
    EmailTags: NotRequired[Sequence[MessageTagTypeDef]]
    ConfigurationSetName: NotRequired[str]

class CreateConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class UpdateConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str
    EventDestination: EventDestinationDefinitionTypeDef

class PutDeliverabilityDashboardOptionRequestTypeDef(TypedDict):
    DashboardEnabled: bool
    SubscribedDomains: NotRequired[Sequence[DomainDeliverabilityTrackingOptionUnionTypeDef]]
