"""
Type annotations for mediapackage-vod service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediapackage_vod.client import MediaPackageVodClient
    from mypy_boto3_mediapackage_vod.paginator import (
        ListAssetsPaginator,
        ListPackagingConfigurationsPaginator,
        ListPackagingGroupsPaginator,
    )

    session = Session()
    client: MediaPackageVodClient = session.client("mediapackage-vod")

    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_packaging_configurations_paginator: ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
    list_packaging_groups_paginator: ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssetsRequestPaginateTypeDef,
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsRequestPaginateTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsRequestPaginateTypeDef,
    ListPackagingGroupsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)

if TYPE_CHECKING:
    _ListAssetsPaginatorBase = Paginator[ListAssetsResponseTypeDef]
else:
    _ListAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetsPaginator(_ListAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListAssets.html#MediaPackageVod.Paginator.ListAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListAssets.html#MediaPackageVod.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listassetspaginator)
        """

if TYPE_CHECKING:
    _ListPackagingConfigurationsPaginatorBase = Paginator[
        ListPackagingConfigurationsResponseTypeDef
    ]
else:
    _ListPackagingConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackagingConfigurationsPaginator(_ListPackagingConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListPackagingConfigurations.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listpackagingconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackagingConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListPackagingConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListPackagingConfigurations.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listpackagingconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListPackagingGroupsPaginatorBase = Paginator[ListPackagingGroupsResponseTypeDef]
else:
    _ListPackagingGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackagingGroupsPaginator(_ListPackagingGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListPackagingGroups.html#MediaPackageVod.Paginator.ListPackagingGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listpackaginggroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackagingGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListPackagingGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod/paginator/ListPackagingGroups.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators/#listpackaginggroupspaginator)
        """
