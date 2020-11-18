# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mobile service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mobile import MobileClient
    from mypy_boto3_mobile.paginator import (
        ListBundlesPaginator,
        ListProjectsPaginator,
    )

    client: MobileClient = boto3.client("mobile")

    list_bundles_paginator: ListBundlesPaginator = client.get_paginator("list_bundles")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mobile.type_defs import (
    ListBundlesResultTypeDef,
    ListProjectsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListBundlesPaginator", "ListProjectsPaginator")


class ListBundlesPaginator(Boto3Paginator):
    """
    [Paginator.ListBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mobile.html#Mobile.Paginator.ListBundles)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBundlesResultTypeDef]:
        """
        [ListBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mobile.html#Mobile.Paginator.ListBundles.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mobile.html#Mobile.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mobile.html#Mobile.Paginator.ListProjects.paginate)
        """
