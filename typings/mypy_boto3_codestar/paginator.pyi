# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for codestar service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codestar import CodeStarClient
    from mypy_boto3_codestar.paginator import (
        ListProjectsPaginator,
        ListResourcesPaginator,
        ListTeamMembersPaginator,
        ListUserProfilesPaginator,
    )

    client: CodeStarClient = boto3.client("codestar")

    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_team_members_paginator: ListTeamMembersPaginator = client.get_paginator("list_team_members")
    list_user_profiles_paginator: ListUserProfilesPaginator = client.get_paginator("list_user_profiles")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codestar.type_defs import (
    ListProjectsResultTypeDef,
    ListResourcesResultTypeDef,
    ListTeamMembersResultTypeDef,
    ListUserProfilesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListProjectsPaginator",
    "ListResourcesPaginator",
    "ListTeamMembersPaginator",
    "ListUserProfilesPaginator",
)


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListProjects.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListResources)
    """

    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesResultTypeDef]:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListResources.paginate)
        """


class ListTeamMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListTeamMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
    """

    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTeamMembersResultTypeDef]:
        """
        [ListTeamMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserProfilesResultTypeDef]:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles.paginate)
        """
