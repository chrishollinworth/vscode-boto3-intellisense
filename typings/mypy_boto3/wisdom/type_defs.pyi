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
    "AssistantIntegrationConfigurationTypeDef",
    "AssistantSummaryTypeDef",
    "ConfigurationTypeDef",
    "ConnectConfigurationTypeDef",
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
    "CreateQuickResponseRequestRequestTypeDef",
    "CreateQuickResponseResponseTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteImportJobRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DeleteQuickResponseRequestRequestTypeDef",
    "DocumentTextTypeDef",
    "DocumentTypeDef",
    "ExternalSourceConfigurationTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetAssistantResponseTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetContentSummaryResponseTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetQuickResponseRequestRequestTypeDef",
    "GetQuickResponseResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GroupingConfigurationTypeDef",
    "HighlightTypeDef",
    "ImportJobDataTypeDef",
    "ImportJobSummaryTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListAssistantsResponseTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListContentsResponseTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListQuickResponsesRequestRequestTypeDef",
    "ListQuickResponsesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryAssistantRequestRequestTypeDef",
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
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultDataTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentResponseTypeDef",
    "SearchExpressionTypeDef",
    "SearchQuickResponsesRequestRequestTypeDef",
    "SearchQuickResponsesResponseTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionDataTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "SessionSummaryTypeDef",
    "SourceConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "StartContentUploadResponseTypeDef",
    "StartImportJobRequestRequestTypeDef",
    "StartImportJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateContentResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "UpdateQuickResponseRequestRequestTypeDef",
    "UpdateQuickResponseResponseTypeDef",
)

_RequiredAppIntegrationsConfigurationTypeDef = TypedDict(
    "_RequiredAppIntegrationsConfigurationTypeDef",
    {
        "appIntegrationArn": str,
    },
)
_OptionalAppIntegrationsConfigurationTypeDef = TypedDict(
    "_OptionalAppIntegrationsConfigurationTypeDef",
    {
        "objectFields": List[str],
    },
    total=False,
)

class AppIntegrationsConfigurationTypeDef(
    _RequiredAppIntegrationsConfigurationTypeDef, _OptionalAppIntegrationsConfigurationTypeDef
):
    pass

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
        "integrationConfiguration": "AssistantIntegrationConfigurationTypeDef",
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantDataTypeDef(_RequiredAssistantDataTypeDef, _OptionalAssistantDataTypeDef):
    pass

AssistantIntegrationConfigurationTypeDef = TypedDict(
    "AssistantIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": str,
    },
    total=False,
)

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
        "integrationConfiguration": "AssistantIntegrationConfigurationTypeDef",
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class AssistantSummaryTypeDef(_RequiredAssistantSummaryTypeDef, _OptionalAssistantSummaryTypeDef):
    pass

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "connectConfiguration": "ConnectConfigurationTypeDef",
    },
    total=False,
)

ConnectConfigurationTypeDef = TypedDict(
    "ConnectConfigurationTypeDef",
    {
        "instanceId": str,
    },
    total=False,
)

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

_RequiredCreateQuickResponseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuickResponseRequestRequestTypeDef",
    {
        "content": "QuickResponseDataProviderTypeDef",
        "knowledgeBaseId": str,
        "name": str,
    },
)
_OptionalCreateQuickResponseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuickResponseRequestRequestTypeDef",
    {
        "channels": List[str],
        "clientToken": str,
        "contentType": str,
        "description": str,
        "groupingConfiguration": "GroupingConfigurationTypeDef",
        "isActive": bool,
        "language": str,
        "shortcutKey": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateQuickResponseRequestRequestTypeDef(
    _RequiredCreateQuickResponseRequestRequestTypeDef,
    _OptionalCreateQuickResponseRequestRequestTypeDef,
):
    pass

CreateQuickResponseResponseTypeDef = TypedDict(
    "CreateQuickResponseResponseTypeDef",
    {
        "quickResponse": "QuickResponseDataTypeDef",
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

DeleteImportJobRequestRequestTypeDef = TypedDict(
    "DeleteImportJobRequestRequestTypeDef",
    {
        "importJobId": str,
        "knowledgeBaseId": str,
    },
)

DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

DeleteQuickResponseRequestRequestTypeDef = TypedDict(
    "DeleteQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
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

ExternalSourceConfigurationTypeDef = TypedDict(
    "ExternalSourceConfigurationTypeDef",
    {
        "configuration": "ConfigurationTypeDef",
        "source": Literal["AMAZON_CONNECT"],
    },
)

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

GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "importJobId": str,
        "knowledgeBaseId": str,
    },
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "importJob": "ImportJobDataTypeDef",
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

GetQuickResponseRequestRequestTypeDef = TypedDict(
    "GetQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
    },
)

GetQuickResponseResponseTypeDef = TypedDict(
    "GetQuickResponseResponseTypeDef",
    {
        "quickResponse": "QuickResponseDataTypeDef",
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

GroupingConfigurationTypeDef = TypedDict(
    "GroupingConfigurationTypeDef",
    {
        "criteria": str,
        "values": List[str],
    },
    total=False,
)

HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "beginOffsetInclusive": int,
        "endOffsetExclusive": int,
    },
    total=False,
)

_RequiredImportJobDataTypeDef = TypedDict(
    "_RequiredImportJobDataTypeDef",
    {
        "createdTime": datetime,
        "importJobId": str,
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "status": ImportJobStatusType,
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
    },
)
_OptionalImportJobDataTypeDef = TypedDict(
    "_OptionalImportJobDataTypeDef",
    {
        "externalSourceConfiguration": "ExternalSourceConfigurationTypeDef",
        "failedRecordReport": str,
        "metadata": Dict[str, str],
    },
    total=False,
)

class ImportJobDataTypeDef(_RequiredImportJobDataTypeDef, _OptionalImportJobDataTypeDef):
    pass

_RequiredImportJobSummaryTypeDef = TypedDict(
    "_RequiredImportJobSummaryTypeDef",
    {
        "createdTime": datetime,
        "importJobId": str,
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "status": ImportJobStatusType,
        "uploadId": str,
    },
)
_OptionalImportJobSummaryTypeDef = TypedDict(
    "_OptionalImportJobSummaryTypeDef",
    {
        "externalSourceConfiguration": "ExternalSourceConfigurationTypeDef",
        "metadata": Dict[str, str],
    },
    total=False,
)

class ImportJobSummaryTypeDef(_RequiredImportJobSummaryTypeDef, _OptionalImportJobSummaryTypeDef):
    pass

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

_RequiredListImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListImportJobsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListImportJobsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListImportJobsRequestRequestTypeDef(
    _RequiredListImportJobsRequestRequestTypeDef, _OptionalListImportJobsRequestRequestTypeDef
):
    pass

ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {
        "importJobSummaries": List["ImportJobSummaryTypeDef"],
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

_RequiredListQuickResponsesRequestRequestTypeDef = TypedDict(
    "_RequiredListQuickResponsesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListQuickResponsesRequestRequestTypeDef = TypedDict(
    "_OptionalListQuickResponsesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListQuickResponsesRequestRequestTypeDef(
    _RequiredListQuickResponsesRequestRequestTypeDef,
    _OptionalListQuickResponsesRequestRequestTypeDef,
):
    pass

ListQuickResponsesResponseTypeDef = TypedDict(
    "ListQuickResponsesResponseTypeDef",
    {
        "nextToken": str,
        "quickResponseSummaries": List["QuickResponseSummaryTypeDef"],
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

QuickResponseContentProviderTypeDef = TypedDict(
    "QuickResponseContentProviderTypeDef",
    {
        "content": str,
    },
    total=False,
)

QuickResponseContentsTypeDef = TypedDict(
    "QuickResponseContentsTypeDef",
    {
        "markdown": "QuickResponseContentProviderTypeDef",
        "plainText": "QuickResponseContentProviderTypeDef",
    },
    total=False,
)

QuickResponseDataProviderTypeDef = TypedDict(
    "QuickResponseDataProviderTypeDef",
    {
        "content": str,
    },
    total=False,
)

_RequiredQuickResponseDataTypeDef = TypedDict(
    "_RequiredQuickResponseDataTypeDef",
    {
        "contentType": str,
        "createdTime": datetime,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
    },
)
_OptionalQuickResponseDataTypeDef = TypedDict(
    "_OptionalQuickResponseDataTypeDef",
    {
        "channels": List[str],
        "contents": "QuickResponseContentsTypeDef",
        "description": str,
        "groupingConfiguration": "GroupingConfigurationTypeDef",
        "isActive": bool,
        "language": str,
        "lastModifiedBy": str,
        "shortcutKey": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class QuickResponseDataTypeDef(
    _RequiredQuickResponseDataTypeDef, _OptionalQuickResponseDataTypeDef
):
    pass

_RequiredQuickResponseFilterFieldTypeDef = TypedDict(
    "_RequiredQuickResponseFilterFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseFilterOperatorType,
    },
)
_OptionalQuickResponseFilterFieldTypeDef = TypedDict(
    "_OptionalQuickResponseFilterFieldTypeDef",
    {
        "includeNoExistence": bool,
        "values": List[str],
    },
    total=False,
)

class QuickResponseFilterFieldTypeDef(
    _RequiredQuickResponseFilterFieldTypeDef, _OptionalQuickResponseFilterFieldTypeDef
):
    pass

_RequiredQuickResponseOrderFieldTypeDef = TypedDict(
    "_RequiredQuickResponseOrderFieldTypeDef",
    {
        "name": str,
    },
)
_OptionalQuickResponseOrderFieldTypeDef = TypedDict(
    "_OptionalQuickResponseOrderFieldTypeDef",
    {
        "order": OrderType,
    },
    total=False,
)

class QuickResponseOrderFieldTypeDef(
    _RequiredQuickResponseOrderFieldTypeDef, _OptionalQuickResponseOrderFieldTypeDef
):
    pass

_RequiredQuickResponseQueryFieldTypeDef = TypedDict(
    "_RequiredQuickResponseQueryFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseQueryOperatorType,
        "values": List[str],
    },
)
_OptionalQuickResponseQueryFieldTypeDef = TypedDict(
    "_OptionalQuickResponseQueryFieldTypeDef",
    {
        "allowFuzziness": bool,
        "priority": PriorityType,
    },
    total=False,
)

class QuickResponseQueryFieldTypeDef(
    _RequiredQuickResponseQueryFieldTypeDef, _OptionalQuickResponseQueryFieldTypeDef
):
    pass

QuickResponseSearchExpressionTypeDef = TypedDict(
    "QuickResponseSearchExpressionTypeDef",
    {
        "filters": List["QuickResponseFilterFieldTypeDef"],
        "orderOnField": "QuickResponseOrderFieldTypeDef",
        "queries": List["QuickResponseQueryFieldTypeDef"],
    },
    total=False,
)

_RequiredQuickResponseSearchResultDataTypeDef = TypedDict(
    "_RequiredQuickResponseSearchResultDataTypeDef",
    {
        "contentType": str,
        "contents": "QuickResponseContentsTypeDef",
        "createdTime": datetime,
        "isActive": bool,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
    },
)
_OptionalQuickResponseSearchResultDataTypeDef = TypedDict(
    "_OptionalQuickResponseSearchResultDataTypeDef",
    {
        "attributesInterpolated": List[str],
        "attributesNotInterpolated": List[str],
        "channels": List[str],
        "description": str,
        "groupingConfiguration": "GroupingConfigurationTypeDef",
        "language": str,
        "lastModifiedBy": str,
        "shortcutKey": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class QuickResponseSearchResultDataTypeDef(
    _RequiredQuickResponseSearchResultDataTypeDef, _OptionalQuickResponseSearchResultDataTypeDef
):
    pass

_RequiredQuickResponseSummaryTypeDef = TypedDict(
    "_RequiredQuickResponseSummaryTypeDef",
    {
        "contentType": str,
        "createdTime": datetime,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
    },
)
_OptionalQuickResponseSummaryTypeDef = TypedDict(
    "_OptionalQuickResponseSummaryTypeDef",
    {
        "channels": List[str],
        "description": str,
        "isActive": bool,
        "lastModifiedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class QuickResponseSummaryTypeDef(
    _RequiredQuickResponseSummaryTypeDef, _OptionalQuickResponseSummaryTypeDef
):
    pass

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

_RequiredSearchQuickResponsesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchQuickResponsesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": "QuickResponseSearchExpressionTypeDef",
    },
)
_OptionalSearchQuickResponsesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchQuickResponsesRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchQuickResponsesRequestRequestTypeDef(
    _RequiredSearchQuickResponsesRequestRequestTypeDef,
    _OptionalSearchQuickResponsesRequestRequestTypeDef,
):
    pass

SearchQuickResponsesResponseTypeDef = TypedDict(
    "SearchQuickResponsesResponseTypeDef",
    {
        "nextToken": str,
        "results": List["QuickResponseSearchResultDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "integrationConfiguration": "SessionIntegrationConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class SessionDataTypeDef(_RequiredSessionDataTypeDef, _OptionalSessionDataTypeDef):
    pass

SessionIntegrationConfigurationTypeDef = TypedDict(
    "SessionIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": str,
    },
    total=False,
)

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

_RequiredStartContentUploadRequestRequestTypeDef = TypedDict(
    "_RequiredStartContentUploadRequestRequestTypeDef",
    {
        "contentType": str,
        "knowledgeBaseId": str,
    },
)
_OptionalStartContentUploadRequestRequestTypeDef = TypedDict(
    "_OptionalStartContentUploadRequestRequestTypeDef",
    {
        "presignedUrlTimeToLive": int,
    },
    total=False,
)

class StartContentUploadRequestRequestTypeDef(
    _RequiredStartContentUploadRequestRequestTypeDef,
    _OptionalStartContentUploadRequestRequestTypeDef,
):
    pass

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

_RequiredStartImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportJobRequestRequestTypeDef",
    {
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseId": str,
        "uploadId": str,
    },
)
_OptionalStartImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "externalSourceConfiguration": "ExternalSourceConfigurationTypeDef",
        "metadata": Dict[str, str],
    },
    total=False,
)

class StartImportJobRequestRequestTypeDef(
    _RequiredStartImportJobRequestRequestTypeDef, _OptionalStartImportJobRequestRequestTypeDef
):
    pass

StartImportJobResponseTypeDef = TypedDict(
    "StartImportJobResponseTypeDef",
    {
        "importJob": "ImportJobDataTypeDef",
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

_RequiredUpdateQuickResponseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
    },
)
_OptionalUpdateQuickResponseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuickResponseRequestRequestTypeDef",
    {
        "channels": List[str],
        "content": "QuickResponseDataProviderTypeDef",
        "contentType": str,
        "description": str,
        "groupingConfiguration": "GroupingConfigurationTypeDef",
        "isActive": bool,
        "language": str,
        "name": str,
        "removeDescription": bool,
        "removeGroupingConfiguration": bool,
        "removeShortcutKey": bool,
        "shortcutKey": str,
    },
    total=False,
)

class UpdateQuickResponseRequestRequestTypeDef(
    _RequiredUpdateQuickResponseRequestRequestTypeDef,
    _OptionalUpdateQuickResponseRequestRequestTypeDef,
):
    pass

UpdateQuickResponseResponseTypeDef = TypedDict(
    "UpdateQuickResponseResponseTypeDef",
    {
        "quickResponse": "QuickResponseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
