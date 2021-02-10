"""
Main interface for location service client

Usage::

    ```python
    import boto3
    from mypy_boto3_location import LocationServiceClient

    client: LocationServiceClient = boto3.client("location")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_location.paginator import (
    GetDevicePositionHistoryPaginator,
    ListGeofenceCollectionsPaginator,
    ListGeofencesPaginator,
    ListMapsPaginator,
    ListPlaceIndexesPaginator,
    ListTrackerConsumersPaginator,
    ListTrackersPaginator,
)
from mypy_boto3_location.type_defs import (
    BatchDeleteGeofenceResponseTypeDef,
    BatchEvaluateGeofencesResponseTypeDef,
    BatchGetDevicePositionResponseTypeDef,
    BatchPutGeofenceRequestEntryTypeDef,
    BatchPutGeofenceResponseTypeDef,
    BatchUpdateDevicePositionResponseTypeDef,
    CreateGeofenceCollectionResponseTypeDef,
    CreateMapResponseTypeDef,
    CreatePlaceIndexResponseTypeDef,
    CreateTrackerResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DescribeGeofenceCollectionResponseTypeDef,
    DescribeMapResponseTypeDef,
    DescribePlaceIndexResponseTypeDef,
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
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesResponseTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersResponseTypeDef,
    MapConfigurationTypeDef,
    PutGeofenceResponseTypeDef,
    SearchPlaceIndexForPositionResponseTypeDef,
    SearchPlaceIndexForTextResponseTypeDef,
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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LocationServiceClient:
    """
    [LocationService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_tracker_consumer(self, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        [Client.associate_tracker_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.associate_tracker_consumer)
        """

    def batch_delete_geofence(
        self, CollectionName: str, GeofenceIds: List[str]
    ) -> BatchDeleteGeofenceResponseTypeDef:
        """
        [Client.batch_delete_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.batch_delete_geofence)
        """

    def batch_evaluate_geofences(
        self, CollectionName: str, DevicePositionUpdates: List[DevicePositionUpdateTypeDef]
    ) -> BatchEvaluateGeofencesResponseTypeDef:
        """
        [Client.batch_evaluate_geofences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.batch_evaluate_geofences)
        """

    def batch_get_device_position(
        self, DeviceIds: List[str], TrackerName: str
    ) -> BatchGetDevicePositionResponseTypeDef:
        """
        [Client.batch_get_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.batch_get_device_position)
        """

    def batch_put_geofence(
        self, CollectionName: str, Entries: List[BatchPutGeofenceRequestEntryTypeDef]
    ) -> BatchPutGeofenceResponseTypeDef:
        """
        [Client.batch_put_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.batch_put_geofence)
        """

    def batch_update_device_position(
        self, TrackerName: str, Updates: List[DevicePositionUpdateTypeDef]
    ) -> BatchUpdateDevicePositionResponseTypeDef:
        """
        [Client.batch_update_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.batch_update_device_position)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.can_paginate)
        """

    def create_geofence_collection(
        self,
        CollectionName: str,
        PricingPlan: Literal["RequestBasedUsage", "MobileAssetTracking", "MobileAssetManagement"],
        Description: str = None,
    ) -> CreateGeofenceCollectionResponseTypeDef:
        """
        [Client.create_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.create_geofence_collection)
        """

    def create_map(
        self,
        Configuration: "MapConfigurationTypeDef",
        MapName: str,
        PricingPlan: Literal["RequestBasedUsage", "MobileAssetTracking", "MobileAssetManagement"],
        Description: str = None,
    ) -> CreateMapResponseTypeDef:
        """
        [Client.create_map documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.create_map)
        """

    def create_place_index(
        self,
        DataSource: str,
        IndexName: str,
        PricingPlan: Literal["RequestBasedUsage", "MobileAssetTracking", "MobileAssetManagement"],
        DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
    ) -> CreatePlaceIndexResponseTypeDef:
        """
        [Client.create_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.create_place_index)
        """

    def create_tracker(
        self,
        PricingPlan: Literal["RequestBasedUsage", "MobileAssetTracking", "MobileAssetManagement"],
        TrackerName: str,
        Description: str = None,
    ) -> CreateTrackerResponseTypeDef:
        """
        [Client.create_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.create_tracker)
        """

    def delete_geofence_collection(self, CollectionName: str) -> Dict[str, Any]:
        """
        [Client.delete_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.delete_geofence_collection)
        """

    def delete_map(self, MapName: str) -> Dict[str, Any]:
        """
        [Client.delete_map documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.delete_map)
        """

    def delete_place_index(self, IndexName: str) -> Dict[str, Any]:
        """
        [Client.delete_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.delete_place_index)
        """

    def delete_tracker(self, TrackerName: str) -> Dict[str, Any]:
        """
        [Client.delete_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.delete_tracker)
        """

    def describe_geofence_collection(
        self, CollectionName: str
    ) -> DescribeGeofenceCollectionResponseTypeDef:
        """
        [Client.describe_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.describe_geofence_collection)
        """

    def describe_map(self, MapName: str) -> DescribeMapResponseTypeDef:
        """
        [Client.describe_map documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.describe_map)
        """

    def describe_place_index(self, IndexName: str) -> DescribePlaceIndexResponseTypeDef:
        """
        [Client.describe_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.describe_place_index)
        """

    def describe_tracker(self, TrackerName: str) -> DescribeTrackerResponseTypeDef:
        """
        [Client.describe_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.describe_tracker)
        """

    def disassociate_tracker_consumer(self, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_tracker_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.disassociate_tracker_consumer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.generate_presigned_url)
        """

    def get_device_position(
        self, DeviceId: str, TrackerName: str
    ) -> GetDevicePositionResponseTypeDef:
        """
        [Client.get_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_device_position)
        """

    def get_device_position_history(
        self,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: datetime = None,
        NextToken: str = None,
        StartTimeInclusive: datetime = None,
    ) -> GetDevicePositionHistoryResponseTypeDef:
        """
        [Client.get_device_position_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_device_position_history)
        """

    def get_geofence(self, CollectionName: str, GeofenceId: str) -> GetGeofenceResponseTypeDef:
        """
        [Client.get_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_geofence)
        """

    def get_map_glyphs(
        self, FontStack: str, FontUnicodeRange: str, MapName: str
    ) -> GetMapGlyphsResponseTypeDef:
        """
        [Client.get_map_glyphs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_map_glyphs)
        """

    def get_map_sprites(self, FileName: str, MapName: str) -> GetMapSpritesResponseTypeDef:
        """
        [Client.get_map_sprites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_map_sprites)
        """

    def get_map_style_descriptor(self, MapName: str) -> GetMapStyleDescriptorResponseTypeDef:
        """
        [Client.get_map_style_descriptor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_map_style_descriptor)
        """

    def get_map_tile(self, MapName: str, X: str, Y: str, Z: str) -> GetMapTileResponseTypeDef:
        """
        [Client.get_map_tile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.get_map_tile)
        """

    def list_geofence_collections(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListGeofenceCollectionsResponseTypeDef:
        """
        [Client.list_geofence_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_geofence_collections)
        """

    def list_geofences(
        self, CollectionName: str, NextToken: str = None
    ) -> ListGeofencesResponseTypeDef:
        """
        [Client.list_geofences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_geofences)
        """

    def list_maps(self, MaxResults: int = None, NextToken: str = None) -> ListMapsResponseTypeDef:
        """
        [Client.list_maps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_maps)
        """

    def list_place_indexes(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaceIndexesResponseTypeDef:
        """
        [Client.list_place_indexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_place_indexes)
        """

    def list_tracker_consumers(
        self, TrackerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackerConsumersResponseTypeDef:
        """
        [Client.list_tracker_consumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_tracker_consumers)
        """

    def list_trackers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackersResponseTypeDef:
        """
        [Client.list_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.list_trackers)
        """

    def put_geofence(
        self, CollectionName: str, GeofenceId: str, Geometry: "GeofenceGeometryTypeDef"
    ) -> PutGeofenceResponseTypeDef:
        """
        [Client.put_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.put_geofence)
        """

    def search_place_index_for_position(
        self, IndexName: str, Position: List[float], MaxResults: int = None
    ) -> SearchPlaceIndexForPositionResponseTypeDef:
        """
        [Client.search_place_index_for_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.search_place_index_for_position)
        """

    def search_place_index_for_text(
        self,
        IndexName: str,
        Text: str,
        BiasPosition: List[float] = None,
        FilterBBox: List[float] = None,
        FilterCountries: List[str] = None,
        MaxResults: int = None,
    ) -> SearchPlaceIndexForTextResponseTypeDef:
        """
        [Client.search_place_index_for_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Client.search_place_index_for_text)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_device_position_history"]
    ) -> GetDevicePositionHistoryPaginator:
        """
        [Paginator.GetDevicePositionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geofence_collections"]
    ) -> ListGeofenceCollectionsPaginator:
        """
        [Paginator.ListGeofenceCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_geofences"]) -> ListGeofencesPaginator:
        """
        [Paginator.ListGeofences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListGeofences)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_maps"]) -> ListMapsPaginator:
        """
        [Paginator.ListMaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListMaps)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_place_indexes"]
    ) -> ListPlaceIndexesPaginator:
        """
        [Paginator.ListPlaceIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tracker_consumers"]
    ) -> ListTrackerConsumersPaginator:
        """
        [Paginator.ListTrackerConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trackers"]) -> ListTrackersPaginator:
        """
        [Paginator.ListTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/location.html#LocationService.Paginator.ListTrackers)
        """
