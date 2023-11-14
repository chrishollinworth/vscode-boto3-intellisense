"""
Type annotations for textract service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_textract import TextractClient
    from mypy_boto3_textract.paginator import (
        ListAdapterVersionsPaginator,
        ListAdaptersPaginator,
    )

    client: TextractClient = boto3.client("textract")

    list_adapter_versions_paginator: ListAdapterVersionsPaginator = client.get_paginator("list_adapter_versions")
    list_adapters_paginator: ListAdaptersPaginator = client.get_paginator("list_adapters")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAdaptersResponseTypeDef,
    ListAdapterVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListAdapterVersionsPaginator", "ListAdaptersPaginator")

class ListAdapterVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/textract.html#Textract.Paginator.ListAdapterVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/paginators.html#listadapterversionspaginator)
    """

    def paginate(
        self,
        *,
        AdapterId: str = None,
        AfterCreationTime: Union[datetime, str] = None,
        BeforeCreationTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAdapterVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/textract.html#Textract.Paginator.ListAdapterVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/paginators.html#listadapterversionspaginator)
        """

class ListAdaptersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/textract.html#Textract.Paginator.ListAdapters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/paginators.html#listadapterspaginator)
    """

    def paginate(
        self,
        *,
        AfterCreationTime: Union[datetime, str] = None,
        BeforeCreationTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAdaptersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/textract.html#Textract.Paginator.ListAdapters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/paginators.html#listadapterspaginator)
        """
