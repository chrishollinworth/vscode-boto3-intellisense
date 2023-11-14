"""
Type annotations for mediapackagev2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/literals.html)

Usage::

    ```python
    from mypy_boto3_mediapackagev2.literals import AdMarkerHlsType

    data: AdMarkerHlsType = "DATERANGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdMarkerHlsType",
    "CmafEncryptionMethodType",
    "ContainerTypeType",
    "DrmSystemType",
    "ListChannelGroupsPaginatorName",
    "ListChannelsPaginatorName",
    "ListOriginEndpointsPaginatorName",
    "PresetSpeke20AudioType",
    "PresetSpeke20VideoType",
    "ScteFilterType",
    "TsEncryptionMethodType",
)

AdMarkerHlsType = Literal["DATERANGE"]
CmafEncryptionMethodType = Literal["CBCS", "CENC"]
ContainerTypeType = Literal["CMAF", "TS"]
DrmSystemType = Literal["CLEAR_KEY_AES_128", "FAIRPLAY", "PLAYREADY", "WIDEVINE"]
ListChannelGroupsPaginatorName = Literal["list_channel_groups"]
ListChannelsPaginatorName = Literal["list_channels"]
ListOriginEndpointsPaginatorName = Literal["list_origin_endpoints"]
PresetSpeke20AudioType = Literal[
    "PRESET_AUDIO_1", "PRESET_AUDIO_2", "PRESET_AUDIO_3", "SHARED", "UNENCRYPTED"
]
PresetSpeke20VideoType = Literal[
    "PRESET_VIDEO_1",
    "PRESET_VIDEO_2",
    "PRESET_VIDEO_3",
    "PRESET_VIDEO_4",
    "PRESET_VIDEO_5",
    "PRESET_VIDEO_6",
    "PRESET_VIDEO_7",
    "PRESET_VIDEO_8",
    "SHARED",
    "UNENCRYPTED",
]
ScteFilterType = Literal[
    "BREAK",
    "DISTRIBUTOR_ADVERTISEMENT",
    "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
    "PROGRAM",
    "PROVIDER_ADVERTISEMENT",
    "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
    "PROVIDER_PLACEMENT_OPPORTUNITY",
    "SPLICE_INSERT",
]
TsEncryptionMethodType = Literal["AES_128", "SAMPLE_AES"]
