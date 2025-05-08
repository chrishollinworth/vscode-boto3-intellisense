"""
Type annotations for codestar-notifications service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import TargetTypeDef

    data: TargetTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    DetailTypeType,
    ListEventTypesFilterNameType,
    ListNotificationRulesFilterNameType,
    ListTargetsFilterNameType,
    NotificationRuleStatusType,
    TargetStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateNotificationRuleRequestTypeDef",
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleRequestTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "DeleteTargetRequestTypeDef",
    "DescribeNotificationRuleRequestTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "EventTypeSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesRequestPaginateTypeDef",
    "ListEventTypesRequestTypeDef",
    "ListEventTypesResultTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesRequestPaginateTypeDef",
    "ListNotificationRulesRequestTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsRequestPaginateTypeDef",
    "ListTargetsRequestTypeDef",
    "ListTargetsResultTypeDef",
    "NotificationRuleSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SubscribeRequestTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResultTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UnsubscribeRequestTypeDef",
    "UnsubscribeResultTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateNotificationRuleRequestTypeDef",
)

class TargetTypeDef(TypedDict):
    TargetType: NotRequired[str]
    TargetAddress: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteNotificationRuleRequestTypeDef(TypedDict):
    Arn: str

class DeleteTargetRequestTypeDef(TypedDict):
    TargetAddress: str
    ForceUnsubscribeAll: NotRequired[bool]

class DescribeNotificationRuleRequestTypeDef(TypedDict):
    Arn: str

EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {
        "EventTypeId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "EventTypeName": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

class TargetSummaryTypeDef(TypedDict):
    TargetAddress: NotRequired[str]
    TargetType: NotRequired[str]
    TargetStatus: NotRequired[TargetStatusType]

class ListEventTypesFilterTypeDef(TypedDict):
    Name: ListEventTypesFilterNameType
    Value: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListNotificationRulesFilterTypeDef(TypedDict):
    Name: ListNotificationRulesFilterNameType
    Value: str

class NotificationRuleSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    Arn: str

class ListTargetsFilterTypeDef(TypedDict):
    Name: ListTargetsFilterNameType
    Value: str

class TagResourceRequestTypeDef(TypedDict):
    Arn: str
    Tags: Mapping[str, str]

class UnsubscribeRequestTypeDef(TypedDict):
    Arn: str
    TargetAddress: str

class UntagResourceRequestTypeDef(TypedDict):
    Arn: str
    TagKeys: Sequence[str]

class CreateNotificationRuleRequestTypeDef(TypedDict):
    Name: str
    EventTypeIds: Sequence[str]
    Resource: str
    Targets: Sequence[TargetTypeDef]
    DetailType: DetailTypeType
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    Status: NotRequired[NotificationRuleStatusType]

class SubscribeRequestTypeDef(TypedDict):
    Arn: str
    Target: TargetTypeDef
    ClientRequestToken: NotRequired[str]

class UpdateNotificationRuleRequestTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Status: NotRequired[NotificationRuleStatusType]
    EventTypeIds: NotRequired[Sequence[str]]
    Targets: NotRequired[Sequence[TargetTypeDef]]
    DetailType: NotRequired[DetailTypeType]

class CreateNotificationRuleResultTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNotificationRuleResultTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResultTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResultTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnsubscribeResultTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTypesResultTypeDef(TypedDict):
    EventTypes: List[EventTypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeNotificationRuleResultTypeDef(TypedDict):
    Arn: str
    Name: str
    EventTypes: List[EventTypeSummaryTypeDef]
    Resource: str
    Targets: List[TargetSummaryTypeDef]
    DetailType: DetailTypeType
    CreatedBy: str
    Status: NotificationRuleStatusType
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsResultTypeDef(TypedDict):
    Targets: List[TargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEventTypesRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListEventTypesFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventTypesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListEventTypesFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationRulesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListNotificationRulesFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationRulesRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListNotificationRulesFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListNotificationRulesResultTypeDef(TypedDict):
    NotificationRules: List[NotificationRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTargetsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListTargetsFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ListTargetsFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
