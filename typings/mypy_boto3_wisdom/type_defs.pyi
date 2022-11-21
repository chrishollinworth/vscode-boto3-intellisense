"""
Type annotations for wisdom service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wisdom.type_defs import AppIntegrationsConfigurationTypeDef

    data: AppIntegrationsConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AssistantStatusType,
    ContentStatusType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    RecommendationSourceTypeType,
    RelevanceLevelType,
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
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "AssistantDataTypeDef",
    "AssistantSummaryTypeDef",
    "ContentDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "CreateAssistantAssociationRequestRequestTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "CreateAssistantRequestRequestTypeDef",
    "CreateAssistantResponseTypeDef",
    "CreateContentRequestRequestTypeDef",
    "CreateContentResponseTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DocumentTextTypeDef",
    "DocumentTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetAssistantResponseTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetContentSummaryResponseTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "HighlightTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListAssistantsResponseTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListContentsResponseTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryAssistantRequestRequestTypeDef",
    "QueryAssistantResponseTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "RecommendationDataTypeDef",
    "RecommendationTriggerDataTypeDef",
    "RecommendationTriggerTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultDataTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentResponseTypeDef",
    "SearchExpressionTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionDataTypeDef",
    "SessionSummaryTypeDef",
    "SourceConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "StartContentUploadResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateContentResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
)

AppIntegrationsConfigurationTypeDef = TypedDict(
    "AppIntegrationsConfigurationTypeDef",
    {
        "appIntegrationArn": str,
        "objectFields": List[str],
    },
)

_RequiredAssistantAssociationDataTypeDef = TypedDict(
    "_RequiredAssistantAssociationDataTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": "AssistantAssociationOutputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
    },
)
_OptionalAssistantAssociationDataTypeDef = TypedDict(
    "_OptionalAssistantAssociationDataTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantAssociationDataTypeDef(
    _RequiredAssistantAssociationDataTypeDef, _OptionalAssistantAssociationDataTypeDef
):
    pass

AssistantAssociationInputDataTypeDef = TypedDict(
    "AssistantAssociationInputDataTypeDef",
    {
        "knowledgeBaseId": str,
    },
    total=False,
)

AssistantAssociationOutputDataTypeDef = TypedDict(
    "AssistantAssociationOutputDataTypeDef",
    {
        "knowledgeBaseAssociation": "KnowledgeBaseAssociationDataTypeDef",
    },
    total=False,
)

_RequiredAssistantAssociationSummaryTypeDef = TypedDict(
    "_RequiredAssistantAssociationSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": "AssistantAssociationOutputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
    },
)
_OptionalAssistantAssociationSummaryTypeDef = TypedDict(
    "_OptionalAssistantAssociationSummaryTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantAssociationSummaryTypeDef(
    _RequiredAssistantAssociationSummaryTypeDef, _OptionalAssistantAssociationSummaryTypeDef
):
    pass

_RequiredAssistantDataTypeDef = TypedDict(
    "_RequiredAssistantDataTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
    },
)
_OptionalAssistantDataTypeDef = TypedDict(
    "_OptionalAssistantDataTypeDef",
    {
        "description": str,
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantDataTypeDef(_RequiredAssistantDataTypeDef, _OptionalAssistantDataTypeDef):
    pass

_RequiredAssistantSummaryTypeDef = TypedDict(
    "_RequiredAssistantSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
    },
)
_OptionalAssistantSummaryTypeDef = TypedDict(
    "_OptionalAssistantSummaryTypeDef",
    {
        "description": str,
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantSummaryTypeDef(_RequiredAssistantSummaryTypeDef, _OptionalAssistantSummaryTypeDef):
    pass

_RequiredContentDataTypeDef = TypedDict(
    "_RequiredContentDataTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
        "url": str,
        "urlExpiry": datetime,
    },
)
_OptionalContentDataTypeDef = TypedDict(
    "_OptionalContentDataTypeDef",
    {
        "linkOutUri": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ContentDataTypeDef(_RequiredContentDataTypeDef, _OptionalContentDataTypeDef):
    pass

ContentReferenceTypeDef = TypedDict(
    "ContentReferenceTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
    },
    total=False,
)

_RequiredContentSummaryTypeDef = TypedDict(
    "_RequiredContentSummaryTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
    },
)
_OptionalContentSummaryTypeDef = TypedDict(
    "_OptionalContentSummaryTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class ContentSummaryTypeDef(_RequiredContentSummaryTypeDef, _OptionalContentSummaryTypeDef):
    pass

_RequiredCreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssistantAssociationRequestRequestTypeDef",
    {
        "assistantId": str,
        "association": "AssistantAssociationInputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
    },
)
_OptionalCreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssistantAssociationRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAssistantAssociationRequestRequestTypeDef(
    _RequiredCreateAssistantAssociationRequestRequestTypeDef,
    _OptionalCreateAssistantAssociationRequestRequestTypeDef,
):
    pass

CreateAssistantAssociationResponseTypeDef = TypedDict(
    "CreateAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": "AssistantAssociationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssistantRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssistantRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
    },
)
_OptionalCreateAssistantRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssistantRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAssistantRequestRequestTypeDef(
    _RequiredCreateAssistantRequestRequestTypeDef, _OptionalCreateAssistantRequestRequestTypeDef
):
    pass

CreateAssistantResponseTypeDef = TypedDict(
    "CreateAssistantResponseTypeDef",
    {
        "assistant": "AssistantDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "uploadId": str,
    },
)
_OptionalCreateContentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContentRequestRequestTypeDef",
    {
        "clientToken": str,
        "metadata": Dict[str, str],
        "overrideLinkOutUri": str,
        "tags": Dict[str, str],
        "title": str,
    },
    total=False,
)

class CreateContentRequestRequestTypeDef(
    _RequiredCreateContentRequestRequestTypeDef, _OptionalCreateContentRequestRequestTypeDef
):
    pass

CreateContentResponseTypeDef = TypedDict(
    "CreateContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
    },
)
_OptionalCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "renderingConfiguration": "RenderingConfigurationTypeDef",
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "sourceConfiguration": "SourceConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateKnowledgeBaseRequestRequestTypeDef(
    _RequiredCreateKnowledgeBaseRequestRequestTypeDef,
    _OptionalCreateKnowledgeBaseRequestRequestTypeDef,
):
    pass

CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
    },
)
_OptionalCreateSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSessionRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSessionRequestRequestTypeDef(
    _RequiredCreateSessionRequestRequestTypeDef, _OptionalCreateSessionRequestRequestTypeDef
):
    pass

CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "session": "SessionDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssistantAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

DeleteAssistantRequestRequestTypeDef = TypedDict(
    "DeleteAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

DeleteContentRequestRequestTypeDef = TypedDict(
    "DeleteContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

DocumentTextTypeDef = TypedDict(
    "DocumentTextTypeDef",
    {
        "highlights": List["HighlightTypeDef"],
        "text": str,
    },
    total=False,
)

_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "contentReference": "ContentReferenceTypeDef",
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "excerpt": "DocumentTextTypeDef",
        "title": "DocumentTextTypeDef",
    },
    total=False,
)

class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)

GetAssistantAssociationRequestRequestTypeDef = TypedDict(
    "GetAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

GetAssistantAssociationResponseTypeDef = TypedDict(
    "GetAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": "AssistantAssociationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssistantRequestRequestTypeDef = TypedDict(
    "GetAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

GetAssistantResponseTypeDef = TypedDict(
    "GetAssistantResponseTypeDef",
    {
        "assistant": "AssistantDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentRequestRequestTypeDef = TypedDict(
    "GetContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetContentResponseTypeDef = TypedDict(
    "GetContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentSummaryRequestRequestTypeDef = TypedDict(
    "GetContentSummaryRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetContentSummaryResponseTypeDef = TypedDict(
    "GetContentSummaryResponseTypeDef",
    {
        "contentSummary": "ContentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)
_OptionalGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "waitTimeSeconds": int,
    },
    total=False,
)

class GetRecommendationsRequestRequestTypeDef(
    _RequiredGetRecommendationsRequestRequestTypeDef,
    _OptionalGetRecommendationsRequestRequestTypeDef,
):
    pass

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "recommendations": List["RecommendationDataTypeDef"],
        "triggers": List["RecommendationTriggerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "session": "SessionDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "beginOffsetInclusive": int,
        "endOffsetExclusive": int,
    },
    total=False,
)

KnowledgeBaseAssociationDataTypeDef = TypedDict(
    "KnowledgeBaseAssociationDataTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
    },
    total=False,
)

_RequiredKnowledgeBaseDataTypeDef = TypedDict(
    "_RequiredKnowledgeBaseDataTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
    },
)
_OptionalKnowledgeBaseDataTypeDef = TypedDict(
    "_OptionalKnowledgeBaseDataTypeDef",
    {
        "description": str,
        "lastContentModificationTime": datetime,
        "renderingConfiguration": "RenderingConfigurationTypeDef",
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "sourceConfiguration": "SourceConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class KnowledgeBaseDataTypeDef(
    _RequiredKnowledgeBaseDataTypeDef, _OptionalKnowledgeBaseDataTypeDef
):
    pass

_RequiredKnowledgeBaseSummaryTypeDef = TypedDict(
    "_RequiredKnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
    },
)
_OptionalKnowledgeBaseSummaryTypeDef = TypedDict(
    "_OptionalKnowledgeBaseSummaryTypeDef",
    {
        "description": str,
        "renderingConfiguration": "RenderingConfigurationTypeDef",
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "sourceConfiguration": "SourceConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class KnowledgeBaseSummaryTypeDef(
    _RequiredKnowledgeBaseSummaryTypeDef, _OptionalKnowledgeBaseSummaryTypeDef
):
    pass

_RequiredListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssistantAssociationsRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)
_OptionalListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssistantAssociationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAssistantAssociationsRequestRequestTypeDef(
    _RequiredListAssistantAssociationsRequestRequestTypeDef,
    _OptionalListAssistantAssociationsRequestRequestTypeDef,
):
    pass

ListAssistantAssociationsResponseTypeDef = TypedDict(
    "ListAssistantAssociationsResponseTypeDef",
    {
        "assistantAssociationSummaries": List["AssistantAssociationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssistantsRequestRequestTypeDef = TypedDict(
    "ListAssistantsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAssistantsResponseTypeDef = TypedDict(
    "ListAssistantsResponseTypeDef",
    {
        "assistantSummaries": List["AssistantSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListContentsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListContentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListContentsRequestRequestTypeDef(
    _RequiredListContentsRequestRequestTypeDef, _OptionalListContentsRequestRequestTypeDef
):
    pass

ListContentsResponseTypeDef = TypedDict(
    "ListContentsResponseTypeDef",
    {
        "contentSummaries": List["ContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List["KnowledgeBaseSummaryTypeDef"],
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

NotifyRecommendationsReceivedErrorTypeDef = TypedDict(
    "NotifyRecommendationsReceivedErrorTypeDef",
    {
        "message": str,
        "recommendationId": str,
    },
    total=False,
)

NotifyRecommendationsReceivedRequestRequestTypeDef = TypedDict(
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    {
        "assistantId": str,
        "recommendationIds": List[str],
        "sessionId": str,
    },
)

NotifyRecommendationsReceivedResponseTypeDef = TypedDict(
    "NotifyRecommendationsReceivedResponseTypeDef",
    {
        "errors": List["NotifyRecommendationsReceivedErrorTypeDef"],
        "recommendationIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredQueryAssistantRequestRequestTypeDef = TypedDict(
    "_RequiredQueryAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
        "queryText": str,
    },
)
_OptionalQueryAssistantRequestRequestTypeDef = TypedDict(
    "_OptionalQueryAssistantRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class QueryAssistantRequestRequestTypeDef(
    _RequiredQueryAssistantRequestRequestTypeDef, _OptionalQueryAssistantRequestRequestTypeDef
):
    pass

QueryAssistantResponseTypeDef = TypedDict(
    "QueryAssistantResponseTypeDef",
    {
        "nextToken": str,
        "results": List["ResultDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryRecommendationTriggerDataTypeDef = TypedDict(
    "QueryRecommendationTriggerDataTypeDef",
    {
        "text": str,
    },
    total=False,
)

_RequiredRecommendationDataTypeDef = TypedDict(
    "_RequiredRecommendationDataTypeDef",
    {
        "document": "DocumentTypeDef",
        "recommendationId": str,
    },
)
_OptionalRecommendationDataTypeDef = TypedDict(
    "_OptionalRecommendationDataTypeDef",
    {
        "relevanceLevel": RelevanceLevelType,
        "relevanceScore": float,
        "type": Literal["KNOWLEDGE_CONTENT"],
    },
    total=False,
)

class RecommendationDataTypeDef(
    _RequiredRecommendationDataTypeDef, _OptionalRecommendationDataTypeDef
):
    pass

RecommendationTriggerDataTypeDef = TypedDict(
    "RecommendationTriggerDataTypeDef",
    {
        "query": "QueryRecommendationTriggerDataTypeDef",
    },
    total=False,
)

RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "data": "RecommendationTriggerDataTypeDef",
        "id": str,
        "recommendationIds": List[str],
        "source": RecommendationSourceTypeType,
        "type": Literal["QUERY"],
    },
)

RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

RenderingConfigurationTypeDef = TypedDict(
    "RenderingConfigurationTypeDef",
    {
        "templateUri": str,
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

_RequiredResultDataTypeDef = TypedDict(
    "_RequiredResultDataTypeDef",
    {
        "document": "DocumentTypeDef",
        "resultId": str,
    },
)
_OptionalResultDataTypeDef = TypedDict(
    "_OptionalResultDataTypeDef",
    {
        "relevanceScore": float,
    },
    total=False,
)

class ResultDataTypeDef(_RequiredResultDataTypeDef, _OptionalResultDataTypeDef):
    pass

_RequiredSearchContentRequestRequestTypeDef = TypedDict(
    "_RequiredSearchContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": "SearchExpressionTypeDef",
    },
)
_OptionalSearchContentRequestRequestTypeDef = TypedDict(
    "_OptionalSearchContentRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchContentRequestRequestTypeDef(
    _RequiredSearchContentRequestRequestTypeDef, _OptionalSearchContentRequestRequestTypeDef
):
    pass

SearchContentResponseTypeDef = TypedDict(
    "SearchContentResponseTypeDef",
    {
        "contentSummaries": List["ContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "filters": List["FilterTypeDef"],
    },
)

_RequiredSearchSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchSessionsRequestRequestTypeDef",
    {
        "assistantId": str,
        "searchExpression": "SearchExpressionTypeDef",
    },
)
_OptionalSearchSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchSessionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchSessionsRequestRequestTypeDef(
    _RequiredSearchSessionsRequestRequestTypeDef, _OptionalSearchSessionsRequestRequestTypeDef
):
    pass

SearchSessionsResponseTypeDef = TypedDict(
    "SearchSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessionSummaries": List["SessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

_RequiredSessionDataTypeDef = TypedDict(
    "_RequiredSessionDataTypeDef",
    {
        "name": str,
        "sessionArn": str,
        "sessionId": str,
    },
)
_OptionalSessionDataTypeDef = TypedDict(
    "_OptionalSessionDataTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class SessionDataTypeDef(_RequiredSessionDataTypeDef, _OptionalSessionDataTypeDef):
    pass

SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "sessionArn": str,
        "sessionId": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "appIntegrations": "AppIntegrationsConfigurationTypeDef",
    },
    total=False,
)

StartContentUploadRequestRequestTypeDef = TypedDict(
    "StartContentUploadRequestRequestTypeDef",
    {
        "contentType": str,
        "knowledgeBaseId": str,
    },
)

StartContentUploadResponseTypeDef = TypedDict(
    "StartContentUploadResponseTypeDef",
    {
        "headersToInclude": Dict[str, str],
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateContentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)
_OptionalUpdateContentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContentRequestRequestTypeDef",
    {
        "metadata": Dict[str, str],
        "overrideLinkOutUri": str,
        "removeOverrideLinkOutUri": bool,
        "revisionId": str,
        "title": str,
        "uploadId": str,
    },
    total=False,
)

class UpdateContentRequestRequestTypeDef(
    _RequiredUpdateContentRequestRequestTypeDef, _OptionalUpdateContentRequestRequestTypeDef
):
    pass

UpdateContentResponseTypeDef = TypedDict(
    "UpdateContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "templateUri": str,
    },
)

UpdateKnowledgeBaseTemplateUriResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
