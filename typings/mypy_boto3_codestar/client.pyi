# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codestar service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar import CodeStarClient

    client: CodeStarClient = boto3.client("codestar")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codestar.paginator import (
    ListProjectsPaginator,
    ListResourcesPaginator,
    ListTeamMembersPaginator,
    ListUserProfilesPaginator,
)
from mypy_boto3_codestar.type_defs import (
    AssociateTeamMemberResultTypeDef,
    CodeTypeDef,
    CreateProjectResultTypeDef,
    CreateUserProfileResultTypeDef,
    DeleteProjectResultTypeDef,
    DeleteUserProfileResultTypeDef,
    DescribeProjectResultTypeDef,
    DescribeUserProfileResultTypeDef,
    ListProjectsResultTypeDef,
    ListResourcesResultTypeDef,
    ListTagsForProjectResultTypeDef,
    ListTeamMembersResultTypeDef,
    ListUserProfilesResultTypeDef,
    TagProjectResultTypeDef,
    ToolchainTypeDef,
    UpdateTeamMemberResultTypeDef,
    UpdateUserProfileResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidServiceRoleException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ProjectAlreadyExistsException: Type[Boto3ClientError]
    ProjectConfigurationException: Type[Boto3ClientError]
    ProjectCreationFailedException: Type[Boto3ClientError]
    ProjectNotFoundException: Type[Boto3ClientError]
    TeamMemberAlreadyAssociatedException: Type[Boto3ClientError]
    TeamMemberNotFoundException: Type[Boto3ClientError]
    UserProfileAlreadyExistsException: Type[Boto3ClientError]
    UserProfileNotFoundException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class CodeStarClient:
    """
    [CodeStar.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client)
    """

    exceptions: Exceptions

    def associate_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str,
        clientRequestToken: str = None,
        remoteAccessAllowed: bool = None,
    ) -> AssociateTeamMemberResultTypeDef:
        """
        [Client.associate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.associate_team_member)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.can_paginate)
        """

    def create_project(
        self,
        name: str,
        id: str,
        description: str = None,
        clientRequestToken: str = None,
        sourceCode: List[CodeTypeDef] = None,
        toolchain: ToolchainTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> CreateProjectResultTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.create_project)
        """

    def create_user_profile(
        self, userArn: str, displayName: str, emailAddress: str, sshPublicKey: str = None
    ) -> CreateUserProfileResultTypeDef:
        """
        [Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.create_user_profile)
        """

    def delete_project(
        self, id: str, clientRequestToken: str = None, deleteStack: bool = None
    ) -> DeleteProjectResultTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.delete_project)
        """

    def delete_user_profile(self, userArn: str) -> DeleteUserProfileResultTypeDef:
        """
        [Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.delete_user_profile)
        """

    def describe_project(self, id: str) -> DescribeProjectResultTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.describe_project)
        """

    def describe_user_profile(self, userArn: str) -> DescribeUserProfileResultTypeDef:
        """
        [Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.describe_user_profile)
        """

    def disassociate_team_member(self, projectId: str, userArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.disassociate_team_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.generate_presigned_url)
        """

    def list_projects(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResultTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.list_projects)
        """

    def list_resources(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResourcesResultTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.list_resources)
        """

    def list_tags_for_project(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForProjectResultTypeDef:
        """
        [Client.list_tags_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.list_tags_for_project)
        """

    def list_team_members(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListTeamMembersResultTypeDef:
        """
        [Client.list_team_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.list_team_members)
        """

    def list_user_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListUserProfilesResultTypeDef:
        """
        [Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.list_user_profiles)
        """

    def tag_project(self, id: str, tags: Dict[str, str]) -> TagProjectResultTypeDef:
        """
        [Client.tag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.tag_project)
        """

    def untag_project(self, id: str, tags: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.untag_project)
        """

    def update_project(self, id: str, name: str = None, description: str = None) -> Dict[str, Any]:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.update_project)
        """

    def update_team_member(
        self,
        projectId: str,
        userArn: str,
        projectRole: str = None,
        remoteAccessAllowed: bool = None,
    ) -> UpdateTeamMemberResultTypeDef:
        """
        [Client.update_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.update_team_member)
        """

    def update_user_profile(
        self,
        userArn: str,
        displayName: str = None,
        emailAddress: str = None,
        sshPublicKey: str = None,
    ) -> UpdateUserProfileResultTypeDef:
        """
        [Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Client.update_user_profile)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Paginator.ListResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_team_members"]
    ) -> ListTeamMembersPaginator:
        """
        [Paginator.ListTeamMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
