"""
Type annotations for gamelift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_gamelift.type_defs import AcceptMatchInputRequestTypeDef

    data: AcceptMatchInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AcceptanceTypeType,
    BackfillModeType,
    BalancingStrategyType,
    BuildStatusType,
    CertificateTypeType,
    ComparisonOperatorTypeType,
    EC2InstanceTypeType,
    EventCodeType,
    FleetStatusType,
    FleetTypeType,
    FlexMatchModeType,
    GameServerGroupDeleteOptionType,
    GameServerGroupInstanceTypeType,
    GameServerGroupStatusType,
    GameServerInstanceStatusType,
    GameServerProtectionPolicyType,
    GameServerUtilizationStatusType,
    GameSessionPlacementStateType,
    GameSessionStatusType,
    InstanceStatusType,
    IpProtocolType,
    MatchmakingConfigurationStatusType,
    MetricNameType,
    OperatingSystemType,
    PlayerSessionCreationPolicyType,
    PlayerSessionStatusType,
    PolicyTypeType,
    PriorityTypeType,
    ProtectionPolicyType,
    RoutingStrategyTypeType,
    ScalingAdjustmentTypeType,
    ScalingStatusTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptMatchInputRequestTypeDef",
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "ClaimGameServerInputRequestTypeDef",
    "ClaimGameServerOutputTypeDef",
    "CreateAliasInputRequestTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateBuildInputRequestTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateFleetInputRequestTypeDef",
    "CreateFleetLocationsInputRequestTypeDef",
    "CreateFleetLocationsOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateGameServerGroupInputRequestTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "CreateGameSessionInputRequestTypeDef",
    "CreateGameSessionOutputTypeDef",
    "CreateGameSessionQueueInputRequestTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "CreateMatchmakingConfigurationInputRequestTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "CreateMatchmakingRuleSetInputRequestTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "CreatePlayerSessionInputRequestTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsInputRequestTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "CreateScriptInputRequestTypeDef",
    "CreateScriptOutputTypeDef",
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteBuildInputRequestTypeDef",
    "DeleteFleetInputRequestTypeDef",
    "DeleteFleetLocationsInputRequestTypeDef",
    "DeleteFleetLocationsOutputTypeDef",
    "DeleteGameServerGroupInputRequestTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DeleteGameSessionQueueInputRequestTypeDef",
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    "DeleteScalingPolicyInputRequestTypeDef",
    "DeleteScriptInputRequestTypeDef",
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    "DeregisterGameServerInputRequestTypeDef",
    "DescribeAliasInputRequestTypeDef",
    "DescribeAliasOutputTypeDef",
    "DescribeBuildInputRequestTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesInputRequestTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetCapacityInputRequestTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetEventsInputRequestTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetLocationAttributesInputRequestTypeDef",
    "DescribeFleetLocationAttributesOutputTypeDef",
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    "DescribeFleetLocationCapacityOutputTypeDef",
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    "DescribeFleetLocationUtilizationOutputTypeDef",
    "DescribeFleetPortSettingsInputRequestTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "DescribeFleetUtilizationInputRequestTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerGroupInputRequestTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "DescribeGameServerInputRequestTypeDef",
    "DescribeGameServerInstancesInputRequestTypeDef",
    "DescribeGameServerInstancesOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "DescribeGameSessionDetailsInputRequestTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeGameSessionPlacementInputRequestTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesInputRequestTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "DescribeGameSessionsInputRequestTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "DescribeInstancesInputRequestTypeDef",
    "DescribeInstancesOutputTypeDef",
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "DescribeMatchmakingInputRequestTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "DescribePlayerSessionsInputRequestTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "DescribeScalingPoliciesInputRequestTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "DescribeScriptInputRequestTypeDef",
    "DescribeScriptOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    "DesiredPlayerSessionTypeDef",
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FilterConfigurationTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerInstanceTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "GetGameSessionLogUrlInputRequestTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessInputRequestTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsInputRequestTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsInputRequestTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsInputRequestTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersInputRequestTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsInputRequestTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationAttributesTypeDef",
    "LocationConfigurationTypeDef",
    "LocationStateTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PaginatorConfigTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "PriorityConfigurationTypeDef",
    "PutScalingPolicyInputRequestTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerInputRequestTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsInputRequestTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasInputRequestTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeGameServerGroupInputRequestTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "SearchGameSessionsInputRequestTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "ServerProcessTypeDef",
    "StartFleetActionsInputRequestTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StartGameSessionPlacementInputRequestTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillInputRequestTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingInputRequestTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopFleetActionsInputRequestTypeDef",
    "StopFleetActionsOutputTypeDef",
    "StopGameSessionPlacementInputRequestTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "StopMatchmakingInputRequestTypeDef",
    "SuspendGameServerGroupInputRequestTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "UpdateAliasOutputTypeDef",
    "UpdateBuildInputRequestTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesInputRequestTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityInputRequestTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsInputRequestTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerGroupInputRequestTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "UpdateGameServerInputRequestTypeDef",
    "UpdateGameServerOutputTypeDef",
    "UpdateGameSessionInputRequestTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "UpdateGameSessionQueueInputRequestTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "UpdateMatchmakingConfigurationInputRequestTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "UpdateScriptInputRequestTypeDef",
    "UpdateScriptOutputTypeDef",
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
)

AcceptMatchInputRequestTypeDef = TypedDict(
    "AcceptMatchInputRequestTypeDef",
    {
        "TicketId": str,
        "PlayerIds": List[str],
        "AcceptanceType": AcceptanceTypeType,
    },
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": float,
        "SL": List[str],
        "SDM": Dict[str, float],
    },
    total=False,
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
    },
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": str,
        "BuildArn": str,
        "Name": str,
        "Version": str,
        "Status": BuildStatusType,
        "SizeOnDisk": int,
        "OperatingSystem": OperatingSystemType,
        "CreationTime": datetime,
    },
    total=False,
)

CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef",
    {
        "CertificateType": CertificateTypeType,
    },
)

_RequiredClaimGameServerInputRequestTypeDef = TypedDict(
    "_RequiredClaimGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalClaimGameServerInputRequestTypeDef = TypedDict(
    "_OptionalClaimGameServerInputRequestTypeDef",
    {
        "GameServerId": str,
        "GameServerData": str,
    },
    total=False,
)

class ClaimGameServerInputRequestTypeDef(
    _RequiredClaimGameServerInputRequestTypeDef, _OptionalClaimGameServerInputRequestTypeDef
):
    pass

ClaimGameServerOutputTypeDef = TypedDict(
    "ClaimGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAliasInputRequestTypeDef = TypedDict(
    "_RequiredCreateAliasInputRequestTypeDef",
    {
        "Name": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
    },
)
_OptionalCreateAliasInputRequestTypeDef = TypedDict(
    "_OptionalCreateAliasInputRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAliasInputRequestTypeDef(
    _RequiredCreateAliasInputRequestTypeDef, _OptionalCreateAliasInputRequestTypeDef
):
    pass

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBuildInputRequestTypeDef = TypedDict(
    "CreateBuildInputRequestTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "OperatingSystem": OperatingSystemType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetInputRequestTypeDef = TypedDict(
    "_RequiredCreateFleetInputRequestTypeDef",
    {
        "Name": str,
        "EC2InstanceType": EC2InstanceTypeType,
    },
)
_OptionalCreateFleetInputRequestTypeDef = TypedDict(
    "_OptionalCreateFleetInputRequestTypeDef",
    {
        "Description": str,
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "EC2InboundPermissions": List["IpPermissionTypeDef"],
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "FleetType": FleetTypeType,
        "InstanceRoleArn": str,
        "CertificateConfiguration": "CertificateConfigurationTypeDef",
        "Locations": List["LocationConfigurationTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFleetInputRequestTypeDef(
    _RequiredCreateFleetInputRequestTypeDef, _OptionalCreateFleetInputRequestTypeDef
):
    pass

CreateFleetLocationsInputRequestTypeDef = TypedDict(
    "CreateFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": List["LocationConfigurationTypeDef"],
    },
)

CreateFleetLocationsOutputTypeDef = TypedDict(
    "CreateFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef",
    {
        "FleetAttributes": "FleetAttributesTypeDef",
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameServerGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
    },
)
_OptionalCreateGameServerGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateGameServerGroupInputRequestTypeDef",
    {
        "AutoScalingPolicy": "GameServerGroupAutoScalingPolicyTypeDef",
        "BalancingStrategy": BalancingStrategyType,
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "VpcSubnets": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateGameServerGroupInputRequestTypeDef(
    _RequiredCreateGameServerGroupInputRequestTypeDef,
    _OptionalCreateGameServerGroupInputRequestTypeDef,
):
    pass

CreateGameServerGroupOutputTypeDef = TypedDict(
    "CreateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameSessionInputRequestTypeDef = TypedDict(
    "_RequiredCreateGameSessionInputRequestTypeDef",
    {
        "MaximumPlayerSessionCount": int,
    },
)
_OptionalCreateGameSessionInputRequestTypeDef = TypedDict(
    "_OptionalCreateGameSessionInputRequestTypeDef",
    {
        "FleetId": str,
        "AliasId": str,
        "Name": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "CreatorId": str,
        "GameSessionId": str,
        "IdempotencyToken": str,
        "GameSessionData": str,
        "Location": str,
    },
    total=False,
)

class CreateGameSessionInputRequestTypeDef(
    _RequiredCreateGameSessionInputRequestTypeDef, _OptionalCreateGameSessionInputRequestTypeDef
):
    pass

CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameSessionQueueInputRequestTypeDef = TypedDict(
    "_RequiredCreateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGameSessionQueueInputRequestTypeDef = TypedDict(
    "_OptionalCreateGameSessionQueueInputRequestTypeDef",
    {
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateGameSessionQueueInputRequestTypeDef(
    _RequiredCreateGameSessionQueueInputRequestTypeDef,
    _OptionalCreateGameSessionQueueInputRequestTypeDef,
):
    pass

CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredCreateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "RequestTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
    },
)
_OptionalCreateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalCreateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Description": str,
        "GameSessionQueueArns": List[str],
        "AcceptanceTimeoutSeconds": int,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMatchmakingConfigurationInputRequestTypeDef(
    _RequiredCreateMatchmakingConfigurationInputRequestTypeDef,
    _OptionalCreateMatchmakingConfigurationInputRequestTypeDef,
):
    pass

CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "_RequiredCreateMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
        "RuleSetBody": str,
    },
)
_OptionalCreateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "_OptionalCreateMatchmakingRuleSetInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMatchmakingRuleSetInputRequestTypeDef(
    _RequiredCreateMatchmakingRuleSetInputRequestTypeDef,
    _OptionalCreateMatchmakingRuleSetInputRequestTypeDef,
):
    pass

CreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputTypeDef",
    {
        "RuleSet": "MatchmakingRuleSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlayerSessionInputRequestTypeDef = TypedDict(
    "_RequiredCreatePlayerSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
    },
)
_OptionalCreatePlayerSessionInputRequestTypeDef = TypedDict(
    "_OptionalCreatePlayerSessionInputRequestTypeDef",
    {
        "PlayerData": str,
    },
    total=False,
)

class CreatePlayerSessionInputRequestTypeDef(
    _RequiredCreatePlayerSessionInputRequestTypeDef, _OptionalCreatePlayerSessionInputRequestTypeDef
):
    pass

CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef",
    {
        "PlayerSession": "PlayerSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlayerSessionsInputRequestTypeDef = TypedDict(
    "_RequiredCreatePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerIds": List[str],
    },
)
_OptionalCreatePlayerSessionsInputRequestTypeDef = TypedDict(
    "_OptionalCreatePlayerSessionsInputRequestTypeDef",
    {
        "PlayerDataMap": Dict[str, str],
    },
    total=False,
)

class CreatePlayerSessionsInputRequestTypeDef(
    _RequiredCreatePlayerSessionsInputRequestTypeDef,
    _OptionalCreatePlayerSessionsInputRequestTypeDef,
):
    pass

CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptInputRequestTypeDef = TypedDict(
    "CreateScriptInputRequestTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {
        "VpcPeeringAuthorization": "VpcPeeringAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

DeleteBuildInputRequestTypeDef = TypedDict(
    "DeleteBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

DeleteFleetInputRequestTypeDef = TypedDict(
    "DeleteFleetInputRequestTypeDef",
    {
        "FleetId": str,
    },
)

DeleteFleetLocationsInputRequestTypeDef = TypedDict(
    "DeleteFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": List[str],
    },
)

DeleteFleetLocationsOutputTypeDef = TypedDict(
    "DeleteFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteGameServerGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalDeleteGameServerGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteGameServerGroupInputRequestTypeDef",
    {
        "DeleteOption": GameServerGroupDeleteOptionType,
    },
    total=False,
)

class DeleteGameServerGroupInputRequestTypeDef(
    _RequiredDeleteGameServerGroupInputRequestTypeDef,
    _OptionalDeleteGameServerGroupInputRequestTypeDef,
):
    pass

DeleteGameServerGroupOutputTypeDef = TypedDict(
    "DeleteGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameSessionQueueInputRequestTypeDef = TypedDict(
    "DeleteGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScalingPolicyInputRequestTypeDef = TypedDict(
    "DeleteScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
    },
)

DeleteScriptInputRequestTypeDef = TypedDict(
    "DeleteScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)

DeleteVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "VpcPeeringConnectionId": str,
    },
)

DeregisterGameServerInputRequestTypeDef = TypedDict(
    "DeregisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

DescribeAliasInputRequestTypeDef = TypedDict(
    "DescribeAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBuildInputRequestTypeDef = TypedDict(
    "DescribeBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEC2InstanceLimitsInputRequestTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    {
        "EC2InstanceType": EC2InstanceTypeType,
        "Location": str,
    },
    total=False,
)

DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {
        "EC2InstanceLimits": List["EC2InstanceLimitTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAttributesInputRequestTypeDef = TypedDict(
    "DescribeFleetAttributesInputRequestTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {
        "FleetAttributes": List["FleetAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetCapacityInputRequestTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {
        "FleetCapacity": List["FleetCapacityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetEventsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetEventsInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetEventsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetEventsInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeFleetEventsInputRequestTypeDef(
    _RequiredDescribeFleetEventsInputRequestTypeDef, _OptionalDescribeFleetEventsInputRequestTypeDef
):
    pass

DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetLocationAttributesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetLocationAttributesInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetLocationAttributesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetLocationAttributesInputRequestTypeDef",
    {
        "Locations": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeFleetLocationAttributesInputRequestTypeDef(
    _RequiredDescribeFleetLocationAttributesInputRequestTypeDef,
    _OptionalDescribeFleetLocationAttributesInputRequestTypeDef,
):
    pass

DescribeFleetLocationAttributesOutputTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List["LocationAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationCapacityOutputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputTypeDef",
    {
        "FleetCapacity": "FleetCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputTypeDef",
    {
        "FleetUtilization": "FleetUtilizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetPortSettingsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetPortSettingsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetPortSettingsInputRequestTypeDef",
    {
        "Location": str,
    },
    total=False,
)

class DescribeFleetPortSettingsInputRequestTypeDef(
    _RequiredDescribeFleetPortSettingsInputRequestTypeDef,
    _OptionalDescribeFleetPortSettingsInputRequestTypeDef,
):
    pass

DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List["IpPermissionTypeDef"],
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetUtilizationInputRequestTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {
        "FleetUtilization": List["FleetUtilizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerGroupInputRequestTypeDef = TypedDict(
    "DescribeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)

DescribeGameServerGroupOutputTypeDef = TypedDict(
    "DescribeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerInputRequestTypeDef = TypedDict(
    "DescribeGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

_RequiredDescribeGameServerInstancesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeGameServerInstancesInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalDescribeGameServerInstancesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeGameServerInstancesInputRequestTypeDef",
    {
        "InstanceIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeGameServerInstancesInputRequestTypeDef(
    _RequiredDescribeGameServerInstancesInputRequestTypeDef,
    _OptionalDescribeGameServerInstancesInputRequestTypeDef,
):
    pass

DescribeGameServerInstancesOutputTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputTypeDef",
    {
        "GameServerInstances": List["GameServerInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerOutputTypeDef = TypedDict(
    "DescribeGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionDetailsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionDetailsInputRequestTypeDef",
    {
        "FleetId": str,
        "GameSessionId": str,
        "AliasId": str,
        "Location": str,
        "StatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {
        "GameSessionDetails": List["GameSessionDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionPlacementInputRequestTypeDef = TypedDict(
    "DescribeGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)

DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionQueuesInputRequestTypeDef = TypedDict(
    "DescribeGameSessionQueuesInputRequestTypeDef",
    {
        "Names": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {
        "GameSessionQueues": List["GameSessionQueueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionsInputRequestTypeDef",
    {
        "FleetId": str,
        "GameSessionId": str,
        "AliasId": str,
        "Location": str,
        "StatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancesInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeInstancesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancesInputRequestTypeDef",
    {
        "InstanceId": str,
        "Limit": int,
        "NextToken": str,
        "Location": str,
    },
    total=False,
)

class DescribeInstancesInputRequestTypeDef(
    _RequiredDescribeInstancesInputRequestTypeDef, _OptionalDescribeInstancesInputRequestTypeDef
):
    pass

DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingConfigurationsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    {
        "Names": List[str],
        "RuleSetName": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {
        "Configurations": List["MatchmakingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingInputRequestTypeDef",
    {
        "TicketIds": List[str],
    },
)

DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef",
    {
        "TicketList": List["MatchmakingTicketTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingRuleSetsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    {
        "Names": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    {
        "RuleSets": List["MatchmakingRuleSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlayerSessionsInputRequestTypeDef = TypedDict(
    "DescribePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
        "PlayerSessionId": str,
        "PlayerSessionStatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
    },
)

DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingPoliciesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingPoliciesInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeScalingPoliciesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingPoliciesInputRequestTypeDef",
    {
        "StatusFilter": ScalingStatusTypeType,
        "Limit": int,
        "NextToken": str,
        "Location": str,
    },
    total=False,
)

class DescribeScalingPoliciesInputRequestTypeDef(
    _RequiredDescribeScalingPoliciesInputRequestTypeDef,
    _OptionalDescribeScalingPoliciesInputRequestTypeDef,
):
    pass

DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScriptInputRequestTypeDef = TypedDict(
    "DescribeScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)

DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {
        "VpcPeeringAuthorizations": List["VpcPeeringAuthorizationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsInputRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    {
        "FleetId": str,
    },
    total=False,
)

DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerData": str,
    },
    total=False,
)

EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": EC2InstanceTypeType,
        "CurrentInstances": int,
        "InstanceLimit": int,
        "Location": str,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": EventCodeType,
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "AllowedLocations": List[str],
    },
    total=False,
)

FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": FleetTypeType,
        "InstanceType": EC2InstanceTypeType,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": FleetStatusType,
        "BuildId": str,
        "BuildArn": str,
        "ScriptId": str,
        "ScriptArn": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "OperatingSystem": OperatingSystemType,
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
        "StoppedActions": List[Literal["AUTO_SCALING"]],
        "InstanceRoleArn": str,
        "CertificateConfiguration": "CertificateConfigurationTypeDef",
    },
    total=False,
)

FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceType": EC2InstanceTypeType,
        "InstanceCounts": "EC2InstanceCountsTypeDef",
        "Location": str,
    },
    total=False,
)

FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Location": str,
    },
    total=False,
)

GamePropertyTypeDef = TypedDict(
    "GamePropertyTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_RequiredGameServerGroupAutoScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
    },
)
_OptionalGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_OptionalGameServerGroupAutoScalingPolicyTypeDef",
    {
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

class GameServerGroupAutoScalingPolicyTypeDef(
    _RequiredGameServerGroupAutoScalingPolicyTypeDef,
    _OptionalGameServerGroupAutoScalingPolicyTypeDef,
):
    pass

GameServerGroupTypeDef = TypedDict(
    "GameServerGroupTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "RoleArn": str,
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
        "BalancingStrategy": BalancingStrategyType,
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "AutoScalingGroupArn": str,
        "Status": GameServerGroupStatusType,
        "StatusReason": str,
        "SuspendedActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

GameServerInstanceTypeDef = TypedDict(
    "GameServerInstanceTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "InstanceId": str,
        "InstanceStatus": GameServerInstanceStatusType,
    },
    total=False,
)

GameServerTypeDef = TypedDict(
    "GameServerTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "GameServerId": str,
        "InstanceId": str,
        "ConnectionInfo": str,
        "GameServerData": str,
        "ClaimStatus": Literal["CLAIMED"],
        "UtilizationStatus": GameServerUtilizationStatusType,
        "RegistrationTime": datetime,
        "LastClaimTime": datetime,
        "LastHealthCheckTime": datetime,
    },
    total=False,
)

GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List["MatchedPlayerSessionTypeDef"],
    },
    total=False,
)

GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ProtectionPolicy": ProtectionPolicyType,
    },
    total=False,
)

GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": GameSessionPlacementStateType,
        "GameProperties": List["GamePropertyTypeDef"],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List["PlayerLatencyTypeDef"],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List["PlacedPlayerSessionTypeDef"],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
    },
    total=False,
)

GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": GameSessionStatusType,
        "StatusReason": Literal["INTERRUPTED"],
        "GameProperties": List["GamePropertyTypeDef"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": PlayerSessionCreationPolicyType,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
        "Location": str,
    },
    total=False,
)

GetGameSessionLogUrlInputRequestTypeDef = TypedDict(
    "GetGameSessionLogUrlInputRequestTypeDef",
    {
        "GameSessionId": str,
    },
)

GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef",
    {
        "PreSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceAccessInputRequestTypeDef = TypedDict(
    "GetInstanceAccessInputRequestTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
    },
)

GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef",
    {
        "InstanceAccess": "InstanceAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": OperatingSystemType,
        "Credentials": "InstanceCredentialsTypeDef",
    },
    total=False,
)

InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef",
    {
        "UserName": str,
        "Secret": str,
    },
    total=False,
)

_RequiredInstanceDefinitionTypeDef = TypedDict(
    "_RequiredInstanceDefinitionTypeDef",
    {
        "InstanceType": GameServerGroupInstanceTypeType,
    },
)
_OptionalInstanceDefinitionTypeDef = TypedDict(
    "_OptionalInstanceDefinitionTypeDef",
    {
        "WeightedCapacity": str,
    },
    total=False,
)

class InstanceDefinitionTypeDef(
    _RequiredInstanceDefinitionTypeDef, _OptionalInstanceDefinitionTypeDef
):
    pass

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": OperatingSystemType,
        "Type": EC2InstanceTypeType,
        "Status": InstanceStatusType,
        "CreationTime": datetime,
        "Location": str,
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "IpRange": str,
        "Protocol": IpProtocolType,
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "RoutingStrategyType": RoutingStrategyTypeType,
        "Name": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputRequestTypeDef = TypedDict(
    "ListBuildsInputRequestTypeDef",
    {
        "Status": BuildStatusType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "Builds": List["BuildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsInputRequestTypeDef = TypedDict(
    "ListFleetsInputRequestTypeDef",
    {
        "BuildId": str,
        "ScriptId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef",
    {
        "FleetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServerGroupsInputRequestTypeDef = TypedDict(
    "ListGameServerGroupsInputRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListGameServerGroupsOutputTypeDef = TypedDict(
    "ListGameServerGroupsOutputTypeDef",
    {
        "GameServerGroups": List["GameServerGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGameServersInputRequestTypeDef = TypedDict(
    "_RequiredListGameServersInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalListGameServersInputRequestTypeDef = TypedDict(
    "_OptionalListGameServersInputRequestTypeDef",
    {
        "SortOrder": SortOrderType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListGameServersInputRequestTypeDef(
    _RequiredListGameServersInputRequestTypeDef, _OptionalListGameServersInputRequestTypeDef
):
    pass

ListGameServersOutputTypeDef = TypedDict(
    "ListGameServersOutputTypeDef",
    {
        "GameServers": List["GameServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScriptsInputRequestTypeDef = TypedDict(
    "ListScriptsInputRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef",
    {
        "Scripts": List["ScriptTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationAttributesTypeDef = TypedDict(
    "LocationAttributesTypeDef",
    {
        "LocationState": "LocationStateTypeDef",
        "StoppedActions": List[Literal["AUTO_SCALING"]],
        "UpdateStatus": Literal["PENDING_UPDATE"],
    },
    total=False,
)

LocationConfigurationTypeDef = TypedDict(
    "LocationConfigurationTypeDef",
    {
        "Location": str,
    },
    total=False,
)

LocationStateTypeDef = TypedDict(
    "LocationStateTypeDef",
    {
        "Location": str,
        "Status": FleetStatusType,
    },
    total=False,
)

MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerSessionId": str,
    },
    total=False,
)

MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": str,
        "ConfigurationArn": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "RuleSetArn": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
    },
    total=False,
)

_RequiredMatchmakingRuleSetTypeDef = TypedDict(
    "_RequiredMatchmakingRuleSetTypeDef",
    {
        "RuleSetBody": str,
    },
)
_OptionalMatchmakingRuleSetTypeDef = TypedDict(
    "_OptionalMatchmakingRuleSetTypeDef",
    {
        "RuleSetName": str,
        "RuleSetArn": str,
        "CreationTime": datetime,
    },
    total=False,
)

class MatchmakingRuleSetTypeDef(
    _RequiredMatchmakingRuleSetTypeDef, _OptionalMatchmakingRuleSetTypeDef
):
    pass

MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "ConfigurationArn": str,
        "Status": MatchmakingConfigurationStatusType,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List["PlayerTypeDef"],
        "GameSessionConnectionInfo": "GameSessionConnectionInfoTypeDef",
        "EstimatedWaitTime": int,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerSessionId": str,
    },
    total=False,
)

PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {
        "MaximumIndividualPlayerLatencyMilliseconds": int,
        "PolicyDurationSeconds": int,
    },
    total=False,
)

PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {
        "PlayerId": str,
        "RegionIdentifier": str,
        "LatencyInMilliseconds": float,
    },
    total=False,
)

PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": PlayerSessionStatusType,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, "AttributeValueTypeDef"],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

PriorityConfigurationTypeDef = TypedDict(
    "PriorityConfigurationTypeDef",
    {
        "PriorityOrder": List[PriorityTypeType],
        "LocationOrder": List[str],
    },
    total=False,
)

_RequiredPutScalingPolicyInputRequestTypeDef = TypedDict(
    "_RequiredPutScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
        "MetricName": MetricNameType,
    },
)
_OptionalPutScalingPolicyInputRequestTypeDef = TypedDict(
    "_OptionalPutScalingPolicyInputRequestTypeDef",
    {
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": ScalingAdjustmentTypeType,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorTypeType,
        "EvaluationPeriods": int,
        "PolicyType": PolicyTypeType,
        "TargetConfiguration": "TargetConfigurationTypeDef",
    },
    total=False,
)

class PutScalingPolicyInputRequestTypeDef(
    _RequiredPutScalingPolicyInputRequestTypeDef, _OptionalPutScalingPolicyInputRequestTypeDef
):
    pass

PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterGameServerInputRequestTypeDef = TypedDict(
    "_RequiredRegisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "InstanceId": str,
    },
)
_OptionalRegisterGameServerInputRequestTypeDef = TypedDict(
    "_OptionalRegisterGameServerInputRequestTypeDef",
    {
        "ConnectionInfo": str,
        "GameServerData": str,
    },
    total=False,
)

class RegisterGameServerInputRequestTypeDef(
    _RequiredRegisterGameServerInputRequestTypeDef, _OptionalRegisterGameServerInputRequestTypeDef
):
    pass

RegisterGameServerOutputTypeDef = TypedDict(
    "RegisterGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestUploadCredentialsInputRequestTypeDef = TypedDict(
    "RequestUploadCredentialsInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveAliasInputRequestTypeDef = TypedDict(
    "ResolveAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

ResolveAliasOutputTypeDef = TypedDict(
    "ResolveAliasOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {
        "NewGameSessionsPerCreator": int,
        "PolicyPeriodInMinutes": int,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResumeGameServerGroupInputRequestTypeDef = TypedDict(
    "ResumeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "ResumeActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

ResumeGameServerGroupOutputTypeDef = TypedDict(
    "ResumeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {
        "Type": RoutingStrategyTypeType,
        "FleetId": str,
        "Message": str,
    },
    total=False,
)

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List["ServerProcessTypeDef"],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "RoleArn": str,
        "ObjectVersion": str,
    },
    total=False,
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Name": str,
        "Status": ScalingStatusTypeType,
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": ScalingAdjustmentTypeType,
        "ComparisonOperator": ComparisonOperatorTypeType,
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": MetricNameType,
        "PolicyType": PolicyTypeType,
        "TargetConfiguration": "TargetConfigurationTypeDef",
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
    },
    total=False,
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": str,
        "ScriptArn": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": "S3LocationTypeDef",
    },
    total=False,
)

SearchGameSessionsInputRequestTypeDef = TypedDict(
    "SearchGameSessionsInputRequestTypeDef",
    {
        "FleetId": str,
        "AliasId": str,
        "Location": str,
        "FilterExpression": str,
        "SortExpression": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredServerProcessTypeDef = TypedDict(
    "_RequiredServerProcessTypeDef",
    {
        "LaunchPath": str,
        "ConcurrentExecutions": int,
    },
)
_OptionalServerProcessTypeDef = TypedDict(
    "_OptionalServerProcessTypeDef",
    {
        "Parameters": str,
    },
    total=False,
)

class ServerProcessTypeDef(_RequiredServerProcessTypeDef, _OptionalServerProcessTypeDef):
    pass

_RequiredStartFleetActionsInputRequestTypeDef = TypedDict(
    "_RequiredStartFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": List[Literal["AUTO_SCALING"]],
    },
)
_OptionalStartFleetActionsInputRequestTypeDef = TypedDict(
    "_OptionalStartFleetActionsInputRequestTypeDef",
    {
        "Location": str,
    },
    total=False,
)

class StartFleetActionsInputRequestTypeDef(
    _RequiredStartFleetActionsInputRequestTypeDef, _OptionalStartFleetActionsInputRequestTypeDef
):
    pass

StartFleetActionsOutputTypeDef = TypedDict(
    "StartFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartGameSessionPlacementInputRequestTypeDef = TypedDict(
    "_RequiredStartGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "MaximumPlayerSessionCount": int,
    },
)
_OptionalStartGameSessionPlacementInputRequestTypeDef = TypedDict(
    "_OptionalStartGameSessionPlacementInputRequestTypeDef",
    {
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionName": str,
        "PlayerLatencies": List["PlayerLatencyTypeDef"],
        "DesiredPlayerSessions": List["DesiredPlayerSessionTypeDef"],
        "GameSessionData": str,
    },
    total=False,
)

class StartGameSessionPlacementInputRequestTypeDef(
    _RequiredStartGameSessionPlacementInputRequestTypeDef,
    _OptionalStartGameSessionPlacementInputRequestTypeDef,
):
    pass

StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMatchBackfillInputRequestTypeDef = TypedDict(
    "_RequiredStartMatchBackfillInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": List["PlayerTypeDef"],
    },
)
_OptionalStartMatchBackfillInputRequestTypeDef = TypedDict(
    "_OptionalStartMatchBackfillInputRequestTypeDef",
    {
        "TicketId": str,
        "GameSessionArn": str,
    },
    total=False,
)

class StartMatchBackfillInputRequestTypeDef(
    _RequiredStartMatchBackfillInputRequestTypeDef, _OptionalStartMatchBackfillInputRequestTypeDef
):
    pass

StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMatchmakingInputRequestTypeDef = TypedDict(
    "_RequiredStartMatchmakingInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": List["PlayerTypeDef"],
    },
)
_OptionalStartMatchmakingInputRequestTypeDef = TypedDict(
    "_OptionalStartMatchmakingInputRequestTypeDef",
    {
        "TicketId": str,
    },
    total=False,
)

class StartMatchmakingInputRequestTypeDef(
    _RequiredStartMatchmakingInputRequestTypeDef, _OptionalStartMatchmakingInputRequestTypeDef
):
    pass

StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopFleetActionsInputRequestTypeDef = TypedDict(
    "_RequiredStopFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": List[Literal["AUTO_SCALING"]],
    },
)
_OptionalStopFleetActionsInputRequestTypeDef = TypedDict(
    "_OptionalStopFleetActionsInputRequestTypeDef",
    {
        "Location": str,
    },
    total=False,
)

class StopFleetActionsInputRequestTypeDef(
    _RequiredStopFleetActionsInputRequestTypeDef, _OptionalStopFleetActionsInputRequestTypeDef
):
    pass

StopFleetActionsOutputTypeDef = TypedDict(
    "StopFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopGameSessionPlacementInputRequestTypeDef = TypedDict(
    "StopGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)

StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMatchmakingInputRequestTypeDef = TypedDict(
    "StopMatchmakingInputRequestTypeDef",
    {
        "TicketId": str,
    },
)

SuspendGameServerGroupInputRequestTypeDef = TypedDict(
    "SuspendGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "SuspendActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

SuspendGameServerGroupOutputTypeDef = TypedDict(
    "SuspendGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAliasInputRequestTypeDef = TypedDict(
    "_RequiredUpdateAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)
_OptionalUpdateAliasInputRequestTypeDef = TypedDict(
    "_OptionalUpdateAliasInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
    },
    total=False,
)

class UpdateAliasInputRequestTypeDef(
    _RequiredUpdateAliasInputRequestTypeDef, _OptionalUpdateAliasInputRequestTypeDef
):
    pass

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBuildInputRequestTypeDef = TypedDict(
    "_RequiredUpdateBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)
_OptionalUpdateBuildInputRequestTypeDef = TypedDict(
    "_OptionalUpdateBuildInputRequestTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

class UpdateBuildInputRequestTypeDef(
    _RequiredUpdateBuildInputRequestTypeDef, _OptionalUpdateBuildInputRequestTypeDef
):
    pass

UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetAttributesInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetAttributesInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetAttributesInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetAttributesInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
    },
    total=False,
)

class UpdateFleetAttributesInputRequestTypeDef(
    _RequiredUpdateFleetAttributesInputRequestTypeDef,
    _OptionalUpdateFleetAttributesInputRequestTypeDef,
):
    pass

UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetCapacityInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetCapacityInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetCapacityInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetCapacityInputRequestTypeDef",
    {
        "DesiredInstances": int,
        "MinSize": int,
        "MaxSize": int,
        "Location": str,
    },
    total=False,
)

class UpdateFleetCapacityInputRequestTypeDef(
    _RequiredUpdateFleetCapacityInputRequestTypeDef, _OptionalUpdateFleetCapacityInputRequestTypeDef
):
    pass

UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetPortSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetPortSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetPortSettingsInputRequestTypeDef",
    {
        "InboundPermissionAuthorizations": List["IpPermissionTypeDef"],
        "InboundPermissionRevocations": List["IpPermissionTypeDef"],
    },
    total=False,
)

class UpdateFleetPortSettingsInputRequestTypeDef(
    _RequiredUpdateFleetPortSettingsInputRequestTypeDef,
    _OptionalUpdateFleetPortSettingsInputRequestTypeDef,
):
    pass

UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameServerGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalUpdateGameServerGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGameServerGroupInputRequestTypeDef",
    {
        "RoleArn": str,
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "BalancingStrategy": BalancingStrategyType,
    },
    total=False,
)

class UpdateGameServerGroupInputRequestTypeDef(
    _RequiredUpdateGameServerGroupInputRequestTypeDef,
    _OptionalUpdateGameServerGroupInputRequestTypeDef,
):
    pass

UpdateGameServerGroupOutputTypeDef = TypedDict(
    "UpdateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameServerInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)
_OptionalUpdateGameServerInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGameServerInputRequestTypeDef",
    {
        "GameServerData": str,
        "UtilizationStatus": GameServerUtilizationStatusType,
        "HealthCheck": Literal["HEALTHY"],
    },
    total=False,
)

class UpdateGameServerInputRequestTypeDef(
    _RequiredUpdateGameServerInputRequestTypeDef, _OptionalUpdateGameServerInputRequestTypeDef
):
    pass

UpdateGameServerOutputTypeDef = TypedDict(
    "UpdateGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameSessionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGameSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
    },
)
_OptionalUpdateGameSessionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGameSessionInputRequestTypeDef",
    {
        "MaximumPlayerSessionCount": int,
        "Name": str,
        "PlayerSessionCreationPolicy": PlayerSessionCreationPolicyType,
        "ProtectionPolicy": ProtectionPolicyType,
    },
    total=False,
)

class UpdateGameSessionInputRequestTypeDef(
    _RequiredUpdateGameSessionInputRequestTypeDef, _OptionalUpdateGameSessionInputRequestTypeDef
):
    pass

UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameSessionQueueInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateGameSessionQueueInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGameSessionQueueInputRequestTypeDef",
    {
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
    },
    total=False,
)

class UpdateGameSessionQueueInputRequestTypeDef(
    _RequiredUpdateGameSessionQueueInputRequestTypeDef,
    _OptionalUpdateGameSessionQueueInputRequestTypeDef,
):
    pass

UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
    },
    total=False,
)

class UpdateMatchmakingConfigurationInputRequestTypeDef(
    _RequiredUpdateMatchmakingConfigurationInputRequestTypeDef,
    _OptionalUpdateMatchmakingConfigurationInputRequestTypeDef,
):
    pass

UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
    },
)

UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScriptInputRequestTypeDef = TypedDict(
    "_RequiredUpdateScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)
_OptionalUpdateScriptInputRequestTypeDef = TypedDict(
    "_OptionalUpdateScriptInputRequestTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class UpdateScriptInputRequestTypeDef(
    _RequiredUpdateScriptInputRequestTypeDef, _OptionalUpdateScriptInputRequestTypeDef
):
    pass

UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    {
        "RuleSetBody": str,
    },
)

ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef",
    {
        "Valid": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": "VpcPeeringConnectionStatusTypeDef",
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)
