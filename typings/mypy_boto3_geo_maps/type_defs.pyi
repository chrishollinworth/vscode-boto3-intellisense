"""
Type annotations for geo-maps service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_geo_maps.type_defs import GetGlyphsRequestTypeDef

    data: GetGlyphsRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from botocore.response import StreamingBody

from .literals import (
    ColorSchemeType,
    LabelSizeType,
    MapFeatureModeType,
    MapStyleType,
    ScaleBarUnitType,
    StaticMapStyleType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "GetGlyphsRequestTypeDef",
    "GetGlyphsResponseTypeDef",
    "GetSpritesRequestTypeDef",
    "GetSpritesResponseTypeDef",
    "GetStaticMapRequestTypeDef",
    "GetStaticMapResponseTypeDef",
    "GetStyleDescriptorRequestTypeDef",
    "GetStyleDescriptorResponseTypeDef",
    "GetTileRequestTypeDef",
    "GetTileResponseTypeDef",
    "ResponseMetadataTypeDef",
)

class GetGlyphsRequestTypeDef(TypedDict):
    FontStack: str
    FontUnicodeRange: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetSpritesRequestTypeDef(TypedDict):
    FileName: str
    Style: MapStyleType
    ColorScheme: ColorSchemeType
    Variant: Literal["Default"]

class GetStaticMapRequestTypeDef(TypedDict):
    Height: int
    FileName: str
    Width: int
    BoundingBox: NotRequired[str]
    BoundedPositions: NotRequired[str]
    Center: NotRequired[str]
    ColorScheme: NotRequired[ColorSchemeType]
    CompactOverlay: NotRequired[str]
    CropLabels: NotRequired[bool]
    GeoJsonOverlay: NotRequired[str]
    Key: NotRequired[str]
    LabelSize: NotRequired[LabelSizeType]
    Language: NotRequired[str]
    Padding: NotRequired[int]
    PoliticalView: NotRequired[str]
    PointsOfInterests: NotRequired[MapFeatureModeType]
    Radius: NotRequired[int]
    ScaleBarUnit: NotRequired[ScaleBarUnitType]
    Style: NotRequired[StaticMapStyleType]
    Zoom: NotRequired[float]

class GetStyleDescriptorRequestTypeDef(TypedDict):
    Style: MapStyleType
    ColorScheme: NotRequired[ColorSchemeType]
    PoliticalView: NotRequired[str]
    Key: NotRequired[str]

class GetTileRequestTypeDef(TypedDict):
    Tileset: str
    Z: str
    X: str
    Y: str
    Key: NotRequired[str]

class GetGlyphsResponseTypeDef(TypedDict):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpritesResponseTypeDef(TypedDict):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStaticMapResponseTypeDef(TypedDict):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStyleDescriptorResponseTypeDef(TypedDict):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTileResponseTypeDef(TypedDict):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ETag: str
    PricingBucket: str
    ResponseMetadata: ResponseMetadataTypeDef
