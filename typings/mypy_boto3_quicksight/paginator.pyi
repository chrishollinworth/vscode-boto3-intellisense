"""
Type annotations for quicksight service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_quicksight import QuickSightClient
    from mypy_boto3_quicksight.paginator import (
        DescribeFolderPermissionsPaginator,
        DescribeFolderResolvedPermissionsPaginator,
        ListAnalysesPaginator,
        ListAssetBundleExportJobsPaginator,
        ListAssetBundleImportJobsPaginator,
        ListDashboardVersionsPaginator,
        ListDashboardsPaginator,
        ListDataSetsPaginator,
        ListDataSourcesPaginator,
        ListFolderMembersPaginator,
        ListFoldersPaginator,
        ListGroupMembershipsPaginator,
        ListGroupsPaginator,
        ListIAMPolicyAssignmentsPaginator,
        ListIAMPolicyAssignmentsForUserPaginator,
        ListIngestionsPaginator,
        ListNamespacesPaginator,
        ListRoleMembershipsPaginator,
        ListTemplateAliasesPaginator,
        ListTemplateVersionsPaginator,
        ListTemplatesPaginator,
        ListThemeVersionsPaginator,
        ListThemesPaginator,
        ListUserGroupsPaginator,
        ListUsersPaginator,
        SearchAnalysesPaginator,
        SearchDashboardsPaginator,
        SearchDataSetsPaginator,
        SearchDataSourcesPaginator,
        SearchFoldersPaginator,
        SearchGroupsPaginator,
    )

    client: QuickSightClient = boto3.client("quicksight")

    describe_folder_permissions_paginator: DescribeFolderPermissionsPaginator = client.get_paginator("describe_folder_permissions")
    describe_folder_resolved_permissions_paginator: DescribeFolderResolvedPermissionsPaginator = client.get_paginator("describe_folder_resolved_permissions")
    list_analyses_paginator: ListAnalysesPaginator = client.get_paginator("list_analyses")
    list_asset_bundle_export_jobs_paginator: ListAssetBundleExportJobsPaginator = client.get_paginator("list_asset_bundle_export_jobs")
    list_asset_bundle_import_jobs_paginator: ListAssetBundleImportJobsPaginator = client.get_paginator("list_asset_bundle_import_jobs")
    list_dashboard_versions_paginator: ListDashboardVersionsPaginator = client.get_paginator("list_dashboard_versions")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_folder_members_paginator: ListFolderMembersPaginator = client.get_paginator("list_folder_members")
    list_folders_paginator: ListFoldersPaginator = client.get_paginator("list_folders")
    list_group_memberships_paginator: ListGroupMembershipsPaginator = client.get_paginator("list_group_memberships")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_iam_policy_assignments_paginator: ListIAMPolicyAssignmentsPaginator = client.get_paginator("list_iam_policy_assignments")
    list_iam_policy_assignments_for_user_paginator: ListIAMPolicyAssignmentsForUserPaginator = client.get_paginator("list_iam_policy_assignments_for_user")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_role_memberships_paginator: ListRoleMembershipsPaginator = client.get_paginator("list_role_memberships")
    list_template_aliases_paginator: ListTemplateAliasesPaginator = client.get_paginator("list_template_aliases")
    list_template_versions_paginator: ListTemplateVersionsPaginator = client.get_paginator("list_template_versions")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    list_theme_versions_paginator: ListThemeVersionsPaginator = client.get_paginator("list_theme_versions")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    list_user_groups_paginator: ListUserGroupsPaginator = client.get_paginator("list_user_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    search_analyses_paginator: SearchAnalysesPaginator = client.get_paginator("search_analyses")
    search_dashboards_paginator: SearchDashboardsPaginator = client.get_paginator("search_dashboards")
    search_data_sets_paginator: SearchDataSetsPaginator = client.get_paginator("search_data_sets")
    search_data_sources_paginator: SearchDataSourcesPaginator = client.get_paginator("search_data_sources")
    search_folders_paginator: SearchFoldersPaginator = client.get_paginator("search_folders")
    search_groups_paginator: SearchGroupsPaginator = client.get_paginator("search_groups")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import AssignmentStatusType, RoleType, ThemeTypeType
from .type_defs import (
    AnalysisSearchFilterTypeDef,
    DashboardSearchFilterTypeDef,
    DataSetSearchFilterTypeDef,
    DataSourceSearchFilterTypeDef,
    DescribeFolderPermissionsResponseTypeDef,
    DescribeFolderResolvedPermissionsResponseTypeDef,
    FolderSearchFilterTypeDef,
    GroupSearchFilterTypeDef,
    ListAnalysesResponseTypeDef,
    ListAssetBundleExportJobsResponseTypeDef,
    ListAssetBundleImportJobsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFolderMembersResponseTypeDef,
    ListFoldersResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIAMPolicyAssignmentsForUserResponseTypeDef,
    ListIAMPolicyAssignmentsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListRoleMembershipsResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsResponseTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsResponseTypeDef,
    SearchDataSetsResponseTypeDef,
    SearchDataSourcesResponseTypeDef,
    SearchFoldersResponseTypeDef,
    SearchGroupsResponseTypeDef,
)

__all__ = (
    "DescribeFolderPermissionsPaginator",
    "DescribeFolderResolvedPermissionsPaginator",
    "ListAnalysesPaginator",
    "ListAssetBundleExportJobsPaginator",
    "ListAssetBundleImportJobsPaginator",
    "ListDashboardVersionsPaginator",
    "ListDashboardsPaginator",
    "ListDataSetsPaginator",
    "ListDataSourcesPaginator",
    "ListFolderMembersPaginator",
    "ListFoldersPaginator",
    "ListGroupMembershipsPaginator",
    "ListGroupsPaginator",
    "ListIAMPolicyAssignmentsPaginator",
    "ListIAMPolicyAssignmentsForUserPaginator",
    "ListIngestionsPaginator",
    "ListNamespacesPaginator",
    "ListRoleMembershipsPaginator",
    "ListTemplateAliasesPaginator",
    "ListTemplateVersionsPaginator",
    "ListTemplatesPaginator",
    "ListThemeVersionsPaginator",
    "ListThemesPaginator",
    "ListUserGroupsPaginator",
    "ListUsersPaginator",
    "SearchAnalysesPaginator",
    "SearchDashboardsPaginator",
    "SearchDataSetsPaginator",
    "SearchDataSourcesPaginator",
    "SearchFoldersPaginator",
    "SearchGroupsPaginator",
)

class DescribeFolderPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderpermissionspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFolderPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderpermissionspaginator)
        """

class DescribeFolderResolvedPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderResolvedPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderresolvedpermissionspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFolderResolvedPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderResolvedPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderresolvedpermissionspaginator)
        """

class ListAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
        """

class ListAssetBundleExportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleExportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleexportjobspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetBundleExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleExportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleexportjobspaginator)
        """

class ListAssetBundleImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleimportjobspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetBundleImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleimportjobspaginator)
        """

class ListDashboardVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
        """

class ListDashboardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
        """

class ListDataSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
        """

class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
        """

class ListFolderMembersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListFolderMembers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfoldermemberspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, FolderId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFolderMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListFolderMembers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfoldermemberspaginator)
        """

class ListFoldersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListFolders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfolderspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFoldersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListFolders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfolderspaginator)
        """

class ListGroupMembershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListGroupMemberships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupmembershipspaginator)
    """

    def paginate(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListGroupMemberships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupmembershipspaginator)
        """

class ListGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, Namespace: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupspaginator)
        """

class ListIAMPolicyAssignmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: AssignmentStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIAMPolicyAssignmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentspaginator)
        """

class ListIAMPolicyAssignmentsForUserPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignmentsForUser)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentsforuserpaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIAMPolicyAssignmentsForUserResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignmentsForUser.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentsforuserpaginator)
        """

class ListIngestionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
    """

    def paginate(
        self, *, DataSetId: str, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
        """

class ListNamespacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
        """

class ListRoleMembershipsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListRoleMemberships)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listrolemembershipspaginator)
    """

    def paginate(
        self,
        *,
        Role: RoleType,
        AwsAccountId: str,
        Namespace: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoleMembershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListRoleMemberships.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listrolemembershipspaginator)
        """

class ListTemplateAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
        """

class ListTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
        """

class ListTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
        """

class ListThemeVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, ThemeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
        """

class ListThemesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Type: ThemeTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListThemes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
        """

class ListUserGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListUserGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listusergroupspaginator)
    """

    def paginate(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListUserGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listusergroupspaginator)
        """

class ListUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listuserspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, Namespace: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listuserspaginator)
        """

class SearchAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["AnalysisSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
        """

class SearchDashboardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DashboardSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
        """

class SearchDataSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasetspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSetSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasetspaginator)
        """

class SearchDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasourcespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSourceSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasourcespaginator)
        """

class SearchFoldersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchFolders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchfolderspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["FolderSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchFoldersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchFolders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchfolderspaginator)
        """

class SearchGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchgroupspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        Filters: List["GroupSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/quicksight.html#QuickSight.Paginator.SearchGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchgroupspaginator)
        """
