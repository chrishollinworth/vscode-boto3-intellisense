"""
Type annotations for bedrock service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock.literals import CommitmentDurationType

    data: CommitmentDurationType = "OneMonth"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CommitmentDurationType",
    "CustomizationTypeType",
    "EvaluationJobStatusType",
    "EvaluationJobTypeType",
    "EvaluationTaskTypeType",
    "FineTuningJobStatusType",
    "FoundationModelLifecycleStatusType",
    "GuardrailContentFilterTypeType",
    "GuardrailFilterStrengthType",
    "GuardrailManagedWordsTypeType",
    "GuardrailPiiEntityTypeType",
    "GuardrailSensitiveInformationActionType",
    "GuardrailStatusType",
    "GuardrailTopicTypeType",
    "InferenceTypeType",
    "ListCustomModelsPaginatorName",
    "ListEvaluationJobsPaginatorName",
    "ListGuardrailsPaginatorName",
    "ListModelCustomizationJobsPaginatorName",
    "ListProvisionedModelThroughputsPaginatorName",
    "ModelCustomizationJobStatusType",
    "ModelCustomizationType",
    "ModelModalityType",
    "ProvisionedModelStatusType",
    "SortByProvisionedModelsType",
    "SortJobsByType",
    "SortModelsByType",
    "SortOrderType",
)

CommitmentDurationType = Literal["OneMonth", "SixMonths"]
CustomizationTypeType = Literal["CONTINUED_PRE_TRAINING", "FINE_TUNING"]
EvaluationJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
EvaluationJobTypeType = Literal["Automated", "Human"]
EvaluationTaskTypeType = Literal[
    "Classification", "Custom", "Generation", "QuestionAndAnswer", "Summarization"
]
FineTuningJobStatusType = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
FoundationModelLifecycleStatusType = Literal["ACTIVE", "LEGACY"]
GuardrailContentFilterTypeType = Literal[
    "HATE", "INSULTS", "MISCONDUCT", "PROMPT_ATTACK", "SEXUAL", "VIOLENCE"
]
GuardrailFilterStrengthType = Literal["HIGH", "LOW", "MEDIUM", "NONE"]
GuardrailManagedWordsTypeType = Literal["PROFANITY"]
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
GuardrailSensitiveInformationActionType = Literal["ANONYMIZE", "BLOCK"]
GuardrailStatusType = Literal["CREATING", "DELETING", "FAILED", "READY", "UPDATING", "VERSIONING"]
GuardrailTopicTypeType = Literal["DENY"]
InferenceTypeType = Literal["ON_DEMAND", "PROVISIONED"]
ListCustomModelsPaginatorName = Literal["list_custom_models"]
ListEvaluationJobsPaginatorName = Literal["list_evaluation_jobs"]
ListGuardrailsPaginatorName = Literal["list_guardrails"]
ListModelCustomizationJobsPaginatorName = Literal["list_model_customization_jobs"]
ListProvisionedModelThroughputsPaginatorName = Literal["list_provisioned_model_throughputs"]
ModelCustomizationJobStatusType = Literal[
    "Completed", "Failed", "InProgress", "Stopped", "Stopping"
]
ModelCustomizationType = Literal["CONTINUED_PRE_TRAINING", "FINE_TUNING"]
ModelModalityType = Literal["EMBEDDING", "IMAGE", "TEXT"]
ProvisionedModelStatusType = Literal["Creating", "Failed", "InService", "Updating"]
SortByProvisionedModelsType = Literal["CreationTime"]
SortJobsByType = Literal["CreationTime"]
SortModelsByType = Literal["CreationTime"]
SortOrderType = Literal["Ascending", "Descending"]
