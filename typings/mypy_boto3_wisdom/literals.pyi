"""
Type annotations for wisdom service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/literals.html)

Usage::

    ```python
    from mypy_boto3_wisdom.literals import AssistantStatusType

    data: AssistantStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssistantStatusType",
    "AssistantTypeType",
    "AssociationTypeType",
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
    "ListContentsPaginatorName",
    "ListImportJobsPaginatorName",
    "ListKnowledgeBasesPaginatorName",
    "ListQuickResponsesPaginatorName",
    "OrderType",
    "PriorityType",
    "QueryAssistantPaginatorName",
    "QuickResponseFilterOperatorType",
    "QuickResponseQueryOperatorType",
    "QuickResponseStatusType",
    "RecommendationSourceTypeType",
    "RecommendationTriggerTypeType",
    "RecommendationTypeType",
    "RelevanceLevelType",
    "SearchContentPaginatorName",
    "SearchQuickResponsesPaginatorName",
    "SearchSessionsPaginatorName",
)

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
ListContentsPaginatorName = Literal["list_contents"]
ListImportJobsPaginatorName = Literal["list_import_jobs"]
ListKnowledgeBasesPaginatorName = Literal["list_knowledge_bases"]
ListQuickResponsesPaginatorName = Literal["list_quick_responses"]
OrderType = Literal["ASC", "DESC"]
PriorityType = Literal["HIGH", "LOW", "MEDIUM"]
QueryAssistantPaginatorName = Literal["query_assistant"]
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
RecommendationTriggerTypeType = Literal["QUERY"]
RecommendationTypeType = Literal["KNOWLEDGE_CONTENT"]
RelevanceLevelType = Literal["HIGH", "LOW", "MEDIUM"]
SearchContentPaginatorName = Literal["search_content"]
SearchQuickResponsesPaginatorName = Literal["search_quick_responses"]
SearchSessionsPaginatorName = Literal["search_sessions"]
