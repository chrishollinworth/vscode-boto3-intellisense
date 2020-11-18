"""
Main interface for personalize-events service type definitions.

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import EventTypeDef

    data: EventTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("EventTypeDef", "ItemTypeDef", "UserTypeDef")

_RequiredEventTypeDef = TypedDict("_RequiredEventTypeDef", {"eventType": str, "sentAt": datetime})
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


_RequiredItemTypeDef = TypedDict("_RequiredItemTypeDef", {"itemId": str})
_OptionalItemTypeDef = TypedDict("_OptionalItemTypeDef", {"properties": str}, total=False)


class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass


_RequiredUserTypeDef = TypedDict("_RequiredUserTypeDef", {"userId": str})
_OptionalUserTypeDef = TypedDict("_OptionalUserTypeDef", {"properties": str}, total=False)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass
