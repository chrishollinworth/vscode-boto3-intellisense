# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for quicksight service client

Usage::

    ```python
    import boto3
    from mypy_boto3_quicksight import QuickSightClient

    client: QuickSightClient = boto3.client("quicksight")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_quicksight.type_defs import (
    AccountCustomizationTypeDef,
    AnalysisSearchFilterTypeDef,
    AnalysisSourceEntityTypeDef,
    CancelIngestionResponseTypeDef,
    ColumnGroupTypeDef,
    ColumnLevelPermissionRuleTypeDef,
    CreateAccountCustomizationResponseTypeDef,
    CreateAnalysisResponseTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDataSetResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateIAMPolicyAssignmentResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateTemplateAliasResponseTypeDef,
    CreateTemplateResponseTypeDef,
    CreateThemeAliasResponseTypeDef,
    CreateThemeResponseTypeDef,
    DashboardPublishOptionsTypeDef,
    DashboardSearchFilterTypeDef,
    DashboardSourceEntityTypeDef,
    DataSourceCredentialsTypeDef,
    DataSourceParametersTypeDef,
    DeleteAccountCustomizationResponseTypeDef,
    DeleteAnalysisResponseTypeDef,
    DeleteDashboardResponseTypeDef,
    DeleteDataSetResponseTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteGroupMembershipResponseTypeDef,
    DeleteGroupResponseTypeDef,
    DeleteIAMPolicyAssignmentResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteTemplateAliasResponseTypeDef,
    DeleteTemplateResponseTypeDef,
    DeleteThemeAliasResponseTypeDef,
    DeleteThemeResponseTypeDef,
    DeleteUserByPrincipalIdResponseTypeDef,
    DeleteUserResponseTypeDef,
    DescribeAccountCustomizationResponseTypeDef,
    DescribeAccountSettingsResponseTypeDef,
    DescribeAnalysisPermissionsResponseTypeDef,
    DescribeAnalysisResponseTypeDef,
    DescribeDashboardPermissionsResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDataSetPermissionsResponseTypeDef,
    DescribeDataSetResponseTypeDef,
    DescribeDataSourcePermissionsResponseTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeIAMPolicyAssignmentResponseTypeDef,
    DescribeIngestionResponseTypeDef,
    DescribeNamespaceResponseTypeDef,
    DescribeTemplateAliasResponseTypeDef,
    DescribeTemplatePermissionsResponseTypeDef,
    DescribeTemplateResponseTypeDef,
    DescribeThemeAliasResponseTypeDef,
    DescribeThemePermissionsResponseTypeDef,
    DescribeThemeResponseTypeDef,
    DescribeUserResponseTypeDef,
    GetDashboardEmbedUrlResponseTypeDef,
    GetSessionEmbedUrlResponseTypeDef,
    ListAnalysesResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIAMPolicyAssignmentsForUserResponseTypeDef,
    ListIAMPolicyAssignmentsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemeAliasesResponseTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsResponseTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogicalTableTypeDef,
    ParametersTypeDef,
    PhysicalTableTypeDef,
    RegisterUserResponseTypeDef,
    ResourcePermissionTypeDef,
    RestoreAnalysisResponseTypeDef,
    RowLevelPermissionDataSetTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsResponseTypeDef,
    SslPropertiesTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    TemplateSourceEntityTypeDef,
    ThemeConfigurationTypeDef,
    UntagResourceResponseTypeDef,
    UpdateAccountCustomizationResponseTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateAnalysisPermissionsResponseTypeDef,
    UpdateAnalysisResponseTypeDef,
    UpdateDashboardPermissionsResponseTypeDef,
    UpdateDashboardPublishedVersionResponseTypeDef,
    UpdateDashboardResponseTypeDef,
    UpdateDataSetPermissionsResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateDataSourcePermissionsResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIAMPolicyAssignmentResponseTypeDef,
    UpdateTemplateAliasResponseTypeDef,
    UpdateTemplatePermissionsResponseTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateThemeAliasResponseTypeDef,
    UpdateThemePermissionsResponseTypeDef,
    UpdateThemeResponseTypeDef,
    UpdateUserResponseTypeDef,
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
    LimitExceededException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    QuickSightUserNotFoundException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    SessionLifetimeInMinutesInvalidException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedUserEditionException: Type[BotocoreClientError]


class QuickSightClient:
    """
    [QuickSight.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        """

    def cancel_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> CancelIngestionResponseTypeDef:
        """
        [Client.cancel_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        """

    def create_account_customization(
        self,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAccountCustomizationResponseTypeDef:
        """
        [Client.create_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_account_customization)
        """

    def create_analysis(
        self,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: AnalysisSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        ThemeArn: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAnalysisResponseTypeDef:
        """
        [Client.create_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_analysis)
        """

    def create_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
        ThemeArn: str = None,
    ) -> CreateDashboardResponseTypeDef:
        """
        [Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        """

    def create_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        """

    def create_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "ORACLE",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TWITTER",
            "TIMESTREAM",
        ],
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        """

    def create_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_group)
        """

    def create_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        [Client.create_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        """

    def create_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"],
        Namespace: str,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> CreateIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.create_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        """

    def create_ingestion(
        self, DataSetId: str, IngestionId: str, AwsAccountId: str
    ) -> CreateIngestionResponseTypeDef:
        """
        [Client.create_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        """

    def create_namespace(
        self,
        AwsAccountId: str,
        Namespace: str,
        IdentityStore: Literal["QUICKSIGHT"],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateNamespaceResponseTypeDef:
        """
        [Client.create_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_namespace)
        """

    def create_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        Name: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        VersionDescription: str = None,
    ) -> CreateTemplateResponseTypeDef:
        """
        [Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_template)
        """

    def create_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> CreateTemplateAliasResponseTypeDef:
        """
        [Client.create_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        """

    def create_theme(
        self,
        AwsAccountId: str,
        ThemeId: str,
        Name: str,
        BaseThemeId: str,
        Configuration: "ThemeConfigurationTypeDef",
        VersionDescription: str = None,
        Permissions: List["ResourcePermissionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateThemeResponseTypeDef:
        """
        [Client.create_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_theme)
        """

    def create_theme_alias(
        self, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> CreateThemeAliasResponseTypeDef:
        """
        [Client.create_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)
        """

    def delete_account_customization(
        self, AwsAccountId: str, Namespace: str = None
    ) -> DeleteAccountCustomizationResponseTypeDef:
        """
        [Client.delete_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_account_customization)
        """

    def delete_analysis(
        self,
        AwsAccountId: str,
        AnalysisId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None,
    ) -> DeleteAnalysisResponseTypeDef:
        """
        [Client.delete_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_analysis)
        """

    def delete_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> DeleteDashboardResponseTypeDef:
        """
        [Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        """

    def delete_data_set(self, AwsAccountId: str, DataSetId: str) -> DeleteDataSetResponseTypeDef:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        """

    def delete_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DeleteDataSourceResponseTypeDef:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        """

    def delete_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupResponseTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_group)
        """

    def delete_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupMembershipResponseTypeDef:
        """
        [Client.delete_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DeleteIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.delete_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        """

    def delete_namespace(self, AwsAccountId: str, Namespace: str) -> DeleteNamespaceResponseTypeDef:
        """
        [Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_namespace)
        """

    def delete_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> DeleteTemplateResponseTypeDef:
        """
        [Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_template)
        """

    def delete_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DeleteTemplateAliasResponseTypeDef:
        """
        [Client.delete_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        """

    def delete_theme(
        self, AwsAccountId: str, ThemeId: str, VersionNumber: int = None
    ) -> DeleteThemeResponseTypeDef:
        """
        [Client.delete_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_theme)
        """

    def delete_theme_alias(
        self, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DeleteThemeAliasResponseTypeDef:
        """
        [Client.delete_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)
        """

    def delete_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserResponseTypeDef:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_user)
        """

    def delete_user_by_principal_id(
        self, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserByPrincipalIdResponseTypeDef:
        """
        [Client.delete_user_by_principal_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        """

    def describe_account_customization(
        self, AwsAccountId: str, Namespace: str = None, Resolved: bool = None
    ) -> DescribeAccountCustomizationResponseTypeDef:
        """
        [Client.describe_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)
        """

    def describe_account_settings(
        self, AwsAccountId: str
    ) -> DescribeAccountSettingsResponseTypeDef:
        """
        [Client.describe_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)
        """

    def describe_analysis(
        self, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisResponseTypeDef:
        """
        [Client.describe_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_analysis)
        """

    def describe_analysis_permissions(
        self, AwsAccountId: str, AnalysisId: str
    ) -> DescribeAnalysisPermissionsResponseTypeDef:
        """
        [Client.describe_analysis_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_analysis_permissions)
        """

    def describe_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeDashboardResponseTypeDef:
        """
        [Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        """

    def describe_dashboard_permissions(
        self, AwsAccountId: str, DashboardId: str
    ) -> DescribeDashboardPermissionsResponseTypeDef:
        """
        [Client.describe_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        """

    def describe_data_set(
        self, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetResponseTypeDef:
        """
        [Client.describe_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        """

    def describe_data_set_permissions(
        self, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetPermissionsResponseTypeDef:
        """
        [Client.describe_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        """

    def describe_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourceResponseTypeDef:
        """
        [Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        """

    def describe_data_source_permissions(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourcePermissionsResponseTypeDef:
        """
        [Client.describe_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        """

    def describe_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupResponseTypeDef:
        """
        [Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_group)
        """

    def describe_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DescribeIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.describe_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> DescribeIngestionResponseTypeDef:
        """
        [Client.describe_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        """

    def describe_namespace(
        self, AwsAccountId: str, Namespace: str
    ) -> DescribeNamespaceResponseTypeDef:
        """
        [Client.describe_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_namespace)
        """

    def describe_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeTemplateResponseTypeDef:
        """
        [Client.describe_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_template)
        """

    def describe_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DescribeTemplateAliasResponseTypeDef:
        """
        [Client.describe_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        """

    def describe_template_permissions(
        self, AwsAccountId: str, TemplateId: str
    ) -> DescribeTemplatePermissionsResponseTypeDef:
        """
        [Client.describe_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        """

    def describe_theme(
        self, AwsAccountId: str, ThemeId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeThemeResponseTypeDef:
        """
        [Client.describe_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_theme)
        """

    def describe_theme_alias(
        self, AwsAccountId: str, ThemeId: str, AliasName: str
    ) -> DescribeThemeAliasResponseTypeDef:
        """
        [Client.describe_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)
        """

    def describe_theme_permissions(
        self, AwsAccountId: str, ThemeId: str
    ) -> DescribeThemePermissionsResponseTypeDef:
        """
        [Client.describe_theme_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)
        """

    def describe_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        """

    def get_dashboard_embed_url(
        self,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        StatePersistenceEnabled: bool = None,
        UserArn: str = None,
    ) -> GetDashboardEmbedUrlResponseTypeDef:
        """
        [Client.get_dashboard_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        """

    def get_session_embed_url(
        self,
        AwsAccountId: str,
        EntryPoint: str = None,
        SessionLifetimeInMinutes: int = None,
        UserArn: str = None,
    ) -> GetSessionEmbedUrlResponseTypeDef:
        """
        [Client.get_session_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)
        """

    def list_analyses(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAnalysesResponseTypeDef:
        """
        [Client.list_analyses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_analyses)
        """

    def list_dashboard_versions(
        self, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardVersionsResponseTypeDef:
        """
        [Client.list_dashboard_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        """

    def list_dashboards(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        """

    def list_data_sets(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        """

    def list_data_sources(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        """

    def list_group_memberships(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        [Client.list_group_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        """

    def list_groups(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_groups)
        """

    def list_iam_policy_assignments(
        self,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListIAMPolicyAssignmentsResponseTypeDef:
        """
        [Client.list_iam_policy_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        """

    def list_iam_policy_assignments_for_user(
        self,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
        """
        [Client.list_iam_policy_assignments_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        """

    def list_ingestions(
        self, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIngestionsResponseTypeDef:
        """
        [Client.list_ingestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        """

    def list_namespaces(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListNamespacesResponseTypeDef:
        """
        [Client.list_namespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_namespaces)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        """

    def list_template_aliases(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateAliasesResponseTypeDef:
        """
        [Client.list_template_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        """

    def list_template_versions(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        [Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        """

    def list_templates(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_templates)
        """

    def list_theme_aliases(
        self, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeAliasesResponseTypeDef:
        """
        [Client.list_theme_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)
        """

    def list_theme_versions(
        self, AwsAccountId: str, ThemeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThemeVersionsResponseTypeDef:
        """
        [Client.list_theme_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_theme_versions)
        """

    def list_themes(
        self,
        AwsAccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Type: Literal["QUICKSIGHT", "CUSTOM", "ALL"] = None,
    ) -> ListThemesResponseTypeDef:
        """
        [Client.list_themes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_themes)
        """

    def list_user_groups(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListUserGroupsResponseTypeDef:
        """
        [Client.list_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        """

    def list_users(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.list_users)
        """

    def register_user(
        self,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        Email: str,
        UserRole: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
        CustomPermissionsName: str = None,
    ) -> RegisterUserResponseTypeDef:
        """
        [Client.register_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.register_user)
        """

    def restore_analysis(
        self, AwsAccountId: str, AnalysisId: str
    ) -> RestoreAnalysisResponseTypeDef:
        """
        [Client.restore_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.restore_analysis)
        """

    def search_analyses(
        self,
        AwsAccountId: str,
        Filters: List[AnalysisSearchFilterTypeDef],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchAnalysesResponseTypeDef:
        """
        [Client.search_analyses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.search_analyses)
        """

    def search_dashboards(
        self,
        AwsAccountId: str,
        Filters: List[DashboardSearchFilterTypeDef],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchDashboardsResponseTypeDef:
        """
        [Client.search_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.search_dashboards)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> UntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        """

    def update_account_customization(
        self,
        AwsAccountId: str,
        AccountCustomization: "AccountCustomizationTypeDef",
        Namespace: str = None,
    ) -> UpdateAccountCustomizationResponseTypeDef:
        """
        [Client.update_account_customization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_account_customization)
        """

    def update_account_settings(
        self, AwsAccountId: str, DefaultNamespace: str, NotificationEmail: str = None
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        [Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_account_settings)
        """

    def update_analysis(
        self,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        SourceEntity: AnalysisSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        ThemeArn: str = None,
    ) -> UpdateAnalysisResponseTypeDef:
        """
        [Client.update_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_analysis)
        """

    def update_analysis_permissions(
        self,
        AwsAccountId: str,
        AnalysisId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateAnalysisPermissionsResponseTypeDef:
        """
        [Client.update_analysis_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)
        """

    def update_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
        ThemeArn: str = None,
    ) -> UpdateDashboardResponseTypeDef:
        """
        [Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        """

    def update_dashboard_permissions(
        self,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateDashboardPermissionsResponseTypeDef:
        """
        [Client.update_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> UpdateDashboardPublishedVersionResponseTypeDef:
        """
        [Client.update_dashboard_published_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        """

    def update_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, "PhysicalTableTypeDef"],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, "LogicalTableTypeDef"] = None,
        ColumnGroups: List["ColumnGroupTypeDef"] = None,
        RowLevelPermissionDataSet: "RowLevelPermissionDataSetTypeDef" = None,
        ColumnLevelPermissionRules: List["ColumnLevelPermissionRuleTypeDef"] = None,
    ) -> UpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        """

    def update_data_set_permissions(
        self,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateDataSetPermissionsResponseTypeDef:
        """
        [Client.update_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        """

    def update_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: "DataSourceParametersTypeDef" = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        VpcConnectionProperties: "VpcConnectionPropertiesTypeDef" = None,
        SslProperties: "SslPropertiesTypeDef" = None,
    ) -> UpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        """

    def update_data_source_permissions(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateDataSourcePermissionsResponseTypeDef:
        """
        [Client.update_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        """

    def update_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> UpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_group)
        """

    def update_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> UpdateIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.update_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        """

    def update_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        VersionDescription: str = None,
        Name: str = None,
    ) -> UpdateTemplateResponseTypeDef:
        """
        [Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_template)
        """

    def update_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> UpdateTemplateAliasResponseTypeDef:
        """
        [Client.update_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        """

    def update_template_permissions(
        self,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateTemplatePermissionsResponseTypeDef:
        """
        [Client.update_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        """

    def update_theme(
        self,
        AwsAccountId: str,
        ThemeId: str,
        BaseThemeId: str,
        Name: str = None,
        VersionDescription: str = None,
        Configuration: "ThemeConfigurationTypeDef" = None,
    ) -> UpdateThemeResponseTypeDef:
        """
        [Client.update_theme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_theme)
        """

    def update_theme_alias(
        self, AwsAccountId: str, ThemeId: str, AliasName: str, ThemeVersionNumber: int
    ) -> UpdateThemeAliasResponseTypeDef:
        """
        [Client.update_theme_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_theme_alias)
        """

    def update_theme_permissions(
        self,
        AwsAccountId: str,
        ThemeId: str,
        GrantPermissions: List["ResourcePermissionTypeDef"] = None,
        RevokePermissions: List["ResourcePermissionTypeDef"] = None,
    ) -> UpdateThemePermissionsResponseTypeDef:
        """
        [Client.update_theme_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_theme_permissions)
        """

    def update_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        CustomPermissionsName: str = None,
        UnapplyCustomPermissions: bool = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/quicksight.html#QuickSight.Client.update_user)
        """
