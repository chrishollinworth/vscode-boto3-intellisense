"""
Type annotations for bedrock-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.literals import ConversationRoleType

    data: ConversationRoleType = "assistant"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConversationRoleType",
    "DocumentFormatType",
    "GuardrailContentFilterConfidenceType",
    "GuardrailContentFilterTypeType",
    "GuardrailContentPolicyActionType",
    "GuardrailManagedWordTypeType",
    "GuardrailPiiEntityTypeType",
    "GuardrailSensitiveInformationPolicyActionType",
    "GuardrailStreamProcessingModeType",
    "GuardrailTopicPolicyActionType",
    "GuardrailTopicTypeType",
    "GuardrailTraceType",
    "GuardrailWordPolicyActionType",
    "ImageFormatType",
    "StopReasonType",
    "ToolResultStatusType",
    "TraceType",
)

ConversationRoleType = Literal["assistant", "user"]
DocumentFormatType = Literal["csv", "doc", "docx", "html", "md", "pdf", "txt", "xls", "xlsx"]
GuardrailContentFilterConfidenceType = Literal["HIGH", "LOW", "MEDIUM", "NONE"]
GuardrailContentFilterTypeType = Literal[
    "HATE", "INSULTS", "MISCONDUCT", "PROMPT_ATTACK", "SEXUAL", "VIOLENCE"
]
GuardrailContentPolicyActionType = Literal["BLOCKED"]
GuardrailManagedWordTypeType = Literal["PROFANITY"]
GuardrailPiiEntityTypeType = Literal[
    "ADDRESS",
    "AGE",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "CA_HEALTH_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "CREDIT_DEBIT_CARD_CVV",
    "CREDIT_DEBIT_CARD_EXPIRY",
    "CREDIT_DEBIT_CARD_NUMBER",
    "DRIVER_ID",
    "EMAIL",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "IP_ADDRESS",
    "LICENSE_PLATE",
    "MAC_ADDRESS",
    "NAME",
    "PASSWORD",
    "PHONE",
    "PIN",
    "SWIFT_CODE",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
    "UK_NATIONAL_INSURANCE_NUMBER",
    "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    "URL",
    "USERNAME",
    "US_BANK_ACCOUNT_NUMBER",
    "US_BANK_ROUTING_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "US_PASSPORT_NUMBER",
    "US_SOCIAL_SECURITY_NUMBER",
    "VEHICLE_IDENTIFICATION_NUMBER",
]
GuardrailSensitiveInformationPolicyActionType = Literal["ANONYMIZED", "BLOCKED"]
GuardrailStreamProcessingModeType = Literal["async", "sync"]
GuardrailTopicPolicyActionType = Literal["BLOCKED"]
GuardrailTopicTypeType = Literal["DENY"]
GuardrailTraceType = Literal["disabled", "enabled"]
GuardrailWordPolicyActionType = Literal["BLOCKED"]
ImageFormatType = Literal["gif", "jpeg", "png", "webp"]
StopReasonType = Literal[
    "content_filtered",
    "end_turn",
    "guardrail_intervened",
    "max_tokens",
    "stop_sequence",
    "tool_use",
]
ToolResultStatusType = Literal["error", "success"]
TraceType = Literal["DISABLED", "ENABLED"]
