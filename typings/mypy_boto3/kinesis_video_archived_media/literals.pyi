"""
Type annotations for kinesis-video-archived-media service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.literals import ClipFragmentSelectorTypeType

    data: ClipFragmentSelectorTypeType = "PRODUCER_TIMESTAMP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ClipFragmentSelectorTypeType",
    "ContainerFormatType",
    "DASHDisplayFragmentNumberType",
    "DASHDisplayFragmentTimestampType",
    "DASHFragmentSelectorTypeType",
    "DASHPlaybackModeType",
    "FragmentSelectorTypeType",
    "HLSDiscontinuityModeType",
    "HLSDisplayFragmentTimestampType",
    "HLSFragmentSelectorTypeType",
    "HLSPlaybackModeType",
    "ListFragmentsPaginatorName",
)

ClipFragmentSelectorTypeType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
ContainerFormatType = Literal["FRAGMENTED_MP4", "MPEG_TS"]
DASHDisplayFragmentNumberType = Literal["ALWAYS", "NEVER"]
DASHDisplayFragmentTimestampType = Literal["ALWAYS", "NEVER"]
DASHFragmentSelectorTypeType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
DASHPlaybackModeType = Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]
FragmentSelectorTypeType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
HLSDiscontinuityModeType = Literal["ALWAYS", "NEVER", "ON_DISCONTINUITY"]
HLSDisplayFragmentTimestampType = Literal["ALWAYS", "NEVER"]
HLSFragmentSelectorTypeType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
HLSPlaybackModeType = Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]
ListFragmentsPaginatorName = Literal["list_fragments"]
