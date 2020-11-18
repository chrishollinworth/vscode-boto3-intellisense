# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mediatailor service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediatailor import MediaTailorClient
    from mypy_boto3_mediatailor.paginator import (
        ListPlaybackConfigurationsPaginator,
    )

    client: MediaTailorClient = boto3.client("mediatailor")

    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediatailor.type_defs import (
    ListPlaybackConfigurationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListPlaybackConfigurationsPaginator",)


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlaybackConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaybackConfigurationsResponseTypeDef]:
        """
        [ListPlaybackConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations.paginate)
        """
