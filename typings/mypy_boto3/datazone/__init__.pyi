"""
Main interface for datazone service.

Usage::

    ```python
    import boto3
    from mypy_boto3_datazone import (
        Client,
        DataZoneClient,
        ListAssetRevisionsPaginator,
        ListDataSourceRunActivitiesPaginator,
        ListDataSourceRunsPaginator,
        ListDataSourcesPaginator,
        ListDomainsPaginator,
        ListEnvironmentActionsPaginator,
        ListEnvironmentBlueprintConfigurationsPaginator,
        ListEnvironmentBlueprintsPaginator,
        ListEnvironmentProfilesPaginator,
        ListEnvironmentsPaginator,
        ListLineageNodeHistoryPaginator,
        ListMetadataGenerationRunsPaginator,
        ListNotificationsPaginator,
        ListProjectMembershipsPaginator,
        ListProjectsPaginator,
        ListSubscriptionGrantsPaginator,
        ListSubscriptionRequestsPaginator,
        ListSubscriptionTargetsPaginator,
        ListSubscriptionsPaginator,
        ListTimeSeriesDataPointsPaginator,
        SearchGroupProfilesPaginator,
        SearchListingsPaginator,
        SearchPaginator,
        SearchTypesPaginator,
        SearchUserProfilesPaginator,
    )

    session = boto3.Session()

    client: DataZoneClient = boto3.client("datazone")
    session_client: DataZoneClient = session.client("datazone")

    list_asset_revisions_paginator: ListAssetRevisionsPaginator = client.get_paginator("list_asset_revisions")
    list_data_source_run_activities_paginator: ListDataSourceRunActivitiesPaginator = client.get_paginator("list_data_source_run_activities")
    list_data_source_runs_paginator: ListDataSourceRunsPaginator = client.get_paginator("list_data_source_runs")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_environment_actions_paginator: ListEnvironmentActionsPaginator = client.get_paginator("list_environment_actions")
    list_environment_blueprint_configurations_paginator: ListEnvironmentBlueprintConfigurationsPaginator = client.get_paginator("list_environment_blueprint_configurations")
    list_environment_blueprints_paginator: ListEnvironmentBlueprintsPaginator = client.get_paginator("list_environment_blueprints")
    list_environment_profiles_paginator: ListEnvironmentProfilesPaginator = client.get_paginator("list_environment_profiles")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_lineage_node_history_paginator: ListLineageNodeHistoryPaginator = client.get_paginator("list_lineage_node_history")
    list_metadata_generation_runs_paginator: ListMetadataGenerationRunsPaginator = client.get_paginator("list_metadata_generation_runs")
    list_notifications_paginator: ListNotificationsPaginator = client.get_paginator("list_notifications")
    list_project_memberships_paginator: ListProjectMembershipsPaginator = client.get_paginator("list_project_memberships")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_subscription_grants_paginator: ListSubscriptionGrantsPaginator = client.get_paginator("list_subscription_grants")
    list_subscription_requests_paginator: ListSubscriptionRequestsPaginator = client.get_paginator("list_subscription_requests")
    list_subscription_targets_paginator: ListSubscriptionTargetsPaginator = client.get_paginator("list_subscription_targets")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_time_series_data_points_paginator: ListTimeSeriesDataPointsPaginator = client.get_paginator("list_time_series_data_points")
    search_paginator: SearchPaginator = client.get_paginator("search")
    search_group_profiles_paginator: SearchGroupProfilesPaginator = client.get_paginator("search_group_profiles")
    search_listings_paginator: SearchListingsPaginator = client.get_paginator("search_listings")
    search_types_paginator: SearchTypesPaginator = client.get_paginator("search_types")
    search_user_profiles_paginator: SearchUserProfilesPaginator = client.get_paginator("search_user_profiles")
    ```
"""

from .client import DataZoneClient
from .paginator import (
    ListAssetRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListEnvironmentActionsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListLineageNodeHistoryPaginator,
    ListMetadataGenerationRunsPaginator,
    ListNotificationsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectsPaginator,
    ListSubscriptionGrantsPaginator,
    ListSubscriptionRequestsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionTargetsPaginator,
    ListTimeSeriesDataPointsPaginator,
    SearchGroupProfilesPaginator,
    SearchListingsPaginator,
    SearchPaginator,
    SearchTypesPaginator,
    SearchUserProfilesPaginator,
)

Client = DataZoneClient

__all__ = (
    "Client",
    "DataZoneClient",
    "ListAssetRevisionsPaginator",
    "ListDataSourceRunActivitiesPaginator",
    "ListDataSourceRunsPaginator",
    "ListDataSourcesPaginator",
    "ListDomainsPaginator",
    "ListEnvironmentActionsPaginator",
    "ListEnvironmentBlueprintConfigurationsPaginator",
    "ListEnvironmentBlueprintsPaginator",
    "ListEnvironmentProfilesPaginator",
    "ListEnvironmentsPaginator",
    "ListLineageNodeHistoryPaginator",
    "ListMetadataGenerationRunsPaginator",
    "ListNotificationsPaginator",
    "ListProjectMembershipsPaginator",
    "ListProjectsPaginator",
    "ListSubscriptionGrantsPaginator",
    "ListSubscriptionRequestsPaginator",
    "ListSubscriptionTargetsPaginator",
    "ListSubscriptionsPaginator",
    "ListTimeSeriesDataPointsPaginator",
    "SearchGroupProfilesPaginator",
    "SearchListingsPaginator",
    "SearchPaginator",
    "SearchTypesPaginator",
    "SearchUserProfilesPaginator",
)
