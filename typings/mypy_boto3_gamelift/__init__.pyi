"""
Main interface for gamelift service.

Usage::

    ```python
    import boto3
    from mypy_boto3_gamelift import (
        Client,
        DescribeFleetAttributesPaginator,
        DescribeFleetCapacityPaginator,
        DescribeFleetEventsPaginator,
        DescribeFleetUtilizationPaginator,
        DescribeGameSessionDetailsPaginator,
        DescribeGameSessionQueuesPaginator,
        DescribeGameSessionsPaginator,
        DescribeInstancesPaginator,
        DescribeMatchmakingConfigurationsPaginator,
        DescribeMatchmakingRuleSetsPaginator,
        DescribePlayerSessionsPaginator,
        DescribeScalingPoliciesPaginator,
        GameLiftClient,
        ListAliasesPaginator,
        ListBuildsPaginator,
        ListFleetsPaginator,
        SearchGameSessionsPaginator,
    )

    session = boto3.Session()

    client: GameLiftClient = boto3.client("gamelift")
    session_client: GameLiftClient = session.client("gamelift")

    describe_fleet_attributes_paginator: DescribeFleetAttributesPaginator = client.get_paginator("describe_fleet_attributes")
    describe_fleet_capacity_paginator: DescribeFleetCapacityPaginator = client.get_paginator("describe_fleet_capacity")
    describe_fleet_events_paginator: DescribeFleetEventsPaginator = client.get_paginator("describe_fleet_events")
    describe_fleet_utilization_paginator: DescribeFleetUtilizationPaginator = client.get_paginator("describe_fleet_utilization")
    describe_game_session_details_paginator: DescribeGameSessionDetailsPaginator = client.get_paginator("describe_game_session_details")
    describe_game_session_queues_paginator: DescribeGameSessionQueuesPaginator = client.get_paginator("describe_game_session_queues")
    describe_game_sessions_paginator: DescribeGameSessionsPaginator = client.get_paginator("describe_game_sessions")
    describe_instances_paginator: DescribeInstancesPaginator = client.get_paginator("describe_instances")
    describe_matchmaking_configurations_paginator: DescribeMatchmakingConfigurationsPaginator = client.get_paginator("describe_matchmaking_configurations")
    describe_matchmaking_rule_sets_paginator: DescribeMatchmakingRuleSetsPaginator = client.get_paginator("describe_matchmaking_rule_sets")
    describe_player_sessions_paginator: DescribePlayerSessionsPaginator = client.get_paginator("describe_player_sessions")
    describe_scaling_policies_paginator: DescribeScalingPoliciesPaginator = client.get_paginator("describe_scaling_policies")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_builds_paginator: ListBuildsPaginator = client.get_paginator("list_builds")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    search_game_sessions_paginator: SearchGameSessionsPaginator = client.get_paginator("search_game_sessions")
    ```
"""
from mypy_boto3_gamelift.client import GameLiftClient
from mypy_boto3_gamelift.paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
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
    ListFleetsPaginator,
    SearchGameSessionsPaginator,
)

Client = GameLiftClient


__all__ = (
    "Client",
    "DescribeFleetAttributesPaginator",
    "DescribeFleetCapacityPaginator",
    "DescribeFleetEventsPaginator",
    "DescribeFleetUtilizationPaginator",
    "DescribeGameSessionDetailsPaginator",
    "DescribeGameSessionQueuesPaginator",
    "DescribeGameSessionsPaginator",
    "DescribeInstancesPaginator",
    "DescribeMatchmakingConfigurationsPaginator",
    "DescribeMatchmakingRuleSetsPaginator",
    "DescribePlayerSessionsPaginator",
    "DescribeScalingPoliciesPaginator",
    "GameLiftClient",
    "ListAliasesPaginator",
    "ListBuildsPaginator",
    "ListFleetsPaginator",
    "SearchGameSessionsPaginator",
)
