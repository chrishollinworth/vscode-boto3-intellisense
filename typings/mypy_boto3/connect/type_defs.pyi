"""
Type annotations for connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AgentContactReferenceTypeDef

    data: AgentContactReferenceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentStatusStateType,
    AgentStatusTypeType,
    ChannelType,
    ContactFlowModuleStateType,
    ContactFlowModuleStatusType,
    ContactFlowStateType,
    ContactFlowTypeType,
    ContactInitiationMethodType,
    ContactStateType,
    CurrentMetricNameType,
    DirectoryTypeType,
    GroupingType,
    HierarchyGroupMatchTypeType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InstanceAttributeTypeType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneNumberWorkflowStatusType,
    PhoneTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    ReferenceStatusType,
    ReferenceTypeType,
    SourceTypeType,
    StatisticType,
    StorageTypeType,
    StringComparisonTypeType,
    TaskTemplateFieldTypeType,
    TaskTemplateStatusType,
    TrafficTypeType,
    UnitType,
    UseCaseTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
    VoiceRecordingTrackType,
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
    "AgentContactReferenceTypeDef",
    "AgentInfoTypeDef",
    "AgentStatusReferenceTypeDef",
    "AgentStatusSummaryTypeDef",
    "AgentStatusTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "AssociateApprovedOriginRequestRequestTypeDef",
    "AssociateBotRequestRequestTypeDef",
    "AssociateDefaultVocabularyRequestRequestTypeDef",
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateLambdaFunctionRequestRequestTypeDef",
    "AssociateLexBotRequestRequestTypeDef",
    "AssociatePhoneNumberContactFlowRequestRequestTypeDef",
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    "AssociateSecurityKeyRequestRequestTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AttachmentReferenceTypeDef",
    "AttributeTypeDef",
    "AvailableNumberSummaryTypeDef",
    "ChatMessageTypeDef",
    "ChatStreamingConfigurationTypeDef",
    "ClaimPhoneNumberRequestRequestTypeDef",
    "ClaimPhoneNumberResponseTypeDef",
    "ClaimedPhoneNumberSummaryTypeDef",
    "ContactFilterTypeDef",
    "ContactFlowModuleSummaryTypeDef",
    "ContactFlowModuleTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "ContactTypeDef",
    "ControlPlaneTagFilterTypeDef",
    "CreateAgentStatusRequestRequestTypeDef",
    "CreateAgentStatusResponseTypeDef",
    "CreateContactFlowModuleRequestRequestTypeDef",
    "CreateContactFlowModuleResponseTypeDef",
    "CreateContactFlowRequestRequestTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateHoursOfOperationRequestRequestTypeDef",
    "CreateHoursOfOperationResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationRequestRequestTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectRequestRequestTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileRequestRequestTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateSecurityProfileRequestRequestTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateTaskTemplateRequestRequestTypeDef",
    "CreateTaskTemplateResponseTypeDef",
    "CreateUseCaseRequestRequestTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupRequestRequestTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DateReferenceTypeDef",
    "DefaultVocabularyTypeDef",
    "DeleteContactFlowModuleRequestRequestTypeDef",
    "DeleteContactFlowRequestRequestTypeDef",
    "DeleteHoursOfOperationRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    "DeleteQuickConnectRequestRequestTypeDef",
    "DeleteSecurityProfileRequestRequestTypeDef",
    "DeleteTaskTemplateRequestRequestTypeDef",
    "DeleteUseCaseRequestRequestTypeDef",
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DeleteVocabularyResponseTypeDef",
    "DescribeAgentStatusRequestRequestTypeDef",
    "DescribeAgentStatusResponseTypeDef",
    "DescribeContactFlowModuleRequestRequestTypeDef",
    "DescribeContactFlowModuleResponseTypeDef",
    "DescribeContactFlowRequestRequestTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeContactResponseTypeDef",
    "DescribeHoursOfOperationRequestRequestTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribePhoneNumberRequestRequestTypeDef",
    "DescribePhoneNumberResponseTypeDef",
    "DescribeQueueRequestRequestTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectRequestRequestTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileRequestRequestTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeSecurityProfileRequestRequestTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeVocabularyRequestRequestTypeDef",
    "DescribeVocabularyResponseTypeDef",
    "DimensionsTypeDef",
    "DisassociateApprovedOriginRequestRequestTypeDef",
    "DisassociateBotRequestRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    "DisassociateLexBotRequestRequestTypeDef",
    "DisassociatePhoneNumberContactFlowRequestRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    "DisassociateSecurityKeyRequestRequestTypeDef",
    "EmailReferenceTypeDef",
    "EncryptionConfigTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesRequestRequestTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataRequestRequestTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetCurrentUserDataRequestRequestTypeDef",
    "GetCurrentUserDataResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataRequestRequestTypeDef",
    "GetMetricDataResponseTypeDef",
    "GetTaskTemplateRequestRequestTypeDef",
    "GetTaskTemplateResponseTypeDef",
    "HierarchyGroupConditionTypeDef",
    "HierarchyGroupSummaryReferenceTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathReferenceTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "InvisibleFieldInfoTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotTypeDef",
    "LexV2BotTypeDef",
    "ListAgentStatusRequestRequestTypeDef",
    "ListAgentStatusResponseTypeDef",
    "ListApprovedOriginsRequestRequestTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListContactFlowModulesRequestRequestTypeDef",
    "ListContactFlowModulesResponseTypeDef",
    "ListContactFlowsRequestRequestTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListContactReferencesRequestRequestTypeDef",
    "ListContactReferencesResponseTypeDef",
    "ListDefaultVocabulariesRequestRequestTypeDef",
    "ListDefaultVocabulariesResponseTypeDef",
    "ListHoursOfOperationsRequestRequestTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesRequestRequestTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsRequestRequestTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsRequestRequestTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsRequestRequestTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsRequestRequestTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPhoneNumbersSummaryTypeDef",
    "ListPhoneNumbersV2RequestRequestTypeDef",
    "ListPhoneNumbersV2ResponseTypeDef",
    "ListPromptsRequestRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsRequestRequestTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsRequestRequestTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRoutingProfileQueuesRequestRequestTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesRequestRequestTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListSecurityKeysRequestRequestTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfilePermissionsRequestRequestTypeDef",
    "ListSecurityProfilePermissionsResponseTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskTemplatesRequestRequestTypeDef",
    "ListTaskTemplatesResponseTypeDef",
    "ListUseCasesRequestRequestTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsRequestRequestTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MediaConcurrencyTypeDef",
    "NumberReferenceTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberStatusTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSummaryTypeDef",
    "PutUserStatusRequestRequestTypeDef",
    "QueueInfoTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReadOnlyFieldInfoTypeDef",
    "ReferenceSummaryTypeDef",
    "ReferenceTypeDef",
    "ReleasePhoneNumberRequestRequestTypeDef",
    "RequiredFieldInfoTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestRequestTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SearchSecurityProfilesRequestRequestTypeDef",
    "SearchSecurityProfilesResponseTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "SearchVocabulariesRequestRequestTypeDef",
    "SearchVocabulariesResponseTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSearchCriteriaTypeDef",
    "SecurityProfileSearchSummaryTypeDef",
    "SecurityProfileSummaryTypeDef",
    "SecurityProfileTypeDef",
    "SecurityProfilesSearchFilterTypeDef",
    "StartChatContactRequestRequestTypeDef",
    "StartChatContactResponseTypeDef",
    "StartContactRecordingRequestRequestTypeDef",
    "StartContactStreamingRequestRequestTypeDef",
    "StartContactStreamingResponseTypeDef",
    "StartOutboundVoiceContactRequestRequestTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactRequestRequestTypeDef",
    "StartTaskContactResponseTypeDef",
    "StopContactRecordingRequestRequestTypeDef",
    "StopContactRequestRequestTypeDef",
    "StopContactStreamingRequestRequestTypeDef",
    "StringConditionTypeDef",
    "StringReferenceTypeDef",
    "SuspendContactRecordingRequestRequestTypeDef",
    "TagConditionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTemplateConstraintsTypeDef",
    "TaskTemplateDefaultFieldValueTypeDef",
    "TaskTemplateDefaultsTypeDef",
    "TaskTemplateFieldIdentifierTypeDef",
    "TaskTemplateFieldTypeDef",
    "TaskTemplateMetadataTypeDef",
    "ThresholdTypeDef",
    "TransferContactRequestRequestTypeDef",
    "TransferContactResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentStatusRequestRequestTypeDef",
    "UpdateContactAttributesRequestRequestTypeDef",
    "UpdateContactFlowContentRequestRequestTypeDef",
    "UpdateContactFlowMetadataRequestRequestTypeDef",
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    "UpdateContactFlowModuleMetadataRequestRequestTypeDef",
    "UpdateContactFlowNameRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateContactScheduleRequestRequestTypeDef",
    "UpdateHoursOfOperationRequestRequestTypeDef",
    "UpdateInstanceAttributeRequestRequestTypeDef",
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    "UpdateQueueMaxContactsRequestRequestTypeDef",
    "UpdateQueueNameRequestRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    "UpdateQueueStatusRequestRequestTypeDef",
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    "UpdateQuickConnectNameRequestRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    "UpdateRoutingProfileNameRequestRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    "UpdateSecurityProfileRequestRequestTypeDef",
    "UpdateTaskTemplateRequestRequestTypeDef",
    "UpdateTaskTemplateResponseTypeDef",
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    "UpdateUserHierarchyRequestRequestTypeDef",
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    "UrlReferenceTypeDef",
    "UseCaseTypeDef",
    "UserDataFiltersTypeDef",
    "UserDataTypeDef",
    "UserIdentityInfoLiteTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserReferenceTypeDef",
    "UserSearchCriteriaTypeDef",
    "UserSearchFilterTypeDef",
    "UserSearchSummaryTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VocabularySummaryTypeDef",
    "VocabularyTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

AgentContactReferenceTypeDef = TypedDict(
    "AgentContactReferenceTypeDef",
    {
        "ContactId": str,
        "Channel": ChannelType,
        "InitiationMethod": ContactInitiationMethodType,
        "AgentContactState": ContactStateType,
        "StateStartTimestamp": datetime,
        "ConnectedToAgentTimestamp": datetime,
        "Queue": "QueueReferenceTypeDef",
    },
    total=False,
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "Id": str,
        "ConnectedToAgentTimestamp": datetime,
    },
    total=False,
)

AgentStatusReferenceTypeDef = TypedDict(
    "AgentStatusReferenceTypeDef",
    {
        "StatusStartTimestamp": datetime,
        "StatusArn": str,
    },
    total=False,
)

AgentStatusSummaryTypeDef = TypedDict(
    "AgentStatusSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": AgentStatusTypeType,
    },
    total=False,
)

AgentStatusTypeDef = TypedDict(
    "AgentStatusTypeDef",
    {
        "AgentStatusARN": str,
        "AgentStatusId": str,
        "Name": str,
        "Description": str,
        "Type": AgentStatusTypeType,
        "DisplayOrder": int,
        "State": AgentStatusStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

AnswerMachineDetectionConfigTypeDef = TypedDict(
    "AnswerMachineDetectionConfigTypeDef",
    {
        "EnableAnswerMachineDetection": bool,
        "AwaitAnswerMachinePrompt": bool,
    },
    total=False,
)

AssociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "AssociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredAssociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalAssociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

class AssociateBotRequestRequestTypeDef(
    _RequiredAssociateBotRequestRequestTypeDef, _OptionalAssociateBotRequestRequestTypeDef
):
    pass

_RequiredAssociateDefaultVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateDefaultVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
    },
)
_OptionalAssociateDefaultVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateDefaultVocabularyRequestRequestTypeDef",
    {
        "VocabularyId": str,
    },
    total=False,
)

class AssociateDefaultVocabularyRequestRequestTypeDef(
    _RequiredAssociateDefaultVocabularyRequestRequestTypeDef,
    _OptionalAssociateDefaultVocabularyRequestRequestTypeDef,
):
    pass

AssociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "AssociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

AssociateInstanceStorageConfigResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "AssociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

AssociateLexBotRequestRequestTypeDef = TypedDict(
    "AssociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": "LexBotTypeDef",
    },
)

AssociatePhoneNumberContactFlowRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumberContactFlowRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

AssociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "AssociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

AssociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "AssociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

AssociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "AssociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Key": str,
    },
)

AssociateSecurityKeyResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentReferenceTypeDef = TypedDict(
    "AttachmentReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
        "Status": ReferenceStatusType,
    },
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
    total=False,
)

AvailableNumberSummaryTypeDef = TypedDict(
    "AvailableNumberSummaryTypeDef",
    {
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
    },
    total=False,
)

ChatMessageTypeDef = TypedDict(
    "ChatMessageTypeDef",
    {
        "ContentType": str,
        "Content": str,
    },
)

ChatStreamingConfigurationTypeDef = TypedDict(
    "ChatStreamingConfigurationTypeDef",
    {
        "StreamingEndpointArn": str,
    },
)

_RequiredClaimPhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredClaimPhoneNumberRequestRequestTypeDef",
    {
        "TargetArn": str,
        "PhoneNumber": str,
    },
)
_OptionalClaimPhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalClaimPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberDescription": str,
        "Tags": Dict[str, str],
        "ClientToken": str,
    },
    total=False,
)

class ClaimPhoneNumberRequestRequestTypeDef(
    _RequiredClaimPhoneNumberRequestRequestTypeDef, _OptionalClaimPhoneNumberRequestRequestTypeDef
):
    pass

ClaimPhoneNumberResponseTypeDef = TypedDict(
    "ClaimPhoneNumberResponseTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClaimedPhoneNumberSummaryTypeDef = TypedDict(
    "ClaimedPhoneNumberSummaryTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberDescription": str,
        "TargetArn": str,
        "Tags": Dict[str, str],
        "PhoneNumberStatus": "PhoneNumberStatusTypeDef",
    },
    total=False,
)

ContactFilterTypeDef = TypedDict(
    "ContactFilterTypeDef",
    {
        "ContactStates": List[ContactStateType],
    },
    total=False,
)

ContactFlowModuleSummaryTypeDef = TypedDict(
    "ContactFlowModuleSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "State": ContactFlowModuleStateType,
    },
    total=False,
)

ContactFlowModuleTypeDef = TypedDict(
    "ContactFlowModuleTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Content": str,
        "Description": str,
        "State": ContactFlowModuleStateType,
        "Status": ContactFlowModuleStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": ContactFlowTypeType,
        "ContactFlowState": ContactFlowStateType,
    },
    total=False,
)

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "State": ContactFlowStateType,
        "Description": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "Arn": str,
        "Id": str,
        "InitialContactId": str,
        "PreviousContactId": str,
        "InitiationMethod": ContactInitiationMethodType,
        "Name": str,
        "Description": str,
        "Channel": ChannelType,
        "QueueInfo": "QueueInfoTypeDef",
        "AgentInfo": "AgentInfoTypeDef",
        "InitiationTimestamp": datetime,
        "DisconnectTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ScheduledTimestamp": datetime,
    },
    total=False,
)

ControlPlaneTagFilterTypeDef = TypedDict(
    "ControlPlaneTagFilterTypeDef",
    {
        "OrConditions": List[List["TagConditionTypeDef"]],
        "AndConditions": List["TagConditionTypeDef"],
        "TagCondition": "TagConditionTypeDef",
    },
    total=False,
)

_RequiredCreateAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "State": AgentStatusStateType,
    },
)
_OptionalCreateAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentStatusRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayOrder": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAgentStatusRequestRequestTypeDef(
    _RequiredCreateAgentStatusRequestRequestTypeDef, _OptionalCreateAgentStatusRequestRequestTypeDef
):
    pass

CreateAgentStatusResponseTypeDef = TypedDict(
    "CreateAgentStatusResponseTypeDef",
    {
        "AgentStatusARN": str,
        "AgentStatusId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactFlowModuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Content": str,
    },
)
_OptionalCreateContactFlowModuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowModuleRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
        "ClientToken": str,
    },
    total=False,
)

class CreateContactFlowModuleRequestRequestTypeDef(
    _RequiredCreateContactFlowModuleRequestRequestTypeDef,
    _OptionalCreateContactFlowModuleRequestRequestTypeDef,
):
    pass

CreateContactFlowModuleResponseTypeDef = TypedDict(
    "CreateContactFlowModuleResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
    },
)
_OptionalCreateContactFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateContactFlowRequestRequestTypeDef(
    _RequiredCreateContactFlowRequestRequestTypeDef, _OptionalCreateContactFlowRequestRequestTypeDef
):
    pass

CreateContactFlowResponseTypeDef = TypedDict(
    "CreateContactFlowResponseTypeDef",
    {
        "ContactFlowId": str,
        "ContactFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
    },
)
_OptionalCreateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHoursOfOperationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateHoursOfOperationRequestRequestTypeDef(
    _RequiredCreateHoursOfOperationRequestRequestTypeDef,
    _OptionalCreateHoursOfOperationRequestRequestTypeDef,
):
    pass

CreateHoursOfOperationResponseTypeDef = TypedDict(
    "CreateHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceRequestRequestTypeDef",
    {
        "IdentityManagementType": DirectoryTypeType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
)
_OptionalCreateInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceAlias": str,
        "DirectoryId": str,
    },
    total=False,
)

class CreateInstanceRequestRequestTypeDef(
    _RequiredCreateInstanceRequestRequestTypeDef, _OptionalCreateInstanceRequestRequestTypeDef
):
    pass

CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationArn": str,
    },
)
_OptionalCreateIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationAssociationRequestRequestTypeDef",
    {
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateIntegrationAssociationRequestRequestTypeDef(
    _RequiredCreateIntegrationAssociationRequestRequestTypeDef,
    _OptionalCreateIntegrationAssociationRequestRequestTypeDef,
):
    pass

CreateIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "HoursOfOperationId": str,
    },
)
_OptionalCreateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestRequestTypeDef",
    {
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "MaxContacts": int,
        "QuickConnectIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateQueueRequestRequestTypeDef(
    _RequiredCreateQueueRequestRequestTypeDef, _OptionalCreateQueueRequestRequestTypeDef
):
    pass

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "QueueArn": str,
        "QueueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)
_OptionalCreateQuickConnectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuickConnectRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateQuickConnectRequestRequestTypeDef(
    _RequiredCreateQuickConnectRequestRequestTypeDef,
    _OptionalCreateQuickConnectRequestRequestTypeDef,
):
    pass

CreateQuickConnectResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Description": str,
        "DefaultOutboundQueueId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)
_OptionalCreateRoutingProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoutingProfileRequestRequestTypeDef",
    {
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRoutingProfileRequestRequestTypeDef(
    _RequiredCreateRoutingProfileRequestRequestTypeDef,
    _OptionalCreateRoutingProfileRequestRequestTypeDef,
):
    pass

CreateRoutingProfileResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseTypeDef",
    {
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileName": str,
        "InstanceId": str,
    },
)
_OptionalCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityProfileRequestRequestTypeDef",
    {
        "Description": str,
        "Permissions": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateSecurityProfileRequestRequestTypeDef(
    _RequiredCreateSecurityProfileRequestRequestTypeDef,
    _OptionalCreateSecurityProfileRequestRequestTypeDef,
):
    pass

CreateSecurityProfileResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseTypeDef",
    {
        "SecurityProfileId": str,
        "SecurityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Fields": List["TaskTemplateFieldTypeDef"],
    },
)
_OptionalCreateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTaskTemplateRequestRequestTypeDef",
    {
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Status": TaskTemplateStatusType,
        "ClientToken": str,
    },
    total=False,
)

class CreateTaskTemplateRequestRequestTypeDef(
    _RequiredCreateTaskTemplateRequestRequestTypeDef,
    _OptionalCreateTaskTemplateRequestRequestTypeDef,
):
    pass

CreateTaskTemplateResponseTypeDef = TypedDict(
    "CreateTaskTemplateResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseType": UseCaseTypeType,
    },
)
_OptionalCreateUseCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUseCaseRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateUseCaseRequestRequestTypeDef(
    _RequiredCreateUseCaseRequestRequestTypeDef, _OptionalCreateUseCaseRequestRequestTypeDef
):
    pass

CreateUseCaseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserHierarchyGroupRequestRequestTypeDef",
    {
        "ParentGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateUserHierarchyGroupRequestRequestTypeDef(
    _RequiredCreateUserHierarchyGroupRequestRequestTypeDef,
    _OptionalCreateUserHierarchyGroupRequestRequestTypeDef,
):
    pass

CreateUserHierarchyGroupResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroupId": str,
        "HierarchyGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Password": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyName": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "Content": str,
    },
)
_OptionalCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateVocabularyRequestRequestTypeDef(
    _RequiredCreateVocabularyRequestRequestTypeDef, _OptionalCreateVocabularyRequestRequestTypeDef
):
    pass

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef",
    {
        "Metric": "CurrentMetricTypeDef",
        "Value": float,
    },
    total=False,
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["CurrentMetricDataTypeDef"],
    },
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": CurrentMetricNameType,
        "Unit": UnitType,
    },
    total=False,
)

DateReferenceTypeDef = TypedDict(
    "DateReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

DefaultVocabularyTypeDef = TypedDict(
    "DefaultVocabularyTypeDef",
    {
        "InstanceId": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "VocabularyId": str,
        "VocabularyName": str,
    },
)

DeleteContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DeleteContactFlowRequestRequestTypeDef = TypedDict(
    "DeleteContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DeleteHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DeleteHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeleteIntegrationAssociationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationAssociationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)

DeleteQuickConnectRequestRequestTypeDef = TypedDict(
    "DeleteQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "DeleteSecurityProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SecurityProfileId": str,
    },
)

DeleteTaskTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TaskTemplateId": str,
    },
)

DeleteUseCaseRequestRequestTypeDef = TypedDict(
    "DeleteUseCaseRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseId": str,
    },
)

DeleteUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DeleteUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "InstanceId": str,
        "UserId": str,
    },
)

DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DeleteVocabularyResponseTypeDef = TypedDict(
    "DeleteVocabularyResponseTypeDef",
    {
        "VocabularyArn": str,
        "VocabularyId": str,
        "State": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAgentStatusRequestRequestTypeDef = TypedDict(
    "DescribeAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
    },
)

DescribeAgentStatusResponseTypeDef = TypedDict(
    "DescribeAgentStatusResponseTypeDef",
    {
        "AgentStatus": "AgentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowModuleRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowModuleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)

DescribeContactFlowModuleResponseTypeDef = TypedDict(
    "DescribeContactFlowModuleResponseTypeDef",
    {
        "ContactFlowModule": "ContactFlowModuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactFlowRequestRequestTypeDef = TypedDict(
    "DescribeContactFlowRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DescribeContactFlowResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseTypeDef",
    {
        "ContactFlow": "ContactFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHoursOfOperationRequestRequestTypeDef = TypedDict(
    "DescribeHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DescribeHoursOfOperationResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseTypeDef",
    {
        "HoursOfOperation": "HoursOfOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
    },
)

DescribeInstanceAttributeResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseTypeDef",
    {
        "Attribute": "AttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DescribeInstanceStorageConfigResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseTypeDef",
    {
        "StorageConfig": "InstanceStorageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePhoneNumberRequestRequestTypeDef = TypedDict(
    "DescribePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DescribePhoneNumberResponseTypeDef = TypedDict(
    "DescribePhoneNumberResponseTypeDef",
    {
        "ClaimedPhoneNumberSummary": "ClaimedPhoneNumberSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueueRequestRequestTypeDef = TypedDict(
    "DescribeQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DescribeQueueResponseTypeDef = TypedDict(
    "DescribeQueueResponseTypeDef",
    {
        "Queue": "QueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuickConnectRequestRequestTypeDef = TypedDict(
    "DescribeQuickConnectRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DescribeQuickConnectResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseTypeDef",
    {
        "QuickConnect": "QuickConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingProfileRequestRequestTypeDef = TypedDict(
    "DescribeRoutingProfileRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DescribeRoutingProfileResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseTypeDef",
    {
        "RoutingProfile": "RoutingProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)

DescribeSecurityProfileResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseTypeDef",
    {
        "SecurityProfile": "SecurityProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyGroupRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyGroupRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {
        "HierarchyGroup": "HierarchyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "DescribeUserHierarchyStructureRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVocabularyRequestRequestTypeDef = TypedDict(
    "DescribeVocabularyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VocabularyId": str,
    },
)

DescribeVocabularyResponseTypeDef = TypedDict(
    "DescribeVocabularyResponseTypeDef",
    {
        "Vocabulary": "VocabularyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {
        "Queue": "QueueReferenceTypeDef",
        "Channel": ChannelType,
    },
    total=False,
)

DisassociateApprovedOriginRequestRequestTypeDef = TypedDict(
    "DisassociateApprovedOriginRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredDisassociateBotRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateBotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDisassociateBotRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateBotRequestRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

class DisassociateBotRequestRequestTypeDef(
    _RequiredDisassociateBotRequestRequestTypeDef, _OptionalDisassociateBotRequestRequestTypeDef
):
    pass

DisassociateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "DisassociateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DisassociateLambdaFunctionRequestRequestTypeDef = TypedDict(
    "DisassociateLambdaFunctionRequestRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

DisassociateLexBotRequestRequestTypeDef = TypedDict(
    "DisassociateLexBotRequestRequestTypeDef",
    {
        "InstanceId": str,
        "BotName": str,
        "LexRegion": str,
    },
)

DisassociatePhoneNumberContactFlowRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberContactFlowRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "InstanceId": str,
    },
)

DisassociateQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "DisassociateQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

DisassociateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "DisassociateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueReferences": List["RoutingProfileQueueReferenceTypeDef"],
    },
)

DisassociateSecurityKeyRequestRequestTypeDef = TypedDict(
    "DisassociateSecurityKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
    },
)

EmailReferenceTypeDef = TypedDict(
    "EmailReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "Queues": List[str],
        "Channels": List[ChannelType],
    },
    total=False,
)

GetContactAttributesRequestRequestTypeDef = TypedDict(
    "GetContactAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InitialContactId": str,
    },
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetCurrentMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "FiltersTypeDef",
        "CurrentMetrics": List["CurrentMetricTypeDef"],
    },
)
_OptionalGetCurrentMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetCurrentMetricDataRequestRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetCurrentMetricDataRequestRequestTypeDef(
    _RequiredGetCurrentMetricDataRequestRequestTypeDef,
    _OptionalGetCurrentMetricDataRequestRequestTypeDef,
):
    pass

GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentUserDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetCurrentUserDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "UserDataFiltersTypeDef",
    },
)
_OptionalGetCurrentUserDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetCurrentUserDataRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetCurrentUserDataRequestRequestTypeDef(
    _RequiredGetCurrentUserDataRequestRequestTypeDef,
    _OptionalGetCurrentUserDataRequestRequestTypeDef,
):
    pass

GetCurrentUserDataResponseTypeDef = TypedDict(
    "GetCurrentUserDataResponseTypeDef",
    {
        "NextToken": str,
        "UserDataList": List["UserDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": List["HistoricalMetricTypeDef"],
    },
)
_OptionalGetMetricDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataRequestRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetMetricDataRequestRequestTypeDef(
    _RequiredGetMetricDataRequestRequestTypeDef, _OptionalGetMetricDataRequestRequestTypeDef
):
    pass

GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["HistoricalMetricResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetTaskTemplateRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TaskTemplateId": str,
    },
)
_OptionalGetTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetTaskTemplateRequestRequestTypeDef",
    {
        "SnapshotVersion": str,
    },
    total=False,
)

class GetTaskTemplateRequestRequestTypeDef(
    _RequiredGetTaskTemplateRequestRequestTypeDef, _OptionalGetTaskTemplateRequestRequestTypeDef
):
    pass

GetTaskTemplateResponseTypeDef = TypedDict(
    "GetTaskTemplateResponseTypeDef",
    {
        "InstanceId": str,
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Fields": List["TaskTemplateFieldTypeDef"],
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HierarchyGroupConditionTypeDef = TypedDict(
    "HierarchyGroupConditionTypeDef",
    {
        "Value": str,
        "HierarchyGroupMatchType": HierarchyGroupMatchTypeType,
    },
    total=False,
)

HierarchyGroupSummaryReferenceTypeDef = TypedDict(
    "HierarchyGroupSummaryReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": "HierarchyPathTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyLevelUpdateTypeDef = TypedDict(
    "HierarchyLevelUpdateTypeDef",
    {
        "Name": str,
    },
)

HierarchyPathReferenceTypeDef = TypedDict(
    "HierarchyPathReferenceTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelTwo": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelThree": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelFour": "HierarchyGroupSummaryReferenceTypeDef",
        "LevelFive": "HierarchyGroupSummaryReferenceTypeDef",
    },
    total=False,
)

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryTypeDef",
        "LevelTwo": "HierarchyGroupSummaryTypeDef",
        "LevelThree": "HierarchyGroupSummaryTypeDef",
        "LevelFour": "HierarchyGroupSummaryTypeDef",
        "LevelFive": "HierarchyGroupSummaryTypeDef",
    },
    total=False,
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": "HierarchyLevelTypeDef",
        "LevelTwo": "HierarchyLevelTypeDef",
        "LevelThree": "HierarchyLevelTypeDef",
        "LevelFour": "HierarchyLevelTypeDef",
        "LevelFive": "HierarchyLevelTypeDef",
    },
    total=False,
)

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": "HierarchyLevelUpdateTypeDef",
        "LevelTwo": "HierarchyLevelUpdateTypeDef",
        "LevelThree": "HierarchyLevelUpdateTypeDef",
        "LevelFour": "HierarchyLevelUpdateTypeDef",
        "LevelFive": "HierarchyLevelUpdateTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {
        "Metric": "HistoricalMetricTypeDef",
        "Value": float,
    },
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["HistoricalMetricDataTypeDef"],
    },
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": HistoricalMetricNameType,
        "Threshold": "ThresholdTypeDef",
        "Statistic": StatisticType,
        "Unit": UnitType,
    },
    total=False,
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredInstanceStorageConfigTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigTypeDef",
    {
        "StorageType": StorageTypeType,
    },
)
_OptionalInstanceStorageConfigTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigTypeDef",
    },
    total=False,
)

class InstanceStorageConfigTypeDef(
    _RequiredInstanceStorageConfigTypeDef, _OptionalInstanceStorageConfigTypeDef
):
    pass

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "StatusReason": "InstanceStatusReasonTypeDef",
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "InstanceId": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
    total=False,
)

InvisibleFieldInfoTypeDef = TypedDict(
    "InvisibleFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
    total=False,
)

KinesisFirehoseConfigTypeDef = TypedDict(
    "KinesisFirehoseConfigTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
)

LexBotConfigTypeDef = TypedDict(
    "LexBotConfigTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

LexBotTypeDef = TypedDict(
    "LexBotTypeDef",
    {
        "Name": str,
        "LexRegion": str,
    },
    total=False,
)

LexV2BotTypeDef = TypedDict(
    "LexV2BotTypeDef",
    {
        "AliasArn": str,
    },
    total=False,
)

_RequiredListAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentStatusRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AgentStatusTypes": List[AgentStatusTypeType],
    },
    total=False,
)

class ListAgentStatusRequestRequestTypeDef(
    _RequiredListAgentStatusRequestRequestTypeDef, _OptionalListAgentStatusRequestRequestTypeDef
):
    pass

ListAgentStatusResponseTypeDef = TypedDict(
    "ListAgentStatusResponseTypeDef",
    {
        "NextToken": str,
        "AgentStatusSummaryList": List["AgentStatusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_RequiredListApprovedOriginsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListApprovedOriginsRequestRequestTypeDef = TypedDict(
    "_OptionalListApprovedOriginsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListApprovedOriginsRequestRequestTypeDef(
    _RequiredListApprovedOriginsRequestRequestTypeDef,
    _OptionalListApprovedOriginsRequestRequestTypeDef,
):
    pass

ListApprovedOriginsResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseTypeDef",
    {
        "Origins": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
    },
)
_OptionalListBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListBotsRequestRequestTypeDef(
    _RequiredListBotsRequestRequestTypeDef, _OptionalListBotsRequestRequestTypeDef
):
    pass

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "LexBots": List["LexBotConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowModulesRequestRequestTypeDef = TypedDict(
    "_RequiredListContactFlowModulesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowModulesRequestRequestTypeDef = TypedDict(
    "_OptionalListContactFlowModulesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ContactFlowModuleState": ContactFlowModuleStateType,
    },
    total=False,
)

class ListContactFlowModulesRequestRequestTypeDef(
    _RequiredListContactFlowModulesRequestRequestTypeDef,
    _OptionalListContactFlowModulesRequestRequestTypeDef,
):
    pass

ListContactFlowModulesResponseTypeDef = TypedDict(
    "ListContactFlowModulesResponseTypeDef",
    {
        "ContactFlowModulesSummaryList": List["ContactFlowModuleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactFlowsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactFlowsRequestRequestTypeDef",
    {
        "ContactFlowTypes": List[ContactFlowTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListContactFlowsRequestRequestTypeDef(
    _RequiredListContactFlowsRequestRequestTypeDef, _OptionalListContactFlowsRequestRequestTypeDef
):
    pass

ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredListContactReferencesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ReferenceTypes": List[ReferenceTypeType],
    },
)
_OptionalListContactReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalListContactReferencesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListContactReferencesRequestRequestTypeDef(
    _RequiredListContactReferencesRequestRequestTypeDef,
    _OptionalListContactReferencesRequestRequestTypeDef,
):
    pass

ListContactReferencesResponseTypeDef = TypedDict(
    "ListContactReferencesResponseTypeDef",
    {
        "ReferenceSummaryList": List["ReferenceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDefaultVocabulariesRequestRequestTypeDef = TypedDict(
    "_RequiredListDefaultVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListDefaultVocabulariesRequestRequestTypeDef = TypedDict(
    "_OptionalListDefaultVocabulariesRequestRequestTypeDef",
    {
        "LanguageCode": VocabularyLanguageCodeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDefaultVocabulariesRequestRequestTypeDef(
    _RequiredListDefaultVocabulariesRequestRequestTypeDef,
    _OptionalListDefaultVocabulariesRequestRequestTypeDef,
):
    pass

ListDefaultVocabulariesResponseTypeDef = TypedDict(
    "ListDefaultVocabulariesResponseTypeDef",
    {
        "DefaultVocabularyList": List["DefaultVocabularyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListHoursOfOperationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListHoursOfOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListHoursOfOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListHoursOfOperationsRequestRequestTypeDef(
    _RequiredListHoursOfOperationsRequestRequestTypeDef,
    _OptionalListHoursOfOperationsRequestRequestTypeDef,
):
    pass

ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListInstanceAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInstanceAttributesRequestRequestTypeDef(
    _RequiredListInstanceAttributesRequestRequestTypeDef,
    _OptionalListInstanceAttributesRequestRequestTypeDef,
):
    pass

ListInstanceAttributesResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)
_OptionalListInstanceStorageConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstanceStorageConfigsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInstanceStorageConfigsRequestRequestTypeDef(
    _RequiredListInstanceStorageConfigsRequestRequestTypeDef,
    _OptionalListInstanceStorageConfigsRequestRequestTypeDef,
):
    pass

ListInstanceStorageConfigsResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseTypeDef",
    {
        "StorageConfigs": List["InstanceStorageConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaryList": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListIntegrationAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListIntegrationAssociationsRequestRequestTypeDef",
    {
        "IntegrationType": IntegrationTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLambdaFunctionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLambdaFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLambdaFunctionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLambdaFunctionsRequestRequestTypeDef(
    _RequiredListLambdaFunctionsRequestRequestTypeDef,
    _OptionalListLambdaFunctionsRequestRequestTypeDef,
):
    pass

ListLambdaFunctionsResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseTypeDef",
    {
        "LambdaFunctions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLexBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListLexBotsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLexBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListLexBotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLexBotsRequestRequestTypeDef(
    _RequiredListLexBotsRequestRequestTypeDef, _OptionalListLexBotsRequestRequestTypeDef
):
    pass

ListLexBotsResponseTypeDef = TypedDict(
    "ListLexBotsResponseTypeDef",
    {
        "LexBots": List["LexBotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredListPhoneNumbersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalListPhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberTypes": List[PhoneNumberTypeType],
        "PhoneNumberCountryCodes": List[PhoneNumberCountryCodeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPhoneNumbersRequestRequestTypeDef(
    _RequiredListPhoneNumbersRequestRequestTypeDef, _OptionalListPhoneNumbersRequestRequestTypeDef
):
    pass

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersSummaryTypeDef = TypedDict(
    "ListPhoneNumbersSummaryTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
        "TargetArn": str,
    },
    total=False,
)

ListPhoneNumbersV2RequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersV2RequestRequestTypeDef",
    {
        "TargetArn": str,
        "MaxResults": int,
        "NextToken": str,
        "PhoneNumberCountryCodes": List[PhoneNumberCountryCodeType],
        "PhoneNumberTypes": List[PhoneNumberTypeType],
        "PhoneNumberPrefix": str,
    },
    total=False,
)

ListPhoneNumbersV2ResponseTypeDef = TypedDict(
    "ListPhoneNumbersV2ResponseTypeDef",
    {
        "NextToken": str,
        "ListPhoneNumbersSummaryList": List["ListPhoneNumbersSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPromptsRequestRequestTypeDef = TypedDict(
    "_RequiredListPromptsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPromptsRequestRequestTypeDef = TypedDict(
    "_OptionalListPromptsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPromptsRequestRequestTypeDef(
    _RequiredListPromptsRequestRequestTypeDef, _OptionalListPromptsRequestRequestTypeDef
):
    pass

ListPromptsResponseTypeDef = TypedDict(
    "ListPromptsResponseTypeDef",
    {
        "PromptSummaryList": List["PromptSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQueueQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalListQueueQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQueueQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQueueQuickConnectsRequestRequestTypeDef(
    _RequiredListQueueQuickConnectsRequestRequestTypeDef,
    _OptionalListQueueQuickConnectsRequestRequestTypeDef,
):
    pass

ListQueueQuickConnectsResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseTypeDef",
    {
        "NextToken": str,
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListQueuesRequestRequestTypeDef",
    {
        "QueueTypes": List[QueueTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListQueuesRequestRequestTypeDef(
    _RequiredListQueuesRequestRequestTypeDef, _OptionalListQueuesRequestRequestTypeDef
):
    pass

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "QueueSummaryList": List["QueueSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_RequiredListQuickConnectsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQuickConnectsRequestRequestTypeDef = TypedDict(
    "_OptionalListQuickConnectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "QuickConnectTypes": List[QuickConnectTypeType],
    },
    total=False,
)

class ListQuickConnectsRequestRequestTypeDef(
    _RequiredListQuickConnectsRequestRequestTypeDef, _OptionalListQuickConnectsRequestRequestTypeDef
):
    pass

ListQuickConnectsResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseTypeDef",
    {
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalListRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfileQueuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRoutingProfileQueuesRequestRequestTypeDef(
    _RequiredListRoutingProfileQueuesRequestRequestTypeDef,
    _OptionalListRoutingProfileQueuesRequestRequestTypeDef,
):
    pass

ListRoutingProfileQueuesResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRoutingProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRoutingProfilesRequestRequestTypeDef(
    _RequiredListRoutingProfilesRequestRequestTypeDef,
    _OptionalListRoutingProfilesRequestRequestTypeDef,
):
    pass

ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityKeysRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityKeysRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSecurityKeysRequestRequestTypeDef(
    _RequiredListSecurityKeysRequestRequestTypeDef, _OptionalListSecurityKeysRequestRequestTypeDef
):
    pass

ListSecurityKeysResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseTypeDef",
    {
        "SecurityKeys": List["SecurityKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilePermissionsRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilePermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSecurityProfilePermissionsRequestRequestTypeDef(
    _RequiredListSecurityProfilePermissionsRequestRequestTypeDef,
    _OptionalListSecurityProfilePermissionsRequestRequestTypeDef,
):
    pass

ListSecurityProfilePermissionsResponseTypeDef = TypedDict(
    "ListSecurityProfilePermissionsResponseTypeDef",
    {
        "Permissions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSecurityProfilesRequestRequestTypeDef(
    _RequiredListSecurityProfilesRequestRequestTypeDef,
    _OptionalListSecurityProfilesRequestRequestTypeDef,
):
    pass

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"],
        "NextToken": str,
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

_RequiredListTaskTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTaskTemplatesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListTaskTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTaskTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": TaskTemplateStatusType,
        "Name": str,
    },
    total=False,
)

class ListTaskTemplatesRequestRequestTypeDef(
    _RequiredListTaskTemplatesRequestRequestTypeDef, _OptionalListTaskTemplatesRequestRequestTypeDef
):
    pass

ListTaskTemplatesResponseTypeDef = TypedDict(
    "ListTaskTemplatesResponseTypeDef",
    {
        "TaskTemplates": List["TaskTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUseCasesRequestRequestTypeDef = TypedDict(
    "_RequiredListUseCasesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)
_OptionalListUseCasesRequestRequestTypeDef = TypedDict(
    "_OptionalListUseCasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUseCasesRequestRequestTypeDef(
    _RequiredListUseCasesRequestRequestTypeDef, _OptionalListUseCasesRequestRequestTypeDef
):
    pass

ListUseCasesResponseTypeDef = TypedDict(
    "ListUseCasesResponseTypeDef",
    {
        "UseCaseSummaryList": List["UseCaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUserHierarchyGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserHierarchyGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUserHierarchyGroupsRequestRequestTypeDef(
    _RequiredListUserHierarchyGroupsRequestRequestTypeDef,
    _OptionalListUserHierarchyGroupsRequestRequestTypeDef,
):
    pass

ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserSummaryList": List["UserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaConcurrencyTypeDef = TypedDict(
    "MediaConcurrencyTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)

NumberReferenceTypeDef = TypedDict(
    "NumberReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {
        "OutboundCallerIdName": str,
        "OutboundCallerIdNumberId": str,
        "OutboundFlowId": str,
    },
    total=False,
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

ParticipantDetailsTypeDef = TypedDict(
    "ParticipantDetailsTypeDef",
    {
        "DisplayName": str,
    },
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberStatusTypeDef = TypedDict(
    "PhoneNumberStatusTypeDef",
    {
        "Status": PhoneNumberWorkflowStatusType,
        "Message": str,
    },
    total=False,
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
    },
    total=False,
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

PutUserStatusRequestRequestTypeDef = TypedDict(
    "PutUserStatusRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
        "AgentStatusId": str,
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "Id": str,
        "EnqueueTimestamp": datetime,
    },
    total=False,
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueReferenceTypeDef = TypedDict(
    "QueueReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QueueType": QueueTypeType,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "QueueArn": str,
        "QueueId": str,
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "HoursOfOperationId": str,
        "MaxContacts": int,
        "Status": QueueStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredQuickConnectConfigTypeDef = TypedDict(
    "_RequiredQuickConnectConfigTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
    },
)
_OptionalQuickConnectConfigTypeDef = TypedDict(
    "_OptionalQuickConnectConfigTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigTypeDef",
        "QueueConfig": "QueueQuickConnectConfigTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigTypeDef",
    },
    total=False,
)

class QuickConnectConfigTypeDef(
    _RequiredQuickConnectConfigTypeDef, _OptionalQuickConnectConfigTypeDef
):
    pass

QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QuickConnectType": QuickConnectTypeType,
    },
    total=False,
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "Name": str,
        "Description": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ReadOnlyFieldInfoTypeDef = TypedDict(
    "ReadOnlyFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
    total=False,
)

ReferenceSummaryTypeDef = TypedDict(
    "ReferenceSummaryTypeDef",
    {
        "Url": "UrlReferenceTypeDef",
        "Attachment": "AttachmentReferenceTypeDef",
        "String": "StringReferenceTypeDef",
        "Number": "NumberReferenceTypeDef",
        "Date": "DateReferenceTypeDef",
        "Email": "EmailReferenceTypeDef",
    },
    total=False,
)

ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Value": str,
        "Type": ReferenceTypeType,
    },
)

_RequiredReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredReleasePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalReleasePhoneNumberRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class ReleasePhoneNumberRequestRequestTypeDef(
    _RequiredReleasePhoneNumberRequestRequestTypeDef,
    _OptionalReleasePhoneNumberRequestRequestTypeDef,
):
    pass

RequiredFieldInfoTypeDef = TypedDict(
    "RequiredFieldInfoTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
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

ResumeContactRecordingRequestRequestTypeDef = TypedDict(
    "ResumeContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": ChannelType,
    },
)

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {
        "QueueReference": "RoutingProfileQueueReferenceTypeDef",
        "Priority": int,
        "Delay": int,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef",
    {
        "QueueId": str,
        "Channel": ChannelType,
    },
)

RoutingProfileReferenceTypeDef = TypedDict(
    "RoutingProfileReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "Description": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
        "DefaultOutboundQueueId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

_RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "TargetArn": str,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
        "PhoneNumberType": PhoneNumberTypeType,
    },
)
_OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberPrefix": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SearchAvailablePhoneNumbersRequestRequestTypeDef(
    _RequiredSearchAvailablePhoneNumbersRequestRequestTypeDef,
    _OptionalSearchAvailablePhoneNumbersRequestRequestTypeDef,
):
    pass

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "NextToken": str,
        "AvailableNumbersList": List["AvailableNumberSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchSecurityProfilesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchSecurityProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchSecurityProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SearchCriteria": "SecurityProfileSearchCriteriaTypeDef",
        "SearchFilter": "SecurityProfilesSearchFilterTypeDef",
    },
    total=False,
)

class SearchSecurityProfilesRequestRequestTypeDef(
    _RequiredSearchSecurityProfilesRequestRequestTypeDef,
    _OptionalSearchSecurityProfilesRequestRequestTypeDef,
):
    pass

SearchSecurityProfilesResponseTypeDef = TypedDict(
    "SearchSecurityProfilesResponseTypeDef",
    {
        "SecurityProfiles": List["SecurityProfileSearchSummaryTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchUsersRequestRequestTypeDef = TypedDict(
    "SearchUsersRequestRequestTypeDef",
    {
        "InstanceId": str,
        "NextToken": str,
        "MaxResults": int,
        "SearchFilter": "UserSearchFilterTypeDef",
        "SearchCriteria": "UserSearchCriteriaTypeDef",
    },
    total=False,
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "Users": List["UserSearchSummaryTypeDef"],
        "NextToken": str,
        "ApproximateTotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchVocabulariesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchVocabulariesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSearchVocabulariesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchVocabulariesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "State": VocabularyStateType,
        "NameStartsWith": str,
        "LanguageCode": VocabularyLanguageCodeType,
    },
    total=False,
)

class SearchVocabulariesRequestRequestTypeDef(
    _RequiredSearchVocabulariesRequestRequestTypeDef,
    _OptionalSearchVocabulariesRequestRequestTypeDef,
):
    pass

SearchVocabulariesResponseTypeDef = TypedDict(
    "SearchVocabulariesResponseTypeDef",
    {
        "VocabularySummaryList": List["VocabularySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef",
    {
        "AssociationId": str,
        "Key": str,
        "CreationTime": datetime,
    },
    total=False,
)

SecurityProfileSearchCriteriaTypeDef = TypedDict(
    "SecurityProfileSearchCriteriaTypeDef",
    {
        "OrConditions": List[Dict[str, Any]],
        "AndConditions": List[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
    },
    total=False,
)

SecurityProfileSearchSummaryTypeDef = TypedDict(
    "SecurityProfileSearchSummaryTypeDef",
    {
        "Id": str,
        "OrganizationResourceId": str,
        "Arn": str,
        "SecurityProfileName": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

SecurityProfileTypeDef = TypedDict(
    "SecurityProfileTypeDef",
    {
        "Id": str,
        "OrganizationResourceId": str,
        "Arn": str,
        "SecurityProfileName": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

SecurityProfilesSearchFilterTypeDef = TypedDict(
    "SecurityProfilesSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

_RequiredStartChatContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartChatContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "ParticipantDetails": "ParticipantDetailsTypeDef",
    },
)
_OptionalStartChatContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartChatContactRequestRequestTypeDef",
    {
        "Attributes": Dict[str, str],
        "InitialMessage": "ChatMessageTypeDef",
        "ClientToken": str,
        "ChatDurationInMinutes": int,
        "SupportedMessagingContentTypes": List[str],
    },
    total=False,
)

class StartChatContactRequestRequestTypeDef(
    _RequiredStartChatContactRequestRequestTypeDef, _OptionalStartChatContactRequestRequestTypeDef
):
    pass

StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {
        "ContactId": str,
        "ParticipantId": str,
        "ParticipantToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContactRecordingRequestRequestTypeDef = TypedDict(
    "StartContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
        "VoiceRecordingConfiguration": "VoiceRecordingConfigurationTypeDef",
    },
)

StartContactStreamingRequestRequestTypeDef = TypedDict(
    "StartContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ChatStreamingConfiguration": "ChatStreamingConfigurationTypeDef",
        "ClientToken": str,
    },
)

StartContactStreamingResponseTypeDef = TypedDict(
    "StartContactStreamingResponseTypeDef",
    {
        "StreamingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "ContactFlowId": str,
        "InstanceId": str,
    },
)
_OptionalStartOutboundVoiceContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartOutboundVoiceContactRequestRequestTypeDef",
    {
        "ClientToken": str,
        "SourcePhoneNumber": str,
        "QueueId": str,
        "Attributes": Dict[str, str],
        "AnswerMachineDetectionConfig": "AnswerMachineDetectionConfigTypeDef",
        "CampaignId": str,
        "TrafficType": TrafficTypeType,
    },
    total=False,
)

class StartOutboundVoiceContactRequestRequestTypeDef(
    _RequiredStartOutboundVoiceContactRequestRequestTypeDef,
    _OptionalStartOutboundVoiceContactRequestRequestTypeDef,
):
    pass

StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTaskContactRequestRequestTypeDef = TypedDict(
    "_RequiredStartTaskContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
    },
)
_OptionalStartTaskContactRequestRequestTypeDef = TypedDict(
    "_OptionalStartTaskContactRequestRequestTypeDef",
    {
        "PreviousContactId": str,
        "ContactFlowId": str,
        "Attributes": Dict[str, str],
        "References": Dict[str, "ReferenceTypeDef"],
        "Description": str,
        "ClientToken": str,
        "ScheduledTime": Union[datetime, str],
        "TaskTemplateId": str,
        "QuickConnectId": str,
    },
    total=False,
)

class StartTaskContactRequestRequestTypeDef(
    _RequiredStartTaskContactRequestRequestTypeDef, _OptionalStartTaskContactRequestRequestTypeDef
):
    pass

StartTaskContactResponseTypeDef = TypedDict(
    "StartTaskContactResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContactRecordingRequestRequestTypeDef = TypedDict(
    "StopContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

StopContactRequestRequestTypeDef = TypedDict(
    "StopContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "InstanceId": str,
    },
)

StopContactStreamingRequestRequestTypeDef = TypedDict(
    "StopContactStreamingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "StreamingId": str,
    },
)

StringConditionTypeDef = TypedDict(
    "StringConditionTypeDef",
    {
        "FieldName": str,
        "Value": str,
        "ComparisonType": StringComparisonTypeType,
    },
    total=False,
)

StringReferenceTypeDef = TypedDict(
    "StringReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

SuspendContactRecordingRequestRequestTypeDef = TypedDict(
    "SuspendContactRecordingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

TagConditionTypeDef = TypedDict(
    "TagConditionTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TaskTemplateConstraintsTypeDef = TypedDict(
    "TaskTemplateConstraintsTypeDef",
    {
        "RequiredFields": List["RequiredFieldInfoTypeDef"],
        "ReadOnlyFields": List["ReadOnlyFieldInfoTypeDef"],
        "InvisibleFields": List["InvisibleFieldInfoTypeDef"],
    },
    total=False,
)

TaskTemplateDefaultFieldValueTypeDef = TypedDict(
    "TaskTemplateDefaultFieldValueTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
        "DefaultValue": str,
    },
    total=False,
)

TaskTemplateDefaultsTypeDef = TypedDict(
    "TaskTemplateDefaultsTypeDef",
    {
        "DefaultFieldValues": List["TaskTemplateDefaultFieldValueTypeDef"],
    },
    total=False,
)

TaskTemplateFieldIdentifierTypeDef = TypedDict(
    "TaskTemplateFieldIdentifierTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredTaskTemplateFieldTypeDef = TypedDict(
    "_RequiredTaskTemplateFieldTypeDef",
    {
        "Id": "TaskTemplateFieldIdentifierTypeDef",
    },
)
_OptionalTaskTemplateFieldTypeDef = TypedDict(
    "_OptionalTaskTemplateFieldTypeDef",
    {
        "Description": str,
        "Type": TaskTemplateFieldTypeType,
        "SingleSelectOptions": List[str],
    },
    total=False,
)

class TaskTemplateFieldTypeDef(
    _RequiredTaskTemplateFieldTypeDef, _OptionalTaskTemplateFieldTypeDef
):
    pass

TaskTemplateMetadataTypeDef = TypedDict(
    "TaskTemplateMetadataTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Comparison": Literal["LT"],
        "ThresholdValue": float,
    },
    total=False,
)

_RequiredTransferContactRequestRequestTypeDef = TypedDict(
    "_RequiredTransferContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ContactFlowId": str,
    },
)
_OptionalTransferContactRequestRequestTypeDef = TypedDict(
    "_OptionalTransferContactRequestRequestTypeDef",
    {
        "QueueId": str,
        "UserId": str,
        "ClientToken": str,
    },
    total=False,
)

class TransferContactRequestRequestTypeDef(
    _RequiredTransferContactRequestRequestTypeDef, _OptionalTransferContactRequestRequestTypeDef
):
    pass

TransferContactResponseTypeDef = TypedDict(
    "TransferContactResponseTypeDef",
    {
        "ContactId": str,
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AgentStatusId": str,
    },
)
_OptionalUpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentStatusRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": AgentStatusStateType,
        "DisplayOrder": int,
        "ResetOrderNumber": bool,
    },
    total=False,
)

class UpdateAgentStatusRequestRequestTypeDef(
    _RequiredUpdateAgentStatusRequestRequestTypeDef, _OptionalUpdateAgentStatusRequestRequestTypeDef
):
    pass

UpdateContactAttributesRequestRequestTypeDef = TypedDict(
    "UpdateContactAttributesRequestRequestTypeDef",
    {
        "InitialContactId": str,
        "InstanceId": str,
        "Attributes": Dict[str, str],
    },
)

UpdateContactFlowContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ContactFlowState": ContactFlowStateType,
    },
    total=False,
)

class UpdateContactFlowMetadataRequestRequestTypeDef(
    _RequiredUpdateContactFlowMetadataRequestRequestTypeDef,
    _OptionalUpdateContactFlowMetadataRequestRequestTypeDef,
):
    pass

UpdateContactFlowModuleContentRequestRequestTypeDef = TypedDict(
    "UpdateContactFlowModuleContentRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowModuleId": str,
    },
)
_OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "State": ContactFlowModuleStateType,
    },
    total=False,
)

class UpdateContactFlowModuleMetadataRequestRequestTypeDef(
    _RequiredUpdateContactFlowModuleMetadataRequestRequestTypeDef,
    _OptionalUpdateContactFlowModuleMetadataRequestRequestTypeDef,
):
    pass

_RequiredUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateContactFlowNameRequestRequestTypeDef(
    _RequiredUpdateContactFlowNameRequestRequestTypeDef,
    _OptionalUpdateContactFlowNameRequestRequestTypeDef,
):
    pass

_RequiredUpdateContactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
    },
)
_OptionalUpdateContactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "References": Dict[str, "ReferenceTypeDef"],
    },
    total=False,
)

class UpdateContactRequestRequestTypeDef(
    _RequiredUpdateContactRequestRequestTypeDef, _OptionalUpdateContactRequestRequestTypeDef
):
    pass

UpdateContactScheduleRequestRequestTypeDef = TypedDict(
    "UpdateContactScheduleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "ScheduledTime": Union[datetime, str],
    },
)

_RequiredUpdateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)
_OptionalUpdateHoursOfOperationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHoursOfOperationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
    },
    total=False,
)

class UpdateHoursOfOperationRequestRequestTypeDef(
    _RequiredUpdateHoursOfOperationRequestRequestTypeDef,
    _OptionalUpdateHoursOfOperationRequestRequestTypeDef,
):
    pass

UpdateInstanceAttributeRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
)

UpdateInstanceStorageConfigRequestRequestTypeDef = TypedDict(
    "UpdateInstanceStorageConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "TargetArn": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberId": str,
        "PhoneNumberArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateQueueHoursOfOperationRequestRequestTypeDef = TypedDict(
    "UpdateQueueHoursOfOperationRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "HoursOfOperationId": str,
    },
)

_RequiredUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueMaxContactsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueMaxContactsRequestRequestTypeDef",
    {
        "MaxContacts": int,
    },
    total=False,
)

class UpdateQueueMaxContactsRequestRequestTypeDef(
    _RequiredUpdateQueueMaxContactsRequestRequestTypeDef,
    _OptionalUpdateQueueMaxContactsRequestRequestTypeDef,
):
    pass

_RequiredUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateQueueNameRequestRequestTypeDef(
    _RequiredUpdateQueueNameRequestRequestTypeDef, _OptionalUpdateQueueNameRequestRequestTypeDef
):
    pass

UpdateQueueOutboundCallerConfigRequestRequestTypeDef = TypedDict(
    "UpdateQueueOutboundCallerConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
    },
)

UpdateQueueStatusRequestRequestTypeDef = TypedDict(
    "UpdateQueueStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Status": QueueStatusType,
    },
)

UpdateQuickConnectConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuickConnectConfigRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)

_RequiredUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)
_OptionalUpdateQuickConnectNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuickConnectNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateQuickConnectNameRequestRequestTypeDef(
    _RequiredUpdateQuickConnectNameRequestRequestTypeDef,
    _OptionalUpdateQuickConnectNameRequestRequestTypeDef,
):
    pass

UpdateRoutingProfileConcurrencyRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileConcurrencyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)

UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "DefaultOutboundQueueId": str,
    },
)

_RequiredUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalUpdateRoutingProfileNameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoutingProfileNameRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateRoutingProfileNameRequestRequestTypeDef(
    _RequiredUpdateRoutingProfileNameRequestRequestTypeDef,
    _OptionalUpdateRoutingProfileNameRequestRequestTypeDef,
):
    pass

UpdateRoutingProfileQueuesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingProfileQueuesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

_RequiredUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityProfileRequestRequestTypeDef",
    {
        "SecurityProfileId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityProfileRequestRequestTypeDef",
    {
        "Description": str,
        "Permissions": List[str],
    },
    total=False,
)

class UpdateSecurityProfileRequestRequestTypeDef(
    _RequiredUpdateSecurityProfileRequestRequestTypeDef,
    _OptionalUpdateSecurityProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskTemplateRequestRequestTypeDef",
    {
        "TaskTemplateId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateTaskTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskTemplateRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Status": TaskTemplateStatusType,
        "Fields": List["TaskTemplateFieldTypeDef"],
    },
    total=False,
)

class UpdateTaskTemplateRequestRequestTypeDef(
    _RequiredUpdateTaskTemplateRequestRequestTypeDef,
    _OptionalUpdateTaskTemplateRequestRequestTypeDef,
):
    pass

UpdateTaskTemplateResponseTypeDef = TypedDict(
    "UpdateTaskTemplateResponseTypeDef",
    {
        "InstanceId": str,
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "ContactFlowId": str,
        "Constraints": "TaskTemplateConstraintsTypeDef",
        "Defaults": "TaskTemplateDefaultsTypeDef",
        "Fields": List["TaskTemplateFieldTypeDef"],
        "Status": TaskTemplateStatusType,
        "LastModifiedTime": datetime,
        "CreatedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserHierarchyGroupNameRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyGroupNameRequestRequestTypeDef",
    {
        "Name": str,
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

_RequiredUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserHierarchyRequestRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateUserHierarchyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserHierarchyRequestRequestTypeDef",
    {
        "HierarchyGroupId": str,
    },
    total=False,
)

class UpdateUserHierarchyRequestRequestTypeDef(
    _RequiredUpdateUserHierarchyRequestRequestTypeDef,
    _OptionalUpdateUserHierarchyRequestRequestTypeDef,
):
    pass

UpdateUserHierarchyStructureRequestRequestTypeDef = TypedDict(
    "UpdateUserHierarchyStructureRequestRequestTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureUpdateTypeDef",
        "InstanceId": str,
    },
)

UpdateUserIdentityInfoRequestRequestTypeDef = TypedDict(
    "UpdateUserIdentityInfoRequestRequestTypeDef",
    {
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserPhoneConfigRequestRequestTypeDef = TypedDict(
    "UpdateUserPhoneConfigRequestRequestTypeDef",
    {
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserRoutingProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserRoutingProfileRequestRequestTypeDef",
    {
        "RoutingProfileId": str,
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserSecurityProfilesRequestRequestTypeDef = TypedDict(
    "UpdateUserSecurityProfilesRequestRequestTypeDef",
    {
        "SecurityProfileIds": List[str],
        "UserId": str,
        "InstanceId": str,
    },
)

UrlReferenceTypeDef = TypedDict(
    "UrlReferenceTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "UseCaseType": UseCaseTypeType,
    },
    total=False,
)

UserDataFiltersTypeDef = TypedDict(
    "UserDataFiltersTypeDef",
    {
        "Queues": List[str],
        "ContactFilter": "ContactFilterTypeDef",
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "User": "UserReferenceTypeDef",
        "RoutingProfile": "RoutingProfileReferenceTypeDef",
        "HierarchyPath": "HierarchyPathReferenceTypeDef",
        "Status": "AgentStatusReferenceTypeDef",
        "AvailableSlotsByChannel": Dict[ChannelType, int],
        "MaxSlotsByChannel": Dict[ChannelType, int],
        "ActiveSlotsByChannel": Dict[ChannelType, int],
        "Contacts": List["AgentContactReferenceTypeDef"],
    },
    total=False,
)

UserIdentityInfoLiteTypeDef = TypedDict(
    "UserIdentityInfoLiteTypeDef",
    {
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
    },
    total=False,
)

_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef",
    {
        "PhoneType": PhoneTypeType,
    },
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)

class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass

UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserReferenceTypeDef = TypedDict(
    "UserReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

UserSearchCriteriaTypeDef = TypedDict(
    "UserSearchCriteriaTypeDef",
    {
        "OrConditions": List[Dict[str, Any]],
        "AndConditions": List[Dict[str, Any]],
        "StringCondition": "StringConditionTypeDef",
        "HierarchyGroupCondition": "HierarchyGroupConditionTypeDef",
    },
    total=False,
)

UserSearchFilterTypeDef = TypedDict(
    "UserSearchFilterTypeDef",
    {
        "TagFilter": "ControlPlaneTagFilterTypeDef",
    },
    total=False,
)

UserSearchSummaryTypeDef = TypedDict(
    "UserSearchSummaryTypeDef",
    {
        "Arn": str,
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Id": str,
        "IdentityInfo": "UserIdentityInfoLiteTypeDef",
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "RoutingProfileId": str,
        "SecurityProfileIds": List[str],
        "Tags": Dict[str, str],
        "Username": str,
    },
    total=False,
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredVocabularySummaryTypeDef = TypedDict(
    "_RequiredVocabularySummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
    },
)
_OptionalVocabularySummaryTypeDef = TypedDict(
    "_OptionalVocabularySummaryTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class VocabularySummaryTypeDef(
    _RequiredVocabularySummaryTypeDef, _OptionalVocabularySummaryTypeDef
):
    pass

_RequiredVocabularyTypeDef = TypedDict(
    "_RequiredVocabularyTypeDef",
    {
        "Name": str,
        "Id": str,
        "Arn": str,
        "LanguageCode": VocabularyLanguageCodeType,
        "State": VocabularyStateType,
        "LastModifiedTime": datetime,
    },
)
_OptionalVocabularyTypeDef = TypedDict(
    "_OptionalVocabularyTypeDef",
    {
        "FailureReason": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class VocabularyTypeDef(_RequiredVocabularyTypeDef, _OptionalVocabularyTypeDef):
    pass

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {
        "VoiceRecordingTrack": VoiceRecordingTrackType,
    },
    total=False,
)
