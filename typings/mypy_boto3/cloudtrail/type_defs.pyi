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

from .literals import LookupAttributeKeyType, ReadWriteTypeType

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
    "CreateTrailRequestRequestTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "DescribeTrailsResponseTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "InsightSelectorTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
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
    "RemoveTagsRequestRequestTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateTrailRequestRequestTypeDef",
    "UpdateTrailResponseTypeDef",
)

_RequiredAddTagsRequestRequestTypeDef = TypedDict(
    "_RequiredAddTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalAddTagsRequestRequestTypeDef = TypedDict(
    "_OptionalAddTagsRequestRequestTypeDef",
    {
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)

class AddTagsRequestRequestTypeDef(
    _RequiredAddTagsRequestRequestTypeDef, _OptionalAddTagsRequestRequestTypeDef
):
    pass

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

DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
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
        "InsightType": Literal["ApiCallRateInsight"],
    },
    total=False,
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

_RequiredRemoveTagsRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalRemoveTagsRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveTagsRequestRequestTypeDef",
    {
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)

class RemoveTagsRequestRequestTypeDef(
    _RequiredRemoveTagsRequestRequestTypeDef, _OptionalRemoveTagsRequestRequestTypeDef
):
    pass

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

StartLoggingRequestRequestTypeDef = TypedDict(
    "StartLoggingRequestRequestTypeDef",
    {
        "Name": str,
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
