"""
Type annotations for codestar service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listprojectspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listprojectspaginator)
        """

class ListResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listresourcespaginator)
    """

    def paginate(
        self, *, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listresourcespaginator)
        """

class ListTeamMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listteammemberspaginator)
    """

    def paginate(
        self, *, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTeamMembersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listteammemberspaginator)
        """

class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listuserprofilespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserProfilesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listuserprofilespaginator)
        """
