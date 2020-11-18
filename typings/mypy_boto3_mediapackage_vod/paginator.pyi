# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mediapackage-vod service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediapackage_vod import MediaPackageVodClient
    from mypy_boto3_mediapackage_vod.paginator import (
        ListAssetsPaginator,
        ListPackagingConfigurationsPaginator,
        ListPackagingGroupsPaginator,
    )

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")

    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_packaging_configurations_paginator: ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
    list_packaging_groups_paginator: ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediapackage_vod.type_defs import (
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)


class ListAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
    """

    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetsResponseTypeDef]:
        """
        [ListAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets.paginate)
        """


class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
    """

    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingConfigurationsResponseTypeDef]:
        """
        [ListPackagingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        """


class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingGroupsResponseTypeDef]:
        """
        [ListPackagingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        """
