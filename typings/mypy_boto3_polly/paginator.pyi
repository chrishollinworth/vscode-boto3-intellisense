"""
Type annotations for polly service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html)

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

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import EngineType, LanguageCodeType, TaskStatusType
from .type_defs import (
    DescribeVoicesOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeVoicesPaginator", "ListLexiconsPaginator", "ListSpeechSynthesisTasksPaginator")

class DescribeVoicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.DescribeVoices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#describevoicespaginator)
    """

    def paginate(
        self,
        *,
        Engine: EngineType = None,
        LanguageCode: LanguageCodeType = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVoicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.DescribeVoices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#describevoicespaginator)
        """

class ListLexiconsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.ListLexicons)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#listlexiconspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLexiconsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.ListLexicons.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#listlexiconspaginator)
        """

class ListSpeechSynthesisTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#listspeechsynthesistaskspaginator)
    """

    def paginate(
        self, *, Status: TaskStatusType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpeechSynthesisTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators.html#listspeechsynthesistaskspaginator)
        """
