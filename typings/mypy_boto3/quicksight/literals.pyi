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
    "AnchorOptionType",
    "ArcThicknessOptionsType",
    "ArcThicknessType",
    "AssignmentStatusType",
    "AuthenticationMethodOptionType",
    "AxisBindingType",
    "BarChartOrientationType",
    "BarsArrangementType",
    "BaseMapStyleTypeType",
    "BoxPlotFillStyleType",
    "CategoricalAggregationFunctionType",
    "CategoryFilterMatchOperatorType",
    "CategoryFilterSelectAllOptionsType",
    "ColorFillTypeType",
    "ColumnDataTypeType",
    "ColumnRoleType",
    "ColumnTagNameType",
    "ComparisonMethodType",
    "ConditionalFormattingIconDisplayOptionType",
    "ConditionalFormattingIconSetTypeType",
    "CrossDatasetTypesType",
    "CustomContentImageScalingConfigurationType",
    "CustomContentTypeType",
    "DashboardBehaviorType",
    "DashboardErrorTypeType",
    "DashboardFilterAttributeType",
    "DashboardUIStateType",
    "DataLabelContentType",
    "DataLabelOverlapType",
    "DataLabelPositionType",
    "DataSetFilterAttributeType",
    "DataSetImportModeType",
    "DataSourceErrorInfoTypeType",
    "DataSourceFilterAttributeType",
    "DataSourceTypeType",
    "DateAggregationFunctionType",
    "DayOfWeekType",
    "EditionType",
    "EmbeddingIdentityTypeType",
    "FileFormatType",
    "FilterNullOptionType",
    "FilterOperatorType",
    "FilterVisualScopeType",
    "FolderFilterAttributeType",
    "FolderTypeType",
    "FontDecorationType",
    "FontStyleType",
    "FontWeightNameType",
    "ForecastComputationSeasonalityType",
    "FunnelChartMeasureDataLabelStyleType",
    "GeoSpatialCountryCodeType",
    "GeoSpatialDataRoleType",
    "GeospatialSelectedPointStyleType",
    "GroupFilterAttributeType",
    "GroupFilterOperatorType",
    "HistogramBinTypeType",
    "HorizontalTextAlignmentType",
    "IconType",
    "IdentityStoreType",
    "IdentityTypeType",
    "IngestionErrorTypeType",
    "IngestionRequestSourceType",
    "IngestionRequestTypeType",
    "IngestionStatusType",
    "IngestionTypeType",
    "InputColumnDataTypeType",
    "JoinTypeType",
    "LayoutElementTypeType",
    "LegendPositionType",
    "LineChartLineStyleType",
    "LineChartMarkerShapeType",
    "LineChartTypeType",
    "LineInterpolationType",
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
    "LookbackWindowSizeUnitType",
    "MapZoomModeType",
    "MaximumMinimumComputationTypeType",
    "MemberTypeType",
    "MissingDataTreatmentOptionType",
    "NamespaceErrorTypeType",
    "NamespaceStatusType",
    "NegativeValueDisplayModeType",
    "NumberScaleType",
    "NumericEqualityMatchOperatorType",
    "NumericFilterSelectAllOptionsType",
    "NumericSeparatorSymbolType",
    "OtherCategoriesType",
    "PanelBorderStyleType",
    "PaperOrientationType",
    "PaperSizeType",
    "ParameterValueTypeType",
    "PivotTableConditionalFormattingScopeRoleType",
    "PivotTableMetricPlacementType",
    "PivotTableSubtotalLevelType",
    "PrimaryValueDisplayTypeType",
    "RadarChartShapeType",
    "ReferenceLineLabelHorizontalPositionType",
    "ReferenceLineLabelVerticalPositionType",
    "ReferenceLinePatternTypeType",
    "ReferenceLineValueLabelRelativePositionType",
    "RefreshIntervalType",
    "RelativeDateTypeType",
    "RelativeFontSizeType",
    "ResizeOptionType",
    "ResourceStatusType",
    "RowLevelPermissionFormatVersionType",
    "RowLevelPermissionPolicyType",
    "SearchAnalysesPaginatorName",
    "SearchDashboardsPaginatorName",
    "SearchDataSetsPaginatorName",
    "SearchDataSourcesPaginatorName",
    "SectionPageBreakStatusType",
    "SelectAllValueOptionsType",
    "SelectedFieldOptionsType",
    "SelectedTooltipTypeType",
    "SheetContentTypeType",
    "SheetControlDateTimePickerTypeType",
    "SheetControlListTypeType",
    "SheetControlSliderTypeType",
    "SimpleNumericalAggregationFunctionType",
    "SortDirectionType",
    "StatusType",
    "TableBorderStyleType",
    "TableCellImageScalingConfigurationType",
    "TableFieldIconSetTypeType",
    "TableOrientationType",
    "TableTotalsPlacementType",
    "TableTotalsScrollStatusType",
    "TargetVisualOptionsType",
    "TemplateErrorTypeType",
    "TextQualifierType",
    "TextWrapType",
    "ThemeErrorTypeType",
    "ThemeTypeType",
    "TimeGranularityType",
    "TooltipTitleTypeType",
    "TopBottomComputationTypeType",
    "TopBottomSortOrderType",
    "URLTargetConfigurationType",
    "UserRoleType",
    "ValueWhenUnsetOptionType",
    "VerticalTextAlignmentType",
    "VisibilityType",
    "VisualCustomActionTriggerType",
    "WidgetStatusType",
    "WordCloudCloudLayoutType",
    "WordCloudWordCasingType",
    "WordCloudWordOrientationType",
    "WordCloudWordPaddingType",
    "WordCloudWordScalingType",
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
AnalysisFilterAttributeType = Literal[
    "ANALYSIS_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
AnchorOptionType = Literal["NOW"]
ArcThicknessOptionsType = Literal["LARGE", "MEDIUM", "SMALL"]
ArcThicknessType = Literal["LARGE", "MEDIUM", "SMALL", "WHOLE"]
AssignmentStatusType = Literal["DISABLED", "DRAFT", "ENABLED"]
AuthenticationMethodOptionType = Literal["ACTIVE_DIRECTORY", "IAM_AND_QUICKSIGHT", "IAM_ONLY"]
AxisBindingType = Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"]
BarChartOrientationType = Literal["HORIZONTAL", "VERTICAL"]
BarsArrangementType = Literal["CLUSTERED", "STACKED", "STACKED_PERCENT"]
BaseMapStyleTypeType = Literal["DARK_GRAY", "IMAGERY", "LIGHT_GRAY", "STREET"]
BoxPlotFillStyleType = Literal["SOLID", "TRANSPARENT"]
CategoricalAggregationFunctionType = Literal["COUNT", "DISTINCT_COUNT"]
CategoryFilterMatchOperatorType = Literal[
    "CONTAINS", "DOES_NOT_CONTAIN", "DOES_NOT_EQUAL", "ENDS_WITH", "EQUALS", "STARTS_WITH"
]
CategoryFilterSelectAllOptionsType = Literal["FILTER_ALL_VALUES"]
ColorFillTypeType = Literal["DISCRETE", "GRADIENT"]
ColumnDataTypeType = Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"]
ColumnRoleType = Literal["DIMENSION", "MEASURE"]
ColumnTagNameType = Literal["COLUMN_DESCRIPTION", "COLUMN_GEOGRAPHIC_ROLE"]
ComparisonMethodType = Literal["DIFFERENCE", "PERCENT", "PERCENT_DIFFERENCE"]
ConditionalFormattingIconDisplayOptionType = Literal["ICON_ONLY"]
ConditionalFormattingIconSetTypeType = Literal[
    "BARS",
    "CARET_UP_MINUS_DOWN",
    "CHECK_X",
    "FLAGS",
    "FOUR_COLOR_ARROW",
    "FOUR_GRAY_ARROW",
    "PLUS_MINUS",
    "THREE_CIRCLE",
    "THREE_COLOR_ARROW",
    "THREE_GRAY_ARROW",
    "THREE_SHAPE",
]
CrossDatasetTypesType = Literal["ALL_DATASETS", "SINGLE_DATASET"]
CustomContentImageScalingConfigurationType = Literal[
    "DO_NOT_SCALE", "FIT_TO_HEIGHT", "FIT_TO_WIDTH", "SCALE_TO_VISUAL"
]
CustomContentTypeType = Literal["IMAGE", "OTHER_EMBEDDED_CONTENT"]
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
DashboardFilterAttributeType = Literal[
    "DASHBOARD_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
DashboardUIStateType = Literal["COLLAPSED", "EXPANDED"]
DataLabelContentType = Literal["PERCENT", "VALUE", "VALUE_AND_PERCENT"]
DataLabelOverlapType = Literal["DISABLE_OVERLAP", "ENABLE_OVERLAP"]
DataLabelPositionType = Literal["BOTTOM", "INSIDE", "LEFT", "OUTSIDE", "RIGHT", "TOP"]
DataSetFilterAttributeType = Literal[
    "DATASET_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
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
DataSourceFilterAttributeType = Literal[
    "DATASOURCE_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
]
DataSourceTypeType = Literal[
    "ADOBE_ANALYTICS",
    "AMAZON_ELASTICSEARCH",
    "AMAZON_OPENSEARCH",
    "ATHENA",
    "AURORA",
    "AURORA_POSTGRESQL",
    "AWS_IOT_ANALYTICS",
    "DATABRICKS",
    "EXASOL",
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
DateAggregationFunctionType = Literal["COUNT", "DISTINCT_COUNT", "MAX", "MIN"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
EditionType = Literal["ENTERPRISE", "ENTERPRISE_AND_Q", "STANDARD"]
EmbeddingIdentityTypeType = Literal["ANONYMOUS", "IAM", "QUICKSIGHT"]
FileFormatType = Literal["CLF", "CSV", "ELF", "JSON", "TSV", "XLSX"]
FilterNullOptionType = Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"]
FilterOperatorType = Literal["StringEquals", "StringLike"]
FilterVisualScopeType = Literal["ALL_VISUALS", "SELECTED_VISUALS"]
FolderFilterAttributeType = Literal[
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "FOLDER_NAME",
    "PARENT_FOLDER_ARN",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
]
FolderTypeType = Literal["SHARED"]
FontDecorationType = Literal["NONE", "UNDERLINE"]
FontStyleType = Literal["ITALIC", "NORMAL"]
FontWeightNameType = Literal["BOLD", "NORMAL"]
ForecastComputationSeasonalityType = Literal["AUTOMATIC", "CUSTOM"]
FunnelChartMeasureDataLabelStyleType = Literal[
    "PERCENTAGE_BY_FIRST_STAGE",
    "PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
    "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
    "VALUE_ONLY",
]
GeoSpatialCountryCodeType = Literal["US"]
GeoSpatialDataRoleType = Literal[
    "CITY", "COUNTRY", "COUNTY", "LATITUDE", "LONGITUDE", "POSTCODE", "STATE"
]
GeospatialSelectedPointStyleType = Literal["CLUSTER", "POINT"]
GroupFilterAttributeType = Literal["GROUP_NAME"]
GroupFilterOperatorType = Literal["StartsWith"]
HistogramBinTypeType = Literal["BIN_COUNT", "BIN_WIDTH"]
HorizontalTextAlignmentType = Literal["AUTO", "CENTER", "LEFT", "RIGHT"]
IconType = Literal[
    "ARROW_DOWN",
    "ARROW_DOWN_LEFT",
    "ARROW_DOWN_RIGHT",
    "ARROW_LEFT",
    "ARROW_RIGHT",
    "ARROW_UP",
    "ARROW_UP_LEFT",
    "ARROW_UP_RIGHT",
    "CARET_DOWN",
    "CARET_UP",
    "CHECKMARK",
    "CIRCLE",
    "FACE_DOWN",
    "FACE_FLAT",
    "FACE_UP",
    "FLAG",
    "MINUS",
    "ONE_BAR",
    "PLUS",
    "SQUARE",
    "THREE_BAR",
    "THUMBS_DOWN",
    "THUMBS_UP",
    "TRIANGLE",
    "TWO_BAR",
    "X",
]
IdentityStoreType = Literal["QUICKSIGHT"]
IdentityTypeType = Literal["IAM", "QUICKSIGHT"]
IngestionErrorTypeType = Literal[
    "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
    "CONNECTION_FAILURE",
    "CURSOR_NOT_ENABLED",
    "CUSTOMER_ERROR",
    "DATA_SET_DELETED",
    "DATA_SET_NOT_SPICE",
    "DATA_SET_SIZE_LIMIT_EXCEEDED",
    "DATA_SOURCE_AUTH_FAILED",
    "DATA_SOURCE_CONNECTION_FAILED",
    "DATA_SOURCE_NOT_FOUND",
    "DATA_TOLERANCE_EXCEPTION",
    "DUPLICATE_COLUMN_NAMES_FOUND",
    "ELASTICSEARCH_CURSOR_NOT_ENABLED",
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
    "PERMISSION_NOT_FOUND",
    "QUERY_TIMEOUT",
    "REFRESH_SUPPRESSED_BY_EDIT",
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
IngestionTypeType = Literal["FULL_REFRESH", "INCREMENTAL_REFRESH"]
InputColumnDataTypeType = Literal[
    "BIT", "BOOLEAN", "DATETIME", "DECIMAL", "INTEGER", "JSON", "STRING"
]
JoinTypeType = Literal["INNER", "LEFT", "OUTER", "RIGHT"]
LayoutElementTypeType = Literal["FILTER_CONTROL", "PARAMETER_CONTROL", "TEXT_BOX", "VISUAL"]
LegendPositionType = Literal["AUTO", "BOTTOM", "RIGHT", "TOP"]
LineChartLineStyleType = Literal["DASHED", "DOTTED", "SOLID"]
LineChartMarkerShapeType = Literal["CIRCLE", "DIAMOND", "ROUNDED_SQUARE", "SQUARE", "TRIANGLE"]
LineChartTypeType = Literal["AREA", "LINE", "STACKED_AREA"]
LineInterpolationType = Literal["LINEAR", "SMOOTH", "STEPPED"]
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
LookbackWindowSizeUnitType = Literal["DAY", "HOUR", "WEEK"]
MapZoomModeType = Literal["AUTO", "MANUAL"]
MaximumMinimumComputationTypeType = Literal["MAXIMUM", "MINIMUM"]
MemberTypeType = Literal["ANALYSIS", "DASHBOARD", "DATASET"]
MissingDataTreatmentOptionType = Literal["INTERPOLATE", "SHOW_AS_BLANK", "SHOW_AS_ZERO"]
NamespaceErrorTypeType = Literal["INTERNAL_SERVICE_ERROR", "PERMISSION_DENIED"]
NamespaceStatusType = Literal[
    "CREATED", "CREATING", "DELETING", "NON_RETRYABLE_FAILURE", "RETRYABLE_FAILURE"
]
NegativeValueDisplayModeType = Literal["NEGATIVE", "POSITIVE"]
NumberScaleType = Literal["AUTO", "BILLIONS", "MILLIONS", "NONE", "THOUSANDS", "TRILLIONS"]
NumericEqualityMatchOperatorType = Literal["DOES_NOT_EQUAL", "EQUALS"]
NumericFilterSelectAllOptionsType = Literal["FILTER_ALL_VALUES"]
NumericSeparatorSymbolType = Literal["COMMA", "DOT", "SPACE"]
OtherCategoriesType = Literal["EXCLUDE", "INCLUDE"]
PanelBorderStyleType = Literal["DASHED", "DOTTED", "SOLID"]
PaperOrientationType = Literal["LANDSCAPE", "PORTRAIT"]
PaperSizeType = Literal[
    "A0",
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "JIS_B4",
    "JIS_B5",
    "US_LEGAL",
    "US_LETTER",
    "US_TABLOID_LEDGER",
]
ParameterValueTypeType = Literal["MULTI_VALUED", "SINGLE_VALUED"]
PivotTableConditionalFormattingScopeRoleType = Literal["FIELD", "FIELD_TOTAL", "GRAND_TOTAL"]
PivotTableMetricPlacementType = Literal["COLUMN", "ROW"]
PivotTableSubtotalLevelType = Literal["ALL", "CUSTOM", "LAST"]
PrimaryValueDisplayTypeType = Literal["ACTUAL", "COMPARISON", "HIDDEN"]
RadarChartShapeType = Literal["CIRCLE", "POLYGON"]
ReferenceLineLabelHorizontalPositionType = Literal["CENTER", "LEFT", "RIGHT"]
ReferenceLineLabelVerticalPositionType = Literal["ABOVE", "BELOW"]
ReferenceLinePatternTypeType = Literal["DASHED", "DOTTED", "SOLID"]
ReferenceLineValueLabelRelativePositionType = Literal["AFTER_CUSTOM_LABEL", "BEFORE_CUSTOM_LABEL"]
RefreshIntervalType = Literal["DAILY", "HOURLY", "MINUTE15", "MINUTE30", "MONTHLY", "WEEKLY"]
RelativeDateTypeType = Literal["LAST", "NEXT", "NOW", "PREVIOUS", "THIS"]
RelativeFontSizeType = Literal["EXTRA_LARGE", "EXTRA_SMALL", "LARGE", "MEDIUM", "SMALL"]
ResizeOptionType = Literal["FIXED", "RESPONSIVE"]
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
SearchDataSetsPaginatorName = Literal["search_data_sets"]
SearchDataSourcesPaginatorName = Literal["search_data_sources"]
SectionPageBreakStatusType = Literal["DISABLED", "ENABLED"]
SelectAllValueOptionsType = Literal["ALL_VALUES"]
SelectedFieldOptionsType = Literal["ALL_FIELDS"]
SelectedTooltipTypeType = Literal["BASIC", "DETAILED"]
SheetContentTypeType = Literal["INTERACTIVE", "PAGINATED"]
SheetControlDateTimePickerTypeType = Literal["DATE_RANGE", "SINGLE_VALUED"]
SheetControlListTypeType = Literal["MULTI_SELECT", "SINGLE_SELECT"]
SheetControlSliderTypeType = Literal["RANGE", "SINGLE_POINT"]
SimpleNumericalAggregationFunctionType = Literal[
    "AVERAGE",
    "COUNT",
    "DISTINCT_COUNT",
    "MAX",
    "MEDIAN",
    "MIN",
    "STDEV",
    "STDEVP",
    "SUM",
    "VAR",
    "VARP",
]
SortDirectionType = Literal["ASC", "DESC"]
StatusType = Literal["DISABLED", "ENABLED"]
TableBorderStyleType = Literal["NONE", "SOLID"]
TableCellImageScalingConfigurationType = Literal[
    "DO_NOT_SCALE", "FIT_TO_CELL_HEIGHT", "FIT_TO_CELL_WIDTH"
]
TableFieldIconSetTypeType = Literal["LINK"]
TableOrientationType = Literal["HORIZONTAL", "VERTICAL"]
TableTotalsPlacementType = Literal["END", "START"]
TableTotalsScrollStatusType = Literal["PINNED", "SCROLLED"]
TargetVisualOptionsType = Literal["ALL_VISUALS"]
TemplateErrorTypeType = Literal[
    "ACCESS_DENIED", "DATA_SET_NOT_FOUND", "INTERNAL_FAILURE", "SOURCE_NOT_FOUND"
]
TextQualifierType = Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"]
TextWrapType = Literal["NONE", "WRAP"]
ThemeErrorTypeType = Literal["INTERNAL_FAILURE"]
ThemeTypeType = Literal["ALL", "CUSTOM", "QUICKSIGHT"]
TimeGranularityType = Literal[
    "DAY", "HOUR", "MILLISECOND", "MINUTE", "MONTH", "QUARTER", "SECOND", "WEEK", "YEAR"
]
TooltipTitleTypeType = Literal["NONE", "PRIMARY_VALUE"]
TopBottomComputationTypeType = Literal["BOTTOM", "TOP"]
TopBottomSortOrderType = Literal["ABSOLUTE_DIFFERENCE", "PERCENT_DIFFERENCE"]
URLTargetConfigurationType = Literal["NEW_TAB", "NEW_WINDOW", "SAME_TAB"]
UserRoleType = Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"]
ValueWhenUnsetOptionType = Literal["NULL", "RECOMMENDED_VALUE"]
VerticalTextAlignmentType = Literal["BOTTOM", "MIDDLE", "TOP"]
VisibilityType = Literal["HIDDEN", "VISIBLE"]
VisualCustomActionTriggerType = Literal["DATA_POINT_CLICK", "DATA_POINT_MENU"]
WidgetStatusType = Literal["DISABLED", "ENABLED"]
WordCloudCloudLayoutType = Literal["FLUID", "NORMAL"]
WordCloudWordCasingType = Literal["EXISTING_CASE", "LOWER_CASE"]
WordCloudWordOrientationType = Literal["HORIZONTAL", "HORIZONTAL_AND_VERTICAL"]
WordCloudWordPaddingType = Literal["LARGE", "MEDIUM", "NONE", "SMALL"]
WordCloudWordScalingType = Literal["EMPHASIZE", "NORMAL"]
