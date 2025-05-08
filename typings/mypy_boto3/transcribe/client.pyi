"""
Type annotations for transcribe service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_transcribe.client import TranscribeServiceClient

    session = Session()
    client: TranscribeServiceClient = session.client("transcribe")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateCallAnalyticsCategoryRequestTypeDef,
    CreateCallAnalyticsCategoryResponseTypeDef,
    CreateLanguageModelRequestTypeDef,
    CreateLanguageModelResponseTypeDef,
    CreateMedicalVocabularyRequestTypeDef,
    CreateMedicalVocabularyResponseTypeDef,
    CreateVocabularyFilterRequestTypeDef,
    CreateVocabularyFilterResponseTypeDef,
    CreateVocabularyRequestTypeDef,
    CreateVocabularyResponseTypeDef,
    DeleteCallAnalyticsCategoryRequestTypeDef,
    DeleteCallAnalyticsJobRequestTypeDef,
    DeleteLanguageModelRequestTypeDef,
    DeleteMedicalScribeJobRequestTypeDef,
    DeleteMedicalTranscriptionJobRequestTypeDef,
    DeleteMedicalVocabularyRequestTypeDef,
    DeleteTranscriptionJobRequestTypeDef,
    DeleteVocabularyFilterRequestTypeDef,
    DeleteVocabularyRequestTypeDef,
    DescribeLanguageModelRequestTypeDef,
    DescribeLanguageModelResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCallAnalyticsCategoryRequestTypeDef,
    GetCallAnalyticsCategoryResponseTypeDef,
    GetCallAnalyticsJobRequestTypeDef,
    GetCallAnalyticsJobResponseTypeDef,
    GetMedicalScribeJobRequestTypeDef,
    GetMedicalScribeJobResponseTypeDef,
    GetMedicalTranscriptionJobRequestTypeDef,
    GetMedicalTranscriptionJobResponseTypeDef,
    GetMedicalVocabularyRequestTypeDef,
    GetMedicalVocabularyResponseTypeDef,
    GetTranscriptionJobRequestTypeDef,
    GetTranscriptionJobResponseTypeDef,
    GetVocabularyFilterRequestTypeDef,
    GetVocabularyFilterResponseTypeDef,
    GetVocabularyRequestTypeDef,
    GetVocabularyResponseTypeDef,
    ListCallAnalyticsCategoriesRequestTypeDef,
    ListCallAnalyticsCategoriesResponseTypeDef,
    ListCallAnalyticsJobsRequestTypeDef,
    ListCallAnalyticsJobsResponseTypeDef,
    ListLanguageModelsRequestTypeDef,
    ListLanguageModelsResponseTypeDef,
    ListMedicalScribeJobsRequestTypeDef,
    ListMedicalScribeJobsResponseTypeDef,
    ListMedicalTranscriptionJobsRequestTypeDef,
    ListMedicalTranscriptionJobsResponseTypeDef,
    ListMedicalVocabulariesRequestTypeDef,
    ListMedicalVocabulariesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTranscriptionJobsRequestTypeDef,
    ListTranscriptionJobsResponseTypeDef,
    ListVocabulariesRequestTypeDef,
    ListVocabulariesResponseTypeDef,
    ListVocabularyFiltersRequestTypeDef,
    ListVocabularyFiltersResponseTypeDef,
    StartCallAnalyticsJobRequestTypeDef,
    StartCallAnalyticsJobResponseTypeDef,
    StartMedicalScribeJobRequestTypeDef,
    StartMedicalScribeJobResponseTypeDef,
    StartMedicalTranscriptionJobRequestTypeDef,
    StartMedicalTranscriptionJobResponseTypeDef,
    StartTranscriptionJobRequestTypeDef,
    StartTranscriptionJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCallAnalyticsCategoryRequestTypeDef,
    UpdateCallAnalyticsCategoryResponseTypeDef,
    UpdateMedicalVocabularyRequestTypeDef,
    UpdateMedicalVocabularyResponseTypeDef,
    UpdateVocabularyFilterRequestTypeDef,
    UpdateVocabularyFilterResponseTypeDef,
    UpdateVocabularyRequestTypeDef,
    UpdateVocabularyResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("TranscribeServiceClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]

class TranscribeServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TranscribeServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#generate_presigned_url)
        """

    def create_call_analytics_category(
        self, **kwargs: Unpack[CreateCallAnalyticsCategoryRequestTypeDef]
    ) -> CreateCallAnalyticsCategoryResponseTypeDef:
        """
        Creates a new Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/create_call_analytics_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#create_call_analytics_category)
        """

    def create_language_model(
        self, **kwargs: Unpack[CreateLanguageModelRequestTypeDef]
    ) -> CreateLanguageModelResponseTypeDef:
        """
        Creates a new custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/create_language_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#create_language_model)
        """

    def create_medical_vocabulary(
        self, **kwargs: Unpack[CreateMedicalVocabularyRequestTypeDef]
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        Creates a new custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/create_medical_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#create_medical_vocabulary)
        """

    def create_vocabulary(
        self, **kwargs: Unpack[CreateVocabularyRequestTypeDef]
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/create_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#create_vocabulary)
        """

    def create_vocabulary_filter(
        self, **kwargs: Unpack[CreateVocabularyFilterRequestTypeDef]
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        Creates a new custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/create_vocabulary_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#create_vocabulary_filter)
        """

    def delete_call_analytics_category(
        self, **kwargs: Unpack[DeleteCallAnalyticsCategoryRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_call_analytics_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_call_analytics_category)
        """

    def delete_call_analytics_job(
        self, **kwargs: Unpack[DeleteCallAnalyticsJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Call Analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_call_analytics_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_call_analytics_job)
        """

    def delete_language_model(
        self, **kwargs: Unpack[DeleteLanguageModelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_language_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_language_model)
        """

    def delete_medical_scribe_job(
        self, **kwargs: Unpack[DeleteMedicalScribeJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Medical Scribe job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_medical_scribe_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_medical_scribe_job)
        """

    def delete_medical_transcription_job(
        self, **kwargs: Unpack[DeleteMedicalTranscriptionJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a medical transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_medical_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_medical_transcription_job)
        """

    def delete_medical_vocabulary(
        self, **kwargs: Unpack[DeleteMedicalVocabularyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_medical_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_medical_vocabulary)
        """

    def delete_transcription_job(
        self, **kwargs: Unpack[DeleteTranscriptionJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_transcription_job)
        """

    def delete_vocabulary(
        self, **kwargs: Unpack[DeleteVocabularyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_vocabulary)
        """

    def delete_vocabulary_filter(
        self, **kwargs: Unpack[DeleteVocabularyFilterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/delete_vocabulary_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#delete_vocabulary_filter)
        """

    def describe_language_model(
        self, **kwargs: Unpack[DescribeLanguageModelRequestTypeDef]
    ) -> DescribeLanguageModelResponseTypeDef:
        """
        Provides information about the specified custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/describe_language_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#describe_language_model)
        """

    def get_call_analytics_category(
        self, **kwargs: Unpack[GetCallAnalyticsCategoryRequestTypeDef]
    ) -> GetCallAnalyticsCategoryResponseTypeDef:
        """
        Provides information about the specified Call Analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_call_analytics_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_call_analytics_category)
        """

    def get_call_analytics_job(
        self, **kwargs: Unpack[GetCallAnalyticsJobRequestTypeDef]
    ) -> GetCallAnalyticsJobResponseTypeDef:
        """
        Provides information about the specified Call Analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_call_analytics_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_call_analytics_job)
        """

    def get_medical_scribe_job(
        self, **kwargs: Unpack[GetMedicalScribeJobRequestTypeDef]
    ) -> GetMedicalScribeJobResponseTypeDef:
        """
        Provides information about the specified Medical Scribe job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_medical_scribe_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_medical_scribe_job)
        """

    def get_medical_transcription_job(
        self, **kwargs: Unpack[GetMedicalTranscriptionJobRequestTypeDef]
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        Provides information about the specified medical transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_medical_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_medical_transcription_job)
        """

    def get_medical_vocabulary(
        self, **kwargs: Unpack[GetMedicalVocabularyRequestTypeDef]
    ) -> GetMedicalVocabularyResponseTypeDef:
        """
        Provides information about the specified custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_medical_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_medical_vocabulary)
        """

    def get_transcription_job(
        self, **kwargs: Unpack[GetTranscriptionJobRequestTypeDef]
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        Provides information about the specified transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_transcription_job)
        """

    def get_vocabulary(
        self, **kwargs: Unpack[GetVocabularyRequestTypeDef]
    ) -> GetVocabularyResponseTypeDef:
        """
        Provides information about the specified custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_vocabulary)
        """

    def get_vocabulary_filter(
        self, **kwargs: Unpack[GetVocabularyFilterRequestTypeDef]
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        Provides information about the specified custom vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/get_vocabulary_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#get_vocabulary_filter)
        """

    def list_call_analytics_categories(
        self, **kwargs: Unpack[ListCallAnalyticsCategoriesRequestTypeDef]
    ) -> ListCallAnalyticsCategoriesResponseTypeDef:
        """
        Provides a list of Call Analytics categories, including all rules that make up
        each category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_call_analytics_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_call_analytics_categories)
        """

    def list_call_analytics_jobs(
        self, **kwargs: Unpack[ListCallAnalyticsJobsRequestTypeDef]
    ) -> ListCallAnalyticsJobsResponseTypeDef:
        """
        Provides a list of Call Analytics jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_call_analytics_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_call_analytics_jobs)
        """

    def list_language_models(
        self, **kwargs: Unpack[ListLanguageModelsRequestTypeDef]
    ) -> ListLanguageModelsResponseTypeDef:
        """
        Provides a list of custom language models that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_language_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_language_models)
        """

    def list_medical_scribe_jobs(
        self, **kwargs: Unpack[ListMedicalScribeJobsRequestTypeDef]
    ) -> ListMedicalScribeJobsResponseTypeDef:
        """
        Provides a list of Medical Scribe jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_medical_scribe_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_medical_scribe_jobs)
        """

    def list_medical_transcription_jobs(
        self, **kwargs: Unpack[ListMedicalTranscriptionJobsRequestTypeDef]
    ) -> ListMedicalTranscriptionJobsResponseTypeDef:
        """
        Provides a list of medical transcription jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_medical_transcription_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_medical_transcription_jobs)
        """

    def list_medical_vocabularies(
        self, **kwargs: Unpack[ListMedicalVocabulariesRequestTypeDef]
    ) -> ListMedicalVocabulariesResponseTypeDef:
        """
        Provides a list of custom medical vocabularies that match the specified
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_medical_vocabularies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_medical_vocabularies)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with the specified transcription job, vocabulary,
        model, or resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_tags_for_resource)
        """

    def list_transcription_jobs(
        self, **kwargs: Unpack[ListTranscriptionJobsRequestTypeDef]
    ) -> ListTranscriptionJobsResponseTypeDef:
        """
        Provides a list of transcription jobs that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_transcription_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_transcription_jobs)
        """

    def list_vocabularies(
        self, **kwargs: Unpack[ListVocabulariesRequestTypeDef]
    ) -> ListVocabulariesResponseTypeDef:
        """
        Provides a list of custom vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_vocabularies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_vocabularies)
        """

    def list_vocabulary_filters(
        self, **kwargs: Unpack[ListVocabularyFiltersRequestTypeDef]
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        Provides a list of custom vocabulary filters that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/list_vocabulary_filters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#list_vocabulary_filters)
        """

    def start_call_analytics_job(
        self, **kwargs: Unpack[StartCallAnalyticsJobRequestTypeDef]
    ) -> StartCallAnalyticsJobResponseTypeDef:
        """
        Transcribes the audio from a customer service call and applies any additional
        Request Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_call_analytics_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#start_call_analytics_job)
        """

    def start_medical_scribe_job(
        self, **kwargs: Unpack[StartMedicalScribeJobRequestTypeDef]
    ) -> StartMedicalScribeJobResponseTypeDef:
        """
        Transcribes patient-clinician conversations and generates clinical notes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_medical_scribe_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#start_medical_scribe_job)
        """

    def start_medical_transcription_job(
        self, **kwargs: Unpack[StartMedicalTranscriptionJobRequestTypeDef]
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        Transcribes the audio from a medical dictation or conversation and applies any
        additional Request Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_medical_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#start_medical_transcription_job)
        """

    def start_transcription_job(
        self, **kwargs: Unpack[StartTranscriptionJobRequestTypeDef]
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        Transcribes the audio from a media file and applies any additional Request
        Parameters you choose to include in your request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_transcription_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#start_transcription_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more custom tags, each in the form of a key:value pair, to the
        specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Amazon Transcribe resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#untag_resource)
        """

    def update_call_analytics_category(
        self, **kwargs: Unpack[UpdateCallAnalyticsCategoryRequestTypeDef]
    ) -> UpdateCallAnalyticsCategoryResponseTypeDef:
        """
        Updates the specified Call Analytics category with new rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/update_call_analytics_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#update_call_analytics_category)
        """

    def update_medical_vocabulary(
        self, **kwargs: Unpack[UpdateMedicalVocabularyRequestTypeDef]
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        Updates an existing custom medical vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/update_medical_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#update_medical_vocabulary)
        """

    def update_vocabulary(
        self, **kwargs: Unpack[UpdateVocabularyRequestTypeDef]
    ) -> UpdateVocabularyResponseTypeDef:
        """
        Updates an existing custom vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/update_vocabulary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#update_vocabulary)
        """

    def update_vocabulary_filter(
        self, **kwargs: Unpack[UpdateVocabularyFilterRequestTypeDef]
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        Updates an existing custom vocabulary filter with a new list of words.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/update_vocabulary_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client/#update_vocabulary_filter)
        """
