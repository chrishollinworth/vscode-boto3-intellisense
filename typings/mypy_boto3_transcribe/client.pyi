"""
Type annotations for transcribe service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_transcribe import TranscribeServiceClient

    client: TranscribeServiceClient = boto3.client("transcribe")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BaseModelNameType,
    CallAnalyticsJobStatusType,
    CLMLanguageCodeType,
    InputTypeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyStateType,
)
from .type_defs import (
    CallAnalyticsJobSettingsTypeDef,
    ChannelDefinitionTypeDef,
    ContentRedactionTypeDef,
    CreateCallAnalyticsCategoryResponseTypeDef,
    CreateLanguageModelResponseTypeDef,
    CreateMedicalVocabularyResponseTypeDef,
    CreateVocabularyFilterResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    DescribeLanguageModelResponseTypeDef,
    GetCallAnalyticsCategoryResponseTypeDef,
    GetCallAnalyticsJobResponseTypeDef,
    GetMedicalTranscriptionJobResponseTypeDef,
    GetMedicalVocabularyResponseTypeDef,
    GetTranscriptionJobResponseTypeDef,
    GetVocabularyFilterResponseTypeDef,
    GetVocabularyResponseTypeDef,
    InputDataConfigTypeDef,
    JobExecutionSettingsTypeDef,
    LanguageIdSettingsTypeDef,
    ListCallAnalyticsCategoriesResponseTypeDef,
    ListCallAnalyticsJobsResponseTypeDef,
    ListLanguageModelsResponseTypeDef,
    ListMedicalTranscriptionJobsResponseTypeDef,
    ListMedicalVocabulariesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTranscriptionJobsResponseTypeDef,
    ListVocabulariesResponseTypeDef,
    ListVocabularyFiltersResponseTypeDef,
    MediaTypeDef,
    MedicalTranscriptionSettingTypeDef,
    ModelSettingsTypeDef,
    RuleTypeDef,
    SettingsTypeDef,
    StartCallAnalyticsJobResponseTypeDef,
    StartMedicalTranscriptionJobResponseTypeDef,
    StartTranscriptionJobResponseTypeDef,
    SubtitlesTypeDef,
    TagTypeDef,
    ToxicityDetectionSettingsTypeDef,
    UpdateCallAnalyticsCategoryResponseTypeDef,
    UpdateMedicalVocabularyResponseTypeDef,
    UpdateVocabularyFilterResponseTypeDef,
    UpdateVocabularyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TranscribeServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]

class TranscribeServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TranscribeServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#close)
        """
    def create_call_analytics_category(
        self, *, CategoryName: str, Rules: List["RuleTypeDef"], InputType: InputTypeType = None
    ) -> CreateCallAnalyticsCategoryResponseTypeDef:
        """
        Creates a new Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.create_call_analytics_category)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_call_analytics_category)
        """
    def create_language_model(
        self,
        *,
        LanguageCode: CLMLanguageCodeType,
        BaseModelName: BaseModelNameType,
        ModelName: str,
        InputDataConfig: "InputDataConfigTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateLanguageModelResponseTypeDef:
        """
        Creates a new custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.create_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_language_model)
        """
    def create_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        VocabularyFileUri: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        Creates a new custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_medical_vocabulary)
        """
    def create_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
        Tags: List["TagTypeDef"] = None,
        DataAccessRoleArn: str = None
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary)
        """
    def create_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        LanguageCode: LanguageCodeType,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None,
        Tags: List["TagTypeDef"] = None,
        DataAccessRoleArn: str = None
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        Creates a new custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary_filter)
        """
    def delete_call_analytics_category(self, *, CategoryName: str) -> Dict[str, Any]:
        """
        Deletes a Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_call_analytics_category)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_call_analytics_category)
        """
    def delete_call_analytics_job(self, *, CallAnalyticsJobName: str) -> Dict[str, Any]:
        """
        Deletes a Call Analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_call_analytics_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_call_analytics_job)
        """
    def delete_language_model(self, *, ModelName: str) -> None:
        """
        Deletes a custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_language_model)
        """
    def delete_medical_transcription_job(self, *, MedicalTranscriptionJobName: str) -> None:
        """
        Deletes a medical transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_transcription_job)
        """
    def delete_medical_vocabulary(self, *, VocabularyName: str) -> None:
        """
        Deletes a custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_vocabulary)
        """
    def delete_transcription_job(self, *, TranscriptionJobName: str) -> None:
        """
        Deletes a transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_transcription_job)
        """
    def delete_vocabulary(self, *, VocabularyName: str) -> None:
        """
        Deletes a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary)
        """
    def delete_vocabulary_filter(self, *, VocabularyFilterName: str) -> None:
        """
        Deletes a custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary_filter)
        """
    def describe_language_model(self, *, ModelName: str) -> DescribeLanguageModelResponseTypeDef:
        """
        Provides information about the specified custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#describe_language_model)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#generate_presigned_url)
        """
    def get_call_analytics_category(
        self, *, CategoryName: str
    ) -> GetCallAnalyticsCategoryResponseTypeDef:
        """
        Provides information about the specified Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_call_analytics_category)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_call_analytics_category)
        """
    def get_call_analytics_job(
        self, *, CallAnalyticsJobName: str
    ) -> GetCallAnalyticsJobResponseTypeDef:
        """
        Provides information about the specified Call Analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_call_analytics_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_call_analytics_job)
        """
    def get_medical_transcription_job(
        self, *, MedicalTranscriptionJobName: str
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        Provides information about the specified medical transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_transcription_job)
        """
    def get_medical_vocabulary(self, *, VocabularyName: str) -> GetMedicalVocabularyResponseTypeDef:
        """
        Provides information about the specified custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_vocabulary)
        """
    def get_transcription_job(
        self, *, TranscriptionJobName: str
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        Provides information about the specified transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_transcription_job)
        """
    def get_vocabulary(self, *, VocabularyName: str) -> GetVocabularyResponseTypeDef:
        """
        Provides information about the specified custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary)
        """
    def get_vocabulary_filter(
        self, *, VocabularyFilterName: str
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        Provides information about the specified custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary_filter)
        """
    def list_call_analytics_categories(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListCallAnalyticsCategoriesResponseTypeDef:
        """
        Provides a list of Call Analytics categories, including all rules that make up
        each category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_call_analytics_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_call_analytics_categories)
        """
    def list_call_analytics_jobs(
        self,
        *,
        Status: CallAnalyticsJobStatusType = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCallAnalyticsJobsResponseTypeDef:
        """
        Provides a list of Call Analytics jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_call_analytics_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_call_analytics_jobs)
        """
    def list_language_models(
        self,
        *,
        StatusEquals: ModelStatusType = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLanguageModelsResponseTypeDef:
        """
        Provides a list of custom language models that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_language_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_language_models)
        """
    def list_medical_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListMedicalTranscriptionJobsResponseTypeDef:
        """
        Provides a list of medical transcription jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_medical_transcription_jobs)
        """
    def list_medical_vocabularies(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: VocabularyStateType = None,
        NameContains: str = None
    ) -> ListMedicalVocabulariesResponseTypeDef:
        """
        Provides a list of custom medical vocabularies that match the specified
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_medical_vocabularies)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with the specified transcription job, vocabulary,
        model, or resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_tags_for_resource)
        """
    def list_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTranscriptionJobsResponseTypeDef:
        """
        Provides a list of transcription jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_transcription_jobs)
        """
    def list_vocabularies(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: VocabularyStateType = None,
        NameContains: str = None
    ) -> ListVocabulariesResponseTypeDef:
        """
        Provides a list of custom vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabularies)
        """
    def list_vocabulary_filters(
        self, *, NextToken: str = None, MaxResults: int = None, NameContains: str = None
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        Provides a list of custom vocabulary filters that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabulary_filters)
        """
    def start_call_analytics_job(
        self,
        *,
        CallAnalyticsJobName: str,
        Media: "MediaTypeDef",
        OutputLocation: str = None,
        OutputEncryptionKMSKeyId: str = None,
        DataAccessRoleArn: str = None,
        Settings: "CallAnalyticsJobSettingsTypeDef" = None,
        ChannelDefinitions: List["ChannelDefinitionTypeDef"] = None
    ) -> StartCallAnalyticsJobResponseTypeDef:
        """
        Transcribes the audio from a customer service call and applies any additional
        Request Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.start_call_analytics_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_call_analytics_job)
        """
    def start_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
        LanguageCode: LanguageCodeType,
        Media: "MediaTypeDef",
        OutputBucketName: str,
        Specialty: Literal["PRIMARYCARE"],
        Type: TypeType,
        MediaSampleRateHertz: int = None,
        MediaFormat: MediaFormatType = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        KMSEncryptionContext: Dict[str, str] = None,
        Settings: "MedicalTranscriptionSettingTypeDef" = None,
        ContentIdentificationType: Literal["PHI"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        Transcribes the audio from a medical dictation or conversation and applies any
        additional Request Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_medical_transcription_job)
        """
    def start_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
        Media: "MediaTypeDef",
        LanguageCode: LanguageCodeType = None,
        MediaSampleRateHertz: int = None,
        MediaFormat: MediaFormatType = None,
        OutputBucketName: str = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        KMSEncryptionContext: Dict[str, str] = None,
        Settings: "SettingsTypeDef" = None,
        ModelSettings: "ModelSettingsTypeDef" = None,
        JobExecutionSettings: "JobExecutionSettingsTypeDef" = None,
        ContentRedaction: "ContentRedactionTypeDef" = None,
        IdentifyLanguage: bool = None,
        IdentifyMultipleLanguages: bool = None,
        LanguageOptions: List[LanguageCodeType] = None,
        Subtitles: "SubtitlesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        LanguageIdSettings: Dict[LanguageCodeType, "LanguageIdSettingsTypeDef"] = None,
        ToxicityDetection: List["ToxicityDetectionSettingsTypeDef"] = None
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        Transcribes the audio from a media file and applies any additional Request
        Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_transcription_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more custom tags, each in the form of a key:value pair, to the
        specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Amazon Transcribe resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#untag_resource)
        """
    def update_call_analytics_category(
        self, *, CategoryName: str, Rules: List["RuleTypeDef"], InputType: InputTypeType = None
    ) -> UpdateCallAnalyticsCategoryResponseTypeDef:
        """
        Updates the specified Call Analytics category with new rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.update_call_analytics_category)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_call_analytics_category)
        """
    def update_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        Updates an existing custom medical vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_medical_vocabulary)
        """
    def update_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
        DataAccessRoleArn: str = None
    ) -> UpdateVocabularyResponseTypeDef:
        """
        Updates an existing custom vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary)
        """
    def update_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None,
        DataAccessRoleArn: str = None
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        Updates an existing custom vocabulary filter with a new list of words.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary_filter)
        """
