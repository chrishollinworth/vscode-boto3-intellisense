from mypy_boto3_iotsitewise.type_defs import (
    AccessPolicySummaryTypeDef,
    AggregatedValueTypeDef,
    AggregatesTypeDef,
    AssetErrorDetailsTypeDef,
    AssetHierarchyTypeDef,
    AssetModelHierarchyTypeDef,
    AssetModelPropertyTypeDef,
    AssetModelStatusTypeDef,
    AssetModelSummaryTypeDef,
    AssetPropertyTypeDef,
    AssetPropertyValueTypeDef,
    AssetStatusTypeDef,
    AssetSummaryTypeDef,
    AssociatedAssetsSummaryTypeDef,
    AttributeTypeDef,
    BatchPutAssetPropertyErrorEntryTypeDef,
    BatchPutAssetPropertyErrorTypeDef,
    ConfigurationErrorDetailsTypeDef,
    ConfigurationStatusTypeDef,
    DashboardSummaryTypeDef,
    ErrorDetailsTypeDef,
    ExpressionVariableTypeDef,
    GatewayCapabilitySummaryTypeDef,
    GatewayPlatformTypeDef,
    GatewaySummaryTypeDef,
    GreengrassTypeDef,
    GroupIdentityTypeDef,
    IAMUserIdentityTypeDef,
    IdentityTypeDef,
    ImageFileTypeDef,
    ImageLocationTypeDef,
    LoggingOptionsTypeDef,
    MetricTypeDef,
    MetricWindowTypeDef,
    MonitorErrorDetailsTypeDef,
    PortalResourceTypeDef,
    PortalStatusTypeDef,
    PortalSummaryTypeDef,
    ProjectResourceTypeDef,
    ProjectSummaryTypeDef,
    PropertyNotificationTypeDef,
    PropertyTypeDef,
    PropertyTypeTypeDef,
    ResourceTypeDef,
    TimeInNanosTypeDef,
    TransformTypeDef,
    TumblingWindowTypeDef,
    UserIdentityTypeDef,
    VariableValueTypeDef,
    VariantTypeDef,
    AssetModelHierarchyDefinitionTypeDef,
    AssetModelPropertyDefinitionTypeDef,
    BatchAssociateProjectAssetsResponseTypeDef,
    BatchDisassociateProjectAssetsResponseTypeDef,
    BatchPutAssetPropertyValueResponseTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateAssetModelResponseTypeDef,
    CreateAssetResponseTypeDef,
    CreateDashboardResponseTypeDef,
    CreateGatewayResponseTypeDef,
    CreatePortalResponseTypeDef,
    CreatePresignedPortalUrlResponseTypeDef,
    CreateProjectResponseTypeDef,
    DeleteAssetModelResponseTypeDef,
    DeleteAssetResponseTypeDef,
    DeletePortalResponseTypeDef,
    DescribeAccessPolicyResponseTypeDef,
    DescribeAssetModelResponseTypeDef,
    DescribeAssetPropertyResponseTypeDef,
    DescribeAssetResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDefaultEncryptionConfigurationResponseTypeDef,
    DescribeGatewayCapabilityConfigurationResponseTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePortalResponseTypeDef,
    DescribeProjectResponseTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetAssetPropertyValueResponseTypeDef,
    ImageTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    PutAssetPropertyValueEntryTypeDef,
    PutDefaultEncryptionConfigurationResponseTypeDef,
    UpdateAssetModelResponseTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateGatewayCapabilityConfigurationResponseTypeDef,
    UpdatePortalResponseTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "AccessPolicySummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "DashboardSummaryTypeDef",
    "ErrorDetailsTypeDef",
    "ExpressionVariableTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GreengrassTypeDef",
    "GroupIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "LoggingOptionsTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "ResourceTypeDef",
    "TimeInNanosTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateAssetModelResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreatePortalResponseTypeDef",
    "CreatePresignedPortalUrlResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "DeleteAssetResponseTypeDef",
    "DeletePortalResponseTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePortalResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "ImageTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "UpdatePortalResponseTypeDef",
    "WaiterConfigTypeDef",
)
