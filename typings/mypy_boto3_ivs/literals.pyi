"""
Type annotations for ivs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/literals.html)

Usage::

    ```python
    from mypy_boto3_ivs.literals import ChannelLatencyModeType

    data: ChannelLatencyModeType = "LOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChannelLatencyModeType",
    "ChannelTypeType",
    "ListChannelsPaginatorName",
    "ListPlaybackKeyPairsPaginatorName",
    "ListRecordingConfigurationsPaginatorName",
    "ListStreamKeysPaginatorName",
    "ListStreamsPaginatorName",
    "RecordingConfigurationStateType",
    "StreamHealthType",
    "StreamStateType",
)

ChannelLatencyModeType = Literal["LOW", "NORMAL"]
ChannelTypeType = Literal["BASIC", "STANDARD"]
ListChannelsPaginatorName = Literal["list_channels"]
ListPlaybackKeyPairsPaginatorName = Literal["list_playback_key_pairs"]
ListRecordingConfigurationsPaginatorName = Literal["list_recording_configurations"]
ListStreamKeysPaginatorName = Literal["list_stream_keys"]
ListStreamsPaginatorName = Literal["list_streams"]
RecordingConfigurationStateType = Literal["ACTIVE", "CREATE_FAILED", "CREATING"]
StreamHealthType = Literal["HEALTHY", "STARVING", "UNKNOWN"]
StreamStateType = Literal["LIVE", "OFFLINE"]
