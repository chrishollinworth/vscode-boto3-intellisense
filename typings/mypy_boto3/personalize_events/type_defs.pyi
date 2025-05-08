"""
Type annotations for personalize-events service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from collections.abc import Sequence
else:
    from typing import Dict, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionInteractionTypeDef",
    "ActionTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventTypeDef",
    "ItemTypeDef",
    "MetricAttributionTypeDef",
    "PutActionInteractionsRequestTypeDef",
    "PutActionsRequestTypeDef",
    "PutEventsRequestTypeDef",
    "PutItemsRequestTypeDef",
    "PutUsersRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "UserTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class ActionTypeDef(TypedDict):
    actionId: str
    properties: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MetricAttributionTypeDef(TypedDict):
    eventAttributionSource: str

class ItemTypeDef(TypedDict):
    itemId: str
    properties: NotRequired[str]

class UserTypeDef(TypedDict):
    userId: str
    properties: NotRequired[str]

class ActionInteractionTypeDef(TypedDict):
    actionId: str
    sessionId: str
    timestamp: TimestampTypeDef
    eventType: str
    userId: NotRequired[str]
    eventId: NotRequired[str]
    recommendationId: NotRequired[str]
    impression: NotRequired[Sequence[str]]
    properties: NotRequired[str]

class PutActionsRequestTypeDef(TypedDict):
    datasetArn: str
    actions: Sequence[ActionTypeDef]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(TypedDict):
    eventType: str
    sentAt: TimestampTypeDef
    eventId: NotRequired[str]
    eventValue: NotRequired[float]
    itemId: NotRequired[str]
    properties: NotRequired[str]
    recommendationId: NotRequired[str]
    impression: NotRequired[Sequence[str]]
    metricAttribution: NotRequired[MetricAttributionTypeDef]

class PutItemsRequestTypeDef(TypedDict):
    datasetArn: str
    items: Sequence[ItemTypeDef]

class PutUsersRequestTypeDef(TypedDict):
    datasetArn: str
    users: Sequence[UserTypeDef]

class PutActionInteractionsRequestTypeDef(TypedDict):
    trackingId: str
    actionInteractions: Sequence[ActionInteractionTypeDef]

class PutEventsRequestTypeDef(TypedDict):
    trackingId: str
    sessionId: str
    eventList: Sequence[EventTypeDef]
    userId: NotRequired[str]
