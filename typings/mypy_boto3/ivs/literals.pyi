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
    "RecordingModeType",
    "RenditionConfigurationRenditionSelectionType",
    "RenditionConfigurationRenditionType",
    "StreamHealthType",
    "StreamStateType",
    "ThumbnailConfigurationResolutionType",
    "ThumbnailConfigurationStorageType",
    "TranscodePresetType",
)

ChannelLatencyModeType = Literal["LOW", "NORMAL"]
ChannelTypeType = Literal["ADVANCED_HD", "ADVANCED_SD", "BASIC", "STANDARD"]
ListChannelsPaginatorName = Literal["list_channels"]
ListPlaybackKeyPairsPaginatorName = Literal["list_playback_key_pairs"]
ListRecordingConfigurationsPaginatorName = Literal["list_recording_configurations"]
ListStreamKeysPaginatorName = Literal["list_stream_keys"]
ListStreamsPaginatorName = Literal["list_streams"]
RecordingConfigurationStateType = Literal["ACTIVE", "CREATE_FAILED", "CREATING"]
RecordingModeType = Literal["DISABLED", "INTERVAL"]
RenditionConfigurationRenditionSelectionType = Literal["ALL", "CUSTOM", "NONE"]
RenditionConfigurationRenditionType = Literal["FULL_HD", "HD", "LOWEST_RESOLUTION", "SD"]
StreamHealthType = Literal["HEALTHY", "STARVING", "UNKNOWN"]
StreamStateType = Literal["LIVE", "OFFLINE"]
ThumbnailConfigurationResolutionType = Literal["FULL_HD", "HD", "LOWEST_RESOLUTION", "SD"]
ThumbnailConfigurationStorageType = Literal["LATEST", "SEQUENTIAL"]
TranscodePresetType = Literal["CONSTRAINED_BANDWIDTH_DELIVERY", "HIGHER_BANDWIDTH_DELIVERY"]
