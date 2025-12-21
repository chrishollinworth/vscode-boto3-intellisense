"""
Main interface for datazone service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datazone import (
        Client,
        DataZoneClient,
        ListAccountPoolsPaginator,
        ListAccountsInAccountPoolPaginator,
        ListAssetFiltersPaginator,
        ListAssetRevisionsPaginator,
        ListConnectionsPaginator,
        ListDataProductRevisionsPaginator,
        ListDataSourceRunActivitiesPaginator,
        ListDataSourceRunsPaginator,
        ListDataSourcesPaginator,
        ListDomainUnitsForParentPaginator,
        ListDomainsPaginator,
        ListEntityOwnersPaginator,
        ListEnvironmentActionsPaginator,
        ListEnvironmentBlueprintConfigurationsPaginator,
        ListEnvironmentBlueprintsPaginator,
        ListEnvironmentProfilesPaginator,
        ListEnvironmentsPaginator,
        ListJobRunsPaginator,
        ListLineageEventsPaginator,
        ListLineageNodeHistoryPaginator,
        ListMetadataGenerationRunsPaginator,
        ListNotificationsPaginator,
        ListPolicyGrantsPaginator,
        ListProjectMembershipsPaginator,
        ListProjectProfilesPaginator,
        ListProjectsPaginator,
        ListRulesPaginator,
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

    session = Session()
    client: DataZoneClient = session.client("datazone")

    list_account_pools_paginator: ListAccountPoolsPaginator = client.get_paginator("list_account_pools")
    list_accounts_in_account_pool_paginator: ListAccountsInAccountPoolPaginator = client.get_paginator("list_accounts_in_account_pool")
    list_asset_filters_paginator: ListAssetFiltersPaginator = client.get_paginator("list_asset_filters")
    list_asset_revisions_paginator: ListAssetRevisionsPaginator = client.get_paginator("list_asset_revisions")
    list_connections_paginator: ListConnectionsPaginator = client.get_paginator("list_connections")
    list_data_product_revisions_paginator: ListDataProductRevisionsPaginator = client.get_paginator("list_data_product_revisions")
    list_data_source_run_activities_paginator: ListDataSourceRunActivitiesPaginator = client.get_paginator("list_data_source_run_activities")
    list_data_source_runs_paginator: ListDataSourceRunsPaginator = client.get_paginator("list_data_source_runs")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_domain_units_for_parent_paginator: ListDomainUnitsForParentPaginator = client.get_paginator("list_domain_units_for_parent")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_entity_owners_paginator: ListEntityOwnersPaginator = client.get_paginator("list_entity_owners")
    list_environment_actions_paginator: ListEnvironmentActionsPaginator = client.get_paginator("list_environment_actions")
    list_environment_blueprint_configurations_paginator: ListEnvironmentBlueprintConfigurationsPaginator = client.get_paginator("list_environment_blueprint_configurations")
    list_environment_blueprints_paginator: ListEnvironmentBlueprintsPaginator = client.get_paginator("list_environment_blueprints")
    list_environment_profiles_paginator: ListEnvironmentProfilesPaginator = client.get_paginator("list_environment_profiles")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_lineage_events_paginator: ListLineageEventsPaginator = client.get_paginator("list_lineage_events")
    list_lineage_node_history_paginator: ListLineageNodeHistoryPaginator = client.get_paginator("list_lineage_node_history")
    list_metadata_generation_runs_paginator: ListMetadataGenerationRunsPaginator = client.get_paginator("list_metadata_generation_runs")
    list_notifications_paginator: ListNotificationsPaginator = client.get_paginator("list_notifications")
    list_policy_grants_paginator: ListPolicyGrantsPaginator = client.get_paginator("list_policy_grants")
    list_project_memberships_paginator: ListProjectMembershipsPaginator = client.get_paginator("list_project_memberships")
    list_project_profiles_paginator: ListProjectProfilesPaginator = client.get_paginator("list_project_profiles")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_subscription_grants_paginator: ListSubscriptionGrantsPaginator = client.get_paginator("list_subscription_grants")
    list_subscription_requests_paginator: ListSubscriptionRequestsPaginator = client.get_paginator("list_subscription_requests")
    list_subscription_targets_paginator: ListSubscriptionTargetsPaginator = client.get_paginator("list_subscription_targets")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    list_time_series_data_points_paginator: ListTimeSeriesDataPointsPaginator = client.get_paginator("list_time_series_data_points")
    search_group_profiles_paginator: SearchGroupProfilesPaginator = client.get_paginator("search_group_profiles")
    search_listings_paginator: SearchListingsPaginator = client.get_paginator("search_listings")
    search_paginator: SearchPaginator = client.get_paginator("search")
    search_types_paginator: SearchTypesPaginator = client.get_paginator("search_types")
    search_user_profiles_paginator: SearchUserProfilesPaginator = client.get_paginator("search_user_profiles")
    ```
"""

from .client import DataZoneClient
from .paginator import (
    ListAccountPoolsPaginator,
    ListAccountsInAccountPoolPaginator,
    ListAssetFiltersPaginator,
    ListAssetRevisionsPaginator,
    ListConnectionsPaginator,
    ListDataProductRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListDomainUnitsForParentPaginator,
    ListEntityOwnersPaginator,
    ListEnvironmentActionsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListJobRunsPaginator,
    ListLineageEventsPaginator,
    ListLineageNodeHistoryPaginator,
    ListMetadataGenerationRunsPaginator,
    ListNotificationsPaginator,
    ListPolicyGrantsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectProfilesPaginator,
    ListProjectsPaginator,
    ListRulesPaginator,
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
    "ListAccountPoolsPaginator",
    "ListAccountsInAccountPoolPaginator",
    "ListAssetFiltersPaginator",
    "ListAssetRevisionsPaginator",
    "ListConnectionsPaginator",
    "ListDataProductRevisionsPaginator",
    "ListDataSourceRunActivitiesPaginator",
    "ListDataSourceRunsPaginator",
    "ListDataSourcesPaginator",
    "ListDomainUnitsForParentPaginator",
    "ListDomainsPaginator",
    "ListEntityOwnersPaginator",
    "ListEnvironmentActionsPaginator",
    "ListEnvironmentBlueprintConfigurationsPaginator",
    "ListEnvironmentBlueprintsPaginator",
    "ListEnvironmentProfilesPaginator",
    "ListEnvironmentsPaginator",
    "ListJobRunsPaginator",
    "ListLineageEventsPaginator",
    "ListLineageNodeHistoryPaginator",
    "ListMetadataGenerationRunsPaginator",
    "ListNotificationsPaginator",
    "ListPolicyGrantsPaginator",
    "ListProjectMembershipsPaginator",
    "ListProjectProfilesPaginator",
    "ListProjectsPaginator",
    "ListRulesPaginator",
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
