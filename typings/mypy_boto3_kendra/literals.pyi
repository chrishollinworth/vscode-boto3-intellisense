"""
Type annotations for kendra service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/literals.html)

Usage::

    ```python
    from mypy_boto3_kendra.literals import AdditionalResultAttributeValueTypeType

    data: AdditionalResultAttributeValueTypeType = "TEXT_WITH_HIGHLIGHTS_VALUE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdditionalResultAttributeValueTypeType",
    "AlfrescoEntityType",
    "ConditionOperatorType",
    "ConfluenceAttachmentFieldNameType",
    "ConfluenceAuthenticationTypeType",
    "ConfluenceBlogFieldNameType",
    "ConfluencePageFieldNameType",
    "ConfluenceSpaceFieldNameType",
    "ConfluenceVersionType",
    "ContentTypeType",
    "DataSourceStatusType",
    "DataSourceSyncJobStatusType",
    "DataSourceTypeType",
    "DatabaseEngineTypeType",
    "DocumentAttributeValueTypeType",
    "DocumentStatusType",
    "EndpointTypeType",
    "EntityTypeType",
    "ErrorCodeType",
    "ExperienceStatusType",
    "FaqFileFormatType",
    "FaqStatusType",
    "FsxFileSystemTypeType",
    "HighlightTypeType",
    "IndexEditionType",
    "IndexStatusType",
    "IntervalType",
    "IssueSubEntityType",
    "KeyLocationType",
    "MetricTypeType",
    "ModeType",
    "OrderType",
    "PersonaType",
    "PrincipalMappingStatusType",
    "PrincipalTypeType",
    "QueryIdentifiersEnclosingOptionType",
    "QueryResultFormatType",
    "QueryResultTypeType",
    "QuerySuggestionsBlockListStatusType",
    "QuerySuggestionsStatusType",
    "ReadAccessTypeType",
    "RelevanceTypeType",
    "SalesforceChatterFeedIncludeFilterTypeType",
    "SalesforceKnowledgeArticleStateType",
    "SalesforceStandardObjectNameType",
    "ScoreConfidenceType",
    "ServiceNowAuthenticationTypeType",
    "ServiceNowBuildVersionTypeType",
    "SharePointOnlineAuthenticationTypeType",
    "SharePointVersionType",
    "SlackEntityType",
    "SortOrderType",
    "ThesaurusStatusType",
    "TypeType",
    "UserContextPolicyType",
    "UserGroupResolutionModeType",
    "WarningCodeType",
    "WebCrawlerModeType",
)

AdditionalResultAttributeValueTypeType = Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
AlfrescoEntityType = Literal["blog", "documentLibrary", "wiki"]
ConditionOperatorType = Literal[
    "BeginsWith",
    "Contains",
    "Equals",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEquals",
    "LessThan",
    "LessThanOrEquals",
    "NotContains",
    "NotEquals",
    "NotExists",
]
ConfluenceAttachmentFieldNameType = Literal[
    "AUTHOR",
    "CONTENT_TYPE",
    "CREATED_DATE",
    "DISPLAY_URL",
    "FILE_SIZE",
    "ITEM_TYPE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceAuthenticationTypeType = Literal["HTTP_BASIC", "PAT"]
ConfluenceBlogFieldNameType = Literal[
    "AUTHOR",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "PUBLISH_DATE",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluencePageFieldNameType = Literal[
    "AUTHOR",
    "CONTENT_STATUS",
    "CREATED_DATE",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "MODIFIED_DATE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceSpaceFieldNameType = Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"]
ConfluenceVersionType = Literal["CLOUD", "SERVER"]
ContentTypeType = Literal["HTML", "MS_WORD", "PDF", "PLAIN_TEXT", "PPT"]
DataSourceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DataSourceSyncJobStatusType = Literal[
    "ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"
]
DataSourceTypeType = Literal[
    "ALFRESCO",
    "BOX",
    "CONFLUENCE",
    "CUSTOM",
    "DATABASE",
    "FSX",
    "GITHUB",
    "GOOGLEDRIVE",
    "JIRA",
    "ONEDRIVE",
    "QUIP",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SHAREPOINT",
    "SLACK",
    "TEMPLATE",
    "WEBCRAWLER",
    "WORKDOCS",
]
DatabaseEngineTypeType = Literal[
    "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
]
DocumentAttributeValueTypeType = Literal[
    "DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"
]
DocumentStatusType = Literal[
    "FAILED", "INDEXED", "NOT_FOUND", "PROCESSING", "UPDATED", "UPDATE_FAILED"
]
EndpointTypeType = Literal["HOME"]
EntityTypeType = Literal["GROUP", "USER"]
ErrorCodeType = Literal["InternalError", "InvalidRequest"]
ExperienceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
FaqFileFormatType = Literal["CSV", "CSV_WITH_HEADER", "JSON"]
FaqStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
FsxFileSystemTypeType = Literal["WINDOWS"]
HighlightTypeType = Literal["STANDARD", "THESAURUS_SYNONYM"]
IndexEditionType = Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"]
IntervalType = Literal[
    "ONE_MONTH_AGO", "ONE_WEEK_AGO", "THIS_MONTH", "THIS_WEEK", "TWO_MONTHS_AGO", "TWO_WEEKS_AGO"
]
IssueSubEntityType = Literal["ATTACHMENTS", "COMMENTS", "WORKLOGS"]
KeyLocationType = Literal["SECRET_MANAGER", "URL"]
MetricTypeType = Literal[
    "AGG_QUERY_DOC_METRICS",
    "DOCS_BY_CLICK_COUNT",
    "QUERIES_BY_COUNT",
    "QUERIES_BY_ZERO_CLICK_RATE",
    "QUERIES_BY_ZERO_RESULT_RATE",
    "TREND_QUERY_DOC_METRICS",
]
ModeType = Literal["ENABLED", "LEARN_ONLY"]
OrderType = Literal["ASCENDING", "DESCENDING"]
PersonaType = Literal["OWNER", "VIEWER"]
PrincipalMappingStatusType = Literal["DELETED", "DELETING", "FAILED", "PROCESSING", "SUCCEEDED"]
PrincipalTypeType = Literal["GROUP", "USER"]
QueryIdentifiersEnclosingOptionType = Literal["DOUBLE_QUOTES", "NONE"]
QueryResultFormatType = Literal["TABLE", "TEXT"]
QueryResultTypeType = Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]
QuerySuggestionsBlockListStatusType = Literal[
    "ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"
]
QuerySuggestionsStatusType = Literal["ACTIVE", "UPDATING"]
ReadAccessTypeType = Literal["ALLOW", "DENY"]
RelevanceTypeType = Literal["NOT_RELEVANT", "RELEVANT"]
SalesforceChatterFeedIncludeFilterTypeType = Literal["ACTIVE_USER", "STANDARD_USER"]
SalesforceKnowledgeArticleStateType = Literal["ARCHIVED", "DRAFT", "PUBLISHED"]
SalesforceStandardObjectNameType = Literal[
    "ACCOUNT",
    "CAMPAIGN",
    "CASE",
    "CONTACT",
    "CONTRACT",
    "DOCUMENT",
    "GROUP",
    "IDEA",
    "LEAD",
    "OPPORTUNITY",
    "PARTNER",
    "PRICEBOOK",
    "PRODUCT",
    "PROFILE",
    "SOLUTION",
    "TASK",
    "USER",
]
ScoreConfidenceType = Literal["HIGH", "LOW", "MEDIUM", "NOT_AVAILABLE", "VERY_HIGH"]
ServiceNowAuthenticationTypeType = Literal["HTTP_BASIC", "OAUTH2"]
ServiceNowBuildVersionTypeType = Literal["LONDON", "OTHERS"]
SharePointOnlineAuthenticationTypeType = Literal["HTTP_BASIC", "OAUTH2"]
SharePointVersionType = Literal[
    "SHAREPOINT_2013", "SHAREPOINT_2016", "SHAREPOINT_2019", "SHAREPOINT_ONLINE"
]
SlackEntityType = Literal["DIRECT_MESSAGE", "GROUP_MESSAGE", "PRIVATE_CHANNEL", "PUBLIC_CHANNEL"]
SortOrderType = Literal["ASC", "DESC"]
ThesaurusStatusType = Literal[
    "ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"
]
TypeType = Literal["ON_PREMISE", "SAAS"]
UserContextPolicyType = Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]
UserGroupResolutionModeType = Literal["AWS_SSO", "NONE"]
WarningCodeType = Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]
WebCrawlerModeType = Literal["EVERYTHING", "HOST_ONLY", "SUBDOMAINS"]
