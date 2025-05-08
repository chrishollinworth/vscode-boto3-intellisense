"""
Type annotations for iottwinmaker service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iottwinmaker.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ColumnTypeType,
    ComponentUpdateTypeType,
    DestinationTypeType,
    ErrorCodeType,
    MetadataTransferJobStateType,
    OrderByTimeType,
    OrderType,
    ParentEntityUpdateTypeType,
    PricingModeType,
    PricingTierType,
    PropertyGroupUpdateTypeType,
    PropertyUpdateTypeType,
    ScopeType,
    SourceTypeType,
    StateType,
    SyncJobStateType,
    SyncResourceStateType,
    SyncResourceTypeType,
    TypeType,
    UpdateReasonType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BatchPutPropertyErrorEntryTypeDef",
    "BatchPutPropertyErrorTypeDef",
    "BatchPutPropertyValuesRequestTypeDef",
    "BatchPutPropertyValuesResponseTypeDef",
    "BundleInformationTypeDef",
    "CancelMetadataTransferJobRequestTypeDef",
    "CancelMetadataTransferJobResponseTypeDef",
    "ColumnDescriptionTypeDef",
    "ComponentPropertyGroupRequestTypeDef",
    "ComponentPropertyGroupResponseTypeDef",
    "ComponentRequestTypeDef",
    "ComponentResponseTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeSummaryTypeDef",
    "ComponentUpdateRequestTypeDef",
    "CompositeComponentRequestTypeDef",
    "CompositeComponentTypeRequestTypeDef",
    "CompositeComponentTypeResponseTypeDef",
    "CompositeComponentUpdateRequestTypeDef",
    "CreateComponentTypeRequestTypeDef",
    "CreateComponentTypeResponseTypeDef",
    "CreateEntityRequestTypeDef",
    "CreateEntityResponseTypeDef",
    "CreateMetadataTransferJobRequestTypeDef",
    "CreateMetadataTransferJobResponseTypeDef",
    "CreateSceneRequestTypeDef",
    "CreateSceneResponseTypeDef",
    "CreateSyncJobRequestTypeDef",
    "CreateSyncJobResponseTypeDef",
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DataConnectorTypeDef",
    "DataTypeOutputTypeDef",
    "DataTypeTypeDef",
    "DataTypeUnionTypeDef",
    "DataValueOutputTypeDef",
    "DataValueTypeDef",
    "DataValueUnionTypeDef",
    "DeleteComponentTypeRequestTypeDef",
    "DeleteComponentTypeResponseTypeDef",
    "DeleteEntityRequestTypeDef",
    "DeleteEntityResponseTypeDef",
    "DeleteSceneRequestTypeDef",
    "DeleteSyncJobRequestTypeDef",
    "DeleteSyncJobResponseTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "EntityPropertyReferenceOutputTypeDef",
    "EntityPropertyReferenceTypeDef",
    "EntityPropertyReferenceUnionTypeDef",
    "EntitySummaryTypeDef",
    "ErrorDetailsTypeDef",
    "ExecuteQueryRequestTypeDef",
    "ExecuteQueryResponseTypeDef",
    "FilterByAssetModelTypeDef",
    "FilterByAssetTypeDef",
    "FilterByComponentTypeTypeDef",
    "FilterByEntityTypeDef",
    "FunctionRequestTypeDef",
    "FunctionResponseTypeDef",
    "GetComponentTypeRequestTypeDef",
    "GetComponentTypeResponseTypeDef",
    "GetEntityRequestTypeDef",
    "GetEntityResponseTypeDef",
    "GetMetadataTransferJobRequestTypeDef",
    "GetMetadataTransferJobResponseTypeDef",
    "GetPricingPlanResponseTypeDef",
    "GetPropertyValueHistoryRequestTypeDef",
    "GetPropertyValueHistoryResponseTypeDef",
    "GetPropertyValueRequestTypeDef",
    "GetPropertyValueResponseTypeDef",
    "GetSceneRequestTypeDef",
    "GetSceneResponseTypeDef",
    "GetSyncJobRequestTypeDef",
    "GetSyncJobResponseTypeDef",
    "GetWorkspaceRequestTypeDef",
    "GetWorkspaceResponseTypeDef",
    "InterpolationParametersTypeDef",
    "IotSiteWiseSourceConfigurationFilterTypeDef",
    "IotSiteWiseSourceConfigurationOutputTypeDef",
    "IotSiteWiseSourceConfigurationTypeDef",
    "IotSiteWiseSourceConfigurationUnionTypeDef",
    "IotTwinMakerDestinationConfigurationTypeDef",
    "IotTwinMakerSourceConfigurationFilterTypeDef",
    "IotTwinMakerSourceConfigurationOutputTypeDef",
    "IotTwinMakerSourceConfigurationTypeDef",
    "IotTwinMakerSourceConfigurationUnionTypeDef",
    "LambdaFunctionTypeDef",
    "ListComponentTypesFilterTypeDef",
    "ListComponentTypesRequestTypeDef",
    "ListComponentTypesResponseTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListEntitiesFilterTypeDef",
    "ListEntitiesRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListMetadataTransferJobsFilterTypeDef",
    "ListMetadataTransferJobsRequestTypeDef",
    "ListMetadataTransferJobsResponseTypeDef",
    "ListPropertiesRequestTypeDef",
    "ListPropertiesResponseTypeDef",
    "ListScenesRequestTypeDef",
    "ListScenesResponseTypeDef",
    "ListSyncJobsRequestTypeDef",
    "ListSyncJobsResponseTypeDef",
    "ListSyncResourcesRequestTypeDef",
    "ListSyncResourcesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "MetadataTransferJobProgressTypeDef",
    "MetadataTransferJobStatusTypeDef",
    "MetadataTransferJobSummaryTypeDef",
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
    "PropertySummaryTypeDef",
    "PropertyValueEntryOutputTypeDef",
    "PropertyValueEntryTypeDef",
    "PropertyValueEntryUnionTypeDef",
    "PropertyValueHistoryTypeDef",
    "PropertyValueOutputTypeDef",
    "PropertyValueTypeDef",
    "PropertyValueUnionTypeDef",
    "RelationshipTypeDef",
    "RelationshipValueTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3SourceConfigurationTypeDef",
    "SceneErrorTypeDef",
    "SceneSummaryTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "SourceConfigurationUnionTypeDef",
    "StatusTypeDef",
    "SyncJobStatusTypeDef",
    "SyncJobSummaryTypeDef",
    "SyncResourceFilterTypeDef",
    "SyncResourceStatusTypeDef",
    "SyncResourceSummaryTypeDef",
    "TabularConditionsTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateComponentTypeRequestTypeDef",
    "UpdateComponentTypeResponseTypeDef",
    "UpdateEntityRequestTypeDef",
    "UpdateEntityResponseTypeDef",
    "UpdatePricingPlanRequestTypeDef",
    "UpdatePricingPlanResponseTypeDef",
    "UpdateSceneRequestTypeDef",
    "UpdateSceneResponseTypeDef",
    "UpdateWorkspaceRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "WorkspaceSummaryTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BundleInformationTypeDef(TypedDict):
    bundleNames: List[str]
    pricingTier: NotRequired[PricingTierType]

class CancelMetadataTransferJobRequestTypeDef(TypedDict):
    metadataTransferJobId: str

class MetadataTransferJobProgressTypeDef(TypedDict):
    totalCount: NotRequired[int]
    succeededCount: NotRequired[int]
    skippedCount: NotRequired[int]
    failedCount: NotRequired[int]

ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[ColumnTypeType],
    },
)

class ComponentPropertyGroupRequestTypeDef(TypedDict):
    groupType: NotRequired[Literal["TABULAR"]]
    propertyNames: NotRequired[Sequence[str]]
    updateType: NotRequired[PropertyGroupUpdateTypeType]

class ComponentPropertyGroupResponseTypeDef(TypedDict):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class CompositeComponentTypeRequestTypeDef(TypedDict):
    componentTypeId: NotRequired[str]

class CompositeComponentTypeResponseTypeDef(TypedDict):
    componentTypeId: NotRequired[str]
    isInherited: NotRequired[bool]

class PropertyGroupRequestTypeDef(TypedDict):
    groupType: NotRequired[Literal["TABULAR"]]
    propertyNames: NotRequired[Sequence[str]]

class CreateSceneRequestTypeDef(TypedDict):
    workspaceId: str
    sceneId: str
    contentLocation: str
    description: NotRequired[str]
    capabilities: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]
    sceneMetadata: NotRequired[Mapping[str, str]]

class CreateSyncJobRequestTypeDef(TypedDict):
    workspaceId: str
    syncSource: str
    syncRole: str
    tags: NotRequired[Mapping[str, str]]

class CreateWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str
    description: NotRequired[str]
    s3Location: NotRequired[str]
    role: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class LambdaFunctionTypeDef(TypedDict):
    arn: str

class RelationshipTypeDef(TypedDict):
    targetComponentTypeId: NotRequired[str]
    relationshipType: NotRequired[str]

class RelationshipValueTypeDef(TypedDict):
    targetEntityId: NotRequired[str]
    targetComponentName: NotRequired[str]

class DeleteComponentTypeRequestTypeDef(TypedDict):
    workspaceId: str
    componentTypeId: str

class DeleteEntityRequestTypeDef(TypedDict):
    workspaceId: str
    entityId: str
    isRecursive: NotRequired[bool]

class DeleteSceneRequestTypeDef(TypedDict):
    workspaceId: str
    sceneId: str

class DeleteSyncJobRequestTypeDef(TypedDict):
    workspaceId: str
    syncSource: str

class DeleteWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str

class IotTwinMakerDestinationConfigurationTypeDef(TypedDict):
    workspace: str

class S3DestinationConfigurationTypeDef(TypedDict):
    location: str

class EntityPropertyReferenceOutputTypeDef(TypedDict):
    propertyName: str
    componentName: NotRequired[str]
    componentPath: NotRequired[str]
    externalIdProperty: NotRequired[Dict[str, str]]
    entityId: NotRequired[str]

class EntityPropertyReferenceTypeDef(TypedDict):
    propertyName: str
    componentName: NotRequired[str]
    componentPath: NotRequired[str]
    externalIdProperty: NotRequired[Mapping[str, str]]
    entityId: NotRequired[str]

class ErrorDetailsTypeDef(TypedDict):
    code: NotRequired[ErrorCodeType]
    message: NotRequired[str]

class ExecuteQueryRequestTypeDef(TypedDict):
    workspaceId: str
    queryStatement: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class RowTypeDef(TypedDict):
    rowData: NotRequired[List[Dict[str, Any]]]

class FilterByAssetModelTypeDef(TypedDict):
    assetModelId: NotRequired[str]
    assetModelExternalId: NotRequired[str]
    includeOffspring: NotRequired[bool]
    includeAssets: NotRequired[bool]

class FilterByAssetTypeDef(TypedDict):
    assetId: NotRequired[str]
    assetExternalId: NotRequired[str]
    includeOffspring: NotRequired[bool]
    includeAssetModel: NotRequired[bool]

class FilterByComponentTypeTypeDef(TypedDict):
    componentTypeId: str

class FilterByEntityTypeDef(TypedDict):
    entityId: str

class GetComponentTypeRequestTypeDef(TypedDict):
    workspaceId: str
    componentTypeId: str

class PropertyGroupResponseTypeDef(TypedDict):
    groupType: Literal["TABULAR"]
    propertyNames: List[str]
    isInherited: bool

class GetEntityRequestTypeDef(TypedDict):
    workspaceId: str
    entityId: str

class GetMetadataTransferJobRequestTypeDef(TypedDict):
    metadataTransferJobId: str

class InterpolationParametersTypeDef(TypedDict):
    interpolationType: NotRequired[Literal["LINEAR"]]
    intervalInSeconds: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class GetSceneRequestTypeDef(TypedDict):
    workspaceId: str
    sceneId: str

class SceneErrorTypeDef(TypedDict):
    code: NotRequired[Literal["MATTERPORT_ERROR"]]
    message: NotRequired[str]

class GetSyncJobRequestTypeDef(TypedDict):
    syncSource: str
    workspaceId: NotRequired[str]

class GetWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str

class ListComponentTypesFilterTypeDef(TypedDict):
    extendsFrom: NotRequired[str]
    namespace: NotRequired[str]
    isAbstract: NotRequired[bool]

class ListComponentsRequestTypeDef(TypedDict):
    workspaceId: str
    entityId: str
    componentPath: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEntitiesFilterTypeDef(TypedDict):
    parentEntityId: NotRequired[str]
    componentTypeId: NotRequired[str]
    externalId: NotRequired[str]

class ListMetadataTransferJobsFilterTypeDef(TypedDict):
    workspaceId: NotRequired[str]
    state: NotRequired[MetadataTransferJobStateType]

class ListPropertiesRequestTypeDef(TypedDict):
    workspaceId: str
    entityId: str
    componentName: NotRequired[str]
    componentPath: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListScenesRequestTypeDef(TypedDict):
    workspaceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SceneSummaryTypeDef(TypedDict):
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: NotRequired[str]

class ListSyncJobsRequestTypeDef(TypedDict):
    workspaceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SyncResourceFilterTypeDef(TypedDict):
    state: NotRequired[SyncResourceStateType]
    resourceType: NotRequired[SyncResourceTypeType]
    resourceId: NotRequired[str]
    externalId: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceARN: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListWorkspacesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class WorkspaceSummaryTypeDef(TypedDict):
    workspaceId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: NotRequired[str]
    linkedServices: NotRequired[List[str]]

class OrderByTypeDef(TypedDict):
    propertyName: str
    order: NotRequired[OrderType]

class ParentEntityUpdateRequestTypeDef(TypedDict):
    updateType: ParentEntityUpdateTypeType
    parentEntityId: NotRequired[str]

class S3SourceConfigurationTypeDef(TypedDict):
    location: str

class TagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdatePricingPlanRequestTypeDef(TypedDict):
    pricingMode: PricingModeType
    bundleNames: NotRequired[Sequence[str]]

class UpdateSceneRequestTypeDef(TypedDict):
    workspaceId: str
    sceneId: str
    contentLocation: NotRequired[str]
    description: NotRequired[str]
    capabilities: NotRequired[Sequence[str]]
    sceneMetadata: NotRequired[Mapping[str, str]]

class UpdateWorkspaceRequestTypeDef(TypedDict):
    workspaceId: str
    description: NotRequired[str]
    role: NotRequired[str]
    s3Location: NotRequired[str]

class CreateComponentTypeResponseTypeDef(TypedDict):
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityResponseTypeDef(TypedDict):
    entityId: str
    arn: str
    creationDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSceneResponseTypeDef(TypedDict):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncJobResponseTypeDef(TypedDict):
    arn: str
    creationDateTime: datetime
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(TypedDict):
    arn: str
    creationDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentTypeResponseTypeDef(TypedDict):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEntityResponseTypeDef(TypedDict):
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSyncJobResponseTypeDef(TypedDict):
    state: SyncJobStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkspaceResponseTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkspaceResponseTypeDef(TypedDict):
    workspaceId: str
    arn: str
    description: str
    linkedServices: List[str]
    s3Location: str
    role: str
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateComponentTypeResponseTypeDef(TypedDict):
    workspaceId: str
    arn: str
    componentTypeId: str
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEntityResponseTypeDef(TypedDict):
    updateDateTime: datetime
    state: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSceneResponseTypeDef(TypedDict):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkspaceResponseTypeDef(TypedDict):
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PricingPlanTypeDef(TypedDict):
    effectiveDateTime: datetime
    pricingMode: PricingModeType
    updateDateTime: datetime
    updateReason: UpdateReasonType
    billableEntityCount: NotRequired[int]
    bundleInformation: NotRequired[BundleInformationTypeDef]

DataConnectorTypeDef = TypedDict(
    "DataConnectorTypeDef",
    {
        "lambda": NotRequired[LambdaFunctionTypeDef],
        "isNative": NotRequired[bool],
    },
)

class DataValueOutputTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    integerValue: NotRequired[int]
    longValue: NotRequired[int]
    stringValue: NotRequired[str]
    listValue: NotRequired[List[Dict[str, Any]]]
    mapValue: NotRequired[Dict[str, Dict[str, Any]]]
    relationshipValue: NotRequired[RelationshipValueTypeDef]
    expression: NotRequired[str]

class DataValueTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    integerValue: NotRequired[int]
    longValue: NotRequired[int]
    stringValue: NotRequired[str]
    listValue: NotRequired[Sequence[Mapping[str, Any]]]
    mapValue: NotRequired[Mapping[str, Mapping[str, Any]]]
    relationshipValue: NotRequired[RelationshipValueTypeDef]
    expression: NotRequired[str]

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "type": DestinationTypeType,
        "s3Configuration": NotRequired[S3DestinationConfigurationTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerDestinationConfigurationTypeDef],
    },
)
EntityPropertyReferenceUnionTypeDef = Union[
    EntityPropertyReferenceTypeDef, EntityPropertyReferenceOutputTypeDef
]

class MetadataTransferJobStatusTypeDef(TypedDict):
    state: NotRequired[MetadataTransferJobStateType]
    error: NotRequired[ErrorDetailsTypeDef]
    queuedPosition: NotRequired[int]

class StatusTypeDef(TypedDict):
    state: NotRequired[StateType]
    error: NotRequired[ErrorDetailsTypeDef]

class SyncJobStatusTypeDef(TypedDict):
    state: NotRequired[SyncJobStateType]
    error: NotRequired[ErrorDetailsTypeDef]

class SyncResourceStatusTypeDef(TypedDict):
    state: NotRequired[SyncResourceStateType]
    error: NotRequired[ErrorDetailsTypeDef]

class ExecuteQueryResponseTypeDef(TypedDict):
    columnDescriptions: List[ColumnDescriptionTypeDef]
    rows: List[RowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IotSiteWiseSourceConfigurationFilterTypeDef(TypedDict):
    filterByAssetModel: NotRequired[FilterByAssetModelTypeDef]
    filterByAsset: NotRequired[FilterByAssetTypeDef]

class IotTwinMakerSourceConfigurationFilterTypeDef(TypedDict):
    filterByComponentType: NotRequired[FilterByComponentTypeTypeDef]
    filterByEntity: NotRequired[FilterByEntityTypeDef]

class GetSceneResponseTypeDef(TypedDict):
    workspaceId: str
    sceneId: str
    contentLocation: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: str
    capabilities: List[str]
    sceneMetadata: Dict[str, str]
    generatedSceneMetadata: Dict[str, str]
    error: SceneErrorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentTypesRequestTypeDef(TypedDict):
    workspaceId: str
    filters: NotRequired[Sequence[ListComponentTypesFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListEntitiesRequestTypeDef(TypedDict):
    workspaceId: str
    filters: NotRequired[Sequence[ListEntitiesFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListMetadataTransferJobsRequestTypeDef(TypedDict):
    sourceType: SourceTypeType
    destinationType: DestinationTypeType
    filters: NotRequired[Sequence[ListMetadataTransferJobsFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListScenesResponseTypeDef(TypedDict):
    sceneSummaries: List[SceneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSyncResourcesRequestTypeDef(TypedDict):
    workspaceId: str
    syncSource: str
    filters: NotRequired[Sequence[SyncResourceFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListWorkspacesResponseTypeDef(TypedDict):
    workspaceSummaries: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetPricingPlanResponseTypeDef(TypedDict):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePricingPlanResponseTypeDef(TypedDict):
    currentPricingPlan: PricingPlanTypeDef
    pendingPricingPlan: PricingPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionRequestTypeDef(TypedDict):
    requiredProperties: NotRequired[Sequence[str]]
    scope: NotRequired[ScopeType]
    implementedBy: NotRequired[DataConnectorTypeDef]

class FunctionResponseTypeDef(TypedDict):
    requiredProperties: NotRequired[List[str]]
    scope: NotRequired[ScopeType]
    implementedBy: NotRequired[DataConnectorTypeDef]
    isInherited: NotRequired[bool]

DataTypeOutputTypeDef = TypedDict(
    "DataTypeOutputTypeDef",
    {
        "type": TypeType,
        "nestedType": NotRequired[Dict[str, Any]],
        "allowedValues": NotRequired[List[DataValueOutputTypeDef]],
        "unitOfMeasure": NotRequired[str],
        "relationship": NotRequired[RelationshipTypeDef],
    },
)

class PropertyLatestValueTypeDef(TypedDict):
    propertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValue: NotRequired[DataValueOutputTypeDef]

class PropertyValueOutputTypeDef(TypedDict):
    value: DataValueOutputTypeDef
    timestamp: NotRequired[datetime]
    time: NotRequired[str]

DataValueUnionTypeDef = Union[DataValueTypeDef, DataValueOutputTypeDef]

class CancelMetadataTransferJobResponseTypeDef(TypedDict):
    metadataTransferJobId: str
    arn: str
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: MetadataTransferJobProgressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetadataTransferJobResponseTypeDef(TypedDict):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MetadataTransferJobSummaryTypeDef(TypedDict):
    metadataTransferJobId: str
    arn: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: NotRequired[MetadataTransferJobProgressTypeDef]

class ComponentSummaryTypeDef(TypedDict):
    componentName: str
    componentTypeId: str
    status: StatusTypeDef
    definedIn: NotRequired[str]
    description: NotRequired[str]
    propertyGroups: NotRequired[Dict[str, ComponentPropertyGroupResponseTypeDef]]
    syncSource: NotRequired[str]
    componentPath: NotRequired[str]

class ComponentTypeSummaryTypeDef(TypedDict):
    arn: str
    componentTypeId: str
    creationDateTime: datetime
    updateDateTime: datetime
    description: NotRequired[str]
    status: NotRequired[StatusTypeDef]
    componentTypeName: NotRequired[str]

class EntitySummaryTypeDef(TypedDict):
    entityId: str
    entityName: str
    arn: str
    status: StatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    parentEntityId: NotRequired[str]
    description: NotRequired[str]
    hasChildEntities: NotRequired[bool]

class GetSyncJobResponseTypeDef(TypedDict):
    arn: str
    workspaceId: str
    syncSource: str
    syncRole: str
    status: SyncJobStatusTypeDef
    creationDateTime: datetime
    updateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SyncJobSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    workspaceId: NotRequired[str]
    syncSource: NotRequired[str]
    status: NotRequired[SyncJobStatusTypeDef]
    creationDateTime: NotRequired[datetime]
    updateDateTime: NotRequired[datetime]

class SyncResourceSummaryTypeDef(TypedDict):
    resourceType: NotRequired[SyncResourceTypeType]
    externalId: NotRequired[str]
    resourceId: NotRequired[str]
    status: NotRequired[SyncResourceStatusTypeDef]
    updateDateTime: NotRequired[datetime]

class IotSiteWiseSourceConfigurationOutputTypeDef(TypedDict):
    filters: NotRequired[List[IotSiteWiseSourceConfigurationFilterTypeDef]]

class IotSiteWiseSourceConfigurationTypeDef(TypedDict):
    filters: NotRequired[Sequence[IotSiteWiseSourceConfigurationFilterTypeDef]]

class IotTwinMakerSourceConfigurationOutputTypeDef(TypedDict):
    workspace: str
    filters: NotRequired[List[IotTwinMakerSourceConfigurationFilterTypeDef]]

class IotTwinMakerSourceConfigurationTypeDef(TypedDict):
    workspace: str
    filters: NotRequired[Sequence[IotTwinMakerSourceConfigurationFilterTypeDef]]

class PropertyDefinitionResponseTypeDef(TypedDict):
    dataType: DataTypeOutputTypeDef
    isTimeSeries: bool
    isRequiredInEntity: bool
    isExternalId: bool
    isStoredExternally: bool
    isImported: bool
    isFinal: bool
    isInherited: bool
    defaultValue: NotRequired[DataValueOutputTypeDef]
    configuration: NotRequired[Dict[str, str]]
    displayName: NotRequired[str]

class GetPropertyValueResponseTypeDef(TypedDict):
    propertyValues: Dict[str, PropertyLatestValueTypeDef]
    tabularPropertyValues: List[List[Dict[str, DataValueOutputTypeDef]]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PropertyValueEntryOutputTypeDef(TypedDict):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    propertyValues: NotRequired[List[PropertyValueOutputTypeDef]]

class PropertyValueHistoryTypeDef(TypedDict):
    entityPropertyReference: EntityPropertyReferenceOutputTypeDef
    values: NotRequired[List[PropertyValueOutputTypeDef]]

DataTypeTypeDef = TypedDict(
    "DataTypeTypeDef",
    {
        "type": TypeType,
        "nestedType": NotRequired[Mapping[str, Any]],
        "allowedValues": NotRequired[Sequence[DataValueUnionTypeDef]],
        "unitOfMeasure": NotRequired[str],
        "relationship": NotRequired[RelationshipTypeDef],
    },
)
PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "propertyName": NotRequired[str],
        "operator": NotRequired[str],
        "value": NotRequired[DataValueUnionTypeDef],
    },
)

class PropertyValueTypeDef(TypedDict):
    value: DataValueUnionTypeDef
    timestamp: NotRequired[TimestampTypeDef]
    time: NotRequired[str]

class ListMetadataTransferJobsResponseTypeDef(TypedDict):
    metadataTransferJobSummaries: List[MetadataTransferJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListComponentsResponseTypeDef(TypedDict):
    componentSummaries: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListComponentTypesResponseTypeDef(TypedDict):
    workspaceId: str
    componentTypeSummaries: List[ComponentTypeSummaryTypeDef]
    maxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEntitiesResponseTypeDef(TypedDict):
    entitySummaries: List[EntitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSyncJobsResponseTypeDef(TypedDict):
    syncJobSummaries: List[SyncJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSyncResourcesResponseTypeDef(TypedDict):
    syncResources: List[SyncResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

IotSiteWiseSourceConfigurationUnionTypeDef = Union[
    IotSiteWiseSourceConfigurationTypeDef, IotSiteWiseSourceConfigurationOutputTypeDef
]
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "type": SourceTypeType,
        "s3Configuration": NotRequired[S3SourceConfigurationTypeDef],
        "iotSiteWiseConfiguration": NotRequired[IotSiteWiseSourceConfigurationOutputTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerSourceConfigurationOutputTypeDef],
    },
)
IotTwinMakerSourceConfigurationUnionTypeDef = Union[
    IotTwinMakerSourceConfigurationTypeDef, IotTwinMakerSourceConfigurationOutputTypeDef
]

class GetComponentTypeResponseTypeDef(TypedDict):
    workspaceId: str
    isSingleton: bool
    componentTypeId: str
    description: str
    propertyDefinitions: Dict[str, PropertyDefinitionResponseTypeDef]
    extendsFrom: List[str]
    functions: Dict[str, FunctionResponseTypeDef]
    creationDateTime: datetime
    updateDateTime: datetime
    arn: str
    isAbstract: bool
    isSchemaInitialized: bool
    status: StatusTypeDef
    propertyGroups: Dict[str, PropertyGroupResponseTypeDef]
    syncSource: str
    componentTypeName: str
    compositeComponentTypes: Dict[str, CompositeComponentTypeResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PropertyResponseTypeDef(TypedDict):
    definition: NotRequired[PropertyDefinitionResponseTypeDef]
    value: NotRequired[DataValueOutputTypeDef]
    areAllPropertyValuesReturned: NotRequired[bool]

class PropertySummaryTypeDef(TypedDict):
    propertyName: str
    definition: NotRequired[PropertyDefinitionResponseTypeDef]
    value: NotRequired[DataValueOutputTypeDef]
    areAllPropertyValuesReturned: NotRequired[bool]

class BatchPutPropertyErrorTypeDef(TypedDict):
    errorCode: str
    errorMessage: str
    entry: PropertyValueEntryOutputTypeDef

class GetPropertyValueHistoryResponseTypeDef(TypedDict):
    propertyValues: List[PropertyValueHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DataTypeUnionTypeDef = Union[DataTypeTypeDef, DataTypeOutputTypeDef]

class GetPropertyValueHistoryRequestTypeDef(TypedDict):
    workspaceId: str
    selectedProperties: Sequence[str]
    entityId: NotRequired[str]
    componentName: NotRequired[str]
    componentPath: NotRequired[str]
    componentTypeId: NotRequired[str]
    propertyFilters: NotRequired[Sequence[PropertyFilterTypeDef]]
    startDateTime: NotRequired[TimestampTypeDef]
    endDateTime: NotRequired[TimestampTypeDef]
    interpolation: NotRequired[InterpolationParametersTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    orderByTime: NotRequired[OrderByTimeType]
    startTime: NotRequired[str]
    endTime: NotRequired[str]

class TabularConditionsTypeDef(TypedDict):
    orderBy: NotRequired[Sequence[OrderByTypeDef]]
    propertyFilters: NotRequired[Sequence[PropertyFilterTypeDef]]

PropertyValueUnionTypeDef = Union[PropertyValueTypeDef, PropertyValueOutputTypeDef]

class GetMetadataTransferJobResponseTypeDef(TypedDict):
    metadataTransferJobId: str
    arn: str
    description: str
    sources: List[SourceConfigurationOutputTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobRole: str
    reportUrl: str
    creationDateTime: datetime
    updateDateTime: datetime
    status: MetadataTransferJobStatusTypeDef
    progress: MetadataTransferJobProgressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "type": SourceTypeType,
        "s3Configuration": NotRequired[S3SourceConfigurationTypeDef],
        "iotSiteWiseConfiguration": NotRequired[IotSiteWiseSourceConfigurationUnionTypeDef],
        "iotTwinMakerConfiguration": NotRequired[IotTwinMakerSourceConfigurationUnionTypeDef],
    },
)

class ComponentResponseTypeDef(TypedDict):
    componentName: NotRequired[str]
    description: NotRequired[str]
    componentTypeId: NotRequired[str]
    status: NotRequired[StatusTypeDef]
    definedIn: NotRequired[str]
    properties: NotRequired[Dict[str, PropertyResponseTypeDef]]
    propertyGroups: NotRequired[Dict[str, ComponentPropertyGroupResponseTypeDef]]
    syncSource: NotRequired[str]
    areAllPropertiesReturned: NotRequired[bool]
    compositeComponents: NotRequired[Dict[str, ComponentSummaryTypeDef]]
    areAllCompositeComponentsReturned: NotRequired[bool]

class ListPropertiesResponseTypeDef(TypedDict):
    propertySummaries: List[PropertySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchPutPropertyErrorEntryTypeDef(TypedDict):
    errors: List[BatchPutPropertyErrorTypeDef]

class PropertyDefinitionRequestTypeDef(TypedDict):
    dataType: NotRequired[DataTypeUnionTypeDef]
    isRequiredInEntity: NotRequired[bool]
    isExternalId: NotRequired[bool]
    isStoredExternally: NotRequired[bool]
    isTimeSeries: NotRequired[bool]
    defaultValue: NotRequired[DataValueUnionTypeDef]
    configuration: NotRequired[Mapping[str, str]]
    displayName: NotRequired[str]

class GetPropertyValueRequestTypeDef(TypedDict):
    selectedProperties: Sequence[str]
    workspaceId: str
    componentName: NotRequired[str]
    componentPath: NotRequired[str]
    componentTypeId: NotRequired[str]
    entityId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    propertyGroupName: NotRequired[str]
    tabularConditions: NotRequired[TabularConditionsTypeDef]

class PropertyValueEntryTypeDef(TypedDict):
    entityPropertyReference: EntityPropertyReferenceUnionTypeDef
    propertyValues: NotRequired[Sequence[PropertyValueUnionTypeDef]]

SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]

class GetEntityResponseTypeDef(TypedDict):
    entityId: str
    entityName: str
    arn: str
    status: StatusTypeDef
    workspaceId: str
    description: str
    components: Dict[str, ComponentResponseTypeDef]
    parentEntityId: str
    hasChildEntities: bool
    creationDateTime: datetime
    updateDateTime: datetime
    syncSource: str
    areAllComponentsReturned: bool
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutPropertyValuesResponseTypeDef(TypedDict):
    errorEntries: List[BatchPutPropertyErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentTypeRequestTypeDef(TypedDict):
    workspaceId: str
    componentTypeId: str
    isSingleton: NotRequired[bool]
    description: NotRequired[str]
    propertyDefinitions: NotRequired[Mapping[str, PropertyDefinitionRequestTypeDef]]
    extendsFrom: NotRequired[Sequence[str]]
    functions: NotRequired[Mapping[str, FunctionRequestTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    propertyGroups: NotRequired[Mapping[str, PropertyGroupRequestTypeDef]]
    componentTypeName: NotRequired[str]
    compositeComponentTypes: NotRequired[Mapping[str, CompositeComponentTypeRequestTypeDef]]

class PropertyRequestTypeDef(TypedDict):
    definition: NotRequired[PropertyDefinitionRequestTypeDef]
    value: NotRequired[DataValueUnionTypeDef]
    updateType: NotRequired[PropertyUpdateTypeType]

class UpdateComponentTypeRequestTypeDef(TypedDict):
    workspaceId: str
    componentTypeId: str
    isSingleton: NotRequired[bool]
    description: NotRequired[str]
    propertyDefinitions: NotRequired[Mapping[str, PropertyDefinitionRequestTypeDef]]
    extendsFrom: NotRequired[Sequence[str]]
    functions: NotRequired[Mapping[str, FunctionRequestTypeDef]]
    propertyGroups: NotRequired[Mapping[str, PropertyGroupRequestTypeDef]]
    componentTypeName: NotRequired[str]
    compositeComponentTypes: NotRequired[Mapping[str, CompositeComponentTypeRequestTypeDef]]

PropertyValueEntryUnionTypeDef = Union[PropertyValueEntryTypeDef, PropertyValueEntryOutputTypeDef]

class CreateMetadataTransferJobRequestTypeDef(TypedDict):
    sources: Sequence[SourceConfigurationUnionTypeDef]
    destination: DestinationConfigurationTypeDef
    metadataTransferJobId: NotRequired[str]
    description: NotRequired[str]

class ComponentRequestTypeDef(TypedDict):
    description: NotRequired[str]
    componentTypeId: NotRequired[str]
    properties: NotRequired[Mapping[str, PropertyRequestTypeDef]]
    propertyGroups: NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]]

class ComponentUpdateRequestTypeDef(TypedDict):
    updateType: NotRequired[ComponentUpdateTypeType]
    description: NotRequired[str]
    componentTypeId: NotRequired[str]
    propertyUpdates: NotRequired[Mapping[str, PropertyRequestTypeDef]]
    propertyGroupUpdates: NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]]

class CompositeComponentRequestTypeDef(TypedDict):
    description: NotRequired[str]
    properties: NotRequired[Mapping[str, PropertyRequestTypeDef]]
    propertyGroups: NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]]

class CompositeComponentUpdateRequestTypeDef(TypedDict):
    updateType: NotRequired[ComponentUpdateTypeType]
    description: NotRequired[str]
    propertyUpdates: NotRequired[Mapping[str, PropertyRequestTypeDef]]
    propertyGroupUpdates: NotRequired[Mapping[str, ComponentPropertyGroupRequestTypeDef]]

class BatchPutPropertyValuesRequestTypeDef(TypedDict):
    workspaceId: str
    entries: Sequence[PropertyValueEntryUnionTypeDef]

class CreateEntityRequestTypeDef(TypedDict):
    workspaceId: str
    entityName: str
    entityId: NotRequired[str]
    description: NotRequired[str]
    components: NotRequired[Mapping[str, ComponentRequestTypeDef]]
    compositeComponents: NotRequired[Mapping[str, CompositeComponentRequestTypeDef]]
    parentEntityId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateEntityRequestTypeDef(TypedDict):
    workspaceId: str
    entityId: str
    entityName: NotRequired[str]
    description: NotRequired[str]
    componentUpdates: NotRequired[Mapping[str, ComponentUpdateRequestTypeDef]]
    compositeComponentUpdates: NotRequired[Mapping[str, CompositeComponentUpdateRequestTypeDef]]
    parentEntityUpdate: NotRequired[ParentEntityUpdateRequestTypeDef]
