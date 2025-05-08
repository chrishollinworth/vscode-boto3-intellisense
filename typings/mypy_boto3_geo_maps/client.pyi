"""
Type annotations for geo-maps service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_geo_maps.client import LocationServiceMapsV2Client

    session = Session()
    client: LocationServiceMapsV2Client = session.client("geo-maps")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GetGlyphsRequestTypeDef,
    GetGlyphsResponseTypeDef,
    GetSpritesRequestTypeDef,
    GetSpritesResponseTypeDef,
    GetStaticMapRequestTypeDef,
    GetStaticMapResponseTypeDef,
    GetStyleDescriptorRequestTypeDef,
    GetStyleDescriptorResponseTypeDef,
    GetTileRequestTypeDef,
    GetTileResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("LocationServiceMapsV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LocationServiceMapsV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps.html#LocationServiceMapsV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LocationServiceMapsV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps.html#LocationServiceMapsV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#generate_presigned_url)
        """

    def get_glyphs(self, **kwargs: Unpack[GetGlyphsRequestTypeDef]) -> GetGlyphsResponseTypeDef:
        """
        <code>GetGlyphs</code> returns the map's glyphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_glyphs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#get_glyphs)
        """

    def get_sprites(self, **kwargs: Unpack[GetSpritesRequestTypeDef]) -> GetSpritesResponseTypeDef:
        """
        <code>GetSprites</code> returns the map's sprites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_sprites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#get_sprites)
        """

    def get_static_map(
        self, **kwargs: Unpack[GetStaticMapRequestTypeDef]
    ) -> GetStaticMapResponseTypeDef:
        """
        <code>GetStaticMap</code> provides high-quality static map images with
        customizable options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_static_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#get_static_map)
        """

    def get_style_descriptor(
        self, **kwargs: Unpack[GetStyleDescriptorRequestTypeDef]
    ) -> GetStyleDescriptorResponseTypeDef:
        """
        <code>GetStyleDescriptor</code> returns information about the style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_style_descriptor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#get_style_descriptor)
        """

    def get_tile(self, **kwargs: Unpack[GetTileRequestTypeDef]) -> GetTileResponseTypeDef:
        """
        <code>GetTile</code> returns a tile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_tile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_maps/client/#get_tile)
        """
