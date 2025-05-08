"""
Type annotations for qconnect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_qconnect.type_defs import AIAgentConfigurationDataTypeDef

    data: AIAgentConfigurationDataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AIAgentTypeType,
    AIPromptAPIFormatType,
    AIPromptTypeType,
    AssistantCapabilityTypeType,
    AssistantStatusType,
    ChannelSubtypeType,
    ChunkingStrategyType,
    ContentStatusType,
    ConversationStatusReasonType,
    ConversationStatusType,
    GuardrailContentFilterTypeType,
    GuardrailContextualGroundingFilterTypeType,
    GuardrailFilterStrengthType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationActionType,
    ImportJobStatusType,
    KnowledgeBaseSearchTypeType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    MessageTemplateAttributeTypeType,
    MessageTemplateFilterOperatorType,
    MessageTemplateQueryOperatorType,
    OrderType,
    OriginType,
    ParticipantType,
    PriorityType,
    QueryResultTypeType,
    QuickResponseFilterOperatorType,
    QuickResponseQueryOperatorType,
    QuickResponseStatusType,
    RecommendationSourceTypeType,
    RecommendationTriggerTypeType,
    RecommendationTypeType,
    ReferenceTypeType,
    RelevanceLevelType,
    RelevanceType,
    StatusType,
    SyncStatusType,
    TargetTypeType,
    VisibilityStatusType,
    WebScopeTypeType,
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
    "AIAgentConfigurationDataTypeDef",
    "AIAgentConfigurationOutputTypeDef",
    "AIAgentConfigurationTypeDef",
    "AIAgentConfigurationUnionTypeDef",
    "AIAgentDataTypeDef",
    "AIAgentSummaryTypeDef",
    "AIAgentVersionSummaryTypeDef",
    "AIGuardrailContentPolicyConfigOutputTypeDef",
    "AIGuardrailContentPolicyConfigTypeDef",
    "AIGuardrailContentPolicyConfigUnionTypeDef",
    "AIGuardrailContextualGroundingPolicyConfigOutputTypeDef",
    "AIGuardrailContextualGroundingPolicyConfigTypeDef",
    "AIGuardrailContextualGroundingPolicyConfigUnionTypeDef",
    "AIGuardrailDataTypeDef",
    "AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef",
    "AIGuardrailSensitiveInformationPolicyConfigTypeDef",
    "AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef",
    "AIGuardrailSummaryTypeDef",
    "AIGuardrailTopicPolicyConfigOutputTypeDef",
    "AIGuardrailTopicPolicyConfigTypeDef",
    "AIGuardrailTopicPolicyConfigUnionTypeDef",
    "AIGuardrailVersionSummaryTypeDef",
    "AIGuardrailWordPolicyConfigOutputTypeDef",
    "AIGuardrailWordPolicyConfigTypeDef",
    "AIGuardrailWordPolicyConfigUnionTypeDef",
    "AIPromptDataTypeDef",
    "AIPromptSummaryTypeDef",
    "AIPromptTemplateConfigurationTypeDef",
    "AIPromptVersionSummaryTypeDef",
    "ActivateMessageTemplateRequestTypeDef",
    "ActivateMessageTemplateResponseTypeDef",
    "AgentAttributesTypeDef",
    "AmazonConnectGuideAssociationDataTypeDef",
    "AnswerRecommendationAIAgentConfigurationOutputTypeDef",
    "AnswerRecommendationAIAgentConfigurationTypeDef",
    "AppIntegrationsConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "AssistantCapabilityConfigurationTypeDef",
    "AssistantDataTypeDef",
    "AssistantIntegrationConfigurationTypeDef",
    "AssistantSummaryTypeDef",
    "AssociationConfigurationDataOutputTypeDef",
    "AssociationConfigurationDataTypeDef",
    "AssociationConfigurationOutputTypeDef",
    "AssociationConfigurationTypeDef",
    "BedrockFoundationModelConfigurationForParsingTypeDef",
    "ChunkingConfigurationOutputTypeDef",
    "ChunkingConfigurationTypeDef",
    "CitationSpanTypeDef",
    "ConfigurationTypeDef",
    "ConnectConfigurationTypeDef",
    "ContentAssociationContentsTypeDef",
    "ContentAssociationDataTypeDef",
    "ContentAssociationSummaryTypeDef",
    "ContentDataDetailsTypeDef",
    "ContentDataTypeDef",
    "ContentFeedbackDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "ConversationContextTypeDef",
    "ConversationStateTypeDef",
    "CreateAIAgentRequestTypeDef",
    "CreateAIAgentResponseTypeDef",
    "CreateAIAgentVersionRequestTypeDef",
    "CreateAIAgentVersionResponseTypeDef",
    "CreateAIGuardrailRequestTypeDef",
    "CreateAIGuardrailResponseTypeDef",
    "CreateAIGuardrailVersionRequestTypeDef",
    "CreateAIGuardrailVersionResponseTypeDef",
    "CreateAIPromptRequestTypeDef",
    "CreateAIPromptResponseTypeDef",
    "CreateAIPromptVersionRequestTypeDef",
    "CreateAIPromptVersionResponseTypeDef",
    "CreateAssistantAssociationRequestTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "CreateAssistantRequestTypeDef",
    "CreateAssistantResponseTypeDef",
    "CreateContentAssociationRequestTypeDef",
    "CreateContentAssociationResponseTypeDef",
    "CreateContentRequestTypeDef",
    "CreateContentResponseTypeDef",
    "CreateKnowledgeBaseRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "CreateMessageTemplateAttachmentRequestTypeDef",
    "CreateMessageTemplateAttachmentResponseTypeDef",
    "CreateMessageTemplateRequestTypeDef",
    "CreateMessageTemplateResponseTypeDef",
    "CreateMessageTemplateVersionRequestTypeDef",
    "CreateMessageTemplateVersionResponseTypeDef",
    "CreateQuickResponseRequestTypeDef",
    "CreateQuickResponseResponseTypeDef",
    "CreateSessionRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "CustomerProfileAttributesOutputTypeDef",
    "CustomerProfileAttributesTypeDef",
    "DataDetailsPaginatorTypeDef",
    "DataDetailsTypeDef",
    "DataReferenceTypeDef",
    "DataSummaryPaginatorTypeDef",
    "DataSummaryTypeDef",
    "DeactivateMessageTemplateRequestTypeDef",
    "DeactivateMessageTemplateResponseTypeDef",
    "DeleteAIAgentRequestTypeDef",
    "DeleteAIAgentVersionRequestTypeDef",
    "DeleteAIGuardrailRequestTypeDef",
    "DeleteAIGuardrailVersionRequestTypeDef",
    "DeleteAIPromptRequestTypeDef",
    "DeleteAIPromptVersionRequestTypeDef",
    "DeleteAssistantAssociationRequestTypeDef",
    "DeleteAssistantRequestTypeDef",
    "DeleteContentAssociationRequestTypeDef",
    "DeleteContentRequestTypeDef",
    "DeleteImportJobRequestTypeDef",
    "DeleteKnowledgeBaseRequestTypeDef",
    "DeleteMessageTemplateAttachmentRequestTypeDef",
    "DeleteMessageTemplateRequestTypeDef",
    "DeleteQuickResponseRequestTypeDef",
    "DocumentTextTypeDef",
    "DocumentTypeDef",
    "EmailHeaderTypeDef",
    "EmailMessageTemplateContentBodyTypeDef",
    "EmailMessageTemplateContentOutputTypeDef",
    "EmailMessageTemplateContentTypeDef",
    "ExtendedMessageTemplateDataTypeDef",
    "ExternalSourceConfigurationTypeDef",
    "FilterTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "GenerativeChunkDataDetailsPaginatorTypeDef",
    "GenerativeChunkDataDetailsTypeDef",
    "GenerativeContentFeedbackDataTypeDef",
    "GenerativeDataDetailsPaginatorTypeDef",
    "GenerativeDataDetailsTypeDef",
    "GenerativeReferenceTypeDef",
    "GetAIAgentRequestTypeDef",
    "GetAIAgentResponseTypeDef",
    "GetAIGuardrailRequestTypeDef",
    "GetAIGuardrailResponseTypeDef",
    "GetAIPromptRequestTypeDef",
    "GetAIPromptResponseTypeDef",
    "GetAssistantAssociationRequestTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "GetAssistantRequestTypeDef",
    "GetAssistantResponseTypeDef",
    "GetContentAssociationRequestTypeDef",
    "GetContentAssociationResponseTypeDef",
    "GetContentRequestTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryRequestTypeDef",
    "GetContentSummaryResponseTypeDef",
    "GetImportJobRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetKnowledgeBaseRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetMessageTemplateRequestTypeDef",
    "GetMessageTemplateResponseTypeDef",
    "GetNextMessageRequestTypeDef",
    "GetNextMessageResponseTypeDef",
    "GetQuickResponseRequestTypeDef",
    "GetQuickResponseResponseTypeDef",
    "GetRecommendationsRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GroupingConfigurationOutputTypeDef",
    "GroupingConfigurationTypeDef",
    "GroupingConfigurationUnionTypeDef",
    "GuardrailContentFilterConfigTypeDef",
    "GuardrailContextualGroundingFilterConfigTypeDef",
    "GuardrailManagedWordsConfigTypeDef",
    "GuardrailPiiEntityConfigTypeDef",
    "GuardrailRegexConfigTypeDef",
    "GuardrailTopicConfigOutputTypeDef",
    "GuardrailTopicConfigTypeDef",
    "GuardrailWordConfigTypeDef",
    "HierarchicalChunkingConfigurationOutputTypeDef",
    "HierarchicalChunkingConfigurationTypeDef",
    "HierarchicalChunkingLevelConfigurationTypeDef",
    "HighlightTypeDef",
    "ImportJobDataTypeDef",
    "ImportJobSummaryTypeDef",
    "IntentDetectedDataDetailsTypeDef",
    "IntentInputDataTypeDef",
    "KnowledgeBaseAssociationConfigurationDataOutputTypeDef",
    "KnowledgeBaseAssociationConfigurationDataTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ListAIAgentVersionsRequestPaginateTypeDef",
    "ListAIAgentVersionsRequestTypeDef",
    "ListAIAgentVersionsResponseTypeDef",
    "ListAIAgentsRequestPaginateTypeDef",
    "ListAIAgentsRequestTypeDef",
    "ListAIAgentsResponseTypeDef",
    "ListAIGuardrailVersionsRequestPaginateTypeDef",
    "ListAIGuardrailVersionsRequestTypeDef",
    "ListAIGuardrailVersionsResponseTypeDef",
    "ListAIGuardrailsRequestPaginateTypeDef",
    "ListAIGuardrailsRequestTypeDef",
    "ListAIGuardrailsResponseTypeDef",
    "ListAIPromptVersionsRequestPaginateTypeDef",
    "ListAIPromptVersionsRequestTypeDef",
    "ListAIPromptVersionsResponseTypeDef",
    "ListAIPromptsRequestPaginateTypeDef",
    "ListAIPromptsRequestTypeDef",
    "ListAIPromptsResponseTypeDef",
    "ListAssistantAssociationsRequestPaginateTypeDef",
    "ListAssistantAssociationsRequestTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ListAssistantsRequestPaginateTypeDef",
    "ListAssistantsRequestTypeDef",
    "ListAssistantsResponseTypeDef",
    "ListContentAssociationsRequestPaginateTypeDef",
    "ListContentAssociationsRequestTypeDef",
    "ListContentAssociationsResponseTypeDef",
    "ListContentsRequestPaginateTypeDef",
    "ListContentsRequestTypeDef",
    "ListContentsResponseTypeDef",
    "ListImportJobsRequestPaginateTypeDef",
    "ListImportJobsRequestTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListKnowledgeBasesRequestPaginateTypeDef",
    "ListKnowledgeBasesRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListMessageTemplateVersionsRequestPaginateTypeDef",
    "ListMessageTemplateVersionsRequestTypeDef",
    "ListMessageTemplateVersionsResponseTypeDef",
    "ListMessageTemplatesRequestPaginateTypeDef",
    "ListMessageTemplatesRequestTypeDef",
    "ListMessageTemplatesResponseTypeDef",
    "ListMessagesRequestPaginateTypeDef",
    "ListMessagesRequestTypeDef",
    "ListMessagesResponseTypeDef",
    "ListQuickResponsesRequestPaginateTypeDef",
    "ListQuickResponsesRequestTypeDef",
    "ListQuickResponsesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedSourceConfigurationOutputTypeDef",
    "ManagedSourceConfigurationTypeDef",
    "ManualSearchAIAgentConfigurationOutputTypeDef",
    "ManualSearchAIAgentConfigurationTypeDef",
    "MessageConfigurationTypeDef",
    "MessageDataTypeDef",
    "MessageInputTypeDef",
    "MessageOutputTypeDef",
    "MessageTemplateAttachmentTypeDef",
    "MessageTemplateAttributesOutputTypeDef",
    "MessageTemplateAttributesTypeDef",
    "MessageTemplateAttributesUnionTypeDef",
    "MessageTemplateBodyContentProviderTypeDef",
    "MessageTemplateContentProviderOutputTypeDef",
    "MessageTemplateContentProviderTypeDef",
    "MessageTemplateContentProviderUnionTypeDef",
    "MessageTemplateDataTypeDef",
    "MessageTemplateFilterFieldTypeDef",
    "MessageTemplateOrderFieldTypeDef",
    "MessageTemplateQueryFieldTypeDef",
    "MessageTemplateSearchExpressionTypeDef",
    "MessageTemplateSearchResultDataTypeDef",
    "MessageTemplateSummaryTypeDef",
    "MessageTemplateVersionSummaryTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "OrConditionOutputTypeDef",
    "OrConditionTypeDef",
    "PaginatorConfigTypeDef",
    "ParsingConfigurationTypeDef",
    "ParsingPromptTypeDef",
    "PutFeedbackRequestTypeDef",
    "PutFeedbackResponseTypeDef",
    "QueryAssistantRequestPaginateTypeDef",
    "QueryAssistantRequestTypeDef",
    "QueryAssistantResponsePaginatorTypeDef",
    "QueryAssistantResponseTypeDef",
    "QueryConditionItemTypeDef",
    "QueryConditionTypeDef",
    "QueryInputDataTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "QueryTextInputDataTypeDef",
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
    "RankingDataTypeDef",
    "RecommendationDataTypeDef",
    "RecommendationTriggerDataTypeDef",
    "RecommendationTriggerTypeDef",
    "RemoveAssistantAIAgentRequestTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestTypeDef",
    "RenderMessageTemplateRequestTypeDef",
    "RenderMessageTemplateResponseTypeDef",
    "RenderingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultDataPaginatorTypeDef",
    "ResultDataTypeDef",
    "RuntimeSessionDataTypeDef",
    "RuntimeSessionDataValueTypeDef",
    "SMSMessageTemplateContentBodyTypeDef",
    "SMSMessageTemplateContentTypeDef",
    "SearchContentRequestPaginateTypeDef",
    "SearchContentRequestTypeDef",
    "SearchContentResponseTypeDef",
    "SearchExpressionTypeDef",
    "SearchMessageTemplatesRequestPaginateTypeDef",
    "SearchMessageTemplatesRequestTypeDef",
    "SearchMessageTemplatesResponseTypeDef",
    "SearchQuickResponsesRequestPaginateTypeDef",
    "SearchQuickResponsesRequestTypeDef",
    "SearchQuickResponsesResponseTypeDef",
    "SearchSessionsRequestPaginateTypeDef",
    "SearchSessionsRequestTypeDef",
    "SearchSessionsResponseTypeDef",
    "SeedUrlTypeDef",
    "SelfServiceAIAgentConfigurationOutputTypeDef",
    "SelfServiceAIAgentConfigurationTypeDef",
    "SelfServiceConversationHistoryTypeDef",
    "SemanticChunkingConfigurationTypeDef",
    "SendMessageRequestTypeDef",
    "SendMessageResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionDataTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "SessionSummaryTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "SourceConfigurationUnionTypeDef",
    "SourceContentDataDetailsTypeDef",
    "StartContentUploadRequestTypeDef",
    "StartContentUploadResponseTypeDef",
    "StartImportJobRequestTypeDef",
    "StartImportJobResponseTypeDef",
    "SystemAttributesTypeDef",
    "SystemEndpointAttributesTypeDef",
    "TagConditionTypeDef",
    "TagFilterOutputTypeDef",
    "TagFilterTypeDef",
    "TagFilterUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TextDataTypeDef",
    "TextFullAIPromptEditTemplateConfigurationTypeDef",
    "TextMessageTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAIAgentRequestTypeDef",
    "UpdateAIAgentResponseTypeDef",
    "UpdateAIGuardrailRequestTypeDef",
    "UpdateAIGuardrailResponseTypeDef",
    "UpdateAIPromptRequestTypeDef",
    "UpdateAIPromptResponseTypeDef",
    "UpdateAssistantAIAgentRequestTypeDef",
    "UpdateAssistantAIAgentResponseTypeDef",
    "UpdateContentRequestTypeDef",
    "UpdateContentResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "UpdateMessageTemplateMetadataRequestTypeDef",
    "UpdateMessageTemplateMetadataResponseTypeDef",
    "UpdateMessageTemplateRequestTypeDef",
    "UpdateMessageTemplateResponseTypeDef",
    "UpdateQuickResponseRequestTypeDef",
    "UpdateQuickResponseResponseTypeDef",
    "UpdateSessionDataRequestTypeDef",
    "UpdateSessionDataResponseTypeDef",
    "UpdateSessionRequestTypeDef",
    "UpdateSessionResponseTypeDef",
    "UrlConfigurationOutputTypeDef",
    "UrlConfigurationTypeDef",
    "VectorIngestionConfigurationOutputTypeDef",
    "VectorIngestionConfigurationTypeDef",
    "VectorIngestionConfigurationUnionTypeDef",
    "WebCrawlerConfigurationOutputTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "WebCrawlerLimitsTypeDef",
)

class AIAgentConfigurationDataTypeDef(TypedDict):
    aiAgentId: str

GuardrailContentFilterConfigTypeDef = TypedDict(
    "GuardrailContentFilterConfigTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "inputStrength": GuardrailFilterStrengthType,
        "outputStrength": GuardrailFilterStrengthType,
    },
)
GuardrailContextualGroundingFilterConfigTypeDef = TypedDict(
    "GuardrailContextualGroundingFilterConfigTypeDef",
    {
        "type": GuardrailContextualGroundingFilterTypeType,
        "threshold": float,
    },
)
GuardrailPiiEntityConfigTypeDef = TypedDict(
    "GuardrailPiiEntityConfigTypeDef",
    {
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationActionType,
    },
)

class GuardrailRegexConfigTypeDef(TypedDict):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: NotRequired[str]

class AIGuardrailSummaryTypeDef(TypedDict):
    name: str
    assistantId: str
    assistantArn: str
    aiGuardrailId: str
    aiGuardrailArn: str
    visibilityStatus: VisibilityStatusType
    modifiedTime: NotRequired[datetime]
    description: NotRequired[str]
    status: NotRequired[StatusType]
    tags: NotRequired[Dict[str, str]]

GuardrailTopicConfigOutputTypeDef = TypedDict(
    "GuardrailTopicConfigOutputTypeDef",
    {
        "name": str,
        "definition": str,
        "type": Literal["DENY"],
        "examples": NotRequired[List[str]],
    },
)
GuardrailTopicConfigTypeDef = TypedDict(
    "GuardrailTopicConfigTypeDef",
    {
        "name": str,
        "definition": str,
        "type": Literal["DENY"],
        "examples": NotRequired[Sequence[str]],
    },
)
GuardrailManagedWordsConfigTypeDef = TypedDict(
    "GuardrailManagedWordsConfigTypeDef",
    {
        "type": Literal["PROFANITY"],
    },
)

class GuardrailWordConfigTypeDef(TypedDict):
    text: str

AIPromptSummaryTypeDef = TypedDict(
    "AIPromptSummaryTypeDef",
    {
        "name": str,
        "assistantId": str,
        "assistantArn": str,
        "aiPromptId": str,
        "type": AIPromptTypeType,
        "aiPromptArn": str,
        "templateType": Literal["TEXT"],
        "modelId": str,
        "apiFormat": AIPromptAPIFormatType,
        "visibilityStatus": VisibilityStatusType,
        "modifiedTime": NotRequired[datetime],
        "origin": NotRequired[OriginType],
        "description": NotRequired[str],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)

class TextFullAIPromptEditTemplateConfigurationTypeDef(TypedDict):
    text: str

class ActivateMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AgentAttributesTypeDef(TypedDict):
    firstName: NotRequired[str]
    lastName: NotRequired[str]

class AmazonConnectGuideAssociationDataTypeDef(TypedDict):
    flowId: NotRequired[str]

class AppIntegrationsConfigurationOutputTypeDef(TypedDict):
    appIntegrationArn: str
    objectFields: NotRequired[List[str]]

class AppIntegrationsConfigurationTypeDef(TypedDict):
    appIntegrationArn: str
    objectFields: NotRequired[Sequence[str]]

class AssistantAssociationInputDataTypeDef(TypedDict):
    knowledgeBaseId: NotRequired[str]

class KnowledgeBaseAssociationDataTypeDef(TypedDict):
    knowledgeBaseId: NotRequired[str]
    knowledgeBaseArn: NotRequired[str]

AssistantCapabilityConfigurationTypeDef = TypedDict(
    "AssistantCapabilityConfigurationTypeDef",
    {
        "type": NotRequired[AssistantCapabilityTypeType],
    },
)

class AssistantIntegrationConfigurationTypeDef(TypedDict):
    topicIntegrationArn: NotRequired[str]

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]

class ParsingPromptTypeDef(TypedDict):
    parsingPromptText: str

class FixedSizeChunkingConfigurationTypeDef(TypedDict):
    maxTokens: int
    overlapPercentage: int

class SemanticChunkingConfigurationTypeDef(TypedDict):
    maxTokens: int
    bufferSize: int
    breakpointPercentileThreshold: int

class CitationSpanTypeDef(TypedDict):
    beginOffsetInclusive: NotRequired[int]
    endOffsetExclusive: NotRequired[int]

class ConnectConfigurationTypeDef(TypedDict):
    instanceId: NotRequired[str]

class RankingDataTypeDef(TypedDict):
    relevanceScore: NotRequired[float]
    relevanceLevel: NotRequired[RelevanceLevelType]

class ContentDataTypeDef(TypedDict):
    contentArn: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    revisionId: str
    title: str
    contentType: str
    status: ContentStatusType
    metadata: Dict[str, str]
    url: str
    urlExpiry: datetime
    tags: NotRequired[Dict[str, str]]
    linkOutUri: NotRequired[str]

class GenerativeContentFeedbackDataTypeDef(TypedDict):
    relevance: RelevanceType

class ContentReferenceTypeDef(TypedDict):
    knowledgeBaseArn: NotRequired[str]
    knowledgeBaseId: NotRequired[str]
    contentArn: NotRequired[str]
    contentId: NotRequired[str]
    sourceURL: NotRequired[str]
    referenceType: NotRequired[ReferenceTypeType]

class ContentSummaryTypeDef(TypedDict):
    contentArn: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    revisionId: str
    title: str
    contentType: str
    status: ContentStatusType
    metadata: Dict[str, str]
    tags: NotRequired[Dict[str, str]]

class SelfServiceConversationHistoryTypeDef(TypedDict):
    turnNumber: int
    inputTranscript: NotRequired[str]
    botResponse: NotRequired[str]

class ConversationStateTypeDef(TypedDict):
    status: ConversationStatusType
    reason: NotRequired[ConversationStatusReasonType]

TimestampTypeDef = Union[datetime, str]

class CreateContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    uploadId: str
    title: NotRequired[str]
    overrideLinkOutUri: NotRequired[str]
    metadata: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class RenderingConfigurationTypeDef(TypedDict):
    templateUri: NotRequired[str]

class CreateMessageTemplateAttachmentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    contentDisposition: Literal["ATTACHMENT"]
    name: str
    body: str
    clientToken: NotRequired[str]

class MessageTemplateAttachmentTypeDef(TypedDict):
    contentDisposition: Literal["ATTACHMENT"]
    name: str
    uploadedTime: datetime
    url: str
    urlExpiry: datetime
    attachmentId: str

class CreateMessageTemplateVersionRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    messageTemplateContentSha256: NotRequired[str]

class QuickResponseDataProviderTypeDef(TypedDict):
    content: NotRequired[str]

class CustomerProfileAttributesOutputTypeDef(TypedDict):
    profileId: NotRequired[str]
    profileARN: NotRequired[str]
    firstName: NotRequired[str]
    middleName: NotRequired[str]
    lastName: NotRequired[str]
    accountNumber: NotRequired[str]
    emailAddress: NotRequired[str]
    phoneNumber: NotRequired[str]
    additionalInformation: NotRequired[str]
    partyType: NotRequired[str]
    businessName: NotRequired[str]
    birthDate: NotRequired[str]
    gender: NotRequired[str]
    mobilePhoneNumber: NotRequired[str]
    homePhoneNumber: NotRequired[str]
    businessPhoneNumber: NotRequired[str]
    businessEmailAddress: NotRequired[str]
    address1: NotRequired[str]
    address2: NotRequired[str]
    address3: NotRequired[str]
    address4: NotRequired[str]
    city: NotRequired[str]
    county: NotRequired[str]
    country: NotRequired[str]
    postalCode: NotRequired[str]
    province: NotRequired[str]
    state: NotRequired[str]
    shippingAddress1: NotRequired[str]
    shippingAddress2: NotRequired[str]
    shippingAddress3: NotRequired[str]
    shippingAddress4: NotRequired[str]
    shippingCity: NotRequired[str]
    shippingCounty: NotRequired[str]
    shippingCountry: NotRequired[str]
    shippingPostalCode: NotRequired[str]
    shippingProvince: NotRequired[str]
    shippingState: NotRequired[str]
    mailingAddress1: NotRequired[str]
    mailingAddress2: NotRequired[str]
    mailingAddress3: NotRequired[str]
    mailingAddress4: NotRequired[str]
    mailingCity: NotRequired[str]
    mailingCounty: NotRequired[str]
    mailingCountry: NotRequired[str]
    mailingPostalCode: NotRequired[str]
    mailingProvince: NotRequired[str]
    mailingState: NotRequired[str]
    billingAddress1: NotRequired[str]
    billingAddress2: NotRequired[str]
    billingAddress3: NotRequired[str]
    billingAddress4: NotRequired[str]
    billingCity: NotRequired[str]
    billingCounty: NotRequired[str]
    billingCountry: NotRequired[str]
    billingPostalCode: NotRequired[str]
    billingProvince: NotRequired[str]
    billingState: NotRequired[str]
    custom: NotRequired[Dict[str, str]]

class CustomerProfileAttributesTypeDef(TypedDict):
    profileId: NotRequired[str]
    profileARN: NotRequired[str]
    firstName: NotRequired[str]
    middleName: NotRequired[str]
    lastName: NotRequired[str]
    accountNumber: NotRequired[str]
    emailAddress: NotRequired[str]
    phoneNumber: NotRequired[str]
    additionalInformation: NotRequired[str]
    partyType: NotRequired[str]
    businessName: NotRequired[str]
    birthDate: NotRequired[str]
    gender: NotRequired[str]
    mobilePhoneNumber: NotRequired[str]
    homePhoneNumber: NotRequired[str]
    businessPhoneNumber: NotRequired[str]
    businessEmailAddress: NotRequired[str]
    address1: NotRequired[str]
    address2: NotRequired[str]
    address3: NotRequired[str]
    address4: NotRequired[str]
    city: NotRequired[str]
    county: NotRequired[str]
    country: NotRequired[str]
    postalCode: NotRequired[str]
    province: NotRequired[str]
    state: NotRequired[str]
    shippingAddress1: NotRequired[str]
    shippingAddress2: NotRequired[str]
    shippingAddress3: NotRequired[str]
    shippingAddress4: NotRequired[str]
    shippingCity: NotRequired[str]
    shippingCounty: NotRequired[str]
    shippingCountry: NotRequired[str]
    shippingPostalCode: NotRequired[str]
    shippingProvince: NotRequired[str]
    shippingState: NotRequired[str]
    mailingAddress1: NotRequired[str]
    mailingAddress2: NotRequired[str]
    mailingAddress3: NotRequired[str]
    mailingAddress4: NotRequired[str]
    mailingCity: NotRequired[str]
    mailingCounty: NotRequired[str]
    mailingCountry: NotRequired[str]
    mailingPostalCode: NotRequired[str]
    mailingProvince: NotRequired[str]
    mailingState: NotRequired[str]
    billingAddress1: NotRequired[str]
    billingAddress2: NotRequired[str]
    billingAddress3: NotRequired[str]
    billingAddress4: NotRequired[str]
    billingCity: NotRequired[str]
    billingCounty: NotRequired[str]
    billingCountry: NotRequired[str]
    billingPostalCode: NotRequired[str]
    billingProvince: NotRequired[str]
    billingState: NotRequired[str]
    custom: NotRequired[Mapping[str, str]]

class GenerativeChunkDataDetailsPaginatorTypeDef(TypedDict):
    completion: NotRequired[str]
    references: NotRequired[List[Dict[str, Any]]]
    nextChunkToken: NotRequired[str]

class IntentDetectedDataDetailsTypeDef(TypedDict):
    intent: str
    intentId: str

class GenerativeChunkDataDetailsTypeDef(TypedDict):
    completion: NotRequired[str]
    references: NotRequired[List[Dict[str, Any]]]
    nextChunkToken: NotRequired[str]

class GenerativeReferenceTypeDef(TypedDict):
    modelId: NotRequired[str]
    generationId: NotRequired[str]

class DeactivateMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int

class DeleteAIAgentRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str

class DeleteAIAgentVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str
    versionNumber: int

class DeleteAIGuardrailRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str

class DeleteAIGuardrailVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str
    versionNumber: int

class DeleteAIPromptRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str

class DeleteAIPromptVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str
    versionNumber: int

class DeleteAssistantAssociationRequestTypeDef(TypedDict):
    assistantAssociationId: str
    assistantId: str

class DeleteAssistantRequestTypeDef(TypedDict):
    assistantId: str

class DeleteContentAssociationRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    contentAssociationId: str

class DeleteContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str

class DeleteImportJobRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    importJobId: str

class DeleteKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class DeleteMessageTemplateAttachmentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    attachmentId: str

class DeleteMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str

class DeleteQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    quickResponseId: str

class HighlightTypeDef(TypedDict):
    beginOffsetInclusive: NotRequired[int]
    endOffsetExclusive: NotRequired[int]

class EmailHeaderTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class MessageTemplateBodyContentProviderTypeDef(TypedDict):
    content: NotRequired[str]

class GroupingConfigurationOutputTypeDef(TypedDict):
    criteria: NotRequired[str]
    values: NotRequired[List[str]]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)

class GetAIAgentRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str

class GetAIGuardrailRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str

class GetAIPromptRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str

class GetAssistantAssociationRequestTypeDef(TypedDict):
    assistantAssociationId: str
    assistantId: str

class GetAssistantRequestTypeDef(TypedDict):
    assistantId: str

class GetContentAssociationRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    contentAssociationId: str

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

class GetMessageTemplateRequestTypeDef(TypedDict):
    messageTemplateId: str
    knowledgeBaseId: str

class GetNextMessageRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    nextMessageToken: str

class GetQuickResponseRequestTypeDef(TypedDict):
    quickResponseId: str
    knowledgeBaseId: str

class GetRecommendationsRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    maxResults: NotRequired[int]
    waitTimeSeconds: NotRequired[int]
    nextChunkToken: NotRequired[str]

class GetSessionRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str

class GroupingConfigurationTypeDef(TypedDict):
    criteria: NotRequired[str]
    values: NotRequired[Sequence[str]]

class HierarchicalChunkingLevelConfigurationTypeDef(TypedDict):
    maxTokens: int

class IntentInputDataTypeDef(TypedDict):
    intentId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAIAgentVersionsRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    origin: NotRequired[OriginType]

class ListAIAgentsRequestTypeDef(TypedDict):
    assistantId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    origin: NotRequired[OriginType]

class ListAIGuardrailVersionsRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAIGuardrailsRequestTypeDef(TypedDict):
    assistantId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAIPromptVersionsRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    origin: NotRequired[OriginType]

class ListAIPromptsRequestTypeDef(TypedDict):
    assistantId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    origin: NotRequired[OriginType]

class ListAssistantAssociationsRequestTypeDef(TypedDict):
    assistantId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAssistantsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListContentAssociationsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListContentsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListImportJobsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListKnowledgeBasesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMessageTemplateVersionsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MessageTemplateVersionSummaryTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    channelSubtype: ChannelSubtypeType
    isActive: bool
    versionNumber: int

class ListMessageTemplatesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MessageTemplateSummaryTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    lastModifiedTime: datetime
    lastModifiedBy: str
    activeVersionNumber: NotRequired[int]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListMessagesRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListQuickResponsesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class QuickResponseSummaryTypeDef(TypedDict):
    quickResponseArn: str
    quickResponseId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    contentType: str
    status: QuickResponseStatusType
    createdTime: datetime
    lastModifiedTime: datetime
    description: NotRequired[str]
    lastModifiedBy: NotRequired[str]
    isActive: NotRequired[bool]
    channels: NotRequired[List[str]]
    tags: NotRequired[Dict[str, str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class MessageConfigurationTypeDef(TypedDict):
    generateFillerMessage: NotRequired[bool]

class TextMessageTypeDef(TypedDict):
    value: NotRequired[str]

MessageTemplateFilterFieldTypeDef = TypedDict(
    "MessageTemplateFilterFieldTypeDef",
    {
        "name": str,
        "operator": MessageTemplateFilterOperatorType,
        "values": NotRequired[Sequence[str]],
        "includeNoExistence": NotRequired[bool],
    },
)

class MessageTemplateOrderFieldTypeDef(TypedDict):
    name: str
    order: NotRequired[OrderType]

MessageTemplateQueryFieldTypeDef = TypedDict(
    "MessageTemplateQueryFieldTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "operator": MessageTemplateQueryOperatorType,
        "allowFuzziness": NotRequired[bool],
        "priority": NotRequired[PriorityType],
    },
)

class NotifyRecommendationsReceivedErrorTypeDef(TypedDict):
    recommendationId: NotRequired[str]
    message: NotRequired[str]

class NotifyRecommendationsReceivedRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    recommendationIds: Sequence[str]

class TagConditionTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class QueryConditionItemTypeDef(TypedDict):
    field: Literal["RESULT_TYPE"]
    comparator: Literal["EQUALS"]
    value: str

class QueryTextInputDataTypeDef(TypedDict):
    text: str

class QueryRecommendationTriggerDataTypeDef(TypedDict):
    text: NotRequired[str]

class QuickResponseContentProviderTypeDef(TypedDict):
    content: NotRequired[str]

QuickResponseFilterFieldTypeDef = TypedDict(
    "QuickResponseFilterFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseFilterOperatorType,
        "values": NotRequired[Sequence[str]],
        "includeNoExistence": NotRequired[bool],
    },
)

class QuickResponseOrderFieldTypeDef(TypedDict):
    name: str
    order: NotRequired[OrderType]

QuickResponseQueryFieldTypeDef = TypedDict(
    "QuickResponseQueryFieldTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "operator": QuickResponseQueryOperatorType,
        "allowFuzziness": NotRequired[bool],
        "priority": NotRequired[PriorityType],
    },
)

class RemoveAssistantAIAgentRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentType: AIAgentTypeType

class RemoveKnowledgeBaseTemplateUriRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class RuntimeSessionDataValueTypeDef(TypedDict):
    stringValue: NotRequired[str]

class SessionSummaryTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    assistantId: str
    assistantArn: str

class SeedUrlTypeDef(TypedDict):
    url: NotRequired[str]

class SessionIntegrationConfigurationTypeDef(TypedDict):
    topicIntegrationArn: NotRequired[str]

class StartContentUploadRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentType: str
    presignedUrlTimeToLive: NotRequired[int]

class SystemEndpointAttributesTypeDef(TypedDict):
    address: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    revisionId: NotRequired[str]
    title: NotRequired[str]
    overrideLinkOutUri: NotRequired[str]
    removeOverrideLinkOutUri: NotRequired[bool]
    metadata: NotRequired[Mapping[str, str]]
    uploadId: NotRequired[str]

class UpdateKnowledgeBaseTemplateUriRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    templateUri: str

class WebCrawlerLimitsTypeDef(TypedDict):
    rateLimit: NotRequired[int]

class UpdateAssistantAIAgentRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentType: AIAgentTypeType
    configuration: AIAgentConfigurationDataTypeDef

class AIGuardrailContentPolicyConfigOutputTypeDef(TypedDict):
    filtersConfig: List[GuardrailContentFilterConfigTypeDef]

class AIGuardrailContentPolicyConfigTypeDef(TypedDict):
    filtersConfig: Sequence[GuardrailContentFilterConfigTypeDef]

class AIGuardrailContextualGroundingPolicyConfigOutputTypeDef(TypedDict):
    filtersConfig: List[GuardrailContextualGroundingFilterConfigTypeDef]

class AIGuardrailContextualGroundingPolicyConfigTypeDef(TypedDict):
    filtersConfig: Sequence[GuardrailContextualGroundingFilterConfigTypeDef]

class AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef(TypedDict):
    piiEntitiesConfig: NotRequired[List[GuardrailPiiEntityConfigTypeDef]]
    regexesConfig: NotRequired[List[GuardrailRegexConfigTypeDef]]

class AIGuardrailSensitiveInformationPolicyConfigTypeDef(TypedDict):
    piiEntitiesConfig: NotRequired[Sequence[GuardrailPiiEntityConfigTypeDef]]
    regexesConfig: NotRequired[Sequence[GuardrailRegexConfigTypeDef]]

class AIGuardrailVersionSummaryTypeDef(TypedDict):
    aiGuardrailSummary: NotRequired[AIGuardrailSummaryTypeDef]
    versionNumber: NotRequired[int]

class AIGuardrailTopicPolicyConfigOutputTypeDef(TypedDict):
    topicsConfig: List[GuardrailTopicConfigOutputTypeDef]

class AIGuardrailTopicPolicyConfigTypeDef(TypedDict):
    topicsConfig: Sequence[GuardrailTopicConfigTypeDef]

class AIGuardrailWordPolicyConfigOutputTypeDef(TypedDict):
    wordsConfig: NotRequired[List[GuardrailWordConfigTypeDef]]
    managedWordListsConfig: NotRequired[List[GuardrailManagedWordsConfigTypeDef]]

class AIGuardrailWordPolicyConfigTypeDef(TypedDict):
    wordsConfig: NotRequired[Sequence[GuardrailWordConfigTypeDef]]
    managedWordListsConfig: NotRequired[Sequence[GuardrailManagedWordsConfigTypeDef]]

class AIPromptVersionSummaryTypeDef(TypedDict):
    aiPromptSummary: NotRequired[AIPromptSummaryTypeDef]
    versionNumber: NotRequired[int]

class AIPromptTemplateConfigurationTypeDef(TypedDict):
    textFullAIPromptEditTemplateConfiguration: NotRequired[
        TextFullAIPromptEditTemplateConfigurationTypeDef
    ]

class ActivateMessageTemplateResponseTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateMessageTemplateResponseTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListAIGuardrailsResponseTypeDef(TypedDict):
    aiGuardrailSummaries: List[AIGuardrailSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAIPromptsResponseTypeDef(TypedDict):
    aiPromptSummaries: List[AIPromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartContentUploadResponseTypeDef(TypedDict):
    uploadId: str
    url: str
    urlExpiry: datetime
    headersToInclude: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ContentAssociationContentsTypeDef(TypedDict):
    amazonConnectGuideAssociation: NotRequired[AmazonConnectGuideAssociationDataTypeDef]

class CreateAssistantAssociationRequestTypeDef(TypedDict):
    assistantId: str
    associationType: Literal["KNOWLEDGE_BASE"]
    association: AssistantAssociationInputDataTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class AssistantAssociationOutputDataTypeDef(TypedDict):
    knowledgeBaseAssociation: NotRequired[KnowledgeBaseAssociationDataTypeDef]

AssistantDataTypeDef = TypedDict(
    "AssistantDataTypeDef",
    {
        "assistantId": str,
        "assistantArn": str,
        "name": str,
        "type": Literal["AGENT"],
        "status": AssistantStatusType,
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "capabilityConfiguration": NotRequired[AssistantCapabilityConfigurationTypeDef],
        "aiAgentConfiguration": NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]],
    },
)
AssistantSummaryTypeDef = TypedDict(
    "AssistantSummaryTypeDef",
    {
        "assistantId": str,
        "assistantArn": str,
        "name": str,
        "type": Literal["AGENT"],
        "status": AssistantStatusType,
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "capabilityConfiguration": NotRequired[AssistantCapabilityConfigurationTypeDef],
        "aiAgentConfiguration": NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]],
    },
)
CreateAssistantRequestTypeDef = TypedDict(
    "CreateAssistantRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
    },
)

class BedrockFoundationModelConfigurationForParsingTypeDef(TypedDict):
    modelArn: str
    parsingPrompt: NotRequired[ParsingPromptTypeDef]

class ConfigurationTypeDef(TypedDict):
    connectConfiguration: NotRequired[ConnectConfigurationTypeDef]

class GenerativeDataDetailsPaginatorTypeDef(TypedDict):
    completion: str
    references: List[Dict[str, Any]]
    rankingData: RankingDataTypeDef

class GenerativeDataDetailsTypeDef(TypedDict):
    completion: str
    references: List[Dict[str, Any]]
    rankingData: RankingDataTypeDef

class CreateContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContentResponseTypeDef(TypedDict):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContentFeedbackDataTypeDef(TypedDict):
    generativeContentFeedbackData: NotRequired[GenerativeContentFeedbackDataTypeDef]

class GetContentSummaryResponseTypeDef(TypedDict):
    contentSummary: ContentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentsResponseTypeDef(TypedDict):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchContentResponseTypeDef(TypedDict):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConversationContextTypeDef(TypedDict):
    selfServiceConversationHistory: Sequence[SelfServiceConversationHistoryTypeDef]

class CreateAIAgentVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str
    modifiedTime: NotRequired[TimestampTypeDef]
    clientToken: NotRequired[str]

class CreateAIGuardrailVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str
    modifiedTime: NotRequired[TimestampTypeDef]
    clientToken: NotRequired[str]

class CreateAIPromptVersionRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str
    modifiedTime: NotRequired[TimestampTypeDef]
    clientToken: NotRequired[str]

class CreateMessageTemplateAttachmentResponseTypeDef(TypedDict):
    attachment: MessageTemplateAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataReferenceTypeDef(TypedDict):
    contentReference: NotRequired[ContentReferenceTypeDef]
    generativeReference: NotRequired[GenerativeReferenceTypeDef]

class DocumentTextTypeDef(TypedDict):
    text: NotRequired[str]
    highlights: NotRequired[List[HighlightTypeDef]]

class EmailMessageTemplateContentBodyTypeDef(TypedDict):
    plainText: NotRequired[MessageTemplateBodyContentProviderTypeDef]
    html: NotRequired[MessageTemplateBodyContentProviderTypeDef]

class SMSMessageTemplateContentBodyTypeDef(TypedDict):
    plainText: NotRequired[MessageTemplateBodyContentProviderTypeDef]

class MessageTemplateSearchResultDataTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    lastModifiedTime: datetime
    lastModifiedBy: str
    isActive: NotRequired[bool]
    versionNumber: NotRequired[int]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    language: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class SearchExpressionTypeDef(TypedDict):
    filters: Sequence[FilterTypeDef]

GroupingConfigurationUnionTypeDef = Union[
    GroupingConfigurationTypeDef, GroupingConfigurationOutputTypeDef
]

class HierarchicalChunkingConfigurationOutputTypeDef(TypedDict):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class HierarchicalChunkingConfigurationTypeDef(TypedDict):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class ListAIAgentVersionsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str
    origin: NotRequired[OriginType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAIAgentsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    origin: NotRequired[OriginType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAIGuardrailVersionsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAIGuardrailsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAIPromptVersionsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str
    origin: NotRequired[OriginType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAIPromptsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    origin: NotRequired[OriginType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssistantAssociationsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssistantsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContentAssociationsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContentsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportJobsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKnowledgeBasesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMessageTemplateVersionsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMessageTemplatesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMessagesRequestPaginateTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQuickResponsesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMessageTemplateVersionsResponseTypeDef(TypedDict):
    messageTemplateVersionSummaries: List[MessageTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMessageTemplatesResponseTypeDef(TypedDict):
    messageTemplateSummaries: List[MessageTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQuickResponsesResponseTypeDef(TypedDict):
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SendMessageResponseTypeDef(TypedDict):
    requestMessageId: str
    configuration: MessageConfigurationTypeDef
    nextMessageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MessageDataTypeDef(TypedDict):
    text: NotRequired[TextMessageTypeDef]

class MessageTemplateSearchExpressionTypeDef(TypedDict):
    queries: NotRequired[Sequence[MessageTemplateQueryFieldTypeDef]]
    filters: NotRequired[Sequence[MessageTemplateFilterFieldTypeDef]]
    orderOnField: NotRequired[MessageTemplateOrderFieldTypeDef]

class NotifyRecommendationsReceivedResponseTypeDef(TypedDict):
    recommendationIds: List[str]
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrConditionOutputTypeDef(TypedDict):
    andConditions: NotRequired[List[TagConditionTypeDef]]
    tagCondition: NotRequired[TagConditionTypeDef]

class OrConditionTypeDef(TypedDict):
    andConditions: NotRequired[Sequence[TagConditionTypeDef]]
    tagCondition: NotRequired[TagConditionTypeDef]

class QueryConditionTypeDef(TypedDict):
    single: NotRequired[QueryConditionItemTypeDef]

class QueryInputDataTypeDef(TypedDict):
    queryTextInputData: NotRequired[QueryTextInputDataTypeDef]
    intentInputData: NotRequired[IntentInputDataTypeDef]

class RecommendationTriggerDataTypeDef(TypedDict):
    query: NotRequired[QueryRecommendationTriggerDataTypeDef]

class QuickResponseContentsTypeDef(TypedDict):
    plainText: NotRequired[QuickResponseContentProviderTypeDef]
    markdown: NotRequired[QuickResponseContentProviderTypeDef]

class QuickResponseSearchExpressionTypeDef(TypedDict):
    queries: NotRequired[Sequence[QuickResponseQueryFieldTypeDef]]
    filters: NotRequired[Sequence[QuickResponseFilterFieldTypeDef]]
    orderOnField: NotRequired[QuickResponseOrderFieldTypeDef]

class RuntimeSessionDataTypeDef(TypedDict):
    key: str
    value: RuntimeSessionDataValueTypeDef

class SearchSessionsResponseTypeDef(TypedDict):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UrlConfigurationOutputTypeDef(TypedDict):
    seedUrls: NotRequired[List[SeedUrlTypeDef]]

class UrlConfigurationTypeDef(TypedDict):
    seedUrls: NotRequired[Sequence[SeedUrlTypeDef]]

class SystemAttributesTypeDef(TypedDict):
    name: NotRequired[str]
    customerEndpoint: NotRequired[SystemEndpointAttributesTypeDef]
    systemEndpoint: NotRequired[SystemEndpointAttributesTypeDef]

AIGuardrailContentPolicyConfigUnionTypeDef = Union[
    AIGuardrailContentPolicyConfigTypeDef, AIGuardrailContentPolicyConfigOutputTypeDef
]
AIGuardrailContextualGroundingPolicyConfigUnionTypeDef = Union[
    AIGuardrailContextualGroundingPolicyConfigTypeDef,
    AIGuardrailContextualGroundingPolicyConfigOutputTypeDef,
]
AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef = Union[
    AIGuardrailSensitiveInformationPolicyConfigTypeDef,
    AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef,
]

class ListAIGuardrailVersionsResponseTypeDef(TypedDict):
    aiGuardrailVersionSummaries: List[AIGuardrailVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

AIGuardrailTopicPolicyConfigUnionTypeDef = Union[
    AIGuardrailTopicPolicyConfigTypeDef, AIGuardrailTopicPolicyConfigOutputTypeDef
]

class AIGuardrailDataTypeDef(TypedDict):
    assistantId: str
    assistantArn: str
    aiGuardrailArn: str
    aiGuardrailId: str
    name: str
    visibilityStatus: VisibilityStatusType
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: NotRequired[str]
    topicPolicyConfig: NotRequired[AIGuardrailTopicPolicyConfigOutputTypeDef]
    contentPolicyConfig: NotRequired[AIGuardrailContentPolicyConfigOutputTypeDef]
    wordPolicyConfig: NotRequired[AIGuardrailWordPolicyConfigOutputTypeDef]
    sensitiveInformationPolicyConfig: NotRequired[
        AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef
    ]
    contextualGroundingPolicyConfig: NotRequired[
        AIGuardrailContextualGroundingPolicyConfigOutputTypeDef
    ]
    tags: NotRequired[Dict[str, str]]
    status: NotRequired[StatusType]
    modifiedTime: NotRequired[datetime]

AIGuardrailWordPolicyConfigUnionTypeDef = Union[
    AIGuardrailWordPolicyConfigTypeDef, AIGuardrailWordPolicyConfigOutputTypeDef
]

class ListAIPromptVersionsResponseTypeDef(TypedDict):
    aiPromptVersionSummaries: List[AIPromptVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

AIPromptDataTypeDef = TypedDict(
    "AIPromptDataTypeDef",
    {
        "assistantId": str,
        "assistantArn": str,
        "aiPromptId": str,
        "aiPromptArn": str,
        "name": str,
        "type": AIPromptTypeType,
        "templateType": Literal["TEXT"],
        "modelId": str,
        "apiFormat": AIPromptAPIFormatType,
        "templateConfiguration": AIPromptTemplateConfigurationTypeDef,
        "visibilityStatus": VisibilityStatusType,
        "modifiedTime": NotRequired[datetime],
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
    },
)
CreateAIPromptRequestTypeDef = TypedDict(
    "CreateAIPromptRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
        "type": AIPromptTypeType,
        "templateConfiguration": AIPromptTemplateConfigurationTypeDef,
        "visibilityStatus": VisibilityStatusType,
        "templateType": Literal["TEXT"],
        "modelId": str,
        "apiFormat": AIPromptAPIFormatType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
    },
)

class UpdateAIPromptRequestTypeDef(TypedDict):
    assistantId: str
    aiPromptId: str
    visibilityStatus: VisibilityStatusType
    clientToken: NotRequired[str]
    templateConfiguration: NotRequired[AIPromptTemplateConfigurationTypeDef]
    description: NotRequired[str]

class ContentAssociationDataTypeDef(TypedDict):
    knowledgeBaseId: str
    knowledgeBaseArn: str
    contentId: str
    contentArn: str
    contentAssociationId: str
    contentAssociationArn: str
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    associationData: ContentAssociationContentsTypeDef
    tags: NotRequired[Dict[str, str]]

class ContentAssociationSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    knowledgeBaseArn: str
    contentId: str
    contentArn: str
    contentAssociationId: str
    contentAssociationArn: str
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    associationData: ContentAssociationContentsTypeDef
    tags: NotRequired[Dict[str, str]]

class CreateContentAssociationRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    contentId: str
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    association: ContentAssociationContentsTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class AssistantAssociationDataTypeDef(TypedDict):
    assistantAssociationId: str
    assistantAssociationArn: str
    assistantId: str
    assistantArn: str
    associationType: Literal["KNOWLEDGE_BASE"]
    associationData: AssistantAssociationOutputDataTypeDef
    tags: NotRequired[Dict[str, str]]

class AssistantAssociationSummaryTypeDef(TypedDict):
    assistantAssociationId: str
    assistantAssociationArn: str
    assistantId: str
    assistantArn: str
    associationType: Literal["KNOWLEDGE_BASE"]
    associationData: AssistantAssociationOutputDataTypeDef
    tags: NotRequired[Dict[str, str]]

class CreateAssistantResponseTypeDef(TypedDict):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantResponseTypeDef(TypedDict):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssistantAIAgentResponseTypeDef(TypedDict):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantsResponseTypeDef(TypedDict):
    assistantSummaries: List[AssistantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ParsingConfigurationTypeDef(TypedDict):
    parsingStrategy: Literal["BEDROCK_FOUNDATION_MODEL"]
    bedrockFoundationModelConfiguration: NotRequired[
        BedrockFoundationModelConfigurationForParsingTypeDef
    ]

class ExternalSourceConfigurationTypeDef(TypedDict):
    source: Literal["AMAZON_CONNECT"]
    configuration: ConfigurationTypeDef

class PutFeedbackRequestTypeDef(TypedDict):
    assistantId: str
    targetId: str
    targetType: TargetTypeType
    contentFeedback: ContentFeedbackDataTypeDef

class PutFeedbackResponseTypeDef(TypedDict):
    assistantId: str
    assistantArn: str
    targetId: str
    targetType: TargetTypeType
    contentFeedback: ContentFeedbackDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentTypeDef(TypedDict):
    contentReference: ContentReferenceTypeDef
    title: NotRequired[DocumentTextTypeDef]
    excerpt: NotRequired[DocumentTextTypeDef]

class TextDataTypeDef(TypedDict):
    title: NotRequired[DocumentTextTypeDef]
    excerpt: NotRequired[DocumentTextTypeDef]

class EmailMessageTemplateContentOutputTypeDef(TypedDict):
    subject: NotRequired[str]
    body: NotRequired[EmailMessageTemplateContentBodyTypeDef]
    headers: NotRequired[List[EmailHeaderTypeDef]]

class EmailMessageTemplateContentTypeDef(TypedDict):
    subject: NotRequired[str]
    body: NotRequired[EmailMessageTemplateContentBodyTypeDef]
    headers: NotRequired[Sequence[EmailHeaderTypeDef]]

class SMSMessageTemplateContentTypeDef(TypedDict):
    body: NotRequired[SMSMessageTemplateContentBodyTypeDef]

class SearchMessageTemplatesResponseTypeDef(TypedDict):
    results: List[MessageTemplateSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchContentRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchContentRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SearchSessionsRequestPaginateTypeDef(TypedDict):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSessionsRequestTypeDef(TypedDict):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class CreateQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    content: QuickResponseDataProviderTypeDef
    contentType: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]
    description: NotRequired[str]
    shortcutKey: NotRequired[str]
    isActive: NotRequired[bool]
    channels: NotRequired[Sequence[str]]
    language: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateMessageTemplateMetadataRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    name: NotRequired[str]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]

class UpdateQuickResponseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    quickResponseId: str
    name: NotRequired[str]
    content: NotRequired[QuickResponseDataProviderTypeDef]
    contentType: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]
    removeGroupingConfiguration: NotRequired[bool]
    description: NotRequired[str]
    removeDescription: NotRequired[bool]
    shortcutKey: NotRequired[str]
    removeShortcutKey: NotRequired[bool]
    isActive: NotRequired[bool]
    channels: NotRequired[Sequence[str]]
    language: NotRequired[str]

class ChunkingConfigurationOutputTypeDef(TypedDict):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: NotRequired[FixedSizeChunkingConfigurationTypeDef]
    hierarchicalChunkingConfiguration: NotRequired[HierarchicalChunkingConfigurationOutputTypeDef]
    semanticChunkingConfiguration: NotRequired[SemanticChunkingConfigurationTypeDef]

class ChunkingConfigurationTypeDef(TypedDict):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: NotRequired[FixedSizeChunkingConfigurationTypeDef]
    hierarchicalChunkingConfiguration: NotRequired[HierarchicalChunkingConfigurationTypeDef]
    semanticChunkingConfiguration: NotRequired[SemanticChunkingConfigurationTypeDef]

class MessageInputTypeDef(TypedDict):
    value: MessageDataTypeDef

class MessageOutputTypeDef(TypedDict):
    value: MessageDataTypeDef
    messageId: str
    participant: ParticipantType
    timestamp: datetime

class SearchMessageTemplatesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpressionTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchMessageTemplatesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpressionTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TagFilterOutputTypeDef(TypedDict):
    tagCondition: NotRequired[TagConditionTypeDef]
    andConditions: NotRequired[List[TagConditionTypeDef]]
    orConditions: NotRequired[List[OrConditionOutputTypeDef]]

class TagFilterTypeDef(TypedDict):
    tagCondition: NotRequired[TagConditionTypeDef]
    andConditions: NotRequired[Sequence[TagConditionTypeDef]]
    orConditions: NotRequired[Sequence[OrConditionTypeDef]]

class QueryAssistantRequestPaginateTypeDef(TypedDict):
    assistantId: str
    queryText: NotRequired[str]
    sessionId: NotRequired[str]
    queryCondition: NotRequired[Sequence[QueryConditionTypeDef]]
    queryInputData: NotRequired[QueryInputDataTypeDef]
    overrideKnowledgeBaseSearchType: NotRequired[KnowledgeBaseSearchTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class QueryAssistantRequestTypeDef(TypedDict):
    assistantId: str
    queryText: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    sessionId: NotRequired[str]
    queryCondition: NotRequired[Sequence[QueryConditionTypeDef]]
    queryInputData: NotRequired[QueryInputDataTypeDef]
    overrideKnowledgeBaseSearchType: NotRequired[KnowledgeBaseSearchTypeType]

RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "id": str,
        "type": RecommendationTriggerTypeType,
        "source": RecommendationSourceTypeType,
        "data": RecommendationTriggerDataTypeDef,
        "recommendationIds": List[str],
    },
)

class QuickResponseDataTypeDef(TypedDict):
    quickResponseArn: str
    quickResponseId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    contentType: str
    status: QuickResponseStatusType
    createdTime: datetime
    lastModifiedTime: datetime
    contents: NotRequired[QuickResponseContentsTypeDef]
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    shortcutKey: NotRequired[str]
    lastModifiedBy: NotRequired[str]
    isActive: NotRequired[bool]
    channels: NotRequired[List[str]]
    language: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class QuickResponseSearchResultDataTypeDef(TypedDict):
    quickResponseArn: str
    quickResponseId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    contentType: str
    status: QuickResponseStatusType
    contents: QuickResponseContentsTypeDef
    createdTime: datetime
    lastModifiedTime: datetime
    isActive: bool
    description: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    shortcutKey: NotRequired[str]
    lastModifiedBy: NotRequired[str]
    channels: NotRequired[List[str]]
    language: NotRequired[str]
    attributesNotInterpolated: NotRequired[List[str]]
    attributesInterpolated: NotRequired[List[str]]
    tags: NotRequired[Dict[str, str]]

class SearchQuickResponsesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchQuickResponsesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    attributes: NotRequired[Mapping[str, str]]

class UpdateSessionDataRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    data: Sequence[RuntimeSessionDataTypeDef]
    namespace: NotRequired[Literal["Custom"]]

class UpdateSessionDataResponseTypeDef(TypedDict):
    sessionArn: str
    sessionId: str
    namespace: Literal["Custom"]
    data: List[RuntimeSessionDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WebCrawlerConfigurationOutputTypeDef(TypedDict):
    urlConfiguration: UrlConfigurationOutputTypeDef
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    inclusionFilters: NotRequired[List[str]]
    exclusionFilters: NotRequired[List[str]]
    scope: NotRequired[WebScopeTypeType]

class WebCrawlerConfigurationTypeDef(TypedDict):
    urlConfiguration: UrlConfigurationTypeDef
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    inclusionFilters: NotRequired[Sequence[str]]
    exclusionFilters: NotRequired[Sequence[str]]
    scope: NotRequired[WebScopeTypeType]

class MessageTemplateAttributesOutputTypeDef(TypedDict):
    systemAttributes: NotRequired[SystemAttributesTypeDef]
    agentAttributes: NotRequired[AgentAttributesTypeDef]
    customerProfileAttributes: NotRequired[CustomerProfileAttributesOutputTypeDef]
    customAttributes: NotRequired[Dict[str, str]]

class MessageTemplateAttributesTypeDef(TypedDict):
    systemAttributes: NotRequired[SystemAttributesTypeDef]
    agentAttributes: NotRequired[AgentAttributesTypeDef]
    customerProfileAttributes: NotRequired[CustomerProfileAttributesTypeDef]
    customAttributes: NotRequired[Mapping[str, str]]

class CreateAIGuardrailResponseTypeDef(TypedDict):
    aiGuardrail: AIGuardrailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAIGuardrailVersionResponseTypeDef(TypedDict):
    aiGuardrail: AIGuardrailDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetAIGuardrailResponseTypeDef(TypedDict):
    aiGuardrail: AIGuardrailDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAIGuardrailResponseTypeDef(TypedDict):
    aiGuardrail: AIGuardrailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAIGuardrailRequestTypeDef(TypedDict):
    assistantId: str
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    visibilityStatus: VisibilityStatusType
    clientToken: NotRequired[str]
    description: NotRequired[str]
    topicPolicyConfig: NotRequired[AIGuardrailTopicPolicyConfigUnionTypeDef]
    contentPolicyConfig: NotRequired[AIGuardrailContentPolicyConfigUnionTypeDef]
    wordPolicyConfig: NotRequired[AIGuardrailWordPolicyConfigUnionTypeDef]
    sensitiveInformationPolicyConfig: NotRequired[
        AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef
    ]
    contextualGroundingPolicyConfig: NotRequired[
        AIGuardrailContextualGroundingPolicyConfigUnionTypeDef
    ]
    tags: NotRequired[Mapping[str, str]]

class UpdateAIGuardrailRequestTypeDef(TypedDict):
    assistantId: str
    aiGuardrailId: str
    visibilityStatus: VisibilityStatusType
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    topicPolicyConfig: NotRequired[AIGuardrailTopicPolicyConfigUnionTypeDef]
    contentPolicyConfig: NotRequired[AIGuardrailContentPolicyConfigUnionTypeDef]
    wordPolicyConfig: NotRequired[AIGuardrailWordPolicyConfigUnionTypeDef]
    sensitiveInformationPolicyConfig: NotRequired[
        AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef
    ]
    contextualGroundingPolicyConfig: NotRequired[
        AIGuardrailContextualGroundingPolicyConfigUnionTypeDef
    ]

class CreateAIPromptResponseTypeDef(TypedDict):
    aiPrompt: AIPromptDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAIPromptVersionResponseTypeDef(TypedDict):
    aiPrompt: AIPromptDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetAIPromptResponseTypeDef(TypedDict):
    aiPrompt: AIPromptDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAIPromptResponseTypeDef(TypedDict):
    aiPrompt: AIPromptDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContentAssociationResponseTypeDef(TypedDict):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentAssociationResponseTypeDef(TypedDict):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentAssociationsResponseTypeDef(TypedDict):
    contentAssociationSummaries: List[ContentAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

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
    importJobId: str
    knowledgeBaseId: str
    uploadId: str
    knowledgeBaseArn: str
    importJobType: Literal["QUICK_RESPONSES"]
    status: ImportJobStatusType
    url: str
    urlExpiry: datetime
    createdTime: datetime
    lastModifiedTime: datetime
    failedRecordReport: NotRequired[str]
    metadata: NotRequired[Dict[str, str]]
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]

class ImportJobSummaryTypeDef(TypedDict):
    importJobId: str
    knowledgeBaseId: str
    uploadId: str
    knowledgeBaseArn: str
    importJobType: Literal["QUICK_RESPONSES"]
    status: ImportJobStatusType
    createdTime: datetime
    lastModifiedTime: datetime
    metadata: NotRequired[Dict[str, str]]
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]

class StartImportJobRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    importJobType: Literal["QUICK_RESPONSES"]
    uploadId: str
    clientToken: NotRequired[str]
    metadata: NotRequired[Mapping[str, str]]
    externalSourceConfiguration: NotRequired[ExternalSourceConfigurationTypeDef]

class ContentDataDetailsTypeDef(TypedDict):
    textData: TextDataTypeDef
    rankingData: RankingDataTypeDef

SourceContentDataDetailsTypeDef = TypedDict(
    "SourceContentDataDetailsTypeDef",
    {
        "id": str,
        "type": Literal["KNOWLEDGE_CONTENT"],
        "textData": TextDataTypeDef,
        "rankingData": RankingDataTypeDef,
        "citationSpan": NotRequired[CitationSpanTypeDef],
    },
)

class MessageTemplateContentProviderOutputTypeDef(TypedDict):
    email: NotRequired[EmailMessageTemplateContentOutputTypeDef]
    sms: NotRequired[SMSMessageTemplateContentTypeDef]

class MessageTemplateContentProviderTypeDef(TypedDict):
    email: NotRequired[EmailMessageTemplateContentTypeDef]
    sms: NotRequired[SMSMessageTemplateContentTypeDef]

class VectorIngestionConfigurationOutputTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationOutputTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]

class VectorIngestionConfigurationTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]

SendMessageRequestTypeDef = TypedDict(
    "SendMessageRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
        "type": Literal["TEXT"],
        "message": MessageInputTypeDef,
        "conversationContext": NotRequired[ConversationContextTypeDef],
        "configuration": NotRequired[MessageConfigurationTypeDef],
        "clientToken": NotRequired[str],
    },
)
GetNextMessageResponseTypeDef = TypedDict(
    "GetNextMessageResponseTypeDef",
    {
        "type": Literal["TEXT"],
        "response": MessageOutputTypeDef,
        "requestMessageId": str,
        "conversationState": ConversationStateTypeDef,
        "nextMessageToken": str,
        "conversationSessionData": List[RuntimeSessionDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListMessagesResponseTypeDef(TypedDict):
    messages: List[MessageOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class KnowledgeBaseAssociationConfigurationDataOutputTypeDef(TypedDict):
    contentTagFilter: NotRequired[TagFilterOutputTypeDef]
    maxResults: NotRequired[int]
    overrideKnowledgeBaseSearchType: NotRequired[KnowledgeBaseSearchTypeType]

class SessionDataTypeDef(TypedDict):
    sessionArn: str
    sessionId: str
    name: str
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    integrationConfiguration: NotRequired[SessionIntegrationConfigurationTypeDef]
    tagFilter: NotRequired[TagFilterOutputTypeDef]
    aiAgentConfiguration: NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]]
    origin: NotRequired[OriginType]

class KnowledgeBaseAssociationConfigurationDataTypeDef(TypedDict):
    contentTagFilter: NotRequired[TagFilterTypeDef]
    maxResults: NotRequired[int]
    overrideKnowledgeBaseSearchType: NotRequired[KnowledgeBaseSearchTypeType]

TagFilterUnionTypeDef = Union[TagFilterTypeDef, TagFilterOutputTypeDef]

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

class ManagedSourceConfigurationOutputTypeDef(TypedDict):
    webCrawlerConfiguration: NotRequired[WebCrawlerConfigurationOutputTypeDef]

class ManagedSourceConfigurationTypeDef(TypedDict):
    webCrawlerConfiguration: NotRequired[WebCrawlerConfigurationTypeDef]

MessageTemplateAttributesUnionTypeDef = Union[
    MessageTemplateAttributesTypeDef, MessageTemplateAttributesOutputTypeDef
]

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

class DataDetailsPaginatorTypeDef(TypedDict):
    contentData: NotRequired[ContentDataDetailsTypeDef]
    generativeData: NotRequired[GenerativeDataDetailsPaginatorTypeDef]
    intentDetectedData: NotRequired[IntentDetectedDataDetailsTypeDef]
    sourceContentData: NotRequired[SourceContentDataDetailsTypeDef]
    generativeChunkData: NotRequired[GenerativeChunkDataDetailsPaginatorTypeDef]

class DataDetailsTypeDef(TypedDict):
    contentData: NotRequired[ContentDataDetailsTypeDef]
    generativeData: NotRequired[GenerativeDataDetailsTypeDef]
    intentDetectedData: NotRequired[IntentDetectedDataDetailsTypeDef]
    sourceContentData: NotRequired[SourceContentDataDetailsTypeDef]
    generativeChunkData: NotRequired[GenerativeChunkDataDetailsTypeDef]

class ExtendedMessageTemplateDataTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    lastModifiedTime: datetime
    lastModifiedBy: str
    content: MessageTemplateContentProviderOutputTypeDef
    messageTemplateContentSha256: str
    description: NotRequired[str]
    language: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    defaultAttributes: NotRequired[MessageTemplateAttributesOutputTypeDef]
    attributeTypes: NotRequired[List[MessageTemplateAttributeTypeType]]
    attachments: NotRequired[List[MessageTemplateAttachmentTypeDef]]
    isActive: NotRequired[bool]
    versionNumber: NotRequired[int]
    tags: NotRequired[Dict[str, str]]

class MessageTemplateDataTypeDef(TypedDict):
    messageTemplateArn: str
    messageTemplateId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    name: str
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    lastModifiedTime: datetime
    lastModifiedBy: str
    content: MessageTemplateContentProviderOutputTypeDef
    messageTemplateContentSha256: str
    description: NotRequired[str]
    language: NotRequired[str]
    groupingConfiguration: NotRequired[GroupingConfigurationOutputTypeDef]
    defaultAttributes: NotRequired[MessageTemplateAttributesOutputTypeDef]
    attributeTypes: NotRequired[List[MessageTemplateAttributeTypeType]]
    tags: NotRequired[Dict[str, str]]

class RenderMessageTemplateResponseTypeDef(TypedDict):
    content: MessageTemplateContentProviderOutputTypeDef
    attributesNotInterpolated: List[str]
    attachments: List[MessageTemplateAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

MessageTemplateContentProviderUnionTypeDef = Union[
    MessageTemplateContentProviderTypeDef, MessageTemplateContentProviderOutputTypeDef
]
VectorIngestionConfigurationUnionTypeDef = Union[
    VectorIngestionConfigurationTypeDef, VectorIngestionConfigurationOutputTypeDef
]

class AssociationConfigurationDataOutputTypeDef(TypedDict):
    knowledgeBaseAssociationConfigurationData: NotRequired[
        KnowledgeBaseAssociationConfigurationDataOutputTypeDef
    ]

class CreateSessionResponseTypeDef(TypedDict):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(TypedDict):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSessionResponseTypeDef(TypedDict):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociationConfigurationDataTypeDef(TypedDict):
    knowledgeBaseAssociationConfigurationData: NotRequired[
        KnowledgeBaseAssociationConfigurationDataTypeDef
    ]

class CreateSessionRequestTypeDef(TypedDict):
    assistantId: str
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    tagFilter: NotRequired[TagFilterUnionTypeDef]
    aiAgentConfiguration: NotRequired[Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]]

class UpdateSessionRequestTypeDef(TypedDict):
    assistantId: str
    sessionId: str
    description: NotRequired[str]
    tagFilter: NotRequired[TagFilterUnionTypeDef]
    aiAgentConfiguration: NotRequired[Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]]

class SourceConfigurationOutputTypeDef(TypedDict):
    appIntegrations: NotRequired[AppIntegrationsConfigurationOutputTypeDef]
    managedSourceConfiguration: NotRequired[ManagedSourceConfigurationOutputTypeDef]

class SourceConfigurationTypeDef(TypedDict):
    appIntegrations: NotRequired[AppIntegrationsConfigurationTypeDef]
    managedSourceConfiguration: NotRequired[ManagedSourceConfigurationTypeDef]

class RenderMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    attributes: MessageTemplateAttributesUnionTypeDef

class DataSummaryPaginatorTypeDef(TypedDict):
    reference: DataReferenceTypeDef
    details: DataDetailsPaginatorTypeDef

class DataSummaryTypeDef(TypedDict):
    reference: DataReferenceTypeDef
    details: DataDetailsTypeDef

class CreateMessageTemplateVersionResponseTypeDef(TypedDict):
    messageTemplate: ExtendedMessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMessageTemplateResponseTypeDef(TypedDict):
    messageTemplate: ExtendedMessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMessageTemplateResponseTypeDef(TypedDict):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMessageTemplateMetadataResponseTypeDef(TypedDict):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMessageTemplateResponseTypeDef(TypedDict):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    content: MessageTemplateContentProviderUnionTypeDef
    channelSubtype: ChannelSubtypeType
    description: NotRequired[str]
    language: NotRequired[str]
    defaultAttributes: NotRequired[MessageTemplateAttributesUnionTypeDef]
    groupingConfiguration: NotRequired[GroupingConfigurationUnionTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateMessageTemplateRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    messageTemplateId: str
    content: NotRequired[MessageTemplateContentProviderUnionTypeDef]
    language: NotRequired[str]
    defaultAttributes: NotRequired[MessageTemplateAttributesUnionTypeDef]

class AssociationConfigurationOutputTypeDef(TypedDict):
    associationId: NotRequired[str]
    associationType: NotRequired[Literal["KNOWLEDGE_BASE"]]
    associationConfigurationData: NotRequired[AssociationConfigurationDataOutputTypeDef]

class AssociationConfigurationTypeDef(TypedDict):
    associationId: NotRequired[str]
    associationType: NotRequired[Literal["KNOWLEDGE_BASE"]]
    associationConfigurationData: NotRequired[AssociationConfigurationDataTypeDef]

class KnowledgeBaseDataTypeDef(TypedDict):
    knowledgeBaseId: str
    knowledgeBaseArn: str
    name: str
    knowledgeBaseType: KnowledgeBaseTypeType
    status: KnowledgeBaseStatusType
    lastContentModificationTime: NotRequired[datetime]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationOutputTypeDef]
    sourceConfiguration: NotRequired[SourceConfigurationOutputTypeDef]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    ingestionStatus: NotRequired[SyncStatusType]
    ingestionFailureReasons: NotRequired[List[str]]

class KnowledgeBaseSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    knowledgeBaseArn: str
    name: str
    knowledgeBaseType: KnowledgeBaseTypeType
    status: KnowledgeBaseStatusType
    sourceConfiguration: NotRequired[SourceConfigurationOutputTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationOutputTypeDef]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]
ResultDataPaginatorTypeDef = TypedDict(
    "ResultDataPaginatorTypeDef",
    {
        "resultId": str,
        "document": NotRequired[DocumentTypeDef],
        "relevanceScore": NotRequired[float],
        "data": NotRequired[DataSummaryPaginatorTypeDef],
        "type": NotRequired[QueryResultTypeType],
    },
)
RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "recommendationId": str,
        "document": NotRequired[DocumentTypeDef],
        "relevanceScore": NotRequired[float],
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "type": NotRequired[RecommendationTypeType],
        "data": NotRequired[DataSummaryTypeDef],
    },
)
ResultDataTypeDef = TypedDict(
    "ResultDataTypeDef",
    {
        "resultId": str,
        "document": NotRequired[DocumentTypeDef],
        "relevanceScore": NotRequired[float],
        "data": NotRequired[DataSummaryTypeDef],
        "type": NotRequired[QueryResultTypeType],
    },
)

class AnswerRecommendationAIAgentConfigurationOutputTypeDef(TypedDict):
    intentLabelingGenerationAIPromptId: NotRequired[str]
    queryReformulationAIPromptId: NotRequired[str]
    answerGenerationAIPromptId: NotRequired[str]
    answerGenerationAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[List[AssociationConfigurationOutputTypeDef]]
    locale: NotRequired[str]

class ManualSearchAIAgentConfigurationOutputTypeDef(TypedDict):
    answerGenerationAIPromptId: NotRequired[str]
    answerGenerationAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[List[AssociationConfigurationOutputTypeDef]]
    locale: NotRequired[str]

class SelfServiceAIAgentConfigurationOutputTypeDef(TypedDict):
    selfServicePreProcessingAIPromptId: NotRequired[str]
    selfServiceAnswerGenerationAIPromptId: NotRequired[str]
    selfServiceAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[List[AssociationConfigurationOutputTypeDef]]

class AnswerRecommendationAIAgentConfigurationTypeDef(TypedDict):
    intentLabelingGenerationAIPromptId: NotRequired[str]
    queryReformulationAIPromptId: NotRequired[str]
    answerGenerationAIPromptId: NotRequired[str]
    answerGenerationAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[Sequence[AssociationConfigurationTypeDef]]
    locale: NotRequired[str]

class ManualSearchAIAgentConfigurationTypeDef(TypedDict):
    answerGenerationAIPromptId: NotRequired[str]
    answerGenerationAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[Sequence[AssociationConfigurationTypeDef]]
    locale: NotRequired[str]

class SelfServiceAIAgentConfigurationTypeDef(TypedDict):
    selfServicePreProcessingAIPromptId: NotRequired[str]
    selfServiceAnswerGenerationAIPromptId: NotRequired[str]
    selfServiceAIGuardrailId: NotRequired[str]
    associationConfigurations: NotRequired[Sequence[AssociationConfigurationTypeDef]]

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
    name: str
    knowledgeBaseType: KnowledgeBaseTypeType
    clientToken: NotRequired[str]
    sourceConfiguration: NotRequired[SourceConfigurationUnionTypeDef]
    renderingConfiguration: NotRequired[RenderingConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationUnionTypeDef]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class QueryAssistantResponsePaginatorTypeDef(TypedDict):
    results: List[ResultDataPaginatorTypeDef]
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

class AIAgentConfigurationOutputTypeDef(TypedDict):
    manualSearchAIAgentConfiguration: NotRequired[ManualSearchAIAgentConfigurationOutputTypeDef]
    answerRecommendationAIAgentConfiguration: NotRequired[
        AnswerRecommendationAIAgentConfigurationOutputTypeDef
    ]
    selfServiceAIAgentConfiguration: NotRequired[SelfServiceAIAgentConfigurationOutputTypeDef]

class AIAgentConfigurationTypeDef(TypedDict):
    manualSearchAIAgentConfiguration: NotRequired[ManualSearchAIAgentConfigurationTypeDef]
    answerRecommendationAIAgentConfiguration: NotRequired[
        AnswerRecommendationAIAgentConfigurationTypeDef
    ]
    selfServiceAIAgentConfiguration: NotRequired[SelfServiceAIAgentConfigurationTypeDef]

AIAgentDataTypeDef = TypedDict(
    "AIAgentDataTypeDef",
    {
        "assistantId": str,
        "assistantArn": str,
        "aiAgentId": str,
        "aiAgentArn": str,
        "name": str,
        "type": AIAgentTypeType,
        "configuration": AIAgentConfigurationOutputTypeDef,
        "visibilityStatus": VisibilityStatusType,
        "modifiedTime": NotRequired[datetime],
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
    },
)
AIAgentSummaryTypeDef = TypedDict(
    "AIAgentSummaryTypeDef",
    {
        "name": str,
        "assistantId": str,
        "assistantArn": str,
        "aiAgentId": str,
        "type": AIAgentTypeType,
        "aiAgentArn": str,
        "visibilityStatus": VisibilityStatusType,
        "modifiedTime": NotRequired[datetime],
        "configuration": NotRequired[AIAgentConfigurationOutputTypeDef],
        "origin": NotRequired[OriginType],
        "description": NotRequired[str],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)
AIAgentConfigurationUnionTypeDef = Union[
    AIAgentConfigurationTypeDef, AIAgentConfigurationOutputTypeDef
]

class CreateAIAgentResponseTypeDef(TypedDict):
    aiAgent: AIAgentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAIAgentVersionResponseTypeDef(TypedDict):
    aiAgent: AIAgentDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetAIAgentResponseTypeDef(TypedDict):
    aiAgent: AIAgentDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAIAgentResponseTypeDef(TypedDict):
    aiAgent: AIAgentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AIAgentVersionSummaryTypeDef(TypedDict):
    aiAgentSummary: NotRequired[AIAgentSummaryTypeDef]
    versionNumber: NotRequired[int]

class ListAIAgentsResponseTypeDef(TypedDict):
    aiAgentSummaries: List[AIAgentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateAIAgentRequestTypeDef = TypedDict(
    "CreateAIAgentRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
        "type": AIAgentTypeType,
        "configuration": AIAgentConfigurationUnionTypeDef,
        "visibilityStatus": VisibilityStatusType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
    },
)

class UpdateAIAgentRequestTypeDef(TypedDict):
    assistantId: str
    aiAgentId: str
    visibilityStatus: VisibilityStatusType
    clientToken: NotRequired[str]
    configuration: NotRequired[AIAgentConfigurationUnionTypeDef]
    description: NotRequired[str]

class ListAIAgentVersionsResponseTypeDef(TypedDict):
    aiAgentVersionSummaries: List[AIAgentVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
