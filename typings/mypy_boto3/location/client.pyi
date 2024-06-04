"""
Type annotations for location service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_location import LocationServiceClient

    client: LocationServiceClient = boto3.client("location")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DistanceUnitType,
    OptimizationModeType,
    PositionFilteringType,
    PricingPlanType,
    TravelModeType,
)
from .paginator import (
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
    ApiKeyFilterTypeDef,
    ApiKeyRestrictionsTypeDef,
    BatchDeleteDevicePositionHistoryResponseTypeDef,
    BatchDeleteGeofenceResponseTypeDef,
    BatchEvaluateGeofencesResponseTypeDef,
    BatchGetDevicePositionResponseTypeDef,
    BatchPutGeofenceRequestEntryTypeDef,
    BatchPutGeofenceResponseTypeDef,
    BatchUpdateDevicePositionResponseTypeDef,
    CalculateRouteCarModeOptionsTypeDef,
    CalculateRouteMatrixResponseTypeDef,
    CalculateRouteResponseTypeDef,
    CalculateRouteTruckModeOptionsTypeDef,
    CreateGeofenceCollectionResponseTypeDef,
    CreateKeyResponseTypeDef,
    CreateMapResponseTypeDef,
    CreatePlaceIndexResponseTypeDef,
    CreateRouteCalculatorResponseTypeDef,
    CreateTrackerResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DescribeGeofenceCollectionResponseTypeDef,
    DescribeKeyResponseTypeDef,
    DescribeMapResponseTypeDef,
    DescribePlaceIndexResponseTypeDef,
    DescribeRouteCalculatorResponseTypeDef,
    DescribeTrackerResponseTypeDef,
    DevicePositionUpdateTypeDef,
    GeofenceGeometryTypeDef,
    GetDevicePositionHistoryResponseTypeDef,
    GetDevicePositionResponseTypeDef,
    GetGeofenceResponseTypeDef,
    GetMapGlyphsResponseTypeDef,
    GetMapSpritesResponseTypeDef,
    GetMapStyleDescriptorResponseTypeDef,
    GetMapTileResponseTypeDef,
    GetPlaceResponseTypeDef,
    ListDevicePositionsResponseTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesResponseTypeDef,
    ListKeysResponseTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListRouteCalculatorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersResponseTypeDef,
    MapConfigurationTypeDef,
    MapConfigurationUpdateTypeDef,
    PutGeofenceResponseTypeDef,
    SearchPlaceIndexForPositionResponseTypeDef,
    SearchPlaceIndexForSuggestionsResponseTypeDef,
    SearchPlaceIndexForTextResponseTypeDef,
    TrackingFilterGeometryTypeDef,
    UpdateGeofenceCollectionResponseTypeDef,
    UpdateKeyResponseTypeDef,
    UpdateMapResponseTypeDef,
    UpdatePlaceIndexResponseTypeDef,
    UpdateRouteCalculatorResponseTypeDef,
    UpdateTrackerResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LocationServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LocationServiceClient exceptions.
        """

    def associate_tracker_consumer(self, *, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        Creates an association between a geofence collection and a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.associate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#associate_tracker_consumer)
        """

    def batch_delete_device_position_history(
        self, *, DeviceIds: List[str], TrackerName: str
    ) -> BatchDeleteDevicePositionHistoryResponseTypeDef:
        """
        Deletes the position history of one or more devices from a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_delete_device_position_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_delete_device_position_history)
        """

    def batch_delete_geofence(
        self, *, CollectionName: str, GeofenceIds: List[str]
    ) -> BatchDeleteGeofenceResponseTypeDef:
        """
        Deletes a batch of geofences from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_delete_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_delete_geofence)
        """

    def batch_evaluate_geofences(
        self, *, CollectionName: str, DevicePositionUpdates: List["DevicePositionUpdateTypeDef"]
    ) -> BatchEvaluateGeofencesResponseTypeDef:
        """
        Evaluates device positions against the geofence geometries from a given geofence
        collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_evaluate_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_evaluate_geofences)
        """

    def batch_get_device_position(
        self, *, DeviceIds: List[str], TrackerName: str
    ) -> BatchGetDevicePositionResponseTypeDef:
        """
        Lists the latest device positions for requested devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_get_device_position)
        """

    def batch_put_geofence(
        self, *, CollectionName: str, Entries: List["BatchPutGeofenceRequestEntryTypeDef"]
    ) -> BatchPutGeofenceResponseTypeDef:
        """
        A batch request for storing geofence geometries into a given geofence
        collection, or updates the geometry of an existing geofence if a geofence ID is
        included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_put_geofence)
        """

    def batch_update_device_position(
        self, *, TrackerName: str, Updates: List["DevicePositionUpdateTypeDef"]
    ) -> BatchUpdateDevicePositionResponseTypeDef:
        """
        Uploads position update data for one or more devices to a tracker resource (up
        to 10 devices per batch).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.batch_update_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_update_device_position)
        """

    def calculate_route(
        self,
        *,
        CalculatorName: str,
        DeparturePosition: List[float],
        DestinationPosition: List[float],
        ArrivalTime: Union[datetime, str] = None,
        CarModeOptions: "CalculateRouteCarModeOptionsTypeDef" = None,
        DepartNow: bool = None,
        DepartureTime: Union[datetime, str] = None,
        DistanceUnit: DistanceUnitType = None,
        IncludeLegGeometry: bool = None,
        Key: str = None,
        OptimizeFor: OptimizationModeType = None,
        TravelMode: TravelModeType = None,
        TruckModeOptions: "CalculateRouteTruckModeOptionsTypeDef" = None,
        WaypointPositions: List[List[float]] = None
    ) -> CalculateRouteResponseTypeDef:
        """
        `Calculates a route
        <https://docs.aws.amazon.com/location/latest/developerguide/calculate-
        route.html>`__ given the following required parameters: `DeparturePosition` and
        `DestinationPosition`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.calculate_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#calculate_route)
        """

    def calculate_route_matrix(
        self,
        *,
        CalculatorName: str,
        DeparturePositions: List[List[float]],
        DestinationPositions: List[List[float]],
        CarModeOptions: "CalculateRouteCarModeOptionsTypeDef" = None,
        DepartNow: bool = None,
        DepartureTime: Union[datetime, str] = None,
        DistanceUnit: DistanceUnitType = None,
        Key: str = None,
        TravelMode: TravelModeType = None,
        TruckModeOptions: "CalculateRouteTruckModeOptionsTypeDef" = None
    ) -> CalculateRouteMatrixResponseTypeDef:
        """
        `Calculates a route matrix
        <https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-
        matrix.html>`__ given the following required parameters: `DeparturePositions`
        and `DestinationPositions`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.calculate_route_matrix)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#calculate_route_matrix)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#close)
        """

    def create_geofence_collection(
        self,
        *,
        CollectionName: str,
        Description: str = None,
        KmsKeyId: str = None,
        PricingPlan: PricingPlanType = None,
        PricingPlanDataSource: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateGeofenceCollectionResponseTypeDef:
        """
        Creates a geofence collection, which manages and stores geofences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_geofence_collection)
        """

    def create_key(
        self,
        *,
        KeyName: str,
        Restrictions: "ApiKeyRestrictionsTypeDef",
        Description: str = None,
        ExpireTime: Union[datetime, str] = None,
        NoExpiry: bool = None,
        Tags: Dict[str, str] = None
    ) -> CreateKeyResponseTypeDef:
        """
        Creates an API key resource in your Amazon Web Services account, which lets you
        grant actions for Amazon Location resources to the API key bearer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_key)
        """

    def create_map(
        self,
        *,
        Configuration: "MapConfigurationTypeDef",
        MapName: str,
        Description: str = None,
        PricingPlan: PricingPlanType = None,
        Tags: Dict[str, str] = None
    ) -> CreateMapResponseTypeDef:
        """
        Creates a map resource in your Amazon Web Services account, which provides map
        tiles of different styles sourced from global location data providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_map)
        """

    def create_place_index(
        self,
        *,
        DataSource: str,
        IndexName: str,
        DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        PricingPlan: PricingPlanType = None,
        Tags: Dict[str, str] = None
    ) -> CreatePlaceIndexResponseTypeDef:
        """
        Creates a place index resource in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_place_index)
        """

    def create_route_calculator(
        self,
        *,
        CalculatorName: str,
        DataSource: str,
        Description: str = None,
        PricingPlan: PricingPlanType = None,
        Tags: Dict[str, str] = None
    ) -> CreateRouteCalculatorResponseTypeDef:
        """
        Creates a route calculator resource in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_route_calculator)
        """

    def create_tracker(
        self,
        *,
        TrackerName: str,
        Description: str = None,
        EventBridgeEnabled: bool = None,
        KmsKeyEnableGeospatialQueries: bool = None,
        KmsKeyId: str = None,
        PositionFiltering: PositionFilteringType = None,
        PricingPlan: PricingPlanType = None,
        PricingPlanDataSource: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateTrackerResponseTypeDef:
        """
        Creates a tracker resource in your Amazon Web Services account, which lets you
        retrieve current and historical location of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.create_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_tracker)
        """

    def delete_geofence_collection(self, *, CollectionName: str) -> Dict[str, Any]:
        """
        Deletes a geofence collection from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_geofence_collection)
        """

    def delete_key(self, *, KeyName: str, ForceDelete: bool = None) -> Dict[str, Any]:
        """
        Deletes the specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_key)
        """

    def delete_map(self, *, MapName: str) -> Dict[str, Any]:
        """
        Deletes a map resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_map)
        """

    def delete_place_index(self, *, IndexName: str) -> Dict[str, Any]:
        """
        Deletes a place index resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_place_index)
        """

    def delete_route_calculator(self, *, CalculatorName: str) -> Dict[str, Any]:
        """
        Deletes a route calculator resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_route_calculator)
        """

    def delete_tracker(self, *, TrackerName: str) -> Dict[str, Any]:
        """
        Deletes a tracker resource from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.delete_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_tracker)
        """

    def describe_geofence_collection(
        self, *, CollectionName: str
    ) -> DescribeGeofenceCollectionResponseTypeDef:
        """
        Retrieves the geofence collection details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_geofence_collection)
        """

    def describe_key(self, *, KeyName: str) -> DescribeKeyResponseTypeDef:
        """
        Retrieves the API key resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_key)
        """

    def describe_map(self, *, MapName: str) -> DescribeMapResponseTypeDef:
        """
        Retrieves the map resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_map)
        """

    def describe_place_index(self, *, IndexName: str) -> DescribePlaceIndexResponseTypeDef:
        """
        Retrieves the place index resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_place_index)
        """

    def describe_route_calculator(
        self, *, CalculatorName: str
    ) -> DescribeRouteCalculatorResponseTypeDef:
        """
        Retrieves the route calculator resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_route_calculator)
        """

    def describe_tracker(self, *, TrackerName: str) -> DescribeTrackerResponseTypeDef:
        """
        Retrieves the tracker resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.describe_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_tracker)
        """

    def disassociate_tracker_consumer(
        self, *, ConsumerArn: str, TrackerName: str
    ) -> Dict[str, Any]:
        """
        Removes the association between a tracker resource and a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.disassociate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#disassociate_tracker_consumer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#generate_presigned_url)
        """

    def get_device_position(
        self, *, DeviceId: str, TrackerName: str
    ) -> GetDevicePositionResponseTypeDef:
        """
        Retrieves a device's most recent position according to its sample time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_device_position)
        """

    def get_device_position_history(
        self,
        *,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        StartTimeInclusive: Union[datetime, str] = None
    ) -> GetDevicePositionHistoryResponseTypeDef:
        """
        Retrieves the device position history from a tracker resource within a specified
        range of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_device_position_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_device_position_history)
        """

    def get_geofence(self, *, CollectionName: str, GeofenceId: str) -> GetGeofenceResponseTypeDef:
        """
        Retrieves the geofence details from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_geofence)
        """

    def get_map_glyphs(
        self, *, FontStack: str, FontUnicodeRange: str, MapName: str, Key: str = None
    ) -> GetMapGlyphsResponseTypeDef:
        """
        Retrieves glyphs used to display labels on a map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_map_glyphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_glyphs)
        """

    def get_map_sprites(
        self, *, FileName: str, MapName: str, Key: str = None
    ) -> GetMapSpritesResponseTypeDef:
        """
        Retrieves the sprite sheet corresponding to a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_map_sprites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_sprites)
        """

    def get_map_style_descriptor(
        self, *, MapName: str, Key: str = None
    ) -> GetMapStyleDescriptorResponseTypeDef:
        """
        Retrieves the map style descriptor from a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_map_style_descriptor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_style_descriptor)
        """

    def get_map_tile(
        self, *, MapName: str, X: str, Y: str, Z: str, Key: str = None
    ) -> GetMapTileResponseTypeDef:
        """
        Retrieves a vector data tile from the map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_map_tile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_tile)
        """

    def get_place(
        self, *, IndexName: str, PlaceId: str, Key: str = None, Language: str = None
    ) -> GetPlaceResponseTypeDef:
        """
        Finds a place by its unique ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.get_place)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_place)
        """

    def list_device_positions(
        self,
        *,
        TrackerName: str,
        FilterGeometry: "TrackingFilterGeometryTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListDevicePositionsResponseTypeDef:
        """
        A batch request to retrieve all device positions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_device_positions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_device_positions)
        """

    def list_geofence_collections(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListGeofenceCollectionsResponseTypeDef:
        """
        Lists geofence collections in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_geofence_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_geofence_collections)
        """

    def list_geofences(
        self, *, CollectionName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListGeofencesResponseTypeDef:
        """
        Lists geofences stored in a given geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_geofences)
        """

    def list_keys(
        self, *, Filter: "ApiKeyFilterTypeDef" = None, MaxResults: int = None, NextToken: str = None
    ) -> ListKeysResponseTypeDef:
        """
        Lists API key resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_keys)
        """

    def list_maps(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListMapsResponseTypeDef:
        """
        Lists map resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_maps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_maps)
        """

    def list_place_indexes(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaceIndexesResponseTypeDef:
        """
        Lists place index resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_place_indexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_place_indexes)
        """

    def list_route_calculators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListRouteCalculatorsResponseTypeDef:
        """
        Lists route calculator resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_route_calculators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_route_calculators)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified Amazon Location
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_tags_for_resource)
        """

    def list_tracker_consumers(
        self, *, TrackerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackerConsumersResponseTypeDef:
        """
        Lists geofence collections currently associated to the given tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_tracker_consumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_tracker_consumers)
        """

    def list_trackers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackersResponseTypeDef:
        """
        Lists tracker resources in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.list_trackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_trackers)
        """

    def put_geofence(
        self,
        *,
        CollectionName: str,
        GeofenceId: str,
        Geometry: "GeofenceGeometryTypeDef",
        GeofenceProperties: Dict[str, str] = None
    ) -> PutGeofenceResponseTypeDef:
        """
        Stores a geofence geometry in a given geofence collection, or updates the
        geometry of an existing geofence if a geofence ID is included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#put_geofence)
        """

    def search_place_index_for_position(
        self,
        *,
        IndexName: str,
        Position: List[float],
        Key: str = None,
        Language: str = None,
        MaxResults: int = None
    ) -> SearchPlaceIndexForPositionResponseTypeDef:
        """
        Reverse geocodes a given coordinate and returns a legible address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.search_place_index_for_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search_place_index_for_position)
        """

    def search_place_index_for_suggestions(
        self,
        *,
        IndexName: str,
        Text: str,
        BiasPosition: List[float] = None,
        FilterBBox: List[float] = None,
        FilterCategories: List[str] = None,
        FilterCountries: List[str] = None,
        Key: str = None,
        Language: str = None,
        MaxResults: int = None
    ) -> SearchPlaceIndexForSuggestionsResponseTypeDef:
        """
        Generates suggestions for addresses and points of interest based on partial or
        misspelled free-form text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.search_place_index_for_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search_place_index_for_suggestions)
        """

    def search_place_index_for_text(
        self,
        *,
        IndexName: str,
        Text: str,
        BiasPosition: List[float] = None,
        FilterBBox: List[float] = None,
        FilterCategories: List[str] = None,
        FilterCountries: List[str] = None,
        Key: str = None,
        Language: str = None,
        MaxResults: int = None
    ) -> SearchPlaceIndexForTextResponseTypeDef:
        """
        Geocodes free-form text, such as an address, name, city, or region to allow you
        to search for Places or points of interest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.search_place_index_for_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search_place_index_for_text)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Location
        Service resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Location resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#untag_resource)
        """

    def update_geofence_collection(
        self,
        *,
        CollectionName: str,
        Description: str = None,
        PricingPlan: PricingPlanType = None,
        PricingPlanDataSource: str = None
    ) -> UpdateGeofenceCollectionResponseTypeDef:
        """
        Updates the specified properties of a given geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_geofence_collection)
        """

    def update_key(
        self,
        *,
        KeyName: str,
        Description: str = None,
        ExpireTime: Union[datetime, str] = None,
        ForceUpdate: bool = None,
        NoExpiry: bool = None,
        Restrictions: "ApiKeyRestrictionsTypeDef" = None
    ) -> UpdateKeyResponseTypeDef:
        """
        Updates the specified properties of a given API key resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_key)
        """

    def update_map(
        self,
        *,
        MapName: str,
        ConfigurationUpdate: "MapConfigurationUpdateTypeDef" = None,
        Description: str = None,
        PricingPlan: PricingPlanType = None
    ) -> UpdateMapResponseTypeDef:
        """
        Updates the specified properties of a given map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_map)
        """

    def update_place_index(
        self,
        *,
        IndexName: str,
        DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        PricingPlan: PricingPlanType = None
    ) -> UpdatePlaceIndexResponseTypeDef:
        """
        Updates the specified properties of a given place index resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_place_index)
        """

    def update_route_calculator(
        self, *, CalculatorName: str, Description: str = None, PricingPlan: PricingPlanType = None
    ) -> UpdateRouteCalculatorResponseTypeDef:
        """
        Updates the specified properties for a given route calculator resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_route_calculator)
        """

    def update_tracker(
        self,
        *,
        TrackerName: str,
        Description: str = None,
        EventBridgeEnabled: bool = None,
        KmsKeyEnableGeospatialQueries: bool = None,
        PositionFiltering: PositionFilteringType = None,
        PricingPlan: PricingPlanType = None,
        PricingPlanDataSource: str = None
    ) -> UpdateTrackerResponseTypeDef:
        """
        Updates the specified properties of a given tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Client.update_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#update_tracker)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_device_position_history"]
    ) -> GetDevicePositionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#getdevicepositionhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_positions"]
    ) -> ListDevicePositionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListDevicePositions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listdevicepositionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geofence_collections"]
    ) -> ListGeofenceCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencecollectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_geofences"]) -> ListGeofencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListGeofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_keys"]) -> ListKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listkeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_maps"]) -> ListMapsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListMaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listmapspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_place_indexes"]
    ) -> ListPlaceIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listplaceindexespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_route_calculators"]
    ) -> ListRouteCalculatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListRouteCalculators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listroutecalculatorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tracker_consumers"]
    ) -> ListTrackerConsumersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerconsumerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trackers"]) -> ListTrackersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/location.html#LocationService.Paginator.ListTrackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerspaginator)
        """
