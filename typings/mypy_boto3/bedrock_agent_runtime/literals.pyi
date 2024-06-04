"""
Type annotations for bedrock-agent-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock_agent_runtime.literals import CreationModeType

    data: CreationModeType = "DEFAULT"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CreationModeType",
    "ExternalSourceTypeType",
    "GuadrailActionType",
    "GuardrailActionType",
    "GuardrailContentFilterConfidenceType",
    "GuardrailContentFilterTypeType",
    "GuardrailContentPolicyActionType",
    "GuardrailManagedWordTypeType",
    "GuardrailPiiEntityTypeType",
    "GuardrailSensitiveInformationPolicyActionType",
    "GuardrailTopicPolicyActionType",
    "GuardrailTopicTypeType",
    "GuardrailWordPolicyActionType",
    "InvocationTypeType",
    "PromptTypeType",
    "ResponseStateType",
    "RetrievalResultLocationTypeType",
    "RetrieveAndGenerateTypeType",
    "RetrievePaginatorName",
    "SearchTypeType",
    "SourceType",
    "TypeType",
)

CreationModeType = Literal["DEFAULT", "OVERRIDDEN"]
ExternalSourceTypeType = Literal["BYTE_CONTENT", "S3"]
GuadrailActionType = Literal["INTERVENED", "NONE"]
GuardrailActionType = Literal["INTERVENED", "NONE"]
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
GuardrailTopicPolicyActionType = Literal["BLOCKED"]
GuardrailTopicTypeType = Literal["DENY"]
GuardrailWordPolicyActionType = Literal["BLOCKED"]
InvocationTypeType = Literal["ACTION_GROUP", "FINISH", "KNOWLEDGE_BASE"]
PromptTypeType = Literal[
    "KNOWLEDGE_BASE_RESPONSE_GENERATION", "ORCHESTRATION", "POST_PROCESSING", "PRE_PROCESSING"
]
ResponseStateType = Literal["FAILURE", "REPROMPT"]
RetrievalResultLocationTypeType = Literal["S3"]
RetrieveAndGenerateTypeType = Literal["EXTERNAL_SOURCES", "KNOWLEDGE_BASE"]
RetrievePaginatorName = Literal["retrieve"]
SearchTypeType = Literal["HYBRID", "SEMANTIC"]
SourceType = Literal["ACTION_GROUP", "KNOWLEDGE_BASE", "PARSER"]
TypeType = Literal["ACTION_GROUP", "ASK_USER", "FINISH", "KNOWLEDGE_BASE", "REPROMPT"]
