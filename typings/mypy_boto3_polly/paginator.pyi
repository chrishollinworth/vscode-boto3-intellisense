"""
Type annotations for polly service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_polly.client import PollyClient
    from mypy_boto3_polly.paginator import (
        DescribeVoicesPaginator,
        ListLexiconsPaginator,
        ListSpeechSynthesisTasksPaginator,
    )

    session = Session()
    client: PollyClient = session.client("polly")

    describe_voices_paginator: DescribeVoicesPaginator = client.get_paginator("describe_voices")
    list_lexicons_paginator: ListLexiconsPaginator = client.get_paginator("list_lexicons")
    list_speech_synthesis_tasks_paginator: ListSpeechSynthesisTasksPaginator = client.get_paginator("list_speech_synthesis_tasks")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeVoicesInputPaginateTypeDef,
    DescribeVoicesOutputTypeDef,
    ListLexiconsInputPaginateTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksInputPaginateTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeVoicesPaginator", "ListLexiconsPaginator", "ListSpeechSynthesisTasksPaginator")

if TYPE_CHECKING:
    _DescribeVoicesPaginatorBase = Paginator[DescribeVoicesOutputTypeDef]
else:
    _DescribeVoicesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVoicesPaginator(_DescribeVoicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/DescribeVoices.html#Polly.Paginator.DescribeVoices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#describevoicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVoicesInputPaginateTypeDef]
    ) -> PageIterator[DescribeVoicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/DescribeVoices.html#Polly.Paginator.DescribeVoices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#describevoicespaginator)
        """

if TYPE_CHECKING:
    _ListLexiconsPaginatorBase = Paginator[ListLexiconsOutputTypeDef]
else:
    _ListLexiconsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLexiconsPaginator(_ListLexiconsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/ListLexicons.html#Polly.Paginator.ListLexicons)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#listlexiconspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLexiconsInputPaginateTypeDef]
    ) -> PageIterator[ListLexiconsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/ListLexicons.html#Polly.Paginator.ListLexicons.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#listlexiconspaginator)
        """

if TYPE_CHECKING:
    _ListSpeechSynthesisTasksPaginatorBase = Paginator[ListSpeechSynthesisTasksOutputTypeDef]
else:
    _ListSpeechSynthesisTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListSpeechSynthesisTasksPaginator(_ListSpeechSynthesisTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/ListSpeechSynthesisTasks.html#Polly.Paginator.ListSpeechSynthesisTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#listspeechsynthesistaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSpeechSynthesisTasksInputPaginateTypeDef]
    ) -> PageIterator[ListSpeechSynthesisTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/paginator/ListSpeechSynthesisTasks.html#Polly.Paginator.ListSpeechSynthesisTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/paginators/#listspeechsynthesistaskspaginator)
        """
