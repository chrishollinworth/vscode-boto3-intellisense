"""
Type annotations for connect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/literals.html)

Usage::

    ```python
    from mypy_boto3_connect.literals import AgentStatusStateType

    data: AgentStatusStateType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentStatusStateType",
    "AgentStatusTypeType",
    "ChannelType",
    "ComparisonType",
    "ContactFlowTypeType",
    "ContactInitiationMethodType",
    "CurrentMetricNameType",
    "DirectoryTypeType",
    "EncryptionTypeType",
    "GetMetricDataPaginatorName",
    "GroupingType",
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
    "ListContactFlowsPaginatorName",
    "ListContactReferencesPaginatorName",
    "ListHoursOfOperationsPaginatorName",
    "ListInstanceAttributesPaginatorName",
    "ListInstanceStorageConfigsPaginatorName",
    "ListInstancesPaginatorName",
    "ListIntegrationAssociationsPaginatorName",
    "ListLambdaFunctionsPaginatorName",
    "ListLexBotsPaginatorName",
    "ListPhoneNumbersPaginatorName",
    "ListPromptsPaginatorName",
    "ListQueueQuickConnectsPaginatorName",
    "ListQueuesPaginatorName",
    "ListQuickConnectsPaginatorName",
    "ListRoutingProfileQueuesPaginatorName",
    "ListRoutingProfilesPaginatorName",
    "ListSecurityKeysPaginatorName",
    "ListSecurityProfilePermissionsPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListUseCasesPaginatorName",
    "ListUserHierarchyGroupsPaginatorName",
    "ListUsersPaginatorName",
    "PhoneNumberCountryCodeType",
    "PhoneNumberTypeType",
    "PhoneTypeType",
    "QueueStatusType",
    "QueueTypeType",
    "QuickConnectTypeType",
    "ReferenceStatusType",
    "ReferenceTypeType",
    "SourceTypeType",
    "StatisticType",
    "StorageTypeType",
    "TrafficTypeType",
    "UnitType",
    "UseCaseTypeType",
    "VoiceRecordingTrackType",
)

AgentStatusStateType = Literal["DISABLED", "ENABLED"]
AgentStatusTypeType = Literal["CUSTOM", "OFFLINE", "ROUTABLE"]
ChannelType = Literal["CHAT", "TASK", "VOICE"]
ComparisonType = Literal["LT"]
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
    "API", "CALLBACK", "INBOUND", "OUTBOUND", "QUEUE_TRANSFER", "TRANSFER"
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
GetMetricDataPaginatorName = Literal["get_metric_data"]
GroupingType = Literal["CHANNEL", "QUEUE"]
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
    "INBOUND_CALLS",
    "OUTBOUND_CALLS",
    "USE_CUSTOM_TTS_VOICES",
]
InstanceStatusType = Literal["ACTIVE", "CREATION_FAILED", "CREATION_IN_PROGRESS"]
InstanceStorageResourceTypeType = Literal[
    "AGENT_EVENTS",
    "CALL_RECORDINGS",
    "CHAT_TRANSCRIPTS",
    "CONTACT_TRACE_RECORDS",
    "MEDIA_STREAMS",
    "SCHEDULED_REPORTS",
]
IntegrationTypeType = Literal[
    "EVENT", "PINPOINT_APP", "VOICE_ID", "WISDOM_ASSISTANT", "WISDOM_KNOWLEDGE_BASE"
]
LexVersionType = Literal["V1", "V2"]
ListAgentStatusesPaginatorName = Literal["list_agent_statuses"]
ListApprovedOriginsPaginatorName = Literal["list_approved_origins"]
ListBotsPaginatorName = Literal["list_bots"]
ListContactFlowsPaginatorName = Literal["list_contact_flows"]
ListContactReferencesPaginatorName = Literal["list_contact_references"]
ListHoursOfOperationsPaginatorName = Literal["list_hours_of_operations"]
ListInstanceAttributesPaginatorName = Literal["list_instance_attributes"]
ListInstanceStorageConfigsPaginatorName = Literal["list_instance_storage_configs"]
ListInstancesPaginatorName = Literal["list_instances"]
ListIntegrationAssociationsPaginatorName = Literal["list_integration_associations"]
ListLambdaFunctionsPaginatorName = Literal["list_lambda_functions"]
ListLexBotsPaginatorName = Literal["list_lex_bots"]
ListPhoneNumbersPaginatorName = Literal["list_phone_numbers"]
ListPromptsPaginatorName = Literal["list_prompts"]
ListQueueQuickConnectsPaginatorName = Literal["list_queue_quick_connects"]
ListQueuesPaginatorName = Literal["list_queues"]
ListQuickConnectsPaginatorName = Literal["list_quick_connects"]
ListRoutingProfileQueuesPaginatorName = Literal["list_routing_profile_queues"]
ListRoutingProfilesPaginatorName = Literal["list_routing_profiles"]
ListSecurityKeysPaginatorName = Literal["list_security_keys"]
ListSecurityProfilePermissionsPaginatorName = Literal["list_security_profile_permissions"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListUseCasesPaginatorName = Literal["list_use_cases"]
ListUserHierarchyGroupsPaginatorName = Literal["list_user_hierarchy_groups"]
ListUsersPaginatorName = Literal["list_users"]
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
PhoneTypeType = Literal["DESK_PHONE", "SOFT_PHONE"]
QueueStatusType = Literal["DISABLED", "ENABLED"]
QueueTypeType = Literal["AGENT", "STANDARD"]
QuickConnectTypeType = Literal["PHONE_NUMBER", "QUEUE", "USER"]
ReferenceStatusType = Literal["APPROVED", "REJECTED"]
ReferenceTypeType = Literal["ATTACHMENT", "URL"]
SourceTypeType = Literal["SALESFORCE", "ZENDESK"]
StatisticType = Literal["AVG", "MAX", "SUM"]
StorageTypeType = Literal["KINESIS_FIREHOSE", "KINESIS_STREAM", "KINESIS_VIDEO_STREAM", "S3"]
TrafficTypeType = Literal["CAMPAIGN", "GENERAL"]
UnitType = Literal["COUNT", "PERCENT", "SECONDS"]
UseCaseTypeType = Literal["CONNECT_CAMPAIGNS", "RULES_EVALUATION"]
VoiceRecordingTrackType = Literal["ALL", "FROM_AGENT", "TO_AGENT"]
