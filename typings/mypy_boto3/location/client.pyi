"""
Type annotations for location service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_location.client import LocationServiceClient

    session = Session()
    client: LocationServiceClient = session.client("location")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ForecastGeofenceEventsPaginator,
    GetDevicePositionHistoryPaginator,
    ListDevicePositionsPaginator,
    ListGeofenceCollectionsPaginator,
    ListGeofencesPaginator,
    ListKeysPaginator,
    ListMapsPaginator,
    ListPlaceIndexesPaginator,
    ListRouteCalculatorsPaginator,
    ListTrackerConsumersPaginator,
    ListTrackersPaginator,
)
from .type_defs import (
    AssociateTrackerConsumerRequestTypeDef,
    BatchDeleteDevicePositionHistoryRequestTypeDef,
    BatchDeleteDevicePositionHistoryResponseTypeDef,
    BatchDeleteGeofenceRequestTypeDef,
    BatchDeleteGeofenceResponseTypeDef,
    BatchEvaluateGeofencesRequestTypeDef,
    BatchEvaluateGeofencesResponseTypeDef,
    BatchGetDevicePositionRequestTypeDef,
    BatchGetDevicePositionResponseTypeDef,
    BatchPutGeofenceRequestTypeDef,
    BatchPutGeofenceResponseTypeDef,
    BatchUpdateDevicePositionRequestTypeDef,
    BatchUpdateDevicePositionResponseTypeDef,
    CalculateRouteMatrixRequestTypeDef,
    CalculateRouteMatrixResponseTypeDef,
    CalculateRouteRequestTypeDef,
    CalculateRouteResponseTypeDef,
    CreateGeofenceCollectionRequestTypeDef,
    CreateGeofenceCollectionResponseTypeDef,
    CreateKeyRequestTypeDef,
    CreateKeyResponseTypeDef,
    CreateMapRequestTypeDef,
    CreateMapResponseTypeDef,
    CreatePlaceIndexRequestTypeDef,
    CreatePlaceIndexResponseTypeDef,
    CreateRouteCalculatorRequestTypeDef,
    CreateRouteCalculatorResponseTypeDef,
    CreateTrackerRequestTypeDef,
    CreateTrackerResponseTypeDef,
    DeleteGeofenceCollectionRequestTypeDef,
    DeleteKeyRequestTypeDef,
    DeleteMapRequestTypeDef,
    DeletePlaceIndexRequestTypeDef,
    DeleteRouteCalculatorRequestTypeDef,
    DeleteTrackerRequestTypeDef,
    DescribeGeofenceCollectionRequestTypeDef,
    DescribeGeofenceCollectionResponseTypeDef,
    DescribeKeyRequestTypeDef,
    DescribeKeyResponseTypeDef,
    DescribeMapRequestTypeDef,
    DescribeMapResponseTypeDef,
    DescribePlaceIndexRequestTypeDef,
    DescribePlaceIndexResponseTypeDef,
    DescribeRouteCalculatorRequestTypeDef,
    DescribeRouteCalculatorResponseTypeDef,
    DescribeTrackerRequestTypeDef,
    DescribeTrackerResponseTypeDef,
    DisassociateTrackerConsumerRequestTypeDef,
    ForecastGeofenceEventsRequestTypeDef,
    ForecastGeofenceEventsResponseTypeDef,
    GetDevicePositionHistoryRequestTypeDef,
    GetDevicePositionHistoryResponseTypeDef,
    GetDevicePositionRequestTypeDef,
    GetDevicePositionResponseTypeDef,
    GetGeofenceRequestTypeDef,
    GetGeofenceResponseTypeDef,
    GetMapGlyphsRequestTypeDef,
    GetMapGlyphsResponseTypeDef,
    GetMapSpritesRequestTypeDef,
    GetMapSpritesResponseTypeDef,
    GetMapStyleDescriptorRequestTypeDef,
    GetMapStyleDescriptorResponseTypeDef,
    GetMapTileRequestTypeDef,
    GetMapTileResponseTypeDef,
    GetPlaceRequestTypeDef,
    GetPlaceResponseTypeDef,
    ListDevicePositionsRequestTypeDef,
    ListDevicePositionsResponseTypeDef,
    ListGeofenceCollectionsRequestTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesRequestTypeDef,
    ListGeofencesResponseTypeDef,
    ListKeysRequestTypeDef,
    ListKeysResponseTypeDef,
    ListMapsRequestTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesRequestTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListRouteCalculatorsRequestTypeDef,
    ListRouteCalculatorsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrackerConsumersRequestTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersRequestTypeDef,
    ListTrackersResponseTypeDef,
    PutGeofenceRequestTypeDef,
    PutGeofenceResponseTypeDef,
    SearchPlaceIndexForPositionRequestTypeDef,
    SearchPlaceIndexForPositionResponseTypeDef,
    SearchPlaceIndexForSuggestionsRequestTypeDef,
    SearchPlaceIndexForSuggestionsResponseTypeDef,
    SearchPlaceIndexForTextRequestTypeDef,
    SearchPlaceIndexForTextResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateGeofenceCollectionRequestTypeDef,
    UpdateGeofenceCollectionResponseTypeDef,
    UpdateKeyRequestTypeDef,
    UpdateKeyResponseTypeDef,
    UpdateMapRequestTypeDef,
    UpdateMapResponseTypeDef,
    UpdatePlaceIndexRequestTypeDef,
    UpdatePlaceIndexResponseTypeDef,
    UpdateRouteCalculatorRequestTypeDef,
    UpdateRouteCalculatorResponseTypeDef,
    UpdateTrackerRequestTypeDef,
    UpdateTrackerResponseTypeDef,
    VerifyDevicePositionRequestTypeDef,
    VerifyDevicePositionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("LocationServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LocationServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LocationServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#generate_presigned_url)
        """

    def associate_tracker_consumer(
        self, **kwargs: Unpack[AssociateTrackerConsumerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates an association between a geofence collection and a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/associate_tracker_consumer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#associate_tracker_consumer)
        """

    def batch_delete_device_position_history(
        self, **kwargs: Unpack[BatchDeleteDevicePositionHistoryRequestTypeDef]
    ) -> BatchDeleteDevicePositionHistoryResponseTypeDef:
        """
        Deletes the position history of one or more devices from a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_delete_device_position_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_delete_device_position_history)
        """

    def batch_delete_geofence(
        self, **kwargs: Unpack[BatchDeleteGeofenceRequestTypeDef]
    ) -> BatchDeleteGeofenceResponseTypeDef:
        """
        Deletes a batch of geofences from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_delete_geofence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_delete_geofence)
        """

    def batch_evaluate_geofences(
        self, **kwargs: Unpack[BatchEvaluateGeofencesRequestTypeDef]
    ) -> BatchEvaluateGeofencesResponseTypeDef:
        """
        Evaluates device positions against the geofence geometries from a given
        geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_evaluate_geofences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_evaluate_geofences)
        """

    def batch_get_device_position(
        self, **kwargs: Unpack[BatchGetDevicePositionRequestTypeDef]
    ) -> BatchGetDevicePositionResponseTypeDef:
        """
        Lists the latest device positions for requested devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_get_device_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_get_device_position)
        """

    def batch_put_geofence(
        self, **kwargs: Unpack[BatchPutGeofenceRequestTypeDef]
    ) -> BatchPutGeofenceResponseTypeDef:
        """
        A batch request for storing geofence geometries into a given geofence
        collection, or updates the geometry of an existing geofence if a geofence ID is
        included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_put_geofence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_put_geofence)
        """

    def batch_update_device_position(
        self, **kwargs: Unpack[BatchUpdateDevicePositionRequestTypeDef]
    ) -> BatchUpdateDevicePositionResponseTypeDef:
        """
        Uploads position update data for one or more devices to a tracker resource (up
        to 10 devices per batch).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/batch_update_device_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#batch_update_device_position)
        """

    def calculate_route(
        self, **kwargs: Unpack[CalculateRouteRequestTypeDef]
    ) -> CalculateRouteResponseTypeDef:
        """
        <a
        href="https://docs.aws.amazon.com/location/latest/developerguide/calculate-route.html">Calculates
        a route</a> given the following required parameters:
        <code>DeparturePosition</code> and <code>DestinationPosition</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/calculate_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#calculate_route)
        """

    def calculate_route_matrix(
        self, **kwargs: Unpack[CalculateRouteMatrixRequestTypeDef]
    ) -> CalculateRouteMatrixResponseTypeDef:
        """
        <a
        href="https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html">
        Calculates a route matrix</a> given the following required parameters:
        <code>DeparturePositions</code> and <code>DestinationPositions</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/calculate_route_matrix.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#calculate_route_matrix)
        """

    def create_geofence_collection(
        self, **kwargs: Unpack[CreateGeofenceCollectionRequestTypeDef]
    ) -> CreateGeofenceCollectionResponseTypeDef:
        """
        Creates a geofence collection, which manages and stores geofences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_geofence_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_geofence_collection)
        """

    def create_key(self, **kwargs: Unpack[CreateKeyRequestTypeDef]) -> CreateKeyResponseTypeDef:
        """
        Creates an API key resource in your Amazon Web Services account, which lets you
        grant actions for Amazon Location resources to the API key bearer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_key)
        """

    def create_map(self, **kwargs: Unpack[CreateMapRequestTypeDef]) -> CreateMapResponseTypeDef:
        """
        Creates a map resource in your Amazon Web Services account, which provides map
        tiles of different styles sourced from global location data providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_map)
        """

    def create_place_index(
        self, **kwargs: Unpack[CreatePlaceIndexRequestTypeDef]
    ) -> CreatePlaceIndexResponseTypeDef:
        """
        Creates a place index resource in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_place_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_place_index)
        """

    def create_route_calculator(
        self, **kwargs: Unpack[CreateRouteCalculatorRequestTypeDef]
    ) -> CreateRouteCalculatorResponseTypeDef:
        """
        Creates a route calculator resource in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_route_calculator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_route_calculator)
        """

    def create_tracker(
        self, **kwargs: Unpack[CreateTrackerRequestTypeDef]
    ) -> CreateTrackerResponseTypeDef:
        """
        Creates a tracker resource in your Amazon Web Services account, which lets you
        retrieve current and historical location of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/create_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#create_tracker)
        """

    def delete_geofence_collection(
        self, **kwargs: Unpack[DeleteGeofenceCollectionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a geofence collection from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_geofence_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_geofence_collection)
        """

    def delete_key(self, **kwargs: Unpack[DeleteKeyRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_key)
        """

    def delete_map(self, **kwargs: Unpack[DeleteMapRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a map resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_map)
        """

    def delete_place_index(
        self, **kwargs: Unpack[DeletePlaceIndexRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a place index resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_place_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_place_index)
        """

    def delete_route_calculator(
        self, **kwargs: Unpack[DeleteRouteCalculatorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a route calculator resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_route_calculator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_route_calculator)
        """

    def delete_tracker(self, **kwargs: Unpack[DeleteTrackerRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a tracker resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/delete_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#delete_tracker)
        """

    def describe_geofence_collection(
        self, **kwargs: Unpack[DescribeGeofenceCollectionRequestTypeDef]
    ) -> DescribeGeofenceCollectionResponseTypeDef:
        """
        Retrieves the geofence collection details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_geofence_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_geofence_collection)
        """

    def describe_key(
        self, **kwargs: Unpack[DescribeKeyRequestTypeDef]
    ) -> DescribeKeyResponseTypeDef:
        """
        Retrieves the API key resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_key)
        """

    def describe_map(
        self, **kwargs: Unpack[DescribeMapRequestTypeDef]
    ) -> DescribeMapResponseTypeDef:
        """
        Retrieves the map resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_map)
        """

    def describe_place_index(
        self, **kwargs: Unpack[DescribePlaceIndexRequestTypeDef]
    ) -> DescribePlaceIndexResponseTypeDef:
        """
        Retrieves the place index resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_place_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_place_index)
        """

    def describe_route_calculator(
        self, **kwargs: Unpack[DescribeRouteCalculatorRequestTypeDef]
    ) -> DescribeRouteCalculatorResponseTypeDef:
        """
        Retrieves the route calculator resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_route_calculator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_route_calculator)
        """

    def describe_tracker(
        self, **kwargs: Unpack[DescribeTrackerRequestTypeDef]
    ) -> DescribeTrackerResponseTypeDef:
        """
        Retrieves the tracker resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/describe_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#describe_tracker)
        """

    def disassociate_tracker_consumer(
        self, **kwargs: Unpack[DisassociateTrackerConsumerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the association between a tracker resource and a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/disassociate_tracker_consumer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#disassociate_tracker_consumer)
        """

    def forecast_geofence_events(
        self, **kwargs: Unpack[ForecastGeofenceEventsRequestTypeDef]
    ) -> ForecastGeofenceEventsResponseTypeDef:
        """
        Evaluates device positions against geofence geometries from a given geofence
        collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/forecast_geofence_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#forecast_geofence_events)
        """

    def get_device_position(
        self, **kwargs: Unpack[GetDevicePositionRequestTypeDef]
    ) -> GetDevicePositionResponseTypeDef:
        """
        Retrieves a device's most recent position according to its sample time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_device_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_device_position)
        """

    def get_device_position_history(
        self, **kwargs: Unpack[GetDevicePositionHistoryRequestTypeDef]
    ) -> GetDevicePositionHistoryResponseTypeDef:
        """
        Retrieves the device position history from a tracker resource within a
        specified range of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_device_position_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_device_position_history)
        """

    def get_geofence(
        self, **kwargs: Unpack[GetGeofenceRequestTypeDef]
    ) -> GetGeofenceResponseTypeDef:
        """
        Retrieves the geofence details from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_geofence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_geofence)
        """

    def get_map_glyphs(
        self, **kwargs: Unpack[GetMapGlyphsRequestTypeDef]
    ) -> GetMapGlyphsResponseTypeDef:
        """
        Retrieves glyphs used to display labels on a map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_map_glyphs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_map_glyphs)
        """

    def get_map_sprites(
        self, **kwargs: Unpack[GetMapSpritesRequestTypeDef]
    ) -> GetMapSpritesResponseTypeDef:
        """
        Retrieves the sprite sheet corresponding to a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_map_sprites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_map_sprites)
        """

    def get_map_style_descriptor(
        self, **kwargs: Unpack[GetMapStyleDescriptorRequestTypeDef]
    ) -> GetMapStyleDescriptorResponseTypeDef:
        """
        Retrieves the map style descriptor from a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_map_style_descriptor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_map_style_descriptor)
        """

    def get_map_tile(self, **kwargs: Unpack[GetMapTileRequestTypeDef]) -> GetMapTileResponseTypeDef:
        """
        Retrieves a vector data tile from the map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_map_tile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_map_tile)
        """

    def get_place(self, **kwargs: Unpack[GetPlaceRequestTypeDef]) -> GetPlaceResponseTypeDef:
        """
        Finds a place by its unique ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_place.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_place)
        """

    def list_device_positions(
        self, **kwargs: Unpack[ListDevicePositionsRequestTypeDef]
    ) -> ListDevicePositionsResponseTypeDef:
        """
        A batch request to retrieve all device positions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_device_positions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_device_positions)
        """

    def list_geofence_collections(
        self, **kwargs: Unpack[ListGeofenceCollectionsRequestTypeDef]
    ) -> ListGeofenceCollectionsResponseTypeDef:
        """
        Lists geofence collections in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_geofence_collections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_geofence_collections)
        """

    def list_geofences(
        self, **kwargs: Unpack[ListGeofencesRequestTypeDef]
    ) -> ListGeofencesResponseTypeDef:
        """
        Lists geofences stored in a given geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_geofences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_geofences)
        """

    def list_keys(self, **kwargs: Unpack[ListKeysRequestTypeDef]) -> ListKeysResponseTypeDef:
        """
        Lists API key resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_keys)
        """

    def list_maps(self, **kwargs: Unpack[ListMapsRequestTypeDef]) -> ListMapsResponseTypeDef:
        """
        Lists map resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_maps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_maps)
        """

    def list_place_indexes(
        self, **kwargs: Unpack[ListPlaceIndexesRequestTypeDef]
    ) -> ListPlaceIndexesResponseTypeDef:
        """
        Lists place index resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_place_indexes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_place_indexes)
        """

    def list_route_calculators(
        self, **kwargs: Unpack[ListRouteCalculatorsRequestTypeDef]
    ) -> ListRouteCalculatorsResponseTypeDef:
        """
        Lists route calculator resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_route_calculators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_route_calculators)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified Amazon Location
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_tags_for_resource)
        """

    def list_tracker_consumers(
        self, **kwargs: Unpack[ListTrackerConsumersRequestTypeDef]
    ) -> ListTrackerConsumersResponseTypeDef:
        """
        Lists geofence collections currently associated to the given tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_tracker_consumers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_tracker_consumers)
        """

    def list_trackers(
        self, **kwargs: Unpack[ListTrackersRequestTypeDef]
    ) -> ListTrackersResponseTypeDef:
        """
        Lists tracker resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/list_trackers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#list_trackers)
        """

    def put_geofence(
        self, **kwargs: Unpack[PutGeofenceRequestTypeDef]
    ) -> PutGeofenceResponseTypeDef:
        """
        Stores a geofence geometry in a given geofence collection, or updates the
        geometry of an existing geofence if a geofence ID is included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/put_geofence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#put_geofence)
        """

    def search_place_index_for_position(
        self, **kwargs: Unpack[SearchPlaceIndexForPositionRequestTypeDef]
    ) -> SearchPlaceIndexForPositionResponseTypeDef:
        """
        Reverse geocodes a given coordinate and returns a legible address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/search_place_index_for_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#search_place_index_for_position)
        """

    def search_place_index_for_suggestions(
        self, **kwargs: Unpack[SearchPlaceIndexForSuggestionsRequestTypeDef]
    ) -> SearchPlaceIndexForSuggestionsResponseTypeDef:
        """
        Generates suggestions for addresses and points of interest based on partial or
        misspelled free-form text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/search_place_index_for_suggestions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#search_place_index_for_suggestions)
        """

    def search_place_index_for_text(
        self, **kwargs: Unpack[SearchPlaceIndexForTextRequestTypeDef]
    ) -> SearchPlaceIndexForTextResponseTypeDef:
        """
        Geocodes free-form text, such as an address, name, city, or region to allow you
        to search for Places or points of interest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/search_place_index_for_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#search_place_index_for_text)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Location
        Service resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Location resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#untag_resource)
        """

    def update_geofence_collection(
        self, **kwargs: Unpack[UpdateGeofenceCollectionRequestTypeDef]
    ) -> UpdateGeofenceCollectionResponseTypeDef:
        """
        Updates the specified properties of a given geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_geofence_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_geofence_collection)
        """

    def update_key(self, **kwargs: Unpack[UpdateKeyRequestTypeDef]) -> UpdateKeyResponseTypeDef:
        """
        Updates the specified properties of a given API key resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_key)
        """

    def update_map(self, **kwargs: Unpack[UpdateMapRequestTypeDef]) -> UpdateMapResponseTypeDef:
        """
        Updates the specified properties of a given map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_map)
        """

    def update_place_index(
        self, **kwargs: Unpack[UpdatePlaceIndexRequestTypeDef]
    ) -> UpdatePlaceIndexResponseTypeDef:
        """
        Updates the specified properties of a given place index resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_place_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_place_index)
        """

    def update_route_calculator(
        self, **kwargs: Unpack[UpdateRouteCalculatorRequestTypeDef]
    ) -> UpdateRouteCalculatorResponseTypeDef:
        """
        Updates the specified properties for a given route calculator resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_route_calculator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_route_calculator)
        """

    def update_tracker(
        self, **kwargs: Unpack[UpdateTrackerRequestTypeDef]
    ) -> UpdateTrackerResponseTypeDef:
        """
        Updates the specified properties of a given tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/update_tracker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#update_tracker)
        """

    def verify_device_position(
        self, **kwargs: Unpack[VerifyDevicePositionRequestTypeDef]
    ) -> VerifyDevicePositionResponseTypeDef:
        """
        Verifies the integrity of the device's position by determining if it was
        reported behind a proxy, and by comparing it to an inferred position estimated
        based on the device's state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/verify_device_position.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#verify_device_position)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["forecast_geofence_events"]
    ) -> ForecastGeofenceEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_device_position_history"]
    ) -> GetDevicePositionHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_positions"]
    ) -> ListDevicePositionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_geofence_collections"]
    ) -> ListGeofenceCollectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_geofences"]
    ) -> ListGeofencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_keys"]
    ) -> ListKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_maps"]
    ) -> ListMapsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_place_indexes"]
    ) -> ListPlaceIndexesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_route_calculators"]
    ) -> ListRouteCalculatorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tracker_consumers"]
    ) -> ListTrackerConsumersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_trackers"]
    ) -> ListTrackersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/client/#get_paginator)
        """
