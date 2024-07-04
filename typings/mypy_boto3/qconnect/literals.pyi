"""
Type annotations for qconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_qconnect.literals import AssistantCapabilityTypeType

    data: AssistantCapabilityTypeType = "V1"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssistantCapabilityTypeType",
    "AssistantStatusType",
    "AssistantTypeType",
    "AssociationTypeType",
    "ContentAssociationTypeType",
    "ContentStatusType",
    "ExternalSourceType",
    "FilterFieldType",
    "FilterOperatorType",
    "ImportJobStatusType",
    "ImportJobTypeType",
    "KnowledgeBaseStatusType",
    "KnowledgeBaseTypeType",
    "ListAssistantAssociationsPaginatorName",
    "ListAssistantsPaginatorName",
    "ListContentAssociationsPaginatorName",
    "ListContentsPaginatorName",
    "ListImportJobsPaginatorName",
    "ListKnowledgeBasesPaginatorName",
    "ListQuickResponsesPaginatorName",
    "OrderType",
    "PriorityType",
    "QueryAssistantPaginatorName",
    "QueryConditionComparisonOperatorType",
    "QueryConditionFieldNameType",
    "QueryResultTypeType",
    "QuickResponseFilterOperatorType",
    "QuickResponseQueryOperatorType",
    "QuickResponseStatusType",
    "RecommendationSourceTypeType",
    "RecommendationTriggerTypeType",
    "RecommendationTypeType",
    "RelevanceLevelType",
    "RelevanceType",
    "SearchContentPaginatorName",
    "SearchQuickResponsesPaginatorName",
    "SearchSessionsPaginatorName",
    "SourceContentTypeType",
    "TargetTypeType",
)

AssistantCapabilityTypeType = Literal["V1", "V2"]
AssistantStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
]
AssistantTypeType = Literal["AGENT"]
AssociationTypeType = Literal["KNOWLEDGE_BASE"]
ContentAssociationTypeType = Literal["AMAZON_CONNECT_GUIDE"]
ContentStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
]
ExternalSourceType = Literal["AMAZON_CONNECT"]
FilterFieldType = Literal["NAME"]
FilterOperatorType = Literal["EQUALS"]
ImportJobStatusType = Literal[
    "COMPLETE", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "FAILED", "START_IN_PROGRESS"
]
ImportJobTypeType = Literal["QUICK_RESPONSES"]
KnowledgeBaseStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
]
KnowledgeBaseTypeType = Literal["CUSTOM", "EXTERNAL", "QUICK_RESPONSES"]
ListAssistantAssociationsPaginatorName = Literal["list_assistant_associations"]
ListAssistantsPaginatorName = Literal["list_assistants"]
ListContentAssociationsPaginatorName = Literal["list_content_associations"]
ListContentsPaginatorName = Literal["list_contents"]
ListImportJobsPaginatorName = Literal["list_import_jobs"]
ListKnowledgeBasesPaginatorName = Literal["list_knowledge_bases"]
ListQuickResponsesPaginatorName = Literal["list_quick_responses"]
OrderType = Literal["ASC", "DESC"]
PriorityType = Literal["HIGH", "LOW", "MEDIUM"]
QueryAssistantPaginatorName = Literal["query_assistant"]
QueryConditionComparisonOperatorType = Literal["EQUALS"]
QueryConditionFieldNameType = Literal["RESULT_TYPE"]
QueryResultTypeType = Literal["GENERATIVE_ANSWER", "KNOWLEDGE_CONTENT"]
QuickResponseFilterOperatorType = Literal["EQUALS", "PREFIX"]
QuickResponseQueryOperatorType = Literal["CONTAINS", "CONTAINS_AND_PREFIX"]
QuickResponseStatusType = Literal[
    "CREATED",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
RecommendationSourceTypeType = Literal["ISSUE_DETECTION", "OTHER", "RULE_EVALUATION"]
RecommendationTriggerTypeType = Literal["GENERATIVE", "QUERY"]
RecommendationTypeType = Literal["GENERATIVE_ANSWER", "GENERATIVE_RESPONSE", "KNOWLEDGE_CONTENT"]
RelevanceLevelType = Literal["HIGH", "LOW", "MEDIUM"]
RelevanceType = Literal["HELPFUL", "NOT_HELPFUL"]
SearchContentPaginatorName = Literal["search_content"]
SearchQuickResponsesPaginatorName = Literal["search_quick_responses"]
SearchSessionsPaginatorName = Literal["search_sessions"]
SourceContentTypeType = Literal["KNOWLEDGE_CONTENT"]
TargetTypeType = Literal["RECOMMENDATION", "RESULT"]
