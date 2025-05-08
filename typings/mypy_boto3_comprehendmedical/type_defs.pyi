"""
Type annotations for comprehendmedical service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import TraitTypeDef

    data: TraitTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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
    RxNormTraitNameType,
    SNOMEDCTAttributeTypeType,
    SNOMEDCTEntityCategoryType,
    SNOMEDCTEntityTypeType,
    SNOMEDCTRelationshipTypeType,
    SNOMEDCTTraitNameType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AttributeTypeDef",
    "CharactersTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "DescribeEntitiesDetectionV2JobRequestTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobRequestTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobRequestTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobRequestTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DescribeSNOMEDCTInferenceJobRequestTypeDef",
    "DescribeSNOMEDCTInferenceJobResponseTypeDef",
    "DetectEntitiesRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2RequestTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIRequestTypeDef",
    "DetectPHIResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMRequestTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormRequestTypeDef",
    "InferRxNormResponseTypeDef",
    "InferSNOMEDCTRequestTypeDef",
    "InferSNOMEDCTResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsRequestTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsRequestTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsRequestTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsRequestTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "ListSNOMEDCTInferenceJobsRequestTypeDef",
    "ListSNOMEDCTInferenceJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "SNOMEDCTAttributeTypeDef",
    "SNOMEDCTConceptTypeDef",
    "SNOMEDCTDetailsTypeDef",
    "SNOMEDCTEntityTypeDef",
    "SNOMEDCTTraitTypeDef",
    "StartEntitiesDetectionV2JobRequestTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobRequestTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobRequestTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobRequestTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StartSNOMEDCTInferenceJobRequestTypeDef",
    "StartSNOMEDCTInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobRequestTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobRequestTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobRequestTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobRequestTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
    "StopSNOMEDCTInferenceJobRequestTypeDef",
    "StopSNOMEDCTInferenceJobResponseTypeDef",
    "TimestampTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
)

class TraitTypeDef(TypedDict):
    Name: NotRequired[AttributeNameType]
    Score: NotRequired[float]

class CharactersTypeDef(TypedDict):
    OriginalTextCharacters: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class InputDataConfigTypeDef(TypedDict):
    S3Bucket: str
    S3Key: NotRequired[str]

class OutputDataConfigTypeDef(TypedDict):
    S3Bucket: str
    S3Key: NotRequired[str]

class DescribeEntitiesDetectionV2JobRequestTypeDef(TypedDict):
    JobId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DescribeICD10CMInferenceJobRequestTypeDef(TypedDict):
    JobId: str

class DescribePHIDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeRxNormInferenceJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeSNOMEDCTInferenceJobRequestTypeDef(TypedDict):
    JobId: str

DetectEntitiesRequestTypeDef = TypedDict(
    "DetectEntitiesRequestTypeDef",
    {
        "Text": str,
    },
)
DetectEntitiesV2RequestTypeDef = TypedDict(
    "DetectEntitiesV2RequestTypeDef",
    {
        "Text": str,
    },
)
DetectPHIRequestTypeDef = TypedDict(
    "DetectPHIRequestTypeDef",
    {
        "Text": str,
    },
)

class ICD10CMTraitTypeDef(TypedDict):
    Name: NotRequired[ICD10CMTraitNameType]
    Score: NotRequired[float]

class ICD10CMConceptTypeDef(TypedDict):
    Description: NotRequired[str]
    Code: NotRequired[str]
    Score: NotRequired[float]

InferICD10CMRequestTypeDef = TypedDict(
    "InferICD10CMRequestTypeDef",
    {
        "Text": str,
    },
)
InferRxNormRequestTypeDef = TypedDict(
    "InferRxNormRequestTypeDef",
    {
        "Text": str,
    },
)
InferSNOMEDCTRequestTypeDef = TypedDict(
    "InferSNOMEDCTRequestTypeDef",
    {
        "Text": str,
    },
)

class SNOMEDCTDetailsTypeDef(TypedDict):
    Edition: NotRequired[str]
    Language: NotRequired[str]
    VersionDate: NotRequired[str]

class RxNormTraitTypeDef(TypedDict):
    Name: NotRequired[RxNormTraitNameType]
    Score: NotRequired[float]

class RxNormConceptTypeDef(TypedDict):
    Description: NotRequired[str]
    Code: NotRequired[str]
    Score: NotRequired[float]

class SNOMEDCTConceptTypeDef(TypedDict):
    Description: NotRequired[str]
    Code: NotRequired[str]
    Score: NotRequired[float]

class SNOMEDCTTraitTypeDef(TypedDict):
    Name: NotRequired[SNOMEDCTTraitNameType]
    Score: NotRequired[float]

class StopEntitiesDetectionV2JobRequestTypeDef(TypedDict):
    JobId: str

class StopICD10CMInferenceJobRequestTypeDef(TypedDict):
    JobId: str

class StopPHIDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopRxNormInferenceJobRequestTypeDef(TypedDict):
    JobId: str

class StopSNOMEDCTInferenceJobRequestTypeDef(TypedDict):
    JobId: str

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": NotRequired[EntitySubTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[RelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Traits": NotRequired[List[TraitTypeDef]],
    },
)

class ComprehendMedicalAsyncJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class ComprehendMedicalAsyncJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    ExpirationTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[Literal["en"]]
    DataAccessRoleArn: NotRequired[str]
    ManifestFilePath: NotRequired[str]
    KMSKey: NotRequired[str]
    ModelVersion: NotRequired[str]

class StartEntitiesDetectionV2JobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    KMSKey: NotRequired[str]

class StartICD10CMInferenceJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    KMSKey: NotRequired[str]

class StartPHIDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    KMSKey: NotRequired[str]

class StartRxNormInferenceJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    KMSKey: NotRequired[str]

class StartSNOMEDCTInferenceJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: Literal["en"]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    KMSKey: NotRequired[str]

class StartEntitiesDetectionV2JobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartICD10CMInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPHIDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRxNormInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSNOMEDCTInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionV2JobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopICD10CMInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPHIDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRxNormInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopSNOMEDCTInferenceJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": NotRequired[ICD10CMAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[ICD10CMTraitTypeDef]],
        "Category": NotRequired[ICD10CMEntityTypeType],
        "RelationshipType": NotRequired[ICD10CMRelationshipTypeType],
    },
)
RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": NotRequired[RxNormAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[RxNormTraitTypeDef]],
    },
)
SNOMEDCTAttributeTypeDef = TypedDict(
    "SNOMEDCTAttributeTypeDef",
    {
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[SNOMEDCTRelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[SNOMEDCTTraitTypeDef]],
        "SNOMEDCTConcepts": NotRequired[List[SNOMEDCTConceptTypeDef]],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Type": NotRequired[EntitySubTypeType],
        "Traits": NotRequired[List[TraitTypeDef]],
        "Attributes": NotRequired[List[AttributeTypeDef]],
    },
)
UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": NotRequired[EntityTypeType],
        "Attribute": NotRequired[AttributeTypeDef],
    },
)

class ListEntitiesDetectionV2JobsRequestTypeDef(TypedDict):
    Filter: NotRequired[ComprehendMedicalAsyncJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListICD10CMInferenceJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[ComprehendMedicalAsyncJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPHIDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[ComprehendMedicalAsyncJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRxNormInferenceJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[ComprehendMedicalAsyncJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSNOMEDCTInferenceJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[ComprehendMedicalAsyncJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeEntitiesDetectionV2JobResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeICD10CMInferenceJobResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePHIDetectionJobResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRxNormInferenceJobResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSNOMEDCTInferenceJobResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobProperties: ComprehendMedicalAsyncJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionV2JobsResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListICD10CMInferenceJobsResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPHIDetectionJobsResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRxNormInferenceJobsResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSNOMEDCTInferenceJobsResponseTypeDef(TypedDict):
    ComprehendMedicalAsyncJobPropertiesList: List[ComprehendMedicalAsyncJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICAL_CONDITION"]],
        "Type": NotRequired[ICD10CMEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[ICD10CMAttributeTypeDef]],
        "Traits": NotRequired[List[ICD10CMTraitTypeDef]],
        "ICD10CMConcepts": NotRequired[List[ICD10CMConceptTypeDef]],
    },
)
RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICATION"]],
        "Type": NotRequired[RxNormEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[RxNormAttributeTypeDef]],
        "Traits": NotRequired[List[RxNormTraitTypeDef]],
        "RxNormConcepts": NotRequired[List[RxNormConceptTypeDef]],
    },
)
SNOMEDCTEntityTypeDef = TypedDict(
    "SNOMEDCTEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[SNOMEDCTAttributeTypeDef]],
        "Traits": NotRequired[List[SNOMEDCTTraitTypeDef]],
        "SNOMEDCTConcepts": NotRequired[List[SNOMEDCTConceptTypeDef]],
    },
)

class DetectPHIResponseTypeDef(TypedDict):
    Entities: List[EntityTypeDef]
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class DetectEntitiesResponseTypeDef(TypedDict):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class DetectEntitiesV2ResponseTypeDef(TypedDict):
    Entities: List[EntityTypeDef]
    UnmappedAttributes: List[UnmappedAttributeTypeDef]
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class InferICD10CMResponseTypeDef(TypedDict):
    Entities: List[ICD10CMEntityTypeDef]
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class InferRxNormResponseTypeDef(TypedDict):
    Entities: List[RxNormEntityTypeDef]
    ModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class InferSNOMEDCTResponseTypeDef(TypedDict):
    Entities: List[SNOMEDCTEntityTypeDef]
    ModelVersion: str
    SNOMEDCTDetails: SNOMEDCTDetailsTypeDef
    Characters: CharactersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]
