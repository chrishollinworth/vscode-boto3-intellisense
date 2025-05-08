"""
Type annotations for translate service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_translate.type_defs import TermTypeDef

    data: TermTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    DirectionalityType,
    DisplayLanguageCodeType,
    FormalityType,
    JobStatusType,
    ParallelDataFormatType,
    ParallelDataStatusType,
    TerminologyDataFormatType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AppliedTerminologyTypeDef",
    "BlobTypeDef",
    "CreateParallelDataRequestTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataRequestTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DeleteTerminologyRequestTypeDef",
    "DescribeTextTranslationJobRequestTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "DocumentTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionKeyTypeDef",
    "GetParallelDataRequestTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyRequestTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyRequestTypeDef",
    "ImportTerminologyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "LanguageTypeDef",
    "ListLanguagesRequestTypeDef",
    "ListLanguagesResponseTypeDef",
    "ListParallelDataRequestTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTerminologiesRequestPaginateTypeDef",
    "ListTerminologiesRequestTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsRequestTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "StartTextTranslationJobRequestTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobRequestTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyDataTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "TimestampTypeDef",
    "TranslateDocumentRequestTypeDef",
    "TranslateDocumentResponseTypeDef",
    "TranslateTextRequestTypeDef",
    "TranslateTextResponseTypeDef",
    "TranslatedDocumentTypeDef",
    "TranslationSettingsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateParallelDataRequestTypeDef",
    "UpdateParallelDataResponseTypeDef",
)

class TermTypeDef(TypedDict):
    SourceText: NotRequired[str]
    TargetText: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "Type": Literal["KMS"],
        "Id": str,
    },
)

class ParallelDataConfigTypeDef(TypedDict):
    S3Uri: NotRequired[str]
    Format: NotRequired[ParallelDataFormatType]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteParallelDataRequestTypeDef(TypedDict):
    Name: str

class DeleteTerminologyRequestTypeDef(TypedDict):
    Name: str

class DescribeTextTranslationJobRequestTypeDef(TypedDict):
    JobId: str

class GetParallelDataRequestTypeDef(TypedDict):
    Name: str

class ParallelDataDataLocationTypeDef(TypedDict):
    RepositoryType: str
    Location: str

class GetTerminologyRequestTypeDef(TypedDict):
    Name: str
    TerminologyDataFormat: NotRequired[TerminologyDataFormatType]

class TerminologyDataLocationTypeDef(TypedDict):
    RepositoryType: str
    Location: str

class InputDataConfigTypeDef(TypedDict):
    S3Uri: str
    ContentType: str

class JobDetailsTypeDef(TypedDict):
    TranslatedDocumentsCount: NotRequired[int]
    DocumentsWithErrorsCount: NotRequired[int]
    InputDocumentsCount: NotRequired[int]

class LanguageTypeDef(TypedDict):
    LanguageName: str
    LanguageCode: str

class ListLanguagesRequestTypeDef(TypedDict):
    DisplayLanguageCode: NotRequired[DisplayLanguageCodeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListParallelDataRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTerminologiesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class TranslationSettingsTypeDef(TypedDict):
    Formality: NotRequired[FormalityType]
    Profanity: NotRequired[Literal["MASK"]]
    Brevity: NotRequired[Literal["ON"]]

class StopTextTranslationJobRequestTypeDef(TypedDict):
    JobId: str

TimestampTypeDef = Union[datetime, str]

class TranslatedDocumentTypeDef(TypedDict):
    Content: bytes

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class AppliedTerminologyTypeDef(TypedDict):
    Name: NotRequired[str]
    Terms: NotRequired[List[TermTypeDef]]

class DocumentTypeDef(TypedDict):
    Content: BlobTypeDef
    ContentType: str

class TerminologyDataTypeDef(TypedDict):
    File: BlobTypeDef
    Format: TerminologyDataFormatType
    Directionality: NotRequired[DirectionalityType]

class OutputDataConfigTypeDef(TypedDict):
    S3Uri: str
    EncryptionKey: NotRequired[EncryptionKeyTypeDef]

class TerminologyPropertiesTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Arn: NotRequired[str]
    SourceLanguageCode: NotRequired[str]
    TargetLanguageCodes: NotRequired[List[str]]
    EncryptionKey: NotRequired[EncryptionKeyTypeDef]
    SizeBytes: NotRequired[int]
    TermCount: NotRequired[int]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Directionality: NotRequired[DirectionalityType]
    Message: NotRequired[str]
    SkippedTermCount: NotRequired[int]
    Format: NotRequired[TerminologyDataFormatType]

class ParallelDataPropertiesTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[ParallelDataStatusType]
    SourceLanguageCode: NotRequired[str]
    TargetLanguageCodes: NotRequired[List[str]]
    ParallelDataConfig: NotRequired[ParallelDataConfigTypeDef]
    Message: NotRequired[str]
    ImportedDataSize: NotRequired[int]
    ImportedRecordCount: NotRequired[int]
    FailedRecordCount: NotRequired[int]
    SkippedRecordCount: NotRequired[int]
    EncryptionKey: NotRequired[EncryptionKeyTypeDef]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    LatestUpdateAttemptStatus: NotRequired[ParallelDataStatusType]
    LatestUpdateAttemptAt: NotRequired[datetime]

class UpdateParallelDataRequestTypeDef(TypedDict):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: NotRequired[str]

class CreateParallelDataRequestTypeDef(TypedDict):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: NotRequired[str]
    EncryptionKey: NotRequired[EncryptionKeyTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateParallelDataResponseTypeDef(TypedDict):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParallelDataResponseTypeDef(TypedDict):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTextTranslationJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTextTranslationJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParallelDataResponseTypeDef(TypedDict):
    Name: str
    Status: ParallelDataStatusType
    LatestUpdateAttemptStatus: ParallelDataStatusType
    LatestUpdateAttemptAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListLanguagesResponseTypeDef(TypedDict):
    Languages: List[LanguageTypeDef]
    DisplayLanguageCode: DisplayLanguageCodeType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTerminologiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

TranslateTextRequestTypeDef = TypedDict(
    "TranslateTextRequestTypeDef",
    {
        "Text": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "TerminologyNames": NotRequired[Sequence[str]],
        "Settings": NotRequired[TranslationSettingsTypeDef],
    },
)

class TextTranslationJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmittedBeforeTime: NotRequired[TimestampTypeDef]
    SubmittedAfterTime: NotRequired[TimestampTypeDef]

class TranslateDocumentResponseTypeDef(TypedDict):
    TranslatedDocument: TranslatedDocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateTextResponseTypeDef(TypedDict):
    TranslatedText: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateDocumentRequestTypeDef(TypedDict):
    Document: DocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: NotRequired[Sequence[str]]
    Settings: NotRequired[TranslationSettingsTypeDef]

class ImportTerminologyRequestTypeDef(TypedDict):
    Name: str
    MergeStrategy: Literal["OVERWRITE"]
    TerminologyData: TerminologyDataTypeDef
    Description: NotRequired[str]
    EncryptionKey: NotRequired[EncryptionKeyTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartTextTranslationJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    SourceLanguageCode: str
    TargetLanguageCodes: Sequence[str]
    ClientToken: str
    JobName: NotRequired[str]
    TerminologyNames: NotRequired[Sequence[str]]
    ParallelDataNames: NotRequired[Sequence[str]]
    Settings: NotRequired[TranslationSettingsTypeDef]

class TextTranslationJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    JobDetails: NotRequired[JobDetailsTypeDef]
    SourceLanguageCode: NotRequired[str]
    TargetLanguageCodes: NotRequired[List[str]]
    TerminologyNames: NotRequired[List[str]]
    ParallelDataNames: NotRequired[List[str]]
    Message: NotRequired[str]
    SubmittedTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    DataAccessRoleArn: NotRequired[str]
    Settings: NotRequired[TranslationSettingsTypeDef]

class GetTerminologyResponseTypeDef(TypedDict):
    TerminologyProperties: TerminologyPropertiesTypeDef
    TerminologyDataLocation: TerminologyDataLocationTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTerminologyResponseTypeDef(TypedDict):
    TerminologyProperties: TerminologyPropertiesTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTerminologiesResponseTypeDef(TypedDict):
    TerminologyPropertiesList: List[TerminologyPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetParallelDataResponseTypeDef(TypedDict):
    ParallelDataProperties: ParallelDataPropertiesTypeDef
    DataLocation: ParallelDataDataLocationTypeDef
    AuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    LatestUpdateAttemptAuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListParallelDataResponseTypeDef(TypedDict):
    ParallelDataPropertiesList: List[ParallelDataPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTextTranslationJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[TextTranslationJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeTextTranslationJobResponseTypeDef(TypedDict):
    TextTranslationJobProperties: TextTranslationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTextTranslationJobsResponseTypeDef(TypedDict):
    TextTranslationJobPropertiesList: List[TextTranslationJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
