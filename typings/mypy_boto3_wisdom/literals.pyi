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
    "FilterFieldType",
    "FilterOperatorType",
    "KnowledgeBaseStatusType",
    "KnowledgeBaseTypeType",
    "ListAssistantAssociationsPaginatorName",
    "ListAssistantsPaginatorName",
    "ListContentsPaginatorName",
    "ListKnowledgeBasesPaginatorName",
    "QueryAssistantPaginatorName",
    "RelevanceLevelType",
    "SearchContentPaginatorName",
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
FilterFieldType = Literal["NAME"]
FilterOperatorType = Literal["EQUALS"]
KnowledgeBaseStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
]
KnowledgeBaseTypeType = Literal["CUSTOM", "EXTERNAL"]
ListAssistantAssociationsPaginatorName = Literal["list_assistant_associations"]
ListAssistantsPaginatorName = Literal["list_assistants"]
ListContentsPaginatorName = Literal["list_contents"]
ListKnowledgeBasesPaginatorName = Literal["list_knowledge_bases"]
QueryAssistantPaginatorName = Literal["query_assistant"]
RelevanceLevelType = Literal["HIGH", "LOW", "MEDIUM"]
SearchContentPaginatorName = Literal["search_content"]
SearchSessionsPaginatorName = Literal["search_sessions"]
