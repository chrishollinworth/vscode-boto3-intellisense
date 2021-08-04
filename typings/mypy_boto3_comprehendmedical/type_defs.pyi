"""
Type annotations for comprehendmedical service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AttributeNameType,
    EntitySubTypeType,
    EntityTypeType,
    ICD10CMAttributeTypeType,
    ICD10CMEntityTypeType,
    ICD10CMRelationshipTypeType,
    ICD10CMTraitNameType,
    JobStatusType,
    RelationshipTypeType,
    RxNormAttributeTypeType,
    RxNormEntityTypeType,
)

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
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobRequestRequestTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2RequestRequestTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIRequestRequestTypeDef",
    "DetectPHIResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMRequestRequestTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormRequestRequestTypeDef",
    "InferRxNormResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsRequestRequestTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "StartEntitiesDetectionV2JobRequestRequestTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobRequestRequestTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobRequestRequestTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobRequestRequestTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobRequestRequestTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobRequestRequestTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": EntitySubTypeType,
        "Score": float,
        "RelationshipScore": float,
        "RelationshipType": RelationshipTypeType,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Category": EntityTypeType,
        "Traits": List["TraitTypeDef"],
    },
    total=False,
)

ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
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

DescribeEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeICD10CMInferenceJobResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePHIDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeRxNormInferenceJobResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": "ComprehendMedicalAsyncJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesRequestRequestTypeDef = TypedDict(
    "DetectEntitiesRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectEntitiesV2RequestRequestTypeDef = TypedDict(
    "DetectEntitiesV2RequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectEntitiesV2ResponseTypeDef = TypedDict(
    "DetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "UnmappedAttributes": List["UnmappedAttributeTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPHIRequestRequestTypeDef = TypedDict(
    "DetectPHIRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectPHIResponseTypeDef = TypedDict(
    "DetectPHIResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": EntityTypeType,
        "Type": EntitySubTypeType,
        "Traits": List["TraitTypeDef"],
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": ICD10CMAttributeTypeType,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["ICD10CMTraitTypeDef"],
        "Category": ICD10CMEntityTypeType,
        "RelationshipType": ICD10CMRelationshipTypeType,
    },
    total=False,
)

ICD10CMConceptTypeDef = TypedDict(
    "ICD10CMConceptTypeDef",
    {
        "Description": str,
        "Code": str,
        "Score": float,
    },
    total=False,
)

ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICAL_CONDITION"],
        "Type": ICD10CMEntityTypeType,
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
    {
        "Name": ICD10CMTraitNameType,
        "Score": float,
    },
    total=False,
)

InferICD10CMRequestRequestTypeDef = TypedDict(
    "InferICD10CMRequestRequestTypeDef",
    {
        "Text": str,
    },
)

InferICD10CMResponseTypeDef = TypedDict(
    "InferICD10CMResponseTypeDef",
    {
        "Entities": List["ICD10CMEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferRxNormRequestRequestTypeDef = TypedDict(
    "InferRxNormRequestRequestTypeDef",
    {
        "Text": str,
    },
)

InferRxNormResponseTypeDef = TypedDict(
    "InferRxNormResponseTypeDef",
    {
        "Entities": List["RxNormEntityTypeDef"],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "S3Key": str,
    },
    total=False,
)

class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass

ListEntitiesDetectionV2JobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            "ComprehendMedicalAsyncJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListICD10CMInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPHIDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPHIDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRxNormInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    {
        "Filter": "ComprehendMedicalAsyncJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "S3Key": str,
    },
    total=False,
)

class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": RxNormAttributeTypeType,
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
    "RxNormConceptTypeDef",
    {
        "Description": str,
        "Code": str,
        "Score": float,
    },
    total=False,
)

RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICATION"],
        "Type": RxNormEntityTypeType,
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
    "RxNormTraitTypeDef",
    {
        "Name": Literal["NEGATION"],
        "Score": float,
    },
    total=False,
)

_RequiredStartEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "_RequiredStartEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "_OptionalStartEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)

class StartEntitiesDetectionV2JobRequestRequestTypeDef(
    _RequiredStartEntitiesDetectionV2JobRequestRequestTypeDef,
    _OptionalStartEntitiesDetectionV2JobRequestRequestTypeDef,
):
    pass

StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartICD10CMInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)

class StartICD10CMInferenceJobRequestRequestTypeDef(
    _RequiredStartICD10CMInferenceJobRequestRequestTypeDef,
    _OptionalStartICD10CMInferenceJobRequestRequestTypeDef,
):
    pass

StartICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartPHIDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartPHIDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)

class StartPHIDetectionJobRequestRequestTypeDef(
    _RequiredStartPHIDetectionJobRequestRequestTypeDef,
    _OptionalStartPHIDetectionJobRequestRequestTypeDef,
):
    pass

StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartRxNormInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
    },
)
_OptionalStartRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "KMSKey": str,
    },
    total=False,
)

class StartRxNormInferenceJobRequestRequestTypeDef(
    _RequiredStartRxNormInferenceJobRequestRequestTypeDef,
    _OptionalStartRxNormInferenceJobRequestRequestTypeDef,
):
    pass

StartRxNormInferenceJobResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "StopRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopRxNormInferenceJobResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {
        "Name": AttributeNameType,
        "Score": float,
    },
    total=False,
)

UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": EntityTypeType,
        "Attribute": "AttributeTypeDef",
    },
    total=False,
)
