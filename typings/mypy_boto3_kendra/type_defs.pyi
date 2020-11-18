"""
Main interface for kendra service type definitions.

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlListConfigurationTypeDef

    data: AccessControlListConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "AdditionalResultAttributeTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "CapacityUnitsConfigurationTypeDef",
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
    "DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "FacetResultTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PrincipalTypeDef",
    "QueryResultItemTypeDef",
    "RelevanceTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3PathTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "SearchTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SqlConfigurationTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "UserTokenConfigurationTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "ClickFeedbackTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeIndexResponseTypeDef",
    "AttributeFilterTypeDef",
    "DocumentTypeDef",
    "FacetTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFaqsResponseTypeDef",
    "ListIndicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "QueryResultTypeDef",
    "RelevanceFeedbackTypeDef",
    "SortingConfigurationTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "TimeRangeTypeDef",
    "UserContextTypeDef",
)

AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef", {"KeyPath": str}, total=False
)

AclConfigurationTypeDef = TypedDict("AclConfigurationTypeDef", {"AllowedGroupsColumnName": str})

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
    {"TextWithHighlightsValue": "TextWithHighlightsTypeDef"},
    total=False,
)

BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {"Id": str, "ErrorCode": Literal["InternalError", "InvalidRequest"], "ErrorMessage": str},
    total=False,
)

BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {"Id": str, "ErrorCode": Literal["InternalError", "InvalidRequest"], "ErrorMessage": str},
    total=False,
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef", {"StorageCapacityUnits": int, "QueryCapacityUnits": int}
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
    {"DocumentTitleColumnName": str, "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"]},
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
        "DataSourceFieldName": Literal[
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
        ],
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {"BlogFieldMappings": List["ConfluenceBlogToIndexFieldMappingTypeDef"]},
    total=False,
)

ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": Literal[
            "AUTHOR",
            "DISPLAY_URL",
            "ITEM_TYPE",
            "LABELS",
            "PUBLISH_DATE",
            "SPACE_KEY",
            "SPACE_NAME",
            "URL",
            "VERSION",
        ],
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

_RequiredConfluenceConfigurationTypeDef = TypedDict(
    "_RequiredConfluenceConfigurationTypeDef",
    {"ServerUrl": str, "SecretArn": str, "Version": Literal["CLOUD", "SERVER"]},
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
    },
    total=False,
)


class ConfluenceConfigurationTypeDef(
    _RequiredConfluenceConfigurationTypeDef, _OptionalConfluenceConfigurationTypeDef
):
    pass


ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {"PageFieldMappings": List["ConfluencePageToIndexFieldMappingTypeDef"]},
    total=False,
)

ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": Literal[
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
        ],
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
        "DataSourceFieldName": Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"],
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
    },
    total=False,
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": Literal[
            "S3",
            "SHAREPOINT",
            "DATABASE",
            "SALESFORCE",
            "ONEDRIVE",
            "SERVICENOW",
            "CUSTOM",
            "CONFLUENCE",
        ],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": Literal["CREATING", "DELETING", "FAILED", "UPDATING", "ACTIVE"],
    },
    total=False,
)

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
        "Status": Literal[
            "FAILED",
            "SUCCEEDED",
            "SYNCING",
            "INCOMPLETE",
            "STOPPING",
            "ABORTED",
            "SYNCING_INDEXING",
        ],
        "ErrorMessage": str,
        "ErrorCode": Literal["InternalError", "InvalidRequest"],
        "DataSourceErrorCode": str,
        "Metrics": "DataSourceSyncJobMetricsTypeDef",
    },
    total=False,
)

_RequiredDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_RequiredDataSourceToIndexFieldMappingTypeDef",
    {"DataSourceFieldName": str, "IndexFieldName": str},
)
_OptionalDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_OptionalDataSourceToIndexFieldMappingTypeDef", {"DateFieldFormat": str}, total=False
)


class DataSourceToIndexFieldMappingTypeDef(
    _RequiredDataSourceToIndexFieldMappingTypeDef, _OptionalDataSourceToIndexFieldMappingTypeDef
):
    pass


DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}
)

_RequiredDatabaseConfigurationTypeDef = TypedDict(
    "_RequiredDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": Literal[
            "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
        ],
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


DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef", {"Key": str, "Value": "DocumentAttributeValueTypeDef"}
)

DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {"DocumentAttributeValue": "DocumentAttributeValueTypeDef", "Count": int},
    total=False,
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

_RequiredDocumentMetadataConfigurationTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationTypeDef",
    {"Name": str, "Type": Literal["STRING_VALUE", "STRING_LIST_VALUE", "LONG_VALUE", "DATE_VALUE"]},
)
_OptionalDocumentMetadataConfigurationTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationTypeDef",
    {"Relevance": "RelevanceTypeDef", "Search": "SearchTypeDef"},
    total=False,
)


class DocumentMetadataConfigurationTypeDef(
    _RequiredDocumentMetadataConfigurationTypeDef, _OptionalDocumentMetadataConfigurationTypeDef
):
    pass


DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef", {"S3Prefix": str}, total=False
)

FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": str,
        "DocumentAttributeValueType": Literal[
            "STRING_VALUE", "STRING_LIST_VALUE", "LONG_VALUE", "DATE_VALUE"
        ],
        "DocumentAttributeValueCountPairs": List["DocumentAttributeValueCountPairTypeDef"],
    },
    total=False,
)

FaqStatisticsTypeDef = TypedDict("FaqStatisticsTypeDef", {"IndexedQuestionAnswersCount": int})

FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "FileFormat": Literal["CSV", "CSV_WITH_HEADER", "JSON"],
    },
    total=False,
)

_RequiredHighlightTypeDef = TypedDict(
    "_RequiredHighlightTypeDef", {"BeginOffset": int, "EndOffset": int}
)
_OptionalHighlightTypeDef = TypedDict("_OptionalHighlightTypeDef", {"TopAnswer": bool}, total=False)


class HighlightTypeDef(_RequiredHighlightTypeDef, _OptionalHighlightTypeDef):
    pass


_RequiredIndexConfigurationSummaryTypeDef = TypedDict(
    "_RequiredIndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": Literal[
            "CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING", "SYSTEM_UPDATING"
        ],
    },
)
_OptionalIndexConfigurationSummaryTypeDef = TypedDict(
    "_OptionalIndexConfigurationSummaryTypeDef",
    {"Name": str, "Id": str, "Edition": Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]},
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

JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef", {"UserNameAttributeField": str, "GroupAttributeField": str}
)

_RequiredJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_RequiredJwtTokenTypeConfigurationTypeDef", {"KeyLocation": Literal["URL", "SECRET_MANAGER"]}
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


_RequiredOneDriveConfigurationTypeDef = TypedDict(
    "_RequiredOneDriveConfigurationTypeDef",
    {"TenantDomain": str, "SecretArn": str, "OneDriveUsers": "OneDriveUsersTypeDef"},
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
    {"OneDriveUserList": List[str], "OneDriveUserS3Path": "S3PathTypeDef"},
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {"Name": str, "Type": Literal["USER", "GROUP"], "Access": Literal["ALLOW", "DENY"]},
)

QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": str,
        "Type": Literal["DOCUMENT", "QUESTION_ANSWER", "ANSWER"],
        "AdditionalAttributes": List["AdditionalResultAttributeTypeDef"],
        "DocumentId": str,
        "DocumentTitle": "TextWithHighlightsTypeDef",
        "DocumentExcerpt": "TextWithHighlightsTypeDef",
        "DocumentURI": str,
        "DocumentAttributes": List["DocumentAttributeTypeDef"],
        "ScoreAttributes": "ScoreAttributesTypeDef",
    },
    total=False,
)

RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": Literal["ASCENDING", "DESCENDING"],
        "ValueImportanceMap": Dict[str, int],
    },
    total=False,
)

_RequiredS3DataSourceConfigurationTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationTypeDef", {"BucketName": str}
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


S3PathTypeDef = TypedDict("S3PathTypeDef", {"Bucket": str, "Key": str})

_RequiredSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceChatterFeedConfigurationTypeDef", {"DocumentDataFieldName": str}
)
_OptionalSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "IncludeFilterTypes": List[Literal["ACTIVE_USER", "STANDARD_USER"]],
    },
    total=False,
)


class SalesforceChatterFeedConfigurationTypeDef(
    _RequiredSalesforceChatterFeedConfigurationTypeDef,
    _OptionalSalesforceChatterFeedConfigurationTypeDef,
):
    pass


_RequiredSalesforceConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceConfigurationTypeDef", {"ServerUrl": str, "SecretArn": str}
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
    {"Name": str, "DocumentDataFieldName": str},
)
_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {"DocumentTitleFieldName": str, "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"]},
    total=False,
)


class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


_RequiredSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceKnowledgeArticleConfigurationTypeDef",
    {"IncludedStates": List[Literal["DRAFT", "PUBLISHED", "ARCHIVED"]]},
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
    {"DocumentDataFieldName": str},
)
_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {"DocumentTitleFieldName": str, "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"]},
    total=False,
)


class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {"DocumentTitleFieldName": str, "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"]},
    total=False,
)

_RequiredSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": Literal[
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
        ],
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardObjectConfigurationTypeDef",
    {"DocumentTitleFieldName": str, "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"]},
    total=False,
)


class SalesforceStandardObjectConfigurationTypeDef(
    _RequiredSalesforceStandardObjectConfigurationTypeDef,
    _OptionalSalesforceStandardObjectConfigurationTypeDef,
):
    pass


ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {"ScoreConfidence": Literal["VERY_HIGH", "HIGH", "MEDIUM", "LOW"]},
    total=False,
)

SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {"Facetable": bool, "Searchable": bool, "Displayable": bool, "Sortable": bool},
    total=False,
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef", {"KmsKeyId": str}, total=False
)

_RequiredServiceNowConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowConfigurationTypeDef",
    {"HostUrl": str, "SecretArn": str, "ServiceNowBuildVersion": Literal["LONDON", "OTHERS"]},
)
_OptionalServiceNowConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowConfigurationTypeDef",
    {
        "KnowledgeArticleConfiguration": "ServiceNowKnowledgeArticleConfigurationTypeDef",
        "ServiceCatalogConfiguration": "ServiceNowServiceCatalogConfigurationTypeDef",
    },
    total=False,
)


class ServiceNowConfigurationTypeDef(
    _RequiredServiceNowConfigurationTypeDef, _OptionalServiceNowConfigurationTypeDef
):
    pass


_RequiredServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowKnowledgeArticleConfigurationTypeDef", {"DocumentDataFieldName": str}
)
_OptionalServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class ServiceNowKnowledgeArticleConfigurationTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationTypeDef,
    _OptionalServiceNowKnowledgeArticleConfigurationTypeDef,
):
    pass


_RequiredServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowServiceCatalogConfigurationTypeDef", {"DocumentDataFieldName": str}
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
    {"SharePointVersion": Literal["SHAREPOINT_ONLINE"], "Urls": List[str], "SecretArn": str},
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
    },
    total=False,
)


class SharePointConfigurationTypeDef(
    _RequiredSharePointConfigurationTypeDef, _OptionalSharePointConfigurationTypeDef
):
    pass


SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {"QueryIdentifiersEnclosingOption": Literal["DOUBLE_QUOTES", "NONE"]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef", {"IndexedTextDocumentsCount": int, "IndexedTextBytes": int}
)

TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef", {"Text": str, "Highlights": List["HighlightTypeDef"]}, total=False
)

UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": "JwtTokenTypeConfigurationTypeDef",
        "JsonTokenTypeConfiguration": "JsonTokenTypeConfigurationTypeDef",
    },
    total=False,
)

BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {"FailedDocuments": List["BatchDeleteDocumentResponseFailedDocumentTypeDef"]},
    total=False,
)

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {"FailedDocuments": List["BatchPutDocumentResponseFailedDocumentTypeDef"]},
    total=False,
)

ClickFeedbackTypeDef = TypedDict("ClickFeedbackTypeDef", {"ResultId": str, "ClickTime": datetime})

CreateDataSourceResponseTypeDef = TypedDict("CreateDataSourceResponseTypeDef", {"Id": str})

CreateFaqResponseTypeDef = TypedDict("CreateFaqResponseTypeDef", {"Id": str}, total=False)

CreateIndexResponseTypeDef = TypedDict("CreateIndexResponseTypeDef", {"Id": str}, total=False)

DataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "DataSourceSyncJobMetricTargetTypeDef", {"DataSourceId": str, "DataSourceSyncJobId": str}
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": Literal[
            "S3",
            "SHAREPOINT",
            "DATABASE",
            "SALESFORCE",
            "ONEDRIVE",
            "SERVICENOW",
            "CUSTOM",
            "CONFLUENCE",
        ],
        "Configuration": "DataSourceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "UPDATING", "ACTIVE"],
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
    },
    total=False,
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
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": Literal["CSV", "CSV_WITH_HEADER", "JSON"],
    },
    total=False,
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"],
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Status": Literal[
            "CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING", "SYSTEM_UPDATING"
        ],
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List["DocumentMetadataConfigurationTypeDef"],
        "IndexStatistics": "IndexStatisticsTypeDef",
        "ErrorMessage": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": Literal["ATTRIBUTE_FILTER", "USER_TOKEN"],
    },
    total=False,
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

_RequiredDocumentTypeDef = TypedDict("_RequiredDocumentTypeDef", {"Id": str})
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "Title": str,
        "Blob": Union[bytes, IO[bytes]],
        "S3Path": "S3PathTypeDef",
        "Attributes": List["DocumentAttributeTypeDef"],
        "AccessControlList": List["PrincipalTypeDef"],
        "ContentType": Literal["PDF", "HTML", "MS_WORD", "PLAIN_TEXT", "PPT"],
    },
    total=False,
)


class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass


FacetTypeDef = TypedDict("FacetTypeDef", {"DocumentAttributeKey": str}, total=False)

ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {"History": List["DataSourceSyncJobTypeDef"], "NextToken": str},
    total=False,
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {"SummaryItems": List["DataSourceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {"NextToken": str, "FaqSummaryItems": List["FaqSummaryTypeDef"]},
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {"IndexConfigurationSummaryItems": List["IndexConfigurationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List["QueryResultItemTypeDef"],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
    },
    total=False,
)

RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {"ResultId": str, "RelevanceValue": Literal["RELEVANT", "NOT_RELEVANT"]},
)

SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {"DocumentAttributeKey": str, "SortOrder": Literal["DESC", "ASC"]},
)

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef", {"ExecutionId": str}, total=False
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef", {"StartTime": datetime, "EndTime": datetime}, total=False
)

UserContextTypeDef = TypedDict("UserContextTypeDef", {"Token": str}, total=False)
