"""
Type annotations for mediapackage-vod service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/literals.html)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.literals import AdMarkersType

    data: AdMarkersType = "NONE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdMarkersType",
    "EncryptionMethodType",
    "ListAssetsPaginatorName",
    "ListPackagingConfigurationsPaginatorName",
    "ListPackagingGroupsPaginatorName",
    "ManifestLayoutType",
    "PresetSpeke20AudioType",
    "PresetSpeke20VideoType",
    "ProfileType",
    "ScteMarkersSourceType",
    "SegmentTemplateFormatType",
    "StreamOrderType",
    "__PeriodTriggersElementType",
)

AdMarkersType = Literal["NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
EncryptionMethodType = Literal["AES_128", "SAMPLE_AES"]
ListAssetsPaginatorName = Literal["list_assets"]
ListPackagingConfigurationsPaginatorName = Literal["list_packaging_configurations"]
ListPackagingGroupsPaginatorName = Literal["list_packaging_groups"]
ManifestLayoutType = Literal["COMPACT", "FULL"]
PresetSpeke20AudioType = Literal[
    "PRESET-AUDIO-1", "PRESET-AUDIO-2", "PRESET-AUDIO-3", "SHARED", "UNENCRYPTED"
]
PresetSpeke20VideoType = Literal[
    "PRESET-VIDEO-1",
    "PRESET-VIDEO-2",
    "PRESET-VIDEO-3",
    "PRESET-VIDEO-4",
    "PRESET-VIDEO-5",
    "PRESET-VIDEO-6",
    "PRESET-VIDEO-7",
    "PRESET-VIDEO-8",
    "SHARED",
    "UNENCRYPTED",
]
ProfileType = Literal["HBBTV_1_5", "NONE"]
ScteMarkersSourceType = Literal["MANIFEST", "SEGMENTS"]
SegmentTemplateFormatType = Literal[
    "NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"
]
StreamOrderType = Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"]
__PeriodTriggersElementType = Literal["ADS"]
