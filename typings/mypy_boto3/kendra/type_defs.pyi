"""
Type annotations for kendra service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlConfigurationSummaryTypeDef

    data: AccessControlConfigurationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AlfrescoEntityType,
    ConditionOperatorType,
    ConfluenceAttachmentFieldNameType,
    ConfluenceAuthenticationTypeType,
    ConfluenceBlogFieldNameType,
    ConfluencePageFieldNameType,
    ConfluenceSpaceFieldNameType,
    ConfluenceVersionType,
    ContentTypeType,
    DatabaseEngineTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    DocumentAttributeValueTypeType,
    DocumentStatusType,
    EntityTypeType,
    ErrorCodeType,
    ExperienceStatusType,
    FaqFileFormatType,
    FaqStatusType,
    HighlightTypeType,
    IndexEditionType,
    IndexStatusType,
    IntervalType,
    IssueSubEntityType,
    KeyLocationType,
    MetricTypeType,
    ModeType,
    OrderType,
    PersonaType,
    PrincipalMappingStatusType,
    PrincipalTypeType,
    QueryIdentifiersEnclosingOptionType,
    QueryResultFormatType,
    QueryResultTypeType,
    QuerySuggestionsBlockListStatusType,
    QuerySuggestionsStatusType,
    ReadAccessTypeType,
    RelevanceTypeType,
    SalesforceChatterFeedIncludeFilterTypeType,
    SalesforceKnowledgeArticleStateType,
    SalesforceStandardObjectNameType,
    ScoreConfidenceType,
    ServiceNowAuthenticationTypeType,
    ServiceNowBuildVersionTypeType,
    SharePointOnlineAuthenticationTypeType,
    SharePointVersionType,
    SlackEntityType,
    SortOrderType,
    ThesaurusStatusType,
    TypeType,
    UserContextPolicyType,
    UserGroupResolutionModeType,
    WebCrawlerModeType,
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
    "AccessControlConfigurationSummaryTypeDef",
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "AdditionalResultAttributeTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "AlfrescoConfigurationTypeDef",
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    "AssociateEntitiesToExperienceResponseTypeDef",
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    "AssociatePersonasToEntitiesResponseTypeDef",
    "AttributeFilterTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BasicAuthenticationConfigurationTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchGetDocumentStatusRequestRequestTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "BatchGetDocumentStatusResponseTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "BoxConfigurationTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClearQuerySuggestionsRequestRequestTypeDef",
    "ClickFeedbackTypeDef",
    "ColumnConfigurationTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ConfluenceConfigurationTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "ContentSourceConfigurationTypeDef",
    "CorrectionTypeDef",
    "CreateAccessControlConfigurationRequestRequestTypeDef",
    "CreateAccessControlConfigurationResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateExperienceRequestRequestTypeDef",
    "CreateExperienceResponseTypeDef",
    "CreateFaqRequestRequestTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    "CreateThesaurusRequestRequestTypeDef",
    "CreateThesaurusResponseTypeDef",
    "CustomDocumentEnrichmentConfigurationTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceGroupTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteExperienceRequestRequestTypeDef",
    "DeleteFaqRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePrincipalMappingRequestRequestTypeDef",
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    "DeleteThesaurusRequestRequestTypeDef",
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    "DescribeAccessControlConfigurationResponseTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeExperienceRequestRequestTypeDef",
    "DescribeExperienceResponseTypeDef",
    "DescribeFaqRequestRequestTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribePrincipalMappingRequestRequestTypeDef",
    "DescribePrincipalMappingResponseTypeDef",
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    "DescribeThesaurusRequestRequestTypeDef",
    "DescribeThesaurusResponseTypeDef",
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentInfoTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "DocumentTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "EntityConfigurationTypeDef",
    "EntityDisplayDataTypeDef",
    "EntityPersonaConfigurationTypeDef",
    "ExperienceConfigurationTypeDef",
    "ExperienceEndpointTypeDef",
    "ExperienceEntitiesSummaryTypeDef",
    "ExperiencesSummaryTypeDef",
    "FacetResultTypeDef",
    "FacetTypeDef",
    "FailedEntityTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "FsxConfigurationTypeDef",
    "GetQuerySuggestionsRequestRequestTypeDef",
    "GetQuerySuggestionsResponseTypeDef",
    "GetSnapshotsRequestRequestTypeDef",
    "GetSnapshotsResponseTypeDef",
    "GitHubConfigurationTypeDef",
    "GitHubDocumentCrawlPropertiesTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "GroupMembersTypeDef",
    "GroupOrderingIdSummaryTypeDef",
    "GroupSummaryTypeDef",
    "HierarchicalPrincipalTypeDef",
    "HighlightTypeDef",
    "HookConfigurationTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    "JiraConfigurationTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListAccessControlConfigurationsRequestRequestTypeDef",
    "ListAccessControlConfigurationsResponseTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListEntityPersonasRequestRequestTypeDef",
    "ListEntityPersonasResponseTypeDef",
    "ListExperienceEntitiesRequestRequestTypeDef",
    "ListExperienceEntitiesResponseTypeDef",
    "ListExperiencesRequestRequestTypeDef",
    "ListExperiencesResponseTypeDef",
    "ListFaqsRequestRequestTypeDef",
    "ListFaqsResponseTypeDef",
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListIndicesResponseTypeDef",
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThesauriRequestRequestTypeDef",
    "ListThesauriResponseTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "OnPremiseConfigurationTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PersonasSummaryTypeDef",
    "PrincipalTypeDef",
    "ProxyConfigurationTypeDef",
    "PutPrincipalMappingRequestRequestTypeDef",
    "QueryRequestRequestTypeDef",
    "QueryResultItemTypeDef",
    "QueryResultTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "QuipConfigurationTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3PathTypeDef",
    "SaaSConfigurationTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "SearchTypeDef",
    "SeedUrlConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SiteMapsConfigurationTypeDef",
    "SlackConfigurationTypeDef",
    "SortingConfigurationTypeDef",
    "SpellCorrectedQueryTypeDef",
    "SpellCorrectionConfigurationTypeDef",
    "SqlConfigurationTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "StatusTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "SuggestionHighlightTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "SuggestionTypeDef",
    "SuggestionValueTypeDef",
    "TableCellTypeDef",
    "TableExcerptTypeDef",
    "TableRowTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TemplateConfigurationTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "ThesaurusSummaryTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessControlConfigurationRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateExperienceRequestRequestTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    "UpdateThesaurusRequestRequestTypeDef",
    "UrlsTypeDef",
    "UserContextTypeDef",
    "UserGroupResolutionConfigurationTypeDef",
    "UserIdentityConfigurationTypeDef",
    "UserTokenConfigurationTypeDef",
    "WarningTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "WorkDocsConfigurationTypeDef",
)

AccessControlConfigurationSummaryTypeDef = TypedDict(
    "AccessControlConfigurationSummaryTypeDef",
    {
        "Id": str,
    },
)

AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef",
    {
        "KeyPath": str,
    },
    total=False,
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "AllowedGroupsColumnName": str,
    },
)

AdditionalResultAttributeTypeDef = TypedDict(
    "AdditionalResultAttributeTypeDef",
    {
        "Key": str,
        "ValueType": Literal["TEXT_WITH_HIGHLIGHTS_VALUE"],
        "Value": "AdditionalResultAttributeValueTypeDef",
    },
)

AdditionalResultAttributeValueTypeDef = TypedDict(
    "AdditionalResultAttributeValueTypeDef",
    {
        "TextWithHighlightsValue": "TextWithHighlightsTypeDef",
    },
    total=False,
)

_RequiredAlfrescoConfigurationTypeDef = TypedDict(
    "_RequiredAlfrescoConfigurationTypeDef",
    {
        "SiteUrl": str,
        "SiteId": str,
        "SecretArn": str,
        "SslCertificateS3Path": "S3PathTypeDef",
    },
)
_OptionalAlfrescoConfigurationTypeDef = TypedDict(
    "_OptionalAlfrescoConfigurationTypeDef",
    {
        "CrawlSystemFolders": bool,
        "CrawlComments": bool,
        "EntityFilter": List[AlfrescoEntityType],
        "DocumentLibraryFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "BlogFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "WikiFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
    },
    total=False,
)

class AlfrescoConfigurationTypeDef(
    _RequiredAlfrescoConfigurationTypeDef, _OptionalAlfrescoConfigurationTypeDef
):
    pass

AssociateEntitiesToExperienceRequestRequestTypeDef = TypedDict(
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": List["EntityConfigurationTypeDef"],
    },
)

AssociateEntitiesToExperienceResponseTypeDef = TypedDict(
    "AssociateEntitiesToExperienceResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePersonasToEntitiesRequestRequestTypeDef = TypedDict(
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Personas": List["EntityPersonaConfigurationTypeDef"],
    },
)

AssociatePersonasToEntitiesResponseTypeDef = TypedDict(
    "AssociatePersonasToEntitiesResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "AndAllFilters": List[Dict[str, Any]],
        "OrAllFilters": List[Dict[str, Any]],
        "NotFilter": Dict[str, Any],
        "EqualsTo": "DocumentAttributeTypeDef",
        "ContainsAll": "DocumentAttributeTypeDef",
        "ContainsAny": "DocumentAttributeTypeDef",
        "GreaterThan": "DocumentAttributeTypeDef",
        "GreaterThanOrEquals": "DocumentAttributeTypeDef",
        "LessThan": "DocumentAttributeTypeDef",
        "LessThanOrEquals": "DocumentAttributeTypeDef",
    },
    total=False,
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "BasicAuthentication": List["BasicAuthenticationConfigurationTypeDef"],
    },
    total=False,
)

BasicAuthenticationConfigurationTypeDef = TypedDict(
    "BasicAuthenticationConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": str,
    },
)

_RequiredBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentIdList": List[str],
    },
)
_OptionalBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteDocumentRequestRequestTypeDef",
    {
        "DataSourceSyncJobMetricTarget": "DataSourceSyncJobMetricTargetTypeDef",
    },
    total=False,
)

class BatchDeleteDocumentRequestRequestTypeDef(
    _RequiredBatchDeleteDocumentRequestRequestTypeDef,
    _OptionalBatchDeleteDocumentRequestRequestTypeDef,
):
    pass

BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchDeleteDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDocumentStatusRequestRequestTypeDef = TypedDict(
    "BatchGetDocumentStatusRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentInfoList": List["DocumentInfoTypeDef"],
    },
)

BatchGetDocumentStatusResponseErrorTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseErrorTypeDef",
    {
        "DocumentId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchGetDocumentStatusResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseTypeDef",
    {
        "Errors": List["BatchGetDocumentStatusResponseErrorTypeDef"],
        "DocumentStatusList": List["StatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchPutDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "Documents": List["DocumentTypeDef"],
    },
)
_OptionalBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchPutDocumentRequestRequestTypeDef",
    {
        "RoleArn": str,
        "CustomDocumentEnrichmentConfiguration": "CustomDocumentEnrichmentConfigurationTypeDef",
    },
    total=False,
)

class BatchPutDocumentRequestRequestTypeDef(
    _RequiredBatchPutDocumentRequestRequestTypeDef, _OptionalBatchPutDocumentRequestRequestTypeDef
):
    pass

BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchPutDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBoxConfigurationTypeDef = TypedDict(
    "_RequiredBoxConfigurationTypeDef",
    {
        "EnterpriseId": str,
        "SecretArn": str,
    },
)
_OptionalBoxConfigurationTypeDef = TypedDict(
    "_OptionalBoxConfigurationTypeDef",
    {
        "UseChangeLog": bool,
        "CrawlComments": bool,
        "CrawlTasks": bool,
        "CrawlWebLinks": bool,
        "FileFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "TaskFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "CommentFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "WebLinkFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
    },
    total=False,
)

class BoxConfigurationTypeDef(_RequiredBoxConfigurationTypeDef, _OptionalBoxConfigurationTypeDef):
    pass

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)

ClearQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "ClearQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": Union[datetime, str],
    },
)

_RequiredColumnConfigurationTypeDef = TypedDict(
    "_RequiredColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": List[str],
    },
)
_OptionalColumnConfigurationTypeDef = TypedDict(
    "_OptionalColumnConfigurationTypeDef",
    {
        "DocumentTitleColumnName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class ColumnConfigurationTypeDef(
    _RequiredColumnConfigurationTypeDef, _OptionalColumnConfigurationTypeDef
):
    pass

ConfluenceAttachmentConfigurationTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "AttachmentFieldMappings": List["ConfluenceAttachmentToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceAttachmentToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceAttachmentFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {
        "BlogFieldMappings": List["ConfluenceBlogToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceBlogFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

_RequiredConfluenceConfigurationTypeDef = TypedDict(
    "_RequiredConfluenceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
    },
)
_OptionalConfluenceConfigurationTypeDef = TypedDict(
    "_OptionalConfluenceConfigurationTypeDef",
    {
        "SpaceConfiguration": "ConfluenceSpaceConfigurationTypeDef",
        "PageConfiguration": "ConfluencePageConfigurationTypeDef",
        "BlogConfiguration": "ConfluenceBlogConfigurationTypeDef",
        "AttachmentConfiguration": "ConfluenceAttachmentConfigurationTypeDef",
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "ProxyConfiguration": "ProxyConfigurationTypeDef",
        "AuthenticationType": ConfluenceAuthenticationTypeType,
    },
    total=False,
)

class ConfluenceConfigurationTypeDef(
    _RequiredConfluenceConfigurationTypeDef, _OptionalConfluenceConfigurationTypeDef
):
    pass

ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {
        "PageFieldMappings": List["ConfluencePageToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluencePageFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceSpaceConfigurationTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationTypeDef",
    {
        "CrawlPersonalSpaces": bool,
        "CrawlArchivedSpaces": bool,
        "IncludeSpaces": List[str],
        "ExcludeSpaces": List[str],
        "SpaceFieldMappings": List["ConfluenceSpaceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceSpaceToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceSpaceFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConnectionConfigurationTypeDef = TypedDict(
    "ConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
)

ContentSourceConfigurationTypeDef = TypedDict(
    "ContentSourceConfigurationTypeDef",
    {
        "DataSourceIds": List[str],
        "FaqIds": List[str],
        "DirectPutContent": bool,
    },
    total=False,
)

CorrectionTypeDef = TypedDict(
    "CorrectionTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
        "Term": str,
        "CorrectedTerm": str,
    },
    total=False,
)

_RequiredCreateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
    },
)
_OptionalCreateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessControlConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "AccessControlList": List["PrincipalTypeDef"],
        "HierarchicalAccessControlList": List["HierarchicalPrincipalTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateAccessControlConfigurationRequestRequestTypeDef(
    _RequiredCreateAccessControlConfigurationRequestRequestTypeDef,
    _OptionalCreateAccessControlConfigurationRequestRequestTypeDef,
):
    pass

CreateAccessControlConfigurationResponseTypeDef = TypedDict(
    "CreateAccessControlConfigurationResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "Configuration": "DataSourceConfigurationTypeDef",
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": "CustomDocumentEnrichmentConfigurationTypeDef",
    },
    total=False,
)

class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
    },
)
_OptionalCreateExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperienceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Configuration": "ExperienceConfigurationTypeDef",
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)

class CreateExperienceRequestRequestTypeDef(
    _RequiredCreateExperienceRequestRequestTypeDef, _OptionalCreateExperienceRequestRequestTypeDef
):
    pass

CreateExperienceResponseTypeDef = TypedDict(
    "CreateExperienceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFaqRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFaqRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "S3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateFaqRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFaqRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "FileFormat": FaqFileFormatType,
        "ClientToken": str,
        "LanguageCode": str,
    },
    total=False,
)

class CreateFaqRequestRequestTypeDef(
    _RequiredCreateFaqRequestRequestTypeDef, _OptionalCreateFaqRequestRequestTypeDef
):
    pass

CreateFaqResponseTypeDef = TypedDict(
    "CreateFaqResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalCreateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestRequestTypeDef",
    {
        "Edition": IndexEditionType,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Description": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": "UserGroupResolutionConfigurationTypeDef",
    },
    total=False,
)

class CreateIndexRequestRequestTypeDef(
    _RequiredCreateIndexRequestRequestTypeDef, _OptionalCreateIndexRequestRequestTypeDef
):
    pass

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "SourceS3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateQuerySuggestionsBlockListRequestRequestTypeDef(
    _RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef,
    _OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef,
):
    pass

CreateQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThesaurusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThesaurusRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
    },
)
_OptionalCreateThesaurusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThesaurusRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateThesaurusRequestRequestTypeDef(
    _RequiredCreateThesaurusRequestRequestTypeDef, _OptionalCreateThesaurusRequestRequestTypeDef
):
    pass

CreateThesaurusResponseTypeDef = TypedDict(
    "CreateThesaurusResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationTypeDef",
    {
        "InlineConfigurations": List["InlineCustomDocumentEnrichmentConfigurationTypeDef"],
        "PreExtractionHookConfiguration": "HookConfigurationTypeDef",
        "PostExtractionHookConfiguration": "HookConfigurationTypeDef",
        "RoleArn": str,
    },
    total=False,
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "S3Configuration": "S3DataSourceConfigurationTypeDef",
        "SharePointConfiguration": "SharePointConfigurationTypeDef",
        "DatabaseConfiguration": "DatabaseConfigurationTypeDef",
        "SalesforceConfiguration": "SalesforceConfigurationTypeDef",
        "OneDriveConfiguration": "OneDriveConfigurationTypeDef",
        "ServiceNowConfiguration": "ServiceNowConfigurationTypeDef",
        "ConfluenceConfiguration": "ConfluenceConfigurationTypeDef",
        "GoogleDriveConfiguration": "GoogleDriveConfigurationTypeDef",
        "WebCrawlerConfiguration": "WebCrawlerConfigurationTypeDef",
        "WorkDocsConfiguration": "WorkDocsConfigurationTypeDef",
        "FsxConfiguration": "FsxConfigurationTypeDef",
        "SlackConfiguration": "SlackConfigurationTypeDef",
        "BoxConfiguration": "BoxConfigurationTypeDef",
        "QuipConfiguration": "QuipConfigurationTypeDef",
        "JiraConfiguration": "JiraConfigurationTypeDef",
        "GitHubConfiguration": "GitHubConfigurationTypeDef",
        "AlfrescoConfiguration": "AlfrescoConfigurationTypeDef",
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
    },
    total=False,
)

DataSourceGroupTypeDef = TypedDict(
    "DataSourceGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": str,
    },
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": DataSourceTypeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": DataSourceStatusType,
        "LanguageCode": str,
    },
    total=False,
)

_RequiredDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_RequiredDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_OptionalDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceSyncJobId": str,
    },
    total=False,
)

class DataSourceSyncJobMetricTargetTypeDef(
    _RequiredDataSourceSyncJobMetricTargetTypeDef, _OptionalDataSourceSyncJobMetricTargetTypeDef
):
    pass

DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "DocumentsAdded": str,
        "DocumentsModified": str,
        "DocumentsDeleted": str,
        "DocumentsFailed": str,
        "DocumentsScanned": str,
    },
    total=False,
)

DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "ExecutionId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": DataSourceSyncJobStatusType,
        "ErrorMessage": str,
        "ErrorCode": ErrorCodeType,
        "DataSourceErrorCode": str,
        "Metrics": "DataSourceSyncJobMetricsTypeDef",
    },
    total=False,
)

_RequiredDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_RequiredDataSourceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": str,
        "IndexFieldName": str,
    },
)
_OptionalDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_OptionalDataSourceToIndexFieldMappingTypeDef",
    {
        "DateFieldFormat": str,
    },
    total=False,
)

class DataSourceToIndexFieldMappingTypeDef(
    _RequiredDataSourceToIndexFieldMappingTypeDef, _OptionalDataSourceToIndexFieldMappingTypeDef
):
    pass

DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

_RequiredDatabaseConfigurationTypeDef = TypedDict(
    "_RequiredDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": "ConnectionConfigurationTypeDef",
        "ColumnConfiguration": "ColumnConfigurationTypeDef",
    },
)
_OptionalDatabaseConfigurationTypeDef = TypedDict(
    "_OptionalDatabaseConfigurationTypeDef",
    {
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "AclConfiguration": "AclConfigurationTypeDef",
        "SqlConfiguration": "SqlConfigurationTypeDef",
    },
    total=False,
)

class DatabaseConfigurationTypeDef(
    _RequiredDatabaseConfigurationTypeDef, _OptionalDatabaseConfigurationTypeDef
):
    pass

DeleteAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteExperienceRequestRequestTypeDef = TypedDict(
    "DeleteExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteFaqRequestRequestTypeDef = TypedDict(
    "DeleteFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredDeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
    },
)
_OptionalDeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "OrderingId": int,
    },
    total=False,
)

class DeletePrincipalMappingRequestRequestTypeDef(
    _RequiredDeletePrincipalMappingRequestRequestTypeDef,
    _OptionalDeletePrincipalMappingRequestRequestTypeDef,
):
    pass

DeleteQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteThesaurusRequestRequestTypeDef = TypedDict(
    "DeleteThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeAccessControlConfigurationResponseTypeDef = TypedDict(
    "DescribeAccessControlConfigurationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "ErrorMessage": str,
        "AccessControlList": List["PrincipalTypeDef"],
        "HierarchicalAccessControlList": List["HierarchicalPrincipalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Configuration": "DataSourceConfigurationTypeDef",
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatusType,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": "CustomDocumentEnrichmentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExperienceRequestRequestTypeDef = TypedDict(
    "DescribeExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeExperienceResponseTypeDef = TypedDict(
    "DescribeExperienceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Endpoints": List["ExperienceEndpointTypeDef"],
        "Configuration": "ExperienceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": ExperienceStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFaqRequestRequestTypeDef = TypedDict(
    "DescribeFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeFaqResponseTypeDef = TypedDict(
    "DescribeFaqResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": "S3PathTypeDef",
        "Status": FaqStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Status": IndexStatusType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List["DocumentMetadataConfigurationTypeDef"],
        "IndexStatistics": "IndexStatisticsTypeDef",
        "ErrorMessage": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": "UserGroupResolutionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
    },
)
_OptionalDescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)

class DescribePrincipalMappingRequestRequestTypeDef(
    _RequiredDescribePrincipalMappingRequestRequestTypeDef,
    _OptionalDescribePrincipalMappingRequestRequestTypeDef,
):
    pass

DescribePrincipalMappingResponseTypeDef = TypedDict(
    "DescribePrincipalMappingResponseTypeDef",
    {
        "IndexId": str,
        "DataSourceId": str,
        "GroupId": str,
        "GroupOrderingIdSummaries": List["GroupOrderingIdSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "SourceS3Path": "S3PathTypeDef",
        "ItemCount": int,
        "FileSizeBytes": int,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

DescribeQuerySuggestionsConfigResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    {
        "Mode": ModeType,
        "Status": QuerySuggestionsStatusType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "LastSuggestionsBuildTime": datetime,
        "LastClearTime": datetime,
        "TotalSuggestionsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThesaurusRequestRequestTypeDef = TypedDict(
    "DescribeThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeThesaurusResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "Status": ThesaurusStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
        "FileSizeBytes": int,
        "TermCount": int,
        "SynonymRuleCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEntitiesFromExperienceRequestRequestTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": List["EntityConfigurationTypeDef"],
    },
)

DisassociateEntitiesFromExperienceResponseTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePersonasFromEntitiesRequestRequestTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityIds": List[str],
    },
)

DisassociatePersonasFromEntitiesResponseTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentAttributeConditionTypeDef = TypedDict(
    "_RequiredDocumentAttributeConditionTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
    },
)
_OptionalDocumentAttributeConditionTypeDef = TypedDict(
    "_OptionalDocumentAttributeConditionTypeDef",
    {
        "ConditionOnValue": "DocumentAttributeValueTypeDef",
    },
    total=False,
)

class DocumentAttributeConditionTypeDef(
    _RequiredDocumentAttributeConditionTypeDef, _OptionalDocumentAttributeConditionTypeDef
):
    pass

DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "TargetDocumentAttributeKey": str,
        "TargetDocumentAttributeValueDeletion": bool,
        "TargetDocumentAttributeValue": "DocumentAttributeValueTypeDef",
    },
    total=False,
)

DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "Key": str,
        "Value": "DocumentAttributeValueTypeDef",
    },
)

DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {
        "DocumentAttributeValue": "DocumentAttributeValueTypeDef",
        "Count": int,
        "FacetResults": List[Dict[str, Any]],
    },
    total=False,
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "StringValue": str,
        "StringListValue": List[str],
        "LongValue": int,
        "DateValue": Union[datetime, str],
    },
    total=False,
)

_RequiredDocumentInfoTypeDef = TypedDict(
    "_RequiredDocumentInfoTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalDocumentInfoTypeDef = TypedDict(
    "_OptionalDocumentInfoTypeDef",
    {
        "Attributes": List["DocumentAttributeTypeDef"],
    },
    total=False,
)

class DocumentInfoTypeDef(_RequiredDocumentInfoTypeDef, _OptionalDocumentInfoTypeDef):
    pass

_RequiredDocumentMetadataConfigurationTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
    },
)
_OptionalDocumentMetadataConfigurationTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationTypeDef",
    {
        "Relevance": "RelevanceTypeDef",
        "Search": "SearchTypeDef",
    },
    total=False,
)

class DocumentMetadataConfigurationTypeDef(
    _RequiredDocumentMetadataConfigurationTypeDef, _OptionalDocumentMetadataConfigurationTypeDef
):
    pass

DocumentRelevanceConfigurationTypeDef = TypedDict(
    "DocumentRelevanceConfigurationTypeDef",
    {
        "Name": str,
        "Relevance": "RelevanceTypeDef",
    },
)

_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "Id": str,
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "Title": str,
        "Blob": Union[bytes, IO[bytes], StreamingBody],
        "S3Path": "S3PathTypeDef",
        "Attributes": List["DocumentAttributeTypeDef"],
        "AccessControlList": List["PrincipalTypeDef"],
        "HierarchicalAccessControlList": List["HierarchicalPrincipalTypeDef"],
        "ContentType": ContentTypeType,
        "AccessControlConfigurationId": str,
    },
    total=False,
)

class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass

DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)

EntityConfigurationTypeDef = TypedDict(
    "EntityConfigurationTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
    },
)

EntityDisplayDataTypeDef = TypedDict(
    "EntityDisplayDataTypeDef",
    {
        "UserName": str,
        "GroupName": str,
        "IdentifiedUserName": str,
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)

EntityPersonaConfigurationTypeDef = TypedDict(
    "EntityPersonaConfigurationTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
    },
)

ExperienceConfigurationTypeDef = TypedDict(
    "ExperienceConfigurationTypeDef",
    {
        "ContentSourceConfiguration": "ContentSourceConfigurationTypeDef",
        "UserIdentityConfiguration": "UserIdentityConfigurationTypeDef",
    },
    total=False,
)

ExperienceEndpointTypeDef = TypedDict(
    "ExperienceEndpointTypeDef",
    {
        "EndpointType": Literal["HOME"],
        "Endpoint": str,
    },
    total=False,
)

ExperienceEntitiesSummaryTypeDef = TypedDict(
    "ExperienceEntitiesSummaryTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
        "DisplayData": "EntityDisplayDataTypeDef",
    },
    total=False,
)

ExperiencesSummaryTypeDef = TypedDict(
    "ExperiencesSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "CreatedAt": datetime,
        "Status": ExperienceStatusType,
        "Endpoints": List["ExperienceEndpointTypeDef"],
    },
    total=False,
)

FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": str,
        "DocumentAttributeValueType": DocumentAttributeValueTypeType,
        "DocumentAttributeValueCountPairs": List[Dict[str, Any]],
    },
    total=False,
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "DocumentAttributeKey": str,
        "Facets": List[Dict[str, Any]],
        "MaxResults": int,
    },
    total=False,
)

FailedEntityTypeDef = TypedDict(
    "FailedEntityTypeDef",
    {
        "EntityId": str,
        "ErrorMessage": str,
    },
    total=False,
)

FaqStatisticsTypeDef = TypedDict(
    "FaqStatisticsTypeDef",
    {
        "IndexedQuestionAnswersCount": int,
    },
)

FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FaqStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
    },
    total=False,
)

_RequiredFsxConfigurationTypeDef = TypedDict(
    "_RequiredFsxConfigurationTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
    },
)
_OptionalFsxConfigurationTypeDef = TypedDict(
    "_OptionalFsxConfigurationTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class FsxConfigurationTypeDef(_RequiredFsxConfigurationTypeDef, _OptionalFsxConfigurationTypeDef):
    pass

_RequiredGetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
    },
)
_OptionalGetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetQuerySuggestionsRequestRequestTypeDef",
    {
        "MaxSuggestionsCount": int,
    },
    total=False,
)

class GetQuerySuggestionsRequestRequestTypeDef(
    _RequiredGetQuerySuggestionsRequestRequestTypeDef,
    _OptionalGetQuerySuggestionsRequestRequestTypeDef,
):
    pass

GetQuerySuggestionsResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List["SuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSnapshotsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSnapshotsRequestRequestTypeDef",
    {
        "IndexId": str,
        "Interval": IntervalType,
        "MetricType": MetricTypeType,
    },
)
_OptionalGetSnapshotsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSnapshotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetSnapshotsRequestRequestTypeDef(
    _RequiredGetSnapshotsRequestRequestTypeDef, _OptionalGetSnapshotsRequestRequestTypeDef
):
    pass

GetSnapshotsResponseTypeDef = TypedDict(
    "GetSnapshotsResponseTypeDef",
    {
        "SnapShotTimeFilter": "TimeRangeTypeDef",
        "SnapshotsDataHeader": List[str],
        "SnapshotsData": List[List[str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGitHubConfigurationTypeDef = TypedDict(
    "_RequiredGitHubConfigurationTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGitHubConfigurationTypeDef = TypedDict(
    "_OptionalGitHubConfigurationTypeDef",
    {
        "SaaSConfiguration": "SaaSConfigurationTypeDef",
        "OnPremiseConfiguration": "OnPremiseConfigurationTypeDef",
        "Type": TypeType,
        "UseChangeLog": bool,
        "GitHubDocumentCrawlProperties": "GitHubDocumentCrawlPropertiesTypeDef",
        "RepositoryFilter": List[str],
        "InclusionFolderNamePatterns": List[str],
        "InclusionFileTypePatterns": List[str],
        "InclusionFileNamePatterns": List[str],
        "ExclusionFolderNamePatterns": List[str],
        "ExclusionFileTypePatterns": List[str],
        "ExclusionFileNamePatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "GitHubRepositoryConfigurationFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "GitHubCommitConfigurationFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "GitHubIssueDocumentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
        "GitHubIssueCommentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
        "GitHubIssueAttachmentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
        "GitHubPullRequestCommentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
        "GitHubPullRequestDocumentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
        "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": List[
            "DataSourceToIndexFieldMappingTypeDef"
        ],
    },
    total=False,
)

class GitHubConfigurationTypeDef(
    _RequiredGitHubConfigurationTypeDef, _OptionalGitHubConfigurationTypeDef
):
    pass

GitHubDocumentCrawlPropertiesTypeDef = TypedDict(
    "GitHubDocumentCrawlPropertiesTypeDef",
    {
        "CrawlRepositoryDocuments": bool,
        "CrawlIssue": bool,
        "CrawlIssueComment": bool,
        "CrawlIssueCommentAttachment": bool,
        "CrawlPullRequest": bool,
        "CrawlPullRequestComment": bool,
        "CrawlPullRequestCommentAttachment": bool,
    },
    total=False,
)

_RequiredGoogleDriveConfigurationTypeDef = TypedDict(
    "_RequiredGoogleDriveConfigurationTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGoogleDriveConfigurationTypeDef = TypedDict(
    "_OptionalGoogleDriveConfigurationTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "ExcludeMimeTypes": List[str],
        "ExcludeUserAccounts": List[str],
        "ExcludeSharedDrives": List[str],
    },
    total=False,
)

class GoogleDriveConfigurationTypeDef(
    _RequiredGoogleDriveConfigurationTypeDef, _OptionalGoogleDriveConfigurationTypeDef
):
    pass

GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "MemberGroups": List["MemberGroupTypeDef"],
        "MemberUsers": List["MemberUserTypeDef"],
        "S3PathforGroupMembers": "S3PathTypeDef",
    },
    total=False,
)

GroupOrderingIdSummaryTypeDef = TypedDict(
    "GroupOrderingIdSummaryTypeDef",
    {
        "Status": PrincipalMappingStatusType,
        "LastUpdatedAt": datetime,
        "ReceivedAt": datetime,
        "OrderingId": int,
        "FailureReason": str,
    },
    total=False,
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupId": str,
        "OrderingId": int,
    },
    total=False,
)

HierarchicalPrincipalTypeDef = TypedDict(
    "HierarchicalPrincipalTypeDef",
    {
        "PrincipalList": List["PrincipalTypeDef"],
    },
)

_RequiredHighlightTypeDef = TypedDict(
    "_RequiredHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
)
_OptionalHighlightTypeDef = TypedDict(
    "_OptionalHighlightTypeDef",
    {
        "TopAnswer": bool,
        "Type": HighlightTypeType,
    },
    total=False,
)

class HighlightTypeDef(_RequiredHighlightTypeDef, _OptionalHighlightTypeDef):
    pass

_RequiredHookConfigurationTypeDef = TypedDict(
    "_RequiredHookConfigurationTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
    },
)
_OptionalHookConfigurationTypeDef = TypedDict(
    "_OptionalHookConfigurationTypeDef",
    {
        "InvocationCondition": "DocumentAttributeConditionTypeDef",
    },
    total=False,
)

class HookConfigurationTypeDef(
    _RequiredHookConfigurationTypeDef, _OptionalHookConfigurationTypeDef
):
    pass

_RequiredIndexConfigurationSummaryTypeDef = TypedDict(
    "_RequiredIndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": IndexStatusType,
    },
)
_OptionalIndexConfigurationSummaryTypeDef = TypedDict(
    "_OptionalIndexConfigurationSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
    },
    total=False,
)

class IndexConfigurationSummaryTypeDef(
    _RequiredIndexConfigurationSummaryTypeDef, _OptionalIndexConfigurationSummaryTypeDef
):
    pass

IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "FaqStatistics": "FaqStatisticsTypeDef",
        "TextDocumentStatistics": "TextDocumentStatisticsTypeDef",
    },
)

InlineCustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    {
        "Condition": "DocumentAttributeConditionTypeDef",
        "Target": "DocumentAttributeTargetTypeDef",
        "DocumentContentDeletion": bool,
    },
    total=False,
)

_RequiredJiraConfigurationTypeDef = TypedDict(
    "_RequiredJiraConfigurationTypeDef",
    {
        "JiraAccountUrl": str,
        "SecretArn": str,
    },
)
_OptionalJiraConfigurationTypeDef = TypedDict(
    "_OptionalJiraConfigurationTypeDef",
    {
        "UseChangeLog": bool,
        "Project": List[str],
        "IssueType": List[str],
        "Status": List[str],
        "IssueSubEntityFilter": List[IssueSubEntityType],
        "AttachmentFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "CommentFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "IssueFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "ProjectFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "WorkLogFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
    },
    total=False,
)

class JiraConfigurationTypeDef(
    _RequiredJiraConfigurationTypeDef, _OptionalJiraConfigurationTypeDef
):
    pass

JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef",
    {
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
    },
)

_RequiredJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_RequiredJwtTokenTypeConfigurationTypeDef",
    {
        "KeyLocation": KeyLocationType,
    },
)
_OptionalJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_OptionalJwtTokenTypeConfigurationTypeDef",
    {
        "URL": str,
        "SecretManagerArn": str,
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
        "Issuer": str,
        "ClaimRegex": str,
    },
    total=False,
)

class JwtTokenTypeConfigurationTypeDef(
    _RequiredJwtTokenTypeConfigurationTypeDef, _OptionalJwtTokenTypeConfigurationTypeDef
):
    pass

_RequiredListAccessControlConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessControlConfigurationsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListAccessControlConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessControlConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAccessControlConfigurationsRequestRequestTypeDef(
    _RequiredListAccessControlConfigurationsRequestRequestTypeDef,
    _OptionalListAccessControlConfigurationsRequestRequestTypeDef,
):
    pass

ListAccessControlConfigurationsResponseTypeDef = TypedDict(
    "ListAccessControlConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "AccessControlConfigurations": List["AccessControlConfigurationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTimeFilter": "TimeRangeTypeDef",
        "StatusFilter": DataSourceSyncJobStatusType,
    },
    total=False,
)

class ListDataSourceSyncJobsRequestRequestTypeDef(
    _RequiredListDataSourceSyncJobsRequestRequestTypeDef,
    _OptionalListDataSourceSyncJobsRequestRequestTypeDef,
):
    pass

ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "History": List["DataSourceSyncJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "SummaryItems": List["DataSourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntityPersonasRequestRequestTypeDef = TypedDict(
    "_RequiredListEntityPersonasRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListEntityPersonasRequestRequestTypeDef = TypedDict(
    "_OptionalListEntityPersonasRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEntityPersonasRequestRequestTypeDef(
    _RequiredListEntityPersonasRequestRequestTypeDef,
    _OptionalListEntityPersonasRequestRequestTypeDef,
):
    pass

ListEntityPersonasResponseTypeDef = TypedDict(
    "ListEntityPersonasResponseTypeDef",
    {
        "SummaryItems": List["PersonasSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListExperienceEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListExperienceEntitiesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListExperienceEntitiesRequestRequestTypeDef(
    _RequiredListExperienceEntitiesRequestRequestTypeDef,
    _OptionalListExperienceEntitiesRequestRequestTypeDef,
):
    pass

ListExperienceEntitiesResponseTypeDef = TypedDict(
    "ListExperienceEntitiesResponseTypeDef",
    {
        "SummaryItems": List["ExperienceEntitiesSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExperiencesRequestRequestTypeDef = TypedDict(
    "_RequiredListExperiencesRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListExperiencesRequestRequestTypeDef = TypedDict(
    "_OptionalListExperiencesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListExperiencesRequestRequestTypeDef(
    _RequiredListExperiencesRequestRequestTypeDef, _OptionalListExperiencesRequestRequestTypeDef
):
    pass

ListExperiencesResponseTypeDef = TypedDict(
    "ListExperiencesResponseTypeDef",
    {
        "SummaryItems": List["ExperiencesSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFaqsRequestRequestTypeDef = TypedDict(
    "_RequiredListFaqsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListFaqsRequestRequestTypeDef = TypedDict(
    "_OptionalListFaqsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListFaqsRequestRequestTypeDef(
    _RequiredListFaqsRequestRequestTypeDef, _OptionalListFaqsRequestRequestTypeDef
):
    pass

ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {
        "NextToken": str,
        "FaqSummaryItems": List["FaqSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "IndexId": str,
        "OrderingId": int,
    },
)
_OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListGroupsOlderThanOrderingIdRequestRequestTypeDef(
    _RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef,
    _OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef,
):
    pass

ListGroupsOlderThanOrderingIdResponseTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    {
        "GroupsSummaries": List["GroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List["IndexConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "_RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "_OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQuerySuggestionsBlockListsRequestRequestTypeDef(
    _RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef,
    _OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef,
):
    pass

ListQuerySuggestionsBlockListsResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    {
        "BlockListSummaryItems": List["QuerySuggestionsBlockListSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThesauriRequestRequestTypeDef = TypedDict(
    "_RequiredListThesauriRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListThesauriRequestRequestTypeDef = TypedDict(
    "_OptionalListThesauriRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListThesauriRequestRequestTypeDef(
    _RequiredListThesauriRequestRequestTypeDef, _OptionalListThesauriRequestRequestTypeDef
):
    pass

ListThesauriResponseTypeDef = TypedDict(
    "ListThesauriResponseTypeDef",
    {
        "NextToken": str,
        "ThesaurusSummaryItems": List["ThesaurusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMemberGroupTypeDef = TypedDict(
    "_RequiredMemberGroupTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalMemberGroupTypeDef = TypedDict(
    "_OptionalMemberGroupTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)

class MemberGroupTypeDef(_RequiredMemberGroupTypeDef, _OptionalMemberGroupTypeDef):
    pass

MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "UserId": str,
    },
)

OnPremiseConfigurationTypeDef = TypedDict(
    "OnPremiseConfigurationTypeDef",
    {
        "HostUrl": str,
        "OrganizationName": str,
        "SslCertificateS3Path": "S3PathTypeDef",
    },
)

_RequiredOneDriveConfigurationTypeDef = TypedDict(
    "_RequiredOneDriveConfigurationTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": "OneDriveUsersTypeDef",
    },
)
_OptionalOneDriveConfigurationTypeDef = TypedDict(
    "_OptionalOneDriveConfigurationTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "DisableLocalGroups": bool,
    },
    total=False,
)

class OneDriveConfigurationTypeDef(
    _RequiredOneDriveConfigurationTypeDef, _OptionalOneDriveConfigurationTypeDef
):
    pass

OneDriveUsersTypeDef = TypedDict(
    "OneDriveUsersTypeDef",
    {
        "OneDriveUserList": List[str],
        "OneDriveUserS3Path": "S3PathTypeDef",
    },
    total=False,
)

PersonasSummaryTypeDef = TypedDict(
    "PersonasSummaryTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredPrincipalTypeDef = TypedDict(
    "_RequiredPrincipalTypeDef",
    {
        "Name": str,
        "Type": PrincipalTypeType,
        "Access": ReadAccessTypeType,
    },
)
_OptionalPrincipalTypeDef = TypedDict(
    "_OptionalPrincipalTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)

class PrincipalTypeDef(_RequiredPrincipalTypeDef, _OptionalPrincipalTypeDef):
    pass

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "Credentials": str,
    },
    total=False,
)

class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass

_RequiredPutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredPutPrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "GroupMembers": "GroupMembersTypeDef",
    },
)
_OptionalPutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalPutPrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "OrderingId": int,
        "RoleArn": str,
    },
    total=False,
)

class PutPrincipalMappingRequestRequestTypeDef(
    _RequiredPutPrincipalMappingRequestRequestTypeDef,
    _OptionalPutPrincipalMappingRequestRequestTypeDef,
):
    pass

_RequiredQueryRequestRequestTypeDef = TypedDict(
    "_RequiredQueryRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalQueryRequestRequestTypeDef = TypedDict(
    "_OptionalQueryRequestRequestTypeDef",
    {
        "QueryText": str,
        "AttributeFilter": "AttributeFilterTypeDef",
        "Facets": List["FacetTypeDef"],
        "RequestedDocumentAttributes": List[str],
        "QueryResultTypeFilter": QueryResultTypeType,
        "DocumentRelevanceOverrideConfigurations": List["DocumentRelevanceConfigurationTypeDef"],
        "PageNumber": int,
        "PageSize": int,
        "SortingConfiguration": "SortingConfigurationTypeDef",
        "UserContext": "UserContextTypeDef",
        "VisitorId": str,
        "SpellCorrectionConfiguration": "SpellCorrectionConfigurationTypeDef",
    },
    total=False,
)

class QueryRequestRequestTypeDef(
    _RequiredQueryRequestRequestTypeDef, _OptionalQueryRequestRequestTypeDef
):
    pass

QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": str,
        "Type": QueryResultTypeType,
        "Format": QueryResultFormatType,
        "AdditionalAttributes": List["AdditionalResultAttributeTypeDef"],
        "DocumentId": str,
        "DocumentTitle": "TextWithHighlightsTypeDef",
        "DocumentExcerpt": "TextWithHighlightsTypeDef",
        "DocumentURI": str,
        "DocumentAttributes": List["DocumentAttributeTypeDef"],
        "ScoreAttributes": "ScoreAttributesTypeDef",
        "FeedbackToken": str,
        "TableExcerpt": "TableExcerptTypeDef",
    },
    total=False,
)

QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List["QueryResultItemTypeDef"],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
        "Warnings": List["WarningTypeDef"],
        "SpellCorrectedQueries": List["SpellCorrectedQueryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuerySuggestionsBlockListSummaryTypeDef = TypedDict(
    "QuerySuggestionsBlockListSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ItemCount": int,
    },
    total=False,
)

_RequiredQuipConfigurationTypeDef = TypedDict(
    "_RequiredQuipConfigurationTypeDef",
    {
        "Domain": str,
        "SecretArn": str,
    },
)
_OptionalQuipConfigurationTypeDef = TypedDict(
    "_OptionalQuipConfigurationTypeDef",
    {
        "CrawlFileComments": bool,
        "CrawlChatRooms": bool,
        "CrawlAttachments": bool,
        "FolderIds": List[str],
        "ThreadFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "MessageFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "AttachmentFieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
    },
    total=False,
)

class QuipConfigurationTypeDef(
    _RequiredQuipConfigurationTypeDef, _OptionalQuipConfigurationTypeDef
):
    pass

RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {
        "ResultId": str,
        "RelevanceValue": RelevanceTypeType,
    },
)

RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": OrderType,
        "ValueImportanceMap": Dict[str, int],
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

_RequiredS3DataSourceConfigurationTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3DataSourceConfigurationTypeDef = TypedDict(
    "_OptionalS3DataSourceConfigurationTypeDef",
    {
        "InclusionPrefixes": List[str],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": "DocumentsMetadataConfigurationTypeDef",
        "AccessControlListConfiguration": "AccessControlListConfigurationTypeDef",
    },
    total=False,
)

class S3DataSourceConfigurationTypeDef(
    _RequiredS3DataSourceConfigurationTypeDef, _OptionalS3DataSourceConfigurationTypeDef
):
    pass

S3PathTypeDef = TypedDict(
    "S3PathTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

SaaSConfigurationTypeDef = TypedDict(
    "SaaSConfigurationTypeDef",
    {
        "OrganizationName": str,
        "HostUrl": str,
    },
)

_RequiredSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "IncludeFilterTypes": List[SalesforceChatterFeedIncludeFilterTypeType],
    },
    total=False,
)

class SalesforceChatterFeedConfigurationTypeDef(
    _RequiredSalesforceChatterFeedConfigurationTypeDef,
    _OptionalSalesforceChatterFeedConfigurationTypeDef,
):
    pass

_RequiredSalesforceConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
    },
)
_OptionalSalesforceConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceConfigurationTypeDef",
    {
        "StandardObjectConfigurations": List["SalesforceStandardObjectConfigurationTypeDef"],
        "KnowledgeArticleConfiguration": "SalesforceKnowledgeArticleConfigurationTypeDef",
        "ChatterFeedConfiguration": "SalesforceChatterFeedConfigurationTypeDef",
        "CrawlAttachments": bool,
        "StandardObjectAttachmentConfiguration": "SalesforceStandardObjectAttachmentConfigurationTypeDef",
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
    },
    total=False,
)

class SalesforceConfigurationTypeDef(
    _RequiredSalesforceConfigurationTypeDef, _OptionalSalesforceConfigurationTypeDef
):
    pass

_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
):
    pass

_RequiredSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "IncludedStates": List[SalesforceKnowledgeArticleStateType],
    },
)
_OptionalSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "StandardKnowledgeArticleTypeConfiguration": "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
        "CustomKnowledgeArticleTypeConfigurations": List[
            "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
        ],
    },
    total=False,
)

class SalesforceKnowledgeArticleConfigurationTypeDef(
    _RequiredSalesforceKnowledgeArticleConfigurationTypeDef,
    _OptionalSalesforceKnowledgeArticleConfigurationTypeDef,
):
    pass

_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
):
    pass

SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

_RequiredSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardObjectConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class SalesforceStandardObjectConfigurationTypeDef(
    _RequiredSalesforceStandardObjectConfigurationTypeDef,
    _OptionalSalesforceStandardObjectConfigurationTypeDef,
):
    pass

ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {
        "ScoreConfidence": ScoreConfidenceType,
    },
    total=False,
)

SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {
        "Facetable": bool,
        "Searchable": bool,
        "Displayable": bool,
        "Sortable": bool,
    },
    total=False,
)

_RequiredSeedUrlConfigurationTypeDef = TypedDict(
    "_RequiredSeedUrlConfigurationTypeDef",
    {
        "SeedUrls": List[str],
    },
)
_OptionalSeedUrlConfigurationTypeDef = TypedDict(
    "_OptionalSeedUrlConfigurationTypeDef",
    {
        "WebCrawlerMode": WebCrawlerModeType,
    },
    total=False,
)

class SeedUrlConfigurationTypeDef(
    _RequiredSeedUrlConfigurationTypeDef, _OptionalSeedUrlConfigurationTypeDef
):
    pass

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredServiceNowConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowConfigurationTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
    },
)
_OptionalServiceNowConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowConfigurationTypeDef",
    {
        "KnowledgeArticleConfiguration": "ServiceNowKnowledgeArticleConfigurationTypeDef",
        "ServiceCatalogConfiguration": "ServiceNowServiceCatalogConfigurationTypeDef",
        "AuthenticationType": ServiceNowAuthenticationTypeType,
    },
    total=False,
)

class ServiceNowConfigurationTypeDef(
    _RequiredServiceNowConfigurationTypeDef, _OptionalServiceNowConfigurationTypeDef
):
    pass

_RequiredServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "FilterQuery": str,
    },
    total=False,
)

class ServiceNowKnowledgeArticleConfigurationTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationTypeDef,
    _OptionalServiceNowKnowledgeArticleConfigurationTypeDef,
):
    pass

_RequiredServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowServiceCatalogConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowServiceCatalogConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class ServiceNowServiceCatalogConfigurationTypeDef(
    _RequiredServiceNowServiceCatalogConfigurationTypeDef,
    _OptionalServiceNowServiceCatalogConfigurationTypeDef,
):
    pass

_RequiredSharePointConfigurationTypeDef = TypedDict(
    "_RequiredSharePointConfigurationTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": List[str],
        "SecretArn": str,
    },
)
_OptionalSharePointConfigurationTypeDef = TypedDict(
    "_OptionalSharePointConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "DocumentTitleFieldName": str,
        "DisableLocalGroups": bool,
        "SslCertificateS3Path": "S3PathTypeDef",
        "AuthenticationType": SharePointOnlineAuthenticationTypeType,
        "ProxyConfiguration": "ProxyConfigurationTypeDef",
    },
    total=False,
)

class SharePointConfigurationTypeDef(
    _RequiredSharePointConfigurationTypeDef, _OptionalSharePointConfigurationTypeDef
):
    pass

SiteMapsConfigurationTypeDef = TypedDict(
    "SiteMapsConfigurationTypeDef",
    {
        "SiteMaps": List[str],
    },
)

_RequiredSlackConfigurationTypeDef = TypedDict(
    "_RequiredSlackConfigurationTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": List[SlackEntityType],
        "SinceCrawlDate": str,
    },
)
_OptionalSlackConfigurationTypeDef = TypedDict(
    "_OptionalSlackConfigurationTypeDef",
    {
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "UseChangeLog": bool,
        "CrawlBotMessage": bool,
        "ExcludeArchived": bool,
        "LookBackPeriod": int,
        "PrivateChannelFilter": List[str],
        "PublicChannelFilter": List[str],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class SlackConfigurationTypeDef(
    _RequiredSlackConfigurationTypeDef, _OptionalSlackConfigurationTypeDef
):
    pass

SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortOrder": SortOrderType,
    },
)

SpellCorrectedQueryTypeDef = TypedDict(
    "SpellCorrectedQueryTypeDef",
    {
        "SuggestedQueryText": str,
        "Corrections": List["CorrectionTypeDef"],
    },
    total=False,
)

SpellCorrectionConfigurationTypeDef = TypedDict(
    "SpellCorrectionConfigurationTypeDef",
    {
        "IncludeQuerySpellCheckSuggestions": bool,
    },
)

SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {
        "QueryIdentifiersEnclosingOption": QueryIdentifiersEnclosingOptionType,
    },
    total=False,
)

StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "ExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "DocumentId": str,
        "DocumentStatus": DocumentStatusType,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

_RequiredSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitFeedbackRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryId": str,
    },
)
_OptionalSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitFeedbackRequestRequestTypeDef",
    {
        "ClickFeedbackItems": List["ClickFeedbackTypeDef"],
        "RelevanceFeedbackItems": List["RelevanceFeedbackTypeDef"],
    },
    total=False,
)

class SubmitFeedbackRequestRequestTypeDef(
    _RequiredSubmitFeedbackRequestRequestTypeDef, _OptionalSubmitFeedbackRequestRequestTypeDef
):
    pass

SuggestionHighlightTypeDef = TypedDict(
    "SuggestionHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

SuggestionTextWithHighlightsTypeDef = TypedDict(
    "SuggestionTextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List["SuggestionHighlightTypeDef"],
    },
    total=False,
)

SuggestionTypeDef = TypedDict(
    "SuggestionTypeDef",
    {
        "Id": str,
        "Value": "SuggestionValueTypeDef",
    },
    total=False,
)

SuggestionValueTypeDef = TypedDict(
    "SuggestionValueTypeDef",
    {
        "Text": "SuggestionTextWithHighlightsTypeDef",
    },
    total=False,
)

TableCellTypeDef = TypedDict(
    "TableCellTypeDef",
    {
        "Value": str,
        "TopAnswer": bool,
        "Highlighted": bool,
        "Header": bool,
    },
    total=False,
)

TableExcerptTypeDef = TypedDict(
    "TableExcerptTypeDef",
    {
        "Rows": List["TableRowTypeDef"],
        "TotalNumberOfRows": int,
    },
    total=False,
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "Cells": List["TableCellTypeDef"],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "Template": Dict[str, Any],
    },
    total=False,
)

TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "IndexedTextDocumentsCount": int,
        "IndexedTextBytes": int,
    },
)

TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List["HighlightTypeDef"],
    },
    total=False,
)

ThesaurusSummaryTypeDef = TypedDict(
    "ThesaurusSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ThesaurusStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
_OptionalUpdateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessControlConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "AccessControlList": List["PrincipalTypeDef"],
        "HierarchicalAccessControlList": List["HierarchicalPrincipalTypeDef"],
    },
    total=False,
)

class UpdateAccessControlConfigurationRequestRequestTypeDef(
    _RequiredUpdateAccessControlConfigurationRequestRequestTypeDef,
    _OptionalUpdateAccessControlConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Configuration": "DataSourceConfigurationTypeDef",
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": "CustomDocumentEnrichmentConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

_RequiredUpdateExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Configuration": "ExperienceConfigurationTypeDef",
        "Description": str,
    },
    total=False,
)

class UpdateExperienceRequestRequestTypeDef(
    _RequiredUpdateExperienceRequestRequestTypeDef, _OptionalUpdateExperienceRequestRequestTypeDef
):
    pass

_RequiredUpdateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Description": str,
        "DocumentMetadataConfigurationUpdates": List["DocumentMetadataConfigurationTypeDef"],
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": "UserGroupResolutionConfigurationTypeDef",
    },
    total=False,
)

class UpdateIndexRequestRequestTypeDef(
    _RequiredUpdateIndexRequestRequestTypeDef, _OptionalUpdateIndexRequestRequestTypeDef
):
    pass

_RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
_OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceS3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
    total=False,
)

class UpdateQuerySuggestionsBlockListRequestRequestTypeDef(
    _RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef,
    _OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef,
):
    pass

_RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "Mode": ModeType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
    },
    total=False,
)

class UpdateQuerySuggestionsConfigRequestRequestTypeDef(
    _RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef,
    _OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef,
):
    pass

_RequiredUpdateThesaurusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateThesaurusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThesaurusRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
    },
    total=False,
)

class UpdateThesaurusRequestRequestTypeDef(
    _RequiredUpdateThesaurusRequestRequestTypeDef, _OptionalUpdateThesaurusRequestRequestTypeDef
):
    pass

UrlsTypeDef = TypedDict(
    "UrlsTypeDef",
    {
        "SeedUrlConfiguration": "SeedUrlConfigurationTypeDef",
        "SiteMapsConfiguration": "SiteMapsConfigurationTypeDef",
    },
    total=False,
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "Token": str,
        "UserId": str,
        "Groups": List[str],
        "DataSourceGroups": List["DataSourceGroupTypeDef"],
    },
    total=False,
)

UserGroupResolutionConfigurationTypeDef = TypedDict(
    "UserGroupResolutionConfigurationTypeDef",
    {
        "UserGroupResolutionMode": UserGroupResolutionModeType,
    },
)

UserIdentityConfigurationTypeDef = TypedDict(
    "UserIdentityConfigurationTypeDef",
    {
        "IdentityAttributeName": str,
    },
    total=False,
)

UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": "JwtTokenTypeConfigurationTypeDef",
        "JsonTokenTypeConfiguration": "JsonTokenTypeConfigurationTypeDef",
    },
    total=False,
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Message": str,
        "Code": Literal["QUERY_LANGUAGE_INVALID_SYNTAX"],
    },
    total=False,
)

_RequiredWebCrawlerConfigurationTypeDef = TypedDict(
    "_RequiredWebCrawlerConfigurationTypeDef",
    {
        "Urls": "UrlsTypeDef",
    },
)
_OptionalWebCrawlerConfigurationTypeDef = TypedDict(
    "_OptionalWebCrawlerConfigurationTypeDef",
    {
        "CrawlDepth": int,
        "MaxLinksPerPage": int,
        "MaxContentSizePerPageInMegaBytes": float,
        "MaxUrlsPerMinuteCrawlRate": int,
        "UrlInclusionPatterns": List[str],
        "UrlExclusionPatterns": List[str],
        "ProxyConfiguration": "ProxyConfigurationTypeDef",
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
    },
    total=False,
)

class WebCrawlerConfigurationTypeDef(
    _RequiredWebCrawlerConfigurationTypeDef, _OptionalWebCrawlerConfigurationTypeDef
):
    pass

_RequiredWorkDocsConfigurationTypeDef = TypedDict(
    "_RequiredWorkDocsConfigurationTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalWorkDocsConfigurationTypeDef = TypedDict(
    "_OptionalWorkDocsConfigurationTypeDef",
    {
        "CrawlComments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

class WorkDocsConfigurationTypeDef(
    _RequiredWorkDocsConfigurationTypeDef, _OptionalWorkDocsConfigurationTypeDef
):
    pass
