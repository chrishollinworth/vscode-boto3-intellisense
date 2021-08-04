"""
Type annotations for ssm-incidents service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_incidents.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
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
    "ActionTypeDef",
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "ChatChannelTypeDef",
    "ConditionTypeDef",
    "CreateReplicationSetInputRequestTypeDef",
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanInputRequestTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventInputRequestTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "DeleteIncidentRecordInputRequestTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteResponsePlanInputRequestTypeDef",
    "DeleteTimelineEventInputRequestTypeDef",
    "EventSummaryTypeDef",
    "FilterTypeDef",
    "GetIncidentRecordInputRequestTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "GetReplicationSetInputRequestTypeDef",
    "GetReplicationSetOutputTypeDef",
    "GetResourcePoliciesInputRequestTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "GetResponsePlanInputRequestTypeDef",
    "GetResponsePlanOutputTypeDef",
    "GetTimelineEventInputRequestTypeDef",
    "GetTimelineEventOutputTypeDef",
    "IncidentRecordSourceTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateTypeDef",
    "ItemIdentifierTypeDef",
    "ItemValueTypeDef",
    "ListIncidentRecordsInputRequestTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "ListRelatedItemsInputRequestTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "ListReplicationSetsInputRequestTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListResponsePlansInputRequestTypeDef",
    "ListResponsePlansOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimelineEventsInputRequestTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "NotificationTargetItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegionInfoTypeDef",
    "RegionMapInputValueTypeDef",
    "RelatedItemTypeDef",
    "RelatedItemsUpdateTypeDef",
    "ReplicationSetTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePlanSummaryTypeDef",
    "SsmAutomationTypeDef",
    "StartIncidentInputRequestTypeDef",
    "StartIncidentOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimelineEventTypeDef",
    "TriggerDetailsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeletionProtectionInputRequestTypeDef",
    "UpdateIncidentRecordInputRequestTypeDef",
    "UpdateRelatedItemsInputRequestTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "UpdateReplicationSetInputRequestTypeDef",
    "UpdateResponsePlanInputRequestTypeDef",
    "UpdateTimelineEventInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ssmAutomation": "SsmAutomationTypeDef",
    },
    total=False,
)

_RequiredAddRegionActionTypeDef = TypedDict(
    "_RequiredAddRegionActionTypeDef",
    {
        "regionName": str,
    },
)
_OptionalAddRegionActionTypeDef = TypedDict(
    "_OptionalAddRegionActionTypeDef",
    {
        "sseKmsKeyId": str,
    },
    total=False,
)

class AddRegionActionTypeDef(_RequiredAddRegionActionTypeDef, _OptionalAddRegionActionTypeDef):
    pass

AttributeValueListTypeDef = TypedDict(
    "AttributeValueListTypeDef",
    {
        "integerValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "ssmExecutionArn": str,
    },
    total=False,
)

ChatChannelTypeDef = TypedDict(
    "ChatChannelTypeDef",
    {
        "chatbotSns": List[str],
        "empty": Dict[str, Any],
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "after": Union[datetime, str],
        "before": Union[datetime, str],
        "equals": "AttributeValueListTypeDef",
    },
    total=False,
)

_RequiredCreateReplicationSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationSetInputRequestTypeDef",
    {
        "regions": Dict[str, "RegionMapInputValueTypeDef"],
    },
)
_OptionalCreateReplicationSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationSetInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateReplicationSetInputRequestTypeDef(
    _RequiredCreateReplicationSetInputRequestTypeDef,
    _OptionalCreateReplicationSetInputRequestTypeDef,
):
    pass

CreateReplicationSetOutputTypeDef = TypedDict(
    "CreateReplicationSetOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResponsePlanInputRequestTypeDef = TypedDict(
    "_RequiredCreateResponsePlanInputRequestTypeDef",
    {
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
    },
)
_OptionalCreateResponsePlanInputRequestTypeDef = TypedDict(
    "_OptionalCreateResponsePlanInputRequestTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "displayName": str,
        "engagements": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateResponsePlanInputRequestTypeDef(
    _RequiredCreateResponsePlanInputRequestTypeDef, _OptionalCreateResponsePlanInputRequestTypeDef
):
    pass

CreateResponsePlanOutputTypeDef = TypedDict(
    "CreateResponsePlanOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTimelineEventInputRequestTypeDef = TypedDict(
    "CreateTimelineEventInputRequestTypeDef",
    {
        "clientToken": str,
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
        "incidentRecordArn": str,
    },
)

CreateTimelineEventOutputTypeDef = TypedDict(
    "CreateTimelineEventOutputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIncidentRecordInputRequestTypeDef = TypedDict(
    "DeleteIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
    },
)

DeleteReplicationSetInputRequestTypeDef = TypedDict(
    "DeleteReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "policyId": str,
        "resourceArn": str,
    },
)

DeleteResponsePlanInputRequestTypeDef = TypedDict(
    "DeleteResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTimelineEventInputRequestTypeDef = TypedDict(
    "DeleteTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

EventSummaryTypeDef = TypedDict(
    "EventSummaryTypeDef",
    {
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "condition": "ConditionTypeDef",
        "key": str,
    },
)

GetIncidentRecordInputRequestTypeDef = TypedDict(
    "GetIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetIncidentRecordOutputTypeDef = TypedDict(
    "GetIncidentRecordOutputTypeDef",
    {
        "incidentRecord": "IncidentRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationSetInputRequestTypeDef = TypedDict(
    "GetReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetReplicationSetOutputTypeDef = TypedDict(
    "GetReplicationSetOutputTypeDef",
    {
        "replicationSet": "ReplicationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePoliciesInputRequestTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetResourcePoliciesInputRequestTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetResourcePoliciesInputRequestTypeDef(
    _RequiredGetResourcePoliciesInputRequestTypeDef, _OptionalGetResourcePoliciesInputRequestTypeDef
):
    pass

GetResourcePoliciesOutputTypeDef = TypedDict(
    "GetResourcePoliciesOutputTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponsePlanInputRequestTypeDef = TypedDict(
    "GetResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetResponsePlanOutputTypeDef = TypedDict(
    "GetResponsePlanOutputTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "arn": str,
        "chatChannel": "ChatChannelTypeDef",
        "displayName": str,
        "engagements": List[str],
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTimelineEventInputRequestTypeDef = TypedDict(
    "GetTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

GetTimelineEventOutputTypeDef = TypedDict(
    "GetTimelineEventOutputTypeDef",
    {
        "event": "TimelineEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIncidentRecordSourceTypeDef = TypedDict(
    "_RequiredIncidentRecordSourceTypeDef",
    {
        "createdBy": str,
        "source": str,
    },
)
_OptionalIncidentRecordSourceTypeDef = TypedDict(
    "_OptionalIncidentRecordSourceTypeDef",
    {
        "invokedBy": str,
        "resourceArn": str,
    },
    total=False,
)

class IncidentRecordSourceTypeDef(
    _RequiredIncidentRecordSourceTypeDef, _OptionalIncidentRecordSourceTypeDef
):
    pass

_RequiredIncidentRecordSummaryTypeDef = TypedDict(
    "_RequiredIncidentRecordSummaryTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordSummaryTypeDef = TypedDict(
    "_OptionalIncidentRecordSummaryTypeDef",
    {
        "resolvedTime": datetime,
    },
    total=False,
)

class IncidentRecordSummaryTypeDef(
    _RequiredIncidentRecordSummaryTypeDef, _OptionalIncidentRecordSummaryTypeDef
):
    pass

_RequiredIncidentRecordTypeDef = TypedDict(
    "_RequiredIncidentRecordTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "dedupeString": str,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordTypeDef = TypedDict(
    "_OptionalIncidentRecordTypeDef",
    {
        "automationExecutions": List["AutomationExecutionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "resolvedTime": datetime,
        "summary": str,
    },
    total=False,
)

class IncidentRecordTypeDef(_RequiredIncidentRecordTypeDef, _OptionalIncidentRecordTypeDef):
    pass

_RequiredIncidentTemplateTypeDef = TypedDict(
    "_RequiredIncidentTemplateTypeDef",
    {
        "impact": int,
        "title": str,
    },
)
_OptionalIncidentTemplateTypeDef = TypedDict(
    "_OptionalIncidentTemplateTypeDef",
    {
        "dedupeString": str,
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "summary": str,
    },
    total=False,
)

class IncidentTemplateTypeDef(_RequiredIncidentTemplateTypeDef, _OptionalIncidentTemplateTypeDef):
    pass

ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": "ItemValueTypeDef",
    },
)

ItemValueTypeDef = TypedDict(
    "ItemValueTypeDef",
    {
        "arn": str,
        "metricDefinition": str,
        "url": str,
    },
    total=False,
)

ListIncidentRecordsInputRequestTypeDef = TypedDict(
    "ListIncidentRecordsInputRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListIncidentRecordsOutputTypeDef = TypedDict(
    "ListIncidentRecordsOutputTypeDef",
    {
        "incidentRecordSummaries": List["IncidentRecordSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRelatedItemsInputRequestTypeDef = TypedDict(
    "_RequiredListRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListRelatedItemsInputRequestTypeDef = TypedDict(
    "_OptionalListRelatedItemsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListRelatedItemsInputRequestTypeDef(
    _RequiredListRelatedItemsInputRequestTypeDef, _OptionalListRelatedItemsInputRequestTypeDef
):
    pass

ListRelatedItemsOutputTypeDef = TypedDict(
    "ListRelatedItemsOutputTypeDef",
    {
        "nextToken": str,
        "relatedItems": List["RelatedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplicationSetsInputRequestTypeDef = TypedDict(
    "ListReplicationSetsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListReplicationSetsOutputTypeDef = TypedDict(
    "ListReplicationSetsOutputTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResponsePlansInputRequestTypeDef = TypedDict(
    "ListResponsePlansInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListResponsePlansOutputTypeDef = TypedDict(
    "ListResponsePlansOutputTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List["ResponsePlanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTimelineEventsInputRequestTypeDef = TypedDict(
    "_RequiredListTimelineEventsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListTimelineEventsInputRequestTypeDef = TypedDict(
    "_OptionalListTimelineEventsInputRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["EVENT_TIME"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

class ListTimelineEventsInputRequestTypeDef(
    _RequiredListTimelineEventsInputRequestTypeDef, _OptionalListTimelineEventsInputRequestTypeDef
):
    pass

ListTimelineEventsOutputTypeDef = TypedDict(
    "ListTimelineEventsOutputTypeDef",
    {
        "eventSummaries": List["EventSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationTargetItemTypeDef = TypedDict(
    "NotificationTargetItemTypeDef",
    {
        "snsTopicArn": str,
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

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "policyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegionInfoTypeDef = TypedDict(
    "_RequiredRegionInfoTypeDef",
    {
        "status": RegionStatusType,
        "statusUpdateDateTime": datetime,
    },
)
_OptionalRegionInfoTypeDef = TypedDict(
    "_OptionalRegionInfoTypeDef",
    {
        "sseKmsKeyId": str,
        "statusMessage": str,
    },
    total=False,
)

class RegionInfoTypeDef(_RequiredRegionInfoTypeDef, _OptionalRegionInfoTypeDef):
    pass

RegionMapInputValueTypeDef = TypedDict(
    "RegionMapInputValueTypeDef",
    {
        "sseKmsKeyId": str,
    },
    total=False,
)

_RequiredRelatedItemTypeDef = TypedDict(
    "_RequiredRelatedItemTypeDef",
    {
        "identifier": "ItemIdentifierTypeDef",
    },
)
_OptionalRelatedItemTypeDef = TypedDict(
    "_OptionalRelatedItemTypeDef",
    {
        "title": str,
    },
    total=False,
)

class RelatedItemTypeDef(_RequiredRelatedItemTypeDef, _OptionalRelatedItemTypeDef):
    pass

RelatedItemsUpdateTypeDef = TypedDict(
    "RelatedItemsUpdateTypeDef",
    {
        "itemToAdd": "RelatedItemTypeDef",
        "itemToRemove": "ItemIdentifierTypeDef",
    },
    total=False,
)

ReplicationSetTypeDef = TypedDict(
    "ReplicationSetTypeDef",
    {
        "createdBy": str,
        "createdTime": datetime,
        "deletionProtected": bool,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "regionMap": Dict[str, "RegionInfoTypeDef"],
        "status": ReplicationSetStatusType,
    },
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyDocument": str,
        "policyId": str,
        "ramResourceShareRegion": str,
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

_RequiredResponsePlanSummaryTypeDef = TypedDict(
    "_RequiredResponsePlanSummaryTypeDef",
    {
        "arn": str,
        "name": str,
    },
)
_OptionalResponsePlanSummaryTypeDef = TypedDict(
    "_OptionalResponsePlanSummaryTypeDef",
    {
        "displayName": str,
    },
    total=False,
)

class ResponsePlanSummaryTypeDef(
    _RequiredResponsePlanSummaryTypeDef, _OptionalResponsePlanSummaryTypeDef
):
    pass

_RequiredSsmAutomationTypeDef = TypedDict(
    "_RequiredSsmAutomationTypeDef",
    {
        "documentName": str,
        "roleArn": str,
    },
)
_OptionalSsmAutomationTypeDef = TypedDict(
    "_OptionalSsmAutomationTypeDef",
    {
        "documentVersion": str,
        "parameters": Dict[str, List[str]],
        "targetAccount": SsmTargetAccountType,
    },
    total=False,
)

class SsmAutomationTypeDef(_RequiredSsmAutomationTypeDef, _OptionalSsmAutomationTypeDef):
    pass

_RequiredStartIncidentInputRequestTypeDef = TypedDict(
    "_RequiredStartIncidentInputRequestTypeDef",
    {
        "responsePlanArn": str,
    },
)
_OptionalStartIncidentInputRequestTypeDef = TypedDict(
    "_OptionalStartIncidentInputRequestTypeDef",
    {
        "clientToken": str,
        "impact": int,
        "relatedItems": List["RelatedItemTypeDef"],
        "title": str,
        "triggerDetails": "TriggerDetailsTypeDef",
    },
    total=False,
)

class StartIncidentInputRequestTypeDef(
    _RequiredStartIncidentInputRequestTypeDef, _OptionalStartIncidentInputRequestTypeDef
):
    pass

StartIncidentOutputTypeDef = TypedDict(
    "StartIncidentOutputTypeDef",
    {
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TimelineEventTypeDef = TypedDict(
    "TimelineEventTypeDef",
    {
        "eventData": str,
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

_RequiredTriggerDetailsTypeDef = TypedDict(
    "_RequiredTriggerDetailsTypeDef",
    {
        "source": str,
        "timestamp": Union[datetime, str],
    },
)
_OptionalTriggerDetailsTypeDef = TypedDict(
    "_OptionalTriggerDetailsTypeDef",
    {
        "rawData": str,
        "triggerArn": str,
    },
    total=False,
)

class TriggerDetailsTypeDef(_RequiredTriggerDetailsTypeDef, _OptionalTriggerDetailsTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDeletionProtectionInputRequestTypeDef",
    {
        "arn": str,
        "deletionProtected": bool,
    },
)
_OptionalUpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDeletionProtectionInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateDeletionProtectionInputRequestTypeDef(
    _RequiredUpdateDeletionProtectionInputRequestTypeDef,
    _OptionalUpdateDeletionProtectionInputRequestTypeDef,
):
    pass

_RequiredUpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "_RequiredUpdateIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIncidentRecordInputRequestTypeDef",
    {
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "impact": int,
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "status": IncidentRecordStatusType,
        "summary": str,
        "title": str,
    },
    total=False,
)

class UpdateIncidentRecordInputRequestTypeDef(
    _RequiredUpdateIncidentRecordInputRequestTypeDef,
    _OptionalUpdateIncidentRecordInputRequestTypeDef,
):
    pass

_RequiredUpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "relatedItemsUpdate": "RelatedItemsUpdateTypeDef",
    },
)
_OptionalUpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRelatedItemsInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateRelatedItemsInputRequestTypeDef(
    _RequiredUpdateRelatedItemsInputRequestTypeDef, _OptionalUpdateRelatedItemsInputRequestTypeDef
):
    pass

UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": "AddRegionActionTypeDef",
        "deleteRegionAction": "DeleteRegionActionTypeDef",
    },
    total=False,
)

_RequiredUpdateReplicationSetInputRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationSetInputRequestTypeDef",
    {
        "actions": List["UpdateReplicationSetActionTypeDef"],
        "arn": str,
    },
)
_OptionalUpdateReplicationSetInputRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationSetInputRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateReplicationSetInputRequestTypeDef(
    _RequiredUpdateReplicationSetInputRequestTypeDef,
    _OptionalUpdateReplicationSetInputRequestTypeDef,
):
    pass

_RequiredUpdateResponsePlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdateResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateResponsePlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdateResponsePlanInputRequestTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "displayName": str,
        "engagements": List[str],
        "incidentTemplateDedupeString": str,
        "incidentTemplateImpact": int,
        "incidentTemplateNotificationTargets": List["NotificationTargetItemTypeDef"],
        "incidentTemplateSummary": str,
        "incidentTemplateTitle": str,
    },
    total=False,
)

class UpdateResponsePlanInputRequestTypeDef(
    _RequiredUpdateResponsePlanInputRequestTypeDef, _OptionalUpdateResponsePlanInputRequestTypeDef
):
    pass

_RequiredUpdateTimelineEventInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTimelineEventInputRequestTypeDef",
    {
        "clientToken": str,
        "eventId": str,
        "incidentRecordArn": str,
    },
)
_OptionalUpdateTimelineEventInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTimelineEventInputRequestTypeDef",
    {
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
    },
    total=False,
)

class UpdateTimelineEventInputRequestTypeDef(
    _RequiredUpdateTimelineEventInputRequestTypeDef, _OptionalUpdateTimelineEventInputRequestTypeDef
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
