# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for groundstation service client

Usage::

    ```python
    import boto3
    from mypy_boto3_groundstation import GroundStationClient

    client: GroundStationClient = boto3.client("groundstation")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_groundstation.paginator import (
    ListConfigsPaginator,
    ListContactsPaginator,
    ListDataflowEndpointGroupsPaginator,
    ListGroundStationsPaginator,
    ListMissionProfilesPaginator,
    ListSatellitesPaginator,
)
from mypy_boto3_groundstation.type_defs import (
    ConfigIdResponseTypeDef,
    ConfigTypeDataTypeDef,
    ContactIdResponseTypeDef,
    DataflowEndpointGroupIdResponseTypeDef,
    DescribeContactResponseTypeDef,
    EndpointDetailsTypeDef,
    GetConfigResponseTypeDef,
    GetDataflowEndpointGroupResponseTypeDef,
    GetMinuteUsageResponseTypeDef,
    GetMissionProfileResponseTypeDef,
    GetSatelliteResponseTypeDef,
    ListConfigsResponseTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MissionProfileIdResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GroundStationClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DependencyException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class GroundStationClient:
    """
    [GroundStation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.can_paginate)
        """

    def cancel_contact(self, contactId: str) -> ContactIdResponseTypeDef:
        """
        [Client.cancel_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.cancel_contact)
        """

    def create_config(
        self, configData: "ConfigTypeDataTypeDef", name: str, tags: Dict[str, str] = None
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.create_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.create_config)
        """

    def create_dataflow_endpoint_group(
        self, endpointDetails: List["EndpointDetailsTypeDef"], tags: Dict[str, str] = None
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        [Client.create_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.create_dataflow_endpoint_group)
        """

    def create_mission_profile(
        self,
        dataflowEdges: List[List[str]],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, str] = None,
    ) -> MissionProfileIdResponseTypeDef:
        """
        [Client.create_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.create_mission_profile)
        """

    def delete_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.delete_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.delete_config)
        """

    def delete_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        [Client.delete_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.delete_dataflow_endpoint_group)
        """

    def delete_mission_profile(self, missionProfileId: str) -> MissionProfileIdResponseTypeDef:
        """
        [Client.delete_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.delete_mission_profile)
        """

    def describe_contact(self, contactId: str) -> DescribeContactResponseTypeDef:
        """
        [Client.describe_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.describe_contact)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.generate_presigned_url)
        """

    def get_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> GetConfigResponseTypeDef:
        """
        [Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.get_config)
        """

    def get_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> GetDataflowEndpointGroupResponseTypeDef:
        """
        [Client.get_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.get_dataflow_endpoint_group)
        """

    def get_minute_usage(self, month: int, year: int) -> GetMinuteUsageResponseTypeDef:
        """
        [Client.get_minute_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.get_minute_usage)
        """

    def get_mission_profile(self, missionProfileId: str) -> GetMissionProfileResponseTypeDef:
        """
        [Client.get_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.get_mission_profile)
        """

    def get_satellite(self, satelliteId: str) -> GetSatelliteResponseTypeDef:
        """
        [Client.get_satellite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.get_satellite)
        """

    def list_configs(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListConfigsResponseTypeDef:
        """
        [Client.list_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_configs)
        """

    def list_contacts(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[
            Literal[
                "AVAILABLE",
                "AWS_CANCELLED",
                "AWS_FAILED",
                "CANCELLED",
                "CANCELLING",
                "COMPLETED",
                "FAILED",
                "FAILED_TO_SCHEDULE",
                "PASS",
                "POSTPASS",
                "PREPASS",
                "SCHEDULED",
                "SCHEDULING",
            ]
        ],
        groundStation: str = None,
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None,
    ) -> ListContactsResponseTypeDef:
        """
        [Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_contacts)
        """

    def list_dataflow_endpoint_groups(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListDataflowEndpointGroupsResponseTypeDef:
        """
        [Client.list_dataflow_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_dataflow_endpoint_groups)
        """

    def list_ground_stations(
        self, maxResults: int = None, nextToken: str = None, satelliteId: str = None
    ) -> ListGroundStationsResponseTypeDef:
        """
        [Client.list_ground_stations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_ground_stations)
        """

    def list_mission_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListMissionProfilesResponseTypeDef:
        """
        [Client.list_mission_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_mission_profiles)
        """

    def list_satellites(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListSatellitesResponseTypeDef:
        """
        [Client.list_satellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_satellites)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.list_tags_for_resource)
        """

    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Dict[str, str] = None,
    ) -> ContactIdResponseTypeDef:
        """
        [Client.reserve_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.reserve_contact)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.untag_resource)
        """

    def update_config(
        self,
        configData: "ConfigTypeDataTypeDef",
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        name: str,
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.update_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.update_config)
        """

    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[List[str]] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None,
    ) -> MissionProfileIdResponseTypeDef:
        """
        [Client.update_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Client.update_mission_profile)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_configs"]) -> ListConfigsPaginator:
        """
        [Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contacts"]) -> ListContactsPaginator:
        """
        [Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> ListDataflowEndpointGroupsPaginator:
        """
        [Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ground_stations"]
    ) -> ListGroundStationsPaginator:
        """
        [Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mission_profiles"]
    ) -> ListMissionProfilesPaginator:
        """
        [Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_satellites"]) -> ListSatellitesPaginator:
        """
        [Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
        """
