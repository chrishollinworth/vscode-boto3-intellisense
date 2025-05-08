"""
Type annotations for wisdom service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_wisdom.type_defs import AppIntegrationsConfigurationOutputTypeDef

    data: AppIntegrationsConfigurationOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AssistantStatusType,
    ContentStatusType,
    ImportJobStatusType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    OrderType,
    PriorityType,
    QuickResponseFilterOperatorType,
    QuickResponseQueryOperatorType,
    QuickResponseStatusType,
    RecommendationSourceTypeType,
    RelevanceLevelType,
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
    "AppIntegrationsConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "AssistantDataTypeDef",
    "AssistantIntegrationConfigurationTypeDef",
    "AssistantSummaryTypeDef",
    "ConfigurationTypeDef",
    "ConnectConfigurationTypeDef",
    "ContentDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "CreateAssistantAssociationRequestTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "CreateAssistantRequestTypeDef",
    "CreateAssistantResponseTypeDef",
    "CreateContentRequestTypeDef",
    "CreateContentResponseTypeDef",
    "CreateKnowledgeBaseRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "CreateQuickResponseRequestTypeDef",
    "CreateQuickResponseResponseTypeDef",
    "CreateSessionRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "DeleteAssistantAssociationRequestTypeDef",
    "DeleteAssistantRequestTypeDef",
    "DeleteContentRequestTypeDef",
    "DeleteImportJobRequestTypeDef",
    "DeleteKnowledgeBaseRequestTypeDef",
    "DeleteQuickResponseRequestTypeDef",
    "DocumentTextTypeDef",
    "DocumentTypeDef",
    "ExternalSourceConfigurationTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "GetAssistantRequestTypeDef",
    "GetAssistantResponseTypeDef",
    "GetContentRequestTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryRequestTypeDef",
    "GetContentSummaryResponseTypeDef",
    "GetImportJobRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetKnowledgeBaseRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetQuickResponseRequestTypeDef",
    "GetQuickResponseResponseTypeDef",
    "GetRecommendationsRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GroupingConfigurationOutputTypeDef",
    "GroupingConfigurationTypeDef",
    "GroupingConfigurationUnionTypeDef",
    "HighlightTypeDef",
    "ImportJobDataTypeDef",
    "ImportJobSummaryTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ListAssistantAssociationsRequestPaginateTypeDef",
    "ListAssistantAssociationsRequestTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ListAssistantsRequestPaginateTypeDef",
    "ListAssistantsRequestTypeDef",
    "ListAssistantsResponseTypeDef",
    "ListContentsRequestPaginateTypeDef",
    "ListContentsRequestTypeDef",
    "ListContentsResponseTypeDef",
    "ListImportJobsRequestPaginateTypeDef",
    "ListImportJobsRequestTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListKnowledgeBasesRequestPaginateTypeDef",
    "ListKnowledgeBasesRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListQuickResponsesRequestPaginateTypeDef",
    "ListQuickResponsesRequestTypeDef",
    "ListQuickResponsesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryAssistantRequestPaginateTypeDef",
    "QueryAssistantRequestTypeDef",
    "QueryAssistantResponseTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "QuickResponseContentProviderTypeDef",
    "QuickResponseContentsTypeDef",
    "QuickResponseDataProviderTypeDef",
    "QuickResponseDataTypeDef",
    "QuickResponseFilterFieldTypeDef",
    "QuickResponseOrderFieldTypeDef",
    "QuickResponseQueryFieldTypeDef",
    "QuickResponseSearchExpressionTypeDef",
    "QuickResponseSearchResultDataTypeDef",
    "QuickResponseSummaryTypeDef",
    "RecommendationDataTypeDef",
    "RecommendationTriggerDataTypeDef",
    "RecommendationTriggerTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultDataTypeDef",
    "SearchContentRequestPaginateTypeDef",
    "SearchContentRequestTypeDef",
    "SearchContentResponseTypeDef",
    "SearchExpressionTypeDef",
    "SearchQuickResponsesRequestPaginateTypeDef",
    "SearchQuickResponsesRequestTypeDef",
    "SearchQuickResponsesResponseTypeDef",
    "SearchSessionsRequestPaginateTypeDef",
    "SearchSessionsRequestTypeDef",
    "SearchSessionsResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionDataTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "SessionSummaryTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "SourceConfigurationUnionTypeDef",
    "StartContentUploadRequestTypeDef",
    "StartContentUploadResponseTypeDef",
    "StartImportJobRequestTypeDef",
    "StartImportJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateContentRequestTypeDef",
    "UpdateContentResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "UpdateQuickResponseRequestTypeDef",
    "UpdateQuickResponseResponseTypeDef",
)

class AppIntegrationsConfigurationOutputTypeDef(TypedDict):
    appIntegrationArn: str
    objectFields: NotRequired[List[str]]

class AppIntegrationsConfigurationTypeDef(TypedDict):
    appIntegrationArn: str
    objectFields: NotRequired[Sequence[str]]

class AssistantAssociationInputDataTypeDef(TypedDict):
    knowledgeBaseId: NotRequired[str]

class KnowledgeBaseAssociationDataTypeDef(TypedDict):
    knowledgeBaseArn: NotRequired[str]
    knowledgeBaseId: NotRequired[str]

class AssistantIntegrationConfigurationTypeDef(TypedDict):
    topicIntegrationArn: NotRequired[str]

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]

class ConnectConfigurationTypeDef(TypedDict):
    instanceId: NotRequired[str]

class ContentDataTypeDef(TypedDict):
    contentArn: str
    contentId: str
    contentType: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    metadata: Dict[str, str]
    name: str
    revisionId: str
    status: ContentStatusType
    title: str
    url: str
    urlExpiry: datetime
    linkOutUri: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ContentReferenceTypeDef(TypedDict):
    contentArn: NotRequired[str]
    contentId: NotRequired[str]
    knowledgeBaseArn: NotRequired[str]
    knowledgeBaseId: NotRequired[str]

class ContentSummaryTypeDef(TypedDict):
    contentArn: str
    contentId: str
    contentType: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    metadata: Dict[str, str]
    name: str
    revisionId: str
    status: ContentStatusType
    title: str
    tags: NotRequired[Dict[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    uploadId: str
    clientToken: NotRequired[str]
    metadata: NotRequired[Mapping[str, str]]
    overrideLinkOutUri: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    title: NotRequired[str]

class RenderingConfigurationTypeDef(TypedDict):
    templateUri: NotRequired[str]

class QuickResponseDataProviderTypeDef(TypedDict):
    content: NotRequired[str]

class CreateSessionRequestTypeDef(TypedDict):
    assistantId: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DeleteAssistantAssociationRequestTypeDef(TypedDict):
    assistantAssociationId: str
    assistantId: str

class DeleteAssistantRequestTypeDef(TypedDict):
    assistantId: str

class DeleteContentRequestTypeDef(TypedDict):
    contentId: str
    knowledgeBaseId: str

class DeleteImportJobRequestTypeDef(TypedDict):
    importJobId: str
    knowledgeBaseId: str

class DeleteKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class DeleteQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    quickResponseId: str

class HighlightTypeDef(TypedDict):
    beginOffsetInclusive: NotRequired[int]
    endOffsetExclusive: NotRequired[int]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)

class GetAssistantAssociationRequestTypeDef(TypedDict):
    assistantAssociationId: str
    assistantId: str

class GetAssistantRequestTypeDef(TypedDict):
    assistantId: str

class GetContentRequestTypeDef(TypedDict):
    contentId: str
    knowledgeBaseId: str

class GetContentSummaryRequestTypeDef(TypedDict):
    contentId: str
    knowledgeBaseId: str

class GetImportJobRequestTypeDef(TypedDict):
    importJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class GetQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    quickResponseId: str

class GetRecommendationsRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    maxResults: NotRequired[int]
    waitTimeSeconds: NotRequired[int]

class GetSessionRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str

class GroupingConfigurationOutputTypeDef(TypedDict):
    criteria: NotRequired[str]
    values: NotRequired[List[str]]

class GroupingConfigurationTypeDef(TypedDict):
    criteria: NotRequired[str]
    values: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAssistantAssociationsRequestTypeDef(TypedDict):
    assistantId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAssistantsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListContentsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListImportJobsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListKnowledgeBasesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListQuickResponsesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class QuickResponseSummaryTypeDef(TypedDict):
    contentType: str
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    channels: NotRequired[List[str]]
    description: NotRequired[str]
    isActive: NotRequired[bool]
    lastModifiedBy: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NotifyRecommendationsReceivedErrorTypeDef(TypedDict):
    message: NotRequired[str]
    recommendationId: NotRequired[str]

class NotifyRecommendationsReceivedRequestTypeDef(TypedDict):
    assistantId: str
    recommendationIds: Sequence[str]
    sessionId: str

class QueryAssistantRequestTypeDef(TypedDict):
    assistantId: str
    queryText: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class QueryRecommendationTriggerDataTypeDef(TypedDict):
    text: NotRequired[str]

class QuickResponseContentProviderTypeDef(TypedDict):
    content: NotRequired[str]

QuickResponseFilterFieldTypeDef = TypedDict(
    "QuickResponseFilterFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseFilterOperatorType,
        "includeNoExistence": NotRequired[bool],
        "values": NotRequired[Sequence[str]],
    },
)

class QuickResponseOrderFieldTypeDef(TypedDict):
    name: str
    order: NotRequired[OrderType]

QuickResponseQueryFieldTypeDef = TypedDict(
    "QuickResponseQueryFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseQueryOperatorType,
        "values": Sequence[str],
        "allowFuzziness": NotRequired[bool],
        "priority": NotRequired[PriorityType],
    },
)

class RemoveKnowledgeBaseTemplateUriRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class SessionSummaryTypeDef(TypedDict):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str

class SessionIntegrationConfigurationTypeDef(TypedDict):
    topicIntegrationArn: NotRequired[str]

class StartContentUploadRequestTypeDef(TypedDict):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: NotRequired[int]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContentRequestTypeDef(TypedDict):
    contentId: str
    knowledgeBaseId: str
    metadata: NotRequired[Mapping[str, str]]
    overrideLinkOutUri: NotRequired[str]
    removeOverrideLinkOutUri: NotRequired[bool]
    revisionId: NotRequired[str]
    title: NotRequired[str]
    uploadId: NotRequired[str]

class UpdateKnowledgeBaseTemplateUriRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    templateUri: str

class SourceConfigurationOutputTypeDef(TypedDict):
    appIntegrations: NotRequired[AppIntegrationsConfigurationOutputTypeDef]

class SourceConfigurationTypeDef(TypedDict):
    appIntegrations: NotRequired[AppIntegrationsConfigurationTypeDef]

class CreateAssistantAssociationRequestTypeDef(TypedDict):
    assistantId: str
    association: AssistantAssociationInputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class AssistantAssociationOutputDataTypeDef(TypedDict):
    knowledgeBaseAssociation: NotRequired[KnowledgeBaseAssociationDataTypeDef]

AssistantDataTypeDef = TypedDict(
    "AssistantDataTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
AssistantSummaryTypeDef = TypedDict(
    "AssistantSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateAssistantRequestTypeDef = TypedDict(
    "CreateAssistantRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class ConfigurationTypeDef(TypedDict):
    connectConfiguration: NotRequired[ConnectConfigurationTypeDef]

class CreateContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentSummaryResponseTypeDef(TypedDict):
    contentSummary: ContentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentsResponseTypeDef(TypedDict):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContentResponseTypeDef(TypedDict):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartContentUploadResponseTypeDef(TypedDict):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentTextTypeDef(TypedDict):
    highlights: NotRequired[List[HighlightTypeDef]]
    text: NotRequired[str]

class SearchExpressionTypeDef(TypedDict):
    filters: Sequence[FilterTypeDef]

GroupingConfigurationUnionTypeDef = Union[
    GroupingConfigurationTypeDef, GroupingConfigurationOutputTypeDef
]

class ListAssistantAssociationsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssistantsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContentsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportJobsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKnowledgeBasesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQuickResponsesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class QueryAssistantRequestPaginateTypeDef(TypedDict):
    assistantId: str
    queryText: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQuickResponsesResponseTypeDef(TypedDict):
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NotifyRecommendationsReceivedResponseTypeDef(TypedDict):
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTriggerDataTypeDef(TypedDict):
    query: NotRequired[QueryRecommendationTriggerDataTypeDef]

class QuickResponseContentsTypeDef(TypedDict):
    markdown: NotRequired[QuickResponseContentProviderTypeDef]
    plainText: NotRequired[QuickResponseContentProviderTypeDef]

class QuickResponseSearchExpressionTypeDef(TypedDict):
    filters: NotRequired[Sequence[QuickResponseFilterFieldTypeDef]]
    orderOnField: NotRequired[QuickResponseOrderFieldTypeDef]
    queries: NotRequired[Sequence[QuickResponseQueryFieldTypeDef]]

class SearchSessionsResponseTypeDef(TypedDict):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SessionDataTypeDef(TypedDict):
    name: str
    sessionArn: str
    sessionId: str
    description: NotRequired[str]
    integrationConfiguration: NotRequired[SessionIntegrationConfigurationTypeDef]
    tags: NotRequired[Dict[str, str]]

class KnowledgeBaseDataTypeDef(TypedDict):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: NotRequired[str]
    lastContentModificationTime: NotRequired[datetime]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    sourceConfiguration: NotRequired[SourceConfigurationOutputTypeDef]
    tags: NotRequired[Dict[str, str]]

class KnowledgeBaseSummaryTypeDef(TypedDict):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: NotRequired[str]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    sourceConfiguration: NotRequired[SourceConfigurationOutputTypeDef]
    tags: NotRequired[Dict[str, str]]

SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]

class AssistantAssociationDataTypeDef(TypedDict):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: NotRequired[Dict[str, str]]

class AssistantAssociationSummaryTypeDef(TypedDict):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: NotRequired[Dict[str, str]]

class CreateAssistantResponseTypeDef(TypedDict):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantResponseTypeDef(TypedDict):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantsResponseTypeDef(TypedDict):
    assistantSummaries: List[AssistantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ExternalSourceConfigurationTypeDef(TypedDict):
    configuration: ConfigurationTypeDef
    source: Literal["AMAZON_CONNECT"]

class DocumentTypeDef(TypedDict):
    contentReference: ContentReferenceTypeDef
    excerpt: NotRequired[DocumentTextTypeDef]
    title: NotRequired[DocumentTextTypeDef]

class SearchContentRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SearchSessionsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSessionsRequestTypeDef(TypedDict):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class CreateQuickResponseRequestTypeDef(TypedDict):
    content: QuickResponseDataProviderTypeDef
    knowledgeBaseId: str
    name: str
    channels: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]
    contentType: NotRequired[str]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]
    isActive: NotRequired[bool]
    language: NotRequired[str]
    shortcutKey: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    quickResponseId: str
    channels: NotRequired[Sequence[str]]
    content: NotRequired[QuickResponseDataProviderTypeDef]
    contentType: NotRequired[str]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]
    isActive: NotRequired[bool]
    language: NotRequired[str]
    name: NotRequired[str]
    removeDescription: NotRequired[bool]
    removeGroupingConfiguration: NotRequired[bool]
    removeShortcutKey: NotRequired[bool]
    shortcutKey: NotRequired[str]

RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "data": RecommendationTriggerDataTypeDef,
        "id": str,
        "recommendationIds": List[str],
        "source": RecommendationSourceTypeType,
        "type": Literal["QUERY"],
    },
)

class QuickResponseDataTypeDef(TypedDict):
    contentType: str
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    channels: NotRequired[List[str]]
    contents: NotRequired[QuickResponseContentsTypeDef]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    isActive: NotRequired[bool]
    language: NotRequired[str]
    lastModifiedBy: NotRequired[str]
    shortcutKey: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class QuickResponseSearchResultDataTypeDef(TypedDict):
    contentType: str
    contents: QuickResponseContentsTypeDef
    createdTime: datetime
    isActive: bool
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    attributesInterpolated: NotRequired[List[str]]
    attributesNotInterpolated: NotRequired[List[str]]
    channels: NotRequired[List[str]]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    language: NotRequired[str]
    lastModifiedBy: NotRequired[str]
    shortcutKey: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class SearchQuickResponsesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchQuickResponsesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: NotRequired[Mapping[str, str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class CreateSessionResponseTypeDef(TypedDict):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(TypedDict):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseTemplateUriResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKnowledgeBasesResponseTypeDef(TypedDict):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    sourceConfiguration: NotRequired[SourceConfigurationUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class CreateAssistantAssociationResponseTypeDef(TypedDict):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantAssociationResponseTypeDef(TypedDict):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantAssociationsResponseTypeDef(TypedDict):
    assistantAssociationSummaries: List[AssistantAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ImportJobDataTypeDef(TypedDict):
    createdTime: datetime
    importJobId: str
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    url: str
    urlExpiry: datetime
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]
    failedRecordReport: NotRequired[str]
    metadata: NotRequired[Dict[str, str]]

class ImportJobSummaryTypeDef(TypedDict):
    createdTime: datetime
    importJobId: str
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]
    metadata: NotRequired[Dict[str, str]]

class StartImportJobRequestTypeDef(TypedDict):
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseId: str
    uploadId: str
    clientToken: NotRequired[str]
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]
    metadata: NotRequired[Mapping[str, str]]

RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "document": DocumentTypeDef,
        "recommendationId": str,
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "relevanceScore": NotRequired[float],
        "type": NotRequired[Literal["KNOWLEDGE_CONTENT"]],
    },
)

class ResultDataTypeDef(TypedDict):
    document: DocumentTypeDef
    resultId: str
    relevanceScore: NotRequired[float]

class CreateQuickResponseResponseTypeDef(TypedDict):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQuickResponseResponseTypeDef(TypedDict):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQuickResponseResponseTypeDef(TypedDict):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickResponsesResponseTypeDef(TypedDict):
    results: List[QuickResponseSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetImportJobResponseTypeDef(TypedDict):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportJobResponseTypeDef(TypedDict):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportJobsResponseTypeDef(TypedDict):
    importJobSummaries: List[ImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetRecommendationsResponseTypeDef(TypedDict):
    recommendations: List[RecommendationDataTypeDef]
    triggers: List[RecommendationTriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryAssistantResponseTypeDef(TypedDict):
    results: List[ResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
