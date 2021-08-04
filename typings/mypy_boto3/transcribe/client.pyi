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
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyStateType,
)
from .type_defs import (
    ContentRedactionTypeDef,
    CreateLanguageModelResponseTypeDef,
    CreateMedicalVocabularyResponseTypeDef,
    CreateVocabularyFilterResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    DescribeLanguageModelResponseTypeDef,
    GetMedicalTranscriptionJobResponseTypeDef,
    GetMedicalVocabularyResponseTypeDef,
    GetTranscriptionJobResponseTypeDef,
    GetVocabularyFilterResponseTypeDef,
    GetVocabularyResponseTypeDef,
    InputDataConfigTypeDef,
    JobExecutionSettingsTypeDef,
    ListLanguageModelsResponseTypeDef,
    ListMedicalTranscriptionJobsResponseTypeDef,
    ListMedicalVocabulariesResponseTypeDef,
    ListTranscriptionJobsResponseTypeDef,
    ListVocabulariesResponseTypeDef,
    ListVocabularyFiltersResponseTypeDef,
    MediaTypeDef,
    MedicalTranscriptionSettingTypeDef,
    ModelSettingsTypeDef,
    SettingsTypeDef,
    StartMedicalTranscriptionJobResponseTypeDef,
    StartTranscriptionJobResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#can_paginate)
        """
    def create_language_model(
        self,
        *,
        LanguageCode: CLMLanguageCodeType,
        BaseModelName: BaseModelNameType,
        ModelName: str,
        InputDataConfig: "InputDataConfigTypeDef"
    ) -> CreateLanguageModelResponseTypeDef:
        """
        Creates a new custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.create_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_language_model)
        """
    def create_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary that you can use to change how Amazon Transcribe
        Medical transcribes your audio file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_medical_vocabulary)
        """
    def create_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary that you can use to change the way Amazon
        Transcribe handles transcription of an audio file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary)
        """
    def create_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        LanguageCode: LanguageCodeType,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        Creates a new vocabulary filter that you can use to filter words, such as
        profane words, from the output of a transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary_filter)
        """
    def delete_language_model(self, *, ModelName: str) -> None:
        """
        Deletes a custom language model using its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_language_model)
        """
    def delete_medical_transcription_job(self, *, MedicalTranscriptionJobName: str) -> None:
        """
        Deletes a transcription job generated by Amazon Transcribe Medical and any
        related information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_transcription_job)
        """
    def delete_medical_vocabulary(self, *, VocabularyName: str) -> None:
        """
        Deletes a vocabulary from Amazon Transcribe Medical.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_vocabulary)
        """
    def delete_transcription_job(self, *, TranscriptionJobName: str) -> None:
        """
        Deletes a previously submitted transcription job along with any other generated
        results such as the transcription, models, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_transcription_job)
        """
    def delete_vocabulary(self, *, VocabularyName: str) -> None:
        """
        Deletes a vocabulary from Amazon Transcribe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary)
        """
    def delete_vocabulary_filter(self, *, VocabularyFilterName: str) -> None:
        """
        Removes a vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary_filter)
        """
    def describe_language_model(self, *, ModelName: str) -> DescribeLanguageModelResponseTypeDef:
        """
        Gets information about a single custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#generate_presigned_url)
        """
    def get_medical_transcription_job(
        self, *, MedicalTranscriptionJobName: str
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        Returns information about a transcription job from Amazon Transcribe Medical.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_transcription_job)
        """
    def get_medical_vocabulary(self, *, VocabularyName: str) -> GetMedicalVocabularyResponseTypeDef:
        """
        Retrieves information about a medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_vocabulary)
        """
    def get_transcription_job(
        self, *, TranscriptionJobName: str
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        Returns information about a transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_transcription_job)
        """
    def get_vocabulary(self, *, VocabularyName: str) -> GetVocabularyResponseTypeDef:
        """
        Gets information about a vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary)
        """
    def get_vocabulary_filter(
        self, *, VocabularyFilterName: str
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        Returns information about a vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary_filter)
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
        Provides more information about the custom language models you've created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_language_models)
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
        Lists medical transcription jobs with a specified status or substring that
        matches their names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)
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
        Returns a list of vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_medical_vocabularies)
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
        Lists transcription jobs with the specified status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)
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
        Returns a list of vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabularies)
        """
    def list_vocabulary_filters(
        self, *, NextToken: str = None, MaxResults: int = None, NameContains: str = None
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        Gets information about vocabulary filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabulary_filters)
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
        Settings: "MedicalTranscriptionSettingTypeDef" = None,
        ContentIdentificationType: Literal["PHI"] = None
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        Starts a batch job to transcribe medical speech to text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)
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
        Settings: "SettingsTypeDef" = None,
        ModelSettings: "ModelSettingsTypeDef" = None,
        JobExecutionSettings: "JobExecutionSettingsTypeDef" = None,
        ContentRedaction: "ContentRedactionTypeDef" = None,
        IdentifyLanguage: bool = None,
        LanguageOptions: List[LanguageCodeType] = None
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        Starts an asynchronous job to transcribe speech to text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_transcription_job)
        """
    def update_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str = None
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        Updates a vocabulary with new values that you provide in a different text file
        from the one you used to create the vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_medical_vocabulary)
        """
    def update_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None
    ) -> UpdateVocabularyResponseTypeDef:
        """
        Updates an existing vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary)
        """
    def update_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        Updates a vocabulary filter with a new list of filtered words.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary_filter)
        """
