"""
Type annotations for mediatailor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/literals.html)

Usage::

    ```python
    from mypy_boto3_mediatailor.literals import AccessTypeType

    data: AccessTypeType = "S3_SIGV4"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessTypeType",
    "ChannelStateType",
    "GetChannelSchedulePaginatorName",
    "ListAlertsPaginatorName",
    "ListChannelsPaginatorName",
    "ListPlaybackConfigurationsPaginatorName",
    "ListSourceLocationsPaginatorName",
    "ListVodSourcesPaginatorName",
    "MessageTypeType",
    "ModeType",
    "OriginManifestTypeType",
    "PlaybackModeType",
    "RelativePositionType",
    "TypeType",
)

AccessTypeType = Literal["S3_SIGV4", "SECRETS_MANAGER_ACCESS_TOKEN"]
ChannelStateType = Literal["RUNNING", "STOPPED"]
GetChannelSchedulePaginatorName = Literal["get_channel_schedule"]
ListAlertsPaginatorName = Literal["list_alerts"]
ListChannelsPaginatorName = Literal["list_channels"]
ListPlaybackConfigurationsPaginatorName = Literal["list_playback_configurations"]
ListSourceLocationsPaginatorName = Literal["list_source_locations"]
ListVodSourcesPaginatorName = Literal["list_vod_sources"]
MessageTypeType = Literal["SPLICE_INSERT"]
ModeType = Literal["BEHIND_LIVE_EDGE", "OFF"]
OriginManifestTypeType = Literal["MULTI_PERIOD", "SINGLE_PERIOD"]
PlaybackModeType = Literal["LOOP"]
RelativePositionType = Literal["AFTER_PROGRAM", "BEFORE_PROGRAM"]
TypeType = Literal["DASH", "HLS"]
