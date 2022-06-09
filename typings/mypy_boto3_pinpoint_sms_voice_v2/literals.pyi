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
    "ConfigurationSetFilterNameType",
    "DescribeAccountAttributesPaginatorName",
    "DescribeAccountLimitsPaginatorName",
    "DescribeConfigurationSetsPaginatorName",
    "DescribeKeywordsPaginatorName",
    "DescribeOptOutListsPaginatorName",
    "DescribeOptedOutNumbersPaginatorName",
    "DescribePhoneNumbersPaginatorName",
    "DescribePoolsPaginatorName",
    "DescribeSenderIdsPaginatorName",
    "DescribeSpendLimitsPaginatorName",
    "DestinationCountryParameterKeyType",
    "EventTypeType",
    "KeywordActionType",
    "KeywordFilterNameType",
    "ListPoolOriginationIdentitiesPaginatorName",
    "MessageTypeType",
    "NumberCapabilityType",
    "NumberStatusType",
    "NumberTypeType",
    "OptedOutFilterNameType",
    "PhoneNumberFilterNameType",
    "PoolFilterNameType",
    "PoolOriginationIdentitiesFilterNameType",
    "PoolStatusType",
    "RequestableNumberTypeType",
    "SenderIdFilterNameType",
    "SpendLimitNameType",
    "VoiceIdType",
    "VoiceMessageBodyTextTypeType",
)

AccountAttributeNameType = Literal["ACCOUNT_TIER"]
AccountLimitNameType = Literal["CONFIGURATION_SETS", "OPT_OUT_LISTS", "PHONE_NUMBERS", "POOLS"]
ConfigurationSetFilterNameType = Literal[
    "default-message-type", "default-sender-id", "event-destination-name", "matching-event-types"
]
DescribeAccountAttributesPaginatorName = Literal["describe_account_attributes"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeConfigurationSetsPaginatorName = Literal["describe_configuration_sets"]
DescribeKeywordsPaginatorName = Literal["describe_keywords"]
DescribeOptOutListsPaginatorName = Literal["describe_opt_out_lists"]
DescribeOptedOutNumbersPaginatorName = Literal["describe_opted_out_numbers"]
DescribePhoneNumbersPaginatorName = Literal["describe_phone_numbers"]
DescribePoolsPaginatorName = Literal["describe_pools"]
DescribeSenderIdsPaginatorName = Literal["describe_sender_ids"]
DescribeSpendLimitsPaginatorName = Literal["describe_spend_limits"]
DestinationCountryParameterKeyType = Literal["IN_ENTITY_ID", "IN_TEMPLATE_ID"]
EventTypeType = Literal[
    "ALL",
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
KeywordActionType = Literal["AUTOMATIC_RESPONSE", "OPT_IN", "OPT_OUT"]
KeywordFilterNameType = Literal["keyword-action"]
ListPoolOriginationIdentitiesPaginatorName = Literal["list_pool_origination_identities"]
MessageTypeType = Literal["PROMOTIONAL", "TRANSACTIONAL"]
NumberCapabilityType = Literal["SMS", "VOICE"]
NumberStatusType = Literal["ACTIVE", "ASSOCIATING", "DELETED", "DISASSOCIATING", "PENDING"]
NumberTypeType = Literal["LONG_CODE", "SHORT_CODE", "TEN_DLC", "TOLL_FREE"]
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
    "two-way-enabled",
]
PoolFilterNameType = Literal[
    "deletion-protection-enabled",
    "message-type",
    "opt-out-list-name",
    "self-managed-opt-outs-enabled",
    "shared-routes-enabled",
    "status",
    "two-way-enabled",
]
PoolOriginationIdentitiesFilterNameType = Literal["iso-country-code", "number-capability"]
PoolStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
RequestableNumberTypeType = Literal["LONG_CODE", "TEN_DLC", "TOLL_FREE"]
SenderIdFilterNameType = Literal["iso-country-code", "message-type", "sender-id"]
SpendLimitNameType = Literal[
    "TEXT_MESSAGE_MONTHLY_SPEND_LIMIT", "VOICE_MESSAGE_MONTHLY_SPEND_LIMIT"
]
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
