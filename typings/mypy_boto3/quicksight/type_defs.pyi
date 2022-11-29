"""
Type annotations for quicksight service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/type_defs.html)

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnalysisErrorTypeType,
    AnalysisFilterAttributeType,
    ArcThicknessOptionsType,
    ArcThicknessType,
    AssignmentStatusType,
    AuthenticationMethodOptionType,
    AxisBindingType,
    BarChartOrientationType,
    BarsArrangementType,
    BaseMapStyleTypeType,
    BoxPlotFillStyleType,
    CategoricalAggregationFunctionType,
    CategoryFilterMatchOperatorType,
    ColorFillTypeType,
    ColumnDataTypeType,
    ColumnRoleType,
    ColumnTagNameType,
    ComparisonMethodType,
    ConditionalFormattingIconSetTypeType,
    CrossDatasetTypesType,
    CustomContentImageScalingConfigurationType,
    CustomContentTypeType,
    DashboardBehaviorType,
    DashboardErrorTypeType,
    DashboardFilterAttributeType,
    DashboardUIStateType,
    DataLabelContentType,
    DataLabelOverlapType,
    DataLabelPositionType,
    DataSetFilterAttributeType,
    DataSetImportModeType,
    DataSourceErrorInfoTypeType,
    DataSourceFilterAttributeType,
    DataSourceTypeType,
    DateAggregationFunctionType,
    EditionType,
    EmbeddingIdentityTypeType,
    FileFormatType,
    FilterNullOptionType,
    FilterOperatorType,
    FilterVisualScopeType,
    FolderFilterAttributeType,
    FontDecorationType,
    FontStyleType,
    FontWeightNameType,
    ForecastComputationSeasonalityType,
    FunnelChartMeasureDataLabelStyleType,
    GeoSpatialDataRoleType,
    GeospatialSelectedPointStyleType,
    HistogramBinTypeType,
    HorizontalTextAlignmentType,
    IconType,
    IdentityTypeType,
    IngestionErrorTypeType,
    IngestionRequestSourceType,
    IngestionRequestTypeType,
    IngestionStatusType,
    IngestionTypeType,
    InputColumnDataTypeType,
    JoinTypeType,
    LayoutElementTypeType,
    LegendPositionType,
    LineChartLineStyleType,
    LineChartMarkerShapeType,
    LineChartTypeType,
    LineInterpolationType,
    MapZoomModeType,
    MaximumMinimumComputationTypeType,
    MemberTypeType,
    MissingDataTreatmentOptionType,
    NamespaceErrorTypeType,
    NamespaceStatusType,
    NegativeValueDisplayModeType,
    NumberScaleType,
    NumericEqualityMatchOperatorType,
    NumericSeparatorSymbolType,
    OtherCategoriesType,
    PanelBorderStyleType,
    PaperOrientationType,
    PaperSizeType,
    ParameterValueTypeType,
    PivotTableConditionalFormattingScopeRoleType,
    PivotTableMetricPlacementType,
    PivotTableSubtotalLevelType,
    PrimaryValueDisplayTypeType,
    ReferenceLineLabelHorizontalPositionType,
    ReferenceLineLabelVerticalPositionType,
    ReferenceLinePatternTypeType,
    ReferenceLineValueLabelRelativePositionType,
    RelativeDateTypeType,
    RelativeFontSizeType,
    ResizeOptionType,
    ResourceStatusType,
    RowLevelPermissionFormatVersionType,
    RowLevelPermissionPolicyType,
    SectionPageBreakStatusType,
    SelectedTooltipTypeType,
    SheetContentTypeType,
    SheetControlDateTimePickerTypeType,
    SheetControlListTypeType,
    SheetControlSliderTypeType,
    SimpleNumericalAggregationFunctionType,
    SortDirectionType,
    StatusType,
    TableBorderStyleType,
    TableCellImageScalingConfigurationType,
    TableOrientationType,
    TableTotalsPlacementType,
    TableTotalsScrollStatusType,
    TemplateErrorTypeType,
    TextQualifierType,
    TextWrapType,
    ThemeTypeType,
    TimeGranularityType,
    TooltipTitleTypeType,
    TopBottomComputationTypeType,
    TopBottomSortOrderType,
    URLTargetConfigurationType,
    UserRoleType,
    ValueWhenUnsetOptionType,
    VerticalTextAlignmentType,
    VisibilityType,
    VisualCustomActionTriggerType,
    WidgetStatusType,
    WordCloudCloudLayoutType,
    WordCloudWordCasingType,
    WordCloudWordOrientationType,
    WordCloudWordPaddingType,
    WordCloudWordScalingType,
)

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
    "AccountInfoTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AggregationFunctionTypeDef",
    "AggregationSortConfigurationTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AmazonOpenSearchParametersTypeDef",
    "AnalysisDefaultsTypeDef",
    "AnalysisDefinitionTypeDef",
    "AnalysisErrorTypeDef",
    "AnalysisSearchFilterTypeDef",
    "AnalysisSourceEntityTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "AnalysisSummaryTypeDef",
    "AnalysisTypeDef",
    "AnchorDateConfigurationTypeDef",
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    "ArcAxisConfigurationTypeDef",
    "ArcAxisDisplayRangeTypeDef",
    "ArcConfigurationTypeDef",
    "ArcOptionsTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "AxisDataOptionsTypeDef",
    "AxisDisplayMinMaxRangeTypeDef",
    "AxisDisplayOptionsTypeDef",
    "AxisDisplayRangeTypeDef",
    "AxisLabelOptionsTypeDef",
    "AxisLabelReferenceOptionsTypeDef",
    "AxisLinearScaleTypeDef",
    "AxisLogarithmicScaleTypeDef",
    "AxisScaleTypeDef",
    "AxisTickLabelOptionsTypeDef",
    "BarChartAggregatedFieldWellsTypeDef",
    "BarChartConfigurationTypeDef",
    "BarChartFieldWellsTypeDef",
    "BarChartSortConfigurationTypeDef",
    "BarChartVisualTypeDef",
    "BinCountOptionsTypeDef",
    "BinWidthOptionsTypeDef",
    "BodySectionConfigurationTypeDef",
    "BodySectionContentTypeDef",
    "BorderStyleTypeDef",
    "BoxPlotAggregatedFieldWellsTypeDef",
    "BoxPlotChartConfigurationTypeDef",
    "BoxPlotFieldWellsTypeDef",
    "BoxPlotOptionsTypeDef",
    "BoxPlotSortConfigurationTypeDef",
    "BoxPlotStyleOptionsTypeDef",
    "BoxPlotVisualTypeDef",
    "CalculatedColumnTypeDef",
    "CalculatedFieldTypeDef",
    "CalculatedMeasureFieldTypeDef",
    "CancelIngestionRequestRequestTypeDef",
    "CancelIngestionResponseTypeDef",
    "CascadingControlConfigurationTypeDef",
    "CascadingControlSourceTypeDef",
    "CastColumnTypeOperationTypeDef",
    "CategoricalDimensionFieldTypeDef",
    "CategoricalMeasureFieldTypeDef",
    "CategoryDrillDownFilterTypeDef",
    "CategoryFilterConfigurationTypeDef",
    "CategoryFilterTypeDef",
    "ChartAxisLabelOptionsTypeDef",
    "ClusterMarkerConfigurationTypeDef",
    "ClusterMarkerTypeDef",
    "ColorScaleTypeDef",
    "ColumnConfigurationTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupTypeDef",
    "ColumnHierarchyTypeDef",
    "ColumnIdentifierTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnSortTypeDef",
    "ColumnTagTypeDef",
    "ColumnTooltipItemTypeDef",
    "ComboChartAggregatedFieldWellsTypeDef",
    "ComboChartConfigurationTypeDef",
    "ComboChartFieldWellsTypeDef",
    "ComboChartSortConfigurationTypeDef",
    "ComboChartVisualTypeDef",
    "ComparisonConfigurationTypeDef",
    "ComparisonFormatConfigurationTypeDef",
    "ComputationTypeDef",
    "ConditionalFormattingColorTypeDef",
    "ConditionalFormattingCustomIconConditionTypeDef",
    "ConditionalFormattingCustomIconOptionsTypeDef",
    "ConditionalFormattingGradientColorTypeDef",
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    "ConditionalFormattingIconSetTypeDef",
    "ConditionalFormattingIconTypeDef",
    "ConditionalFormattingSolidColorTypeDef",
    "ContributionAnalysisDefaultTypeDef",
    "CreateAccountCustomizationRequestRequestTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAccountSubscriptionRequestRequestTypeDef",
    "CreateAccountSubscriptionResponseTypeDef",
    "CreateAnalysisRequestRequestTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateColumnsOperationTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFolderMembershipRequestRequestTypeDef",
    "CreateFolderMembershipResponseTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateTemplateAliasRequestRequestTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeAliasRequestRequestTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "CredentialPairTypeDef",
    "CurrencyDisplayFormatConfigurationTypeDef",
    "CustomActionFilterOperationTypeDef",
    "CustomActionNavigationOperationTypeDef",
    "CustomActionSetParametersOperationTypeDef",
    "CustomActionURLOperationTypeDef",
    "CustomContentConfigurationTypeDef",
    "CustomContentVisualTypeDef",
    "CustomFilterConfigurationTypeDef",
    "CustomFilterListConfigurationTypeDef",
    "CustomNarrativeOptionsTypeDef",
    "CustomParameterValuesTypeDef",
    "CustomSqlTypeDef",
    "CustomValuesConfigurationTypeDef",
    "DashboardErrorTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSourceEntityTypeDef",
    "DashboardSourceTemplateTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardTypeDef",
    "DashboardVersionDefinitionTypeDef",
    "DashboardVersionSummaryTypeDef",
    "DashboardVersionTypeDef",
    "DashboardVisualIdTypeDef",
    "DashboardVisualPublishOptionsTypeDef",
    "DataColorPaletteTypeDef",
    "DataColorTypeDef",
    "DataFieldSeriesItemTypeDef",
    "DataLabelOptionsTypeDef",
    "DataLabelTypeTypeDef",
    "DataPathColorTypeDef",
    "DataPathLabelTypeTypeDef",
    "DataPathSortTypeDef",
    "DataPathValueTypeDef",
    "DataSetConfigurationTypeDef",
    "DataSetIdentifierDeclarationTypeDef",
    "DataSetReferenceTypeDef",
    "DataSetSchemaTypeDef",
    "DataSetSearchFilterTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DataSetUsageConfigurationTypeDef",
    "DataSourceCredentialsTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DataSourceParametersTypeDef",
    "DataSourceSearchFilterTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceTypeDef",
    "DatabricksParametersTypeDef",
    "DateAxisOptionsTypeDef",
    "DateDimensionFieldTypeDef",
    "DateMeasureFieldTypeDef",
    "DateTimeDefaultValuesTypeDef",
    "DateTimeFormatConfigurationTypeDef",
    "DateTimeHierarchyTypeDef",
    "DateTimeParameterDeclarationTypeDef",
    "DateTimeParameterTypeDef",
    "DateTimePickerControlDisplayOptionsTypeDef",
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    "DecimalDefaultValuesTypeDef",
    "DecimalParameterDeclarationTypeDef",
    "DecimalParameterTypeDef",
    "DecimalPlacesConfigurationTypeDef",
    "DecimalValueWhenUnsetConfigurationTypeDef",
    "DefaultFreeFormLayoutConfigurationTypeDef",
    "DefaultGridLayoutConfigurationTypeDef",
    "DefaultInteractiveLayoutConfigurationTypeDef",
    "DefaultNewSheetConfigurationTypeDef",
    "DefaultPaginatedLayoutConfigurationTypeDef",
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    "DeleteAccountCustomizationRequestRequestTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    "DeleteAccountSubscriptionResponseTypeDef",
    "DeleteAnalysisRequestRequestTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteFolderMembershipRequestRequestTypeDef",
    "DeleteFolderMembershipResponseTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteFolderResponseTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteTemplateAliasRequestRequestTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasRequestRequestTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeAccountCustomizationRequestRequestTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsRequestRequestTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    "DescribeAccountSubscriptionResponseTypeDef",
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    "DescribeAnalysisDefinitionResponseTypeDef",
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeAnalysisRequestRequestTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DescribeDashboardDefinitionRequestRequestTypeDef",
    "DescribeDashboardDefinitionResponseTypeDef",
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSetRequestRequestTypeDef",
    "DescribeDataSetResponseTypeDef",
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeFolderPermissionsRequestRequestTypeDef",
    "DescribeFolderPermissionsResponseTypeDef",
    "DescribeFolderRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    "DescribeFolderResponseTypeDef",
    "DescribeGroupMembershipRequestRequestTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeIngestionRequestRequestTypeDef",
    "DescribeIngestionResponseTypeDef",
    "DescribeIpRestrictionRequestRequestTypeDef",
    "DescribeIpRestrictionResponseTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DescribeTemplateAliasRequestRequestTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "DescribeTemplateDefinitionRequestRequestTypeDef",
    "DescribeTemplateDefinitionResponseTypeDef",
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeTemplateRequestRequestTypeDef",
    "DescribeTemplateResponseTypeDef",
    "DescribeThemeAliasRequestRequestTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "DescribeThemePermissionsRequestRequestTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeThemeRequestRequestTypeDef",
    "DescribeThemeResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DestinationParameterValueConfigurationTypeDef",
    "DimensionFieldTypeDef",
    "DonutCenterOptionsTypeDef",
    "DonutOptionsTypeDef",
    "DrillDownFilterTypeDef",
    "DropDownControlDisplayOptionsTypeDef",
    "DynamicDefaultValueTypeDef",
    "EmptyVisualTypeDef",
    "EntityTypeDef",
    "ErrorInfoTypeDef",
    "ExasolParametersTypeDef",
    "ExcludePeriodConfigurationTypeDef",
    "ExplicitHierarchyTypeDef",
    "ExportHiddenFieldsOptionTypeDef",
    "ExportToCSVOptionTypeDef",
    "FieldBasedTooltipTypeDef",
    "FieldFolderTypeDef",
    "FieldLabelTypeTypeDef",
    "FieldSeriesItemTypeDef",
    "FieldSortOptionsTypeDef",
    "FieldSortTypeDef",
    "FieldTooltipItemTypeDef",
    "FilledMapAggregatedFieldWellsTypeDef",
    "FilledMapConditionalFormattingOptionTypeDef",
    "FilledMapConditionalFormattingTypeDef",
    "FilledMapConfigurationTypeDef",
    "FilledMapFieldWellsTypeDef",
    "FilledMapShapeConditionalFormattingTypeDef",
    "FilledMapSortConfigurationTypeDef",
    "FilledMapVisualTypeDef",
    "FilterControlTypeDef",
    "FilterDateTimePickerControlTypeDef",
    "FilterDropDownControlTypeDef",
    "FilterGroupTypeDef",
    "FilterListConfigurationTypeDef",
    "FilterListControlTypeDef",
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    "FilterOperationTargetVisualsConfigurationTypeDef",
    "FilterOperationTypeDef",
    "FilterRelativeDateTimeControlTypeDef",
    "FilterScopeConfigurationTypeDef",
    "FilterSelectableValuesTypeDef",
    "FilterSliderControlTypeDef",
    "FilterTextAreaControlTypeDef",
    "FilterTextFieldControlTypeDef",
    "FilterTypeDef",
    "FolderMemberTypeDef",
    "FolderSearchFilterTypeDef",
    "FolderSummaryTypeDef",
    "FolderTypeDef",
    "FontConfigurationTypeDef",
    "FontSizeTypeDef",
    "FontTypeDef",
    "FontWeightTypeDef",
    "ForecastComputationTypeDef",
    "ForecastConfigurationTypeDef",
    "ForecastScenarioTypeDef",
    "FormatConfigurationTypeDef",
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    "FreeFormLayoutConfigurationTypeDef",
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    "FreeFormLayoutElementBorderStyleTypeDef",
    "FreeFormLayoutElementTypeDef",
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    "FreeFormSectionLayoutConfigurationTypeDef",
    "FunnelChartAggregatedFieldWellsTypeDef",
    "FunnelChartConfigurationTypeDef",
    "FunnelChartDataLabelOptionsTypeDef",
    "FunnelChartFieldWellsTypeDef",
    "FunnelChartSortConfigurationTypeDef",
    "FunnelChartVisualTypeDef",
    "GaugeChartArcConditionalFormattingTypeDef",
    "GaugeChartConditionalFormattingOptionTypeDef",
    "GaugeChartConditionalFormattingTypeDef",
    "GaugeChartConfigurationTypeDef",
    "GaugeChartFieldWellsTypeDef",
    "GaugeChartOptionsTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    "GaugeChartVisualTypeDef",
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GeospatialCoordinateBoundsTypeDef",
    "GeospatialMapAggregatedFieldWellsTypeDef",
    "GeospatialMapConfigurationTypeDef",
    "GeospatialMapFieldWellsTypeDef",
    "GeospatialMapStyleOptionsTypeDef",
    "GeospatialMapVisualTypeDef",
    "GeospatialPointStyleOptionsTypeDef",
    "GeospatialWindowOptionsTypeDef",
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlRequestRequestTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "GlobalTableBorderOptionsTypeDef",
    "GradientColorTypeDef",
    "GradientStopTypeDef",
    "GridLayoutCanvasSizeOptionsTypeDef",
    "GridLayoutConfigurationTypeDef",
    "GridLayoutElementTypeDef",
    "GridLayoutScreenCanvasSizeOptionsTypeDef",
    "GroupMemberTypeDef",
    "GroupSearchFilterTypeDef",
    "GroupTypeDef",
    "GrowthRateComputationTypeDef",
    "GutterStyleTypeDef",
    "HeaderFooterSectionConfigurationTypeDef",
    "HeatMapAggregatedFieldWellsTypeDef",
    "HeatMapConfigurationTypeDef",
    "HeatMapFieldWellsTypeDef",
    "HeatMapSortConfigurationTypeDef",
    "HeatMapVisualTypeDef",
    "HistogramAggregatedFieldWellsTypeDef",
    "HistogramBinOptionsTypeDef",
    "HistogramConfigurationTypeDef",
    "HistogramFieldWellsTypeDef",
    "HistogramVisualTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "IngestionTypeDef",
    "InputColumnTypeDef",
    "InsightConfigurationTypeDef",
    "InsightVisualTypeDef",
    "IntegerDefaultValuesTypeDef",
    "IntegerParameterDeclarationTypeDef",
    "IntegerParameterTypeDef",
    "IntegerValueWhenUnsetConfigurationTypeDef",
    "ItemsLimitConfigurationTypeDef",
    "JiraParametersTypeDef",
    "JoinInstructionTypeDef",
    "JoinKeyPropertiesTypeDef",
    "KPIConditionalFormattingOptionTypeDef",
    "KPIConditionalFormattingTypeDef",
    "KPIConfigurationTypeDef",
    "KPIFieldWellsTypeDef",
    "KPIOptionsTypeDef",
    "KPIPrimaryValueConditionalFormattingTypeDef",
    "KPIProgressBarConditionalFormattingTypeDef",
    "KPISortConfigurationTypeDef",
    "KPIVisualTypeDef",
    "LabelOptionsTypeDef",
    "LayoutConfigurationTypeDef",
    "LayoutTypeDef",
    "LegendOptionsTypeDef",
    "LineChartAggregatedFieldWellsTypeDef",
    "LineChartConfigurationTypeDef",
    "LineChartDefaultSeriesSettingsTypeDef",
    "LineChartFieldWellsTypeDef",
    "LineChartLineStyleSettingsTypeDef",
    "LineChartMarkerStyleSettingsTypeDef",
    "LineChartSeriesSettingsTypeDef",
    "LineChartSortConfigurationTypeDef",
    "LineChartVisualTypeDef",
    "LineSeriesAxisDisplayOptionsTypeDef",
    "LinkSharingConfigurationTypeDef",
    "ListAnalysesRequestRequestTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListControlDisplayOptionsTypeDef",
    "ListControlSearchOptionsTypeDef",
    "ListControlSelectAllOptionsTypeDef",
    "ListDashboardVersionsRequestRequestTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFolderMembersRequestRequestTypeDef",
    "ListFolderMembersResponseTypeDef",
    "ListFoldersRequestRequestTypeDef",
    "ListFoldersResponseTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateAliasesRequestRequestTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeAliasesRequestRequestTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "ListThemeVersionsRequestRequestTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "ListUserGroupsRequestRequestTypeDef",
    "ListUserGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LoadingAnimationTypeDef",
    "LocalNavigationConfigurationTypeDef",
    "LogicalTableSourceTypeDef",
    "LogicalTableTypeDef",
    "LongFormatTextTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "MariaDbParametersTypeDef",
    "MaximumLabelTypeTypeDef",
    "MaximumMinimumComputationTypeDef",
    "MeasureFieldTypeDef",
    "MemberIdArnPairTypeDef",
    "MetricComparisonComputationTypeDef",
    "MinimumLabelTypeTypeDef",
    "MissingDataConfigurationTypeDef",
    "MySqlParametersTypeDef",
    "NamespaceErrorTypeDef",
    "NamespaceInfoV2TypeDef",
    "NegativeValueConfigurationTypeDef",
    "NullValueFormatConfigurationTypeDef",
    "NumberDisplayFormatConfigurationTypeDef",
    "NumberFormatConfigurationTypeDef",
    "NumericAxisOptionsTypeDef",
    "NumericEqualityDrillDownFilterTypeDef",
    "NumericEqualityFilterTypeDef",
    "NumericFormatConfigurationTypeDef",
    "NumericRangeFilterTypeDef",
    "NumericRangeFilterValueTypeDef",
    "NumericSeparatorConfigurationTypeDef",
    "NumericalAggregationFunctionTypeDef",
    "NumericalDimensionFieldTypeDef",
    "NumericalMeasureFieldTypeDef",
    "OracleParametersTypeDef",
    "OutputColumnTypeDef",
    "PaginationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PanelConfigurationTypeDef",
    "PanelTitleOptionsTypeDef",
    "ParameterControlTypeDef",
    "ParameterDateTimePickerControlTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterDropDownControlTypeDef",
    "ParameterListControlTypeDef",
    "ParameterSelectableValuesTypeDef",
    "ParameterSliderControlTypeDef",
    "ParameterTextAreaControlTypeDef",
    "ParameterTextFieldControlTypeDef",
    "ParametersTypeDef",
    "PercentVisibleRangeTypeDef",
    "PercentageDisplayFormatConfigurationTypeDef",
    "PercentileAggregationTypeDef",
    "PeriodOverPeriodComputationTypeDef",
    "PeriodToDateComputationTypeDef",
    "PhysicalTableTypeDef",
    "PieChartAggregatedFieldWellsTypeDef",
    "PieChartConfigurationTypeDef",
    "PieChartFieldWellsTypeDef",
    "PieChartSortConfigurationTypeDef",
    "PieChartVisualTypeDef",
    "PivotFieldSortOptionsTypeDef",
    "PivotTableAggregatedFieldWellsTypeDef",
    "PivotTableCellConditionalFormattingTypeDef",
    "PivotTableConditionalFormattingOptionTypeDef",
    "PivotTableConditionalFormattingScopeTypeDef",
    "PivotTableConditionalFormattingTypeDef",
    "PivotTableConfigurationTypeDef",
    "PivotTableDataPathOptionTypeDef",
    "PivotTableFieldOptionTypeDef",
    "PivotTableFieldOptionsTypeDef",
    "PivotTableFieldSubtotalOptionsTypeDef",
    "PivotTableFieldWellsTypeDef",
    "PivotTableOptionsTypeDef",
    "PivotTablePaginatedReportOptionsTypeDef",
    "PivotTableSortByTypeDef",
    "PivotTableSortConfigurationTypeDef",
    "PivotTableTotalOptionsTypeDef",
    "PivotTableVisualTypeDef",
    "PivotTotalOptionsTypeDef",
    "PostgreSqlParametersTypeDef",
    "PredefinedHierarchyTypeDef",
    "PrestoParametersTypeDef",
    "ProgressBarOptionsTypeDef",
    "ProjectOperationTypeDef",
    "QueueInfoTypeDef",
    "RangeEndsLabelTypeTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "ReferenceLineCustomLabelConfigurationTypeDef",
    "ReferenceLineDataConfigurationTypeDef",
    "ReferenceLineDynamicDataConfigurationTypeDef",
    "ReferenceLineLabelConfigurationTypeDef",
    "ReferenceLineStaticDataConfigurationTypeDef",
    "ReferenceLineStyleConfigurationTypeDef",
    "ReferenceLineTypeDef",
    "ReferenceLineValueLabelConfigurationTypeDef",
    "RegisterUserRequestRequestTypeDef",
    "RegisterUserResponseTypeDef",
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    "RelationalTableTypeDef",
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    "RelativeDatesFilterTypeDef",
    "RenameColumnOperationTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAnalysisRequestRequestTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "RollingDateConfigurationTypeDef",
    "RowAlternateColorOptionsTypeDef",
    "RowInfoTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "RowLevelPermissionTagConfigurationTypeDef",
    "RowLevelPermissionTagRuleTypeDef",
    "S3ParametersTypeDef",
    "S3SourceTypeDef",
    "SameSheetTargetVisualConfigurationTypeDef",
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    "SankeyDiagramChartConfigurationTypeDef",
    "SankeyDiagramFieldWellsTypeDef",
    "SankeyDiagramSortConfigurationTypeDef",
    "SankeyDiagramVisualTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    "ScatterPlotConfigurationTypeDef",
    "ScatterPlotFieldWellsTypeDef",
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    "ScatterPlotVisualTypeDef",
    "ScrollBarOptionsTypeDef",
    "SearchAnalysesRequestRequestTypeDef",
    "SearchAnalysesResponseTypeDef",
    "SearchDashboardsRequestRequestTypeDef",
    "SearchDashboardsResponseTypeDef",
    "SearchDataSetsRequestRequestTypeDef",
    "SearchDataSetsResponseTypeDef",
    "SearchDataSourcesRequestRequestTypeDef",
    "SearchDataSourcesResponseTypeDef",
    "SearchFoldersRequestRequestTypeDef",
    "SearchFoldersResponseTypeDef",
    "SearchGroupsRequestRequestTypeDef",
    "SearchGroupsResponseTypeDef",
    "SecondaryValueOptionsTypeDef",
    "SectionAfterPageBreakTypeDef",
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    "SectionBasedLayoutConfigurationTypeDef",
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    "SectionLayoutConfigurationTypeDef",
    "SectionPageBreakConfigurationTypeDef",
    "SectionStyleTypeDef",
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    "SeriesItemTypeDef",
    "ServiceNowParametersTypeDef",
    "SessionTagTypeDef",
    "SetParameterValueConfigurationTypeDef",
    "ShapeConditionalFormatTypeDef",
    "SheetControlLayoutConfigurationTypeDef",
    "SheetControlLayoutTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetDefinitionTypeDef",
    "SheetElementConfigurationOverridesTypeDef",
    "SheetElementRenderingRuleTypeDef",
    "SheetStyleTypeDef",
    "SheetTextBoxTypeDef",
    "SheetTypeDef",
    "SheetVisualScopingConfigurationTypeDef",
    "ShortFormatTextTypeDef",
    "SignupResponseTypeDef",
    "SimpleClusterMarkerTypeDef",
    "SliderControlDisplayOptionsTypeDef",
    "SmallMultiplesOptionsTypeDef",
    "SnowflakeParametersTypeDef",
    "SpacingTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "SslPropertiesTypeDef",
    "StringDefaultValuesTypeDef",
    "StringFormatConfigurationTypeDef",
    "StringParameterDeclarationTypeDef",
    "StringParameterTypeDef",
    "StringValueWhenUnsetConfigurationTypeDef",
    "SubtotalOptionsTypeDef",
    "TableAggregatedFieldWellsTypeDef",
    "TableBorderOptionsTypeDef",
    "TableCellConditionalFormattingTypeDef",
    "TableCellImageSizingConfigurationTypeDef",
    "TableCellStyleTypeDef",
    "TableConditionalFormattingOptionTypeDef",
    "TableConditionalFormattingTypeDef",
    "TableConfigurationTypeDef",
    "TableFieldCustomIconContentTypeDef",
    "TableFieldCustomTextContentTypeDef",
    "TableFieldImageConfigurationTypeDef",
    "TableFieldLinkConfigurationTypeDef",
    "TableFieldLinkContentConfigurationTypeDef",
    "TableFieldOptionTypeDef",
    "TableFieldOptionsTypeDef",
    "TableFieldURLConfigurationTypeDef",
    "TableFieldWellsTypeDef",
    "TableOptionsTypeDef",
    "TablePaginatedReportOptionsTypeDef",
    "TableRowConditionalFormattingTypeDef",
    "TableSideBorderOptionsTypeDef",
    "TableSortConfigurationTypeDef",
    "TableUnaggregatedFieldWellsTypeDef",
    "TableVisualTypeDef",
    "TagColumnOperationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "TemplateAliasTypeDef",
    "TemplateErrorTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "TemplateSourceEntityTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateVersionDefinitionTypeDef",
    "TemplateVersionSummaryTypeDef",
    "TemplateVersionTypeDef",
    "TeradataParametersTypeDef",
    "TextAreaControlDisplayOptionsTypeDef",
    "TextConditionalFormatTypeDef",
    "TextControlPlaceholderOptionsTypeDef",
    "TextFieldControlDisplayOptionsTypeDef",
    "ThemeAliasTypeDef",
    "ThemeConfigurationTypeDef",
    "ThemeErrorTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ThemeVersionTypeDef",
    "ThousandSeparatorOptionsTypeDef",
    "TileLayoutStyleTypeDef",
    "TileStyleTypeDef",
    "TimeBasedForecastPropertiesTypeDef",
    "TimeEqualityFilterTypeDef",
    "TimeRangeDrillDownFilterTypeDef",
    "TimeRangeFilterTypeDef",
    "TimeRangeFilterValueTypeDef",
    "TooltipItemTypeDef",
    "TooltipOptionsTypeDef",
    "TopBottomFilterTypeDef",
    "TopBottomMoversComputationTypeDef",
    "TopBottomRankedComputationTypeDef",
    "TotalAggregationComputationTypeDef",
    "TotalOptionsTypeDef",
    "TransformOperationTypeDef",
    "TreeMapAggregatedFieldWellsTypeDef",
    "TreeMapConfigurationTypeDef",
    "TreeMapFieldWellsTypeDef",
    "TreeMapSortConfigurationTypeDef",
    "TreeMapVisualTypeDef",
    "TrendArrowOptionsTypeDef",
    "TwitterParametersTypeDef",
    "TypographyTypeDef",
    "UIColorPaletteTypeDef",
    "UnaggregatedFieldTypeDef",
    "UniqueValuesComputationTypeDef",
    "UntagColumnOperationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationRequestRequestTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateAnalysisRequestRequestTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFolderPermissionsRequestRequestTypeDef",
    "UpdateFolderPermissionsResponseTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "UpdateFolderResponseTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateIpRestrictionRequestRequestTypeDef",
    "UpdateIpRestrictionResponseTypeDef",
    "UpdatePublicSharingSettingsRequestRequestTypeDef",
    "UpdatePublicSharingSettingsResponseTypeDef",
    "UpdateTemplateAliasRequestRequestTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeAliasRequestRequestTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "UpdateThemePermissionsRequestRequestTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadSettingsTypeDef",
    "UserTypeDef",
    "VisibleRangeOptionsTypeDef",
    "VisualCustomActionOperationTypeDef",
    "VisualCustomActionTypeDef",
    "VisualPaletteTypeDef",
    "VisualSubtitleLabelOptionsTypeDef",
    "VisualTitleLabelOptionsTypeDef",
    "VisualTypeDef",
    "VpcConnectionPropertiesTypeDef",
    "WaterfallChartAggregatedFieldWellsTypeDef",
    "WaterfallChartConfigurationTypeDef",
    "WaterfallChartFieldWellsTypeDef",
    "WaterfallChartOptionsTypeDef",
    "WaterfallChartSortConfigurationTypeDef",
    "WaterfallVisualTypeDef",
    "WhatIfPointScenarioTypeDef",
    "WhatIfRangeScenarioTypeDef",
    "WordCloudAggregatedFieldWellsTypeDef",
    "WordCloudChartConfigurationTypeDef",
    "WordCloudFieldWellsTypeDef",
    "WordCloudOptionsTypeDef",
    "WordCloudSortConfigurationTypeDef",
    "WordCloudVisualTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef",
    {
        "DefaultTheme": str,
        "DefaultEmailCustomizationTemplate": str,
    },
    total=False,
)

AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef",
    {
        "AccountName": str,
        "Edition": EditionType,
        "NotificationEmail": str,
        "AuthenticationType": str,
        "AccountSubscriptionStatus": str,
    },
    total=False,
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": str,
        "Edition": EditionType,
        "DefaultNamespace": str,
        "NotificationEmail": str,
        "PublicSharingEnabled": bool,
        "TerminationProtectionEnabled": bool,
    },
    total=False,
)

ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef",
    {
        "AssignmentName": str,
        "PolicyArn": str,
    },
    total=False,
)

AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

AggregationFunctionTypeDef = TypedDict(
    "AggregationFunctionTypeDef",
    {
        "NumericalAggregationFunction": "NumericalAggregationFunctionTypeDef",
        "CategoricalAggregationFunction": CategoricalAggregationFunctionType,
        "DateAggregationFunction": DateAggregationFunctionType,
    },
    total=False,
)

AggregationSortConfigurationTypeDef = TypedDict(
    "AggregationSortConfigurationTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
        "SortDirection": SortDirectionType,
        "AggregationFunction": "AggregationFunctionTypeDef",
    },
)

AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AmazonOpenSearchParametersTypeDef = TypedDict(
    "AmazonOpenSearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AnalysisDefaultsTypeDef = TypedDict(
    "AnalysisDefaultsTypeDef",
    {
        "DefaultNewSheetConfiguration": "DefaultNewSheetConfigurationTypeDef",
    },
)

_RequiredAnalysisDefinitionTypeDef = TypedDict(
    "_RequiredAnalysisDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": List["DataSetIdentifierDeclarationTypeDef"],
    },
)
_OptionalAnalysisDefinitionTypeDef = TypedDict(
    "_OptionalAnalysisDefinitionTypeDef",
    {
        "Sheets": List["SheetDefinitionTypeDef"],
        "CalculatedFields": List["CalculatedFieldTypeDef"],
        "ParameterDeclarations": List["ParameterDeclarationTypeDef"],
        "FilterGroups": List["FilterGroupTypeDef"],
        "ColumnConfigurations": List["ColumnConfigurationTypeDef"],
        "AnalysisDefaults": "AnalysisDefaultsTypeDef",
    },
    total=False,
)

class AnalysisDefinitionTypeDef(
    _RequiredAnalysisDefinitionTypeDef, _OptionalAnalysisDefinitionTypeDef
):
    pass

AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": AnalysisErrorTypeType,
        "Message": str,
        "ViolatedEntities": List["EntityTypeDef"],
    },
    total=False,
)

AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": AnalysisFilterAttributeType,
        "Value": str,
    },
    total=False,
)

AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef",
    {
        "SourceTemplate": "AnalysisSourceTemplateTypeDef",
    },
    total=False,
)

AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {
        "DataSetReferences": List["DataSetReferenceTypeDef"],
        "Arn": str,
    },
)

AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "Name": str,
        "Status": ResourceStatusType,
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
        "Status": ResourceStatusType,
        "Errors": List["AnalysisErrorTypeDef"],
        "DataSetArns": List[str],
        "ThemeArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

AnchorDateConfigurationTypeDef = TypedDict(
    "AnchorDateConfigurationTypeDef",
    {
        "AnchorOption": Literal["NOW"],
        "ParameterName": str,
    },
    total=False,
)

AnonymousUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)

AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": "DashboardVisualIdTypeDef",
    },
)

AnonymousUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
        "DashboardVisual": "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
        "QSearchBar": "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    },
    total=False,
)

AnonymousUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
)

ArcAxisConfigurationTypeDef = TypedDict(
    "ArcAxisConfigurationTypeDef",
    {
        "Range": "ArcAxisDisplayRangeTypeDef",
        "ReserveRange": int,
    },
    total=False,
)

ArcAxisDisplayRangeTypeDef = TypedDict(
    "ArcAxisDisplayRangeTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

ArcConfigurationTypeDef = TypedDict(
    "ArcConfigurationTypeDef",
    {
        "ArcAngle": float,
        "ArcThickness": ArcThicknessOptionsType,
    },
    total=False,
)

ArcOptionsTypeDef = TypedDict(
    "ArcOptionsTypeDef",
    {
        "ArcThickness": ArcThicknessType,
    },
    total=False,
)

AthenaParametersTypeDef = TypedDict(
    "AthenaParametersTypeDef",
    {
        "WorkGroup": str,
        "RoleArn": str,
    },
    total=False,
)

AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef",
    {
        "DataSetName": str,
    },
)

AxisDataOptionsTypeDef = TypedDict(
    "AxisDataOptionsTypeDef",
    {
        "NumericAxisOptions": "NumericAxisOptionsTypeDef",
        "DateAxisOptions": "DateAxisOptionsTypeDef",
    },
    total=False,
)

AxisDisplayMinMaxRangeTypeDef = TypedDict(
    "AxisDisplayMinMaxRangeTypeDef",
    {
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)

AxisDisplayOptionsTypeDef = TypedDict(
    "AxisDisplayOptionsTypeDef",
    {
        "TickLabelOptions": "AxisTickLabelOptionsTypeDef",
        "AxisLineVisibility": VisibilityType,
        "GridLineVisibility": VisibilityType,
        "DataOptions": "AxisDataOptionsTypeDef",
        "ScrollbarOptions": "ScrollBarOptionsTypeDef",
        "AxisOffset": str,
    },
    total=False,
)

AxisDisplayRangeTypeDef = TypedDict(
    "AxisDisplayRangeTypeDef",
    {
        "MinMax": "AxisDisplayMinMaxRangeTypeDef",
        "DataDriven": Dict[str, Any],
    },
    total=False,
)

AxisLabelOptionsTypeDef = TypedDict(
    "AxisLabelOptionsTypeDef",
    {
        "FontConfiguration": "FontConfigurationTypeDef",
        "CustomLabel": str,
        "ApplyTo": "AxisLabelReferenceOptionsTypeDef",
    },
    total=False,
)

AxisLabelReferenceOptionsTypeDef = TypedDict(
    "AxisLabelReferenceOptionsTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)

AxisLinearScaleTypeDef = TypedDict(
    "AxisLinearScaleTypeDef",
    {
        "StepCount": int,
        "StepSize": float,
    },
    total=False,
)

AxisLogarithmicScaleTypeDef = TypedDict(
    "AxisLogarithmicScaleTypeDef",
    {
        "Base": float,
    },
    total=False,
)

AxisScaleTypeDef = TypedDict(
    "AxisScaleTypeDef",
    {
        "Linear": "AxisLinearScaleTypeDef",
        "Logarithmic": "AxisLogarithmicScaleTypeDef",
    },
    total=False,
)

AxisTickLabelOptionsTypeDef = TypedDict(
    "AxisTickLabelOptionsTypeDef",
    {
        "LabelOptions": "LabelOptionsTypeDef",
        "RotationAngle": float,
    },
    total=False,
)

BarChartAggregatedFieldWellsTypeDef = TypedDict(
    "BarChartAggregatedFieldWellsTypeDef",
    {
        "Category": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
        "Colors": List["DimensionFieldTypeDef"],
        "SmallMultiples": List["DimensionFieldTypeDef"],
    },
    total=False,
)

BarChartConfigurationTypeDef = TypedDict(
    "BarChartConfigurationTypeDef",
    {
        "FieldWells": "BarChartFieldWellsTypeDef",
        "SortConfiguration": "BarChartSortConfigurationTypeDef",
        "Orientation": BarChartOrientationType,
        "BarsArrangement": BarsArrangementType,
        "VisualPalette": "VisualPaletteTypeDef",
        "SmallMultiplesOptions": "SmallMultiplesOptionsTypeDef",
        "CategoryAxis": "AxisDisplayOptionsTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ValueAxis": "AxisDisplayOptionsTypeDef",
        "ValueLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColorLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "ReferenceLines": List["ReferenceLineTypeDef"],
        "ContributionAnalysisDefaults": List["ContributionAnalysisDefaultTypeDef"],
    },
    total=False,
)

BarChartFieldWellsTypeDef = TypedDict(
    "BarChartFieldWellsTypeDef",
    {
        "BarChartAggregatedFieldWells": "BarChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

BarChartSortConfigurationTypeDef = TypedDict(
    "BarChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "CategoryItemsLimit": "ItemsLimitConfigurationTypeDef",
        "ColorSort": List["FieldSortOptionsTypeDef"],
        "ColorItemsLimit": "ItemsLimitConfigurationTypeDef",
        "SmallMultiplesSort": List["FieldSortOptionsTypeDef"],
        "SmallMultiplesLimitConfiguration": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredBarChartVisualTypeDef = TypedDict(
    "_RequiredBarChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBarChartVisualTypeDef = TypedDict(
    "_OptionalBarChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "BarChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class BarChartVisualTypeDef(_RequiredBarChartVisualTypeDef, _OptionalBarChartVisualTypeDef):
    pass

BinCountOptionsTypeDef = TypedDict(
    "BinCountOptionsTypeDef",
    {
        "Value": int,
    },
    total=False,
)

BinWidthOptionsTypeDef = TypedDict(
    "BinWidthOptionsTypeDef",
    {
        "Value": float,
        "BinCountLimit": int,
    },
    total=False,
)

_RequiredBodySectionConfigurationTypeDef = TypedDict(
    "_RequiredBodySectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Content": "BodySectionContentTypeDef",
    },
)
_OptionalBodySectionConfigurationTypeDef = TypedDict(
    "_OptionalBodySectionConfigurationTypeDef",
    {
        "Style": "SectionStyleTypeDef",
        "PageBreakConfiguration": "SectionPageBreakConfigurationTypeDef",
    },
    total=False,
)

class BodySectionConfigurationTypeDef(
    _RequiredBodySectionConfigurationTypeDef, _OptionalBodySectionConfigurationTypeDef
):
    pass

BodySectionContentTypeDef = TypedDict(
    "BodySectionContentTypeDef",
    {
        "Layout": "SectionLayoutConfigurationTypeDef",
    },
    total=False,
)

BorderStyleTypeDef = TypedDict(
    "BorderStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

BoxPlotAggregatedFieldWellsTypeDef = TypedDict(
    "BoxPlotAggregatedFieldWellsTypeDef",
    {
        "GroupBy": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

BoxPlotChartConfigurationTypeDef = TypedDict(
    "BoxPlotChartConfigurationTypeDef",
    {
        "FieldWells": "BoxPlotFieldWellsTypeDef",
        "SortConfiguration": "BoxPlotSortConfigurationTypeDef",
        "BoxPlotOptions": "BoxPlotOptionsTypeDef",
        "CategoryAxis": "AxisDisplayOptionsTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "PrimaryYAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "PrimaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "ReferenceLines": List["ReferenceLineTypeDef"],
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

BoxPlotFieldWellsTypeDef = TypedDict(
    "BoxPlotFieldWellsTypeDef",
    {
        "BoxPlotAggregatedFieldWells": "BoxPlotAggregatedFieldWellsTypeDef",
    },
    total=False,
)

BoxPlotOptionsTypeDef = TypedDict(
    "BoxPlotOptionsTypeDef",
    {
        "StyleOptions": "BoxPlotStyleOptionsTypeDef",
        "OutlierVisibility": VisibilityType,
        "AllDataPointsVisibility": VisibilityType,
    },
    total=False,
)

BoxPlotSortConfigurationTypeDef = TypedDict(
    "BoxPlotSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "PaginationConfiguration": "PaginationConfigurationTypeDef",
    },
    total=False,
)

BoxPlotStyleOptionsTypeDef = TypedDict(
    "BoxPlotStyleOptionsTypeDef",
    {
        "FillStyle": BoxPlotFillStyleType,
    },
    total=False,
)

_RequiredBoxPlotVisualTypeDef = TypedDict(
    "_RequiredBoxPlotVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBoxPlotVisualTypeDef = TypedDict(
    "_OptionalBoxPlotVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "BoxPlotChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class BoxPlotVisualTypeDef(_RequiredBoxPlotVisualTypeDef, _OptionalBoxPlotVisualTypeDef):
    pass

CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnId": str,
        "Expression": str,
    },
)

CalculatedFieldTypeDef = TypedDict(
    "CalculatedFieldTypeDef",
    {
        "DataSetIdentifier": str,
        "Name": str,
        "Expression": str,
    },
)

CalculatedMeasureFieldTypeDef = TypedDict(
    "CalculatedMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Expression": str,
    },
)

CancelIngestionRequestRequestTypeDef = TypedDict(
    "CancelIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

CancelIngestionResponseTypeDef = TypedDict(
    "CancelIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CascadingControlConfigurationTypeDef = TypedDict(
    "CascadingControlConfigurationTypeDef",
    {
        "SourceControls": List["CascadingControlSourceTypeDef"],
    },
    total=False,
)

CascadingControlSourceTypeDef = TypedDict(
    "CascadingControlSourceTypeDef",
    {
        "SourceSheetControlId": str,
        "ColumnToMatch": "ColumnIdentifierTypeDef",
    },
    total=False,
)

_RequiredCastColumnTypeOperationTypeDef = TypedDict(
    "_RequiredCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": ColumnDataTypeType,
    },
)
_OptionalCastColumnTypeOperationTypeDef = TypedDict(
    "_OptionalCastColumnTypeOperationTypeDef",
    {
        "Format": str,
    },
    total=False,
)

class CastColumnTypeOperationTypeDef(
    _RequiredCastColumnTypeOperationTypeDef, _OptionalCastColumnTypeOperationTypeDef
):
    pass

_RequiredCategoricalDimensionFieldTypeDef = TypedDict(
    "_RequiredCategoricalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalCategoricalDimensionFieldTypeDef = TypedDict(
    "_OptionalCategoricalDimensionFieldTypeDef",
    {
        "HierarchyId": str,
        "FormatConfiguration": "StringFormatConfigurationTypeDef",
    },
    total=False,
)

class CategoricalDimensionFieldTypeDef(
    _RequiredCategoricalDimensionFieldTypeDef, _OptionalCategoricalDimensionFieldTypeDef
):
    pass

_RequiredCategoricalMeasureFieldTypeDef = TypedDict(
    "_RequiredCategoricalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalCategoricalMeasureFieldTypeDef = TypedDict(
    "_OptionalCategoricalMeasureFieldTypeDef",
    {
        "AggregationFunction": CategoricalAggregationFunctionType,
        "FormatConfiguration": "StringFormatConfigurationTypeDef",
    },
    total=False,
)

class CategoricalMeasureFieldTypeDef(
    _RequiredCategoricalMeasureFieldTypeDef, _OptionalCategoricalMeasureFieldTypeDef
):
    pass

CategoryDrillDownFilterTypeDef = TypedDict(
    "CategoryDrillDownFilterTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
        "CategoryValues": List[str],
    },
)

CategoryFilterConfigurationTypeDef = TypedDict(
    "CategoryFilterConfigurationTypeDef",
    {
        "FilterListConfiguration": "FilterListConfigurationTypeDef",
        "CustomFilterListConfiguration": "CustomFilterListConfigurationTypeDef",
        "CustomFilterConfiguration": "CustomFilterConfigurationTypeDef",
    },
    total=False,
)

_RequiredCategoryFilterTypeDef = TypedDict(
    "_RequiredCategoryFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalCategoryFilterTypeDef = TypedDict(
    "_OptionalCategoryFilterTypeDef",
    {
        "Configuration": "CategoryFilterConfigurationTypeDef",
    },
    total=False,
)

class CategoryFilterTypeDef(_RequiredCategoryFilterTypeDef, _OptionalCategoryFilterTypeDef):
    pass

ChartAxisLabelOptionsTypeDef = TypedDict(
    "ChartAxisLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "SortIconVisibility": VisibilityType,
        "AxisLabelOptions": List["AxisLabelOptionsTypeDef"],
    },
    total=False,
)

ClusterMarkerConfigurationTypeDef = TypedDict(
    "ClusterMarkerConfigurationTypeDef",
    {
        "ClusterMarker": "ClusterMarkerTypeDef",
    },
    total=False,
)

ClusterMarkerTypeDef = TypedDict(
    "ClusterMarkerTypeDef",
    {
        "SimpleClusterMarker": "SimpleClusterMarkerTypeDef",
    },
    total=False,
)

_RequiredColorScaleTypeDef = TypedDict(
    "_RequiredColorScaleTypeDef",
    {
        "Colors": List["DataColorTypeDef"],
        "ColorFillType": ColorFillTypeType,
    },
)
_OptionalColorScaleTypeDef = TypedDict(
    "_OptionalColorScaleTypeDef",
    {
        "NullValueColor": "DataColorTypeDef",
    },
    total=False,
)

class ColorScaleTypeDef(_RequiredColorScaleTypeDef, _OptionalColorScaleTypeDef):
    pass

_RequiredColumnConfigurationTypeDef = TypedDict(
    "_RequiredColumnConfigurationTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalColumnConfigurationTypeDef = TypedDict(
    "_OptionalColumnConfigurationTypeDef",
    {
        "FormatConfiguration": "FormatConfigurationTypeDef",
        "Role": ColumnRoleType,
    },
    total=False,
)

class ColumnConfigurationTypeDef(
    _RequiredColumnConfigurationTypeDef, _OptionalColumnConfigurationTypeDef
):
    pass

ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "Text": str,
    },
    total=False,
)

ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": List["ColumnGroupColumnSchemaTypeDef"],
    },
    total=False,
)

ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef",
    {
        "GeoSpatialColumnGroup": "GeoSpatialColumnGroupTypeDef",
    },
    total=False,
)

ColumnHierarchyTypeDef = TypedDict(
    "ColumnHierarchyTypeDef",
    {
        "ExplicitHierarchy": "ExplicitHierarchyTypeDef",
        "DateTimeHierarchy": "DateTimeHierarchyTypeDef",
        "PredefinedHierarchy": "PredefinedHierarchyTypeDef",
    },
    total=False,
)

ColumnIdentifierTypeDef = TypedDict(
    "ColumnIdentifierTypeDef",
    {
        "DataSetIdentifier": str,
        "ColumnName": str,
    },
)

ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {
        "Principals": List[str],
        "ColumnNames": List[str],
    },
    total=False,
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "Name": str,
        "DataType": str,
        "GeographicRole": str,
    },
    total=False,
)

_RequiredColumnSortTypeDef = TypedDict(
    "_RequiredColumnSortTypeDef",
    {
        "SortBy": "ColumnIdentifierTypeDef",
        "Direction": SortDirectionType,
    },
)
_OptionalColumnSortTypeDef = TypedDict(
    "_OptionalColumnSortTypeDef",
    {
        "AggregationFunction": "AggregationFunctionTypeDef",
    },
    total=False,
)

class ColumnSortTypeDef(_RequiredColumnSortTypeDef, _OptionalColumnSortTypeDef):
    pass

ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": GeoSpatialDataRoleType,
        "ColumnDescription": "ColumnDescriptionTypeDef",
    },
    total=False,
)

_RequiredColumnTooltipItemTypeDef = TypedDict(
    "_RequiredColumnTooltipItemTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalColumnTooltipItemTypeDef = TypedDict(
    "_OptionalColumnTooltipItemTypeDef",
    {
        "Label": str,
        "Visibility": VisibilityType,
        "Aggregation": "AggregationFunctionTypeDef",
    },
    total=False,
)

class ColumnTooltipItemTypeDef(
    _RequiredColumnTooltipItemTypeDef, _OptionalColumnTooltipItemTypeDef
):
    pass

ComboChartAggregatedFieldWellsTypeDef = TypedDict(
    "ComboChartAggregatedFieldWellsTypeDef",
    {
        "Category": List["DimensionFieldTypeDef"],
        "BarValues": List["MeasureFieldTypeDef"],
        "Colors": List["DimensionFieldTypeDef"],
        "LineValues": List["MeasureFieldTypeDef"],
    },
    total=False,
)

ComboChartConfigurationTypeDef = TypedDict(
    "ComboChartConfigurationTypeDef",
    {
        "FieldWells": "ComboChartFieldWellsTypeDef",
        "SortConfiguration": "ComboChartSortConfigurationTypeDef",
        "BarsArrangement": BarsArrangementType,
        "CategoryAxis": "AxisDisplayOptionsTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "PrimaryYAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "PrimaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "SecondaryYAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "SecondaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColorLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "BarDataLabels": "DataLabelOptionsTypeDef",
        "LineDataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "ReferenceLines": List["ReferenceLineTypeDef"],
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

ComboChartFieldWellsTypeDef = TypedDict(
    "ComboChartFieldWellsTypeDef",
    {
        "ComboChartAggregatedFieldWells": "ComboChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

ComboChartSortConfigurationTypeDef = TypedDict(
    "ComboChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "CategoryItemsLimit": "ItemsLimitConfigurationTypeDef",
        "ColorSort": List["FieldSortOptionsTypeDef"],
        "ColorItemsLimit": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredComboChartVisualTypeDef = TypedDict(
    "_RequiredComboChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalComboChartVisualTypeDef = TypedDict(
    "_OptionalComboChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "ComboChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class ComboChartVisualTypeDef(_RequiredComboChartVisualTypeDef, _OptionalComboChartVisualTypeDef):
    pass

ComparisonConfigurationTypeDef = TypedDict(
    "ComparisonConfigurationTypeDef",
    {
        "ComparisonMethod": ComparisonMethodType,
        "ComparisonFormat": "ComparisonFormatConfigurationTypeDef",
    },
    total=False,
)

ComparisonFormatConfigurationTypeDef = TypedDict(
    "ComparisonFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": "NumberDisplayFormatConfigurationTypeDef",
        "PercentageDisplayFormatConfiguration": "PercentageDisplayFormatConfigurationTypeDef",
    },
    total=False,
)

ComputationTypeDef = TypedDict(
    "ComputationTypeDef",
    {
        "TopBottomRanked": "TopBottomRankedComputationTypeDef",
        "TopBottomMovers": "TopBottomMoversComputationTypeDef",
        "TotalAggregation": "TotalAggregationComputationTypeDef",
        "MaximumMinimum": "MaximumMinimumComputationTypeDef",
        "MetricComparison": "MetricComparisonComputationTypeDef",
        "PeriodOverPeriod": "PeriodOverPeriodComputationTypeDef",
        "PeriodToDate": "PeriodToDateComputationTypeDef",
        "GrowthRate": "GrowthRateComputationTypeDef",
        "UniqueValues": "UniqueValuesComputationTypeDef",
        "Forecast": "ForecastComputationTypeDef",
    },
    total=False,
)

ConditionalFormattingColorTypeDef = TypedDict(
    "ConditionalFormattingColorTypeDef",
    {
        "Solid": "ConditionalFormattingSolidColorTypeDef",
        "Gradient": "ConditionalFormattingGradientColorTypeDef",
    },
    total=False,
)

_RequiredConditionalFormattingCustomIconConditionTypeDef = TypedDict(
    "_RequiredConditionalFormattingCustomIconConditionTypeDef",
    {
        "Expression": str,
        "IconOptions": "ConditionalFormattingCustomIconOptionsTypeDef",
    },
)
_OptionalConditionalFormattingCustomIconConditionTypeDef = TypedDict(
    "_OptionalConditionalFormattingCustomIconConditionTypeDef",
    {
        "Color": str,
        "DisplayConfiguration": "ConditionalFormattingIconDisplayConfigurationTypeDef",
    },
    total=False,
)

class ConditionalFormattingCustomIconConditionTypeDef(
    _RequiredConditionalFormattingCustomIconConditionTypeDef,
    _OptionalConditionalFormattingCustomIconConditionTypeDef,
):
    pass

ConditionalFormattingCustomIconOptionsTypeDef = TypedDict(
    "ConditionalFormattingCustomIconOptionsTypeDef",
    {
        "Icon": IconType,
        "UnicodeIcon": str,
    },
    total=False,
)

ConditionalFormattingGradientColorTypeDef = TypedDict(
    "ConditionalFormattingGradientColorTypeDef",
    {
        "Expression": str,
        "Color": "GradientColorTypeDef",
    },
)

ConditionalFormattingIconDisplayConfigurationTypeDef = TypedDict(
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    {
        "IconDisplayOption": Literal["ICON_ONLY"],
    },
    total=False,
)

_RequiredConditionalFormattingIconSetTypeDef = TypedDict(
    "_RequiredConditionalFormattingIconSetTypeDef",
    {
        "Expression": str,
    },
)
_OptionalConditionalFormattingIconSetTypeDef = TypedDict(
    "_OptionalConditionalFormattingIconSetTypeDef",
    {
        "IconSetType": ConditionalFormattingIconSetTypeType,
    },
    total=False,
)

class ConditionalFormattingIconSetTypeDef(
    _RequiredConditionalFormattingIconSetTypeDef, _OptionalConditionalFormattingIconSetTypeDef
):
    pass

ConditionalFormattingIconTypeDef = TypedDict(
    "ConditionalFormattingIconTypeDef",
    {
        "IconSet": "ConditionalFormattingIconSetTypeDef",
        "CustomCondition": "ConditionalFormattingCustomIconConditionTypeDef",
    },
    total=False,
)

_RequiredConditionalFormattingSolidColorTypeDef = TypedDict(
    "_RequiredConditionalFormattingSolidColorTypeDef",
    {
        "Expression": str,
    },
)
_OptionalConditionalFormattingSolidColorTypeDef = TypedDict(
    "_OptionalConditionalFormattingSolidColorTypeDef",
    {
        "Color": str,
    },
    total=False,
)

class ConditionalFormattingSolidColorTypeDef(
    _RequiredConditionalFormattingSolidColorTypeDef, _OptionalConditionalFormattingSolidColorTypeDef
):
    pass

ContributionAnalysisDefaultTypeDef = TypedDict(
    "ContributionAnalysisDefaultTypeDef",
    {
        "MeasureFieldId": str,
        "ContributorDimensions": List["ColumnIdentifierTypeDef"],
    },
)

_RequiredCreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
    },
)
_OptionalCreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAccountCustomizationRequestRequestTypeDef(
    _RequiredCreateAccountCustomizationRequestRequestTypeDef,
    _OptionalCreateAccountCustomizationRequestRequestTypeDef,
):
    pass

CreateAccountCustomizationResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccountSubscriptionRequestRequestTypeDef",
    {
        "Edition": EditionType,
        "AuthenticationMethod": AuthenticationMethodOptionType,
        "AwsAccountId": str,
        "AccountName": str,
        "NotificationEmail": str,
    },
)
_OptionalCreateAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccountSubscriptionRequestRequestTypeDef",
    {
        "ActiveDirectoryName": str,
        "Realm": str,
        "DirectoryId": str,
        "AdminGroup": List[str],
        "AuthorGroup": List[str],
        "ReaderGroup": List[str],
        "FirstName": str,
        "LastName": str,
        "EmailAddress": str,
        "ContactNumber": str,
    },
    total=False,
)

class CreateAccountSubscriptionRequestRequestTypeDef(
    _RequiredCreateAccountSubscriptionRequestRequestTypeDef,
    _OptionalCreateAccountSubscriptionRequestRequestTypeDef,
):
    pass

CreateAccountSubscriptionResponseTypeDef = TypedDict(
    "CreateAccountSubscriptionResponseTypeDef",
    {
        "SignupResponse": "SignupResponseTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
    },
)
_OptionalCreateAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnalysisRequestRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "SourceEntity": "AnalysisSourceEntityTypeDef",
        "ThemeArn": str,
        "Tags": List["TagTypeDef"],
        "Definition": "AnalysisDefinitionTypeDef",
    },
    total=False,
)

class CreateAnalysisRequestRequestTypeDef(
    _RequiredCreateAnalysisRequestRequestTypeDef, _OptionalCreateAnalysisRequestRequestTypeDef
):
    pass

CreateAnalysisResponseTypeDef = TypedDict(
    "CreateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef",
    {
        "Columns": List["CalculatedColumnTypeDef"],
    },
)

_RequiredCreateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
    },
)
_OptionalCreateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDashboardRequestRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "SourceEntity": "DashboardSourceEntityTypeDef",
        "Tags": List["TagTypeDef"],
        "VersionDescription": str,
        "DashboardPublishOptions": "DashboardPublishOptionsTypeDef",
        "ThemeArn": str,
        "Definition": "DashboardVersionDefinitionTypeDef",
    },
    total=False,
)

class CreateDashboardRequestRequestTypeDef(
    _RequiredCreateDashboardRequestRequestTypeDef, _OptionalCreateDashboardRequestRequestTypeDef
):
    pass

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalCreateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSetRequestRequestTypeDef",
    {
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "Permissions": List["ResourcePermissionTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "RowLevelPermissionTagConfiguration": "RowLevelPermissionTagConfigurationTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
        "Tags": List["TagTypeDef"],
        "DataSetUsageConfiguration": "DataSetUsageConfigurationTypeDef",
    },
    total=False,
)

class CreateDataSetRequestRequestTypeDef(
    _RequiredCreateDataSetRequestRequestTypeDef, _OptionalCreateDataSetRequestRequestTypeDef
):
    pass

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "Credentials": "DataSourceCredentialsTypeDef",
        "Permissions": List["ResourcePermissionTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFolderMembershipRequestRequestTypeDef = TypedDict(
    "CreateFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

CreateFolderMembershipResponseTypeDef = TypedDict(
    "CreateFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "FolderMember": "FolderMemberTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFolderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalCreateFolderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFolderRequestRequestTypeDef",
    {
        "Name": str,
        "FolderType": Literal["SHARED"],
        "ParentFolderArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFolderRequestRequestTypeDef(
    _RequiredCreateFolderRequestRequestTypeDef, _OptionalCreateFolderRequestRequestTypeDef
):
    pass

CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": "GroupMemberTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
        "Namespace": str,
    },
)
_OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
    },
    total=False,
)

class CreateIAMPolicyAssignmentRequestRequestTypeDef(
    _RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef,
    _OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef,
):
    pass

CreateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIngestionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIngestionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "IngestionId": str,
        "AwsAccountId": str,
    },
)
_OptionalCreateIngestionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIngestionRequestRequestTypeDef",
    {
        "IngestionType": IngestionTypeType,
    },
    total=False,
)

class CreateIngestionRequestRequestTypeDef(
    _RequiredCreateIngestionRequestRequestTypeDef, _OptionalCreateIngestionRequestRequestTypeDef
):
    pass

CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": IngestionStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "IdentityStore": Literal["QUICKSIGHT"],
    },
)
_OptionalCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNamespaceRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateNamespaceRequestRequestTypeDef(
    _RequiredCreateNamespaceRequestRequestTypeDef, _OptionalCreateNamespaceRequestRequestTypeDef
):
    pass

CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateAliasRequestRequestTypeDef = TypedDict(
    "CreateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

CreateTemplateAliasResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalCreateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateRequestRequestTypeDef",
    {
        "Name": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "SourceEntity": "TemplateSourceEntityTypeDef",
        "Tags": List["TagTypeDef"],
        "VersionDescription": str,
        "Definition": "TemplateVersionDefinitionTypeDef",
    },
    total=False,
)

class CreateTemplateRequestRequestTypeDef(
    _RequiredCreateTemplateRequestRequestTypeDef, _OptionalCreateTemplateRequestRequestTypeDef
):
    pass

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThemeAliasRequestRequestTypeDef = TypedDict(
    "CreateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

CreateThemeAliasResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "Name": str,
        "BaseThemeId": str,
        "Configuration": "ThemeConfigurationTypeDef",
    },
)
_OptionalCreateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestRequestTypeDef",
    {
        "VersionDescription": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateThemeRequestRequestTypeDef(
    _RequiredCreateThemeRequestRequestTypeDef, _OptionalCreateThemeRequestRequestTypeDef
):
    pass

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCredentialPairTypeDef = TypedDict(
    "_RequiredCredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
_OptionalCredentialPairTypeDef = TypedDict(
    "_OptionalCredentialPairTypeDef",
    {
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
    },
    total=False,
)

class CredentialPairTypeDef(_RequiredCredentialPairTypeDef, _OptionalCredentialPairTypeDef):
    pass

CurrencyDisplayFormatConfigurationTypeDef = TypedDict(
    "CurrencyDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": "NumericSeparatorConfigurationTypeDef",
        "Symbol": str,
        "DecimalPlacesConfiguration": "DecimalPlacesConfigurationTypeDef",
        "NumberScale": NumberScaleType,
        "NegativeValueConfiguration": "NegativeValueConfigurationTypeDef",
        "NullValueFormatConfiguration": "NullValueFormatConfigurationTypeDef",
    },
    total=False,
)

CustomActionFilterOperationTypeDef = TypedDict(
    "CustomActionFilterOperationTypeDef",
    {
        "SelectedFieldsConfiguration": "FilterOperationSelectedFieldsConfigurationTypeDef",
        "TargetVisualsConfiguration": "FilterOperationTargetVisualsConfigurationTypeDef",
    },
)

CustomActionNavigationOperationTypeDef = TypedDict(
    "CustomActionNavigationOperationTypeDef",
    {
        "LocalNavigationConfiguration": "LocalNavigationConfigurationTypeDef",
    },
    total=False,
)

CustomActionSetParametersOperationTypeDef = TypedDict(
    "CustomActionSetParametersOperationTypeDef",
    {
        "ParameterValueConfigurations": List["SetParameterValueConfigurationTypeDef"],
    },
)

CustomActionURLOperationTypeDef = TypedDict(
    "CustomActionURLOperationTypeDef",
    {
        "URLTemplate": str,
        "URLTarget": URLTargetConfigurationType,
    },
)

CustomContentConfigurationTypeDef = TypedDict(
    "CustomContentConfigurationTypeDef",
    {
        "ContentUrl": str,
        "ContentType": CustomContentTypeType,
        "ImageScaling": CustomContentImageScalingConfigurationType,
    },
    total=False,
)

_RequiredCustomContentVisualTypeDef = TypedDict(
    "_RequiredCustomContentVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalCustomContentVisualTypeDef = TypedDict(
    "_OptionalCustomContentVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "CustomContentConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class CustomContentVisualTypeDef(
    _RequiredCustomContentVisualTypeDef, _OptionalCustomContentVisualTypeDef
):
    pass

_RequiredCustomFilterConfigurationTypeDef = TypedDict(
    "_RequiredCustomFilterConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalCustomFilterConfigurationTypeDef = TypedDict(
    "_OptionalCustomFilterConfigurationTypeDef",
    {
        "CategoryValue": str,
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "ParameterName": str,
    },
    total=False,
)

class CustomFilterConfigurationTypeDef(
    _RequiredCustomFilterConfigurationTypeDef, _OptionalCustomFilterConfigurationTypeDef
):
    pass

_RequiredCustomFilterListConfigurationTypeDef = TypedDict(
    "_RequiredCustomFilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalCustomFilterListConfigurationTypeDef = TypedDict(
    "_OptionalCustomFilterListConfigurationTypeDef",
    {
        "CategoryValues": List[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)

class CustomFilterListConfigurationTypeDef(
    _RequiredCustomFilterListConfigurationTypeDef, _OptionalCustomFilterListConfigurationTypeDef
):
    pass

CustomNarrativeOptionsTypeDef = TypedDict(
    "CustomNarrativeOptionsTypeDef",
    {
        "Narrative": str,
    },
)

CustomParameterValuesTypeDef = TypedDict(
    "CustomParameterValuesTypeDef",
    {
        "StringValues": List[str],
        "IntegerValues": List[int],
        "DecimalValues": List[float],
        "DateTimeValues": List[Union[datetime, str]],
    },
    total=False,
)

_RequiredCustomSqlTypeDef = TypedDict(
    "_RequiredCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
    },
)
_OptionalCustomSqlTypeDef = TypedDict(
    "_OptionalCustomSqlTypeDef",
    {
        "Columns": List["InputColumnTypeDef"],
    },
    total=False,
)

class CustomSqlTypeDef(_RequiredCustomSqlTypeDef, _OptionalCustomSqlTypeDef):
    pass

_RequiredCustomValuesConfigurationTypeDef = TypedDict(
    "_RequiredCustomValuesConfigurationTypeDef",
    {
        "CustomValues": "CustomParameterValuesTypeDef",
    },
)
_OptionalCustomValuesConfigurationTypeDef = TypedDict(
    "_OptionalCustomValuesConfigurationTypeDef",
    {
        "IncludeNullValue": bool,
    },
    total=False,
)

class CustomValuesConfigurationTypeDef(
    _RequiredCustomValuesConfigurationTypeDef, _OptionalCustomValuesConfigurationTypeDef
):
    pass

DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": DashboardErrorTypeType,
        "Message": str,
        "ViolatedEntities": List["EntityTypeDef"],
    },
    total=False,
)

DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": "AdHocFilteringOptionTypeDef",
        "ExportToCSVOption": "ExportToCSVOptionTypeDef",
        "SheetControlsOption": "SheetControlsOptionTypeDef",
        "VisualPublishOptions": "DashboardVisualPublishOptionsTypeDef",
    },
    total=False,
)

_RequiredDashboardSearchFilterTypeDef = TypedDict(
    "_RequiredDashboardSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
    },
)
_OptionalDashboardSearchFilterTypeDef = TypedDict(
    "_OptionalDashboardSearchFilterTypeDef",
    {
        "Name": DashboardFilterAttributeType,
        "Value": str,
    },
    total=False,
)

class DashboardSearchFilterTypeDef(
    _RequiredDashboardSearchFilterTypeDef, _OptionalDashboardSearchFilterTypeDef
):
    pass

DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {
        "SourceTemplate": "DashboardSourceTemplateTypeDef",
    },
    total=False,
)

DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {
        "DataSetReferences": List["DataSetReferenceTypeDef"],
        "Arn": str,
    },
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

_RequiredDashboardVersionDefinitionTypeDef = TypedDict(
    "_RequiredDashboardVersionDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": List["DataSetIdentifierDeclarationTypeDef"],
    },
)
_OptionalDashboardVersionDefinitionTypeDef = TypedDict(
    "_OptionalDashboardVersionDefinitionTypeDef",
    {
        "Sheets": List["SheetDefinitionTypeDef"],
        "CalculatedFields": List["CalculatedFieldTypeDef"],
        "ParameterDeclarations": List["ParameterDeclarationTypeDef"],
        "FilterGroups": List["FilterGroupTypeDef"],
        "ColumnConfigurations": List["ColumnConfigurationTypeDef"],
        "AnalysisDefaults": "AnalysisDefaultsTypeDef",
    },
    total=False,
)

class DashboardVersionDefinitionTypeDef(
    _RequiredDashboardVersionDefinitionTypeDef, _OptionalDashboardVersionDefinitionTypeDef
):
    pass

DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": ResourceStatusType,
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
        "Status": ResourceStatusType,
        "Arn": str,
        "SourceEntityArn": str,
        "DataSetArns": List[str],
        "Description": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

DashboardVisualIdTypeDef = TypedDict(
    "DashboardVisualIdTypeDef",
    {
        "DashboardId": str,
        "SheetId": str,
        "VisualId": str,
    },
)

DashboardVisualPublishOptionsTypeDef = TypedDict(
    "DashboardVisualPublishOptionsTypeDef",
    {
        "ExportHiddenFieldsOption": "ExportHiddenFieldsOptionTypeDef",
    },
    total=False,
)

DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {
        "Colors": List[str],
        "MinMaxGradient": List[str],
        "EmptyFillColor": str,
    },
    total=False,
)

DataColorTypeDef = TypedDict(
    "DataColorTypeDef",
    {
        "Color": str,
        "DataValue": float,
    },
    total=False,
)

_RequiredDataFieldSeriesItemTypeDef = TypedDict(
    "_RequiredDataFieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
    },
)
_OptionalDataFieldSeriesItemTypeDef = TypedDict(
    "_OptionalDataFieldSeriesItemTypeDef",
    {
        "FieldValue": str,
        "Settings": "LineChartSeriesSettingsTypeDef",
    },
    total=False,
)

class DataFieldSeriesItemTypeDef(
    _RequiredDataFieldSeriesItemTypeDef, _OptionalDataFieldSeriesItemTypeDef
):
    pass

DataLabelOptionsTypeDef = TypedDict(
    "DataLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "CategoryLabelVisibility": VisibilityType,
        "MeasureLabelVisibility": VisibilityType,
        "DataLabelTypes": List["DataLabelTypeTypeDef"],
        "Position": DataLabelPositionType,
        "LabelContent": DataLabelContentType,
        "LabelFontConfiguration": "FontConfigurationTypeDef",
        "LabelColor": str,
        "Overlap": DataLabelOverlapType,
    },
    total=False,
)

DataLabelTypeTypeDef = TypedDict(
    "DataLabelTypeTypeDef",
    {
        "FieldLabelType": "FieldLabelTypeTypeDef",
        "DataPathLabelType": "DataPathLabelTypeTypeDef",
        "RangeEndsLabelType": "RangeEndsLabelTypeTypeDef",
        "MinimumLabelType": "MinimumLabelTypeTypeDef",
        "MaximumLabelType": "MaximumLabelTypeTypeDef",
    },
    total=False,
)

_RequiredDataPathColorTypeDef = TypedDict(
    "_RequiredDataPathColorTypeDef",
    {
        "Element": "DataPathValueTypeDef",
        "Color": str,
    },
)
_OptionalDataPathColorTypeDef = TypedDict(
    "_OptionalDataPathColorTypeDef",
    {
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)

class DataPathColorTypeDef(_RequiredDataPathColorTypeDef, _OptionalDataPathColorTypeDef):
    pass

DataPathLabelTypeTypeDef = TypedDict(
    "DataPathLabelTypeTypeDef",
    {
        "FieldId": str,
        "FieldValue": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

DataPathSortTypeDef = TypedDict(
    "DataPathSortTypeDef",
    {
        "Direction": SortDirectionType,
        "SortPaths": List["DataPathValueTypeDef"],
    },
)

DataPathValueTypeDef = TypedDict(
    "DataPathValueTypeDef",
    {
        "FieldId": str,
        "FieldValue": str,
    },
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

DataSetIdentifierDeclarationTypeDef = TypedDict(
    "DataSetIdentifierDeclarationTypeDef",
    {
        "Identifier": str,
        "DataSetArn": str,
    },
)

DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef",
    {
        "DataSetPlaceholder": str,
        "DataSetArn": str,
    },
)

DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef",
    {
        "ColumnSchemaList": List["ColumnSchemaTypeDef"],
    },
    total=False,
)

DataSetSearchFilterTypeDef = TypedDict(
    "DataSetSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSetFilterAttributeType,
        "Value": str,
    },
)

DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": DataSetImportModeType,
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "RowLevelPermissionTagConfigurationApplied": bool,
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
        "ImportMode": DataSetImportModeType,
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "RowLevelPermissionTagConfiguration": "RowLevelPermissionTagConfigurationTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
        "DataSetUsageConfiguration": "DataSetUsageConfigurationTypeDef",
    },
    total=False,
)

DataSetUsageConfigurationTypeDef = TypedDict(
    "DataSetUsageConfigurationTypeDef",
    {
        "DisableUseAsDirectQuerySource": bool,
        "DisableUseAsImportedSource": bool,
    },
    total=False,
)

DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {
        "CredentialPair": "CredentialPairTypeDef",
        "CopySourceArn": str,
        "SecretArn": str,
    },
    total=False,
)

DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": DataSourceErrorInfoTypeType,
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
        "AmazonOpenSearchParameters": "AmazonOpenSearchParametersTypeDef",
        "ExasolParameters": "ExasolParametersTypeDef",
        "DatabricksParameters": "DatabricksParametersTypeDef",
    },
    total=False,
)

DataSourceSearchFilterTypeDef = TypedDict(
    "DataSourceSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSourceFilterAttributeType,
        "Value": str,
    },
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Status": ResourceStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "AlternateDataSourceParameters": List["DataSourceParametersTypeDef"],
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
        "ErrorInfo": "DataSourceErrorInfoTypeDef",
        "SecretArn": str,
    },
    total=False,
)

DatabricksParametersTypeDef = TypedDict(
    "DatabricksParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "SqlEndpointPath": str,
    },
)

DateAxisOptionsTypeDef = TypedDict(
    "DateAxisOptionsTypeDef",
    {
        "MissingDateVisibility": VisibilityType,
    },
    total=False,
)

_RequiredDateDimensionFieldTypeDef = TypedDict(
    "_RequiredDateDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalDateDimensionFieldTypeDef = TypedDict(
    "_OptionalDateDimensionFieldTypeDef",
    {
        "DateGranularity": TimeGranularityType,
        "HierarchyId": str,
        "FormatConfiguration": "DateTimeFormatConfigurationTypeDef",
    },
    total=False,
)

class DateDimensionFieldTypeDef(
    _RequiredDateDimensionFieldTypeDef, _OptionalDateDimensionFieldTypeDef
):
    pass

_RequiredDateMeasureFieldTypeDef = TypedDict(
    "_RequiredDateMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalDateMeasureFieldTypeDef = TypedDict(
    "_OptionalDateMeasureFieldTypeDef",
    {
        "AggregationFunction": DateAggregationFunctionType,
        "FormatConfiguration": "DateTimeFormatConfigurationTypeDef",
    },
    total=False,
)

class DateMeasureFieldTypeDef(_RequiredDateMeasureFieldTypeDef, _OptionalDateMeasureFieldTypeDef):
    pass

DateTimeDefaultValuesTypeDef = TypedDict(
    "DateTimeDefaultValuesTypeDef",
    {
        "DynamicValue": "DynamicDefaultValueTypeDef",
        "StaticValues": List[Union[datetime, str]],
        "RollingDate": "RollingDateConfigurationTypeDef",
    },
    total=False,
)

DateTimeFormatConfigurationTypeDef = TypedDict(
    "DateTimeFormatConfigurationTypeDef",
    {
        "DateTimeFormat": str,
        "NullValueFormatConfiguration": "NullValueFormatConfigurationTypeDef",
        "NumericFormatConfiguration": "NumericFormatConfigurationTypeDef",
    },
    total=False,
)

_RequiredDateTimeHierarchyTypeDef = TypedDict(
    "_RequiredDateTimeHierarchyTypeDef",
    {
        "HierarchyId": str,
    },
)
_OptionalDateTimeHierarchyTypeDef = TypedDict(
    "_OptionalDateTimeHierarchyTypeDef",
    {
        "DrillDownFilters": List["DrillDownFilterTypeDef"],
    },
    total=False,
)

class DateTimeHierarchyTypeDef(
    _RequiredDateTimeHierarchyTypeDef, _OptionalDateTimeHierarchyTypeDef
):
    pass

_RequiredDateTimeParameterDeclarationTypeDef = TypedDict(
    "_RequiredDateTimeParameterDeclarationTypeDef",
    {
        "Name": str,
    },
)
_OptionalDateTimeParameterDeclarationTypeDef = TypedDict(
    "_OptionalDateTimeParameterDeclarationTypeDef",
    {
        "DefaultValues": "DateTimeDefaultValuesTypeDef",
        "TimeGranularity": TimeGranularityType,
        "ValueWhenUnset": "DateTimeValueWhenUnsetConfigurationTypeDef",
    },
    total=False,
)

class DateTimeParameterDeclarationTypeDef(
    _RequiredDateTimeParameterDeclarationTypeDef, _OptionalDateTimeParameterDeclarationTypeDef
):
    pass

DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef",
    {
        "Name": str,
        "Values": List[Union[datetime, str]],
    },
)

DateTimePickerControlDisplayOptionsTypeDef = TypedDict(
    "DateTimePickerControlDisplayOptionsTypeDef",
    {
        "TitleOptions": "LabelOptionsTypeDef",
        "DateTimeFormat": str,
    },
    total=False,
)

DateTimeValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": Union[datetime, str],
    },
    total=False,
)

DecimalDefaultValuesTypeDef = TypedDict(
    "DecimalDefaultValuesTypeDef",
    {
        "DynamicValue": "DynamicDefaultValueTypeDef",
        "StaticValues": List[float],
    },
    total=False,
)

_RequiredDecimalParameterDeclarationTypeDef = TypedDict(
    "_RequiredDecimalParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalDecimalParameterDeclarationTypeDef = TypedDict(
    "_OptionalDecimalParameterDeclarationTypeDef",
    {
        "DefaultValues": "DecimalDefaultValuesTypeDef",
        "ValueWhenUnset": "DecimalValueWhenUnsetConfigurationTypeDef",
    },
    total=False,
)

class DecimalParameterDeclarationTypeDef(
    _RequiredDecimalParameterDeclarationTypeDef, _OptionalDecimalParameterDeclarationTypeDef
):
    pass

DecimalParameterTypeDef = TypedDict(
    "DecimalParameterTypeDef",
    {
        "Name": str,
        "Values": List[float],
    },
)

DecimalPlacesConfigurationTypeDef = TypedDict(
    "DecimalPlacesConfigurationTypeDef",
    {
        "DecimalPlaces": int,
    },
)

DecimalValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DecimalValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": float,
    },
    total=False,
)

DefaultFreeFormLayoutConfigurationTypeDef = TypedDict(
    "DefaultFreeFormLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": "FreeFormLayoutCanvasSizeOptionsTypeDef",
    },
)

DefaultGridLayoutConfigurationTypeDef = TypedDict(
    "DefaultGridLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": "GridLayoutCanvasSizeOptionsTypeDef",
    },
)

DefaultInteractiveLayoutConfigurationTypeDef = TypedDict(
    "DefaultInteractiveLayoutConfigurationTypeDef",
    {
        "Grid": "DefaultGridLayoutConfigurationTypeDef",
        "FreeForm": "DefaultFreeFormLayoutConfigurationTypeDef",
    },
    total=False,
)

DefaultNewSheetConfigurationTypeDef = TypedDict(
    "DefaultNewSheetConfigurationTypeDef",
    {
        "InteractiveLayoutConfiguration": "DefaultInteractiveLayoutConfigurationTypeDef",
        "PaginatedLayoutConfiguration": "DefaultPaginatedLayoutConfigurationTypeDef",
        "SheetContentType": SheetContentTypeType,
    },
    total=False,
)

DefaultPaginatedLayoutConfigurationTypeDef = TypedDict(
    "DefaultPaginatedLayoutConfigurationTypeDef",
    {
        "SectionBased": "DefaultSectionBasedLayoutConfigurationTypeDef",
    },
    total=False,
)

DefaultSectionBasedLayoutConfigurationTypeDef = TypedDict(
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    },
)

_RequiredDeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)

class DeleteAccountCustomizationRequestRequestTypeDef(
    _RequiredDeleteAccountCustomizationRequestRequestTypeDef,
    _OptionalDeleteAccountCustomizationRequestRequestTypeDef,
):
    pass

DeleteAccountCustomizationResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DeleteAccountSubscriptionResponseTypeDef = TypedDict(
    "DeleteAccountSubscriptionResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalDeleteAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalysisRequestRequestTypeDef",
    {
        "RecoveryWindowInDays": int,
        "ForceDeleteWithoutRecovery": bool,
    },
    total=False,
)

class DeleteAnalysisRequestRequestTypeDef(
    _RequiredDeleteAnalysisRequestRequestTypeDef, _OptionalDeleteAnalysisRequestRequestTypeDef
):
    pass

DeleteAnalysisResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "DeletionTime": datetime,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDashboardRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)

class DeleteDashboardRequestRequestTypeDef(
    _RequiredDeleteDashboardRequestRequestTypeDef, _OptionalDeleteDashboardRequestRequestTypeDef
):
    pass

DeleteDashboardResponseTypeDef = TypedDict(
    "DeleteDashboardResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "DashboardId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DeleteDataSetResponseTypeDef = TypedDict(
    "DeleteDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderMembershipRequestRequestTypeDef = TypedDict(
    "DeleteFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

DeleteFolderMembershipResponseTypeDef = TypedDict(
    "DeleteFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DeleteFolderResponseTypeDef = TypedDict(
    "DeleteFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupMembershipResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupResponseTypeDef = TypedDict(
    "DeleteGroupResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DeleteIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateAliasRequestRequestTypeDef = TypedDict(
    "DeleteTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DeleteTemplateAliasResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseTypeDef",
    {
        "Status": int,
        "TemplateId": str,
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDeleteTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTemplateRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)

class DeleteTemplateRequestRequestTypeDef(
    _RequiredDeleteTemplateRequestRequestTypeDef, _OptionalDeleteTemplateRequestRequestTypeDef
):
    pass

DeleteTemplateResponseTypeDef = TypedDict(
    "DeleteTemplateResponseTypeDef",
    {
        "RequestId": str,
        "Arn": str,
        "TemplateId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteThemeAliasRequestRequestTypeDef = TypedDict(
    "DeleteThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DeleteThemeAliasResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteThemeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDeleteThemeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThemeRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)

class DeleteThemeRequestRequestTypeDef(
    _RequiredDeleteThemeRequestRequestTypeDef, _OptionalDeleteThemeRequestRequestTypeDef
):
    pass

DeleteThemeResponseTypeDef = TypedDict(
    "DeleteThemeResponseTypeDef",
    {
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserByPrincipalIdRequestRequestTypeDef = TypedDict(
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    {
        "PrincipalId": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
        "Resolved": bool,
    },
    total=False,
)

class DescribeAccountCustomizationRequestRequestTypeDef(
    _RequiredDescribeAccountCustomizationRequestRequestTypeDef,
    _OptionalDescribeAccountCustomizationRequestRequestTypeDef,
):
    pass

DescribeAccountCustomizationResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountSettingsRequestRequestTypeDef = TypedDict(
    "DescribeAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAccountSubscriptionResponseTypeDef = TypedDict(
    "DescribeAccountSubscriptionResponseTypeDef",
    {
        "AccountInfo": "AccountInfoTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisDefinitionResponseTypeDef = TypedDict(
    "DescribeAnalysisDefinitionResponseTypeDef",
    {
        "AnalysisId": str,
        "Name": str,
        "Errors": List["AnalysisErrorTypeDef"],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": "AnalysisDefinitionTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisPermissionsResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseTypeDef",
    {
        "Analysis": "AnalysisTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDashboardDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDashboardDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDescribeDashboardDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDashboardDefinitionRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)

class DescribeDashboardDefinitionRequestRequestTypeDef(
    _RequiredDescribeDashboardDefinitionRequestRequestTypeDef,
    _OptionalDescribeDashboardDefinitionRequestRequestTypeDef,
):
    pass

DescribeDashboardDefinitionResponseTypeDef = TypedDict(
    "DescribeDashboardDefinitionResponseTypeDef",
    {
        "DashboardId": str,
        "Errors": List["DashboardErrorTypeDef"],
        "Name": str,
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": "DashboardVersionDefinitionTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)

DescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "LinkSharingConfiguration": "LinkSharingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDescribeDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDashboardRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)

class DescribeDashboardRequestRequestTypeDef(
    _RequiredDescribeDashboardRequestRequestTypeDef, _OptionalDescribeDashboardRequestRequestTypeDef
):
    pass

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "Dashboard": "DashboardTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetResponseTypeDef = TypedDict(
    "DescribeDataSetResponseTypeDef",
    {
        "DataSet": "DataSetTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderRequestRequestTypeDef = TypedDict(
    "DescribeFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderResponseTypeDef = TypedDict(
    "DescribeFolderResponseTypeDef",
    {
        "Status": int,
        "Folder": "FolderTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupMembershipRequestRequestTypeDef = TypedDict(
    "DescribeGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeGroupMembershipResponseTypeDef = TypedDict(
    "DescribeGroupMembershipResponseTypeDef",
    {
        "GroupMember": "GroupMemberTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DescribeIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": "IAMPolicyAssignmentTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIngestionRequestRequestTypeDef = TypedDict(
    "DescribeIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

DescribeIngestionResponseTypeDef = TypedDict(
    "DescribeIngestionResponseTypeDef",
    {
        "Ingestion": "IngestionTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpRestrictionRequestRequestTypeDef = TypedDict(
    "DescribeIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeIpRestrictionResponseTypeDef = TypedDict(
    "DescribeIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": Dict[str, str],
        "Enabled": bool,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "Namespace": "NamespaceInfoV2TypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplateAliasRequestRequestTypeDef = TypedDict(
    "DescribeTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DescribeTemplateAliasResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTemplateDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTemplateDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDescribeTemplateDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTemplateDefinitionRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)

class DescribeTemplateDefinitionRequestRequestTypeDef(
    _RequiredDescribeTemplateDefinitionRequestRequestTypeDef,
    _OptionalDescribeTemplateDefinitionRequestRequestTypeDef,
):
    pass

DescribeTemplateDefinitionResponseTypeDef = TypedDict(
    "DescribeTemplateDefinitionResponseTypeDef",
    {
        "Name": str,
        "TemplateId": str,
        "Errors": List["TemplateErrorTypeDef"],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": "TemplateVersionDefinitionTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)

DescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDescribeTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTemplateRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)

class DescribeTemplateRequestRequestTypeDef(
    _RequiredDescribeTemplateRequestRequestTypeDef, _OptionalDescribeTemplateRequestRequestTypeDef
):
    pass

DescribeTemplateResponseTypeDef = TypedDict(
    "DescribeTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemeAliasRequestRequestTypeDef = TypedDict(
    "DescribeThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DescribeThemeAliasResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)

DescribeThemePermissionsResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeThemeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDescribeThemeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeThemeRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)

class DescribeThemeRequestRequestTypeDef(
    _RequiredDescribeThemeRequestRequestTypeDef, _OptionalDescribeThemeRequestRequestTypeDef
):
    pass

DescribeThemeResponseTypeDef = TypedDict(
    "DescribeThemeResponseTypeDef",
    {
        "Theme": "ThemeTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationParameterValueConfigurationTypeDef = TypedDict(
    "DestinationParameterValueConfigurationTypeDef",
    {
        "CustomValuesConfiguration": "CustomValuesConfigurationTypeDef",
        "SelectAllValueOptions": Literal["ALL_VALUES"],
        "SourceParameterName": str,
        "SourceField": str,
    },
    total=False,
)

DimensionFieldTypeDef = TypedDict(
    "DimensionFieldTypeDef",
    {
        "NumericalDimensionField": "NumericalDimensionFieldTypeDef",
        "CategoricalDimensionField": "CategoricalDimensionFieldTypeDef",
        "DateDimensionField": "DateDimensionFieldTypeDef",
    },
    total=False,
)

DonutCenterOptionsTypeDef = TypedDict(
    "DonutCenterOptionsTypeDef",
    {
        "LabelVisibility": VisibilityType,
    },
    total=False,
)

DonutOptionsTypeDef = TypedDict(
    "DonutOptionsTypeDef",
    {
        "ArcOptions": "ArcOptionsTypeDef",
        "DonutCenterOptions": "DonutCenterOptionsTypeDef",
    },
    total=False,
)

DrillDownFilterTypeDef = TypedDict(
    "DrillDownFilterTypeDef",
    {
        "NumericEqualityFilter": "NumericEqualityDrillDownFilterTypeDef",
        "CategoryFilter": "CategoryDrillDownFilterTypeDef",
        "TimeRangeFilter": "TimeRangeDrillDownFilterTypeDef",
    },
    total=False,
)

DropDownControlDisplayOptionsTypeDef = TypedDict(
    "DropDownControlDisplayOptionsTypeDef",
    {
        "SelectAllOptions": "ListControlSelectAllOptionsTypeDef",
        "TitleOptions": "LabelOptionsTypeDef",
    },
    total=False,
)

_RequiredDynamicDefaultValueTypeDef = TypedDict(
    "_RequiredDynamicDefaultValueTypeDef",
    {
        "DefaultValueColumn": "ColumnIdentifierTypeDef",
    },
)
_OptionalDynamicDefaultValueTypeDef = TypedDict(
    "_OptionalDynamicDefaultValueTypeDef",
    {
        "UserNameColumn": "ColumnIdentifierTypeDef",
        "GroupNameColumn": "ColumnIdentifierTypeDef",
    },
    total=False,
)

class DynamicDefaultValueTypeDef(
    _RequiredDynamicDefaultValueTypeDef, _OptionalDynamicDefaultValueTypeDef
):
    pass

_RequiredEmptyVisualTypeDef = TypedDict(
    "_RequiredEmptyVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalEmptyVisualTypeDef = TypedDict(
    "_OptionalEmptyVisualTypeDef",
    {
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class EmptyVisualTypeDef(_RequiredEmptyVisualTypeDef, _OptionalEmptyVisualTypeDef):
    pass

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Path": str,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": IngestionErrorTypeType,
        "Message": str,
    },
    total=False,
)

ExasolParametersTypeDef = TypedDict(
    "ExasolParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

_RequiredExcludePeriodConfigurationTypeDef = TypedDict(
    "_RequiredExcludePeriodConfigurationTypeDef",
    {
        "Amount": int,
        "Granularity": TimeGranularityType,
    },
)
_OptionalExcludePeriodConfigurationTypeDef = TypedDict(
    "_OptionalExcludePeriodConfigurationTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)

class ExcludePeriodConfigurationTypeDef(
    _RequiredExcludePeriodConfigurationTypeDef, _OptionalExcludePeriodConfigurationTypeDef
):
    pass

_RequiredExplicitHierarchyTypeDef = TypedDict(
    "_RequiredExplicitHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": List["ColumnIdentifierTypeDef"],
    },
)
_OptionalExplicitHierarchyTypeDef = TypedDict(
    "_OptionalExplicitHierarchyTypeDef",
    {
        "DrillDownFilters": List["DrillDownFilterTypeDef"],
    },
    total=False,
)

class ExplicitHierarchyTypeDef(
    _RequiredExplicitHierarchyTypeDef, _OptionalExplicitHierarchyTypeDef
):
    pass

ExportHiddenFieldsOptionTypeDef = TypedDict(
    "ExportHiddenFieldsOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

FieldBasedTooltipTypeDef = TypedDict(
    "FieldBasedTooltipTypeDef",
    {
        "AggregationVisibility": VisibilityType,
        "TooltipTitleType": TooltipTitleTypeType,
        "TooltipFields": List["TooltipItemTypeDef"],
    },
    total=False,
)

FieldFolderTypeDef = TypedDict(
    "FieldFolderTypeDef",
    {
        "description": str,
        "columns": List[str],
    },
    total=False,
)

FieldLabelTypeTypeDef = TypedDict(
    "FieldLabelTypeTypeDef",
    {
        "FieldId": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

_RequiredFieldSeriesItemTypeDef = TypedDict(
    "_RequiredFieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
    },
)
_OptionalFieldSeriesItemTypeDef = TypedDict(
    "_OptionalFieldSeriesItemTypeDef",
    {
        "Settings": "LineChartSeriesSettingsTypeDef",
    },
    total=False,
)

class FieldSeriesItemTypeDef(_RequiredFieldSeriesItemTypeDef, _OptionalFieldSeriesItemTypeDef):
    pass

FieldSortOptionsTypeDef = TypedDict(
    "FieldSortOptionsTypeDef",
    {
        "FieldSort": "FieldSortTypeDef",
        "ColumnSort": "ColumnSortTypeDef",
    },
    total=False,
)

FieldSortTypeDef = TypedDict(
    "FieldSortTypeDef",
    {
        "FieldId": str,
        "Direction": SortDirectionType,
    },
)

_RequiredFieldTooltipItemTypeDef = TypedDict(
    "_RequiredFieldTooltipItemTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalFieldTooltipItemTypeDef = TypedDict(
    "_OptionalFieldTooltipItemTypeDef",
    {
        "Label": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

class FieldTooltipItemTypeDef(_RequiredFieldTooltipItemTypeDef, _OptionalFieldTooltipItemTypeDef):
    pass

FilledMapAggregatedFieldWellsTypeDef = TypedDict(
    "FilledMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

FilledMapConditionalFormattingOptionTypeDef = TypedDict(
    "FilledMapConditionalFormattingOptionTypeDef",
    {
        "Shape": "FilledMapShapeConditionalFormattingTypeDef",
    },
)

FilledMapConditionalFormattingTypeDef = TypedDict(
    "FilledMapConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": List["FilledMapConditionalFormattingOptionTypeDef"],
    },
)

FilledMapConfigurationTypeDef = TypedDict(
    "FilledMapConfigurationTypeDef",
    {
        "FieldWells": "FilledMapFieldWellsTypeDef",
        "SortConfiguration": "FilledMapSortConfigurationTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "WindowOptions": "GeospatialWindowOptionsTypeDef",
        "MapStyleOptions": "GeospatialMapStyleOptionsTypeDef",
    },
    total=False,
)

FilledMapFieldWellsTypeDef = TypedDict(
    "FilledMapFieldWellsTypeDef",
    {
        "FilledMapAggregatedFieldWells": "FilledMapAggregatedFieldWellsTypeDef",
    },
    total=False,
)

_RequiredFilledMapShapeConditionalFormattingTypeDef = TypedDict(
    "_RequiredFilledMapShapeConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalFilledMapShapeConditionalFormattingTypeDef = TypedDict(
    "_OptionalFilledMapShapeConditionalFormattingTypeDef",
    {
        "Format": "ShapeConditionalFormatTypeDef",
    },
    total=False,
)

class FilledMapShapeConditionalFormattingTypeDef(
    _RequiredFilledMapShapeConditionalFormattingTypeDef,
    _OptionalFilledMapShapeConditionalFormattingTypeDef,
):
    pass

FilledMapSortConfigurationTypeDef = TypedDict(
    "FilledMapSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
    },
    total=False,
)

_RequiredFilledMapVisualTypeDef = TypedDict(
    "_RequiredFilledMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFilledMapVisualTypeDef = TypedDict(
    "_OptionalFilledMapVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "FilledMapConfigurationTypeDef",
        "ConditionalFormatting": "FilledMapConditionalFormattingTypeDef",
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class FilledMapVisualTypeDef(_RequiredFilledMapVisualTypeDef, _OptionalFilledMapVisualTypeDef):
    pass

FilterControlTypeDef = TypedDict(
    "FilterControlTypeDef",
    {
        "DateTimePicker": "FilterDateTimePickerControlTypeDef",
        "List": "FilterListControlTypeDef",
        "Dropdown": "FilterDropDownControlTypeDef",
        "TextField": "FilterTextFieldControlTypeDef",
        "TextArea": "FilterTextAreaControlTypeDef",
        "Slider": "FilterSliderControlTypeDef",
        "RelativeDateTime": "FilterRelativeDateTimeControlTypeDef",
    },
    total=False,
)

_RequiredFilterDateTimePickerControlTypeDef = TypedDict(
    "_RequiredFilterDateTimePickerControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterDateTimePickerControlTypeDef = TypedDict(
    "_OptionalFilterDateTimePickerControlTypeDef",
    {
        "DisplayOptions": "DateTimePickerControlDisplayOptionsTypeDef",
        "Type": SheetControlDateTimePickerTypeType,
    },
    total=False,
)

class FilterDateTimePickerControlTypeDef(
    _RequiredFilterDateTimePickerControlTypeDef, _OptionalFilterDateTimePickerControlTypeDef
):
    pass

_RequiredFilterDropDownControlTypeDef = TypedDict(
    "_RequiredFilterDropDownControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterDropDownControlTypeDef = TypedDict(
    "_OptionalFilterDropDownControlTypeDef",
    {
        "DisplayOptions": "DropDownControlDisplayOptionsTypeDef",
        "Type": SheetControlListTypeType,
        "SelectableValues": "FilterSelectableValuesTypeDef",
        "CascadingControlConfiguration": "CascadingControlConfigurationTypeDef",
    },
    total=False,
)

class FilterDropDownControlTypeDef(
    _RequiredFilterDropDownControlTypeDef, _OptionalFilterDropDownControlTypeDef
):
    pass

_RequiredFilterGroupTypeDef = TypedDict(
    "_RequiredFilterGroupTypeDef",
    {
        "FilterGroupId": str,
        "Filters": List["FilterTypeDef"],
        "ScopeConfiguration": "FilterScopeConfigurationTypeDef",
        "CrossDataset": CrossDatasetTypesType,
    },
)
_OptionalFilterGroupTypeDef = TypedDict(
    "_OptionalFilterGroupTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)

class FilterGroupTypeDef(_RequiredFilterGroupTypeDef, _OptionalFilterGroupTypeDef):
    pass

_RequiredFilterListConfigurationTypeDef = TypedDict(
    "_RequiredFilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
    },
)
_OptionalFilterListConfigurationTypeDef = TypedDict(
    "_OptionalFilterListConfigurationTypeDef",
    {
        "CategoryValues": List[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)

class FilterListConfigurationTypeDef(
    _RequiredFilterListConfigurationTypeDef, _OptionalFilterListConfigurationTypeDef
):
    pass

_RequiredFilterListControlTypeDef = TypedDict(
    "_RequiredFilterListControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterListControlTypeDef = TypedDict(
    "_OptionalFilterListControlTypeDef",
    {
        "DisplayOptions": "ListControlDisplayOptionsTypeDef",
        "Type": SheetControlListTypeType,
        "SelectableValues": "FilterSelectableValuesTypeDef",
        "CascadingControlConfiguration": "CascadingControlConfigurationTypeDef",
    },
    total=False,
)

class FilterListControlTypeDef(
    _RequiredFilterListControlTypeDef, _OptionalFilterListControlTypeDef
):
    pass

FilterOperationSelectedFieldsConfigurationTypeDef = TypedDict(
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    {
        "SelectedFields": List[str],
        "SelectedFieldOptions": Literal["ALL_FIELDS"],
    },
    total=False,
)

FilterOperationTargetVisualsConfigurationTypeDef = TypedDict(
    "FilterOperationTargetVisualsConfigurationTypeDef",
    {
        "SameSheetTargetVisualConfiguration": "SameSheetTargetVisualConfigurationTypeDef",
    },
    total=False,
)

FilterOperationTypeDef = TypedDict(
    "FilterOperationTypeDef",
    {
        "ConditionExpression": str,
    },
)

_RequiredFilterRelativeDateTimeControlTypeDef = TypedDict(
    "_RequiredFilterRelativeDateTimeControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterRelativeDateTimeControlTypeDef = TypedDict(
    "_OptionalFilterRelativeDateTimeControlTypeDef",
    {
        "DisplayOptions": "RelativeDateTimeControlDisplayOptionsTypeDef",
    },
    total=False,
)

class FilterRelativeDateTimeControlTypeDef(
    _RequiredFilterRelativeDateTimeControlTypeDef, _OptionalFilterRelativeDateTimeControlTypeDef
):
    pass

FilterScopeConfigurationTypeDef = TypedDict(
    "FilterScopeConfigurationTypeDef",
    {
        "SelectedSheets": "SelectedSheetsFilterScopeConfigurationTypeDef",
    },
    total=False,
)

FilterSelectableValuesTypeDef = TypedDict(
    "FilterSelectableValuesTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

_RequiredFilterSliderControlTypeDef = TypedDict(
    "_RequiredFilterSliderControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
    },
)
_OptionalFilterSliderControlTypeDef = TypedDict(
    "_OptionalFilterSliderControlTypeDef",
    {
        "DisplayOptions": "SliderControlDisplayOptionsTypeDef",
        "Type": SheetControlSliderTypeType,
    },
    total=False,
)

class FilterSliderControlTypeDef(
    _RequiredFilterSliderControlTypeDef, _OptionalFilterSliderControlTypeDef
):
    pass

_RequiredFilterTextAreaControlTypeDef = TypedDict(
    "_RequiredFilterTextAreaControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterTextAreaControlTypeDef = TypedDict(
    "_OptionalFilterTextAreaControlTypeDef",
    {
        "Delimiter": str,
        "DisplayOptions": "TextAreaControlDisplayOptionsTypeDef",
    },
    total=False,
)

class FilterTextAreaControlTypeDef(
    _RequiredFilterTextAreaControlTypeDef, _OptionalFilterTextAreaControlTypeDef
):
    pass

_RequiredFilterTextFieldControlTypeDef = TypedDict(
    "_RequiredFilterTextFieldControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterTextFieldControlTypeDef = TypedDict(
    "_OptionalFilterTextFieldControlTypeDef",
    {
        "DisplayOptions": "TextFieldControlDisplayOptionsTypeDef",
    },
    total=False,
)

class FilterTextFieldControlTypeDef(
    _RequiredFilterTextFieldControlTypeDef, _OptionalFilterTextFieldControlTypeDef
):
    pass

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "CategoryFilter": "CategoryFilterTypeDef",
        "NumericRangeFilter": "NumericRangeFilterTypeDef",
        "NumericEqualityFilter": "NumericEqualityFilterTypeDef",
        "TimeEqualityFilter": "TimeEqualityFilterTypeDef",
        "TimeRangeFilter": "TimeRangeFilterTypeDef",
        "RelativeDatesFilter": "RelativeDatesFilterTypeDef",
        "TopBottomFilter": "TopBottomFilterTypeDef",
    },
    total=False,
)

FolderMemberTypeDef = TypedDict(
    "FolderMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
    total=False,
)

FolderSearchFilterTypeDef = TypedDict(
    "FolderSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": FolderFilterAttributeType,
        "Value": str,
    },
    total=False,
)

FolderSummaryTypeDef = TypedDict(
    "FolderSummaryTypeDef",
    {
        "Arn": str,
        "FolderId": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "FolderId": str,
        "Arn": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "FolderPath": List[str],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

FontConfigurationTypeDef = TypedDict(
    "FontConfigurationTypeDef",
    {
        "FontSize": "FontSizeTypeDef",
        "FontDecoration": FontDecorationType,
        "FontColor": str,
        "FontWeight": "FontWeightTypeDef",
        "FontStyle": FontStyleType,
    },
    total=False,
)

FontSizeTypeDef = TypedDict(
    "FontSizeTypeDef",
    {
        "Relative": RelativeFontSizeType,
    },
    total=False,
)

FontTypeDef = TypedDict(
    "FontTypeDef",
    {
        "FontFamily": str,
    },
    total=False,
)

FontWeightTypeDef = TypedDict(
    "FontWeightTypeDef",
    {
        "Name": FontWeightNameType,
    },
    total=False,
)

_RequiredForecastComputationTypeDef = TypedDict(
    "_RequiredForecastComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
    },
)
_OptionalForecastComputationTypeDef = TypedDict(
    "_OptionalForecastComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
        "PeriodsForward": int,
        "PeriodsBackward": int,
        "UpperBoundary": float,
        "LowerBoundary": float,
        "PredictionInterval": int,
        "Seasonality": ForecastComputationSeasonalityType,
        "CustomSeasonalityValue": int,
    },
    total=False,
)

class ForecastComputationTypeDef(
    _RequiredForecastComputationTypeDef, _OptionalForecastComputationTypeDef
):
    pass

ForecastConfigurationTypeDef = TypedDict(
    "ForecastConfigurationTypeDef",
    {
        "ForecastProperties": "TimeBasedForecastPropertiesTypeDef",
        "Scenario": "ForecastScenarioTypeDef",
    },
    total=False,
)

ForecastScenarioTypeDef = TypedDict(
    "ForecastScenarioTypeDef",
    {
        "WhatIfPointScenario": "WhatIfPointScenarioTypeDef",
        "WhatIfRangeScenario": "WhatIfRangeScenarioTypeDef",
    },
    total=False,
)

FormatConfigurationTypeDef = TypedDict(
    "FormatConfigurationTypeDef",
    {
        "StringFormatConfiguration": "StringFormatConfigurationTypeDef",
        "NumberFormatConfiguration": "NumberFormatConfigurationTypeDef",
        "DateTimeFormatConfiguration": "DateTimeFormatConfigurationTypeDef",
    },
    total=False,
)

FreeFormLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    },
    total=False,
)

_RequiredFreeFormLayoutConfigurationTypeDef = TypedDict(
    "_RequiredFreeFormLayoutConfigurationTypeDef",
    {
        "Elements": List["FreeFormLayoutElementTypeDef"],
    },
)
_OptionalFreeFormLayoutConfigurationTypeDef = TypedDict(
    "_OptionalFreeFormLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": "FreeFormLayoutCanvasSizeOptionsTypeDef",
    },
    total=False,
)

class FreeFormLayoutConfigurationTypeDef(
    _RequiredFreeFormLayoutConfigurationTypeDef, _OptionalFreeFormLayoutConfigurationTypeDef
):
    pass

FreeFormLayoutElementBackgroundStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "Color": str,
    },
    total=False,
)

FreeFormLayoutElementBorderStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBorderStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "Color": str,
    },
    total=False,
)

_RequiredFreeFormLayoutElementTypeDef = TypedDict(
    "_RequiredFreeFormLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "XAxisLocation": str,
        "YAxisLocation": str,
        "Width": str,
        "Height": str,
    },
)
_OptionalFreeFormLayoutElementTypeDef = TypedDict(
    "_OptionalFreeFormLayoutElementTypeDef",
    {
        "Visibility": VisibilityType,
        "RenderingRules": List["SheetElementRenderingRuleTypeDef"],
        "BorderStyle": "FreeFormLayoutElementBorderStyleTypeDef",
        "SelectedBorderStyle": "FreeFormLayoutElementBorderStyleTypeDef",
        "BackgroundStyle": "FreeFormLayoutElementBackgroundStyleTypeDef",
        "LoadingAnimation": "LoadingAnimationTypeDef",
    },
    total=False,
)

class FreeFormLayoutElementTypeDef(
    _RequiredFreeFormLayoutElementTypeDef, _OptionalFreeFormLayoutElementTypeDef
):
    pass

FreeFormLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "OptimizedViewPortWidth": str,
    },
)

FreeFormSectionLayoutConfigurationTypeDef = TypedDict(
    "FreeFormSectionLayoutConfigurationTypeDef",
    {
        "Elements": List["FreeFormLayoutElementTypeDef"],
    },
)

FunnelChartAggregatedFieldWellsTypeDef = TypedDict(
    "FunnelChartAggregatedFieldWellsTypeDef",
    {
        "Category": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

FunnelChartConfigurationTypeDef = TypedDict(
    "FunnelChartConfigurationTypeDef",
    {
        "FieldWells": "FunnelChartFieldWellsTypeDef",
        "SortConfiguration": "FunnelChartSortConfigurationTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ValueLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "DataLabelOptions": "FunnelChartDataLabelOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

FunnelChartDataLabelOptionsTypeDef = TypedDict(
    "FunnelChartDataLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "CategoryLabelVisibility": VisibilityType,
        "MeasureLabelVisibility": VisibilityType,
        "Position": DataLabelPositionType,
        "LabelFontConfiguration": "FontConfigurationTypeDef",
        "LabelColor": str,
        "MeasureDataLabelStyle": FunnelChartMeasureDataLabelStyleType,
    },
    total=False,
)

FunnelChartFieldWellsTypeDef = TypedDict(
    "FunnelChartFieldWellsTypeDef",
    {
        "FunnelChartAggregatedFieldWells": "FunnelChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

FunnelChartSortConfigurationTypeDef = TypedDict(
    "FunnelChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "CategoryItemsLimit": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredFunnelChartVisualTypeDef = TypedDict(
    "_RequiredFunnelChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFunnelChartVisualTypeDef = TypedDict(
    "_OptionalFunnelChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "FunnelChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class FunnelChartVisualTypeDef(
    _RequiredFunnelChartVisualTypeDef, _OptionalFunnelChartVisualTypeDef
):
    pass

GaugeChartArcConditionalFormattingTypeDef = TypedDict(
    "GaugeChartArcConditionalFormattingTypeDef",
    {
        "ForegroundColor": "ConditionalFormattingColorTypeDef",
    },
    total=False,
)

GaugeChartConditionalFormattingOptionTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": "GaugeChartPrimaryValueConditionalFormattingTypeDef",
        "Arc": "GaugeChartArcConditionalFormattingTypeDef",
    },
    total=False,
)

GaugeChartConditionalFormattingTypeDef = TypedDict(
    "GaugeChartConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": List["GaugeChartConditionalFormattingOptionTypeDef"],
    },
    total=False,
)

GaugeChartConfigurationTypeDef = TypedDict(
    "GaugeChartConfigurationTypeDef",
    {
        "FieldWells": "GaugeChartFieldWellsTypeDef",
        "GaugeChartOptions": "GaugeChartOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "TooltipOptions": "TooltipOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

GaugeChartFieldWellsTypeDef = TypedDict(
    "GaugeChartFieldWellsTypeDef",
    {
        "Values": List["MeasureFieldTypeDef"],
        "TargetValues": List["MeasureFieldTypeDef"],
    },
    total=False,
)

GaugeChartOptionsTypeDef = TypedDict(
    "GaugeChartOptionsTypeDef",
    {
        "PrimaryValueDisplayType": PrimaryValueDisplayTypeType,
        "Comparison": "ComparisonConfigurationTypeDef",
        "ArcAxis": "ArcAxisConfigurationTypeDef",
        "Arc": "ArcConfigurationTypeDef",
        "PrimaryValueFontConfiguration": "FontConfigurationTypeDef",
    },
    total=False,
)

GaugeChartPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": "ConditionalFormattingColorTypeDef",
        "Icon": "ConditionalFormattingIconTypeDef",
    },
    total=False,
)

_RequiredGaugeChartVisualTypeDef = TypedDict(
    "_RequiredGaugeChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGaugeChartVisualTypeDef = TypedDict(
    "_OptionalGaugeChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "GaugeChartConfigurationTypeDef",
        "ConditionalFormatting": "GaugeChartConditionalFormattingTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class GaugeChartVisualTypeDef(_RequiredGaugeChartVisualTypeDef, _OptionalGaugeChartVisualTypeDef):
    pass

_RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AuthorizedResourceArns": List[str],
        "ExperienceConfiguration": "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    },
)
_OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "SessionTags": List["SessionTagTypeDef"],
        "AllowedDomains": List[str],
    },
    total=False,
)

class GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef(
    _RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef,
    _OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef,
):
    pass

GenerateEmbedUrlForAnonymousUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "AnonymousUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserArn": str,
        "ExperienceConfiguration": "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    },
)
_OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "AllowedDomains": List[str],
    },
    total=False,
)

class GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef(
    _RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef,
    _OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef,
):
    pass

GenerateEmbedUrlForRegisteredUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredGeoSpatialColumnGroupTypeDef",
    {
        "Name": str,
        "Columns": List[str],
    },
)
_OptionalGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalGeoSpatialColumnGroupTypeDef",
    {
        "CountryCode": Literal["US"],
    },
    total=False,
)

class GeoSpatialColumnGroupTypeDef(
    _RequiredGeoSpatialColumnGroupTypeDef, _OptionalGeoSpatialColumnGroupTypeDef
):
    pass

GeospatialCoordinateBoundsTypeDef = TypedDict(
    "GeospatialCoordinateBoundsTypeDef",
    {
        "North": float,
        "South": float,
        "West": float,
        "East": float,
    },
)

GeospatialMapAggregatedFieldWellsTypeDef = TypedDict(
    "GeospatialMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
        "Colors": List["DimensionFieldTypeDef"],
    },
    total=False,
)

GeospatialMapConfigurationTypeDef = TypedDict(
    "GeospatialMapConfigurationTypeDef",
    {
        "FieldWells": "GeospatialMapFieldWellsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "WindowOptions": "GeospatialWindowOptionsTypeDef",
        "MapStyleOptions": "GeospatialMapStyleOptionsTypeDef",
        "PointStyleOptions": "GeospatialPointStyleOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

GeospatialMapFieldWellsTypeDef = TypedDict(
    "GeospatialMapFieldWellsTypeDef",
    {
        "GeospatialMapAggregatedFieldWells": "GeospatialMapAggregatedFieldWellsTypeDef",
    },
    total=False,
)

GeospatialMapStyleOptionsTypeDef = TypedDict(
    "GeospatialMapStyleOptionsTypeDef",
    {
        "BaseMapStyle": BaseMapStyleTypeType,
    },
    total=False,
)

_RequiredGeospatialMapVisualTypeDef = TypedDict(
    "_RequiredGeospatialMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGeospatialMapVisualTypeDef = TypedDict(
    "_OptionalGeospatialMapVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "GeospatialMapConfigurationTypeDef",
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class GeospatialMapVisualTypeDef(
    _RequiredGeospatialMapVisualTypeDef, _OptionalGeospatialMapVisualTypeDef
):
    pass

GeospatialPointStyleOptionsTypeDef = TypedDict(
    "GeospatialPointStyleOptionsTypeDef",
    {
        "SelectedPointStyle": GeospatialSelectedPointStyleType,
        "ClusterMarkerConfiguration": "ClusterMarkerConfigurationTypeDef",
    },
    total=False,
)

GeospatialWindowOptionsTypeDef = TypedDict(
    "GeospatialWindowOptionsTypeDef",
    {
        "Bounds": "GeospatialCoordinateBoundsTypeDef",
        "MapZoomMode": MapZoomModeType,
    },
    total=False,
)

_RequiredGetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "_RequiredGetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "IdentityType": EmbeddingIdentityTypeType,
    },
)
_OptionalGetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "_OptionalGetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "UndoRedoDisabled": bool,
        "ResetDisabled": bool,
        "StatePersistenceEnabled": bool,
        "UserArn": str,
        "Namespace": str,
        "AdditionalDashboardIds": List[str],
    },
    total=False,
)

class GetDashboardEmbedUrlRequestRequestTypeDef(
    _RequiredGetDashboardEmbedUrlRequestRequestTypeDef,
    _OptionalGetDashboardEmbedUrlRequestRequestTypeDef,
):
    pass

GetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "_RequiredGetSessionEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalGetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "_OptionalGetSessionEmbedUrlRequestRequestTypeDef",
    {
        "EntryPoint": str,
        "SessionLifetimeInMinutes": int,
        "UserArn": str,
    },
    total=False,
)

class GetSessionEmbedUrlRequestRequestTypeDef(
    _RequiredGetSessionEmbedUrlRequestRequestTypeDef,
    _OptionalGetSessionEmbedUrlRequestRequestTypeDef,
):
    pass

GetSessionEmbedUrlResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalTableBorderOptionsTypeDef = TypedDict(
    "GlobalTableBorderOptionsTypeDef",
    {
        "UniformBorder": "TableBorderOptionsTypeDef",
        "SideSpecificBorder": "TableSideBorderOptionsTypeDef",
    },
    total=False,
)

GradientColorTypeDef = TypedDict(
    "GradientColorTypeDef",
    {
        "Stops": List["GradientStopTypeDef"],
    },
    total=False,
)

_RequiredGradientStopTypeDef = TypedDict(
    "_RequiredGradientStopTypeDef",
    {
        "GradientOffset": float,
    },
)
_OptionalGradientStopTypeDef = TypedDict(
    "_OptionalGradientStopTypeDef",
    {
        "DataValue": float,
        "Color": str,
    },
    total=False,
)

class GradientStopTypeDef(_RequiredGradientStopTypeDef, _OptionalGradientStopTypeDef):
    pass

GridLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "GridLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": "GridLayoutScreenCanvasSizeOptionsTypeDef",
    },
    total=False,
)

_RequiredGridLayoutConfigurationTypeDef = TypedDict(
    "_RequiredGridLayoutConfigurationTypeDef",
    {
        "Elements": List["GridLayoutElementTypeDef"],
    },
)
_OptionalGridLayoutConfigurationTypeDef = TypedDict(
    "_OptionalGridLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": "GridLayoutCanvasSizeOptionsTypeDef",
    },
    total=False,
)

class GridLayoutConfigurationTypeDef(
    _RequiredGridLayoutConfigurationTypeDef, _OptionalGridLayoutConfigurationTypeDef
):
    pass

_RequiredGridLayoutElementTypeDef = TypedDict(
    "_RequiredGridLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "ColumnSpan": int,
        "RowSpan": int,
    },
)
_OptionalGridLayoutElementTypeDef = TypedDict(
    "_OptionalGridLayoutElementTypeDef",
    {
        "ColumnIndex": int,
        "RowIndex": int,
    },
    total=False,
)

class GridLayoutElementTypeDef(
    _RequiredGridLayoutElementTypeDef, _OptionalGridLayoutElementTypeDef
):
    pass

_RequiredGridLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "_RequiredGridLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "ResizeOption": ResizeOptionType,
    },
)
_OptionalGridLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "_OptionalGridLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "OptimizedViewPortWidth": str,
    },
    total=False,
)

class GridLayoutScreenCanvasSizeOptionsTypeDef(
    _RequiredGridLayoutScreenCanvasSizeOptionsTypeDef,
    _OptionalGridLayoutScreenCanvasSizeOptionsTypeDef,
):
    pass

GroupMemberTypeDef = TypedDict(
    "GroupMemberTypeDef",
    {
        "Arn": str,
        "MemberName": str,
    },
    total=False,
)

GroupSearchFilterTypeDef = TypedDict(
    "GroupSearchFilterTypeDef",
    {
        "Operator": Literal["StartsWith"],
        "Name": Literal["GROUP_NAME"],
        "Value": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Arn": str,
        "GroupName": str,
        "Description": str,
        "PrincipalId": str,
    },
    total=False,
)

_RequiredGrowthRateComputationTypeDef = TypedDict(
    "_RequiredGrowthRateComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
    },
)
_OptionalGrowthRateComputationTypeDef = TypedDict(
    "_OptionalGrowthRateComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
        "PeriodSize": int,
    },
    total=False,
)

class GrowthRateComputationTypeDef(
    _RequiredGrowthRateComputationTypeDef, _OptionalGrowthRateComputationTypeDef
):
    pass

GutterStyleTypeDef = TypedDict(
    "GutterStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

_RequiredHeaderFooterSectionConfigurationTypeDef = TypedDict(
    "_RequiredHeaderFooterSectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Layout": "SectionLayoutConfigurationTypeDef",
    },
)
_OptionalHeaderFooterSectionConfigurationTypeDef = TypedDict(
    "_OptionalHeaderFooterSectionConfigurationTypeDef",
    {
        "Style": "SectionStyleTypeDef",
    },
    total=False,
)

class HeaderFooterSectionConfigurationTypeDef(
    _RequiredHeaderFooterSectionConfigurationTypeDef,
    _OptionalHeaderFooterSectionConfigurationTypeDef,
):
    pass

HeatMapAggregatedFieldWellsTypeDef = TypedDict(
    "HeatMapAggregatedFieldWellsTypeDef",
    {
        "Rows": List["DimensionFieldTypeDef"],
        "Columns": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

HeatMapConfigurationTypeDef = TypedDict(
    "HeatMapConfigurationTypeDef",
    {
        "FieldWells": "HeatMapFieldWellsTypeDef",
        "SortConfiguration": "HeatMapSortConfigurationTypeDef",
        "RowLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColumnLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColorScale": "ColorScaleTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
    },
    total=False,
)

HeatMapFieldWellsTypeDef = TypedDict(
    "HeatMapFieldWellsTypeDef",
    {
        "HeatMapAggregatedFieldWells": "HeatMapAggregatedFieldWellsTypeDef",
    },
    total=False,
)

HeatMapSortConfigurationTypeDef = TypedDict(
    "HeatMapSortConfigurationTypeDef",
    {
        "HeatMapRowSort": List["FieldSortOptionsTypeDef"],
        "HeatMapColumnSort": List["FieldSortOptionsTypeDef"],
        "HeatMapRowItemsLimitConfiguration": "ItemsLimitConfigurationTypeDef",
        "HeatMapColumnItemsLimitConfiguration": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredHeatMapVisualTypeDef = TypedDict(
    "_RequiredHeatMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHeatMapVisualTypeDef = TypedDict(
    "_OptionalHeatMapVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "HeatMapConfigurationTypeDef",
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class HeatMapVisualTypeDef(_RequiredHeatMapVisualTypeDef, _OptionalHeatMapVisualTypeDef):
    pass

HistogramAggregatedFieldWellsTypeDef = TypedDict(
    "HistogramAggregatedFieldWellsTypeDef",
    {
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

HistogramBinOptionsTypeDef = TypedDict(
    "HistogramBinOptionsTypeDef",
    {
        "SelectedBinType": HistogramBinTypeType,
        "BinCount": "BinCountOptionsTypeDef",
        "BinWidth": "BinWidthOptionsTypeDef",
        "StartValue": float,
    },
    total=False,
)

HistogramConfigurationTypeDef = TypedDict(
    "HistogramConfigurationTypeDef",
    {
        "FieldWells": "HistogramFieldWellsTypeDef",
        "XAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "XAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "YAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "BinOptions": "HistogramBinOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

HistogramFieldWellsTypeDef = TypedDict(
    "HistogramFieldWellsTypeDef",
    {
        "HistogramAggregatedFieldWells": "HistogramAggregatedFieldWellsTypeDef",
    },
    total=False,
)

_RequiredHistogramVisualTypeDef = TypedDict(
    "_RequiredHistogramVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHistogramVisualTypeDef = TypedDict(
    "_OptionalHistogramVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "HistogramConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class HistogramVisualTypeDef(_RequiredHistogramVisualTypeDef, _OptionalHistogramVisualTypeDef):
    pass

IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
    },
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
        "AssignmentStatus": AssignmentStatusType,
    },
    total=False,
)

_RequiredIngestionTypeDef = TypedDict(
    "_RequiredIngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": IngestionStatusType,
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
        "RequestSource": IngestionRequestSourceType,
        "RequestType": IngestionRequestTypeType,
    },
    total=False,
)

class IngestionTypeDef(_RequiredIngestionTypeDef, _OptionalIngestionTypeDef):
    pass

InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": InputColumnDataTypeType,
    },
)

InsightConfigurationTypeDef = TypedDict(
    "InsightConfigurationTypeDef",
    {
        "Computations": List["ComputationTypeDef"],
        "CustomNarrative": "CustomNarrativeOptionsTypeDef",
    },
    total=False,
)

_RequiredInsightVisualTypeDef = TypedDict(
    "_RequiredInsightVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalInsightVisualTypeDef = TypedDict(
    "_OptionalInsightVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "InsightConfiguration": "InsightConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class InsightVisualTypeDef(_RequiredInsightVisualTypeDef, _OptionalInsightVisualTypeDef):
    pass

IntegerDefaultValuesTypeDef = TypedDict(
    "IntegerDefaultValuesTypeDef",
    {
        "DynamicValue": "DynamicDefaultValueTypeDef",
        "StaticValues": List[int],
    },
    total=False,
)

_RequiredIntegerParameterDeclarationTypeDef = TypedDict(
    "_RequiredIntegerParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalIntegerParameterDeclarationTypeDef = TypedDict(
    "_OptionalIntegerParameterDeclarationTypeDef",
    {
        "DefaultValues": "IntegerDefaultValuesTypeDef",
        "ValueWhenUnset": "IntegerValueWhenUnsetConfigurationTypeDef",
    },
    total=False,
)

class IntegerParameterDeclarationTypeDef(
    _RequiredIntegerParameterDeclarationTypeDef, _OptionalIntegerParameterDeclarationTypeDef
):
    pass

IntegerParameterTypeDef = TypedDict(
    "IntegerParameterTypeDef",
    {
        "Name": str,
        "Values": List[int],
    },
)

IntegerValueWhenUnsetConfigurationTypeDef = TypedDict(
    "IntegerValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": int,
    },
    total=False,
)

ItemsLimitConfigurationTypeDef = TypedDict(
    "ItemsLimitConfigurationTypeDef",
    {
        "ItemsLimit": int,
        "OtherCategories": OtherCategoriesType,
    },
    total=False,
)

JiraParametersTypeDef = TypedDict(
    "JiraParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

_RequiredJoinInstructionTypeDef = TypedDict(
    "_RequiredJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": JoinTypeType,
        "OnClause": str,
    },
)
_OptionalJoinInstructionTypeDef = TypedDict(
    "_OptionalJoinInstructionTypeDef",
    {
        "LeftJoinKeyProperties": "JoinKeyPropertiesTypeDef",
        "RightJoinKeyProperties": "JoinKeyPropertiesTypeDef",
    },
    total=False,
)

class JoinInstructionTypeDef(_RequiredJoinInstructionTypeDef, _OptionalJoinInstructionTypeDef):
    pass

JoinKeyPropertiesTypeDef = TypedDict(
    "JoinKeyPropertiesTypeDef",
    {
        "UniqueKey": bool,
    },
    total=False,
)

KPIConditionalFormattingOptionTypeDef = TypedDict(
    "KPIConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": "KPIPrimaryValueConditionalFormattingTypeDef",
        "ProgressBar": "KPIProgressBarConditionalFormattingTypeDef",
    },
    total=False,
)

KPIConditionalFormattingTypeDef = TypedDict(
    "KPIConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": List["KPIConditionalFormattingOptionTypeDef"],
    },
    total=False,
)

KPIConfigurationTypeDef = TypedDict(
    "KPIConfigurationTypeDef",
    {
        "FieldWells": "KPIFieldWellsTypeDef",
        "SortConfiguration": "KPISortConfigurationTypeDef",
        "KPIOptions": "KPIOptionsTypeDef",
    },
    total=False,
)

KPIFieldWellsTypeDef = TypedDict(
    "KPIFieldWellsTypeDef",
    {
        "Values": List["MeasureFieldTypeDef"],
        "TargetValues": List["MeasureFieldTypeDef"],
        "TrendGroups": List["DimensionFieldTypeDef"],
    },
    total=False,
)

KPIOptionsTypeDef = TypedDict(
    "KPIOptionsTypeDef",
    {
        "ProgressBar": "ProgressBarOptionsTypeDef",
        "TrendArrows": "TrendArrowOptionsTypeDef",
        "SecondaryValue": "SecondaryValueOptionsTypeDef",
        "Comparison": "ComparisonConfigurationTypeDef",
        "PrimaryValueDisplayType": PrimaryValueDisplayTypeType,
        "PrimaryValueFontConfiguration": "FontConfigurationTypeDef",
        "SecondaryValueFontConfiguration": "FontConfigurationTypeDef",
    },
    total=False,
)

KPIPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "KPIPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": "ConditionalFormattingColorTypeDef",
        "Icon": "ConditionalFormattingIconTypeDef",
    },
    total=False,
)

KPIProgressBarConditionalFormattingTypeDef = TypedDict(
    "KPIProgressBarConditionalFormattingTypeDef",
    {
        "ForegroundColor": "ConditionalFormattingColorTypeDef",
    },
    total=False,
)

KPISortConfigurationTypeDef = TypedDict(
    "KPISortConfigurationTypeDef",
    {
        "TrendGroupSort": List["FieldSortOptionsTypeDef"],
    },
    total=False,
)

_RequiredKPIVisualTypeDef = TypedDict(
    "_RequiredKPIVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalKPIVisualTypeDef = TypedDict(
    "_OptionalKPIVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "KPIConfigurationTypeDef",
        "ConditionalFormatting": "KPIConditionalFormattingTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class KPIVisualTypeDef(_RequiredKPIVisualTypeDef, _OptionalKPIVisualTypeDef):
    pass

LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": "FontConfigurationTypeDef",
        "CustomLabel": str,
    },
    total=False,
)

LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "GridLayout": "GridLayoutConfigurationTypeDef",
        "FreeFormLayout": "FreeFormLayoutConfigurationTypeDef",
        "SectionBasedLayout": "SectionBasedLayoutConfigurationTypeDef",
    },
    total=False,
)

LayoutTypeDef = TypedDict(
    "LayoutTypeDef",
    {
        "Configuration": "LayoutConfigurationTypeDef",
    },
)

LegendOptionsTypeDef = TypedDict(
    "LegendOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "Title": "LabelOptionsTypeDef",
        "Position": LegendPositionType,
        "Width": str,
        "Height": str,
    },
    total=False,
)

LineChartAggregatedFieldWellsTypeDef = TypedDict(
    "LineChartAggregatedFieldWellsTypeDef",
    {
        "Category": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
        "Colors": List["DimensionFieldTypeDef"],
        "SmallMultiples": List["DimensionFieldTypeDef"],
    },
    total=False,
)

LineChartConfigurationTypeDef = TypedDict(
    "LineChartConfigurationTypeDef",
    {
        "FieldWells": "LineChartFieldWellsTypeDef",
        "SortConfiguration": "LineChartSortConfigurationTypeDef",
        "ForecastConfigurations": List["ForecastConfigurationTypeDef"],
        "Type": LineChartTypeType,
        "SmallMultiplesOptions": "SmallMultiplesOptionsTypeDef",
        "XAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "XAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "PrimaryYAxisDisplayOptions": "LineSeriesAxisDisplayOptionsTypeDef",
        "PrimaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "SecondaryYAxisDisplayOptions": "LineSeriesAxisDisplayOptionsTypeDef",
        "SecondaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "DefaultSeriesSettings": "LineChartDefaultSeriesSettingsTypeDef",
        "Series": List["SeriesItemTypeDef"],
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "ReferenceLines": List["ReferenceLineTypeDef"],
        "Tooltip": "TooltipOptionsTypeDef",
        "ContributionAnalysisDefaults": List["ContributionAnalysisDefaultTypeDef"],
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

LineChartDefaultSeriesSettingsTypeDef = TypedDict(
    "LineChartDefaultSeriesSettingsTypeDef",
    {
        "AxisBinding": AxisBindingType,
        "LineStyleSettings": "LineChartLineStyleSettingsTypeDef",
        "MarkerStyleSettings": "LineChartMarkerStyleSettingsTypeDef",
    },
    total=False,
)

LineChartFieldWellsTypeDef = TypedDict(
    "LineChartFieldWellsTypeDef",
    {
        "LineChartAggregatedFieldWells": "LineChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

LineChartLineStyleSettingsTypeDef = TypedDict(
    "LineChartLineStyleSettingsTypeDef",
    {
        "LineVisibility": VisibilityType,
        "LineInterpolation": LineInterpolationType,
        "LineStyle": LineChartLineStyleType,
        "LineWidth": str,
    },
    total=False,
)

LineChartMarkerStyleSettingsTypeDef = TypedDict(
    "LineChartMarkerStyleSettingsTypeDef",
    {
        "MarkerVisibility": VisibilityType,
        "MarkerShape": LineChartMarkerShapeType,
        "MarkerSize": str,
        "MarkerColor": str,
    },
    total=False,
)

LineChartSeriesSettingsTypeDef = TypedDict(
    "LineChartSeriesSettingsTypeDef",
    {
        "LineStyleSettings": "LineChartLineStyleSettingsTypeDef",
        "MarkerStyleSettings": "LineChartMarkerStyleSettingsTypeDef",
    },
    total=False,
)

LineChartSortConfigurationTypeDef = TypedDict(
    "LineChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "CategoryItemsLimitConfiguration": "ItemsLimitConfigurationTypeDef",
        "ColorItemsLimitConfiguration": "ItemsLimitConfigurationTypeDef",
        "SmallMultiplesSort": List["FieldSortOptionsTypeDef"],
        "SmallMultiplesLimitConfiguration": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredLineChartVisualTypeDef = TypedDict(
    "_RequiredLineChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalLineChartVisualTypeDef = TypedDict(
    "_OptionalLineChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "LineChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class LineChartVisualTypeDef(_RequiredLineChartVisualTypeDef, _OptionalLineChartVisualTypeDef):
    pass

LineSeriesAxisDisplayOptionsTypeDef = TypedDict(
    "LineSeriesAxisDisplayOptionsTypeDef",
    {
        "AxisOptions": "AxisDisplayOptionsTypeDef",
        "MissingDataConfigurations": List["MissingDataConfigurationTypeDef"],
    },
    total=False,
)

LinkSharingConfigurationTypeDef = TypedDict(
    "LinkSharingConfigurationTypeDef",
    {
        "Permissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

_RequiredListAnalysesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAnalysesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnalysesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAnalysesRequestRequestTypeDef(
    _RequiredListAnalysesRequestRequestTypeDef, _OptionalListAnalysesRequestRequestTypeDef
):
    pass

ListAnalysesResponseTypeDef = TypedDict(
    "ListAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListControlDisplayOptionsTypeDef = TypedDict(
    "ListControlDisplayOptionsTypeDef",
    {
        "SearchOptions": "ListControlSearchOptionsTypeDef",
        "SelectAllOptions": "ListControlSelectAllOptionsTypeDef",
        "TitleOptions": "LabelOptionsTypeDef",
    },
    total=False,
)

ListControlSearchOptionsTypeDef = TypedDict(
    "ListControlSearchOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

ListControlSelectAllOptionsTypeDef = TypedDict(
    "ListControlSelectAllOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

_RequiredListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDashboardVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDashboardVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDashboardVersionsRequestRequestTypeDef(
    _RequiredListDashboardVersionsRequestRequestTypeDef,
    _OptionalListDashboardVersionsRequestRequestTypeDef,
):
    pass

ListDashboardVersionsResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List["DashboardVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDashboardsRequestRequestTypeDef = TypedDict(
    "_RequiredListDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDashboardsRequestRequestTypeDef = TypedDict(
    "_OptionalListDashboardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDashboardsRequestRequestTypeDef(
    _RequiredListDashboardsRequestRequestTypeDef, _OptionalListDashboardsRequestRequestTypeDef
):
    pass

ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDataSetsRequestRequestTypeDef(
    _RequiredListDataSetsRequestRequestTypeDef, _OptionalListDataSetsRequestRequestTypeDef
):
    pass

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List["DataSetSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "DataSources": List["DataSourceTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFolderMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListFolderMembersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalListFolderMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListFolderMembersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListFolderMembersRequestRequestTypeDef(
    _RequiredListFolderMembersRequestRequestTypeDef, _OptionalListFolderMembersRequestRequestTypeDef
):
    pass

ListFolderMembersResponseTypeDef = TypedDict(
    "ListFolderMembersResponseTypeDef",
    {
        "Status": int,
        "FolderMemberList": List["MemberIdArnPairTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFoldersRequestRequestTypeDef = TypedDict(
    "_RequiredListFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListFoldersRequestRequestTypeDef = TypedDict(
    "_OptionalListFoldersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListFoldersRequestRequestTypeDef(
    _RequiredListFoldersRequestRequestTypeDef, _OptionalListFoldersRequestRequestTypeDef
):
    pass

ListFoldersResponseTypeDef = TypedDict(
    "ListFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupMembershipsRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupMembershipsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGroupMembershipsRequestRequestTypeDef(
    _RequiredListGroupMembershipsRequestRequestTypeDef,
    _OptionalListGroupMembershipsRequestRequestTypeDef,
):
    pass

ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List["GroupMemberTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIAMPolicyAssignmentsForUserRequestRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef,
    _OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef,
):
    pass

ListIAMPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List["ActiveIAMPolicyAssignmentTypeDef"],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIAMPolicyAssignmentsRequestRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsRequestRequestTypeDef,
    _OptionalListIAMPolicyAssignmentsRequestRequestTypeDef,
):
    pass

ListIAMPolicyAssignmentsResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List["IAMPolicyAssignmentSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIngestionsRequestRequestTypeDef = TypedDict(
    "_RequiredListIngestionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
    },
)
_OptionalListIngestionsRequestRequestTypeDef = TypedDict(
    "_OptionalListIngestionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIngestionsRequestRequestTypeDef(
    _RequiredListIngestionsRequestRequestTypeDef, _OptionalListIngestionsRequestRequestTypeDef
):
    pass

ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "Ingestions": List["IngestionTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNamespacesRequestRequestTypeDef = TypedDict(
    "_RequiredListNamespacesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListNamespacesRequestRequestTypeDef = TypedDict(
    "_OptionalListNamespacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListNamespacesRequestRequestTypeDef(
    _RequiredListNamespacesRequestRequestTypeDef, _OptionalListNamespacesRequestRequestTypeDef
):
    pass

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceInfoV2TypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateAliasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTemplateAliasesRequestRequestTypeDef(
    _RequiredListTemplateAliasesRequestRequestTypeDef,
    _OptionalListTemplateAliasesRequestRequestTypeDef,
):
    pass

ListTemplateAliasesResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List["TemplateAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTemplateVersionsRequestRequestTypeDef(
    _RequiredListTemplateVersionsRequestRequestTypeDef,
    _OptionalListTemplateVersionsRequestRequestTypeDef,
):
    pass

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List["TemplateVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplatesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTemplatesRequestRequestTypeDef(
    _RequiredListTemplatesRequestRequestTypeDef, _OptionalListTemplatesRequestRequestTypeDef
):
    pass

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List["TemplateSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemeAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemeAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemeAliasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListThemeAliasesRequestRequestTypeDef(
    _RequiredListThemeAliasesRequestRequestTypeDef, _OptionalListThemeAliasesRequestRequestTypeDef
):
    pass

ListThemeAliasesResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseTypeDef",
    {
        "ThemeAliasList": List["ThemeAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListThemeVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListThemeVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListThemeVersionsRequestRequestTypeDef(
    _RequiredListThemeVersionsRequestRequestTypeDef, _OptionalListThemeVersionsRequestRequestTypeDef
):
    pass

ListThemeVersionsResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseTypeDef",
    {
        "ThemeVersionSummaryList": List["ThemeVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListThemesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Type": ThemeTypeType,
    },
    total=False,
)

class ListThemesRequestRequestTypeDef(
    _RequiredListThemesRequestRequestTypeDef, _OptionalListThemesRequestRequestTypeDef
):
    pass

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "ThemeSummaryList": List["ThemeSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserGroupsRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUserGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUserGroupsRequestRequestTypeDef(
    _RequiredListUserGroupsRequestRequestTypeDef, _OptionalListUserGroupsRequestRequestTypeDef
):
    pass

ListUserGroupsResponseTypeDef = TypedDict(
    "ListUserGroupsResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserList": List["UserTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadingAnimationTypeDef = TypedDict(
    "LoadingAnimationTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

LocalNavigationConfigurationTypeDef = TypedDict(
    "LocalNavigationConfigurationTypeDef",
    {
        "TargetSheetId": str,
    },
)

LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {
        "JoinInstruction": "JoinInstructionTypeDef",
        "PhysicalTableId": str,
        "DataSetArn": str,
    },
    total=False,
)

_RequiredLogicalTableTypeDef = TypedDict(
    "_RequiredLogicalTableTypeDef",
    {
        "Alias": str,
        "Source": "LogicalTableSourceTypeDef",
    },
)
_OptionalLogicalTableTypeDef = TypedDict(
    "_OptionalLogicalTableTypeDef",
    {
        "DataTransforms": List["TransformOperationTypeDef"],
    },
    total=False,
)

class LogicalTableTypeDef(_RequiredLogicalTableTypeDef, _OptionalLogicalTableTypeDef):
    pass

LongFormatTextTypeDef = TypedDict(
    "LongFormatTextTypeDef",
    {
        "PlainText": str,
        "RichText": str,
    },
    total=False,
)

ManifestFileLocationTypeDef = TypedDict(
    "ManifestFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

MarginStyleTypeDef = TypedDict(
    "MarginStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

MaximumLabelTypeTypeDef = TypedDict(
    "MaximumLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

_RequiredMaximumMinimumComputationTypeDef = TypedDict(
    "_RequiredMaximumMinimumComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
        "Type": MaximumMinimumComputationTypeType,
    },
)
_OptionalMaximumMinimumComputationTypeDef = TypedDict(
    "_OptionalMaximumMinimumComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
    },
    total=False,
)

class MaximumMinimumComputationTypeDef(
    _RequiredMaximumMinimumComputationTypeDef, _OptionalMaximumMinimumComputationTypeDef
):
    pass

MeasureFieldTypeDef = TypedDict(
    "MeasureFieldTypeDef",
    {
        "NumericalMeasureField": "NumericalMeasureFieldTypeDef",
        "CategoricalMeasureField": "CategoricalMeasureFieldTypeDef",
        "DateMeasureField": "DateMeasureFieldTypeDef",
        "CalculatedMeasureField": "CalculatedMeasureFieldTypeDef",
    },
    total=False,
)

MemberIdArnPairTypeDef = TypedDict(
    "MemberIdArnPairTypeDef",
    {
        "MemberId": str,
        "MemberArn": str,
    },
    total=False,
)

_RequiredMetricComparisonComputationTypeDef = TypedDict(
    "_RequiredMetricComparisonComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
        "FromValue": "MeasureFieldTypeDef",
        "TargetValue": "MeasureFieldTypeDef",
    },
)
_OptionalMetricComparisonComputationTypeDef = TypedDict(
    "_OptionalMetricComparisonComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class MetricComparisonComputationTypeDef(
    _RequiredMetricComparisonComputationTypeDef, _OptionalMetricComparisonComputationTypeDef
):
    pass

MinimumLabelTypeTypeDef = TypedDict(
    "MinimumLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

MissingDataConfigurationTypeDef = TypedDict(
    "MissingDataConfigurationTypeDef",
    {
        "TreatmentOption": MissingDataTreatmentOptionType,
    },
    total=False,
)

MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {
        "Type": NamespaceErrorTypeType,
        "Message": str,
    },
    total=False,
)

NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": str,
        "Arn": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "NamespaceError": "NamespaceErrorTypeDef",
    },
    total=False,
)

NegativeValueConfigurationTypeDef = TypedDict(
    "NegativeValueConfigurationTypeDef",
    {
        "DisplayMode": NegativeValueDisplayModeType,
    },
)

NullValueFormatConfigurationTypeDef = TypedDict(
    "NullValueFormatConfigurationTypeDef",
    {
        "NullString": str,
    },
)

NumberDisplayFormatConfigurationTypeDef = TypedDict(
    "NumberDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": "NumericSeparatorConfigurationTypeDef",
        "DecimalPlacesConfiguration": "DecimalPlacesConfigurationTypeDef",
        "NumberScale": NumberScaleType,
        "NegativeValueConfiguration": "NegativeValueConfigurationTypeDef",
        "NullValueFormatConfiguration": "NullValueFormatConfigurationTypeDef",
    },
    total=False,
)

NumberFormatConfigurationTypeDef = TypedDict(
    "NumberFormatConfigurationTypeDef",
    {
        "FormatConfiguration": "NumericFormatConfigurationTypeDef",
    },
    total=False,
)

NumericAxisOptionsTypeDef = TypedDict(
    "NumericAxisOptionsTypeDef",
    {
        "Scale": "AxisScaleTypeDef",
        "Range": "AxisDisplayRangeTypeDef",
    },
    total=False,
)

NumericEqualityDrillDownFilterTypeDef = TypedDict(
    "NumericEqualityDrillDownFilterTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
        "Value": float,
    },
)

_RequiredNumericEqualityFilterTypeDef = TypedDict(
    "_RequiredNumericEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
        "MatchOperator": NumericEqualityMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalNumericEqualityFilterTypeDef = TypedDict(
    "_OptionalNumericEqualityFilterTypeDef",
    {
        "Value": float,
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "AggregationFunction": "AggregationFunctionTypeDef",
        "ParameterName": str,
    },
    total=False,
)

class NumericEqualityFilterTypeDef(
    _RequiredNumericEqualityFilterTypeDef, _OptionalNumericEqualityFilterTypeDef
):
    pass

NumericFormatConfigurationTypeDef = TypedDict(
    "NumericFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": "NumberDisplayFormatConfigurationTypeDef",
        "CurrencyDisplayFormatConfiguration": "CurrencyDisplayFormatConfigurationTypeDef",
        "PercentageDisplayFormatConfiguration": "PercentageDisplayFormatConfigurationTypeDef",
    },
    total=False,
)

_RequiredNumericRangeFilterTypeDef = TypedDict(
    "_RequiredNumericRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
        "NullOption": FilterNullOptionType,
    },
)
_OptionalNumericRangeFilterTypeDef = TypedDict(
    "_OptionalNumericRangeFilterTypeDef",
    {
        "IncludeMinimum": bool,
        "IncludeMaximum": bool,
        "RangeMinimum": "NumericRangeFilterValueTypeDef",
        "RangeMaximum": "NumericRangeFilterValueTypeDef",
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "AggregationFunction": "AggregationFunctionTypeDef",
    },
    total=False,
)

class NumericRangeFilterTypeDef(
    _RequiredNumericRangeFilterTypeDef, _OptionalNumericRangeFilterTypeDef
):
    pass

NumericRangeFilterValueTypeDef = TypedDict(
    "NumericRangeFilterValueTypeDef",
    {
        "StaticValue": float,
        "Parameter": str,
    },
    total=False,
)

NumericSeparatorConfigurationTypeDef = TypedDict(
    "NumericSeparatorConfigurationTypeDef",
    {
        "DecimalSeparator": NumericSeparatorSymbolType,
        "ThousandsSeparator": "ThousandSeparatorOptionsTypeDef",
    },
    total=False,
)

NumericalAggregationFunctionTypeDef = TypedDict(
    "NumericalAggregationFunctionTypeDef",
    {
        "SimpleNumericalAggregation": SimpleNumericalAggregationFunctionType,
        "PercentileAggregation": "PercentileAggregationTypeDef",
    },
    total=False,
)

_RequiredNumericalDimensionFieldTypeDef = TypedDict(
    "_RequiredNumericalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalNumericalDimensionFieldTypeDef = TypedDict(
    "_OptionalNumericalDimensionFieldTypeDef",
    {
        "HierarchyId": str,
        "FormatConfiguration": "NumberFormatConfigurationTypeDef",
    },
    total=False,
)

class NumericalDimensionFieldTypeDef(
    _RequiredNumericalDimensionFieldTypeDef, _OptionalNumericalDimensionFieldTypeDef
):
    pass

_RequiredNumericalMeasureFieldTypeDef = TypedDict(
    "_RequiredNumericalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalNumericalMeasureFieldTypeDef = TypedDict(
    "_OptionalNumericalMeasureFieldTypeDef",
    {
        "AggregationFunction": "NumericalAggregationFunctionTypeDef",
        "FormatConfiguration": "NumberFormatConfigurationTypeDef",
    },
    total=False,
)

class NumericalMeasureFieldTypeDef(
    _RequiredNumericalMeasureFieldTypeDef, _OptionalNumericalMeasureFieldTypeDef
):
    pass

OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ColumnDataTypeType,
    },
    total=False,
)

PaginationConfigurationTypeDef = TypedDict(
    "PaginationConfigurationTypeDef",
    {
        "PageSize": int,
        "PageNumber": int,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PanelConfigurationTypeDef = TypedDict(
    "PanelConfigurationTypeDef",
    {
        "Title": "PanelTitleOptionsTypeDef",
        "BorderVisibility": VisibilityType,
        "BorderThickness": str,
        "BorderStyle": PanelBorderStyleType,
        "BorderColor": str,
        "GutterVisibility": VisibilityType,
        "GutterSpacing": str,
        "BackgroundVisibility": VisibilityType,
        "BackgroundColor": str,
    },
    total=False,
)

PanelTitleOptionsTypeDef = TypedDict(
    "PanelTitleOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": "FontConfigurationTypeDef",
        "HorizontalTextAlignment": HorizontalTextAlignmentType,
    },
    total=False,
)

ParameterControlTypeDef = TypedDict(
    "ParameterControlTypeDef",
    {
        "DateTimePicker": "ParameterDateTimePickerControlTypeDef",
        "List": "ParameterListControlTypeDef",
        "Dropdown": "ParameterDropDownControlTypeDef",
        "TextField": "ParameterTextFieldControlTypeDef",
        "TextArea": "ParameterTextAreaControlTypeDef",
        "Slider": "ParameterSliderControlTypeDef",
    },
    total=False,
)

_RequiredParameterDateTimePickerControlTypeDef = TypedDict(
    "_RequiredParameterDateTimePickerControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterDateTimePickerControlTypeDef = TypedDict(
    "_OptionalParameterDateTimePickerControlTypeDef",
    {
        "DisplayOptions": "DateTimePickerControlDisplayOptionsTypeDef",
    },
    total=False,
)

class ParameterDateTimePickerControlTypeDef(
    _RequiredParameterDateTimePickerControlTypeDef, _OptionalParameterDateTimePickerControlTypeDef
):
    pass

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "StringParameterDeclaration": "StringParameterDeclarationTypeDef",
        "DecimalParameterDeclaration": "DecimalParameterDeclarationTypeDef",
        "IntegerParameterDeclaration": "IntegerParameterDeclarationTypeDef",
        "DateTimeParameterDeclaration": "DateTimeParameterDeclarationTypeDef",
    },
    total=False,
)

_RequiredParameterDropDownControlTypeDef = TypedDict(
    "_RequiredParameterDropDownControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterDropDownControlTypeDef = TypedDict(
    "_OptionalParameterDropDownControlTypeDef",
    {
        "DisplayOptions": "DropDownControlDisplayOptionsTypeDef",
        "Type": SheetControlListTypeType,
        "SelectableValues": "ParameterSelectableValuesTypeDef",
        "CascadingControlConfiguration": "CascadingControlConfigurationTypeDef",
    },
    total=False,
)

class ParameterDropDownControlTypeDef(
    _RequiredParameterDropDownControlTypeDef, _OptionalParameterDropDownControlTypeDef
):
    pass

_RequiredParameterListControlTypeDef = TypedDict(
    "_RequiredParameterListControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterListControlTypeDef = TypedDict(
    "_OptionalParameterListControlTypeDef",
    {
        "DisplayOptions": "ListControlDisplayOptionsTypeDef",
        "Type": SheetControlListTypeType,
        "SelectableValues": "ParameterSelectableValuesTypeDef",
        "CascadingControlConfiguration": "CascadingControlConfigurationTypeDef",
    },
    total=False,
)

class ParameterListControlTypeDef(
    _RequiredParameterListControlTypeDef, _OptionalParameterListControlTypeDef
):
    pass

ParameterSelectableValuesTypeDef = TypedDict(
    "ParameterSelectableValuesTypeDef",
    {
        "Values": List[str],
        "LinkToDataSetColumn": "ColumnIdentifierTypeDef",
    },
    total=False,
)

_RequiredParameterSliderControlTypeDef = TypedDict(
    "_RequiredParameterSliderControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
    },
)
_OptionalParameterSliderControlTypeDef = TypedDict(
    "_OptionalParameterSliderControlTypeDef",
    {
        "DisplayOptions": "SliderControlDisplayOptionsTypeDef",
    },
    total=False,
)

class ParameterSliderControlTypeDef(
    _RequiredParameterSliderControlTypeDef, _OptionalParameterSliderControlTypeDef
):
    pass

_RequiredParameterTextAreaControlTypeDef = TypedDict(
    "_RequiredParameterTextAreaControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterTextAreaControlTypeDef = TypedDict(
    "_OptionalParameterTextAreaControlTypeDef",
    {
        "Delimiter": str,
        "DisplayOptions": "TextAreaControlDisplayOptionsTypeDef",
    },
    total=False,
)

class ParameterTextAreaControlTypeDef(
    _RequiredParameterTextAreaControlTypeDef, _OptionalParameterTextAreaControlTypeDef
):
    pass

_RequiredParameterTextFieldControlTypeDef = TypedDict(
    "_RequiredParameterTextFieldControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterTextFieldControlTypeDef = TypedDict(
    "_OptionalParameterTextFieldControlTypeDef",
    {
        "DisplayOptions": "TextFieldControlDisplayOptionsTypeDef",
    },
    total=False,
)

class ParameterTextFieldControlTypeDef(
    _RequiredParameterTextFieldControlTypeDef, _OptionalParameterTextFieldControlTypeDef
):
    pass

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

PercentVisibleRangeTypeDef = TypedDict(
    "PercentVisibleRangeTypeDef",
    {
        "From": float,
        "To": float,
    },
    total=False,
)

PercentageDisplayFormatConfigurationTypeDef = TypedDict(
    "PercentageDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": "NumericSeparatorConfigurationTypeDef",
        "DecimalPlacesConfiguration": "DecimalPlacesConfigurationTypeDef",
        "NegativeValueConfiguration": "NegativeValueConfigurationTypeDef",
        "NullValueFormatConfiguration": "NullValueFormatConfigurationTypeDef",
    },
    total=False,
)

PercentileAggregationTypeDef = TypedDict(
    "PercentileAggregationTypeDef",
    {
        "PercentileValue": float,
    },
    total=False,
)

_RequiredPeriodOverPeriodComputationTypeDef = TypedDict(
    "_RequiredPeriodOverPeriodComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
    },
)
_OptionalPeriodOverPeriodComputationTypeDef = TypedDict(
    "_OptionalPeriodOverPeriodComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
    },
    total=False,
)

class PeriodOverPeriodComputationTypeDef(
    _RequiredPeriodOverPeriodComputationTypeDef, _OptionalPeriodOverPeriodComputationTypeDef
):
    pass

_RequiredPeriodToDateComputationTypeDef = TypedDict(
    "_RequiredPeriodToDateComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
    },
)
_OptionalPeriodToDateComputationTypeDef = TypedDict(
    "_OptionalPeriodToDateComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
        "PeriodTimeGranularity": TimeGranularityType,
    },
    total=False,
)

class PeriodToDateComputationTypeDef(
    _RequiredPeriodToDateComputationTypeDef, _OptionalPeriodToDateComputationTypeDef
):
    pass

PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": "RelationalTableTypeDef",
        "CustomSql": "CustomSqlTypeDef",
        "S3Source": "S3SourceTypeDef",
    },
    total=False,
)

PieChartAggregatedFieldWellsTypeDef = TypedDict(
    "PieChartAggregatedFieldWellsTypeDef",
    {
        "Category": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
        "SmallMultiples": List["DimensionFieldTypeDef"],
    },
    total=False,
)

PieChartConfigurationTypeDef = TypedDict(
    "PieChartConfigurationTypeDef",
    {
        "FieldWells": "PieChartFieldWellsTypeDef",
        "SortConfiguration": "PieChartSortConfigurationTypeDef",
        "DonutOptions": "DonutOptionsTypeDef",
        "SmallMultiplesOptions": "SmallMultiplesOptionsTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ValueLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
        "ContributionAnalysisDefaults": List["ContributionAnalysisDefaultTypeDef"],
    },
    total=False,
)

PieChartFieldWellsTypeDef = TypedDict(
    "PieChartFieldWellsTypeDef",
    {
        "PieChartAggregatedFieldWells": "PieChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

PieChartSortConfigurationTypeDef = TypedDict(
    "PieChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "CategoryItemsLimit": "ItemsLimitConfigurationTypeDef",
        "SmallMultiplesSort": List["FieldSortOptionsTypeDef"],
        "SmallMultiplesLimitConfiguration": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredPieChartVisualTypeDef = TypedDict(
    "_RequiredPieChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPieChartVisualTypeDef = TypedDict(
    "_OptionalPieChartVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "PieChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class PieChartVisualTypeDef(_RequiredPieChartVisualTypeDef, _OptionalPieChartVisualTypeDef):
    pass

PivotFieldSortOptionsTypeDef = TypedDict(
    "PivotFieldSortOptionsTypeDef",
    {
        "FieldId": str,
        "SortBy": "PivotTableSortByTypeDef",
    },
)

PivotTableAggregatedFieldWellsTypeDef = TypedDict(
    "PivotTableAggregatedFieldWellsTypeDef",
    {
        "Rows": List["DimensionFieldTypeDef"],
        "Columns": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

_RequiredPivotTableCellConditionalFormattingTypeDef = TypedDict(
    "_RequiredPivotTableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalPivotTableCellConditionalFormattingTypeDef = TypedDict(
    "_OptionalPivotTableCellConditionalFormattingTypeDef",
    {
        "TextFormat": "TextConditionalFormatTypeDef",
        "Scope": "PivotTableConditionalFormattingScopeTypeDef",
    },
    total=False,
)

class PivotTableCellConditionalFormattingTypeDef(
    _RequiredPivotTableCellConditionalFormattingTypeDef,
    _OptionalPivotTableCellConditionalFormattingTypeDef,
):
    pass

PivotTableConditionalFormattingOptionTypeDef = TypedDict(
    "PivotTableConditionalFormattingOptionTypeDef",
    {
        "Cell": "PivotTableCellConditionalFormattingTypeDef",
    },
    total=False,
)

PivotTableConditionalFormattingScopeTypeDef = TypedDict(
    "PivotTableConditionalFormattingScopeTypeDef",
    {
        "Role": PivotTableConditionalFormattingScopeRoleType,
    },
    total=False,
)

PivotTableConditionalFormattingTypeDef = TypedDict(
    "PivotTableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": List["PivotTableConditionalFormattingOptionTypeDef"],
    },
    total=False,
)

PivotTableConfigurationTypeDef = TypedDict(
    "PivotTableConfigurationTypeDef",
    {
        "FieldWells": "PivotTableFieldWellsTypeDef",
        "SortConfiguration": "PivotTableSortConfigurationTypeDef",
        "TableOptions": "PivotTableOptionsTypeDef",
        "TotalOptions": "PivotTableTotalOptionsTypeDef",
        "FieldOptions": "PivotTableFieldOptionsTypeDef",
        "PaginatedReportOptions": "PivotTablePaginatedReportOptionsTypeDef",
    },
    total=False,
)

_RequiredPivotTableDataPathOptionTypeDef = TypedDict(
    "_RequiredPivotTableDataPathOptionTypeDef",
    {
        "DataPathList": List["DataPathValueTypeDef"],
    },
)
_OptionalPivotTableDataPathOptionTypeDef = TypedDict(
    "_OptionalPivotTableDataPathOptionTypeDef",
    {
        "Width": str,
    },
    total=False,
)

class PivotTableDataPathOptionTypeDef(
    _RequiredPivotTableDataPathOptionTypeDef, _OptionalPivotTableDataPathOptionTypeDef
):
    pass

_RequiredPivotTableFieldOptionTypeDef = TypedDict(
    "_RequiredPivotTableFieldOptionTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalPivotTableFieldOptionTypeDef = TypedDict(
    "_OptionalPivotTableFieldOptionTypeDef",
    {
        "CustomLabel": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

class PivotTableFieldOptionTypeDef(
    _RequiredPivotTableFieldOptionTypeDef, _OptionalPivotTableFieldOptionTypeDef
):
    pass

PivotTableFieldOptionsTypeDef = TypedDict(
    "PivotTableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": List["PivotTableFieldOptionTypeDef"],
        "DataPathOptions": List["PivotTableDataPathOptionTypeDef"],
    },
    total=False,
)

PivotTableFieldSubtotalOptionsTypeDef = TypedDict(
    "PivotTableFieldSubtotalOptionsTypeDef",
    {
        "FieldId": str,
    },
    total=False,
)

PivotTableFieldWellsTypeDef = TypedDict(
    "PivotTableFieldWellsTypeDef",
    {
        "PivotTableAggregatedFieldWells": "PivotTableAggregatedFieldWellsTypeDef",
    },
    total=False,
)

PivotTableOptionsTypeDef = TypedDict(
    "PivotTableOptionsTypeDef",
    {
        "MetricPlacement": PivotTableMetricPlacementType,
        "SingleMetricVisibility": VisibilityType,
        "ColumnNamesVisibility": VisibilityType,
        "ToggleButtonsVisibility": VisibilityType,
        "ColumnHeaderStyle": "TableCellStyleTypeDef",
        "RowHeaderStyle": "TableCellStyleTypeDef",
        "CellStyle": "TableCellStyleTypeDef",
        "RowFieldNamesStyle": "TableCellStyleTypeDef",
        "RowAlternateColorOptions": "RowAlternateColorOptionsTypeDef",
    },
    total=False,
)

PivotTablePaginatedReportOptionsTypeDef = TypedDict(
    "PivotTablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": VisibilityType,
        "OverflowColumnHeaderVisibility": VisibilityType,
    },
    total=False,
)

PivotTableSortByTypeDef = TypedDict(
    "PivotTableSortByTypeDef",
    {
        "Field": "FieldSortTypeDef",
        "Column": "ColumnSortTypeDef",
        "DataPath": "DataPathSortTypeDef",
    },
    total=False,
)

PivotTableSortConfigurationTypeDef = TypedDict(
    "PivotTableSortConfigurationTypeDef",
    {
        "FieldSortOptions": List["PivotFieldSortOptionsTypeDef"],
    },
    total=False,
)

PivotTableTotalOptionsTypeDef = TypedDict(
    "PivotTableTotalOptionsTypeDef",
    {
        "RowSubtotalOptions": "SubtotalOptionsTypeDef",
        "ColumnSubtotalOptions": "SubtotalOptionsTypeDef",
        "RowTotalOptions": "PivotTotalOptionsTypeDef",
        "ColumnTotalOptions": "PivotTotalOptionsTypeDef",
    },
    total=False,
)

_RequiredPivotTableVisualTypeDef = TypedDict(
    "_RequiredPivotTableVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPivotTableVisualTypeDef = TypedDict(
    "_OptionalPivotTableVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "PivotTableConfigurationTypeDef",
        "ConditionalFormatting": "PivotTableConditionalFormattingTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class PivotTableVisualTypeDef(_RequiredPivotTableVisualTypeDef, _OptionalPivotTableVisualTypeDef):
    pass

PivotTotalOptionsTypeDef = TypedDict(
    "PivotTotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "Placement": TableTotalsPlacementType,
        "ScrollStatus": TableTotalsScrollStatusType,
        "CustomLabel": str,
        "TotalCellStyle": "TableCellStyleTypeDef",
        "ValueCellStyle": "TableCellStyleTypeDef",
        "MetricHeaderCellStyle": "TableCellStyleTypeDef",
    },
    total=False,
)

PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

_RequiredPredefinedHierarchyTypeDef = TypedDict(
    "_RequiredPredefinedHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": List["ColumnIdentifierTypeDef"],
    },
)
_OptionalPredefinedHierarchyTypeDef = TypedDict(
    "_OptionalPredefinedHierarchyTypeDef",
    {
        "DrillDownFilters": List["DrillDownFilterTypeDef"],
    },
    total=False,
)

class PredefinedHierarchyTypeDef(
    _RequiredPredefinedHierarchyTypeDef, _OptionalPredefinedHierarchyTypeDef
):
    pass

PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)

ProgressBarOptionsTypeDef = TypedDict(
    "ProgressBarOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

ProjectOperationTypeDef = TypedDict(
    "ProjectOperationTypeDef",
    {
        "ProjectedColumns": List[str],
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "WaitingOnIngestion": str,
        "QueuedIngestion": str,
    },
)

RangeEndsLabelTypeTypeDef = TypedDict(
    "RangeEndsLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

RdsParametersTypeDef = TypedDict(
    "RdsParametersTypeDef",
    {
        "InstanceId": str,
        "Database": str,
    },
)

_RequiredRedshiftParametersTypeDef = TypedDict(
    "_RequiredRedshiftParametersTypeDef",
    {
        "Database": str,
    },
)
_OptionalRedshiftParametersTypeDef = TypedDict(
    "_OptionalRedshiftParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "ClusterId": str,
    },
    total=False,
)

class RedshiftParametersTypeDef(
    _RequiredRedshiftParametersTypeDef, _OptionalRedshiftParametersTypeDef
):
    pass

ReferenceLineCustomLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineCustomLabelConfigurationTypeDef",
    {
        "CustomLabel": str,
    },
)

ReferenceLineDataConfigurationTypeDef = TypedDict(
    "ReferenceLineDataConfigurationTypeDef",
    {
        "StaticConfiguration": "ReferenceLineStaticDataConfigurationTypeDef",
        "DynamicConfiguration": "ReferenceLineDynamicDataConfigurationTypeDef",
        "AxisBinding": AxisBindingType,
    },
    total=False,
)

ReferenceLineDynamicDataConfigurationTypeDef = TypedDict(
    "ReferenceLineDynamicDataConfigurationTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
        "MeasureAggregationFunction": "AggregationFunctionTypeDef",
        "Calculation": "NumericalAggregationFunctionTypeDef",
    },
)

ReferenceLineLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineLabelConfigurationTypeDef",
    {
        "ValueLabelConfiguration": "ReferenceLineValueLabelConfigurationTypeDef",
        "CustomLabelConfiguration": "ReferenceLineCustomLabelConfigurationTypeDef",
        "FontConfiguration": "FontConfigurationTypeDef",
        "FontColor": str,
        "HorizontalPosition": ReferenceLineLabelHorizontalPositionType,
        "VerticalPosition": ReferenceLineLabelVerticalPositionType,
    },
    total=False,
)

ReferenceLineStaticDataConfigurationTypeDef = TypedDict(
    "ReferenceLineStaticDataConfigurationTypeDef",
    {
        "Value": float,
    },
)

ReferenceLineStyleConfigurationTypeDef = TypedDict(
    "ReferenceLineStyleConfigurationTypeDef",
    {
        "Pattern": ReferenceLinePatternTypeType,
        "Color": str,
    },
    total=False,
)

_RequiredReferenceLineTypeDef = TypedDict(
    "_RequiredReferenceLineTypeDef",
    {
        "DataConfiguration": "ReferenceLineDataConfigurationTypeDef",
    },
)
_OptionalReferenceLineTypeDef = TypedDict(
    "_OptionalReferenceLineTypeDef",
    {
        "Status": WidgetStatusType,
        "StyleConfiguration": "ReferenceLineStyleConfigurationTypeDef",
        "LabelConfiguration": "ReferenceLineLabelConfigurationTypeDef",
    },
    total=False,
)

class ReferenceLineTypeDef(_RequiredReferenceLineTypeDef, _OptionalReferenceLineTypeDef):
    pass

ReferenceLineValueLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineValueLabelConfigurationTypeDef",
    {
        "RelativePosition": ReferenceLineValueLabelRelativePositionType,
        "FormatConfiguration": "NumericFormatConfigurationTypeDef",
    },
    total=False,
)

_RequiredRegisterUserRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterUserRequestRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "Email": str,
        "UserRole": UserRoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalRegisterUserRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterUserRequestRequestTypeDef",
    {
        "IamArn": str,
        "SessionName": str,
        "UserName": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)

class RegisterUserRequestRequestTypeDef(
    _RequiredRegisterUserRequestRequestTypeDef, _OptionalRegisterUserRequestRequestTypeDef
):
    pass

RegisterUserResponseTypeDef = TypedDict(
    "RegisterUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisteredUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)

RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": "DashboardVisualIdTypeDef",
    },
)

RegisteredUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
        "QuickSightConsole": "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
        "QSearchBar": "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
        "DashboardVisual": "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    },
    total=False,
)

RegisteredUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
    total=False,
)

RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    {
        "InitialPath": str,
    },
    total=False,
)

_RequiredRelationalTableTypeDef = TypedDict(
    "_RequiredRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": List["InputColumnTypeDef"],
    },
)
_OptionalRelationalTableTypeDef = TypedDict(
    "_OptionalRelationalTableTypeDef",
    {
        "Catalog": str,
        "Schema": str,
    },
    total=False,
)

class RelationalTableTypeDef(_RequiredRelationalTableTypeDef, _OptionalRelationalTableTypeDef):
    pass

RelativeDateTimeControlDisplayOptionsTypeDef = TypedDict(
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    {
        "TitleOptions": "LabelOptionsTypeDef",
        "DateTimeFormat": str,
    },
    total=False,
)

_RequiredRelativeDatesFilterTypeDef = TypedDict(
    "_RequiredRelativeDatesFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
        "AnchorDateConfiguration": "AnchorDateConfigurationTypeDef",
        "TimeGranularity": TimeGranularityType,
        "RelativeDateType": RelativeDateTypeType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalRelativeDatesFilterTypeDef = TypedDict(
    "_OptionalRelativeDatesFilterTypeDef",
    {
        "MinimumGranularity": TimeGranularityType,
        "RelativeDateValue": int,
        "ParameterName": str,
        "ExcludePeriodConfiguration": "ExcludePeriodConfigurationTypeDef",
    },
    total=False,
)

class RelativeDatesFilterTypeDef(
    _RequiredRelativeDatesFilterTypeDef, _OptionalRelativeDatesFilterTypeDef
):
    pass

RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnName": str,
    },
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "Principal": str,
        "Actions": List[str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RestoreAnalysisRequestRequestTypeDef = TypedDict(
    "RestoreAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

RestoreAnalysisResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRollingDateConfigurationTypeDef = TypedDict(
    "_RequiredRollingDateConfigurationTypeDef",
    {
        "Expression": str,
    },
)
_OptionalRollingDateConfigurationTypeDef = TypedDict(
    "_OptionalRollingDateConfigurationTypeDef",
    {
        "DataSetIdentifier": str,
    },
    total=False,
)

class RollingDateConfigurationTypeDef(
    _RequiredRollingDateConfigurationTypeDef, _OptionalRollingDateConfigurationTypeDef
):
    pass

RowAlternateColorOptionsTypeDef = TypedDict(
    "RowAlternateColorOptionsTypeDef",
    {
        "Status": WidgetStatusType,
        "RowAlternateColors": List[str],
    },
    total=False,
)

RowInfoTypeDef = TypedDict(
    "RowInfoTypeDef",
    {
        "RowsIngested": int,
        "RowsDropped": int,
        "TotalRowsInDataset": int,
    },
    total=False,
)

_RequiredRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredRowLevelPermissionDataSetTypeDef",
    {
        "Arn": str,
        "PermissionPolicy": RowLevelPermissionPolicyType,
    },
)
_OptionalRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalRowLevelPermissionDataSetTypeDef",
    {
        "Namespace": str,
        "FormatVersion": RowLevelPermissionFormatVersionType,
        "Status": StatusType,
    },
    total=False,
)

class RowLevelPermissionDataSetTypeDef(
    _RequiredRowLevelPermissionDataSetTypeDef, _OptionalRowLevelPermissionDataSetTypeDef
):
    pass

_RequiredRowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "_RequiredRowLevelPermissionTagConfigurationTypeDef",
    {
        "TagRules": List["RowLevelPermissionTagRuleTypeDef"],
    },
)
_OptionalRowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "_OptionalRowLevelPermissionTagConfigurationTypeDef",
    {
        "Status": StatusType,
    },
    total=False,
)

class RowLevelPermissionTagConfigurationTypeDef(
    _RequiredRowLevelPermissionTagConfigurationTypeDef,
    _OptionalRowLevelPermissionTagConfigurationTypeDef,
):
    pass

_RequiredRowLevelPermissionTagRuleTypeDef = TypedDict(
    "_RequiredRowLevelPermissionTagRuleTypeDef",
    {
        "TagKey": str,
        "ColumnName": str,
    },
)
_OptionalRowLevelPermissionTagRuleTypeDef = TypedDict(
    "_OptionalRowLevelPermissionTagRuleTypeDef",
    {
        "TagMultiValueDelimiter": str,
        "MatchAllValue": str,
    },
    total=False,
)

class RowLevelPermissionTagRuleTypeDef(
    _RequiredRowLevelPermissionTagRuleTypeDef, _OptionalRowLevelPermissionTagRuleTypeDef
):
    pass

S3ParametersTypeDef = TypedDict(
    "S3ParametersTypeDef",
    {
        "ManifestFileLocation": "ManifestFileLocationTypeDef",
    },
)

_RequiredS3SourceTypeDef = TypedDict(
    "_RequiredS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": List["InputColumnTypeDef"],
    },
)
_OptionalS3SourceTypeDef = TypedDict(
    "_OptionalS3SourceTypeDef",
    {
        "UploadSettings": "UploadSettingsTypeDef",
    },
    total=False,
)

class S3SourceTypeDef(_RequiredS3SourceTypeDef, _OptionalS3SourceTypeDef):
    pass

SameSheetTargetVisualConfigurationTypeDef = TypedDict(
    "SameSheetTargetVisualConfigurationTypeDef",
    {
        "TargetVisuals": List[str],
        "TargetVisualOptions": Literal["ALL_VISUALS"],
    },
    total=False,
)

SankeyDiagramAggregatedFieldWellsTypeDef = TypedDict(
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    {
        "Source": List["DimensionFieldTypeDef"],
        "Destination": List["DimensionFieldTypeDef"],
        "Weight": List["MeasureFieldTypeDef"],
    },
    total=False,
)

SankeyDiagramChartConfigurationTypeDef = TypedDict(
    "SankeyDiagramChartConfigurationTypeDef",
    {
        "FieldWells": "SankeyDiagramFieldWellsTypeDef",
        "SortConfiguration": "SankeyDiagramSortConfigurationTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
    },
    total=False,
)

SankeyDiagramFieldWellsTypeDef = TypedDict(
    "SankeyDiagramFieldWellsTypeDef",
    {
        "SankeyDiagramAggregatedFieldWells": "SankeyDiagramAggregatedFieldWellsTypeDef",
    },
    total=False,
)

SankeyDiagramSortConfigurationTypeDef = TypedDict(
    "SankeyDiagramSortConfigurationTypeDef",
    {
        "WeightSort": List["FieldSortOptionsTypeDef"],
        "SourceItemsLimit": "ItemsLimitConfigurationTypeDef",
        "DestinationItemsLimit": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredSankeyDiagramVisualTypeDef = TypedDict(
    "_RequiredSankeyDiagramVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalSankeyDiagramVisualTypeDef = TypedDict(
    "_OptionalSankeyDiagramVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "SankeyDiagramChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class SankeyDiagramVisualTypeDef(
    _RequiredSankeyDiagramVisualTypeDef, _OptionalSankeyDiagramVisualTypeDef
):
    pass

ScatterPlotCategoricallyAggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    {
        "XAxis": List["MeasureFieldTypeDef"],
        "YAxis": List["MeasureFieldTypeDef"],
        "Category": List["DimensionFieldTypeDef"],
        "Size": List["MeasureFieldTypeDef"],
    },
    total=False,
)

ScatterPlotConfigurationTypeDef = TypedDict(
    "ScatterPlotConfigurationTypeDef",
    {
        "FieldWells": "ScatterPlotFieldWellsTypeDef",
        "XAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "XAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "YAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "YAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

ScatterPlotFieldWellsTypeDef = TypedDict(
    "ScatterPlotFieldWellsTypeDef",
    {
        "ScatterPlotCategoricallyAggregatedFieldWells": "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
        "ScatterPlotUnaggregatedFieldWells": "ScatterPlotUnaggregatedFieldWellsTypeDef",
    },
    total=False,
)

ScatterPlotUnaggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    {
        "XAxis": List["DimensionFieldTypeDef"],
        "YAxis": List["DimensionFieldTypeDef"],
        "Size": List["MeasureFieldTypeDef"],
    },
    total=False,
)

_RequiredScatterPlotVisualTypeDef = TypedDict(
    "_RequiredScatterPlotVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalScatterPlotVisualTypeDef = TypedDict(
    "_OptionalScatterPlotVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "ScatterPlotConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class ScatterPlotVisualTypeDef(
    _RequiredScatterPlotVisualTypeDef, _OptionalScatterPlotVisualTypeDef
):
    pass

ScrollBarOptionsTypeDef = TypedDict(
    "ScrollBarOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "VisibleRange": "VisibleRangeOptionsTypeDef",
    },
    total=False,
)

_RequiredSearchAnalysesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["AnalysisSearchFilterTypeDef"],
    },
)
_OptionalSearchAnalysesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAnalysesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchAnalysesRequestRequestTypeDef(
    _RequiredSearchAnalysesRequestRequestTypeDef, _OptionalSearchAnalysesRequestRequestTypeDef
):
    pass

SearchAnalysesResponseTypeDef = TypedDict(
    "SearchAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchDashboardsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["DashboardSearchFilterTypeDef"],
    },
)
_OptionalSearchDashboardsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDashboardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchDashboardsRequestRequestTypeDef(
    _RequiredSearchDashboardsRequestRequestTypeDef, _OptionalSearchDashboardsRequestRequestTypeDef
):
    pass

SearchDashboardsResponseTypeDef = TypedDict(
    "SearchDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchDataSetsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["DataSetSearchFilterTypeDef"],
    },
)
_OptionalSearchDataSetsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDataSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchDataSetsRequestRequestTypeDef(
    _RequiredSearchDataSetsRequestRequestTypeDef, _OptionalSearchDataSetsRequestRequestTypeDef
):
    pass

SearchDataSetsResponseTypeDef = TypedDict(
    "SearchDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List["DataSetSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["DataSourceSearchFilterTypeDef"],
    },
)
_OptionalSearchDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDataSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchDataSourcesRequestRequestTypeDef(
    _RequiredSearchDataSourcesRequestRequestTypeDef, _OptionalSearchDataSourcesRequestRequestTypeDef
):
    pass

SearchDataSourcesResponseTypeDef = TypedDict(
    "SearchDataSourcesResponseTypeDef",
    {
        "DataSourceSummaries": List["DataSourceSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchFoldersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": List["FolderSearchFilterTypeDef"],
    },
)
_OptionalSearchFoldersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchFoldersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchFoldersRequestRequestTypeDef(
    _RequiredSearchFoldersRequestRequestTypeDef, _OptionalSearchFoldersRequestRequestTypeDef
):
    pass

SearchFoldersResponseTypeDef = TypedDict(
    "SearchFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "Filters": List["GroupSearchFilterTypeDef"],
    },
)
_OptionalSearchGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class SearchGroupsRequestRequestTypeDef(
    _RequiredSearchGroupsRequestRequestTypeDef, _OptionalSearchGroupsRequestRequestTypeDef
):
    pass

SearchGroupsResponseTypeDef = TypedDict(
    "SearchGroupsResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecondaryValueOptionsTypeDef = TypedDict(
    "SecondaryValueOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

SectionAfterPageBreakTypeDef = TypedDict(
    "SectionAfterPageBreakTypeDef",
    {
        "Status": SectionPageBreakStatusType,
    },
    total=False,
)

SectionBasedLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    {
        "PaperCanvasSizeOptions": "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    },
    total=False,
)

SectionBasedLayoutConfigurationTypeDef = TypedDict(
    "SectionBasedLayoutConfigurationTypeDef",
    {
        "HeaderSections": List["HeaderFooterSectionConfigurationTypeDef"],
        "BodySections": List["BodySectionConfigurationTypeDef"],
        "FooterSections": List["HeaderFooterSectionConfigurationTypeDef"],
        "CanvasSizeOptions": "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    },
)

SectionBasedLayoutPaperCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    {
        "PaperSize": PaperSizeType,
        "PaperOrientation": PaperOrientationType,
        "PaperMargin": "SpacingTypeDef",
    },
    total=False,
)

SectionLayoutConfigurationTypeDef = TypedDict(
    "SectionLayoutConfigurationTypeDef",
    {
        "FreeFormLayout": "FreeFormSectionLayoutConfigurationTypeDef",
    },
)

SectionPageBreakConfigurationTypeDef = TypedDict(
    "SectionPageBreakConfigurationTypeDef",
    {
        "After": "SectionAfterPageBreakTypeDef",
    },
    total=False,
)

SectionStyleTypeDef = TypedDict(
    "SectionStyleTypeDef",
    {
        "Height": str,
        "Padding": "SpacingTypeDef",
    },
    total=False,
)

SelectedSheetsFilterScopeConfigurationTypeDef = TypedDict(
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    {
        "SheetVisualScopingConfigurations": List["SheetVisualScopingConfigurationTypeDef"],
    },
    total=False,
)

SeriesItemTypeDef = TypedDict(
    "SeriesItemTypeDef",
    {
        "FieldSeriesItem": "FieldSeriesItemTypeDef",
        "DataFieldSeriesItem": "DataFieldSeriesItemTypeDef",
    },
    total=False,
)

ServiceNowParametersTypeDef = TypedDict(
    "ServiceNowParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

SessionTagTypeDef = TypedDict(
    "SessionTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SetParameterValueConfigurationTypeDef = TypedDict(
    "SetParameterValueConfigurationTypeDef",
    {
        "DestinationParameterName": str,
        "Value": "DestinationParameterValueConfigurationTypeDef",
    },
)

ShapeConditionalFormatTypeDef = TypedDict(
    "ShapeConditionalFormatTypeDef",
    {
        "BackgroundColor": "ConditionalFormattingColorTypeDef",
    },
)

SheetControlLayoutConfigurationTypeDef = TypedDict(
    "SheetControlLayoutConfigurationTypeDef",
    {
        "GridLayout": "GridLayoutConfigurationTypeDef",
    },
    total=False,
)

SheetControlLayoutTypeDef = TypedDict(
    "SheetControlLayoutTypeDef",
    {
        "Configuration": "SheetControlLayoutConfigurationTypeDef",
    },
)

SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef",
    {
        "VisibilityState": DashboardUIStateType,
    },
    total=False,
)

_RequiredSheetDefinitionTypeDef = TypedDict(
    "_RequiredSheetDefinitionTypeDef",
    {
        "SheetId": str,
    },
)
_OptionalSheetDefinitionTypeDef = TypedDict(
    "_OptionalSheetDefinitionTypeDef",
    {
        "Title": str,
        "Description": str,
        "Name": str,
        "ParameterControls": List["ParameterControlTypeDef"],
        "FilterControls": List["FilterControlTypeDef"],
        "Visuals": List["VisualTypeDef"],
        "TextBoxes": List["SheetTextBoxTypeDef"],
        "Layouts": List["LayoutTypeDef"],
        "SheetControlLayouts": List["SheetControlLayoutTypeDef"],
        "ContentType": SheetContentTypeType,
    },
    total=False,
)

class SheetDefinitionTypeDef(_RequiredSheetDefinitionTypeDef, _OptionalSheetDefinitionTypeDef):
    pass

SheetElementConfigurationOverridesTypeDef = TypedDict(
    "SheetElementConfigurationOverridesTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

SheetElementRenderingRuleTypeDef = TypedDict(
    "SheetElementRenderingRuleTypeDef",
    {
        "Expression": str,
        "ConfigurationOverrides": "SheetElementConfigurationOverridesTypeDef",
    },
)

SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {
        "Tile": "TileStyleTypeDef",
        "TileLayout": "TileLayoutStyleTypeDef",
    },
    total=False,
)

_RequiredSheetTextBoxTypeDef = TypedDict(
    "_RequiredSheetTextBoxTypeDef",
    {
        "SheetTextBoxId": str,
    },
)
_OptionalSheetTextBoxTypeDef = TypedDict(
    "_OptionalSheetTextBoxTypeDef",
    {
        "Content": str,
    },
    total=False,
)

class SheetTextBoxTypeDef(_RequiredSheetTextBoxTypeDef, _OptionalSheetTextBoxTypeDef):
    pass

SheetTypeDef = TypedDict(
    "SheetTypeDef",
    {
        "SheetId": str,
        "Name": str,
    },
    total=False,
)

_RequiredSheetVisualScopingConfigurationTypeDef = TypedDict(
    "_RequiredSheetVisualScopingConfigurationTypeDef",
    {
        "SheetId": str,
        "Scope": FilterVisualScopeType,
    },
)
_OptionalSheetVisualScopingConfigurationTypeDef = TypedDict(
    "_OptionalSheetVisualScopingConfigurationTypeDef",
    {
        "VisualIds": List[str],
    },
    total=False,
)

class SheetVisualScopingConfigurationTypeDef(
    _RequiredSheetVisualScopingConfigurationTypeDef, _OptionalSheetVisualScopingConfigurationTypeDef
):
    pass

ShortFormatTextTypeDef = TypedDict(
    "ShortFormatTextTypeDef",
    {
        "PlainText": str,
        "RichText": str,
    },
    total=False,
)

SignupResponseTypeDef = TypedDict(
    "SignupResponseTypeDef",
    {
        "IAMUser": bool,
        "userLoginName": str,
        "accountName": str,
        "directoryType": str,
    },
    total=False,
)

SimpleClusterMarkerTypeDef = TypedDict(
    "SimpleClusterMarkerTypeDef",
    {
        "Color": str,
    },
    total=False,
)

SliderControlDisplayOptionsTypeDef = TypedDict(
    "SliderControlDisplayOptionsTypeDef",
    {
        "TitleOptions": "LabelOptionsTypeDef",
    },
    total=False,
)

SmallMultiplesOptionsTypeDef = TypedDict(
    "SmallMultiplesOptionsTypeDef",
    {
        "MaxVisibleRows": int,
        "MaxVisibleColumns": int,
        "PanelConfiguration": "PanelConfigurationTypeDef",
    },
    total=False,
)

SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef",
    {
        "Host": str,
        "Database": str,
        "Warehouse": str,
    },
)

SpacingTypeDef = TypedDict(
    "SpacingTypeDef",
    {
        "Top": str,
        "Bottom": str,
        "Left": str,
        "Right": str,
    },
    total=False,
)

SparkParametersTypeDef = TypedDict(
    "SparkParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

SslPropertiesTypeDef = TypedDict(
    "SslPropertiesTypeDef",
    {
        "DisableSsl": bool,
    },
    total=False,
)

StringDefaultValuesTypeDef = TypedDict(
    "StringDefaultValuesTypeDef",
    {
        "DynamicValue": "DynamicDefaultValueTypeDef",
        "StaticValues": List[str],
    },
    total=False,
)

StringFormatConfigurationTypeDef = TypedDict(
    "StringFormatConfigurationTypeDef",
    {
        "NullValueFormatConfiguration": "NullValueFormatConfigurationTypeDef",
        "NumericFormatConfiguration": "NumericFormatConfigurationTypeDef",
    },
    total=False,
)

_RequiredStringParameterDeclarationTypeDef = TypedDict(
    "_RequiredStringParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalStringParameterDeclarationTypeDef = TypedDict(
    "_OptionalStringParameterDeclarationTypeDef",
    {
        "DefaultValues": "StringDefaultValuesTypeDef",
        "ValueWhenUnset": "StringValueWhenUnsetConfigurationTypeDef",
    },
    total=False,
)

class StringParameterDeclarationTypeDef(
    _RequiredStringParameterDeclarationTypeDef, _OptionalStringParameterDeclarationTypeDef
):
    pass

StringParameterTypeDef = TypedDict(
    "StringParameterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

StringValueWhenUnsetConfigurationTypeDef = TypedDict(
    "StringValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": str,
    },
    total=False,
)

SubtotalOptionsTypeDef = TypedDict(
    "SubtotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "CustomLabel": str,
        "FieldLevel": PivotTableSubtotalLevelType,
        "FieldLevelOptions": List["PivotTableFieldSubtotalOptionsTypeDef"],
        "TotalCellStyle": "TableCellStyleTypeDef",
        "ValueCellStyle": "TableCellStyleTypeDef",
        "MetricHeaderCellStyle": "TableCellStyleTypeDef",
    },
    total=False,
)

TableAggregatedFieldWellsTypeDef = TypedDict(
    "TableAggregatedFieldWellsTypeDef",
    {
        "GroupBy": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
    },
    total=False,
)

TableBorderOptionsTypeDef = TypedDict(
    "TableBorderOptionsTypeDef",
    {
        "Color": str,
        "Thickness": int,
        "Style": TableBorderStyleType,
    },
    total=False,
)

_RequiredTableCellConditionalFormattingTypeDef = TypedDict(
    "_RequiredTableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalTableCellConditionalFormattingTypeDef = TypedDict(
    "_OptionalTableCellConditionalFormattingTypeDef",
    {
        "TextFormat": "TextConditionalFormatTypeDef",
    },
    total=False,
)

class TableCellConditionalFormattingTypeDef(
    _RequiredTableCellConditionalFormattingTypeDef, _OptionalTableCellConditionalFormattingTypeDef
):
    pass

TableCellImageSizingConfigurationTypeDef = TypedDict(
    "TableCellImageSizingConfigurationTypeDef",
    {
        "TableCellImageScalingConfiguration": TableCellImageScalingConfigurationType,
    },
    total=False,
)

TableCellStyleTypeDef = TypedDict(
    "TableCellStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": "FontConfigurationTypeDef",
        "TextWrap": TextWrapType,
        "HorizontalTextAlignment": HorizontalTextAlignmentType,
        "VerticalTextAlignment": VerticalTextAlignmentType,
        "BackgroundColor": str,
        "Height": int,
        "Border": "GlobalTableBorderOptionsTypeDef",
    },
    total=False,
)

TableConditionalFormattingOptionTypeDef = TypedDict(
    "TableConditionalFormattingOptionTypeDef",
    {
        "Cell": "TableCellConditionalFormattingTypeDef",
        "Row": "TableRowConditionalFormattingTypeDef",
    },
    total=False,
)

TableConditionalFormattingTypeDef = TypedDict(
    "TableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": List["TableConditionalFormattingOptionTypeDef"],
    },
    total=False,
)

TableConfigurationTypeDef = TypedDict(
    "TableConfigurationTypeDef",
    {
        "FieldWells": "TableFieldWellsTypeDef",
        "SortConfiguration": "TableSortConfigurationTypeDef",
        "TableOptions": "TableOptionsTypeDef",
        "TotalOptions": "TotalOptionsTypeDef",
        "FieldOptions": "TableFieldOptionsTypeDef",
        "PaginatedReportOptions": "TablePaginatedReportOptionsTypeDef",
    },
    total=False,
)

TableFieldCustomIconContentTypeDef = TypedDict(
    "TableFieldCustomIconContentTypeDef",
    {
        "Icon": Literal["LINK"],
    },
    total=False,
)

_RequiredTableFieldCustomTextContentTypeDef = TypedDict(
    "_RequiredTableFieldCustomTextContentTypeDef",
    {
        "FontConfiguration": "FontConfigurationTypeDef",
    },
)
_OptionalTableFieldCustomTextContentTypeDef = TypedDict(
    "_OptionalTableFieldCustomTextContentTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TableFieldCustomTextContentTypeDef(
    _RequiredTableFieldCustomTextContentTypeDef, _OptionalTableFieldCustomTextContentTypeDef
):
    pass

TableFieldImageConfigurationTypeDef = TypedDict(
    "TableFieldImageConfigurationTypeDef",
    {
        "SizingOptions": "TableCellImageSizingConfigurationTypeDef",
    },
    total=False,
)

TableFieldLinkConfigurationTypeDef = TypedDict(
    "TableFieldLinkConfigurationTypeDef",
    {
        "Target": URLTargetConfigurationType,
        "Content": "TableFieldLinkContentConfigurationTypeDef",
    },
)

TableFieldLinkContentConfigurationTypeDef = TypedDict(
    "TableFieldLinkContentConfigurationTypeDef",
    {
        "CustomTextContent": "TableFieldCustomTextContentTypeDef",
        "CustomIconContent": "TableFieldCustomIconContentTypeDef",
    },
    total=False,
)

_RequiredTableFieldOptionTypeDef = TypedDict(
    "_RequiredTableFieldOptionTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalTableFieldOptionTypeDef = TypedDict(
    "_OptionalTableFieldOptionTypeDef",
    {
        "Width": str,
        "CustomLabel": str,
        "Visibility": VisibilityType,
        "URLStyling": "TableFieldURLConfigurationTypeDef",
    },
    total=False,
)

class TableFieldOptionTypeDef(_RequiredTableFieldOptionTypeDef, _OptionalTableFieldOptionTypeDef):
    pass

TableFieldOptionsTypeDef = TypedDict(
    "TableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": List["TableFieldOptionTypeDef"],
        "Order": List[str],
    },
    total=False,
)

TableFieldURLConfigurationTypeDef = TypedDict(
    "TableFieldURLConfigurationTypeDef",
    {
        "LinkConfiguration": "TableFieldLinkConfigurationTypeDef",
        "ImageConfiguration": "TableFieldImageConfigurationTypeDef",
    },
    total=False,
)

TableFieldWellsTypeDef = TypedDict(
    "TableFieldWellsTypeDef",
    {
        "TableAggregatedFieldWells": "TableAggregatedFieldWellsTypeDef",
        "TableUnaggregatedFieldWells": "TableUnaggregatedFieldWellsTypeDef",
    },
    total=False,
)

TableOptionsTypeDef = TypedDict(
    "TableOptionsTypeDef",
    {
        "Orientation": TableOrientationType,
        "HeaderStyle": "TableCellStyleTypeDef",
        "CellStyle": "TableCellStyleTypeDef",
        "RowAlternateColorOptions": "RowAlternateColorOptionsTypeDef",
    },
    total=False,
)

TablePaginatedReportOptionsTypeDef = TypedDict(
    "TablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": VisibilityType,
        "OverflowColumnHeaderVisibility": VisibilityType,
    },
    total=False,
)

TableRowConditionalFormattingTypeDef = TypedDict(
    "TableRowConditionalFormattingTypeDef",
    {
        "BackgroundColor": "ConditionalFormattingColorTypeDef",
        "TextColor": "ConditionalFormattingColorTypeDef",
    },
    total=False,
)

TableSideBorderOptionsTypeDef = TypedDict(
    "TableSideBorderOptionsTypeDef",
    {
        "InnerVertical": "TableBorderOptionsTypeDef",
        "InnerHorizontal": "TableBorderOptionsTypeDef",
        "Left": "TableBorderOptionsTypeDef",
        "Right": "TableBorderOptionsTypeDef",
        "Top": "TableBorderOptionsTypeDef",
        "Bottom": "TableBorderOptionsTypeDef",
    },
    total=False,
)

TableSortConfigurationTypeDef = TypedDict(
    "TableSortConfigurationTypeDef",
    {
        "RowSort": List["FieldSortOptionsTypeDef"],
        "PaginationConfiguration": "PaginationConfigurationTypeDef",
    },
    total=False,
)

TableUnaggregatedFieldWellsTypeDef = TypedDict(
    "TableUnaggregatedFieldWellsTypeDef",
    {
        "Values": List["UnaggregatedFieldTypeDef"],
    },
    total=False,
)

_RequiredTableVisualTypeDef = TypedDict(
    "_RequiredTableVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTableVisualTypeDef = TypedDict(
    "_OptionalTableVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "TableConfigurationTypeDef",
        "ConditionalFormatting": "TableConditionalFormattingTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
    },
    total=False,
)

class TableVisualTypeDef(_RequiredTableVisualTypeDef, _OptionalTableVisualTypeDef):
    pass

TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List["ColumnTagTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "TemplateVersionNumber": int,
    },
    total=False,
)

TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": TemplateErrorTypeType,
        "Message": str,
        "ViolatedEntities": List["EntityTypeDef"],
    },
    total=False,
)

TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {
        "Arn": str,
        "DataSetReferences": List["DataSetReferenceTypeDef"],
    },
)

TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": "TemplateSourceAnalysisTypeDef",
        "SourceTemplate": "TemplateSourceTemplateTypeDef",
    },
    total=False,
)

TemplateSourceTemplateTypeDef = TypedDict(
    "TemplateSourceTemplateTypeDef",
    {
        "Arn": str,
    },
)

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

_RequiredTemplateVersionDefinitionTypeDef = TypedDict(
    "_RequiredTemplateVersionDefinitionTypeDef",
    {
        "DataSetConfigurations": List["DataSetConfigurationTypeDef"],
    },
)
_OptionalTemplateVersionDefinitionTypeDef = TypedDict(
    "_OptionalTemplateVersionDefinitionTypeDef",
    {
        "Sheets": List["SheetDefinitionTypeDef"],
        "CalculatedFields": List["CalculatedFieldTypeDef"],
        "ParameterDeclarations": List["ParameterDeclarationTypeDef"],
        "FilterGroups": List["FilterGroupTypeDef"],
        "ColumnConfigurations": List["ColumnConfigurationTypeDef"],
        "AnalysisDefaults": "AnalysisDefaultsTypeDef",
    },
    total=False,
)

class TemplateVersionDefinitionTypeDef(
    _RequiredTemplateVersionDefinitionTypeDef, _OptionalTemplateVersionDefinitionTypeDef
):
    pass

TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": ResourceStatusType,
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
        "Status": ResourceStatusType,
        "DataSetConfigurations": List["DataSetConfigurationTypeDef"],
        "Description": str,
        "SourceEntityArn": str,
        "ThemeArn": str,
        "Sheets": List["SheetTypeDef"],
    },
    total=False,
)

TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

TextAreaControlDisplayOptionsTypeDef = TypedDict(
    "TextAreaControlDisplayOptionsTypeDef",
    {
        "TitleOptions": "LabelOptionsTypeDef",
        "PlaceholderOptions": "TextControlPlaceholderOptionsTypeDef",
    },
    total=False,
)

TextConditionalFormatTypeDef = TypedDict(
    "TextConditionalFormatTypeDef",
    {
        "BackgroundColor": "ConditionalFormattingColorTypeDef",
        "TextColor": "ConditionalFormattingColorTypeDef",
        "Icon": "ConditionalFormattingIconTypeDef",
    },
    total=False,
)

TextControlPlaceholderOptionsTypeDef = TypedDict(
    "TextControlPlaceholderOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

TextFieldControlDisplayOptionsTypeDef = TypedDict(
    "TextFieldControlDisplayOptionsTypeDef",
    {
        "TitleOptions": "LabelOptionsTypeDef",
        "PlaceholderOptions": "TextControlPlaceholderOptionsTypeDef",
    },
    total=False,
)

ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef",
    {
        "Arn": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
    total=False,
)

ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": "DataColorPaletteTypeDef",
        "UIColorPalette": "UIColorPaletteTypeDef",
        "Sheet": "SheetStyleTypeDef",
        "Typography": "TypographyTypeDef",
    },
    total=False,
)

ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef",
    {
        "Type": Literal["INTERNAL_FAILURE"],
        "Message": str,
    },
    total=False,
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
        "Type": ThemeTypeType,
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
        "Status": ResourceStatusType,
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
        "Status": ResourceStatusType,
    },
    total=False,
)

ThousandSeparatorOptionsTypeDef = TypedDict(
    "ThousandSeparatorOptionsTypeDef",
    {
        "Symbol": NumericSeparatorSymbolType,
        "Visibility": VisibilityType,
    },
    total=False,
)

TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {
        "Gutter": "GutterStyleTypeDef",
        "Margin": "MarginStyleTypeDef",
    },
    total=False,
)

TileStyleTypeDef = TypedDict(
    "TileStyleTypeDef",
    {
        "Border": "BorderStyleTypeDef",
    },
    total=False,
)

TimeBasedForecastPropertiesTypeDef = TypedDict(
    "TimeBasedForecastPropertiesTypeDef",
    {
        "PeriodsForward": int,
        "PeriodsBackward": int,
        "UpperBoundary": float,
        "LowerBoundary": float,
        "PredictionInterval": int,
        "Seasonality": int,
    },
    total=False,
)

_RequiredTimeEqualityFilterTypeDef = TypedDict(
    "_RequiredTimeEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalTimeEqualityFilterTypeDef = TypedDict(
    "_OptionalTimeEqualityFilterTypeDef",
    {
        "Value": Union[datetime, str],
        "ParameterName": str,
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)

class TimeEqualityFilterTypeDef(
    _RequiredTimeEqualityFilterTypeDef, _OptionalTimeEqualityFilterTypeDef
):
    pass

TimeRangeDrillDownFilterTypeDef = TypedDict(
    "TimeRangeDrillDownFilterTypeDef",
    {
        "Column": "ColumnIdentifierTypeDef",
        "RangeMinimum": Union[datetime, str],
        "RangeMaximum": Union[datetime, str],
        "TimeGranularity": TimeGranularityType,
    },
)

_RequiredTimeRangeFilterTypeDef = TypedDict(
    "_RequiredTimeRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
        "NullOption": FilterNullOptionType,
    },
)
_OptionalTimeRangeFilterTypeDef = TypedDict(
    "_OptionalTimeRangeFilterTypeDef",
    {
        "IncludeMinimum": bool,
        "IncludeMaximum": bool,
        "RangeMinimumValue": "TimeRangeFilterValueTypeDef",
        "RangeMaximumValue": "TimeRangeFilterValueTypeDef",
        "ExcludePeriodConfiguration": "ExcludePeriodConfigurationTypeDef",
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)

class TimeRangeFilterTypeDef(_RequiredTimeRangeFilterTypeDef, _OptionalTimeRangeFilterTypeDef):
    pass

TimeRangeFilterValueTypeDef = TypedDict(
    "TimeRangeFilterValueTypeDef",
    {
        "StaticValue": Union[datetime, str],
        "RollingDate": "RollingDateConfigurationTypeDef",
        "Parameter": str,
    },
    total=False,
)

TooltipItemTypeDef = TypedDict(
    "TooltipItemTypeDef",
    {
        "FieldTooltipItem": "FieldTooltipItemTypeDef",
        "ColumnTooltipItem": "ColumnTooltipItemTypeDef",
    },
    total=False,
)

TooltipOptionsTypeDef = TypedDict(
    "TooltipOptionsTypeDef",
    {
        "TooltipVisibility": VisibilityType,
        "SelectedTooltipType": SelectedTooltipTypeType,
        "FieldBasedTooltip": "FieldBasedTooltipTypeDef",
    },
    total=False,
)

_RequiredTopBottomFilterTypeDef = TypedDict(
    "_RequiredTopBottomFilterTypeDef",
    {
        "FilterId": str,
        "Column": "ColumnIdentifierTypeDef",
        "AggregationSortConfigurations": List["AggregationSortConfigurationTypeDef"],
    },
)
_OptionalTopBottomFilterTypeDef = TypedDict(
    "_OptionalTopBottomFilterTypeDef",
    {
        "Limit": int,
        "TimeGranularity": TimeGranularityType,
        "ParameterName": str,
    },
    total=False,
)

class TopBottomFilterTypeDef(_RequiredTopBottomFilterTypeDef, _OptionalTopBottomFilterTypeDef):
    pass

_RequiredTopBottomMoversComputationTypeDef = TypedDict(
    "_RequiredTopBottomMoversComputationTypeDef",
    {
        "ComputationId": str,
        "Time": "DimensionFieldTypeDef",
        "Category": "DimensionFieldTypeDef",
        "Type": TopBottomComputationTypeType,
    },
)
_OptionalTopBottomMoversComputationTypeDef = TypedDict(
    "_OptionalTopBottomMoversComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
        "MoverSize": int,
        "SortOrder": TopBottomSortOrderType,
    },
    total=False,
)

class TopBottomMoversComputationTypeDef(
    _RequiredTopBottomMoversComputationTypeDef, _OptionalTopBottomMoversComputationTypeDef
):
    pass

_RequiredTopBottomRankedComputationTypeDef = TypedDict(
    "_RequiredTopBottomRankedComputationTypeDef",
    {
        "ComputationId": str,
        "Category": "DimensionFieldTypeDef",
        "Type": TopBottomComputationTypeType,
    },
)
_OptionalTopBottomRankedComputationTypeDef = TypedDict(
    "_OptionalTopBottomRankedComputationTypeDef",
    {
        "Name": str,
        "Value": "MeasureFieldTypeDef",
        "ResultSize": int,
    },
    total=False,
)

class TopBottomRankedComputationTypeDef(
    _RequiredTopBottomRankedComputationTypeDef, _OptionalTopBottomRankedComputationTypeDef
):
    pass

_RequiredTotalAggregationComputationTypeDef = TypedDict(
    "_RequiredTotalAggregationComputationTypeDef",
    {
        "ComputationId": str,
        "Value": "MeasureFieldTypeDef",
    },
)
_OptionalTotalAggregationComputationTypeDef = TypedDict(
    "_OptionalTotalAggregationComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class TotalAggregationComputationTypeDef(
    _RequiredTotalAggregationComputationTypeDef, _OptionalTotalAggregationComputationTypeDef
):
    pass

TotalOptionsTypeDef = TypedDict(
    "TotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "Placement": TableTotalsPlacementType,
        "ScrollStatus": TableTotalsScrollStatusType,
        "CustomLabel": str,
        "TotalCellStyle": "TableCellStyleTypeDef",
    },
    total=False,
)

TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": "ProjectOperationTypeDef",
        "FilterOperation": "FilterOperationTypeDef",
        "CreateColumnsOperation": "CreateColumnsOperationTypeDef",
        "RenameColumnOperation": "RenameColumnOperationTypeDef",
        "CastColumnTypeOperation": "CastColumnTypeOperationTypeDef",
        "TagColumnOperation": "TagColumnOperationTypeDef",
        "UntagColumnOperation": "UntagColumnOperationTypeDef",
    },
    total=False,
)

TreeMapAggregatedFieldWellsTypeDef = TypedDict(
    "TreeMapAggregatedFieldWellsTypeDef",
    {
        "Groups": List["DimensionFieldTypeDef"],
        "Sizes": List["MeasureFieldTypeDef"],
        "Colors": List["MeasureFieldTypeDef"],
    },
    total=False,
)

TreeMapConfigurationTypeDef = TypedDict(
    "TreeMapConfigurationTypeDef",
    {
        "FieldWells": "TreeMapFieldWellsTypeDef",
        "SortConfiguration": "TreeMapSortConfigurationTypeDef",
        "GroupLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "SizeLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColorLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "ColorScale": "ColorScaleTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "Tooltip": "TooltipOptionsTypeDef",
    },
    total=False,
)

TreeMapFieldWellsTypeDef = TypedDict(
    "TreeMapFieldWellsTypeDef",
    {
        "TreeMapAggregatedFieldWells": "TreeMapAggregatedFieldWellsTypeDef",
    },
    total=False,
)

TreeMapSortConfigurationTypeDef = TypedDict(
    "TreeMapSortConfigurationTypeDef",
    {
        "TreeMapSort": List["FieldSortOptionsTypeDef"],
        "TreeMapGroupItemsLimitConfiguration": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredTreeMapVisualTypeDef = TypedDict(
    "_RequiredTreeMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTreeMapVisualTypeDef = TypedDict(
    "_OptionalTreeMapVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "TreeMapConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class TreeMapVisualTypeDef(_RequiredTreeMapVisualTypeDef, _OptionalTreeMapVisualTypeDef):
    pass

TrendArrowOptionsTypeDef = TypedDict(
    "TrendArrowOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

TwitterParametersTypeDef = TypedDict(
    "TwitterParametersTypeDef",
    {
        "Query": str,
        "MaxRows": int,
    },
)

TypographyTypeDef = TypedDict(
    "TypographyTypeDef",
    {
        "FontFamilies": List["FontTypeDef"],
    },
    total=False,
)

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

_RequiredUnaggregatedFieldTypeDef = TypedDict(
    "_RequiredUnaggregatedFieldTypeDef",
    {
        "FieldId": str,
        "Column": "ColumnIdentifierTypeDef",
    },
)
_OptionalUnaggregatedFieldTypeDef = TypedDict(
    "_OptionalUnaggregatedFieldTypeDef",
    {
        "FormatConfiguration": "FormatConfigurationTypeDef",
    },
    total=False,
)

class UnaggregatedFieldTypeDef(
    _RequiredUnaggregatedFieldTypeDef, _OptionalUnaggregatedFieldTypeDef
):
    pass

_RequiredUniqueValuesComputationTypeDef = TypedDict(
    "_RequiredUniqueValuesComputationTypeDef",
    {
        "ComputationId": str,
        "Category": "DimensionFieldTypeDef",
    },
)
_OptionalUniqueValuesComputationTypeDef = TypedDict(
    "_OptionalUniqueValuesComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UniqueValuesComputationTypeDef(
    _RequiredUniqueValuesComputationTypeDef, _OptionalUniqueValuesComputationTypeDef
):
    pass

UntagColumnOperationTypeDef = TypedDict(
    "UntagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "TagNames": List[ColumnTagNameType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
    },
)
_OptionalUpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)

class UpdateAccountCustomizationRequestRequestTypeDef(
    _RequiredUpdateAccountCustomizationRequestRequestTypeDef,
    _OptionalUpdateAccountCustomizationRequestRequestTypeDef,
):
    pass

UpdateAccountCustomizationResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultNamespace": str,
    },
)
_OptionalUpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountSettingsRequestRequestTypeDef",
    {
        "NotificationEmail": str,
        "TerminationProtectionEnabled": bool,
    },
    total=False,
)

class UpdateAccountSettingsRequestRequestTypeDef(
    _RequiredUpdateAccountSettingsRequestRequestTypeDef,
    _OptionalUpdateAccountSettingsRequestRequestTypeDef,
):
    pass

UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalUpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateAnalysisPermissionsRequestRequestTypeDef(
    _RequiredUpdateAnalysisPermissionsRequestRequestTypeDef,
    _OptionalUpdateAnalysisPermissionsRequestRequestTypeDef,
):
    pass

UpdateAnalysisPermissionsResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
    },
)
_OptionalUpdateAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisRequestRequestTypeDef",
    {
        "Parameters": "ParametersTypeDef",
        "SourceEntity": "AnalysisSourceEntityTypeDef",
        "ThemeArn": str,
        "Definition": "AnalysisDefinitionTypeDef",
    },
    total=False,
)

class UpdateAnalysisRequestRequestTypeDef(
    _RequiredUpdateAnalysisRequestRequestTypeDef, _OptionalUpdateAnalysisRequestRequestTypeDef
):
    pass

UpdateAnalysisResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalUpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
        "GrantLinkPermissions": List["ResourcePermissionTypeDef"],
        "RevokeLinkPermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateDashboardPermissionsRequestRequestTypeDef(
    _RequiredUpdateDashboardPermissionsRequestRequestTypeDef,
    _OptionalUpdateDashboardPermissionsRequestRequestTypeDef,
):
    pass

UpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "LinkSharingConfiguration": "LinkSharingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardPublishedVersionRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": int,
    },
)

UpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
    },
)
_OptionalUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardRequestRequestTypeDef",
    {
        "SourceEntity": "DashboardSourceEntityTypeDef",
        "Parameters": "ParametersTypeDef",
        "VersionDescription": str,
        "DashboardPublishOptions": "DashboardPublishOptionsTypeDef",
        "ThemeArn": str,
        "Definition": "DashboardVersionDefinitionTypeDef",
    },
    total=False,
)

class UpdateDashboardRequestRequestTypeDef(
    _RequiredUpdateDashboardRequestRequestTypeDef, _OptionalUpdateDashboardRequestRequestTypeDef
):
    pass

UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
_OptionalUpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateDataSetPermissionsRequestRequestTypeDef(
    _RequiredUpdateDataSetPermissionsRequestRequestTypeDef,
    _OptionalUpdateDataSetPermissionsRequestRequestTypeDef,
):
    pass

UpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Dict[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetRequestRequestTypeDef",
    {
        "LogicalTableMap": Dict[str, "LogicalTableTypeDef"],
        "ColumnGroups": List["ColumnGroupTypeDef"],
        "FieldFolders": Dict[str, "FieldFolderTypeDef"],
        "RowLevelPermissionDataSet": "RowLevelPermissionDataSetTypeDef",
        "RowLevelPermissionTagConfiguration": "RowLevelPermissionTagConfigurationTypeDef",
        "ColumnLevelPermissionRules": List["ColumnLevelPermissionRuleTypeDef"],
        "DataSetUsageConfiguration": "DataSetUsageConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataSetRequestRequestTypeDef(
    _RequiredUpdateDataSetRequestRequestTypeDef, _OptionalUpdateDataSetRequestRequestTypeDef
):
    pass

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)
_OptionalUpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateDataSourcePermissionsRequestRequestTypeDef(
    _RequiredUpdateDataSourcePermissionsRequestRequestTypeDef,
    _OptionalUpdateDataSourcePermissionsRequestRequestTypeDef,
):
    pass

UpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "DataSourceParameters": "DataSourceParametersTypeDef",
        "Credentials": "DataSourceCredentialsTypeDef",
        "VpcConnectionProperties": "VpcConnectionPropertiesTypeDef",
        "SslProperties": "SslPropertiesTypeDef",
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalUpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFolderPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateFolderPermissionsRequestRequestTypeDef(
    _RequiredUpdateFolderPermissionsRequestRequestTypeDef,
    _OptionalUpdateFolderPermissionsRequestRequestTypeDef,
):
    pass

UpdateFolderPermissionsResponseTypeDef = TypedDict(
    "UpdateFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": str,
    },
)

UpdateFolderResponseTypeDef = TypedDict(
    "UpdateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)
_OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
    },
    total=False,
)

class UpdateIAMPolicyAssignmentRequestRequestTypeDef(
    _RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef,
    _OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef,
):
    pass

UpdateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalUpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIpRestrictionRequestRequestTypeDef",
    {
        "IpRestrictionRuleMap": Dict[str, str],
        "Enabled": bool,
    },
    total=False,
)

class UpdateIpRestrictionRequestRequestTypeDef(
    _RequiredUpdateIpRestrictionRequestRequestTypeDef,
    _OptionalUpdateIpRestrictionRequestRequestTypeDef,
):
    pass

UpdateIpRestrictionResponseTypeDef = TypedDict(
    "UpdateIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePublicSharingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePublicSharingSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalUpdatePublicSharingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePublicSharingSettingsRequestRequestTypeDef",
    {
        "PublicSharingEnabled": bool,
    },
    total=False,
)

class UpdatePublicSharingSettingsRequestRequestTypeDef(
    _RequiredUpdatePublicSharingSettingsRequestRequestTypeDef,
    _OptionalUpdatePublicSharingSettingsRequestRequestTypeDef,
):
    pass

UpdatePublicSharingSettingsResponseTypeDef = TypedDict(
    "UpdatePublicSharingSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateAliasRequestRequestTypeDef = TypedDict(
    "UpdateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

UpdateTemplateAliasResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalUpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateTemplatePermissionsRequestRequestTypeDef(
    _RequiredUpdateTemplatePermissionsRequestRequestTypeDef,
    _OptionalUpdateTemplatePermissionsRequestRequestTypeDef,
):
    pass

UpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateRequestRequestTypeDef",
    {
        "SourceEntity": "TemplateSourceEntityTypeDef",
        "VersionDescription": str,
        "Name": str,
        "Definition": "TemplateVersionDefinitionTypeDef",
    },
    total=False,
)

class UpdateTemplateRequestRequestTypeDef(
    _RequiredUpdateTemplateRequestRequestTypeDef, _OptionalUpdateTemplateRequestRequestTypeDef
):
    pass

UpdateTemplateResponseTypeDef = TypedDict(
    "UpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemeAliasRequestRequestTypeDef = TypedDict(
    "UpdateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

UpdateThemeAliasResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalUpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": List["ResourcePermissionTypeDef"],
        "RevokePermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

class UpdateThemePermissionsRequestRequestTypeDef(
    _RequiredUpdateThemePermissionsRequestRequestTypeDef,
    _OptionalUpdateThemePermissionsRequestRequestTypeDef,
):
    pass

UpdateThemePermissionsResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "BaseThemeId": str,
    },
)
_OptionalUpdateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestRequestTypeDef",
    {
        "Name": str,
        "VersionDescription": str,
        "Configuration": "ThemeConfigurationTypeDef",
    },
    total=False,
)

class UpdateThemeRequestRequestTypeDef(
    _RequiredUpdateThemeRequestRequestTypeDef, _OptionalUpdateThemeRequestRequestTypeDef
):
    pass

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Email": str,
        "Role": UserRoleType,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "CustomPermissionsName": str,
        "UnapplyCustomPermissions": bool,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": FileFormatType,
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": TextQualifierType,
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
        "Role": UserRoleType,
        "IdentityType": IdentityTypeType,
        "Active": bool,
        "PrincipalId": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "ExternalLoginFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)

VisibleRangeOptionsTypeDef = TypedDict(
    "VisibleRangeOptionsTypeDef",
    {
        "PercentRange": "PercentVisibleRangeTypeDef",
    },
    total=False,
)

VisualCustomActionOperationTypeDef = TypedDict(
    "VisualCustomActionOperationTypeDef",
    {
        "FilterOperation": "CustomActionFilterOperationTypeDef",
        "NavigationOperation": "CustomActionNavigationOperationTypeDef",
        "URLOperation": "CustomActionURLOperationTypeDef",
        "SetParametersOperation": "CustomActionSetParametersOperationTypeDef",
    },
    total=False,
)

_RequiredVisualCustomActionTypeDef = TypedDict(
    "_RequiredVisualCustomActionTypeDef",
    {
        "CustomActionId": str,
        "Name": str,
        "Trigger": VisualCustomActionTriggerType,
        "ActionOperations": List["VisualCustomActionOperationTypeDef"],
    },
)
_OptionalVisualCustomActionTypeDef = TypedDict(
    "_OptionalVisualCustomActionTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)

class VisualCustomActionTypeDef(
    _RequiredVisualCustomActionTypeDef, _OptionalVisualCustomActionTypeDef
):
    pass

VisualPaletteTypeDef = TypedDict(
    "VisualPaletteTypeDef",
    {
        "ChartColor": str,
        "ColorMap": List["DataPathColorTypeDef"],
    },
    total=False,
)

VisualSubtitleLabelOptionsTypeDef = TypedDict(
    "VisualSubtitleLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FormatText": "LongFormatTextTypeDef",
    },
    total=False,
)

VisualTitleLabelOptionsTypeDef = TypedDict(
    "VisualTitleLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FormatText": "ShortFormatTextTypeDef",
    },
    total=False,
)

VisualTypeDef = TypedDict(
    "VisualTypeDef",
    {
        "TableVisual": "TableVisualTypeDef",
        "PivotTableVisual": "PivotTableVisualTypeDef",
        "BarChartVisual": "BarChartVisualTypeDef",
        "KPIVisual": "KPIVisualTypeDef",
        "PieChartVisual": "PieChartVisualTypeDef",
        "GaugeChartVisual": "GaugeChartVisualTypeDef",
        "LineChartVisual": "LineChartVisualTypeDef",
        "HeatMapVisual": "HeatMapVisualTypeDef",
        "TreeMapVisual": "TreeMapVisualTypeDef",
        "GeospatialMapVisual": "GeospatialMapVisualTypeDef",
        "FilledMapVisual": "FilledMapVisualTypeDef",
        "FunnelChartVisual": "FunnelChartVisualTypeDef",
        "ScatterPlotVisual": "ScatterPlotVisualTypeDef",
        "ComboChartVisual": "ComboChartVisualTypeDef",
        "BoxPlotVisual": "BoxPlotVisualTypeDef",
        "WaterfallVisual": "WaterfallVisualTypeDef",
        "HistogramVisual": "HistogramVisualTypeDef",
        "WordCloudVisual": "WordCloudVisualTypeDef",
        "InsightVisual": "InsightVisualTypeDef",
        "SankeyDiagramVisual": "SankeyDiagramVisualTypeDef",
        "CustomContentVisual": "CustomContentVisualTypeDef",
        "EmptyVisual": "EmptyVisualTypeDef",
    },
    total=False,
)

VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef",
    {
        "VpcConnectionArn": str,
    },
)

WaterfallChartAggregatedFieldWellsTypeDef = TypedDict(
    "WaterfallChartAggregatedFieldWellsTypeDef",
    {
        "Categories": List["DimensionFieldTypeDef"],
        "Values": List["MeasureFieldTypeDef"],
        "Breakdowns": List["DimensionFieldTypeDef"],
    },
    total=False,
)

WaterfallChartConfigurationTypeDef = TypedDict(
    "WaterfallChartConfigurationTypeDef",
    {
        "FieldWells": "WaterfallChartFieldWellsTypeDef",
        "SortConfiguration": "WaterfallChartSortConfigurationTypeDef",
        "WaterfallChartOptions": "WaterfallChartOptionsTypeDef",
        "CategoryAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "CategoryAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "PrimaryYAxisLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "PrimaryYAxisDisplayOptions": "AxisDisplayOptionsTypeDef",
        "Legend": "LegendOptionsTypeDef",
        "DataLabels": "DataLabelOptionsTypeDef",
        "VisualPalette": "VisualPaletteTypeDef",
    },
    total=False,
)

WaterfallChartFieldWellsTypeDef = TypedDict(
    "WaterfallChartFieldWellsTypeDef",
    {
        "WaterfallChartAggregatedFieldWells": "WaterfallChartAggregatedFieldWellsTypeDef",
    },
    total=False,
)

WaterfallChartOptionsTypeDef = TypedDict(
    "WaterfallChartOptionsTypeDef",
    {
        "TotalBarLabel": str,
    },
    total=False,
)

WaterfallChartSortConfigurationTypeDef = TypedDict(
    "WaterfallChartSortConfigurationTypeDef",
    {
        "CategorySort": List["FieldSortOptionsTypeDef"],
        "BreakdownItemsLimit": "ItemsLimitConfigurationTypeDef",
    },
    total=False,
)

_RequiredWaterfallVisualTypeDef = TypedDict(
    "_RequiredWaterfallVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWaterfallVisualTypeDef = TypedDict(
    "_OptionalWaterfallVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "WaterfallChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class WaterfallVisualTypeDef(_RequiredWaterfallVisualTypeDef, _OptionalWaterfallVisualTypeDef):
    pass

WhatIfPointScenarioTypeDef = TypedDict(
    "WhatIfPointScenarioTypeDef",
    {
        "Date": Union[datetime, str],
        "Value": float,
    },
)

WhatIfRangeScenarioTypeDef = TypedDict(
    "WhatIfRangeScenarioTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "Value": float,
    },
)

WordCloudAggregatedFieldWellsTypeDef = TypedDict(
    "WordCloudAggregatedFieldWellsTypeDef",
    {
        "GroupBy": List["DimensionFieldTypeDef"],
        "Size": List["MeasureFieldTypeDef"],
    },
    total=False,
)

WordCloudChartConfigurationTypeDef = TypedDict(
    "WordCloudChartConfigurationTypeDef",
    {
        "FieldWells": "WordCloudFieldWellsTypeDef",
        "SortConfiguration": "WordCloudSortConfigurationTypeDef",
        "CategoryLabelOptions": "ChartAxisLabelOptionsTypeDef",
        "WordCloudOptions": "WordCloudOptionsTypeDef",
    },
    total=False,
)

WordCloudFieldWellsTypeDef = TypedDict(
    "WordCloudFieldWellsTypeDef",
    {
        "WordCloudAggregatedFieldWells": "WordCloudAggregatedFieldWellsTypeDef",
    },
    total=False,
)

WordCloudOptionsTypeDef = TypedDict(
    "WordCloudOptionsTypeDef",
    {
        "WordOrientation": WordCloudWordOrientationType,
        "WordScaling": WordCloudWordScalingType,
        "CloudLayout": WordCloudCloudLayoutType,
        "WordCasing": WordCloudWordCasingType,
        "WordPadding": WordCloudWordPaddingType,
        "MaximumStringLength": int,
    },
    total=False,
)

WordCloudSortConfigurationTypeDef = TypedDict(
    "WordCloudSortConfigurationTypeDef",
    {
        "CategoryItemsLimit": "ItemsLimitConfigurationTypeDef",
        "CategorySort": List["FieldSortOptionsTypeDef"],
    },
    total=False,
)

_RequiredWordCloudVisualTypeDef = TypedDict(
    "_RequiredWordCloudVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWordCloudVisualTypeDef = TypedDict(
    "_OptionalWordCloudVisualTypeDef",
    {
        "Title": "VisualTitleLabelOptionsTypeDef",
        "Subtitle": "VisualSubtitleLabelOptionsTypeDef",
        "ChartConfiguration": "WordCloudChartConfigurationTypeDef",
        "Actions": List["VisualCustomActionTypeDef"],
        "ColumnHierarchies": List["ColumnHierarchyTypeDef"],
    },
    total=False,
)

class WordCloudVisualTypeDef(_RequiredWordCloudVisualTypeDef, _OptionalWordCloudVisualTypeDef):
    pass
