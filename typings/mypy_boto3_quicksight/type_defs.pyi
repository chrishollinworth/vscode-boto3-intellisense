"""
Main interface for quicksight service type definitions.

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountCustomizationTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AnalysisErrorTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "AnalysisSummaryTypeDef",
    "AnalysisTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "BorderStyleTypeDef",
    "CalculatedColumnTypeDef",
    "CastColumnTypeOperationTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnTagTypeDef",
    "CreateColumnsOperationTypeDef",
    "CredentialPairTypeDef",
    "CustomSqlTypeDef",
    "DashboardErrorTypeDef",
    "DashboardSourceTemplateTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardTypeDef",
    "DashboardVersionSummaryTypeDef",
    "DashboardVersionTypeDef",
    "DataColorPaletteTypeDef",
    "DataSetConfigurationTypeDef",
    "DataSetReferenceTypeDef",
    "DataSetSchemaTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DataSourceParametersTypeDef",
    "DataSourceTypeDef",
    "DateTimeParameterTypeDef",
    "DecimalParameterTypeDef",
    "ErrorInfoTypeDef",
    "ExportToCSVOptionTypeDef",
    "FilterOperationTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GroupMemberTypeDef",
    "GroupTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "IngestionTypeDef",
    "InputColumnTypeDef",
    "IntegerParameterTypeDef",
    "JiraParametersTypeDef",
    "JoinInstructionTypeDef",
    "LogicalTableSourceTypeDef",
    "LogicalTableTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "MariaDbParametersTypeDef",
    "MySqlParametersTypeDef",
    "NamespaceErrorTypeDef",
    "NamespaceInfoV2TypeDef",
    "OracleParametersTypeDef",
    "OutputColumnTypeDef",
    "PhysicalTableTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "ProjectOperationTypeDef",
    "QueueInfoTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "RelationalTableTypeDef",
    "RenameColumnOperationTypeDef",
    "ResourcePermissionTypeDef",
    "RowInfoTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "S3ParametersTypeDef",
    "S3SourceTypeDef",
    "ServiceNowParametersTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetStyleTypeDef",
    "SheetTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "SslPropertiesTypeDef",
    "StringParameterTypeDef",
    "TagColumnOperationTypeDef",
    "TagTypeDef",
    "TemplateAliasTypeDef",
    "TemplateErrorTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateVersionSummaryTypeDef",
    "TemplateVersionTypeDef",
    "TeradataParametersTypeDef",
    "ThemeAliasTypeDef",
    "ThemeConfigurationTypeDef",
    "ThemeErrorTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ThemeVersionTypeDef",
    "TileLayoutStyleTypeDef",
    "TileStyleTypeDef",
    "TransformOperationTypeDef",
    "TwitterParametersTypeDef",
    "UIColorPaletteTypeDef",
    "UploadSettingsTypeDef",
    "UserTypeDef",
    "VpcConnectionPropertiesTypeDef",
    "AnalysisSearchFilterTypeDef",
    "AnalysisSourceEntityTypeDef",
    "CancelIngestionResponseTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "CreateThemeResponseTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSourceEntityTypeDef",
    "DataSourceCredentialsTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSetResponseTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeIngestionResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeTemplateResponseTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeThemeResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesResponseTypeDef",
    "ListUserGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ParametersTypeDef",
    "RegisterUserResponseTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "SearchAnalysesResponseTypeDef",
    "SearchDashboardsResponseTypeDef",
    "TagResourceResponseTypeDef",
    "TemplateSourceEntityTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateUserResponseTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef", {"DefaultTheme": str}, total=False
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": str,
        "Edition": Literal["STANDARD", "ENTERPRISE"],
        "DefaultNamespace": str,
        "NotificationEmail": str,
    },
    total=False,
)

ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef", {"AssignmentName": str, "PolicyArn": str}, total=False
)

AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef", {"Domain": str}
)

AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": Literal[
            "ACCESS_DENIED",
            "SOURCE_NOT_FOUND",
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_NOT_FOUND",
            "COLUMN_TYPE_MISMATCH",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
        ],
        "Message": str,
    },
    total=False,
)

AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {"DataSetReferences": List["DataSetReferenceTypeDef"], "Arn": str},
)

AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "Name": str,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "AnalysisId": str,
        "Arn": str,
        "Name": str,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Errors": List["AnalysisErrorTypeDef"],
        "DataSetArns": List[str],
        "ThemeArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

AthenaParametersTypeDef = TypedDict("AthenaParametersTypeDef", {"WorkGroup": str}, total=False)

AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef", {"DataSetName": str}
)

BorderStyleTypeDef = TypedDict("BorderStyleTypeDef", {"Show": bool}, total=False)

CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef", {"ColumnName": str, "ColumnId": str, "Expression": str}
)

_RequiredCastColumnTypeOperationTypeDef = TypedDict(
    "_RequiredCastColumnTypeOperationTypeDef",
    {"ColumnName": str, "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"]},
)
_OptionalCastColumnTypeOperationTypeDef = TypedDict(
    "_OptionalCastColumnTypeOperationTypeDef", {"Format": str}, total=False
)


class CastColumnTypeOperationTypeDef(
    _RequiredCastColumnTypeOperationTypeDef, _OptionalCastColumnTypeOperationTypeDef
):
    pass


ColumnDescriptionTypeDef = TypedDict("ColumnDescriptionTypeDef", {"Text": str}, total=False)

ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef", {"Name": str}, total=False
)

ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {"Name": str, "ColumnGroupColumnSchemaList": List["ColumnGroupColumnSchemaTypeDef"]},
    total=False,
)

ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef", {"GeoSpatialColumnGroup": "GeoSpatialColumnGroupTypeDef"}, total=False
)

ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {"Principals": List[str], "ColumnNames": List[str]},
    total=False,
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef", {"Name": str, "DataType": str, "GeographicRole": str}, total=False
)

ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ],
        "ColumnDescription": "ColumnDescriptionTypeDef",
    },
    total=False,
)

CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef", {"Columns": List["CalculatedColumnTypeDef"]}
)

_RequiredCredentialPairTypeDef = TypedDict(
    "_RequiredCredentialPairTypeDef", {"Username": str, "Password": str}
)
_OptionalCredentialPairTypeDef = TypedDict(
    "_OptionalCredentialPairTypeDef",
    {"AlternateDataSourceParameters": List["DataSourceParametersTypeDef"]},
    total=False,
)


class CredentialPairTypeDef(_RequiredCredentialPairTypeDef, _OptionalCredentialPairTypeDef):
    pass


_RequiredCustomSqlTypeDef = TypedDict(
    "_RequiredCustomSqlTypeDef", {"DataSourceArn": str, "Name": str, "SqlQuery": str}
)
_OptionalCustomSqlTypeDef = TypedDict(
    "_OptionalCustomSqlTypeDef", {"Columns": List["InputColumnTypeDef"]}, total=False
)


class CustomSqlTypeDef(_RequiredCustomSqlTypeDef, _OptionalCustomSqlTypeDef):
    pass


DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": Literal[
            "ACCESS_DENIED",
            "SOURCE_NOT_FOUND",
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_NOT_FOUND",
            "COLUMN_TYPE_MISMATCH",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
        ],
        "Message": str,
    },
    total=False,
)

DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {"DataSetReferences": List["DataSetReferenceTypeDef"], "Arn": str},
)

DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "Arn": str,
        "DashboardId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PublishedVersionNumber": int,
        "LastPublishedTime": datetime,
    },
    total=False,
)

DashboardTypeDef = TypedDict(
    "DashboardTypeDef",
    {
        "DashboardId": str,
        "Arn": str,
        "Name": str,
        "Version": "DashboardVersionTypeDef",
        "CreatedTime": datetime,
        "LastPublishedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)

DashboardVersionTypeDef = TypedDict(
    "DashboardVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List["DashboardErrorTypeDef"],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Arn": str,
        "SourceEntityArn": str,
        "DataSetArns": List[str],
        "Description": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {"Colors": List[str], "MinMaxGradient": List[str], "EmptyFillColor": str},
    total=False,
)

DataSetConfigurationTypeDef = TypedDict(
    "DataSetConfigurationTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": "DataSetSchemaTypeDef",
        "ColumnGroupSchemaList": List["ColumnGroupSchemaTypeDef"],
    },
    total=False,
)

DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef", {"DataSetPlaceholder": str, "DataSetArn": str}
)

DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef", {"ColumnSchemaList": List["ColumnSchemaTypeDef"]}, total=False
)

DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRulesApplied": bool,
    },
    total=False,
)

DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "OutputColumns": List["OutputColumnTypeDef"],
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
    },
    total=False,
)

DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": Literal[
            "ACCESS_DENIED",
            "COPY_SOURCE_NOT_FOUND",
            "TIMEOUT",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "UNKNOWN_HOST",
            "GENERIC_SQL_FAILURE",
            "CONFLICT",
            "UNKNOWN",
        ],
        "Message": str,
    },
    total=False,
)

DataSourceParametersTypeDef = TypedDict(
    "DataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": "AmazonElasticsearchParametersTypeDef",
        "AthenaParameters": "AthenaParametersTypeDef",
        "AuroraParameters": "AuroraParametersTypeDef",
        "AuroraPostgreSqlParameters": "AuroraPostgreSqlParametersTypeDef",
        "AwsIotAnalyticsParameters": "AwsIotAnalyticsParametersTypeDef",
        "JiraParameters": "JiraParametersTypeDef",
        "MariaDbParameters": "MariaDbParametersTypeDef",
        "MySqlParameters": "MySqlParametersTypeDef",
        "OracleParameters": "OracleParametersTypeDef",
        "PostgreSqlParameters": "PostgreSqlParametersTypeDef",
        "PrestoParameters": "PrestoParametersTypeDef",
        "RdsParameters": "RdsParametersTypeDef",
        "RedshiftParameters": "RedshiftParametersTypeDef",
        "S3Parameters": "S3ParametersTypeDef",
        "ServiceNowParameters": "ServiceNowParametersTypeDef",
        "SnowflakeParameters": "SnowflakeParametersTypeDef",
        "SparkParameters": "SparkParametersTypeDef",
        "SqlServerParameters": "SqlServerParametersTypeDef",
        "TeradataParameters": "TeradataParametersTypeDef",
        "TwitterParameters": "TwitterParametersTypeDef",
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": Literal[
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
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "ErrorInfo": "DataSourceErrorInfoTypeDef",
    },
    total=False,
)

DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef", {"Name": str, "Values": List[datetime]}
)

DecimalParameterTypeDef = TypedDict("DecimalParameterTypeDef", {"Name": str, "Values": List[float]})

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": Literal[
            "FAILURE_TO_ASSUME_ROLE",
            "INGESTION_SUPERSEDED",
            "INGESTION_CANCELED",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "S3_UPLOADED_FILE_DELETED",
            "S3_MANIFEST_ERROR",
            "DATA_TOLERANCE_EXCEPTION",
            "SPICE_TABLE_NOT_FOUND",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CUSTOMER_ERROR",
            "DATA_SOURCE_NOT_FOUND",
            "IAM_ROLE_NOT_AVAILABLE",
            "CONNECTION_FAILURE",
            "SQL_TABLE_NOT_FOUND",
            "PERMISSION_DENIED",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "OAUTH_TOKEN_FAILURE",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "INVALID_DATE_FORMAT",
            "INVALID_DATAPREP_SYNTAX",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SQL_INVALID_PARAMETER_VALUE",
            "QUERY_TIMEOUT",
            "SQL_NUMERIC_OVERFLOW",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
            "SQL_EXCEPTION",
            "S3_FILE_INACCESSIBLE",
            "IOT_FILE_NOT_FOUND",
            "IOT_DATA_SET_FILE_EMPTY",
            "INVALID_DATA_SOURCE_CONFIG",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "INTERNAL_SERVICE_ERROR",
        ],
        "Message": str,
    },
    total=False,
)

ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef", {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]}, total=False
)

FilterOperationTypeDef = TypedDict("FilterOperationTypeDef", {"ConditionExpression": str})

GeoSpatialColumnGroupTypeDef = TypedDict(
    "GeoSpatialColumnGroupTypeDef",
    {"Name": str, "CountryCode": Literal["US"], "Columns": List[str]},
)

GroupMemberTypeDef = TypedDict("GroupMemberTypeDef", {"Arn": str, "MemberName": str}, total=False)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

GutterStyleTypeDef = TypedDict("GutterStyleTypeDef", {"Show": bool}, total=False)

IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {"AssignmentName": str, "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"]},
    total=False,
)

IAMPolicyAssignmentTypeDef = TypedDict(
    "IAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentId": str,
        "AssignmentName": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
    },
    total=False,
)

_RequiredIngestionTypeDef = TypedDict(
    "_RequiredIngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "CreatedTime": datetime,
    },
)
_OptionalIngestionTypeDef = TypedDict(
    "_OptionalIngestionTypeDef",
    {
        "IngestionId": str,
        "ErrorInfo": "ErrorInfoTypeDef",
        "RowInfo": "RowInfoTypeDef",
        "QueueInfo": "QueueInfoTypeDef",
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": Literal["MANUAL", "SCHEDULED"],
        "RequestType": Literal["INITIAL_INGESTION", "EDIT", "INCREMENTAL_REFRESH", "FULL_REFRESH"],
    },
    total=False,
)


class IngestionTypeDef(_RequiredIngestionTypeDef, _OptionalIngestionTypeDef):
    pass


InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
)

IntegerParameterTypeDef = TypedDict("IntegerParameterTypeDef", {"Name": str, "Values": List[int]})

JiraParametersTypeDef = TypedDict("JiraParametersTypeDef", {"SiteBaseUrl": str})

JoinInstructionTypeDef = TypedDict(
    "JoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
)

LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {"JoinInstruction": "JoinInstructionTypeDef", "PhysicalTableId": str},
    total=False,
)

_RequiredLogicalTableTypeDef = TypedDict(
    "_RequiredLogicalTableTypeDef", {"Alias": str, "Source": "LogicalTableSourceTypeDef"}
)
_OptionalLogicalTableTypeDef = TypedDict(
    "_OptionalLogicalTableTypeDef",
    {"DataTransforms": List["TransformOperationTypeDef"]},
    total=False,
)


class LogicalTableTypeDef(_RequiredLogicalTableTypeDef, _OptionalLogicalTableTypeDef):
    pass


ManifestFileLocationTypeDef = TypedDict("ManifestFileLocationTypeDef", {"Bucket": str, "Key": str})

MarginStyleTypeDef = TypedDict("MarginStyleTypeDef", {"Show": bool}, total=False)

MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {"Type": Literal["PERMISSION_DENIED", "INTERNAL_SERVICE_ERROR"], "Message": str},
    total=False,
)

NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": str,
        "Arn": str,
        "CapacityRegion": str,
        "CreationStatus": Literal[
            "CREATED", "CREATING", "DELETING", "RETRYABLE_FAILURE", "NON_RETRYABLE_FAILURE"
        ],
        "IdentityStore": Literal["QUICKSIGHT"],
        "NamespaceError": "NamespaceErrorTypeDef",
    },
    total=False,
)

OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {"Name": str, "Description": str, "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"]},
    total=False,
)

PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": "RelationalTableTypeDef",
        "CustomSql": "CustomSqlTypeDef",
        "S3Source": "S3SourceTypeDef",
    },
    total=False,
)

PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef", {"Host": str, "Port": int, "Catalog": str}
)

ProjectOperationTypeDef = TypedDict("ProjectOperationTypeDef", {"ProjectedColumns": List[str]})

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef", {"WaitingOnIngestion": str, "QueuedIngestion": str}
)

RdsParametersTypeDef = TypedDict("RdsParametersTypeDef", {"InstanceId": str, "Database": str})

_RequiredRedshiftParametersTypeDef = TypedDict(
    "_RequiredRedshiftParametersTypeDef", {"Database": str}
)
_OptionalRedshiftParametersTypeDef = TypedDict(
    "_OptionalRedshiftParametersTypeDef", {"Host": str, "Port": int, "ClusterId": str}, total=False
)


class RedshiftParametersTypeDef(
    _RequiredRedshiftParametersTypeDef, _OptionalRedshiftParametersTypeDef
):
    pass


_RequiredRelationalTableTypeDef = TypedDict(
    "_RequiredRelationalTableTypeDef",
    {"DataSourceArn": str, "Name": str, "InputColumns": List["InputColumnTypeDef"]},
)
_OptionalRelationalTableTypeDef = TypedDict(
    "_OptionalRelationalTableTypeDef", {"Schema": str}, total=False
)


class RelationalTableTypeDef(_RequiredRelationalTableTypeDef, _OptionalRelationalTableTypeDef):
    pass


RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef", {"ColumnName": str, "NewColumnName": str}
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef", {"Principal": str, "Actions": List[str]}
)

RowInfoTypeDef = TypedDict("RowInfoTypeDef", {"RowsIngested": int, "RowsDropped": int}, total=False)

_RequiredRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredRowLevelPermissionDataSetTypeDef",
    {"Arn": str, "PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
)
_OptionalRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalRowLevelPermissionDataSetTypeDef", {"Namespace": str}, total=False
)


class RowLevelPermissionDataSetTypeDef(
    _RequiredRowLevelPermissionDataSetTypeDef, _OptionalRowLevelPermissionDataSetTypeDef
):
    pass


S3ParametersTypeDef = TypedDict(
    "S3ParametersTypeDef", {"ManifestFileLocation": "ManifestFileLocationTypeDef"}
)

_RequiredS3SourceTypeDef = TypedDict(
    "_RequiredS3SourceTypeDef", {"DataSourceArn": str, "InputColumns": List["InputColumnTypeDef"]}
)
_OptionalS3SourceTypeDef = TypedDict(
    "_OptionalS3SourceTypeDef", {"UploadSettings": "UploadSettingsTypeDef"}, total=False
)


class S3SourceTypeDef(_RequiredS3SourceTypeDef, _OptionalS3SourceTypeDef):
    pass


ServiceNowParametersTypeDef = TypedDict("ServiceNowParametersTypeDef", {"SiteBaseUrl": str})

SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef", {"VisibilityState": Literal["EXPANDED", "COLLAPSED"]}, total=False
)

SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {"Tile": "TileStyleTypeDef", "TileLayout": "TileLayoutStyleTypeDef"},
    total=False,
)

SheetTypeDef = TypedDict("SheetTypeDef", {"SheetId": str, "Name": str}, total=False)

SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef", {"Host": str, "Database": str, "Warehouse": str}
)

SparkParametersTypeDef = TypedDict("SparkParametersTypeDef", {"Host": str, "Port": int})

SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

SslPropertiesTypeDef = TypedDict("SslPropertiesTypeDef", {"DisableSsl": bool}, total=False)

StringParameterTypeDef = TypedDict("StringParameterTypeDef", {"Name": str, "Values": List[str]})

TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef", {"ColumnName": str, "Tags": List["ColumnTagTypeDef"]}
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)

TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": Literal[
            "SOURCE_NOT_FOUND", "DATA_SET_NOT_FOUND", "INTERNAL_FAILURE", "ACCESS_DENIED"
        ],
        "Message": str,
    },
    total=False,
)

TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {"Arn": str, "DataSetReferences": List["DataSetReferenceTypeDef"]},
)

TemplateSourceTemplateTypeDef = TypedDict("TemplateSourceTemplateTypeDef", {"Arn": str})

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": str,
        "TemplateId": str,
        "Name": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Version": "TemplateVersionTypeDef",
        "TemplateId": str,
        "LastUpdatedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Description": str,
    },
    total=False,
)

TemplateVersionTypeDef = TypedDict(
    "TemplateVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List["TemplateErrorTypeDef"],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "DataSetConfigurations": List["DataSetConfigurationTypeDef"],
        "Description": str,
        "SourceEntityArn": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef", {"Host": str, "Port": int, "Database": str}
)

ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef", {"Arn": str, "AliasName": str, "ThemeVersionNumber": int}, total=False
)

ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": "DataColorPaletteTypeDef",
        "UIColorPalette": "UIColorPaletteTypeDef",
        "Sheet": "SheetStyleTypeDef",
    },
    total=False,
)

ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef", {"Type": Literal["INTERNAL_FAILURE"], "Message": str}, total=False
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "Version": "ThemeVersionTypeDef",
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Type": Literal["QUICKSIGHT", "CUSTOM", "ALL"],
    },
    total=False,
)

ThemeVersionSummaryTypeDef = TypedDict(
    "ThemeVersionSummaryTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "CreatedTime": datetime,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
    },
    total=False,
)

ThemeVersionTypeDef = TypedDict(
    "ThemeVersionTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "BaseThemeId": str,
        "CreatedTime": datetime,
        "Configuration": "ThemeConfigurationTypeDef",
        "Errors": List["ThemeErrorTypeDef"],
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
    },
    total=False,
)

TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {"Gutter": "GutterStyleTypeDef", "Margin": "MarginStyleTypeDef"},
    total=False,
)

TileStyleTypeDef = TypedDict("TileStyleTypeDef", {"Border": "BorderStyleTypeDef"}, total=False)

TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": "ProjectOperationTypeDef",
        "FilterOperation": "FilterOperationTypeDef",
        "CreateColumnsOperation": "CreateColumnsOperationTypeDef",
        "RenameColumnOperation": "RenameColumnOperationTypeDef",
        "CastColumnTypeOperation": "CastColumnTypeOperationTypeDef",
        "TagColumnOperation": "TagColumnOperationTypeDef",
    },
    total=False,
)

TwitterParametersTypeDef = TypedDict("TwitterParametersTypeDef", {"Query": str, "MaxRows": int})

UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": str,
        "PrimaryBackground": str,
        "SecondaryForeground": str,
        "SecondaryBackground": str,
        "Accent": str,
        "AccentForeground": str,
        "Danger": str,
        "DangerForeground": str,
        "Warning": str,
        "WarningForeground": str,
        "Success": str,
        "SuccessForeground": str,
        "Dimension": str,
        "DimensionForeground": str,
        "Measure": str,
        "MeasureForeground": str,
    },
    total=False,
)

UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
        "CustomPermissionsName": str,
    },
    total=False,
)

VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef", {"VpcConnectionArn": str}
)

AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {"Operator": Literal["StringEquals"], "Name": Literal["QUICKSIGHT_USER"], "Value": str},
    total=False,
)

AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef", {"SourceTemplate": "AnalysisSourceTemplateTypeDef"}, total=False
)

CancelIngestionResponseTypeDef = TypedDict(
    "CancelIngestionResponseTypeDef",
    {"Arn": str, "IngestionId": str, "RequestId": str, "Status": int},
    total=False,
)

CreateAccountCustomizationResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateAnalysisResponseTypeDef = TypedDict(
    "CreateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {"GroupMember": "GroupMemberTypeDef", "RequestId": str, "Status": int},
    total=False,
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {"Group": "GroupTypeDef", "RequestId": str, "Status": int},
    total=False,
)

CreateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": Literal[
            "CREATED", "CREATING", "DELETING", "RETRYABLE_FAILURE", "NON_RETRYABLE_FAILURE"
        ],
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

CreateTemplateAliasResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseTypeDef",
    {"TemplateAlias": "TemplateAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

CreateThemeAliasResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseTypeDef",
    {"ThemeAlias": "ThemeAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": "AdHocFilteringOptionTypeDef",
        "ExportToCSVOption": "ExportToCSVOptionTypeDef",
        "SheetControlsOption": "SheetControlsOptionTypeDef",
    },
    total=False,
)

_RequiredDashboardSearchFilterTypeDef = TypedDict(
    "_RequiredDashboardSearchFilterTypeDef", {"Operator": Literal["StringEquals"]}
)
_OptionalDashboardSearchFilterTypeDef = TypedDict(
    "_OptionalDashboardSearchFilterTypeDef",
    {"Name": Literal["QUICKSIGHT_USER"], "Value": str},
    total=False,
)


class DashboardSearchFilterTypeDef(
    _RequiredDashboardSearchFilterTypeDef, _OptionalDashboardSearchFilterTypeDef
):
    pass


DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {"SourceTemplate": "DashboardSourceTemplateTypeDef"},
    total=False,
)

DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {"CredentialPair": "CredentialPairTypeDef", "CopySourceArn": str},
    total=False,
)

DeleteAccountCustomizationResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DeleteAnalysisResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseTypeDef",
    {"Status": int, "Arn": str, "AnalysisId": str, "DeletionTime": datetime, "RequestId": str},
    total=False,
)

DeleteDashboardResponseTypeDef = TypedDict(
    "DeleteDashboardResponseTypeDef",
    {"Status": int, "Arn": str, "DashboardId": str, "RequestId": str},
    total=False,
)

DeleteDataSetResponseTypeDef = TypedDict(
    "DeleteDataSetResponseTypeDef",
    {"Arn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {"Arn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)

DeleteGroupMembershipResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DeleteGroupResponseTypeDef = TypedDict(
    "DeleteGroupResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DeleteIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    {"AssignmentName": str, "RequestId": str, "Status": int},
    total=False,
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DeleteTemplateAliasResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseTypeDef",
    {"Status": int, "TemplateId": str, "AliasName": str, "Arn": str, "RequestId": str},
    total=False,
)

DeleteTemplateResponseTypeDef = TypedDict(
    "DeleteTemplateResponseTypeDef",
    {"RequestId": str, "Arn": str, "TemplateId": str, "Status": int},
    total=False,
)

DeleteThemeAliasResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseTypeDef",
    {"AliasName": str, "Arn": str, "RequestId": str, "Status": int, "ThemeId": str},
    total=False,
)

DeleteThemeResponseTypeDef = TypedDict(
    "DeleteThemeResponseTypeDef",
    {"Arn": str, "RequestId": str, "Status": int, "ThemeId": str},
    total=False,
)

DeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

DescribeAccountCustomizationResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {"AccountSettings": "AccountSettingsTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeAnalysisPermissionsResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

DescribeAnalysisResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseTypeDef",
    {"Analysis": "AnalysisTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {"Dashboard": "DashboardTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

DescribeDataSetResponseTypeDef = TypedDict(
    "DescribeDataSetResponseTypeDef",
    {"DataSet": "DataSetTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {"DataSource": "DataSourceTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {"Group": "GroupTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    {"IAMPolicyAssignment": "IAMPolicyAssignmentTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeIngestionResponseTypeDef = TypedDict(
    "DescribeIngestionResponseTypeDef",
    {"Ingestion": "IngestionTypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {"Namespace": "NamespaceInfoV2TypeDef", "RequestId": str, "Status": int},
    total=False,
)

DescribeTemplateAliasResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseTypeDef",
    {"TemplateAlias": "TemplateAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

DescribeTemplateResponseTypeDef = TypedDict(
    "DescribeTemplateResponseTypeDef",
    {"Template": "TemplateTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeThemeAliasResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseTypeDef",
    {"ThemeAlias": "ThemeAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeThemePermissionsResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

DescribeThemeResponseTypeDef = TypedDict(
    "DescribeThemeResponseTypeDef",
    {"Theme": "ThemeTypeDef", "Status": int, "RequestId": str},
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {"User": "UserTypeDef", "RequestId": str, "Status": int},
    total=False,
)

GetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseTypeDef",
    {"EmbedUrl": str, "Status": int, "RequestId": str},
    total=False,
)

GetSessionEmbedUrlResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseTypeDef",
    {"EmbedUrl": str, "Status": int, "RequestId": str},
    total=False,
)

ListAnalysesResponseTypeDef = TypedDict(
    "ListAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListDashboardVersionsResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List["DashboardVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List["DataSetSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {"DataSources": List["DataSourceTypeDef"], "NextToken": str, "RequestId": str, "Status": int},
    total=False,
)

ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List["GroupMemberTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {"GroupList": List["GroupTypeDef"], "NextToken": str, "RequestId": str, "Status": int},
    total=False,
)

ListIAMPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List["ActiveIAMPolicyAssignmentTypeDef"],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
    },
    total=False,
)

ListIAMPolicyAssignmentsResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List["IAMPolicyAssignmentSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {"Ingestions": List["IngestionTypeDef"], "NextToken": str, "RequestId": str, "Status": int},
    total=False,
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceInfoV2TypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "RequestId": str, "Status": int},
    total=False,
)

ListTemplateAliasesResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List["TemplateAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
    },
    total=False,
)

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List["TemplateVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List["TemplateSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListThemeAliasesResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseTypeDef",
    {
        "ThemeAliasList": List["ThemeAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
    },
    total=False,
)

ListThemeVersionsResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseTypeDef",
    {
        "ThemeVersionSummaryList": List["ThemeVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "ThemeSummaryList": List["ThemeSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ListUserGroupsResponseTypeDef = TypedDict(
    "ListUserGroupsResponseTypeDef",
    {"GroupList": List["GroupTypeDef"], "NextToken": str, "RequestId": str, "Status": int},
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"UserList": List["UserTypeDef"], "NextToken": str, "RequestId": str, "Status": int},
    total=False,
)

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "StringParameters": List["StringParameterTypeDef"],
        "IntegerParameters": List["IntegerParameterTypeDef"],
        "DecimalParameters": List["DecimalParameterTypeDef"],
        "DateTimeParameters": List["DateTimeParameterTypeDef"],
    },
    total=False,
)

RegisterUserResponseTypeDef = TypedDict(
    "RegisterUserResponseTypeDef",
    {"User": "UserTypeDef", "UserInvitationUrl": str, "RequestId": str, "Status": int},
    total=False,
)

RestoreAnalysisResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseTypeDef",
    {"Status": int, "Arn": str, "AnalysisId": str, "RequestId": str},
    total=False,
)

SearchAnalysesResponseTypeDef = TypedDict(
    "SearchAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

SearchDashboardsResponseTypeDef = TypedDict(
    "SearchDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": "TemplateSourceAnalysisTypeDef",
        "SourceTemplate": "TemplateSourceTemplateTypeDef",
    },
    total=False,
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

UpdateAccountCustomizationResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

UpdateAnalysisPermissionsResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateAnalysisResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

UpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseTypeDef",
    {"DashboardId": str, "DashboardArn": str, "Status": int, "RequestId": str},
    total=False,
)

UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

UpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseTypeDef",
    {"DataSetArn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseTypeDef",
    {"DataSourceArn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {"Group": "GroupTypeDef", "RequestId": str, "Status": int},
    total=False,
)

UpdateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateTemplateAliasResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseTypeDef",
    {"TemplateAlias": "TemplateAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

UpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateTemplateResponseTypeDef = TypedDict(
    "UpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

UpdateThemeAliasResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseTypeDef",
    {"ThemeAlias": "ThemeAliasTypeDef", "Status": int, "RequestId": str},
    total=False,
)

UpdateThemePermissionsResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
            "DELETED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {"User": "UserTypeDef", "RequestId": str, "Status": int},
    total=False,
)
