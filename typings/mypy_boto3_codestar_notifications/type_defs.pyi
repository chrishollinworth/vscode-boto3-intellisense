"""
Type annotations for codestar-notifications service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import CreateNotificationRuleRequestRequestTypeDef

    data: CreateNotificationRuleRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DetailTypeType,
    ListEventTypesFilterNameType,
    ListNotificationRulesFilterNameType,
    ListTargetsFilterNameType,
    NotificationRuleStatusType,
    TargetStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateNotificationRuleRequestRequestTypeDef",
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleRequestRequestTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "DeleteTargetRequestRequestTypeDef",
    "DescribeNotificationRuleRequestRequestTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "EventTypeSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesRequestRequestTypeDef",
    "ListEventTypesResultTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesRequestRequestTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsRequestRequestTypeDef",
    "ListTargetsResultTypeDef",
    "NotificationRuleSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SubscribeRequestRequestTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResultTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UnsubscribeRequestRequestTypeDef",
    "UnsubscribeResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateNotificationRuleRequestRequestTypeDef",
)

_RequiredCreateNotificationRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNotificationRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventTypeIds": List[str],
        "Resource": str,
        "Targets": List["TargetTypeDef"],
        "DetailType": DetailTypeType,
    },
)
_OptionalCreateNotificationRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNotificationRuleRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Dict[str, str],
        "Status": NotificationRuleStatusType,
    },
    total=False,
)

class CreateNotificationRuleRequestRequestTypeDef(
    _RequiredCreateNotificationRuleRequestRequestTypeDef,
    _OptionalCreateNotificationRuleRequestRequestTypeDef,
):
    pass

CreateNotificationRuleResultTypeDef = TypedDict(
    "CreateNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNotificationRuleRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteNotificationRuleResultTypeDef = TypedDict(
    "DeleteNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTargetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTargetRequestRequestTypeDef",
    {
        "TargetAddress": str,
    },
)
_OptionalDeleteTargetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTargetRequestRequestTypeDef",
    {
        "ForceUnsubscribeAll": bool,
    },
    total=False,
)

class DeleteTargetRequestRequestTypeDef(
    _RequiredDeleteTargetRequestRequestTypeDef, _OptionalDeleteTargetRequestRequestTypeDef
):
    pass

DescribeNotificationRuleRequestRequestTypeDef = TypedDict(
    "DescribeNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeNotificationRuleResultTypeDef = TypedDict(
    "DescribeNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "Resource": str,
        "Targets": List["TargetSummaryTypeDef"],
        "DetailType": DetailTypeType,
        "CreatedBy": str,
        "Status": NotificationRuleStatusType,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {
        "EventTypeId": str,
        "ServiceName": str,
        "EventTypeName": str,
        "ResourceType": str,
    },
    total=False,
)

ListEventTypesFilterTypeDef = TypedDict(
    "ListEventTypesFilterTypeDef",
    {
        "Name": ListEventTypesFilterNameType,
        "Value": str,
    },
)

ListEventTypesRequestRequestTypeDef = TypedDict(
    "ListEventTypesRequestRequestTypeDef",
    {
        "Filters": List["ListEventTypesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventTypesResultTypeDef = TypedDict(
    "ListEventTypesResultTypeDef",
    {
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationRulesFilterTypeDef = TypedDict(
    "ListNotificationRulesFilterTypeDef",
    {
        "Name": ListNotificationRulesFilterNameType,
        "Value": str,
    },
)

ListNotificationRulesRequestRequestTypeDef = TypedDict(
    "ListNotificationRulesRequestRequestTypeDef",
    {
        "Filters": List["ListNotificationRulesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNotificationRulesResultTypeDef = TypedDict(
    "ListNotificationRulesResultTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List["NotificationRuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsFilterTypeDef = TypedDict(
    "ListTargetsFilterTypeDef",
    {
        "Name": ListTargetsFilterNameType,
        "Value": str,
    },
)

ListTargetsRequestRequestTypeDef = TypedDict(
    "ListTargetsRequestRequestTypeDef",
    {
        "Filters": List["ListTargetsFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTargetsResultTypeDef = TypedDict(
    "ListTargetsResultTypeDef",
    {
        "Targets": List["TargetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationRuleSummaryTypeDef = TypedDict(
    "NotificationRuleSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
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

_RequiredSubscribeRequestRequestTypeDef = TypedDict(
    "_RequiredSubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "Target": "TargetTypeDef",
    },
)
_OptionalSubscribeRequestRequestTypeDef = TypedDict(
    "_OptionalSubscribeRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class SubscribeRequestRequestTypeDef(
    _RequiredSubscribeRequestRequestTypeDef, _OptionalSubscribeRequestRequestTypeDef
):
    pass

SubscribeResultTypeDef = TypedDict(
    "SubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
    },
)

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": TargetStatusType,
    },
    total=False,
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "TargetType": str,
        "TargetAddress": str,
    },
    total=False,
)

UnsubscribeRequestRequestTypeDef = TypedDict(
    "UnsubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "TargetAddress": str,
    },
)

UnsubscribeResultTypeDef = TypedDict(
    "UnsubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateNotificationRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateNotificationRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNotificationRuleRequestRequestTypeDef",
    {
        "Name": str,
        "Status": NotificationRuleStatusType,
        "EventTypeIds": List[str],
        "Targets": List["TargetTypeDef"],
        "DetailType": DetailTypeType,
    },
    total=False,
)

class UpdateNotificationRuleRequestRequestTypeDef(
    _RequiredUpdateNotificationRuleRequestRequestTypeDef,
    _OptionalUpdateNotificationRuleRequestRequestTypeDef,
):
    pass
