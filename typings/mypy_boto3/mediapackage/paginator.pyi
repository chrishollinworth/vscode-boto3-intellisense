"""
Type annotations for mediapackage service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediapackage.client import MediaPackageClient
    from mypy_boto3_mediapackage.paginator import (
        ListChannelsPaginator,
        ListHarvestJobsPaginator,
        ListOriginEndpointsPaginator,
    )

    session = Session()
    client: MediaPackageClient = session.client("mediapackage")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_harvest_jobs_paginator: ListHarvestJobsPaginator = client.get_paginator("list_harvest_jobs")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChannelsRequestPaginateTypeDef,
    ListChannelsResponseTypeDef,
    ListHarvestJobsRequestPaginateTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsRequestPaginateTypeDef,
    ListOriginEndpointsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListChannelsPaginator", "ListHarvestJobsPaginator", "ListOriginEndpointsPaginator")

if TYPE_CHECKING:
    _ListChannelsPaginatorBase = Paginator[ListChannelsResponseTypeDef]
else:
    _ListChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelsPaginator(_ListChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListChannels.html#MediaPackage.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListChannels.html#MediaPackage.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listchannelspaginator)
        """

if TYPE_CHECKING:
    _ListHarvestJobsPaginatorBase = Paginator[ListHarvestJobsResponseTypeDef]
else:
    _ListHarvestJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHarvestJobsPaginator(_ListHarvestJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListHarvestJobs.html#MediaPackage.Paginator.ListHarvestJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listharvestjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHarvestJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListHarvestJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListHarvestJobs.html#MediaPackage.Paginator.ListHarvestJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listharvestjobspaginator)
        """

if TYPE_CHECKING:
    _ListOriginEndpointsPaginatorBase = Paginator[ListOriginEndpointsResponseTypeDef]
else:
    _ListOriginEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOriginEndpointsPaginator(_ListOriginEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListOriginEndpoints.html#MediaPackage.Paginator.ListOriginEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listoriginendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOriginEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListOriginEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage/paginator/ListOriginEndpoints.html#MediaPackage.Paginator.ListOriginEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/paginators/#listoriginendpointspaginator)
        """
