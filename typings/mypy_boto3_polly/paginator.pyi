# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for polly service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_polly import PollyClient
    from mypy_boto3_polly.paginator import (
        DescribeVoicesPaginator,
        ListLexiconsPaginator,
        ListSpeechSynthesisTasksPaginator,
    )

    client: PollyClient = boto3.client("polly")

    describe_voices_paginator: DescribeVoicesPaginator = client.get_paginator("describe_voices")
    list_lexicons_paginator: ListLexiconsPaginator = client.get_paginator("list_lexicons")
    list_speech_synthesis_tasks_paginator: ListSpeechSynthesisTasksPaginator = client.get_paginator("list_speech_synthesis_tasks")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_polly.type_defs import (
    DescribeVoicesOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DescribeVoicesPaginator", "ListLexiconsPaginator", "ListSpeechSynthesisTasksPaginator")


class DescribeVoicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.DescribeVoices)
    """

    def paginate(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVoicesOutputTypeDef]:
        """
        [DescribeVoices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.DescribeVoices.paginate)
        """


class ListLexiconsPaginator(Boto3Paginator):
    """
    [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.ListLexicons)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLexiconsOutputTypeDef]:
        """
        [ListLexicons.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.ListLexicons.paginate)
        """


class ListSpeechSynthesisTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
    """

    def paginate(
        self,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSpeechSynthesisTasksOutputTypeDef]:
        """
        [ListSpeechSynthesisTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks.paginate)
        """
