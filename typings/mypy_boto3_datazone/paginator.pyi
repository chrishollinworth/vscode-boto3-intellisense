"""
Type annotations for datazone service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_datazone.client import DataZoneClient
    from mypy_boto3_datazone.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssetFiltersInputPaginateTypeDef,
    ListAssetFiltersOutputTypeDef,
    ListAssetRevisionsInputPaginateTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListConnectionsInputPaginateTypeDef,
    ListConnectionsOutputTypeDef,
    ListDataProductRevisionsInputPaginateTypeDef,
    ListDataProductRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesInputPaginateTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsInputPaginateTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesInputPaginateTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsInputPaginateTypeDef,
    ListDomainsOutputTypeDef,
    ListDomainUnitsForParentInputPaginateTypeDef,
    ListDomainUnitsForParentOutputTypeDef,
    ListEntityOwnersInputPaginateTypeDef,
    ListEntityOwnersOutputTypeDef,
    ListEnvironmentActionsInputPaginateTypeDef,
    ListEnvironmentActionsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsInputPaginateTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesInputPaginateTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsInputPaginateTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListJobRunsInputPaginateTypeDef,
    ListJobRunsOutputTypeDef,
    ListLineageEventsInputPaginateTypeDef,
    ListLineageEventsOutputTypeDef,
    ListLineageNodeHistoryInputPaginateTypeDef,
    ListLineageNodeHistoryOutputTypeDef,
    ListMetadataGenerationRunsInputPaginateTypeDef,
    ListMetadataGenerationRunsOutputTypeDef,
    ListNotificationsInputPaginateTypeDef,
    ListNotificationsOutputTypeDef,
    ListPolicyGrantsInputPaginateTypeDef,
    ListPolicyGrantsOutputTypeDef,
    ListProjectMembershipsInputPaginateTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectProfilesInputPaginateTypeDef,
    ListProjectProfilesOutputTypeDef,
    ListProjectsInputPaginateTypeDef,
    ListProjectsOutputTypeDef,
    ListRulesInputPaginateTypeDef,
    ListRulesOutputTypeDef,
    ListSubscriptionGrantsInputPaginateTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsInputPaginateTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsInputPaginateTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsInputPaginateTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    ListTimeSeriesDataPointsInputPaginateTypeDef,
    ListTimeSeriesDataPointsOutputTypeDef,
    SearchGroupProfilesInputPaginateTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInputPaginateTypeDef,
    SearchListingsInputPaginateTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchTypesInputPaginateTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesInputPaginateTypeDef,
    SearchUserProfilesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _ListAssetFiltersPaginatorBase = Paginator[ListAssetFiltersOutputTypeDef]
else:
    _ListAssetFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetFiltersPaginator(_ListAssetFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListAssetFilters.html#DataZone.Paginator.ListAssetFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listassetfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetFiltersInputPaginateTypeDef]
    ) -> PageIterator[ListAssetFiltersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListAssetFilters.html#DataZone.Paginator.ListAssetFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listassetfilterspaginator)
        """

if TYPE_CHECKING:
    _ListAssetRevisionsPaginatorBase = Paginator[ListAssetRevisionsOutputTypeDef]
else:
    _ListAssetRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetRevisionsPaginator(_ListAssetRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListAssetRevisions.html#DataZone.Paginator.ListAssetRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listassetrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetRevisionsInputPaginateTypeDef]
    ) -> PageIterator[ListAssetRevisionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListAssetRevisions.html#DataZone.Paginator.ListAssetRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listassetrevisionspaginator)
        """

if TYPE_CHECKING:
    _ListConnectionsPaginatorBase = Paginator[ListConnectionsOutputTypeDef]
else:
    _ListConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionsPaginator(_ListConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListConnections.html#DataZone.Paginator.ListConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionsInputPaginateTypeDef]
    ) -> PageIterator[ListConnectionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListConnections.html#DataZone.Paginator.ListConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListDataProductRevisionsPaginatorBase = Paginator[ListDataProductRevisionsOutputTypeDef]
else:
    _ListDataProductRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataProductRevisionsPaginator(_ListDataProductRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataProductRevisions.html#DataZone.Paginator.ListDataProductRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdataproductrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataProductRevisionsInputPaginateTypeDef]
    ) -> PageIterator[ListDataProductRevisionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataProductRevisions.html#DataZone.Paginator.ListDataProductRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdataproductrevisionspaginator)
        """

if TYPE_CHECKING:
    _ListDataSourceRunActivitiesPaginatorBase = Paginator[ListDataSourceRunActivitiesOutputTypeDef]
else:
    _ListDataSourceRunActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourceRunActivitiesPaginator(_ListDataSourceRunActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSourceRunActivities.html#DataZone.Paginator.ListDataSourceRunActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcerunactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourceRunActivitiesInputPaginateTypeDef]
    ) -> PageIterator[ListDataSourceRunActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSourceRunActivities.html#DataZone.Paginator.ListDataSourceRunActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcerunactivitiespaginator)
        """

if TYPE_CHECKING:
    _ListDataSourceRunsPaginatorBase = Paginator[ListDataSourceRunsOutputTypeDef]
else:
    _ListDataSourceRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourceRunsPaginator(_ListDataSourceRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSourceRuns.html#DataZone.Paginator.ListDataSourceRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcerunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourceRunsInputPaginateTypeDef]
    ) -> PageIterator[ListDataSourceRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSourceRuns.html#DataZone.Paginator.ListDataSourceRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcerunspaginator)
        """

if TYPE_CHECKING:
    _ListDataSourcesPaginatorBase = Paginator[ListDataSourcesOutputTypeDef]
else:
    _ListDataSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourcesPaginator(_ListDataSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSources.html#DataZone.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourcesInputPaginateTypeDef]
    ) -> PageIterator[ListDataSourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDataSources.html#DataZone.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdatasourcespaginator)
        """

if TYPE_CHECKING:
    _ListDomainUnitsForParentPaginatorBase = Paginator[ListDomainUnitsForParentOutputTypeDef]
else:
    _ListDomainUnitsForParentPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainUnitsForParentPaginator(_ListDomainUnitsForParentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDomainUnitsForParent.html#DataZone.Paginator.ListDomainUnitsForParent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdomainunitsforparentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainUnitsForParentInputPaginateTypeDef]
    ) -> PageIterator[ListDomainUnitsForParentOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDomainUnitsForParent.html#DataZone.Paginator.ListDomainUnitsForParent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdomainunitsforparentpaginator)
        """

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsOutputTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDomains.html#DataZone.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsInputPaginateTypeDef]
    ) -> PageIterator[ListDomainsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListDomains.html#DataZone.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListEntityOwnersPaginatorBase = Paginator[ListEntityOwnersOutputTypeDef]
else:
    _ListEntityOwnersPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntityOwnersPaginator(_ListEntityOwnersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEntityOwners.html#DataZone.Paginator.ListEntityOwners)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listentityownerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntityOwnersInputPaginateTypeDef]
    ) -> PageIterator[ListEntityOwnersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEntityOwners.html#DataZone.Paginator.ListEntityOwners.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listentityownerspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentActionsPaginatorBase = Paginator[ListEnvironmentActionsOutputTypeDef]
else:
    _ListEnvironmentActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentActionsPaginator(_ListEnvironmentActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentActions.html#DataZone.Paginator.ListEnvironmentActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentActionsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentActions.html#DataZone.Paginator.ListEnvironmentActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentactionspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentBlueprintConfigurationsPaginatorBase = Paginator[
        ListEnvironmentBlueprintConfigurationsOutputTypeDef
    ]
else:
    _ListEnvironmentBlueprintConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentBlueprintConfigurationsPaginator(
    _ListEnvironmentBlueprintConfigurationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentBlueprintConfigurations.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentblueprintconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentBlueprintConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentBlueprintConfigurations.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentblueprintconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentBlueprintsPaginatorBase = Paginator[ListEnvironmentBlueprintsOutputTypeDef]
else:
    _ListEnvironmentBlueprintsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentBlueprintsPaginator(_ListEnvironmentBlueprintsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentBlueprints.html#DataZone.Paginator.ListEnvironmentBlueprints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentblueprintspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentBlueprintsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentBlueprintsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentBlueprints.html#DataZone.Paginator.ListEnvironmentBlueprints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentblueprintspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentProfilesPaginatorBase = Paginator[ListEnvironmentProfilesOutputTypeDef]
else:
    _ListEnvironmentProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentProfilesPaginator(_ListEnvironmentProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentProfiles.html#DataZone.Paginator.ListEnvironmentProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentProfilesInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironmentProfiles.html#DataZone.Paginator.ListEnvironmentProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentprofilespaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsOutputTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironments.html#DataZone.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListEnvironments.html#DataZone.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListJobRunsPaginatorBase = Paginator[ListJobRunsOutputTypeDef]
else:
    _ListJobRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobRunsPaginator(_ListJobRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListJobRuns.html#DataZone.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listjobrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobRunsInputPaginateTypeDef]
    ) -> PageIterator[ListJobRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListJobRuns.html#DataZone.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listjobrunspaginator)
        """

if TYPE_CHECKING:
    _ListLineageEventsPaginatorBase = Paginator[ListLineageEventsOutputTypeDef]
else:
    _ListLineageEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLineageEventsPaginator(_ListLineageEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListLineageEvents.html#DataZone.Paginator.ListLineageEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listlineageeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLineageEventsInputPaginateTypeDef]
    ) -> PageIterator[ListLineageEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListLineageEvents.html#DataZone.Paginator.ListLineageEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listlineageeventspaginator)
        """

if TYPE_CHECKING:
    _ListLineageNodeHistoryPaginatorBase = Paginator[ListLineageNodeHistoryOutputTypeDef]
else:
    _ListLineageNodeHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListLineageNodeHistoryPaginator(_ListLineageNodeHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListLineageNodeHistory.html#DataZone.Paginator.ListLineageNodeHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listlineagenodehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLineageNodeHistoryInputPaginateTypeDef]
    ) -> PageIterator[ListLineageNodeHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListLineageNodeHistory.html#DataZone.Paginator.ListLineageNodeHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listlineagenodehistorypaginator)
        """

if TYPE_CHECKING:
    _ListMetadataGenerationRunsPaginatorBase = Paginator[ListMetadataGenerationRunsOutputTypeDef]
else:
    _ListMetadataGenerationRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMetadataGenerationRunsPaginator(_ListMetadataGenerationRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListMetadataGenerationRuns.html#DataZone.Paginator.ListMetadataGenerationRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listmetadatagenerationrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMetadataGenerationRunsInputPaginateTypeDef]
    ) -> PageIterator[ListMetadataGenerationRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListMetadataGenerationRuns.html#DataZone.Paginator.ListMetadataGenerationRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listmetadatagenerationrunspaginator)
        """

if TYPE_CHECKING:
    _ListNotificationsPaginatorBase = Paginator[ListNotificationsOutputTypeDef]
else:
    _ListNotificationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationsPaginator(_ListNotificationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListNotifications.html#DataZone.Paginator.ListNotifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listnotificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationsInputPaginateTypeDef]
    ) -> PageIterator[ListNotificationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListNotifications.html#DataZone.Paginator.ListNotifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listnotificationspaginator)
        """

if TYPE_CHECKING:
    _ListPolicyGrantsPaginatorBase = Paginator[ListPolicyGrantsOutputTypeDef]
else:
    _ListPolicyGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyGrantsPaginator(_ListPolicyGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListPolicyGrants.html#DataZone.Paginator.ListPolicyGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listpolicygrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyGrantsInputPaginateTypeDef]
    ) -> PageIterator[ListPolicyGrantsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListPolicyGrants.html#DataZone.Paginator.ListPolicyGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listpolicygrantspaginator)
        """

if TYPE_CHECKING:
    _ListProjectMembershipsPaginatorBase = Paginator[ListProjectMembershipsOutputTypeDef]
else:
    _ListProjectMembershipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectMembershipsPaginator(_ListProjectMembershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjectMemberships.html#DataZone.Paginator.ListProjectMemberships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectmembershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectMembershipsInputPaginateTypeDef]
    ) -> PageIterator[ListProjectMembershipsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjectMemberships.html#DataZone.Paginator.ListProjectMemberships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectmembershipspaginator)
        """

if TYPE_CHECKING:
    _ListProjectProfilesPaginatorBase = Paginator[ListProjectProfilesOutputTypeDef]
else:
    _ListProjectProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectProfilesPaginator(_ListProjectProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjectProfiles.html#DataZone.Paginator.ListProjectProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectProfilesInputPaginateTypeDef]
    ) -> PageIterator[ListProjectProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjectProfiles.html#DataZone.Paginator.ListProjectProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectprofilespaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsOutputTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjects.html#DataZone.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsInputPaginateTypeDef]
    ) -> PageIterator[ListProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListProjects.html#DataZone.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListRulesPaginatorBase = Paginator[ListRulesOutputTypeDef]
else:
    _ListRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPaginator(_ListRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListRules.html#DataZone.Paginator.ListRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesInputPaginateTypeDef]
    ) -> PageIterator[ListRulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListRules.html#DataZone.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listrulespaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionGrantsPaginatorBase = Paginator[ListSubscriptionGrantsOutputTypeDef]
else:
    _ListSubscriptionGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionGrantsPaginator(_ListSubscriptionGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionGrants.html#DataZone.Paginator.ListSubscriptionGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptiongrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionGrantsInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionGrantsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionGrants.html#DataZone.Paginator.ListSubscriptionGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptiongrantspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionRequestsPaginatorBase = Paginator[ListSubscriptionRequestsOutputTypeDef]
else:
    _ListSubscriptionRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionRequestsPaginator(_ListSubscriptionRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionRequests.html#DataZone.Paginator.ListSubscriptionRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptionrequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionRequestsInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionRequests.html#DataZone.Paginator.ListSubscriptionRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptionrequestspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionTargetsPaginatorBase = Paginator[ListSubscriptionTargetsOutputTypeDef]
else:
    _ListSubscriptionTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionTargetsPaginator(_ListSubscriptionTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionTargets.html#DataZone.Paginator.ListSubscriptionTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptiontargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionTargetsInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionTargetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptionTargets.html#DataZone.Paginator.ListSubscriptionTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptiontargetspaginator)
        """

if TYPE_CHECKING:
    _ListSubscriptionsPaginatorBase = Paginator[ListSubscriptionsOutputTypeDef]
else:
    _ListSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubscriptionsPaginator(_ListSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptions.html#DataZone.Paginator.ListSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubscriptionsInputPaginateTypeDef]
    ) -> PageIterator[ListSubscriptionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListSubscriptions.html#DataZone.Paginator.ListSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListTimeSeriesDataPointsPaginatorBase = Paginator[ListTimeSeriesDataPointsOutputTypeDef]
else:
    _ListTimeSeriesDataPointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTimeSeriesDataPointsPaginator(_ListTimeSeriesDataPointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListTimeSeriesDataPoints.html#DataZone.Paginator.ListTimeSeriesDataPoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listtimeseriesdatapointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTimeSeriesDataPointsInputPaginateTypeDef]
    ) -> PageIterator[ListTimeSeriesDataPointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/ListTimeSeriesDataPoints.html#DataZone.Paginator.ListTimeSeriesDataPoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#listtimeseriesdatapointspaginator)
        """

if TYPE_CHECKING:
    _SearchGroupProfilesPaginatorBase = Paginator[SearchGroupProfilesOutputTypeDef]
else:
    _SearchGroupProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchGroupProfilesPaginator(_SearchGroupProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchGroupProfiles.html#DataZone.Paginator.SearchGroupProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchgroupprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchGroupProfilesInputPaginateTypeDef]
    ) -> PageIterator[SearchGroupProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchGroupProfiles.html#DataZone.Paginator.SearchGroupProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchgroupprofilespaginator)
        """

if TYPE_CHECKING:
    _SearchListingsPaginatorBase = Paginator[SearchListingsOutputTypeDef]
else:
    _SearchListingsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchListingsPaginator(_SearchListingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchListings.html#DataZone.Paginator.SearchListings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchlistingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchListingsInputPaginateTypeDef]
    ) -> PageIterator[SearchListingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchListings.html#DataZone.Paginator.SearchListings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchlistingspaginator)
        """

if TYPE_CHECKING:
    _SearchPaginatorBase = Paginator[SearchOutputTypeDef]
else:
    _SearchPaginatorBase = Paginator  # type: ignore[assignment]

class SearchPaginator(_SearchPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/Search.html#DataZone.Paginator.Search)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchInputPaginateTypeDef]
    ) -> PageIterator[SearchOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/Search.html#DataZone.Paginator.Search.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchpaginator)
        """

if TYPE_CHECKING:
    _SearchTypesPaginatorBase = Paginator[SearchTypesOutputTypeDef]
else:
    _SearchTypesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchTypesPaginator(_SearchTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchTypes.html#DataZone.Paginator.SearchTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchTypesInputPaginateTypeDef]
    ) -> PageIterator[SearchTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchTypes.html#DataZone.Paginator.SearchTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchtypespaginator)
        """

if TYPE_CHECKING:
    _SearchUserProfilesPaginatorBase = Paginator[SearchUserProfilesOutputTypeDef]
else:
    _SearchUserProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchUserProfilesPaginator(_SearchUserProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchUserProfiles.html#DataZone.Paginator.SearchUserProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchuserprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchUserProfilesInputPaginateTypeDef]
    ) -> PageIterator[SearchUserProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone/paginator/SearchUserProfiles.html#DataZone.Paginator.SearchUserProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators/#searchuserprofilespaginator)
        """
