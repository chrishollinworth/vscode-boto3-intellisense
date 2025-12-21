"""
Type annotations for connect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_connect.type_defs import ActionSummaryTypeDef

    data: ActionSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ActionTypeType,
    AgentAvailabilityTimerType,
    AgentStatusStateType,
    AgentStatusTypeType,
    AiUseCaseType,
    AllowedUserActionType,
    AnsweringMachineDetectionStatusType,
    ApplicationTypeType,
    ArtifactStatusType,
    AutoEvaluationStatusType,
    BehaviorTypeType,
    BooleanComparisonTypeType,
    ChannelType,
    ChatEventTypeType,
    ContactFlowModuleStateType,
    ContactFlowModuleStatusType,
    ContactFlowStateType,
    ContactFlowStatusType,
    ContactFlowTypeType,
    ContactInitiationMethodType,
    ContactInteractionTypeType,
    ContactMediaProcessingFailureModeType,
    ContactParticipantRoleType,
    ContactRecordingTypeType,
    ContactStateType,
    CurrentMetricNameType,
    DataTableAttributeValueTypeType,
    DataTableLockLevelType,
    DateComparisonTypeType,
    DateTimeComparisonTypeType,
    DecimalComparisonTypeType,
    DeviceTypeType,
    DirectoryTypeType,
    EmailHeaderTypeType,
    EndpointTypeType,
    EntityTypeType,
    EvaluationFormItemEnablementActionType,
    EvaluationFormItemEnablementOperatorType,
    EvaluationFormItemSourceValuesComparatorType,
    EvaluationFormLanguageCodeType,
    EvaluationFormMultiSelectQuestionDisplayModeType,
    EvaluationFormQuestionAutomationAnswerSourceTypeType,
    EvaluationFormQuestionTypeType,
    EvaluationFormScoringModeType,
    EvaluationFormScoringStatusType,
    EvaluationFormSingleSelectQuestionDisplayModeType,
    EvaluationFormVersionStatusType,
    EvaluationQuestionAnswerAnalysisTypeType,
    EvaluationStatusType,
    EvaluationSuggestedAnswerStatusType,
    EvaluationTranscriptTypeType,
    EvaluationTypeType,
    EventSourceNameType,
    FailureReasonCodeType,
    FileStatusTypeType,
    FileUseCaseTypeType,
    FlowAssociationResourceTypeType,
    GroupingType,
    HierarchyGroupMatchTypeType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InitiateAsType,
    InstanceAttributeTypeType,
    InstanceReplicationStatusType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    IntervalPeriodType,
    LexVersionType,
    ListFlowAssociationResourceTypeType,
    MediaStreamTypeType,
    MediaTypeType,
    MeetingFeatureStatusType,
    MonitorCapabilityType,
    MultiSelectQuestionRuleCategoryAutomationConditionType,
    NumberComparisonTypeType,
    NumericQuestionPropertyAutomationLabelType,
    OutboundMessageSourceTypeType,
    OverrideDaysType,
    ParticipantRoleType,
    ParticipantStateType,
    ParticipantTimerTypeType,
    ParticipantTypeType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneNumberWorkflowStatusType,
    PhoneTypeType,
    QuestionRuleCategoryAutomationConditionType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    RealTimeContactAnalysisOutputTypeType,
    RealTimeContactAnalysisPostContactSummaryFailureCodeType,
    RealTimeContactAnalysisPostContactSummaryStatusType,
    RealTimeContactAnalysisSegmentTypeType,
    RealTimeContactAnalysisSentimentLabelType,
    RealTimeContactAnalysisStatusType,
    RealTimeContactAnalysisSupportedChannelType,
    RecordingStatusType,
    ReferenceStatusType,
    ReferenceTypeType,
    RehydrationTypeType,
    ResponseModeType,
    RoutingCriteriaStepStatusType,
    RulePublishStatusType,
    SearchContactsMatchTypeType,
    SearchContactsTimeRangeTypeType,
    SingleSelectQuestionRuleCategoryAutomationConditionType,
    SortableFieldNameType,
    SortOrderType,
    SourceTypeType,
    StatisticType,
    StatusType,
    StorageTypeType,
    StringComparisonTypeType,
    TaskTemplateFieldTypeType,
    TaskTemplateStatusType,
    TimerEligibleParticipantRolesType,
    TrafficDistributionGroupStatusType,
    TrafficTypeType,
    UnitType,
    UseCaseTypeType,
    ViewStatusType,
    ViewTypeType,
    VisibilityType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
    VoiceRecordingTrackType,
    WorkspaceFontFamilyType,
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
    "ActionSummaryTypeDef",
    "ActivateEvaluationFormRequestTypeDef",
    "ActivateEvaluationFormResponseTypeDef",
    "AdditionalEmailRecipientsTypeDef",
    "AgentConfigOutputTypeDef",
    "AgentConfigTypeDef",
    "AgentConfigUnionTypeDef",
    "AgentContactReferenceTypeDef",
    "AgentFirstOutputTypeDef",
    "AgentFirstTypeDef",
    "AgentFirstUnionTypeDef",
    "AgentHierarchyGroupTypeDef",
    "AgentHierarchyGroupsTypeDef",
    "AgentInfoTypeDef",
    "AgentQualityMetricsTypeDef",
    "AgentStatusIdentifierTypeDef",
    "AgentStatusReferenceTypeDef",
    "AgentStatusSearchCriteriaPaginatorTypeDef",
    "AgentStatusSearchCriteriaTypeDef",
    "AgentStatusSearchFilterTypeDef",
    "AgentStatusSummaryTypeDef",
    "AgentStatusTypeDef",
    "AgentsCriteriaOutputTypeDef",
    "AgentsCriteriaTypeDef",
    "AgentsCriteriaUnionTypeDef",
    "AiAgentInfoTypeDef",
    "AliasConfigurationTypeDef",
    "AllowedCapabilitiesTypeDef",
    "AnalyticsDataAssociationResultTypeDef",
    "AnalyticsDataSetsResultTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "ApplicationOutputTypeDef",
    "ApplicationTypeDef",
    "ApplicationUnionTypeDef",
    "AssignSlaActionDefinitionOutputTypeDef",
    "AssignSlaActionDefinitionTypeDef",
    "AssignSlaActionDefinitionUnionTypeDef",
    "AssociateAnalyticsDataSetRequestTypeDef",
    "AssociateAnalyticsDataSetResponseTypeDef",
    "AssociateApprovedOriginRequestTypeDef",
    "AssociateBotRequestTypeDef",
    "AssociateContactWithUserRequestTypeDef",
    "AssociateDefaultVocabularyRequestTypeDef",
    "AssociateEmailAddressAliasRequestTypeDef",
    "AssociateFlowRequestTypeDef",
    "AssociateInstanceStorageConfigRequestTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateLambdaFunctionRequestTypeDef",
    "AssociateLexBotRequestTypeDef",
    "AssociatePhoneNumberContactFlowRequestTypeDef",
    "AssociateQueueQuickConnectsRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestTypeDef",
    "AssociateSecurityKeyRequestTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AssociateSecurityProfilesRequestTypeDef",
    "AssociateTrafficDistributionGroupUserRequestTypeDef",
    "AssociateUserProficienciesRequestTypeDef",
    "AssociateWorkspaceRequestTypeDef",
    "AssociateWorkspaceResponseTypeDef",
    "AssociatedContactSummaryTypeDef",
    "AttachedFileErrorTypeDef",
    "AttachedFileTypeDef",
    "AttachmentReferenceTypeDef",
    "AttendeeTypeDef",
    "AttributeAndConditionTypeDef",
    "AttributeConditionOutputTypeDef",
    "AttributeConditionTypeDef",
    "AttributeConditionUnionTypeDef",
    "AttributeTypeDef",
    "AudioFeaturesTypeDef",
    "AudioQualityMetricsInfoTypeDef",
    "AuthenticationProfileSummaryTypeDef",
    "AuthenticationProfileTypeDef",
    "AutoEvaluationConfigurationTypeDef",
    "AutoEvaluationDetailsTypeDef",
    "AutomaticFailConfigurationTypeDef",
    "AvailableNumberSummaryTypeDef",
    "BatchAssociateAnalyticsDataSetRequestTypeDef",
    "BatchAssociateAnalyticsDataSetResponseTypeDef",
    "BatchCreateDataTableValueFailureResultTypeDef",
    "BatchCreateDataTableValueRequestTypeDef",
    "BatchCreateDataTableValueResponseTypeDef",
    "BatchCreateDataTableValueSuccessResultTypeDef",
    "BatchDeleteDataTableValueFailureResultTypeDef",
    "BatchDeleteDataTableValueRequestTypeDef",
    "BatchDeleteDataTableValueResponseTypeDef",
    "BatchDeleteDataTableValueSuccessResultTypeDef",
    "BatchDescribeDataTableValueFailureResultTypeDef",
    "BatchDescribeDataTableValueRequestTypeDef",
    "BatchDescribeDataTableValueResponseTypeDef",
    "BatchDescribeDataTableValueSuccessResultTypeDef",
    "BatchDisassociateAnalyticsDataSetRequestTypeDef",
    "BatchDisassociateAnalyticsDataSetResponseTypeDef",
    "BatchGetAttachedFileMetadataRequestTypeDef",
    "BatchGetAttachedFileMetadataResponseTypeDef",
    "BatchGetFlowAssociationRequestTypeDef",
    "BatchGetFlowAssociationResponseTypeDef",
    "BatchPutContactRequestTypeDef",
    "BatchPutContactResponseTypeDef",
    "BatchUpdateDataTableValueFailureResultTypeDef",
    "BatchUpdateDataTableValueRequestTypeDef",
    "BatchUpdateDataTableValueResponseTypeDef",
    "BatchUpdateDataTableValueSuccessResultTypeDef",
    "BooleanConditionTypeDef",
    "CampaignTypeDef",
    "CaseSlaConfigurationOutputTypeDef",
    "CaseSlaConfigurationTypeDef",
    "CaseSlaConfigurationUnionTypeDef",
    "ChatContactMetricsTypeDef",
    "ChatEventTypeDef",
    "ChatMessageTypeDef",
    "ChatMetricsTypeDef",
    "ChatParticipantRoleConfigTypeDef",
    "ChatStreamingConfigurationTypeDef",
    "ClaimPhoneNumberRequestTypeDef",
    "ClaimPhoneNumberResponseTypeDef",
    "ClaimedPhoneNumberSummaryTypeDef",
    "CommonAttributeAndConditionTypeDef",
    "CompleteAttachedFileUploadRequestTypeDef",
    "ConditionTypeDef",
    "ConnectionDataTypeDef",
    "ContactAnalysisTypeDef",
    "ContactConfigurationTypeDef",
    "ContactDataRequestTypeDef",
    "ContactDetailsTypeDef",
    "ContactEvaluationTypeDef",
    "ContactFilterTypeDef",
    "ContactFlowAttributeAndConditionTypeDef",
    "ContactFlowAttributeFilterTypeDef",
    "ContactFlowModuleAliasInfoTypeDef",
    "ContactFlowModuleAliasSummaryTypeDef",
    "ContactFlowModuleSearchCriteriaPaginatorTypeDef",
    "ContactFlowModuleSearchCriteriaTypeDef",
    "ContactFlowModuleSearchFilterTypeDef",
    "ContactFlowModuleSummaryTypeDef",
    "ContactFlowModuleTypeDef",
    "ContactFlowModuleVersionSummaryTypeDef",
    "ContactFlowSearchCriteriaPaginatorTypeDef",
    "ContactFlowSearchCriteriaTypeDef",
    "ContactFlowSearchFilterTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeConditionTypeDef",
    "ContactFlowTypeDef",
    "ContactFlowVersionSummaryTypeDef",
    "ContactMetricInfoTypeDef",
    "ContactMetricResultTypeDef",
    "ContactMetricValueTypeDef",
    "ContactSearchSummaryAgentInfoTypeDef",
    "ContactSearchSummaryPaginatorTypeDef",
    "ContactSearchSummaryQueueInfoTypeDef",
    "ContactSearchSummarySegmentAttributeValuePaginatorTypeDef",
    "ContactSearchSummarySegmentAttributeValueTypeDef",
    "ContactSearchSummaryTypeDef",
    "ContactTypeDef",
    "ControlPlaneAttributeFilterTypeDef",
    "ControlPlaneTagFilterTypeDef",
    "ControlPlaneUserAttributeFilterTypeDef",
    "CreateAgentStatusRequestTypeDef",
    "CreateAgentStatusResponseTypeDef",
    "CreateCaseActionDefinitionOutputTypeDef",
    "CreateCaseActionDefinitionTypeDef",
    "CreateCaseActionDefinitionUnionTypeDef",
    "CreateContactFlowModuleAliasRequestTypeDef",
    "CreateContactFlowModuleAliasResponseTypeDef",
    "CreateContactFlowModuleRequestTypeDef",
    "CreateContactFlowModuleResponseTypeDef",
    "CreateContactFlowModuleVersionRequestTypeDef",
    "CreateContactFlowModuleVersionResponseTypeDef",
    "CreateContactFlowRequestTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateContactFlowVersionRequestTypeDef",
    "CreateContactFlowVersionResponseTypeDef",
    "CreateContactRequestTypeDef",
    "CreateContactResponseTypeDef",
    "CreateDataTableAttributeRequestTypeDef",
    "CreateDataTableAttributeResponseTypeDef",
    "CreateDataTableRequestTypeDef",
    "CreateDataTableResponseTypeDef",
    "CreateEmailAddressRequestTypeDef",
    "CreateEmailAddressResponseTypeDef",
    "CreateEvaluationFormRequestTypeDef",
    "CreateEvaluationFormResponseTypeDef",
    "CreateHoursOfOperationOverrideRequestTypeDef",
    "CreateHoursOfOperationOverrideResponseTypeDef",
    "CreateHoursOfOperationRequestTypeDef",
    "CreateHoursOfOperationResponseTypeDef",
    "CreateInstanceRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationRequestTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateParticipantRequestTypeDef",
    "CreateParticipantResponseTypeDef",
    "CreatePersistentContactAssociationRequestTypeDef",
    "CreatePersistentContactAssociationResponseTypeDef",
    "CreatePredefinedAttributeRequestTypeDef",
    "CreatePromptRequestTypeDef",
    "CreatePromptResponseTypeDef",
    "CreatePushNotificationRegistrationRequestTypeDef",
    "CreatePushNotificationRegistrationResponseTypeDef",
    "CreateQueueRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectRequestTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileRequestTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateRuleRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSecurityProfileRequestTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateTaskTemplateRequestTypeDef",
    "CreateTaskTemplateResponseTypeDef",
    "CreateTrafficDistributionGroupRequestTypeDef",
    "CreateTrafficDistributionGroupResponseTypeDef",
    "CreateUseCaseRequestTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupRequestTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateViewRequestTypeDef",
    "CreateViewResponseTypeDef",
    "CreateViewVersionRequestTypeDef",
    "CreateViewVersionResponseTypeDef",
    "CreateVocabularyRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "CreateWorkspacePageRequestTypeDef",
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "CreatedByInfoTypeDef",
    "CredentialsTypeDef",
    "CrossChannelBehaviorTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricSortCriteriaTypeDef",
    "CurrentMetricTypeDef",
    "CustomerQualityMetricsTypeDef",
    "CustomerTypeDef",
    "CustomerVoiceActivityTypeDef",
    "DataTableAccessControlConfigurationOutputTypeDef",
    "DataTableAccessControlConfigurationTypeDef",
    "DataTableAttributeTypeDef",
    "DataTableDeleteValueIdentifierTypeDef",
    "DataTableEvaluatedValueTypeDef",
    "DataTableLockVersionTypeDef",
    "DataTableSearchCriteriaPaginatorTypeDef",
    "DataTableSearchCriteriaTypeDef",
    "DataTableSearchFilterTypeDef",
    "DataTableSummaryTypeDef",
    "DataTableTypeDef",
    "DataTableValueEvaluationSetTypeDef",
    "DataTableValueIdentifierTypeDef",
    "DataTableValueSummaryTypeDef",
    "DataTableValueTypeDef",
    "DateConditionTypeDef",
    "DateReferenceTypeDef",
    "DateTimeConditionTypeDef",
    "DeactivateEvaluationFormRequestTypeDef",
    "DeactivateEvaluationFormResponseTypeDef",
    "DecimalConditionTypeDef",
    "DefaultVocabularyTypeDef",
    "DeleteAttachedFileRequestTypeDef",
    "DeleteContactEvaluationRequestTypeDef",
    "DeleteContactFlowModuleAliasRequestTypeDef",
    "DeleteContactFlowModuleRequestTypeDef",
    "DeleteContactFlowModuleVersionRequestTypeDef",
    "DeleteContactFlowRequestTypeDef",
    "DeleteContactFlowVersionRequestTypeDef",
    "DeleteDataTableAttributeRequestTypeDef",
    "DeleteDataTableAttributeResponseTypeDef",
    "DeleteDataTableRequestTypeDef",
    "DeleteEmailAddressRequestTypeDef",
    "DeleteEvaluationFormRequestTypeDef",
    "DeleteHoursOfOperationOverrideRequestTypeDef",
    "DeleteHoursOfOperationRequestTypeDef",
    "DeleteInstanceRequestTypeDef",
    "DeleteIntegrationAssociationRequestTypeDef",
    "DeletePredefinedAttributeRequestTypeDef",
    "DeletePromptRequestTypeDef",
    "DeletePushNotificationRegistrationRequestTypeDef",
    "DeleteQueueRequestTypeDef",
    "DeleteQuickConnectRequestTypeDef",
    "DeleteRoutingProfileRequestTypeDef",
    "DeleteRuleRequestTypeDef",
    "DeleteSecurityProfileRequestTypeDef",
    "DeleteTaskTemplateRequestTypeDef",
    "DeleteTrafficDistributionGroupRequestTypeDef",
    "DeleteUseCaseRequestTypeDef",
    "DeleteUserHierarchyGroupRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeleteViewRequestTypeDef",
    "DeleteViewVersionRequestTypeDef",
    "DeleteVocabularyRequestTypeDef",
    "DeleteVocabularyResponseTypeDef",
    "DeleteWorkspaceMediaRequestTypeDef",
    "DeleteWorkspacePageRequestTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DescribeAgentStatusRequestTypeDef",
    "DescribeAgentStatusResponseTypeDef",
    "DescribeAuthenticationProfileRequestTypeDef",
    "DescribeAuthenticationProfileResponseTypeDef",
    "DescribeContactEvaluationRequestTypeDef",
    "DescribeContactEvaluationResponseTypeDef",
    "DescribeContactFlowModuleAliasRequestTypeDef",
    "DescribeContactFlowModuleAliasResponseTypeDef",
    "DescribeContactFlowModuleRequestTypeDef",
    "DescribeContactFlowModuleResponseTypeDef",
    "DescribeContactFlowRequestTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeContactRequestTypeDef",
    "DescribeContactResponseTypeDef",
    "DescribeDataTableAttributeRequestTypeDef",
    "DescribeDataTableAttributeResponseTypeDef",
    "DescribeDataTableRequestTypeDef",
    "DescribeDataTableResponseTypeDef",
    "DescribeEmailAddressRequestTypeDef",
    "DescribeEmailAddressResponseTypeDef",
    "DescribeEvaluationFormRequestTypeDef",
    "DescribeEvaluationFormResponseTypeDef",
    "DescribeHoursOfOperationOverrideRequestTypeDef",
    "DescribeHoursOfOperationOverrideResponseTypeDef",
    "DescribeHoursOfOperationRequestTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeRequestTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceRequestTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigRequestTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribePhoneNumberRequestTypeDef",
    "DescribePhoneNumberResponseTypeDef",
    "DescribePredefinedAttributeRequestTypeDef",
    "DescribePredefinedAttributeResponseTypeDef",
    "DescribePromptRequestTypeDef",
    "DescribePromptResponseTypeDef",
    "DescribeQueueRequestTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectRequestTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileRequestTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeRuleRequestTypeDef",
    "DescribeRuleResponseTypeDef",
    "DescribeSecurityProfileRequestTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeTrafficDistributionGroupRequestTypeDef",
    "DescribeTrafficDistributionGroupResponseTypeDef",
    "DescribeUserHierarchyGroupRequestTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureRequestTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeViewRequestTypeDef",
    "DescribeViewResponseTypeDef",
    "DescribeVocabularyRequestTypeDef",
    "DescribeVocabularyResponseTypeDef",
    "DescribeWorkspaceRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DeviceInfoTypeDef",
    "DimensionsTypeDef",
    "DisassociateAnalyticsDataSetRequestTypeDef",
    "DisassociateApprovedOriginRequestTypeDef",
    "DisassociateBotRequestTypeDef",
    "DisassociateEmailAddressAliasRequestTypeDef",
    "DisassociateFlowRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestTypeDef",
    "DisassociateLambdaFunctionRequestTypeDef",
    "DisassociateLexBotRequestTypeDef",
    "DisassociatePhoneNumberContactFlowRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestTypeDef",
    "DisassociateSecurityKeyRequestTypeDef",
    "DisassociateSecurityProfilesRequestTypeDef",
    "DisassociateTrafficDistributionGroupUserRequestTypeDef",
    "DisassociateUserProficienciesRequestTypeDef",
    "DisassociateWorkspaceRequestTypeDef",
    "DisassociateWorkspaceResponseTypeDef",
    "DisconnectDetailsTypeDef",
    "DisconnectReasonTypeDef",
    "DismissUserContactRequestTypeDef",
    "DistributionTypeDef",
    "DownloadUrlMetadataTypeDef",
    "EffectiveHoursOfOperationsTypeDef",
    "EmailAddressInfoTypeDef",
    "EmailAddressMetadataTypeDef",
    "EmailAddressSearchCriteriaTypeDef",
    "EmailAddressSearchFilterTypeDef",
    "EmailAttachmentTypeDef",
    "EmailMessageReferenceTypeDef",
    "EmailRecipientTypeDef",
    "EmailReferenceTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigTypeDef",
    "EndpointInfoTypeDef",
    "EndpointTypeDef",
    "ErrorResultTypeDef",
    "EvaluateDataTableValuesRequestTypeDef",
    "EvaluateDataTableValuesResponseTypeDef",
    "EvaluationAcknowledgementSummaryTypeDef",
    "EvaluationAcknowledgementTypeDef",
    "EvaluationAnswerDataOutputTypeDef",
    "EvaluationAnswerDataTypeDef",
    "EvaluationAnswerDataUnionTypeDef",
    "EvaluationAnswerInputTypeDef",
    "EvaluationAnswerOutputTypeDef",
    "EvaluationAutomationRuleCategoryTypeDef",
    "EvaluationContactLensAnswerAnalysisDetailsTypeDef",
    "EvaluationContactParticipantTypeDef",
    "EvaluationFormAutoEvaluationConfigurationTypeDef",
    "EvaluationFormContentTypeDef",
    "EvaluationFormItemEnablementConditionOperandOutputTypeDef",
    "EvaluationFormItemEnablementConditionOperandTypeDef",
    "EvaluationFormItemEnablementConditionOperandUnionTypeDef",
    "EvaluationFormItemEnablementConditionOutputTypeDef",
    "EvaluationFormItemEnablementConditionTypeDef",
    "EvaluationFormItemEnablementConditionUnionTypeDef",
    "EvaluationFormItemEnablementConfigurationOutputTypeDef",
    "EvaluationFormItemEnablementConfigurationTypeDef",
    "EvaluationFormItemEnablementConfigurationUnionTypeDef",
    "EvaluationFormItemEnablementExpressionOutputTypeDef",
    "EvaluationFormItemEnablementExpressionTypeDef",
    "EvaluationFormItemEnablementExpressionUnionTypeDef",
    "EvaluationFormItemEnablementSourceTypeDef",
    "EvaluationFormItemEnablementSourceValueTypeDef",
    "EvaluationFormItemOutputTypeDef",
    "EvaluationFormItemTypeDef",
    "EvaluationFormItemUnionTypeDef",
    "EvaluationFormLanguageConfigurationTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationOptionOutputTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationOptionTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationOptionUnionTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationOutputTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationTypeDef",
    "EvaluationFormMultiSelectQuestionAutomationUnionTypeDef",
    "EvaluationFormMultiSelectQuestionOptionTypeDef",
    "EvaluationFormMultiSelectQuestionPropertiesOutputTypeDef",
    "EvaluationFormMultiSelectQuestionPropertiesTypeDef",
    "EvaluationFormMultiSelectQuestionPropertiesUnionTypeDef",
    "EvaluationFormNumericQuestionAutomationTypeDef",
    "EvaluationFormNumericQuestionOptionTypeDef",
    "EvaluationFormNumericQuestionPropertiesOutputTypeDef",
    "EvaluationFormNumericQuestionPropertiesTypeDef",
    "EvaluationFormNumericQuestionPropertiesUnionTypeDef",
    "EvaluationFormQuestionAutomationAnswerSourceTypeDef",
    "EvaluationFormQuestionOutputTypeDef",
    "EvaluationFormQuestionTypeDef",
    "EvaluationFormQuestionTypePropertiesOutputTypeDef",
    "EvaluationFormQuestionTypePropertiesTypeDef",
    "EvaluationFormQuestionTypePropertiesUnionTypeDef",
    "EvaluationFormQuestionUnionTypeDef",
    "EvaluationFormScoringStrategyTypeDef",
    "EvaluationFormSearchCriteriaTypeDef",
    "EvaluationFormSearchFilterTypeDef",
    "EvaluationFormSearchSummaryTypeDef",
    "EvaluationFormSectionOutputTypeDef",
    "EvaluationFormSectionTypeDef",
    "EvaluationFormSectionUnionTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationOptionTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationOutputTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationTypeDef",
    "EvaluationFormSingleSelectQuestionAutomationUnionTypeDef",
    "EvaluationFormSingleSelectQuestionOptionTypeDef",
    "EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef",
    "EvaluationFormSingleSelectQuestionPropertiesTypeDef",
    "EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef",
    "EvaluationFormSummaryTypeDef",
    "EvaluationFormTargetConfigurationTypeDef",
    "EvaluationFormTextQuestionAutomationTypeDef",
    "EvaluationFormTextQuestionPropertiesTypeDef",
    "EvaluationFormTypeDef",
    "EvaluationFormVersionSummaryTypeDef",
    "EvaluationGenAIAnswerAnalysisDetailsTypeDef",
    "EvaluationMetadataTypeDef",
    "EvaluationNoteTypeDef",
    "EvaluationQuestionAnswerAnalysisDetailsTypeDef",
    "EvaluationQuestionInputDetailsTypeDef",
    "EvaluationScoreTypeDef",
    "EvaluationSearchCriteriaTypeDef",
    "EvaluationSearchFilterTypeDef",
    "EvaluationSearchMetadataTypeDef",
    "EvaluationSearchSummaryTypeDef",
    "EvaluationSuggestedAnswerTranscriptMillisecondOffsetsTypeDef",
    "EvaluationSuggestedAnswerTypeDef",
    "EvaluationSummaryTypeDef",
    "EvaluationTranscriptPointOfInterestTypeDef",
    "EvaluationTypeDef",
    "EvaluatorUserUnionTypeDef",
    "EventBridgeActionDefinitionTypeDef",
    "ExpiryTypeDef",
    "ExpressionOutputTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "ExpressionUnionTypeDef",
    "ExternalInvocationConfigurationTypeDef",
    "FailedBatchAssociationSummaryTypeDef",
    "FailedRequestTypeDef",
    "FieldValueOutputTypeDef",
    "FieldValueTypeDef",
    "FieldValueUnionExtraTypeDef",
    "FieldValueUnionOutputTypeDef",
    "FieldValueUnionTypeDef",
    "FieldValueUnionUnionTypeDef",
    "FilterV2StringConditionTypeDef",
    "FilterV2TypeDef",
    "FiltersTypeDef",
    "FlowAssociationSummaryTypeDef",
    "FlowModuleTypeDef",
    "FlowQuickConnectConfigTypeDef",
    "FontFamilyTypeDef",
    "GetAttachedFileRequestTypeDef",
    "GetAttachedFileResponseTypeDef",
    "GetContactAttributesRequestTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetContactMetricsRequestTypeDef",
    "GetContactMetricsResponseTypeDef",
    "GetCurrentMetricDataRequestTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetCurrentUserDataRequestTypeDef",
    "GetCurrentUserDataResponseTypeDef",
    "GetEffectiveHoursOfOperationsRequestTypeDef",
    "GetEffectiveHoursOfOperationsResponseTypeDef",
    "GetFederationTokenRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetFlowAssociationRequestTypeDef",
    "GetFlowAssociationResponseTypeDef",
    "GetMetricDataRequestPaginateTypeDef",
    "GetMetricDataRequestTypeDef",
    "GetMetricDataResponseTypeDef",
    "GetMetricDataV2RequestTypeDef",
    "GetMetricDataV2ResponseTypeDef",
    "GetPromptFileRequestTypeDef",
    "GetPromptFileResponseTypeDef",
    "GetTaskTemplateRequestTypeDef",
    "GetTaskTemplateResponseTypeDef",
    "GetTrafficDistributionRequestTypeDef",
    "GetTrafficDistributionResponseTypeDef",
    "GranularAccessControlConfigurationOutputTypeDef",
    "GranularAccessControlConfigurationTypeDef",
    "GranularAccessControlConfigurationUnionTypeDef",
    "HierarchyGroupConditionTypeDef",
    "HierarchyGroupSummaryReferenceTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyGroupsTypeDef",
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
    "HoursOfOperationOverrideConfigTypeDef",
    "HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef",
    "HoursOfOperationOverrideSearchCriteriaTypeDef",
    "HoursOfOperationOverrideTypeDef",
    "HoursOfOperationSearchCriteriaPaginatorTypeDef",
    "HoursOfOperationSearchCriteriaTypeDef",
    "HoursOfOperationSearchFilterTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "ImagesLogoTypeDef",
    "ImportPhoneNumberRequestTypeDef",
    "ImportPhoneNumberResponseTypeDef",
    "ImportWorkspaceMediaRequestTypeDef",
    "InboundAdditionalRecipientsTypeDef",
    "InboundEmailContentTypeDef",
    "InboundRawMessageTypeDef",
    "InputPredefinedAttributeConfigurationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "IntervalDetailsTypeDef",
    "InvisibleFieldInfoTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotTypeDef",
    "LexV2BotTypeDef",
    "ListAgentStatusRequestPaginateTypeDef",
    "ListAgentStatusRequestTypeDef",
    "ListAgentStatusResponseTypeDef",
    "ListAnalyticsDataAssociationsRequestTypeDef",
    "ListAnalyticsDataAssociationsResponseTypeDef",
    "ListAnalyticsDataLakeDataSetsRequestTypeDef",
    "ListAnalyticsDataLakeDataSetsResponseTypeDef",
    "ListApprovedOriginsRequestPaginateTypeDef",
    "ListApprovedOriginsRequestTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListAssociatedContactsRequestTypeDef",
    "ListAssociatedContactsResponseTypeDef",
    "ListAuthenticationProfilesRequestPaginateTypeDef",
    "ListAuthenticationProfilesRequestTypeDef",
    "ListAuthenticationProfilesResponseTypeDef",
    "ListBotsRequestPaginateTypeDef",
    "ListBotsRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListConditionTypeDef",
    "ListContactEvaluationsRequestPaginateTypeDef",
    "ListContactEvaluationsRequestTypeDef",
    "ListContactEvaluationsResponseTypeDef",
    "ListContactFlowModuleAliasesRequestPaginateTypeDef",
    "ListContactFlowModuleAliasesRequestTypeDef",
    "ListContactFlowModuleAliasesResponseTypeDef",
    "ListContactFlowModuleVersionsRequestPaginateTypeDef",
    "ListContactFlowModuleVersionsRequestTypeDef",
    "ListContactFlowModuleVersionsResponseTypeDef",
    "ListContactFlowModulesRequestPaginateTypeDef",
    "ListContactFlowModulesRequestTypeDef",
    "ListContactFlowModulesResponseTypeDef",
    "ListContactFlowVersionsRequestPaginateTypeDef",
    "ListContactFlowVersionsRequestTypeDef",
    "ListContactFlowVersionsResponseTypeDef",
    "ListContactFlowsRequestPaginateTypeDef",
    "ListContactFlowsRequestTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListContactReferencesRequestPaginateTypeDef",
    "ListContactReferencesRequestTypeDef",
    "ListContactReferencesResponseTypeDef",
    "ListDataTableAttributesRequestPaginateTypeDef",
    "ListDataTableAttributesRequestTypeDef",
    "ListDataTableAttributesResponseTypeDef",
    "ListDataTablePrimaryValuesRequestPaginateTypeDef",
    "ListDataTablePrimaryValuesRequestTypeDef",
    "ListDataTablePrimaryValuesResponseTypeDef",
    "ListDataTableValuesRequestPaginateTypeDef",
    "ListDataTableValuesRequestTypeDef",
    "ListDataTableValuesResponseTypeDef",
    "ListDataTablesRequestPaginateTypeDef",
    "ListDataTablesRequestTypeDef",
    "ListDataTablesResponseTypeDef",
    "ListDefaultVocabulariesRequestPaginateTypeDef",
    "ListDefaultVocabulariesRequestTypeDef",
    "ListDefaultVocabulariesResponseTypeDef",
    "ListEntitySecurityProfilesRequestTypeDef",
    "ListEntitySecurityProfilesResponseTypeDef",
    "ListEvaluationFormVersionsRequestPaginateTypeDef",
    "ListEvaluationFormVersionsRequestTypeDef",
    "ListEvaluationFormVersionsResponseTypeDef",
    "ListEvaluationFormsRequestPaginateTypeDef",
    "ListEvaluationFormsRequestTypeDef",
    "ListEvaluationFormsResponseTypeDef",
    "ListFlowAssociationsRequestPaginateTypeDef",
    "ListFlowAssociationsRequestTypeDef",
    "ListFlowAssociationsResponseTypeDef",
    "ListHoursOfOperationOverridesRequestPaginateTypeDef",
    "ListHoursOfOperationOverridesRequestTypeDef",
    "ListHoursOfOperationOverridesResponseTypeDef",
    "ListHoursOfOperationsRequestPaginateTypeDef",
    "ListHoursOfOperationsRequestTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesRequestPaginateTypeDef",
    "ListInstanceAttributesRequestTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsRequestPaginateTypeDef",
    "ListInstanceStorageConfigsRequestTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesRequestPaginateTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsRequestPaginateTypeDef",
    "ListIntegrationAssociationsRequestTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsRequestPaginateTypeDef",
    "ListLambdaFunctionsRequestTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsRequestPaginateTypeDef",
    "ListLexBotsRequestTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersRequestPaginateTypeDef",
    "ListPhoneNumbersRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPhoneNumbersSummaryTypeDef",
    "ListPhoneNumbersV2RequestPaginateTypeDef",
    "ListPhoneNumbersV2RequestTypeDef",
    "ListPhoneNumbersV2ResponseTypeDef",
    "ListPredefinedAttributesRequestPaginateTypeDef",
    "ListPredefinedAttributesRequestTypeDef",
    "ListPredefinedAttributesResponseTypeDef",
    "ListPromptsRequestPaginateTypeDef",
    "ListPromptsRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsRequestPaginateTypeDef",
    "ListQueueQuickConnectsRequestTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesRequestPaginateTypeDef",
    "ListQueuesRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsRequestPaginateTypeDef",
    "ListQuickConnectsRequestTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRealtimeContactAnalysisSegmentsV2RequestTypeDef",
    "ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef",
    "ListRoutingProfileManualAssignmentQueuesRequestPaginateTypeDef",
    "ListRoutingProfileManualAssignmentQueuesRequestTypeDef",
    "ListRoutingProfileManualAssignmentQueuesResponseTypeDef",
    "ListRoutingProfileQueuesRequestPaginateTypeDef",
    "ListRoutingProfileQueuesRequestTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesRequestPaginateTypeDef",
    "ListRoutingProfilesRequestTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListRulesRequestPaginateTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListSecurityKeysRequestPaginateTypeDef",
    "ListSecurityKeysRequestTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfileApplicationsRequestPaginateTypeDef",
    "ListSecurityProfileApplicationsRequestTypeDef",
    "ListSecurityProfileApplicationsResponseTypeDef",
    "ListSecurityProfileFlowModulesRequestTypeDef",
    "ListSecurityProfileFlowModulesResponseTypeDef",
    "ListSecurityProfilePermissionsRequestPaginateTypeDef",
    "ListSecurityProfilePermissionsRequestTypeDef",
    "ListSecurityProfilePermissionsResponseTypeDef",
    "ListSecurityProfilesRequestPaginateTypeDef",
    "ListSecurityProfilesRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskTemplatesRequestPaginateTypeDef",
    "ListTaskTemplatesRequestTypeDef",
    "ListTaskTemplatesResponseTypeDef",
    "ListTrafficDistributionGroupUsersRequestPaginateTypeDef",
    "ListTrafficDistributionGroupUsersRequestTypeDef",
    "ListTrafficDistributionGroupUsersResponseTypeDef",
    "ListTrafficDistributionGroupsRequestPaginateTypeDef",
    "ListTrafficDistributionGroupsRequestTypeDef",
    "ListTrafficDistributionGroupsResponseTypeDef",
    "ListUseCasesRequestPaginateTypeDef",
    "ListUseCasesRequestTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsRequestPaginateTypeDef",
    "ListUserHierarchyGroupsRequestTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUserProficienciesRequestPaginateTypeDef",
    "ListUserProficienciesRequestTypeDef",
    "ListUserProficienciesResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListViewVersionsRequestPaginateTypeDef",
    "ListViewVersionsRequestTypeDef",
    "ListViewVersionsResponseTypeDef",
    "ListViewsRequestPaginateTypeDef",
    "ListViewsRequestTypeDef",
    "ListViewsResponseTypeDef",
    "ListWorkspaceMediaRequestTypeDef",
    "ListWorkspaceMediaResponseTypeDef",
    "ListWorkspacePagesRequestPaginateTypeDef",
    "ListWorkspacePagesRequestTypeDef",
    "ListWorkspacePagesResponseTypeDef",
    "ListWorkspacesRequestPaginateTypeDef",
    "ListWorkspacesRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "MatchCriteriaOutputTypeDef",
    "MatchCriteriaTypeDef",
    "MatchCriteriaUnionTypeDef",
    "MediaConcurrencyTypeDef",
    "MediaItemTypeDef",
    "MediaPlacementTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "MeetingTypeDef",
    "MetricDataV2TypeDef",
    "MetricFilterV2OutputTypeDef",
    "MetricFilterV2TypeDef",
    "MetricFilterV2UnionTypeDef",
    "MetricIntervalTypeDef",
    "MetricResultV2TypeDef",
    "MetricV2OutputTypeDef",
    "MetricV2TypeDef",
    "MetricV2UnionTypeDef",
    "MonitorContactRequestTypeDef",
    "MonitorContactResponseTypeDef",
    "MultiSelectQuestionRuleCategoryAutomationOutputTypeDef",
    "MultiSelectQuestionRuleCategoryAutomationTypeDef",
    "MultiSelectQuestionRuleCategoryAutomationUnionTypeDef",
    "NameCriteriaTypeDef",
    "NewSessionDetailsTypeDef",
    "NextContactEntryTypeDef",
    "NextContactMetadataTypeDef",
    "NotificationRecipientTypeOutputTypeDef",
    "NotificationRecipientTypeTypeDef",
    "NotificationRecipientTypeUnionTypeDef",
    "NumberConditionTypeDef",
    "NumberReferenceTypeDef",
    "NumericQuestionPropertyValueAutomationTypeDef",
    "OperationalHourTypeDef",
    "OutboundAdditionalRecipientsTypeDef",
    "OutboundCallerConfigTypeDef",
    "OutboundEmailConfigTypeDef",
    "OutboundEmailContentTypeDef",
    "OutboundRawMessageTypeDef",
    "OutboundStrategyConfigOutputTypeDef",
    "OutboundStrategyConfigTypeDef",
    "OutboundStrategyConfigUnionTypeDef",
    "OutboundStrategyOutputTypeDef",
    "OutboundStrategyTypeDef",
    "OutboundStrategyUnionTypeDef",
    "OverrideTimeSliceTypeDef",
    "PaginatorConfigTypeDef",
    "PaletteCanvasTypeDef",
    "PaletteHeaderTypeDef",
    "PaletteNavigationTypeDef",
    "PalettePrimaryTypeDef",
    "ParticipantCapabilitiesTypeDef",
    "ParticipantConfigurationTypeDef",
    "ParticipantDetailsToAddTypeDef",
    "ParticipantDetailsTypeDef",
    "ParticipantMetricsTypeDef",
    "ParticipantTimerConfigurationTypeDef",
    "ParticipantTimerValueTypeDef",
    "ParticipantTokenCredentialsTypeDef",
    "PauseContactRequestTypeDef",
    "PersistentChatTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberStatusTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PostAcceptTimeoutConfigTypeDef",
    "PredefinedAttributeConfigurationTypeDef",
    "PredefinedAttributeSearchCriteriaPaginatorTypeDef",
    "PredefinedAttributeSearchCriteriaTypeDef",
    "PredefinedAttributeSummaryTypeDef",
    "PredefinedAttributeTypeDef",
    "PredefinedAttributeValuesOutputTypeDef",
    "PredefinedAttributeValuesTypeDef",
    "PredefinedAttributeValuesUnionTypeDef",
    "PreviewOutputTypeDef",
    "PreviewTypeDef",
    "PreviewUnionTypeDef",
    "PrimaryAttributeAccessControlConfigurationItemOutputTypeDef",
    "PrimaryAttributeAccessControlConfigurationItemTypeDef",
    "PrimaryAttributeValueFilterTypeDef",
    "PrimaryAttributeValueOutputTypeDef",
    "PrimaryAttributeValueTypeDef",
    "PrimaryValueResponseTypeDef",
    "PrimaryValueTypeDef",
    "PromptSearchCriteriaPaginatorTypeDef",
    "PromptSearchCriteriaTypeDef",
    "PromptSearchFilterTypeDef",
    "PromptSummaryTypeDef",
    "PromptTypeDef",
    "PutUserStatusRequestTypeDef",
    "QualityMetricsTypeDef",
    "QueueInfoInputTypeDef",
    "QueueInfoTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSearchCriteriaPaginatorTypeDef",
    "QueueSearchCriteriaTypeDef",
    "QueueSearchFilterTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectContactDataTypeDef",
    "QuickConnectSearchCriteriaPaginatorTypeDef",
    "QuickConnectSearchCriteriaTypeDef",
    "QuickConnectSearchFilterTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "RangeTypeDef",
    "ReadOnlyFieldInfoTypeDef",
    "RealTimeContactAnalysisAttachmentTypeDef",
    "RealTimeContactAnalysisCategoryDetailsTypeDef",
    "RealTimeContactAnalysisCharacterIntervalTypeDef",
    "RealTimeContactAnalysisIssueDetectedTypeDef",
    "RealTimeContactAnalysisPointOfInterestTypeDef",
    "RealTimeContactAnalysisSegmentAttachmentsTypeDef",
    "RealTimeContactAnalysisSegmentCategoriesTypeDef",
    "RealTimeContactAnalysisSegmentEventTypeDef",
    "RealTimeContactAnalysisSegmentIssuesTypeDef",
    "RealTimeContactAnalysisSegmentPostContactSummaryTypeDef",
    "RealTimeContactAnalysisSegmentTranscriptTypeDef",
    "RealTimeContactAnalysisTimeDataTypeDef",
    "RealTimeContactAnalysisTranscriptItemRedactionTypeDef",
    "RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef",
    "RealTimeContactAnalysisTranscriptItemWithContentTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "RecordPrimaryValueTypeDef",
    "RecordingInfoTypeDef",
    "ReferenceSummaryTypeDef",
    "ReferenceTypeDef",
    "ReleasePhoneNumberRequestTypeDef",
    "ReplicateInstanceRequestTypeDef",
    "ReplicateInstanceResponseTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationStatusSummaryTypeDef",
    "RequiredFieldInfoTypeDef",
    "ResourceTagsSearchCriteriaTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestTypeDef",
    "ResumeContactRequestTypeDef",
    "RoutingCriteriaInputStepExpiryTypeDef",
    "RoutingCriteriaInputStepTypeDef",
    "RoutingCriteriaInputTypeDef",
    "RoutingCriteriaPaginatorTypeDef",
    "RoutingCriteriaTypeDef",
    "RoutingProfileManualAssignmentQueueConfigSummaryTypeDef",
    "RoutingProfileManualAssignmentQueueConfigTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileReferenceTypeDef",
    "RoutingProfileSearchCriteriaPaginatorTypeDef",
    "RoutingProfileSearchCriteriaTypeDef",
    "RoutingProfileSearchFilterTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "RuleActionOutputTypeDef",
    "RuleActionTypeDef",
    "RuleActionUnionTypeDef",
    "RuleSummaryTypeDef",
    "RuleTriggerEventSourceTypeDef",
    "RuleTypeDef",
    "S3ConfigTypeDef",
    "SearchAgentStatusesRequestPaginateTypeDef",
    "SearchAgentStatusesRequestTypeDef",
    "SearchAgentStatusesResponseTypeDef",
    "SearchAvailablePhoneNumbersRequestPaginateTypeDef",
    "SearchAvailablePhoneNumbersRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SearchContactEvaluationsRequestTypeDef",
    "SearchContactEvaluationsResponseTypeDef",
    "SearchContactFlowModulesRequestPaginateTypeDef",
    "SearchContactFlowModulesRequestTypeDef",
    "SearchContactFlowModulesResponseTypeDef",
    "SearchContactFlowsRequestPaginateTypeDef",
    "SearchContactFlowsRequestTypeDef",
    "SearchContactFlowsResponseTypeDef",
    "SearchContactsAdditionalTimeRangeCriteriaTypeDef",
    "SearchContactsAdditionalTimeRangeTypeDef",
    "SearchContactsRequestPaginateTypeDef",
    "SearchContactsRequestTypeDef",
    "SearchContactsResponsePaginatorTypeDef",
    "SearchContactsResponseTypeDef",
    "SearchContactsTimeRangeTypeDef",
    "SearchContactsTimestampConditionTypeDef",
    "SearchCriteriaTypeDef",
    "SearchDataTablesRequestPaginateTypeDef",
    "SearchDataTablesRequestTypeDef",
    "SearchDataTablesResponseTypeDef",
    "SearchEmailAddressesRequestTypeDef",
    "SearchEmailAddressesResponseTypeDef",
    "SearchEvaluationFormsRequestTypeDef",
    "SearchEvaluationFormsResponseTypeDef",
    "SearchHoursOfOperationOverridesRequestPaginateTypeDef",
    "SearchHoursOfOperationOverridesRequestTypeDef",
    "SearchHoursOfOperationOverridesResponseTypeDef",
    "SearchHoursOfOperationsRequestPaginateTypeDef",
    "SearchHoursOfOperationsRequestTypeDef",
    "SearchHoursOfOperationsResponseTypeDef",
    "SearchPredefinedAttributesRequestPaginateTypeDef",
    "SearchPredefinedAttributesRequestTypeDef",
    "SearchPredefinedAttributesResponseTypeDef",
    "SearchPromptsRequestPaginateTypeDef",
    "SearchPromptsRequestTypeDef",
    "SearchPromptsResponseTypeDef",
    "SearchQueuesRequestPaginateTypeDef",
    "SearchQueuesRequestTypeDef",
    "SearchQueuesResponseTypeDef",
    "SearchQuickConnectsRequestPaginateTypeDef",
    "SearchQuickConnectsRequestTypeDef",
    "SearchQuickConnectsResponseTypeDef",
    "SearchResourceTagsRequestPaginateTypeDef",
    "SearchResourceTagsRequestTypeDef",
    "SearchResourceTagsResponseTypeDef",
    "SearchRoutingProfilesRequestPaginateTypeDef",
    "SearchRoutingProfilesRequestTypeDef",
    "SearchRoutingProfilesResponseTypeDef",
    "SearchSecurityProfilesRequestPaginateTypeDef",
    "SearchSecurityProfilesRequestTypeDef",
    "SearchSecurityProfilesResponseTypeDef",
    "SearchUserHierarchyGroupsRequestPaginateTypeDef",
    "SearchUserHierarchyGroupsRequestTypeDef",
    "SearchUserHierarchyGroupsResponseTypeDef",
    "SearchUsersRequestPaginateTypeDef",
    "SearchUsersRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "SearchViewsRequestPaginateTypeDef",
    "SearchViewsRequestTypeDef",
    "SearchViewsResponseTypeDef",
    "SearchVocabulariesRequestPaginateTypeDef",
    "SearchVocabulariesRequestTypeDef",
    "SearchVocabulariesResponseTypeDef",
    "SearchWorkspaceAssociationsRequestPaginateTypeDef",
    "SearchWorkspaceAssociationsRequestTypeDef",
    "SearchWorkspaceAssociationsResponseTypeDef",
    "SearchWorkspacesRequestPaginateTypeDef",
    "SearchWorkspacesRequestTypeDef",
    "SearchWorkspacesResponseTypeDef",
    "SearchableAgentCriteriaStepTypeDef",
    "SearchableContactAttributesCriteriaTypeDef",
    "SearchableContactAttributesTypeDef",
    "SearchableRoutingCriteriaStepTypeDef",
    "SearchableRoutingCriteriaTypeDef",
    "SearchableSegmentAttributesCriteriaTypeDef",
    "SearchableSegmentAttributesTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileItemTypeDef",
    "SecurityProfileSearchCriteriaPaginatorTypeDef",
    "SecurityProfileSearchCriteriaTypeDef",
    "SecurityProfileSearchSummaryTypeDef",
    "SecurityProfileSummaryTypeDef",
    "SecurityProfileTypeDef",
    "SecurityProfilesSearchFilterTypeDef",
    "SegmentAttributeValueOutputTypeDef",
    "SegmentAttributeValuePaginatorTypeDef",
    "SegmentAttributeValueTypeDef",
    "SegmentAttributeValueUnionTypeDef",
    "SendChatIntegrationEventRequestTypeDef",
    "SendChatIntegrationEventResponseTypeDef",
    "SendNotificationActionDefinitionOutputTypeDef",
    "SendNotificationActionDefinitionTypeDef",
    "SendNotificationActionDefinitionUnionTypeDef",
    "SendOutboundEmailRequestTypeDef",
    "SignInConfigOutputTypeDef",
    "SignInConfigTypeDef",
    "SignInConfigUnionTypeDef",
    "SignInDistributionTypeDef",
    "SingleSelectQuestionRuleCategoryAutomationTypeDef",
    "SortTypeDef",
    "SourceCampaignTypeDef",
    "StartAttachedFileUploadRequestTypeDef",
    "StartAttachedFileUploadResponseTypeDef",
    "StartChatContactRequestTypeDef",
    "StartChatContactResponseTypeDef",
    "StartContactEvaluationRequestTypeDef",
    "StartContactEvaluationResponseTypeDef",
    "StartContactMediaProcessingRequestTypeDef",
    "StartContactRecordingRequestTypeDef",
    "StartContactStreamingRequestTypeDef",
    "StartContactStreamingResponseTypeDef",
    "StartEmailContactRequestTypeDef",
    "StartEmailContactResponseTypeDef",
    "StartOutboundChatContactRequestTypeDef",
    "StartOutboundChatContactResponseTypeDef",
    "StartOutboundEmailContactRequestTypeDef",
    "StartOutboundEmailContactResponseTypeDef",
    "StartOutboundVoiceContactRequestTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartScreenSharingRequestTypeDef",
    "StartTaskContactRequestTypeDef",
    "StartTaskContactResponseTypeDef",
    "StartWebRTCContactRequestTypeDef",
    "StartWebRTCContactResponseTypeDef",
    "StateTransitionTypeDef",
    "StepPaginatorTypeDef",
    "StepTypeDef",
    "StopContactMediaProcessingRequestTypeDef",
    "StopContactRecordingRequestTypeDef",
    "StopContactRequestTypeDef",
    "StopContactStreamingRequestTypeDef",
    "StringConditionTypeDef",
    "StringReferenceTypeDef",
    "SubmitAutoEvaluationActionDefinitionTypeDef",
    "SubmitContactEvaluationRequestTypeDef",
    "SubmitContactEvaluationResponseTypeDef",
    "SuccessfulBatchAssociationSummaryTypeDef",
    "SuccessfulRequestTypeDef",
    "SuspendContactRecordingRequestTypeDef",
    "TagConditionTypeDef",
    "TagContactRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagSearchConditionTypeDef",
    "TagSetTypeDef",
    "TaskActionDefinitionOutputTypeDef",
    "TaskActionDefinitionTypeDef",
    "TaskActionDefinitionUnionTypeDef",
    "TaskTemplateConstraintsOutputTypeDef",
    "TaskTemplateConstraintsTypeDef",
    "TaskTemplateConstraintsUnionTypeDef",
    "TaskTemplateDefaultFieldValueTypeDef",
    "TaskTemplateDefaultsOutputTypeDef",
    "TaskTemplateDefaultsTypeDef",
    "TaskTemplateDefaultsUnionTypeDef",
    "TaskTemplateFieldIdentifierTypeDef",
    "TaskTemplateFieldOutputTypeDef",
    "TaskTemplateFieldTypeDef",
    "TaskTemplateFieldUnionTypeDef",
    "TaskTemplateInfoV2TypeDef",
    "TaskTemplateMetadataTypeDef",
    "TelephonyConfigOutputTypeDef",
    "TelephonyConfigTypeDef",
    "TelephonyConfigUnionTypeDef",
    "TemplateAttributesTypeDef",
    "TemplatedMessageConfigTypeDef",
    "ThresholdTypeDef",
    "ThresholdV2TypeDef",
    "TimestampTypeDef",
    "TrafficDistributionGroupSummaryTypeDef",
    "TrafficDistributionGroupTypeDef",
    "TrafficDistributionGroupUserSummaryTypeDef",
    "TranscriptCriteriaTypeDef",
    "TranscriptTypeDef",
    "TransferContactRequestTypeDef",
    "TransferContactResponseTypeDef",
    "UntagContactRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentStatusRequestTypeDef",
    "UpdateAuthenticationProfileRequestTypeDef",
    "UpdateCaseActionDefinitionOutputTypeDef",
    "UpdateCaseActionDefinitionTypeDef",
    "UpdateCaseActionDefinitionUnionTypeDef",
    "UpdateContactAttributesRequestTypeDef",
    "UpdateContactEvaluationRequestTypeDef",
    "UpdateContactEvaluationResponseTypeDef",
    "UpdateContactFlowContentRequestTypeDef",
    "UpdateContactFlowMetadataRequestTypeDef",
    "UpdateContactFlowModuleAliasRequestTypeDef",
    "UpdateContactFlowModuleContentRequestTypeDef",
    "UpdateContactFlowModuleMetadataRequestTypeDef",
    "UpdateContactFlowNameRequestTypeDef",
    "UpdateContactRequestTypeDef",
    "UpdateContactRoutingDataRequestTypeDef",
    "UpdateContactScheduleRequestTypeDef",
    "UpdateDataTableAttributeRequestTypeDef",
    "UpdateDataTableAttributeResponseTypeDef",
    "UpdateDataTableMetadataRequestTypeDef",
    "UpdateDataTableMetadataResponseTypeDef",
    "UpdateDataTablePrimaryValuesRequestTypeDef",
    "UpdateDataTablePrimaryValuesResponseTypeDef",
    "UpdateEmailAddressMetadataRequestTypeDef",
    "UpdateEmailAddressMetadataResponseTypeDef",
    "UpdateEvaluationFormRequestTypeDef",
    "UpdateEvaluationFormResponseTypeDef",
    "UpdateHoursOfOperationOverrideRequestTypeDef",
    "UpdateHoursOfOperationRequestTypeDef",
    "UpdateInstanceAttributeRequestTypeDef",
    "UpdateInstanceStorageConfigRequestTypeDef",
    "UpdateParticipantAuthenticationRequestTypeDef",
    "UpdateParticipantRoleConfigChannelInfoTypeDef",
    "UpdateParticipantRoleConfigRequestTypeDef",
    "UpdatePhoneNumberMetadataRequestTypeDef",
    "UpdatePhoneNumberRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePredefinedAttributeRequestTypeDef",
    "UpdatePromptRequestTypeDef",
    "UpdatePromptResponseTypeDef",
    "UpdateQueueHoursOfOperationRequestTypeDef",
    "UpdateQueueMaxContactsRequestTypeDef",
    "UpdateQueueNameRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestTypeDef",
    "UpdateQueueOutboundEmailConfigRequestTypeDef",
    "UpdateQueueStatusRequestTypeDef",
    "UpdateQuickConnectConfigRequestTypeDef",
    "UpdateQuickConnectNameRequestTypeDef",
    "UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef",
    "UpdateRoutingProfileNameRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestTypeDef",
    "UpdateRuleRequestTypeDef",
    "UpdateSecurityProfileRequestTypeDef",
    "UpdateTaskTemplateRequestTypeDef",
    "UpdateTaskTemplateResponseTypeDef",
    "UpdateTrafficDistributionRequestTypeDef",
    "UpdateUserHierarchyGroupNameRequestTypeDef",
    "UpdateUserHierarchyRequestTypeDef",
    "UpdateUserHierarchyStructureRequestTypeDef",
    "UpdateUserIdentityInfoRequestTypeDef",
    "UpdateUserPhoneConfigRequestTypeDef",
    "UpdateUserProficienciesRequestTypeDef",
    "UpdateUserRoutingProfileRequestTypeDef",
    "UpdateUserSecurityProfilesRequestTypeDef",
    "UpdateViewContentRequestTypeDef",
    "UpdateViewContentResponseTypeDef",
    "UpdateViewMetadataRequestTypeDef",
    "UpdateWorkspaceMetadataRequestTypeDef",
    "UpdateWorkspacePageRequestTypeDef",
    "UpdateWorkspaceThemeRequestTypeDef",
    "UpdateWorkspaceVisibilityRequestTypeDef",
    "UploadUrlMetadataTypeDef",
    "UrlReferenceTypeDef",
    "UseCaseTypeDef",
    "UserDataFiltersTypeDef",
    "UserDataTypeDef",
    "UserHierarchyGroupSearchCriteriaPaginatorTypeDef",
    "UserHierarchyGroupSearchCriteriaTypeDef",
    "UserHierarchyGroupSearchFilterTypeDef",
    "UserIdentityInfoLiteTypeDef",
    "UserIdentityInfoTypeDef",
    "UserInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserProficiencyDisassociateTypeDef",
    "UserProficiencyTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserReferenceTypeDef",
    "UserSearchCriteriaPaginatorTypeDef",
    "UserSearchCriteriaTypeDef",
    "UserSearchFilterTypeDef",
    "UserSearchSummaryTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "ValidationEnumOutputTypeDef",
    "ValidationEnumTypeDef",
    "ValidationOutputTypeDef",
    "ValidationTypeDef",
    "ValidationUnionTypeDef",
    "ViewContentTypeDef",
    "ViewInputContentTypeDef",
    "ViewSearchCriteriaPaginatorTypeDef",
    "ViewSearchCriteriaTypeDef",
    "ViewSearchFilterTypeDef",
    "ViewSummaryTypeDef",
    "ViewTypeDef",
    "ViewVersionSummaryTypeDef",
    "VocabularySummaryTypeDef",
    "VocabularyTypeDef",
    "VoiceRecordingConfigurationTypeDef",
    "WisdomInfoTypeDef",
    "WorkspaceAssociationSearchCriteriaPaginatorTypeDef",
    "WorkspaceAssociationSearchCriteriaTypeDef",
    "WorkspaceAssociationSearchFilterTypeDef",
    "WorkspaceAssociationSearchSummaryTypeDef",
    "WorkspacePageTypeDef",
    "WorkspaceSearchCriteriaPaginatorTypeDef",
    "WorkspaceSearchCriteriaTypeDef",
    "WorkspaceSearchFilterTypeDef",
    "WorkspaceSearchSummaryTypeDef",
    "WorkspaceSummaryTypeDef",
    "WorkspaceThemeConfigTypeDef",
    "WorkspaceThemeImagesTypeDef",
    "WorkspaceThemePaletteTypeDef",
    "WorkspaceThemeTypeDef",
    "WorkspaceThemeTypographyTypeDef",
    "WorkspaceTypeDef",
)

class ActionSummaryTypeDef(TypedDict):
    ActionType: ActionTypeType

class ActivateEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EmailRecipientTypeDef(TypedDict):
    Address: NotRequired[str]
    DisplayName: NotRequired[str]

class DistributionTypeDef(TypedDict):
    Region: str
    Percentage: int

class QueueReferenceTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class AgentHierarchyGroupTypeDef(TypedDict):
    Arn: NotRequired[str]

class AgentHierarchyGroupsTypeDef(TypedDict):
    L1Ids: NotRequired[Sequence[str]]
    L2Ids: NotRequired[Sequence[str]]
    L3Ids: NotRequired[Sequence[str]]
    L4Ids: NotRequired[Sequence[str]]
    L5Ids: NotRequired[Sequence[str]]

class DeviceInfoTypeDef(TypedDict):
    PlatformName: NotRequired[str]
    PlatformVersion: NotRequired[str]
    OperatingSystem: NotRequired[str]

class ParticipantCapabilitiesTypeDef(TypedDict):
    Video: NotRequired[Literal["SEND"]]
    ScreenShare: NotRequired[Literal["SEND"]]

class StateTransitionTypeDef(TypedDict):
    State: NotRequired[ParticipantStateType]
    StateStartTimestamp: NotRequired[datetime]
    StateEndTimestamp: NotRequired[datetime]

class AudioQualityMetricsInfoTypeDef(TypedDict):
    QualityScore: NotRequired[float]
    PotentialQualityIssues: NotRequired[List[str]]

class AgentStatusIdentifierTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]

class AgentStatusReferenceTypeDef(TypedDict):
    StatusStartTimestamp: NotRequired[datetime]
    StatusArn: NotRequired[str]
    StatusName: NotRequired[str]

StringConditionTypeDef = TypedDict(
    "StringConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "Value": NotRequired[str],
        "ComparisonType": NotRequired[StringComparisonTypeType],
    },
)
AgentStatusSummaryTypeDef = TypedDict(
    "AgentStatusSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AgentStatusTypeType],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedRegion": NotRequired[str],
    },
)
AgentStatusTypeDef = TypedDict(
    "AgentStatusTypeDef",
    {
        "AgentStatusARN": NotRequired[str],
        "AgentStatusId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[AgentStatusTypeType],
        "DisplayOrder": NotRequired[int],
        "State": NotRequired[AgentStatusStateType],
        "Tags": NotRequired[Dict[str, str]],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedRegion": NotRequired[str],
    },
)

class AgentsCriteriaOutputTypeDef(TypedDict):
    AgentIds: NotRequired[List[str]]

class AgentsCriteriaTypeDef(TypedDict):
    AgentIds: NotRequired[Sequence[str]]

class AiAgentInfoTypeDef(TypedDict):
    AiUseCase: NotRequired[AiUseCaseType]
    AiAgentVersionId: NotRequired[str]
    AiAgentEscalated: NotRequired[bool]

class AliasConfigurationTypeDef(TypedDict):
    EmailAddressId: str

class AnalyticsDataAssociationResultTypeDef(TypedDict):
    DataSetId: NotRequired[str]
    TargetAccountId: NotRequired[str]
    ResourceShareId: NotRequired[str]
    ResourceShareArn: NotRequired[str]
    ResourceShareStatus: NotRequired[str]

class AnalyticsDataSetsResultTypeDef(TypedDict):
    DataSetId: NotRequired[str]
    DataSetName: NotRequired[str]

class AnswerMachineDetectionConfigTypeDef(TypedDict):
    EnableAnswerMachineDetection: NotRequired[bool]
    AwaitAnswerMachinePrompt: NotRequired[bool]

ApplicationOutputTypeDef = TypedDict(
    "ApplicationOutputTypeDef",
    {
        "Namespace": NotRequired[str],
        "ApplicationPermissions": NotRequired[List[str]],
        "Type": NotRequired[ApplicationTypeType],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Namespace": NotRequired[str],
        "ApplicationPermissions": NotRequired[Sequence[str]],
        "Type": NotRequired[ApplicationTypeType],
    },
)

class AssociateAnalyticsDataSetRequestTypeDef(TypedDict):
    InstanceId: str
    DataSetId: str
    TargetAccountId: NotRequired[str]

class AssociateApprovedOriginRequestTypeDef(TypedDict):
    InstanceId: str
    Origin: str
    ClientToken: NotRequired[str]

class LexBotTypeDef(TypedDict):
    Name: str
    LexRegion: str

class LexV2BotTypeDef(TypedDict):
    AliasArn: NotRequired[str]

class AssociateContactWithUserRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    UserId: str

class AssociateDefaultVocabularyRequestTypeDef(TypedDict):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: NotRequired[str]

class AssociateFlowRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType

class AssociateLambdaFunctionRequestTypeDef(TypedDict):
    InstanceId: str
    FunctionArn: str
    ClientToken: NotRequired[str]

class AssociatePhoneNumberContactFlowRequestTypeDef(TypedDict):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str

class AssociateQueueQuickConnectsRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class AssociateSecurityKeyRequestTypeDef(TypedDict):
    InstanceId: str
    Key: str
    ClientToken: NotRequired[str]

class SecurityProfileItemTypeDef(TypedDict):
    Id: NotRequired[str]

class AssociateTrafficDistributionGroupUserRequestTypeDef(TypedDict):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: str
    Level: float

class AssociateWorkspaceRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    ResourceArns: Sequence[str]

class FailedBatchAssociationSummaryTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class SuccessfulBatchAssociationSummaryTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class AssociatedContactSummaryTypeDef(TypedDict):
    ContactId: NotRequired[str]
    ContactArn: NotRequired[str]
    InitiationTimestamp: NotRequired[datetime]
    DisconnectTimestamp: NotRequired[datetime]
    InitialContactId: NotRequired[str]
    PreviousContactId: NotRequired[str]
    RelatedContactId: NotRequired[str]
    InitiationMethod: NotRequired[ContactInitiationMethodType]
    Channel: NotRequired[ChannelType]

class AttachedFileErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    FileId: NotRequired[str]

class CreatedByInfoTypeDef(TypedDict):
    ConnectUserArn: NotRequired[str]
    AWSIdentityArn: NotRequired[str]

class AttachmentReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]
    Status: NotRequired[ReferenceStatusType]
    Arn: NotRequired[str]

class AttendeeTypeDef(TypedDict):
    AttendeeId: NotRequired[str]
    JoinToken: NotRequired[str]

class HierarchyGroupConditionTypeDef(TypedDict):
    Value: NotRequired[str]
    HierarchyGroupMatchType: NotRequired[HierarchyGroupMatchTypeType]

class TagConditionTypeDef(TypedDict):
    TagKey: NotRequired[str]
    TagValue: NotRequired[str]

class RangeTypeDef(TypedDict):
    MinProficiencyLevel: NotRequired[float]
    MaxProficiencyLevel: NotRequired[float]

class AttributeTypeDef(TypedDict):
    AttributeType: NotRequired[InstanceAttributeTypeType]
    Value: NotRequired[str]

class AudioFeaturesTypeDef(TypedDict):
    EchoReduction: NotRequired[MeetingFeatureStatusType]

class AuthenticationProfileSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    IsDefault: NotRequired[bool]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class AuthenticationProfileTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    AllowedIps: NotRequired[List[str]]
    BlockedIps: NotRequired[List[str]]
    IsDefault: NotRequired[bool]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]
    PeriodicSessionDuration: NotRequired[int]
    MaxSessionDuration: NotRequired[int]
    SessionInactivityDuration: NotRequired[int]
    SessionInactivityHandlingEnabled: NotRequired[bool]

class AutoEvaluationConfigurationTypeDef(TypedDict):
    Enabled: bool

class AutoEvaluationDetailsTypeDef(TypedDict):
    AutoEvaluationEnabled: bool
    AutoEvaluationStatus: NotRequired[AutoEvaluationStatusType]

class AutomaticFailConfigurationTypeDef(TypedDict):
    TargetSection: NotRequired[str]

class AvailableNumberSummaryTypeDef(TypedDict):
    PhoneNumber: NotRequired[str]
    PhoneNumberCountryCode: NotRequired[PhoneNumberCountryCodeType]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]

class BatchAssociateAnalyticsDataSetRequestTypeDef(TypedDict):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: NotRequired[str]

class ErrorResultTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class PrimaryValueTypeDef(TypedDict):
    AttributeName: str
    Value: str

class DataTableLockVersionTypeDef(TypedDict):
    DataTable: NotRequired[str]
    Attribute: NotRequired[str]
    PrimaryValues: NotRequired[str]
    Value: NotRequired[str]

class PrimaryValueResponseTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeId: NotRequired[str]
    Value: NotRequired[str]

class BatchDisassociateAnalyticsDataSetRequestTypeDef(TypedDict):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: NotRequired[str]

class BatchGetAttachedFileMetadataRequestTypeDef(TypedDict):
    FileIds: Sequence[str]
    InstanceId: str
    AssociatedResourceArn: str

class BatchGetFlowAssociationRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceIds: Sequence[str]
    ResourceType: NotRequired[ListFlowAssociationResourceTypeType]

class FlowAssociationSummaryTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    FlowId: NotRequired[str]
    ResourceType: NotRequired[ListFlowAssociationResourceTypeType]

class FailedRequestTypeDef(TypedDict):
    RequestIdentifier: NotRequired[str]
    FailureReasonCode: NotRequired[FailureReasonCodeType]
    FailureReasonMessage: NotRequired[str]

class SuccessfulRequestTypeDef(TypedDict):
    RequestIdentifier: NotRequired[str]
    ContactId: NotRequired[str]

BooleanConditionTypeDef = TypedDict(
    "BooleanConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "ComparisonType": NotRequired[BooleanComparisonTypeType],
    },
)

class CampaignTypeDef(TypedDict):
    CampaignId: NotRequired[str]

class FieldValueUnionOutputTypeDef(TypedDict):
    BooleanValue: NotRequired[bool]
    DoubleValue: NotRequired[float]
    EmptyValue: NotRequired[Dict[str, Any]]
    StringValue: NotRequired[str]

class ChatContactMetricsTypeDef(TypedDict):
    MultiParty: NotRequired[bool]
    TotalMessages: NotRequired[int]
    TotalBotMessages: NotRequired[int]
    TotalBotMessageLengthInChars: NotRequired[int]
    ConversationCloseTimeInMillis: NotRequired[int]
    ConversationTurnCount: NotRequired[int]
    AgentFirstResponseTimestamp: NotRequired[datetime]
    AgentFirstResponseTimeInMillis: NotRequired[int]

ChatEventTypeDef = TypedDict(
    "ChatEventTypeDef",
    {
        "Type": ChatEventTypeType,
        "ContentType": NotRequired[str],
        "Content": NotRequired[str],
    },
)

class ChatMessageTypeDef(TypedDict):
    ContentType: str
    Content: str

class ParticipantMetricsTypeDef(TypedDict):
    ParticipantId: NotRequired[str]
    ParticipantType: NotRequired[ParticipantTypeType]
    ConversationAbandon: NotRequired[bool]
    MessagesSent: NotRequired[int]
    NumResponses: NotRequired[int]
    MessageLengthInChars: NotRequired[int]
    TotalResponseTimeInMillis: NotRequired[int]
    MaxResponseTimeInMillis: NotRequired[int]
    LastMessageTimestamp: NotRequired[datetime]

class ChatStreamingConfigurationTypeDef(TypedDict):
    StreamingEndpointArn: str

class ClaimPhoneNumberRequestTypeDef(TypedDict):
    PhoneNumber: str
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    PhoneNumberDescription: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]

class PhoneNumberStatusTypeDef(TypedDict):
    Status: NotRequired[PhoneNumberWorkflowStatusType]
    Message: NotRequired[str]

class CompleteAttachedFileUploadRequestTypeDef(TypedDict):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

NumberConditionTypeDef = TypedDict(
    "NumberConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "MinValue": NotRequired[int],
        "MaxValue": NotRequired[int],
        "ComparisonType": NotRequired[NumberComparisonTypeType],
    },
)

class ContactConfigurationTypeDef(TypedDict):
    ContactId: str
    ParticipantRole: NotRequired[ParticipantRoleType]
    IncludeRawMessage: NotRequired[bool]

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Type": NotRequired[EndpointTypeType],
        "Address": NotRequired[str],
    },
)

class ContactDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]

class ContactEvaluationTypeDef(TypedDict):
    FormId: NotRequired[str]
    EvaluationArn: NotRequired[str]
    Status: NotRequired[StatusType]
    StartTimestamp: NotRequired[datetime]
    EndTimestamp: NotRequired[datetime]
    DeleteTimestamp: NotRequired[datetime]
    ExportLocation: NotRequired[str]

class ContactFilterTypeDef(TypedDict):
    ContactStates: NotRequired[Sequence[ContactStateType]]

class ContactFlowTypeConditionTypeDef(TypedDict):
    ContactFlowType: NotRequired[ContactFlowTypeType]

class ContactFlowModuleAliasInfoTypeDef(TypedDict):
    ContactFlowModuleId: NotRequired[str]
    ContactFlowModuleArn: NotRequired[str]
    AliasId: NotRequired[str]
    Version: NotRequired[int]
    Name: NotRequired[str]
    Description: NotRequired[str]
    LastModifiedRegion: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]

class ContactFlowModuleAliasSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    AliasId: NotRequired[str]
    Version: NotRequired[int]
    AliasName: NotRequired[str]
    AliasDescription: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]

class ContactFlowModuleSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[ContactFlowModuleStateType]

class ExternalInvocationConfigurationTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class ContactFlowModuleVersionSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    VersionDescription: NotRequired[str]
    Version: NotRequired[int]

class ContactFlowSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    ContactFlowType: NotRequired[ContactFlowTypeType]
    ContactFlowState: NotRequired[ContactFlowStateType]
    ContactFlowStatus: NotRequired[ContactFlowStatusType]

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ContactFlowTypeType],
        "State": NotRequired[ContactFlowStateType],
        "Status": NotRequired[ContactFlowStatusType],
        "Description": NotRequired[str],
        "Content": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "FlowContentSha256": NotRequired[str],
        "Version": NotRequired[int],
        "VersionDescription": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
        "LastModifiedRegion": NotRequired[str],
    },
)

class ContactFlowVersionSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    VersionDescription: NotRequired[str]
    Version: NotRequired[int]

class ContactMetricInfoTypeDef(TypedDict):
    Name: Literal["POSITION_IN_QUEUE"]

class ContactMetricValueTypeDef(TypedDict):
    Number: NotRequired[float]

class ContactSearchSummaryAgentInfoTypeDef(TypedDict):
    Id: NotRequired[str]
    ConnectedToAgentTimestamp: NotRequired[datetime]

class ContactSearchSummaryQueueInfoTypeDef(TypedDict):
    Id: NotRequired[str]
    EnqueueTimestamp: NotRequired[datetime]

class SegmentAttributeValuePaginatorTypeDef(TypedDict):
    ValueString: NotRequired[str]
    ValueMap: NotRequired[Dict[str, Dict[str, Any]]]
    ValueInteger: NotRequired[int]
    ValueList: NotRequired[List[Dict[str, Any]]]
    ValueArn: NotRequired[str]

class SegmentAttributeValueOutputTypeDef(TypedDict):
    ValueString: NotRequired[str]
    ValueMap: NotRequired[Dict[str, Dict[str, Any]]]
    ValueInteger: NotRequired[int]
    ValueList: NotRequired[List[Dict[str, Any]]]
    ValueArn: NotRequired[str]

class CustomerVoiceActivityTypeDef(TypedDict):
    GreetingStartTimestamp: NotRequired[datetime]
    GreetingEndTimestamp: NotRequired[datetime]

class DisconnectDetailsTypeDef(TypedDict):
    PotentialDisconnectIssue: NotRequired[str]

EndpointInfoTypeDef = TypedDict(
    "EndpointInfoTypeDef",
    {
        "Type": NotRequired[EndpointTypeType],
        "Address": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)

class QueueInfoTypeDef(TypedDict):
    Id: NotRequired[str]
    EnqueueTimestamp: NotRequired[datetime]

class RecordingInfoTypeDef(TypedDict):
    StorageType: NotRequired[StorageTypeType]
    Location: NotRequired[str]
    MediaStreamType: NotRequired[MediaStreamTypeType]
    ParticipantType: NotRequired[ParticipantTypeType]
    FragmentStartNumber: NotRequired[str]
    FragmentStopNumber: NotRequired[str]
    StartTimestamp: NotRequired[datetime]
    StopTimestamp: NotRequired[datetime]
    Status: NotRequired[RecordingStatusType]
    DeletionReason: NotRequired[str]
    UnprocessedTranscriptLocation: NotRequired[str]

class TaskTemplateInfoV2TypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class CreateAgentStatusRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: NotRequired[str]
    DisplayOrder: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class CreateContactFlowModuleAliasRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    ContactFlowModuleVersion: int
    AliasName: str
    Description: NotRequired[str]

class CreateContactFlowModuleVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    Description: NotRequired[str]
    FlowModuleContentSha256: NotRequired[str]

CreateContactFlowRequestTypeDef = TypedDict(
    "CreateContactFlowRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
        "Description": NotRequired[str],
        "Status": NotRequired[ContactFlowStatusType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
TimestampTypeDef = Union[datetime, str]
ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Type": ReferenceTypeType,
        "Value": NotRequired[str],
        "Status": NotRequired[ReferenceStatusType],
        "Arn": NotRequired[str],
        "StatusReason": NotRequired[str],
    },
)

class UserInfoTypeDef(TypedDict):
    UserId: NotRequired[str]

class CreateDataTableRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    TimeZone: str
    ValueLockLevel: DataTableLockLevelType
    Status: Literal["PUBLISHED"]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateEmailAddressRequestTypeDef(TypedDict):
    InstanceId: str
    EmailAddress: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]

class EvaluationFormAutoEvaluationConfigurationTypeDef(TypedDict):
    Enabled: bool

class EvaluationFormLanguageConfigurationTypeDef(TypedDict):
    FormLanguage: NotRequired[EvaluationFormLanguageCodeType]

class EvaluationFormScoringStrategyTypeDef(TypedDict):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType

class EvaluationFormTargetConfigurationTypeDef(TypedDict):
    ContactInteractionType: ContactInteractionTypeType

class CreateInstanceRequestTypeDef(TypedDict):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: NotRequired[str]
    InstanceAlias: NotRequired[str]
    DirectoryId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateIntegrationAssociationRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationType: IntegrationTypeType
    IntegrationArn: str
    SourceApplicationUrl: NotRequired[str]
    SourceApplicationName: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    Tags: NotRequired[Mapping[str, str]]

class ParticipantTokenCredentialsTypeDef(TypedDict):
    ParticipantToken: NotRequired[str]
    Expiry: NotRequired[str]

class CreatePersistentContactAssociationRequestTypeDef(TypedDict):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: NotRequired[str]

class InputPredefinedAttributeConfigurationTypeDef(TypedDict):
    EnableValueValidationOnAssociation: NotRequired[bool]

class CreatePromptRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class OutboundCallerConfigTypeDef(TypedDict):
    OutboundCallerIdName: NotRequired[str]
    OutboundCallerIdNumberId: NotRequired[str]
    OutboundFlowId: NotRequired[str]

class OutboundEmailConfigTypeDef(TypedDict):
    OutboundEmailAddressId: NotRequired[str]

class RuleTriggerEventSourceTypeDef(TypedDict):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: NotRequired[str]

FlowModuleTypeDef = TypedDict(
    "FlowModuleTypeDef",
    {
        "Type": NotRequired[Literal["MCP"]],
        "FlowModuleId": NotRequired[str],
    },
)

class CreateTrafficDistributionGroupRequestTypeDef(TypedDict):
    Name: str
    InstanceId: str
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateUseCaseRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: NotRequired[Mapping[str, str]]

class CreateUserHierarchyGroupRequestTypeDef(TypedDict):
    Name: str
    InstanceId: str
    ParentGroupId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UserIdentityInfoTypeDef(TypedDict):
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    Email: NotRequired[str]
    SecondaryEmail: NotRequired[str]
    Mobile: NotRequired[str]

class UserPhoneConfigTypeDef(TypedDict):
    PhoneType: PhoneTypeType
    AutoAccept: NotRequired[bool]
    AfterContactWorkTimeLimit: NotRequired[int]
    DeskPhoneNumber: NotRequired[str]
    PersistentConnection: NotRequired[bool]

class ViewInputContentTypeDef(TypedDict):
    Template: NotRequired[str]
    Actions: NotRequired[Sequence[str]]

class CreateViewVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    VersionDescription: NotRequired[str]
    ViewContentSha256: NotRequired[str]

class CreateVocabularyRequestTypeDef(TypedDict):
    InstanceId: str
    VocabularyName: str
    LanguageCode: VocabularyLanguageCodeType
    Content: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateWorkspacePageRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    ResourceArn: str
    Page: str
    Slug: NotRequired[str]
    InputData: NotRequired[str]

class CredentialsTypeDef(TypedDict):
    AccessToken: NotRequired[str]
    AccessTokenExpiration: NotRequired[datetime]
    RefreshToken: NotRequired[str]
    RefreshTokenExpiration: NotRequired[datetime]

class CrossChannelBehaviorTypeDef(TypedDict):
    BehaviorType: BehaviorTypeType

class CurrentMetricTypeDef(TypedDict):
    Name: NotRequired[CurrentMetricNameType]
    MetricId: NotRequired[str]
    Unit: NotRequired[UnitType]

class CurrentMetricSortCriteriaTypeDef(TypedDict):
    SortByMetric: NotRequired[CurrentMetricNameType]
    SortOrder: NotRequired[SortOrderType]

class DataTableSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Arn: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

DateConditionTypeDef = TypedDict(
    "DateConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "Value": NotRequired[str],
        "ComparisonType": NotRequired[DateComparisonTypeType],
    },
)

class DateReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

DateTimeConditionTypeDef = TypedDict(
    "DateTimeConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "MinValue": NotRequired[str],
        "MaxValue": NotRequired[str],
        "ComparisonType": NotRequired[DateTimeComparisonTypeType],
    },
)

class DeactivateEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

DecimalConditionTypeDef = TypedDict(
    "DecimalConditionTypeDef",
    {
        "FieldName": NotRequired[str],
        "MinValue": NotRequired[float],
        "MaxValue": NotRequired[float],
        "ComparisonType": NotRequired[DecimalComparisonTypeType],
    },
)

class DefaultVocabularyTypeDef(TypedDict):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: str
    VocabularyName: str

class DeleteAttachedFileRequestTypeDef(TypedDict):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

class DeleteContactEvaluationRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationId: str

class DeleteContactFlowModuleAliasRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    AliasId: str

class DeleteContactFlowModuleRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str

class DeleteContactFlowModuleVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    ContactFlowModuleVersion: int

class DeleteContactFlowRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str

class DeleteContactFlowVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    ContactFlowVersion: int

class DeleteDataTableAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    AttributeName: str

class DeleteDataTableRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str

class DeleteEmailAddressRequestTypeDef(TypedDict):
    InstanceId: str
    EmailAddressId: str

class DeleteEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: NotRequired[int]

class DeleteHoursOfOperationOverrideRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str

class DeleteHoursOfOperationRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str

class DeleteInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    ClientToken: NotRequired[str]

class DeleteIntegrationAssociationRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationAssociationId: str

class DeletePredefinedAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str

class DeletePromptRequestTypeDef(TypedDict):
    InstanceId: str
    PromptId: str

class DeletePushNotificationRegistrationRequestTypeDef(TypedDict):
    InstanceId: str
    RegistrationId: str
    ContactId: str

class DeleteQueueRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str

class DeleteQuickConnectRequestTypeDef(TypedDict):
    InstanceId: str
    QuickConnectId: str

class DeleteRoutingProfileRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str

class DeleteRuleRequestTypeDef(TypedDict):
    InstanceId: str
    RuleId: str

class DeleteSecurityProfileRequestTypeDef(TypedDict):
    InstanceId: str
    SecurityProfileId: str

class DeleteTaskTemplateRequestTypeDef(TypedDict):
    InstanceId: str
    TaskTemplateId: str

class DeleteTrafficDistributionGroupRequestTypeDef(TypedDict):
    TrafficDistributionGroupId: str

class DeleteUseCaseRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str

class DeleteUserHierarchyGroupRequestTypeDef(TypedDict):
    HierarchyGroupId: str
    InstanceId: str

class DeleteUserRequestTypeDef(TypedDict):
    InstanceId: str
    UserId: str

class DeleteViewRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str

class DeleteViewVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    ViewVersion: int

class DeleteVocabularyRequestTypeDef(TypedDict):
    InstanceId: str
    VocabularyId: str

class DeleteWorkspaceMediaRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    MediaType: MediaTypeType

class DeleteWorkspacePageRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    Page: str

class DeleteWorkspaceRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str

class DescribeAgentStatusRequestTypeDef(TypedDict):
    InstanceId: str
    AgentStatusId: str

class DescribeAuthenticationProfileRequestTypeDef(TypedDict):
    AuthenticationProfileId: str
    InstanceId: str

class DescribeContactEvaluationRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationId: str

class DescribeContactFlowModuleAliasRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    AliasId: str

class DescribeContactFlowModuleRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str

class DescribeContactFlowRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str

class DescribeContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str

class DescribeDataTableAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    AttributeName: str

class DescribeDataTableRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str

class DescribeEmailAddressRequestTypeDef(TypedDict):
    InstanceId: str
    EmailAddressId: str

class DescribeEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: NotRequired[int]

class DescribeHoursOfOperationOverrideRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str

class DescribeHoursOfOperationRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str

class DescribeInstanceAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType

class DescribeInstanceRequestTypeDef(TypedDict):
    InstanceId: str

class DescribeInstanceStorageConfigRequestTypeDef(TypedDict):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType

class DescribePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class DescribePredefinedAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str

class DescribePromptRequestTypeDef(TypedDict):
    InstanceId: str
    PromptId: str

class PromptTypeDef(TypedDict):
    PromptARN: NotRequired[str]
    PromptId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class DescribeQueueRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str

class DescribeQuickConnectRequestTypeDef(TypedDict):
    InstanceId: str
    QuickConnectId: str

class DescribeRoutingProfileRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str

class DescribeRuleRequestTypeDef(TypedDict):
    InstanceId: str
    RuleId: str

class DescribeSecurityProfileRequestTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str

class DescribeTrafficDistributionGroupRequestTypeDef(TypedDict):
    TrafficDistributionGroupId: str

class TrafficDistributionGroupTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    InstanceArn: NotRequired[str]
    Status: NotRequired[TrafficDistributionGroupStatusType]
    Tags: NotRequired[Dict[str, str]]
    IsDefault: NotRequired[bool]

class DescribeUserHierarchyGroupRequestTypeDef(TypedDict):
    HierarchyGroupId: str
    InstanceId: str

class DescribeUserHierarchyStructureRequestTypeDef(TypedDict):
    InstanceId: str

class DescribeUserRequestTypeDef(TypedDict):
    UserId: str
    InstanceId: str

class DescribeViewRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str

class DescribeVocabularyRequestTypeDef(TypedDict):
    InstanceId: str
    VocabularyId: str

class VocabularyTypeDef(TypedDict):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: NotRequired[str]
    Content: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class DescribeWorkspaceRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str

class RoutingProfileReferenceTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class DisassociateAnalyticsDataSetRequestTypeDef(TypedDict):
    InstanceId: str
    DataSetId: str
    TargetAccountId: NotRequired[str]

class DisassociateApprovedOriginRequestTypeDef(TypedDict):
    InstanceId: str
    Origin: str
    ClientToken: NotRequired[str]

class DisassociateFlowRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType

class DisassociateInstanceStorageConfigRequestTypeDef(TypedDict):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    ClientToken: NotRequired[str]

class DisassociateLambdaFunctionRequestTypeDef(TypedDict):
    InstanceId: str
    FunctionArn: str
    ClientToken: NotRequired[str]

class DisassociateLexBotRequestTypeDef(TypedDict):
    InstanceId: str
    BotName: str
    LexRegion: str
    ClientToken: NotRequired[str]

class DisassociatePhoneNumberContactFlowRequestTypeDef(TypedDict):
    PhoneNumberId: str
    InstanceId: str

class DisassociateQueueQuickConnectsRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class RoutingProfileQueueReferenceTypeDef(TypedDict):
    QueueId: str
    Channel: ChannelType

class DisassociateSecurityKeyRequestTypeDef(TypedDict):
    InstanceId: str
    AssociationId: str
    ClientToken: NotRequired[str]

class DisassociateTrafficDistributionGroupUserRequestTypeDef(TypedDict):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyDisassociateTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: str

class DisassociateWorkspaceRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    ResourceArns: Sequence[str]

class DisconnectReasonTypeDef(TypedDict):
    Code: NotRequired[str]

class DismissUserContactRequestTypeDef(TypedDict):
    UserId: str
    InstanceId: str
    ContactId: str

class DownloadUrlMetadataTypeDef(TypedDict):
    Url: NotRequired[str]
    UrlExpiry: NotRequired[str]

class EmailAddressInfoTypeDef(TypedDict):
    EmailAddress: str
    DisplayName: NotRequired[str]

class EmailAttachmentTypeDef(TypedDict):
    FileName: str
    S3Url: str

class EmailMessageReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]

class EmailReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class EncryptionConfigTypeDef(TypedDict):
    EncryptionType: Literal["KMS"]
    KeyId: str

class EvaluationAcknowledgementSummaryTypeDef(TypedDict):
    AcknowledgedTime: NotRequired[datetime]
    AcknowledgedBy: NotRequired[str]
    AcknowledgerComment: NotRequired[str]

class EvaluationAcknowledgementTypeDef(TypedDict):
    AcknowledgedTime: datetime
    AcknowledgedBy: str
    AcknowledgerComment: NotRequired[str]

class EvaluationAnswerDataOutputTypeDef(TypedDict):
    StringValue: NotRequired[str]
    NumericValue: NotRequired[float]
    StringValues: NotRequired[List[str]]
    DateTimeValue: NotRequired[str]
    NotApplicable: NotRequired[bool]

class EvaluationAnswerDataTypeDef(TypedDict):
    StringValue: NotRequired[str]
    NumericValue: NotRequired[float]
    StringValues: NotRequired[Sequence[str]]
    DateTimeValue: NotRequired[str]
    NotApplicable: NotRequired[bool]

class EvaluationContactParticipantTypeDef(TypedDict):
    ContactParticipantRole: NotRequired[ContactParticipantRoleType]
    ContactParticipantId: NotRequired[str]

EvaluationFormItemEnablementSourceTypeDef = TypedDict(
    "EvaluationFormItemEnablementSourceTypeDef",
    {
        "Type": Literal["QUESTION_REF_ID"],
        "RefId": NotRequired[str],
    },
)
EvaluationFormItemEnablementSourceValueTypeDef = TypedDict(
    "EvaluationFormItemEnablementSourceValueTypeDef",
    {
        "Type": Literal["OPTION_REF_ID"],
        "RefId": NotRequired[str],
    },
)

class EvaluationFormSectionOutputTypeDef(TypedDict):
    Title: str
    RefId: str
    Items: List[Dict[str, Any]]
    Instructions: NotRequired[str]
    Weight: NotRequired[float]

class MultiSelectQuestionRuleCategoryAutomationOutputTypeDef(TypedDict):
    Category: str
    Condition: MultiSelectQuestionRuleCategoryAutomationConditionType
    OptionRefIds: List[str]

class EvaluationFormQuestionAutomationAnswerSourceTypeDef(TypedDict):
    SourceType: EvaluationFormQuestionAutomationAnswerSourceTypeType

EvaluationFormMultiSelectQuestionOptionTypeDef = TypedDict(
    "EvaluationFormMultiSelectQuestionOptionTypeDef",
    {
        "RefId": str,
        "Text": str,
    },
)

class NumericQuestionPropertyValueAutomationTypeDef(TypedDict):
    Label: NumericQuestionPropertyAutomationLabelType

class EvaluationFormSearchSummaryTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Status: EvaluationFormVersionStatusType
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    LatestVersion: int
    Description: NotRequired[str]
    LastActivatedTime: NotRequired[datetime]
    LastActivatedBy: NotRequired[str]
    ActiveVersion: NotRequired[int]
    AutoEvaluationEnabled: NotRequired[bool]
    EvaluationFormLanguage: NotRequired[EvaluationFormLanguageCodeType]
    ContactInteractionType: NotRequired[ContactInteractionTypeType]
    Tags: NotRequired[Dict[str, str]]

class EvaluationFormSectionTypeDef(TypedDict):
    Title: str
    RefId: str
    Items: Sequence[Mapping[str, Any]]
    Instructions: NotRequired[str]
    Weight: NotRequired[float]

class SingleSelectQuestionRuleCategoryAutomationTypeDef(TypedDict):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str

class EvaluationFormSummaryTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    LatestVersion: int
    LastActivatedTime: NotRequired[datetime]
    LastActivatedBy: NotRequired[str]
    ActiveVersion: NotRequired[int]

class EvaluationFormVersionSummaryTypeDef(TypedDict):
    EvaluationFormArn: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    Status: EvaluationFormVersionStatusType
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str

class EvaluationScoreTypeDef(TypedDict):
    Percentage: NotRequired[float]
    NotApplicable: NotRequired[bool]
    AutomaticFail: NotRequired[bool]
    AppliedWeight: NotRequired[float]

class EvaluationNoteTypeDef(TypedDict):
    Value: NotRequired[str]

class EvaluationQuestionInputDetailsTypeDef(TypedDict):
    TranscriptType: NotRequired[EvaluationTranscriptTypeType]

class EvaluationSearchMetadataTypeDef(TypedDict):
    ContactId: str
    EvaluatorArn: str
    ContactAgentId: NotRequired[str]
    CalibrationSessionId: NotRequired[str]
    ScorePercentage: NotRequired[float]
    ScoreAutomaticFail: NotRequired[bool]
    ScoreNotApplicable: NotRequired[bool]
    AutoEvaluationEnabled: NotRequired[bool]
    AutoEvaluationStatus: NotRequired[AutoEvaluationStatusType]
    AcknowledgedTime: NotRequired[datetime]
    AcknowledgedBy: NotRequired[str]
    AcknowledgerComment: NotRequired[str]
    SamplingJobId: NotRequired[str]
    ReviewId: NotRequired[str]
    ContactParticipantRole: NotRequired[ContactParticipantRoleType]
    ContactParticipantId: NotRequired[str]

class EvaluationSuggestedAnswerTranscriptMillisecondOffsetsTypeDef(TypedDict):
    BeginOffsetMillis: int

class EvaluatorUserUnionTypeDef(TypedDict):
    ConnectUserArn: NotRequired[str]

class EventBridgeActionDefinitionTypeDef(TypedDict):
    Name: str

class ExpiryTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]
    ExpiryTimestamp: NotRequired[datetime]

class FieldValueUnionTypeDef(TypedDict):
    BooleanValue: NotRequired[bool]
    DoubleValue: NotRequired[float]
    EmptyValue: NotRequired[Mapping[str, Any]]
    StringValue: NotRequired[str]

class FilterV2StringConditionTypeDef(TypedDict):
    Comparison: NotRequired[Literal["NOT_EXISTS"]]

class FiltersTypeDef(TypedDict):
    Queues: NotRequired[Sequence[str]]
    Channels: NotRequired[Sequence[ChannelType]]
    RoutingProfiles: NotRequired[Sequence[str]]
    RoutingStepExpressions: NotRequired[Sequence[str]]
    AgentStatuses: NotRequired[Sequence[str]]
    Subtypes: NotRequired[Sequence[str]]
    ValidationTestTypes: NotRequired[Sequence[str]]

class FlowQuickConnectConfigTypeDef(TypedDict):
    ContactFlowId: str

class FontFamilyTypeDef(TypedDict):
    Default: NotRequired[WorkspaceFontFamilyType]

class GetAttachedFileRequestTypeDef(TypedDict):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: NotRequired[int]

class GetContactAttributesRequestTypeDef(TypedDict):
    InstanceId: str
    InitialContactId: str

class GetEffectiveHoursOfOperationsRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    FromDate: str
    ToDate: str

class GetFederationTokenRequestTypeDef(TypedDict):
    InstanceId: str

class GetFlowAssociationRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class IntervalDetailsTypeDef(TypedDict):
    TimeZone: NotRequired[str]
    IntervalPeriod: NotRequired[IntervalPeriodType]

class GetPromptFileRequestTypeDef(TypedDict):
    InstanceId: str
    PromptId: str

class GetTaskTemplateRequestTypeDef(TypedDict):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: NotRequired[str]

class GetTrafficDistributionRequestTypeDef(TypedDict):
    Id: str

class HierarchyGroupSummaryReferenceTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class HierarchyGroupSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class HierarchyLevelTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class HierarchyLevelUpdateTypeDef(TypedDict):
    Name: str

class ThresholdTypeDef(TypedDict):
    Comparison: NotRequired[Literal["LT"]]
    ThresholdValue: NotRequired[float]

class HoursOfOperationTimeSliceTypeDef(TypedDict):
    Hours: int
    Minutes: int

class OverrideTimeSliceTypeDef(TypedDict):
    Hours: int
    Minutes: int

class HoursOfOperationSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ImagesLogoTypeDef(TypedDict):
    Default: NotRequired[str]
    Favicon: NotRequired[str]

class ImportPhoneNumberRequestTypeDef(TypedDict):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]

class ImportWorkspaceMediaRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    MediaType: MediaTypeType
    MediaSource: str

class InboundRawMessageTypeDef(TypedDict):
    Subject: str
    Body: str
    ContentType: str
    Headers: NotRequired[Mapping[EmailHeaderTypeType, str]]

class InstanceStatusReasonTypeDef(TypedDict):
    Message: NotRequired[str]

class KinesisFirehoseConfigTypeDef(TypedDict):
    FirehoseArn: str

class KinesisStreamConfigTypeDef(TypedDict):
    StreamArn: str

class InstanceSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    IdentityManagementType: NotRequired[DirectoryTypeType]
    InstanceAlias: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    ServiceRole: NotRequired[str]
    InstanceStatus: NotRequired[InstanceStatusType]
    InboundCallsEnabled: NotRequired[bool]
    OutboundCallsEnabled: NotRequired[bool]
    InstanceAccessUrl: NotRequired[str]

class IntegrationAssociationSummaryTypeDef(TypedDict):
    IntegrationAssociationId: NotRequired[str]
    IntegrationAssociationArn: NotRequired[str]
    InstanceId: NotRequired[str]
    IntegrationType: NotRequired[IntegrationTypeType]
    IntegrationArn: NotRequired[str]
    SourceApplicationUrl: NotRequired[str]
    SourceApplicationName: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]

class TaskTemplateFieldIdentifierTypeDef(TypedDict):
    Name: NotRequired[str]

class ListAgentStatusRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AgentStatusTypes: NotRequired[Sequence[AgentStatusTypeType]]

class ListAnalyticsDataAssociationsRequestTypeDef(TypedDict):
    InstanceId: str
    DataSetId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAnalyticsDataLakeDataSetsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListApprovedOriginsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAssociatedContactsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAuthenticationProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListBotsRequestTypeDef(TypedDict):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListContactEvaluationsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    NextToken: NotRequired[str]

class ListContactFlowModuleAliasesRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListContactFlowModuleVersionsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListContactFlowModulesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ContactFlowModuleState: NotRequired[ContactFlowModuleStateType]

class ListContactFlowVersionsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListContactFlowsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowTypes: NotRequired[Sequence[ContactFlowTypeType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListContactReferencesRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    NextToken: NotRequired[str]

class ListDataTableAttributesRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    AttributeIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PrimaryAttributeValueFilterTypeDef(TypedDict):
    AttributeName: str
    Values: Sequence[str]

class ListDataTablesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDefaultVocabulariesRequestTypeDef(TypedDict):
    InstanceId: str
    LanguageCode: NotRequired[VocabularyLanguageCodeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEntitySecurityProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    EntityType: EntityTypeType
    EntityArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEvaluationFormVersionsRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEvaluationFormsRequestTypeDef(TypedDict):
    InstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFlowAssociationsRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceType: NotRequired[ListFlowAssociationResourceTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListHoursOfOperationOverridesRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListHoursOfOperationsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListInstanceAttributesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListInstanceStorageConfigsRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListInstancesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIntegrationAssociationsRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationType: NotRequired[IntegrationTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    IntegrationArn: NotRequired[str]

class ListLambdaFunctionsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLexBotsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPhoneNumbersRequestTypeDef(TypedDict):
    InstanceId: str
    PhoneNumberTypes: NotRequired[Sequence[PhoneNumberTypeType]]
    PhoneNumberCountryCodes: NotRequired[Sequence[PhoneNumberCountryCodeType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PhoneNumberSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]
    PhoneNumberCountryCode: NotRequired[PhoneNumberCountryCodeType]

class ListPhoneNumbersSummaryTypeDef(TypedDict):
    PhoneNumberId: NotRequired[str]
    PhoneNumberArn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    PhoneNumberCountryCode: NotRequired[PhoneNumberCountryCodeType]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    PhoneNumberDescription: NotRequired[str]
    SourcePhoneNumberArn: NotRequired[str]

class ListPhoneNumbersV2RequestTypeDef(TypedDict):
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    PhoneNumberCountryCodes: NotRequired[Sequence[PhoneNumberCountryCodeType]]
    PhoneNumberTypes: NotRequired[Sequence[PhoneNumberTypeType]]
    PhoneNumberPrefix: NotRequired[str]

class ListPredefinedAttributesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PredefinedAttributeSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListPromptsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PromptSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListQueueQuickConnectsRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class QuickConnectSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    QuickConnectType: NotRequired[QuickConnectTypeType]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    QueueTypes: NotRequired[Sequence[QueueTypeType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class QueueSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    QueueType: NotRequired[QueueTypeType]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListQuickConnectsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    QuickConnectTypes: NotRequired[Sequence[QuickConnectTypeType]]

class ListRealtimeContactAnalysisSegmentsV2RequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: Sequence[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRoutingProfileManualAssignmentQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RoutingProfileManualAssignmentQueueConfigSummaryTypeDef(TypedDict):
    QueueId: str
    QueueArn: str
    QueueName: str
    Channel: ChannelType

class ListRoutingProfileQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RoutingProfileQueueConfigSummaryTypeDef(TypedDict):
    QueueId: str
    QueueArn: str
    QueueName: str
    Priority: int
    Delay: int
    Channel: ChannelType

class ListRoutingProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RoutingProfileSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListRulesRequestTypeDef(TypedDict):
    InstanceId: str
    PublishStatus: NotRequired[RulePublishStatusType]
    EventSourceName: NotRequired[EventSourceNameType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSecurityKeysRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SecurityKeyTypeDef(TypedDict):
    AssociationId: NotRequired[str]
    Key: NotRequired[str]
    CreationTime: NotRequired[datetime]

class ListSecurityProfileApplicationsRequestTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSecurityProfileFlowModulesRequestTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSecurityProfilePermissionsRequestTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSecurityProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SecurityProfileSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTaskTemplatesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[TaskTemplateStatusType]
    Name: NotRequired[str]

class TaskTemplateMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[TaskTemplateStatusType]
    LastModifiedTime: NotRequired[datetime]
    CreatedTime: NotRequired[datetime]

class ListTrafficDistributionGroupUsersRequestTypeDef(TypedDict):
    TrafficDistributionGroupId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TrafficDistributionGroupUserSummaryTypeDef(TypedDict):
    UserId: NotRequired[str]

class ListTrafficDistributionGroupsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    InstanceId: NotRequired[str]

class TrafficDistributionGroupSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    InstanceArn: NotRequired[str]
    Status: NotRequired[TrafficDistributionGroupStatusType]
    IsDefault: NotRequired[bool]

class ListUseCasesRequestTypeDef(TypedDict):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class UseCaseTypeDef(TypedDict):
    UseCaseId: NotRequired[str]
    UseCaseArn: NotRequired[str]
    UseCaseType: NotRequired[UseCaseTypeType]

class ListUserHierarchyGroupsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListUserProficienciesRequestTypeDef(TypedDict):
    InstanceId: str
    UserId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListUsersRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class UserSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Username: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class ListViewVersionsRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ViewVersionSummaryTypeDef = TypedDict(
    "ViewVersionSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ViewTypeType],
        "Version": NotRequired[int],
        "VersionDescription": NotRequired[str],
    },
)
ListViewsRequestTypeDef = TypedDict(
    "ListViewsRequestTypeDef",
    {
        "InstanceId": str,
        "Type": NotRequired[ViewTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ViewSummaryTypeDef = TypedDict(
    "ViewSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ViewTypeType],
        "Status": NotRequired[ViewStatusType],
        "Description": NotRequired[str],
    },
)

class ListWorkspaceMediaRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str

MediaItemTypeDef = TypedDict(
    "MediaItemTypeDef",
    {
        "Type": NotRequired[MediaTypeType],
        "Source": NotRequired[str],
    },
)

class ListWorkspacePagesRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class WorkspacePageTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    Page: NotRequired[str]
    Slug: NotRequired[str]
    InputData: NotRequired[str]

class ListWorkspacesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class WorkspaceSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class MediaPlacementTypeDef(TypedDict):
    AudioHostUrl: NotRequired[str]
    AudioFallbackUrl: NotRequired[str]
    SignalingUrl: NotRequired[str]
    TurnControlUrl: NotRequired[str]
    EventIngestionUrl: NotRequired[str]

class MetricFilterV2OutputTypeDef(TypedDict):
    MetricFilterKey: NotRequired[str]
    MetricFilterValues: NotRequired[List[str]]
    Negate: NotRequired[bool]

class MetricFilterV2TypeDef(TypedDict):
    MetricFilterKey: NotRequired[str]
    MetricFilterValues: NotRequired[Sequence[str]]
    Negate: NotRequired[bool]

class MetricIntervalTypeDef(TypedDict):
    Interval: NotRequired[IntervalPeriodType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class ThresholdV2TypeDef(TypedDict):
    Comparison: NotRequired[str]
    ThresholdValue: NotRequired[float]

class MonitorContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    UserId: str
    AllowedMonitorCapabilities: NotRequired[Sequence[MonitorCapabilityType]]
    ClientToken: NotRequired[str]

class MultiSelectQuestionRuleCategoryAutomationTypeDef(TypedDict):
    Category: str
    Condition: MultiSelectQuestionRuleCategoryAutomationConditionType
    OptionRefIds: Sequence[str]

class NameCriteriaTypeDef(TypedDict):
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType

class ParticipantDetailsTypeDef(TypedDict):
    DisplayName: str

class QuickConnectContactDataTypeDef(TypedDict):
    ContactId: NotRequired[str]
    InitiationTimestamp: NotRequired[datetime]
    QuickConnectId: NotRequired[str]
    QuickConnectName: NotRequired[str]
    QuickConnectType: NotRequired[QuickConnectTypeType]

class NotificationRecipientTypeOutputTypeDef(TypedDict):
    UserTags: NotRequired[Dict[str, str]]
    UserIds: NotRequired[List[str]]

class NotificationRecipientTypeTypeDef(TypedDict):
    UserTags: NotRequired[Mapping[str, str]]
    UserIds: NotRequired[Sequence[str]]

class NumberReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class OutboundRawMessageTypeDef(TypedDict):
    Subject: str
    Body: str
    ContentType: str

class PaletteCanvasTypeDef(TypedDict):
    ContainerBackground: NotRequired[str]
    PageBackground: NotRequired[str]
    ActiveBackground: NotRequired[str]

PaletteHeaderTypeDef = TypedDict(
    "PaletteHeaderTypeDef",
    {
        "Background": NotRequired[str],
        "Text": NotRequired[str],
        "TextHover": NotRequired[str],
        "InvertActionsColors": NotRequired[bool],
    },
)
PaletteNavigationTypeDef = TypedDict(
    "PaletteNavigationTypeDef",
    {
        "Background": NotRequired[str],
        "TextBackgroundHover": NotRequired[str],
        "TextBackgroundActive": NotRequired[str],
        "Text": NotRequired[str],
        "TextHover": NotRequired[str],
        "TextActive": NotRequired[str],
        "InvertActionsColors": NotRequired[bool],
    },
)

class PalettePrimaryTypeDef(TypedDict):
    Default: NotRequired[str]
    Active: NotRequired[str]
    ContrastText: NotRequired[str]

class ParticipantConfigurationTypeDef(TypedDict):
    ResponseMode: NotRequired[ResponseModeType]

class ParticipantTimerValueTypeDef(TypedDict):
    ParticipantTimerAction: NotRequired[Literal["Unset"]]
    ParticipantTimerDurationInMinutes: NotRequired[int]

class PauseContactRequestTypeDef(TypedDict):
    ContactId: str
    InstanceId: str
    ContactFlowId: NotRequired[str]

class PersistentChatTypeDef(TypedDict):
    RehydrationType: NotRequired[RehydrationTypeType]
    SourceContactId: NotRequired[str]

class PhoneNumberQuickConnectConfigTypeDef(TypedDict):
    PhoneNumber: str

class PostAcceptTimeoutConfigTypeDef(TypedDict):
    DurationInSeconds: int

class PredefinedAttributeConfigurationTypeDef(TypedDict):
    EnableValueValidationOnAssociation: NotRequired[bool]
    IsReadOnly: NotRequired[bool]

class PredefinedAttributeValuesOutputTypeDef(TypedDict):
    StringList: NotRequired[List[str]]

class PredefinedAttributeValuesTypeDef(TypedDict):
    StringList: NotRequired[Sequence[str]]

class PrimaryAttributeValueOutputTypeDef(TypedDict):
    AccessType: NotRequired[Literal["ALLOW"]]
    AttributeName: NotRequired[str]
    Values: NotRequired[List[str]]

class PrimaryAttributeValueTypeDef(TypedDict):
    AccessType: NotRequired[Literal["ALLOW"]]
    AttributeName: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class PutUserStatusRequestTypeDef(TypedDict):
    UserId: str
    InstanceId: str
    AgentStatusId: str

class QueueInfoInputTypeDef(TypedDict):
    Id: NotRequired[str]

class QueueQuickConnectConfigTypeDef(TypedDict):
    QueueId: str
    ContactFlowId: str

class UserQuickConnectConfigTypeDef(TypedDict):
    UserId: str
    ContactFlowId: str

class RealTimeContactAnalysisAttachmentTypeDef(TypedDict):
    AttachmentName: str
    AttachmentId: str
    ContentType: NotRequired[str]
    Status: NotRequired[ArtifactStatusType]

class RealTimeContactAnalysisCharacterIntervalTypeDef(TypedDict):
    BeginOffsetChar: int
    EndOffsetChar: int

class RealTimeContactAnalysisTimeDataTypeDef(TypedDict):
    AbsoluteTime: NotRequired[datetime]

class RealTimeContactAnalysisSegmentPostContactSummaryTypeDef(TypedDict):
    Status: RealTimeContactAnalysisPostContactSummaryStatusType
    Content: NotRequired[str]
    FailureCode: NotRequired[RealTimeContactAnalysisPostContactSummaryFailureCodeType]

class StringReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class UrlReferenceTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class ReleasePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str
    ClientToken: NotRequired[str]

class ReplicateInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    ReplicaRegion: str
    ReplicaAlias: str
    ClientToken: NotRequired[str]

class ReplicationStatusSummaryTypeDef(TypedDict):
    Region: NotRequired[str]
    ReplicationStatus: NotRequired[InstanceReplicationStatusType]
    ReplicationStatusReason: NotRequired[str]

class TagSearchConditionTypeDef(TypedDict):
    tagKey: NotRequired[str]
    tagValue: NotRequired[str]
    tagKeyComparisonType: NotRequired[StringComparisonTypeType]
    tagValueComparisonType: NotRequired[StringComparisonTypeType]

class ResumeContactRecordingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: NotRequired[ContactRecordingTypeType]

class ResumeContactRequestTypeDef(TypedDict):
    ContactId: str
    InstanceId: str
    ContactFlowId: NotRequired[str]

class RoutingCriteriaInputStepExpiryTypeDef(TypedDict):
    DurationInSeconds: NotRequired[int]

class SubmitAutoEvaluationActionDefinitionTypeDef(TypedDict):
    EvaluationFormId: str

class SearchAvailablePhoneNumbersRequestTypeDef(TypedDict):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    PhoneNumberPrefix: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

SearchContactsTimestampConditionTypeDef = TypedDict(
    "SearchContactsTimestampConditionTypeDef",
    {
        "Type": SearchContactsTimeRangeTypeType,
        "ConditionType": Literal["NOT_EXISTS"],
    },
)

class SortTypeDef(TypedDict):
    FieldName: SortableFieldNameType
    Order: SortOrderType

class TagSetTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class SecurityProfileSearchSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    OrganizationResourceId: NotRequired[str]
    Arn: NotRequired[str]
    SecurityProfileName: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class SearchVocabulariesRequestTypeDef(TypedDict):
    InstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    State: NotRequired[VocabularyStateType]
    NameStartsWith: NotRequired[str]
    LanguageCode: NotRequired[VocabularyLanguageCodeType]

class VocabularySummaryTypeDef(TypedDict):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: NotRequired[str]

class WorkspaceAssociationSearchSummaryTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]
    WorkspaceArn: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceName: NotRequired[str]

class WorkspaceSearchSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Visibility: NotRequired[VisibilityType]
    Description: NotRequired[str]
    Title: NotRequired[str]
    Arn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]

class SearchableAgentCriteriaStepTypeDef(TypedDict):
    AgentIds: NotRequired[Sequence[str]]
    MatchType: NotRequired[SearchContactsMatchTypeType]

class SearchableContactAttributesCriteriaTypeDef(TypedDict):
    Key: str
    Values: Sequence[str]

class SearchableSegmentAttributesCriteriaTypeDef(TypedDict):
    Key: str
    Values: Sequence[str]

class SegmentAttributeValueTypeDef(TypedDict):
    ValueString: NotRequired[str]
    ValueMap: NotRequired[Mapping[str, Mapping[str, Any]]]
    ValueInteger: NotRequired[int]
    ValueList: NotRequired[Sequence[Mapping[str, Any]]]
    ValueArn: NotRequired[str]

class SourceCampaignTypeDef(TypedDict):
    CampaignId: NotRequired[str]
    OutboundRequestId: NotRequired[str]

class SignInDistributionTypeDef(TypedDict):
    Region: str
    Enabled: bool

class UploadUrlMetadataTypeDef(TypedDict):
    Url: NotRequired[str]
    UrlExpiry: NotRequired[str]
    HeadersToInclude: NotRequired[Dict[str, str]]

class StartContactMediaProcessingRequestTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    ContactId: NotRequired[str]
    ProcessorArn: NotRequired[str]
    FailureMode: NotRequired[ContactMediaProcessingFailureModeType]

class VoiceRecordingConfigurationTypeDef(TypedDict):
    VoiceRecordingTrack: NotRequired[VoiceRecordingTrackType]
    IvrRecordingTrack: NotRequired[Literal["ALL"]]

class StartScreenSharingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ClientToken: NotRequired[str]

class StopContactMediaProcessingRequestTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    ContactId: NotRequired[str]

class StopContactRecordingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: NotRequired[ContactRecordingTypeType]

class StopContactStreamingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    StreamingId: str

class SuspendContactRecordingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: NotRequired[ContactRecordingTypeType]

class TagContactRequestTypeDef(TypedDict):
    ContactId: str
    InstanceId: str
    Tags: Mapping[str, str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TemplateAttributesTypeDef(TypedDict):
    CustomAttributes: NotRequired[Mapping[str, str]]
    CustomerProfileAttributes: NotRequired[str]

class TranscriptCriteriaTypeDef(TypedDict):
    ParticipantRole: ParticipantRoleType
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType

class TransferContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ContactFlowId: str
    QueueId: NotRequired[str]
    UserId: NotRequired[str]
    ClientToken: NotRequired[str]

class UntagContactRequestTypeDef(TypedDict):
    ContactId: str
    InstanceId: str
    TagKeys: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentStatusRequestTypeDef(TypedDict):
    InstanceId: str
    AgentStatusId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[AgentStatusStateType]
    DisplayOrder: NotRequired[int]
    ResetOrderNumber: NotRequired[bool]

class UpdateAuthenticationProfileRequestTypeDef(TypedDict):
    AuthenticationProfileId: str
    InstanceId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    AllowedIps: NotRequired[Sequence[str]]
    BlockedIps: NotRequired[Sequence[str]]
    PeriodicSessionDuration: NotRequired[int]
    SessionInactivityDuration: NotRequired[int]
    SessionInactivityHandlingEnabled: NotRequired[bool]

class UpdateContactAttributesRequestTypeDef(TypedDict):
    InitialContactId: str
    InstanceId: str
    Attributes: Mapping[str, str]

class UpdateContactFlowContentRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    Content: str

class UpdateContactFlowMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    ContactFlowState: NotRequired[ContactFlowStateType]

class UpdateContactFlowModuleAliasRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    AliasId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    ContactFlowModuleVersion: NotRequired[int]

class UpdateContactFlowModuleContentRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    Content: NotRequired[str]
    Settings: NotRequired[str]

class UpdateContactFlowModuleMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[ContactFlowModuleStateType]

class UpdateContactFlowNameRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateDataTableMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Name: str
    ValueLockLevel: DataTableLockLevelType
    TimeZone: str
    Description: NotRequired[str]

class UpdateEmailAddressMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    EmailAddressId: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    ClientToken: NotRequired[str]

class UpdateInstanceAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType
    Value: str
    ClientToken: NotRequired[str]

class UpdateParticipantAuthenticationRequestTypeDef(TypedDict):
    State: str
    InstanceId: str
    Code: NotRequired[str]
    Error: NotRequired[str]
    ErrorDescription: NotRequired[str]

class UpdatePhoneNumberMetadataRequestTypeDef(TypedDict):
    PhoneNumberId: str
    PhoneNumberDescription: NotRequired[str]
    ClientToken: NotRequired[str]

class UpdatePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    ClientToken: NotRequired[str]

class UpdatePromptRequestTypeDef(TypedDict):
    InstanceId: str
    PromptId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    S3Uri: NotRequired[str]

class UpdateQueueHoursOfOperationRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str

class UpdateQueueMaxContactsRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    MaxContacts: NotRequired[int]

class UpdateQueueNameRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateQueueStatusRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType

class UpdateQuickConnectNameRequestTypeDef(TypedDict):
    InstanceId: str
    QuickConnectId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType

class UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str

class UpdateRoutingProfileNameRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateUserHierarchyGroupNameRequestTypeDef(TypedDict):
    Name: str
    HierarchyGroupId: str
    InstanceId: str

class UpdateUserHierarchyRequestTypeDef(TypedDict):
    UserId: str
    InstanceId: str
    HierarchyGroupId: NotRequired[str]

class UpdateUserRoutingProfileRequestTypeDef(TypedDict):
    RoutingProfileId: str
    UserId: str
    InstanceId: str

class UpdateUserSecurityProfilesRequestTypeDef(TypedDict):
    SecurityProfileIds: Sequence[str]
    UserId: str
    InstanceId: str

class UpdateViewMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateWorkspaceMetadataRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Title: NotRequired[str]

class UpdateWorkspacePageRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    Page: str
    NewPage: NotRequired[str]
    ResourceArn: NotRequired[str]
    Slug: NotRequired[str]
    InputData: NotRequired[str]

class UpdateWorkspaceVisibilityRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    Visibility: VisibilityType

class UserReferenceTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class UserIdentityInfoLiteTypeDef(TypedDict):
    FirstName: NotRequired[str]
    LastName: NotRequired[str]

class ValidationEnumOutputTypeDef(TypedDict):
    Strict: NotRequired[bool]
    Values: NotRequired[List[str]]

class ValidationEnumTypeDef(TypedDict):
    Strict: NotRequired[bool]
    Values: NotRequired[Sequence[str]]

class ViewContentTypeDef(TypedDict):
    InputSchema: NotRequired[str]
    Template: NotRequired[str]
    Actions: NotRequired[List[str]]

class RuleSummaryTypeDef(TypedDict):
    Name: str
    RuleId: str
    RuleArn: str
    EventSourceName: EventSourceNameType
    PublishStatus: RulePublishStatusType
    ActionSummaries: List[ActionSummaryTypeDef]
    CreatedTime: datetime
    LastUpdatedTime: datetime

class ActivateEvaluationFormResponseTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateAnalyticsDataSetResponseTypeDef(TypedDict):
    DataSetId: str
    TargetAccountId: str
    ResourceShareId: str
    ResourceShareArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateInstanceStorageConfigResponseTypeDef(TypedDict):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSecurityKeyResponseTypeDef(TypedDict):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClaimPhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentStatusResponseTypeDef(TypedDict):
    AgentStatusARN: str
    AgentStatusId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowModuleAliasResponseTypeDef(TypedDict):
    ContactFlowModuleArn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowModuleResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowModuleVersionResponseTypeDef(TypedDict):
    ContactFlowModuleArn: str
    Version: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowResponseTypeDef(TypedDict):
    ContactFlowId: str
    ContactFlowArn: str
    FlowContentSha256: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowVersionResponseTypeDef(TypedDict):
    ContactFlowArn: str
    Version: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactResponseTypeDef(TypedDict):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEmailAddressResponseTypeDef(TypedDict):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationFormResponseTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHoursOfOperationOverrideResponseTypeDef(TypedDict):
    HoursOfOperationOverrideId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHoursOfOperationResponseTypeDef(TypedDict):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationAssociationResponseTypeDef(TypedDict):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePersistentContactAssociationResponseTypeDef(TypedDict):
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePromptResponseTypeDef(TypedDict):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePushNotificationRegistrationResponseTypeDef(TypedDict):
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(TypedDict):
    QueueArn: str
    QueueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuickConnectResponseTypeDef(TypedDict):
    QuickConnectARN: str
    QuickConnectId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoutingProfileResponseTypeDef(TypedDict):
    RoutingProfileArn: str
    RoutingProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(TypedDict):
    RuleArn: str
    RuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityProfileResponseTypeDef(TypedDict):
    SecurityProfileId: str
    SecurityProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskTemplateResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficDistributionGroupResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUseCaseResponseTypeDef(TypedDict):
    UseCaseId: str
    UseCaseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserHierarchyGroupResponseTypeDef(TypedDict):
    HierarchyGroupId: str
    HierarchyGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(TypedDict):
    UserId: str
    UserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyResponseTypeDef(TypedDict):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(TypedDict):
    WorkspaceId: str
    WorkspaceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateEvaluationFormResponseTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVocabularyResponseTypeDef(TypedDict):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactAttributesResponseTypeDef(TypedDict):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowAssociationResponseTypeDef(TypedDict):
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetPromptFileResponseTypeDef(TypedDict):
    PromptPresignedUrl: str
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApprovedOriginsResponseTypeDef(TypedDict):
    Origins: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLambdaFunctionsResponseTypeDef(TypedDict):
    LambdaFunctions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSecurityProfilePermissionsResponseTypeDef(TypedDict):
    Permissions: List[str]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MonitorContactResponseTypeDef(TypedDict):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateInstanceResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendChatIntegrationEventResponseTypeDef(TypedDict):
    InitialContactId: str
    NewChatCreated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartChatContactResponseTypeDef(TypedDict):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactEvaluationResponseTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactStreamingResponseTypeDef(TypedDict):
    StreamingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEmailContactResponseTypeDef(TypedDict):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOutboundChatContactResponseTypeDef(TypedDict):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOutboundEmailContactResponseTypeDef(TypedDict):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOutboundVoiceContactResponseTypeDef(TypedDict):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskContactResponseTypeDef(TypedDict):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitContactEvaluationResponseTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferContactResponseTypeDef(TypedDict):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactEvaluationResponseTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEmailAddressMetadataResponseTypeDef(TypedDict):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluationFormResponseTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(TypedDict):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePromptResponseTypeDef(TypedDict):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdditionalEmailRecipientsTypeDef(TypedDict):
    ToList: NotRequired[List[EmailRecipientTypeDef]]
    CcList: NotRequired[List[EmailRecipientTypeDef]]

class AgentConfigOutputTypeDef(TypedDict):
    Distributions: List[DistributionTypeDef]

class AgentConfigTypeDef(TypedDict):
    Distributions: Sequence[DistributionTypeDef]

class TelephonyConfigOutputTypeDef(TypedDict):
    Distributions: List[DistributionTypeDef]

class TelephonyConfigTypeDef(TypedDict):
    Distributions: Sequence[DistributionTypeDef]

class AgentContactReferenceTypeDef(TypedDict):
    ContactId: NotRequired[str]
    Channel: NotRequired[ChannelType]
    InitiationMethod: NotRequired[ContactInitiationMethodType]
    AgentContactState: NotRequired[ContactStateType]
    StateStartTimestamp: NotRequired[datetime]
    ConnectedToAgentTimestamp: NotRequired[datetime]
    Queue: NotRequired[QueueReferenceTypeDef]

class HierarchyGroupsTypeDef(TypedDict):
    Level1: NotRequired[AgentHierarchyGroupTypeDef]
    Level2: NotRequired[AgentHierarchyGroupTypeDef]
    Level3: NotRequired[AgentHierarchyGroupTypeDef]
    Level4: NotRequired[AgentHierarchyGroupTypeDef]
    Level5: NotRequired[AgentHierarchyGroupTypeDef]

class AllowedCapabilitiesTypeDef(TypedDict):
    Customer: NotRequired[ParticipantCapabilitiesTypeDef]
    Agent: NotRequired[ParticipantCapabilitiesTypeDef]

class CustomerTypeDef(TypedDict):
    DeviceInfo: NotRequired[DeviceInfoTypeDef]
    Capabilities: NotRequired[ParticipantCapabilitiesTypeDef]

class ParticipantDetailsToAddTypeDef(TypedDict):
    ParticipantRole: NotRequired[ParticipantRoleType]
    DisplayName: NotRequired[str]
    ParticipantCapabilities: NotRequired[ParticipantCapabilitiesTypeDef]

class AgentQualityMetricsTypeDef(TypedDict):
    Audio: NotRequired[AudioQualityMetricsInfoTypeDef]

class CustomerQualityMetricsTypeDef(TypedDict):
    Audio: NotRequired[AudioQualityMetricsInfoTypeDef]

class AgentStatusSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class AgentStatusSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class ContactFlowModuleSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    StateCondition: NotRequired[ContactFlowModuleStateType]
    StatusCondition: NotRequired[ContactFlowModuleStatusType]

class ContactFlowModuleSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    StateCondition: NotRequired[ContactFlowModuleStateType]
    StatusCondition: NotRequired[ContactFlowModuleStatusType]

class ContactFlowSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    TypeCondition: NotRequired[ContactFlowTypeType]
    StateCondition: NotRequired[ContactFlowStateType]
    StatusCondition: NotRequired[ContactFlowStatusType]

class ContactFlowSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    TypeCondition: NotRequired[ContactFlowTypeType]
    StateCondition: NotRequired[ContactFlowStateType]
    StatusCondition: NotRequired[ContactFlowStatusType]

class DataTableSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class DataTableSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class EmailAddressSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class HoursOfOperationSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class HoursOfOperationSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class PredefinedAttributeSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class PredefinedAttributeSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class PromptSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class PromptSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class QueueSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    QueueTypeCondition: NotRequired[Literal["STANDARD"]]

class QueueSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    QueueTypeCondition: NotRequired[Literal["STANDARD"]]

class QuickConnectSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class QuickConnectSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class RoutingProfileSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class RoutingProfileSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class SecurityProfileSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class SecurityProfileSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class UserHierarchyGroupSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class UserHierarchyGroupSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class ViewSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    ViewTypeCondition: NotRequired[ViewTypeType]
    ViewStatusCondition: NotRequired[ViewStatusType]

class ViewSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    ViewTypeCondition: NotRequired[ViewTypeType]
    ViewStatusCondition: NotRequired[ViewStatusType]

class WorkspaceAssociationSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class WorkspaceAssociationSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class WorkspaceSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class WorkspaceSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]

class ListAgentStatusResponseTypeDef(TypedDict):
    AgentStatusSummaryList: List[AgentStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeAgentStatusResponseTypeDef(TypedDict):
    AgentStatus: AgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAgentStatusesResponseTypeDef(TypedDict):
    AgentStatuses: List[AgentStatusTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MatchCriteriaOutputTypeDef(TypedDict):
    AgentsCriteria: NotRequired[AgentsCriteriaOutputTypeDef]

AgentsCriteriaUnionTypeDef = Union[AgentsCriteriaTypeDef, AgentsCriteriaOutputTypeDef]

class WisdomInfoTypeDef(TypedDict):
    SessionArn: NotRequired[str]
    AiAgents: NotRequired[List[AiAgentInfoTypeDef]]

class AssociateEmailAddressAliasRequestTypeDef(TypedDict):
    EmailAddressId: str
    InstanceId: str
    AliasConfiguration: AliasConfigurationTypeDef
    ClientToken: NotRequired[str]

class DescribeEmailAddressResponseTypeDef(TypedDict):
    EmailAddressId: str
    EmailAddressArn: str
    EmailAddress: str
    DisplayName: str
    Description: str
    CreateTimestamp: str
    ModifiedTimestamp: str
    AliasConfigurations: List[AliasConfigurationTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateEmailAddressAliasRequestTypeDef(TypedDict):
    EmailAddressId: str
    InstanceId: str
    AliasConfiguration: AliasConfigurationTypeDef
    ClientToken: NotRequired[str]

class EmailAddressMetadataTypeDef(TypedDict):
    EmailAddressId: NotRequired[str]
    EmailAddressArn: NotRequired[str]
    EmailAddress: NotRequired[str]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    AliasConfigurations: NotRequired[List[AliasConfigurationTypeDef]]

class ListAnalyticsDataAssociationsResponseTypeDef(TypedDict):
    Results: List[AnalyticsDataAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAnalyticsDataLakeDataSetsResponseTypeDef(TypedDict):
    Results: List[AnalyticsDataSetsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSecurityProfileApplicationsResponseTypeDef(TypedDict):
    Applications: List[ApplicationOutputTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ApplicationUnionTypeDef = Union[ApplicationTypeDef, ApplicationOutputTypeDef]

class AssociateLexBotRequestTypeDef(TypedDict):
    InstanceId: str
    LexBot: LexBotTypeDef
    ClientToken: NotRequired[str]

class ListLexBotsResponseTypeDef(TypedDict):
    LexBots: List[LexBotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateBotRequestTypeDef(TypedDict):
    InstanceId: str
    LexBot: NotRequired[LexBotTypeDef]
    LexV2Bot: NotRequired[LexV2BotTypeDef]
    ClientToken: NotRequired[str]

class DisassociateBotRequestTypeDef(TypedDict):
    InstanceId: str
    LexBot: NotRequired[LexBotTypeDef]
    LexV2Bot: NotRequired[LexV2BotTypeDef]
    ClientToken: NotRequired[str]

class LexBotConfigTypeDef(TypedDict):
    LexBot: NotRequired[LexBotTypeDef]
    LexV2Bot: NotRequired[LexV2BotTypeDef]

class AssociateSecurityProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    SecurityProfiles: Sequence[SecurityProfileItemTypeDef]
    EntityType: EntityTypeType
    EntityArn: str

class DisassociateSecurityProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    SecurityProfiles: Sequence[SecurityProfileItemTypeDef]
    EntityType: EntityTypeType
    EntityArn: str

class ListEntitySecurityProfilesResponseTypeDef(TypedDict):
    SecurityProfiles: List[SecurityProfileItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateUserProficienciesRequestTypeDef(TypedDict):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class ListUserProficienciesResponseTypeDef(TypedDict):
    UserProficiencyList: List[UserProficiencyTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateUserProficienciesRequestTypeDef(TypedDict):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class AssociateWorkspaceResponseTypeDef(TypedDict):
    SuccessfulList: List[SuccessfulBatchAssociationSummaryTypeDef]
    FailedList: List[FailedBatchAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateWorkspaceResponseTypeDef(TypedDict):
    SuccessfulList: List[SuccessfulBatchAssociationSummaryTypeDef]
    FailedList: List[FailedBatchAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedContactsResponseTypeDef(TypedDict):
    ContactSummaryList: List[AssociatedContactSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttachedFileTypeDef(TypedDict):
    CreationTime: str
    FileArn: str
    FileId: str
    FileName: str
    FileSizeInBytes: int
    FileStatus: FileStatusTypeType
    CreatedBy: NotRequired[CreatedByInfoTypeDef]
    FileUseCaseType: NotRequired[FileUseCaseTypeType]
    AssociatedResourceArn: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class StartAttachedFileUploadRequestTypeDef(TypedDict):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: FileUseCaseTypeType
    AssociatedResourceArn: str
    ClientToken: NotRequired[str]
    UrlExpiryInSeconds: NotRequired[int]
    CreatedBy: NotRequired[CreatedByInfoTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class AttributeAndConditionTypeDef(TypedDict):
    TagConditions: NotRequired[Sequence[TagConditionTypeDef]]
    HierarchyGroupCondition: NotRequired[HierarchyGroupConditionTypeDef]

class CommonAttributeAndConditionTypeDef(TypedDict):
    TagConditions: NotRequired[Sequence[TagConditionTypeDef]]

class ControlPlaneTagFilterTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Sequence[TagConditionTypeDef]]]
    AndConditions: NotRequired[Sequence[TagConditionTypeDef]]
    TagCondition: NotRequired[TagConditionTypeDef]

class DescribeInstanceAttributeResponseTypeDef(TypedDict):
    Attribute: AttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceAttributesResponseTypeDef(TypedDict):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MeetingFeaturesConfigurationTypeDef(TypedDict):
    Audio: NotRequired[AudioFeaturesTypeDef]

class ListAuthenticationProfilesResponseTypeDef(TypedDict):
    AuthenticationProfileSummaryList: List[AuthenticationProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeAuthenticationProfileResponseTypeDef(TypedDict):
    AuthenticationProfile: AuthenticationProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactEvaluationRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    AutoEvaluationConfiguration: NotRequired[AutoEvaluationConfigurationTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class EvaluationFormNumericQuestionOptionTypeDef(TypedDict):
    MinValue: int
    MaxValue: int
    Score: NotRequired[int]
    AutomaticFail: NotRequired[bool]
    AutomaticFailConfiguration: NotRequired[AutomaticFailConfigurationTypeDef]

EvaluationFormSingleSelectQuestionOptionTypeDef = TypedDict(
    "EvaluationFormSingleSelectQuestionOptionTypeDef",
    {
        "RefId": str,
        "Text": str,
        "Score": NotRequired[int],
        "AutomaticFail": NotRequired[bool],
        "AutomaticFailConfiguration": NotRequired[AutomaticFailConfigurationTypeDef],
    },
)

class SearchAvailablePhoneNumbersResponseTypeDef(TypedDict):
    AvailableNumbersList: List[AvailableNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchAssociateAnalyticsDataSetResponseTypeDef(TypedDict):
    Created: List[AnalyticsDataAssociationResultTypeDef]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAnalyticsDataSetResponseTypeDef(TypedDict):
    Deleted: List[str]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDataTableValueFailureResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    Message: str

class BatchDeleteDataTableValueFailureResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    Message: str

class BatchDescribeDataTableValueFailureResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    Message: str

class BatchUpdateDataTableValueFailureResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    Message: str

class DataTableEvaluatedValueTypeDef(TypedDict):
    RecordId: str
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    ValueType: DataTableAttributeValueTypeType
    Found: bool
    Error: bool
    EvaluatedValue: str

class DataTableValueEvaluationSetTypeDef(TypedDict):
    AttributeNames: Sequence[str]
    PrimaryValues: NotRequired[Sequence[PrimaryValueTypeDef]]

class DataTableValueIdentifierTypeDef(TypedDict):
    AttributeName: str
    PrimaryValues: NotRequired[Sequence[PrimaryValueTypeDef]]

class BatchCreateDataTableValueSuccessResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    RecordId: str
    LockVersion: DataTableLockVersionTypeDef

class BatchDeleteDataTableValueSuccessResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    LockVersion: DataTableLockVersionTypeDef

class BatchUpdateDataTableValueSuccessResultTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueTypeDef]
    AttributeName: str
    LockVersion: DataTableLockVersionTypeDef

class CreateDataTableAttributeResponseTypeDef(TypedDict):
    Name: str
    AttributeId: str
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataTableResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataTableDeleteValueIdentifierTypeDef(TypedDict):
    AttributeName: str
    LockVersion: DataTableLockVersionTypeDef
    PrimaryValues: NotRequired[Sequence[PrimaryValueTypeDef]]

class DataTableTypeDef(TypedDict):
    Name: str
    Id: str
    Arn: str
    TimeZone: str
    LastModifiedTime: datetime
    Description: NotRequired[str]
    ValueLockLevel: NotRequired[DataTableLockLevelType]
    LockVersion: NotRequired[DataTableLockVersionTypeDef]
    Version: NotRequired[str]
    VersionDescription: NotRequired[str]
    Status: NotRequired[Literal["PUBLISHED"]]
    CreatedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class DeleteDataTableAttributeResponseTypeDef(TypedDict):
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataTableAttributeResponseTypeDef(TypedDict):
    Name: str
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataTableMetadataResponseTypeDef(TypedDict):
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataTablePrimaryValuesRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    PrimaryValues: Sequence[PrimaryValueTypeDef]
    NewPrimaryValues: Sequence[PrimaryValueTypeDef]
    LockVersion: DataTableLockVersionTypeDef

class UpdateDataTablePrimaryValuesResponseTypeDef(TypedDict):
    LockVersion: DataTableLockVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDescribeDataTableValueSuccessResultTypeDef(TypedDict):
    RecordId: str
    AttributeId: str
    PrimaryValues: List[PrimaryValueResponseTypeDef]
    AttributeName: str
    LockVersion: DataTableLockVersionTypeDef
    Value: NotRequired[str]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class DataTableValueSummaryTypeDef(TypedDict):
    PrimaryValues: List[PrimaryValueResponseTypeDef]
    AttributeName: str
    ValueType: DataTableAttributeValueTypeType
    Value: str
    RecordId: NotRequired[str]
    AttributeId: NotRequired[str]
    LockVersion: NotRequired[DataTableLockVersionTypeDef]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class RecordPrimaryValueTypeDef(TypedDict):
    RecordId: NotRequired[str]
    PrimaryValues: NotRequired[List[PrimaryValueResponseTypeDef]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class BatchGetFlowAssociationResponseTypeDef(TypedDict):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlowAssociationsResponseTypeDef(TypedDict):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchPutContactResponseTypeDef(TypedDict):
    SuccessfulRequestList: List[SuccessfulRequestTypeDef]
    FailedRequestList: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CaseSlaConfigurationOutputTypeDef = TypedDict(
    "CaseSlaConfigurationOutputTypeDef",
    {
        "Name": str,
        "Type": Literal["CaseField"],
        "TargetSlaMinutes": int,
        "FieldId": NotRequired[str],
        "TargetFieldValues": NotRequired[List[FieldValueUnionOutputTypeDef]],
    },
)

class FieldValueOutputTypeDef(TypedDict):
    Id: str
    Value: FieldValueUnionOutputTypeDef

class ChatMetricsTypeDef(TypedDict):
    ChatContactMetrics: NotRequired[ChatContactMetricsTypeDef]
    AgentMetrics: NotRequired[ParticipantMetricsTypeDef]
    CustomerMetrics: NotRequired[ParticipantMetricsTypeDef]

class StartContactStreamingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ChatStreamingConfiguration: ChatStreamingConfigurationTypeDef
    ClientToken: str

class ClaimedPhoneNumberSummaryTypeDef(TypedDict):
    PhoneNumberId: NotRequired[str]
    PhoneNumberArn: NotRequired[str]
    PhoneNumber: NotRequired[str]
    PhoneNumberCountryCode: NotRequired[PhoneNumberCountryCodeType]
    PhoneNumberType: NotRequired[PhoneNumberTypeType]
    PhoneNumberDescription: NotRequired[str]
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    PhoneNumberStatus: NotRequired[PhoneNumberStatusTypeDef]
    SourcePhoneNumberArn: NotRequired[str]

class ConditionTypeDef(TypedDict):
    StringCondition: NotRequired[StringConditionTypeDef]
    NumberCondition: NotRequired[NumberConditionTypeDef]

class CreatePushNotificationRegistrationRequestTypeDef(TypedDict):
    InstanceId: str
    PinpointAppArn: str
    DeviceToken: str
    DeviceType: DeviceTypeType
    ContactConfiguration: ContactConfigurationTypeDef
    ClientToken: NotRequired[str]

class UserDataFiltersTypeDef(TypedDict):
    Queues: NotRequired[Sequence[str]]
    ContactFilter: NotRequired[ContactFilterTypeDef]
    RoutingProfiles: NotRequired[Sequence[str]]
    Agents: NotRequired[Sequence[str]]
    UserHierarchyGroups: NotRequired[Sequence[str]]

class ContactFlowAttributeAndConditionTypeDef(TypedDict):
    TagConditions: NotRequired[Sequence[TagConditionTypeDef]]
    ContactFlowTypeCondition: NotRequired[ContactFlowTypeConditionTypeDef]

class DescribeContactFlowModuleAliasResponseTypeDef(TypedDict):
    ContactFlowModuleAlias: ContactFlowModuleAliasInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContactFlowModuleAliasesResponseTypeDef(TypedDict):
    ContactFlowModuleAliasSummaryList: List[ContactFlowModuleAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListContactFlowModulesResponseTypeDef(TypedDict):
    ContactFlowModulesSummaryList: List[ContactFlowModuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ContactFlowModuleTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Content: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[ContactFlowModuleStateType]
    Status: NotRequired[ContactFlowModuleStatusType]
    Tags: NotRequired[Dict[str, str]]
    FlowModuleContentSha256: NotRequired[str]
    Version: NotRequired[int]
    VersionDescription: NotRequired[str]
    Settings: NotRequired[str]
    ExternalInvocationConfiguration: NotRequired[ExternalInvocationConfigurationTypeDef]

class CreateContactFlowModuleRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Content: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]
    Settings: NotRequired[str]
    ExternalInvocationConfiguration: NotRequired[ExternalInvocationConfigurationTypeDef]

class ListContactFlowModuleVersionsResponseTypeDef(TypedDict):
    ContactFlowModuleVersionSummaryList: List[ContactFlowModuleVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListContactFlowsResponseTypeDef(TypedDict):
    ContactFlowSummaryList: List[ContactFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeContactFlowResponseTypeDef(TypedDict):
    ContactFlow: ContactFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowsResponseTypeDef(TypedDict):
    ContactFlows: List[ContactFlowTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListContactFlowVersionsResponseTypeDef(TypedDict):
    ContactFlowVersionSummaryList: List[ContactFlowVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetContactMetricsRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    Metrics: Sequence[ContactMetricInfoTypeDef]

class ContactMetricResultTypeDef(TypedDict):
    Name: Literal["POSITION_IN_QUEUE"]
    Value: ContactMetricValueTypeDef

class ContactSearchSummarySegmentAttributeValuePaginatorTypeDef(TypedDict):
    ValueString: NotRequired[str]
    ValueMap: NotRequired[Dict[str, SegmentAttributeValuePaginatorTypeDef]]

class ContactSearchSummarySegmentAttributeValueTypeDef(TypedDict):
    ValueString: NotRequired[str]
    ValueMap: NotRequired[Dict[str, SegmentAttributeValueOutputTypeDef]]

class CreateContactFlowVersionRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    Description: NotRequired[str]
    FlowContentSha256: NotRequired[str]
    ContactFlowVersion: NotRequired[int]
    LastModifiedTime: NotRequired[TimestampTypeDef]
    LastModifiedRegion: NotRequired[str]

class DataTableValueTypeDef(TypedDict):
    AttributeName: str
    Value: str
    PrimaryValues: NotRequired[Sequence[PrimaryValueTypeDef]]
    LockVersion: NotRequired[DataTableLockVersionTypeDef]
    LastModifiedTime: NotRequired[TimestampTypeDef]
    LastModifiedRegion: NotRequired[str]

SearchContactsTimeRangeTypeDef = TypedDict(
    "SearchContactsTimeRangeTypeDef",
    {
        "Type": SearchContactsTimeRangeTypeType,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)

class UpdateContactScheduleRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ScheduledTime: TimestampTypeDef

class TaskActionDefinitionOutputTypeDef(TypedDict):
    Name: str
    ContactFlowId: str
    Description: NotRequired[str]
    References: NotRequired[Dict[str, ReferenceTypeDef]]

class TaskActionDefinitionTypeDef(TypedDict):
    Name: str
    ContactFlowId: str
    Description: NotRequired[str]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]

class CreateParticipantResponseTypeDef(TypedDict):
    ParticipantCredentials: ParticipantTokenCredentialsTypeDef
    ParticipantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQueueOutboundCallerConfigRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfigTypeDef

class CreateQueueRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: NotRequired[str]
    OutboundCallerConfig: NotRequired[OutboundCallerConfigTypeDef]
    OutboundEmailConfig: NotRequired[OutboundEmailConfigTypeDef]
    MaxContacts: NotRequired[int]
    QuickConnectIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class QueueTypeDef(TypedDict):
    Name: NotRequired[str]
    QueueArn: NotRequired[str]
    QueueId: NotRequired[str]
    Description: NotRequired[str]
    OutboundCallerConfig: NotRequired[OutboundCallerConfigTypeDef]
    OutboundEmailConfig: NotRequired[OutboundEmailConfigTypeDef]
    HoursOfOperationId: NotRequired[str]
    MaxContacts: NotRequired[int]
    Status: NotRequired[QueueStatusType]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class UpdateQueueOutboundEmailConfigRequestTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    OutboundEmailConfig: OutboundEmailConfigTypeDef

class ListSecurityProfileFlowModulesResponseTypeDef(TypedDict):
    AllowedFlowModules: List[FlowModuleTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateUserIdentityInfoRequestTypeDef(TypedDict):
    IdentityInfo: UserIdentityInfoTypeDef
    UserId: str
    InstanceId: str

class CreateUserRequestTypeDef(TypedDict):
    Username: str
    PhoneConfig: UserPhoneConfigTypeDef
    SecurityProfileIds: Sequence[str]
    RoutingProfileId: str
    InstanceId: str
    Password: NotRequired[str]
    IdentityInfo: NotRequired[UserIdentityInfoTypeDef]
    DirectoryUserId: NotRequired[str]
    HierarchyGroupId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateUserPhoneConfigRequestTypeDef(TypedDict):
    PhoneConfig: UserPhoneConfigTypeDef
    UserId: str
    InstanceId: str

class UserTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Username: NotRequired[str]
    IdentityInfo: NotRequired[UserIdentityInfoTypeDef]
    PhoneConfig: NotRequired[UserPhoneConfigTypeDef]
    DirectoryUserId: NotRequired[str]
    SecurityProfileIds: NotRequired[List[str]]
    RoutingProfileId: NotRequired[str]
    HierarchyGroupId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class CreateViewRequestTypeDef(TypedDict):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef
    Name: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateViewContentRequestTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef

class GetFederationTokenResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    SignInUrl: str
    UserArn: str
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MediaConcurrencyTypeDef(TypedDict):
    Channel: ChannelType
    Concurrency: int
    CrossChannelBehavior: NotRequired[CrossChannelBehaviorTypeDef]

class CurrentMetricDataTypeDef(TypedDict):
    Metric: NotRequired[CurrentMetricTypeDef]
    Value: NotRequired[float]

class ListDataTablesResponseTypeDef(TypedDict):
    DataTableSummaryList: List[DataTableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    DateCondition: NotRequired[DateConditionTypeDef]

class HoursOfOperationOverrideSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    DateCondition: NotRequired[DateConditionTypeDef]

class EvaluationFormSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    NumberCondition: NotRequired[NumberConditionTypeDef]
    BooleanCondition: NotRequired[BooleanConditionTypeDef]
    DateTimeCondition: NotRequired[DateTimeConditionTypeDef]

class EvaluationSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    NumberCondition: NotRequired[NumberConditionTypeDef]
    BooleanCondition: NotRequired[BooleanConditionTypeDef]
    DateTimeCondition: NotRequired[DateTimeConditionTypeDef]
    DecimalCondition: NotRequired[DecimalConditionTypeDef]

class ListDefaultVocabulariesResponseTypeDef(TypedDict):
    DefaultVocabularyList: List[DefaultVocabularyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribePromptResponseTypeDef(TypedDict):
    Prompt: PromptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPromptsResponseTypeDef(TypedDict):
    Prompts: List[PromptTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeTrafficDistributionGroupResponseTypeDef(TypedDict):
    TrafficDistributionGroup: TrafficDistributionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVocabularyResponseTypeDef(TypedDict):
    Vocabulary: VocabularyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DimensionsTypeDef(TypedDict):
    Queue: NotRequired[QueueReferenceTypeDef]
    Channel: NotRequired[ChannelType]
    RoutingProfile: NotRequired[RoutingProfileReferenceTypeDef]
    RoutingStepExpression: NotRequired[str]
    AgentStatus: NotRequired[AgentStatusIdentifierTypeDef]
    Subtype: NotRequired[str]
    ValidationTestType: NotRequired[str]

class DisassociateRoutingProfileQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: NotRequired[Sequence[RoutingProfileQueueReferenceTypeDef]]
    ManualAssignmentQueueReferences: NotRequired[Sequence[RoutingProfileQueueReferenceTypeDef]]

class RoutingProfileManualAssignmentQueueConfigTypeDef(TypedDict):
    QueueReference: RoutingProfileQueueReferenceTypeDef

class RoutingProfileQueueConfigTypeDef(TypedDict):
    QueueReference: RoutingProfileQueueReferenceTypeDef
    Priority: int
    Delay: int

class DisassociateUserProficienciesRequestTypeDef(TypedDict):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyDisassociateTypeDef]

class StopContactRequestTypeDef(TypedDict):
    ContactId: str
    InstanceId: str
    DisconnectReason: NotRequired[DisconnectReasonTypeDef]

class GetAttachedFileResponseTypeDef(TypedDict):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    FileName: str
    FileSizeInBytes: int
    AssociatedResourceArn: str
    FileUseCaseType: FileUseCaseTypeType
    CreatedBy: CreatedByInfoTypeDef
    DownloadUrlMetadata: DownloadUrlMetadataTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class InboundAdditionalRecipientsTypeDef(TypedDict):
    ToAddresses: NotRequired[Sequence[EmailAddressInfoTypeDef]]
    CcAddresses: NotRequired[Sequence[EmailAddressInfoTypeDef]]

class OutboundAdditionalRecipientsTypeDef(TypedDict):
    CcEmailAddresses: NotRequired[Sequence[EmailAddressInfoTypeDef]]

class KinesisVideoStreamConfigTypeDef(TypedDict):
    Prefix: str
    RetentionPeriodHours: int
    EncryptionConfig: EncryptionConfigTypeDef

class S3ConfigTypeDef(TypedDict):
    BucketName: str
    BucketPrefix: str
    EncryptionConfig: NotRequired[EncryptionConfigTypeDef]

EvaluationAnswerDataUnionTypeDef = Union[
    EvaluationAnswerDataTypeDef, EvaluationAnswerDataOutputTypeDef
]

class EvaluationFormItemEnablementExpressionOutputTypeDef(TypedDict):
    Source: EvaluationFormItemEnablementSourceTypeDef
    Values: List[EvaluationFormItemEnablementSourceValueTypeDef]
    Comparator: EvaluationFormItemSourceValuesComparatorType

class EvaluationFormItemEnablementExpressionTypeDef(TypedDict):
    Source: EvaluationFormItemEnablementSourceTypeDef
    Values: Sequence[EvaluationFormItemEnablementSourceValueTypeDef]
    Comparator: EvaluationFormItemSourceValuesComparatorType

class EvaluationFormMultiSelectQuestionAutomationOptionOutputTypeDef(TypedDict):
    RuleCategory: NotRequired[MultiSelectQuestionRuleCategoryAutomationOutputTypeDef]

class EvaluationFormTextQuestionAutomationTypeDef(TypedDict):
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class EvaluationFormNumericQuestionAutomationTypeDef(TypedDict):
    PropertyValue: NotRequired[NumericQuestionPropertyValueAutomationTypeDef]
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class SearchEvaluationFormsResponseTypeDef(TypedDict):
    EvaluationFormSearchSummaryList: List[EvaluationFormSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

EvaluationFormSectionUnionTypeDef = Union[
    EvaluationFormSectionTypeDef, EvaluationFormSectionOutputTypeDef
]

class EvaluationFormSingleSelectQuestionAutomationOptionTypeDef(TypedDict):
    RuleCategory: NotRequired[SingleSelectQuestionRuleCategoryAutomationTypeDef]

class ListEvaluationFormsResponseTypeDef(TypedDict):
    EvaluationFormSummaryList: List[EvaluationFormSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEvaluationFormVersionsResponseTypeDef(TypedDict):
    EvaluationFormVersionSummaryList: List[EvaluationFormVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EvaluationMetadataTypeDef(TypedDict):
    ContactId: str
    EvaluatorArn: str
    ContactAgentId: NotRequired[str]
    CalibrationSessionId: NotRequired[str]
    Score: NotRequired[EvaluationScoreTypeDef]
    AutoEvaluation: NotRequired[AutoEvaluationDetailsTypeDef]
    Acknowledgement: NotRequired[EvaluationAcknowledgementTypeDef]
    ContactParticipant: NotRequired[EvaluationContactParticipantTypeDef]
    SamplingJobId: NotRequired[str]

class EvaluationSummaryTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    EvaluationFormTitle: str
    EvaluationFormId: str
    Status: EvaluationStatusType
    EvaluatorArn: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    CalibrationSessionId: NotRequired[str]
    AutoEvaluationEnabled: NotRequired[bool]
    AutoEvaluationStatus: NotRequired[AutoEvaluationStatusType]
    Score: NotRequired[EvaluationScoreTypeDef]
    Acknowledgement: NotRequired[EvaluationAcknowledgementSummaryTypeDef]
    EvaluationType: NotRequired[EvaluationTypeType]
    ContactParticipant: NotRequired[EvaluationContactParticipantTypeDef]

class EvaluationSearchSummaryTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    EvaluationFormVersion: int
    Metadata: EvaluationSearchMetadataTypeDef
    Status: EvaluationStatusType
    CreatedTime: datetime
    LastModifiedTime: datetime
    EvaluationFormId: NotRequired[str]
    EvaluationFormTitle: NotRequired[str]
    EvaluationType: NotRequired[EvaluationTypeType]
    Tags: NotRequired[Dict[str, str]]

class EvaluationTranscriptPointOfInterestTypeDef(TypedDict):
    MillisecondOffsets: NotRequired[EvaluationSuggestedAnswerTranscriptMillisecondOffsetsTypeDef]
    TranscriptSegment: NotRequired[str]

FieldValueUnionUnionTypeDef = Union[FieldValueUnionTypeDef, FieldValueUnionOutputTypeDef]

class FilterV2TypeDef(TypedDict):
    FilterKey: NotRequired[str]
    FilterValues: NotRequired[Sequence[str]]
    StringCondition: NotRequired[FilterV2StringConditionTypeDef]

class GetCurrentMetricDataRequestTypeDef(TypedDict):
    InstanceId: str
    Filters: FiltersTypeDef
    CurrentMetrics: Sequence[CurrentMetricTypeDef]
    Groupings: NotRequired[Sequence[GroupingType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SortCriteria: NotRequired[Sequence[CurrentMetricSortCriteriaTypeDef]]

class WorkspaceThemeTypographyTypeDef(TypedDict):
    FontFamily: NotRequired[FontFamilyTypeDef]

class ListAgentStatusRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    AgentStatusTypes: NotRequired[Sequence[AgentStatusTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApprovedOriginsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAuthenticationProfilesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBotsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    LexVersion: LexVersionType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactEvaluationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactFlowModuleAliasesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactFlowModuleVersionsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactFlowModulesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactFlowModuleState: NotRequired[ContactFlowModuleStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactFlowVersionsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactFlowsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactFlowTypes: NotRequired[Sequence[ContactFlowTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactReferencesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataTableAttributesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    AttributeIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataTablesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDefaultVocabulariesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    LanguageCode: NotRequired[VocabularyLanguageCodeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEvaluationFormVersionsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEvaluationFormsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFlowAssociationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ResourceType: NotRequired[ListFlowAssociationResourceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHoursOfOperationOverridesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHoursOfOperationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstanceAttributesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstanceStorageConfigsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstancesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIntegrationAssociationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    IntegrationType: NotRequired[IntegrationTypeType]
    IntegrationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLambdaFunctionsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLexBotsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPhoneNumbersRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PhoneNumberTypes: NotRequired[Sequence[PhoneNumberTypeType]]
    PhoneNumberCountryCodes: NotRequired[Sequence[PhoneNumberCountryCodeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPhoneNumbersV2RequestPaginateTypeDef(TypedDict):
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    PhoneNumberCountryCodes: NotRequired[Sequence[PhoneNumberCountryCodeType]]
    PhoneNumberTypes: NotRequired[Sequence[PhoneNumberTypeType]]
    PhoneNumberPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPredefinedAttributesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPromptsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueueQuickConnectsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    QueueId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    QueueTypes: NotRequired[Sequence[QueueTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQuickConnectsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    QuickConnectTypes: NotRequired[Sequence[QuickConnectTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoutingProfileManualAssignmentQueuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoutingProfileQueuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoutingProfilesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PublishStatus: NotRequired[RulePublishStatusType]
    EventSourceName: NotRequired[EventSourceNameType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityKeysRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityProfileApplicationsRequestPaginateTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityProfilePermissionsRequestPaginateTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityProfilesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaskTemplatesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    Status: NotRequired[TaskTemplateStatusType]
    Name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrafficDistributionGroupUsersRequestPaginateTypeDef(TypedDict):
    TrafficDistributionGroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTrafficDistributionGroupsRequestPaginateTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUseCasesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    IntegrationAssociationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUserHierarchyGroupsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUserProficienciesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    UserId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListViewVersionsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ViewId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListViewsRequestPaginateTypeDef = TypedDict(
    "ListViewsRequestPaginateTypeDef",
    {
        "InstanceId": str,
        "Type": NotRequired[ViewTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListWorkspacePagesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspacesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchAvailablePhoneNumbersRequestPaginateTypeDef(TypedDict):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: NotRequired[str]
    InstanceId: NotRequired[str]
    PhoneNumberPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchVocabulariesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    State: NotRequired[VocabularyStateType]
    NameStartsWith: NotRequired[str]
    LanguageCode: NotRequired[VocabularyLanguageCodeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class HierarchyPathReferenceTypeDef(TypedDict):
    LevelOne: NotRequired[HierarchyGroupSummaryReferenceTypeDef]
    LevelTwo: NotRequired[HierarchyGroupSummaryReferenceTypeDef]
    LevelThree: NotRequired[HierarchyGroupSummaryReferenceTypeDef]
    LevelFour: NotRequired[HierarchyGroupSummaryReferenceTypeDef]
    LevelFive: NotRequired[HierarchyGroupSummaryReferenceTypeDef]

class HierarchyPathTypeDef(TypedDict):
    LevelOne: NotRequired[HierarchyGroupSummaryTypeDef]
    LevelTwo: NotRequired[HierarchyGroupSummaryTypeDef]
    LevelThree: NotRequired[HierarchyGroupSummaryTypeDef]
    LevelFour: NotRequired[HierarchyGroupSummaryTypeDef]
    LevelFive: NotRequired[HierarchyGroupSummaryTypeDef]

class ListUserHierarchyGroupsResponseTypeDef(TypedDict):
    UserHierarchyGroupSummaryList: List[HierarchyGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class HierarchyStructureTypeDef(TypedDict):
    LevelOne: NotRequired[HierarchyLevelTypeDef]
    LevelTwo: NotRequired[HierarchyLevelTypeDef]
    LevelThree: NotRequired[HierarchyLevelTypeDef]
    LevelFour: NotRequired[HierarchyLevelTypeDef]
    LevelFive: NotRequired[HierarchyLevelTypeDef]

class HierarchyStructureUpdateTypeDef(TypedDict):
    LevelOne: NotRequired[HierarchyLevelUpdateTypeDef]
    LevelTwo: NotRequired[HierarchyLevelUpdateTypeDef]
    LevelThree: NotRequired[HierarchyLevelUpdateTypeDef]
    LevelFour: NotRequired[HierarchyLevelUpdateTypeDef]
    LevelFive: NotRequired[HierarchyLevelUpdateTypeDef]

class HistoricalMetricTypeDef(TypedDict):
    Name: NotRequired[HistoricalMetricNameType]
    Threshold: NotRequired[ThresholdTypeDef]
    Statistic: NotRequired[StatisticType]
    Unit: NotRequired[UnitType]

class HoursOfOperationConfigTypeDef(TypedDict):
    Day: HoursOfOperationDaysType
    StartTime: HoursOfOperationTimeSliceTypeDef
    EndTime: HoursOfOperationTimeSliceTypeDef

class HoursOfOperationOverrideConfigTypeDef(TypedDict):
    Day: NotRequired[OverrideDaysType]
    StartTime: NotRequired[OverrideTimeSliceTypeDef]
    EndTime: NotRequired[OverrideTimeSliceTypeDef]

class OperationalHourTypeDef(TypedDict):
    Start: NotRequired[OverrideTimeSliceTypeDef]
    End: NotRequired[OverrideTimeSliceTypeDef]

class ListHoursOfOperationsResponseTypeDef(TypedDict):
    HoursOfOperationSummaryList: List[HoursOfOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class WorkspaceThemeImagesTypeDef(TypedDict):
    Logo: NotRequired[ImagesLogoTypeDef]

class InboundEmailContentTypeDef(TypedDict):
    MessageSourceType: Literal["RAW"]
    RawMessage: NotRequired[InboundRawMessageTypeDef]

class InstanceTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    IdentityManagementType: NotRequired[DirectoryTypeType]
    InstanceAlias: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    ServiceRole: NotRequired[str]
    InstanceStatus: NotRequired[InstanceStatusType]
    StatusReason: NotRequired[InstanceStatusReasonTypeDef]
    InboundCallsEnabled: NotRequired[bool]
    OutboundCallsEnabled: NotRequired[bool]
    InstanceAccessUrl: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ListInstancesResponseTypeDef(TypedDict):
    InstanceSummaryList: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIntegrationAssociationsResponseTypeDef(TypedDict):
    IntegrationAssociationSummaryList: List[IntegrationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InvisibleFieldInfoTypeDef(TypedDict):
    Id: NotRequired[TaskTemplateFieldIdentifierTypeDef]

class ReadOnlyFieldInfoTypeDef(TypedDict):
    Id: NotRequired[TaskTemplateFieldIdentifierTypeDef]

class RequiredFieldInfoTypeDef(TypedDict):
    Id: NotRequired[TaskTemplateFieldIdentifierTypeDef]

class TaskTemplateDefaultFieldValueTypeDef(TypedDict):
    Id: NotRequired[TaskTemplateFieldIdentifierTypeDef]
    DefaultValue: NotRequired[str]

TaskTemplateFieldOutputTypeDef = TypedDict(
    "TaskTemplateFieldOutputTypeDef",
    {
        "Id": TaskTemplateFieldIdentifierTypeDef,
        "Description": NotRequired[str],
        "Type": NotRequired[TaskTemplateFieldTypeType],
        "SingleSelectOptions": NotRequired[List[str]],
    },
)
TaskTemplateFieldTypeDef = TypedDict(
    "TaskTemplateFieldTypeDef",
    {
        "Id": TaskTemplateFieldIdentifierTypeDef,
        "Description": NotRequired[str],
        "Type": NotRequired[TaskTemplateFieldTypeType],
        "SingleSelectOptions": NotRequired[Sequence[str]],
    },
)

class ListDataTablePrimaryValuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    RecordIds: NotRequired[Sequence[str]]
    PrimaryAttributeValues: NotRequired[Sequence[PrimaryAttributeValueFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataTablePrimaryValuesRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    RecordIds: NotRequired[Sequence[str]]
    PrimaryAttributeValues: NotRequired[Sequence[PrimaryAttributeValueFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataTableValuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    RecordIds: NotRequired[Sequence[str]]
    PrimaryAttributeValues: NotRequired[Sequence[PrimaryAttributeValueFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataTableValuesRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    RecordIds: NotRequired[Sequence[str]]
    PrimaryAttributeValues: NotRequired[Sequence[PrimaryAttributeValueFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPhoneNumbersResponseTypeDef(TypedDict):
    PhoneNumberSummaryList: List[PhoneNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPhoneNumbersV2ResponseTypeDef(TypedDict):
    ListPhoneNumbersSummaryList: List[ListPhoneNumbersSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPredefinedAttributesResponseTypeDef(TypedDict):
    PredefinedAttributeSummaryList: List[PredefinedAttributeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPromptsResponseTypeDef(TypedDict):
    PromptSummaryList: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQueueQuickConnectsResponseTypeDef(TypedDict):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQuickConnectsResponseTypeDef(TypedDict):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQueuesResponseTypeDef(TypedDict):
    QueueSummaryList: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRoutingProfileManualAssignmentQueuesResponseTypeDef(TypedDict):
    RoutingProfileManualAssignmentQueueConfigSummaryList: List[
        RoutingProfileManualAssignmentQueueConfigSummaryTypeDef
    ]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRoutingProfileQueuesResponseTypeDef(TypedDict):
    RoutingProfileQueueConfigSummaryList: List[RoutingProfileQueueConfigSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRoutingProfilesResponseTypeDef(TypedDict):
    RoutingProfileSummaryList: List[RoutingProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSecurityKeysResponseTypeDef(TypedDict):
    SecurityKeys: List[SecurityKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSecurityProfilesResponseTypeDef(TypedDict):
    SecurityProfileSummaryList: List[SecurityProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTaskTemplatesResponseTypeDef(TypedDict):
    TaskTemplates: List[TaskTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTrafficDistributionGroupUsersResponseTypeDef(TypedDict):
    TrafficDistributionGroupUserSummaryList: List[TrafficDistributionGroupUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTrafficDistributionGroupsResponseTypeDef(TypedDict):
    TrafficDistributionGroupSummaryList: List[TrafficDistributionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUseCasesResponseTypeDef(TypedDict):
    UseCaseSummaryList: List[UseCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsersResponseTypeDef(TypedDict):
    UserSummaryList: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListViewVersionsResponseTypeDef(TypedDict):
    ViewVersionSummaryList: List[ViewVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListViewsResponseTypeDef(TypedDict):
    ViewsSummaryList: List[ViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkspaceMediaResponseTypeDef(TypedDict):
    Media: List[MediaItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspacePagesResponseTypeDef(TypedDict):
    WorkspacePageList: List[WorkspacePageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkspacesResponseTypeDef(TypedDict):
    WorkspaceSummaryList: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MetricFilterV2UnionTypeDef = Union[MetricFilterV2TypeDef, MetricFilterV2OutputTypeDef]

class MetricV2OutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Threshold: NotRequired[List[ThresholdV2TypeDef]]
    MetricId: NotRequired[str]
    MetricFilters: NotRequired[List[MetricFilterV2OutputTypeDef]]

MultiSelectQuestionRuleCategoryAutomationUnionTypeDef = Union[
    MultiSelectQuestionRuleCategoryAutomationTypeDef,
    MultiSelectQuestionRuleCategoryAutomationOutputTypeDef,
]

class NewSessionDetailsTypeDef(TypedDict):
    SupportedMessagingContentTypes: NotRequired[Sequence[str]]
    ParticipantDetails: NotRequired[ParticipantDetailsTypeDef]
    Attributes: NotRequired[Mapping[str, str]]
    StreamingConfiguration: NotRequired[ChatStreamingConfigurationTypeDef]

class NextContactMetadataTypeDef(TypedDict):
    QuickConnectContactData: NotRequired[QuickConnectContactDataTypeDef]

class SendNotificationActionDefinitionOutputTypeDef(TypedDict):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeOutputTypeDef
    Subject: NotRequired[str]
    Exclusion: NotRequired[NotificationRecipientTypeOutputTypeDef]

NotificationRecipientTypeUnionTypeDef = Union[
    NotificationRecipientTypeTypeDef, NotificationRecipientTypeOutputTypeDef
]

class WorkspaceThemePaletteTypeDef(TypedDict):
    Header: NotRequired[PaletteHeaderTypeDef]
    Navigation: NotRequired[PaletteNavigationTypeDef]
    Canvas: NotRequired[PaletteCanvasTypeDef]
    Primary: NotRequired[PalettePrimaryTypeDef]

class ParticipantTimerConfigurationTypeDef(TypedDict):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValueTypeDef

class PreviewOutputTypeDef(TypedDict):
    PostAcceptTimeoutConfig: PostAcceptTimeoutConfigTypeDef
    AllowedUserActions: List[AllowedUserActionType]

class PreviewTypeDef(TypedDict):
    PostAcceptTimeoutConfig: PostAcceptTimeoutConfigTypeDef
    AllowedUserActions: Sequence[AllowedUserActionType]

class PredefinedAttributeTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[PredefinedAttributeValuesOutputTypeDef]
    Purposes: NotRequired[List[str]]
    AttributeConfiguration: NotRequired[PredefinedAttributeConfigurationTypeDef]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

PredefinedAttributeValuesUnionTypeDef = Union[
    PredefinedAttributeValuesTypeDef, PredefinedAttributeValuesOutputTypeDef
]

class PrimaryAttributeAccessControlConfigurationItemOutputTypeDef(TypedDict):
    PrimaryAttributeValues: NotRequired[List[PrimaryAttributeValueOutputTypeDef]]

class PrimaryAttributeAccessControlConfigurationItemTypeDef(TypedDict):
    PrimaryAttributeValues: NotRequired[Sequence[PrimaryAttributeValueTypeDef]]

class QuickConnectConfigTypeDef(TypedDict):
    QuickConnectType: QuickConnectTypeType
    UserConfig: NotRequired[UserQuickConnectConfigTypeDef]
    QueueConfig: NotRequired[QueueQuickConnectConfigTypeDef]
    PhoneConfig: NotRequired[PhoneNumberQuickConnectConfigTypeDef]
    FlowConfig: NotRequired[FlowQuickConnectConfigTypeDef]

class RealTimeContactAnalysisTranscriptItemRedactionTypeDef(TypedDict):
    CharacterOffsets: NotRequired[List[RealTimeContactAnalysisCharacterIntervalTypeDef]]

class RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef(TypedDict):
    Id: str
    CharacterOffsets: NotRequired[RealTimeContactAnalysisCharacterIntervalTypeDef]

class RealTimeContactAnalysisTranscriptItemWithContentTypeDef(TypedDict):
    Id: str
    Content: NotRequired[str]
    CharacterOffsets: NotRequired[RealTimeContactAnalysisCharacterIntervalTypeDef]

class RealTimeContactAnalysisSegmentAttachmentsTypeDef(TypedDict):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Attachments: List[RealTimeContactAnalysisAttachmentTypeDef]
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: NotRequired[str]

class RealTimeContactAnalysisSegmentEventTypeDef(TypedDict):
    Id: str
    EventType: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    ParticipantId: NotRequired[str]
    ParticipantRole: NotRequired[ParticipantRoleType]
    DisplayName: NotRequired[str]

class ReferenceSummaryTypeDef(TypedDict):
    Url: NotRequired[UrlReferenceTypeDef]
    Attachment: NotRequired[AttachmentReferenceTypeDef]
    EmailMessage: NotRequired[EmailMessageReferenceTypeDef]
    EmailMessagePlainText: NotRequired[EmailMessageReferenceTypeDef]
    String: NotRequired[StringReferenceTypeDef]
    Number: NotRequired[NumberReferenceTypeDef]
    Date: NotRequired[DateReferenceTypeDef]
    Email: NotRequired[EmailReferenceTypeDef]

class ReplicationConfigurationTypeDef(TypedDict):
    ReplicationStatusSummaryList: NotRequired[List[ReplicationStatusSummaryTypeDef]]
    SourceRegion: NotRequired[str]
    GlobalSignInEndpoint: NotRequired[str]

class ResourceTagsSearchCriteriaTypeDef(TypedDict):
    TagSearchCondition: NotRequired[TagSearchConditionTypeDef]

class SearchResourceTagsResponseTypeDef(TypedDict):
    Tags: List[TagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchSecurityProfilesResponseTypeDef(TypedDict):
    SecurityProfiles: List[SecurityProfileSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchVocabulariesResponseTypeDef(TypedDict):
    VocabularySummaryList: List[VocabularySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchWorkspaceAssociationsResponseTypeDef(TypedDict):
    WorkspaceAssociations: List[WorkspaceAssociationSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchWorkspacesResponseTypeDef(TypedDict):
    Workspaces: List[WorkspaceSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchableRoutingCriteriaStepTypeDef(TypedDict):
    AgentCriteria: NotRequired[SearchableAgentCriteriaStepTypeDef]

class SearchableContactAttributesTypeDef(TypedDict):
    Criteria: Sequence[SearchableContactAttributesCriteriaTypeDef]
    MatchType: NotRequired[SearchContactsMatchTypeType]

class SearchableSegmentAttributesTypeDef(TypedDict):
    Criteria: Sequence[SearchableSegmentAttributesCriteriaTypeDef]
    MatchType: NotRequired[SearchContactsMatchTypeType]

SegmentAttributeValueUnionTypeDef = Union[
    SegmentAttributeValueTypeDef, SegmentAttributeValueOutputTypeDef
]

class SignInConfigOutputTypeDef(TypedDict):
    Distributions: List[SignInDistributionTypeDef]

class SignInConfigTypeDef(TypedDict):
    Distributions: Sequence[SignInDistributionTypeDef]

class StartAttachedFileUploadResponseTypeDef(TypedDict):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    CreatedBy: CreatedByInfoTypeDef
    UploadUrlMetadata: UploadUrlMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactRecordingRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef

class TemplatedMessageConfigTypeDef(TypedDict):
    KnowledgeBaseId: str
    MessageTemplateId: str
    TemplateAttributes: TemplateAttributesTypeDef

class TranscriptTypeDef(TypedDict):
    Criteria: Sequence[TranscriptCriteriaTypeDef]
    MatchType: NotRequired[SearchContactsMatchTypeType]

class UserSearchSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    DirectoryUserId: NotRequired[str]
    HierarchyGroupId: NotRequired[str]
    Id: NotRequired[str]
    IdentityInfo: NotRequired[UserIdentityInfoLiteTypeDef]
    PhoneConfig: NotRequired[UserPhoneConfigTypeDef]
    RoutingProfileId: NotRequired[str]
    SecurityProfileIds: NotRequired[List[str]]
    Tags: NotRequired[Dict[str, str]]
    Username: NotRequired[str]

class ValidationOutputTypeDef(TypedDict):
    MinLength: NotRequired[int]
    MaxLength: NotRequired[int]
    MinValues: NotRequired[int]
    MaxValues: NotRequired[int]
    IgnoreCase: NotRequired[bool]
    Minimum: NotRequired[float]
    Maximum: NotRequired[float]
    ExclusiveMinimum: NotRequired[float]
    ExclusiveMaximum: NotRequired[float]
    MultipleOf: NotRequired[float]
    Enum: NotRequired[ValidationEnumOutputTypeDef]

class ValidationTypeDef(TypedDict):
    MinLength: NotRequired[int]
    MaxLength: NotRequired[int]
    MinValues: NotRequired[int]
    MaxValues: NotRequired[int]
    IgnoreCase: NotRequired[bool]
    Minimum: NotRequired[float]
    Maximum: NotRequired[float]
    ExclusiveMinimum: NotRequired[float]
    ExclusiveMaximum: NotRequired[float]
    MultipleOf: NotRequired[float]
    Enum: NotRequired[ValidationEnumTypeDef]

ViewTypeDef = TypedDict(
    "ViewTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ViewStatusType],
        "Type": NotRequired[ViewTypeType],
        "Description": NotRequired[str],
        "Version": NotRequired[int],
        "VersionDescription": NotRequired[str],
        "Content": NotRequired[ViewContentTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "ViewContentSha256": NotRequired[str],
    },
)

class ListRulesResponseTypeDef(TypedDict):
    RuleSummaryList: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

AgentConfigUnionTypeDef = Union[AgentConfigTypeDef, AgentConfigOutputTypeDef]
TelephonyConfigUnionTypeDef = Union[TelephonyConfigTypeDef, TelephonyConfigOutputTypeDef]

class AgentInfoTypeDef(TypedDict):
    Id: NotRequired[str]
    AcceptedByAgentTimestamp: NotRequired[datetime]
    PreviewEndTimestamp: NotRequired[datetime]
    ConnectedToAgentTimestamp: NotRequired[datetime]
    AgentPauseDurationInSeconds: NotRequired[int]
    HierarchyGroups: NotRequired[HierarchyGroupsTypeDef]
    DeviceInfo: NotRequired[DeviceInfoTypeDef]
    Capabilities: NotRequired[ParticipantCapabilitiesTypeDef]
    AfterContactWorkDuration: NotRequired[int]
    AfterContactWorkStartTimestamp: NotRequired[datetime]
    AfterContactWorkEndTimestamp: NotRequired[datetime]
    AgentInitiatedHoldDuration: NotRequired[int]
    StateTransitions: NotRequired[List[StateTransitionTypeDef]]

class StartWebRTCContactRequestTypeDef(TypedDict):
    ContactFlowId: str
    InstanceId: str
    ParticipantDetails: ParticipantDetailsTypeDef
    Attributes: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]
    AllowedCapabilities: NotRequired[AllowedCapabilitiesTypeDef]
    RelatedContactId: NotRequired[str]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    Description: NotRequired[str]

class CreateParticipantRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAddTypeDef
    ClientToken: NotRequired[str]

class QualityMetricsTypeDef(TypedDict):
    Agent: NotRequired[AgentQualityMetricsTypeDef]
    Customer: NotRequired[CustomerQualityMetricsTypeDef]

class SearchPredefinedAttributesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchCriteria: NotRequired[PredefinedAttributeSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchPredefinedAttributesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchCriteria: NotRequired[PredefinedAttributeSearchCriteriaTypeDef]

class AttributeConditionOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]
    ProficiencyLevel: NotRequired[float]
    Range: NotRequired[RangeTypeDef]
    MatchCriteria: NotRequired[MatchCriteriaOutputTypeDef]
    ComparisonOperator: NotRequired[str]

class MatchCriteriaTypeDef(TypedDict):
    AgentsCriteria: NotRequired[AgentsCriteriaUnionTypeDef]

class SearchEmailAddressesResponseTypeDef(TypedDict):
    EmailAddresses: List[EmailAddressMetadataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBotsResponseTypeDef(TypedDict):
    LexBots: List[LexBotConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetAttachedFileMetadataResponseTypeDef(TypedDict):
    Files: List[AttachedFileTypeDef]
    Errors: List[AttachedFileErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ControlPlaneUserAttributeFilterTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[AttributeAndConditionTypeDef]]
    AndCondition: NotRequired[AttributeAndConditionTypeDef]
    TagCondition: NotRequired[TagConditionTypeDef]
    HierarchyGroupCondition: NotRequired[HierarchyGroupConditionTypeDef]

class ControlPlaneAttributeFilterTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[CommonAttributeAndConditionTypeDef]]
    AndCondition: NotRequired[CommonAttributeAndConditionTypeDef]
    TagCondition: NotRequired[TagConditionTypeDef]

class ContactFlowModuleSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class EmailAddressSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class HoursOfOperationSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class PromptSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class QueueSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class QuickConnectSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class RoutingProfileSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class SecurityProfilesSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]

class MeetingTypeDef(TypedDict):
    MediaRegion: NotRequired[str]
    MediaPlacement: NotRequired[MediaPlacementTypeDef]
    MeetingFeatures: NotRequired[MeetingFeaturesConfigurationTypeDef]
    MeetingId: NotRequired[str]

class EvaluateDataTableValuesResponseTypeDef(TypedDict):
    Values: List[DataTableEvaluatedValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EvaluateDataTableValuesRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Values: Sequence[DataTableValueEvaluationSetTypeDef]
    TimeZone: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchDescribeDataTableValueRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Values: Sequence[DataTableValueIdentifierTypeDef]

class BatchCreateDataTableValueResponseTypeDef(TypedDict):
    Successful: List[BatchCreateDataTableValueSuccessResultTypeDef]
    Failed: List[BatchCreateDataTableValueFailureResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDataTableValueResponseTypeDef(TypedDict):
    Successful: List[BatchDeleteDataTableValueSuccessResultTypeDef]
    Failed: List[BatchDeleteDataTableValueFailureResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateDataTableValueResponseTypeDef(TypedDict):
    Successful: List[BatchUpdateDataTableValueSuccessResultTypeDef]
    Failed: List[BatchUpdateDataTableValueFailureResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDataTableValueRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Values: Sequence[DataTableDeleteValueIdentifierTypeDef]

class DescribeDataTableResponseTypeDef(TypedDict):
    DataTable: DataTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchDataTablesResponseTypeDef(TypedDict):
    DataTables: List[DataTableTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDescribeDataTableValueResponseTypeDef(TypedDict):
    Successful: List[BatchDescribeDataTableValueSuccessResultTypeDef]
    Failed: List[BatchDescribeDataTableValueFailureResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataTableValuesResponseTypeDef(TypedDict):
    Values: List[DataTableValueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDataTablePrimaryValuesResponseTypeDef(TypedDict):
    PrimaryValuesList: List[RecordPrimaryValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssignSlaActionDefinitionOutputTypeDef(TypedDict):
    SlaAssignmentType: Literal["CASES"]
    CaseSlaConfiguration: NotRequired[CaseSlaConfigurationOutputTypeDef]

class CreateCaseActionDefinitionOutputTypeDef(TypedDict):
    Fields: List[FieldValueOutputTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionOutputTypeDef(TypedDict):
    Fields: List[FieldValueOutputTypeDef]

class DescribePhoneNumberResponseTypeDef(TypedDict):
    ClaimedPhoneNumberSummary: ClaimedPhoneNumberSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConditionTypeDef(TypedDict):
    TargetListType: NotRequired[Literal["PROFICIENCIES"]]
    Conditions: NotRequired[Sequence[ConditionTypeDef]]

class GetCurrentUserDataRequestTypeDef(TypedDict):
    InstanceId: str
    Filters: UserDataFiltersTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ContactFlowAttributeFilterTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[ContactFlowAttributeAndConditionTypeDef]]
    AndCondition: NotRequired[ContactFlowAttributeAndConditionTypeDef]
    TagCondition: NotRequired[TagConditionTypeDef]
    ContactFlowTypeCondition: NotRequired[ContactFlowTypeConditionTypeDef]

class DescribeContactFlowModuleResponseTypeDef(TypedDict):
    ContactFlowModule: ContactFlowModuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowModulesResponseTypeDef(TypedDict):
    ContactFlowModules: List[ContactFlowModuleTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetContactMetricsResponseTypeDef(TypedDict):
    MetricResults: List[ContactMetricResultTypeDef]
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDataTableValueRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Values: Sequence[DataTableValueTypeDef]

class BatchUpdateDataTableValueRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Values: Sequence[DataTableValueTypeDef]

class SearchContactsAdditionalTimeRangeCriteriaTypeDef(TypedDict):
    TimeRange: NotRequired[SearchContactsTimeRangeTypeDef]
    TimestampCondition: NotRequired[SearchContactsTimestampConditionTypeDef]

TaskActionDefinitionUnionTypeDef = Union[
    TaskActionDefinitionTypeDef, TaskActionDefinitionOutputTypeDef
]

class DescribeQueueResponseTypeDef(TypedDict):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQueuesResponseTypeDef(TypedDict):
    Queues: List[QueueTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RoutingProfileTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    Name: NotRequired[str]
    RoutingProfileArn: NotRequired[str]
    RoutingProfileId: NotRequired[str]
    Description: NotRequired[str]
    MediaConcurrencies: NotRequired[List[MediaConcurrencyTypeDef]]
    DefaultOutboundQueueId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    NumberOfAssociatedQueues: NotRequired[int]
    NumberOfAssociatedManualAssignmentQueues: NotRequired[int]
    NumberOfAssociatedUsers: NotRequired[int]
    AgentAvailabilityTimer: NotRequired[AgentAvailabilityTimerType]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]
    IsDefault: NotRequired[bool]
    AssociatedQueueIds: NotRequired[List[str]]
    AssociatedManualAssignmentQueueIds: NotRequired[List[str]]

class UpdateRoutingProfileConcurrencyRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]

class CurrentMetricResultTypeDef(TypedDict):
    Dimensions: NotRequired[DimensionsTypeDef]
    Collections: NotRequired[List[CurrentMetricDataTypeDef]]

class AssociateRoutingProfileQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: NotRequired[Sequence[RoutingProfileQueueConfigTypeDef]]
    ManualAssignmentQueueConfigs: NotRequired[
        Sequence[RoutingProfileManualAssignmentQueueConfigTypeDef]
    ]

class CreateRoutingProfileRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]
    QueueConfigs: NotRequired[Sequence[RoutingProfileQueueConfigTypeDef]]
    ManualAssignmentQueueConfigs: NotRequired[
        Sequence[RoutingProfileManualAssignmentQueueConfigTypeDef]
    ]
    Tags: NotRequired[Mapping[str, str]]
    AgentAvailabilityTimer: NotRequired[AgentAvailabilityTimerType]

class UpdateRoutingProfileQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]

class InstanceStorageConfigTypeDef(TypedDict):
    StorageType: StorageTypeType
    AssociationId: NotRequired[str]
    S3Config: NotRequired[S3ConfigTypeDef]
    KinesisVideoStreamConfig: NotRequired[KinesisVideoStreamConfigTypeDef]
    KinesisStreamConfig: NotRequired[KinesisStreamConfigTypeDef]
    KinesisFirehoseConfig: NotRequired[KinesisFirehoseConfigTypeDef]

class EvaluationAnswerInputTypeDef(TypedDict):
    Value: NotRequired[EvaluationAnswerDataUnionTypeDef]

class EvaluationFormItemEnablementConditionOperandOutputTypeDef(TypedDict):
    Expression: NotRequired[EvaluationFormItemEnablementExpressionOutputTypeDef]
    Condition: NotRequired[Dict[str, Any]]

EvaluationFormItemEnablementExpressionUnionTypeDef = Union[
    EvaluationFormItemEnablementExpressionTypeDef,
    EvaluationFormItemEnablementExpressionOutputTypeDef,
]

class EvaluationFormMultiSelectQuestionAutomationOutputTypeDef(TypedDict):
    Options: NotRequired[List[EvaluationFormMultiSelectQuestionAutomationOptionOutputTypeDef]]
    DefaultOptionRefIds: NotRequired[List[str]]
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class EvaluationFormTextQuestionPropertiesTypeDef(TypedDict):
    Automation: NotRequired[EvaluationFormTextQuestionAutomationTypeDef]

class EvaluationFormNumericQuestionPropertiesOutputTypeDef(TypedDict):
    MinValue: int
    MaxValue: int
    Options: NotRequired[List[EvaluationFormNumericQuestionOptionTypeDef]]
    Automation: NotRequired[EvaluationFormNumericQuestionAutomationTypeDef]

class EvaluationFormNumericQuestionPropertiesTypeDef(TypedDict):
    MinValue: int
    MaxValue: int
    Options: NotRequired[Sequence[EvaluationFormNumericQuestionOptionTypeDef]]
    Automation: NotRequired[EvaluationFormNumericQuestionAutomationTypeDef]

class EvaluationFormSingleSelectQuestionAutomationOutputTypeDef(TypedDict):
    Options: NotRequired[List[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]]
    DefaultOptionRefId: NotRequired[str]
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class EvaluationFormSingleSelectQuestionAutomationTypeDef(TypedDict):
    Options: NotRequired[Sequence[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]]
    DefaultOptionRefId: NotRequired[str]
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class ListContactEvaluationsResponseTypeDef(TypedDict):
    EvaluationSummaryList: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchContactEvaluationsResponseTypeDef(TypedDict):
    EvaluationSearchSummaryList: List[EvaluationSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EvaluationAutomationRuleCategoryTypeDef(TypedDict):
    Category: str
    Condition: QuestionRuleCategoryAutomationConditionType
    PointsOfInterest: NotRequired[List[EvaluationTranscriptPointOfInterestTypeDef]]

class EvaluationGenAIAnswerAnalysisDetailsTypeDef(TypedDict):
    Justification: NotRequired[str]
    PointsOfInterest: NotRequired[List[EvaluationTranscriptPointOfInterestTypeDef]]

CaseSlaConfigurationTypeDef = TypedDict(
    "CaseSlaConfigurationTypeDef",
    {
        "Name": str,
        "Type": Literal["CaseField"],
        "TargetSlaMinutes": int,
        "FieldId": NotRequired[str],
        "TargetFieldValues": NotRequired[Sequence[FieldValueUnionUnionTypeDef]],
    },
)

class FieldValueTypeDef(TypedDict):
    Id: str
    Value: FieldValueUnionUnionTypeDef

class UserDataTypeDef(TypedDict):
    User: NotRequired[UserReferenceTypeDef]
    RoutingProfile: NotRequired[RoutingProfileReferenceTypeDef]
    HierarchyPath: NotRequired[HierarchyPathReferenceTypeDef]
    Status: NotRequired[AgentStatusReferenceTypeDef]
    AvailableSlotsByChannel: NotRequired[Dict[ChannelType, int]]
    MaxSlotsByChannel: NotRequired[Dict[ChannelType, int]]
    ActiveSlotsByChannel: NotRequired[Dict[ChannelType, int]]
    Contacts: NotRequired[List[AgentContactReferenceTypeDef]]
    NextStatus: NotRequired[str]

class HierarchyGroupTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    LevelId: NotRequired[str]
    HierarchyPath: NotRequired[HierarchyPathTypeDef]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class DescribeUserHierarchyStructureResponseTypeDef(TypedDict):
    HierarchyStructure: HierarchyStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserHierarchyStructureRequestTypeDef(TypedDict):
    HierarchyStructure: HierarchyStructureUpdateTypeDef
    InstanceId: str

class GetMetricDataRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: NotRequired[Sequence[GroupingType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetMetricDataRequestTypeDef(TypedDict):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: NotRequired[Sequence[GroupingType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class HistoricalMetricDataTypeDef(TypedDict):
    Metric: NotRequired[HistoricalMetricTypeDef]
    Value: NotRequired[float]

class CreateHoursOfOperationRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    TimeZone: str
    Config: Sequence[HoursOfOperationConfigTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class HoursOfOperationTypeDef(TypedDict):
    HoursOfOperationId: NotRequired[str]
    HoursOfOperationArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    TimeZone: NotRequired[str]
    Config: NotRequired[List[HoursOfOperationConfigTypeDef]]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class UpdateHoursOfOperationRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    TimeZone: NotRequired[str]
    Config: NotRequired[Sequence[HoursOfOperationConfigTypeDef]]

class CreateHoursOfOperationOverrideRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    Name: str
    Config: Sequence[HoursOfOperationOverrideConfigTypeDef]
    EffectiveFrom: str
    EffectiveTill: str
    Description: NotRequired[str]

class HoursOfOperationOverrideTypeDef(TypedDict):
    HoursOfOperationOverrideId: NotRequired[str]
    HoursOfOperationId: NotRequired[str]
    HoursOfOperationArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Config: NotRequired[List[HoursOfOperationOverrideConfigTypeDef]]
    EffectiveFrom: NotRequired[str]
    EffectiveTill: NotRequired[str]

class UpdateHoursOfOperationOverrideRequestTypeDef(TypedDict):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Config: NotRequired[Sequence[HoursOfOperationOverrideConfigTypeDef]]
    EffectiveFrom: NotRequired[str]
    EffectiveTill: NotRequired[str]

class EffectiveHoursOfOperationsTypeDef(TypedDict):
    Date: NotRequired[str]
    OperationalHours: NotRequired[List[OperationalHourTypeDef]]

class TaskTemplateConstraintsOutputTypeDef(TypedDict):
    RequiredFields: NotRequired[List[RequiredFieldInfoTypeDef]]
    ReadOnlyFields: NotRequired[List[ReadOnlyFieldInfoTypeDef]]
    InvisibleFields: NotRequired[List[InvisibleFieldInfoTypeDef]]

class TaskTemplateConstraintsTypeDef(TypedDict):
    RequiredFields: NotRequired[Sequence[RequiredFieldInfoTypeDef]]
    ReadOnlyFields: NotRequired[Sequence[ReadOnlyFieldInfoTypeDef]]
    InvisibleFields: NotRequired[Sequence[InvisibleFieldInfoTypeDef]]

class TaskTemplateDefaultsOutputTypeDef(TypedDict):
    DefaultFieldValues: NotRequired[List[TaskTemplateDefaultFieldValueTypeDef]]

class TaskTemplateDefaultsTypeDef(TypedDict):
    DefaultFieldValues: NotRequired[Sequence[TaskTemplateDefaultFieldValueTypeDef]]

TaskTemplateFieldUnionTypeDef = Union[TaskTemplateFieldTypeDef, TaskTemplateFieldOutputTypeDef]

class MetricV2TypeDef(TypedDict):
    Name: NotRequired[str]
    Threshold: NotRequired[Sequence[ThresholdV2TypeDef]]
    MetricId: NotRequired[str]
    MetricFilters: NotRequired[Sequence[MetricFilterV2UnionTypeDef]]

class MetricDataV2TypeDef(TypedDict):
    Metric: NotRequired[MetricV2OutputTypeDef]
    Value: NotRequired[float]

class EvaluationFormMultiSelectQuestionAutomationOptionTypeDef(TypedDict):
    RuleCategory: NotRequired[MultiSelectQuestionRuleCategoryAutomationUnionTypeDef]

class SendChatIntegrationEventRequestTypeDef(TypedDict):
    SourceId: str
    DestinationId: str
    Event: ChatEventTypeDef
    Subtype: NotRequired[str]
    NewSessionDetails: NotRequired[NewSessionDetailsTypeDef]

NextContactEntryTypeDef = TypedDict(
    "NextContactEntryTypeDef",
    {
        "Type": NotRequired[Literal["QUICK_CONNECT"]],
        "NextContactMetadata": NotRequired[NextContactMetadataTypeDef],
    },
)

class SendNotificationActionDefinitionTypeDef(TypedDict):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeUnionTypeDef
    Subject: NotRequired[str]
    Exclusion: NotRequired[NotificationRecipientTypeUnionTypeDef]

class WorkspaceThemeConfigTypeDef(TypedDict):
    Palette: NotRequired[WorkspaceThemePaletteTypeDef]
    Images: NotRequired[WorkspaceThemeImagesTypeDef]
    Typography: NotRequired[WorkspaceThemeTypographyTypeDef]

class ChatParticipantRoleConfigTypeDef(TypedDict):
    ParticipantTimerConfigList: Sequence[ParticipantTimerConfigurationTypeDef]

class AgentFirstOutputTypeDef(TypedDict):
    Preview: NotRequired[PreviewOutputTypeDef]

PreviewUnionTypeDef = Union[PreviewTypeDef, PreviewOutputTypeDef]

class DescribePredefinedAttributeResponseTypeDef(TypedDict):
    PredefinedAttribute: PredefinedAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPredefinedAttributesResponseTypeDef(TypedDict):
    PredefinedAttributes: List[PredefinedAttributeTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreatePredefinedAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Values: NotRequired[PredefinedAttributeValuesUnionTypeDef]
    Purposes: NotRequired[Sequence[str]]
    AttributeConfiguration: NotRequired[InputPredefinedAttributeConfigurationTypeDef]

class UpdatePredefinedAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Values: NotRequired[PredefinedAttributeValuesUnionTypeDef]
    Purposes: NotRequired[Sequence[str]]
    AttributeConfiguration: NotRequired[InputPredefinedAttributeConfigurationTypeDef]

class DataTableAccessControlConfigurationOutputTypeDef(TypedDict):
    PrimaryAttributeAccessControlConfiguration: NotRequired[
        PrimaryAttributeAccessControlConfigurationItemOutputTypeDef
    ]

class DataTableAccessControlConfigurationTypeDef(TypedDict):
    PrimaryAttributeAccessControlConfiguration: NotRequired[
        PrimaryAttributeAccessControlConfigurationItemTypeDef
    ]

class CreateQuickConnectRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    QuickConnectConfig: QuickConnectConfigTypeDef
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class QuickConnectTypeDef(TypedDict):
    QuickConnectARN: NotRequired[str]
    QuickConnectId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    QuickConnectConfig: NotRequired[QuickConnectConfigTypeDef]
    Tags: NotRequired[Dict[str, str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]

class UpdateQuickConnectConfigRequestTypeDef(TypedDict):
    InstanceId: str
    QuickConnectId: str
    QuickConnectConfig: QuickConnectConfigTypeDef

class RealTimeContactAnalysisSegmentTranscriptTypeDef(TypedDict):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Content: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: NotRequired[str]
    ContentType: NotRequired[str]
    Redaction: NotRequired[RealTimeContactAnalysisTranscriptItemRedactionTypeDef]
    Sentiment: NotRequired[RealTimeContactAnalysisSentimentLabelType]

class RealTimeContactAnalysisPointOfInterestTypeDef(TypedDict):
    TranscriptItems: NotRequired[
        List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef]
    ]

class RealTimeContactAnalysisIssueDetectedTypeDef(TypedDict):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContentTypeDef]

class ListContactReferencesResponseTypeDef(TypedDict):
    ReferenceSummaryList: List[ReferenceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeInstanceResponseTypeDef(TypedDict):
    Instance: InstanceTypeDef
    ReplicationConfiguration: ReplicationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourceTagsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    ResourceTypes: NotRequired[Sequence[str]]
    SearchCriteria: NotRequired[ResourceTagsSearchCriteriaTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchResourceTagsRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceTypes: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchCriteria: NotRequired[ResourceTagsSearchCriteriaTypeDef]

class SearchableRoutingCriteriaTypeDef(TypedDict):
    Steps: NotRequired[Sequence[SearchableRoutingCriteriaStepTypeDef]]

class CreateContactRequestTypeDef(TypedDict):
    InstanceId: str
    Channel: ChannelType
    InitiationMethod: ContactInitiationMethodType
    ClientToken: NotRequired[str]
    RelatedContactId: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    ExpiryDurationInMinutes: NotRequired[int]
    UserInfo: NotRequired[UserInfoTypeDef]
    InitiateAs: NotRequired[InitiateAsType]
    Name: NotRequired[str]
    Description: NotRequired[str]
    SegmentAttributes: NotRequired[Mapping[str, SegmentAttributeValueUnionTypeDef]]
    PreviousContactId: NotRequired[str]

class StartChatContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactFlowId: str
    ParticipantDetails: ParticipantDetailsTypeDef
    Attributes: NotRequired[Mapping[str, str]]
    ParticipantConfiguration: NotRequired[ParticipantConfigurationTypeDef]
    InitialMessage: NotRequired[ChatMessageTypeDef]
    ClientToken: NotRequired[str]
    ChatDurationInMinutes: NotRequired[int]
    SupportedMessagingContentTypes: NotRequired[Sequence[str]]
    PersistentChat: NotRequired[PersistentChatTypeDef]
    RelatedContactId: NotRequired[str]
    SegmentAttributes: NotRequired[Mapping[str, SegmentAttributeValueUnionTypeDef]]
    CustomerId: NotRequired[str]
    DisconnectOnCustomerExit: NotRequired[Sequence[Literal["AGENT"]]]

class StartEmailContactRequestTypeDef(TypedDict):
    InstanceId: str
    FromEmailAddress: EmailAddressInfoTypeDef
    DestinationEmailAddress: str
    EmailMessage: InboundEmailContentTypeDef
    Description: NotRequired[str]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    Name: NotRequired[str]
    AdditionalRecipients: NotRequired[InboundAdditionalRecipientsTypeDef]
    Attachments: NotRequired[Sequence[EmailAttachmentTypeDef]]
    ContactFlowId: NotRequired[str]
    RelatedContactId: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    SegmentAttributes: NotRequired[Mapping[str, SegmentAttributeValueUnionTypeDef]]
    ClientToken: NotRequired[str]

class StartTaskContactRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    PreviousContactId: NotRequired[str]
    ContactFlowId: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    ScheduledTime: NotRequired[TimestampTypeDef]
    TaskTemplateId: NotRequired[str]
    QuickConnectId: NotRequired[str]
    RelatedContactId: NotRequired[str]
    SegmentAttributes: NotRequired[Mapping[str, SegmentAttributeValueUnionTypeDef]]

class UpdateContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    SegmentAttributes: NotRequired[Mapping[str, SegmentAttributeValueUnionTypeDef]]
    QueueInfo: NotRequired[QueueInfoInputTypeDef]
    UserInfo: NotRequired[UserInfoTypeDef]
    CustomerEndpoint: NotRequired[EndpointTypeDef]
    SystemEndpoint: NotRequired[EndpointTypeDef]

class GetTrafficDistributionResponseTypeDef(TypedDict):
    TelephonyConfig: TelephonyConfigOutputTypeDef
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutputTypeDef
    AgentConfig: AgentConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

SignInConfigUnionTypeDef = Union[SignInConfigTypeDef, SignInConfigOutputTypeDef]

class OutboundEmailContentTypeDef(TypedDict):
    MessageSourceType: OutboundMessageSourceTypeType
    TemplatedMessageConfig: NotRequired[TemplatedMessageConfigTypeDef]
    RawMessage: NotRequired[OutboundRawMessageTypeDef]

class StartOutboundChatContactRequestTypeDef(TypedDict):
    SourceEndpoint: EndpointTypeDef
    DestinationEndpoint: EndpointTypeDef
    InstanceId: str
    SegmentAttributes: Mapping[str, SegmentAttributeValueUnionTypeDef]
    ContactFlowId: str
    Attributes: NotRequired[Mapping[str, str]]
    ChatDurationInMinutes: NotRequired[int]
    ParticipantDetails: NotRequired[ParticipantDetailsTypeDef]
    InitialSystemMessage: NotRequired[ChatMessageTypeDef]
    InitialTemplatedSystemMessage: NotRequired[TemplatedMessageConfigTypeDef]
    RelatedContactId: NotRequired[str]
    SupportedMessagingContentTypes: NotRequired[Sequence[str]]
    ClientToken: NotRequired[str]

class ContactAnalysisTypeDef(TypedDict):
    Transcript: NotRequired[TranscriptTypeDef]

class SearchUsersResponseTypeDef(TypedDict):
    Users: List[UserSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DataTableAttributeTypeDef(TypedDict):
    Name: str
    ValueType: DataTableAttributeValueTypeType
    AttributeId: NotRequired[str]
    Description: NotRequired[str]
    DataTableId: NotRequired[str]
    DataTableArn: NotRequired[str]
    Primary: NotRequired[bool]
    Version: NotRequired[str]
    LockVersion: NotRequired[DataTableLockVersionTypeDef]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]
    Validation: NotRequired[ValidationOutputTypeDef]

ValidationUnionTypeDef = Union[ValidationTypeDef, ValidationOutputTypeDef]

class CreateViewResponseTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewVersionResponseTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeViewResponseTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchViewsResponseTypeDef(TypedDict):
    Views: List[ViewTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateViewContentResponseTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionOutputTypeDef(TypedDict):
    AttributeCondition: NotRequired[AttributeConditionOutputTypeDef]
    AndExpression: NotRequired[List[Dict[str, Any]]]
    OrExpression: NotRequired[List[Dict[str, Any]]]
    NotAttributeCondition: NotRequired[AttributeConditionOutputTypeDef]

class ExpressionPaginatorTypeDef(TypedDict):
    AttributeCondition: NotRequired[AttributeConditionOutputTypeDef]
    AndExpression: NotRequired[List[Dict[str, Any]]]
    OrExpression: NotRequired[List[Dict[str, Any]]]
    NotAttributeCondition: NotRequired[AttributeConditionOutputTypeDef]

MatchCriteriaUnionTypeDef = Union[MatchCriteriaTypeDef, MatchCriteriaOutputTypeDef]

class UserSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]
    UserAttributeFilter: NotRequired[ControlPlaneUserAttributeFilterTypeDef]

class AgentStatusSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class DataTableSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class EvaluationFormSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class EvaluationSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class UserHierarchyGroupSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class ViewSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class WorkspaceAssociationSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class WorkspaceSearchFilterTypeDef(TypedDict):
    AttributeFilter: NotRequired[ControlPlaneAttributeFilterTypeDef]

class SearchContactFlowModulesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[ContactFlowModuleSearchFilterTypeDef]
    SearchCriteria: NotRequired[ContactFlowModuleSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchContactFlowModulesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[ContactFlowModuleSearchFilterTypeDef]
    SearchCriteria: NotRequired[ContactFlowModuleSearchCriteriaTypeDef]

class SearchEmailAddressesRequestTypeDef(TypedDict):
    InstanceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SearchCriteria: NotRequired[EmailAddressSearchCriteriaTypeDef]
    SearchFilter: NotRequired[EmailAddressSearchFilterTypeDef]

class SearchHoursOfOperationOverridesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[HoursOfOperationSearchFilterTypeDef]
    SearchCriteria: NotRequired[HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchHoursOfOperationOverridesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[HoursOfOperationSearchFilterTypeDef]
    SearchCriteria: NotRequired[HoursOfOperationOverrideSearchCriteriaTypeDef]

class SearchHoursOfOperationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[HoursOfOperationSearchFilterTypeDef]
    SearchCriteria: NotRequired[HoursOfOperationSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchHoursOfOperationsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[HoursOfOperationSearchFilterTypeDef]
    SearchCriteria: NotRequired[HoursOfOperationSearchCriteriaTypeDef]

class SearchPromptsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[PromptSearchFilterTypeDef]
    SearchCriteria: NotRequired[PromptSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchPromptsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[PromptSearchFilterTypeDef]
    SearchCriteria: NotRequired[PromptSearchCriteriaTypeDef]

class SearchQueuesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[QueueSearchFilterTypeDef]
    SearchCriteria: NotRequired[QueueSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchQueuesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[QueueSearchFilterTypeDef]
    SearchCriteria: NotRequired[QueueSearchCriteriaTypeDef]

class SearchQuickConnectsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[QuickConnectSearchFilterTypeDef]
    SearchCriteria: NotRequired[QuickConnectSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchQuickConnectsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[QuickConnectSearchFilterTypeDef]
    SearchCriteria: NotRequired[QuickConnectSearchCriteriaTypeDef]

class SearchRoutingProfilesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[RoutingProfileSearchFilterTypeDef]
    SearchCriteria: NotRequired[RoutingProfileSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchRoutingProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[RoutingProfileSearchFilterTypeDef]
    SearchCriteria: NotRequired[RoutingProfileSearchCriteriaTypeDef]

class SearchSecurityProfilesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchCriteria: NotRequired[SecurityProfileSearchCriteriaPaginatorTypeDef]
    SearchFilter: NotRequired[SecurityProfilesSearchFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSecurityProfilesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchCriteria: NotRequired[SecurityProfileSearchCriteriaTypeDef]
    SearchFilter: NotRequired[SecurityProfilesSearchFilterTypeDef]

class ConnectionDataTypeDef(TypedDict):
    Attendee: NotRequired[AttendeeTypeDef]
    Meeting: NotRequired[MeetingTypeDef]

class RuleActionOutputTypeDef(TypedDict):
    ActionType: ActionTypeType
    TaskAction: NotRequired[TaskActionDefinitionOutputTypeDef]
    EventBridgeAction: NotRequired[EventBridgeActionDefinitionTypeDef]
    AssignContactCategoryAction: NotRequired[Dict[str, Any]]
    SendNotificationAction: NotRequired[SendNotificationActionDefinitionOutputTypeDef]
    CreateCaseAction: NotRequired[CreateCaseActionDefinitionOutputTypeDef]
    UpdateCaseAction: NotRequired[UpdateCaseActionDefinitionOutputTypeDef]
    AssignSlaAction: NotRequired[AssignSlaActionDefinitionOutputTypeDef]
    EndAssociatedTasksAction: NotRequired[Dict[str, Any]]
    SubmitAutoEvaluationAction: NotRequired[SubmitAutoEvaluationActionDefinitionTypeDef]

class UserSearchCriteriaPaginatorTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    ListCondition: NotRequired[ListConditionTypeDef]
    HierarchyGroupCondition: NotRequired[HierarchyGroupConditionTypeDef]

class UserSearchCriteriaTypeDef(TypedDict):
    OrConditions: NotRequired[Sequence[Mapping[str, Any]]]
    AndConditions: NotRequired[Sequence[Mapping[str, Any]]]
    StringCondition: NotRequired[StringConditionTypeDef]
    ListCondition: NotRequired[ListConditionTypeDef]
    HierarchyGroupCondition: NotRequired[HierarchyGroupConditionTypeDef]

class ContactFlowSearchFilterTypeDef(TypedDict):
    TagFilter: NotRequired[ControlPlaneTagFilterTypeDef]
    FlowAttributeFilter: NotRequired[ContactFlowAttributeFilterTypeDef]

class SearchContactsAdditionalTimeRangeTypeDef(TypedDict):
    Criteria: Sequence[SearchContactsAdditionalTimeRangeCriteriaTypeDef]
    MatchType: SearchContactsMatchTypeType

class DescribeRoutingProfileResponseTypeDef(TypedDict):
    RoutingProfile: RoutingProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRoutingProfilesResponseTypeDef(TypedDict):
    RoutingProfiles: List[RoutingProfileTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCurrentMetricDataResponseTypeDef(TypedDict):
    MetricResults: List[CurrentMetricResultTypeDef]
    DataSnapshotTime: datetime
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateInstanceStorageConfigRequestTypeDef(TypedDict):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef
    ClientToken: NotRequired[str]

class DescribeInstanceStorageConfigResponseTypeDef(TypedDict):
    StorageConfig: InstanceStorageConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceStorageConfigsResponseTypeDef(TypedDict):
    StorageConfigs: List[InstanceStorageConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateInstanceStorageConfigRequestTypeDef(TypedDict):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef
    ClientToken: NotRequired[str]

class SubmitContactEvaluationRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationId: str
    Answers: NotRequired[Mapping[str, EvaluationAnswerInputTypeDef]]
    Notes: NotRequired[Mapping[str, EvaluationNoteTypeDef]]
    SubmittedBy: NotRequired[EvaluatorUserUnionTypeDef]

class UpdateContactEvaluationRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationId: str
    Answers: NotRequired[Mapping[str, EvaluationAnswerInputTypeDef]]
    Notes: NotRequired[Mapping[str, EvaluationNoteTypeDef]]
    UpdatedBy: NotRequired[EvaluatorUserUnionTypeDef]

class EvaluationFormItemEnablementConditionOutputTypeDef(TypedDict):
    Operands: List[EvaluationFormItemEnablementConditionOperandOutputTypeDef]
    Operator: NotRequired[EvaluationFormItemEnablementOperatorType]

class EvaluationFormItemEnablementConditionOperandTypeDef(TypedDict):
    Expression: NotRequired[EvaluationFormItemEnablementExpressionUnionTypeDef]
    Condition: NotRequired[Mapping[str, Any]]

class EvaluationFormMultiSelectQuestionPropertiesOutputTypeDef(TypedDict):
    Options: List[EvaluationFormMultiSelectQuestionOptionTypeDef]
    DisplayAs: NotRequired[EvaluationFormMultiSelectQuestionDisplayModeType]
    Automation: NotRequired[EvaluationFormMultiSelectQuestionAutomationOutputTypeDef]

EvaluationFormNumericQuestionPropertiesUnionTypeDef = Union[
    EvaluationFormNumericQuestionPropertiesTypeDef,
    EvaluationFormNumericQuestionPropertiesOutputTypeDef,
]

class EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef(TypedDict):
    Options: List[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: NotRequired[EvaluationFormSingleSelectQuestionDisplayModeType]
    Automation: NotRequired[EvaluationFormSingleSelectQuestionAutomationOutputTypeDef]

EvaluationFormSingleSelectQuestionAutomationUnionTypeDef = Union[
    EvaluationFormSingleSelectQuestionAutomationTypeDef,
    EvaluationFormSingleSelectQuestionAutomationOutputTypeDef,
]

class EvaluationContactLensAnswerAnalysisDetailsTypeDef(TypedDict):
    MatchedRuleCategories: NotRequired[List[EvaluationAutomationRuleCategoryTypeDef]]

CaseSlaConfigurationUnionTypeDef = Union[
    CaseSlaConfigurationTypeDef, CaseSlaConfigurationOutputTypeDef
]
FieldValueUnionExtraTypeDef = Union[FieldValueTypeDef, FieldValueOutputTypeDef]

class GetCurrentUserDataResponseTypeDef(TypedDict):
    UserDataList: List[UserDataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeUserHierarchyGroupResponseTypeDef(TypedDict):
    HierarchyGroup: HierarchyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchUserHierarchyGroupsResponseTypeDef(TypedDict):
    UserHierarchyGroups: List[HierarchyGroupTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class HistoricalMetricResultTypeDef(TypedDict):
    Dimensions: NotRequired[DimensionsTypeDef]
    Collections: NotRequired[List[HistoricalMetricDataTypeDef]]

class DescribeHoursOfOperationResponseTypeDef(TypedDict):
    HoursOfOperation: HoursOfOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchHoursOfOperationsResponseTypeDef(TypedDict):
    HoursOfOperations: List[HoursOfOperationTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeHoursOfOperationOverrideResponseTypeDef(TypedDict):
    HoursOfOperationOverride: HoursOfOperationOverrideTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHoursOfOperationOverridesResponseTypeDef(TypedDict):
    HoursOfOperationOverrideList: List[HoursOfOperationOverrideTypeDef]
    LastModifiedRegion: str
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchHoursOfOperationOverridesResponseTypeDef(TypedDict):
    HoursOfOperationOverrides: List[HoursOfOperationOverrideTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetEffectiveHoursOfOperationsResponseTypeDef(TypedDict):
    EffectiveHoursOfOperationList: List[EffectiveHoursOfOperationsTypeDef]
    TimeZone: str
    ResponseMetadata: ResponseMetadataTypeDef

TaskTemplateConstraintsUnionTypeDef = Union[
    TaskTemplateConstraintsTypeDef, TaskTemplateConstraintsOutputTypeDef
]

class GetTaskTemplateResponseTypeDef(TypedDict):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    SelfAssignFlowId: str
    Constraints: TaskTemplateConstraintsOutputTypeDef
    Defaults: TaskTemplateDefaultsOutputTypeDef
    Fields: List[TaskTemplateFieldOutputTypeDef]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskTemplateResponseTypeDef(TypedDict):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    SelfAssignFlowId: str
    Constraints: TaskTemplateConstraintsOutputTypeDef
    Defaults: TaskTemplateDefaultsOutputTypeDef
    Fields: List[TaskTemplateFieldOutputTypeDef]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

TaskTemplateDefaultsUnionTypeDef = Union[
    TaskTemplateDefaultsTypeDef, TaskTemplateDefaultsOutputTypeDef
]
MetricV2UnionTypeDef = Union[MetricV2TypeDef, MetricV2OutputTypeDef]

class MetricResultV2TypeDef(TypedDict):
    Dimensions: NotRequired[Dict[str, str]]
    MetricInterval: NotRequired[MetricIntervalTypeDef]
    Collections: NotRequired[List[MetricDataV2TypeDef]]

EvaluationFormMultiSelectQuestionAutomationOptionUnionTypeDef = Union[
    EvaluationFormMultiSelectQuestionAutomationOptionTypeDef,
    EvaluationFormMultiSelectQuestionAutomationOptionOutputTypeDef,
]
SendNotificationActionDefinitionUnionTypeDef = Union[
    SendNotificationActionDefinitionTypeDef, SendNotificationActionDefinitionOutputTypeDef
]

class WorkspaceThemeTypeDef(TypedDict):
    Light: NotRequired[WorkspaceThemeConfigTypeDef]
    Dark: NotRequired[WorkspaceThemeConfigTypeDef]

class UpdateParticipantRoleConfigChannelInfoTypeDef(TypedDict):
    Chat: NotRequired[ChatParticipantRoleConfigTypeDef]

class OutboundStrategyConfigOutputTypeDef(TypedDict):
    AgentFirst: NotRequired[AgentFirstOutputTypeDef]

class AgentFirstTypeDef(TypedDict):
    Preview: NotRequired[PreviewUnionTypeDef]

class GranularAccessControlConfigurationOutputTypeDef(TypedDict):
    DataTableAccessControlConfiguration: NotRequired[
        DataTableAccessControlConfigurationOutputTypeDef
    ]

class GranularAccessControlConfigurationTypeDef(TypedDict):
    DataTableAccessControlConfiguration: NotRequired[DataTableAccessControlConfigurationTypeDef]

class DescribeQuickConnectResponseTypeDef(TypedDict):
    QuickConnect: QuickConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickConnectsResponseTypeDef(TypedDict):
    QuickConnects: List[QuickConnectTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RealTimeContactAnalysisCategoryDetailsTypeDef(TypedDict):
    PointsOfInterest: List[RealTimeContactAnalysisPointOfInterestTypeDef]

class RealTimeContactAnalysisSegmentIssuesTypeDef(TypedDict):
    IssuesDetected: List[RealTimeContactAnalysisIssueDetectedTypeDef]

class UpdateTrafficDistributionRequestTypeDef(TypedDict):
    Id: str
    TelephonyConfig: NotRequired[TelephonyConfigUnionTypeDef]
    SignInConfig: NotRequired[SignInConfigUnionTypeDef]
    AgentConfig: NotRequired[AgentConfigUnionTypeDef]

class SendOutboundEmailRequestTypeDef(TypedDict):
    InstanceId: str
    FromEmailAddress: EmailAddressInfoTypeDef
    DestinationEmailAddress: EmailAddressInfoTypeDef
    EmailMessage: OutboundEmailContentTypeDef
    TrafficType: TrafficTypeType
    AdditionalRecipients: NotRequired[OutboundAdditionalRecipientsTypeDef]
    SourceCampaign: NotRequired[SourceCampaignTypeDef]
    ClientToken: NotRequired[str]

class StartOutboundEmailContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    DestinationEmailAddress: EmailAddressInfoTypeDef
    EmailMessage: OutboundEmailContentTypeDef
    FromEmailAddress: NotRequired[EmailAddressInfoTypeDef]
    AdditionalRecipients: NotRequired[OutboundAdditionalRecipientsTypeDef]
    ClientToken: NotRequired[str]

class DescribeDataTableAttributeResponseTypeDef(TypedDict):
    Attribute: DataTableAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataTableAttributesResponseTypeDef(TypedDict):
    Attributes: List[DataTableAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDataTableAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    Name: str
    ValueType: DataTableAttributeValueTypeType
    Description: NotRequired[str]
    Primary: NotRequired[bool]
    Validation: NotRequired[ValidationUnionTypeDef]

class UpdateDataTableAttributeRequestTypeDef(TypedDict):
    InstanceId: str
    DataTableId: str
    AttributeName: str
    Name: str
    ValueType: DataTableAttributeValueTypeType
    Description: NotRequired[str]
    Primary: NotRequired[bool]
    Validation: NotRequired[ValidationUnionTypeDef]

class StepTypeDef(TypedDict):
    Expiry: NotRequired[ExpiryTypeDef]
    Expression: NotRequired[ExpressionOutputTypeDef]
    Status: NotRequired[RoutingCriteriaStepStatusType]

class StepPaginatorTypeDef(TypedDict):
    Expiry: NotRequired[ExpiryTypeDef]
    Expression: NotRequired[ExpressionPaginatorTypeDef]
    Status: NotRequired[RoutingCriteriaStepStatusType]

class AttributeConditionTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]
    ProficiencyLevel: NotRequired[float]
    Range: NotRequired[RangeTypeDef]
    MatchCriteria: NotRequired[MatchCriteriaUnionTypeDef]
    ComparisonOperator: NotRequired[str]

class SearchAgentStatusesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[AgentStatusSearchFilterTypeDef]
    SearchCriteria: NotRequired[AgentStatusSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchAgentStatusesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[AgentStatusSearchFilterTypeDef]
    SearchCriteria: NotRequired[AgentStatusSearchCriteriaTypeDef]

class SearchDataTablesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[DataTableSearchFilterTypeDef]
    SearchCriteria: NotRequired[DataTableSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchDataTablesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[DataTableSearchFilterTypeDef]
    SearchCriteria: NotRequired[DataTableSearchCriteriaTypeDef]

class SearchEvaluationFormsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchCriteria: NotRequired[EvaluationFormSearchCriteriaTypeDef]
    SearchFilter: NotRequired[EvaluationFormSearchFilterTypeDef]

class SearchContactEvaluationsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchCriteria: NotRequired[EvaluationSearchCriteriaTypeDef]
    SearchFilter: NotRequired[EvaluationSearchFilterTypeDef]

class SearchUserHierarchyGroupsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[UserHierarchyGroupSearchFilterTypeDef]
    SearchCriteria: NotRequired[UserHierarchyGroupSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchUserHierarchyGroupsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[UserHierarchyGroupSearchFilterTypeDef]
    SearchCriteria: NotRequired[UserHierarchyGroupSearchCriteriaTypeDef]

class SearchViewsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[ViewSearchFilterTypeDef]
    SearchCriteria: NotRequired[ViewSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchViewsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[ViewSearchFilterTypeDef]
    SearchCriteria: NotRequired[ViewSearchCriteriaTypeDef]

class SearchWorkspaceAssociationsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[WorkspaceAssociationSearchFilterTypeDef]
    SearchCriteria: NotRequired[WorkspaceAssociationSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchWorkspaceAssociationsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[WorkspaceAssociationSearchFilterTypeDef]
    SearchCriteria: NotRequired[WorkspaceAssociationSearchCriteriaTypeDef]

class SearchWorkspacesRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[WorkspaceSearchFilterTypeDef]
    SearchCriteria: NotRequired[WorkspaceSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchWorkspacesRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[WorkspaceSearchFilterTypeDef]
    SearchCriteria: NotRequired[WorkspaceSearchCriteriaTypeDef]

class StartWebRTCContactResponseTypeDef(TypedDict):
    ConnectionData: ConnectionDataTypeDef
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RuleTypeDef(TypedDict):
    Name: str
    RuleId: str
    RuleArn: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: List[RuleActionOutputTypeDef]
    PublishStatus: RulePublishStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    LastUpdatedBy: str
    Tags: NotRequired[Dict[str, str]]

class SearchUsersRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[UserSearchFilterTypeDef]
    SearchCriteria: NotRequired[UserSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchUsersRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[UserSearchFilterTypeDef]
    SearchCriteria: NotRequired[UserSearchCriteriaTypeDef]

class SearchContactFlowsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    SearchFilter: NotRequired[ContactFlowSearchFilterTypeDef]
    SearchCriteria: NotRequired[ContactFlowSearchCriteriaPaginatorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchContactFlowsRequestTypeDef(TypedDict):
    InstanceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SearchFilter: NotRequired[ContactFlowSearchFilterTypeDef]
    SearchCriteria: NotRequired[ContactFlowSearchCriteriaTypeDef]

class SearchCriteriaTypeDef(TypedDict):
    Name: NotRequired[NameCriteriaTypeDef]
    AgentIds: NotRequired[Sequence[str]]
    AgentHierarchyGroups: NotRequired[AgentHierarchyGroupsTypeDef]
    Channels: NotRequired[Sequence[ChannelType]]
    ContactAnalysis: NotRequired[ContactAnalysisTypeDef]
    InitiationMethods: NotRequired[Sequence[ContactInitiationMethodType]]
    QueueIds: NotRequired[Sequence[str]]
    RoutingCriteria: NotRequired[SearchableRoutingCriteriaTypeDef]
    AdditionalTimeRange: NotRequired[SearchContactsAdditionalTimeRangeTypeDef]
    SearchableContactAttributes: NotRequired[SearchableContactAttributesTypeDef]
    SearchableSegmentAttributes: NotRequired[SearchableSegmentAttributesTypeDef]

class EvaluationFormItemEnablementConfigurationOutputTypeDef(TypedDict):
    Condition: EvaluationFormItemEnablementConditionOutputTypeDef
    Action: EvaluationFormItemEnablementActionType
    DefaultAction: NotRequired[EvaluationFormItemEnablementActionType]

EvaluationFormItemEnablementConditionOperandUnionTypeDef = Union[
    EvaluationFormItemEnablementConditionOperandTypeDef,
    EvaluationFormItemEnablementConditionOperandOutputTypeDef,
]
EvaluationFormQuestionTypePropertiesOutputTypeDef = TypedDict(
    "EvaluationFormQuestionTypePropertiesOutputTypeDef",
    {
        "Numeric": NotRequired[EvaluationFormNumericQuestionPropertiesOutputTypeDef],
        "SingleSelect": NotRequired[EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef],
        "Text": NotRequired[EvaluationFormTextQuestionPropertiesTypeDef],
        "MultiSelect": NotRequired[EvaluationFormMultiSelectQuestionPropertiesOutputTypeDef],
    },
)

class EvaluationFormSingleSelectQuestionPropertiesTypeDef(TypedDict):
    Options: Sequence[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: NotRequired[EvaluationFormSingleSelectQuestionDisplayModeType]
    Automation: NotRequired[EvaluationFormSingleSelectQuestionAutomationUnionTypeDef]

class EvaluationQuestionAnswerAnalysisDetailsTypeDef(TypedDict):
    GenAI: NotRequired[EvaluationGenAIAnswerAnalysisDetailsTypeDef]
    ContactLens: NotRequired[EvaluationContactLensAnswerAnalysisDetailsTypeDef]

class AssignSlaActionDefinitionTypeDef(TypedDict):
    SlaAssignmentType: Literal["CASES"]
    CaseSlaConfiguration: NotRequired[CaseSlaConfigurationUnionTypeDef]

class CreateCaseActionDefinitionTypeDef(TypedDict):
    Fields: Sequence[FieldValueUnionExtraTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionTypeDef(TypedDict):
    Fields: Sequence[FieldValueUnionExtraTypeDef]

class GetMetricDataResponseTypeDef(TypedDict):
    MetricResults: List[HistoricalMetricResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateTaskTemplateRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Fields: Sequence[TaskTemplateFieldUnionTypeDef]
    Description: NotRequired[str]
    ContactFlowId: NotRequired[str]
    SelfAssignFlowId: NotRequired[str]
    Constraints: NotRequired[TaskTemplateConstraintsUnionTypeDef]
    Defaults: NotRequired[TaskTemplateDefaultsUnionTypeDef]
    Status: NotRequired[TaskTemplateStatusType]
    ClientToken: NotRequired[str]

class UpdateTaskTemplateRequestTypeDef(TypedDict):
    TaskTemplateId: str
    InstanceId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    ContactFlowId: NotRequired[str]
    SelfAssignFlowId: NotRequired[str]
    Constraints: NotRequired[TaskTemplateConstraintsUnionTypeDef]
    Defaults: NotRequired[TaskTemplateDefaultsUnionTypeDef]
    Status: NotRequired[TaskTemplateStatusType]
    Fields: NotRequired[Sequence[TaskTemplateFieldUnionTypeDef]]

class GetMetricDataV2RequestTypeDef(TypedDict):
    ResourceArn: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: Sequence[FilterV2TypeDef]
    Metrics: Sequence[MetricV2UnionTypeDef]
    Interval: NotRequired[IntervalDetailsTypeDef]
    Groupings: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetMetricDataV2ResponseTypeDef(TypedDict):
    MetricResults: List[MetricResultV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EvaluationFormMultiSelectQuestionAutomationTypeDef(TypedDict):
    Options: NotRequired[Sequence[EvaluationFormMultiSelectQuestionAutomationOptionUnionTypeDef]]
    DefaultOptionRefIds: NotRequired[Sequence[str]]
    AnswerSource: NotRequired[EvaluationFormQuestionAutomationAnswerSourceTypeDef]

class CreateWorkspaceRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    Description: NotRequired[str]
    Theme: NotRequired[WorkspaceThemeTypeDef]
    Title: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateWorkspaceThemeRequestTypeDef(TypedDict):
    InstanceId: str
    WorkspaceId: str
    Theme: NotRequired[WorkspaceThemeTypeDef]

class WorkspaceTypeDef(TypedDict):
    Id: str
    Name: str
    Arn: str
    LastModifiedTime: datetime
    Visibility: NotRequired[VisibilityType]
    Description: NotRequired[str]
    Theme: NotRequired[WorkspaceThemeTypeDef]
    Title: NotRequired[str]
    LastModifiedRegion: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class UpdateParticipantRoleConfigRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    ChannelConfiguration: UpdateParticipantRoleConfigChannelInfoTypeDef

OutboundStrategyOutputTypeDef = TypedDict(
    "OutboundStrategyOutputTypeDef",
    {
        "Type": Literal["AGENT_FIRST"],
        "Config": NotRequired[OutboundStrategyConfigOutputTypeDef],
    },
)
AgentFirstUnionTypeDef = Union[AgentFirstTypeDef, AgentFirstOutputTypeDef]

class SecurityProfileTypeDef(TypedDict):
    Id: NotRequired[str]
    OrganizationResourceId: NotRequired[str]
    Arn: NotRequired[str]
    SecurityProfileName: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    AllowedAccessControlTags: NotRequired[Dict[str, str]]
    TagRestrictedResources: NotRequired[List[str]]
    LastModifiedTime: NotRequired[datetime]
    LastModifiedRegion: NotRequired[str]
    HierarchyRestrictedResources: NotRequired[List[str]]
    AllowedAccessControlHierarchyGroupId: NotRequired[str]
    GranularAccessControlConfiguration: NotRequired[GranularAccessControlConfigurationOutputTypeDef]

GranularAccessControlConfigurationUnionTypeDef = Union[
    GranularAccessControlConfigurationTypeDef, GranularAccessControlConfigurationOutputTypeDef
]

class RealTimeContactAnalysisSegmentCategoriesTypeDef(TypedDict):
    MatchedDetails: Dict[str, RealTimeContactAnalysisCategoryDetailsTypeDef]

class RoutingCriteriaTypeDef(TypedDict):
    Steps: NotRequired[List[StepTypeDef]]
    ActivationTimestamp: NotRequired[datetime]
    Index: NotRequired[int]

class RoutingCriteriaPaginatorTypeDef(TypedDict):
    Steps: NotRequired[List[StepPaginatorTypeDef]]
    ActivationTimestamp: NotRequired[datetime]
    Index: NotRequired[int]

AttributeConditionUnionTypeDef = Union[AttributeConditionTypeDef, AttributeConditionOutputTypeDef]

class DescribeRuleResponseTypeDef(TypedDict):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactsRequestPaginateTypeDef(TypedDict):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: NotRequired[SearchCriteriaTypeDef]
    Sort: NotRequired[SortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchContactsRequestTypeDef(TypedDict):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: NotRequired[SearchCriteriaTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[SortTypeDef]

class EvaluationFormItemEnablementConditionTypeDef(TypedDict):
    Operands: Sequence[EvaluationFormItemEnablementConditionOperandUnionTypeDef]
    Operator: NotRequired[EvaluationFormItemEnablementOperatorType]

class EvaluationFormQuestionOutputTypeDef(TypedDict):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: NotRequired[str]
    NotApplicableEnabled: NotRequired[bool]
    QuestionTypeProperties: NotRequired[EvaluationFormQuestionTypePropertiesOutputTypeDef]
    Enablement: NotRequired[EvaluationFormItemEnablementConfigurationOutputTypeDef]
    Weight: NotRequired[float]

EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef = Union[
    EvaluationFormSingleSelectQuestionPropertiesTypeDef,
    EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef,
]

class EvaluationSuggestedAnswerTypeDef(TypedDict):
    Status: EvaluationSuggestedAnswerStatusType
    AnalysisType: EvaluationQuestionAnswerAnalysisTypeType
    Value: NotRequired[EvaluationAnswerDataOutputTypeDef]
    Input: NotRequired[EvaluationQuestionInputDetailsTypeDef]
    AnalysisDetails: NotRequired[EvaluationQuestionAnswerAnalysisDetailsTypeDef]

AssignSlaActionDefinitionUnionTypeDef = Union[
    AssignSlaActionDefinitionTypeDef, AssignSlaActionDefinitionOutputTypeDef
]
CreateCaseActionDefinitionUnionTypeDef = Union[
    CreateCaseActionDefinitionTypeDef, CreateCaseActionDefinitionOutputTypeDef
]
UpdateCaseActionDefinitionUnionTypeDef = Union[
    UpdateCaseActionDefinitionTypeDef, UpdateCaseActionDefinitionOutputTypeDef
]
EvaluationFormMultiSelectQuestionAutomationUnionTypeDef = Union[
    EvaluationFormMultiSelectQuestionAutomationTypeDef,
    EvaluationFormMultiSelectQuestionAutomationOutputTypeDef,
]

class DescribeWorkspaceResponseTypeDef(TypedDict):
    Workspace: WorkspaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OutboundStrategyConfigTypeDef(TypedDict):
    AgentFirst: NotRequired[AgentFirstUnionTypeDef]

class DescribeSecurityProfileResponseTypeDef(TypedDict):
    SecurityProfile: SecurityProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityProfileRequestTypeDef(TypedDict):
    SecurityProfileName: str
    InstanceId: str
    Description: NotRequired[str]
    Permissions: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]
    AllowedAccessControlTags: NotRequired[Mapping[str, str]]
    TagRestrictedResources: NotRequired[Sequence[str]]
    Applications: NotRequired[Sequence[ApplicationUnionTypeDef]]
    HierarchyRestrictedResources: NotRequired[Sequence[str]]
    AllowedAccessControlHierarchyGroupId: NotRequired[str]
    AllowedFlowModules: NotRequired[Sequence[FlowModuleTypeDef]]
    GranularAccessControlConfiguration: NotRequired[GranularAccessControlConfigurationUnionTypeDef]

class UpdateSecurityProfileRequestTypeDef(TypedDict):
    SecurityProfileId: str
    InstanceId: str
    Description: NotRequired[str]
    Permissions: NotRequired[Sequence[str]]
    AllowedAccessControlTags: NotRequired[Mapping[str, str]]
    TagRestrictedResources: NotRequired[Sequence[str]]
    Applications: NotRequired[Sequence[ApplicationUnionTypeDef]]
    HierarchyRestrictedResources: NotRequired[Sequence[str]]
    AllowedAccessControlHierarchyGroupId: NotRequired[str]
    AllowedFlowModules: NotRequired[Sequence[FlowModuleTypeDef]]
    GranularAccessControlConfiguration: NotRequired[GranularAccessControlConfigurationUnionTypeDef]

class RealtimeContactAnalysisSegmentTypeDef(TypedDict):
    Transcript: NotRequired[RealTimeContactAnalysisSegmentTranscriptTypeDef]
    Categories: NotRequired[RealTimeContactAnalysisSegmentCategoriesTypeDef]
    Issues: NotRequired[RealTimeContactAnalysisSegmentIssuesTypeDef]
    Event: NotRequired[RealTimeContactAnalysisSegmentEventTypeDef]
    Attachments: NotRequired[RealTimeContactAnalysisSegmentAttachmentsTypeDef]
    PostContactSummary: NotRequired[RealTimeContactAnalysisSegmentPostContactSummaryTypeDef]

class ContactSearchSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    InitialContactId: NotRequired[str]
    PreviousContactId: NotRequired[str]
    InitiationMethod: NotRequired[ContactInitiationMethodType]
    Channel: NotRequired[ChannelType]
    QueueInfo: NotRequired[ContactSearchSummaryQueueInfoTypeDef]
    AgentInfo: NotRequired[ContactSearchSummaryAgentInfoTypeDef]
    InitiationTimestamp: NotRequired[datetime]
    DisconnectTimestamp: NotRequired[datetime]
    ScheduledTimestamp: NotRequired[datetime]
    SegmentAttributes: NotRequired[Dict[str, ContactSearchSummarySegmentAttributeValueTypeDef]]
    Name: NotRequired[str]
    RoutingCriteria: NotRequired[RoutingCriteriaTypeDef]

class ContactTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    InitialContactId: NotRequired[str]
    PreviousContactId: NotRequired[str]
    ContactAssociationId: NotRequired[str]
    InitiationMethod: NotRequired[ContactInitiationMethodType]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Channel: NotRequired[ChannelType]
    QueueInfo: NotRequired[QueueInfoTypeDef]
    AgentInfo: NotRequired[AgentInfoTypeDef]
    InitiationTimestamp: NotRequired[datetime]
    DisconnectTimestamp: NotRequired[datetime]
    LastUpdateTimestamp: NotRequired[datetime]
    LastPausedTimestamp: NotRequired[datetime]
    LastResumedTimestamp: NotRequired[datetime]
    RingStartTimestamp: NotRequired[datetime]
    TotalPauseCount: NotRequired[int]
    TotalPauseDurationInSeconds: NotRequired[int]
    ScheduledTimestamp: NotRequired[datetime]
    RelatedContactId: NotRequired[str]
    WisdomInfo: NotRequired[WisdomInfoTypeDef]
    CustomerId: NotRequired[str]
    CustomerEndpoint: NotRequired[EndpointInfoTypeDef]
    SystemEndpoint: NotRequired[EndpointInfoTypeDef]
    QueueTimeAdjustmentSeconds: NotRequired[int]
    QueuePriority: NotRequired[int]
    Tags: NotRequired[Dict[str, str]]
    ConnectedToSystemTimestamp: NotRequired[datetime]
    RoutingCriteria: NotRequired[RoutingCriteriaTypeDef]
    Customer: NotRequired[CustomerTypeDef]
    Campaign: NotRequired[CampaignTypeDef]
    AnsweringMachineDetectionStatus: NotRequired[AnsweringMachineDetectionStatusType]
    CustomerVoiceActivity: NotRequired[CustomerVoiceActivityTypeDef]
    QualityMetrics: NotRequired[QualityMetricsTypeDef]
    ChatMetrics: NotRequired[ChatMetricsTypeDef]
    DisconnectDetails: NotRequired[DisconnectDetailsTypeDef]
    AdditionalEmailRecipients: NotRequired[AdditionalEmailRecipientsTypeDef]
    SegmentAttributes: NotRequired[Dict[str, SegmentAttributeValueOutputTypeDef]]
    Recordings: NotRequired[List[RecordingInfoTypeDef]]
    DisconnectReason: NotRequired[str]
    ContactEvaluations: NotRequired[Dict[str, ContactEvaluationTypeDef]]
    TaskTemplateInfo: NotRequired[TaskTemplateInfoV2TypeDef]
    ContactDetails: NotRequired[ContactDetailsTypeDef]
    OutboundStrategy: NotRequired[OutboundStrategyOutputTypeDef]
    Attributes: NotRequired[Dict[str, str]]
    NextContacts: NotRequired[List[NextContactEntryTypeDef]]

class ContactSearchSummaryPaginatorTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    InitialContactId: NotRequired[str]
    PreviousContactId: NotRequired[str]
    InitiationMethod: NotRequired[ContactInitiationMethodType]
    Channel: NotRequired[ChannelType]
    QueueInfo: NotRequired[ContactSearchSummaryQueueInfoTypeDef]
    AgentInfo: NotRequired[ContactSearchSummaryAgentInfoTypeDef]
    InitiationTimestamp: NotRequired[datetime]
    DisconnectTimestamp: NotRequired[datetime]
    ScheduledTimestamp: NotRequired[datetime]
    SegmentAttributes: NotRequired[
        Dict[str, ContactSearchSummarySegmentAttributeValuePaginatorTypeDef]
    ]
    Name: NotRequired[str]
    RoutingCriteria: NotRequired[RoutingCriteriaPaginatorTypeDef]

class ExpressionTypeDef(TypedDict):
    AttributeCondition: NotRequired[AttributeConditionUnionTypeDef]
    AndExpression: NotRequired[Sequence[Mapping[str, Any]]]
    OrExpression: NotRequired[Sequence[Mapping[str, Any]]]
    NotAttributeCondition: NotRequired[AttributeConditionUnionTypeDef]

EvaluationFormItemEnablementConditionUnionTypeDef = Union[
    EvaluationFormItemEnablementConditionTypeDef, EvaluationFormItemEnablementConditionOutputTypeDef
]

class EvaluationFormItemOutputTypeDef(TypedDict):
    Section: NotRequired[EvaluationFormSectionOutputTypeDef]
    Question: NotRequired[EvaluationFormQuestionOutputTypeDef]

class EvaluationAnswerOutputTypeDef(TypedDict):
    Value: NotRequired[EvaluationAnswerDataOutputTypeDef]
    SystemSuggestedValue: NotRequired[EvaluationAnswerDataOutputTypeDef]
    SuggestedAnswers: NotRequired[List[EvaluationSuggestedAnswerTypeDef]]

class RuleActionTypeDef(TypedDict):
    ActionType: ActionTypeType
    TaskAction: NotRequired[TaskActionDefinitionUnionTypeDef]
    EventBridgeAction: NotRequired[EventBridgeActionDefinitionTypeDef]
    AssignContactCategoryAction: NotRequired[Mapping[str, Any]]
    SendNotificationAction: NotRequired[SendNotificationActionDefinitionUnionTypeDef]
    CreateCaseAction: NotRequired[CreateCaseActionDefinitionUnionTypeDef]
    UpdateCaseAction: NotRequired[UpdateCaseActionDefinitionUnionTypeDef]
    AssignSlaAction: NotRequired[AssignSlaActionDefinitionUnionTypeDef]
    EndAssociatedTasksAction: NotRequired[Mapping[str, Any]]
    SubmitAutoEvaluationAction: NotRequired[SubmitAutoEvaluationActionDefinitionTypeDef]

class EvaluationFormMultiSelectQuestionPropertiesTypeDef(TypedDict):
    Options: Sequence[EvaluationFormMultiSelectQuestionOptionTypeDef]
    DisplayAs: NotRequired[EvaluationFormMultiSelectQuestionDisplayModeType]
    Automation: NotRequired[EvaluationFormMultiSelectQuestionAutomationUnionTypeDef]

OutboundStrategyConfigUnionTypeDef = Union[
    OutboundStrategyConfigTypeDef, OutboundStrategyConfigOutputTypeDef
]

class ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef(TypedDict):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchContactsResponseTypeDef(TypedDict):
    Contacts: List[ContactSearchSummaryTypeDef]
    TotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeContactResponseTypeDef(TypedDict):
    Contact: ContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactsResponsePaginatorTypeDef(TypedDict):
    Contacts: List[ContactSearchSummaryPaginatorTypeDef]
    TotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ExpressionUnionTypeDef = Union[ExpressionTypeDef, ExpressionOutputTypeDef]

class EvaluationFormItemEnablementConfigurationTypeDef(TypedDict):
    Condition: EvaluationFormItemEnablementConditionUnionTypeDef
    Action: EvaluationFormItemEnablementActionType
    DefaultAction: NotRequired[EvaluationFormItemEnablementActionType]

class EvaluationFormContentTypeDef(TypedDict):
    EvaluationFormVersion: int
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Items: List[EvaluationFormItemOutputTypeDef]
    Description: NotRequired[str]
    ScoringStrategy: NotRequired[EvaluationFormScoringStrategyTypeDef]
    AutoEvaluationConfiguration: NotRequired[EvaluationFormAutoEvaluationConfigurationTypeDef]
    TargetConfiguration: NotRequired[EvaluationFormTargetConfigurationTypeDef]
    LanguageConfiguration: NotRequired[EvaluationFormLanguageConfigurationTypeDef]

class EvaluationFormTypeDef(TypedDict):
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    EvaluationFormArn: str
    Title: str
    Status: EvaluationFormVersionStatusType
    Items: List[EvaluationFormItemOutputTypeDef]
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    Description: NotRequired[str]
    ScoringStrategy: NotRequired[EvaluationFormScoringStrategyTypeDef]
    AutoEvaluationConfiguration: NotRequired[EvaluationFormAutoEvaluationConfigurationTypeDef]
    Tags: NotRequired[Dict[str, str]]
    TargetConfiguration: NotRequired[EvaluationFormTargetConfigurationTypeDef]
    LanguageConfiguration: NotRequired[EvaluationFormLanguageConfigurationTypeDef]

class EvaluationTypeDef(TypedDict):
    EvaluationId: str
    EvaluationArn: str
    Metadata: EvaluationMetadataTypeDef
    Answers: Dict[str, EvaluationAnswerOutputTypeDef]
    Notes: Dict[str, EvaluationNoteTypeDef]
    Status: EvaluationStatusType
    CreatedTime: datetime
    LastModifiedTime: datetime
    Scores: NotRequired[Dict[str, EvaluationScoreTypeDef]]
    EvaluationType: NotRequired[EvaluationTypeType]
    Tags: NotRequired[Dict[str, str]]

RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]
EvaluationFormMultiSelectQuestionPropertiesUnionTypeDef = Union[
    EvaluationFormMultiSelectQuestionPropertiesTypeDef,
    EvaluationFormMultiSelectQuestionPropertiesOutputTypeDef,
]
OutboundStrategyTypeDef = TypedDict(
    "OutboundStrategyTypeDef",
    {
        "Type": Literal["AGENT_FIRST"],
        "Config": NotRequired[OutboundStrategyConfigUnionTypeDef],
    },
)

class RoutingCriteriaInputStepTypeDef(TypedDict):
    Expiry: NotRequired[RoutingCriteriaInputStepExpiryTypeDef]
    Expression: NotRequired[ExpressionUnionTypeDef]

EvaluationFormItemEnablementConfigurationUnionTypeDef = Union[
    EvaluationFormItemEnablementConfigurationTypeDef,
    EvaluationFormItemEnablementConfigurationOutputTypeDef,
]

class DescribeEvaluationFormResponseTypeDef(TypedDict):
    EvaluationForm: EvaluationFormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContactEvaluationResponseTypeDef(TypedDict):
    Evaluation: EvaluationTypeDef
    EvaluationForm: EvaluationFormContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestTypeDef(TypedDict):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType
    ClientToken: NotRequired[str]

class UpdateRuleRequestTypeDef(TypedDict):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType

EvaluationFormQuestionTypePropertiesTypeDef = TypedDict(
    "EvaluationFormQuestionTypePropertiesTypeDef",
    {
        "Numeric": NotRequired[EvaluationFormNumericQuestionPropertiesUnionTypeDef],
        "SingleSelect": NotRequired[EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef],
        "Text": NotRequired[EvaluationFormTextQuestionPropertiesTypeDef],
        "MultiSelect": NotRequired[EvaluationFormMultiSelectQuestionPropertiesUnionTypeDef],
    },
)
OutboundStrategyUnionTypeDef = Union[OutboundStrategyTypeDef, OutboundStrategyOutputTypeDef]

class RoutingCriteriaInputTypeDef(TypedDict):
    Steps: NotRequired[Sequence[RoutingCriteriaInputStepTypeDef]]

EvaluationFormQuestionTypePropertiesUnionTypeDef = Union[
    EvaluationFormQuestionTypePropertiesTypeDef, EvaluationFormQuestionTypePropertiesOutputTypeDef
]

class ContactDataRequestTypeDef(TypedDict):
    SystemEndpoint: NotRequired[EndpointTypeDef]
    CustomerEndpoint: NotRequired[EndpointTypeDef]
    RequestIdentifier: NotRequired[str]
    QueueId: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    Campaign: NotRequired[CampaignTypeDef]
    OutboundStrategy: NotRequired[OutboundStrategyUnionTypeDef]

class StartOutboundVoiceContactRequestTypeDef(TypedDict):
    DestinationPhoneNumber: str
    ContactFlowId: str
    InstanceId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    References: NotRequired[Mapping[str, ReferenceTypeDef]]
    RelatedContactId: NotRequired[str]
    ClientToken: NotRequired[str]
    SourcePhoneNumber: NotRequired[str]
    QueueId: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    AnswerMachineDetectionConfig: NotRequired[AnswerMachineDetectionConfigTypeDef]
    CampaignId: NotRequired[str]
    TrafficType: NotRequired[TrafficTypeType]
    OutboundStrategy: NotRequired[OutboundStrategyUnionTypeDef]
    RingTimeoutInSeconds: NotRequired[int]

class UpdateContactRoutingDataRequestTypeDef(TypedDict):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: NotRequired[int]
    QueuePriority: NotRequired[int]
    RoutingCriteria: NotRequired[RoutingCriteriaInputTypeDef]

class EvaluationFormQuestionTypeDef(TypedDict):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: NotRequired[str]
    NotApplicableEnabled: NotRequired[bool]
    QuestionTypeProperties: NotRequired[EvaluationFormQuestionTypePropertiesUnionTypeDef]
    Enablement: NotRequired[EvaluationFormItemEnablementConfigurationUnionTypeDef]
    Weight: NotRequired[float]

class BatchPutContactRequestTypeDef(TypedDict):
    InstanceId: str
    ContactDataRequestList: Sequence[ContactDataRequestTypeDef]
    ClientToken: NotRequired[str]

EvaluationFormQuestionUnionTypeDef = Union[
    EvaluationFormQuestionTypeDef, EvaluationFormQuestionOutputTypeDef
]

class EvaluationFormItemTypeDef(TypedDict):
    Section: NotRequired[EvaluationFormSectionUnionTypeDef]
    Question: NotRequired[EvaluationFormQuestionUnionTypeDef]

EvaluationFormItemUnionTypeDef = Union[EvaluationFormItemTypeDef, EvaluationFormItemOutputTypeDef]

class CreateEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    Description: NotRequired[str]
    ScoringStrategy: NotRequired[EvaluationFormScoringStrategyTypeDef]
    AutoEvaluationConfiguration: NotRequired[EvaluationFormAutoEvaluationConfigurationTypeDef]
    ClientToken: NotRequired[str]
    AsDraft: NotRequired[bool]
    Tags: NotRequired[Mapping[str, str]]
    TargetConfiguration: NotRequired[EvaluationFormTargetConfigurationTypeDef]
    LanguageConfiguration: NotRequired[EvaluationFormLanguageConfigurationTypeDef]

class UpdateEvaluationFormRequestTypeDef(TypedDict):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    CreateNewVersion: NotRequired[bool]
    Description: NotRequired[str]
    ScoringStrategy: NotRequired[EvaluationFormScoringStrategyTypeDef]
    AutoEvaluationConfiguration: NotRequired[EvaluationFormAutoEvaluationConfigurationTypeDef]
    AsDraft: NotRequired[bool]
    ClientToken: NotRequired[str]
    TargetConfiguration: NotRequired[EvaluationFormTargetConfigurationTypeDef]
    LanguageConfiguration: NotRequired[EvaluationFormLanguageConfigurationTypeDef]
