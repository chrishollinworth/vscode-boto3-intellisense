"""
Type annotations for translate service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_translate.client import TranslateClient

    session = Session()
    client: TranslateClient = session.client("translate")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListTerminologiesPaginator
from .type_defs import (
    CreateParallelDataRequestTypeDef,
    CreateParallelDataResponseTypeDef,
    DeleteParallelDataRequestTypeDef,
    DeleteParallelDataResponseTypeDef,
    DeleteTerminologyRequestTypeDef,
    DescribeTextTranslationJobRequestTypeDef,
    DescribeTextTranslationJobResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetParallelDataRequestTypeDef,
    GetParallelDataResponseTypeDef,
    GetTerminologyRequestTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyRequestTypeDef,
    ImportTerminologyResponseTypeDef,
    ListLanguagesRequestTypeDef,
    ListLanguagesResponseTypeDef,
    ListParallelDataRequestTypeDef,
    ListParallelDataResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTerminologiesRequestTypeDef,
    ListTerminologiesResponseTypeDef,
    ListTextTranslationJobsRequestTypeDef,
    ListTextTranslationJobsResponseTypeDef,
    StartTextTranslationJobRequestTypeDef,
    StartTextTranslationJobResponseTypeDef,
    StopTextTranslationJobRequestTypeDef,
    StopTextTranslationJobResponseTypeDef,
    TagResourceRequestTypeDef,
    TranslateDocumentRequestTypeDef,
    TranslateDocumentResponseTypeDef,
    TranslateTextRequestTypeDef,
    TranslateTextResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateParallelDataRequestTypeDef,
    UpdateParallelDataResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("TranslateClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DetectedLanguageLowConfidenceException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedDisplayLanguageCodeException: Type[BotocoreClientError]
    UnsupportedLanguagePairException: Type[BotocoreClientError]

class TranslateClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TranslateClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#generate_presigned_url)
        """

    def create_parallel_data(
        self, **kwargs: Unpack[CreateParallelDataRequestTypeDef]
    ) -> CreateParallelDataResponseTypeDef:
        """
        Creates a parallel data resource in Amazon Translate by importing an input file
        from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/create_parallel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#create_parallel_data)
        """

    def delete_parallel_data(
        self, **kwargs: Unpack[DeleteParallelDataRequestTypeDef]
    ) -> DeleteParallelDataResponseTypeDef:
        """
        Deletes a parallel data resource in Amazon Translate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/delete_parallel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#delete_parallel_data)
        """

    def delete_terminology(
        self, **kwargs: Unpack[DeleteTerminologyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        A synchronous action that deletes a custom terminology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/delete_terminology.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#delete_terminology)
        """

    def describe_text_translation_job(
        self, **kwargs: Unpack[DescribeTextTranslationJobRequestTypeDef]
    ) -> DescribeTextTranslationJobResponseTypeDef:
        """
        Gets the properties associated with an asynchronous batch translation job
        including name, ID, status, source and target languages, input/output S3
        buckets, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/describe_text_translation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#describe_text_translation_job)
        """

    def get_parallel_data(
        self, **kwargs: Unpack[GetParallelDataRequestTypeDef]
    ) -> GetParallelDataResponseTypeDef:
        """
        Provides information about a parallel data resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/get_parallel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#get_parallel_data)
        """

    def get_terminology(
        self, **kwargs: Unpack[GetTerminologyRequestTypeDef]
    ) -> GetTerminologyResponseTypeDef:
        """
        Retrieves a custom terminology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/get_terminology.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#get_terminology)
        """

    def import_terminology(
        self, **kwargs: Unpack[ImportTerminologyRequestTypeDef]
    ) -> ImportTerminologyResponseTypeDef:
        """
        Creates or updates a custom terminology, depending on whether one already
        exists for the given terminology name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/import_terminology.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#import_terminology)
        """

    def list_languages(
        self, **kwargs: Unpack[ListLanguagesRequestTypeDef]
    ) -> ListLanguagesResponseTypeDef:
        """
        Provides a list of languages (RFC-5646 codes and names) that Amazon Translate
        supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/list_languages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#list_languages)
        """

    def list_parallel_data(
        self, **kwargs: Unpack[ListParallelDataRequestTypeDef]
    ) -> ListParallelDataResponseTypeDef:
        """
        Provides a list of your parallel data resources in Amazon Translate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/list_parallel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#list_parallel_data)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given Amazon Translate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#list_tags_for_resource)
        """

    def list_terminologies(
        self, **kwargs: Unpack[ListTerminologiesRequestTypeDef]
    ) -> ListTerminologiesResponseTypeDef:
        """
        Provides a list of custom terminologies associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/list_terminologies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#list_terminologies)
        """

    def list_text_translation_jobs(
        self, **kwargs: Unpack[ListTextTranslationJobsRequestTypeDef]
    ) -> ListTextTranslationJobsResponseTypeDef:
        """
        Gets a list of the batch translation jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/list_text_translation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#list_text_translation_jobs)
        """

    def start_text_translation_job(
        self, **kwargs: Unpack[StartTextTranslationJobRequestTypeDef]
    ) -> StartTextTranslationJobResponseTypeDef:
        """
        Starts an asynchronous batch translation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/start_text_translation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#start_text_translation_job)
        """

    def stop_text_translation_job(
        self, **kwargs: Unpack[StopTextTranslationJobRequestTypeDef]
    ) -> StopTextTranslationJobResponseTypeDef:
        """
        Stops an asynchronous batch translation job that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/stop_text_translation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#stop_text_translation_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates a specific tag with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#tag_resource)
        """

    def translate_document(
        self, **kwargs: Unpack[TranslateDocumentRequestTypeDef]
    ) -> TranslateDocumentResponseTypeDef:
        """
        Translates the input document from the source language to the target language.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/translate_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#translate_document)
        """

    def translate_text(
        self, **kwargs: Unpack[TranslateTextRequestTypeDef]
    ) -> TranslateTextResponseTypeDef:
        """
        Translates input text from the source language to the target language.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/translate_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#translate_text)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a specific tag associated with an Amazon Translate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#untag_resource)
        """

    def update_parallel_data(
        self, **kwargs: Unpack[UpdateParallelDataRequestTypeDef]
    ) -> UpdateParallelDataResponseTypeDef:
        """
        Updates a previously created parallel data resource by importing a new input
        file from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/update_parallel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#update_parallel_data)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_terminologies"]
    ) -> ListTerminologiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/client/#get_paginator)
        """
