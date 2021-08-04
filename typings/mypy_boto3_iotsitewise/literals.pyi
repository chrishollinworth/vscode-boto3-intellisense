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
    "AssetNotExistsWaiterName",
    "AssetRelationshipTypeType",
    "AssetStateType",
    "AuthModeType",
    "BatchPutAssetPropertyValueErrorCodeType",
    "CapabilitySyncStatusType",
    "ComputeLocationType",
    "ConfigurationStateType",
    "DetailedErrorCodeType",
    "EncryptionTypeType",
    "ErrorCodeType",
    "ForwardingConfigStateType",
    "GetAssetPropertyAggregatesPaginatorName",
    "GetAssetPropertyValueHistoryPaginatorName",
    "GetInterpolatedAssetPropertyValuesPaginatorName",
    "IdentityTypeType",
    "ImageFileTypeType",
    "ListAccessPoliciesPaginatorName",
    "ListAssetModelsPaginatorName",
    "ListAssetRelationshipsPaginatorName",
    "ListAssetsFilterType",
    "ListAssetsPaginatorName",
    "ListAssociatedAssetsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListGatewaysPaginatorName",
    "ListPortalsPaginatorName",
    "ListProjectAssetsPaginatorName",
    "ListProjectsPaginatorName",
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
    "StorageTypeType",
    "TimeOrderingType",
    "TraversalDirectionType",
    "TraversalTypeType",
)

AggregateTypeType = Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
AssetActiveWaiterName = Literal["asset_active"]
AssetErrorCodeType = Literal["INTERNAL_FAILURE"]
AssetModelActiveWaiterName = Literal["asset_model_active"]
AssetModelNotExistsWaiterName = Literal["asset_model_not_exists"]
AssetModelStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PROPAGATING", "UPDATING"]
AssetNotExistsWaiterName = Literal["asset_not_exists"]
AssetRelationshipTypeType = Literal["HIERARCHY"]
AssetStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
AuthModeType = Literal["IAM", "SSO"]
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
ComputeLocationType = Literal["CLOUD", "EDGE"]
ConfigurationStateType = Literal["ACTIVE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"]
DetailedErrorCodeType = Literal[
    "INCOMPATIBLE_COMPUTE_LOCATION", "INCOMPATIBLE_FORWARDING_CONFIGURATION"
]
EncryptionTypeType = Literal["KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"]
ErrorCodeType = Literal["INTERNAL_FAILURE", "VALIDATION_ERROR"]
ForwardingConfigStateType = Literal["DISABLED", "ENABLED"]
GetAssetPropertyAggregatesPaginatorName = Literal["get_asset_property_aggregates"]
GetAssetPropertyValueHistoryPaginatorName = Literal["get_asset_property_value_history"]
GetInterpolatedAssetPropertyValuesPaginatorName = Literal["get_interpolated_asset_property_values"]
IdentityTypeType = Literal["GROUP", "IAM", "USER"]
ImageFileTypeType = Literal["PNG"]
ListAccessPoliciesPaginatorName = Literal["list_access_policies"]
ListAssetModelsPaginatorName = Literal["list_asset_models"]
ListAssetRelationshipsPaginatorName = Literal["list_asset_relationships"]
ListAssetsFilterType = Literal["ALL", "TOP_LEVEL"]
ListAssetsPaginatorName = Literal["list_assets"]
ListAssociatedAssetsPaginatorName = Literal["list_associated_assets"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListPortalsPaginatorName = Literal["list_portals"]
ListProjectAssetsPaginatorName = Literal["list_project_assets"]
ListProjectsPaginatorName = Literal["list_projects"]
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
StorageTypeType = Literal["MULTI_LAYER_STORAGE", "SITEWISE_DEFAULT_STORAGE"]
TimeOrderingType = Literal["ASCENDING", "DESCENDING"]
TraversalDirectionType = Literal["CHILD", "PARENT"]
TraversalTypeType = Literal["PATH_TO_ROOT"]
