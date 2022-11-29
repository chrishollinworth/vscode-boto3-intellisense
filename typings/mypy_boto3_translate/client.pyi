"""
Type annotations for translate service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_translate import TranslateClient

    client: TranslateClient = boto3.client("translate")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import DisplayLanguageCodeType, TerminologyDataFormatType
from .paginator import ListTerminologiesPaginator
from .type_defs import (
    CreateParallelDataResponseTypeDef,
    DeleteParallelDataResponseTypeDef,
    DescribeTextTranslationJobResponseTypeDef,
    EncryptionKeyTypeDef,
    GetParallelDataResponseTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyResponseTypeDef,
    InputDataConfigTypeDef,
    ListLanguagesResponseTypeDef,
    ListParallelDataResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTerminologiesResponseTypeDef,
    ListTextTranslationJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    ParallelDataConfigTypeDef,
    StartTextTranslationJobResponseTypeDef,
    StopTextTranslationJobResponseTypeDef,
    TagTypeDef,
    TerminologyDataTypeDef,
    TextTranslationJobFilterTypeDef,
    TranslateTextResponseTypeDef,
    TranslationSettingsTypeDef,
    UpdateParallelDataResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TranslateClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TranslateClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#close)
        """
    def create_parallel_data(
        self,
        *,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateParallelDataResponseTypeDef:
        """
        Creates a parallel data resource in Amazon Translate by importing an input file
        from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.create_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#create_parallel_data)
        """
    def delete_parallel_data(self, *, Name: str) -> DeleteParallelDataResponseTypeDef:
        """
        Deletes a parallel data resource in Amazon Translate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.delete_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#delete_parallel_data)
        """
    def delete_terminology(self, *, Name: str) -> None:
        """
        A synchronous action that deletes a custom terminology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.delete_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#delete_terminology)
        """
    def describe_text_translation_job(
        self, *, JobId: str
    ) -> DescribeTextTranslationJobResponseTypeDef:
        """
        Gets the properties associated with an asynchronous batch translation job
        including name, ID, status, source and target languages, input/output S3
        buckets, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.describe_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#describe_text_translation_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#generate_presigned_url)
        """
    def get_parallel_data(self, *, Name: str) -> GetParallelDataResponseTypeDef:
        """
        Provides information about a parallel data resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.get_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#get_parallel_data)
        """
    def get_terminology(
        self, *, Name: str, TerminologyDataFormat: TerminologyDataFormatType = None
    ) -> GetTerminologyResponseTypeDef:
        """
        Retrieves a custom terminology.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.get_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#get_terminology)
        """
    def import_terminology(
        self,
        *,
        Name: str,
        MergeStrategy: Literal["OVERWRITE"],
        TerminologyData: "TerminologyDataTypeDef",
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportTerminologyResponseTypeDef:
        """
        Creates or updates a custom terminology, depending on whether one already exists
        for the given terminology name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.import_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#import_terminology)
        """
    def list_languages(
        self,
        *,
        DisplayLanguageCode: DisplayLanguageCodeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLanguagesResponseTypeDef:
        """
        Provides a list of languages (RFC-5646 codes and names) that Amazon Translate
        supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.list_languages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list_languages)
        """
    def list_parallel_data(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListParallelDataResponseTypeDef:
        """
        Provides a list of your parallel data resources in Amazon Translate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.list_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list_parallel_data)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given Amazon Translate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list_tags_for_resource)
        """
    def list_terminologies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListTerminologiesResponseTypeDef:
        """
        Provides a list of custom terminologies associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.list_terminologies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list_terminologies)
        """
    def list_text_translation_jobs(
        self,
        *,
        Filter: "TextTranslationJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTextTranslationJobsResponseTypeDef:
        """
        Gets a list of the batch translation jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.list_text_translation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list_text_translation_jobs)
        """
    def start_text_translation_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        SourceLanguageCode: str,
        TargetLanguageCodes: List[str],
        ClientToken: str,
        JobName: str = None,
        TerminologyNames: List[str] = None,
        ParallelDataNames: List[str] = None,
        Settings: "TranslationSettingsTypeDef" = None
    ) -> StartTextTranslationJobResponseTypeDef:
        """
        Starts an asynchronous batch translation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.start_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#start_text_translation_job)
        """
    def stop_text_translation_job(self, *, JobId: str) -> StopTextTranslationJobResponseTypeDef:
        """
        Stops an asynchronous batch translation job that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.stop_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#stop_text_translation_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates a specific tag with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#tag_resource)
        """
    def translate_text(
        self,
        *,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: List[str] = None,
        Settings: "TranslationSettingsTypeDef" = None
    ) -> TranslateTextResponseTypeDef:
        """
        Translates input text from the source language to the target language.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.translate_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#translate_text)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a specific tag associated with an Amazon Translate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#untag_resource)
        """
    def update_parallel_data(
        self,
        *,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None
    ) -> UpdateParallelDataResponseTypeDef:
        """
        Updates a previously created parallel data resource by importing a new input
        file from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Client.update_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#update_parallel_data)
        """
    def get_paginator(
        self, operation_name: Literal["list_terminologies"]
    ) -> ListTerminologiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/translate.html#Translate.Paginator.ListTerminologies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators.html#listterminologiespaginator)
        """
