"""
Type annotations for qbusiness service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/literals.html)

Usage::

    ```python
    from mypy_boto3_qbusiness.literals import APISchemaTypeType

    data: APISchemaTypeType = "OPEN_API_V3"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "APISchemaTypeType",
    "ActionPayloadFieldTypeType",
    "ApplicationStatusType",
    "AttachmentStatusType",
    "AttachmentsControlModeType",
    "AttributeTypeType",
    "AttributeValueOperatorType",
    "ChatModeType",
    "ContentTypeType",
    "CreatorModeControlType",
    "DataSourceStatusType",
    "DataSourceSyncJobStatusType",
    "DocumentAttributeBoostingLevelType",
    "DocumentContentOperatorType",
    "DocumentEnrichmentConditionOperatorType",
    "DocumentStatusType",
    "ErrorCodeType",
    "GetChatControlsConfigurationPaginatorName",
    "GroupStatusType",
    "IndexStatusType",
    "IndexTypeType",
    "ListApplicationsPaginatorName",
    "ListConversationsPaginatorName",
    "ListDataSourceSyncJobsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListDocumentsPaginatorName",
    "ListGroupsPaginatorName",
    "ListIndicesPaginatorName",
    "ListMessagesPaginatorName",
    "ListPluginsPaginatorName",
    "ListRetrieversPaginatorName",
    "ListWebExperiencesPaginatorName",
    "MemberRelationType",
    "MembershipTypeType",
    "MessageTypeType",
    "MessageUsefulnessReasonType",
    "MessageUsefulnessType",
    "NumberAttributeBoostingTypeType",
    "PluginBuildStatusType",
    "PluginStateType",
    "PluginTypeType",
    "ReadAccessTypeType",
    "ResponseScopeType",
    "RetrieverStatusType",
    "RetrieverTypeType",
    "RuleTypeType",
    "StatusType",
    "StringAttributeValueBoostingLevelType",
    "WebExperienceSamplePromptsControlModeType",
    "WebExperienceStatusType",
)

APISchemaTypeType = Literal["OPEN_API_V3"]
ActionPayloadFieldTypeType = Literal["ARRAY", "BOOLEAN", "NUMBER", "STRING"]
ApplicationStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
AttachmentStatusType = Literal["FAILED", "SUCCEEDED"]
AttachmentsControlModeType = Literal["DISABLED", "ENABLED"]
AttributeTypeType = Literal["DATE", "NUMBER", "STRING", "STRING_LIST"]
AttributeValueOperatorType = Literal["DELETE"]
ChatModeType = Literal["CREATOR_MODE", "PLUGIN_MODE", "RETRIEVAL_MODE"]
ContentTypeType = Literal[
    "CSV",
    "HTML",
    "JSON",
    "MD",
    "MS_EXCEL",
    "MS_WORD",
    "PDF",
    "PLAIN_TEXT",
    "PPT",
    "RTF",
    "XML",
    "XSLT",
]
CreatorModeControlType = Literal["DISABLED", "ENABLED"]
DataSourceStatusType = Literal[
    "ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING_CREATION", "UPDATING"
]
DataSourceSyncJobStatusType = Literal[
    "ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"
]
DocumentAttributeBoostingLevelType = Literal["HIGH", "LOW", "MEDIUM", "NONE", "VERY_HIGH"]
DocumentContentOperatorType = Literal["DELETE"]
DocumentEnrichmentConditionOperatorType = Literal[
    "BEGINS_WITH",
    "CONTAINS",
    "EQUALS",
    "EXISTS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "NOT_CONTAINS",
    "NOT_EQUALS",
    "NOT_EXISTS",
]
DocumentStatusType = Literal[
    "DELETED",
    "DELETING",
    "DOCUMENT_FAILED_TO_INDEX",
    "FAILED",
    "INDEXED",
    "PROCESSING",
    "RECEIVED",
    "UPDATED",
]
ErrorCodeType = Literal["InternalError", "InvalidRequest", "ResourceInactive", "ResourceNotFound"]
GetChatControlsConfigurationPaginatorName = Literal["get_chat_controls_configuration"]
GroupStatusType = Literal["DELETED", "DELETING", "FAILED", "PROCESSING", "SUCCEEDED"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
IndexTypeType = Literal["ENTERPRISE", "STARTER"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListConversationsPaginatorName = Literal["list_conversations"]
ListDataSourceSyncJobsPaginatorName = Literal["list_data_source_sync_jobs"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListDocumentsPaginatorName = Literal["list_documents"]
ListGroupsPaginatorName = Literal["list_groups"]
ListIndicesPaginatorName = Literal["list_indices"]
ListMessagesPaginatorName = Literal["list_messages"]
ListPluginsPaginatorName = Literal["list_plugins"]
ListRetrieversPaginatorName = Literal["list_retrievers"]
ListWebExperiencesPaginatorName = Literal["list_web_experiences"]
MemberRelationType = Literal["AND", "OR"]
MembershipTypeType = Literal["DATASOURCE", "INDEX"]
MessageTypeType = Literal["SYSTEM", "USER"]
MessageUsefulnessReasonType = Literal[
    "COMPLETE",
    "FACTUALLY_CORRECT",
    "HARMFUL_OR_UNSAFE",
    "HELPFUL",
    "INCORRECT_OR_MISSING_SOURCES",
    "NOT_BASED_ON_DOCUMENTS",
    "NOT_COMPLETE",
    "NOT_CONCISE",
    "NOT_FACTUALLY_CORRECT",
    "NOT_HELPFUL",
    "OTHER",
    "RELEVANT_SOURCES",
]
MessageUsefulnessType = Literal["NOT_USEFUL", "USEFUL"]
NumberAttributeBoostingTypeType = Literal["PRIORITIZE_LARGER_VALUES", "PRIORITIZE_SMALLER_VALUES"]
PluginBuildStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
PluginStateType = Literal["DISABLED", "ENABLED"]
PluginTypeType = Literal["CUSTOM", "JIRA", "SALESFORCE", "SERVICE_NOW", "ZENDESK"]
ReadAccessTypeType = Literal["ALLOW", "DENY"]
ResponseScopeType = Literal["ENTERPRISE_CONTENT_ONLY", "EXTENDED_KNOWLEDGE_ENABLED"]
RetrieverStatusType = Literal["ACTIVE", "CREATING", "FAILED"]
RetrieverTypeType = Literal["KENDRA_INDEX", "NATIVE_INDEX"]
RuleTypeType = Literal["CONTENT_BLOCKER_RULE", "CONTENT_RETRIEVAL_RULE"]
StatusType = Literal["DISABLED", "ENABLED"]
StringAttributeValueBoostingLevelType = Literal["HIGH", "LOW", "MEDIUM", "VERY_HIGH"]
WebExperienceSamplePromptsControlModeType = Literal["DISABLED", "ENABLED"]
WebExperienceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING_AUTH_CONFIG"]
