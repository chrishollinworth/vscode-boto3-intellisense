"""
Type annotations for geo-places service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_geo_places.client import LocationServicePlacesV2Client

    session = Session()
    client: LocationServicePlacesV2Client = session.client("geo-places")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AutocompleteRequestTypeDef,
    AutocompleteResponseTypeDef,
    GeocodeRequestTypeDef,
    GeocodeResponseTypeDef,
    GetPlaceRequestTypeDef,
    GetPlaceResponseTypeDef,
    ReverseGeocodeRequestTypeDef,
    ReverseGeocodeResponseTypeDef,
    SearchNearbyRequestTypeDef,
    SearchNearbyResponseTypeDef,
    SearchTextRequestTypeDef,
    SearchTextResponseTypeDef,
    SuggestRequestTypeDef,
    SuggestResponseTypeDef,
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

__all__ = ("LocationServicePlacesV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LocationServicePlacesV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places.html#LocationServicePlacesV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LocationServicePlacesV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places.html#LocationServicePlacesV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#generate_presigned_url)
        """

    def autocomplete(
        self, **kwargs: Unpack[AutocompleteRequestTypeDef]
    ) -> AutocompleteResponseTypeDef:
        """
        <code>Autocomplete</code> completes potential places and addresses as the user
        types, based on the partial input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/autocomplete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#autocomplete)
        """

    def geocode(self, **kwargs: Unpack[GeocodeRequestTypeDef]) -> GeocodeResponseTypeDef:
        """
        <code>Geocode</code> converts a textual address or place into geographic
        coordinates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/geocode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#geocode)
        """

    def get_place(self, **kwargs: Unpack[GetPlaceRequestTypeDef]) -> GetPlaceResponseTypeDef:
        """
        <code>GetPlace</code> finds a place by its unique ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/get_place.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#get_place)
        """

    def reverse_geocode(
        self, **kwargs: Unpack[ReverseGeocodeRequestTypeDef]
    ) -> ReverseGeocodeResponseTypeDef:
        """
        <code>ReverseGeocode</code> converts geographic coordinates into a
        human-readable address or place.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/reverse_geocode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#reverse_geocode)
        """

    def search_nearby(
        self, **kwargs: Unpack[SearchNearbyRequestTypeDef]
    ) -> SearchNearbyResponseTypeDef:
        """
        <code>SearchNearby</code> queries for points of interest within a radius from a
        central coordinates, returning place results with optional filters such as
        categories, business chains, food types and more.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/search_nearby.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#search_nearby)
        """

    def search_text(self, **kwargs: Unpack[SearchTextRequestTypeDef]) -> SearchTextResponseTypeDef:
        """
        <code>SearchText</code> searches for geocode and place information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/search_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#search_text)
        """

    def suggest(self, **kwargs: Unpack[SuggestRequestTypeDef]) -> SuggestResponseTypeDef:
        """
        <code>Suggest</code> provides intelligent predictions or recommendations based
        on the user's input or context, such as relevant places, points of interest,
        query terms or search category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/suggest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#suggest)
        """
