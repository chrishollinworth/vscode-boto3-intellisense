"""
Type annotations for nimble service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_nimble import NimbleStudioClient

    client: NimbleStudioClient = boto3.client("nimble")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    LaunchProfileStateType,
    StreamingInstanceTypeType,
    StudioComponentStateType,
    StudioComponentSubtypeType,
    StudioComponentTypeType,
    VolumeRetentionModeType,
)
from .paginator import (
    ListEulaAcceptancesPaginator,
    ListEulasPaginator,
    ListLaunchProfileMembersPaginator,
    ListLaunchProfilesPaginator,
    ListStreamingImagesPaginator,
    ListStreamingSessionBackupsPaginator,
    ListStreamingSessionsPaginator,
    ListStudioComponentsPaginator,
    ListStudioMembersPaginator,
    ListStudiosPaginator,
)
from .type_defs import (
    AcceptEulasResponseTypeDef,
    CreateLaunchProfileResponseTypeDef,
    CreateStreamingImageResponseTypeDef,
    CreateStreamingSessionResponseTypeDef,
    CreateStreamingSessionStreamResponseTypeDef,
    CreateStudioComponentResponseTypeDef,
    CreateStudioResponseTypeDef,
    DeleteLaunchProfileResponseTypeDef,
    DeleteStreamingImageResponseTypeDef,
    DeleteStreamingSessionResponseTypeDef,
    DeleteStudioComponentResponseTypeDef,
    DeleteStudioResponseTypeDef,
    GetEulaResponseTypeDef,
    GetLaunchProfileDetailsResponseTypeDef,
    GetLaunchProfileInitializationResponseTypeDef,
    GetLaunchProfileMemberResponseTypeDef,
    GetLaunchProfileResponseTypeDef,
    GetStreamingImageResponseTypeDef,
    GetStreamingSessionBackupResponseTypeDef,
    GetStreamingSessionResponseTypeDef,
    GetStreamingSessionStreamResponseTypeDef,
    GetStudioComponentResponseTypeDef,
    GetStudioMemberResponseTypeDef,
    GetStudioResponseTypeDef,
    ListEulaAcceptancesResponseTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionBackupsResponseTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NewLaunchProfileMemberTypeDef,
    NewStudioMemberTypeDef,
    ScriptParameterKeyValueTypeDef,
    StartStreamingSessionResponseTypeDef,
    StartStudioSSOConfigurationRepairResponseTypeDef,
    StopStreamingSessionResponseTypeDef,
    StreamConfigurationCreateTypeDef,
    StudioComponentConfigurationTypeDef,
    StudioComponentInitializationScriptTypeDef,
    StudioEncryptionConfigurationTypeDef,
    UpdateLaunchProfileMemberResponseTypeDef,
    UpdateLaunchProfileResponseTypeDef,
    UpdateStreamingImageResponseTypeDef,
    UpdateStudioComponentResponseTypeDef,
    UpdateStudioResponseTypeDef,
)
from .waiter import (
    LaunchProfileDeletedWaiter,
    LaunchProfileReadyWaiter,
    StreamingImageDeletedWaiter,
    StreamingImageReadyWaiter,
    StreamingSessionDeletedWaiter,
    StreamingSessionReadyWaiter,
    StreamingSessionStoppedWaiter,
    StreamingSessionStreamReadyWaiter,
    StudioComponentDeletedWaiter,
    StudioComponentReadyWaiter,
    StudioDeletedWaiter,
    StudioReadyWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NimbleStudioClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NimbleStudioClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NimbleStudioClient exceptions.
        """

    def accept_eulas(
        self, *, studioId: str, clientToken: str = None, eulaIds: List[str] = None
    ) -> AcceptEulasResponseTypeDef:
        """
        Accept EULAs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.accept_eulas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#accept_eulas)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#close)
        """

    def create_launch_profile(
        self,
        *,
        ec2SubnetIds: List[str],
        launchProfileProtocolVersions: List[str],
        name: str,
        streamConfiguration: "StreamConfigurationCreateTypeDef",
        studioComponentIds: List[str],
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateLaunchProfileResponseTypeDef:
        """
        Create a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_launch_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_launch_profile)
        """

    def create_streaming_image(
        self,
        *,
        ec2ImageId: str,
        name: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateStreamingImageResponseTypeDef:
        """
        Creates a streaming image resource in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_streaming_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_streaming_image)
        """

    def create_streaming_session(
        self,
        *,
        launchProfileId: str,
        studioId: str,
        clientToken: str = None,
        ec2InstanceType: StreamingInstanceTypeType = None,
        ownedBy: str = None,
        streamingImageId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateStreamingSessionResponseTypeDef:
        """
        Creates a streaming session in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_streaming_session)
        """

    def create_streaming_session_stream(
        self,
        *,
        sessionId: str,
        studioId: str,
        clientToken: str = None,
        expirationInSeconds: int = None
    ) -> CreateStreamingSessionStreamResponseTypeDef:
        """
        Creates a streaming session stream for a streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_streaming_session_stream)
        """

    def create_studio(
        self,
        *,
        adminRoleArn: str,
        displayName: str,
        studioName: str,
        userRoleArn: str,
        clientToken: str = None,
        studioEncryptionConfiguration: "StudioEncryptionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateStudioResponseTypeDef:
        """
        Create a new studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_studio)
        """

    def create_studio_component(
        self,
        *,
        name: str,
        studioId: str,
        type: StudioComponentTypeType,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        runtimeRoleArn: str = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        secureInitializationRoleArn: str = None,
        subtype: StudioComponentSubtypeType = None,
        tags: Dict[str, str] = None
    ) -> CreateStudioComponentResponseTypeDef:
        """
        Creates a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.create_studio_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#create_studio_component)
        """

    def delete_launch_profile(
        self, *, launchProfileId: str, studioId: str, clientToken: str = None
    ) -> DeleteLaunchProfileResponseTypeDef:
        """
        Permanently delete a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_launch_profile)
        """

    def delete_launch_profile_member(
        self, *, launchProfileId: str, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Delete a user from launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_launch_profile_member)
        """

    def delete_streaming_image(
        self, *, streamingImageId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingImageResponseTypeDef:
        """
        Delete streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_streaming_image)
        """

    def delete_streaming_session(
        self, *, sessionId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingSessionResponseTypeDef:
        """
        Deletes streaming session resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_streaming_session)
        """

    def delete_studio(
        self, *, studioId: str, clientToken: str = None
    ) -> DeleteStudioResponseTypeDef:
        """
        Delete a studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_studio)
        """

    def delete_studio_component(
        self, *, studioComponentId: str, studioId: str, clientToken: str = None
    ) -> DeleteStudioComponentResponseTypeDef:
        """
        Deletes a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_studio_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_studio_component)
        """

    def delete_studio_member(
        self, *, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Delete a user from studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.delete_studio_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#delete_studio_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#generate_presigned_url)
        """

    def get_eula(self, *, eulaId: str) -> GetEulaResponseTypeDef:
        """
        Get EULA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_eula)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_eula)
        """

    def get_launch_profile(
        self, *, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileResponseTypeDef:
        """
        Get a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_launch_profile)
        """

    def get_launch_profile_details(
        self, *, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileDetailsResponseTypeDef:
        """
        Launch profile details include the launch profile resource and summary
        information of resources that are used by, or available to, the launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_launch_profile_details)
        """

    def get_launch_profile_initialization(
        self,
        *,
        launchProfileId: str,
        launchProfileProtocolVersions: List[str],
        launchPurpose: str,
        platform: str,
        studioId: str
    ) -> GetLaunchProfileInitializationResponseTypeDef:
        """
        Get a launch profile initialization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_initialization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_launch_profile_initialization)
        """

    def get_launch_profile_member(
        self, *, launchProfileId: str, principalId: str, studioId: str
    ) -> GetLaunchProfileMemberResponseTypeDef:
        """
        Get a user persona in launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_launch_profile_member)
        """

    def get_streaming_image(
        self, *, streamingImageId: str, studioId: str
    ) -> GetStreamingImageResponseTypeDef:
        """
        Get streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_streaming_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_streaming_image)
        """

    def get_streaming_session(
        self, *, sessionId: str, studioId: str
    ) -> GetStreamingSessionResponseTypeDef:
        """
        Gets StreamingSession resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_streaming_session)
        """

    def get_streaming_session_backup(
        self, *, backupId: str, studioId: str
    ) -> GetStreamingSessionBackupResponseTypeDef:
        """
        Gets `StreamingSessionBackup` resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_streaming_session_backup)
        """

    def get_streaming_session_stream(
        self, *, sessionId: str, streamId: str, studioId: str
    ) -> GetStreamingSessionStreamResponseTypeDef:
        """
        Gets a StreamingSessionStream for a streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_streaming_session_stream)
        """

    def get_studio(self, *, studioId: str) -> GetStudioResponseTypeDef:
        """
        Get a studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_studio)
        """

    def get_studio_component(
        self, *, studioComponentId: str, studioId: str
    ) -> GetStudioComponentResponseTypeDef:
        """
        Gets a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_studio_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_studio_component)
        """

    def get_studio_member(
        self, *, principalId: str, studioId: str
    ) -> GetStudioMemberResponseTypeDef:
        """
        Get a user's membership in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.get_studio_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#get_studio_member)
        """

    def list_eula_acceptances(
        self, *, studioId: str, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulaAcceptancesResponseTypeDef:
        """
        List EULA acceptances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_eula_acceptances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_eula_acceptances)
        """

    def list_eulas(
        self, *, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulasResponseTypeDef:
        """
        List EULAs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_eulas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_eulas)
        """

    def list_launch_profile_members(
        self, *, launchProfileId: str, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListLaunchProfileMembersResponseTypeDef:
        """
        Get all users in a given launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_launch_profile_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_launch_profile_members)
        """

    def list_launch_profiles(
        self,
        *,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None,
        states: List[LaunchProfileStateType] = None
    ) -> ListLaunchProfilesResponseTypeDef:
        """
        List all the launch profiles a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_launch_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_launch_profiles)
        """

    def list_streaming_images(
        self, *, studioId: str, nextToken: str = None, owner: str = None
    ) -> ListStreamingImagesResponseTypeDef:
        """
        List the streaming image resources available to this studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_streaming_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_streaming_images)
        """

    def list_streaming_session_backups(
        self, *, studioId: str, nextToken: str = None, ownedBy: str = None
    ) -> ListStreamingSessionBackupsResponseTypeDef:
        """
        Lists the backups of a streaming session in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_streaming_session_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_streaming_session_backups)
        """

    def list_streaming_sessions(
        self,
        *,
        studioId: str,
        createdBy: str = None,
        nextToken: str = None,
        ownedBy: str = None,
        sessionIds: str = None
    ) -> ListStreamingSessionsResponseTypeDef:
        """
        Lists the streaming sessions in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_streaming_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_streaming_sessions)
        """

    def list_studio_components(
        self,
        *,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        states: List[StudioComponentStateType] = None,
        types: List[StudioComponentTypeType] = None
    ) -> ListStudioComponentsResponseTypeDef:
        """
        Lists the `StudioComponents` in a studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_studio_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_studio_components)
        """

    def list_studio_members(
        self, *, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListStudioMembersResponseTypeDef:
        """
        Get all users in a given studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_studio_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_studio_members)
        """

    def list_studios(self, *, nextToken: str = None) -> ListStudiosResponseTypeDef:
        """
        List studios in your Amazon Web Services accounts in the requested Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_studios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_studios)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets the tags for a resource, given its Amazon Resource Names (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#list_tags_for_resource)
        """

    def put_launch_profile_members(
        self,
        *,
        identityStoreId: str,
        launchProfileId: str,
        members: List["NewLaunchProfileMemberTypeDef"],
        studioId: str,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Add/update users with given persona to launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.put_launch_profile_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#put_launch_profile_members)
        """

    def put_studio_members(
        self,
        *,
        identityStoreId: str,
        members: List["NewStudioMemberTypeDef"],
        studioId: str,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Add/update users with given persona to studio membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.put_studio_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#put_studio_members)
        """

    def start_streaming_session(
        self, *, sessionId: str, studioId: str, backupId: str = None, clientToken: str = None
    ) -> StartStreamingSessionResponseTypeDef:
        """
        Transitions sessions from the `STOPPED` state into the `READY` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.start_streaming_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#start_streaming_session)
        """

    def start_studio_sso_configuration_repair(
        self, *, studioId: str, clientToken: str = None
    ) -> StartStudioSSOConfigurationRepairResponseTypeDef:
        """
        Repairs the IAM Identity Center configuration for a given studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.start_studio_sso_configuration_repair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#start_studio_sso_configuration_repair)
        """

    def stop_streaming_session(
        self,
        *,
        sessionId: str,
        studioId: str,
        clientToken: str = None,
        volumeRetentionMode: VolumeRetentionModeType = None
    ) -> StopStreamingSessionResponseTypeDef:
        """
        Transitions sessions from the `READY` state into the `STOPPED` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.stop_streaming_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#stop_streaming_session)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Creates tags for a resource, given its ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#untag_resource)
        """

    def update_launch_profile(
        self,
        *,
        launchProfileId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        launchProfileProtocolVersions: List[str] = None,
        name: str = None,
        streamConfiguration: "StreamConfigurationCreateTypeDef" = None,
        studioComponentIds: List[str] = None
    ) -> UpdateLaunchProfileResponseTypeDef:
        """
        Update a launch profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#update_launch_profile)
        """

    def update_launch_profile_member(
        self,
        *,
        launchProfileId: str,
        persona: Literal["USER"],
        principalId: str,
        studioId: str,
        clientToken: str = None
    ) -> UpdateLaunchProfileMemberResponseTypeDef:
        """
        Update a user persona in launch profile membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#update_launch_profile_member)
        """

    def update_streaming_image(
        self,
        *,
        streamingImageId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        name: str = None
    ) -> UpdateStreamingImageResponseTypeDef:
        """
        Update streaming image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.update_streaming_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#update_streaming_image)
        """

    def update_studio(
        self,
        *,
        studioId: str,
        adminRoleArn: str = None,
        clientToken: str = None,
        displayName: str = None,
        userRoleArn: str = None
    ) -> UpdateStudioResponseTypeDef:
        """
        Update a Studio resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.update_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#update_studio)
        """

    def update_studio_component(
        self,
        *,
        studioComponentId: str,
        studioId: str,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        name: str = None,
        runtimeRoleArn: str = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        secureInitializationRoleArn: str = None,
        subtype: StudioComponentSubtypeType = None,
        type: StudioComponentTypeType = None
    ) -> UpdateStudioComponentResponseTypeDef:
        """
        Updates a studio component resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Client.update_studio_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/client.html#update_studio_component)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_eula_acceptances"]
    ) -> ListEulaAcceptancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaacceptancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_eulas"]) -> ListEulasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listeulaspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profile_members"]
    ) -> ListLaunchProfileMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilememberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_profiles"]
    ) -> ListLaunchProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#listlaunchprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_images"]
    ) -> ListStreamingImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_session_backups"]
    ) -> ListStreamingSessionBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessionBackups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingsessionbackupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_streaming_sessions"]
    ) -> ListStreamingSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststreamingsessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_components"]
    ) -> ListStudioComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiocomponentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_members"]
    ) -> ListStudioMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiomemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators.html#liststudiospaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["launch_profile_deleted"]
    ) -> LaunchProfileDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofiledeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["launch_profile_ready"]) -> LaunchProfileReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.LaunchProfileReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#launchprofilereadywaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_image_deleted"]
    ) -> StreamingImageDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagedeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_image_ready"]
    ) -> StreamingImageReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingImageReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingimagereadywaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_deleted"]
    ) -> StreamingSessionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessiondeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_ready"]
    ) -> StreamingSessionReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionreadywaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_stopped"]
    ) -> StreamingSessionStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstoppedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["streaming_session_stream_ready"]
    ) -> StreamingSessionStreamReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StreamingSessionStreamReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#streamingsessionstreamreadywaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["studio_component_deleted"]
    ) -> StudioComponentDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["studio_component_ready"]
    ) -> StudioComponentReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StudioComponentReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiocomponentreadywaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["studio_deleted"]) -> StudioDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StudioDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studiodeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["studio_ready"]) -> StudioReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/nimble.html#NimbleStudio.Waiter.StudioReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/waiters.html#studioreadywaiter)
        """
