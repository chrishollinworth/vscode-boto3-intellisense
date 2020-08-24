# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for translate service client

Usage::

    ```python
    import boto3
    from mypy_boto3_translate import TranslateClient

    client: TranslateClient = boto3.client("translate")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_translate.paginator import ListTerminologiesPaginator
from mypy_boto3_translate.type_defs import (
    DescribeTextTranslationJobResponseTypeDef,
    EncryptionKeyTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyResponseTypeDef,
    InputDataConfigTypeDef,
    ListTerminologiesResponseTypeDef,
    ListTextTranslationJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    StartTextTranslationJobResponseTypeDef,
    StopTextTranslationJobResponseTypeDef,
    TerminologyDataTypeDef,
    TextTranslationJobFilterTypeDef,
    TranslateTextResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranslateClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    DetectedLanguageLowConfidenceException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidFilterException: Type[Boto3ClientError]
    InvalidParameterValueException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    TextSizeLimitExceededException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    UnsupportedLanguagePairException: Type[Boto3ClientError]


class TranslateClient:
    """
    [Translate.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.can_paginate)
        """

    def delete_terminology(self, Name: str) -> None:
        """
        [Client.delete_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.delete_terminology)
        """

    def describe_text_translation_job(
        self, JobId: str
    ) -> DescribeTextTranslationJobResponseTypeDef:
        """
        [Client.describe_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.describe_text_translation_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.generate_presigned_url)
        """

    def get_terminology(
        self, Name: str, TerminologyDataFormat: Literal["CSV", "TMX"]
    ) -> GetTerminologyResponseTypeDef:
        """
        [Client.get_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.get_terminology)
        """

    def import_terminology(
        self,
        Name: str,
        MergeStrategy: Literal["OVERWRITE"],
        TerminologyData: TerminologyDataTypeDef,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
    ) -> ImportTerminologyResponseTypeDef:
        """
        [Client.import_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.import_terminology)
        """

    def list_terminologies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListTerminologiesResponseTypeDef:
        """
        [Client.list_terminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.list_terminologies)
        """

    def list_text_translation_jobs(
        self,
        Filter: TextTranslationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTextTranslationJobsResponseTypeDef:
        """
        [Client.list_text_translation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.list_text_translation_jobs)
        """

    def start_text_translation_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        SourceLanguageCode: str,
        TargetLanguageCodes: List[str],
        ClientToken: str,
        JobName: str = None,
        TerminologyNames: List[str] = None,
    ) -> StartTextTranslationJobResponseTypeDef:
        """
        [Client.start_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.start_text_translation_job)
        """

    def stop_text_translation_job(self, JobId: str) -> StopTextTranslationJobResponseTypeDef:
        """
        [Client.stop_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.stop_text_translation_job)
        """

    def translate_text(
        self,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: List[str] = None,
    ) -> TranslateTextResponseTypeDef:
        """
        [Client.translate_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Client.translate_text)
        """

    def get_paginator(
        self, operation_name: Literal["list_terminologies"]
    ) -> ListTerminologiesPaginator:
        """
        [Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/translate.html#Translate.Paginator.ListTerminologies)
        """
