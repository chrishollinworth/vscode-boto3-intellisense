"""
Type annotations for iottwinmaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iottwinmaker.type_defs import BatchPutPropertyErrorEntryTypeDef

    data: BatchPutPropertyErrorEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ColumnTypeType,
    ComponentUpdateTypeType,
    ErrorCodeType,
    OrderByTimeType,
    OrderType,
    ParentEntityUpdateTypeType,
    PricingModeType,
    PricingTierType,
    PropertyGroupUpdateTypeType,
    PropertyUpdateTypeType,
    ScopeType,
    StateType,
    SyncJobStateType,
    SyncResourceStateType,
    SyncResourceTypeType,
    TypeType,
    UpdateReasonType,
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
    "BatchPutPropertyErrorEntryTypeDef",
    "BatchPutPropertyErrorTypeDef",
    "BatchPutPropertyValuesRequestRequestTypeDef",
    "BatchPutPropertyValuesResponseTypeDef",
    "BundleInformationTypeDef",
    "ColumnDescriptionTypeDef",
    "ComponentPropertyGroupRequestTypeDef",
    "ComponentPropertyGroupResponseTypeDef",
    "ComponentRequestTypeDef",
    "ComponentResponseTypeDef",
    "ComponentTypeSummaryTypeDef",
    "ComponentUpdateRequestTypeDef",
    "CreateComponentTypeRequestRequestTypeDef",
    "CreateComponentTypeResponseTypeDef",
    "CreateEntityRequestRequestTypeDef",
    "CreateEntityResponseTypeDef",
    "CreateSceneRequestRequestTypeDef",
    "CreateSceneResponseTypeDef",
    "CreateSyncJobRequestRequestTypeDef",
    "CreateSyncJobResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DataConnectorTypeDef",
    "DataTypeTypeDef",
    "DataValueTypeDef",
    "DeleteComponentTypeRequestRequestTypeDef",
    "DeleteComponentTypeResponseTypeDef",
    "DeleteEntityRequestRequestTypeDef",
    "DeleteEntityResponseTypeDef",
    "DeleteSceneRequestRequestTypeDef",
    "DeleteSyncJobRequestRequestTypeDef",
    "DeleteSyncJobResponseTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "EntityPropertyReferenceTypeDef",
    "EntitySummaryTypeDef",
    "ErrorDetailsTypeDef",
    "ExecuteQueryRequestRequestTypeDef",
    "ExecuteQueryResponseTypeDef",
    "FunctionRequestTypeDef",
    "FunctionResponseTypeDef",
    "GetComponentTypeRequestRequestTypeDef",
    "GetComponentTypeResponseTypeDef",
    "GetEntityRequestRequestTypeDef",
    "GetEntityResponseTypeDef",
    "GetPricingPlanResponseTypeDef",
    "GetPropertyValueHistoryRequestRequestTypeDef",
    "GetPropertyValueHistoryResponseTypeDef",
    "GetPropertyValueRequestRequestTypeDef",
    "GetPropertyValueResponseTypeDef",
    "GetSceneRequestRequestTypeDef",
    "GetSceneResponseTypeDef",
    "GetSyncJobRequestRequestTypeDef",
    "GetSyncJobResponseTypeDef",
    "GetWorkspaceRequestRequestTypeDef",
    "GetWorkspaceResponseTypeDef",
    "InterpolationParametersTypeDef",
    "LambdaFunctionTypeDef",
    "ListComponentTypesFilterTypeDef",
    "ListComponentTypesRequestRequestTypeDef",
    "ListComponentTypesResponseTypeDef",
    "ListEntitiesFilterTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListScenesRequestRequestTypeDef",
    "ListScenesResponseTypeDef",
    "ListSyncJobsRequestRequestTypeDef",
    "ListSyncJobsResponseTypeDef",
    "ListSyncResourcesRequestRequestTypeDef",
    "ListSyncResourcesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "OrderByTypeDef",
    "ParentEntityUpdateRequestTypeDef",
    "PricingPlanTypeDef",
    "PropertyDefinitionRequestTypeDef",
    "PropertyDefinitionResponseTypeDef",
    "PropertyFilterTypeDef",
    "PropertyGroupRequestTypeDef",
    "PropertyGroupResponseTypeDef",
    "PropertyLatestValueTypeDef",
    "PropertyRequestTypeDef",
    "PropertyResponseTypeDef",
    "PropertyValueEntryTypeDef",
    "PropertyValueHistoryTypeDef",
    "PropertyValueTypeDef",
    "RelationshipTypeDef",
    "RelationshipValueTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "SceneErrorTypeDef",
    "SceneSummaryTypeDef",
    "StatusTypeDef",
    "SyncJobStatusTypeDef",
    "SyncJobSummaryTypeDef",
    "SyncResourceFilterTypeDef",
    "SyncResourceStatusTypeDef",
    "SyncResourceSummaryTypeDef",
    "TabularConditionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateComponentTypeRequestRequestTypeDef",
    "UpdateComponentTypeResponseTypeDef",
    "UpdateEntityRequestRequestTypeDef",
    "UpdateEntityResponseTypeDef",
    "UpdatePricingPlanRequestRequestTypeDef",
    "UpdatePricingPlanResponseTypeDef",
    "UpdateSceneRequestRequestTypeDef",
    "UpdateSceneResponseTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "WorkspaceSummaryTypeDef",
)

BatchPutPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutPropertyErrorEntryTypeDef",
    {
        "errors": List["BatchPutPropertyErrorTypeDef"],
    },
)

BatchPutPropertyErrorTypeDef = TypedDict(
    "BatchPutPropertyErrorTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "entry": "PropertyValueEntryTypeDef",
    },
)

BatchPutPropertyValuesRequestRequestTypeDef = TypedDict(
    "BatchPutPropertyValuesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entries": List["PropertyValueEntryTypeDef"],
    },
)

BatchPutPropertyValuesResponseTypeDef = TypedDict(
    "BatchPutPropertyValuesResponseTypeDef",
    {
        "errorEntries": List["BatchPutPropertyErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBundleInformationTypeDef = TypedDict(
    "_RequiredBundleInformationTypeDef",
    {
        "bundleNames": List[str],
    },
)
_OptionalBundleInformationTypeDef = TypedDict(
    "_OptionalBundleInformationTypeDef",
    {
        "pricingTier": PricingTierType,
    },
    total=False,
)

class BundleInformationTypeDef(
    _RequiredBundleInformationTypeDef, _OptionalBundleInformationTypeDef
):
    pass

ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "name": str,
        "type": ColumnTypeType,
    },
    total=False,
)

ComponentPropertyGroupRequestTypeDef = TypedDict(
    "ComponentPropertyGroupRequestTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
        "updateType": PropertyGroupUpdateTypeType,
    },
    total=False,
)

ComponentPropertyGroupResponseTypeDef = TypedDict(
    "ComponentPropertyGroupResponseTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
        "isInherited": bool,
    },
)

ComponentRequestTypeDef = TypedDict(
    "ComponentRequestTypeDef",
    {
        "description": str,
        "componentTypeId": str,
        "properties": Dict[str, "PropertyRequestTypeDef"],
        "propertyGroups": Dict[str, "ComponentPropertyGroupRequestTypeDef"],
    },
    total=False,
)

ComponentResponseTypeDef = TypedDict(
    "ComponentResponseTypeDef",
    {
        "componentName": str,
        "description": str,
        "componentTypeId": str,
        "status": "StatusTypeDef",
        "definedIn": str,
        "properties": Dict[str, "PropertyResponseTypeDef"],
        "propertyGroups": Dict[str, "ComponentPropertyGroupResponseTypeDef"],
        "syncSource": str,
    },
    total=False,
)

_RequiredComponentTypeSummaryTypeDef = TypedDict(
    "_RequiredComponentTypeSummaryTypeDef",
    {
        "arn": str,
        "componentTypeId": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
    },
)
_OptionalComponentTypeSummaryTypeDef = TypedDict(
    "_OptionalComponentTypeSummaryTypeDef",
    {
        "description": str,
        "status": "StatusTypeDef",
        "componentTypeName": str,
    },
    total=False,
)

class ComponentTypeSummaryTypeDef(
    _RequiredComponentTypeSummaryTypeDef, _OptionalComponentTypeSummaryTypeDef
):
    pass

ComponentUpdateRequestTypeDef = TypedDict(
    "ComponentUpdateRequestTypeDef",
    {
        "updateType": ComponentUpdateTypeType,
        "description": str,
        "componentTypeId": str,
        "propertyUpdates": Dict[str, "PropertyRequestTypeDef"],
        "propertyGroupUpdates": Dict[str, "ComponentPropertyGroupRequestTypeDef"],
    },
    total=False,
)

_RequiredCreateComponentTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)
_OptionalCreateComponentTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentTypeRequestRequestTypeDef",
    {
        "isSingleton": bool,
        "description": str,
        "propertyDefinitions": Dict[str, "PropertyDefinitionRequestTypeDef"],
        "extendsFrom": List[str],
        "functions": Dict[str, "FunctionRequestTypeDef"],
        "tags": Dict[str, str],
        "propertyGroups": Dict[str, "PropertyGroupRequestTypeDef"],
        "componentTypeName": str,
    },
    total=False,
)

class CreateComponentTypeRequestRequestTypeDef(
    _RequiredCreateComponentTypeRequestRequestTypeDef,
    _OptionalCreateComponentTypeRequestRequestTypeDef,
):
    pass

CreateComponentTypeResponseTypeDef = TypedDict(
    "CreateComponentTypeResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEntityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityName": str,
    },
)
_OptionalCreateEntityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEntityRequestRequestTypeDef",
    {
        "entityId": str,
        "description": str,
        "components": Dict[str, "ComponentRequestTypeDef"],
        "parentEntityId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateEntityRequestRequestTypeDef(
    _RequiredCreateEntityRequestRequestTypeDef, _OptionalCreateEntityRequestRequestTypeDef
):
    pass

CreateEntityResponseTypeDef = TypedDict(
    "CreateEntityResponseTypeDef",
    {
        "entityId": str,
        "arn": str,
        "creationDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSceneRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
        "contentLocation": str,
    },
)
_OptionalCreateSceneRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSceneRequestRequestTypeDef",
    {
        "description": str,
        "capabilities": List[str],
        "tags": Dict[str, str],
        "sceneMetadata": Dict[str, str],
    },
    total=False,
)

class CreateSceneRequestRequestTypeDef(
    _RequiredCreateSceneRequestRequestTypeDef, _OptionalCreateSceneRequestRequestTypeDef
):
    pass

CreateSceneResponseTypeDef = TypedDict(
    "CreateSceneResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSyncJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSyncJobRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
        "syncRole": str,
    },
)
_OptionalCreateSyncJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSyncJobRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSyncJobRequestRequestTypeDef(
    _RequiredCreateSyncJobRequestRequestTypeDef, _OptionalCreateSyncJobRequestRequestTypeDef
):
    pass

CreateSyncJobResponseTypeDef = TypedDict(
    "CreateSyncJobResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "state": SyncJobStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkspaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "s3Location": str,
        "role": str,
    },
)
_OptionalCreateWorkspaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspaceRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateWorkspaceRequestRequestTypeDef(
    _RequiredCreateWorkspaceRequestRequestTypeDef, _OptionalCreateWorkspaceRequestRequestTypeDef
):
    pass

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataConnectorTypeDef = TypedDict(
    "DataConnectorTypeDef",
    {
        "lambda": "LambdaFunctionTypeDef",
        "isNative": bool,
    },
    total=False,
)

_RequiredDataTypeTypeDef = TypedDict(
    "_RequiredDataTypeTypeDef",
    {
        "type": TypeType,
    },
)
_OptionalDataTypeTypeDef = TypedDict(
    "_OptionalDataTypeTypeDef",
    {
        "nestedType": Dict[str, Any],
        "allowedValues": List["DataValueTypeDef"],
        "unitOfMeasure": str,
        "relationship": "RelationshipTypeDef",
    },
    total=False,
)

class DataTypeTypeDef(_RequiredDataTypeTypeDef, _OptionalDataTypeTypeDef):
    pass

DataValueTypeDef = TypedDict(
    "DataValueTypeDef",
    {
        "booleanValue": bool,
        "doubleValue": float,
        "integerValue": int,
        "longValue": int,
        "stringValue": str,
        "listValue": List[Dict[str, Any]],
        "mapValue": Dict[str, Dict[str, Any]],
        "relationshipValue": "RelationshipValueTypeDef",
        "expression": str,
    },
    total=False,
)

DeleteComponentTypeRequestRequestTypeDef = TypedDict(
    "DeleteComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)

DeleteComponentTypeResponseTypeDef = TypedDict(
    "DeleteComponentTypeResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteEntityRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
    },
)
_OptionalDeleteEntityRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEntityRequestRequestTypeDef",
    {
        "isRecursive": bool,
    },
    total=False,
)

class DeleteEntityRequestRequestTypeDef(
    _RequiredDeleteEntityRequestRequestTypeDef, _OptionalDeleteEntityRequestRequestTypeDef
):
    pass

DeleteEntityResponseTypeDef = TypedDict(
    "DeleteEntityResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSceneRequestRequestTypeDef = TypedDict(
    "DeleteSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
    },
)

DeleteSyncJobRequestRequestTypeDef = TypedDict(
    "DeleteSyncJobRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
    },
)

DeleteSyncJobResponseTypeDef = TypedDict(
    "DeleteSyncJobResponseTypeDef",
    {
        "state": SyncJobStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

_RequiredEntityPropertyReferenceTypeDef = TypedDict(
    "_RequiredEntityPropertyReferenceTypeDef",
    {
        "propertyName": str,
    },
)
_OptionalEntityPropertyReferenceTypeDef = TypedDict(
    "_OptionalEntityPropertyReferenceTypeDef",
    {
        "componentName": str,
        "externalIdProperty": Dict[str, str],
        "entityId": str,
    },
    total=False,
)

class EntityPropertyReferenceTypeDef(
    _RequiredEntityPropertyReferenceTypeDef, _OptionalEntityPropertyReferenceTypeDef
):
    pass

_RequiredEntitySummaryTypeDef = TypedDict(
    "_RequiredEntitySummaryTypeDef",
    {
        "entityId": str,
        "entityName": str,
        "arn": str,
        "status": "StatusTypeDef",
        "creationDateTime": datetime,
        "updateDateTime": datetime,
    },
)
_OptionalEntitySummaryTypeDef = TypedDict(
    "_OptionalEntitySummaryTypeDef",
    {
        "parentEntityId": str,
        "description": str,
        "hasChildEntities": bool,
    },
    total=False,
)

class EntitySummaryTypeDef(_RequiredEntitySummaryTypeDef, _OptionalEntitySummaryTypeDef):
    pass

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
    total=False,
)

_RequiredExecuteQueryRequestRequestTypeDef = TypedDict(
    "_RequiredExecuteQueryRequestRequestTypeDef",
    {
        "workspaceId": str,
        "queryStatement": str,
    },
)
_OptionalExecuteQueryRequestRequestTypeDef = TypedDict(
    "_OptionalExecuteQueryRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
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
        "columnDescriptions": List["ColumnDescriptionTypeDef"],
        "rows": List["RowTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionRequestTypeDef = TypedDict(
    "FunctionRequestTypeDef",
    {
        "requiredProperties": List[str],
        "scope": ScopeType,
        "implementedBy": "DataConnectorTypeDef",
    },
    total=False,
)

FunctionResponseTypeDef = TypedDict(
    "FunctionResponseTypeDef",
    {
        "requiredProperties": List[str],
        "scope": ScopeType,
        "implementedBy": "DataConnectorTypeDef",
        "isInherited": bool,
    },
    total=False,
)

GetComponentTypeRequestRequestTypeDef = TypedDict(
    "GetComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)

GetComponentTypeResponseTypeDef = TypedDict(
    "GetComponentTypeResponseTypeDef",
    {
        "workspaceId": str,
        "isSingleton": bool,
        "componentTypeId": str,
        "description": str,
        "propertyDefinitions": Dict[str, "PropertyDefinitionResponseTypeDef"],
        "extendsFrom": List[str],
        "functions": Dict[str, "FunctionResponseTypeDef"],
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "arn": str,
        "isAbstract": bool,
        "isSchemaInitialized": bool,
        "status": "StatusTypeDef",
        "propertyGroups": Dict[str, "PropertyGroupResponseTypeDef"],
        "syncSource": str,
        "componentTypeName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEntityRequestRequestTypeDef = TypedDict(
    "GetEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
    },
)

GetEntityResponseTypeDef = TypedDict(
    "GetEntityResponseTypeDef",
    {
        "entityId": str,
        "entityName": str,
        "arn": str,
        "status": "StatusTypeDef",
        "workspaceId": str,
        "description": str,
        "components": Dict[str, "ComponentResponseTypeDef"],
        "parentEntityId": str,
        "hasChildEntities": bool,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "syncSource": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPricingPlanResponseTypeDef = TypedDict(
    "GetPricingPlanResponseTypeDef",
    {
        "currentPricingPlan": "PricingPlanTypeDef",
        "pendingPricingPlan": "PricingPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetPropertyValueHistoryRequestRequestTypeDef",
    {
        "workspaceId": str,
        "selectedProperties": List[str],
    },
)
_OptionalGetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetPropertyValueHistoryRequestRequestTypeDef",
    {
        "entityId": str,
        "componentName": str,
        "componentTypeId": str,
        "propertyFilters": List["PropertyFilterTypeDef"],
        "startDateTime": Union[datetime, str],
        "endDateTime": Union[datetime, str],
        "interpolation": "InterpolationParametersTypeDef",
        "nextToken": str,
        "maxResults": int,
        "orderByTime": OrderByTimeType,
        "startTime": str,
        "endTime": str,
    },
    total=False,
)

class GetPropertyValueHistoryRequestRequestTypeDef(
    _RequiredGetPropertyValueHistoryRequestRequestTypeDef,
    _OptionalGetPropertyValueHistoryRequestRequestTypeDef,
):
    pass

GetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetPropertyValueHistoryResponseTypeDef",
    {
        "propertyValues": List["PropertyValueHistoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPropertyValueRequestRequestTypeDef = TypedDict(
    "_RequiredGetPropertyValueRequestRequestTypeDef",
    {
        "selectedProperties": List[str],
        "workspaceId": str,
    },
)
_OptionalGetPropertyValueRequestRequestTypeDef = TypedDict(
    "_OptionalGetPropertyValueRequestRequestTypeDef",
    {
        "componentName": str,
        "componentTypeId": str,
        "entityId": str,
        "maxResults": int,
        "nextToken": str,
        "propertyGroupName": str,
        "tabularConditions": "TabularConditionsTypeDef",
    },
    total=False,
)

class GetPropertyValueRequestRequestTypeDef(
    _RequiredGetPropertyValueRequestRequestTypeDef, _OptionalGetPropertyValueRequestRequestTypeDef
):
    pass

GetPropertyValueResponseTypeDef = TypedDict(
    "GetPropertyValueResponseTypeDef",
    {
        "propertyValues": Dict[str, "PropertyLatestValueTypeDef"],
        "nextToken": str,
        "tabularPropertyValues": List[List[Dict[str, "DataValueTypeDef"]]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSceneRequestRequestTypeDef = TypedDict(
    "GetSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
    },
)

GetSceneResponseTypeDef = TypedDict(
    "GetSceneResponseTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
        "contentLocation": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": str,
        "capabilities": List[str],
        "sceneMetadata": Dict[str, str],
        "generatedSceneMetadata": Dict[str, str],
        "error": "SceneErrorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSyncJobRequestRequestTypeDef = TypedDict(
    "_RequiredGetSyncJobRequestRequestTypeDef",
    {
        "syncSource": str,
    },
)
_OptionalGetSyncJobRequestRequestTypeDef = TypedDict(
    "_OptionalGetSyncJobRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
    total=False,
)

class GetSyncJobRequestRequestTypeDef(
    _RequiredGetSyncJobRequestRequestTypeDef, _OptionalGetSyncJobRequestRequestTypeDef
):
    pass

GetSyncJobResponseTypeDef = TypedDict(
    "GetSyncJobResponseTypeDef",
    {
        "arn": str,
        "workspaceId": str,
        "syncSource": str,
        "syncRole": str,
        "status": "SyncJobStatusTypeDef",
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkspaceRequestRequestTypeDef = TypedDict(
    "GetWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

GetWorkspaceResponseTypeDef = TypedDict(
    "GetWorkspaceResponseTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "description": str,
        "s3Location": str,
        "role": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterpolationParametersTypeDef = TypedDict(
    "InterpolationParametersTypeDef",
    {
        "interpolationType": Literal["LINEAR"],
        "intervalInSeconds": int,
    },
    total=False,
)

LambdaFunctionTypeDef = TypedDict(
    "LambdaFunctionTypeDef",
    {
        "arn": str,
    },
)

ListComponentTypesFilterTypeDef = TypedDict(
    "ListComponentTypesFilterTypeDef",
    {
        "extendsFrom": str,
        "namespace": str,
        "isAbstract": bool,
    },
    total=False,
)

_RequiredListComponentTypesRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentTypesRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListComponentTypesRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentTypesRequestRequestTypeDef",
    {
        "filters": List["ListComponentTypesFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListComponentTypesRequestRequestTypeDef(
    _RequiredListComponentTypesRequestRequestTypeDef,
    _OptionalListComponentTypesRequestRequestTypeDef,
):
    pass

ListComponentTypesResponseTypeDef = TypedDict(
    "ListComponentTypesResponseTypeDef",
    {
        "workspaceId": str,
        "componentTypeSummaries": List["ComponentTypeSummaryTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesFilterTypeDef = TypedDict(
    "ListEntitiesFilterTypeDef",
    {
        "parentEntityId": str,
        "componentTypeId": str,
        "externalId": str,
    },
    total=False,
)

_RequiredListEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitiesRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitiesRequestRequestTypeDef",
    {
        "filters": List["ListEntitiesFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEntitiesRequestRequestTypeDef(
    _RequiredListEntitiesRequestRequestTypeDef, _OptionalListEntitiesRequestRequestTypeDef
):
    pass

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "entitySummaries": List["EntitySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListScenesRequestRequestTypeDef = TypedDict(
    "_RequiredListScenesRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListScenesRequestRequestTypeDef = TypedDict(
    "_OptionalListScenesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListScenesRequestRequestTypeDef(
    _RequiredListScenesRequestRequestTypeDef, _OptionalListScenesRequestRequestTypeDef
):
    pass

ListScenesResponseTypeDef = TypedDict(
    "ListScenesResponseTypeDef",
    {
        "sceneSummaries": List["SceneSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSyncJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListSyncJobsRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListSyncJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListSyncJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSyncJobsRequestRequestTypeDef(
    _RequiredListSyncJobsRequestRequestTypeDef, _OptionalListSyncJobsRequestRequestTypeDef
):
    pass

ListSyncJobsResponseTypeDef = TypedDict(
    "ListSyncJobsResponseTypeDef",
    {
        "syncJobSummaries": List["SyncJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSyncResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListSyncResourcesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "syncSource": str,
    },
)
_OptionalListSyncResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListSyncResourcesRequestRequestTypeDef",
    {
        "filters": List["SyncResourceFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSyncResourcesRequestRequestTypeDef(
    _RequiredListSyncResourcesRequestRequestTypeDef, _OptionalListSyncResourcesRequestRequestTypeDef
):
    pass

ListSyncResourcesResponseTypeDef = TypedDict(
    "ListSyncResourcesResponseTypeDef",
    {
        "syncResources": List["SyncResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "workspaceSummaries": List["WorkspaceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOrderByTypeDef = TypedDict(
    "_RequiredOrderByTypeDef",
    {
        "propertyName": str,
    },
)
_OptionalOrderByTypeDef = TypedDict(
    "_OptionalOrderByTypeDef",
    {
        "order": OrderType,
    },
    total=False,
)

class OrderByTypeDef(_RequiredOrderByTypeDef, _OptionalOrderByTypeDef):
    pass

_RequiredParentEntityUpdateRequestTypeDef = TypedDict(
    "_RequiredParentEntityUpdateRequestTypeDef",
    {
        "updateType": ParentEntityUpdateTypeType,
    },
)
_OptionalParentEntityUpdateRequestTypeDef = TypedDict(
    "_OptionalParentEntityUpdateRequestTypeDef",
    {
        "parentEntityId": str,
    },
    total=False,
)

class ParentEntityUpdateRequestTypeDef(
    _RequiredParentEntityUpdateRequestTypeDef, _OptionalParentEntityUpdateRequestTypeDef
):
    pass

_RequiredPricingPlanTypeDef = TypedDict(
    "_RequiredPricingPlanTypeDef",
    {
        "effectiveDateTime": datetime,
        "pricingMode": PricingModeType,
        "updateDateTime": datetime,
        "updateReason": UpdateReasonType,
    },
)
_OptionalPricingPlanTypeDef = TypedDict(
    "_OptionalPricingPlanTypeDef",
    {
        "billableEntityCount": int,
        "bundleInformation": "BundleInformationTypeDef",
    },
    total=False,
)

class PricingPlanTypeDef(_RequiredPricingPlanTypeDef, _OptionalPricingPlanTypeDef):
    pass

PropertyDefinitionRequestTypeDef = TypedDict(
    "PropertyDefinitionRequestTypeDef",
    {
        "dataType": "DataTypeTypeDef",
        "isRequiredInEntity": bool,
        "isExternalId": bool,
        "isStoredExternally": bool,
        "isTimeSeries": bool,
        "defaultValue": "DataValueTypeDef",
        "configuration": Dict[str, str],
        "displayName": str,
    },
    total=False,
)

_RequiredPropertyDefinitionResponseTypeDef = TypedDict(
    "_RequiredPropertyDefinitionResponseTypeDef",
    {
        "dataType": "DataTypeTypeDef",
        "isTimeSeries": bool,
        "isRequiredInEntity": bool,
        "isExternalId": bool,
        "isStoredExternally": bool,
        "isImported": bool,
        "isFinal": bool,
        "isInherited": bool,
    },
)
_OptionalPropertyDefinitionResponseTypeDef = TypedDict(
    "_OptionalPropertyDefinitionResponseTypeDef",
    {
        "defaultValue": "DataValueTypeDef",
        "configuration": Dict[str, str],
        "displayName": str,
    },
    total=False,
)

class PropertyDefinitionResponseTypeDef(
    _RequiredPropertyDefinitionResponseTypeDef, _OptionalPropertyDefinitionResponseTypeDef
):
    pass

PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "propertyName": str,
        "operator": str,
        "value": "DataValueTypeDef",
    },
    total=False,
)

PropertyGroupRequestTypeDef = TypedDict(
    "PropertyGroupRequestTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
    },
    total=False,
)

PropertyGroupResponseTypeDef = TypedDict(
    "PropertyGroupResponseTypeDef",
    {
        "groupType": Literal["TABULAR"],
        "propertyNames": List[str],
        "isInherited": bool,
    },
)

_RequiredPropertyLatestValueTypeDef = TypedDict(
    "_RequiredPropertyLatestValueTypeDef",
    {
        "propertyReference": "EntityPropertyReferenceTypeDef",
    },
)
_OptionalPropertyLatestValueTypeDef = TypedDict(
    "_OptionalPropertyLatestValueTypeDef",
    {
        "propertyValue": "DataValueTypeDef",
    },
    total=False,
)

class PropertyLatestValueTypeDef(
    _RequiredPropertyLatestValueTypeDef, _OptionalPropertyLatestValueTypeDef
):
    pass

PropertyRequestTypeDef = TypedDict(
    "PropertyRequestTypeDef",
    {
        "definition": "PropertyDefinitionRequestTypeDef",
        "value": "DataValueTypeDef",
        "updateType": PropertyUpdateTypeType,
    },
    total=False,
)

PropertyResponseTypeDef = TypedDict(
    "PropertyResponseTypeDef",
    {
        "definition": "PropertyDefinitionResponseTypeDef",
        "value": "DataValueTypeDef",
    },
    total=False,
)

_RequiredPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPropertyValueEntryTypeDef",
    {
        "entityPropertyReference": "EntityPropertyReferenceTypeDef",
    },
)
_OptionalPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPropertyValueEntryTypeDef",
    {
        "propertyValues": List["PropertyValueTypeDef"],
    },
    total=False,
)

class PropertyValueEntryTypeDef(
    _RequiredPropertyValueEntryTypeDef, _OptionalPropertyValueEntryTypeDef
):
    pass

_RequiredPropertyValueHistoryTypeDef = TypedDict(
    "_RequiredPropertyValueHistoryTypeDef",
    {
        "entityPropertyReference": "EntityPropertyReferenceTypeDef",
    },
)
_OptionalPropertyValueHistoryTypeDef = TypedDict(
    "_OptionalPropertyValueHistoryTypeDef",
    {
        "values": List["PropertyValueTypeDef"],
    },
    total=False,
)

class PropertyValueHistoryTypeDef(
    _RequiredPropertyValueHistoryTypeDef, _OptionalPropertyValueHistoryTypeDef
):
    pass

_RequiredPropertyValueTypeDef = TypedDict(
    "_RequiredPropertyValueTypeDef",
    {
        "value": "DataValueTypeDef",
    },
)
_OptionalPropertyValueTypeDef = TypedDict(
    "_OptionalPropertyValueTypeDef",
    {
        "timestamp": Union[datetime, str],
        "time": str,
    },
    total=False,
)

class PropertyValueTypeDef(_RequiredPropertyValueTypeDef, _OptionalPropertyValueTypeDef):
    pass

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "targetComponentTypeId": str,
        "relationshipType": str,
    },
    total=False,
)

RelationshipValueTypeDef = TypedDict(
    "RelationshipValueTypeDef",
    {
        "targetEntityId": str,
        "targetComponentName": str,
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

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "rowData": List[Dict[str, Any]],
    },
    total=False,
)

SceneErrorTypeDef = TypedDict(
    "SceneErrorTypeDef",
    {
        "code": Literal["MATTERPORT_ERROR"],
        "message": str,
    },
    total=False,
)

_RequiredSceneSummaryTypeDef = TypedDict(
    "_RequiredSceneSummaryTypeDef",
    {
        "sceneId": str,
        "contentLocation": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
    },
)
_OptionalSceneSummaryTypeDef = TypedDict(
    "_OptionalSceneSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class SceneSummaryTypeDef(_RequiredSceneSummaryTypeDef, _OptionalSceneSummaryTypeDef):
    pass

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "state": StateType,
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)

SyncJobStatusTypeDef = TypedDict(
    "SyncJobStatusTypeDef",
    {
        "state": SyncJobStateType,
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)

SyncJobSummaryTypeDef = TypedDict(
    "SyncJobSummaryTypeDef",
    {
        "arn": str,
        "workspaceId": str,
        "syncSource": str,
        "status": "SyncJobStatusTypeDef",
        "creationDateTime": datetime,
        "updateDateTime": datetime,
    },
    total=False,
)

SyncResourceFilterTypeDef = TypedDict(
    "SyncResourceFilterTypeDef",
    {
        "state": SyncResourceStateType,
        "resourceType": SyncResourceTypeType,
        "resourceId": str,
        "externalId": str,
    },
    total=False,
)

SyncResourceStatusTypeDef = TypedDict(
    "SyncResourceStatusTypeDef",
    {
        "state": SyncResourceStateType,
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)

SyncResourceSummaryTypeDef = TypedDict(
    "SyncResourceSummaryTypeDef",
    {
        "resourceType": SyncResourceTypeType,
        "externalId": str,
        "resourceId": str,
        "status": "SyncResourceStatusTypeDef",
        "updateDateTime": datetime,
    },
    total=False,
)

TabularConditionsTypeDef = TypedDict(
    "TabularConditionsTypeDef",
    {
        "orderBy": List["OrderByTypeDef"],
        "propertyFilters": List["PropertyFilterTypeDef"],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateComponentTypeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentTypeRequestRequestTypeDef",
    {
        "workspaceId": str,
        "componentTypeId": str,
    },
)
_OptionalUpdateComponentTypeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentTypeRequestRequestTypeDef",
    {
        "isSingleton": bool,
        "description": str,
        "propertyDefinitions": Dict[str, "PropertyDefinitionRequestTypeDef"],
        "extendsFrom": List[str],
        "functions": Dict[str, "FunctionRequestTypeDef"],
        "propertyGroups": Dict[str, "PropertyGroupRequestTypeDef"],
        "componentTypeName": str,
    },
    total=False,
)

class UpdateComponentTypeRequestRequestTypeDef(
    _RequiredUpdateComponentTypeRequestRequestTypeDef,
    _OptionalUpdateComponentTypeRequestRequestTypeDef,
):
    pass

UpdateComponentTypeResponseTypeDef = TypedDict(
    "UpdateComponentTypeResponseTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "componentTypeId": str,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEntityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEntityRequestRequestTypeDef",
    {
        "workspaceId": str,
        "entityId": str,
    },
)
_OptionalUpdateEntityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEntityRequestRequestTypeDef",
    {
        "entityName": str,
        "description": str,
        "componentUpdates": Dict[str, "ComponentUpdateRequestTypeDef"],
        "parentEntityUpdate": "ParentEntityUpdateRequestTypeDef",
    },
    total=False,
)

class UpdateEntityRequestRequestTypeDef(
    _RequiredUpdateEntityRequestRequestTypeDef, _OptionalUpdateEntityRequestRequestTypeDef
):
    pass

UpdateEntityResponseTypeDef = TypedDict(
    "UpdateEntityResponseTypeDef",
    {
        "updateDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePricingPlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePricingPlanRequestRequestTypeDef",
    {
        "pricingMode": PricingModeType,
    },
)
_OptionalUpdatePricingPlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePricingPlanRequestRequestTypeDef",
    {
        "bundleNames": List[str],
    },
    total=False,
)

class UpdatePricingPlanRequestRequestTypeDef(
    _RequiredUpdatePricingPlanRequestRequestTypeDef, _OptionalUpdatePricingPlanRequestRequestTypeDef
):
    pass

UpdatePricingPlanResponseTypeDef = TypedDict(
    "UpdatePricingPlanResponseTypeDef",
    {
        "currentPricingPlan": "PricingPlanTypeDef",
        "pendingPricingPlan": "PricingPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSceneRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSceneRequestRequestTypeDef",
    {
        "workspaceId": str,
        "sceneId": str,
    },
)
_OptionalUpdateSceneRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSceneRequestRequestTypeDef",
    {
        "contentLocation": str,
        "description": str,
        "capabilities": List[str],
        "sceneMetadata": Dict[str, str],
    },
    total=False,
)

class UpdateSceneRequestRequestTypeDef(
    _RequiredUpdateSceneRequestRequestTypeDef, _OptionalUpdateSceneRequestRequestTypeDef
):
    pass

UpdateSceneResponseTypeDef = TypedDict(
    "UpdateSceneResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceRequestRequestTypeDef",
    {
        "description": str,
        "role": str,
    },
    total=False,
)

class UpdateWorkspaceRequestRequestTypeDef(
    _RequiredUpdateWorkspaceRequestRequestTypeDef, _OptionalUpdateWorkspaceRequestRequestTypeDef
):
    pass

UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWorkspaceSummaryTypeDef = TypedDict(
    "_RequiredWorkspaceSummaryTypeDef",
    {
        "workspaceId": str,
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
    },
)
_OptionalWorkspaceSummaryTypeDef = TypedDict(
    "_OptionalWorkspaceSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, _OptionalWorkspaceSummaryTypeDef):
    pass
