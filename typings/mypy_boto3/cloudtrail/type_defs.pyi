"""
Type annotations for cloudtrail service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    BillingModeType,
    DashboardStatusType,
    DashboardTypeType,
    DeliveryStatusType,
    DestinationTypeType,
    EventDataStoreStatusType,
    FederationStatusType,
    ImportFailureStatusType,
    ImportStatusType,
    InsightsMetricDataTypeType,
    InsightTypeType,
    LookupAttributeKeyType,
    QueryStatusType,
    ReadWriteTypeType,
    RefreshScheduleFrequencyUnitType,
    RefreshScheduleStatusType,
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
    "AddTagsRequestTypeDef",
    "AdvancedEventSelectorOutputTypeDef",
    "AdvancedEventSelectorTypeDef",
    "AdvancedEventSelectorUnionTypeDef",
    "AdvancedFieldSelectorOutputTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "AdvancedFieldSelectorUnionTypeDef",
    "CancelQueryRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDashboardRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateEventDataStoreRequestTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "CreateTrailRequestTypeDef",
    "CreateTrailResponseTypeDef",
    "DashboardDetailTypeDef",
    "DataResourceOutputTypeDef",
    "DataResourceTypeDef",
    "DataResourceUnionTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteDashboardRequestTypeDef",
    "DeleteEventDataStoreRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteTrailRequestTypeDef",
    "DeregisterOrganizationDelegatedAdminRequestTypeDef",
    "DescribeQueryRequestTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsRequestTypeDef",
    "DescribeTrailsResponseTypeDef",
    "DestinationTypeDef",
    "DisableFederationRequestTypeDef",
    "DisableFederationResponseTypeDef",
    "EnableFederationRequestTypeDef",
    "EnableFederationResponseTypeDef",
    "EventDataStoreTypeDef",
    "EventSelectorOutputTypeDef",
    "EventSelectorTypeDef",
    "EventSelectorUnionTypeDef",
    "EventTypeDef",
    "GenerateQueryRequestTypeDef",
    "GenerateQueryResponseTypeDef",
    "GetChannelRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetDashboardRequestTypeDef",
    "GetDashboardResponseTypeDef",
    "GetEventDataStoreRequestTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "GetEventSelectorsRequestTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetImportRequestTypeDef",
    "GetImportResponseTypeDef",
    "GetInsightSelectorsRequestTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetQueryResultsRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetTrailRequestTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "ImportFailureListItemTypeDef",
    "ImportSourceTypeDef",
    "ImportStatisticsTypeDef",
    "ImportsListItemTypeDef",
    "IngestionStatusTypeDef",
    "InsightSelectorTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDashboardsRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListEventDataStoresRequestTypeDef",
    "ListEventDataStoresResponseTypeDef",
    "ListImportFailuresRequestPaginateTypeDef",
    "ListImportFailuresRequestTypeDef",
    "ListImportFailuresResponseTypeDef",
    "ListImportsRequestPaginateTypeDef",
    "ListImportsRequestTypeDef",
    "ListImportsResponseTypeDef",
    "ListInsightsMetricDataRequestTypeDef",
    "ListInsightsMetricDataResponseTypeDef",
    "ListPublicKeysRequestPaginateTypeDef",
    "ListPublicKeysRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListQueriesRequestTypeDef",
    "ListQueriesResponseTypeDef",
    "ListTagsRequestPaginateTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListTrailsRequestPaginateTypeDef",
    "ListTrailsRequestTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupAttributeTypeDef",
    "LookupEventsRequestPaginateTypeDef",
    "LookupEventsRequestTypeDef",
    "LookupEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionKeyTypeDef",
    "PublicKeyTypeDef",
    "PutEventSelectorsRequestTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "PutInsightSelectorsRequestTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "QueryStatisticsForDescribeQueryTypeDef",
    "QueryStatisticsTypeDef",
    "QueryTypeDef",
    "RefreshScheduleFrequencyTypeDef",
    "RefreshScheduleTypeDef",
    "RegisterOrganizationDelegatedAdminRequestTypeDef",
    "RemoveTagsRequestTypeDef",
    "RequestWidgetTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreEventDataStoreRequestTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "S3ImportSourceTypeDef",
    "SearchSampleQueriesRequestTypeDef",
    "SearchSampleQueriesResponseTypeDef",
    "SearchSampleQueriesSearchResultTypeDef",
    "SourceConfigTypeDef",
    "StartDashboardRefreshRequestTypeDef",
    "StartDashboardRefreshResponseTypeDef",
    "StartEventDataStoreIngestionRequestTypeDef",
    "StartImportRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartLoggingRequestTypeDef",
    "StartQueryRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopEventDataStoreIngestionRequestTypeDef",
    "StopImportRequestTypeDef",
    "StopImportResponseTypeDef",
    "StopLoggingRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateDashboardRequestTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateEventDataStoreRequestTypeDef",
    "UpdateEventDataStoreResponseTypeDef",
    "UpdateTrailRequestTypeDef",
    "UpdateTrailResponseTypeDef",
    "WidgetTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class AdvancedFieldSelectorOutputTypeDef(TypedDict):
    Field: str
    Equals: NotRequired[List[str]]
    StartsWith: NotRequired[List[str]]
    EndsWith: NotRequired[List[str]]
    NotEquals: NotRequired[List[str]]
    NotStartsWith: NotRequired[List[str]]
    NotEndsWith: NotRequired[List[str]]

class AdvancedFieldSelectorTypeDef(TypedDict):
    Field: str
    Equals: NotRequired[Sequence[str]]
    StartsWith: NotRequired[Sequence[str]]
    EndsWith: NotRequired[Sequence[str]]
    NotEquals: NotRequired[Sequence[str]]
    NotStartsWith: NotRequired[Sequence[str]]
    NotEndsWith: NotRequired[Sequence[str]]

class CancelQueryRequestTypeDef(TypedDict):
    QueryId: str
    EventDataStore: NotRequired[str]
    EventDataStoreOwnerAccountId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ChannelTypeDef(TypedDict):
    ChannelArn: NotRequired[str]
    Name: NotRequired[str]

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Type": DestinationTypeType,
        "Location": str,
    },
)

class RequestWidgetTypeDef(TypedDict):
    QueryStatement: str
    ViewProperties: Mapping[str, str]
    QueryParameters: NotRequired[Sequence[str]]

class WidgetTypeDef(TypedDict):
    QueryAlias: NotRequired[str]
    QueryStatement: NotRequired[str]
    QueryParameters: NotRequired[List[str]]
    ViewProperties: NotRequired[Dict[str, str]]

DashboardDetailTypeDef = TypedDict(
    "DashboardDetailTypeDef",
    {
        "DashboardArn": NotRequired[str],
        "Type": NotRequired[DashboardTypeType],
    },
)
DataResourceOutputTypeDef = TypedDict(
    "DataResourceOutputTypeDef",
    {
        "Type": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

class DeleteChannelRequestTypeDef(TypedDict):
    Channel: str

class DeleteDashboardRequestTypeDef(TypedDict):
    DashboardId: str

class DeleteEventDataStoreRequestTypeDef(TypedDict):
    EventDataStore: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteTrailRequestTypeDef(TypedDict):
    Name: str

class DeregisterOrganizationDelegatedAdminRequestTypeDef(TypedDict):
    DelegatedAdminAccountId: str

class DescribeQueryRequestTypeDef(TypedDict):
    EventDataStore: NotRequired[str]
    QueryId: NotRequired[str]
    QueryAlias: NotRequired[str]
    RefreshId: NotRequired[str]
    EventDataStoreOwnerAccountId: NotRequired[str]

class QueryStatisticsForDescribeQueryTypeDef(TypedDict):
    EventsMatched: NotRequired[int]
    EventsScanned: NotRequired[int]
    BytesScanned: NotRequired[int]
    ExecutionTimeInMillis: NotRequired[int]
    CreationTime: NotRequired[datetime]

class DescribeTrailsRequestTypeDef(TypedDict):
    trailNameList: NotRequired[Sequence[str]]
    includeShadowTrails: NotRequired[bool]

class TrailTypeDef(TypedDict):
    Name: NotRequired[str]
    S3BucketName: NotRequired[str]
    S3KeyPrefix: NotRequired[str]
    SnsTopicName: NotRequired[str]
    SnsTopicARN: NotRequired[str]
    IncludeGlobalServiceEvents: NotRequired[bool]
    IsMultiRegionTrail: NotRequired[bool]
    HomeRegion: NotRequired[str]
    TrailARN: NotRequired[str]
    LogFileValidationEnabled: NotRequired[bool]
    CloudWatchLogsLogGroupArn: NotRequired[str]
    CloudWatchLogsRoleArn: NotRequired[str]
    KmsKeyId: NotRequired[str]
    HasCustomEventSelectors: NotRequired[bool]
    HasInsightSelectors: NotRequired[bool]
    IsOrganizationTrail: NotRequired[bool]

class DisableFederationRequestTypeDef(TypedDict):
    EventDataStore: str

class EnableFederationRequestTypeDef(TypedDict):
    EventDataStore: str
    FederationRoleArn: str

class ResourceTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceName: NotRequired[str]

class GenerateQueryRequestTypeDef(TypedDict):
    EventDataStores: Sequence[str]
    Prompt: str

class GetChannelRequestTypeDef(TypedDict):
    Channel: str

class IngestionStatusTypeDef(TypedDict):
    LatestIngestionSuccessTime: NotRequired[datetime]
    LatestIngestionSuccessEventID: NotRequired[str]
    LatestIngestionErrorCode: NotRequired[str]
    LatestIngestionAttemptTime: NotRequired[datetime]
    LatestIngestionAttemptEventID: NotRequired[str]

class GetDashboardRequestTypeDef(TypedDict):
    DashboardId: str

class GetEventDataStoreRequestTypeDef(TypedDict):
    EventDataStore: str

PartitionKeyTypeDef = TypedDict(
    "PartitionKeyTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

class GetEventSelectorsRequestTypeDef(TypedDict):
    TrailName: str

class GetImportRequestTypeDef(TypedDict):
    ImportId: str

class ImportStatisticsTypeDef(TypedDict):
    PrefixesFound: NotRequired[int]
    PrefixesCompleted: NotRequired[int]
    FilesCompleted: NotRequired[int]
    EventsCompleted: NotRequired[int]
    FailedEntries: NotRequired[int]

class GetInsightSelectorsRequestTypeDef(TypedDict):
    TrailName: NotRequired[str]
    EventDataStore: NotRequired[str]

class InsightSelectorTypeDef(TypedDict):
    InsightType: NotRequired[InsightTypeType]

class GetQueryResultsRequestTypeDef(TypedDict):
    QueryId: str
    EventDataStore: NotRequired[str]
    NextToken: NotRequired[str]
    MaxQueryResults: NotRequired[int]
    EventDataStoreOwnerAccountId: NotRequired[str]

class QueryStatisticsTypeDef(TypedDict):
    ResultsCount: NotRequired[int]
    TotalResultsCount: NotRequired[int]
    BytesScanned: NotRequired[int]

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class GetTrailRequestTypeDef(TypedDict):
    Name: str

class GetTrailStatusRequestTypeDef(TypedDict):
    Name: str

class ImportFailureListItemTypeDef(TypedDict):
    Location: NotRequired[str]
    Status: NotRequired[ImportFailureStatusType]
    ErrorType: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LastUpdatedTime: NotRequired[datetime]

class S3ImportSourceTypeDef(TypedDict):
    S3LocationUri: str
    S3BucketRegion: str
    S3BucketAccessRoleArn: str

class ImportsListItemTypeDef(TypedDict):
    ImportId: NotRequired[str]
    ImportStatus: NotRequired[ImportStatusType]
    Destinations: NotRequired[List[str]]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class ListChannelsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

ListDashboardsRequestTypeDef = TypedDict(
    "ListDashboardsRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "Type": NotRequired[DashboardTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

class ListEventDataStoresRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListImportFailuresRequestTypeDef(TypedDict):
    ImportId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListImportsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    Destination: NotRequired[str]
    ImportStatus: NotRequired[ImportStatusType]
    NextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class PublicKeyTypeDef(TypedDict):
    Value: NotRequired[bytes]
    ValidityStartTime: NotRequired[datetime]
    ValidityEndTime: NotRequired[datetime]
    Fingerprint: NotRequired[str]

class QueryTypeDef(TypedDict):
    QueryId: NotRequired[str]
    QueryStatus: NotRequired[QueryStatusType]
    CreationTime: NotRequired[datetime]

class ListTagsRequestTypeDef(TypedDict):
    ResourceIdList: Sequence[str]
    NextToken: NotRequired[str]

class ListTrailsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class TrailInfoTypeDef(TypedDict):
    TrailARN: NotRequired[str]
    Name: NotRequired[str]
    HomeRegion: NotRequired[str]

class LookupAttributeTypeDef(TypedDict):
    AttributeKey: LookupAttributeKeyType
    AttributeValue: str

class PutResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourcePolicy: str

class RefreshScheduleFrequencyTypeDef(TypedDict):
    Unit: NotRequired[RefreshScheduleFrequencyUnitType]
    Value: NotRequired[int]

class RegisterOrganizationDelegatedAdminRequestTypeDef(TypedDict):
    MemberAccountId: str

class RestoreEventDataStoreRequestTypeDef(TypedDict):
    EventDataStore: str

class SearchSampleQueriesRequestTypeDef(TypedDict):
    SearchPhrase: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SearchSampleQueriesSearchResultTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    SQL: NotRequired[str]
    Relevance: NotRequired[float]

class StartDashboardRefreshRequestTypeDef(TypedDict):
    DashboardId: str
    QueryParameterValues: NotRequired[Mapping[str, str]]

class StartEventDataStoreIngestionRequestTypeDef(TypedDict):
    EventDataStore: str

class StartLoggingRequestTypeDef(TypedDict):
    Name: str

class StartQueryRequestTypeDef(TypedDict):
    QueryStatement: NotRequired[str]
    DeliveryS3Uri: NotRequired[str]
    QueryAlias: NotRequired[str]
    QueryParameters: NotRequired[Sequence[str]]
    EventDataStoreOwnerAccountId: NotRequired[str]

class StopEventDataStoreIngestionRequestTypeDef(TypedDict):
    EventDataStore: str

class StopImportRequestTypeDef(TypedDict):
    ImportId: str

class StopLoggingRequestTypeDef(TypedDict):
    Name: str

class UpdateTrailRequestTypeDef(TypedDict):
    Name: str
    S3BucketName: NotRequired[str]
    S3KeyPrefix: NotRequired[str]
    SnsTopicName: NotRequired[str]
    IncludeGlobalServiceEvents: NotRequired[bool]
    IsMultiRegionTrail: NotRequired[bool]
    EnableLogFileValidation: NotRequired[bool]
    CloudWatchLogsLogGroupArn: NotRequired[str]
    CloudWatchLogsRoleArn: NotRequired[str]
    KmsKeyId: NotRequired[str]
    IsOrganizationTrail: NotRequired[bool]

class AddTagsRequestTypeDef(TypedDict):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class CreateTrailRequestTypeDef(TypedDict):
    Name: str
    S3BucketName: str
    S3KeyPrefix: NotRequired[str]
    SnsTopicName: NotRequired[str]
    IncludeGlobalServiceEvents: NotRequired[bool]
    IsMultiRegionTrail: NotRequired[bool]
    EnableLogFileValidation: NotRequired[bool]
    CloudWatchLogsLogGroupArn: NotRequired[str]
    CloudWatchLogsRoleArn: NotRequired[str]
    KmsKeyId: NotRequired[str]
    IsOrganizationTrail: NotRequired[bool]
    TagsList: NotRequired[Sequence[TagTypeDef]]

class RemoveTagsRequestTypeDef(TypedDict):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class ResourceTagTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    TagsList: NotRequired[List[TagTypeDef]]

class AdvancedEventSelectorOutputTypeDef(TypedDict):
    FieldSelectors: List[AdvancedFieldSelectorOutputTypeDef]
    Name: NotRequired[str]

AdvancedFieldSelectorUnionTypeDef = Union[
    AdvancedFieldSelectorTypeDef, AdvancedFieldSelectorOutputTypeDef
]

class CancelQueryResponseTypeDef(TypedDict):
    QueryId: str
    QueryStatus: QueryStatusType
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrailResponseTypeDef(TypedDict):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableFederationResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableFederationResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateQueryResponseTypeDef(TypedDict):
    QueryStatement: str
    QueryAlias: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailStatusResponseTypeDef(TypedDict):
    IsLogging: bool
    LatestDeliveryError: str
    LatestNotificationError: str
    LatestDeliveryTime: datetime
    LatestNotificationTime: datetime
    StartLoggingTime: datetime
    StopLoggingTime: datetime
    LatestCloudWatchLogsDeliveryError: str
    LatestCloudWatchLogsDeliveryTime: datetime
    LatestDigestDeliveryTime: datetime
    LatestDigestDeliveryError: str
    LatestDeliveryAttemptTime: str
    LatestNotificationAttemptTime: str
    LatestNotificationAttemptSucceeded: str
    LatestDeliveryAttemptSucceeded: str
    TimeLoggingStarted: str
    TimeLoggingStopped: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsMetricDataResponseTypeDef(TypedDict):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: str
    Timestamps: List[datetime]
    Values: List[float]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDashboardRefreshResponseTypeDef(TypedDict):
    RefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryResponseTypeDef(TypedDict):
    QueryId: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrailResponseTypeDef(TypedDict):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(TypedDict):
    Channels: List[ChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateChannelRequestTypeDef(TypedDict):
    Name: str
    Source: str
    Destinations: Sequence[DestinationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateChannelResponseTypeDef(TypedDict):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelRequestTypeDef(TypedDict):
    Channel: str
    Destinations: NotRequired[Sequence[DestinationTypeDef]]
    Name: NotRequired[str]

class UpdateChannelResponseTypeDef(TypedDict):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDashboardsResponseTypeDef(TypedDict):
    Dashboards: List[DashboardDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EventSelectorOutputTypeDef(TypedDict):
    ReadWriteType: NotRequired[ReadWriteTypeType]
    IncludeManagementEvents: NotRequired[bool]
    DataResources: NotRequired[List[DataResourceOutputTypeDef]]
    ExcludeManagementEventSources: NotRequired[List[str]]

DataResourceUnionTypeDef = Union[DataResourceTypeDef, DataResourceOutputTypeDef]

class DescribeQueryResponseTypeDef(TypedDict):
    QueryId: str
    QueryString: str
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsForDescribeQueryTypeDef
    ErrorMessage: str
    DeliveryS3Uri: str
    DeliveryStatus: DeliveryStatusType
    Prompt: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrailsResponseTypeDef(TypedDict):
    trailList: List[TrailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailResponseTypeDef(TypedDict):
    Trail: TrailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": NotRequired[str],
        "EventName": NotRequired[str],
        "ReadOnly": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Username": NotRequired[str],
        "Resources": NotRequired[List[ResourceTypeDef]],
        "CloudTrailEvent": NotRequired[str],
    },
)

class GetInsightSelectorsResponseTypeDef(TypedDict):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutInsightSelectorsRequestTypeDef(TypedDict):
    InsightSelectors: Sequence[InsightSelectorTypeDef]
    TrailName: NotRequired[str]
    EventDataStore: NotRequired[str]
    InsightsDestination: NotRequired[str]

class PutInsightSelectorsResponseTypeDef(TypedDict):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsResponseTypeDef(TypedDict):
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsTypeDef
    QueryResultRows: List[List[Dict[str, str]]]
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListImportFailuresResponseTypeDef(TypedDict):
    Failures: List[ImportFailureListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ImportSourceTypeDef(TypedDict):
    S3: S3ImportSourceTypeDef

class ListImportsResponseTypeDef(TypedDict):
    Imports: List[ImportsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListImportFailuresRequestPaginateTypeDef(TypedDict):
    ImportId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportsRequestPaginateTypeDef(TypedDict):
    Destination: NotRequired[str]
    ImportStatus: NotRequired[ImportStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsRequestPaginateTypeDef(TypedDict):
    ResourceIdList: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrailsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInsightsMetricDataRequestTypeDef(TypedDict):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Period: NotRequired[int]
    DataType: NotRequired[InsightsMetricDataTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPublicKeysRequestPaginateTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPublicKeysRequestTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]

class ListQueriesRequestTypeDef(TypedDict):
    EventDataStore: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    QueryStatus: NotRequired[QueryStatusType]

class ListPublicKeysResponseTypeDef(TypedDict):
    PublicKeyList: List[PublicKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQueriesResponseTypeDef(TypedDict):
    Queries: List[QueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTrailsResponseTypeDef(TypedDict):
    Trails: List[TrailInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LookupEventsRequestPaginateTypeDef(TypedDict):
    LookupAttributes: NotRequired[Sequence[LookupAttributeTypeDef]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventCategory: NotRequired[Literal["insight"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LookupEventsRequestTypeDef(TypedDict):
    LookupAttributes: NotRequired[Sequence[LookupAttributeTypeDef]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventCategory: NotRequired[Literal["insight"]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RefreshScheduleTypeDef(TypedDict):
    Frequency: NotRequired[RefreshScheduleFrequencyTypeDef]
    Status: NotRequired[RefreshScheduleStatusType]
    TimeOfDay: NotRequired[str]

class SearchSampleQueriesResponseTypeDef(TypedDict):
    SearchResults: List[SearchSampleQueriesSearchResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsResponseTypeDef(TypedDict):
    ResourceTagList: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateEventDataStoreResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    TagsList: List[TagTypeDef]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadataTypeDef

class EventDataStoreTypeDef(TypedDict):
    EventDataStoreArn: NotRequired[str]
    Name: NotRequired[str]
    TerminationProtectionEnabled: NotRequired[bool]
    Status: NotRequired[EventDataStoreStatusType]
    AdvancedEventSelectors: NotRequired[List[AdvancedEventSelectorOutputTypeDef]]
    MultiRegionEnabled: NotRequired[bool]
    OrganizationEnabled: NotRequired[bool]
    RetentionPeriod: NotRequired[int]
    CreatedTimestamp: NotRequired[datetime]
    UpdatedTimestamp: NotRequired[datetime]

class GetEventDataStoreResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    PartitionKeys: List[PartitionKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreEventDataStoreResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigTypeDef(TypedDict):
    ApplyToAllRegions: NotRequired[bool]
    AdvancedEventSelectors: NotRequired[List[AdvancedEventSelectorOutputTypeDef]]

class UpdateEventDataStoreResponseTypeDef(TypedDict):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdvancedEventSelectorTypeDef(TypedDict):
    FieldSelectors: Sequence[AdvancedFieldSelectorUnionTypeDef]
    Name: NotRequired[str]

class GetEventSelectorsResponseTypeDef(TypedDict):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventSelectorsResponseTypeDef(TypedDict):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventSelectorTypeDef(TypedDict):
    ReadWriteType: NotRequired[ReadWriteTypeType]
    IncludeManagementEvents: NotRequired[bool]
    DataResources: NotRequired[Sequence[DataResourceUnionTypeDef]]
    ExcludeManagementEventSources: NotRequired[Sequence[str]]

class LookupEventsResponseTypeDef(TypedDict):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetImportResponseTypeDef(TypedDict):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSourceTypeDef
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ImportStatistics: ImportStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportRequestTypeDef(TypedDict):
    Destinations: NotRequired[Sequence[str]]
    ImportSource: NotRequired[ImportSourceTypeDef]
    StartEventTime: NotRequired[TimestampTypeDef]
    EndEventTime: NotRequired[TimestampTypeDef]
    ImportId: NotRequired[str]

class StartImportResponseTypeDef(TypedDict):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSourceTypeDef
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopImportResponseTypeDef(TypedDict):
    ImportId: str
    ImportSource: ImportSourceTypeDef
    Destinations: List[str]
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatistics: ImportStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDashboardRequestTypeDef(TypedDict):
    Name: str
    RefreshSchedule: NotRequired[RefreshScheduleTypeDef]
    TagsList: NotRequired[Sequence[TagTypeDef]]
    TerminationProtectionEnabled: NotRequired[bool]
    Widgets: NotRequired[Sequence[RequestWidgetTypeDef]]

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "DashboardArn": str,
        "Name": str,
        "Type": DashboardTypeType,
        "Widgets": List[WidgetTypeDef],
        "TagsList": List[TagTypeDef],
        "RefreshSchedule": RefreshScheduleTypeDef,
        "TerminationProtectionEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDashboardResponseTypeDef = TypedDict(
    "GetDashboardResponseTypeDef",
    {
        "DashboardArn": str,
        "Type": DashboardTypeType,
        "Status": DashboardStatusType,
        "Widgets": List[WidgetTypeDef],
        "RefreshSchedule": RefreshScheduleTypeDef,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "LastRefreshId": str,
        "LastRefreshFailureReason": str,
        "TerminationProtectionEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateDashboardRequestTypeDef(TypedDict):
    DashboardId: str
    Widgets: NotRequired[Sequence[RequestWidgetTypeDef]]
    RefreshSchedule: NotRequired[RefreshScheduleTypeDef]
    TerminationProtectionEnabled: NotRequired[bool]

UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "DashboardArn": str,
        "Name": str,
        "Type": DashboardTypeType,
        "Widgets": List[WidgetTypeDef],
        "RefreshSchedule": RefreshScheduleTypeDef,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListEventDataStoresResponseTypeDef(TypedDict):
    EventDataStores: List[EventDataStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetChannelResponseTypeDef(TypedDict):
    ChannelArn: str
    Name: str
    Source: str
    SourceConfig: SourceConfigTypeDef
    Destinations: List[DestinationTypeDef]
    IngestionStatus: IngestionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

AdvancedEventSelectorUnionTypeDef = Union[
    AdvancedEventSelectorTypeDef, AdvancedEventSelectorOutputTypeDef
]
EventSelectorUnionTypeDef = Union[EventSelectorTypeDef, EventSelectorOutputTypeDef]

class CreateEventDataStoreRequestTypeDef(TypedDict):
    Name: str
    AdvancedEventSelectors: NotRequired[Sequence[AdvancedEventSelectorUnionTypeDef]]
    MultiRegionEnabled: NotRequired[bool]
    OrganizationEnabled: NotRequired[bool]
    RetentionPeriod: NotRequired[int]
    TerminationProtectionEnabled: NotRequired[bool]
    TagsList: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    StartIngestion: NotRequired[bool]
    BillingMode: NotRequired[BillingModeType]

class UpdateEventDataStoreRequestTypeDef(TypedDict):
    EventDataStore: str
    Name: NotRequired[str]
    AdvancedEventSelectors: NotRequired[Sequence[AdvancedEventSelectorUnionTypeDef]]
    MultiRegionEnabled: NotRequired[bool]
    OrganizationEnabled: NotRequired[bool]
    RetentionPeriod: NotRequired[int]
    TerminationProtectionEnabled: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    BillingMode: NotRequired[BillingModeType]

class PutEventSelectorsRequestTypeDef(TypedDict):
    TrailName: str
    EventSelectors: NotRequired[Sequence[EventSelectorUnionTypeDef]]
    AdvancedEventSelectors: NotRequired[Sequence[AdvancedEventSelectorUnionTypeDef]]
