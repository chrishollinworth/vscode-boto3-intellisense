"""
Type annotations for comprehendmedical service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/literals.html)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.literals import AttributeNameType

    data: AttributeNameType = "DIAGNOSIS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeNameType",
    "EntitySubTypeType",
    "EntityTypeType",
    "ICD10CMAttributeTypeType",
    "ICD10CMEntityCategoryType",
    "ICD10CMEntityTypeType",
    "ICD10CMRelationshipTypeType",
    "ICD10CMTraitNameType",
    "JobStatusType",
    "LanguageCodeType",
    "RelationshipTypeType",
    "RxNormAttributeTypeType",
    "RxNormEntityCategoryType",
    "RxNormEntityTypeType",
    "RxNormTraitNameType",
    "SNOMEDCTAttributeTypeType",
    "SNOMEDCTEntityCategoryType",
    "SNOMEDCTEntityTypeType",
    "SNOMEDCTRelationshipTypeType",
    "SNOMEDCTTraitNameType",
)

AttributeNameType = Literal[
    "DIAGNOSIS",
    "FUTURE",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PAST_HISTORY",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",
]
EntitySubTypeType = Literal[
    "ACUITY",
    "ADDRESS",
    "AGE",
    "ALCOHOL_CONSUMPTION",
    "ALLERGIES",
    "AMOUNT",
    "BRAND_NAME",
    "CONTACT_POINT",
    "DATE",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "DX_NAME",
    "EMAIL",
    "FORM",
    "FREQUENCY",
    "GENDER",
    "GENERIC_NAME",
    "ID",
    "IDENTIFIER",
    "NAME",
    "PHONE_OR_FAX",
    "PROCEDURE_NAME",
    "PROFESSION",
    "QUALITY",
    "QUANTITY",
    "RACE_ETHNICITY",
    "RATE",
    "REC_DRUG_USE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_NAME",
    "TEST_UNIT",
    "TEST_UNITS",
    "TEST_VALUE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
    "TIME_TO_MEDICATION_NAME",
    "TIME_TO_PROCEDURE_NAME",
    "TIME_TO_TEST_NAME",
    "TIME_TO_TREATMENT_NAME",
    "TOBACCO_USE",
    "TREATMENT_NAME",
    "URL",
]
EntityTypeType = Literal[
    "ANATOMY",
    "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
    "MEDICAL_CONDITION",
    "MEDICATION",
    "PROTECTED_HEALTH_INFORMATION",
    "TEST_TREATMENT_PROCEDURE",
    "TIME_EXPRESSION",
]
ICD10CMAttributeTypeType = Literal[
    "ACUITY",
    "DIRECTION",
    "QUALITY",
    "QUANTITY",
    "SYSTEM_ORGAN_SITE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
]
ICD10CMEntityCategoryType = Literal["MEDICAL_CONDITION"]
ICD10CMEntityTypeType = Literal["DX_NAME", "TIME_EXPRESSION"]
ICD10CMRelationshipTypeType = Literal["OVERLAP", "QUALITY", "SYSTEM_ORGAN_SITE"]
ICD10CMTraitNameType = Literal[
    "DIAGNOSIS",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",
]
JobStatusType = Literal[
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
    "PARTIAL_SUCCESS",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",
]
LanguageCodeType = Literal["en"]
RelationshipTypeType = Literal[
    "ACUITY",
    "ADMINISTERED_VIA",
    "AMOUNT",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EVERY",
    "FOR",
    "FORM",
    "FREQUENCY",
    "NEGATIVE",
    "OVERLAP",
    "QUALITY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNIT",
    "TEST_UNITS",
    "TEST_VALUE",
    "USAGE",
    "WITH_DOSAGE",
]
RxNormAttributeTypeType = Literal[
    "DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"
]
RxNormEntityCategoryType = Literal["MEDICATION"]
RxNormEntityTypeType = Literal["BRAND_NAME", "GENERIC_NAME"]
RxNormTraitNameType = Literal["NEGATION", "PAST_HISTORY"]
SNOMEDCTAttributeTypeType = Literal[
    "ACUITY", "DIRECTION", "QUALITY", "SYSTEM_ORGAN_SITE", "TEST_UNIT", "TEST_VALUE"
]
SNOMEDCTEntityCategoryType = Literal["ANATOMY", "MEDICAL_CONDITION", "TEST_TREATMENT_PROCEDURE"]
SNOMEDCTEntityTypeType = Literal["DX_NAME", "PROCEDURE_NAME", "TEST_NAME", "TREATMENT_NAME"]
SNOMEDCTRelationshipTypeType = Literal[
    "ACUITY", "DIRECTION", "QUALITY", "SYSTEM_ORGAN_SITE", "TEST_UNIT", "TEST_UNITS", "TEST_VALUE"
]
SNOMEDCTTraitNameType = Literal[
    "DIAGNOSIS",
    "FUTURE",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PAST_HISTORY",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",
]
