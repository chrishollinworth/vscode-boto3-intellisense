"""
Type annotations for mediapackage service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/literals.html)

Usage::

    ```python
    from mypy_boto3_mediapackage.literals import AdMarkersType

    data: AdMarkersType = "DATERANGE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdMarkersType",
    "AdsOnDeliveryRestrictionsType",
    "CmafEncryptionMethodType",
    "EncryptionMethodType",
    "ListChannelsPaginatorName",
    "ListHarvestJobsPaginatorName",
    "ListOriginEndpointsPaginatorName",
    "ManifestLayoutType",
    "OriginationType",
    "PlaylistTypeType",
    "PresetSpeke20AudioType",
    "PresetSpeke20VideoType",
    "ProfileType",
    "SegmentTemplateFormatType",
    "StatusType",
    "StreamOrderType",
    "UtcTimingType",
    "__AdTriggersElementType",
    "__PeriodTriggersElementType",
)

AdMarkersType = Literal["DATERANGE", "NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
AdsOnDeliveryRestrictionsType = Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
CmafEncryptionMethodType = Literal["AES_CTR", "SAMPLE_AES"]
EncryptionMethodType = Literal["AES_128", "SAMPLE_AES"]
ListChannelsPaginatorName = Literal["list_channels"]
ListHarvestJobsPaginatorName = Literal["list_harvest_jobs"]
ListOriginEndpointsPaginatorName = Literal["list_origin_endpoints"]
ManifestLayoutType = Literal["COMPACT", "DRM_TOP_LEVEL_COMPACT", "FULL"]
OriginationType = Literal["ALLOW", "DENY"]
PlaylistTypeType = Literal["EVENT", "NONE", "VOD"]
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
ProfileType = Literal["DVB_DASH_2014", "HBBTV_1_5", "HYBRIDCAST", "NONE"]
SegmentTemplateFormatType = Literal[
    "NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"
]
StatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
StreamOrderType = Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"]
UtcTimingType = Literal["HTTP-HEAD", "HTTP-ISO", "HTTP-XSDATE", "NONE"]
__AdTriggersElementType = Literal[
    "BREAK",
    "DISTRIBUTOR_ADVERTISEMENT",
    "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
    "PROVIDER_ADVERTISEMENT",
    "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
    "PROVIDER_PLACEMENT_OPPORTUNITY",
    "SPLICE_INSERT",
]
__PeriodTriggersElementType = Literal["ADS"]
