"""
Type annotations for notifications service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_notifications.type_defs import SummarizationDimensionDetailTypeDef

    data: SummarizationDimensionDetailTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccessStatusType,
    AccountContactTypeType,
    AggregationDurationType,
    AggregationEventTypeType,
    ChannelAssociationOverrideOptionType,
    ChannelTypeType,
    EventRuleStatusType,
    EventStatusType,
    LocaleCodeType,
    NotificationConfigurationStatusType,
    NotificationHubStatusType,
    NotificationTypeType,
    TextPartTypeType,
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
    "AggregationDetailTypeDef",
    "AggregationKeyTypeDef",
    "AggregationSummaryTypeDef",
    "AssociateChannelRequestTypeDef",
    "AssociateManagedNotificationAccountContactRequestTypeDef",
    "AssociateManagedNotificationAdditionalChannelRequestTypeDef",
    "CreateEventRuleRequestTypeDef",
    "CreateEventRuleResponseTypeDef",
    "CreateNotificationConfigurationRequestTypeDef",
    "CreateNotificationConfigurationResponseTypeDef",
    "DeleteEventRuleRequestTypeDef",
    "DeleteNotificationConfigurationRequestTypeDef",
    "DeregisterNotificationHubRequestTypeDef",
    "DeregisterNotificationHubResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateChannelRequestTypeDef",
    "DisassociateManagedNotificationAccountContactRequestTypeDef",
    "DisassociateManagedNotificationAdditionalChannelRequestTypeDef",
    "EventRuleStatusSummaryTypeDef",
    "EventRuleStructureTypeDef",
    "GetEventRuleRequestTypeDef",
    "GetEventRuleResponseTypeDef",
    "GetManagedNotificationChildEventRequestTypeDef",
    "GetManagedNotificationChildEventResponseTypeDef",
    "GetManagedNotificationConfigurationRequestTypeDef",
    "GetManagedNotificationConfigurationResponseTypeDef",
    "GetManagedNotificationEventRequestTypeDef",
    "GetManagedNotificationEventResponseTypeDef",
    "GetNotificationConfigurationRequestTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetNotificationEventRequestTypeDef",
    "GetNotificationEventResponseTypeDef",
    "GetNotificationsAccessForOrganizationResponseTypeDef",
    "ListChannelsRequestPaginateTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListEventRulesRequestPaginateTypeDef",
    "ListEventRulesRequestTypeDef",
    "ListEventRulesResponseTypeDef",
    "ListManagedNotificationChannelAssociationsRequestPaginateTypeDef",
    "ListManagedNotificationChannelAssociationsRequestTypeDef",
    "ListManagedNotificationChannelAssociationsResponseTypeDef",
    "ListManagedNotificationChildEventsRequestPaginateTypeDef",
    "ListManagedNotificationChildEventsRequestTypeDef",
    "ListManagedNotificationChildEventsResponseTypeDef",
    "ListManagedNotificationConfigurationsRequestPaginateTypeDef",
    "ListManagedNotificationConfigurationsRequestTypeDef",
    "ListManagedNotificationConfigurationsResponseTypeDef",
    "ListManagedNotificationEventsRequestPaginateTypeDef",
    "ListManagedNotificationEventsRequestTypeDef",
    "ListManagedNotificationEventsResponseTypeDef",
    "ListNotificationConfigurationsRequestPaginateTypeDef",
    "ListNotificationConfigurationsRequestTypeDef",
    "ListNotificationConfigurationsResponseTypeDef",
    "ListNotificationEventsRequestPaginateTypeDef",
    "ListNotificationEventsRequestTypeDef",
    "ListNotificationEventsResponseTypeDef",
    "ListNotificationHubsRequestPaginateTypeDef",
    "ListNotificationHubsRequestTypeDef",
    "ListNotificationHubsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedNotificationChannelAssociationSummaryTypeDef",
    "ManagedNotificationChildEventOverviewTypeDef",
    "ManagedNotificationChildEventSummaryTypeDef",
    "ManagedNotificationChildEventTypeDef",
    "ManagedNotificationConfigurationStructureTypeDef",
    "ManagedNotificationEventOverviewTypeDef",
    "ManagedNotificationEventSummaryTypeDef",
    "ManagedNotificationEventTypeDef",
    "ManagedSourceEventMetadataSummaryTypeDef",
    "MediaElementTypeDef",
    "MessageComponentsSummaryTypeDef",
    "MessageComponentsTypeDef",
    "NotificationConfigurationStructureTypeDef",
    "NotificationEventOverviewTypeDef",
    "NotificationEventSummaryTypeDef",
    "NotificationEventTypeDef",
    "NotificationHubOverviewTypeDef",
    "NotificationHubStatusSummaryTypeDef",
    "NotificationsAccessForOrganizationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterNotificationHubRequestTypeDef",
    "RegisterNotificationHubResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SourceEventMetadataSummaryTypeDef",
    "SourceEventMetadataTypeDef",
    "SummarizationDimensionDetailTypeDef",
    "SummarizationDimensionOverviewTypeDef",
    "TagResourceRequestTypeDef",
    "TextPartValueTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEventRuleRequestTypeDef",
    "UpdateEventRuleResponseTypeDef",
    "UpdateNotificationConfigurationRequestTypeDef",
    "UpdateNotificationConfigurationResponseTypeDef",
)

class SummarizationDimensionDetailTypeDef(TypedDict):
    name: str
    value: str

class AggregationKeyTypeDef(TypedDict):
    name: str
    value: str

class SummarizationDimensionOverviewTypeDef(TypedDict):
    name: str
    count: int
    sampleValues: NotRequired[List[str]]

class AssociateChannelRequestTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str

class AssociateManagedNotificationAccountContactRequestTypeDef(TypedDict):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str

class AssociateManagedNotificationAdditionalChannelRequestTypeDef(TypedDict):
    channelArn: str
    managedNotificationConfigurationArn: str

class CreateEventRuleRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    source: str
    eventType: str
    regions: Sequence[str]
    eventPattern: NotRequired[str]

class EventRuleStatusSummaryTypeDef(TypedDict):
    status: EventRuleStatusType
    reason: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateNotificationConfigurationRequestTypeDef(TypedDict):
    name: str
    description: str
    aggregationDuration: NotRequired[AggregationDurationType]
    tags: NotRequired[Mapping[str, str]]

class DeleteEventRuleRequestTypeDef(TypedDict):
    arn: str

class DeleteNotificationConfigurationRequestTypeDef(TypedDict):
    arn: str

class DeregisterNotificationHubRequestTypeDef(TypedDict):
    notificationHubRegion: str

class NotificationHubStatusSummaryTypeDef(TypedDict):
    status: NotificationHubStatusType
    reason: str

class DimensionTypeDef(TypedDict):
    name: str
    value: str

class DisassociateChannelRequestTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str

class DisassociateManagedNotificationAccountContactRequestTypeDef(TypedDict):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str

class DisassociateManagedNotificationAdditionalChannelRequestTypeDef(TypedDict):
    channelArn: str
    managedNotificationConfigurationArn: str

class GetEventRuleRequestTypeDef(TypedDict):
    arn: str

class GetManagedNotificationChildEventRequestTypeDef(TypedDict):
    arn: str
    locale: NotRequired[LocaleCodeType]

class GetManagedNotificationConfigurationRequestTypeDef(TypedDict):
    arn: str

class GetManagedNotificationEventRequestTypeDef(TypedDict):
    arn: str
    locale: NotRequired[LocaleCodeType]

class GetNotificationConfigurationRequestTypeDef(TypedDict):
    arn: str

class GetNotificationEventRequestTypeDef(TypedDict):
    arn: str
    locale: NotRequired[LocaleCodeType]

class NotificationsAccessForOrganizationTypeDef(TypedDict):
    accessStatus: AccessStatusType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChannelsRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEventRulesRequestTypeDef(TypedDict):
    notificationConfigurationArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListManagedNotificationChannelAssociationsRequestTypeDef(TypedDict):
    managedNotificationConfigurationArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ManagedNotificationChannelAssociationSummaryTypeDef(TypedDict):
    channelIdentifier: str
    channelType: ChannelTypeType
    overrideOption: NotRequired[ChannelAssociationOverrideOptionType]

TimestampTypeDef = Union[datetime, str]

class ListManagedNotificationConfigurationsRequestTypeDef(TypedDict):
    channelIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ManagedNotificationConfigurationStructureTypeDef(TypedDict):
    arn: str
    name: str
    description: str

class ListNotificationConfigurationsRequestTypeDef(TypedDict):
    eventRuleSource: NotRequired[str]
    channelArn: NotRequired[str]
    status: NotRequired[NotificationConfigurationStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class NotificationConfigurationStructureTypeDef(TypedDict):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: NotRequired[AggregationDurationType]

class ListNotificationHubsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    arn: str

class ManagedSourceEventMetadataSummaryTypeDef(TypedDict):
    source: str
    eventType: str
    eventOriginRegion: NotRequired[str]

class MessageComponentsSummaryTypeDef(TypedDict):
    headline: str

TextPartValueTypeDef = TypedDict(
    "TextPartValueTypeDef",
    {
        "type": TextPartTypeType,
        "displayText": NotRequired[str],
        "textByLocale": NotRequired[Dict[LocaleCodeType, str]],
        "url": NotRequired[str],
    },
)
MediaElementTypeDef = TypedDict(
    "MediaElementTypeDef",
    {
        "mediaId": str,
        "type": Literal["IMAGE"],
        "url": str,
        "caption": str,
    },
)

class SourceEventMetadataSummaryTypeDef(TypedDict):
    source: str
    eventType: str
    eventOriginRegion: NotRequired[str]

class RegisterNotificationHubRequestTypeDef(TypedDict):
    notificationHubRegion: str

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "detailUrl": NotRequired[str],
        "tags": NotRequired[List[str]],
    },
)

class TagResourceRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    arn: str
    tagKeys: Sequence[str]

class UpdateEventRuleRequestTypeDef(TypedDict):
    arn: str
    eventPattern: NotRequired[str]
    regions: NotRequired[Sequence[str]]

class UpdateNotificationConfigurationRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    aggregationDuration: NotRequired[AggregationDurationType]

class AggregationDetailTypeDef(TypedDict):
    summarizationDimensions: NotRequired[List[SummarizationDimensionDetailTypeDef]]

class AggregationSummaryTypeDef(TypedDict):
    eventCount: int
    aggregatedBy: List[AggregationKeyTypeDef]
    aggregatedAccounts: SummarizationDimensionOverviewTypeDef
    aggregatedRegions: SummarizationDimensionOverviewTypeDef
    aggregatedOrganizationalUnits: NotRequired[SummarizationDimensionOverviewTypeDef]
    additionalSummarizationDimensions: NotRequired[List[SummarizationDimensionOverviewTypeDef]]

class EventRuleStructureTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]

class CreateEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    status: NotificationConfigurationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    description: str
    category: str
    subCategory: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: AggregationDurationType
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(TypedDict):
    channels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventRuleResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotificationConfigurationResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterNotificationHubResponseTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NotificationHubOverviewTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: NotRequired[datetime]

class RegisterNotificationHubResponseTypeDef(TypedDict):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class MessageComponentsTypeDef(TypedDict):
    headline: NotRequired[str]
    paragraphSummary: NotRequired[str]
    completeDescription: NotRequired[str]
    dimensions: NotRequired[List[DimensionTypeDef]]

class GetNotificationsAccessForOrganizationResponseTypeDef(TypedDict):
    notificationsAccessForOrganization: NotificationsAccessForOrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsRequestPaginateTypeDef(TypedDict):
    notificationConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventRulesRequestPaginateTypeDef(TypedDict):
    notificationConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedNotificationChannelAssociationsRequestPaginateTypeDef(TypedDict):
    managedNotificationConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedNotificationConfigurationsRequestPaginateTypeDef(TypedDict):
    channelIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationConfigurationsRequestPaginateTypeDef(TypedDict):
    eventRuleSource: NotRequired[str]
    channelArn: NotRequired[str]
    status: NotRequired[NotificationConfigurationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationHubsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedNotificationChannelAssociationsResponseTypeDef(TypedDict):
    channelAssociations: List[ManagedNotificationChannelAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListManagedNotificationChildEventsRequestPaginateTypeDef(TypedDict):
    aggregateManagedNotificationEventArn: str
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    relatedAccount: NotRequired[str]
    organizationalUnitId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedNotificationChildEventsRequestTypeDef(TypedDict):
    aggregateManagedNotificationEventArn: str
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    maxResults: NotRequired[int]
    relatedAccount: NotRequired[str]
    organizationalUnitId: NotRequired[str]
    nextToken: NotRequired[str]

class ListManagedNotificationEventsRequestPaginateTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    organizationalUnitId: NotRequired[str]
    relatedAccount: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedNotificationEventsRequestTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    organizationalUnitId: NotRequired[str]
    relatedAccount: NotRequired[str]

class ListNotificationEventsRequestPaginateTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    includeChildEvents: NotRequired[bool]
    aggregateNotificationEventArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationEventsRequestTypeDef(TypedDict):
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    locale: NotRequired[LocaleCodeType]
    source: NotRequired[str]
    includeChildEvents: NotRequired[bool]
    aggregateNotificationEventArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListManagedNotificationConfigurationsResponseTypeDef(TypedDict):
    managedNotificationConfigurations: List[ManagedNotificationConfigurationStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListNotificationConfigurationsResponseTypeDef(TypedDict):
    notificationConfigurations: List[NotificationConfigurationStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ManagedNotificationEventSummaryTypeDef(TypedDict):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: ManagedSourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType

class NotificationEventSummaryTypeDef(TypedDict):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: SourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType

class SourceEventMetadataTypeDef(TypedDict):
    eventTypeVersion: str
    sourceEventId: str
    relatedAccount: str
    source: str
    eventOccurrenceTime: datetime
    eventType: str
    relatedResources: List[ResourceTypeDef]
    eventOriginRegion: NotRequired[str]

class ManagedNotificationChildEventSummaryTypeDef(TypedDict):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: ManagedSourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    aggregationDetail: AggregationDetailTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType

class ListEventRulesResponseTypeDef(TypedDict):
    eventRules: List[EventRuleStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListNotificationHubsResponseTypeDef(TypedDict):
    notificationHubs: List[NotificationHubOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ManagedNotificationChildEventTypeDef = TypedDict(
    "ManagedNotificationChildEventTypeDef",
    {
        "schemaVersion": Literal["v1.0"],
        "id": str,
        "messageComponents": MessageComponentsTypeDef,
        "notificationType": NotificationTypeType,
        "aggregateManagedNotificationEventArn": str,
        "textParts": Dict[str, TextPartValueTypeDef],
        "sourceEventDetailUrl": NotRequired[str],
        "sourceEventDetailUrlDisplayText": NotRequired[str],
        "eventStatus": NotRequired[EventStatusType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "organizationalUnitId": NotRequired[str],
        "aggregationDetail": NotRequired[AggregationDetailTypeDef],
    },
)
ManagedNotificationEventTypeDef = TypedDict(
    "ManagedNotificationEventTypeDef",
    {
        "schemaVersion": Literal["v1.0"],
        "id": str,
        "messageComponents": MessageComponentsTypeDef,
        "notificationType": NotificationTypeType,
        "textParts": Dict[str, TextPartValueTypeDef],
        "sourceEventDetailUrl": NotRequired[str],
        "sourceEventDetailUrlDisplayText": NotRequired[str],
        "eventStatus": NotRequired[EventStatusType],
        "aggregationEventType": NotRequired[AggregationEventTypeType],
        "aggregationSummary": NotRequired[AggregationSummaryTypeDef],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "organizationalUnitId": NotRequired[str],
    },
)

class ManagedNotificationEventOverviewTypeDef(TypedDict):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: ManagedNotificationEventSummaryTypeDef
    aggregationEventType: NotRequired[AggregationEventTypeType]
    organizationalUnitId: NotRequired[str]
    aggregationSummary: NotRequired[AggregationSummaryTypeDef]
    aggregatedNotificationRegions: NotRequired[List[str]]

class NotificationEventOverviewTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: NotificationEventSummaryTypeDef
    aggregationEventType: NotRequired[AggregationEventTypeType]
    aggregateNotificationEventArn: NotRequired[str]
    aggregationSummary: NotRequired[AggregationSummaryTypeDef]

NotificationEventTypeDef = TypedDict(
    "NotificationEventTypeDef",
    {
        "schemaVersion": Literal["v1.0"],
        "id": str,
        "sourceEventMetadata": SourceEventMetadataTypeDef,
        "messageComponents": MessageComponentsTypeDef,
        "notificationType": NotificationTypeType,
        "textParts": Dict[str, TextPartValueTypeDef],
        "media": List[MediaElementTypeDef],
        "sourceEventDetailUrl": NotRequired[str],
        "sourceEventDetailUrlDisplayText": NotRequired[str],
        "eventStatus": NotRequired[EventStatusType],
        "aggregationEventType": NotRequired[AggregationEventTypeType],
        "aggregateNotificationEventArn": NotRequired[str],
        "aggregationSummary": NotRequired[AggregationSummaryTypeDef],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)

class ManagedNotificationChildEventOverviewTypeDef(TypedDict):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    childEvent: ManagedNotificationChildEventSummaryTypeDef
    aggregateManagedNotificationEventArn: str
    organizationalUnitId: NotRequired[str]

class GetManagedNotificationChildEventResponseTypeDef(TypedDict):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationChildEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedNotificationEventResponseTypeDef(TypedDict):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedNotificationEventsResponseTypeDef(TypedDict):
    managedNotificationEvents: List[ManagedNotificationEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListNotificationEventsResponseTypeDef(TypedDict):
    notificationEvents: List[NotificationEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetNotificationEventResponseTypeDef(TypedDict):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    content: NotificationEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedNotificationChildEventsResponseTypeDef(TypedDict):
    managedNotificationChildEvents: List[ManagedNotificationChildEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
