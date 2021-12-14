"""
Type annotations for groundstation service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_groundstation import GroundStationClient

    client: GroundStationClient = boto3.client("groundstation")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ConfigCapabilityTypeType, ContactStatusType
from .paginator import (
    ListConfigsPaginator,
    ListContactsPaginator,
    ListDataflowEndpointGroupsPaginator,
    ListGroundStationsPaginator,
    ListMissionProfilesPaginator,
    ListSatellitesPaginator,
)
from .type_defs import (
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

class GroundStationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        GroundStationClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#can_paginate)
        """
    def cancel_contact(self, *, contactId: str) -> ContactIdResponseTypeDef:
        """
        Cancels a contact with a specified contact ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.cancel_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#cancel_contact)
        """
    def create_config(
        self, *, configData: "ConfigTypeDataTypeDef", name: str, tags: Dict[str, str] = None
    ) -> ConfigIdResponseTypeDef:
        """
        Creates a `Config` with the specified `configData` parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.create_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#create_config)
        """
    def create_dataflow_endpoint_group(
        self, *, endpointDetails: List["EndpointDetailsTypeDef"], tags: Dict[str, str] = None
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        Creates a `DataflowEndpoint` group containing the specified list of
        `DataflowEndpoint` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.create_dataflow_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#create_dataflow_endpoint_group)
        """
    def create_mission_profile(
        self,
        *,
        dataflowEdges: List[List[str]],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, str] = None
    ) -> MissionProfileIdResponseTypeDef:
        """
        Creates a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.create_mission_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#create_mission_profile)
        """
    def delete_config(
        self, *, configId: str, configType: ConfigCapabilityTypeType
    ) -> ConfigIdResponseTypeDef:
        """
        Deletes a `Config` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.delete_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#delete_config)
        """
    def delete_dataflow_endpoint_group(
        self, *, dataflowEndpointGroupId: str
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        Deletes a dataflow endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.delete_dataflow_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#delete_dataflow_endpoint_group)
        """
    def delete_mission_profile(self, *, missionProfileId: str) -> MissionProfileIdResponseTypeDef:
        """
        Deletes a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.delete_mission_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#delete_mission_profile)
        """
    def describe_contact(self, *, contactId: str) -> DescribeContactResponseTypeDef:
        """
        Describes an existing contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.describe_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#describe_contact)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#generate_presigned_url)
        """
    def get_config(
        self, *, configId: str, configType: ConfigCapabilityTypeType
    ) -> GetConfigResponseTypeDef:
        """
        Returns `Config` information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.get_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#get_config)
        """
    def get_dataflow_endpoint_group(
        self, *, dataflowEndpointGroupId: str
    ) -> GetDataflowEndpointGroupResponseTypeDef:
        """
        Returns the dataflow endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.get_dataflow_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#get_dataflow_endpoint_group)
        """
    def get_minute_usage(self, *, month: int, year: int) -> GetMinuteUsageResponseTypeDef:
        """
        Returns the number of minutes used by account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.get_minute_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#get_minute_usage)
        """
    def get_mission_profile(self, *, missionProfileId: str) -> GetMissionProfileResponseTypeDef:
        """
        Returns a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.get_mission_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#get_mission_profile)
        """
    def get_satellite(self, *, satelliteId: str) -> GetSatelliteResponseTypeDef:
        """
        Returns a satellite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.get_satellite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#get_satellite)
        """
    def list_configs(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListConfigsResponseTypeDef:
        """
        Returns a list of `Config` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_configs)
        """
    def list_contacts(
        self,
        *,
        endTime: Union[datetime, str],
        startTime: Union[datetime, str],
        statusList: List[ContactStatusType],
        groundStation: str = None,
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None
    ) -> ListContactsResponseTypeDef:
        """
        Returns a list of contacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_contacts)
        """
    def list_dataflow_endpoint_groups(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListDataflowEndpointGroupsResponseTypeDef:
        """
        Returns a list of `DataflowEndpoint` groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_dataflow_endpoint_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_dataflow_endpoint_groups)
        """
    def list_ground_stations(
        self, *, maxResults: int = None, nextToken: str = None, satelliteId: str = None
    ) -> ListGroundStationsResponseTypeDef:
        """
        Returns a list of ground stations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_ground_stations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_ground_stations)
        """
    def list_mission_profiles(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListMissionProfilesResponseTypeDef:
        """
        Returns a list of mission profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_mission_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_mission_profiles)
        """
    def list_satellites(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSatellitesResponseTypeDef:
        """
        Returns a list of satellites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_satellites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_satellites)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#list_tags_for_resource)
        """
    def reserve_contact(
        self,
        *,
        endTime: Union[datetime, str],
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: Union[datetime, str],
        tags: Dict[str, str] = None
    ) -> ContactIdResponseTypeDef:
        """
        Reserves a contact using specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.reserve_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#reserve_contact)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deassigns a resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#untag_resource)
        """
    def update_config(
        self,
        *,
        configData: "ConfigTypeDataTypeDef",
        configId: str,
        configType: ConfigCapabilityTypeType,
        name: str
    ) -> ConfigIdResponseTypeDef:
        """
        Updates the `Config` used when scheduling contacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.update_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#update_config)
        """
    def update_mission_profile(
        self,
        *,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[List[str]] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None
    ) -> MissionProfileIdResponseTypeDef:
        """
        Updates a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Client.update_mission_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client.html#update_mission_profile)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_configs"]) -> ListConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_contacts"]) -> ListContactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listcontactspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> ListDataflowEndpointGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listdataflowendpointgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ground_stations"]
    ) -> ListGroundStationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listgroundstationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_mission_profiles"]
    ) -> ListMissionProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listmissionprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_satellites"]) -> ListSatellitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators.html#listsatellitespaginator)
        """
