"""
Main interface for mediatailor service type definitions.

Usage::

    ```python
    from mypy_boto3_mediatailor.type_defs import AdMarkerPassthroughTypeDef

    data: AdMarkerPassthroughTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AdMarkerPassthroughTypeDef",
    "AvailSuppressionTypeDef",
    "BumperTypeDef",
    "CdnConfigurationTypeDef",
    "DashConfigurationTypeDef",
    "HlsConfigurationTypeDef",
    "LivePreRollConfigurationTypeDef",
    "ManifestProcessingRulesTypeDef",
    "PlaybackConfigurationTypeDef",
    "DashConfigurationForPutTypeDef",
    "GetPlaybackConfigurationResponseTypeDef",
    "ListPlaybackConfigurationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutPlaybackConfigurationResponseTypeDef",
)

AdMarkerPassthroughTypeDef = TypedDict("AdMarkerPassthroughTypeDef", {"Enabled": bool}, total=False)

AvailSuppressionTypeDef = TypedDict(
    "AvailSuppressionTypeDef",
    {"Mode": Literal["OFF", "BEHIND_LIVE_EDGE"], "Value": str},
    total=False,
)

BumperTypeDef = TypedDict("BumperTypeDef", {"EndUrl": str, "StartUrl": str}, total=False)

CdnConfigurationTypeDef = TypedDict(
    "CdnConfigurationTypeDef",
    {"AdSegmentUrlPrefix": str, "ContentSegmentUrlPrefix": str},
    total=False,
)

DashConfigurationTypeDef = TypedDict(
    "DashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"],
    },
    total=False,
)

HlsConfigurationTypeDef = TypedDict(
    "HlsConfigurationTypeDef", {"ManifestEndpointPrefix": str}, total=False
)

LivePreRollConfigurationTypeDef = TypedDict(
    "LivePreRollConfigurationTypeDef",
    {"AdDecisionServerUrl": str, "MaxDurationSeconds": int},
    total=False,
)

ManifestProcessingRulesTypeDef = TypedDict(
    "ManifestProcessingRulesTypeDef",
    {"AdMarkerPassthrough": "AdMarkerPassthroughTypeDef"},
    total=False,
)

PlaybackConfigurationTypeDef = TypedDict(
    "PlaybackConfigurationTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "PersonalizationThresholdSeconds": int,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

DashConfigurationForPutTypeDef = TypedDict(
    "DashConfigurationForPutTypeDef",
    {"MpdLocation": str, "OriginManifestType": Literal["SINGLE_PERIOD", "MULTI_PERIOD"]},
    total=False,
)

GetPlaybackConfigurationResponseTypeDef = TypedDict(
    "GetPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

ListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsResponseTypeDef",
    {"Items": List["PlaybackConfigurationTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutPlaybackConfigurationResponseTypeDef = TypedDict(
    "PutPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)
