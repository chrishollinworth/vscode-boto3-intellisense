"""
Type annotations for personalize-events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import EventTypeDef

    data: EventTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "EventTypeDef",
    "ItemTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutItemsRequestRequestTypeDef",
    "PutUsersRequestRequestTypeDef",
    "UserTypeDef",
)

_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef",
    {
        "eventType": str,
        "sentAt": Union[datetime, str],
    },
)
_OptionalEventTypeDef = TypedDict(
    "_OptionalEventTypeDef",
    {
        "eventId": str,
        "eventValue": float,
        "itemId": str,
        "properties": str,
        "recommendationId": str,
        "impression": List[str],
    },
    total=False,
)

class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass

_RequiredItemTypeDef = TypedDict(
    "_RequiredItemTypeDef",
    {
        "itemId": str,
    },
)
_OptionalItemTypeDef = TypedDict(
    "_OptionalItemTypeDef",
    {
        "properties": str,
    },
    total=False,
)

class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass

_RequiredPutEventsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEventsRequestRequestTypeDef",
    {
        "trackingId": str,
        "sessionId": str,
        "eventList": List["EventTypeDef"],
    },
)
_OptionalPutEventsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEventsRequestRequestTypeDef",
    {
        "userId": str,
    },
    total=False,
)

class PutEventsRequestRequestTypeDef(
    _RequiredPutEventsRequestRequestTypeDef, _OptionalPutEventsRequestRequestTypeDef
):
    pass

PutItemsRequestRequestTypeDef = TypedDict(
    "PutItemsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "items": List["ItemTypeDef"],
    },
)

PutUsersRequestRequestTypeDef = TypedDict(
    "PutUsersRequestRequestTypeDef",
    {
        "datasetArn": str,
        "users": List["UserTypeDef"],
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "userId": str,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "properties": str,
    },
    total=False,
)

class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass
