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
        The autocomplete operation speeds up and increases the accuracy of entering
        addresses by providing a list of address candidates matching a partially
        entered address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/autocomplete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#autocomplete)
        """

    def geocode(self, **kwargs: Unpack[GeocodeRequestTypeDef]) -> GeocodeResponseTypeDef:
        """
        The <code>Geocode</code> action allows you to obtain coordinates, addresses,
        and other information about places.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/geocode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#geocode)
        """

    def get_place(self, **kwargs: Unpack[GetPlaceRequestTypeDef]) -> GetPlaceResponseTypeDef:
        """
        Finds a place by its unique ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/get_place.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#get_place)
        """

    def reverse_geocode(
        self, **kwargs: Unpack[ReverseGeocodeRequestTypeDef]
    ) -> ReverseGeocodeResponseTypeDef:
        """
        The <code>ReverseGeocode</code> operation allows you to retrieve addresses and
        place information from coordinates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/reverse_geocode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#reverse_geocode)
        """

    def search_nearby(
        self, **kwargs: Unpack[SearchNearbyRequestTypeDef]
    ) -> SearchNearbyResponseTypeDef:
        """
        Search nearby a specified location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/search_nearby.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#search_nearby)
        """

    def search_text(self, **kwargs: Unpack[SearchTextRequestTypeDef]) -> SearchTextResponseTypeDef:
        """
        Use the <code>SearchText</code> operation to search for geocode and place
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/search_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#search_text)
        """

    def suggest(self, **kwargs: Unpack[SuggestRequestTypeDef]) -> SuggestResponseTypeDef:
        """
        The <code>Suggest</code> operation finds addresses or place candidates based on
        incomplete or misspelled queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-places/client/suggest.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/client/#suggest)
        """
