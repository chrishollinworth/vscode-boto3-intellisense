"""
Type annotations for quicksight service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/literals.html)

Usage::

    ```python
    from mypy_boto3_quicksight.literals import AnalysisErrorTypeType

    data: AnalysisErrorTypeType = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalysisErrorTypeType",
    "AnalysisFilterAttributeType",
    "AssignmentStatusType",
    "ColumnDataTypeType",
    "DashboardBehaviorType",
    "DashboardErrorTypeType",
    "DashboardFilterAttributeType",
    "DashboardUIStateType",
    "DataSetImportModeType",
    "DataSourceErrorInfoTypeType",
    "DataSourceTypeType",
    "EditionType",
    "EmbeddingIdentityTypeType",
    "FileFormatType",
    "FilterOperatorType",
    "FolderFilterAttributeType",
    "FolderTypeType",
    "GeoSpatialCountryCodeType",
    "GeoSpatialDataRoleType",
    "IdentityStoreType",
    "IdentityTypeType",
    "IngestionErrorTypeType",
    "IngestionRequestSourceType",
    "IngestionRequestTypeType",
    "IngestionStatusType",
    "InputColumnDataTypeType",
    "JoinTypeType",
    "ListAnalysesPaginatorName",
    "ListDashboardVersionsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListDataSetsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListIngestionsPaginatorName",
    "ListNamespacesPaginatorName",
    "ListTemplateAliasesPaginatorName",
    "ListTemplateVersionsPaginatorName",
    "ListTemplatesPaginatorName",
    "ListThemeVersionsPaginatorName",
    "ListThemesPaginatorName",
    "MemberTypeType",
    "NamespaceErrorTypeType",
    "NamespaceStatusType",
    "ResourceStatusType",
    "RowLevelPermissionFormatVersionType",
    "RowLevelPermissionPolicyType",
    "SearchAnalysesPaginatorName",
    "SearchDashboardsPaginatorName",
    "StatusType",
    "TemplateErrorTypeType",
    "TextQualifierType",
    "ThemeErrorTypeType",
    "ThemeTypeType",
    "UserRoleType",
)

AnalysisErrorTypeType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
AnalysisFilterAttributeType = Literal["QUICKSIGHT_USER"]
AssignmentStatusType = Literal["DISABLED", "DRAFT", "ENABLED"]
ColumnDataTypeType = Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"]
DashboardBehaviorType = Literal["DISABLED", "ENABLED"]
DashboardErrorTypeType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
DashboardFilterAttributeType = Literal["QUICKSIGHT_USER"]
DashboardUIStateType = Literal["COLLAPSED", "EXPANDED"]
DataSetImportModeType = Literal["DIRECT_QUERY", "SPICE"]
DataSourceErrorInfoTypeType = Literal[
    "ACCESS_DENIED",
    "CONFLICT",
    "COPY_SOURCE_NOT_FOUND",
    "ENGINE_VERSION_NOT_SUPPORTED",
    "GENERIC_SQL_FAILURE",
    "TIMEOUT",
    "UNKNOWN",
    "UNKNOWN_HOST",
]
DataSourceTypeType = Literal[
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
    "TIMESTREAM",
    "TWITTER",
]
EditionType = Literal["ENTERPRISE", "STANDARD"]
EmbeddingIdentityTypeType = Literal["ANONYMOUS", "IAM", "QUICKSIGHT"]
FileFormatType = Literal["CLF", "CSV", "ELF", "JSON", "TSV", "XLSX"]
FilterOperatorType = Literal["StringEquals"]
FolderFilterAttributeType = Literal["PARENT_FOLDER_ARN"]
FolderTypeType = Literal["SHARED"]
GeoSpatialCountryCodeType = Literal["US"]
GeoSpatialDataRoleType = Literal[
    "CITY", "COUNTRY", "COUNTY", "LATITUDE", "LONGITUDE", "POSTCODE", "STATE"
]
IdentityStoreType = Literal["QUICKSIGHT"]
IdentityTypeType = Literal["IAM", "QUICKSIGHT"]
IngestionErrorTypeType = Literal[
    "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
    "CONNECTION_FAILURE",
    "CUSTOMER_ERROR",
    "DATA_SET_DELETED",
    "DATA_SET_NOT_SPICE",
    "DATA_SET_SIZE_LIMIT_EXCEEDED",
    "DATA_SOURCE_AUTH_FAILED",
    "DATA_SOURCE_CONNECTION_FAILED",
    "DATA_SOURCE_NOT_FOUND",
    "DATA_TOLERANCE_EXCEPTION",
    "FAILURE_TO_ASSUME_ROLE",
    "FAILURE_TO_PROCESS_JSON_FILE",
    "IAM_ROLE_NOT_AVAILABLE",
    "INGESTION_CANCELED",
    "INGESTION_SUPERSEDED",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_DATAPREP_SYNTAX",
    "INVALID_DATA_SOURCE_CONFIG",
    "INVALID_DATE_FORMAT",
    "IOT_DATA_SET_FILE_EMPTY",
    "IOT_FILE_NOT_FOUND",
    "OAUTH_TOKEN_FAILURE",
    "PASSWORD_AUTHENTICATION_FAILURE",
    "PERMISSION_DENIED",
    "QUERY_TIMEOUT",
    "ROW_SIZE_LIMIT_EXCEEDED",
    "S3_FILE_INACCESSIBLE",
    "S3_MANIFEST_ERROR",
    "S3_UPLOADED_FILE_DELETED",
    "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
    "SOURCE_RESOURCE_LIMIT_EXCEEDED",
    "SPICE_TABLE_NOT_FOUND",
    "SQL_EXCEPTION",
    "SQL_INVALID_PARAMETER_VALUE",
    "SQL_NUMERIC_OVERFLOW",
    "SQL_SCHEMA_MISMATCH_ERROR",
    "SQL_TABLE_NOT_FOUND",
    "SSL_CERTIFICATE_VALIDATION_FAILURE",
    "UNRESOLVABLE_HOST",
    "UNROUTABLE_HOST",
]
IngestionRequestSourceType = Literal["MANUAL", "SCHEDULED"]
IngestionRequestTypeType = Literal[
    "EDIT", "FULL_REFRESH", "INCREMENTAL_REFRESH", "INITIAL_INGESTION"
]
IngestionStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "QUEUED", "RUNNING"
]
InputColumnDataTypeType = Literal[
    "BIT", "BOOLEAN", "DATETIME", "DECIMAL", "INTEGER", "JSON", "STRING"
]
JoinTypeType = Literal["INNER", "LEFT", "OUTER", "RIGHT"]
ListAnalysesPaginatorName = Literal["list_analyses"]
ListDashboardVersionsPaginatorName = Literal["list_dashboard_versions"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListIngestionsPaginatorName = Literal["list_ingestions"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListTemplateAliasesPaginatorName = Literal["list_template_aliases"]
ListTemplateVersionsPaginatorName = Literal["list_template_versions"]
ListTemplatesPaginatorName = Literal["list_templates"]
ListThemeVersionsPaginatorName = Literal["list_theme_versions"]
ListThemesPaginatorName = Literal["list_themes"]
MemberTypeType = Literal["ANALYSIS", "DASHBOARD", "DATASET"]
NamespaceErrorTypeType = Literal["INTERNAL_SERVICE_ERROR", "PERMISSION_DENIED"]
NamespaceStatusType = Literal[
    "CREATED", "CREATING", "DELETING", "NON_RETRYABLE_FAILURE", "RETRYABLE_FAILURE"
]
ResourceStatusType = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "DELETED",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
RowLevelPermissionFormatVersionType = Literal["VERSION_1", "VERSION_2"]
RowLevelPermissionPolicyType = Literal["DENY_ACCESS", "GRANT_ACCESS"]
SearchAnalysesPaginatorName = Literal["search_analyses"]
SearchDashboardsPaginatorName = Literal["search_dashboards"]
StatusType = Literal["DISABLED", "ENABLED"]
TemplateErrorTypeType = Literal[
    "ACCESS_DENIED", "DATA_SET_NOT_FOUND", "INTERNAL_FAILURE", "SOURCE_NOT_FOUND"
]
TextQualifierType = Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"]
ThemeErrorTypeType = Literal["INTERNAL_FAILURE"]
ThemeTypeType = Literal["ALL", "CUSTOM", "QUICKSIGHT"]
UserRoleType = Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"]
