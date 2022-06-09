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
    EventDataStoreStatusType,
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
    "CreateEventDataStoreRequestRequestTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "CreateTrailRequestRequestTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceTypeDef",
    "DeleteEventDataStoreRequestRequestTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DescribeQueryRequestRequestTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "DescribeTrailsResponseTypeDef",
    "EventDataStoreTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetEventDataStoreRequestRequestTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "InsightSelectorTypeDef",
    "ListEventDataStoresRequestRequestTypeDef",
    "ListEventDataStoresResponseTypeDef",
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
    "QueryStatisticsForDescribeQueryTypeDef",
    "QueryStatisticsTypeDef",
    "QueryTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreEventDataStoreRequestRequestTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
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

CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
    },
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
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

DeleteEventDataStoreRequestRequestTypeDef = TypedDict(
    "DeleteEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeQueryRequestRequestTypeDef = TypedDict(
    "DescribeQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
    },
)

DescribeQueryResponseTypeDef = TypedDict(
    "DescribeQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryString": str,
        "QueryStatus": QueryStatusType,
        "QueryStatistics": "QueryStatisticsForDescribeQueryTypeDef",
        "ErrorMessage": str,
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

GetInsightSelectorsRequestRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetInsightSelectorsResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
    },
)
_OptionalGetQueryResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsRequestRequestTypeDef",
    {
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

InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": InsightTypeType,
    },
    total=False,
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

PutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "PutInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
    },
)

PutInsightSelectorsResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
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
    },
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "QueryId": str,
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
