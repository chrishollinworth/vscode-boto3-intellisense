"""
Type annotations for mediatailor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediatailor.client import MediaTailorClient
    from mypy_boto3_mediatailor.paginator import (
        GetChannelSchedulePaginator,
        ListAlertsPaginator,
        ListChannelsPaginator,
        ListLiveSourcesPaginator,
        ListPlaybackConfigurationsPaginator,
        ListPrefetchSchedulesPaginator,
        ListSourceLocationsPaginator,
        ListVodSourcesPaginator,
    )

    session = Session()
    client: MediaTailorClient = session.client("mediatailor")

    get_channel_schedule_paginator: GetChannelSchedulePaginator = client.get_paginator("get_channel_schedule")
    list_alerts_paginator: ListAlertsPaginator = client.get_paginator("list_alerts")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_live_sources_paginator: ListLiveSourcesPaginator = client.get_paginator("list_live_sources")
    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
    list_prefetch_schedules_paginator: ListPrefetchSchedulesPaginator = client.get_paginator("list_prefetch_schedules")
    list_source_locations_paginator: ListSourceLocationsPaginator = client.get_paginator("list_source_locations")
    list_vod_sources_paginator: ListVodSourcesPaginator = client.get_paginator("list_vod_sources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetChannelScheduleRequestPaginateTypeDef,
    GetChannelScheduleResponseTypeDef,
    ListAlertsRequestPaginateTypeDef,
    ListAlertsResponseTypeDef,
    ListChannelsRequestPaginateTypeDef,
    ListChannelsResponseTypeDef,
    ListLiveSourcesRequestPaginateTypeDef,
    ListLiveSourcesResponseTypeDef,
    ListPlaybackConfigurationsRequestPaginateTypeDef,
    ListPlaybackConfigurationsResponseTypeDef,
    ListPrefetchSchedulesRequestPaginateTypeDef,
    ListPrefetchSchedulesResponseTypeDef,
    ListSourceLocationsRequestPaginateTypeDef,
    ListSourceLocationsResponseTypeDef,
    ListVodSourcesRequestPaginateTypeDef,
    ListVodSourcesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetChannelSchedulePaginator",
    "ListAlertsPaginator",
    "ListChannelsPaginator",
    "ListLiveSourcesPaginator",
    "ListPlaybackConfigurationsPaginator",
    "ListPrefetchSchedulesPaginator",
    "ListSourceLocationsPaginator",
    "ListVodSourcesPaginator",
)

if TYPE_CHECKING:
    _GetChannelSchedulePaginatorBase = Paginator[GetChannelScheduleResponseTypeDef]
else:
    _GetChannelSchedulePaginatorBase = Paginator  # type: ignore[assignment]

class GetChannelSchedulePaginator(_GetChannelSchedulePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/GetChannelSchedule.html#MediaTailor.Paginator.GetChannelSchedule)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#getchannelschedulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetChannelScheduleRequestPaginateTypeDef]
    ) -> PageIterator[GetChannelScheduleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/GetChannelSchedule.html#MediaTailor.Paginator.GetChannelSchedule.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#getchannelschedulepaginator)
        """

if TYPE_CHECKING:
    _ListAlertsPaginatorBase = Paginator[ListAlertsResponseTypeDef]
else:
    _ListAlertsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAlertsPaginator(_ListAlertsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListAlerts.html#MediaTailor.Paginator.ListAlerts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listalertspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAlertsRequestPaginateTypeDef]
    ) -> PageIterator[ListAlertsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListAlerts.html#MediaTailor.Paginator.ListAlerts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listalertspaginator)
        """

if TYPE_CHECKING:
    _ListChannelsPaginatorBase = Paginator[ListChannelsResponseTypeDef]
else:
    _ListChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelsPaginator(_ListChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListChannels.html#MediaTailor.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListChannels.html#MediaTailor.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listchannelspaginator)
        """

if TYPE_CHECKING:
    _ListLiveSourcesPaginatorBase = Paginator[ListLiveSourcesResponseTypeDef]
else:
    _ListLiveSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListLiveSourcesPaginator(_ListLiveSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListLiveSources.html#MediaTailor.Paginator.ListLiveSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listlivesourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLiveSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListLiveSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListLiveSources.html#MediaTailor.Paginator.ListLiveSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listlivesourcespaginator)
        """

if TYPE_CHECKING:
    _ListPlaybackConfigurationsPaginatorBase = Paginator[ListPlaybackConfigurationsResponseTypeDef]
else:
    _ListPlaybackConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPlaybackConfigurationsPaginator(_ListPlaybackConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListPlaybackConfigurations.html#MediaTailor.Paginator.ListPlaybackConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listplaybackconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPlaybackConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListPlaybackConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListPlaybackConfigurations.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listplaybackconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListPrefetchSchedulesPaginatorBase = Paginator[ListPrefetchSchedulesResponseTypeDef]
else:
    _ListPrefetchSchedulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrefetchSchedulesPaginator(_ListPrefetchSchedulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListPrefetchSchedules.html#MediaTailor.Paginator.ListPrefetchSchedules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listprefetchschedulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrefetchSchedulesRequestPaginateTypeDef]
    ) -> PageIterator[ListPrefetchSchedulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListPrefetchSchedules.html#MediaTailor.Paginator.ListPrefetchSchedules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listprefetchschedulespaginator)
        """

if TYPE_CHECKING:
    _ListSourceLocationsPaginatorBase = Paginator[ListSourceLocationsResponseTypeDef]
else:
    _ListSourceLocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourceLocationsPaginator(_ListSourceLocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListSourceLocations.html#MediaTailor.Paginator.ListSourceLocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listsourcelocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourceLocationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSourceLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListSourceLocations.html#MediaTailor.Paginator.ListSourceLocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listsourcelocationspaginator)
        """

if TYPE_CHECKING:
    _ListVodSourcesPaginatorBase = Paginator[ListVodSourcesResponseTypeDef]
else:
    _ListVodSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVodSourcesPaginator(_ListVodSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListVodSources.html#MediaTailor.Paginator.ListVodSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listvodsourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVodSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListVodSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor/paginator/ListVodSources.html#MediaTailor.Paginator.ListVodSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators/#listvodsourcespaginator)
        """
