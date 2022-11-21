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
    "ListLiveSourcesPaginatorName",
    "ListPlaybackConfigurationsPaginatorName",
    "ListPrefetchSchedulesPaginatorName",
    "ListSourceLocationsPaginatorName",
    "ListVodSourcesPaginatorName",
    "MessageTypeType",
    "ModeType",
    "OperatorType",
    "OriginManifestTypeType",
    "PlaybackModeType",
    "RelativePositionType",
    "ScheduleEntryTypeType",
    "TierType",
    "TypeType",
)

AccessTypeType = Literal["S3_SIGV4", "SECRETS_MANAGER_ACCESS_TOKEN"]
ChannelStateType = Literal["RUNNING", "STOPPED"]
GetChannelSchedulePaginatorName = Literal["get_channel_schedule"]
ListAlertsPaginatorName = Literal["list_alerts"]
ListChannelsPaginatorName = Literal["list_channels"]
ListLiveSourcesPaginatorName = Literal["list_live_sources"]
ListPlaybackConfigurationsPaginatorName = Literal["list_playback_configurations"]
ListPrefetchSchedulesPaginatorName = Literal["list_prefetch_schedules"]
ListSourceLocationsPaginatorName = Literal["list_source_locations"]
ListVodSourcesPaginatorName = Literal["list_vod_sources"]
MessageTypeType = Literal["SPLICE_INSERT", "TIME_SIGNAL"]
ModeType = Literal["BEHIND_LIVE_EDGE", "OFF"]
OperatorType = Literal["EQUALS"]
OriginManifestTypeType = Literal["MULTI_PERIOD", "SINGLE_PERIOD"]
PlaybackModeType = Literal["LINEAR", "LOOP"]
RelativePositionType = Literal["AFTER_PROGRAM", "BEFORE_PROGRAM"]
ScheduleEntryTypeType = Literal["FILLER_SLATE", "PROGRAM"]
TierType = Literal["BASIC", "STANDARD"]
TypeType = Literal["DASH", "HLS"]
