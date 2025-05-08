"""
Type annotations for iotthingsgraph service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import AssociateEntityToThingRequestTypeDef

    data: AssociateEntityToThingRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DeploymentTargetType,
    EntityFilterNameType,
    EntityTypeType,
    FlowExecutionEventTypeType,
    FlowExecutionStatusType,
    NamespaceDeletionStatusType,
    SystemInstanceDeploymentStatusType,
    SystemInstanceFilterNameType,
    UploadStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateEntityToThingRequestTypeDef",
    "CreateFlowTemplateRequestTypeDef",
    "CreateFlowTemplateResponseTypeDef",
    "CreateSystemInstanceRequestTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "CreateSystemTemplateRequestTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "DefinitionDocumentTypeDef",
    "DeleteFlowTemplateRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteSystemInstanceRequestTypeDef",
    "DeleteSystemTemplateRequestTypeDef",
    "DependencyRevisionTypeDef",
    "DeploySystemInstanceRequestTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "DeprecateFlowTemplateRequestTypeDef",
    "DeprecateSystemTemplateRequestTypeDef",
    "DescribeNamespaceRequestTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DissociateEntityFromThingRequestTypeDef",
    "EntityDescriptionTypeDef",
    "EntityFilterTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateFilterTypeDef",
    "FlowTemplateSummaryTypeDef",
    "GetEntitiesRequestTypeDef",
    "GetEntitiesResponseTypeDef",
    "GetFlowTemplateRequestTypeDef",
    "GetFlowTemplateResponseTypeDef",
    "GetFlowTemplateRevisionsRequestPaginateTypeDef",
    "GetFlowTemplateRevisionsRequestTypeDef",
    "GetFlowTemplateRevisionsResponseTypeDef",
    "GetNamespaceDeletionStatusResponseTypeDef",
    "GetSystemInstanceRequestTypeDef",
    "GetSystemInstanceResponseTypeDef",
    "GetSystemTemplateRequestTypeDef",
    "GetSystemTemplateResponseTypeDef",
    "GetSystemTemplateRevisionsRequestPaginateTypeDef",
    "GetSystemTemplateRevisionsRequestTypeDef",
    "GetSystemTemplateRevisionsResponseTypeDef",
    "GetUploadStatusRequestTypeDef",
    "GetUploadStatusResponseTypeDef",
    "ListFlowExecutionMessagesRequestPaginateTypeDef",
    "ListFlowExecutionMessagesRequestTypeDef",
    "ListFlowExecutionMessagesResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SearchEntitiesRequestPaginateTypeDef",
    "SearchEntitiesRequestTypeDef",
    "SearchEntitiesResponseTypeDef",
    "SearchFlowExecutionsRequestPaginateTypeDef",
    "SearchFlowExecutionsRequestTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesRequestPaginateTypeDef",
    "SearchFlowTemplatesRequestTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "SearchSystemInstancesRequestPaginateTypeDef",
    "SearchSystemInstancesRequestTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "SearchSystemTemplatesRequestPaginateTypeDef",
    "SearchSystemTemplatesRequestTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SearchThingsRequestPaginateTypeDef",
    "SearchThingsRequestTypeDef",
    "SearchThingsResponseTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateFilterTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "TimestampTypeDef",
    "UndeploySystemInstanceRequestTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFlowTemplateRequestTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UpdateSystemTemplateRequestTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "UploadEntityDefinitionsRequestTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
)

class AssociateEntityToThingRequestTypeDef(TypedDict):
    thingName: str
    entityId: str
    namespaceVersion: NotRequired[int]

class DefinitionDocumentTypeDef(TypedDict):
    language: Literal["GRAPHQL"]
    text: str

FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MetricsConfigurationTypeDef(TypedDict):
    cloudMetricEnabled: NotRequired[bool]
    metricRuleRoleArn: NotRequired[str]

class TagTypeDef(TypedDict):
    key: str
    value: str

SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[SystemInstanceDeploymentStatusType],
        "target": NotRequired[DeploymentTargetType],
        "greengrassGroupName": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "greengrassGroupId": NotRequired[str],
        "greengrassGroupVersionId": NotRequired[str],
    },
)
SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
    },
)
DeleteFlowTemplateRequestTypeDef = TypedDict(
    "DeleteFlowTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DeleteSystemInstanceRequestTypeDef = TypedDict(
    "DeleteSystemInstanceRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)
DeleteSystemTemplateRequestTypeDef = TypedDict(
    "DeleteSystemTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef",
    {
        "id": NotRequired[str],
        "revisionNumber": NotRequired[int],
    },
)
DeploySystemInstanceRequestTypeDef = TypedDict(
    "DeploySystemInstanceRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)
DeprecateFlowTemplateRequestTypeDef = TypedDict(
    "DeprecateFlowTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DeprecateSystemTemplateRequestTypeDef = TypedDict(
    "DeprecateSystemTemplateRequestTypeDef",
    {
        "id": str,
    },
)

class DescribeNamespaceRequestTypeDef(TypedDict):
    namespaceName: NotRequired[str]

class DissociateEntityFromThingRequestTypeDef(TypedDict):
    thingName: str
    entityType: EntityTypeType

class EntityFilterTypeDef(TypedDict):
    name: NotRequired[EntityFilterNameType]
    value: NotRequired[Sequence[str]]

class FlowExecutionMessageTypeDef(TypedDict):
    messageId: NotRequired[str]
    eventType: NotRequired[FlowExecutionEventTypeType]
    timestamp: NotRequired[datetime]
    payload: NotRequired[str]

class FlowExecutionSummaryTypeDef(TypedDict):
    flowExecutionId: NotRequired[str]
    status: NotRequired[FlowExecutionStatusType]
    systemInstanceId: NotRequired[str]
    flowTemplateId: NotRequired[str]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]

class FlowTemplateFilterTypeDef(TypedDict):
    name: Literal["DEVICE_MODEL_ID"]
    value: Sequence[str]

class GetEntitiesRequestTypeDef(TypedDict):
    ids: Sequence[str]
    namespaceVersion: NotRequired[int]

GetFlowTemplateRequestTypeDef = TypedDict(
    "GetFlowTemplateRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

GetFlowTemplateRevisionsRequestTypeDef = TypedDict(
    "GetFlowTemplateRevisionsRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetSystemInstanceRequestTypeDef = TypedDict(
    "GetSystemInstanceRequestTypeDef",
    {
        "id": str,
    },
)
GetSystemTemplateRequestTypeDef = TypedDict(
    "GetSystemTemplateRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
    },
)
GetSystemTemplateRevisionsRequestTypeDef = TypedDict(
    "GetSystemTemplateRevisionsRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class GetUploadStatusRequestTypeDef(TypedDict):
    uploadId: str

class ListFlowExecutionMessagesRequestTypeDef(TypedDict):
    flowExecutionId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class SystemInstanceFilterTypeDef(TypedDict):
    name: NotRequired[SystemInstanceFilterNameType]
    value: NotRequired[Sequence[str]]

class SystemTemplateFilterTypeDef(TypedDict):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: Sequence[str]

class SearchThingsRequestTypeDef(TypedDict):
    entityId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    namespaceVersion: NotRequired[int]

class ThingTypeDef(TypedDict):
    thingArn: NotRequired[str]
    thingName: NotRequired[str]

UndeploySystemInstanceRequestTypeDef = TypedDict(
    "UndeploySystemInstanceRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateFlowTemplateRequestTypeDef(TypedDict):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: NotRequired[int]

class CreateSystemTemplateRequestTypeDef(TypedDict):
    definition: DefinitionDocumentTypeDef
    compatibleNamespaceVersion: NotRequired[int]

EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "type": NotRequired[EntityTypeType],
        "createdAt": NotRequired[datetime],
        "definition": NotRequired[DefinitionDocumentTypeDef],
    },
)
UpdateFlowTemplateRequestTypeDef = TypedDict(
    "UpdateFlowTemplateRequestTypeDef",
    {
        "id": str,
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)
UpdateSystemTemplateRequestTypeDef = TypedDict(
    "UpdateSystemTemplateRequestTypeDef",
    {
        "id": str,
        "definition": DefinitionDocumentTypeDef,
        "compatibleNamespaceVersion": NotRequired[int],
    },
)

class UploadEntityDefinitionsRequestTypeDef(TypedDict):
    document: NotRequired[DefinitionDocumentTypeDef]
    syncWithPublicNamespace: NotRequired[bool]
    deprecateExistingEntities: NotRequired[bool]

class FlowTemplateDescriptionTypeDef(TypedDict):
    summary: NotRequired[FlowTemplateSummaryTypeDef]
    definition: NotRequired[DefinitionDocumentTypeDef]
    validatedNamespaceVersion: NotRequired[int]

class CreateFlowTemplateResponseTypeDef(TypedDict):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(TypedDict):
    namespaceArn: str
    namespaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNamespaceResponseTypeDef(TypedDict):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowTemplateRevisionsResponseTypeDef(TypedDict):
    summaries: List[FlowTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetNamespaceDeletionStatusResponseTypeDef(TypedDict):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatusType
    errorCode: Literal["VALIDATION_FAILED"]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadStatusResponseTypeDef(TypedDict):
    uploadId: str
    uploadStatus: UploadStatusType
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]
    createdDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFlowTemplatesResponseTypeDef(TypedDict):
    summaries: List[FlowTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateFlowTemplateResponseTypeDef(TypedDict):
    summary: FlowTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UploadEntityDefinitionsResponseTypeDef(TypedDict):
    uploadId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemInstanceRequestTypeDef(TypedDict):
    definition: DefinitionDocumentTypeDef
    target: DeploymentTargetType
    tags: NotRequired[Sequence[TagTypeDef]]
    greengrassGroupName: NotRequired[str]
    s3BucketName: NotRequired[str]
    metricsConfiguration: NotRequired[MetricsConfigurationTypeDef]
    flowActionsRoleArn: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateSystemInstanceResponseTypeDef(TypedDict):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploySystemInstanceResponseTypeDef(TypedDict):
    summary: SystemInstanceSummaryTypeDef
    greengrassDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchSystemInstancesResponseTypeDef(TypedDict):
    summaries: List[SystemInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UndeploySystemInstanceResponseTypeDef(TypedDict):
    summary: SystemInstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSystemTemplateResponseTypeDef(TypedDict):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateRevisionsResponseTypeDef(TypedDict):
    summaries: List[SystemTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchSystemTemplatesResponseTypeDef(TypedDict):
    summaries: List[SystemTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SystemTemplateDescriptionTypeDef(TypedDict):
    summary: NotRequired[SystemTemplateSummaryTypeDef]
    definition: NotRequired[DefinitionDocumentTypeDef]
    validatedNamespaceVersion: NotRequired[int]

class UpdateSystemTemplateResponseTypeDef(TypedDict):
    summary: SystemTemplateSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SystemInstanceDescriptionTypeDef(TypedDict):
    summary: NotRequired[SystemInstanceSummaryTypeDef]
    definition: NotRequired[DefinitionDocumentTypeDef]
    s3BucketName: NotRequired[str]
    metricsConfiguration: NotRequired[MetricsConfigurationTypeDef]
    validatedNamespaceVersion: NotRequired[int]
    validatedDependencyRevisions: NotRequired[List[DependencyRevisionTypeDef]]
    flowActionsRoleArn: NotRequired[str]

class SearchEntitiesRequestTypeDef(TypedDict):
    entityTypes: Sequence[EntityTypeType]
    filters: NotRequired[Sequence[EntityFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    namespaceVersion: NotRequired[int]

class ListFlowExecutionMessagesResponseTypeDef(TypedDict):
    messages: List[FlowExecutionMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchFlowExecutionsResponseTypeDef(TypedDict):
    summaries: List[FlowExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchFlowTemplatesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[FlowTemplateFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

GetFlowTemplateRevisionsRequestPaginateTypeDef = TypedDict(
    "GetFlowTemplateRevisionsRequestPaginateTypeDef",
    {
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSystemTemplateRevisionsRequestPaginateTypeDef = TypedDict(
    "GetSystemTemplateRevisionsRequestPaginateTypeDef",
    {
        "id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListFlowExecutionMessagesRequestPaginateTypeDef(TypedDict):
    flowExecutionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchEntitiesRequestPaginateTypeDef(TypedDict):
    entityTypes: Sequence[EntityTypeType]
    filters: NotRequired[Sequence[EntityFilterTypeDef]]
    namespaceVersion: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchFlowTemplatesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FlowTemplateFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchThingsRequestPaginateTypeDef(TypedDict):
    entityId: str
    namespaceVersion: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchFlowExecutionsRequestPaginateTypeDef(TypedDict):
    systemInstanceId: str
    flowExecutionId: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchFlowExecutionsRequestTypeDef(TypedDict):
    systemInstanceId: str
    flowExecutionId: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    endTime: NotRequired[TimestampTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SearchSystemInstancesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[SystemInstanceFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSystemInstancesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[SystemInstanceFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SearchSystemTemplatesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[SystemTemplateFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSystemTemplatesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[SystemTemplateFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SearchThingsResponseTypeDef(TypedDict):
    things: List[ThingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEntitiesResponseTypeDef(TypedDict):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchEntitiesResponseTypeDef(TypedDict):
    descriptions: List[EntityDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetFlowTemplateResponseTypeDef(TypedDict):
    description: FlowTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemTemplateResponseTypeDef(TypedDict):
    description: SystemTemplateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSystemInstanceResponseTypeDef(TypedDict):
    description: SystemInstanceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
