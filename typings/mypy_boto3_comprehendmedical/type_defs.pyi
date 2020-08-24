"""
Main interface for comprehendmedical service type definitions.

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InputDataConfigTypeDef",
    "OutputDataConfigTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIResponseTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormResponseTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
            "TIME_EXPRESSION",
            "TIME_TO_MEDICATION_NAME",
            "TIME_TO_DX_NAME",
            "TIME_TO_TEST_NAME",
            "TIME_TO_PROCEDURE_NAME",
            "TIME_TO_TREATMENT_NAME",
        ],
        "Score": float,
        "RelationshipScore": float,
        "RelationshipType": Literal[
            "EVERY",
            "WITH_DOSAGE",
            "ADMINISTERED_VIA",
            "FOR",
            "NEGATIVE",
            "OVERLAP",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_VALUE",
            "TEST_UNITS",
            "DIRECTION",
            "SYSTEM_ORGAN_SITE",
        ],
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
            "TIME_EXPRESSION",
        ],
        "Traits": List["TraitTypeDef"],
    },
    total=False,
)

ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": Literal["en"],
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
            "TIME_EXPRESSION",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
            "TIME_EXPRESSION",
            "TIME_TO_MEDICATION_NAME",
            "TIME_TO_DX_NAME",
            "TIME_TO_TEST_NAME",
            "TIME_TO_PROCEDURE_NAME",
            "TIME_TO_TREATMENT_NAME",
        ],
        "Traits": List["TraitTypeDef"],
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": Literal["ACUITY", "DIRECTION", "SYSTEM_ORGAN_SITE", "QUALITY", "QUANTITY"],
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["ICD10CMTraitTypeDef"],
    },
    total=False,
)

ICD10CMConceptTypeDef = TypedDict(
    "ICD10CMConceptTypeDef", {"Description": str, "Code": str, "Score": float}, total=False
)

ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICAL_CONDITION"],
        "Type": Literal["DX_NAME"],
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["ICD10CMAttributeTypeDef"],
        "Traits": List["ICD10CMTraitTypeDef"],
        "ICD10CMConcepts": List["ICD10CMConceptTypeDef"],
    },
    total=False,
)

ICD10CMTraitTypeDef = TypedDict(
    "ICD10CMTraitTypeDef",
    {"Name": Literal["NEGATION", "DIAGNOSIS", "SIGN", "SYMPTOM"], "Score": float},
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict("_RequiredInputDataConfigTypeDef", {"S3Bucket": str})
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


_RequiredOutputDataConfigTypeDef = TypedDict("_RequiredOutputDataConfigTypeDef", {"S3Bucket": str})
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": Literal[
            "DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"
        ],
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["RxNormTraitTypeDef"],
    },
    total=False,
)

RxNormConceptTypeDef = TypedDict(
    "RxNormConceptTypeDef", {"Description": str, "Code": str, "Score": float}, total=False
)

RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICATION"],
        "Type": Literal["BRAND_NAME", "GENERIC_NAME"],
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["RxNormAttributeTypeDef"],
        "Traits": List["RxNormTraitTypeDef"],
        "RxNormConcepts": List["RxNormConceptTypeDef"],
    },
    total=False,
)

RxNormTraitTypeDef = TypedDict(
    "RxNormTraitTypeDef", {"Name": Literal["NEGATION"], "Score": float}, total=False
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": float},
    total=False,
)

UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
            "TIME_EXPRESSION",
        ],
        "Attribute": "AttributeTypeDef",
    },
    total=False,
)

ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef"},
    total=False,
)

DescribeICD10CMInferenceJobResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef"},
    total=False,
)

DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef"},
    total=False,
)

DescribeRxNormInferenceJobResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef"},
    total=False,
)

_RequiredDetectEntitiesResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesResponseTypeDef",
    {"Entities": List["EntityTypeDef"], "ModelVersion": str},
)
_OptionalDetectEntitiesResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesResponseTypeDef",
    {"UnmappedAttributes": List["UnmappedAttributeTypeDef"], "PaginationToken": str},
    total=False,
)


class DetectEntitiesResponseTypeDef(
    _RequiredDetectEntitiesResponseTypeDef, _OptionalDetectEntitiesResponseTypeDef
):
    pass


_RequiredDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesV2ResponseTypeDef",
    {"Entities": List["EntityTypeDef"], "ModelVersion": str},
)
_OptionalDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesV2ResponseTypeDef",
    {"UnmappedAttributes": List["UnmappedAttributeTypeDef"], "PaginationToken": str},
    total=False,
)


class DetectEntitiesV2ResponseTypeDef(
    _RequiredDetectEntitiesV2ResponseTypeDef, _OptionalDetectEntitiesV2ResponseTypeDef
):
    pass


_RequiredDetectPHIResponseTypeDef = TypedDict(
    "_RequiredDetectPHIResponseTypeDef", {"Entities": List["EntityTypeDef"], "ModelVersion": str}
)
_OptionalDetectPHIResponseTypeDef = TypedDict(
    "_OptionalDetectPHIResponseTypeDef", {"PaginationToken": str}, total=False
)


class DetectPHIResponseTypeDef(
    _RequiredDetectPHIResponseTypeDef, _OptionalDetectPHIResponseTypeDef
):
    pass


_RequiredInferICD10CMResponseTypeDef = TypedDict(
    "_RequiredInferICD10CMResponseTypeDef", {"Entities": List["ICD10CMEntityTypeDef"]}
)
_OptionalInferICD10CMResponseTypeDef = TypedDict(
    "_OptionalInferICD10CMResponseTypeDef",
    {"PaginationToken": str, "ModelVersion": str},
    total=False,
)


class InferICD10CMResponseTypeDef(
    _RequiredInferICD10CMResponseTypeDef, _OptionalInferICD10CMResponseTypeDef
):
    pass


_RequiredInferRxNormResponseTypeDef = TypedDict(
    "_RequiredInferRxNormResponseTypeDef", {"Entities": List["RxNormEntityTypeDef"]}
)
_OptionalInferRxNormResponseTypeDef = TypedDict(
    "_OptionalInferRxNormResponseTypeDef",
    {"PaginationToken": str, "ModelVersion": str},
    total=False,
)


class InferRxNormResponseTypeDef(
    _RequiredInferRxNormResponseTypeDef, _OptionalInferRxNormResponseTypeDef
):
    pass


ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListICD10CMInferenceJobsResponseTypeDef = TypedDict(
    "ListICD10CMInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListPHIDetectionJobsResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListRxNormInferenceJobsResponseTypeDef = TypedDict(
    "ListRxNormInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

StartICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseTypeDef", {"JobId": str}, total=False
)

StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef", {"JobId": str}, total=False
)

StartRxNormInferenceJobResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseTypeDef", {"JobId": str}, total=False
)

StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

StopICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseTypeDef", {"JobId": str}, total=False
)

StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef", {"JobId": str}, total=False
)

StopRxNormInferenceJobResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseTypeDef", {"JobId": str}, total=False
)
