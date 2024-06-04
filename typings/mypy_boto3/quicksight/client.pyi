"""
Type annotations for quicksight service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_quicksight import QuickSightClient

    client: QuickSightClient = boto3.client("quicksight")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AssetBundleExportFormatType,
    AssetBundleImportFailureActionType,
    AssignmentStatusType,
    AuthenticationMethodOptionType,
    DataSetImportModeType,
    DataSourceTypeType,
    EditionType,
    EmbeddingIdentityTypeType,
    FolderTypeType,
    IdentityTypeType,
    IngestionTypeType,
    MemberTypeType,
    PurchaseModeType,
    RoleType,
    SharingModelType,
    ThemeTypeType,
    UserRoleType,
)
from .paginator import (
    DescribeFolderPermissionsPaginator,
    DescribeFolderResolvedPermissionsPaginator,
    ListAnalysesPaginator,
    ListAssetBundleExportJobsPaginator,
    ListAssetBundleImportJobsPaginator,
    ListDashboardsPaginator,
    ListDashboardVersionsPaginator,
    ListDataSetsPaginator,
    ListDataSourcesPaginator,
    ListFolderMembersPaginator,
    ListFoldersPaginator,
    ListGroupMembershipsPaginator,
    ListGroupsPaginator,
    ListIAMPolicyAssignmentsForUserPaginator,
    ListIAMPolicyAssignmentsPaginator,
    ListIngestionsPaginator,
    ListNamespacesPaginator,
    ListRoleMembershipsPaginator,
    ListTemplateAliasesPaginator,
    ListTemplatesPaginator,
    ListTemplateVersionsPaginator,
    ListThemesPaginator,
    ListThemeVersionsPaginator,
    ListUserGroupsPaginator,
    ListUsersPaginator,
    SearchAnalysesPaginator,
    SearchDashboardsPaginator,
    SearchDataSetsPaginator,
    SearchDataSourcesPaginator,
    SearchFoldersPaginator,
    SearchGroupsPaginator,
)
from .type_defs import (
    AccountCustomizationTypeDef,
    AnalysisDefinitionTypeDef,
    AnalysisSearchFilterTypeDef,
    AnalysisSourceEntityTypeDef,
    AnonymousUserEmbeddingExperienceConfigurationTypeDef,
    AssetBundleCloudFormationOverridePropertyConfigurationTypeDef,
    AssetBundleExportJobValidationStrategyTypeDef,
    AssetBundleImportJobOverrideParametersTypeDef,
    AssetBundleImportJobOverridePermissionsTypeDef,
    AssetBundleImportJobOverrideTagsTypeDef,
    AssetBundleImportJobOverrideValidationStrategyTypeDef,
    AssetBundleImportSourceTypeDef,
    CancelIngestionResponseTypeDef,
    ColumnGroupTypeDef,
    ColumnLevelPermissionRuleTypeDef,
    CreateAccountCustomizationResponseTypeDef,
    CreateAccountSubscriptionResponseTypeDef,
    CreateAnalysisResponseTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDataSetResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFolderMembershipResponseTypeDef,
    CreateFolderResponseTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateIAMPolicyAssignmentResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateRefreshScheduleResponseTypeDef,
    CreateRoleMembershipResponseTypeDef,
    CreateTemplateAliasResponseTypeDef,
    CreateTemplateResponseTypeDef,
    CreateThemeAliasResponseTypeDef,
    CreateThemeResponseTypeDef,
    CreateTopicRefreshScheduleResponseTypeDef,
    CreateTopicResponseTypeDef,
    CreateVPCConnectionResponseTypeDef,
    DashboardPublishOptionsTypeDef,
    DashboardSearchFilterTypeDef,
    DashboardSourceEntityTypeDef,
    DashboardVersionDefinitionTypeDef,
    DatasetParameterTypeDef,
    DataSetRefreshPropertiesTypeDef,
    DataSetSearchFilterTypeDef,
    DataSetUsageConfigurationTypeDef,
    DataSourceCredentialsTypeDef,
    DataSourceParametersTypeDef,
    DataSourceSearchFilterTypeDef,
    DeleteAccountCustomizationResponseTypeDef,
    DeleteAccountSubscriptionResponseTypeDef,
    DeleteAnalysisResponseTypeDef,
    DeleteDashboardResponseTypeDef,
    DeleteDataSetRefreshPropertiesResponseTypeDef,
    DeleteDataSetResponseTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteFolderMembershipResponseTypeDef,
    DeleteFolderResponseTypeDef,
    DeleteGroupMembershipResponseTypeDef,
    DeleteGroupResponseTypeDef,
    DeleteIAMPolicyAssignmentResponseTypeDef,
    DeleteIdentityPropagationConfigResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteRefreshScheduleResponseTypeDef,
    DeleteRoleCustomPermissionResponseTypeDef,
    DeleteRoleMembershipResponseTypeDef,
    DeleteTemplateAliasResponseTypeDef,
    DeleteTemplateResponseTypeDef,
    DeleteThemeAliasResponseTypeDef,
    DeleteThemeResponseTypeDef,
    DeleteTopicRefreshScheduleResponseTypeDef,
    DeleteTopicResponseTypeDef,
    DeleteUserByPrincipalIdResponseTypeDef,
    DeleteUserResponseTypeDef,
    DeleteVPCConnectionResponseTypeDef,
    DescribeAccountCustomizationResponseTypeDef,
    DescribeAccountSettingsResponseTypeDef,
    DescribeAccountSubscriptionResponseTypeDef,
    DescribeAnalysisDefinitionResponseTypeDef,
    DescribeAnalysisPermissionsResponseTypeDef,
    DescribeAnalysisResponseTypeDef,
    DescribeAssetBundleExportJobResponseTypeDef,
    DescribeAssetBundleImportJobResponseTypeDef,
    DescribeDashboardDefinitionResponseTypeDef,
    DescribeDashboardPermissionsResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDashboardSnapshotJobResponseTypeDef,
    DescribeDashboardSnapshotJobResultResponseTypeDef,
    DescribeDataSetPermissionsResponseTypeDef,
    DescribeDataSetRefreshPropertiesResponseTypeDef,
    DescribeDataSetResponseTypeDef,
    DescribeDataSourcePermissionsResponseTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeFolderPermissionsResponseTypeDef,
    DescribeFolderResolvedPermissionsResponseTypeDef,
    DescribeFolderResponseTypeDef,
    DescribeGroupMembershipResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeIAMPolicyAssignmentResponseTypeDef,
    DescribeIngestionResponseTypeDef,
    DescribeIpRestrictionResponseTypeDef,
    DescribeKeyRegistrationResponseTypeDef,
    DescribeNamespaceResponseTypeDef,
    DescribeRefreshScheduleResponseTypeDef,
    DescribeRoleCustomPermissionResponseTypeDef,
    DescribeTemplateAliasResponseTypeDef,
    DescribeTemplateDefinitionResponseTypeDef,
    DescribeTemplatePermissionsResponseTypeDef,
    DescribeTemplateResponseTypeDef,
    DescribeThemeAliasResponseTypeDef,
    DescribeThemePermissionsResponseTypeDef,
    DescribeThemeResponseTypeDef,
    DescribeTopicPermissionsResponseTypeDef,
    DescribeTopicRefreshResponseTypeDef,
    DescribeTopicRefreshScheduleResponseTypeDef,
    DescribeTopicResponseTypeDef,
    DescribeUserResponseTypeDef,
    DescribeVPCConnectionResponseTypeDef,
    FieldFolderTypeDef,
    FolderSearchFilterTypeDef,
    GenerateEmbedUrlForAnonymousUserResponseTypeDef,
    GenerateEmbedUrlForRegisteredUserResponseTypeDef,
    GetDashboardEmbedUrlResponseTypeDef,
    GetSessionEmbedUrlResponseTypeDef,
    GroupSearchFilterTypeDef,
    LinkSharingConfigurationTypeDef,
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
    ListIdentityPropagationConfigsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListRefreshSchedulesResponseTypeDef,
    ListRoleMembershipsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemeAliasesResponseTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsResponseTypeDef,
    ListTopicRefreshSchedulesResponseTypeDef,
    ListTopicsResponseTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVPCConnectionsResponseTypeDef,
    LogicalTableTypeDef,
    ParametersTypeDef,
    PhysicalTableTypeDef,
    PutDataSetRefreshPropertiesResponseTypeDef,
    RefreshScheduleTypeDef,
    RegisteredCustomerManagedKeyTypeDef,
    RegisteredUserEmbeddingExperienceConfigurationTypeDef,
    RegisterUserResponseTypeDef,
    ResourcePermissionTypeDef,
    RestoreAnalysisResponseTypeDef,
    RowLevelPermissionDataSetTypeDef,
    RowLevelPermissionTagConfigurationTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsResponseTypeDef,
    SearchDataSetsResponseTypeDef,
    SearchDataSourcesResponseTypeDef,
    SearchFoldersResponseTypeDef,
    SearchGroupsResponseTypeDef,
    SessionTagTypeDef,
    SnapshotConfigurationTypeDef,
    SnapshotUserConfigurationTypeDef,
    SslPropertiesTypeDef,
    StartAssetBundleExportJobResponseTypeDef,
    StartAssetBundleImportJobResponseTypeDef,
    StartDashboardSnapshotJobResponseTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    TemplateSourceEntityTypeDef,
    TemplateVersionDefinitionTypeDef,
    ThemeConfigurationTypeDef,
    TopicDetailsTypeDef,
    TopicRefreshScheduleTypeDef,
    UntagResourceResponseTypeDef,
    UpdateAccountCustomizationResponseTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateAnalysisPermissionsResponseTypeDef,
    UpdateAnalysisResponseTypeDef,
    UpdateDashboardLinksResponseTypeDef,
    UpdateDashboardPermissionsResponseTypeDef,
    UpdateDashboardPublishedVersionResponseTypeDef,
    UpdateDashboardResponseTypeDef,
    UpdateDataSetPermissionsResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateDataSourcePermissionsResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFolderPermissionsResponseTypeDef,
    UpdateFolderResponseTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIAMPolicyAssignmentResponseTypeDef,
    UpdateIdentityPropagationConfigResponseTypeDef,
    UpdateIpRestrictionResponseTypeDef,
    UpdateKeyRegistrationResponseTypeDef,
    UpdatePublicSharingSettingsResponseTypeDef,
    UpdateRefreshScheduleResponseTypeDef,
    UpdateRoleCustomPermissionResponseTypeDef,
    UpdateSPICECapacityConfigurationResponseTypeDef,
    UpdateTemplateAliasResponseTypeDef,
    UpdateTemplatePermissionsResponseTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateThemeAliasResponseTypeDef,
    UpdateThemePermissionsResponseTypeDef,
    UpdateThemeResponseTypeDef,
    UpdateTopicPermissionsResponseTypeDef,
    UpdateTopicRefreshScheduleResponseTypeDef,
    UpdateTopicResponseTypeDef,
    UpdateUserResponseTypeDef,
    UpdateVPCConnectionResponseTypeDef,
    ValidationStrategyTypeDef,
    VpcConnectionPropertiesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("QuickSightClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdatingException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DomainNotWhitelistedException: Type[BotocoreClientError]
    IdentityTypeNotSupportedException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    QuickSightUserNotFoundException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    SessionLifetimeInMinutesInvalidException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedPricingPlanException: Type[BotocoreClientError]
    UnsupportedUserEditionException: Type[BotocoreClientError]

class QuickSightClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QuickSightClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#can_paginate)
        """

    def cancel_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> CancelIngestionResponseTypeDef:
        """
        Cancels an ongoing ingestion of data into SPICE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#cancel_ingestion)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#close)
        """

    def create_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccountCustomizationResponseTypeDef:
        """
        Creates Amazon QuickSight customizations for the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_account_customization)
        """

    def create_account_subscription(
        self,
        *,
        AuthenticationMethod: AuthenticationMethodOptionType,
        AwsAccountId: str,
        AccountName: str,
        NotificationEmail: str,
        Edition: EditionType = None,
        ActiveDirectoryName: str = None,
        Realm: str = None,
        DirectoryId: str = None,
        AdminGroup: List[str] = None,
        AuthorGroup: List[str] = None,
        ReaderGroup: List[str] = None,
        AdminProGroup: List[str] = None,
        AuthorProGroup: List[str] = None,
        ReaderProGroup: List[str] = None,
        FirstName: str = None,
        LastName: str = None,
        EmailAddress: str = None,
        ContactNumber: str = None,
        IAMIdentityCenterInstanceArn: str = None
    ) -> CreateAccountSubscriptionResponseTypeDef:
        """
        Creates an Amazon QuickSight account, or subscribes to Amazon QuickSight Q.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_account_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_account_subscription)
        """

    def create_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        Parameters: "ParametersTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        SourceEntity: "AnalysisSourceEntityTypeDef" = None,
        ThemeArn: str = None,
        Tags: List["TagTypeDef"] = None,
        Definition: "AnalysisDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None,
        FolderArns: List[str] = None
    ) -> CreateAnalysisResponseTypeDef:
        """
        Creates an analysis in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_analysis)
        """

    def create_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        Parameters: "ParametersTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        SourceEntity: "DashboardSourceEntityTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: "DashboardPublishOptionsTypeDef" = None,
        ThemeArn: str = None,
        Definition: "DashboardVersionDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None,
        FolderArns: List[str] = None,
        LinkSharingConfiguration: "LinkSharingConfigurationTypeDef" = None,
        LinkEntities: List[str] = None
    ) -> CreateDashboardResponseTypeDef:
        """
        Creates a dashboard from either a template or directly with a
        `DashboardDefinition`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_dashboard)
        """

    def create_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: DataSetImportModeType,
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        RowLevelPermissionTagConfiguration: "RowLevelPermissionTagConfigurationTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        DataSetUsageConfiguration: "DataSetUsageConfigurationTypeDef" = None,
        DatasetParameters: List["DatasetParameterTypeDef"] = None,
        FolderArns: List[str] = None
    ) -> CreateDataSetResponseTypeDef:
        """
        Creates a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_data_set)
        """

    def create_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: DataSourceTypeType,
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: "DataSourceCredentialsTypeDef" = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        FolderArns: List[str] = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_data_source)
        """

    def create_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Name: str = None,
        FolderType: FolderTypeType = None,
        ParentFolderArn: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        SharingModel: SharingModelType = None
    ) -> CreateFolderResponseTypeDef:
        """
        Creates an empty shared folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder)
        """

    def create_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> CreateFolderMembershipResponseTypeDef:
        """
        Adds an asset, such as a dashboard, analysis, or dataset into a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_folder_membership)
        """

    def create_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> CreateGroupResponseTypeDef:
        """
        Use the `CreateGroup` operation to create a group in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_group)
        """

    def create_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        Adds an Amazon QuickSight user to an Amazon QuickSight group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_group_membership)
        """

    def create_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: AssignmentStatusType,
        Namespace: str,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None
    ) -> CreateIAMPolicyAssignmentResponseTypeDef:
        """
        Creates an assignment with one specified IAM policy, identified by its Amazon
        Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_iam_policy_assignment)
        """

    def create_ingestion(
        self,
        *,
        DataSetId: str,
        IngestionId: str,
        AwsAccountId: str,
        IngestionType: IngestionTypeType = None
    ) -> CreateIngestionResponseTypeDef:
        """
        Creates and starts a new SPICE ingestion for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_ingestion)
        """

    def create_namespace(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        IdentityStore: Literal["QUICKSIGHT"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateNamespaceResponseTypeDef:
        """
        (Enterprise edition only) Creates a new namespace for you to use with Amazon
        QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_namespace)
        """

    def create_refresh_schedule(
        self, *, DataSetId: str, AwsAccountId: str, Schedule: "RefreshScheduleTypeDef"
    ) -> CreateRefreshScheduleResponseTypeDef:
        """
        Creates a refresh schedule for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_refresh_schedule)
        """

    def create_role_membership(
        self, *, MemberName: str, AwsAccountId: str, Namespace: str, Role: RoleType
    ) -> CreateRoleMembershipResponseTypeDef:
        """
        Use `CreateRoleMembership` to add an existing Amazon QuickSight group to an
        existing role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_role_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_role_membership)
        """

    def create_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        Name: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        SourceEntity: "TemplateSourceEntityTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
        Definition: "TemplateVersionDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a template either from a `TemplateDefinition` or from an existing Amazon
        QuickSight analysis or template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_template)
        """

    def create_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> CreateTemplateAliasResponseTypeDef:
        """
        Creates a template alias for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_template_alias)
        """

    def create_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        Name: str,
        BaseThemeId: str,
        Configuration: "ThemeConfigurationTypeDef",
        VersionDescription: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateThemeResponseTypeDef:
        """
        Creates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme)
        """

    def create_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> CreateThemeAliasResponseTypeDef:
        """
        Creates a theme alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_theme_alias)
        """

    def create_topic(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Topic: "TopicDetailsTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateTopicResponseTypeDef:
        """
        Creates a new Q topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_topic)
        """

    def create_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetArn: str,
        RefreshSchedule: "TopicRefreshScheduleTypeDef",
        DatasetName: str = None
    ) -> CreateTopicRefreshScheduleResponseTypeDef:
        """
        Creates a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_topic_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_topic_refresh_schedule)
        """

    def create_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
        Name: str,
        SubnetIds: List[str],
        SecurityGroupIds: List[str],
        RoleArn: str,
        DnsResolvers: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateVPCConnectionResponseTypeDef:
        """
        Creates a new VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.create_vpc_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#create_vpc_connection)
        """

    def delete_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None
    ) -> DeleteAccountCustomizationResponseTypeDef:
        """
        Deletes all Amazon QuickSight customizations in this Amazon Web Services Region
        for the specified Amazon Web Services account and Amazon QuickSight namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_account_customization)
        """

    def delete_account_subscription(
        self, *, AwsAccountId: str
    ) -> DeleteAccountSubscriptionResponseTypeDef:
        """
        Use the `DeleteAccountSubscription` operation to delete an Amazon QuickSight
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_account_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_account_subscription)
        """

    def delete_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None
    ) -> DeleteAnalysisResponseTypeDef:
        """
        Deletes an analysis from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_analysis)
        """

    def delete_dashboard(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> DeleteDashboardResponseTypeDef:
        """
        Deletes a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_dashboard)
        """

    def delete_data_set(self, *, AwsAccountId: str, DataSetId: str) -> DeleteDataSetResponseTypeDef:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_set)
        """

    def delete_data_set_refresh_properties(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DeleteDataSetRefreshPropertiesResponseTypeDef:
        """
        Deletes the dataset refresh properties of the dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_data_set_refresh_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_set_refresh_properties)
        """

    def delete_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DeleteDataSourceResponseTypeDef:
        """
        Deletes the data source permanently.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_data_source)
        """

    def delete_folder(self, *, AwsAccountId: str, FolderId: str) -> DeleteFolderResponseTypeDef:
        """
        Deletes an empty folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder)
        """

    def delete_folder_membership(
        self, *, AwsAccountId: str, FolderId: str, MemberId: str, MemberType: MemberTypeType
    ) -> DeleteFolderMembershipResponseTypeDef:
        """
        Removes an asset, such as a dashboard, analysis, or dataset, from a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_folder_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_folder_membership)
        """

    def delete_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupResponseTypeDef:
        """
        Removes a user group from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group)
        """

    def delete_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupMembershipResponseTypeDef:
        """
        Removes a user from a group so that the user is no longer a member of the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DeleteIAMPolicyAssignmentResponseTypeDef:
        """
        Deletes an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_iam_policy_assignment)
        """

    def delete_identity_propagation_config(
        self, *, AwsAccountId: str, Service: Literal["REDSHIFT"]
    ) -> DeleteIdentityPropagationConfigResponseTypeDef:
        """
        Deletes all access scopes and authorized targets that are associated with a
        service from the Amazon QuickSight IAM Identity Center application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_identity_propagation_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_identity_propagation_config)
        """

    def delete_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DeleteNamespaceResponseTypeDef:
        """
        Deletes a namespace and the users and groups that are associated with the
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_namespace)
        """

    def delete_refresh_schedule(
        self, *, DataSetId: str, AwsAccountId: str, ScheduleId: str
    ) -> DeleteRefreshScheduleResponseTypeDef:
        """
        Deletes a refresh schedule from a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_refresh_schedule)
        """

    def delete_role_custom_permission(
        self, *, Role: RoleType, AwsAccountId: str, Namespace: str
    ) -> DeleteRoleCustomPermissionResponseTypeDef:
        """
        Removes custom permissions from the role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_role_custom_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_role_custom_permission)
        """

    def delete_role_membership(
        self, *, MemberName: str, Role: RoleType, AwsAccountId: str, Namespace: str
    ) -> DeleteRoleMembershipResponseTypeDef:
        """
        Removes a group from a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_role_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_role_membership)
        """

    def delete_template(
        self, *, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> DeleteTemplateResponseTypeDef:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template)
        """

    def delete_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DeleteTemplateAliasResponseTypeDef:
        """
        Deletes the item that the specified template alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_template_alias)
        """

    def delete_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None
    ) -> DeleteThemeResponseTypeDef:
        """
        Deletes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme)
        """

    def delete_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DeleteThemeAliasResponseTypeDef:
        """
        Deletes the version of the theme that the specified theme alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_theme_alias)
        """

    def delete_topic(self, *, AwsAccountId: str, TopicId: str) -> DeleteTopicResponseTypeDef:
        """
        Deletes a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_topic)
        """

    def delete_topic_refresh_schedule(
        self, *, AwsAccountId: str, TopicId: str, DatasetId: str
    ) -> DeleteTopicRefreshScheduleResponseTypeDef:
        """
        Deletes a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_topic_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_topic_refresh_schedule)
        """

    def delete_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserResponseTypeDef:
        """
        Deletes the Amazon QuickSight user that is associated with the identity of the
        IAM user or role that's making the call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user)
        """

    def delete_user_by_principal_id(
        self, *, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserByPrincipalIdResponseTypeDef:
        """
        Deletes a user identified by its principal ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_user_by_principal_id)
        """

    def delete_vpc_connection(
        self, *, AwsAccountId: str, VPCConnectionId: str
    ) -> DeleteVPCConnectionResponseTypeDef:
        """
        Deletes a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.delete_vpc_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#delete_vpc_connection)
        """

    def describe_account_customization(
        self, *, AwsAccountId: str, Namespace: str = None, Resolved: bool = None
    ) -> DescribeAccountCustomizationResponseTypeDef:
        """
        Describes the customizations associated with the provided Amazon Web Services
        account and Amazon Amazon QuickSight namespace in an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_customization)
        """

    def describe_account_settings(
        self, *, AwsAccountId: str
    ) -> DescribeAccountSettingsResponseTypeDef:
        """
        Describes the settings that were used when your Amazon QuickSight subscription
        was first created in this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_settings)
        """

    def describe_account_subscription(
        self, *, AwsAccountId: str
    ) -> DescribeAccountSubscriptionResponseTypeDef:
        """
        Use the DescribeAccountSubscription operation to receive a description of an
        Amazon QuickSight account's subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_account_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_account_subscription)
        """

    def describe_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisResponseTypeDef:
        """
        Provides a summary of the metadata for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis)
        """

    def describe_analysis_definition(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_analysis_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis_definition)
        """

    def describe_analysis_permissions(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisPermissionsResponseTypeDef:
        """
        Provides the read and write permissions for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_analysis_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_analysis_permissions)
        """

    def describe_asset_bundle_export_job(
        self, *, AwsAccountId: str, AssetBundleExportJobId: str
    ) -> DescribeAssetBundleExportJobResponseTypeDef:
        """
        Describes an existing export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_asset_bundle_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_asset_bundle_export_job)
        """

    def describe_asset_bundle_import_job(
        self, *, AwsAccountId: str, AssetBundleImportJobId: str
    ) -> DescribeAssetBundleImportJobResponseTypeDef:
        """
        Describes an existing import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_asset_bundle_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_asset_bundle_import_job)
        """

    def describe_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeDashboardResponseTypeDef:
        """
        Provides a summary for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard)
        """

    def describe_dashboard_definition(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeDashboardDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_definition)
        """

    def describe_dashboard_permissions(
        self, *, AwsAccountId: str, DashboardId: str
    ) -> DescribeDashboardPermissionsResponseTypeDef:
        """
        Describes read and write permissions for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_permissions)
        """

    def describe_dashboard_snapshot_job(
        self, *, AwsAccountId: str, DashboardId: str, SnapshotJobId: str
    ) -> DescribeDashboardSnapshotJobResponseTypeDef:
        """
        Describes an existing snapshot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_snapshot_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_snapshot_job)
        """

    def describe_dashboard_snapshot_job_result(
        self, *, AwsAccountId: str, DashboardId: str, SnapshotJobId: str
    ) -> DescribeDashboardSnapshotJobResultResponseTypeDef:
        """
        Describes the result of an existing snapshot job that has finished running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_snapshot_job_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_dashboard_snapshot_job_result)
        """

    def describe_data_set(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetResponseTypeDef:
        """
        Describes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set)
        """

    def describe_data_set_permissions(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetPermissionsResponseTypeDef:
        """
        Describes the permissions on a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set_permissions)
        """

    def describe_data_set_refresh_properties(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetRefreshPropertiesResponseTypeDef:
        """
        Describes the refresh properties of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_data_set_refresh_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_set_refresh_properties)
        """

    def describe_data_source(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourceResponseTypeDef:
        """
        Describes a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source)
        """

    def describe_data_source_permissions(
        self, *, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourcePermissionsResponseTypeDef:
        """
        Describes the resource permissions for a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_data_source_permissions)
        """

    def describe_folder(self, *, AwsAccountId: str, FolderId: str) -> DescribeFolderResponseTypeDef:
        """
        Describes a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder)
        """

    def describe_folder_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFolderPermissionsResponseTypeDef:
        """
        Describes permissions for a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_permissions)
        """

    def describe_folder_resolved_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFolderResolvedPermissionsResponseTypeDef:
        """
        Describes the folder resolved permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_folder_resolved_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_folder_resolved_permissions)
        """

    def describe_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupResponseTypeDef:
        """
        Returns an Amazon QuickSight group's description and Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_group)
        """

    def describe_group_membership(
        self, *, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupMembershipResponseTypeDef:
        """
        Use the `DescribeGroupMembership` operation to determine if a user is a member
        of the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_group_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_group_membership)
        """

    def describe_iam_policy_assignment(
        self, *, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DescribeIAMPolicyAssignmentResponseTypeDef:
        """
        Describes an existing IAM policy assignment, as specified by the assignment
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, *, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> DescribeIngestionResponseTypeDef:
        """
        Describes a SPICE ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_ingestion)
        """

    def describe_ip_restriction(self, *, AwsAccountId: str) -> DescribeIpRestrictionResponseTypeDef:
        """
        Provides a summary and status of IP rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_ip_restriction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_ip_restriction)
        """

    def describe_key_registration(
        self, *, AwsAccountId: str, DefaultKeyOnly: bool = None
    ) -> DescribeKeyRegistrationResponseTypeDef:
        """
        Describes all customer managed key registrations in a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_key_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_key_registration)
        """

    def describe_namespace(
        self, *, AwsAccountId: str, Namespace: str
    ) -> DescribeNamespaceResponseTypeDef:
        """
        Describes the current namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_namespace)
        """

    def describe_refresh_schedule(
        self, *, AwsAccountId: str, DataSetId: str, ScheduleId: str
    ) -> DescribeRefreshScheduleResponseTypeDef:
        """
        Provides a summary of a refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_refresh_schedule)
        """

    def describe_role_custom_permission(
        self, *, Role: RoleType, AwsAccountId: str, Namespace: str
    ) -> DescribeRoleCustomPermissionResponseTypeDef:
        """
        Describes all custom permissions that are mapped to a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_role_custom_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_role_custom_permission)
        """

    def describe_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeTemplateResponseTypeDef:
        """
        Describes a template's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template)
        """

    def describe_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DescribeTemplateAliasResponseTypeDef:
        """
        Describes the template alias for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_alias)
        """

    def describe_template_definition(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int = None,
        AliasName: str = None
    ) -> DescribeTemplateDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_template_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_definition)
        """

    def describe_template_permissions(
        self, *, AwsAccountId: str, TemplateId: str
    ) -> DescribeTemplatePermissionsResponseTypeDef:
        """
        Describes read and write permissions on a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_template_permissions)
        """

    def describe_theme(
        self, *, AwsAccountId: str, ThemeId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeThemeResponseTypeDef:
        """
        Describes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme)
        """

    def describe_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DescribeThemeAliasResponseTypeDef:
        """
        Describes the alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_alias)
        """

    def describe_theme_permissions(
        self, *, AwsAccountId: str, ThemeId: str
    ) -> DescribeThemePermissionsResponseTypeDef:
        """
        Describes the read and write permissions for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_theme_permissions)
        """

    def describe_topic(self, *, AwsAccountId: str, TopicId: str) -> DescribeTopicResponseTypeDef:
        """
        Describes a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_topic)
        """

    def describe_topic_permissions(
        self, *, AwsAccountId: str, TopicId: str
    ) -> DescribeTopicPermissionsResponseTypeDef:
        """
        Describes the permissions of a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_topic_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_topic_permissions)
        """

    def describe_topic_refresh(
        self, *, AwsAccountId: str, TopicId: str, RefreshId: str
    ) -> DescribeTopicRefreshResponseTypeDef:
        """
        Describes the status of a topic refresh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_topic_refresh)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_topic_refresh)
        """

    def describe_topic_refresh_schedule(
        self, *, AwsAccountId: str, TopicId: str, DatasetId: str
    ) -> DescribeTopicRefreshScheduleResponseTypeDef:
        """
        Deletes a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_topic_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_topic_refresh_schedule)
        """

    def describe_user(
        self, *, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeUserResponseTypeDef:
        """
        Returns information about a user, given the user name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_user)
        """

    def describe_vpc_connection(
        self, *, AwsAccountId: str, VPCConnectionId: str
    ) -> DescribeVPCConnectionResponseTypeDef:
        """
        Describes a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.describe_vpc_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#describe_vpc_connection)
        """

    def generate_embed_url_for_anonymous_user(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AuthorizedResourceArns: List[str],
        ExperienceConfiguration: "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
        SessionLifetimeInMinutes: int = None,
        SessionTags: List["SessionTagTypeDef"] = None,
        AllowedDomains: List[str] = None
    ) -> GenerateEmbedUrlForAnonymousUserResponseTypeDef:
        """
        Generates an embed URL that you can use to embed an Amazon QuickSight dashboard
        or visual in your website, without having to register any reader users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.generate_embed_url_for_anonymous_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#generate_embed_url_for_anonymous_user)
        """

    def generate_embed_url_for_registered_user(
        self,
        *,
        AwsAccountId: str,
        UserArn: str,
        ExperienceConfiguration: "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
        SessionLifetimeInMinutes: int = None,
        AllowedDomains: List[str] = None
    ) -> GenerateEmbedUrlForRegisteredUserResponseTypeDef:
        """
        Generates an embed URL that you can use to embed an Amazon QuickSight experience
        in your website.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.generate_embed_url_for_registered_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#generate_embed_url_for_registered_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#generate_presigned_url)
        """

    def get_dashboard_embed_url(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: EmbeddingIdentityTypeType,
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        StatePersistenceEnabled: bool = None,
        UserArn: str = None,
        Namespace: str = None,
        AdditionalDashboardIds: List[str] = None
    ) -> GetDashboardEmbedUrlResponseTypeDef:
        """
        Generates a temporary session URL and authorization code(bearer token) that you
        can use to embed an Amazon QuickSight read-only dashboard in your website or
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#get_dashboard_embed_url)
        """

    def get_session_embed_url(
        self,
        *,
        AwsAccountId: str,
        EntryPoint: str = None,
        SessionLifetimeInMinutes: int = None,
        UserArn: str = None
    ) -> GetSessionEmbedUrlResponseTypeDef:
        """
        Generates a session URL and authorization code that you can use to embed the
        Amazon Amazon QuickSight console in your web server code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#get_session_embed_url)
        """

    def list_analyses(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAnalysesResponseTypeDef:
        """
        Lists Amazon QuickSight analyses that exist in the specified Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_analyses)
        """

    def list_asset_bundle_export_jobs(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAssetBundleExportJobsResponseTypeDef:
        """
        Lists all asset bundle export jobs that have been taken place in the last 14
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_asset_bundle_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_asset_bundle_export_jobs)
        """

    def list_asset_bundle_import_jobs(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAssetBundleImportJobsResponseTypeDef:
        """
        Lists all asset bundle import jobs that have taken place in the last 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_asset_bundle_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_asset_bundle_import_jobs)
        """

    def list_dashboard_versions(
        self, *, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardVersionsResponseTypeDef:
        """
        Lists all the versions of the dashboards in the Amazon QuickSight subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboard_versions)
        """

    def list_dashboards(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        Lists dashboards in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_dashboards)
        """

    def list_data_sets(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSetsResponseTypeDef:
        """
        Lists all of the datasets belonging to the current Amazon Web Services account
        in an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sets)
        """

    def list_data_sources(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists data sources in current Amazon Web Services Region that belong to this
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_data_sources)
        """

    def list_folder_members(
        self, *, AwsAccountId: str, FolderId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFolderMembersResponseTypeDef:
        """
        List all assets ( `DASHBOARD`, `ANALYSIS`, and `DATASET`) in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_folder_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_folder_members)
        """

    def list_folders(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFoldersResponseTypeDef:
        """
        Lists all folders in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_folders)
        """

    def list_group_memberships(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        Lists member users in a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_group_memberships)
        """

    def list_groups(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        Lists all user groups in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_groups)
        """

    def list_iam_policy_assignments(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: AssignmentStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListIAMPolicyAssignmentsResponseTypeDef:
        """
        Lists the IAM policy assignments in the current Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_iam_policy_assignments)
        """

    def list_iam_policy_assignments_for_user(
        self,
        *,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
        """
        Lists all of the IAM policy assignments, including the Amazon Resource Names
        (ARNs), for the IAM policies assigned to the specified user and group, or groups
        that the user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_iam_policy_assignments_for_user)
        """

    def list_identity_propagation_configs(
        self, *, AwsAccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIdentityPropagationConfigsResponseTypeDef:
        """
        Lists all services and authorized targets that the Amazon QuickSight IAM
        Identity Center application can access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_identity_propagation_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_identity_propagation_configs)
        """

    def list_ingestions(
        self, *, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIngestionsResponseTypeDef:
        """
        Lists the history of SPICE ingestions for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_ingestions)
        """

    def list_namespaces(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListNamespacesResponseTypeDef:
        """
        Lists the namespaces for the specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_namespaces)
        """

    def list_refresh_schedules(
        self, *, AwsAccountId: str, DataSetId: str
    ) -> ListRefreshSchedulesResponseTypeDef:
        """
        Lists the refresh schedules of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_refresh_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_refresh_schedules)
        """

    def list_role_memberships(
        self,
        *,
        Role: RoleType,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRoleMembershipsResponseTypeDef:
        """
        Lists all groups that are associated with a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_role_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_role_memberships)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_tags_for_resource)
        """

    def list_template_aliases(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateAliasesResponseTypeDef:
        """
        Lists all the aliases of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_aliases)
        """

    def list_template_versions(
        self, *, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        Lists all the versions of the templates in the current Amazon QuickSight
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_template_versions)
        """

    def list_templates(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists all the templates in the current Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_templates)
        """

    def list_theme_aliases(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeAliasesResponseTypeDef:
        """
        Lists all the aliases of a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_theme_aliases)
        """

    def list_theme_versions(
        self, *, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeVersionsResponseTypeDef:
        """
        Lists all the versions of the themes in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_theme_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_theme_versions)
        """

    def list_themes(
        self,
        *,
        AwsAccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Type: ThemeTypeType = None
    ) -> ListThemesResponseTypeDef:
        """
        Lists all the themes in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_themes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_themes)
        """

    def list_topic_refresh_schedules(
        self, *, AwsAccountId: str, TopicId: str
    ) -> ListTopicRefreshSchedulesResponseTypeDef:
        """
        Lists all of the refresh schedules for a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_topic_refresh_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_topic_refresh_schedules)
        """

    def list_topics(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTopicsResponseTypeDef:
        """
        Lists all of the topics within an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_topics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_topics)
        """

    def list_user_groups(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListUserGroupsResponseTypeDef:
        """
        Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member
        of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_user_groups)
        """

    def list_users(
        self, *, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        Returns a list of all of the Amazon QuickSight users belonging to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_users)
        """

    def list_vpc_connections(
        self, *, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListVPCConnectionsResponseTypeDef:
        """
        Lists all of the VPC connections in the current set Amazon Web Services Region
        of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.list_vpc_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#list_vpc_connections)
        """

    def put_data_set_refresh_properties(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        DataSetRefreshProperties: "DataSetRefreshPropertiesTypeDef"
    ) -> PutDataSetRefreshPropertiesResponseTypeDef:
        """
        Creates or updates the dataset refresh properties for the dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.put_data_set_refresh_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#put_data_set_refresh_properties)
        """

    def register_user(
        self,
        *,
        IdentityType: IdentityTypeType,
        Email: str,
        UserRole: UserRoleType,
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
        CustomPermissionsName: str = None,
        ExternalLoginFederationProviderType: str = None,
        CustomFederationProviderUrl: str = None,
        ExternalLoginId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> RegisterUserResponseTypeDef:
        """
        Creates an Amazon QuickSight user whose identity is associated with the Identity
        and Access Management (IAM) identity or role specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.register_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#register_user)
        """

    def restore_analysis(
        self, *, AwsAccountId: str, AnalysisId: str
    ) -> RestoreAnalysisResponseTypeDef:
        """
        Restores an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.restore_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#restore_analysis)
        """

    def search_analyses(
        self,
        *,
        AwsAccountId: str,
        Filters: List["AnalysisSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchAnalysesResponseTypeDef:
        """
        Searches for analyses that belong to the user specified in the filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_analyses)
        """

    def search_dashboards(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DashboardSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchDashboardsResponseTypeDef:
        """
        Searches for dashboards that belong to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_dashboards)
        """

    def search_data_sets(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSetSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchDataSetsResponseTypeDef:
        """
        Use the `SearchDataSets` operation to search for datasets that belong to an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_data_sets)
        """

    def search_data_sources(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSourceSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchDataSourcesResponseTypeDef:
        """
        Use the `SearchDataSources` operation to search for data sources that belong to
        an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_data_sources)
        """

    def search_folders(
        self,
        *,
        AwsAccountId: str,
        Filters: List["FolderSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchFoldersResponseTypeDef:
        """
        Searches the subfolders in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_folders)
        """

    def search_groups(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        Filters: List["GroupSearchFilterTypeDef"],
        NextToken: str = None,
        MaxResults: int = None
    ) -> SearchGroupsResponseTypeDef:
        """
        Use the `SearchGroups` operation to search groups in a specified Amazon
        QuickSight namespace using the supplied filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.search_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#search_groups)
        """

    def start_asset_bundle_export_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleExportJobId: str,
        ResourceArns: List[str],
        ExportFormat: AssetBundleExportFormatType,
        IncludeAllDependencies: bool = None,
        CloudFormationOverridePropertyConfiguration: "AssetBundleCloudFormationOverridePropertyConfigurationTypeDef" = None,
        IncludePermissions: bool = None,
        IncludeTags: bool = None,
        ValidationStrategy: "AssetBundleExportJobValidationStrategyTypeDef" = None
    ) -> StartAssetBundleExportJobResponseTypeDef:
        """
        Starts an Asset Bundle export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.start_asset_bundle_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#start_asset_bundle_export_job)
        """

    def start_asset_bundle_import_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleImportJobId: str,
        AssetBundleImportSource: "AssetBundleImportSourceTypeDef",
        OverrideParameters: "AssetBundleImportJobOverrideParametersTypeDef" = None,
        FailureAction: AssetBundleImportFailureActionType = None,
        OverridePermissions: "AssetBundleImportJobOverridePermissionsTypeDef" = None,
        OverrideTags: "AssetBundleImportJobOverrideTagsTypeDef" = None,
        OverrideValidationStrategy: "AssetBundleImportJobOverrideValidationStrategyTypeDef" = None
    ) -> StartAssetBundleImportJobResponseTypeDef:
        """
        Starts an Asset Bundle import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.start_asset_bundle_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#start_asset_bundle_import_job)
        """

    def start_dashboard_snapshot_job(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        SnapshotJobId: str,
        UserConfiguration: "SnapshotUserConfigurationTypeDef",
        SnapshotConfiguration: "SnapshotConfigurationTypeDef"
    ) -> StartDashboardSnapshotJobResponseTypeDef:
        """
        Starts an asynchronous job that generates a snapshot of a dashboard's output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.start_dashboard_snapshot_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#start_dashboard_snapshot_job)
        """

    def tag_resource(
        self, *, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseTypeDef:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon QuickSight
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#tag_resource)
        """

    def untag_resource(
        self, *, ResourceArn: str, TagKeys: List[str]
    ) -> UntagResourceResponseTypeDef:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#untag_resource)
        """

    def update_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None
    ) -> UpdateAccountCustomizationResponseTypeDef:
        """
        Updates Amazon QuickSight customizations for the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_account_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_customization)
        """

    def update_account_settings(
        self,
        *,
        AwsAccountId: str,
        DefaultNamespace: str,
        NotificationEmail: str = None,
        TerminationProtectionEnabled: bool = None
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        Updates the Amazon QuickSight settings in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_account_settings)
        """

    def update_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        Parameters: "ParametersTypeDef" = None,
        SourceEntity: "AnalysisSourceEntityTypeDef" = None,
        ThemeArn: str = None,
        Definition: "AnalysisDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None
    ) -> UpdateAnalysisResponseTypeDef:
        """
        Updates an analysis in Amazon QuickSight See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateAnalysis>`_
        **Request Syntax** # This section is too large to render.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_analysis)
        """

    def update_analysis_permissions(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateAnalysisPermissionsResponseTypeDef:
        """
        Updates the read and write permissions for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_analysis_permissions)
        """

    def update_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: "DashboardSourceEntityTypeDef" = None,
        Parameters: "ParametersTypeDef" = None,
        VersionDescription: str = None,
        DashboardPublishOptions: "DashboardPublishOptionsTypeDef" = None,
        ThemeArn: str = None,
        Definition: "DashboardVersionDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None
    ) -> UpdateDashboardResponseTypeDef:
        """
        Updates a dashboard in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard)
        """

    def update_dashboard_links(
        self, *, AwsAccountId: str, DashboardId: str, LinkEntities: List[str]
    ) -> UpdateDashboardLinksResponseTypeDef:
        """
        Updates the linked analyses on a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_dashboard_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_links)
        """

    def update_dashboard_permissions(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
        GrantLinkPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokeLinkPermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDashboardPermissionsResponseTypeDef:
        """
        Updates read and write permissions on a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, *, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> UpdateDashboardPublishedVersionResponseTypeDef:
        """
        Updates the published version of a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_dashboard_published_version)
        """

    def update_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: DataSetImportModeType,
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        FieldFolders: Dict[str, "FieldFolderTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        RowLevelPermissionTagConfiguration: "RowLevelPermissionTagConfigurationTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
        DataSetUsageConfiguration: "DataSetUsageConfigurationTypeDef" = None,
        DatasetParameters: List["DatasetParameterTypeDef"] = None
    ) -> UpdateDataSetResponseTypeDef:
        """
        Updates a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_set)
        """

    def update_data_set_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDataSetPermissionsResponseTypeDef:
        """
        Updates the permissions on a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_set_permissions)
        """

    def update_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: "DataSourceCredentialsTypeDef" = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_source)
        """

    def update_data_source_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateDataSourcePermissionsResponseTypeDef:
        """
        Updates the permissions to a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_data_source_permissions)
        """

    def update_folder(
        self, *, AwsAccountId: str, FolderId: str, Name: str
    ) -> UpdateFolderResponseTypeDef:
        """
        Updates the name of a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_folder)
        """

    def update_folder_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateFolderPermissionsResponseTypeDef:
        """
        Updates permissions of a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_folder_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_folder_permissions)
        """

    def update_group(
        self, *, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> UpdateGroupResponseTypeDef:
        """
        Changes a group description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_group)
        """

    def update_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: AssignmentStatusType = None,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None
    ) -> UpdateIAMPolicyAssignmentResponseTypeDef:
        """
        Updates an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_iam_policy_assignment)
        """

    def update_identity_propagation_config(
        self,
        *,
        AwsAccountId: str,
        Service: Literal["REDSHIFT"],
        AuthorizedTargets: List[str] = None
    ) -> UpdateIdentityPropagationConfigResponseTypeDef:
        """
        Adds or updates services and authorized targets to configure what the Amazon
        QuickSight IAM Identity Center application can access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_identity_propagation_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_identity_propagation_config)
        """

    def update_ip_restriction(
        self,
        *,
        AwsAccountId: str,
        IpRestrictionRuleMap: Dict[str, str] = None,
        VpcIdRestrictionRuleMap: Dict[str, str] = None,
        VpcEndpointIdRestrictionRuleMap: Dict[str, str] = None,
        Enabled: bool = None
    ) -> UpdateIpRestrictionResponseTypeDef:
        """
        Updates the content and status of IP rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_ip_restriction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_ip_restriction)
        """

    def update_key_registration(
        self, *, AwsAccountId: str, KeyRegistration: List["RegisteredCustomerManagedKeyTypeDef"]
    ) -> UpdateKeyRegistrationResponseTypeDef:
        """
        Updates a customer managed key in a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_key_registration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_key_registration)
        """

    def update_public_sharing_settings(
        self, *, AwsAccountId: str, PublicSharingEnabled: bool = None
    ) -> UpdatePublicSharingSettingsResponseTypeDef:
        """
        Use the `UpdatePublicSharingSettings` operation to turn on or turn off the
        public sharing settings of an Amazon QuickSight dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_public_sharing_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_public_sharing_settings)
        """

    def update_refresh_schedule(
        self, *, DataSetId: str, AwsAccountId: str, Schedule: "RefreshScheduleTypeDef"
    ) -> UpdateRefreshScheduleResponseTypeDef:
        """
        Updates a refresh schedule for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_refresh_schedule)
        """

    def update_role_custom_permission(
        self, *, CustomPermissionsName: str, Role: RoleType, AwsAccountId: str, Namespace: str
    ) -> UpdateRoleCustomPermissionResponseTypeDef:
        """
        Updates the custom permissions that are associated with a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_role_custom_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_role_custom_permission)
        """

    def update_spice_capacity_configuration(
        self, *, AwsAccountId: str, PurchaseMode: PurchaseModeType
    ) -> UpdateSPICECapacityConfigurationResponseTypeDef:
        """
        Updates the SPICE capacity configuration for a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_spice_capacity_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_spice_capacity_configuration)
        """

    def update_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: "TemplateSourceEntityTypeDef" = None,
        VersionDescription: str = None,
        Name: str = None,
        Definition: "TemplateVersionDefinitionTypeDef" = None,
        ValidationStrategy: "ValidationStrategyTypeDef" = None
    ) -> UpdateTemplateResponseTypeDef:
        """
        Updates a template from an existing Amazon QuickSight analysis or another
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template)
        """

    def update_template_alias(
        self, *, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> UpdateTemplateAliasResponseTypeDef:
        """
        Updates the template alias of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template_alias)
        """

    def update_template_permissions(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateTemplatePermissionsResponseTypeDef:
        """
        Updates the resource permissions for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_template_permissions)
        """

    def update_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        BaseThemeId: str,
        Name: str = None,
        VersionDescription: str = None,
        Configuration: "ThemeConfigurationTypeDef" = None
    ) -> UpdateThemeResponseTypeDef:
        """
        Updates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_theme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme)
        """

    def update_theme_alias(
        self, *, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> UpdateThemeAliasResponseTypeDef:
        """
        Updates an alias of a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_theme_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme_alias)
        """

    def update_theme_permissions(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateThemePermissionsResponseTypeDef:
        """
        Updates the resource permissions for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_theme_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_theme_permissions)
        """

    def update_topic(
        self, *, AwsAccountId: str, TopicId: str, Topic: "TopicDetailsTypeDef"
    ) -> UpdateTopicResponseTypeDef:
        """
        Updates a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_topic)
        """

    def update_topic_permissions(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None
    ) -> UpdateTopicPermissionsResponseTypeDef:
        """
        Updates the permissions of a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_topic_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_topic_permissions)
        """

    def update_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetId: str,
        RefreshSchedule: "TopicRefreshScheduleTypeDef"
    ) -> UpdateTopicRefreshScheduleResponseTypeDef:
        """
        Updates a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_topic_refresh_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_topic_refresh_schedule)
        """

    def update_user(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: UserRoleType,
        CustomPermissionsName: str = None,
        UnapplyCustomPermissions: bool = None,
        ExternalLoginFederationProviderType: str = None,
        CustomFederationProviderUrl: str = None,
        ExternalLoginId: str = None
    ) -> UpdateUserResponseTypeDef:
        """
        Updates an Amazon QuickSight user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_user)
        """

    def update_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
        Name: str,
        SubnetIds: List[str],
        SecurityGroupIds: List[str],
        RoleArn: str,
        DnsResolvers: List[str] = None
    ) -> UpdateVPCConnectionResponseTypeDef:
        """
        Updates a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Client.update_vpc_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client.html#update_vpc_connection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_permissions"]
    ) -> DescribeFolderPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderpermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_resolved_permissions"]
    ) -> DescribeFolderResolvedPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.DescribeFolderResolvedPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#describefolderresolvedpermissionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyses"]) -> ListAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_bundle_export_jobs"]
    ) -> ListAssetBundleExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleexportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_bundle_import_jobs"]
    ) -> ListAssetBundleImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListAssetBundleImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listassetbundleimportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dashboard_versions"]
    ) -> ListDashboardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_folder_members"]
    ) -> ListFolderMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListFolderMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfoldermemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_folders"]) -> ListFoldersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListFolders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listfolderspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_memberships"]
    ) -> ListGroupMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListGroupMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupmembershipspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_iam_policy_assignments"]
    ) -> ListIAMPolicyAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_iam_policy_assignments_for_user"]
    ) -> ListIAMPolicyAssignmentsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListIAMPolicyAssignmentsForUser)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listiampolicyassignmentsforuserpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_memberships"]
    ) -> ListRoleMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListRoleMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listrolemembershipspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_aliases"]
    ) -> ListTemplateAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_versions"]
    ) -> ListTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_theme_versions"]
    ) -> ListThemeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_themes"]) -> ListThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_user_groups"]) -> ListUserGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListUserGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listusergroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listuserspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_analyses"]) -> SearchAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_dashboards"]
    ) -> SearchDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_data_sets"]) -> SearchDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_data_sources"]
    ) -> SearchDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_folders"]) -> SearchFoldersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchFolders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchfolderspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_groups"]) -> SearchGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/quicksight.html#QuickSight.Paginator.SearchGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchgroupspaginator)
        """
