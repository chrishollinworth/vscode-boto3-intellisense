"""
Type annotations for connect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/literals.html)

Usage::

    ```python
    from mypy_boto3_connect.literals import ActionTypeType

    data: ActionTypeType = "ASSIGN_CONTACT_CATEGORY"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionTypeType",
    "AgentAvailabilityTimerType",
    "AgentStatusStateType",
    "AgentStatusTypeType",
    "AnsweringMachineDetectionStatusType",
    "ArtifactStatusType",
    "BehaviorTypeType",
    "ChannelType",
    "ChatEventTypeType",
    "ComparisonType",
    "ContactFlowModuleStateType",
    "ContactFlowModuleStatusType",
    "ContactFlowStateType",
    "ContactFlowStatusType",
    "ContactFlowTypeType",
    "ContactInitiationMethodType",
    "ContactStateType",
    "CurrentMetricNameType",
    "DirectoryTypeType",
    "EncryptionTypeType",
    "EndpointTypeType",
    "EvaluationFormQuestionTypeType",
    "EvaluationFormScoringModeType",
    "EvaluationFormScoringStatusType",
    "EvaluationFormSingleSelectQuestionDisplayModeType",
    "EvaluationFormVersionStatusType",
    "EvaluationStatusType",
    "EventSourceNameType",
    "FailureReasonCodeType",
    "FileStatusTypeType",
    "FileUseCaseTypeType",
    "FlowAssociationResourceTypeType",
    "GetMetricDataPaginatorName",
    "GroupingType",
    "HierarchyGroupMatchTypeType",
    "HistoricalMetricNameType",
    "HoursOfOperationDaysType",
    "InstanceAttributeTypeType",
    "InstanceStatusType",
    "InstanceStorageResourceTypeType",
    "IntegrationTypeType",
    "IntervalPeriodType",
    "LexVersionType",
    "ListAgentStatusesPaginatorName",
    "ListApprovedOriginsPaginatorName",
    "ListAuthenticationProfilesPaginatorName",
    "ListBotsPaginatorName",
    "ListContactEvaluationsPaginatorName",
    "ListContactFlowModulesPaginatorName",
    "ListContactFlowsPaginatorName",
    "ListContactReferencesPaginatorName",
    "ListDefaultVocabulariesPaginatorName",
    "ListEvaluationFormVersionsPaginatorName",
    "ListEvaluationFormsPaginatorName",
    "ListFlowAssociationResourceTypeType",
    "ListFlowAssociationsPaginatorName",
    "ListHoursOfOperationsPaginatorName",
    "ListInstanceAttributesPaginatorName",
    "ListInstanceStorageConfigsPaginatorName",
    "ListInstancesPaginatorName",
    "ListIntegrationAssociationsPaginatorName",
    "ListLambdaFunctionsPaginatorName",
    "ListLexBotsPaginatorName",
    "ListPhoneNumbersPaginatorName",
    "ListPhoneNumbersV2PaginatorName",
    "ListPredefinedAttributesPaginatorName",
    "ListPromptsPaginatorName",
    "ListQueueQuickConnectsPaginatorName",
    "ListQueuesPaginatorName",
    "ListQuickConnectsPaginatorName",
    "ListRoutingProfileQueuesPaginatorName",
    "ListRoutingProfilesPaginatorName",
    "ListRulesPaginatorName",
    "ListSecurityKeysPaginatorName",
    "ListSecurityProfileApplicationsPaginatorName",
    "ListSecurityProfilePermissionsPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListTaskTemplatesPaginatorName",
    "ListTrafficDistributionGroupUsersPaginatorName",
    "ListTrafficDistributionGroupsPaginatorName",
    "ListUseCasesPaginatorName",
    "ListUserHierarchyGroupsPaginatorName",
    "ListUserProficienciesPaginatorName",
    "ListUsersPaginatorName",
    "ListViewVersionsPaginatorName",
    "ListViewsPaginatorName",
    "MeetingFeatureStatusType",
    "MonitorCapabilityType",
    "NotificationContentTypeType",
    "NotificationDeliveryTypeType",
    "NumericQuestionPropertyAutomationLabelType",
    "ParticipantRoleType",
    "ParticipantTimerActionType",
    "ParticipantTimerTypeType",
    "PhoneNumberCountryCodeType",
    "PhoneNumberTypeType",
    "PhoneNumberWorkflowStatusType",
    "PhoneTypeType",
    "QueueStatusType",
    "QueueTypeType",
    "QuickConnectTypeType",
    "RealTimeContactAnalysisOutputTypeType",
    "RealTimeContactAnalysisSegmentTypeType",
    "RealTimeContactAnalysisSentimentLabelType",
    "RealTimeContactAnalysisStatusType",
    "RealTimeContactAnalysisSupportedChannelType",
    "ReferenceStatusType",
    "ReferenceTypeType",
    "RehydrationTypeType",
    "RoutingCriteriaStepStatusType",
    "RulePublishStatusType",
    "SearchAvailablePhoneNumbersPaginatorName",
    "SearchContactFlowModulesPaginatorName",
    "SearchContactFlowsPaginatorName",
    "SearchContactsMatchTypeType",
    "SearchContactsPaginatorName",
    "SearchContactsTimeRangeTypeType",
    "SearchHoursOfOperationsPaginatorName",
    "SearchPredefinedAttributesPaginatorName",
    "SearchPromptsPaginatorName",
    "SearchQueuesPaginatorName",
    "SearchQuickConnectsPaginatorName",
    "SearchResourceTagsPaginatorName",
    "SearchRoutingProfilesPaginatorName",
    "SearchSecurityProfilesPaginatorName",
    "SearchUsersPaginatorName",
    "SearchVocabulariesPaginatorName",
    "SearchableQueueTypeType",
    "SingleSelectQuestionRuleCategoryAutomationConditionType",
    "SortOrderType",
    "SortableFieldNameType",
    "SourceTypeType",
    "StatisticType",
    "StorageTypeType",
    "StringComparisonTypeType",
    "TaskTemplateFieldTypeType",
    "TaskTemplateStatusType",
    "TimerEligibleParticipantRolesType",
    "TrafficDistributionGroupStatusType",
    "TrafficTypeType",
    "UnitType",
    "UseCaseTypeType",
    "VideoCapabilityType",
    "ViewStatusType",
    "ViewTypeType",
    "VocabularyLanguageCodeType",
    "VocabularyStateType",
    "VoiceRecordingTrackType",
)

ActionTypeType = Literal[
    "ASSIGN_CONTACT_CATEGORY",
    "CREATE_CASE",
    "CREATE_TASK",
    "END_ASSOCIATED_TASKS",
    "GENERATE_EVENTBRIDGE_EVENT",
    "SEND_NOTIFICATION",
    "SUBMIT_AUTO_EVALUATION",
    "UPDATE_CASE",
]
AgentAvailabilityTimerType = Literal["TIME_SINCE_LAST_ACTIVITY", "TIME_SINCE_LAST_INBOUND"]
AgentStatusStateType = Literal["DISABLED", "ENABLED"]
AgentStatusTypeType = Literal["CUSTOM", "OFFLINE", "ROUTABLE"]
AnsweringMachineDetectionStatusType = Literal[
    "AMD_ERROR",
    "AMD_NOT_APPLICABLE",
    "AMD_UNANSWERED",
    "AMD_UNRESOLVED",
    "ANSWERED",
    "ERROR",
    "FAX_MACHINE_DETECTED",
    "HUMAN_ANSWERED",
    "SIT_TONE_BUSY",
    "SIT_TONE_DETECTED",
    "SIT_TONE_INVALID_NUMBER",
    "UNDETECTED",
    "VOICEMAIL_BEEP",
    "VOICEMAIL_NO_BEEP",
]
ArtifactStatusType = Literal["APPROVED", "IN_PROGRESS", "REJECTED"]
BehaviorTypeType = Literal["ROUTE_ANY_CHANNEL", "ROUTE_CURRENT_CHANNEL_ONLY"]
ChannelType = Literal["CHAT", "TASK", "VOICE"]
ChatEventTypeType = Literal["DISCONNECT", "EVENT", "MESSAGE"]
ComparisonType = Literal["LT"]
ContactFlowModuleStateType = Literal["ACTIVE", "ARCHIVED"]
ContactFlowModuleStatusType = Literal["PUBLISHED", "SAVED"]
ContactFlowStateType = Literal["ACTIVE", "ARCHIVED"]
ContactFlowStatusType = Literal["PUBLISHED", "SAVED"]
ContactFlowTypeType = Literal[
    "AGENT_HOLD",
    "AGENT_TRANSFER",
    "AGENT_WHISPER",
    "CONTACT_FLOW",
    "CUSTOMER_HOLD",
    "CUSTOMER_QUEUE",
    "CUSTOMER_WHISPER",
    "OUTBOUND_WHISPER",
    "QUEUE_TRANSFER",
]
ContactInitiationMethodType = Literal[
    "API",
    "CALLBACK",
    "DISCONNECT",
    "EXTERNAL_OUTBOUND",
    "INBOUND",
    "MONITOR",
    "OUTBOUND",
    "QUEUE_TRANSFER",
    "TRANSFER",
]
ContactStateType = Literal[
    "CONNECTED",
    "CONNECTED_ONHOLD",
    "CONNECTING",
    "ENDED",
    "ERROR",
    "INCOMING",
    "MISSED",
    "PENDING",
    "REJECTED",
]
CurrentMetricNameType = Literal[
    "AGENTS_AFTER_CONTACT_WORK",
    "AGENTS_AVAILABLE",
    "AGENTS_ERROR",
    "AGENTS_NON_PRODUCTIVE",
    "AGENTS_ONLINE",
    "AGENTS_ON_CALL",
    "AGENTS_ON_CONTACT",
    "AGENTS_STAFFED",
    "CONTACTS_IN_QUEUE",
    "CONTACTS_SCHEDULED",
    "OLDEST_CONTACT_AGE",
    "SLOTS_ACTIVE",
    "SLOTS_AVAILABLE",
]
DirectoryTypeType = Literal["CONNECT_MANAGED", "EXISTING_DIRECTORY", "SAML"]
EncryptionTypeType = Literal["KMS"]
EndpointTypeType = Literal["CONTACT_FLOW", "TELEPHONE_NUMBER", "VOIP"]
EvaluationFormQuestionTypeType = Literal["NUMERIC", "SINGLESELECT", "TEXT"]
EvaluationFormScoringModeType = Literal["QUESTION_ONLY", "SECTION_ONLY"]
EvaluationFormScoringStatusType = Literal["DISABLED", "ENABLED"]
EvaluationFormSingleSelectQuestionDisplayModeType = Literal["DROPDOWN", "RADIO"]
EvaluationFormVersionStatusType = Literal["ACTIVE", "DRAFT"]
EvaluationStatusType = Literal["DRAFT", "SUBMITTED"]
EventSourceNameType = Literal[
    "OnCaseCreate",
    "OnCaseUpdate",
    "OnContactEvaluationSubmit",
    "OnMetricDataUpdate",
    "OnPostCallAnalysisAvailable",
    "OnPostChatAnalysisAvailable",
    "OnRealTimeCallAnalysisAvailable",
    "OnRealTimeChatAnalysisAvailable",
    "OnSalesforceCaseCreate",
    "OnZendeskTicketCreate",
    "OnZendeskTicketStatusUpdate",
]
FailureReasonCodeType = Literal[
    "IDEMPOTENCY_EXCEPTION",
    "INTERNAL_ERROR",
    "INVALID_ATTRIBUTE_KEY",
    "INVALID_CUSTOMER_ENDPOINT",
    "INVALID_QUEUE",
    "INVALID_SYSTEM_ENDPOINT",
    "MISSING_CAMPAIGN",
    "MISSING_CUSTOMER_ENDPOINT",
    "MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT",
    "REQUEST_THROTTLED",
]
FileStatusTypeType = Literal["APPROVED", "FAILED", "PROCESSING", "REJECTED"]
FileUseCaseTypeType = Literal["ATTACHMENT"]
FlowAssociationResourceTypeType = Literal["SMS_PHONE_NUMBER"]
GetMetricDataPaginatorName = Literal["get_metric_data"]
GroupingType = Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE", "ROUTING_STEP_EXPRESSION"]
HierarchyGroupMatchTypeType = Literal["EXACT", "WITH_CHILD_GROUPS"]
HistoricalMetricNameType = Literal[
    "ABANDON_TIME",
    "AFTER_CONTACT_WORK_TIME",
    "API_CONTACTS_HANDLED",
    "CALLBACK_CONTACTS_HANDLED",
    "CONTACTS_ABANDONED",
    "CONTACTS_AGENT_HUNG_UP_FIRST",
    "CONTACTS_CONSULTED",
    "CONTACTS_HANDLED",
    "CONTACTS_HANDLED_INCOMING",
    "CONTACTS_HANDLED_OUTBOUND",
    "CONTACTS_HOLD_ABANDONS",
    "CONTACTS_MISSED",
    "CONTACTS_QUEUED",
    "CONTACTS_TRANSFERRED_IN",
    "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
    "CONTACTS_TRANSFERRED_OUT",
    "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
    "HANDLE_TIME",
    "HOLD_TIME",
    "INTERACTION_AND_HOLD_TIME",
    "INTERACTION_TIME",
    "OCCUPANCY",
    "QUEUED_TIME",
    "QUEUE_ANSWER_TIME",
    "SERVICE_LEVEL",
]
HoursOfOperationDaysType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
InstanceAttributeTypeType = Literal[
    "AUTO_RESOLVE_BEST_VOICES",
    "CONTACTFLOW_LOGS",
    "CONTACT_LENS",
    "EARLY_MEDIA",
    "ENHANCED_CHAT_MONITORING",
    "ENHANCED_CONTACT_MONITORING",
    "HIGH_VOLUME_OUTBOUND",
    "INBOUND_CALLS",
    "MULTI_PARTY_CONFERENCE",
    "OUTBOUND_CALLS",
    "USE_CUSTOM_TTS_VOICES",
]
InstanceStatusType = Literal["ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS"]
InstanceStorageResourceTypeType = Literal[
    "AGENT_EVENTS",
    "ATTACHMENTS",
    "CALL_RECORDINGS",
    "CHAT_TRANSCRIPTS",
    "CONTACT_EVALUATIONS",
    "CONTACT_TRACE_RECORDS",
    "MEDIA_STREAMS",
    "REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS",
    "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
    "REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS",
    "SCHEDULED_REPORTS",
    "SCREEN_RECORDINGS",
]
IntegrationTypeType = Literal[
    "APPLICATION",
    "CASES_DOMAIN",
    "EVENT",
    "FILE_SCANNER",
    "PINPOINT_APP",
    "VOICE_ID",
    "WISDOM_ASSISTANT",
    "WISDOM_KNOWLEDGE_BASE",
    "WISDOM_QUICK_RESPONSES",
]
IntervalPeriodType = Literal["DAY", "FIFTEEN_MIN", "HOUR", "THIRTY_MIN", "TOTAL", "WEEK"]
LexVersionType = Literal["V1", "V2"]
ListAgentStatusesPaginatorName = Literal["list_agent_statuses"]
ListApprovedOriginsPaginatorName = Literal["list_approved_origins"]
ListAuthenticationProfilesPaginatorName = Literal["list_authentication_profiles"]
ListBotsPaginatorName = Literal["list_bots"]
ListContactEvaluationsPaginatorName = Literal["list_contact_evaluations"]
ListContactFlowModulesPaginatorName = Literal["list_contact_flow_modules"]
ListContactFlowsPaginatorName = Literal["list_contact_flows"]
ListContactReferencesPaginatorName = Literal["list_contact_references"]
ListDefaultVocabulariesPaginatorName = Literal["list_default_vocabularies"]
ListEvaluationFormVersionsPaginatorName = Literal["list_evaluation_form_versions"]
ListEvaluationFormsPaginatorName = Literal["list_evaluation_forms"]
ListFlowAssociationResourceTypeType = Literal["VOICE_PHONE_NUMBER"]
ListFlowAssociationsPaginatorName = Literal["list_flow_associations"]
ListHoursOfOperationsPaginatorName = Literal["list_hours_of_operations"]
ListInstanceAttributesPaginatorName = Literal["list_instance_attributes"]
ListInstanceStorageConfigsPaginatorName = Literal["list_instance_storage_configs"]
ListInstancesPaginatorName = Literal["list_instances"]
ListIntegrationAssociationsPaginatorName = Literal["list_integration_associations"]
ListLambdaFunctionsPaginatorName = Literal["list_lambda_functions"]
ListLexBotsPaginatorName = Literal["list_lex_bots"]
ListPhoneNumbersPaginatorName = Literal["list_phone_numbers"]
ListPhoneNumbersV2PaginatorName = Literal["list_phone_numbers_v2"]
ListPredefinedAttributesPaginatorName = Literal["list_predefined_attributes"]
ListPromptsPaginatorName = Literal["list_prompts"]
ListQueueQuickConnectsPaginatorName = Literal["list_queue_quick_connects"]
ListQueuesPaginatorName = Literal["list_queues"]
ListQuickConnectsPaginatorName = Literal["list_quick_connects"]
ListRoutingProfileQueuesPaginatorName = Literal["list_routing_profile_queues"]
ListRoutingProfilesPaginatorName = Literal["list_routing_profiles"]
ListRulesPaginatorName = Literal["list_rules"]
ListSecurityKeysPaginatorName = Literal["list_security_keys"]
ListSecurityProfileApplicationsPaginatorName = Literal["list_security_profile_applications"]
ListSecurityProfilePermissionsPaginatorName = Literal["list_security_profile_permissions"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListTaskTemplatesPaginatorName = Literal["list_task_templates"]
ListTrafficDistributionGroupUsersPaginatorName = Literal["list_traffic_distribution_group_users"]
ListTrafficDistributionGroupsPaginatorName = Literal["list_traffic_distribution_groups"]
ListUseCasesPaginatorName = Literal["list_use_cases"]
ListUserHierarchyGroupsPaginatorName = Literal["list_user_hierarchy_groups"]
ListUserProficienciesPaginatorName = Literal["list_user_proficiencies"]
ListUsersPaginatorName = Literal["list_users"]
ListViewVersionsPaginatorName = Literal["list_view_versions"]
ListViewsPaginatorName = Literal["list_views"]
MeetingFeatureStatusType = Literal["AVAILABLE", "UNAVAILABLE"]
MonitorCapabilityType = Literal["BARGE", "SILENT_MONITOR"]
NotificationContentTypeType = Literal["PLAIN_TEXT"]
NotificationDeliveryTypeType = Literal["EMAIL"]
NumericQuestionPropertyAutomationLabelType = Literal[
    "AGENT_INTERACTION_DURATION",
    "CONTACT_DURATION",
    "CUSTOMER_HOLD_TIME",
    "NON_TALK_TIME",
    "NON_TALK_TIME_PERCENTAGE",
    "NUMBER_OF_INTERRUPTIONS",
    "OVERALL_AGENT_SENTIMENT_SCORE",
    "OVERALL_CUSTOMER_SENTIMENT_SCORE",
]
ParticipantRoleType = Literal["AGENT", "CUSTOMER", "CUSTOM_BOT", "SUPERVISOR", "SYSTEM"]
ParticipantTimerActionType = Literal["Unset"]
ParticipantTimerTypeType = Literal["DISCONNECT_NONCUSTOMER", "IDLE"]
PhoneNumberCountryCodeType = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
    "AN",
    "AO",
    "AQ",
    "AR",
    "AS",
    "AT",
    "AU",
    "AW",
    "AZ",
    "BA",
    "BB",
    "BD",
    "BE",
    "BF",
    "BG",
    "BH",
    "BI",
    "BJ",
    "BL",
    "BM",
    "BN",
    "BO",
    "BR",
    "BS",
    "BT",
    "BW",
    "BY",
    "BZ",
    "CA",
    "CC",
    "CD",
    "CF",
    "CG",
    "CH",
    "CI",
    "CK",
    "CL",
    "CM",
    "CN",
    "CO",
    "CR",
    "CU",
    "CV",
    "CW",
    "CX",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DK",
    "DM",
    "DO",
    "DZ",
    "EC",
    "EE",
    "EG",
    "EH",
    "ER",
    "ES",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FM",
    "FO",
    "FR",
    "GA",
    "GB",
    "GD",
    "GE",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GQ",
    "GR",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
    "JM",
    "JO",
    "JP",
    "KE",
    "KG",
    "KH",
    "KI",
    "KM",
    "KN",
    "KP",
    "KR",
    "KW",
    "KY",
    "KZ",
    "LA",
    "LB",
    "LC",
    "LI",
    "LK",
    "LR",
    "LS",
    "LT",
    "LU",
    "LV",
    "LY",
    "MA",
    "MC",
    "MD",
    "ME",
    "MF",
    "MG",
    "MH",
    "MK",
    "ML",
    "MM",
    "MN",
    "MO",
    "MP",
    "MR",
    "MS",
    "MT",
    "MU",
    "MV",
    "MW",
    "MX",
    "MY",
    "MZ",
    "NA",
    "NC",
    "NE",
    "NG",
    "NI",
    "NL",
    "NO",
    "NP",
    "NR",
    "NU",
    "NZ",
    "OM",
    "PA",
    "PE",
    "PF",
    "PG",
    "PH",
    "PK",
    "PL",
    "PM",
    "PN",
    "PR",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
    "RO",
    "RS",
    "RU",
    "RW",
    "SA",
    "SB",
    "SC",
    "SD",
    "SE",
    "SG",
    "SH",
    "SI",
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "US",
    "UY",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]
PhoneNumberTypeType = Literal[
    "DID", "SHARED", "SHORT_CODE", "THIRD_PARTY_DID", "THIRD_PARTY_TF", "TOLL_FREE", "UIFN"
]
PhoneNumberWorkflowStatusType = Literal["CLAIMED", "FAILED", "IN_PROGRESS"]
PhoneTypeType = Literal["DESK_PHONE", "SOFT_PHONE"]
QueueStatusType = Literal["DISABLED", "ENABLED"]
QueueTypeType = Literal["AGENT", "STANDARD"]
QuickConnectTypeType = Literal["PHONE_NUMBER", "QUEUE", "USER"]
RealTimeContactAnalysisOutputTypeType = Literal["Raw", "Redacted"]
RealTimeContactAnalysisSegmentTypeType = Literal[
    "Attachments", "Categories", "Event", "Issues", "Transcript"
]
RealTimeContactAnalysisSentimentLabelType = Literal["NEGATIVE", "NEUTRAL", "POSITIVE"]
RealTimeContactAnalysisStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
RealTimeContactAnalysisSupportedChannelType = Literal["CHAT", "VOICE"]
ReferenceStatusType = Literal["APPROVED", "REJECTED"]
ReferenceTypeType = Literal["ATTACHMENT", "DATE", "EMAIL", "NUMBER", "STRING", "URL"]
RehydrationTypeType = Literal["ENTIRE_PAST_SESSION", "FROM_SEGMENT"]
RoutingCriteriaStepStatusType = Literal["ACTIVE", "EXPIRED", "INACTIVE", "JOINED"]
RulePublishStatusType = Literal["DRAFT", "PUBLISHED"]
SearchAvailablePhoneNumbersPaginatorName = Literal["search_available_phone_numbers"]
SearchContactFlowModulesPaginatorName = Literal["search_contact_flow_modules"]
SearchContactFlowsPaginatorName = Literal["search_contact_flows"]
SearchContactsMatchTypeType = Literal["MATCH_ALL", "MATCH_ANY"]
SearchContactsPaginatorName = Literal["search_contacts"]
SearchContactsTimeRangeTypeType = Literal[
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
]
SearchHoursOfOperationsPaginatorName = Literal["search_hours_of_operations"]
SearchPredefinedAttributesPaginatorName = Literal["search_predefined_attributes"]
SearchPromptsPaginatorName = Literal["search_prompts"]
SearchQueuesPaginatorName = Literal["search_queues"]
SearchQuickConnectsPaginatorName = Literal["search_quick_connects"]
SearchResourceTagsPaginatorName = Literal["search_resource_tags"]
SearchRoutingProfilesPaginatorName = Literal["search_routing_profiles"]
SearchSecurityProfilesPaginatorName = Literal["search_security_profiles"]
SearchUsersPaginatorName = Literal["search_users"]
SearchVocabulariesPaginatorName = Literal["search_vocabularies"]
SearchableQueueTypeType = Literal["STANDARD"]
SingleSelectQuestionRuleCategoryAutomationConditionType = Literal["NOT_PRESENT", "PRESENT"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SortableFieldNameType = Literal[
    "CHANNEL",
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "INITIATION_METHOD",
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
]
SourceTypeType = Literal["CASES", "SALESFORCE", "ZENDESK"]
StatisticType = Literal["AVG", "MAX", "SUM"]
StorageTypeType = Literal["KINESIS_FIREHOSE", "KINESIS_STREAM", "KINESIS_VIDEO_STREAM", "S3"]
StringComparisonTypeType = Literal["CONTAINS", "EXACT", "STARTS_WITH"]
TaskTemplateFieldTypeType = Literal[
    "BOOLEAN",
    "DATE_TIME",
    "DESCRIPTION",
    "EMAIL",
    "NAME",
    "NUMBER",
    "QUICK_CONNECT",
    "SCHEDULED_TIME",
    "SINGLE_SELECT",
    "TEXT",
    "TEXT_AREA",
    "URL",
]
TaskTemplateStatusType = Literal["ACTIVE", "INACTIVE"]
TimerEligibleParticipantRolesType = Literal["AGENT", "CUSTOMER"]
TrafficDistributionGroupStatusType = Literal[
    "ACTIVE",
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "DELETION_FAILED",
    "PENDING_DELETION",
    "UPDATE_IN_PROGRESS",
]
TrafficTypeType = Literal["CAMPAIGN", "GENERAL"]
UnitType = Literal["COUNT", "PERCENT", "SECONDS"]
UseCaseTypeType = Literal["CONNECT_CAMPAIGNS", "RULES_EVALUATION"]
VideoCapabilityType = Literal["SEND"]
ViewStatusType = Literal["PUBLISHED", "SAVED"]
ViewTypeType = Literal["AWS_MANAGED", "CUSTOMER_MANAGED"]
VocabularyLanguageCodeType = Literal[
    "ar-AE",
    "de-CH",
    "de-DE",
    "en-AB",
    "en-AU",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-WL",
    "en-ZA",
    "es-ES",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "pt-BR",
    "pt-PT",
    "zh-CN",
]
VocabularyStateType = Literal[
    "ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS", "DELETE_IN_PROGRESS"
]
VoiceRecordingTrackType = Literal["ALL", "FROM_AGENT", "TO_AGENT"]
