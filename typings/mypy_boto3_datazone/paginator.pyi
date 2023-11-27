"""
Type annotations for datazone service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_datazone import DataZoneClient
    from mypy_boto3_datazone.paginator import (
        ListAssetRevisionsPaginator,
        ListDataSourceRunActivitiesPaginator,
        ListDataSourceRunsPaginator,
        ListDataSourcesPaginator,
        ListDomainsPaginator,
        ListEnvironmentBlueprintConfigurationsPaginator,
        ListEnvironmentBlueprintsPaginator,
        ListEnvironmentProfilesPaginator,
        ListEnvironmentsPaginator,
        ListNotificationsPaginator,
        ListProjectMembershipsPaginator,
        ListProjectsPaginator,
        ListSubscriptionGrantsPaginator,
        ListSubscriptionRequestsPaginator,
        ListSubscriptionTargetsPaginator,
        ListSubscriptionsPaginator,
        SearchPaginator,
        SearchGroupProfilesPaginator,
        SearchListingsPaginator,
        SearchTypesPaginator,
        SearchUserProfilesPaginator,
    )

    client: DataZoneClient = boto3.client("datazone")

    list_asset_revisions_paginator: ListAssetRevisionsPaginator = client.get_paginator("list_asset_revisions")
    list_data_source_run_activities_paginator: ListDataSourceRunActivitiesPaginator = client.get_paginator("list_data_source_run_activities")
    list_data_source_runs_paginator: ListDataSourceRunsPaginator = client.get_paginator("list_data_source_runs")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_environment_blueprint_configurations_paginator: ListEnvironmentBlueprintConfigurationsPaginator = client.get_paginator("list_environment_blueprint_configurations")
    list_environment_blueprints_paginator: ListEnvironmentBlueprintsPaginator = client.get_paginator("list_environment_blueprints")
    list_environment_profiles_paginator: ListEnvironmentProfilesPaginator = client.get_paginator("list_environment_profiles")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    list_notifications_paginator: ListNotificationsPaginator = client.get_paginator("list_notifications")
    list_project_memberships_paginator: ListProjectMembershipsPaginator = client.get_paginator("list_project_memberships")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_subscription_grants_paginator: ListSubscriptionGrantsPaginator = client.get_paginator("list_subscription_grants")
    list_subscription_requests_paginator: ListSubscriptionRequestsPaginator = client.get_paginator("list_subscription_requests")
    list_subscription_targets_paginator: ListSubscriptionTargetsPaginator = client.get_paginator("list_subscription_targets")
    list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
    search_paginator: SearchPaginator = client.get_paginator("search")
    search_group_profiles_paginator: SearchGroupProfilesPaginator = client.get_paginator("search_group_profiles")
    search_listings_paginator: SearchListingsPaginator = client.get_paginator("search_listings")
    search_types_paginator: SearchTypesPaginator = client.get_paginator("search_types")
    search_user_profiles_paginator: SearchUserProfilesPaginator = client.get_paginator("search_user_profiles")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    DataAssetActivityStatusType,
    DataSourceRunStatusType,
    DataSourceStatusType,
    DomainStatusType,
    EnvironmentStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    NotificationTypeType,
    SortKeyType,
    SortOrderType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TaskStatusType,
    TypesSearchScopeType,
    UserSearchTypeType,
)
from .type_defs import (
    FilterClauseTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    PaginatorConfigTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInItemTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchSortTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListAssetRevisionsPaginator",
    "ListDataSourceRunActivitiesPaginator",
    "ListDataSourceRunsPaginator",
    "ListDataSourcesPaginator",
    "ListDomainsPaginator",
    "ListEnvironmentBlueprintConfigurationsPaginator",
    "ListEnvironmentBlueprintsPaginator",
    "ListEnvironmentProfilesPaginator",
    "ListEnvironmentsPaginator",
    "ListNotificationsPaginator",
    "ListProjectMembershipsPaginator",
    "ListProjectsPaginator",
    "ListSubscriptionGrantsPaginator",
    "ListSubscriptionRequestsPaginator",
    "ListSubscriptionTargetsPaginator",
    "ListSubscriptionsPaginator",
    "SearchPaginator",
    "SearchGroupProfilesPaginator",
    "SearchListingsPaginator",
    "SearchTypesPaginator",
    "SearchUserProfilesPaginator",
)

class ListAssetRevisionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListAssetRevisions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listassetrevisionspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetRevisionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListAssetRevisions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listassetrevisionspaginator)
        """

class ListDataSourceRunActivitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRunActivities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunactivitiespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        status: DataAssetActivityStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourceRunActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRunActivities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunactivitiespaginator)
        """

class ListDataSourceRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunspaginator)
    """

    def paginate(
        self,
        *,
        dataSourceIdentifier: str,
        domainIdentifier: str,
        status: DataSourceRunStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourceRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcerunspaginator)
        """

class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        environmentIdentifier: str = None,
        name: str = None,
        status: DataSourceStatusType = None,
        type: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdatasourcespaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, status: DomainStatusType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listdomainspaginator)
        """

class ListEnvironmentBlueprintConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintconfigurationspaginator)
    """

    def paginate(
        self, *, domainIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentBlueprintConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintconfigurationspaginator)
        """

class ListEnvironmentBlueprintsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        managed: bool = None,
        name: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentBlueprintsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentblueprintspaginator)
        """

class ListEnvironmentProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        environmentBlueprintIdentifier: str = None,
        name: str = None,
        projectIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentprofilespaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        awsAccountId: str = None,
        awsAccountRegion: str = None,
        environmentBlueprintIdentifier: str = None,
        environmentProfileIdentifier: str = None,
        name: str = None,
        provider: str = None,
        status: EnvironmentStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listenvironmentspaginator)
        """

class ListNotificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListNotifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listnotificationspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        type: NotificationTypeType,
        afterTimestamp: Union[datetime, str] = None,
        beforeTimestamp: Union[datetime, str] = None,
        subjects: List[str] = None,
        taskStatus: TaskStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListNotifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listnotificationspaginator)
        """

class ListProjectMembershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListProjectMemberships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectmembershipspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        sortBy: Literal["NAME"] = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectMembershipsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListProjectMemberships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectmembershipspaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str = None,
        name: str = None,
        userIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listprojectspaginator)
        """

class ListSubscriptionGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionGrants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiongrantspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        environmentId: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        subscribedListingId: str = None,
        subscriptionId: str = None,
        subscriptionTargetId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionGrantsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiongrantspaginator)
        """

class ListSubscriptionRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionrequestspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = None,
        owningProjectId: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        status: SubscriptionRequestStatusType = None,
        subscribedListingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionrequestspaginator)
        """

class ListSubscriptionTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiontargetspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionTargetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptiontargetspaginator)
        """

class ListSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = None,
        owningProjectId: str = None,
        sortBy: SortKeyType = None,
        sortOrder: SortOrderType = None,
        status: SubscriptionStatusType = None,
        subscribedListingId: str = None,
        subscriptionRequestIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.ListSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#listsubscriptionspaginator)
        """

class SearchPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.Search)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchpaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        searchScope: InventorySearchScopeType,
        additionalAttributes: List[Literal["FORMS"]] = None,
        filters: "FilterClauseTypeDef" = None,
        owningProjectIdentifier: str = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.Search.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchpaginator)
        """

class SearchGroupProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchGroupProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchgroupprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        groupType: GroupSearchTypeType,
        searchText: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchGroupProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchGroupProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchgroupprofilespaginator)
        """

class SearchListingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchListings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchlistingspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        additionalAttributes: List[Literal["FORMS"]] = None,
        filters: "FilterClauseTypeDef" = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchListingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchListings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchlistingspaginator)
        """

class SearchTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchtypespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        managed: bool,
        searchScope: TypesSearchScopeType,
        filters: "FilterClauseTypeDef" = None,
        searchIn: List["SearchInItemTypeDef"] = None,
        searchText: str = None,
        sort: "SearchSortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchtypespaginator)
        """

class SearchUserProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchUserProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchuserprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        userType: UserSearchTypeType,
        searchText: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchUserProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/datazone.html#DataZone.Paginator.SearchUserProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datazone/paginators.html#searchuserprofilespaginator)
        """
