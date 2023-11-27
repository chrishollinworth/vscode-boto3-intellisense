"""
Type annotations for iot1click-projects service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iot1click_projects import IoT1ClickProjectsClient
    from mypy_boto3_iot1click_projects.paginator import (
        ListPlacementsPaginator,
        ListProjectsPaginator,
    )

    client: IoT1ClickProjectsClient = boto3.client("iot1click-projects")

    list_placements_paginator: ListPlacementsPaginator = client.get_paginator("list_placements")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListPlacementsResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListPlacementsPaginator", "ListProjectsPaginator")

class ListPlacementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listplacementspaginator)
    """

    def paginate(
        self, *, projectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlacementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listplacementspaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listprojectspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listprojectspaginator)
        """
