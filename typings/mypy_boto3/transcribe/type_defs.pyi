"""
Type annotations for transcribe service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import AbsoluteTimeRangeTypeDef

    data: AbsoluteTimeRangeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    BaseModelNameType,
    CallAnalyticsJobStatusType,
    CallAnalyticsSkippedReasonCodeType,
    CLMLanguageCodeType,
    InputTypeType,
    LanguageCodeType,
    MediaFormatType,
    MedicalScribeJobStatusType,
    MedicalScribeNoteTemplateType,
    MedicalScribeParticipantRoleType,
    ModelStatusType,
    OutputLocationTypeType,
    ParticipantRoleType,
    PiiEntityTypeType,
    RedactionOutputType,
    SentimentValueType,
    SubtitleFormatType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyFilterMethodType,
    VocabularyStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AbsoluteTimeRangeTypeDef",
    "CallAnalyticsJobDetailsTypeDef",
    "CallAnalyticsJobSettingsOutputTypeDef",
    "CallAnalyticsJobSettingsTypeDef",
    "CallAnalyticsJobSettingsUnionTypeDef",
    "CallAnalyticsJobSummaryTypeDef",
    "CallAnalyticsJobTypeDef",
    "CallAnalyticsSkippedFeatureTypeDef",
    "CategoryPropertiesTypeDef",
    "ChannelDefinitionTypeDef",
    "ClinicalNoteGenerationSettingsTypeDef",
    "ContentRedactionOutputTypeDef",
    "ContentRedactionTypeDef",
    "ContentRedactionUnionTypeDef",
    "CreateCallAnalyticsCategoryRequestTypeDef",
    "CreateCallAnalyticsCategoryResponseTypeDef",
    "CreateLanguageModelRequestTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyRequestTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterRequestTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DeleteCallAnalyticsCategoryRequestTypeDef",
    "DeleteCallAnalyticsJobRequestTypeDef",
    "DeleteLanguageModelRequestTypeDef",
    "DeleteMedicalScribeJobRequestTypeDef",
    "DeleteMedicalTranscriptionJobRequestTypeDef",
    "DeleteMedicalVocabularyRequestTypeDef",
    "DeleteTranscriptionJobRequestTypeDef",
    "DeleteVocabularyFilterRequestTypeDef",
    "DeleteVocabularyRequestTypeDef",
    "DescribeLanguageModelRequestTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCallAnalyticsCategoryRequestTypeDef",
    "GetCallAnalyticsCategoryResponseTypeDef",
    "GetCallAnalyticsJobRequestTypeDef",
    "GetCallAnalyticsJobResponseTypeDef",
    "GetMedicalScribeJobRequestTypeDef",
    "GetMedicalScribeJobResponseTypeDef",
    "GetMedicalTranscriptionJobRequestTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyRequestTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobRequestTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterRequestTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyRequestTypeDef",
    "GetVocabularyResponseTypeDef",
    "InputDataConfigTypeDef",
    "InterruptionFilterTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageCodeItemTypeDef",
    "LanguageIdSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListCallAnalyticsCategoriesRequestTypeDef",
    "ListCallAnalyticsCategoriesResponseTypeDef",
    "ListCallAnalyticsJobsRequestTypeDef",
    "ListCallAnalyticsJobsResponseTypeDef",
    "ListLanguageModelsRequestTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalScribeJobsRequestTypeDef",
    "ListMedicalScribeJobsResponseTypeDef",
    "ListMedicalTranscriptionJobsRequestTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesRequestTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTranscriptionJobsRequestTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesRequestTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersRequestTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MediaTypeDef",
    "MedicalScribeChannelDefinitionTypeDef",
    "MedicalScribeJobSummaryTypeDef",
    "MedicalScribeJobTypeDef",
    "MedicalScribeOutputTypeDef",
    "MedicalScribeSettingsTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "NonTalkTimeFilterTypeDef",
    "RelativeTimeRangeTypeDef",
    "ResponseMetadataTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "SentimentFilterOutputTypeDef",
    "SentimentFilterTypeDef",
    "SentimentFilterUnionTypeDef",
    "SettingsTypeDef",
    "StartCallAnalyticsJobRequestTypeDef",
    "StartCallAnalyticsJobResponseTypeDef",
    "StartMedicalScribeJobRequestTypeDef",
    "StartMedicalScribeJobResponseTypeDef",
    "StartMedicalTranscriptionJobRequestTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobRequestTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "SubtitlesOutputTypeDef",
    "SubtitlesTypeDef",
    "SummarizationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ToxicityDetectionSettingsOutputTypeDef",
    "ToxicityDetectionSettingsTypeDef",
    "ToxicityDetectionSettingsUnionTypeDef",
    "TranscriptFilterOutputTypeDef",
    "TranscriptFilterTypeDef",
    "TranscriptFilterUnionTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCallAnalyticsCategoryRequestTypeDef",
    "UpdateCallAnalyticsCategoryResponseTypeDef",
    "UpdateMedicalVocabularyRequestTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterRequestTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyRequestTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
)

class AbsoluteTimeRangeTypeDef(TypedDict):
    StartTime: NotRequired[int]
    EndTime: NotRequired[int]
    First: NotRequired[int]
    Last: NotRequired[int]

class CallAnalyticsSkippedFeatureTypeDef(TypedDict):
    Feature: NotRequired[Literal["GENERATIVE_SUMMARIZATION"]]
    ReasonCode: NotRequired[CallAnalyticsSkippedReasonCodeType]
    Message: NotRequired[str]

class ContentRedactionOutputTypeDef(TypedDict):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: NotRequired[List[PiiEntityTypeType]]

class LanguageIdSettingsTypeDef(TypedDict):
    VocabularyName: NotRequired[str]
    VocabularyFilterName: NotRequired[str]
    LanguageModelName: NotRequired[str]

class SummarizationTypeDef(TypedDict):
    GenerateAbstractiveSummary: bool

class ContentRedactionTypeDef(TypedDict):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: NotRequired[Sequence[PiiEntityTypeType]]

class ChannelDefinitionTypeDef(TypedDict):
    ChannelId: NotRequired[int]
    ParticipantRole: NotRequired[ParticipantRoleType]

class MediaTypeDef(TypedDict):
    MediaFileUri: NotRequired[str]
    RedactedMediaFileUri: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class TranscriptTypeDef(TypedDict):
    TranscriptFileUri: NotRequired[str]
    RedactedTranscriptFileUri: NotRequired[str]

class ClinicalNoteGenerationSettingsTypeDef(TypedDict):
    NoteTemplate: NotRequired[MedicalScribeNoteTemplateType]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class InputDataConfigTypeDef(TypedDict):
    S3Uri: str
    DataAccessRoleArn: str
    TuningDataS3Uri: NotRequired[str]

class DeleteCallAnalyticsCategoryRequestTypeDef(TypedDict):
    CategoryName: str

class DeleteCallAnalyticsJobRequestTypeDef(TypedDict):
    CallAnalyticsJobName: str

class DeleteLanguageModelRequestTypeDef(TypedDict):
    ModelName: str

class DeleteMedicalScribeJobRequestTypeDef(TypedDict):
    MedicalScribeJobName: str

class DeleteMedicalTranscriptionJobRequestTypeDef(TypedDict):
    MedicalTranscriptionJobName: str

class DeleteMedicalVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str

class DeleteTranscriptionJobRequestTypeDef(TypedDict):
    TranscriptionJobName: str

class DeleteVocabularyFilterRequestTypeDef(TypedDict):
    VocabularyFilterName: str

class DeleteVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str

class DescribeLanguageModelRequestTypeDef(TypedDict):
    ModelName: str

class GetCallAnalyticsCategoryRequestTypeDef(TypedDict):
    CategoryName: str

class GetCallAnalyticsJobRequestTypeDef(TypedDict):
    CallAnalyticsJobName: str

class GetMedicalScribeJobRequestTypeDef(TypedDict):
    MedicalScribeJobName: str

class GetMedicalTranscriptionJobRequestTypeDef(TypedDict):
    MedicalTranscriptionJobName: str

class GetMedicalVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str

class GetTranscriptionJobRequestTypeDef(TypedDict):
    TranscriptionJobName: str

class GetVocabularyFilterRequestTypeDef(TypedDict):
    VocabularyFilterName: str

class GetVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str

class RelativeTimeRangeTypeDef(TypedDict):
    StartPercentage: NotRequired[int]
    EndPercentage: NotRequired[int]
    First: NotRequired[int]
    Last: NotRequired[int]

class JobExecutionSettingsTypeDef(TypedDict):
    AllowDeferredExecution: NotRequired[bool]
    DataAccessRoleArn: NotRequired[str]

class LanguageCodeItemTypeDef(TypedDict):
    LanguageCode: NotRequired[LanguageCodeType]
    DurationInSeconds: NotRequired[float]

class ListCallAnalyticsCategoriesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCallAnalyticsJobsRequestTypeDef(TypedDict):
    Status: NotRequired[CallAnalyticsJobStatusType]
    JobNameContains: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLanguageModelsRequestTypeDef(TypedDict):
    StatusEquals: NotRequired[ModelStatusType]
    NameContains: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMedicalScribeJobsRequestTypeDef(TypedDict):
    Status: NotRequired[MedicalScribeJobStatusType]
    JobNameContains: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MedicalScribeJobSummaryTypeDef(TypedDict):
    MedicalScribeJobName: NotRequired[str]
    CreationTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    LanguageCode: NotRequired[Literal["en-US"]]
    MedicalScribeJobStatus: NotRequired[MedicalScribeJobStatusType]
    FailureReason: NotRequired[str]

class ListMedicalTranscriptionJobsRequestTypeDef(TypedDict):
    Status: NotRequired[TranscriptionJobStatusType]
    JobNameContains: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "FailureReason": NotRequired[str],
        "OutputLocationType": NotRequired[OutputLocationTypeType],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Type": NotRequired[TypeType],
    },
)

class ListMedicalVocabulariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StateEquals: NotRequired[VocabularyStateType]
    NameContains: NotRequired[str]

class VocabularyInfoTypeDef(TypedDict):
    VocabularyName: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    LastModifiedTime: NotRequired[datetime]
    VocabularyState: NotRequired[VocabularyStateType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListTranscriptionJobsRequestTypeDef(TypedDict):
    Status: NotRequired[TranscriptionJobStatusType]
    JobNameContains: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListVocabulariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StateEquals: NotRequired[VocabularyStateType]
    NameContains: NotRequired[str]

class ListVocabularyFiltersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    NameContains: NotRequired[str]

class VocabularyFilterInfoTypeDef(TypedDict):
    VocabularyFilterName: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    LastModifiedTime: NotRequired[datetime]

class MedicalScribeChannelDefinitionTypeDef(TypedDict):
    ChannelId: int
    ParticipantRole: MedicalScribeParticipantRoleType

class MedicalScribeOutputTypeDef(TypedDict):
    TranscriptFileUri: str
    ClinicalDocumentUri: str

class MedicalTranscriptTypeDef(TypedDict):
    TranscriptFileUri: NotRequired[str]

class MedicalTranscriptionSettingTypeDef(TypedDict):
    ShowSpeakerLabels: NotRequired[bool]
    MaxSpeakerLabels: NotRequired[int]
    ChannelIdentification: NotRequired[bool]
    ShowAlternatives: NotRequired[bool]
    MaxAlternatives: NotRequired[int]
    VocabularyName: NotRequired[str]

class ModelSettingsTypeDef(TypedDict):
    LanguageModelName: NotRequired[str]

class SettingsTypeDef(TypedDict):
    VocabularyName: NotRequired[str]
    ShowSpeakerLabels: NotRequired[bool]
    MaxSpeakerLabels: NotRequired[int]
    ChannelIdentification: NotRequired[bool]
    ShowAlternatives: NotRequired[bool]
    MaxAlternatives: NotRequired[int]
    VocabularyFilterName: NotRequired[str]
    VocabularyFilterMethod: NotRequired[VocabularyFilterMethodType]

class SubtitlesTypeDef(TypedDict):
    Formats: NotRequired[Sequence[SubtitleFormatType]]
    OutputStartIndex: NotRequired[int]

class SubtitlesOutputTypeDef(TypedDict):
    Formats: NotRequired[List[SubtitleFormatType]]
    SubtitleFileUris: NotRequired[List[str]]
    OutputStartIndex: NotRequired[int]

class ToxicityDetectionSettingsOutputTypeDef(TypedDict):
    ToxicityCategories: List[Literal["ALL"]]

class ToxicityDetectionSettingsTypeDef(TypedDict):
    ToxicityCategories: Sequence[Literal["ALL"]]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateMedicalVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str

class UpdateVocabularyFilterRequestTypeDef(TypedDict):
    VocabularyFilterName: str
    Words: NotRequired[Sequence[str]]
    VocabularyFilterFileUri: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]

class UpdateVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: NotRequired[Sequence[str]]
    VocabularyFileUri: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]

class CallAnalyticsJobDetailsTypeDef(TypedDict):
    Skipped: NotRequired[List[CallAnalyticsSkippedFeatureTypeDef]]

class CallAnalyticsJobSettingsOutputTypeDef(TypedDict):
    VocabularyName: NotRequired[str]
    VocabularyFilterName: NotRequired[str]
    VocabularyFilterMethod: NotRequired[VocabularyFilterMethodType]
    LanguageModelName: NotRequired[str]
    ContentRedaction: NotRequired[ContentRedactionOutputTypeDef]
    LanguageOptions: NotRequired[List[LanguageCodeType]]
    LanguageIdSettings: NotRequired[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]]
    Summarization: NotRequired[SummarizationTypeDef]

class CallAnalyticsJobSettingsTypeDef(TypedDict):
    VocabularyName: NotRequired[str]
    VocabularyFilterName: NotRequired[str]
    VocabularyFilterMethod: NotRequired[VocabularyFilterMethodType]
    LanguageModelName: NotRequired[str]
    ContentRedaction: NotRequired[ContentRedactionTypeDef]
    LanguageOptions: NotRequired[Sequence[LanguageCodeType]]
    LanguageIdSettings: NotRequired[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]]
    Summarization: NotRequired[SummarizationTypeDef]

ContentRedactionUnionTypeDef = Union[ContentRedactionTypeDef, ContentRedactionOutputTypeDef]

class CreateMedicalVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateVocabularyFilterRequestTypeDef(TypedDict):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    Words: NotRequired[Sequence[str]]
    VocabularyFilterFileUri: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataAccessRoleArn: NotRequired[str]

class CreateVocabularyRequestTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: NotRequired[Sequence[str]]
    VocabularyFileUri: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataAccessRoleArn: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class MedicalScribeSettingsTypeDef(TypedDict):
    ShowSpeakerLabels: NotRequired[bool]
    MaxSpeakerLabels: NotRequired[int]
    ChannelIdentification: NotRequired[bool]
    VocabularyName: NotRequired[str]
    VocabularyFilterName: NotRequired[str]
    VocabularyFilterMethod: NotRequired[VocabularyFilterMethodType]
    ClinicalNoteGenerationSettings: NotRequired[ClinicalNoteGenerationSettingsTypeDef]

class CreateMedicalVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyFilterResponseTypeDef(TypedDict):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetMedicalVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVocabularyFilterResponseTypeDef(TypedDict):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMedicalVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVocabularyFilterResponseTypeDef(TypedDict):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVocabularyResponseTypeDef(TypedDict):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLanguageModelRequestTypeDef(TypedDict):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateLanguageModelResponseTypeDef(TypedDict):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    ModelStatus: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class LanguageModelTypeDef(TypedDict):
    ModelName: NotRequired[str]
    CreateTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    LanguageCode: NotRequired[CLMLanguageCodeType]
    BaseModelName: NotRequired[BaseModelNameType]
    ModelStatus: NotRequired[ModelStatusType]
    UpgradeAvailability: NotRequired[bool]
    FailureReason: NotRequired[str]
    InputDataConfig: NotRequired[InputDataConfigTypeDef]

class InterruptionFilterTypeDef(TypedDict):
    Threshold: NotRequired[int]
    ParticipantRole: NotRequired[ParticipantRoleType]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    Negate: NotRequired[bool]

class NonTalkTimeFilterTypeDef(TypedDict):
    Threshold: NotRequired[int]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    Negate: NotRequired[bool]

class SentimentFilterOutputTypeDef(TypedDict):
    Sentiments: List[SentimentValueType]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    ParticipantRole: NotRequired[ParticipantRoleType]
    Negate: NotRequired[bool]

class SentimentFilterTypeDef(TypedDict):
    Sentiments: Sequence[SentimentValueType]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    ParticipantRole: NotRequired[ParticipantRoleType]
    Negate: NotRequired[bool]

class TranscriptFilterOutputTypeDef(TypedDict):
    TranscriptFilterType: Literal["EXACT"]
    Targets: List[str]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    ParticipantRole: NotRequired[ParticipantRoleType]
    Negate: NotRequired[bool]

class TranscriptFilterTypeDef(TypedDict):
    TranscriptFilterType: Literal["EXACT"]
    Targets: Sequence[str]
    AbsoluteTimeRange: NotRequired[AbsoluteTimeRangeTypeDef]
    RelativeTimeRange: NotRequired[RelativeTimeRangeTypeDef]
    ParticipantRole: NotRequired[ParticipantRoleType]
    Negate: NotRequired[bool]

class ListMedicalScribeJobsResponseTypeDef(TypedDict):
    Status: MedicalScribeJobStatusType
    MedicalScribeJobSummaries: List[MedicalScribeJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMedicalTranscriptionJobsResponseTypeDef(TypedDict):
    Status: TranscriptionJobStatusType
    MedicalTranscriptionJobSummaries: List[MedicalTranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMedicalVocabulariesResponseTypeDef(TypedDict):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListVocabulariesResponseTypeDef(TypedDict):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListVocabularyFiltersResponseTypeDef(TypedDict):
    VocabularyFilters: List[VocabularyFilterInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired[MediaTypeDef],
        "Transcript": NotRequired[MedicalTranscriptTypeDef],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired[MedicalTranscriptionSettingTypeDef],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "Type": NotRequired[TypeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
StartMedicalTranscriptionJobRequestTypeDef = TypedDict(
    "StartMedicalTranscriptionJobRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "LanguageCode": LanguageCodeType,
        "Media": MediaTypeDef,
        "OutputBucketName": str,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "OutputKey": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "Settings": NotRequired[MedicalTranscriptionSettingTypeDef],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class TranscriptionJobSummaryTypeDef(TypedDict):
    TranscriptionJobName: NotRequired[str]
    CreationTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    LanguageCode: NotRequired[LanguageCodeType]
    TranscriptionJobStatus: NotRequired[TranscriptionJobStatusType]
    FailureReason: NotRequired[str]
    OutputLocationType: NotRequired[OutputLocationTypeType]
    ContentRedaction: NotRequired[ContentRedactionOutputTypeDef]
    ModelSettings: NotRequired[ModelSettingsTypeDef]
    IdentifyLanguage: NotRequired[bool]
    IdentifyMultipleLanguages: NotRequired[bool]
    IdentifiedLanguageScore: NotRequired[float]
    LanguageCodes: NotRequired[List[LanguageCodeItemTypeDef]]
    ToxicityDetection: NotRequired[List[ToxicityDetectionSettingsOutputTypeDef]]

class TranscriptionJobTypeDef(TypedDict):
    TranscriptionJobName: NotRequired[str]
    TranscriptionJobStatus: NotRequired[TranscriptionJobStatusType]
    LanguageCode: NotRequired[LanguageCodeType]
    MediaSampleRateHertz: NotRequired[int]
    MediaFormat: NotRequired[MediaFormatType]
    Media: NotRequired[MediaTypeDef]
    Transcript: NotRequired[TranscriptTypeDef]
    StartTime: NotRequired[datetime]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    FailureReason: NotRequired[str]
    Settings: NotRequired[SettingsTypeDef]
    ModelSettings: NotRequired[ModelSettingsTypeDef]
    JobExecutionSettings: NotRequired[JobExecutionSettingsTypeDef]
    ContentRedaction: NotRequired[ContentRedactionOutputTypeDef]
    IdentifyLanguage: NotRequired[bool]
    IdentifyMultipleLanguages: NotRequired[bool]
    LanguageOptions: NotRequired[List[LanguageCodeType]]
    IdentifiedLanguageScore: NotRequired[float]
    LanguageCodes: NotRequired[List[LanguageCodeItemTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]
    Subtitles: NotRequired[SubtitlesOutputTypeDef]
    LanguageIdSettings: NotRequired[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]]
    ToxicityDetection: NotRequired[List[ToxicityDetectionSettingsOutputTypeDef]]

ToxicityDetectionSettingsUnionTypeDef = Union[
    ToxicityDetectionSettingsTypeDef, ToxicityDetectionSettingsOutputTypeDef
]

class CallAnalyticsJobSummaryTypeDef(TypedDict):
    CallAnalyticsJobName: NotRequired[str]
    CreationTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    LanguageCode: NotRequired[LanguageCodeType]
    CallAnalyticsJobStatus: NotRequired[CallAnalyticsJobStatusType]
    CallAnalyticsJobDetails: NotRequired[CallAnalyticsJobDetailsTypeDef]
    FailureReason: NotRequired[str]

class CallAnalyticsJobTypeDef(TypedDict):
    CallAnalyticsJobName: NotRequired[str]
    CallAnalyticsJobStatus: NotRequired[CallAnalyticsJobStatusType]
    CallAnalyticsJobDetails: NotRequired[CallAnalyticsJobDetailsTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    MediaSampleRateHertz: NotRequired[int]
    MediaFormat: NotRequired[MediaFormatType]
    Media: NotRequired[MediaTypeDef]
    Transcript: NotRequired[TranscriptTypeDef]
    StartTime: NotRequired[datetime]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    FailureReason: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]
    IdentifiedLanguageScore: NotRequired[float]
    Settings: NotRequired[CallAnalyticsJobSettingsOutputTypeDef]
    ChannelDefinitions: NotRequired[List[ChannelDefinitionTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]

CallAnalyticsJobSettingsUnionTypeDef = Union[
    CallAnalyticsJobSettingsTypeDef, CallAnalyticsJobSettingsOutputTypeDef
]

class MedicalScribeJobTypeDef(TypedDict):
    MedicalScribeJobName: NotRequired[str]
    MedicalScribeJobStatus: NotRequired[MedicalScribeJobStatusType]
    LanguageCode: NotRequired[Literal["en-US"]]
    Media: NotRequired[MediaTypeDef]
    MedicalScribeOutput: NotRequired[MedicalScribeOutputTypeDef]
    StartTime: NotRequired[datetime]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    FailureReason: NotRequired[str]
    Settings: NotRequired[MedicalScribeSettingsTypeDef]
    DataAccessRoleArn: NotRequired[str]
    ChannelDefinitions: NotRequired[List[MedicalScribeChannelDefinitionTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]

class StartMedicalScribeJobRequestTypeDef(TypedDict):
    MedicalScribeJobName: str
    Media: MediaTypeDef
    OutputBucketName: str
    DataAccessRoleArn: str
    Settings: MedicalScribeSettingsTypeDef
    OutputEncryptionKMSKeyId: NotRequired[str]
    KMSEncryptionContext: NotRequired[Mapping[str, str]]
    ChannelDefinitions: NotRequired[Sequence[MedicalScribeChannelDefinitionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeLanguageModelResponseTypeDef(TypedDict):
    LanguageModel: LanguageModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLanguageModelsResponseTypeDef(TypedDict):
    Models: List[LanguageModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

SentimentFilterUnionTypeDef = Union[SentimentFilterTypeDef, SentimentFilterOutputTypeDef]

class RuleOutputTypeDef(TypedDict):
    NonTalkTimeFilter: NotRequired[NonTalkTimeFilterTypeDef]
    InterruptionFilter: NotRequired[InterruptionFilterTypeDef]
    TranscriptFilter: NotRequired[TranscriptFilterOutputTypeDef]
    SentimentFilter: NotRequired[SentimentFilterOutputTypeDef]

TranscriptFilterUnionTypeDef = Union[TranscriptFilterTypeDef, TranscriptFilterOutputTypeDef]

class GetMedicalTranscriptionJobResponseTypeDef(TypedDict):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMedicalTranscriptionJobResponseTypeDef(TypedDict):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTranscriptionJobsResponseTypeDef(TypedDict):
    Status: TranscriptionJobStatusType
    TranscriptionJobSummaries: List[TranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTranscriptionJobResponseTypeDef(TypedDict):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTranscriptionJobResponseTypeDef(TypedDict):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTranscriptionJobRequestTypeDef(TypedDict):
    TranscriptionJobName: str
    Media: MediaTypeDef
    LanguageCode: NotRequired[LanguageCodeType]
    MediaSampleRateHertz: NotRequired[int]
    MediaFormat: NotRequired[MediaFormatType]
    OutputBucketName: NotRequired[str]
    OutputKey: NotRequired[str]
    OutputEncryptionKMSKeyId: NotRequired[str]
    KMSEncryptionContext: NotRequired[Mapping[str, str]]
    Settings: NotRequired[SettingsTypeDef]
    ModelSettings: NotRequired[ModelSettingsTypeDef]
    JobExecutionSettings: NotRequired[JobExecutionSettingsTypeDef]
    ContentRedaction: NotRequired[ContentRedactionUnionTypeDef]
    IdentifyLanguage: NotRequired[bool]
    IdentifyMultipleLanguages: NotRequired[bool]
    LanguageOptions: NotRequired[Sequence[LanguageCodeType]]
    Subtitles: NotRequired[SubtitlesTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    LanguageIdSettings: NotRequired[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]]
    ToxicityDetection: NotRequired[Sequence[ToxicityDetectionSettingsUnionTypeDef]]

class ListCallAnalyticsJobsResponseTypeDef(TypedDict):
    Status: CallAnalyticsJobStatusType
    CallAnalyticsJobSummaries: List[CallAnalyticsJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCallAnalyticsJobResponseTypeDef(TypedDict):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCallAnalyticsJobResponseTypeDef(TypedDict):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCallAnalyticsJobRequestTypeDef(TypedDict):
    CallAnalyticsJobName: str
    Media: MediaTypeDef
    OutputLocation: NotRequired[str]
    OutputEncryptionKMSKeyId: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]
    Settings: NotRequired[CallAnalyticsJobSettingsUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ChannelDefinitions: NotRequired[Sequence[ChannelDefinitionTypeDef]]

class GetMedicalScribeJobResponseTypeDef(TypedDict):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMedicalScribeJobResponseTypeDef(TypedDict):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CategoryPropertiesTypeDef(TypedDict):
    CategoryName: NotRequired[str]
    Rules: NotRequired[List[RuleOutputTypeDef]]
    CreateTime: NotRequired[datetime]
    LastUpdateTime: NotRequired[datetime]
    Tags: NotRequired[List[TagTypeDef]]
    InputType: NotRequired[InputTypeType]

class RuleTypeDef(TypedDict):
    NonTalkTimeFilter: NotRequired[NonTalkTimeFilterTypeDef]
    InterruptionFilter: NotRequired[InterruptionFilterTypeDef]
    TranscriptFilter: NotRequired[TranscriptFilterUnionTypeDef]
    SentimentFilter: NotRequired[SentimentFilterUnionTypeDef]

class CreateCallAnalyticsCategoryResponseTypeDef(TypedDict):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCallAnalyticsCategoryResponseTypeDef(TypedDict):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCallAnalyticsCategoriesResponseTypeDef(TypedDict):
    Categories: List[CategoryPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateCallAnalyticsCategoryResponseTypeDef(TypedDict):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class CreateCallAnalyticsCategoryRequestTypeDef(TypedDict):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    InputType: NotRequired[InputTypeType]

class UpdateCallAnalyticsCategoryRequestTypeDef(TypedDict):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    InputType: NotRequired[InputTypeType]
