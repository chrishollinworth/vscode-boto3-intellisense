"""
Type annotations for translate service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_translate.client import TranslateClient
    from mypy_boto3_translate.paginator import (
        ListTerminologiesPaginator,
    )

    session = Session()
    client: TranslateClient = session.client("translate")

    list_terminologies_paginator: ListTerminologiesPaginator = client.get_paginator("list_terminologies")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListTerminologiesRequestPaginateTypeDef, ListTerminologiesResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListTerminologiesPaginator",)

if TYPE_CHECKING:
    _ListTerminologiesPaginatorBase = Paginator[ListTerminologiesResponseTypeDef]
else:
    _ListTerminologiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTerminologiesPaginator(_ListTerminologiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/paginator/ListTerminologies.html#Translate.Paginator.ListTerminologies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators/#listterminologiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTerminologiesRequestPaginateTypeDef]
    ) -> PageIterator[ListTerminologiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate/paginator/ListTerminologies.html#Translate.Paginator.ListTerminologies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators/#listterminologiespaginator)
        """
