"""
Type annotations for ivs-realtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/literals.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.literals import CompositionStateType

    data: CompositionStateType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CompositionStateType",
    "DestinationStateType",
    "EventErrorCodeType",
    "EventNameType",
    "ListPublicKeysPaginatorName",
    "ParticipantRecordingFilterByRecordingStateType",
    "ParticipantRecordingMediaTypeType",
    "ParticipantRecordingStateType",
    "ParticipantStateType",
    "ParticipantTokenCapabilityType",
    "PipBehaviorType",
    "PipPositionType",
    "RecordingConfigurationFormatType",
    "VideoAspectRatioType",
    "VideoFillModeType",
)

CompositionStateType = Literal["ACTIVE", "FAILED", "STARTING", "STOPPED", "STOPPING"]
DestinationStateType = Literal[
    "ACTIVE", "FAILED", "RECONNECTING", "STARTING", "STOPPED", "STOPPING"
]
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
ListPublicKeysPaginatorName = Literal["list_public_keys"]
ParticipantRecordingFilterByRecordingStateType = Literal[
    "ACTIVE", "FAILED", "STARTING", "STOPPED", "STOPPING"
]
ParticipantRecordingMediaTypeType = Literal["AUDIO_ONLY", "AUDIO_VIDEO"]
ParticipantRecordingStateType = Literal[
    "ACTIVE", "DISABLED", "FAILED", "STARTING", "STOPPED", "STOPPING"
]
ParticipantStateType = Literal["CONNECTED", "DISCONNECTED"]
ParticipantTokenCapabilityType = Literal["PUBLISH", "SUBSCRIBE"]
PipBehaviorType = Literal["DYNAMIC", "STATIC"]
PipPositionType = Literal["BOTTOM_LEFT", "BOTTOM_RIGHT", "TOP_LEFT", "TOP_RIGHT"]
RecordingConfigurationFormatType = Literal["HLS"]
VideoAspectRatioType = Literal["AUTO", "PORTRAIT", "SQUARE", "VIDEO"]
VideoFillModeType = Literal["CONTAIN", "COVER", "FILL"]
