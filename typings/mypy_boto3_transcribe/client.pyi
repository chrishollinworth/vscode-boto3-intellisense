# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for transcribe service client

Usage::

    ```python
    import boto3
    from mypy_boto3_transcribe import TranscribeServiceClient

    client: TranscribeServiceClient = boto3.client("transcribe")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_transcribe.type_defs import (
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


class TranscribeServiceClient:
    """
    [TranscribeService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.can_paginate)
        """

    def create_language_model(
        self,
        LanguageCode: Literal["en-US"],
        BaseModelName: Literal["NarrowBand", "WideBand"],
        ModelName: str,
        InputDataConfig: "InputDataConfigTypeDef",
    ) -> CreateLanguageModelResponseTypeDef:
        """
        [Client.create_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.create_language_model)
        """

    def create_medical_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        VocabularyFileUri: str,
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        [Client.create_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)
        """

    def create_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
    ) -> CreateVocabularyResponseTypeDef:
        """
        [Client.create_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)
        """

    def create_vocabulary_filter(
        self,
        VocabularyFilterName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None,
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        [Client.create_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)
        """

    def delete_language_model(self, ModelName: str) -> None:
        """
        [Client.delete_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)
        """

    def delete_medical_transcription_job(self, MedicalTranscriptionJobName: str) -> None:
        """
        [Client.delete_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)
        """

    def delete_medical_vocabulary(self, VocabularyName: str) -> None:
        """
        [Client.delete_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)
        """

    def delete_transcription_job(self, TranscriptionJobName: str) -> None:
        """
        [Client.delete_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)
        """

    def delete_vocabulary(self, VocabularyName: str) -> None:
        """
        [Client.delete_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)
        """

    def delete_vocabulary_filter(self, VocabularyFilterName: str) -> None:
        """
        [Client.delete_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)
        """

    def describe_language_model(self, ModelName: str) -> DescribeLanguageModelResponseTypeDef:
        """
        [Client.describe_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)
        """

    def get_medical_transcription_job(
        self, MedicalTranscriptionJobName: str
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        [Client.get_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)
        """

    def get_medical_vocabulary(self, VocabularyName: str) -> GetMedicalVocabularyResponseTypeDef:
        """
        [Client.get_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)
        """

    def get_transcription_job(
        self, TranscriptionJobName: str
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        [Client.get_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)
        """

    def get_vocabulary(self, VocabularyName: str) -> GetVocabularyResponseTypeDef:
        """
        [Client.get_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)
        """

    def get_vocabulary_filter(
        self, VocabularyFilterName: str
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        [Client.get_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)
        """

    def list_language_models(
        self,
        StatusEquals: Literal["IN_PROGRESS", "FAILED", "COMPLETED"] = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListLanguageModelsResponseTypeDef:
        """
        [Client.list_language_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_language_models)
        """

    def list_medical_transcription_jobs(
        self,
        Status: Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"] = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListMedicalTranscriptionJobsResponseTypeDef:
        """
        [Client.list_medical_transcription_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)
        """

    def list_medical_vocabularies(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: Literal["PENDING", "READY", "FAILED"] = None,
        NameContains: str = None,
    ) -> ListMedicalVocabulariesResponseTypeDef:
        """
        [Client.list_medical_vocabularies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)
        """

    def list_transcription_jobs(
        self,
        Status: Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"] = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTranscriptionJobsResponseTypeDef:
        """
        [Client.list_transcription_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)
        """

    def list_vocabularies(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: Literal["PENDING", "READY", "FAILED"] = None,
        NameContains: str = None,
    ) -> ListVocabulariesResponseTypeDef:
        """
        [Client.list_vocabularies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)
        """

    def list_vocabulary_filters(
        self, NextToken: str = None, MaxResults: int = None, NameContains: str = None
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        [Client.list_vocabulary_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)
        """

    def start_medical_transcription_job(
        self,
        MedicalTranscriptionJobName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        Media: "MediaTypeDef",
        OutputBucketName: str,
        Specialty: Literal["PRIMARYCARE"],
        Type: Literal["CONVERSATION", "DICTATION"],
        MediaSampleRateHertz: int = None,
        MediaFormat: Literal["mp3", "mp4", "wav", "flac", "ogg", "amr", "webm"] = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: "MedicalTranscriptionSettingTypeDef" = None,
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        [Client.start_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)
        """

    def start_transcription_job(
        self,
        TranscriptionJobName: str,
        Media: "MediaTypeDef",
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ] = None,
        MediaSampleRateHertz: int = None,
        MediaFormat: Literal["mp3", "mp4", "wav", "flac", "ogg", "amr", "webm"] = None,
        OutputBucketName: str = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: "SettingsTypeDef" = None,
        ModelSettings: "ModelSettingsTypeDef" = None,
        JobExecutionSettings: "JobExecutionSettingsTypeDef" = None,
        ContentRedaction: "ContentRedactionTypeDef" = None,
        IdentifyLanguage: bool = None,
        LanguageOptions: List[
            Literal[
                "af-ZA",
                "ar-AE",
                "ar-SA",
                "cy-GB",
                "da-DK",
                "de-CH",
                "de-DE",
                "en-AB",
                "en-AU",
                "en-GB",
                "en-IE",
                "en-IN",
                "en-US",
                "en-WL",
                "es-ES",
                "es-US",
                "fa-IR",
                "fr-CA",
                "fr-FR",
                "ga-IE",
                "gd-GB",
                "he-IL",
                "hi-IN",
                "id-ID",
                "it-IT",
                "ja-JP",
                "ko-KR",
                "ms-MY",
                "nl-NL",
                "pt-BR",
                "pt-PT",
                "ru-RU",
                "ta-IN",
                "te-IN",
                "tr-TR",
                "zh-CN",
            ]
        ] = None,
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        [Client.start_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)
        """

    def update_medical_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        VocabularyFileUri: str = None,
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        [Client.update_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)
        """

    def update_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "af-ZA",
            "ar-AE",
            "ar-SA",
            "cy-GB",
            "da-DK",
            "de-CH",
            "de-DE",
            "en-AB",
            "en-AU",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-US",
            "en-WL",
            "es-ES",
            "es-US",
            "fa-IR",
            "fr-CA",
            "fr-FR",
            "ga-IE",
            "gd-GB",
            "he-IL",
            "hi-IN",
            "id-ID",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "ms-MY",
            "nl-NL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "ta-IN",
            "te-IN",
            "tr-TR",
            "zh-CN",
        ],
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
    ) -> UpdateVocabularyResponseTypeDef:
        """
        [Client.update_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)
        """

    def update_vocabulary_filter(
        self,
        VocabularyFilterName: str,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None,
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        [Client.update_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)
        """
