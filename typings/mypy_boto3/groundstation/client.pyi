"""
Type annotations for groundstation service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_groundstation.client import GroundStationClient

    session = Session()
    client: GroundStationClient = session.client("groundstation")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListConfigsPaginator,
    ListContactsPaginator,
    ListDataflowEndpointGroupsPaginator,
    ListEphemeridesPaginator,
    ListGroundStationsPaginator,
    ListMissionProfilesPaginator,
    ListSatellitesPaginator,
)
from .type_defs import (
    CancelContactRequestTypeDef,
    ConfigIdResponseTypeDef,
    ContactIdResponseTypeDef,
    CreateConfigRequestTypeDef,
    CreateDataflowEndpointGroupRequestTypeDef,
    CreateEphemerisRequestTypeDef,
    CreateMissionProfileRequestTypeDef,
    DataflowEndpointGroupIdResponseTypeDef,
    DeleteConfigRequestTypeDef,
    DeleteDataflowEndpointGroupRequestTypeDef,
    DeleteEphemerisRequestTypeDef,
    DeleteMissionProfileRequestTypeDef,
    DescribeContactRequestTypeDef,
    DescribeContactResponseTypeDef,
    DescribeEphemerisRequestTypeDef,
    DescribeEphemerisResponseTypeDef,
    EphemerisIdResponseTypeDef,
    GetAgentConfigurationRequestTypeDef,
    GetAgentConfigurationResponseTypeDef,
    GetConfigRequestTypeDef,
    GetConfigResponseTypeDef,
    GetDataflowEndpointGroupRequestTypeDef,
    GetDataflowEndpointGroupResponseTypeDef,
    GetMinuteUsageRequestTypeDef,
    GetMinuteUsageResponseTypeDef,
    GetMissionProfileRequestTypeDef,
    GetMissionProfileResponseTypeDef,
    GetSatelliteRequestTypeDef,
    GetSatelliteResponseTypeDef,
    ListConfigsRequestTypeDef,
    ListConfigsResponseTypeDef,
    ListContactsRequestTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsRequestTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListEphemeridesRequestTypeDef,
    ListEphemeridesResponseTypeDef,
    ListGroundStationsRequestTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesRequestTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesRequestTypeDef,
    ListSatellitesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    MissionProfileIdResponseTypeDef,
    RegisterAgentRequestTypeDef,
    RegisterAgentResponseTypeDef,
    ReserveContactRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAgentStatusRequestTypeDef,
    UpdateAgentStatusResponseTypeDef,
    UpdateConfigRequestTypeDef,
    UpdateEphemerisRequestTypeDef,
    UpdateMissionProfileRequestTypeDef,
)
from .waiter import ContactScheduledWaiter

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

__all__ = ("GroundStationClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    DependencyException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class GroundStationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GroundStationClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#generate_presigned_url)
        """

    def cancel_contact(
        self, **kwargs: Unpack[CancelContactRequestTypeDef]
    ) -> ContactIdResponseTypeDef:
        """
        Cancels a contact with a specified contact ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/cancel_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#cancel_contact)
        """

    def create_config(
        self, **kwargs: Unpack[CreateConfigRequestTypeDef]
    ) -> ConfigIdResponseTypeDef:
        """
        Creates a <code>Config</code> with the specified <code>configData</code>
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/create_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#create_config)
        """

    def create_dataflow_endpoint_group(
        self, **kwargs: Unpack[CreateDataflowEndpointGroupRequestTypeDef]
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        Creates a <code>DataflowEndpoint</code> group containing the specified list of
        <code>DataflowEndpoint</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/create_dataflow_endpoint_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#create_dataflow_endpoint_group)
        """

    def create_ephemeris(
        self, **kwargs: Unpack[CreateEphemerisRequestTypeDef]
    ) -> EphemerisIdResponseTypeDef:
        """
        Creates an Ephemeris with the specified <code>EphemerisData</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/create_ephemeris.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#create_ephemeris)
        """

    def create_mission_profile(
        self, **kwargs: Unpack[CreateMissionProfileRequestTypeDef]
    ) -> MissionProfileIdResponseTypeDef:
        """
        Creates a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/create_mission_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#create_mission_profile)
        """

    def delete_config(
        self, **kwargs: Unpack[DeleteConfigRequestTypeDef]
    ) -> ConfigIdResponseTypeDef:
        """
        Deletes a <code>Config</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/delete_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#delete_config)
        """

    def delete_dataflow_endpoint_group(
        self, **kwargs: Unpack[DeleteDataflowEndpointGroupRequestTypeDef]
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        Deletes a dataflow endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/delete_dataflow_endpoint_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#delete_dataflow_endpoint_group)
        """

    def delete_ephemeris(
        self, **kwargs: Unpack[DeleteEphemerisRequestTypeDef]
    ) -> EphemerisIdResponseTypeDef:
        """
        Deletes an ephemeris.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/delete_ephemeris.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#delete_ephemeris)
        """

    def delete_mission_profile(
        self, **kwargs: Unpack[DeleteMissionProfileRequestTypeDef]
    ) -> MissionProfileIdResponseTypeDef:
        """
        Deletes a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/delete_mission_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#delete_mission_profile)
        """

    def describe_contact(
        self, **kwargs: Unpack[DescribeContactRequestTypeDef]
    ) -> DescribeContactResponseTypeDef:
        """
        Describes an existing contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/describe_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#describe_contact)
        """

    def describe_ephemeris(
        self, **kwargs: Unpack[DescribeEphemerisRequestTypeDef]
    ) -> DescribeEphemerisResponseTypeDef:
        """
        Describes an existing ephemeris.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/describe_ephemeris.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#describe_ephemeris)
        """

    def get_agent_configuration(
        self, **kwargs: Unpack[GetAgentConfigurationRequestTypeDef]
    ) -> GetAgentConfigurationResponseTypeDef:
        """
        For use by AWS Ground Station Agent and shouldn't be called directly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_agent_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_agent_configuration)
        """

    def get_config(self, **kwargs: Unpack[GetConfigRequestTypeDef]) -> GetConfigResponseTypeDef:
        """
        Returns <code>Config</code> information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_config)
        """

    def get_dataflow_endpoint_group(
        self, **kwargs: Unpack[GetDataflowEndpointGroupRequestTypeDef]
    ) -> GetDataflowEndpointGroupResponseTypeDef:
        """
        Returns the dataflow endpoint group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_dataflow_endpoint_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_dataflow_endpoint_group)
        """

    def get_minute_usage(
        self, **kwargs: Unpack[GetMinuteUsageRequestTypeDef]
    ) -> GetMinuteUsageResponseTypeDef:
        """
        Returns the number of reserved minutes used by account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_minute_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_minute_usage)
        """

    def get_mission_profile(
        self, **kwargs: Unpack[GetMissionProfileRequestTypeDef]
    ) -> GetMissionProfileResponseTypeDef:
        """
        Returns a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_mission_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_mission_profile)
        """

    def get_satellite(
        self, **kwargs: Unpack[GetSatelliteRequestTypeDef]
    ) -> GetSatelliteResponseTypeDef:
        """
        Returns a satellite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_satellite.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_satellite)
        """

    def list_configs(
        self, **kwargs: Unpack[ListConfigsRequestTypeDef]
    ) -> ListConfigsResponseTypeDef:
        """
        Returns a list of <code>Config</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_configs)
        """

    def list_contacts(
        self, **kwargs: Unpack[ListContactsRequestTypeDef]
    ) -> ListContactsResponseTypeDef:
        """
        Returns a list of contacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_contacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_contacts)
        """

    def list_dataflow_endpoint_groups(
        self, **kwargs: Unpack[ListDataflowEndpointGroupsRequestTypeDef]
    ) -> ListDataflowEndpointGroupsResponseTypeDef:
        """
        Returns a list of <code>DataflowEndpoint</code> groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_dataflow_endpoint_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_dataflow_endpoint_groups)
        """

    def list_ephemerides(
        self, **kwargs: Unpack[ListEphemeridesRequestTypeDef]
    ) -> ListEphemeridesResponseTypeDef:
        """
        List existing ephemerides.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_ephemerides.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_ephemerides)
        """

    def list_ground_stations(
        self, **kwargs: Unpack[ListGroundStationsRequestTypeDef]
    ) -> ListGroundStationsResponseTypeDef:
        """
        Returns a list of ground stations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_ground_stations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_ground_stations)
        """

    def list_mission_profiles(
        self, **kwargs: Unpack[ListMissionProfilesRequestTypeDef]
    ) -> ListMissionProfilesResponseTypeDef:
        """
        Returns a list of mission profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_mission_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_mission_profiles)
        """

    def list_satellites(
        self, **kwargs: Unpack[ListSatellitesRequestTypeDef]
    ) -> ListSatellitesResponseTypeDef:
        """
        Returns a list of satellites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_satellites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_satellites)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#list_tags_for_resource)
        """

    def register_agent(
        self, **kwargs: Unpack[RegisterAgentRequestTypeDef]
    ) -> RegisterAgentResponseTypeDef:
        """
        For use by AWS Ground Station Agent and shouldn't be called directly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/register_agent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#register_agent)
        """

    def reserve_contact(
        self, **kwargs: Unpack[ReserveContactRequestTypeDef]
    ) -> ContactIdResponseTypeDef:
        """
        Reserves a contact using specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/reserve_contact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#reserve_contact)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deassigns a resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#untag_resource)
        """

    def update_agent_status(
        self, **kwargs: Unpack[UpdateAgentStatusRequestTypeDef]
    ) -> UpdateAgentStatusResponseTypeDef:
        """
        For use by AWS Ground Station Agent and shouldn't be called directly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/update_agent_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#update_agent_status)
        """

    def update_config(
        self, **kwargs: Unpack[UpdateConfigRequestTypeDef]
    ) -> ConfigIdResponseTypeDef:
        """
        Updates the <code>Config</code> used when scheduling contacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/update_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#update_config)
        """

    def update_ephemeris(
        self, **kwargs: Unpack[UpdateEphemerisRequestTypeDef]
    ) -> EphemerisIdResponseTypeDef:
        """
        Updates an existing ephemeris.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/update_ephemeris.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#update_ephemeris)
        """

    def update_mission_profile(
        self, **kwargs: Unpack[UpdateMissionProfileRequestTypeDef]
    ) -> MissionProfileIdResponseTypeDef:
        """
        Updates a mission profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/update_mission_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#update_mission_profile)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_configs"]
    ) -> ListConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_contacts"]
    ) -> ListContactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> ListDataflowEndpointGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ephemerides"]
    ) -> ListEphemeridesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ground_stations"]
    ) -> ListGroundStationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_mission_profiles"]
    ) -> ListMissionProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_satellites"]
    ) -> ListSatellitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["contact_scheduled"]
    ) -> ContactScheduledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/client/#get_waiter)
        """
