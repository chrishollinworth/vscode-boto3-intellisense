"""
Type annotations for pinpoint-sms-voice-v2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/literals.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice_v2.literals import AccountAttributeNameType

    data: AccountAttributeNameType = "ACCOUNT_TIER"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountAttributeNameType",
    "AccountLimitNameType",
    "AttachmentStatusType",
    "AttachmentUploadErrorReasonType",
    "ConfigurationSetFilterNameType",
    "DescribeAccountAttributesPaginatorName",
    "DescribeAccountLimitsPaginatorName",
    "DescribeConfigurationSetsPaginatorName",
    "DescribeKeywordsPaginatorName",
    "DescribeOptOutListsPaginatorName",
    "DescribeOptedOutNumbersPaginatorName",
    "DescribePhoneNumbersPaginatorName",
    "DescribePoolsPaginatorName",
    "DescribeProtectConfigurationsPaginatorName",
    "DescribeRegistrationAttachmentsPaginatorName",
    "DescribeRegistrationFieldDefinitionsPaginatorName",
    "DescribeRegistrationFieldValuesPaginatorName",
    "DescribeRegistrationSectionDefinitionsPaginatorName",
    "DescribeRegistrationTypeDefinitionsPaginatorName",
    "DescribeRegistrationVersionsPaginatorName",
    "DescribeRegistrationsPaginatorName",
    "DescribeSenderIdsPaginatorName",
    "DescribeSpendLimitsPaginatorName",
    "DescribeVerifiedDestinationNumbersPaginatorName",
    "DestinationCountryParameterKeyType",
    "EventTypeType",
    "FieldRequirementType",
    "FieldTypeType",
    "KeywordActionType",
    "KeywordFilterNameType",
    "LanguageCodeType",
    "ListPoolOriginationIdentitiesPaginatorName",
    "ListRegistrationAssociationsPaginatorName",
    "MessageTypeType",
    "NumberCapabilityType",
    "NumberStatusType",
    "NumberTypeType",
    "OptedOutFilterNameType",
    "PhoneNumberFilterNameType",
    "PoolFilterNameType",
    "PoolOriginationIdentitiesFilterNameType",
    "PoolStatusType",
    "ProtectConfigurationFilterNameType",
    "ProtectStatusType",
    "RegistrationAssociationBehaviorType",
    "RegistrationAssociationFilterNameType",
    "RegistrationAttachmentFilterNameType",
    "RegistrationDisassociationBehaviorType",
    "RegistrationFilterNameType",
    "RegistrationStatusType",
    "RegistrationTypeFilterNameType",
    "RegistrationVersionFilterNameType",
    "RegistrationVersionStatusType",
    "RequestableNumberTypeType",
    "SenderIdFilterNameType",
    "SpendLimitNameType",
    "VerificationChannelType",
    "VerificationStatusType",
    "VerifiedDestinationNumberFilterNameType",
    "VoiceIdType",
    "VoiceMessageBodyTextTypeType",
)

AccountAttributeNameType = Literal["ACCOUNT_TIER", "DEFAULT_PROTECT_CONFIGURATION_ID"]
AccountLimitNameType = Literal[
    "CONFIGURATION_SETS",
    "OPT_OUT_LISTS",
    "PHONE_NUMBERS",
    "POOLS",
    "REGISTRATIONS",
    "REGISTRATION_ATTACHMENTS",
    "SENDER_IDS",
    "VERIFIED_DESTINATION_NUMBERS",
]
AttachmentStatusType = Literal["DELETED", "UPLOAD_COMPLETE", "UPLOAD_FAILED", "UPLOAD_IN_PROGRESS"]
AttachmentUploadErrorReasonType = Literal["INTERNAL_ERROR"]
ConfigurationSetFilterNameType = Literal[
    "default-message-type",
    "default-sender-id",
    "event-destination-name",
    "matching-event-types",
    "protect-configuration-id",
]
DescribeAccountAttributesPaginatorName = Literal["describe_account_attributes"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeConfigurationSetsPaginatorName = Literal["describe_configuration_sets"]
DescribeKeywordsPaginatorName = Literal["describe_keywords"]
DescribeOptOutListsPaginatorName = Literal["describe_opt_out_lists"]
DescribeOptedOutNumbersPaginatorName = Literal["describe_opted_out_numbers"]
DescribePhoneNumbersPaginatorName = Literal["describe_phone_numbers"]
DescribePoolsPaginatorName = Literal["describe_pools"]
DescribeProtectConfigurationsPaginatorName = Literal["describe_protect_configurations"]
DescribeRegistrationAttachmentsPaginatorName = Literal["describe_registration_attachments"]
DescribeRegistrationFieldDefinitionsPaginatorName = Literal[
    "describe_registration_field_definitions"
]
DescribeRegistrationFieldValuesPaginatorName = Literal["describe_registration_field_values"]
DescribeRegistrationSectionDefinitionsPaginatorName = Literal[
    "describe_registration_section_definitions"
]
DescribeRegistrationTypeDefinitionsPaginatorName = Literal["describe_registration_type_definitions"]
DescribeRegistrationVersionsPaginatorName = Literal["describe_registration_versions"]
DescribeRegistrationsPaginatorName = Literal["describe_registrations"]
DescribeSenderIdsPaginatorName = Literal["describe_sender_ids"]
DescribeSpendLimitsPaginatorName = Literal["describe_spend_limits"]
DescribeVerifiedDestinationNumbersPaginatorName = Literal["describe_verified_destination_numbers"]
DestinationCountryParameterKeyType = Literal["IN_ENTITY_ID", "IN_TEMPLATE_ID"]
EventTypeType = Literal[
    "ALL",
    "MEDIA_ALL",
    "MEDIA_BLOCKED",
    "MEDIA_CARRIER_BLOCKED",
    "MEDIA_CARRIER_UNREACHABLE",
    "MEDIA_DELIVERED",
    "MEDIA_FILE_INACCESSIBLE",
    "MEDIA_FILE_SIZE_EXCEEDED",
    "MEDIA_FILE_TYPE_UNSUPPORTED",
    "MEDIA_INVALID",
    "MEDIA_INVALID_MESSAGE",
    "MEDIA_PENDING",
    "MEDIA_QUEUED",
    "MEDIA_SPAM",
    "MEDIA_SUCCESSFUL",
    "MEDIA_TTL_EXPIRED",
    "MEDIA_UNKNOWN",
    "MEDIA_UNREACHABLE",
    "TEXT_ALL",
    "TEXT_BLOCKED",
    "TEXT_CARRIER_BLOCKED",
    "TEXT_CARRIER_UNREACHABLE",
    "TEXT_DELIVERED",
    "TEXT_INVALID",
    "TEXT_INVALID_MESSAGE",
    "TEXT_PENDING",
    "TEXT_QUEUED",
    "TEXT_SENT",
    "TEXT_SPAM",
    "TEXT_SUCCESSFUL",
    "TEXT_TTL_EXPIRED",
    "TEXT_UNKNOWN",
    "TEXT_UNREACHABLE",
    "VOICE_ALL",
    "VOICE_ANSWERED",
    "VOICE_BUSY",
    "VOICE_COMPLETED",
    "VOICE_FAILED",
    "VOICE_INITIATED",
    "VOICE_NO_ANSWER",
    "VOICE_RINGING",
    "VOICE_TTL_EXPIRED",
]
FieldRequirementType = Literal["CONDITIONAL", "OPTIONAL", "REQUIRED"]
FieldTypeType = Literal["ATTACHMENT", "SELECT", "TEXT"]
KeywordActionType = Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"]
KeywordFilterNameType = Literal["keyword-action"]
LanguageCodeType = Literal[
    "DE_DE",
    "EN_GB",
    "EN_US",
    "ES_419",
    "ES_ES",
    "FR_CA",
    "FR_FR",
    "IT_IT",
    "JA_JP",
    "KO_KR",
    "PT_BR",
    "ZH_CN",
    "ZH_TW",
]
ListPoolOriginationIdentitiesPaginatorName = Literal["list_pool_origination_identities"]
ListRegistrationAssociationsPaginatorName = Literal["list_registration_associations"]
MessageTypeType = Literal["PROMOTIONAL", "TRANSACTIONAL"]
NumberCapabilityType = Literal["MMS", "SMS", "VOICE"]
NumberStatusType = Literal["ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"]
NumberTypeType = Literal["LONG_CODE", "SHORT_CODE", "SIMULATOR", "TEN_DLC", "TOLL_FREE"]
OptedOutFilterNameType = Literal["end-user-opted-out"]
PhoneNumberFilterNameType = Literal[
    "deletion-protection-enabled",
    "iso-country-code",
    "message-type",
    "number-capability",
    "number-type",
    "opt-out-list-name",
    "self-managed-opt-outs-enabled",
    "status",
    "two-way-channel-arn",
    "two-way-enabled",
]
PoolFilterNameType = Literal[
    "deletion-protection-enabled",
    "message-type",
    "opt-out-list-name",
    "self-managed-opt-outs-enabled",
    "shared-routes-enabled",
    "status",
    "two-way-channel-arn",
    "two-way-enabled",
]
PoolOriginationIdentitiesFilterNameType = Literal["iso-country-code", "number-capability"]
PoolStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
ProtectConfigurationFilterNameType = Literal["account-default", "deletion-protection-enabled"]
ProtectStatusType = Literal["ALLOW", "BLOCK"]
RegistrationAssociationBehaviorType = Literal[
    "ASSOCIATE_AFTER_COMPLETE", "ASSOCIATE_BEFORE_SUBMIT", "ASSOCIATE_ON_APPROVAL"
]
RegistrationAssociationFilterNameType = Literal["iso-country-code", "resource-type"]
RegistrationAttachmentFilterNameType = Literal["attachment-status"]
RegistrationDisassociationBehaviorType = Literal[
    "DELETE_REGISTRATION_DISASSOCIATES",
    "DISASSOCIATE_ALL_ALLOWS_DELETE_REGISTRATION",
    "DISASSOCIATE_ALL_CLOSES_REGISTRATION",
]
RegistrationFilterNameType = Literal["registration-status", "registration-type"]
RegistrationStatusType = Literal[
    "CLOSED",
    "COMPLETE",
    "CREATED",
    "DELETED",
    "PROVISIONING",
    "REQUIRES_UPDATES",
    "REVIEWING",
    "SUBMITTED",
]
RegistrationTypeFilterNameType = Literal[
    "supported-association-iso-country-code", "supported-association-resource-type"
]
RegistrationVersionFilterNameType = Literal["registration-version-status"]
RegistrationVersionStatusType = Literal[
    "APPROVED", "ARCHIVED", "DENIED", "DISCARDED", "DRAFT", "REVIEWING", "REVOKED", "SUBMITTED"
]
RequestableNumberTypeType = Literal["LONG_CODE", "SIMULATOR", "TEN_DLC", "TOLL_FREE"]
SenderIdFilterNameType = Literal[
    "deletion-protection-enabled", "iso-country-code", "message-type", "registered", "sender-id"
]
SpendLimitNameType = Literal[
    "MEDIA_MESSAGE_MONTHLY_SPEND_LIMIT",
    "TEXT_MESSAGE_MONTHLY_SPEND_LIMIT",
    "VOICE_MESSAGE_MONTHLY_SPEND_LIMIT",
]
VerificationChannelType = Literal["TEXT", "VOICE"]
VerificationStatusType = Literal["PENDING", "VERIFIED"]
VerifiedDestinationNumberFilterNameType = Literal["status"]
VoiceIdType = Literal[
    "AMY",
    "ASTRID",
    "BIANCA",
    "BRIAN",
    "CAMILA",
    "CARLA",
    "CARMEN",
    "CELINE",
    "CHANTAL",
    "CONCHITA",
    "CRISTIANO",
    "DORA",
    "EMMA",
    "ENRIQUE",
    "EWA",
    "FILIZ",
    "GERAINT",
    "GIORGIO",
    "GWYNETH",
    "HANS",
    "INES",
    "IVY",
    "JACEK",
    "JAN",
    "JOANNA",
    "JOEY",
    "JUSTIN",
    "KARL",
    "KENDRA",
    "KIMBERLY",
    "LEA",
    "LIV",
    "LOTTE",
    "LUCIA",
    "LUPE",
    "MADS",
    "MAJA",
    "MARLENE",
    "MATHIEU",
    "MATTHEW",
    "MAXIM",
    "MIA",
    "MIGUEL",
    "MIZUKI",
    "NAJA",
    "NICOLE",
    "PENELOPE",
    "RAVEENA",
    "RICARDO",
    "RUBEN",
    "RUSSELL",
    "SALLI",
    "SEOYEON",
    "TAKUMI",
    "TATYANA",
    "VICKI",
    "VITORIA",
    "ZEINA",
    "ZHIYU",
]
VoiceMessageBodyTextTypeType = Literal["SSML", "TEXT"]
