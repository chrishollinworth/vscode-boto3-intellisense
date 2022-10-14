"""
Type annotations for nimble service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_nimble import NimbleStudioClient
    from mypy_boto3_nimble.paginator import (
        ListEulaAcceptancesPaginator,
        ListEulasPaginator,
        ListLaunchProfileMembersPaginator,
        ListLaunchProfilesPaginator,
        ListStreamingImagesPaginator,
        ListStreamingSessionsPaginator,
        ListStudioComponentsPaginator,
        ListStudioMembersPaginator,
        ListStudiosPaginator,
    )

    client: NimbleStudioClient = boto3.client("nimble")

    list_eula_acceptances_paginator: ListEulaAcceptancesPaginator = client.get_paginator("list_eula_acceptances")
    list_eulas_paginator: ListEulasPaginator = client.get_paginator("list_eulas")
    list_launch_profile_members_paginator: ListLaunchProfileMembersPaginator = client.get_paginator("list_launch_profile_members")
    list_launch_profiles_paginator: ListLaunchProfilesPaginator = client.get_paginator("list_launch_profiles")
    list_streaming_images_paginator: ListStreamingImagesPaginator = client.get_paginator("list_streaming_images")
    list_streaming_sessions_paginator: ListStreamingSessionsPaginator = client.get_paginator("list_streaming_sessions")
    list_studio_components_paginator: ListStudioComponentsPaginator = client.get_paginator("list_studio_components")
    list_studio_members_paginator: ListStudioMembersPaginator = client.get_paginator("list_studio_members")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import LaunchProfileStateType, StudioComponentStateType, StudioComponentTypeType
from .type_defs import (
    ListEulaAcceptancesResponseTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEulaAcceptancesPaginator",
    "ListEulasPaginator",
    "ListLaunchProfileMembersPaginator",
    "ListLaunchProfilesPaginator",
    "ListStreamingImagesPaginator",
    "ListStreamingSessionsPaginator",
    "ListStudioComponentsPaginator",
    "ListStudioMembersPaginator",
    "ListStudiosPaginator",
)

class ListEulaAcceptancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaacceptancespaginator)
    """

    def paginate(
        self,
        *,
        studioId: str,
        eulaIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEulaAcceptancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaacceptancespaginator)
        """

class ListEulasPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaspaginator)
    """

    def paginate(
        self, *, eulaIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEulasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaspaginator)
        """

class ListLaunchProfileMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilememberspaginator)
    """

    def paginate(
        self,
        *,
        launchProfileId: str,
        studioId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLaunchProfileMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilememberspaginator)
        """

class ListLaunchProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilespaginator)
    """

    def paginate(
        self,
        *,
        studioId: str,
        principalId: str = None,
        states: List[LaunchProfileStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLaunchProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilespaginator)
        """

class ListStreamingImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingimagespaginator)
    """

    def paginate(
        self, *, studioId: str, owner: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamingImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingimagespaginator)
        """

class ListStreamingSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingsessionspaginator)
    """

    def paginate(
        self,
        *,
        studioId: str,
        createdBy: str = None,
        ownedBy: str = None,
        sessionIds: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamingSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingsessionspaginator)
        """

class ListStudioComponentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiocomponentspaginator)
    """

    def paginate(
        self,
        *,
        studioId: str,
        states: List[StudioComponentStateType] = None,
        types: List[StudioComponentTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiocomponentspaginator)
        """

class ListStudioMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiomemberspaginator)
    """

    def paginate(
        self, *, studioId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiomemberspaginator)
        """

class ListStudiosPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiospaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudiosResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiospaginator)
        """
