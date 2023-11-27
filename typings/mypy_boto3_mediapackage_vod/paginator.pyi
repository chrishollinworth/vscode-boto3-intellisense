"""
Type annotations for mediapackage-vod service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listassetspaginator)
    """

    def paginate(
        self, *, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listassetspaginator)
        """

class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackagingconfigurationspaginator)
    """

    def paginate(
        self, *, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackagingconfigurationspaginator)
        """

class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackaginggroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagingGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/paginators.html#listpackaginggroupspaginator)
        """
