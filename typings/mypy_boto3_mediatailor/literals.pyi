"""
Type annotations for mediatailor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/literals.html)

Usage::

    ```python
    from mypy_boto3_mediatailor.literals import AccessTypeType

    data: AccessTypeType = "AUTODETECT_SIGV4"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessTypeType",
    "AdMarkupTypeType",
    "AlertCategoryType",
    "ChannelStateType",
    "FillPolicyType",
    "GetChannelSchedulePaginatorName",
    "InsertionModeType",
    "ListAlertsPaginatorName",
    "ListChannelsPaginatorName",
    "ListLiveSourcesPaginatorName",
    "ListPlaybackConfigurationsPaginatorName",
    "ListPrefetchSchedulesPaginatorName",
    "ListSourceLocationsPaginatorName",
    "ListVodSourcesPaginatorName",
    "LogTypeType",
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

AccessTypeType = Literal["AUTODETECT_SIGV4", "S3_SIGV4", "SECRETS_MANAGER_ACCESS_TOKEN"]
AdMarkupTypeType = Literal["DATERANGE", "SCTE35_ENHANCED"]
AlertCategoryType = Literal["INFO", "PLAYBACK_WARNING", "SCHEDULING_ERROR"]
ChannelStateType = Literal["RUNNING", "STOPPED"]
FillPolicyType = Literal["FULL_AVAIL_ONLY", "PARTIAL_AVAIL"]
GetChannelSchedulePaginatorName = Literal["get_channel_schedule"]
InsertionModeType = Literal["PLAYER_SELECT", "STITCHED_ONLY"]
ListAlertsPaginatorName = Literal["list_alerts"]
ListChannelsPaginatorName = Literal["list_channels"]
ListLiveSourcesPaginatorName = Literal["list_live_sources"]
ListPlaybackConfigurationsPaginatorName = Literal["list_playback_configurations"]
ListPrefetchSchedulesPaginatorName = Literal["list_prefetch_schedules"]
ListSourceLocationsPaginatorName = Literal["list_source_locations"]
ListVodSourcesPaginatorName = Literal["list_vod_sources"]
LogTypeType = Literal["AS_RUN"]
MessageTypeType = Literal["SPLICE_INSERT", "TIME_SIGNAL"]
ModeType = Literal["AFTER_LIVE_EDGE", "BEHIND_LIVE_EDGE", "OFF"]
OperatorType = Literal["EQUALS"]
OriginManifestTypeType = Literal["MULTI_PERIOD", "SINGLE_PERIOD"]
PlaybackModeType = Literal["LINEAR", "LOOP"]
RelativePositionType = Literal["AFTER_PROGRAM", "BEFORE_PROGRAM"]
ScheduleEntryTypeType = Literal["ALTERNATE_MEDIA", "FILLER_SLATE", "PROGRAM"]
TierType = Literal["BASIC", "STANDARD"]
TypeType = Literal["DASH", "HLS"]
