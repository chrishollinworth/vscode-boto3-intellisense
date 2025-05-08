"""
Type annotations for groundstation service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_groundstation.client import GroundStationClient
    from mypy_boto3_groundstation.paginator import (
        ListConfigsPaginator,
        ListContactsPaginator,
        ListDataflowEndpointGroupsPaginator,
        ListEphemeridesPaginator,
        ListGroundStationsPaginator,
        ListMissionProfilesPaginator,
        ListSatellitesPaginator,
    )

    session = Session()
    client: GroundStationClient = session.client("groundstation")

    list_configs_paginator: ListConfigsPaginator = client.get_paginator("list_configs")
    list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
    list_dataflow_endpoint_groups_paginator: ListDataflowEndpointGroupsPaginator = client.get_paginator("list_dataflow_endpoint_groups")
    list_ephemerides_paginator: ListEphemeridesPaginator = client.get_paginator("list_ephemerides")
    list_ground_stations_paginator: ListGroundStationsPaginator = client.get_paginator("list_ground_stations")
    list_mission_profiles_paginator: ListMissionProfilesPaginator = client.get_paginator("list_mission_profiles")
    list_satellites_paginator: ListSatellitesPaginator = client.get_paginator("list_satellites")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConfigsRequestPaginateTypeDef,
    ListConfigsResponseTypeDef,
    ListContactsRequestPaginateTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsRequestPaginateTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListEphemeridesRequestPaginateTypeDef,
    ListEphemeridesResponseTypeDef,
    ListGroundStationsRequestPaginateTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesRequestPaginateTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesRequestPaginateTypeDef,
    ListSatellitesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListEphemeridesPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)

if TYPE_CHECKING:
    _ListConfigsPaginatorBase = Paginator[ListConfigsResponseTypeDef]
else:
    _ListConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConfigsPaginator(_ListConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListConfigs.html#GroundStation.Paginator.ListConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListConfigs.html#GroundStation.Paginator.ListConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listconfigspaginator)
        """

if TYPE_CHECKING:
    _ListContactsPaginatorBase = Paginator[ListContactsResponseTypeDef]
else:
    _ListContactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContactsPaginator(_ListContactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListContacts.html#GroundStation.Paginator.ListContacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listcontactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContactsRequestPaginateTypeDef]
    ) -> PageIterator[ListContactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListContacts.html#GroundStation.Paginator.ListContacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listcontactspaginator)
        """

if TYPE_CHECKING:
    _ListDataflowEndpointGroupsPaginatorBase = Paginator[ListDataflowEndpointGroupsResponseTypeDef]
else:
    _ListDataflowEndpointGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataflowEndpointGroupsPaginator(_ListDataflowEndpointGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListDataflowEndpointGroups.html#GroundStation.Paginator.ListDataflowEndpointGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listdataflowendpointgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataflowEndpointGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataflowEndpointGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListDataflowEndpointGroups.html#GroundStation.Paginator.ListDataflowEndpointGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listdataflowendpointgroupspaginator)
        """

if TYPE_CHECKING:
    _ListEphemeridesPaginatorBase = Paginator[ListEphemeridesResponseTypeDef]
else:
    _ListEphemeridesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEphemeridesPaginator(_ListEphemeridesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListEphemerides.html#GroundStation.Paginator.ListEphemerides)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listephemeridespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEphemeridesRequestPaginateTypeDef]
    ) -> PageIterator[ListEphemeridesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListEphemerides.html#GroundStation.Paginator.ListEphemerides.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listephemeridespaginator)
        """

if TYPE_CHECKING:
    _ListGroundStationsPaginatorBase = Paginator[ListGroundStationsResponseTypeDef]
else:
    _ListGroundStationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroundStationsPaginator(_ListGroundStationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListGroundStations.html#GroundStation.Paginator.ListGroundStations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listgroundstationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroundStationsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroundStationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListGroundStations.html#GroundStation.Paginator.ListGroundStations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listgroundstationspaginator)
        """

if TYPE_CHECKING:
    _ListMissionProfilesPaginatorBase = Paginator[ListMissionProfilesResponseTypeDef]
else:
    _ListMissionProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMissionProfilesPaginator(_ListMissionProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListMissionProfiles.html#GroundStation.Paginator.ListMissionProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listmissionprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMissionProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListMissionProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListMissionProfiles.html#GroundStation.Paginator.ListMissionProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listmissionprofilespaginator)
        """

if TYPE_CHECKING:
    _ListSatellitesPaginatorBase = Paginator[ListSatellitesResponseTypeDef]
else:
    _ListSatellitesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSatellitesPaginator(_ListSatellitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListSatellites.html#GroundStation.Paginator.ListSatellites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listsatellitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSatellitesRequestPaginateTypeDef]
    ) -> PageIterator[ListSatellitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation/paginator/ListSatellites.html#GroundStation.Paginator.ListSatellites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/paginators/#listsatellitespaginator)
        """
