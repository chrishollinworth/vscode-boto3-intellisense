"""
Type annotations for ivs-realtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/literals.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.literals import EventErrorCodeType

    data: EventErrorCodeType = "INSUFFICIENT_CAPABILITIES"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EventErrorCodeType",
    "EventNameType",
    "ParticipantStateType",
    "ParticipantTokenCapabilityType",
)

EventErrorCodeType = Literal["INSUFFICIENT_CAPABILITIES", "PUBLISHER_NOT_FOUND", "QUOTA_EXCEEDED"]
EventNameType = Literal[
    "JOINED",
    "JOIN_ERROR",
    "LEFT",
    "PUBLISH_ERROR",
    "PUBLISH_STARTED",
    "PUBLISH_STOPPED",
    "SUBSCRIBE_ERROR",
    "SUBSCRIBE_STARTED",
    "SUBSCRIBE_STOPPED",
]
ParticipantStateType = Literal["CONNECTED", "DISCONNECTED"]
ParticipantTokenCapabilityType = Literal["PUBLISH", "SUBSCRIBE"]
