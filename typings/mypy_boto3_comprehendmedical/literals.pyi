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
)

AttributeNameType = Literal["DIAGNOSIS", "NEGATION", "SIGN", "SYMPTOM"]
EntitySubTypeType = Literal[
    "ACUITY",
    "ADDRESS",
    "AGE",
    "BRAND_NAME",
    "CONTACT_POINT",
    "DATE",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EMAIL",
    "FORM",
    "FREQUENCY",
    "GENERIC_NAME",
    "IDENTIFIER",
    "NAME",
    "PROCEDURE_NAME",
    "PROFESSION",
    "QUALITY",
    "QUANTITY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_NAME",
    "TEST_UNITS",
    "TEST_VALUE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
    "TIME_TO_MEDICATION_NAME",
    "TIME_TO_PROCEDURE_NAME",
    "TIME_TO_TEST_NAME",
    "TIME_TO_TREATMENT_NAME",
    "TREATMENT_NAME",
    "URL",
]
EntityTypeType = Literal[
    "ANATOMY",
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
ICD10CMRelationshipTypeType = Literal["OVERLAP", "SYSTEM_ORGAN_SITE"]
ICD10CMTraitNameType = Literal["DIAGNOSIS", "NEGATION", "SIGN", "SYMPTOM"]
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
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EVERY",
    "FOR",
    "FORM",
    "FREQUENCY",
    "NEGATIVE",
    "OVERLAP",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNITS",
    "TEST_VALUE",
    "WITH_DOSAGE",
]
RxNormAttributeTypeType = Literal[
    "DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"
]
RxNormEntityCategoryType = Literal["MEDICATION"]
RxNormEntityTypeType = Literal["BRAND_NAME", "GENERIC_NAME"]
RxNormTraitNameType = Literal["NEGATION"]
