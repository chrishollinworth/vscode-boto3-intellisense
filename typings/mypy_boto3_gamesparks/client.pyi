"""
Type annotations for gamesparks service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_gamesparks import GameSparksClient

    client: GameSparksClient = boto3.client("gamesparks")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListExtensionsPaginator,
    ListExtensionVersionsPaginator,
    ListGamesPaginator,
    ListGeneratedCodeJobsPaginator,
    ListSnapshotsPaginator,
    ListStageDeploymentsPaginator,
    ListStagesPaginator,
)
from .type_defs import (
    CreateGameResultTypeDef,
    CreateSnapshotResultTypeDef,
    CreateStageResultTypeDef,
    DisconnectPlayerResultTypeDef,
    ExportSnapshotResultTypeDef,
    GeneratorTypeDef,
    GetExtensionResultTypeDef,
    GetExtensionVersionResultTypeDef,
    GetGameConfigurationResultTypeDef,
    GetGameResultTypeDef,
    GetGeneratedCodeJobResultTypeDef,
    GetPlayerConnectionStatusResultTypeDef,
    GetSnapshotResultTypeDef,
    GetStageDeploymentResultTypeDef,
    GetStageResultTypeDef,
    ImportGameConfigurationResultTypeDef,
    ImportGameConfigurationSourceTypeDef,
    ListExtensionsResultTypeDef,
    ListExtensionVersionsResultTypeDef,
    ListGamesResultTypeDef,
    ListGeneratedCodeJobsResultTypeDef,
    ListSnapshotsResultTypeDef,
    ListStageDeploymentsResultTypeDef,
    ListStagesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    SectionModificationTypeDef,
    StartGeneratedCodeJobResultTypeDef,
    StartStageDeploymentResultTypeDef,
    UpdateGameConfigurationResultTypeDef,
    UpdateGameResultTypeDef,
    UpdateSnapshotResultTypeDef,
    UpdateStageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GameSparksClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class GameSparksClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GameSparksClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#close)
        """
    def create_game(
        self,
        *,
        GameName: str,
        ClientToken: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateGameResultTypeDef:
        """
        Creates a new game with an empty configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.create_game)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#create_game)
        """
    def create_snapshot(
        self, *, GameName: str, Description: str = None
    ) -> CreateSnapshotResultTypeDef:
        """
        Creates a snapshot of the game configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#create_snapshot)
        """
    def create_stage(
        self,
        *,
        GameName: str,
        Role: str,
        StageName: str,
        ClientToken: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateStageResultTypeDef:
        """
        Creates a new stage for stage-by-stage game development and deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#create_stage)
        """
    def delete_game(self, *, GameName: str) -> Dict[str, Any]:
        """
        Deletes a game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.delete_game)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#delete_game)
        """
    def delete_stage(self, *, GameName: str, StageName: str) -> Dict[str, Any]:
        """
        Deletes a stage from a game, along with the associated game runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#delete_stage)
        """
    def disconnect_player(
        self, *, GameName: str, PlayerId: str, StageName: str
    ) -> DisconnectPlayerResultTypeDef:
        """
        Disconnects a player from the game runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.disconnect_player)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#disconnect_player)
        """
    def export_snapshot(self, *, GameName: str, SnapshotId: str) -> ExportSnapshotResultTypeDef:
        """
        Exports a game configuration snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.export_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#export_snapshot)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#generate_presigned_url)
        """
    def get_extension(self, *, Name: str, Namespace: str) -> GetExtensionResultTypeDef:
        """
        Gets details about a specified extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_extension)
        """
    def get_extension_version(
        self, *, ExtensionVersion: str, Name: str, Namespace: str
    ) -> GetExtensionVersionResultTypeDef:
        """
        Gets details about a specified extension version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_extension_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_extension_version)
        """
    def get_game(self, *, GameName: str) -> GetGameResultTypeDef:
        """
        Gets details about a game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_game)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_game)
        """
    def get_game_configuration(
        self, *, GameName: str, Sections: List[str] = None
    ) -> GetGameConfigurationResultTypeDef:
        """
        Gets the configuration of the game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_game_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_game_configuration)
        """
    def get_generated_code_job(
        self, *, GameName: str, JobId: str, SnapshotId: str
    ) -> GetGeneratedCodeJobResultTypeDef:
        """
        Gets details about a job that is generating code for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_generated_code_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_generated_code_job)
        """
    def get_player_connection_status(
        self, *, GameName: str, PlayerId: str, StageName: str
    ) -> GetPlayerConnectionStatusResultTypeDef:
        """
        Gets the status of a player's connection to the game runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_player_connection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_player_connection_status)
        """
    def get_snapshot(
        self, *, GameName: str, SnapshotId: str, Sections: List[str] = None
    ) -> GetSnapshotResultTypeDef:
        """
        Gets a copy of the game configuration in a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_snapshot)
        """
    def get_stage(self, *, GameName: str, StageName: str) -> GetStageResultTypeDef:
        """
        Gets information about a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_stage)
        """
    def get_stage_deployment(
        self, *, GameName: str, StageName: str, DeploymentId: str = None
    ) -> GetStageDeploymentResultTypeDef:
        """
        Gets information about a stage deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.get_stage_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#get_stage_deployment)
        """
    def import_game_configuration(
        self, *, GameName: str, ImportSource: "ImportGameConfigurationSourceTypeDef"
    ) -> ImportGameConfigurationResultTypeDef:
        """
        Imports a game configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.import_game_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#import_game_configuration)
        """
    def list_extension_versions(
        self, *, Name: str, Namespace: str, MaxResults: int = None, NextToken: str = None
    ) -> ListExtensionVersionsResultTypeDef:
        """
        Gets a paginated list of available versions for the extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_extension_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_extension_versions)
        """
    def list_extensions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListExtensionsResultTypeDef:
        """
        Gets a paginated list of available extensions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_extensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_extensions)
        """
    def list_games(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListGamesResultTypeDef:
        """
        Gets a paginated list of games.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_games)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_games)
        """
    def list_generated_code_jobs(
        self, *, GameName: str, SnapshotId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListGeneratedCodeJobsResultTypeDef:
        """
        Gets a paginated list of code generation jobs for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_generated_code_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_generated_code_jobs)
        """
    def list_snapshots(
        self, *, GameName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListSnapshotsResultTypeDef:
        """
        Gets a paginated list of snapshot summaries from the game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_snapshots)
        """
    def list_stage_deployments(
        self, *, GameName: str, StageName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListStageDeploymentsResultTypeDef:
        """
        Gets a paginated list of stage deployment summaries from the game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_stage_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_stage_deployments)
        """
    def list_stages(
        self, *, GameName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListStagesResultTypeDef:
        """
        Gets a paginated list of stage summaries from the game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_stages)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        Lists the tags associated with a GameSparks resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#list_tags_for_resource)
        """
    def start_generated_code_job(
        self, *, GameName: str, Generator: "GeneratorTypeDef", SnapshotId: str
    ) -> StartGeneratedCodeJobResultTypeDef:
        """
        Starts an asynchronous process that generates client code for system-defined and
        custom messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.start_generated_code_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#start_generated_code_job)
        """
    def start_stage_deployment(
        self, *, GameName: str, SnapshotId: str, StageName: str, ClientToken: str = None
    ) -> StartStageDeploymentResultTypeDef:
        """
        Deploys a snapshot to the stage and creates a new game runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.start_stage_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#start_stage_deployment)
        """
    def tag_resource(self, *, ResourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a GameSparks resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a GameSparks resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#untag_resource)
        """
    def update_game(self, *, GameName: str, Description: str = None) -> UpdateGameResultTypeDef:
        """
        Updates details of the game.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.update_game)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#update_game)
        """
    def update_game_configuration(
        self, *, GameName: str, Modifications: List["SectionModificationTypeDef"]
    ) -> UpdateGameConfigurationResultTypeDef:
        """
        Updates one or more sections of the game configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.update_game_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#update_game_configuration)
        """
    def update_snapshot(
        self, *, GameName: str, SnapshotId: str, Description: str = None
    ) -> UpdateSnapshotResultTypeDef:
        """
        Updates the metadata of a GameSparks snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.update_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#update_snapshot)
        """
    def update_stage(
        self, *, GameName: str, StageName: str, Description: str = None, Role: str = None
    ) -> UpdateStageResultTypeDef:
        """
        Updates the metadata of a stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/client.html#update_stage)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_extension_versions"]
    ) -> ListExtensionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensionVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_extensions"]) -> ListExtensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListExtensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listextensionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_games"]) -> ListGamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListGames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgamespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_generated_code_jobs"]
    ) -> ListGeneratedCodeJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListGeneratedCodeJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listgeneratedcodejobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_snapshots"]) -> ListSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#listsnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stage_deployments"]
    ) -> ListStageDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListStageDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagedeploymentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_stages"]) -> ListStagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/gamesparks.html#GameSparks.Paginator.ListStages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/paginators.html#liststagespaginator)
        """
