"""
Type annotations for iotsitewise service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef

    data: AccessPolicySummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AggregateTypeType,
    AssetModelStateType,
    AssetModelTypeType,
    AssetStateType,
    AuthModeType,
    BatchEntryCompletionStatusType,
    BatchGetAssetPropertyAggregatesErrorCodeType,
    BatchGetAssetPropertyValueErrorCodeType,
    BatchGetAssetPropertyValueHistoryErrorCodeType,
    BatchPutAssetPropertyValueErrorCodeType,
    CapabilitySyncStatusType,
    ColumnNameType,
    ComputeLocationType,
    ConfigurationStateType,
    DetailedErrorCodeType,
    DisassociatedDataStorageStateType,
    EncryptionTypeType,
    ErrorCodeType,
    ForwardingConfigStateType,
    IdentityTypeType,
    JobStatusType,
    ListAssetModelPropertiesFilterType,
    ListAssetPropertiesFilterType,
    ListAssetsFilterType,
    ListBulkImportJobsFilterType,
    ListTimeSeriesTypeType,
    LoggingLevelType,
    MonitorErrorCodeType,
    PermissionType,
    PortalStateType,
    PropertyDataTypeType,
    PropertyNotificationStateType,
    QualityType,
    ResourceTypeType,
    ScalarTypeType,
    StorageTypeType,
    TimeOrderingType,
    TraversalDirectionType,
    WarmTierStateType,
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
    "AccessPolicySummaryTypeDef",
    "ActionDefinitionTypeDef",
    "ActionPayloadTypeDef",
    "ActionSummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AlarmsTypeDef",
    "AssetCompositeModelPathSegmentTypeDef",
    "AssetCompositeModelSummaryTypeDef",
    "AssetCompositeModelTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "AssetModelCompositeModelPathSegmentTypeDef",
    "AssetModelCompositeModelSummaryTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyPathSegmentTypeDef",
    "AssetModelPropertySummaryTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyPathSegmentTypeDef",
    "AssetPropertySummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociateAssetsRequestRequestTypeDef",
    "AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchAssociateProjectAssetsRequestRequestTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsRequestRequestTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "BatchGetAssetPropertyAggregatesEntryTypeDef",
    "BatchGetAssetPropertyAggregatesErrorEntryTypeDef",
    "BatchGetAssetPropertyAggregatesErrorInfoTypeDef",
    "BatchGetAssetPropertyAggregatesRequestRequestTypeDef",
    "BatchGetAssetPropertyAggregatesResponseTypeDef",
    "BatchGetAssetPropertyAggregatesSkippedEntryTypeDef",
    "BatchGetAssetPropertyAggregatesSuccessEntryTypeDef",
    "BatchGetAssetPropertyValueEntryTypeDef",
    "BatchGetAssetPropertyValueErrorEntryTypeDef",
    "BatchGetAssetPropertyValueErrorInfoTypeDef",
    "BatchGetAssetPropertyValueHistoryEntryTypeDef",
    "BatchGetAssetPropertyValueHistoryErrorEntryTypeDef",
    "BatchGetAssetPropertyValueHistoryErrorInfoTypeDef",
    "BatchGetAssetPropertyValueHistoryRequestRequestTypeDef",
    "BatchGetAssetPropertyValueHistoryResponseTypeDef",
    "BatchGetAssetPropertyValueHistorySkippedEntryTypeDef",
    "BatchGetAssetPropertyValueHistorySuccessEntryTypeDef",
    "BatchGetAssetPropertyValueRequestRequestTypeDef",
    "BatchGetAssetPropertyValueResponseTypeDef",
    "BatchGetAssetPropertyValueSkippedEntryTypeDef",
    "BatchGetAssetPropertyValueSuccessEntryTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeTypeDef",
    "CompositeModelPropertyTypeDef",
    "CompositionDetailsTypeDef",
    "CompositionRelationshipItemTypeDef",
    "CompositionRelationshipSummaryTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "CreateAccessPolicyRequestRequestTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateAssetModelCompositeModelRequestRequestTypeDef",
    "CreateAssetModelCompositeModelResponseTypeDef",
    "CreateAssetModelRequestRequestTypeDef",
    "CreateAssetModelResponseTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "CreateAssetResponseTypeDef",
    "CreateBulkImportJobRequestRequestTypeDef",
    "CreateBulkImportJobResponseTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayRequestRequestTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CsvTypeDef",
    "CustomerManagedS3StorageTypeDef",
    "DashboardSummaryTypeDef",
    "DatumTypeDef",
    "DeleteAccessPolicyRequestRequestTypeDef",
    "DeleteAssetModelCompositeModelRequestRequestTypeDef",
    "DeleteAssetModelCompositeModelResponseTypeDef",
    "DeleteAssetModelRequestRequestTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteAssetResponseTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteGatewayRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeletePortalResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteTimeSeriesRequestRequestTypeDef",
    "DescribeAccessPolicyRequestRequestTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "DescribeActionRequestRequestTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeAssetCompositeModelRequestRequestTypeDef",
    "DescribeAssetCompositeModelResponseTypeDef",
    "DescribeAssetModelCompositeModelRequestRequestTypeDef",
    "DescribeAssetModelCompositeModelResponseTypeDef",
    "DescribeAssetModelRequestRequestTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyRequestRequestTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribeBulkImportJobRequestRequestTypeDef",
    "DescribeBulkImportJobResponseTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeGatewayRequestRequestTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePortalRequestRequestTypeDef",
    "DescribePortalResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeStorageConfigurationResponseTypeDef",
    "DescribeTimeSeriesRequestRequestTypeDef",
    "DescribeTimeSeriesResponseTypeDef",
    "DetailedErrorTypeDef",
    "DisassociateAssetsRequestRequestTypeDef",
    "DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    "ErrorDetailsTypeDef",
    "ErrorReportLocationTypeDef",
    "ExecuteActionRequestRequestTypeDef",
    "ExecuteActionResponseTypeDef",
    "ExecuteQueryRequestRequestTypeDef",
    "ExecuteQueryResponseTypeDef",
    "ExpressionVariableTypeDef",
    "FileFormatTypeDef",
    "FileTypeDef",
    "ForwardingConfigTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GetAssetPropertyAggregatesRequestRequestTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueRequestRequestTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "GetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    "GreengrassTypeDef",
    "GreengrassV2TypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "ImageTypeDef",
    "InterpolatedAssetPropertyValueTypeDef",
    "JobConfigurationTypeDef",
    "JobSummaryTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListAssetModelCompositeModelsRequestRequestTypeDef",
    "ListAssetModelCompositeModelsResponseTypeDef",
    "ListAssetModelPropertiesRequestRequestTypeDef",
    "ListAssetModelPropertiesResponseTypeDef",
    "ListAssetModelsRequestRequestTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetPropertiesRequestRequestTypeDef",
    "ListAssetPropertiesResponseTypeDef",
    "ListAssetRelationshipsRequestRequestTypeDef",
    "ListAssetRelationshipsResponseTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsRequestRequestTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "ListBulkImportJobsRequestRequestTypeDef",
    "ListBulkImportJobsResponseTypeDef",
    "ListCompositionRelationshipsRequestRequestTypeDef",
    "ListCompositionRelationshipsResponseTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListProjectAssetsRequestRequestTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimeSeriesRequestRequestTypeDef",
    "ListTimeSeriesResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MeasurementProcessingConfigTypeDef",
    "MeasurementTypeDef",
    "MetricProcessingConfigTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "MultiLayerStorageTypeDef",
    "PaginatorConfigTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationRequestRequestTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "PutStorageConfigurationRequestRequestTypeDef",
    "PutStorageConfigurationResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RowTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetResourceTypeDef",
    "TimeInNanosTypeDef",
    "TimeSeriesSummaryTypeDef",
    "TransformProcessingConfigTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessPolicyRequestRequestTypeDef",
    "UpdateAssetModelCompositeModelRequestRequestTypeDef",
    "UpdateAssetModelCompositeModelResponseTypeDef",
    "UpdateAssetModelRequestRequestTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "UpdateAssetPropertyRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "UpdateGatewayRequestRequestTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "WaiterConfigTypeDef",
    "WarmTierRetentionPeriodTypeDef",
)

_RequiredAccessPolicySummaryTypeDef = TypedDict(
    "_RequiredAccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": "IdentityTypeDef",
        "resource": "ResourceTypeDef",
        "permission": PermissionType,
    },
)
_OptionalAccessPolicySummaryTypeDef = TypedDict(
    "_OptionalAccessPolicySummaryTypeDef",
    {
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)

class AccessPolicySummaryTypeDef(
    _RequiredAccessPolicySummaryTypeDef, _OptionalAccessPolicySummaryTypeDef
):
    pass

ActionDefinitionTypeDef = TypedDict(
    "ActionDefinitionTypeDef",
    {
        "actionDefinitionId": str,
        "actionName": str,
        "actionType": str,
    },
)

ActionPayloadTypeDef = TypedDict(
    "ActionPayloadTypeDef",
    {
        "stringValue": str,
    },
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "actionId": str,
        "actionDefinitionId": str,
        "targetResource": "TargetResourceTypeDef",
    },
    total=False,
)

_RequiredAggregatedValueTypeDef = TypedDict(
    "_RequiredAggregatedValueTypeDef",
    {
        "timestamp": datetime,
        "value": "AggregatesTypeDef",
    },
)
_OptionalAggregatedValueTypeDef = TypedDict(
    "_OptionalAggregatedValueTypeDef",
    {
        "quality": QualityType,
    },
    total=False,
)

class AggregatedValueTypeDef(_RequiredAggregatedValueTypeDef, _OptionalAggregatedValueTypeDef):
    pass

AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": float,
        "count": float,
        "maximum": float,
        "minimum": float,
        "sum": float,
        "standardDeviation": float,
    },
    total=False,
)

_RequiredAlarmsTypeDef = TypedDict(
    "_RequiredAlarmsTypeDef",
    {
        "alarmRoleArn": str,
    },
)
_OptionalAlarmsTypeDef = TypedDict(
    "_OptionalAlarmsTypeDef",
    {
        "notificationLambdaArn": str,
    },
    total=False,
)

class AlarmsTypeDef(_RequiredAlarmsTypeDef, _OptionalAlarmsTypeDef):
    pass

AssetCompositeModelPathSegmentTypeDef = TypedDict(
    "AssetCompositeModelPathSegmentTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredAssetCompositeModelSummaryTypeDef = TypedDict(
    "_RequiredAssetCompositeModelSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "type": str,
        "description": str,
        "path": List["AssetCompositeModelPathSegmentTypeDef"],
    },
)
_OptionalAssetCompositeModelSummaryTypeDef = TypedDict(
    "_OptionalAssetCompositeModelSummaryTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

class AssetCompositeModelSummaryTypeDef(
    _RequiredAssetCompositeModelSummaryTypeDef, _OptionalAssetCompositeModelSummaryTypeDef
):
    pass

_RequiredAssetCompositeModelTypeDef = TypedDict(
    "_RequiredAssetCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "properties": List["AssetPropertyTypeDef"],
    },
)
_OptionalAssetCompositeModelTypeDef = TypedDict(
    "_OptionalAssetCompositeModelTypeDef",
    {
        "description": str,
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetCompositeModelTypeDef(
    _RequiredAssetCompositeModelTypeDef, _OptionalAssetCompositeModelTypeDef
):
    pass

AssetErrorDetailsTypeDef = TypedDict(
    "AssetErrorDetailsTypeDef",
    {
        "assetId": str,
        "code": Literal["INTERNAL_FAILURE"],
        "message": str,
    },
)

AssetHierarchyInfoTypeDef = TypedDict(
    "AssetHierarchyInfoTypeDef",
    {
        "parentAssetId": str,
        "childAssetId": str,
    },
    total=False,
)

_RequiredAssetHierarchyTypeDef = TypedDict(
    "_RequiredAssetHierarchyTypeDef",
    {
        "name": str,
    },
)
_OptionalAssetHierarchyTypeDef = TypedDict(
    "_OptionalAssetHierarchyTypeDef",
    {
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetHierarchyTypeDef(_RequiredAssetHierarchyTypeDef, _OptionalAssetHierarchyTypeDef):
    pass

_RequiredAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelDefinitionTypeDef",
    {
        "description": str,
        "properties": List["AssetModelPropertyDefinitionTypeDef"],
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetModelCompositeModelDefinitionTypeDef(
    _RequiredAssetModelCompositeModelDefinitionTypeDef,
    _OptionalAssetModelCompositeModelDefinitionTypeDef,
):
    pass

AssetModelCompositeModelPathSegmentTypeDef = TypedDict(
    "AssetModelCompositeModelPathSegmentTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredAssetModelCompositeModelSummaryTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "type": str,
    },
)
_OptionalAssetModelCompositeModelSummaryTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelSummaryTypeDef",
    {
        "externalId": str,
        "description": str,
        "path": List["AssetModelCompositeModelPathSegmentTypeDef"],
    },
    total=False,
)

class AssetModelCompositeModelSummaryTypeDef(
    _RequiredAssetModelCompositeModelSummaryTypeDef, _OptionalAssetModelCompositeModelSummaryTypeDef
):
    pass

_RequiredAssetModelCompositeModelTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalAssetModelCompositeModelTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelTypeDef",
    {
        "description": str,
        "properties": List["AssetModelPropertyTypeDef"],
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetModelCompositeModelTypeDef(
    _RequiredAssetModelCompositeModelTypeDef, _OptionalAssetModelCompositeModelTypeDef
):
    pass

_RequiredAssetModelHierarchyDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelHierarchyDefinitionTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
    },
)
_OptionalAssetModelHierarchyDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelHierarchyDefinitionTypeDef",
    {
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetModelHierarchyDefinitionTypeDef(
    _RequiredAssetModelHierarchyDefinitionTypeDef, _OptionalAssetModelHierarchyDefinitionTypeDef
):
    pass

_RequiredAssetModelHierarchyTypeDef = TypedDict(
    "_RequiredAssetModelHierarchyTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
    },
)
_OptionalAssetModelHierarchyTypeDef = TypedDict(
    "_OptionalAssetModelHierarchyTypeDef",
    {
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetModelHierarchyTypeDef(
    _RequiredAssetModelHierarchyTypeDef, _OptionalAssetModelHierarchyTypeDef
):
    pass

_RequiredAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelPropertyDefinitionTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelPropertyDefinitionTypeDef",
    {
        "dataTypeSpec": str,
        "unit": str,
        "id": str,
        "externalId": str,
    },
    total=False,
)

class AssetModelPropertyDefinitionTypeDef(
    _RequiredAssetModelPropertyDefinitionTypeDef, _OptionalAssetModelPropertyDefinitionTypeDef
):
    pass

AssetModelPropertyPathSegmentTypeDef = TypedDict(
    "AssetModelPropertyPathSegmentTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredAssetModelPropertySummaryTypeDef = TypedDict(
    "_RequiredAssetModelPropertySummaryTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertySummaryTypeDef = TypedDict(
    "_OptionalAssetModelPropertySummaryTypeDef",
    {
        "id": str,
        "dataTypeSpec": str,
        "unit": str,
        "assetModelCompositeModelId": str,
        "path": List["AssetModelPropertyPathSegmentTypeDef"],
        "externalId": str,
    },
    total=False,
)

class AssetModelPropertySummaryTypeDef(
    _RequiredAssetModelPropertySummaryTypeDef, _OptionalAssetModelPropertySummaryTypeDef
):
    pass

_RequiredAssetModelPropertyTypeDef = TypedDict(
    "_RequiredAssetModelPropertyTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyTypeDef = TypedDict(
    "_OptionalAssetModelPropertyTypeDef",
    {
        "id": str,
        "dataTypeSpec": str,
        "unit": str,
        "path": List["AssetModelPropertyPathSegmentTypeDef"],
        "externalId": str,
    },
    total=False,
)

class AssetModelPropertyTypeDef(
    _RequiredAssetModelPropertyTypeDef, _OptionalAssetModelPropertyTypeDef
):
    pass

_RequiredAssetModelStatusTypeDef = TypedDict(
    "_RequiredAssetModelStatusTypeDef",
    {
        "state": AssetModelStateType,
    },
)
_OptionalAssetModelStatusTypeDef = TypedDict(
    "_OptionalAssetModelStatusTypeDef",
    {
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)

class AssetModelStatusTypeDef(_RequiredAssetModelStatusTypeDef, _OptionalAssetModelStatusTypeDef):
    pass

_RequiredAssetModelSummaryTypeDef = TypedDict(
    "_RequiredAssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetModelStatusTypeDef",
    },
)
_OptionalAssetModelSummaryTypeDef = TypedDict(
    "_OptionalAssetModelSummaryTypeDef",
    {
        "assetModelType": AssetModelTypeType,
        "externalId": str,
    },
    total=False,
)

class AssetModelSummaryTypeDef(
    _RequiredAssetModelSummaryTypeDef, _OptionalAssetModelSummaryTypeDef
):
    pass

AssetPropertyPathSegmentTypeDef = TypedDict(
    "AssetPropertyPathSegmentTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

_RequiredAssetPropertySummaryTypeDef = TypedDict(
    "_RequiredAssetPropertySummaryTypeDef",
    {
        "id": str,
    },
)
_OptionalAssetPropertySummaryTypeDef = TypedDict(
    "_OptionalAssetPropertySummaryTypeDef",
    {
        "alias": str,
        "unit": str,
        "notification": "PropertyNotificationTypeDef",
        "assetCompositeModelId": str,
        "path": List["AssetPropertyPathSegmentTypeDef"],
        "externalId": str,
    },
    total=False,
)

class AssetPropertySummaryTypeDef(
    _RequiredAssetPropertySummaryTypeDef, _OptionalAssetPropertySummaryTypeDef
):
    pass

_RequiredAssetPropertyTypeDef = TypedDict(
    "_RequiredAssetPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
    },
)
_OptionalAssetPropertyTypeDef = TypedDict(
    "_OptionalAssetPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "dataTypeSpec": str,
        "unit": str,
        "path": List["AssetPropertyPathSegmentTypeDef"],
        "externalId": str,
    },
    total=False,
)

class AssetPropertyTypeDef(_RequiredAssetPropertyTypeDef, _OptionalAssetPropertyTypeDef):
    pass

_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {
        "value": "VariantTypeDef",
        "timestamp": "TimeInNanosTypeDef",
    },
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {
        "quality": QualityType,
    },
    total=False,
)

class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass

_RequiredAssetRelationshipSummaryTypeDef = TypedDict(
    "_RequiredAssetRelationshipSummaryTypeDef",
    {
        "relationshipType": Literal["HIERARCHY"],
    },
)
_OptionalAssetRelationshipSummaryTypeDef = TypedDict(
    "_OptionalAssetRelationshipSummaryTypeDef",
    {
        "hierarchyInfo": "AssetHierarchyInfoTypeDef",
    },
    total=False,
)

class AssetRelationshipSummaryTypeDef(
    _RequiredAssetRelationshipSummaryTypeDef, _OptionalAssetRelationshipSummaryTypeDef
):
    pass

_RequiredAssetStatusTypeDef = TypedDict(
    "_RequiredAssetStatusTypeDef",
    {
        "state": AssetStateType,
    },
)
_OptionalAssetStatusTypeDef = TypedDict(
    "_OptionalAssetStatusTypeDef",
    {
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)

class AssetStatusTypeDef(_RequiredAssetStatusTypeDef, _OptionalAssetStatusTypeDef):
    pass

_RequiredAssetSummaryTypeDef = TypedDict(
    "_RequiredAssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)
_OptionalAssetSummaryTypeDef = TypedDict(
    "_OptionalAssetSummaryTypeDef",
    {
        "description": str,
        "externalId": str,
    },
    total=False,
)

class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, _OptionalAssetSummaryTypeDef):
    pass

_RequiredAssociateAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
    },
)
_OptionalAssociateAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateAssetsRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class AssociateAssetsRequestRequestTypeDef(
    _RequiredAssociateAssetsRequestRequestTypeDef, _OptionalAssociateAssetsRequestRequestTypeDef
):
    pass

_RequiredAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
    },
)
_OptionalAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef(
    _RequiredAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef,
    _OptionalAssociateTimeSeriesToAssetPropertyRequestRequestTypeDef,
):
    pass

_RequiredAssociatedAssetsSummaryTypeDef = TypedDict(
    "_RequiredAssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)
_OptionalAssociatedAssetsSummaryTypeDef = TypedDict(
    "_OptionalAssociatedAssetsSummaryTypeDef",
    {
        "description": str,
        "externalId": str,
    },
    total=False,
)

class AssociatedAssetsSummaryTypeDef(
    _RequiredAssociatedAssetsSummaryTypeDef, _OptionalAssociatedAssetsSummaryTypeDef
):
    pass

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "defaultValue": str,
    },
    total=False,
)

_RequiredBatchAssociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": List[str],
    },
)
_OptionalBatchAssociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateProjectAssetsRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class BatchAssociateProjectAssetsRequestRequestTypeDef(
    _RequiredBatchAssociateProjectAssetsRequestRequestTypeDef,
    _OptionalBatchAssociateProjectAssetsRequestRequestTypeDef,
):
    pass

BatchAssociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchAssociateProjectAssetsResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": List[str],
    },
)
_OptionalBatchDisassociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateProjectAssetsRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class BatchDisassociateProjectAssetsRequestRequestTypeDef(
    _RequiredBatchDisassociateProjectAssetsRequestRequestTypeDef,
    _OptionalBatchDisassociateProjectAssetsRequestRequestTypeDef,
):
    pass

BatchDisassociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetAssetPropertyAggregatesEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyAggregatesEntryTypeDef",
    {
        "entryId": str,
        "aggregateTypes": List[AggregateTypeType],
        "resolution": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
    },
)
_OptionalBatchGetAssetPropertyAggregatesEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyAggregatesEntryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
    },
    total=False,
)

class BatchGetAssetPropertyAggregatesEntryTypeDef(
    _RequiredBatchGetAssetPropertyAggregatesEntryTypeDef,
    _OptionalBatchGetAssetPropertyAggregatesEntryTypeDef,
):
    pass

BatchGetAssetPropertyAggregatesErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyAggregatesErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)

BatchGetAssetPropertyAggregatesErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyAggregatesErrorCodeType,
        "errorTimestamp": datetime,
    },
)

_RequiredBatchGetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "entries": List["BatchGetAssetPropertyAggregatesEntryTypeDef"],
    },
)
_OptionalBatchGetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class BatchGetAssetPropertyAggregatesRequestRequestTypeDef(
    _RequiredBatchGetAssetPropertyAggregatesRequestRequestTypeDef,
    _OptionalBatchGetAssetPropertyAggregatesRequestRequestTypeDef,
):
    pass

BatchGetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesResponseTypeDef",
    {
        "errorEntries": List["BatchGetAssetPropertyAggregatesErrorEntryTypeDef"],
        "successEntries": List["BatchGetAssetPropertyAggregatesSuccessEntryTypeDef"],
        "skippedEntries": List["BatchGetAssetPropertyAggregatesSkippedEntryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetAssetPropertyAggregatesSkippedEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyAggregatesSkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
    },
)
_OptionalBatchGetAssetPropertyAggregatesSkippedEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyAggregatesSkippedEntryTypeDef",
    {
        "errorInfo": "BatchGetAssetPropertyAggregatesErrorInfoTypeDef",
    },
    total=False,
)

class BatchGetAssetPropertyAggregatesSkippedEntryTypeDef(
    _RequiredBatchGetAssetPropertyAggregatesSkippedEntryTypeDef,
    _OptionalBatchGetAssetPropertyAggregatesSkippedEntryTypeDef,
):
    pass

BatchGetAssetPropertyAggregatesSuccessEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyAggregatesSuccessEntryTypeDef",
    {
        "entryId": str,
        "aggregatedValues": List["AggregatedValueTypeDef"],
    },
)

_RequiredBatchGetAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
    },
)
_OptionalBatchGetAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueEntryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)

class BatchGetAssetPropertyValueEntryTypeDef(
    _RequiredBatchGetAssetPropertyValueEntryTypeDef, _OptionalBatchGetAssetPropertyValueEntryTypeDef
):
    pass

BatchGetAssetPropertyValueErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)

BatchGetAssetPropertyValueErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyValueErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueErrorCodeType,
        "errorTimestamp": datetime,
    },
)

_RequiredBatchGetAssetPropertyValueHistoryEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueHistoryEntryTypeDef",
    {
        "entryId": str,
    },
)
_OptionalBatchGetAssetPropertyValueHistoryEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueHistoryEntryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
    },
    total=False,
)

class BatchGetAssetPropertyValueHistoryEntryTypeDef(
    _RequiredBatchGetAssetPropertyValueHistoryEntryTypeDef,
    _OptionalBatchGetAssetPropertyValueHistoryEntryTypeDef,
):
    pass

BatchGetAssetPropertyValueHistoryErrorEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryErrorEntryTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueHistoryErrorCodeType,
        "errorMessage": str,
        "entryId": str,
    },
)

BatchGetAssetPropertyValueHistoryErrorInfoTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryErrorInfoTypeDef",
    {
        "errorCode": BatchGetAssetPropertyValueHistoryErrorCodeType,
        "errorTimestamp": datetime,
    },
)

_RequiredBatchGetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "entries": List["BatchGetAssetPropertyValueHistoryEntryTypeDef"],
    },
)
_OptionalBatchGetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class BatchGetAssetPropertyValueHistoryRequestRequestTypeDef(
    _RequiredBatchGetAssetPropertyValueHistoryRequestRequestTypeDef,
    _OptionalBatchGetAssetPropertyValueHistoryRequestRequestTypeDef,
):
    pass

BatchGetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistoryResponseTypeDef",
    {
        "errorEntries": List["BatchGetAssetPropertyValueHistoryErrorEntryTypeDef"],
        "successEntries": List["BatchGetAssetPropertyValueHistorySuccessEntryTypeDef"],
        "skippedEntries": List["BatchGetAssetPropertyValueHistorySkippedEntryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetAssetPropertyValueHistorySkippedEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueHistorySkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
    },
)
_OptionalBatchGetAssetPropertyValueHistorySkippedEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueHistorySkippedEntryTypeDef",
    {
        "errorInfo": "BatchGetAssetPropertyValueHistoryErrorInfoTypeDef",
    },
    total=False,
)

class BatchGetAssetPropertyValueHistorySkippedEntryTypeDef(
    _RequiredBatchGetAssetPropertyValueHistorySkippedEntryTypeDef,
    _OptionalBatchGetAssetPropertyValueHistorySkippedEntryTypeDef,
):
    pass

BatchGetAssetPropertyValueHistorySuccessEntryTypeDef = TypedDict(
    "BatchGetAssetPropertyValueHistorySuccessEntryTypeDef",
    {
        "entryId": str,
        "assetPropertyValueHistory": List["AssetPropertyValueTypeDef"],
    },
)

_RequiredBatchGetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueRequestRequestTypeDef",
    {
        "entries": List["BatchGetAssetPropertyValueEntryTypeDef"],
    },
)
_OptionalBatchGetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class BatchGetAssetPropertyValueRequestRequestTypeDef(
    _RequiredBatchGetAssetPropertyValueRequestRequestTypeDef,
    _OptionalBatchGetAssetPropertyValueRequestRequestTypeDef,
):
    pass

BatchGetAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchGetAssetPropertyValueResponseTypeDef",
    {
        "errorEntries": List["BatchGetAssetPropertyValueErrorEntryTypeDef"],
        "successEntries": List["BatchGetAssetPropertyValueSuccessEntryTypeDef"],
        "skippedEntries": List["BatchGetAssetPropertyValueSkippedEntryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetAssetPropertyValueSkippedEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueSkippedEntryTypeDef",
    {
        "entryId": str,
        "completionStatus": BatchEntryCompletionStatusType,
    },
)
_OptionalBatchGetAssetPropertyValueSkippedEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueSkippedEntryTypeDef",
    {
        "errorInfo": "BatchGetAssetPropertyValueErrorInfoTypeDef",
    },
    total=False,
)

class BatchGetAssetPropertyValueSkippedEntryTypeDef(
    _RequiredBatchGetAssetPropertyValueSkippedEntryTypeDef,
    _OptionalBatchGetAssetPropertyValueSkippedEntryTypeDef,
):
    pass

_RequiredBatchGetAssetPropertyValueSuccessEntryTypeDef = TypedDict(
    "_RequiredBatchGetAssetPropertyValueSuccessEntryTypeDef",
    {
        "entryId": str,
    },
)
_OptionalBatchGetAssetPropertyValueSuccessEntryTypeDef = TypedDict(
    "_OptionalBatchGetAssetPropertyValueSuccessEntryTypeDef",
    {
        "assetPropertyValue": "AssetPropertyValueTypeDef",
    },
    total=False,
)

class BatchGetAssetPropertyValueSuccessEntryTypeDef(
    _RequiredBatchGetAssetPropertyValueSuccessEntryTypeDef,
    _OptionalBatchGetAssetPropertyValueSuccessEntryTypeDef,
):
    pass

BatchPutAssetPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorEntryTypeDef",
    {
        "entryId": str,
        "errors": List["BatchPutAssetPropertyErrorTypeDef"],
    },
)

BatchPutAssetPropertyErrorTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorTypeDef",
    {
        "errorCode": BatchPutAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "timestamps": List["TimeInNanosTypeDef"],
    },
)

BatchPutAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    {
        "entries": List["PutAssetPropertyValueEntryTypeDef"],
    },
)

BatchPutAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchPutAssetPropertyValueResponseTypeDef",
    {
        "errorEntries": List["BatchPutAssetPropertyErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "name": str,
        "type": "ColumnTypeTypeDef",
    },
    total=False,
)

ColumnTypeTypeDef = TypedDict(
    "ColumnTypeTypeDef",
    {
        "scalarType": ScalarTypeType,
    },
    total=False,
)

_RequiredCompositeModelPropertyTypeDef = TypedDict(
    "_RequiredCompositeModelPropertyTypeDef",
    {
        "name": str,
        "type": str,
        "assetProperty": "PropertyTypeDef",
    },
)
_OptionalCompositeModelPropertyTypeDef = TypedDict(
    "_OptionalCompositeModelPropertyTypeDef",
    {
        "id": str,
        "externalId": str,
    },
    total=False,
)

class CompositeModelPropertyTypeDef(
    _RequiredCompositeModelPropertyTypeDef, _OptionalCompositeModelPropertyTypeDef
):
    pass

CompositionDetailsTypeDef = TypedDict(
    "CompositionDetailsTypeDef",
    {
        "compositionRelationship": List["CompositionRelationshipItemTypeDef"],
    },
    total=False,
)

CompositionRelationshipItemTypeDef = TypedDict(
    "CompositionRelationshipItemTypeDef",
    {
        "id": str,
    },
    total=False,
)

CompositionRelationshipSummaryTypeDef = TypedDict(
    "CompositionRelationshipSummaryTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelType": str,
    },
)

ConfigurationErrorDetailsTypeDef = TypedDict(
    "ConfigurationErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)

_RequiredConfigurationStatusTypeDef = TypedDict(
    "_RequiredConfigurationStatusTypeDef",
    {
        "state": ConfigurationStateType,
    },
)
_OptionalConfigurationStatusTypeDef = TypedDict(
    "_OptionalConfigurationStatusTypeDef",
    {
        "error": "ConfigurationErrorDetailsTypeDef",
    },
    total=False,
)

class ConfigurationStatusTypeDef(
    _RequiredConfigurationStatusTypeDef, _OptionalConfigurationStatusTypeDef
):
    pass

_RequiredCreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
    },
)
_OptionalCreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAccessPolicyRequestRequestTypeDef(
    _RequiredCreateAccessPolicyRequestRequestTypeDef,
    _OptionalCreateAccessPolicyRequestRequestTypeDef,
):
    pass

CreateAccessPolicyResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelName": str,
        "assetModelCompositeModelType": str,
    },
)
_OptionalCreateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "parentAssetModelCompositeModelId": str,
        "assetModelCompositeModelExternalId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelDescription": str,
        "clientToken": str,
        "composedAssetModelId": str,
        "assetModelCompositeModelProperties": List["AssetModelPropertyDefinitionTypeDef"],
    },
    total=False,
)

class CreateAssetModelCompositeModelRequestRequestTypeDef(
    _RequiredCreateAssetModelCompositeModelRequestRequestTypeDef,
    _OptionalCreateAssetModelCompositeModelRequestRequestTypeDef,
):
    pass

CreateAssetModelCompositeModelResponseTypeDef = TypedDict(
    "CreateAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelPath": List["AssetModelCompositeModelPathSegmentTypeDef"],
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssetModelRequestRequestTypeDef",
    {
        "assetModelName": str,
    },
)
_OptionalCreateAssetModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssetModelRequestRequestTypeDef",
    {
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyDefinitionTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyDefinitionTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelDefinitionTypeDef"],
        "clientToken": str,
        "tags": Dict[str, str],
        "assetModelId": str,
        "assetModelExternalId": str,
        "assetModelType": AssetModelTypeType,
    },
    total=False,
)

class CreateAssetModelRequestRequestTypeDef(
    _RequiredCreateAssetModelRequestRequestTypeDef, _OptionalCreateAssetModelRequestRequestTypeDef
):
    pass

CreateAssetModelResponseTypeDef = TypedDict(
    "CreateAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssetRequestRequestTypeDef",
    {
        "assetName": str,
        "assetModelId": str,
    },
)
_OptionalCreateAssetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssetRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
        "assetDescription": str,
        "assetId": str,
        "assetExternalId": str,
    },
    total=False,
)

class CreateAssetRequestRequestTypeDef(
    _RequiredCreateAssetRequestRequestTypeDef, _OptionalCreateAssetRequestRequestTypeDef
):
    pass

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBulkImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBulkImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobRoleArn": str,
        "files": List["FileTypeDef"],
        "errorReportLocation": "ErrorReportLocationTypeDef",
        "jobConfiguration": "JobConfigurationTypeDef",
    },
)
_OptionalCreateBulkImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBulkImportJobRequestRequestTypeDef",
    {
        "adaptiveIngestion": bool,
        "deleteFilesAfterImport": bool,
    },
    total=False,
)

class CreateBulkImportJobRequestRequestTypeDef(
    _RequiredCreateBulkImportJobRequestRequestTypeDef,
    _OptionalCreateBulkImportJobRequestRequestTypeDef,
):
    pass

CreateBulkImportJobResponseTypeDef = TypedDict(
    "CreateBulkImportJobResponseTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDashboardRequestRequestTypeDef",
    {
        "projectId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
    },
)
_OptionalCreateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDashboardRequestRequestTypeDef",
    {
        "dashboardDescription": str,
        "clientToken": str,
        "tags": Dict[str, str],
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
        "dashboardId": str,
        "dashboardArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayRequestRequestTypeDef",
    {
        "gatewayName": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
    },
)
_OptionalCreateGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateGatewayRequestRequestTypeDef(
    _RequiredCreateGatewayRequestRequestTypeDef, _OptionalCreateGatewayRequestRequestTypeDef
):
    pass

CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortalRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePortalRequestRequestTypeDef",
    {
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
    },
)
_OptionalCreatePortalRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePortalRequestRequestTypeDef",
    {
        "portalDescription": str,
        "clientToken": str,
        "portalLogoImageFile": "ImageFileTypeDef",
        "tags": Dict[str, str],
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
    },
    total=False,
)

class CreatePortalRequestRequestTypeDef(
    _RequiredCreatePortalRequestRequestTypeDef, _OptionalCreatePortalRequestRequestTypeDef
):
    pass

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalStartUrl": str,
        "portalStatus": "PortalStatusTypeDef",
        "ssoApplicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "portalId": str,
        "projectName": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "projectDescription": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvTypeDef = TypedDict(
    "CsvTypeDef",
    {
        "columnNames": List[ColumnNameType],
    },
)

CustomerManagedS3StorageTypeDef = TypedDict(
    "CustomerManagedS3StorageTypeDef",
    {
        "s3ResourceArn": str,
        "roleArn": str,
    },
)

_RequiredDashboardSummaryTypeDef = TypedDict(
    "_RequiredDashboardSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
_OptionalDashboardSummaryTypeDef = TypedDict(
    "_OptionalDashboardSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)

class DashboardSummaryTypeDef(_RequiredDashboardSummaryTypeDef, _OptionalDashboardSummaryTypeDef):
    pass

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "scalarValue": str,
        "arrayValue": List[Dict[str, Any]],
        "rowValue": Dict[str, Any],
        "nullValue": bool,
    },
    total=False,
)

_RequiredDeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)
_OptionalDeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAccessPolicyRequestRequestTypeDef(
    _RequiredDeleteAccessPolicyRequestRequestTypeDef,
    _OptionalDeleteAccessPolicyRequestRequestTypeDef,
):
    pass

_RequiredDeleteAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
    },
)
_OptionalDeleteAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAssetModelCompositeModelRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAssetModelCompositeModelRequestRequestTypeDef(
    _RequiredDeleteAssetModelCompositeModelRequestRequestTypeDef,
    _OptionalDeleteAssetModelCompositeModelRequestRequestTypeDef,
):
    pass

DeleteAssetModelCompositeModelResponseTypeDef = TypedDict(
    "DeleteAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAssetModelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalDeleteAssetModelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAssetModelRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAssetModelRequestRequestTypeDef(
    _RequiredDeleteAssetModelRequestRequestTypeDef, _OptionalDeleteAssetModelRequestRequestTypeDef
):
    pass

DeleteAssetModelResponseTypeDef = TypedDict(
    "DeleteAssetModelResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAssetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAssetRequestRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalDeleteAssetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAssetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAssetRequestRequestTypeDef(
    _RequiredDeleteAssetRequestRequestTypeDef, _OptionalDeleteAssetRequestRequestTypeDef
):
    pass

DeleteAssetResponseTypeDef = TypedDict(
    "DeleteAssetResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
    },
)
_OptionalDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDashboardRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteDashboardRequestRequestTypeDef(
    _RequiredDeleteDashboardRequestRequestTypeDef, _OptionalDeleteDashboardRequestRequestTypeDef
):
    pass

DeleteGatewayRequestRequestTypeDef = TypedDict(
    "DeleteGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)

_RequiredDeletePortalRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePortalRequestRequestTypeDef",
    {
        "portalId": str,
    },
)
_OptionalDeletePortalRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePortalRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeletePortalRequestRequestTypeDef(
    _RequiredDeletePortalRequestRequestTypeDef, _OptionalDeletePortalRequestRequestTypeDef
):
    pass

DeletePortalResponseTypeDef = TypedDict(
    "DeletePortalResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalDeleteProjectRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteProjectRequestRequestTypeDef(
    _RequiredDeleteProjectRequestRequestTypeDef, _OptionalDeleteProjectRequestRequestTypeDef
):
    pass

DeleteTimeSeriesRequestRequestTypeDef = TypedDict(
    "DeleteTimeSeriesRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
        "clientToken": str,
    },
    total=False,
)

DescribeAccessPolicyRequestRequestTypeDef = TypedDict(
    "DescribeAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)

DescribeAccessPolicyResponseTypeDef = TypedDict(
    "DescribeAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
        "accessPolicyCreationDate": datetime,
        "accessPolicyLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActionRequestRequestTypeDef = TypedDict(
    "DescribeActionRequestRequestTypeDef",
    {
        "actionId": str,
    },
)

DescribeActionResponseTypeDef = TypedDict(
    "DescribeActionResponseTypeDef",
    {
        "actionId": str,
        "targetResource": "TargetResourceTypeDef",
        "actionDefinitionId": str,
        "actionPayload": "ActionPayloadTypeDef",
        "executionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetCompositeModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetCompositeModelRequestRequestTypeDef",
    {
        "assetId": str,
        "assetCompositeModelId": str,
    },
)

DescribeAssetCompositeModelResponseTypeDef = TypedDict(
    "DescribeAssetCompositeModelResponseTypeDef",
    {
        "assetId": str,
        "assetCompositeModelId": str,
        "assetCompositeModelExternalId": str,
        "assetCompositeModelPath": List["AssetCompositeModelPathSegmentTypeDef"],
        "assetCompositeModelName": str,
        "assetCompositeModelDescription": str,
        "assetCompositeModelType": str,
        "assetCompositeModelProperties": List["AssetPropertyTypeDef"],
        "assetCompositeModelSummaries": List["AssetCompositeModelSummaryTypeDef"],
        "actionDefinitions": List["ActionDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
    },
)

DescribeAssetModelCompositeModelResponseTypeDef = TypedDict(
    "DescribeAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelExternalId": str,
        "assetModelCompositeModelPath": List["AssetModelCompositeModelPathSegmentTypeDef"],
        "assetModelCompositeModelName": str,
        "assetModelCompositeModelDescription": str,
        "assetModelCompositeModelType": str,
        "assetModelCompositeModelProperties": List["AssetModelPropertyTypeDef"],
        "compositionDetails": "CompositionDetailsTypeDef",
        "assetModelCompositeModelSummaries": List["AssetModelCompositeModelSummaryTypeDef"],
        "actionDefinitions": List["ActionDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssetModelRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalDescribeAssetModelRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAssetModelRequestRequestTypeDef",
    {
        "excludeProperties": bool,
    },
    total=False,
)

class DescribeAssetModelRequestRequestTypeDef(
    _RequiredDescribeAssetModelRequestRequestTypeDef,
    _OptionalDescribeAssetModelRequestRequestTypeDef,
):
    pass

DescribeAssetModelResponseTypeDef = TypedDict(
    "DescribeAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelName": str,
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"],
        "assetModelCreationDate": datetime,
        "assetModelLastUpdateDate": datetime,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "assetModelType": AssetModelTypeType,
        "assetModelCompositeModelSummaries": List["AssetModelCompositeModelSummaryTypeDef"],
        "assetModelExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetPropertyRequestRequestTypeDef = TypedDict(
    "DescribeAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)

DescribeAssetPropertyResponseTypeDef = TypedDict(
    "DescribeAssetPropertyResponseTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperty": "PropertyTypeDef",
        "compositeModel": "CompositeModelPropertyTypeDef",
        "assetExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssetRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAssetRequestRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalDescribeAssetRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAssetRequestRequestTypeDef",
    {
        "excludeProperties": bool,
    },
    total=False,
)

class DescribeAssetRequestRequestTypeDef(
    _RequiredDescribeAssetRequestRequestTypeDef, _OptionalDescribeAssetRequestRequestTypeDef
):
    pass

DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperties": List["AssetPropertyTypeDef"],
        "assetHierarchies": List["AssetHierarchyTypeDef"],
        "assetCompositeModels": List["AssetCompositeModelTypeDef"],
        "assetCreationDate": datetime,
        "assetLastUpdateDate": datetime,
        "assetStatus": "AssetStatusTypeDef",
        "assetDescription": str,
        "assetCompositeModelSummaries": List["AssetCompositeModelSummaryTypeDef"],
        "assetExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBulkImportJobRequestRequestTypeDef = TypedDict(
    "DescribeBulkImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeBulkImportJobResponseTypeDef = TypedDict(
    "DescribeBulkImportJobResponseTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "jobRoleArn": str,
        "files": List["FileTypeDef"],
        "errorReportLocation": "ErrorReportLocationTypeDef",
        "jobConfiguration": "JobConfigurationTypeDef",
        "jobCreationDate": datetime,
        "jobLastUpdateDate": datetime,
        "adaptiveIngestion": bool,
        "deleteFilesAfterImport": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardRequestRequestTypeDef = TypedDict(
    "DescribeDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
    },
)

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "dashboardName": str,
        "projectId": str,
        "dashboardDescription": str,
        "dashboardDefinition": str,
        "dashboardCreationDate": datetime,
        "dashboardLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
    },
)

DescribeGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayRequestRequestTypeDef = TypedDict(
    "DescribeGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)

DescribeGatewayResponseTypeDef = TypedDict(
    "DescribeGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "gatewayArn": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortalRequestRequestTypeDef = TypedDict(
    "DescribePortalRequestRequestTypeDef",
    {
        "portalId": str,
    },
)

DescribePortalResponseTypeDef = TypedDict(
    "DescribePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalName": str,
        "portalDescription": str,
        "portalClientId": str,
        "portalStartUrl": str,
        "portalContactEmail": str,
        "portalStatus": "PortalStatusTypeDef",
        "portalCreationDate": datetime,
        "portalLastUpdateDate": datetime,
        "portalLogoImageLocation": "ImageLocationTypeDef",
        "roleArn": str,
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "projectName": str,
        "portalId": str,
        "projectDescription": str,
        "projectCreationDate": datetime,
        "projectLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageConfigurationResponseTypeDef = TypedDict(
    "DescribeStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": "MultiLayerStorageTypeDef",
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "configurationStatus": "ConfigurationStatusTypeDef",
        "lastUpdateDate": datetime,
        "warmTier": WarmTierStateType,
        "warmTierRetentionPeriod": "WarmTierRetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeSeriesRequestRequestTypeDef = TypedDict(
    "DescribeTimeSeriesRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
    },
    total=False,
)

DescribeTimeSeriesResponseTypeDef = TypedDict(
    "DescribeTimeSeriesResponseTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "alias": str,
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "dataTypeSpec": str,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "timeSeriesArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetailedErrorTypeDef = TypedDict(
    "DetailedErrorTypeDef",
    {
        "code": DetailedErrorCodeType,
        "message": str,
    },
)

_RequiredDisassociateAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
    },
)
_OptionalDisassociateAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateAssetsRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisassociateAssetsRequestRequestTypeDef(
    _RequiredDisassociateAssetsRequestRequestTypeDef,
    _OptionalDisassociateAssetsRequestRequestTypeDef,
):
    pass

_RequiredDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
    },
)
_OptionalDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef(
    _RequiredDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef,
    _OptionalDisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef,
):
    pass

_RequiredErrorDetailsTypeDef = TypedDict(
    "_RequiredErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)
_OptionalErrorDetailsTypeDef = TypedDict(
    "_OptionalErrorDetailsTypeDef",
    {
        "details": List["DetailedErrorTypeDef"],
    },
    total=False,
)

class ErrorDetailsTypeDef(_RequiredErrorDetailsTypeDef, _OptionalErrorDetailsTypeDef):
    pass

ErrorReportLocationTypeDef = TypedDict(
    "ErrorReportLocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
)

_RequiredExecuteActionRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteActionRequestRequestTypeDef",
    {
        "targetResource": "TargetResourceTypeDef",
        "actionDefinitionId": str,
        "actionPayload": "ActionPayloadTypeDef",
    },
)
_OptionalExecuteActionRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteActionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ExecuteActionRequestRequestTypeDef(
    _RequiredExecuteActionRequestRequestTypeDef, _OptionalExecuteActionRequestRequestTypeDef
):
    pass

ExecuteActionResponseTypeDef = TypedDict(
    "ExecuteActionResponseTypeDef",
    {
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteQueryRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteQueryRequestRequestTypeDef",
    {
        "queryStatement": str,
    },
)
_OptionalExecuteQueryRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteQueryRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ExecuteQueryRequestRequestTypeDef(
    _RequiredExecuteQueryRequestRequestTypeDef, _OptionalExecuteQueryRequestRequestTypeDef
):
    pass

ExecuteQueryResponseTypeDef = TypedDict(
    "ExecuteQueryResponseTypeDef",
    {
        "columns": List["ColumnInfoTypeDef"],
        "rows": List["RowTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExpressionVariableTypeDef = TypedDict(
    "ExpressionVariableTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
)

FileFormatTypeDef = TypedDict(
    "FileFormatTypeDef",
    {
        "csv": "CsvTypeDef",
        "parquet": Dict[str, Any],
    },
    total=False,
)

_RequiredFileTypeDef = TypedDict(
    "_RequiredFileTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalFileTypeDef = TypedDict(
    "_OptionalFileTypeDef",
    {
        "versionId": str,
    },
    total=False,
)

class FileTypeDef(_RequiredFileTypeDef, _OptionalFileTypeDef):
    pass

ForwardingConfigTypeDef = TypedDict(
    "ForwardingConfigTypeDef",
    {
        "state": ForwardingConfigStateType,
    },
)

GatewayCapabilitySummaryTypeDef = TypedDict(
    "GatewayCapabilitySummaryTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
    },
)

GatewayPlatformTypeDef = TypedDict(
    "GatewayPlatformTypeDef",
    {
        "greengrass": "GreengrassTypeDef",
        "greengrassV2": "GreengrassV2TypeDef",
    },
    total=False,
)

_RequiredGatewaySummaryTypeDef = TypedDict(
    "_RequiredGatewaySummaryTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
)
_OptionalGatewaySummaryTypeDef = TypedDict(
    "_OptionalGatewaySummaryTypeDef",
    {
        "gatewayPlatform": "GatewayPlatformTypeDef",
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
    },
    total=False,
)

class GatewaySummaryTypeDef(_RequiredGatewaySummaryTypeDef, _OptionalGatewaySummaryTypeDef):
    pass

_RequiredGetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "_RequiredGetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "aggregateTypes": List[AggregateTypeType],
        "resolution": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
    },
)
_OptionalGetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "_OptionalGetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetAssetPropertyAggregatesRequestRequestTypeDef(
    _RequiredGetAssetPropertyAggregatesRequestRequestTypeDef,
    _OptionalGetAssetPropertyAggregatesRequestRequestTypeDef,
):
    pass

GetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "GetAssetPropertyAggregatesResponseTypeDef",
    {
        "aggregatedValues": List["AggregatedValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryResponseTypeDef",
    {
        "assetPropertyValueHistory": List["AssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)

GetAssetPropertyValueResponseTypeDef = TypedDict(
    "GetAssetPropertyValueResponseTypeDef",
    {
        "propertyValue": "AssetPropertyValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInterpolatedAssetPropertyValuesRequestRequestTypeDef = TypedDict(
    "_RequiredGetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    {
        "startTimeInSeconds": int,
        "endTimeInSeconds": int,
        "quality": QualityType,
        "intervalInSeconds": int,
        "type": str,
    },
)
_OptionalGetInterpolatedAssetPropertyValuesRequestRequestTypeDef = TypedDict(
    "_OptionalGetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "startTimeOffsetInNanos": int,
        "endTimeOffsetInNanos": int,
        "nextToken": str,
        "maxResults": int,
        "intervalWindowInSeconds": int,
    },
    total=False,
)

class GetInterpolatedAssetPropertyValuesRequestRequestTypeDef(
    _RequiredGetInterpolatedAssetPropertyValuesRequestRequestTypeDef,
    _OptionalGetInterpolatedAssetPropertyValuesRequestRequestTypeDef,
):
    pass

GetInterpolatedAssetPropertyValuesResponseTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    {
        "interpolatedAssetPropertyValues": List["InterpolatedAssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GreengrassTypeDef = TypedDict(
    "GreengrassTypeDef",
    {
        "groupArn": str,
    },
)

GreengrassV2TypeDef = TypedDict(
    "GreengrassV2TypeDef",
    {
        "coreDeviceThingName": str,
    },
)

GroupIdentityTypeDef = TypedDict(
    "GroupIdentityTypeDef",
    {
        "id": str,
    },
)

IAMRoleIdentityTypeDef = TypedDict(
    "IAMRoleIdentityTypeDef",
    {
        "arn": str,
    },
)

IAMUserIdentityTypeDef = TypedDict(
    "IAMUserIdentityTypeDef",
    {
        "arn": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "user": "UserIdentityTypeDef",
        "group": "GroupIdentityTypeDef",
        "iamUser": "IAMUserIdentityTypeDef",
        "iamRole": "IAMRoleIdentityTypeDef",
    },
    total=False,
)

ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "type": Literal["PNG"],
    },
)

ImageLocationTypeDef = TypedDict(
    "ImageLocationTypeDef",
    {
        "id": str,
        "url": str,
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "id": str,
        "file": "ImageFileTypeDef",
    },
    total=False,
)

InterpolatedAssetPropertyValueTypeDef = TypedDict(
    "InterpolatedAssetPropertyValueTypeDef",
    {
        "timestamp": "TimeInNanosTypeDef",
        "value": "VariantTypeDef",
    },
)

JobConfigurationTypeDef = TypedDict(
    "JobConfigurationTypeDef",
    {
        "fileFormat": "FileFormatTypeDef",
    },
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "status": JobStatusType,
    },
)

ListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestRequestTypeDef",
    {
        "identityType": IdentityTypeType,
        "identityId": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "iamArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicySummaries": List["AccessPolicySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListActionsRequestRequestTypeDef",
    {
        "targetResourceType": Literal["ASSET"],
        "targetResourceId": str,
    },
)
_OptionalListActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListActionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListActionsRequestRequestTypeDef(
    _RequiredListActionsRequestRequestTypeDef, _OptionalListActionsRequestRequestTypeDef
):
    pass

ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "actionSummaries": List["ActionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetModelCompositeModelsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetModelCompositeModelsRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalListAssetModelCompositeModelsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetModelCompositeModelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssetModelCompositeModelsRequestRequestTypeDef(
    _RequiredListAssetModelCompositeModelsRequestRequestTypeDef,
    _OptionalListAssetModelCompositeModelsRequestRequestTypeDef,
):
    pass

ListAssetModelCompositeModelsResponseTypeDef = TypedDict(
    "ListAssetModelCompositeModelsResponseTypeDef",
    {
        "assetModelCompositeModelSummaries": List["AssetModelCompositeModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetModelPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetModelPropertiesRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalListAssetModelPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetModelPropertiesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": ListAssetModelPropertiesFilterType,
    },
    total=False,
)

class ListAssetModelPropertiesRequestRequestTypeDef(
    _RequiredListAssetModelPropertiesRequestRequestTypeDef,
    _OptionalListAssetModelPropertiesRequestRequestTypeDef,
):
    pass

ListAssetModelPropertiesResponseTypeDef = TypedDict(
    "ListAssetModelPropertiesResponseTypeDef",
    {
        "assetModelPropertySummaries": List["AssetModelPropertySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetModelsRequestRequestTypeDef = TypedDict(
    "ListAssetModelsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "assetModelTypes": List[AssetModelTypeType],
    },
    total=False,
)

ListAssetModelsResponseTypeDef = TypedDict(
    "ListAssetModelsResponseTypeDef",
    {
        "assetModelSummaries": List["AssetModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetPropertiesRequestRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalListAssetPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetPropertiesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": ListAssetPropertiesFilterType,
    },
    total=False,
)

class ListAssetPropertiesRequestRequestTypeDef(
    _RequiredListAssetPropertiesRequestRequestTypeDef,
    _OptionalListAssetPropertiesRequestRequestTypeDef,
):
    pass

ListAssetPropertiesResponseTypeDef = TypedDict(
    "ListAssetPropertiesResponseTypeDef",
    {
        "assetPropertySummaries": List["AssetPropertySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetRelationshipsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetRelationshipsRequestRequestTypeDef",
    {
        "assetId": str,
        "traversalType": Literal["PATH_TO_ROOT"],
    },
)
_OptionalListAssetRelationshipsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetRelationshipsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssetRelationshipsRequestRequestTypeDef(
    _RequiredListAssetRelationshipsRequestRequestTypeDef,
    _OptionalListAssetRelationshipsRequestRequestTypeDef,
):
    pass

ListAssetRelationshipsResponseTypeDef = TypedDict(
    "ListAssetRelationshipsResponseTypeDef",
    {
        "assetRelationshipSummaries": List["AssetRelationshipSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "assetModelId": str,
        "filter": ListAssetsFilterType,
    },
    total=False,
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "assetSummaries": List["AssetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedAssetsRequestRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalListAssociatedAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedAssetsRequestRequestTypeDef",
    {
        "hierarchyId": str,
        "traversalDirection": TraversalDirectionType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssociatedAssetsRequestRequestTypeDef(
    _RequiredListAssociatedAssetsRequestRequestTypeDef,
    _OptionalListAssociatedAssetsRequestRequestTypeDef,
):
    pass

ListAssociatedAssetsResponseTypeDef = TypedDict(
    "ListAssociatedAssetsResponseTypeDef",
    {
        "assetSummaries": List["AssociatedAssetsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBulkImportJobsRequestRequestTypeDef = TypedDict(
    "ListBulkImportJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": ListBulkImportJobsFilterType,
    },
    total=False,
)

ListBulkImportJobsResponseTypeDef = TypedDict(
    "ListBulkImportJobsResponseTypeDef",
    {
        "jobSummaries": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCompositionRelationshipsRequestRequestTypeDef = TypedDict(
    "_RequiredListCompositionRelationshipsRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalListCompositionRelationshipsRequestRequestTypeDef = TypedDict(
    "_OptionalListCompositionRelationshipsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCompositionRelationshipsRequestRequestTypeDef(
    _RequiredListCompositionRelationshipsRequestRequestTypeDef,
    _OptionalListCompositionRelationshipsRequestRequestTypeDef,
):
    pass

ListCompositionRelationshipsResponseTypeDef = TypedDict(
    "ListCompositionRelationshipsResponseTypeDef",
    {
        "compositionRelationshipSummaries": List["CompositionRelationshipSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDashboardsRequestRequestTypeDef = TypedDict(
    "_RequiredListDashboardsRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListDashboardsRequestRequestTypeDef = TypedDict(
    "_OptionalListDashboardsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
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
        "dashboardSummaries": List["DashboardSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "gatewaySummaries": List["GatewaySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "portalSummaries": List["PortalSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredListProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListProjectAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalListProjectAssetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListProjectAssetsRequestRequestTypeDef(
    _RequiredListProjectAssetsRequestRequestTypeDef, _OptionalListProjectAssetsRequestRequestTypeDef
):
    pass

ListProjectAssetsResponseTypeDef = TypedDict(
    "ListProjectAssetsResponseTypeDef",
    {
        "assetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectsRequestRequestTypeDef = TypedDict(
    "_RequiredListProjectsRequestRequestTypeDef",
    {
        "portalId": str,
    },
)
_OptionalListProjectsRequestRequestTypeDef = TypedDict(
    "_OptionalListProjectsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListProjectsRequestRequestTypeDef(
    _RequiredListProjectsRequestRequestTypeDef, _OptionalListProjectsRequestRequestTypeDef
):
    pass

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projectSummaries": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTimeSeriesRequestRequestTypeDef = TypedDict(
    "ListTimeSeriesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "assetId": str,
        "aliasPrefix": str,
        "timeSeriesType": ListTimeSeriesTypeType,
    },
    total=False,
)

ListTimeSeriesResponseTypeDef = TypedDict(
    "ListTimeSeriesResponseTypeDef",
    {
        "TimeSeriesSummaries": List["TimeSeriesSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "level": LoggingLevelType,
    },
)

MeasurementProcessingConfigTypeDef = TypedDict(
    "MeasurementProcessingConfigTypeDef",
    {
        "forwardingConfig": "ForwardingConfigTypeDef",
    },
)

MeasurementTypeDef = TypedDict(
    "MeasurementTypeDef",
    {
        "processingConfig": "MeasurementProcessingConfigTypeDef",
    },
    total=False,
)

MetricProcessingConfigTypeDef = TypedDict(
    "MetricProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
    },
)

_RequiredMetricTypeDef = TypedDict(
    "_RequiredMetricTypeDef",
    {
        "expression": str,
        "variables": List["ExpressionVariableTypeDef"],
        "window": "MetricWindowTypeDef",
    },
)
_OptionalMetricTypeDef = TypedDict(
    "_OptionalMetricTypeDef",
    {
        "processingConfig": "MetricProcessingConfigTypeDef",
    },
    total=False,
)

class MetricTypeDef(_RequiredMetricTypeDef, _OptionalMetricTypeDef):
    pass

MetricWindowTypeDef = TypedDict(
    "MetricWindowTypeDef",
    {
        "tumbling": "TumblingWindowTypeDef",
    },
    total=False,
)

MonitorErrorDetailsTypeDef = TypedDict(
    "MonitorErrorDetailsTypeDef",
    {
        "code": MonitorErrorCodeType,
        "message": str,
    },
    total=False,
)

MultiLayerStorageTypeDef = TypedDict(
    "MultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": "CustomerManagedS3StorageTypeDef",
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

PortalResourceTypeDef = TypedDict(
    "PortalResourceTypeDef",
    {
        "id": str,
    },
)

_RequiredPortalStatusTypeDef = TypedDict(
    "_RequiredPortalStatusTypeDef",
    {
        "state": PortalStateType,
    },
)
_OptionalPortalStatusTypeDef = TypedDict(
    "_OptionalPortalStatusTypeDef",
    {
        "error": "MonitorErrorDetailsTypeDef",
    },
    total=False,
)

class PortalStatusTypeDef(_RequiredPortalStatusTypeDef, _OptionalPortalStatusTypeDef):
    pass

_RequiredPortalSummaryTypeDef = TypedDict(
    "_RequiredPortalSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "startUrl": str,
        "status": "PortalStatusTypeDef",
    },
)
_OptionalPortalSummaryTypeDef = TypedDict(
    "_OptionalPortalSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "roleArn": str,
    },
    total=False,
)

class PortalSummaryTypeDef(_RequiredPortalSummaryTypeDef, _OptionalPortalSummaryTypeDef):
    pass

ProjectResourceTypeDef = TypedDict(
    "ProjectResourceTypeDef",
    {
        "id": str,
    },
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

PropertyNotificationTypeDef = TypedDict(
    "PropertyNotificationTypeDef",
    {
        "topic": str,
        "state": PropertyNotificationStateType,
    },
)

_RequiredPropertyTypeDef = TypedDict(
    "_RequiredPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
    },
)
_OptionalPropertyTypeDef = TypedDict(
    "_OptionalPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "unit": str,
        "type": "PropertyTypeTypeDef",
        "path": List["AssetPropertyPathSegmentTypeDef"],
        "externalId": str,
    },
    total=False,
)

class PropertyTypeDef(_RequiredPropertyTypeDef, _OptionalPropertyTypeDef):
    pass

PropertyTypeTypeDef = TypedDict(
    "PropertyTypeTypeDef",
    {
        "attribute": "AttributeTypeDef",
        "measurement": "MeasurementTypeDef",
        "transform": "TransformTypeDef",
        "metric": "MetricTypeDef",
    },
    total=False,
)

_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "propertyValues": List["AssetPropertyValueTypeDef"],
    },
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)

class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass

_RequiredPutDefaultEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutDefaultEncryptionConfigurationRequestRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalPutDefaultEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutDefaultEncryptionConfigurationRequestRequestTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

class PutDefaultEncryptionConfigurationRequestRequestTypeDef(
    _RequiredPutDefaultEncryptionConfigurationRequestRequestTypeDef,
    _OptionalPutDefaultEncryptionConfigurationRequestRequestTypeDef,
):
    pass

PutDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

_RequiredPutStorageConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutStorageConfigurationRequestRequestTypeDef",
    {
        "storageType": StorageTypeType,
    },
)
_OptionalPutStorageConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutStorageConfigurationRequestRequestTypeDef",
    {
        "multiLayerStorage": "MultiLayerStorageTypeDef",
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "warmTier": WarmTierStateType,
        "warmTierRetentionPeriod": "WarmTierRetentionPeriodTypeDef",
    },
    total=False,
)

class PutStorageConfigurationRequestRequestTypeDef(
    _RequiredPutStorageConfigurationRequestRequestTypeDef,
    _OptionalPutStorageConfigurationRequestRequestTypeDef,
):
    pass

PutStorageConfigurationResponseTypeDef = TypedDict(
    "PutStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": "MultiLayerStorageTypeDef",
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "configurationStatus": "ConfigurationStatusTypeDef",
        "warmTier": WarmTierStateType,
        "warmTierRetentionPeriod": "WarmTierRetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "portal": "PortalResourceTypeDef",
        "project": "ProjectResourceTypeDef",
    },
    total=False,
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "numberOfDays": int,
        "unlimited": bool,
    },
    total=False,
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "data": List[Dict[str, Any]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetResourceTypeDef = TypedDict(
    "TargetResourceTypeDef",
    {
        "assetId": str,
    },
)

_RequiredTimeInNanosTypeDef = TypedDict(
    "_RequiredTimeInNanosTypeDef",
    {
        "timeInSeconds": int,
    },
)
_OptionalTimeInNanosTypeDef = TypedDict(
    "_OptionalTimeInNanosTypeDef",
    {
        "offsetInNanos": int,
    },
    total=False,
)

class TimeInNanosTypeDef(_RequiredTimeInNanosTypeDef, _OptionalTimeInNanosTypeDef):
    pass

_RequiredTimeSeriesSummaryTypeDef = TypedDict(
    "_RequiredTimeSeriesSummaryTypeDef",
    {
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "timeSeriesArn": str,
    },
)
_OptionalTimeSeriesSummaryTypeDef = TypedDict(
    "_OptionalTimeSeriesSummaryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "alias": str,
        "dataTypeSpec": str,
    },
    total=False,
)

class TimeSeriesSummaryTypeDef(
    _RequiredTimeSeriesSummaryTypeDef, _OptionalTimeSeriesSummaryTypeDef
):
    pass

_RequiredTransformProcessingConfigTypeDef = TypedDict(
    "_RequiredTransformProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
    },
)
_OptionalTransformProcessingConfigTypeDef = TypedDict(
    "_OptionalTransformProcessingConfigTypeDef",
    {
        "forwardingConfig": "ForwardingConfigTypeDef",
    },
    total=False,
)

class TransformProcessingConfigTypeDef(
    _RequiredTransformProcessingConfigTypeDef, _OptionalTransformProcessingConfigTypeDef
):
    pass

_RequiredTransformTypeDef = TypedDict(
    "_RequiredTransformTypeDef",
    {
        "expression": str,
        "variables": List["ExpressionVariableTypeDef"],
    },
)
_OptionalTransformTypeDef = TypedDict(
    "_OptionalTransformTypeDef",
    {
        "processingConfig": "TransformProcessingConfigTypeDef",
    },
    total=False,
)

class TransformTypeDef(_RequiredTransformTypeDef, _OptionalTransformTypeDef):
    pass

_RequiredTumblingWindowTypeDef = TypedDict(
    "_RequiredTumblingWindowTypeDef",
    {
        "interval": str,
    },
)
_OptionalTumblingWindowTypeDef = TypedDict(
    "_OptionalTumblingWindowTypeDef",
    {
        "offset": str,
    },
    total=False,
)

class TumblingWindowTypeDef(_RequiredTumblingWindowTypeDef, _OptionalTumblingWindowTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
    },
)
_OptionalUpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateAccessPolicyRequestRequestTypeDef(
    _RequiredUpdateAccessPolicyRequestRequestTypeDef,
    _OptionalUpdateAccessPolicyRequestRequestTypeDef,
):
    pass

_RequiredUpdateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelCompositeModelId": str,
        "assetModelCompositeModelName": str,
    },
)
_OptionalUpdateAssetModelCompositeModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetModelCompositeModelRequestRequestTypeDef",
    {
        "assetModelCompositeModelExternalId": str,
        "assetModelCompositeModelDescription": str,
        "clientToken": str,
        "assetModelCompositeModelProperties": List["AssetModelPropertyTypeDef"],
    },
    total=False,
)

class UpdateAssetModelCompositeModelRequestRequestTypeDef(
    _RequiredUpdateAssetModelCompositeModelRequestRequestTypeDef,
    _OptionalUpdateAssetModelCompositeModelRequestRequestTypeDef,
):
    pass

UpdateAssetModelCompositeModelResponseTypeDef = TypedDict(
    "UpdateAssetModelCompositeModelResponseTypeDef",
    {
        "assetModelCompositeModelPath": List["AssetModelCompositeModelPathSegmentTypeDef"],
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssetModelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelName": str,
    },
)
_OptionalUpdateAssetModelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetModelRequestRequestTypeDef",
    {
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"],
        "clientToken": str,
        "assetModelExternalId": str,
    },
    total=False,
)

class UpdateAssetModelRequestRequestTypeDef(
    _RequiredUpdateAssetModelRequestRequestTypeDef, _OptionalUpdateAssetModelRequestRequestTypeDef
):
    pass

UpdateAssetModelResponseTypeDef = TypedDict(
    "UpdateAssetModelResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssetPropertyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)
_OptionalUpdateAssetPropertyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetPropertyRequestRequestTypeDef",
    {
        "propertyAlias": str,
        "propertyNotificationState": PropertyNotificationStateType,
        "clientToken": str,
        "propertyUnit": str,
    },
    total=False,
)

class UpdateAssetPropertyRequestRequestTypeDef(
    _RequiredUpdateAssetPropertyRequestRequestTypeDef,
    _OptionalUpdateAssetPropertyRequestRequestTypeDef,
):
    pass

_RequiredUpdateAssetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "assetName": str,
    },
)
_OptionalUpdateAssetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetRequestRequestTypeDef",
    {
        "clientToken": str,
        "assetDescription": str,
        "assetExternalId": str,
    },
    total=False,
)

class UpdateAssetRequestRequestTypeDef(
    _RequiredUpdateAssetRequestRequestTypeDef, _OptionalUpdateAssetRequestRequestTypeDef
):
    pass

UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
    },
)
_OptionalUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardRequestRequestTypeDef",
    {
        "dashboardDescription": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateDashboardRequestRequestTypeDef(
    _RequiredUpdateDashboardRequestRequestTypeDef, _OptionalUpdateDashboardRequestRequestTypeDef
):
    pass

UpdateGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
    },
)

UpdateGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayRequestRequestTypeDef = TypedDict(
    "UpdateGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
    },
)

_RequiredUpdatePortalRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePortalRequestRequestTypeDef",
    {
        "portalId": str,
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
    },
)
_OptionalUpdatePortalRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePortalRequestRequestTypeDef",
    {
        "portalDescription": str,
        "portalLogoImage": "ImageTypeDef",
        "clientToken": str,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
    },
    total=False,
)

class UpdatePortalRequestRequestTypeDef(
    _RequiredUpdatePortalRequestRequestTypeDef, _OptionalUpdatePortalRequestRequestTypeDef
):
    pass

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "projectName": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "projectDescription": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "id": str,
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "propertyId": str,
        "hierarchyId": str,
        "propertyPath": List["AssetModelPropertyPathSegmentTypeDef"],
    },
    total=False,
)

VariantTypeDef = TypedDict(
    "VariantTypeDef",
    {
        "stringValue": str,
        "integerValue": int,
        "doubleValue": float,
        "booleanValue": bool,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WarmTierRetentionPeriodTypeDef = TypedDict(
    "WarmTierRetentionPeriodTypeDef",
    {
        "numberOfDays": int,
        "unlimited": bool,
    },
    total=False,
)
