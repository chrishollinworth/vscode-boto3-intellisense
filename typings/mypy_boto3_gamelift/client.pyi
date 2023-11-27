"""
Type annotations for gamelift service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_gamelift import GameLiftClient

    client: GameLiftClient = boto3.client("gamelift")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AcceptanceTypeType,
    BackfillModeType,
    BalancingStrategyType,
    BuildStatusType,
    ComparisonOperatorTypeType,
    ComputeTypeType,
    EC2InstanceTypeType,
    FleetTypeType,
    FlexMatchModeType,
    GameServerGroupDeleteOptionType,
    GameServerProtectionPolicyType,
    GameServerUtilizationStatusType,
    LocationFilterType,
    MetricNameType,
    OperatingSystemType,
    PlayerSessionCreationPolicyType,
    PolicyTypeType,
    ProtectionPolicyType,
    RoutingStrategyTypeType,
    ScalingAdjustmentTypeType,
    ScalingStatusTypeType,
    SortOrderType,
)
from .paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
    DescribeGameServerInstancesPaginator,
    DescribeGameSessionDetailsPaginator,
    DescribeGameSessionQueuesPaginator,
    DescribeGameSessionsPaginator,
    DescribeInstancesPaginator,
    DescribeMatchmakingConfigurationsPaginator,
    DescribeMatchmakingRuleSetsPaginator,
    DescribePlayerSessionsPaginator,
    DescribeScalingPoliciesPaginator,
    ListAliasesPaginator,
    ListBuildsPaginator,
    ListComputePaginator,
    ListFleetsPaginator,
    ListGameServerGroupsPaginator,
    ListGameServersPaginator,
    ListLocationsPaginator,
    ListScriptsPaginator,
    SearchGameSessionsPaginator,
)
from .type_defs import (
    AnywhereConfigurationTypeDef,
    CertificateConfigurationTypeDef,
    ClaimFilterOptionTypeDef,
    ClaimGameServerOutputTypeDef,
    CreateAliasOutputTypeDef,
    CreateBuildOutputTypeDef,
    CreateFleetLocationsOutputTypeDef,
    CreateFleetOutputTypeDef,
    CreateGameServerGroupOutputTypeDef,
    CreateGameSessionOutputTypeDef,
    CreateGameSessionQueueOutputTypeDef,
    CreateLocationOutputTypeDef,
    CreateMatchmakingConfigurationOutputTypeDef,
    CreateMatchmakingRuleSetOutputTypeDef,
    CreatePlayerSessionOutputTypeDef,
    CreatePlayerSessionsOutputTypeDef,
    CreateScriptOutputTypeDef,
    CreateVpcPeeringAuthorizationOutputTypeDef,
    DeleteFleetLocationsOutputTypeDef,
    DeleteGameServerGroupOutputTypeDef,
    DescribeAliasOutputTypeDef,
    DescribeBuildOutputTypeDef,
    DescribeComputeOutputTypeDef,
    DescribeEC2InstanceLimitsOutputTypeDef,
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetLocationAttributesOutputTypeDef,
    DescribeFleetLocationCapacityOutputTypeDef,
    DescribeFleetLocationUtilizationOutputTypeDef,
    DescribeFleetPortSettingsOutputTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameServerGroupOutputTypeDef,
    DescribeGameServerInstancesOutputTypeDef,
    DescribeGameServerOutputTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionPlacementOutputTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingOutputTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeRuntimeConfigurationOutputTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    DescribeScriptOutputTypeDef,
    DescribeVpcPeeringAuthorizationsOutputTypeDef,
    DescribeVpcPeeringConnectionsOutputTypeDef,
    DesiredPlayerSessionTypeDef,
    FilterConfigurationTypeDef,
    GamePropertyTypeDef,
    GameServerGroupAutoScalingPolicyTypeDef,
    GameSessionQueueDestinationTypeDef,
    GetComputeAccessOutputTypeDef,
    GetComputeAuthTokenOutputTypeDef,
    GetGameSessionLogUrlOutputTypeDef,
    GetInstanceAccessOutputTypeDef,
    InstanceDefinitionTypeDef,
    IpPermissionTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListComputeOutputTypeDef,
    ListFleetsOutputTypeDef,
    ListGameServerGroupsOutputTypeDef,
    ListGameServersOutputTypeDef,
    ListLocationsOutputTypeDef,
    ListScriptsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationConfigurationTypeDef,
    PlayerLatencyPolicyTypeDef,
    PlayerLatencyTypeDef,
    PlayerTypeDef,
    PriorityConfigurationTypeDef,
    PutScalingPolicyOutputTypeDef,
    RegisterComputeOutputTypeDef,
    RegisterGameServerOutputTypeDef,
    RequestUploadCredentialsOutputTypeDef,
    ResolveAliasOutputTypeDef,
    ResourceCreationLimitPolicyTypeDef,
    ResumeGameServerGroupOutputTypeDef,
    RoutingStrategyTypeDef,
    RuntimeConfigurationTypeDef,
    S3LocationTypeDef,
    SearchGameSessionsOutputTypeDef,
    StartFleetActionsOutputTypeDef,
    StartGameSessionPlacementOutputTypeDef,
    StartMatchBackfillOutputTypeDef,
    StartMatchmakingOutputTypeDef,
    StopFleetActionsOutputTypeDef,
    StopGameSessionPlacementOutputTypeDef,
    SuspendGameServerGroupOutputTypeDef,
    TagTypeDef,
    TargetConfigurationTypeDef,
    UpdateAliasOutputTypeDef,
    UpdateBuildOutputTypeDef,
    UpdateFleetAttributesOutputTypeDef,
    UpdateFleetCapacityOutputTypeDef,
    UpdateFleetPortSettingsOutputTypeDef,
    UpdateGameServerGroupOutputTypeDef,
    UpdateGameServerOutputTypeDef,
    UpdateGameSessionOutputTypeDef,
    UpdateGameSessionQueueOutputTypeDef,
    UpdateMatchmakingConfigurationOutputTypeDef,
    UpdateRuntimeConfigurationOutputTypeDef,
    UpdateScriptOutputTypeDef,
    ValidateMatchmakingRuleSetOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GameLiftClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    FleetCapacityExceededException: Type[BotocoreClientError]
    GameSessionFullException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidFleetStatusException: Type[BotocoreClientError]
    InvalidGameSessionStatusException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    OutOfCapacityException: Type[BotocoreClientError]
    TaggingFailedException: Type[BotocoreClientError]
    TerminalRoutingStrategyException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnsupportedRegionException: Type[BotocoreClientError]

class GameLiftClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GameLiftClient exceptions.
        """
    def accept_match(
        self, *, TicketId: str, PlayerIds: List[str], AcceptanceType: AcceptanceTypeType
    ) -> Dict[str, Any]:
        """
        Registers a player's acceptance or rejection of a proposed FlexMatch match.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.accept_match)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#accept_match)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#can_paginate)
        """
    def claim_game_server(
        self,
        *,
        GameServerGroupName: str,
        GameServerId: str = None,
        GameServerData: str = None,
        FilterOption: "ClaimFilterOptionTypeDef" = None
    ) -> ClaimGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Locates an available game server and temporarily reserves it to
        host gameplay and players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.claim_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#claim_game_server)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#close)
        """
    def create_alias(
        self,
        *,
        Name: str,
        RoutingStrategy: "RoutingStrategyTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAliasOutputTypeDef:
        """
        Creates an alias for a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_alias)
        """
    def create_build(
        self,
        *,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        OperatingSystem: OperatingSystemType = None,
        Tags: List["TagTypeDef"] = None,
        ServerSdkVersion: str = None
    ) -> CreateBuildOutputTypeDef:
        """
        Creates a new Amazon GameLift build resource for your game server binary files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_build)
        """
    def create_fleet(
        self,
        *,
        Name: str,
        Description: str = None,
        BuildId: str = None,
        ScriptId: str = None,
        ServerLaunchPath: str = None,
        ServerLaunchParameters: str = None,
        LogPaths: List[str] = None,
        EC2InstanceType: EC2InstanceTypeType = None,
        EC2InboundPermissions: List["IpPermissionTypeDef"] = None,
        NewGameSessionProtectionPolicy: ProtectionPolicyType = None,
        RuntimeConfiguration: "RuntimeConfigurationTypeDef" = None,
        ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
        MetricGroups: List[str] = None,
        PeerVpcAwsAccountId: str = None,
        PeerVpcId: str = None,
        FleetType: FleetTypeType = None,
        InstanceRoleArn: str = None,
        CertificateConfiguration: "CertificateConfigurationTypeDef" = None,
        Locations: List["LocationConfigurationTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ComputeType: ComputeTypeType = None,
        AnywhereConfiguration: "AnywhereConfigurationTypeDef" = None,
        InstanceRoleCredentialsProvider: Literal["SHARED_CREDENTIAL_FILE"] = None
    ) -> CreateFleetOutputTypeDef:
        """
        Creates a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances to host
        your custom game server or Realtime Servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_fleet)
        """
    def create_fleet_locations(
        self, *, FleetId: str, Locations: List["LocationConfigurationTypeDef"]
    ) -> CreateFleetLocationsOutputTypeDef:
        """
        Adds remote locations to a fleet and begins populating the new locations with
        EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_fleet_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_fleet_locations)
        """
    def create_game_server_group(
        self,
        *,
        GameServerGroupName: str,
        RoleArn: str,
        MinSize: int,
        MaxSize: int,
        LaunchTemplate: "LaunchTemplateSpecificationTypeDef",
        InstanceDefinitions: List["InstanceDefinitionTypeDef"],
        AutoScalingPolicy: "GameServerGroupAutoScalingPolicyTypeDef" = None,
        BalancingStrategy: BalancingStrategyType = None,
        GameServerProtectionPolicy: GameServerProtectionPolicyType = None,
        VpcSubnets: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Creates a Amazon GameLift FleetIQ game server group for
        managing game hosting on a collection of Amazon Elastic Compute Cloud instances
        for game hosting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_game_server_group)
        """
    def create_game_session(
        self,
        *,
        MaximumPlayerSessionCount: int,
        FleetId: str = None,
        AliasId: str = None,
        Name: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        CreatorId: str = None,
        GameSessionId: str = None,
        IdempotencyToken: str = None,
        GameSessionData: str = None,
        Location: str = None
    ) -> CreateGameSessionOutputTypeDef:
        """
        Creates a multiplayer game session for players in a specific fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_game_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_game_session)
        """
    def create_game_session_queue(
        self,
        *,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
        Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
        FilterConfiguration: "FilterConfigurationTypeDef" = None,
        PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
        CustomEventData: str = None,
        NotificationTarget: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGameSessionQueueOutputTypeDef:
        """
        Creates a placement queue that processes requests for new game sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_game_session_queue)
        """
    def create_location(
        self, *, LocationName: str, Tags: List["TagTypeDef"] = None
    ) -> CreateLocationOutputTypeDef:
        """
        Creates a custom location for use in an Anywhere fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_location)
        """
    def create_matchmaking_configuration(
        self,
        *,
        Name: str,
        RequestTimeoutSeconds: int,
        AcceptanceRequired: bool,
        RuleSetName: str,
        Description: str = None,
        GameSessionQueueArns: List[str] = None,
        AcceptanceTimeoutSeconds: int = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionData: str = None,
        BackfillMode: BackfillModeType = None,
        FlexMatchMode: FlexMatchModeType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMatchmakingConfigurationOutputTypeDef:
        """
        Defines a new matchmaking configuration for use with FlexMatch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_matchmaking_configuration)
        """
    def create_matchmaking_rule_set(
        self, *, Name: str, RuleSetBody: str, Tags: List["TagTypeDef"] = None
    ) -> CreateMatchmakingRuleSetOutputTypeDef:
        """
        Creates a new rule set for FlexMatch matchmaking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_matchmaking_rule_set)
        """
    def create_player_session(
        self, *, GameSessionId: str, PlayerId: str, PlayerData: str = None
    ) -> CreatePlayerSessionOutputTypeDef:
        """
        Reserves an open player slot in a game session for a player.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_player_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_player_session)
        """
    def create_player_sessions(
        self, *, GameSessionId: str, PlayerIds: List[str], PlayerDataMap: Dict[str, str] = None
    ) -> CreatePlayerSessionsOutputTypeDef:
        """
        Reserves open slots in a game session for a group of players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_player_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_player_sessions)
        """
    def create_script(
        self,
        *,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        ZipFile: Union[bytes, IO[bytes], StreamingBody] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateScriptOutputTypeDef:
        """
        Creates a new script record for your Realtime Servers script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_script)
        """
    def create_vpc_peering_authorization(
        self, *, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> CreateVpcPeeringAuthorizationOutputTypeDef:
        """
        Requests authorization to create or delete a peer connection between the VPC for
        your Amazon GameLift fleet and a virtual private cloud (VPC) in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_vpc_peering_authorization)
        """
    def create_vpc_peering_connection(
        self, *, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        Establishes a VPC peering connection between a virtual private cloud (VPC) in an
        Amazon Web Services account with the VPC for your Amazon GameLift fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create_vpc_peering_connection)
        """
    def delete_alias(self, *, AliasId: str) -> None:
        """
        Deletes an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_alias)
        """
    def delete_build(self, *, BuildId: str) -> None:
        """
        Deletes a build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_build)
        """
    def delete_fleet(self, *, FleetId: str) -> None:
        """
        Deletes all resources and information related a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_fleet)
        """
    def delete_fleet_locations(
        self, *, FleetId: str, Locations: List[str]
    ) -> DeleteFleetLocationsOutputTypeDef:
        """
        Removes locations from a multi-location fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_fleet_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_fleet_locations)
        """
    def delete_game_server_group(
        self, *, GameServerGroupName: str, DeleteOption: GameServerGroupDeleteOptionType = None
    ) -> DeleteGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Terminates a game server group and permanently deletes the game
        server group record.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_game_server_group)
        """
    def delete_game_session_queue(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a game session queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_game_session_queue)
        """
    def delete_location(self, *, LocationName: str) -> Dict[str, Any]:
        """
        Deletes a custom location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_location)
        """
    def delete_matchmaking_configuration(self, *, Name: str) -> Dict[str, Any]:
        """
        Permanently removes a FlexMatch matchmaking configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_matchmaking_configuration)
        """
    def delete_matchmaking_rule_set(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an existing matchmaking rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_matchmaking_rule_set)
        """
    def delete_scaling_policy(self, *, Name: str, FleetId: str) -> None:
        """
        Deletes a fleet scaling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_scaling_policy)
        """
    def delete_script(self, *, ScriptId: str) -> None:
        """
        Deletes a Realtime script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_script)
        """
    def delete_vpc_peering_authorization(
        self, *, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        Cancels a pending VPC peering authorization for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_vpc_peering_authorization)
        """
    def delete_vpc_peering_connection(
        self, *, FleetId: str, VpcPeeringConnectionId: str
    ) -> Dict[str, Any]:
        """
        Removes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete_vpc_peering_connection)
        """
    def deregister_compute(self, *, FleetId: str, ComputeName: str) -> Dict[str, Any]:
        """
        Removes a compute resource from an Amazon GameLift Anywhere fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.deregister_compute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#deregister_compute)
        """
    def deregister_game_server(self, *, GameServerGroupName: str, GameServerId: str) -> None:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Removes the game server from a game server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.deregister_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#deregister_game_server)
        """
    def describe_alias(self, *, AliasId: str) -> DescribeAliasOutputTypeDef:
        """
        Retrieves properties for an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_alias)
        """
    def describe_build(self, *, BuildId: str) -> DescribeBuildOutputTypeDef:
        """
        Retrieves properties for a custom game build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_build)
        """
    def describe_compute(self, *, FleetId: str, ComputeName: str) -> DescribeComputeOutputTypeDef:
        """
        Retrieves properties for a compute resource in an Amazon GameLift fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_compute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_compute)
        """
    def describe_ec2_instance_limits(
        self, *, EC2InstanceType: EC2InstanceTypeType = None, Location: str = None
    ) -> DescribeEC2InstanceLimitsOutputTypeDef:
        """
        Retrieves the instance limits and current utilization for an Amazon Web Services
        Region or location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_ec2_instance_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_ec2_instance_limits)
        """
    def describe_fleet_attributes(
        self, *, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetAttributesOutputTypeDef:
        """
        Retrieves core fleet-wide properties, including the computing hardware and
        deployment configuration for all instances in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_attributes)
        """
    def describe_fleet_capacity(
        self, *, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetCapacityOutputTypeDef:
        """
        Retrieves the resource capacity settings for one or more fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_capacity)
        """
    def describe_fleet_events(
        self,
        *,
        FleetId: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeFleetEventsOutputTypeDef:
        """
        Retrieves entries from a fleet's event log.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_events)
        """
    def describe_fleet_location_attributes(
        self, *, FleetId: str, Locations: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetLocationAttributesOutputTypeDef:
        """
        Retrieves information on a fleet's remote locations, including life-cycle status
        and any suspended fleet activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_location_attributes)
        """
    def describe_fleet_location_capacity(
        self, *, FleetId: str, Location: str
    ) -> DescribeFleetLocationCapacityOutputTypeDef:
        """
        Retrieves the resource capacity settings for a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_location_capacity)
        """
    def describe_fleet_location_utilization(
        self, *, FleetId: str, Location: str
    ) -> DescribeFleetLocationUtilizationOutputTypeDef:
        """
        Retrieves current usage data for a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_location_utilization)
        """
    def describe_fleet_port_settings(
        self, *, FleetId: str, Location: str = None
    ) -> DescribeFleetPortSettingsOutputTypeDef:
        """
        Retrieves a fleet's inbound connection permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_port_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_port_settings)
        """
    def describe_fleet_utilization(
        self, *, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetUtilizationOutputTypeDef:
        """
        Retrieves utilization statistics for one or more fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_fleet_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_fleet_utilization)
        """
    def describe_game_server(
        self, *, GameServerGroupName: str, GameServerId: str
    ) -> DescribeGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information for a registered game server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_server)
        """
    def describe_game_server_group(
        self, *, GameServerGroupName: str
    ) -> DescribeGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information on a game server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_server_group)
        """
    def describe_game_server_instances(
        self,
        *,
        GameServerGroupName: str,
        InstanceIds: List[str] = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeGameServerInstancesOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves status information about the Amazon EC2 instances
        associated with a Amazon GameLift FleetIQ game server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_server_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_server_instances)
        """
    def describe_game_session_details(
        self,
        *,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeGameSessionDetailsOutputTypeDef:
        """
        Retrieves additional game session properties, including the game session
        protection policy in force, a set of one or more game sessions in a specific
        fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_session_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_session_details)
        """
    def describe_game_session_placement(
        self, *, PlacementId: str
    ) -> DescribeGameSessionPlacementOutputTypeDef:
        """
        Retrieves information, including current status, about a game session placement
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_session_placement)
        """
    def describe_game_session_queues(
        self, *, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeGameSessionQueuesOutputTypeDef:
        """
        Retrieves the properties for one or more game session queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_session_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_session_queues)
        """
    def describe_game_sessions(
        self,
        *,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeGameSessionsOutputTypeDef:
        """
        Retrieves a set of one or more game sessions in a specific fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_game_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_game_sessions)
        """
    def describe_instances(
        self,
        *,
        FleetId: str,
        InstanceId: str = None,
        Limit: int = None,
        NextToken: str = None,
        Location: str = None
    ) -> DescribeInstancesOutputTypeDef:
        """
        Retrieves information about the EC2 instances in an Amazon GameLift managed
        fleet, including instance ID, connection data, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_instances)
        """
    def describe_matchmaking(self, *, TicketIds: List[str]) -> DescribeMatchmakingOutputTypeDef:
        """
        Retrieves one or more matchmaking tickets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_matchmaking)
        """
    def describe_matchmaking_configurations(
        self,
        *,
        Names: List[str] = None,
        RuleSetName: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribeMatchmakingConfigurationsOutputTypeDef:
        """
        Retrieves the details of FlexMatch matchmaking configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_matchmaking_configurations)
        """
    def describe_matchmaking_rule_sets(
        self, *, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeMatchmakingRuleSetsOutputTypeDef:
        """
        Retrieves the details for FlexMatch matchmaking rule sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_matchmaking_rule_sets)
        """
    def describe_player_sessions(
        self,
        *,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> DescribePlayerSessionsOutputTypeDef:
        """
        Retrieves properties for one or more player sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_player_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_player_sessions)
        """
    def describe_runtime_configuration(
        self, *, FleetId: str
    ) -> DescribeRuntimeConfigurationOutputTypeDef:
        """
        Retrieves a fleet's runtime configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_runtime_configuration)
        """
    def describe_scaling_policies(
        self,
        *,
        FleetId: str,
        StatusFilter: ScalingStatusTypeType = None,
        Limit: int = None,
        NextToken: str = None,
        Location: str = None
    ) -> DescribeScalingPoliciesOutputTypeDef:
        """
        Retrieves all scaling policies applied to a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_scaling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_scaling_policies)
        """
    def describe_script(self, *, ScriptId: str) -> DescribeScriptOutputTypeDef:
        """
        Retrieves properties for a Realtime script.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_script)
        """
    def describe_vpc_peering_authorizations(self) -> DescribeVpcPeeringAuthorizationsOutputTypeDef:
        """
        Retrieves valid VPC peering authorizations that are pending for the Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_vpc_peering_authorizations)
        """
    def describe_vpc_peering_connections(
        self, *, FleetId: str = None
    ) -> DescribeVpcPeeringConnectionsOutputTypeDef:
        """
        Retrieves information on VPC peering connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe_vpc_peering_connections)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#generate_presigned_url)
        """
    def get_compute_access(
        self, *, FleetId: str, ComputeName: str
    ) -> GetComputeAccessOutputTypeDef:
        """
        Requests authorization to remotely connect to a compute resource in an Amazon
        GameLift fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.get_compute_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get_compute_access)
        """
    def get_compute_auth_token(
        self, *, FleetId: str, ComputeName: str
    ) -> GetComputeAuthTokenOutputTypeDef:
        """
        Requests an authentication token from Amazon GameLift for a registered compute
        in an Anywhere fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.get_compute_auth_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get_compute_auth_token)
        """
    def get_game_session_log_url(self, *, GameSessionId: str) -> GetGameSessionLogUrlOutputTypeDef:
        """
        Retrieves the location of stored game session logs for a specified game session
        on Amazon GameLift managed fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.get_game_session_log_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get_game_session_log_url)
        """
    def get_instance_access(
        self, *, FleetId: str, InstanceId: str
    ) -> GetInstanceAccessOutputTypeDef:
        """
        Requests authorization to remotely connect to an instance in an Amazon GameLift
        managed fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.get_instance_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get_instance_access)
        """
    def list_aliases(
        self,
        *,
        RoutingStrategyType: RoutingStrategyTypeType = None,
        Name: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> ListAliasesOutputTypeDef:
        """
        Retrieves all aliases for this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_aliases)
        """
    def list_builds(
        self, *, Status: BuildStatusType = None, Limit: int = None, NextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        Retrieves build resources for all builds associated with the Amazon Web Services
        account in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_builds)
        """
    def list_compute(
        self, *, FleetId: str, Location: str = None, Limit: int = None, NextToken: str = None
    ) -> ListComputeOutputTypeDef:
        """
        Retrieves the compute resources in an Amazon GameLift fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_compute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_compute)
        """
    def list_fleets(
        self, *, BuildId: str = None, ScriptId: str = None, Limit: int = None, NextToken: str = None
    ) -> ListFleetsOutputTypeDef:
        """
        Retrieves a collection of fleet resources in an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_fleets)
        """
    def list_game_server_groups(
        self, *, Limit: int = None, NextToken: str = None
    ) -> ListGameServerGroupsOutputTypeDef:
        """
        Lists a game server groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_game_server_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_game_server_groups)
        """
    def list_game_servers(
        self,
        *,
        GameServerGroupName: str,
        SortOrder: SortOrderType = None,
        Limit: int = None,
        NextToken: str = None
    ) -> ListGameServersOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Retrieves information on all game servers that are currently
        active in a specified game server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_game_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_game_servers)
        """
    def list_locations(
        self, *, Filters: List[LocationFilterType] = None, Limit: int = None, NextToken: str = None
    ) -> ListLocationsOutputTypeDef:
        """
        Lists all custom and Amazon Web Services locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_locations)
        """
    def list_scripts(self, *, Limit: int = None, NextToken: str = None) -> ListScriptsOutputTypeDef:
        """
        Retrieves script records for all Realtime scripts that are associated with the
        Amazon Web Services account in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_scripts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_scripts)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all tags assigned to a Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list_tags_for_resource)
        """
    def put_scaling_policy(
        self,
        *,
        Name: str,
        FleetId: str,
        MetricName: MetricNameType,
        ScalingAdjustment: int = None,
        ScalingAdjustmentType: ScalingAdjustmentTypeType = None,
        Threshold: float = None,
        ComparisonOperator: ComparisonOperatorTypeType = None,
        EvaluationPeriods: int = None,
        PolicyType: PolicyTypeType = None,
        TargetConfiguration: "TargetConfigurationTypeDef" = None
    ) -> PutScalingPolicyOutputTypeDef:
        """
        Creates or updates a scaling policy for a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.put_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#put_scaling_policy)
        """
    def register_compute(
        self,
        *,
        FleetId: str,
        ComputeName: str,
        CertificatePath: str = None,
        DnsName: str = None,
        IpAddress: str = None,
        Location: str = None
    ) -> RegisterComputeOutputTypeDef:
        """
        Registers a compute resource to an Amazon GameLift Anywhere fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.register_compute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#register_compute)
        """
    def register_game_server(
        self,
        *,
        GameServerGroupName: str,
        GameServerId: str,
        InstanceId: str,
        ConnectionInfo: str = None,
        GameServerData: str = None
    ) -> RegisterGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Creates a new game server resource and notifies Amazon GameLift
        FleetIQ that the game server is ready to host gameplay and players.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.register_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#register_game_server)
        """
    def request_upload_credentials(self, *, BuildId: str) -> RequestUploadCredentialsOutputTypeDef:
        """
        Retrieves a fresh set of credentials for use when uploading a new set of game
        build files to Amazon GameLift's Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.request_upload_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#request_upload_credentials)
        """
    def resolve_alias(self, *, AliasId: str) -> ResolveAliasOutputTypeDef:
        """
        Retrieves the fleet ID that an alias is currently pointing to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.resolve_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#resolve_alias)
        """
    def resume_game_server_group(
        self, *, GameServerGroupName: str, ResumeActions: List[Literal["REPLACE_INSTANCE_TYPES"]]
    ) -> ResumeGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Reinstates activity on a game server group after it has been
        suspended.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.resume_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#resume_game_server_group)
        """
    def search_game_sessions(
        self,
        *,
        FleetId: str = None,
        AliasId: str = None,
        Location: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        Limit: int = None,
        NextToken: str = None
    ) -> SearchGameSessionsOutputTypeDef:
        """
        Retrieves all active game sessions that match a set of search criteria and sorts
        them into a specified order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.search_game_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#search_game_sessions)
        """
    def start_fleet_actions(
        self, *, FleetId: str, Actions: List[Literal["AUTO_SCALING"]], Location: str = None
    ) -> StartFleetActionsOutputTypeDef:
        """
        Resumes certain types of activity on fleet instances that were suspended with
        `StopFleetActions <https://docs.aws.amazon.com/gamelift/latest/apireference/API_
        StopFleetActions.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.start_fleet_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start_fleet_actions)
        """
    def start_game_session_placement(
        self,
        *,
        PlacementId: str,
        GameSessionQueueName: str,
        MaximumPlayerSessionCount: int,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionName: str = None,
        PlayerLatencies: List["PlayerLatencyTypeDef"] = None,
        DesiredPlayerSessions: List["DesiredPlayerSessionTypeDef"] = None,
        GameSessionData: str = None
    ) -> StartGameSessionPlacementOutputTypeDef:
        """
        Places a request for a new game session in a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.start_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start_game_session_placement)
        """
    def start_match_backfill(
        self,
        *,
        ConfigurationName: str,
        Players: List["PlayerTypeDef"],
        TicketId: str = None,
        GameSessionArn: str = None
    ) -> StartMatchBackfillOutputTypeDef:
        """
        Finds new players to fill open slots in currently running game sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.start_match_backfill)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start_match_backfill)
        """
    def start_matchmaking(
        self, *, ConfigurationName: str, Players: List["PlayerTypeDef"], TicketId: str = None
    ) -> StartMatchmakingOutputTypeDef:
        """
        Uses FlexMatch to create a game match for a group of players based on custom
        matchmaking rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.start_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start_matchmaking)
        """
    def stop_fleet_actions(
        self, *, FleetId: str, Actions: List[Literal["AUTO_SCALING"]], Location: str = None
    ) -> StopFleetActionsOutputTypeDef:
        """
        Suspends certain types of activity in a fleet location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.stop_fleet_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop_fleet_actions)
        """
    def stop_game_session_placement(
        self, *, PlacementId: str
    ) -> StopGameSessionPlacementOutputTypeDef:
        """
        Cancels a game session placement that is in `PENDING` status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.stop_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop_game_session_placement)
        """
    def stop_matchmaking(self, *, TicketId: str) -> Dict[str, Any]:
        """
        Cancels a matchmaking ticket or match backfill ticket that is currently being
        processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.stop_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop_matchmaking)
        """
    def suspend_game_server_group(
        self, *, GameServerGroupName: str, SuspendActions: List[Literal["REPLACE_INSTANCE_TYPES"]]
    ) -> SuspendGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Temporarily stops activity on a game server group without
        terminating instances or the game server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.suspend_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#suspend_game_server_group)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns a tag to an Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag assigned to a Amazon GameLift resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#untag_resource)
        """
    def update_alias(
        self,
        *,
        AliasId: str,
        Name: str = None,
        Description: str = None,
        RoutingStrategy: "RoutingStrategyTypeDef" = None
    ) -> UpdateAliasOutputTypeDef:
        """
        Updates properties for an alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_alias)
        """
    def update_build(
        self, *, BuildId: str, Name: str = None, Version: str = None
    ) -> UpdateBuildOutputTypeDef:
        """
        Updates metadata in a build resource, including the build name and version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_build)
        """
    def update_fleet_attributes(
        self,
        *,
        FleetId: str,
        Name: str = None,
        Description: str = None,
        NewGameSessionProtectionPolicy: ProtectionPolicyType = None,
        ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
        MetricGroups: List[str] = None,
        AnywhereConfiguration: "AnywhereConfigurationTypeDef" = None
    ) -> UpdateFleetAttributesOutputTypeDef:
        """
        Updates a fleet's mutable attributes, including game session protection and
        resource creation limits.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_fleet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_fleet_attributes)
        """
    def update_fleet_capacity(
        self,
        *,
        FleetId: str,
        DesiredInstances: int = None,
        MinSize: int = None,
        MaxSize: int = None,
        Location: str = None
    ) -> UpdateFleetCapacityOutputTypeDef:
        """
        Updates capacity settings for a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_fleet_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_fleet_capacity)
        """
    def update_fleet_port_settings(
        self,
        *,
        FleetId: str,
        InboundPermissionAuthorizations: List["IpPermissionTypeDef"] = None,
        InboundPermissionRevocations: List["IpPermissionTypeDef"] = None
    ) -> UpdateFleetPortSettingsOutputTypeDef:
        """
        Updates permissions that allow inbound traffic to connect to game sessions that
        are being hosted on instances in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_fleet_port_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_fleet_port_settings)
        """
    def update_game_server(
        self,
        *,
        GameServerGroupName: str,
        GameServerId: str,
        GameServerData: str = None,
        UtilizationStatus: GameServerUtilizationStatusType = None,
        HealthCheck: Literal["HEALTHY"] = None
    ) -> UpdateGameServerOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Updates information about a registered game server to help
        Amazon GameLift FleetIQ track game server availability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_game_server)
        """
    def update_game_server_group(
        self,
        *,
        GameServerGroupName: str,
        RoleArn: str = None,
        InstanceDefinitions: List["InstanceDefinitionTypeDef"] = None,
        GameServerProtectionPolicy: GameServerProtectionPolicyType = None,
        BalancingStrategy: BalancingStrategyType = None
    ) -> UpdateGameServerGroupOutputTypeDef:
        """
        **This operation is used with the Amazon GameLift FleetIQ solution and game
        server groups.** Updates Amazon GameLift FleetIQ-specific properties for a game
        server group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_game_server_group)
        """
    def update_game_session(
        self,
        *,
        GameSessionId: str,
        MaximumPlayerSessionCount: int = None,
        Name: str = None,
        PlayerSessionCreationPolicy: PlayerSessionCreationPolicyType = None,
        ProtectionPolicy: ProtectionPolicyType = None
    ) -> UpdateGameSessionOutputTypeDef:
        """
        Updates the mutable properties of a game session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_game_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_game_session)
        """
    def update_game_session_queue(
        self,
        *,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
        Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
        FilterConfiguration: "FilterConfigurationTypeDef" = None,
        PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
        CustomEventData: str = None,
        NotificationTarget: str = None
    ) -> UpdateGameSessionQueueOutputTypeDef:
        """
        Updates the configuration of a game session queue, which determines how the
        queue processes new game session requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_game_session_queue)
        """
    def update_matchmaking_configuration(
        self,
        *,
        Name: str,
        Description: str = None,
        GameSessionQueueArns: List[str] = None,
        RequestTimeoutSeconds: int = None,
        AcceptanceTimeoutSeconds: int = None,
        AcceptanceRequired: bool = None,
        RuleSetName: str = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionData: str = None,
        BackfillMode: BackfillModeType = None,
        FlexMatchMode: FlexMatchModeType = None
    ) -> UpdateMatchmakingConfigurationOutputTypeDef:
        """
        Updates settings for a FlexMatch matchmaking configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_matchmaking_configuration)
        """
    def update_runtime_configuration(
        self, *, FleetId: str, RuntimeConfiguration: "RuntimeConfigurationTypeDef"
    ) -> UpdateRuntimeConfigurationOutputTypeDef:
        """
        Updates the current runtime configuration for the specified fleet, which tells
        Amazon GameLift how to launch server processes on all instances in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_runtime_configuration)
        """
    def update_script(
        self,
        *,
        ScriptId: str,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        ZipFile: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> UpdateScriptOutputTypeDef:
        """
        Updates Realtime script metadata and content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.update_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update_script)
        """
    def validate_matchmaking_rule_set(
        self, *, RuleSetBody: str
    ) -> ValidateMatchmakingRuleSetOutputTypeDef:
        """
        Validates the syntax of a matchmaking rule or rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Client.validate_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#validate_matchmaking_rule_set)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_attributes"]
    ) -> DescribeFleetAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetattributespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_capacity"]
    ) -> DescribeFleetCapacityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetcapacitypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_events"]
    ) -> DescribeFleetEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleeteventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_utilization"]
    ) -> DescribeFleetUtilizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetutilizationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_server_instances"]
    ) -> DescribeGameServerInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeGameServerInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegameserverinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_details"]
    ) -> DescribeGameSessionDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessiondetailspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_queues"]
    ) -> DescribeGameSessionQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessionqueuespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_sessions"]
    ) -> DescribeGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describeinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_configurations"]
    ) -> DescribeMatchmakingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describematchmakingconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_rule_sets"]
    ) -> DescribeMatchmakingRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describematchmakingrulesetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_player_sessions"]
    ) -> DescribePlayerSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describeplayersessionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describescalingpoliciespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listaliasespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listbuildspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_compute"]) -> ListComputePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListCompute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listcomputepaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listfleetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_server_groups"]
    ) -> ListGameServerGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListGameServerGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listgameservergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_servers"]
    ) -> ListGameServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListGameServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listgameserverspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_locations"]) -> ListLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListLocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listlocationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_scripts"]) -> ListScriptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.ListScripts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listscriptspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_game_sessions"]
    ) -> SearchGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#searchgamesessionspaginator)
        """
