"""
Type annotations for iotsitewise service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/literals.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.literals import AggregateTypeType

    data: AggregateTypeType = "AVERAGE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregateTypeType",
    "AssetActiveWaiterName",
    "AssetErrorCodeType",
    "AssetModelActiveWaiterName",
    "AssetModelNotExistsWaiterName",
    "AssetModelStateType",
    "AssetModelTypeType",
    "AssetNotExistsWaiterName",
    "AssetRelationshipTypeType",
    "AssetStateType",
    "AuthModeType",
    "BatchEntryCompletionStatusType",
    "BatchGetAssetPropertyAggregatesErrorCodeType",
    "BatchGetAssetPropertyValueErrorCodeType",
    "BatchGetAssetPropertyValueHistoryErrorCodeType",
    "BatchPutAssetPropertyValueErrorCodeType",
    "CapabilitySyncStatusType",
    "ColumnNameType",
    "ComputeLocationType",
    "ConfigurationStateType",
    "DetailedErrorCodeType",
    "DisassociatedDataStorageStateType",
    "EncryptionTypeType",
    "ErrorCodeType",
    "ExecuteQueryPaginatorName",
    "ForwardingConfigStateType",
    "GetAssetPropertyAggregatesPaginatorName",
    "GetAssetPropertyValueHistoryPaginatorName",
    "GetInterpolatedAssetPropertyValuesPaginatorName",
    "IdentityTypeType",
    "ImageFileTypeType",
    "JobStatusType",
    "ListAccessPoliciesPaginatorName",
    "ListActionsPaginatorName",
    "ListAssetModelCompositeModelsPaginatorName",
    "ListAssetModelPropertiesFilterType",
    "ListAssetModelPropertiesPaginatorName",
    "ListAssetModelsPaginatorName",
    "ListAssetPropertiesFilterType",
    "ListAssetPropertiesPaginatorName",
    "ListAssetRelationshipsPaginatorName",
    "ListAssetsFilterType",
    "ListAssetsPaginatorName",
    "ListAssociatedAssetsPaginatorName",
    "ListBulkImportJobsFilterType",
    "ListBulkImportJobsPaginatorName",
    "ListCompositionRelationshipsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListGatewaysPaginatorName",
    "ListPortalsPaginatorName",
    "ListProjectAssetsPaginatorName",
    "ListProjectsPaginatorName",
    "ListTimeSeriesPaginatorName",
    "ListTimeSeriesTypeType",
    "LoggingLevelType",
    "MonitorErrorCodeType",
    "PermissionType",
    "PortalActiveWaiterName",
    "PortalNotExistsWaiterName",
    "PortalStateType",
    "PropertyDataTypeType",
    "PropertyNotificationStateType",
    "QualityType",
    "ResourceTypeType",
    "ScalarTypeType",
    "StorageTypeType",
    "TargetResourceTypeType",
    "TimeOrderingType",
    "TraversalDirectionType",
    "TraversalTypeType",
    "WarmTierStateType",
)

AggregateTypeType = Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
AssetActiveWaiterName = Literal["asset_active"]
AssetErrorCodeType = Literal["INTERNAL_FAILURE"]
AssetModelActiveWaiterName = Literal["asset_model_active"]
AssetModelNotExistsWaiterName = Literal["asset_model_not_exists"]
AssetModelStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PROPAGATING", "UPDATING"]
AssetModelTypeType = Literal["ASSET_MODEL", "COMPONENT_MODEL"]
AssetNotExistsWaiterName = Literal["asset_not_exists"]
AssetRelationshipTypeType = Literal["HIERARCHY"]
AssetStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
AuthModeType = Literal["IAM", "SSO"]
BatchEntryCompletionStatusType = Literal["ERROR", "SUCCESS"]
BatchGetAssetPropertyAggregatesErrorCodeType = Literal[
    "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
]
BatchGetAssetPropertyValueErrorCodeType = Literal[
    "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
]
BatchGetAssetPropertyValueHistoryErrorCodeType = Literal[
    "AccessDeniedException", "InvalidRequestException", "ResourceNotFoundException"
]
BatchPutAssetPropertyValueErrorCodeType = Literal[
    "AccessDeniedException",
    "ConflictingOperationException",
    "InternalFailureException",
    "InvalidRequestException",
    "LimitExceededException",
    "ResourceNotFoundException",
    "ServiceUnavailableException",
    "ThrottlingException",
    "TimestampOutOfRangeException",
]
CapabilitySyncStatusType = Literal["IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED", "UNKNOWN"]
ColumnNameType = Literal[
    "ALIAS",
    "ASSET_ID",
    "DATA_TYPE",
    "PROPERTY_ID",
    "QUALITY",
    "TIMESTAMP_NANO_OFFSET",
    "TIMESTAMP_SECONDS",
    "VALUE",
]
ComputeLocationType = Literal["CLOUD", "EDGE"]
ConfigurationStateType = Literal["ACTIVE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"]
DetailedErrorCodeType = Literal[
    "INCOMPATIBLE_COMPUTE_LOCATION", "INCOMPATIBLE_FORWARDING_CONFIGURATION"
]
DisassociatedDataStorageStateType = Literal["DISABLED", "ENABLED"]
EncryptionTypeType = Literal["KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"]
ErrorCodeType = Literal["INTERNAL_FAILURE", "VALIDATION_ERROR"]
ExecuteQueryPaginatorName = Literal["execute_query"]
ForwardingConfigStateType = Literal["DISABLED", "ENABLED"]
GetAssetPropertyAggregatesPaginatorName = Literal["get_asset_property_aggregates"]
GetAssetPropertyValueHistoryPaginatorName = Literal["get_asset_property_value_history"]
GetInterpolatedAssetPropertyValuesPaginatorName = Literal["get_interpolated_asset_property_values"]
IdentityTypeType = Literal["GROUP", "IAM", "USER"]
ImageFileTypeType = Literal["PNG"]
JobStatusType = Literal[
    "CANCELLED", "COMPLETED", "COMPLETED_WITH_FAILURES", "FAILED", "PENDING", "RUNNING"
]
ListAccessPoliciesPaginatorName = Literal["list_access_policies"]
ListActionsPaginatorName = Literal["list_actions"]
ListAssetModelCompositeModelsPaginatorName = Literal["list_asset_model_composite_models"]
ListAssetModelPropertiesFilterType = Literal["ALL", "BASE"]
ListAssetModelPropertiesPaginatorName = Literal["list_asset_model_properties"]
ListAssetModelsPaginatorName = Literal["list_asset_models"]
ListAssetPropertiesFilterType = Literal["ALL", "BASE"]
ListAssetPropertiesPaginatorName = Literal["list_asset_properties"]
ListAssetRelationshipsPaginatorName = Literal["list_asset_relationships"]
ListAssetsFilterType = Literal["ALL", "TOP_LEVEL"]
ListAssetsPaginatorName = Literal["list_assets"]
ListAssociatedAssetsPaginatorName = Literal["list_associated_assets"]
ListBulkImportJobsFilterType = Literal[
    "ALL", "CANCELLED", "COMPLETED", "COMPLETED_WITH_FAILURES", "FAILED", "PENDING", "RUNNING"
]
ListBulkImportJobsPaginatorName = Literal["list_bulk_import_jobs"]
ListCompositionRelationshipsPaginatorName = Literal["list_composition_relationships"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListPortalsPaginatorName = Literal["list_portals"]
ListProjectAssetsPaginatorName = Literal["list_project_assets"]
ListProjectsPaginatorName = Literal["list_projects"]
ListTimeSeriesPaginatorName = Literal["list_time_series"]
ListTimeSeriesTypeType = Literal["ASSOCIATED", "DISASSOCIATED"]
LoggingLevelType = Literal["ERROR", "INFO", "OFF"]
MonitorErrorCodeType = Literal["INTERNAL_FAILURE", "LIMIT_EXCEEDED", "VALIDATION_ERROR"]
PermissionType = Literal["ADMINISTRATOR", "VIEWER"]
PortalActiveWaiterName = Literal["portal_active"]
PortalNotExistsWaiterName = Literal["portal_not_exists"]
PortalStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
PropertyDataTypeType = Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"]
PropertyNotificationStateType = Literal["DISABLED", "ENABLED"]
QualityType = Literal["BAD", "GOOD", "UNCERTAIN"]
ResourceTypeType = Literal["PORTAL", "PROJECT"]
ScalarTypeType = Literal["BOOLEAN", "DOUBLE", "INT", "STRING", "TIMESTAMP"]
StorageTypeType = Literal["MULTI_LAYER_STORAGE", "SITEWISE_DEFAULT_STORAGE"]
TargetResourceTypeType = Literal["ASSET"]
TimeOrderingType = Literal["ASCENDING", "DESCENDING"]
TraversalDirectionType = Literal["CHILD", "PARENT"]
TraversalTypeType = Literal["PATH_TO_ROOT"]
WarmTierStateType = Literal["DISABLED", "ENABLED"]
