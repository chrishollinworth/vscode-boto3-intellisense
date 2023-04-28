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
    "AgentStatusStateType",
    "AgentStatusTypeType",
    "BehaviorTypeType",
    "ChannelType",
    "ComparisonType",
    "ContactFlowModuleStateType",
    "ContactFlowModuleStatusType",
    "ContactFlowStateType",
    "ContactFlowTypeType",
    "ContactInitiationMethodType",
    "ContactStateType",
    "CurrentMetricNameType",
    "DirectoryTypeType",
    "EncryptionTypeType",
    "EvaluationFormQuestionTypeType",
    "EvaluationFormScoringModeType",
    "EvaluationFormScoringStatusType",
    "EvaluationFormSingleSelectQuestionDisplayModeType",
    "EvaluationFormVersionStatusType",
    "EvaluationStatusType",
    "EventSourceNameType",
    "GetMetricDataPaginatorName",
    "GroupingType",
    "HierarchyGroupMatchTypeType",
    "HistoricalMetricNameType",
    "HoursOfOperationDaysType",
    "InstanceAttributeTypeType",
    "InstanceStatusType",
    "InstanceStorageResourceTypeType",
    "IntegrationTypeType",
    "LexVersionType",
    "ListAgentStatusesPaginatorName",
    "ListApprovedOriginsPaginatorName",
    "ListBotsPaginatorName",
    "ListContactEvaluationsPaginatorName",
    "ListContactFlowModulesPaginatorName",
    "ListContactFlowsPaginatorName",
    "ListContactReferencesPaginatorName",
    "ListDefaultVocabulariesPaginatorName",
    "ListEvaluationFormVersionsPaginatorName",
    "ListEvaluationFormsPaginatorName",
    "ListHoursOfOperationsPaginatorName",
    "ListInstanceAttributesPaginatorName",
    "ListInstanceStorageConfigsPaginatorName",
    "ListInstancesPaginatorName",
    "ListIntegrationAssociationsPaginatorName",
    "ListLambdaFunctionsPaginatorName",
    "ListLexBotsPaginatorName",
    "ListPhoneNumbersPaginatorName",
    "ListPhoneNumbersV2PaginatorName",
    "ListPromptsPaginatorName",
    "ListQueueQuickConnectsPaginatorName",
    "ListQueuesPaginatorName",
    "ListQuickConnectsPaginatorName",
    "ListRoutingProfileQueuesPaginatorName",
    "ListRoutingProfilesPaginatorName",
    "ListRulesPaginatorName",
    "ListSecurityKeysPaginatorName",
    "ListSecurityProfilePermissionsPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListTaskTemplatesPaginatorName",
    "ListTrafficDistributionGroupsPaginatorName",
    "ListUseCasesPaginatorName",
    "ListUserHierarchyGroupsPaginatorName",
    "ListUsersPaginatorName",
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
    "ReferenceStatusType",
    "ReferenceTypeType",
    "RehydrationTypeType",
    "RulePublishStatusType",
    "SearchAvailablePhoneNumbersPaginatorName",
    "SearchQueuesPaginatorName",
    "SearchRoutingProfilesPaginatorName",
    "SearchSecurityProfilesPaginatorName",
    "SearchUsersPaginatorName",
    "SearchVocabulariesPaginatorName",
    "SearchableQueueTypeType",
    "SingleSelectQuestionRuleCategoryAutomationConditionType",
    "SortOrderType",
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
    "VocabularyLanguageCodeType",
    "VocabularyStateType",
    "VoiceRecordingTrackType",
)

ActionTypeType = Literal[
    "ASSIGN_CONTACT_CATEGORY", "CREATE_TASK", "GENERATE_EVENTBRIDGE_EVENT", "SEND_NOTIFICATION"
]
AgentStatusStateType = Literal["DISABLED", "ENABLED"]
AgentStatusTypeType = Literal["CUSTOM", "OFFLINE", "ROUTABLE"]
BehaviorTypeType = Literal["ROUTE_ANY_CHANNEL", "ROUTE_CURRENT_CHANNEL_ONLY"]
ChannelType = Literal["CHAT", "TASK", "VOICE"]
ComparisonType = Literal["LT"]
ContactFlowModuleStateType = Literal["ACTIVE", "ARCHIVED"]
ContactFlowModuleStatusType = Literal["PUBLISHED", "SAVED"]
ContactFlowStateType = Literal["ACTIVE", "ARCHIVED"]
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
    "API", "CALLBACK", "DISCONNECT", "INBOUND", "MONITOR", "OUTBOUND", "QUEUE_TRANSFER", "TRANSFER"
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
EvaluationFormQuestionTypeType = Literal["NUMERIC", "SINGLESELECT", "TEXT"]
EvaluationFormScoringModeType = Literal["QUESTION_ONLY", "SECTION_ONLY"]
EvaluationFormScoringStatusType = Literal["DISABLED", "ENABLED"]
EvaluationFormSingleSelectQuestionDisplayModeType = Literal["DROPDOWN", "RADIO"]
EvaluationFormVersionStatusType = Literal["ACTIVE", "DRAFT"]
EvaluationStatusType = Literal["DRAFT", "SUBMITTED"]
EventSourceNameType = Literal[
    "OnPostCallAnalysisAvailable",
    "OnPostChatAnalysisAvailable",
    "OnRealTimeCallAnalysisAvailable",
    "OnSalesforceCaseCreate",
    "OnZendeskTicketCreate",
    "OnZendeskTicketStatusUpdate",
]
GetMetricDataPaginatorName = Literal["get_metric_data"]
GroupingType = Literal["CHANNEL", "QUEUE", "ROUTING_PROFILE"]
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
    "REAL_TIME_CONTACT_ANALYSIS_SEGMENTS",
    "SCHEDULED_REPORTS",
]
IntegrationTypeType = Literal[
    "CASES_DOMAIN", "EVENT", "PINPOINT_APP", "VOICE_ID", "WISDOM_ASSISTANT", "WISDOM_KNOWLEDGE_BASE"
]
LexVersionType = Literal["V1", "V2"]
ListAgentStatusesPaginatorName = Literal["list_agent_statuses"]
ListApprovedOriginsPaginatorName = Literal["list_approved_origins"]
ListBotsPaginatorName = Literal["list_bots"]
ListContactEvaluationsPaginatorName = Literal["list_contact_evaluations"]
ListContactFlowModulesPaginatorName = Literal["list_contact_flow_modules"]
ListContactFlowsPaginatorName = Literal["list_contact_flows"]
ListContactReferencesPaginatorName = Literal["list_contact_references"]
ListDefaultVocabulariesPaginatorName = Literal["list_default_vocabularies"]
ListEvaluationFormVersionsPaginatorName = Literal["list_evaluation_form_versions"]
ListEvaluationFormsPaginatorName = Literal["list_evaluation_forms"]
ListHoursOfOperationsPaginatorName = Literal["list_hours_of_operations"]
ListInstanceAttributesPaginatorName = Literal["list_instance_attributes"]
ListInstanceStorageConfigsPaginatorName = Literal["list_instance_storage_configs"]
ListInstancesPaginatorName = Literal["list_instances"]
ListIntegrationAssociationsPaginatorName = Literal["list_integration_associations"]
ListLambdaFunctionsPaginatorName = Literal["list_lambda_functions"]
ListLexBotsPaginatorName = Literal["list_lex_bots"]
ListPhoneNumbersPaginatorName = Literal["list_phone_numbers"]
ListPhoneNumbersV2PaginatorName = Literal["list_phone_numbers_v2"]
ListPromptsPaginatorName = Literal["list_prompts"]
ListQueueQuickConnectsPaginatorName = Literal["list_queue_quick_connects"]
ListQueuesPaginatorName = Literal["list_queues"]
ListQuickConnectsPaginatorName = Literal["list_quick_connects"]
ListRoutingProfileQueuesPaginatorName = Literal["list_routing_profile_queues"]
ListRoutingProfilesPaginatorName = Literal["list_routing_profiles"]
ListRulesPaginatorName = Literal["list_rules"]
ListSecurityKeysPaginatorName = Literal["list_security_keys"]
ListSecurityProfilePermissionsPaginatorName = Literal["list_security_profile_permissions"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListTaskTemplatesPaginatorName = Literal["list_task_templates"]
ListTrafficDistributionGroupsPaginatorName = Literal["list_traffic_distribution_groups"]
ListUseCasesPaginatorName = Literal["list_use_cases"]
ListUserHierarchyGroupsPaginatorName = Literal["list_user_hierarchy_groups"]
ListUsersPaginatorName = Literal["list_users"]
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
ParticipantRoleType = Literal["AGENT", "CUSTOMER", "CUSTOM_BOT", "SYSTEM"]
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
PhoneNumberTypeType = Literal["DID", "TOLL_FREE"]
PhoneNumberWorkflowStatusType = Literal["CLAIMED", "FAILED", "IN_PROGRESS"]
PhoneTypeType = Literal["DESK_PHONE", "SOFT_PHONE"]
QueueStatusType = Literal["DISABLED", "ENABLED"]
QueueTypeType = Literal["AGENT", "STANDARD"]
QuickConnectTypeType = Literal["PHONE_NUMBER", "QUEUE", "USER"]
ReferenceStatusType = Literal["APPROVED", "REJECTED"]
ReferenceTypeType = Literal["ATTACHMENT", "DATE", "EMAIL", "NUMBER", "STRING", "URL"]
RehydrationTypeType = Literal["ENTIRE_PAST_SESSION", "FROM_SEGMENT"]
RulePublishStatusType = Literal["DRAFT", "PUBLISHED"]
SearchAvailablePhoneNumbersPaginatorName = Literal["search_available_phone_numbers"]
SearchQueuesPaginatorName = Literal["search_queues"]
SearchRoutingProfilesPaginatorName = Literal["search_routing_profiles"]
SearchSecurityProfilesPaginatorName = Literal["search_security_profiles"]
SearchUsersPaginatorName = Literal["search_users"]
SearchVocabulariesPaginatorName = Literal["search_vocabularies"]
SearchableQueueTypeType = Literal["STANDARD"]
SingleSelectQuestionRuleCategoryAutomationConditionType = Literal["NOT_PRESENT", "PRESENT"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SourceTypeType = Literal["SALESFORCE", "ZENDESK"]
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
