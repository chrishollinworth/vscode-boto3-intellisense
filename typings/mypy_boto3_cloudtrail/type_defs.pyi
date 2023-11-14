"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import AddTagsRequestRequestTypeDef

    data: AddTagsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DeliveryStatusType,
    DestinationTypeType,
    EventDataStoreStatusType,
    ImportFailureStatusType,
    ImportStatusType,
    InsightTypeType,
    LookupAttributeKeyType,
    QueryStatusType,
    ReadWriteTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddTagsRequestRequestTypeDef",
    "AdvancedEventSelectorTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CancelQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateEventDataStoreRequestRequestTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "CreateTrailRequestRequestTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventDataStoreRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "DescribeQueryRequestRequestTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "DescribeTrailsResponseTypeDef",
    "DestinationTypeDef",
    "EventDataStoreTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetChannelRequestRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetEventDataStoreRequestRequestTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetImportRequestRequestTypeDef",
    "GetImportResponseTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "ImportFailureListItemTypeDef",
    "ImportSourceTypeDef",
    "ImportStatisticsTypeDef",
    "ImportsListItemTypeDef",
    "IngestionStatusTypeDef",
    "InsightSelectorTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListEventDataStoresRequestRequestTypeDef",
    "ListEventDataStoresResponseTypeDef",
    "ListImportFailuresRequestRequestTypeDef",
    "ListImportFailuresResponseTypeDef",
    "ListImportsRequestRequestTypeDef",
    "ListImportsResponseTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListQueriesRequestRequestTypeDef",
    "ListQueriesResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListTrailsRequestRequestTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupAttributeTypeDef",
    "LookupEventsRequestRequestTypeDef",
    "LookupEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublicKeyTypeDef",
    "PutEventSelectorsRequestRequestTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "PutInsightSelectorsRequestRequestTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "QueryStatisticsForDescribeQueryTypeDef",
    "QueryStatisticsTypeDef",
    "QueryTypeDef",
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreEventDataStoreRequestRequestTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "S3ImportSourceTypeDef",
    "SourceConfigTypeDef",
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    "StopImportRequestRequestTypeDef",
    "StopImportResponseTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateEventDataStoreRequestRequestTypeDef",
    "UpdateEventDataStoreResponseTypeDef",
    "UpdateTrailRequestRequestTypeDef",
    "UpdateTrailResponseTypeDef",
)

AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": List["TagTypeDef"],
    },
)

_RequiredAdvancedEventSelectorTypeDef = TypedDict(
    "_RequiredAdvancedEventSelectorTypeDef",
    {
        "FieldSelectors": List["AdvancedFieldSelectorTypeDef"],
    },
)
_OptionalAdvancedEventSelectorTypeDef = TypedDict(
    "_OptionalAdvancedEventSelectorTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class AdvancedEventSelectorTypeDef(
    _RequiredAdvancedEventSelectorTypeDef, _OptionalAdvancedEventSelectorTypeDef
):
    pass

_RequiredAdvancedFieldSelectorTypeDef = TypedDict(
    "_RequiredAdvancedFieldSelectorTypeDef",
    {
        "Field": str,
    },
)
_OptionalAdvancedFieldSelectorTypeDef = TypedDict(
    "_OptionalAdvancedFieldSelectorTypeDef",
    {
        "Equals": List[str],
        "StartsWith": List[str],
        "EndsWith": List[str],
        "NotEquals": List[str],
        "NotStartsWith": List[str],
        "NotEndsWith": List[str],
    },
    total=False,
)

class AdvancedFieldSelectorTypeDef(
    _RequiredAdvancedFieldSelectorTypeDef, _OptionalAdvancedFieldSelectorTypeDef
):
    pass

_RequiredCancelQueryRequestRequestTypeDef = TypedDict(
    "_RequiredCancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
_OptionalCancelQueryRequestRequestTypeDef = TypedDict(
    "_OptionalCancelQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
    total=False,
)

class CancelQueryRequestRequestTypeDef(
    _RequiredCancelQueryRequestRequestTypeDef, _OptionalCancelQueryRequestRequestTypeDef
):
    pass

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
    },
    total=False,
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "Name": str,
        "Source": str,
        "Destinations": List["DestinationTypeDef"],
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List["DestinationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventDataStoreRequestRequestTypeDef",
    {
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": List["TagTypeDef"],
        "KmsKeyId": str,
        "StartIngestion": bool,
    },
    total=False,
)

class CreateEventDataStoreRequestRequestTypeDef(
    _RequiredCreateEventDataStoreRequestRequestTypeDef,
    _OptionalCreateEventDataStoreRequestRequestTypeDef,
):
    pass

CreateEventDataStoreResponseTypeDef = TypedDict(
    "CreateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrailRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
    },
)
_OptionalCreateTrailRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrailRequestRequestTypeDef",
    {
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrailRequestRequestTypeDef(
    _RequiredCreateTrailRequestRequestTypeDef, _OptionalCreateTrailRequestRequestTypeDef
):
    pass

CreateTrailResponseTypeDef = TypedDict(
    "CreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": str,
        "Values": List[str],
    },
    total=False,
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)

DeleteEventDataStoreRequestRequestTypeDef = TypedDict(
    "DeleteEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeregisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
    },
)

DescribeQueryRequestRequestTypeDef = TypedDict(
    "DescribeQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
        "QueryAlias": str,
    },
    total=False,
)

DescribeQueryResponseTypeDef = TypedDict(
    "DescribeQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryString": str,
        "QueryStatus": QueryStatusType,
        "QueryStatistics": "QueryStatisticsForDescribeQueryTypeDef",
        "ErrorMessage": str,
        "DeliveryS3Uri": str,
        "DeliveryStatus": DeliveryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrailsRequestRequestTypeDef = TypedDict(
    "DescribeTrailsRequestRequestTypeDef",
    {
        "trailNameList": List[str],
        "includeShadowTrails": bool,
    },
    total=False,
)

DescribeTrailsResponseTypeDef = TypedDict(
    "DescribeTrailsResponseTypeDef",
    {
        "trailList": List["TrailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Type": DestinationTypeType,
        "Location": str,
    },
)

EventDataStoreTypeDef = TypedDict(
    "EventDataStoreTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "TerminationProtectionEnabled": bool,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

EventSelectorTypeDef = TypedDict(
    "EventSelectorTypeDef",
    {
        "ReadWriteType": ReadWriteTypeType,
        "IncludeManagementEvents": bool,
        "DataResources": List["DataResourceTypeDef"],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List["ResourceTypeDef"],
        "CloudTrailEvent": str,
    },
    total=False,
)

GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "SourceConfig": "SourceConfigTypeDef",
        "Destinations": List["DestinationTypeDef"],
        "IngestionStatus": "IngestionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventDataStoreRequestRequestTypeDef = TypedDict(
    "GetEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

GetEventDataStoreResponseTypeDef = TypedDict(
    "GetEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSelectorsRequestRequestTypeDef = TypedDict(
    "GetEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetEventSelectorsResponseTypeDef = TypedDict(
    "GetEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)

GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": "ImportSourceTypeDef",
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ImportStatistics": "ImportStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightSelectorsRequestRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "EventDataStore": str,
    },
    total=False,
)

GetInsightSelectorsResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "EventDataStoreArn": str,
        "InsightsDestination": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
_OptionalGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "NextToken": str,
        "MaxQueryResults": int,
    },
    total=False,
)

class GetQueryResultsRequestRequestTypeDef(
    _RequiredGetQueryResultsRequestRequestTypeDef, _OptionalGetQueryResultsRequestRequestTypeDef
):
    pass

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "QueryStatus": QueryStatusType,
        "QueryStatistics": "QueryStatisticsTypeDef",
        "QueryResultRows": List[List[Dict[str, str]]],
        "NextToken": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailRequestRequestTypeDef = TypedDict(
    "GetTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailResponseTypeDef = TypedDict(
    "GetTrailResponseTypeDef",
    {
        "Trail": "TrailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailStatusRequestRequestTypeDef = TypedDict(
    "GetTrailStatusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailStatusResponseTypeDef = TypedDict(
    "GetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportFailureListItemTypeDef = TypedDict(
    "ImportFailureListItemTypeDef",
    {
        "Location": str,
        "Status": ImportFailureStatusType,
        "ErrorType": str,
        "ErrorMessage": str,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ImportSourceTypeDef = TypedDict(
    "ImportSourceTypeDef",
    {
        "S3": "S3ImportSourceTypeDef",
    },
)

ImportStatisticsTypeDef = TypedDict(
    "ImportStatisticsTypeDef",
    {
        "PrefixesFound": int,
        "PrefixesCompleted": int,
        "FilesCompleted": int,
        "EventsCompleted": int,
        "FailedEntries": int,
    },
    total=False,
)

ImportsListItemTypeDef = TypedDict(
    "ImportsListItemTypeDef",
    {
        "ImportId": str,
        "ImportStatus": ImportStatusType,
        "Destinations": List[str],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

IngestionStatusTypeDef = TypedDict(
    "IngestionStatusTypeDef",
    {
        "LatestIngestionSuccessTime": datetime,
        "LatestIngestionSuccessEventID": str,
        "LatestIngestionErrorCode": str,
        "LatestIngestionAttemptTime": datetime,
        "LatestIngestionAttemptEventID": str,
    },
    total=False,
)

InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": InsightTypeType,
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventDataStoresRequestRequestTypeDef = TypedDict(
    "ListEventDataStoresRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventDataStoresResponseTypeDef = TypedDict(
    "ListEventDataStoresResponseTypeDef",
    {
        "EventDataStores": List["EventDataStoreTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImportFailuresRequestRequestTypeDef = TypedDict(
    "_RequiredListImportFailuresRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)
_OptionalListImportFailuresRequestRequestTypeDef = TypedDict(
    "_OptionalListImportFailuresRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListImportFailuresRequestRequestTypeDef(
    _RequiredListImportFailuresRequestRequestTypeDef,
    _OptionalListImportFailuresRequestRequestTypeDef,
):
    pass

ListImportFailuresResponseTypeDef = TypedDict(
    "ListImportFailuresResponseTypeDef",
    {
        "Failures": List["ImportFailureListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "Destination": str,
        "ImportStatus": ImportStatusType,
        "NextToken": str,
    },
    total=False,
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "Imports": List["ImportsListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
    },
    total=False,
)

ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "PublicKeyList": List["PublicKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueriesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueriesRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
_OptionalListQueriesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "QueryStatus": QueryStatusType,
    },
    total=False,
)

class ListQueriesRequestRequestTypeDef(
    _RequiredListQueriesRequestRequestTypeDef, _OptionalListQueriesRequestRequestTypeDef
):
    pass

ListQueriesResponseTypeDef = TypedDict(
    "ListQueriesResponseTypeDef",
    {
        "Queries": List["QueryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "ResourceIdList": List[str],
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "ResourceTagList": List["ResourceTagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrailsRequestRequestTypeDef = TypedDict(
    "ListTrailsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListTrailsResponseTypeDef = TypedDict(
    "ListTrailsResponseTypeDef",
    {
        "Trails": List["TrailInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": LookupAttributeKeyType,
        "AttributeValue": str,
    },
)

LookupEventsRequestRequestTypeDef = TypedDict(
    "LookupEventsRequestRequestTypeDef",
    {
        "LookupAttributes": List["LookupAttributeTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventCategory": Literal["insight"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

LookupEventsResponseTypeDef = TypedDict(
    "LookupEventsResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

_RequiredPutEventSelectorsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)
_OptionalPutEventSelectorsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventSelectorsRequestRequestTypeDef",
    {
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
    },
    total=False,
)

class PutEventSelectorsRequestRequestTypeDef(
    _RequiredPutEventSelectorsRequestRequestTypeDef, _OptionalPutEventSelectorsRequestRequestTypeDef
):
    pass

PutEventSelectorsResponseTypeDef = TypedDict(
    "PutEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "_RequiredPutInsightSelectorsRequestRequestTypeDef",
    {
        "InsightSelectors": List["InsightSelectorTypeDef"],
    },
)
_OptionalPutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "_OptionalPutInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "EventDataStore": str,
        "InsightsDestination": str,
    },
    total=False,
)

class PutInsightSelectorsRequestRequestTypeDef(
    _RequiredPutInsightSelectorsRequestRequestTypeDef,
    _OptionalPutInsightSelectorsRequestRequestTypeDef,
):
    pass

PutInsightSelectorsResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "EventDataStoreArn": str,
        "InsightsDestination": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStatisticsForDescribeQueryTypeDef = TypedDict(
    "QueryStatisticsForDescribeQueryTypeDef",
    {
        "EventsMatched": int,
        "EventsScanned": int,
        "BytesScanned": int,
        "ExecutionTimeInMillis": int,
        "CreationTime": datetime,
    },
    total=False,
)

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "ResultsCount": int,
        "TotalResultsCount": int,
        "BytesScanned": int,
    },
    total=False,
)

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "CreationTime": datetime,
    },
    total=False,
)

RegisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "MemberAccountId": str,
    },
)

RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": List["TagTypeDef"],
    },
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceId": str,
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceName": str,
    },
    total=False,
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

RestoreEventDataStoreRequestRequestTypeDef = TypedDict(
    "RestoreEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

RestoreEventDataStoreResponseTypeDef = TypedDict(
    "RestoreEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ImportSourceTypeDef = TypedDict(
    "S3ImportSourceTypeDef",
    {
        "S3LocationUri": str,
        "S3BucketRegion": str,
        "S3BucketAccessRoleArn": str,
    },
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "ApplyToAllRegions": bool,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
    },
    total=False,
)

StartEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "Destinations": List[str],
        "ImportSource": "ImportSourceTypeDef",
        "StartEventTime": Union[datetime, str],
        "EndEventTime": Union[datetime, str],
        "ImportId": str,
    },
    total=False,
)

StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": "ImportSourceTypeDef",
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLoggingRequestRequestTypeDef = TypedDict(
    "StartLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartQueryRequestRequestTypeDef = TypedDict(
    "StartQueryRequestRequestTypeDef",
    {
        "QueryStatement": str,
        "DeliveryS3Uri": str,
        "QueryAlias": str,
        "QueryParameters": List[str],
    },
    total=False,
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

StopImportRequestRequestTypeDef = TypedDict(
    "StopImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)

StopImportResponseTypeDef = TypedDict(
    "StopImportResponseTypeDef",
    {
        "ImportId": str,
        "ImportSource": "ImportSourceTypeDef",
        "Destinations": List[str],
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatistics": "ImportStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopLoggingRequestRequestTypeDef = TypedDict(
    "StopLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef",
    {
        "TrailARN": str,
        "Name": str,
        "HomeRegion": str,
    },
    total=False,
)

TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Destinations": List["DestinationTypeDef"],
        "Name": str,
    },
    total=False,
)

class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List["DestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
_OptionalUpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

class UpdateEventDataStoreRequestRequestTypeDef(
    _RequiredUpdateEventDataStoreRequestRequestTypeDef,
    _OptionalUpdateEventDataStoreRequestRequestTypeDef,
):
    pass

UpdateEventDataStoreResponseTypeDef = TypedDict(
    "UpdateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrailRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateTrailRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrailRequestRequestTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

class UpdateTrailRequestRequestTypeDef(
    _RequiredUpdateTrailRequestRequestTypeDef, _OptionalUpdateTrailRequestRequestTypeDef
):
    pass

UpdateTrailResponseTypeDef = TypedDict(
    "UpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
