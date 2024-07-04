"""
Type annotations for qbusiness service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qbusiness.type_defs import APISchemaTypeDef

    data: APISchemaTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionPayloadFieldTypeType,
    ApplicationStatusType,
    AttachmentsControlModeType,
    AttachmentStatusType,
    AttributeTypeType,
    ChatModeType,
    ContentTypeType,
    CreatorModeControlType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DocumentAttributeBoostingLevelType,
    DocumentEnrichmentConditionOperatorType,
    DocumentStatusType,
    ErrorCodeType,
    GroupStatusType,
    IndexStatusType,
    IndexTypeType,
    MemberRelationType,
    MembershipTypeType,
    MessageTypeType,
    MessageUsefulnessReasonType,
    MessageUsefulnessType,
    NumberAttributeBoostingTypeType,
    PluginBuildStatusType,
    PluginStateType,
    PluginTypeType,
    QAppsControlModeType,
    ReadAccessTypeType,
    ResponseScopeType,
    RetrieverStatusType,
    RetrieverTypeType,
    RuleTypeType,
    StatusType,
    StringAttributeValueBoostingLevelType,
    WebExperienceSamplePromptsControlModeType,
    WebExperienceStatusType,
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
    "APISchemaTypeDef",
    "AccessConfigurationTypeDef",
    "AccessControlTypeDef",
    "ActionExecutionPayloadFieldTypeDef",
    "ActionExecutionTypeDef",
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    "ActionReviewPayloadFieldTypeDef",
    "ActionReviewTypeDef",
    "ApplicationTypeDef",
    "AppliedAttachmentsConfigurationTypeDef",
    "AppliedCreatorModeConfigurationTypeDef",
    "AttachmentInputTypeDef",
    "AttachmentOutputTypeDef",
    "AttachmentsConfigurationTypeDef",
    "AttributeFilterTypeDef",
    "AuthChallengeRequestTypeDef",
    "AuthChallengeResponseTypeDef",
    "BasicAuthConfigurationTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "BlockedPhrasesConfigurationTypeDef",
    "BlockedPhrasesConfigurationUpdateTypeDef",
    "ChatModeConfigurationTypeDef",
    "ChatSyncInputRequestTypeDef",
    "ChatSyncOutputTypeDef",
    "ContentBlockerRuleTypeDef",
    "ContentRetrievalRuleTypeDef",
    "ConversationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreatePluginRequestRequestTypeDef",
    "CreatePluginResponseTypeDef",
    "CreateRetrieverRequestRequestTypeDef",
    "CreateRetrieverResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateWebExperienceRequestRequestTypeDef",
    "CreateWebExperienceResponseTypeDef",
    "CreatorModeConfigurationTypeDef",
    "CustomPluginConfigurationTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DateAttributeBoostingConfigurationTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    "DeleteConversationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDocumentTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePluginRequestRequestTypeDef",
    "DeleteRetrieverRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWebExperienceRequestRequestTypeDef",
    "DocumentAttributeBoostingConfigurationTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeConfigurationTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentContentTypeDef",
    "DocumentDetailsTypeDef",
    "DocumentEnrichmentConfigurationTypeDef",
    "DocumentTypeDef",
    "EligibleDataSourceTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "FailedDocumentTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetChatControlsConfigurationRequestRequestTypeDef",
    "GetChatControlsConfigurationResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetIndexRequestRequestTypeDef",
    "GetIndexResponseTypeDef",
    "GetPluginRequestRequestTypeDef",
    "GetPluginResponseTypeDef",
    "GetRetrieverRequestRequestTypeDef",
    "GetRetrieverResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetWebExperienceRequestRequestTypeDef",
    "GetWebExperienceResponseTypeDef",
    "GroupMembersTypeDef",
    "GroupStatusDetailTypeDef",
    "GroupSummaryTypeDef",
    "HookConfigurationTypeDef",
    "IndexCapacityConfigurationTypeDef",
    "IndexStatisticsTypeDef",
    "IndexTypeDef",
    "InlineDocumentEnrichmentConfigurationTypeDef",
    "KendraIndexConfigurationTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListConversationsRequestRequestTypeDef",
    "ListConversationsResponseTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "ListDocumentsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListIndicesResponseTypeDef",
    "ListMessagesRequestRequestTypeDef",
    "ListMessagesResponseTypeDef",
    "ListPluginsRequestRequestTypeDef",
    "ListPluginsResponseTypeDef",
    "ListRetrieversRequestRequestTypeDef",
    "ListRetrieversResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebExperiencesRequestRequestTypeDef",
    "ListWebExperiencesResponseTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "MessageTypeDef",
    "MessageUsefulnessFeedbackTypeDef",
    "NativeIndexConfigurationTypeDef",
    "NumberAttributeBoostingConfigurationTypeDef",
    "OAuth2ClientCredentialConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PluginAuthConfigurationTypeDef",
    "PluginConfigurationTypeDef",
    "PluginTypeDef",
    "PrincipalGroupTypeDef",
    "PrincipalTypeDef",
    "PrincipalUserTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "PutGroupRequestRequestTypeDef",
    "QAppsConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieverConfigurationTypeDef",
    "RetrieverTypeDef",
    "RuleConfigurationTypeDef",
    "RuleTypeDef",
    "S3TypeDef",
    "SamlConfigurationTypeDef",
    "SnippetExcerptTypeDef",
    "SourceAttributionTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "StringAttributeBoostingConfigurationTypeDef",
    "StringListAttributeBoostingConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextSegmentTypeDef",
    "TopicConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateChatControlsConfigurationRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "UpdatePluginRequestRequestTypeDef",
    "UpdateRetrieverRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateWebExperienceRequestRequestTypeDef",
    "UserAliasTypeDef",
    "UsersAndGroupsTypeDef",
    "WebExperienceAuthConfigurationTypeDef",
    "WebExperienceTypeDef",
)

APISchemaTypeDef = TypedDict(
    "APISchemaTypeDef",
    {
        "payload": str,
        "s3": "S3TypeDef",
    },
    total=False,
)

_RequiredAccessConfigurationTypeDef = TypedDict(
    "_RequiredAccessConfigurationTypeDef",
    {
        "accessControls": List["AccessControlTypeDef"],
    },
)
_OptionalAccessConfigurationTypeDef = TypedDict(
    "_OptionalAccessConfigurationTypeDef",
    {
        "memberRelation": MemberRelationType,
    },
    total=False,
)

class AccessConfigurationTypeDef(
    _RequiredAccessConfigurationTypeDef, _OptionalAccessConfigurationTypeDef
):
    pass

_RequiredAccessControlTypeDef = TypedDict(
    "_RequiredAccessControlTypeDef",
    {
        "principals": List["PrincipalTypeDef"],
    },
)
_OptionalAccessControlTypeDef = TypedDict(
    "_OptionalAccessControlTypeDef",
    {
        "memberRelation": MemberRelationType,
    },
    total=False,
)

class AccessControlTypeDef(_RequiredAccessControlTypeDef, _OptionalAccessControlTypeDef):
    pass

ActionExecutionPayloadFieldTypeDef = TypedDict(
    "ActionExecutionPayloadFieldTypeDef",
    {
        "value": Dict[str, Any],
    },
)

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "pluginId": str,
        "payload": Dict[str, "ActionExecutionPayloadFieldTypeDef"],
        "payloadFieldNameSeparator": str,
    },
)

ActionReviewPayloadFieldAllowedValueTypeDef = TypedDict(
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    {
        "value": Dict[str, Any],
        "displayValue": Dict[str, Any],
    },
    total=False,
)

ActionReviewPayloadFieldTypeDef = TypedDict(
    "ActionReviewPayloadFieldTypeDef",
    {
        "displayName": str,
        "displayOrder": int,
        "displayDescription": str,
        "type": ActionPayloadFieldTypeType,
        "value": Dict[str, Any],
        "allowedValues": List["ActionReviewPayloadFieldAllowedValueTypeDef"],
        "allowedFormat": str,
        "required": bool,
    },
    total=False,
)

ActionReviewTypeDef = TypedDict(
    "ActionReviewTypeDef",
    {
        "pluginId": str,
        "pluginType": PluginTypeType,
        "payload": Dict[str, "ActionReviewPayloadFieldTypeDef"],
        "payloadFieldNameSeparator": str,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "displayName": str,
        "applicationId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": ApplicationStatusType,
    },
    total=False,
)

AppliedAttachmentsConfigurationTypeDef = TypedDict(
    "AppliedAttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": AttachmentsControlModeType,
    },
    total=False,
)

AppliedCreatorModeConfigurationTypeDef = TypedDict(
    "AppliedCreatorModeConfigurationTypeDef",
    {
        "creatorModeControl": CreatorModeControlType,
    },
)

AttachmentInputTypeDef = TypedDict(
    "AttachmentInputTypeDef",
    {
        "name": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
    },
)

AttachmentOutputTypeDef = TypedDict(
    "AttachmentOutputTypeDef",
    {
        "name": str,
        "status": AttachmentStatusType,
        "error": "ErrorDetailTypeDef",
    },
    total=False,
)

AttachmentsConfigurationTypeDef = TypedDict(
    "AttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": AttachmentsControlModeType,
    },
)

AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "andAllFilters": List[Dict[str, Any]],
        "orAllFilters": List[Dict[str, Any]],
        "notFilter": Dict[str, Any],
        "equalsTo": "DocumentAttributeTypeDef",
        "containsAll": "DocumentAttributeTypeDef",
        "containsAny": "DocumentAttributeTypeDef",
        "greaterThan": "DocumentAttributeTypeDef",
        "greaterThanOrEquals": "DocumentAttributeTypeDef",
        "lessThan": "DocumentAttributeTypeDef",
        "lessThanOrEquals": "DocumentAttributeTypeDef",
    },
    total=False,
)

AuthChallengeRequestTypeDef = TypedDict(
    "AuthChallengeRequestTypeDef",
    {
        "authorizationUrl": str,
    },
)

AuthChallengeResponseTypeDef = TypedDict(
    "AuthChallengeResponseTypeDef",
    {
        "responseMap": Dict[str, str],
    },
)

BasicAuthConfigurationTypeDef = TypedDict(
    "BasicAuthConfigurationTypeDef",
    {
        "secretArn": str,
        "roleArn": str,
    },
)

_RequiredBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "documents": List["DeleteDocumentTypeDef"],
    },
)
_OptionalBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteDocumentRequestRequestTypeDef",
    {
        "dataSourceSyncId": str,
    },
    total=False,
)

class BatchDeleteDocumentRequestRequestTypeDef(
    _RequiredBatchDeleteDocumentRequestRequestTypeDef,
    _OptionalBatchDeleteDocumentRequestRequestTypeDef,
):
    pass

BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "failedDocuments": List["FailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchPutDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "documents": List["DocumentTypeDef"],
    },
)
_OptionalBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchPutDocumentRequestRequestTypeDef",
    {
        "roleArn": str,
        "dataSourceSyncId": str,
    },
    total=False,
)

class BatchPutDocumentRequestRequestTypeDef(
    _RequiredBatchPutDocumentRequestRequestTypeDef, _OptionalBatchPutDocumentRequestRequestTypeDef
):
    pass

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "failedDocuments": List["FailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockedPhrasesConfigurationTypeDef = TypedDict(
    "BlockedPhrasesConfigurationTypeDef",
    {
        "blockedPhrases": List[str],
        "systemMessageOverride": str,
    },
    total=False,
)

BlockedPhrasesConfigurationUpdateTypeDef = TypedDict(
    "BlockedPhrasesConfigurationUpdateTypeDef",
    {
        "blockedPhrasesToCreateOrUpdate": List[str],
        "blockedPhrasesToDelete": List[str],
        "systemMessageOverride": str,
    },
    total=False,
)

ChatModeConfigurationTypeDef = TypedDict(
    "ChatModeConfigurationTypeDef",
    {
        "pluginConfiguration": "PluginConfigurationTypeDef",
    },
    total=False,
)

_RequiredChatSyncInputRequestTypeDef = TypedDict(
    "_RequiredChatSyncInputRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalChatSyncInputRequestTypeDef = TypedDict(
    "_OptionalChatSyncInputRequestTypeDef",
    {
        "userId": str,
        "userGroups": List[str],
        "userMessage": str,
        "attachments": List["AttachmentInputTypeDef"],
        "actionExecution": "ActionExecutionTypeDef",
        "authChallengeResponse": "AuthChallengeResponseTypeDef",
        "conversationId": str,
        "parentMessageId": str,
        "attributeFilter": "AttributeFilterTypeDef",
        "chatMode": ChatModeType,
        "chatModeConfiguration": "ChatModeConfigurationTypeDef",
        "clientToken": str,
    },
    total=False,
)

class ChatSyncInputRequestTypeDef(
    _RequiredChatSyncInputRequestTypeDef, _OptionalChatSyncInputRequestTypeDef
):
    pass

ChatSyncOutputTypeDef = TypedDict(
    "ChatSyncOutputTypeDef",
    {
        "conversationId": str,
        "systemMessage": str,
        "systemMessageId": str,
        "userMessageId": str,
        "actionReview": "ActionReviewTypeDef",
        "authChallengeRequest": "AuthChallengeRequestTypeDef",
        "sourceAttributions": List["SourceAttributionTypeDef"],
        "failedAttachments": List["AttachmentOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContentBlockerRuleTypeDef = TypedDict(
    "ContentBlockerRuleTypeDef",
    {
        "systemMessageOverride": str,
    },
    total=False,
)

ContentRetrievalRuleTypeDef = TypedDict(
    "ContentRetrievalRuleTypeDef",
    {
        "eligibleDataSources": List["EligibleDataSourceTypeDef"],
    },
    total=False,
)

ConversationTypeDef = TypedDict(
    "ConversationTypeDef",
    {
        "conversationId": str,
        "title": str,
        "startTime": datetime,
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "displayName": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "roleArn": str,
        "identityCenterInstanceArn": str,
        "description": str,
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "clientToken": str,
        "attachmentsConfiguration": "AttachmentsConfigurationTypeDef",
        "qAppsConfiguration": "QAppsConfigurationTypeDef",
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "displayName": str,
        "configuration": Dict[str, Any],
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "vpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "description": str,
        "tags": List["TagTypeDef"],
        "syncSchedule": str,
        "roleArn": str,
        "clientToken": str,
        "documentEnrichmentConfiguration": "DocumentEnrichmentConfigurationTypeDef",
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
        "dataSourceId": str,
        "dataSourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "displayName": str,
    },
)
_OptionalCreateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestRequestTypeDef",
    {
        "type": IndexTypeType,
        "description": str,
        "tags": List["TagTypeDef"],
        "capacityConfiguration": "IndexCapacityConfigurationTypeDef",
        "clientToken": str,
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
        "indexId": str,
        "indexArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePluginRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "displayName": str,
        "type": PluginTypeType,
        "authConfiguration": "PluginAuthConfigurationTypeDef",
    },
)
_OptionalCreatePluginRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePluginRequestRequestTypeDef",
    {
        "serverUrl": str,
        "customPluginConfiguration": "CustomPluginConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "clientToken": str,
    },
    total=False,
)

class CreatePluginRequestRequestTypeDef(
    _RequiredCreatePluginRequestRequestTypeDef, _OptionalCreatePluginRequestRequestTypeDef
):
    pass

CreatePluginResponseTypeDef = TypedDict(
    "CreatePluginResponseTypeDef",
    {
        "pluginId": str,
        "pluginArn": str,
        "buildStatus": PluginBuildStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRetrieverRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "type": RetrieverTypeType,
        "displayName": str,
        "configuration": "RetrieverConfigurationTypeDef",
    },
)
_OptionalCreateRetrieverRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRetrieverRequestRequestTypeDef",
    {
        "roleArn": str,
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRetrieverRequestRequestTypeDef(
    _RequiredCreateRetrieverRequestRequestTypeDef, _OptionalCreateRetrieverRequestRequestTypeDef
):
    pass

CreateRetrieverResponseTypeDef = TypedDict(
    "CreateRetrieverResponseTypeDef",
    {
        "retrieverId": str,
        "retrieverArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "userAliases": List["UserAliasTypeDef"],
        "clientToken": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

_RequiredCreateWebExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalCreateWebExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWebExperienceRequestRequestTypeDef",
    {
        "title": str,
        "subtitle": str,
        "welcomeMessage": str,
        "samplePromptsControlMode": WebExperienceSamplePromptsControlModeType,
        "roleArn": str,
        "tags": List["TagTypeDef"],
        "clientToken": str,
    },
    total=False,
)

class CreateWebExperienceRequestRequestTypeDef(
    _RequiredCreateWebExperienceRequestRequestTypeDef,
    _OptionalCreateWebExperienceRequestRequestTypeDef,
):
    pass

CreateWebExperienceResponseTypeDef = TypedDict(
    "CreateWebExperienceResponseTypeDef",
    {
        "webExperienceId": str,
        "webExperienceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatorModeConfigurationTypeDef = TypedDict(
    "CreatorModeConfigurationTypeDef",
    {
        "creatorModeControl": CreatorModeControlType,
    },
)

CustomPluginConfigurationTypeDef = TypedDict(
    "CustomPluginConfigurationTypeDef",
    {
        "description": str,
        "apiSchemaType": Literal["OPEN_API_V3"],
        "apiSchema": "APISchemaTypeDef",
    },
)

DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "documentsAdded": str,
        "documentsModified": str,
        "documentsDeleted": str,
        "documentsFailed": str,
        "documentsScanned": str,
    },
    total=False,
)

DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "executionId": str,
        "startTime": datetime,
        "endTime": datetime,
        "status": DataSourceSyncJobStatusType,
        "error": "ErrorDetailTypeDef",
        "dataSourceErrorCode": str,
        "metrics": "DataSourceSyncJobMetricsTypeDef",
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "displayName": str,
        "dataSourceId": str,
        "type": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": DataSourceStatusType,
    },
    total=False,
)

DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
)

_RequiredDateAttributeBoostingConfigurationTypeDef = TypedDict(
    "_RequiredDateAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
    },
)
_OptionalDateAttributeBoostingConfigurationTypeDef = TypedDict(
    "_OptionalDateAttributeBoostingConfigurationTypeDef",
    {
        "boostingDurationInSeconds": int,
    },
    total=False,
)

class DateAttributeBoostingConfigurationTypeDef(
    _RequiredDateAttributeBoostingConfigurationTypeDef,
    _OptionalDateAttributeBoostingConfigurationTypeDef,
):
    pass

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

DeleteChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

_RequiredDeleteConversationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteConversationRequestRequestTypeDef",
    {
        "conversationId": str,
        "applicationId": str,
    },
)
_OptionalDeleteConversationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteConversationRequestRequestTypeDef",
    {
        "userId": str,
    },
    total=False,
)

class DeleteConversationRequestRequestTypeDef(
    _RequiredDeleteConversationRequestRequestTypeDef,
    _OptionalDeleteConversationRequestRequestTypeDef,
):
    pass

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
    },
)

DeleteDocumentTypeDef = TypedDict(
    "DeleteDocumentTypeDef",
    {
        "documentId": str,
    },
)

_RequiredDeleteGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
    },
)
_OptionalDeleteGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteGroupRequestRequestTypeDef",
    {
        "dataSourceId": str,
    },
    total=False,
)

class DeleteGroupRequestRequestTypeDef(
    _RequiredDeleteGroupRequestRequestTypeDef, _OptionalDeleteGroupRequestRequestTypeDef
):
    pass

DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)

DeletePluginRequestRequestTypeDef = TypedDict(
    "DeletePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)

DeleteRetrieverRequestRequestTypeDef = TypedDict(
    "DeleteRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)

DeleteWebExperienceRequestRequestTypeDef = TypedDict(
    "DeleteWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)

DocumentAttributeBoostingConfigurationTypeDef = TypedDict(
    "DocumentAttributeBoostingConfigurationTypeDef",
    {
        "numberConfiguration": "NumberAttributeBoostingConfigurationTypeDef",
        "stringConfiguration": "StringAttributeBoostingConfigurationTypeDef",
        "dateConfiguration": "DateAttributeBoostingConfigurationTypeDef",
        "stringListConfiguration": "StringListAttributeBoostingConfigurationTypeDef",
    },
    total=False,
)

_RequiredDocumentAttributeConditionTypeDef = TypedDict(
    "_RequiredDocumentAttributeConditionTypeDef",
    {
        "key": str,
        "operator": DocumentEnrichmentConditionOperatorType,
    },
)
_OptionalDocumentAttributeConditionTypeDef = TypedDict(
    "_OptionalDocumentAttributeConditionTypeDef",
    {
        "value": "DocumentAttributeValueTypeDef",
    },
    total=False,
)

class DocumentAttributeConditionTypeDef(
    _RequiredDocumentAttributeConditionTypeDef, _OptionalDocumentAttributeConditionTypeDef
):
    pass

DocumentAttributeConfigurationTypeDef = TypedDict(
    "DocumentAttributeConfigurationTypeDef",
    {
        "name": str,
        "type": AttributeTypeType,
        "search": StatusType,
    },
    total=False,
)

_RequiredDocumentAttributeTargetTypeDef = TypedDict(
    "_RequiredDocumentAttributeTargetTypeDef",
    {
        "key": str,
    },
)
_OptionalDocumentAttributeTargetTypeDef = TypedDict(
    "_OptionalDocumentAttributeTargetTypeDef",
    {
        "value": "DocumentAttributeValueTypeDef",
        "attributeValueOperator": Literal["DELETE"],
    },
    total=False,
)

class DocumentAttributeTargetTypeDef(
    _RequiredDocumentAttributeTargetTypeDef, _OptionalDocumentAttributeTargetTypeDef
):
    pass

DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "name": str,
        "value": "DocumentAttributeValueTypeDef",
    },
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "stringValue": str,
        "stringListValue": List[str],
        "longValue": int,
        "dateValue": Union[datetime, str],
    },
    total=False,
)

DocumentContentTypeDef = TypedDict(
    "DocumentContentTypeDef",
    {
        "blob": Union[bytes, IO[bytes], StreamingBody],
        "s3": "S3TypeDef",
    },
    total=False,
)

DocumentDetailsTypeDef = TypedDict(
    "DocumentDetailsTypeDef",
    {
        "documentId": str,
        "status": DocumentStatusType,
        "error": "ErrorDetailTypeDef",
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

DocumentEnrichmentConfigurationTypeDef = TypedDict(
    "DocumentEnrichmentConfigurationTypeDef",
    {
        "inlineConfigurations": List["InlineDocumentEnrichmentConfigurationTypeDef"],
        "preExtractionHookConfiguration": "HookConfigurationTypeDef",
        "postExtractionHookConfiguration": "HookConfigurationTypeDef",
    },
    total=False,
)

_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "id": str,
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "attributes": List["DocumentAttributeTypeDef"],
        "content": "DocumentContentTypeDef",
        "contentType": ContentTypeType,
        "title": str,
        "accessConfiguration": "AccessConfigurationTypeDef",
        "documentEnrichmentConfiguration": "DocumentEnrichmentConfigurationTypeDef",
    },
    total=False,
)

class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass

EligibleDataSourceTypeDef = TypedDict(
    "EligibleDataSourceTypeDef",
    {
        "indexId": str,
        "dataSourceId": str,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorMessage": str,
        "errorCode": ErrorCodeType,
    },
    total=False,
)

FailedDocumentTypeDef = TypedDict(
    "FailedDocumentTypeDef",
    {
        "id": str,
        "error": "ErrorDetailTypeDef",
        "dataSourceId": str,
    },
    total=False,
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "displayName": str,
        "applicationId": str,
        "applicationArn": str,
        "identityCenterApplicationArn": str,
        "roleArn": str,
        "status": ApplicationStatusType,
        "description": str,
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
        "createdAt": datetime,
        "updatedAt": datetime,
        "error": "ErrorDetailTypeDef",
        "attachmentsConfiguration": "AppliedAttachmentsConfigurationTypeDef",
        "qAppsConfiguration": "QAppsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalGetChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetChatControlsConfigurationRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetChatControlsConfigurationRequestRequestTypeDef(
    _RequiredGetChatControlsConfigurationRequestRequestTypeDef,
    _OptionalGetChatControlsConfigurationRequestRequestTypeDef,
):
    pass

GetChatControlsConfigurationResponseTypeDef = TypedDict(
    "GetChatControlsConfigurationResponseTypeDef",
    {
        "responseScope": ResponseScopeType,
        "blockedPhrases": "BlockedPhrasesConfigurationTypeDef",
        "topicConfigurations": List["TopicConfigurationTypeDef"],
        "creatorModeConfiguration": "AppliedCreatorModeConfigurationTypeDef",
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
        "dataSourceArn": str,
        "displayName": str,
        "type": str,
        "configuration": Dict[str, Any],
        "vpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": str,
        "status": DataSourceStatusType,
        "syncSchedule": str,
        "roleArn": str,
        "error": "ErrorDetailTypeDef",
        "documentEnrichmentConfiguration": "DocumentEnrichmentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredGetGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
    },
)
_OptionalGetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalGetGroupRequestRequestTypeDef",
    {
        "dataSourceId": str,
    },
    total=False,
)

class GetGroupRequestRequestTypeDef(
    _RequiredGetGroupRequestRequestTypeDef, _OptionalGetGroupRequestRequestTypeDef
):
    pass

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "status": "GroupStatusDetailTypeDef",
        "statusHistory": List["GroupStatusDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIndexRequestRequestTypeDef = TypedDict(
    "GetIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)

GetIndexResponseTypeDef = TypedDict(
    "GetIndexResponseTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "displayName": str,
        "type": IndexTypeType,
        "indexArn": str,
        "status": IndexStatusType,
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityConfiguration": "IndexCapacityConfigurationTypeDef",
        "documentAttributeConfigurations": List["DocumentAttributeConfigurationTypeDef"],
        "error": "ErrorDetailTypeDef",
        "indexStatistics": "IndexStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPluginRequestRequestTypeDef = TypedDict(
    "GetPluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)

GetPluginResponseTypeDef = TypedDict(
    "GetPluginResponseTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
        "displayName": str,
        "type": PluginTypeType,
        "serverUrl": str,
        "authConfiguration": "PluginAuthConfigurationTypeDef",
        "customPluginConfiguration": "CustomPluginConfigurationTypeDef",
        "buildStatus": PluginBuildStatusType,
        "pluginArn": str,
        "state": PluginStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRetrieverRequestRequestTypeDef = TypedDict(
    "GetRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)

GetRetrieverResponseTypeDef = TypedDict(
    "GetRetrieverResponseTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
        "retrieverArn": str,
        "type": RetrieverTypeType,
        "status": RetrieverStatusType,
        "displayName": str,
        "configuration": "RetrieverConfigurationTypeDef",
        "roleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userAliases": List["UserAliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebExperienceRequestRequestTypeDef = TypedDict(
    "GetWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)

GetWebExperienceResponseTypeDef = TypedDict(
    "GetWebExperienceResponseTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
        "webExperienceArn": str,
        "defaultEndpoint": str,
        "status": WebExperienceStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "title": str,
        "subtitle": str,
        "welcomeMessage": str,
        "samplePromptsControlMode": WebExperienceSamplePromptsControlModeType,
        "roleArn": str,
        "authenticationConfiguration": "WebExperienceAuthConfigurationTypeDef",
        "error": "ErrorDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "memberGroups": List["MemberGroupTypeDef"],
        "memberUsers": List["MemberUserTypeDef"],
    },
    total=False,
)

GroupStatusDetailTypeDef = TypedDict(
    "GroupStatusDetailTypeDef",
    {
        "status": GroupStatusType,
        "lastUpdatedAt": datetime,
        "errorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "groupName": str,
    },
    total=False,
)

HookConfigurationTypeDef = TypedDict(
    "HookConfigurationTypeDef",
    {
        "invocationCondition": "DocumentAttributeConditionTypeDef",
        "lambdaArn": str,
        "s3BucketName": str,
        "roleArn": str,
    },
    total=False,
)

IndexCapacityConfigurationTypeDef = TypedDict(
    "IndexCapacityConfigurationTypeDef",
    {
        "units": int,
    },
    total=False,
)

IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "textDocumentStatistics": "TextDocumentStatisticsTypeDef",
    },
    total=False,
)

IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "displayName": str,
        "indexId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "status": IndexStatusType,
    },
    total=False,
)

InlineDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineDocumentEnrichmentConfigurationTypeDef",
    {
        "condition": "DocumentAttributeConditionTypeDef",
        "target": "DocumentAttributeTargetTypeDef",
        "documentContentOperator": Literal["DELETE"],
    },
    total=False,
)

KendraIndexConfigurationTypeDef = TypedDict(
    "KendraIndexConfigurationTypeDef",
    {
        "indexId": str,
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "nextToken": str,
        "applications": List["ApplicationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConversationsRequestRequestTypeDef = TypedDict(
    "_RequiredListConversationsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListConversationsRequestRequestTypeDef = TypedDict(
    "_OptionalListConversationsRequestRequestTypeDef",
    {
        "userId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListConversationsRequestRequestTypeDef(
    _RequiredListConversationsRequestRequestTypeDef, _OptionalListConversationsRequestRequestTypeDef
):
    pass

ListConversationsResponseTypeDef = TypedDict(
    "ListConversationsResponseTypeDef",
    {
        "nextToken": str,
        "conversations": List["ConversationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
    },
)
_OptionalListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "statusFilter": DataSourceSyncJobStatusType,
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
        "history": List["DataSourceSyncJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
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
        "dataSources": List["DataSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDocumentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDocumentsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
_OptionalListDocumentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDocumentsRequestRequestTypeDef",
    {
        "dataSourceIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDocumentsRequestRequestTypeDef(
    _RequiredListDocumentsRequestRequestTypeDef, _OptionalListDocumentsRequestRequestTypeDef
):
    pass

ListDocumentsResponseTypeDef = TypedDict(
    "ListDocumentsResponseTypeDef",
    {
        "documentDetailList": List["DocumentDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "updatedEarlierThan": Union[datetime, str],
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "nextToken": str,
        "items": List["GroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIndicesRequestRequestTypeDef = TypedDict(
    "_RequiredListIndicesRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListIndicesRequestRequestTypeDef = TypedDict(
    "_OptionalListIndicesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListIndicesRequestRequestTypeDef(
    _RequiredListIndicesRequestRequestTypeDef, _OptionalListIndicesRequestRequestTypeDef
):
    pass

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "nextToken": str,
        "indices": List["IndexTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMessagesRequestRequestTypeDef = TypedDict(
    "_RequiredListMessagesRequestRequestTypeDef",
    {
        "conversationId": str,
        "applicationId": str,
    },
)
_OptionalListMessagesRequestRequestTypeDef = TypedDict(
    "_OptionalListMessagesRequestRequestTypeDef",
    {
        "userId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListMessagesRequestRequestTypeDef(
    _RequiredListMessagesRequestRequestTypeDef, _OptionalListMessagesRequestRequestTypeDef
):
    pass

ListMessagesResponseTypeDef = TypedDict(
    "ListMessagesResponseTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPluginsRequestRequestTypeDef = TypedDict(
    "_RequiredListPluginsRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListPluginsRequestRequestTypeDef = TypedDict(
    "_OptionalListPluginsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPluginsRequestRequestTypeDef(
    _RequiredListPluginsRequestRequestTypeDef, _OptionalListPluginsRequestRequestTypeDef
):
    pass

ListPluginsResponseTypeDef = TypedDict(
    "ListPluginsResponseTypeDef",
    {
        "nextToken": str,
        "plugins": List["PluginTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRetrieversRequestRequestTypeDef = TypedDict(
    "_RequiredListRetrieversRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListRetrieversRequestRequestTypeDef = TypedDict(
    "_OptionalListRetrieversRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListRetrieversRequestRequestTypeDef(
    _RequiredListRetrieversRequestRequestTypeDef, _OptionalListRetrieversRequestRequestTypeDef
):
    pass

ListRetrieversResponseTypeDef = TypedDict(
    "ListRetrieversResponseTypeDef",
    {
        "retrievers": List["RetrieverTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebExperiencesRequestRequestTypeDef = TypedDict(
    "_RequiredListWebExperiencesRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalListWebExperiencesRequestRequestTypeDef = TypedDict(
    "_OptionalListWebExperiencesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListWebExperiencesRequestRequestTypeDef(
    _RequiredListWebExperiencesRequestRequestTypeDef,
    _OptionalListWebExperiencesRequestRequestTypeDef,
):
    pass

ListWebExperiencesResponseTypeDef = TypedDict(
    "ListWebExperiencesResponseTypeDef",
    {
        "webExperiences": List["WebExperienceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMemberGroupTypeDef = TypedDict(
    "_RequiredMemberGroupTypeDef",
    {
        "groupName": str,
    },
)
_OptionalMemberGroupTypeDef = TypedDict(
    "_OptionalMemberGroupTypeDef",
    {
        "type": MembershipTypeType,
    },
    total=False,
)

class MemberGroupTypeDef(_RequiredMemberGroupTypeDef, _OptionalMemberGroupTypeDef):
    pass

_RequiredMemberUserTypeDef = TypedDict(
    "_RequiredMemberUserTypeDef",
    {
        "userId": str,
    },
)
_OptionalMemberUserTypeDef = TypedDict(
    "_OptionalMemberUserTypeDef",
    {
        "type": MembershipTypeType,
    },
    total=False,
)

class MemberUserTypeDef(_RequiredMemberUserTypeDef, _OptionalMemberUserTypeDef):
    pass

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "body": str,
        "time": datetime,
        "type": MessageTypeType,
        "attachments": List["AttachmentOutputTypeDef"],
        "sourceAttribution": List["SourceAttributionTypeDef"],
        "actionReview": "ActionReviewTypeDef",
        "actionExecution": "ActionExecutionTypeDef",
    },
    total=False,
)

_RequiredMessageUsefulnessFeedbackTypeDef = TypedDict(
    "_RequiredMessageUsefulnessFeedbackTypeDef",
    {
        "usefulness": MessageUsefulnessType,
        "submittedAt": Union[datetime, str],
    },
)
_OptionalMessageUsefulnessFeedbackTypeDef = TypedDict(
    "_OptionalMessageUsefulnessFeedbackTypeDef",
    {
        "reason": MessageUsefulnessReasonType,
        "comment": str,
    },
    total=False,
)

class MessageUsefulnessFeedbackTypeDef(
    _RequiredMessageUsefulnessFeedbackTypeDef, _OptionalMessageUsefulnessFeedbackTypeDef
):
    pass

_RequiredNativeIndexConfigurationTypeDef = TypedDict(
    "_RequiredNativeIndexConfigurationTypeDef",
    {
        "indexId": str,
    },
)
_OptionalNativeIndexConfigurationTypeDef = TypedDict(
    "_OptionalNativeIndexConfigurationTypeDef",
    {
        "boostingOverride": Dict[str, "DocumentAttributeBoostingConfigurationTypeDef"],
    },
    total=False,
)

class NativeIndexConfigurationTypeDef(
    _RequiredNativeIndexConfigurationTypeDef, _OptionalNativeIndexConfigurationTypeDef
):
    pass

_RequiredNumberAttributeBoostingConfigurationTypeDef = TypedDict(
    "_RequiredNumberAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
    },
)
_OptionalNumberAttributeBoostingConfigurationTypeDef = TypedDict(
    "_OptionalNumberAttributeBoostingConfigurationTypeDef",
    {
        "boostingType": NumberAttributeBoostingTypeType,
    },
    total=False,
)

class NumberAttributeBoostingConfigurationTypeDef(
    _RequiredNumberAttributeBoostingConfigurationTypeDef,
    _OptionalNumberAttributeBoostingConfigurationTypeDef,
):
    pass

OAuth2ClientCredentialConfigurationTypeDef = TypedDict(
    "OAuth2ClientCredentialConfigurationTypeDef",
    {
        "secretArn": str,
        "roleArn": str,
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

PluginAuthConfigurationTypeDef = TypedDict(
    "PluginAuthConfigurationTypeDef",
    {
        "basicAuthConfiguration": "BasicAuthConfigurationTypeDef",
        "oAuth2ClientCredentialConfiguration": "OAuth2ClientCredentialConfigurationTypeDef",
        "noAuthConfiguration": Dict[str, Any],
    },
    total=False,
)

PluginConfigurationTypeDef = TypedDict(
    "PluginConfigurationTypeDef",
    {
        "pluginId": str,
    },
)

PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "pluginId": str,
        "displayName": str,
        "type": PluginTypeType,
        "serverUrl": str,
        "state": PluginStateType,
        "buildStatus": PluginBuildStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

_RequiredPrincipalGroupTypeDef = TypedDict(
    "_RequiredPrincipalGroupTypeDef",
    {
        "access": ReadAccessTypeType,
    },
)
_OptionalPrincipalGroupTypeDef = TypedDict(
    "_OptionalPrincipalGroupTypeDef",
    {
        "name": str,
        "membershipType": MembershipTypeType,
    },
    total=False,
)

class PrincipalGroupTypeDef(_RequiredPrincipalGroupTypeDef, _OptionalPrincipalGroupTypeDef):
    pass

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "user": "PrincipalUserTypeDef",
        "group": "PrincipalGroupTypeDef",
    },
    total=False,
)

_RequiredPrincipalUserTypeDef = TypedDict(
    "_RequiredPrincipalUserTypeDef",
    {
        "access": ReadAccessTypeType,
    },
)
_OptionalPrincipalUserTypeDef = TypedDict(
    "_OptionalPrincipalUserTypeDef",
    {
        "id": str,
        "membershipType": MembershipTypeType,
    },
    total=False,
)

class PrincipalUserTypeDef(_RequiredPrincipalUserTypeDef, _OptionalPrincipalUserTypeDef):
    pass

_RequiredPutFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredPutFeedbackRequestRequestTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "messageId": str,
    },
)
_OptionalPutFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalPutFeedbackRequestRequestTypeDef",
    {
        "userId": str,
        "messageCopiedAt": Union[datetime, str],
        "messageUsefulness": "MessageUsefulnessFeedbackTypeDef",
    },
    total=False,
)

class PutFeedbackRequestRequestTypeDef(
    _RequiredPutFeedbackRequestRequestTypeDef, _OptionalPutFeedbackRequestRequestTypeDef
):
    pass

_RequiredPutGroupRequestRequestTypeDef = TypedDict(
    "_RequiredPutGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
        "type": MembershipTypeType,
        "groupMembers": "GroupMembersTypeDef",
    },
)
_OptionalPutGroupRequestRequestTypeDef = TypedDict(
    "_OptionalPutGroupRequestRequestTypeDef",
    {
        "dataSourceId": str,
    },
    total=False,
)

class PutGroupRequestRequestTypeDef(
    _RequiredPutGroupRequestRequestTypeDef, _OptionalPutGroupRequestRequestTypeDef
):
    pass

QAppsConfigurationTypeDef = TypedDict(
    "QAppsConfigurationTypeDef",
    {
        "qAppsControlMode": QAppsControlModeType,
    },
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

RetrieverConfigurationTypeDef = TypedDict(
    "RetrieverConfigurationTypeDef",
    {
        "nativeIndexConfiguration": "NativeIndexConfigurationTypeDef",
        "kendraIndexConfiguration": "KendraIndexConfigurationTypeDef",
    },
    total=False,
)

RetrieverTypeDef = TypedDict(
    "RetrieverTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
        "type": RetrieverTypeType,
        "status": RetrieverStatusType,
        "displayName": str,
    },
    total=False,
)

RuleConfigurationTypeDef = TypedDict(
    "RuleConfigurationTypeDef",
    {
        "contentBlockerRule": "ContentBlockerRuleTypeDef",
        "contentRetrievalRule": "ContentRetrievalRuleTypeDef",
    },
    total=False,
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "ruleType": RuleTypeType,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "includedUsersAndGroups": "UsersAndGroupsTypeDef",
        "excludedUsersAndGroups": "UsersAndGroupsTypeDef",
        "ruleConfiguration": "RuleConfigurationTypeDef",
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

S3TypeDef = TypedDict(
    "S3TypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

_RequiredSamlConfigurationTypeDef = TypedDict(
    "_RequiredSamlConfigurationTypeDef",
    {
        "metadataXML": str,
        "roleArn": str,
        "userIdAttribute": str,
    },
)
_OptionalSamlConfigurationTypeDef = TypedDict(
    "_OptionalSamlConfigurationTypeDef",
    {
        "userGroupAttribute": str,
    },
    total=False,
)

class SamlConfigurationTypeDef(
    _RequiredSamlConfigurationTypeDef, _OptionalSamlConfigurationTypeDef
):
    pass

SnippetExcerptTypeDef = TypedDict(
    "SnippetExcerptTypeDef",
    {
        "text": str,
    },
    total=False,
)

SourceAttributionTypeDef = TypedDict(
    "SourceAttributionTypeDef",
    {
        "title": str,
        "snippet": str,
        "url": str,
        "citationNumber": int,
        "updatedAt": datetime,
        "textMessageSegments": List["TextSegmentTypeDef"],
    },
    total=False,
)

StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
    },
)

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "executionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
    },
)

_RequiredStringAttributeBoostingConfigurationTypeDef = TypedDict(
    "_RequiredStringAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
    },
)
_OptionalStringAttributeBoostingConfigurationTypeDef = TypedDict(
    "_OptionalStringAttributeBoostingConfigurationTypeDef",
    {
        "attributeValueBoosting": Dict[str, StringAttributeValueBoostingLevelType],
    },
    total=False,
)

class StringAttributeBoostingConfigurationTypeDef(
    _RequiredStringAttributeBoostingConfigurationTypeDef,
    _OptionalStringAttributeBoostingConfigurationTypeDef,
):
    pass

StringListAttributeBoostingConfigurationTypeDef = TypedDict(
    "StringListAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "indexedTextBytes": int,
        "indexedTextDocumentCount": int,
    },
    total=False,
)

TextSegmentTypeDef = TypedDict(
    "TextSegmentTypeDef",
    {
        "beginOffset": int,
        "endOffset": int,
        "snippetExcerpt": "SnippetExcerptTypeDef",
    },
    total=False,
)

_RequiredTopicConfigurationTypeDef = TypedDict(
    "_RequiredTopicConfigurationTypeDef",
    {
        "name": str,
        "rules": List["RuleTypeDef"],
    },
)
_OptionalTopicConfigurationTypeDef = TypedDict(
    "_OptionalTopicConfigurationTypeDef",
    {
        "description": str,
        "exampleChatMessages": List[str],
    },
    total=False,
)

class TopicConfigurationTypeDef(
    _RequiredTopicConfigurationTypeDef, _OptionalTopicConfigurationTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "identityCenterInstanceArn": str,
        "displayName": str,
        "description": str,
        "roleArn": str,
        "attachmentsConfiguration": "AttachmentsConfigurationTypeDef",
        "qAppsConfiguration": "QAppsConfigurationTypeDef",
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

_RequiredUpdateChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
_OptionalUpdateChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChatControlsConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "responseScope": ResponseScopeType,
        "blockedPhrasesConfigurationUpdate": "BlockedPhrasesConfigurationUpdateTypeDef",
        "topicConfigurationsToCreateOrUpdate": List["TopicConfigurationTypeDef"],
        "topicConfigurationsToDelete": List["TopicConfigurationTypeDef"],
        "creatorModeConfiguration": "CreatorModeConfigurationTypeDef",
    },
    total=False,
)

class UpdateChatControlsConfigurationRequestRequestTypeDef(
    _RequiredUpdateChatControlsConfigurationRequestRequestTypeDef,
    _OptionalUpdateChatControlsConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "displayName": str,
        "configuration": Dict[str, Any],
        "vpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "description": str,
        "syncSchedule": str,
        "roleArn": str,
        "documentEnrichmentConfiguration": "DocumentEnrichmentConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

_RequiredUpdateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
_OptionalUpdateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIndexRequestRequestTypeDef",
    {
        "displayName": str,
        "description": str,
        "capacityConfiguration": "IndexCapacityConfigurationTypeDef",
        "documentAttributeConfigurations": List["DocumentAttributeConfigurationTypeDef"],
    },
    total=False,
)

class UpdateIndexRequestRequestTypeDef(
    _RequiredUpdateIndexRequestRequestTypeDef, _OptionalUpdateIndexRequestRequestTypeDef
):
    pass

_RequiredUpdatePluginRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)
_OptionalUpdatePluginRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePluginRequestRequestTypeDef",
    {
        "displayName": str,
        "state": PluginStateType,
        "serverUrl": str,
        "customPluginConfiguration": "CustomPluginConfigurationTypeDef",
        "authConfiguration": "PluginAuthConfigurationTypeDef",
    },
    total=False,
)

class UpdatePluginRequestRequestTypeDef(
    _RequiredUpdatePluginRequestRequestTypeDef, _OptionalUpdatePluginRequestRequestTypeDef
):
    pass

_RequiredUpdateRetrieverRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)
_OptionalUpdateRetrieverRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRetrieverRequestRequestTypeDef",
    {
        "configuration": "RetrieverConfigurationTypeDef",
        "displayName": str,
        "roleArn": str,
    },
    total=False,
)

class UpdateRetrieverRequestRequestTypeDef(
    _RequiredUpdateRetrieverRequestRequestTypeDef, _OptionalUpdateRetrieverRequestRequestTypeDef
):
    pass

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "userAliasesToUpdate": List["UserAliasTypeDef"],
        "userAliasesToDelete": List["UserAliasTypeDef"],
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userAliasesAdded": List["UserAliasTypeDef"],
        "userAliasesUpdated": List["UserAliasTypeDef"],
        "userAliasesDeleted": List["UserAliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)
_OptionalUpdateWebExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWebExperienceRequestRequestTypeDef",
    {
        "roleArn": str,
        "authenticationConfiguration": "WebExperienceAuthConfigurationTypeDef",
        "title": str,
        "subtitle": str,
        "welcomeMessage": str,
        "samplePromptsControlMode": WebExperienceSamplePromptsControlModeType,
    },
    total=False,
)

class UpdateWebExperienceRequestRequestTypeDef(
    _RequiredUpdateWebExperienceRequestRequestTypeDef,
    _OptionalUpdateWebExperienceRequestRequestTypeDef,
):
    pass

_RequiredUserAliasTypeDef = TypedDict(
    "_RequiredUserAliasTypeDef",
    {
        "userId": str,
    },
)
_OptionalUserAliasTypeDef = TypedDict(
    "_OptionalUserAliasTypeDef",
    {
        "indexId": str,
        "dataSourceId": str,
    },
    total=False,
)

class UserAliasTypeDef(_RequiredUserAliasTypeDef, _OptionalUserAliasTypeDef):
    pass

UsersAndGroupsTypeDef = TypedDict(
    "UsersAndGroupsTypeDef",
    {
        "userIds": List[str],
        "userGroups": List[str],
    },
    total=False,
)

WebExperienceAuthConfigurationTypeDef = TypedDict(
    "WebExperienceAuthConfigurationTypeDef",
    {
        "samlConfiguration": "SamlConfigurationTypeDef",
    },
    total=False,
)

WebExperienceTypeDef = TypedDict(
    "WebExperienceTypeDef",
    {
        "webExperienceId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "defaultEndpoint": str,
        "status": WebExperienceStatusType,
    },
    total=False,
)
