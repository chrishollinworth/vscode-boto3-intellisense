"""
Type annotations for oam service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_oam import CloudWatchObservabilityAccessManagerClient
    from mypy_boto3_oam.paginator import (
        ListAttachedLinksPaginator,
        ListLinksPaginator,
        ListSinksPaginator,
    )

    client: CloudWatchObservabilityAccessManagerClient = boto3.client("oam")

    list_attached_links_paginator: ListAttachedLinksPaginator = client.get_paginator("list_attached_links")
    list_links_paginator: ListLinksPaginator = client.get_paginator("list_links")
    list_sinks_paginator: ListSinksPaginator = client.get_paginator("list_sinks")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAttachedLinksOutputTypeDef,
    ListLinksOutputTypeDef,
    ListSinksOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListAttachedLinksPaginator", "ListLinksPaginator", "ListSinksPaginator")

class ListAttachedLinksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListAttachedLinks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listattachedlinkspaginator)
    """

    def paginate(
        self, *, SinkIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedLinksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListAttachedLinks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listattachedlinkspaginator)
        """

class ListLinksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListLinks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listlinkspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLinksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListLinks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listlinkspaginator)
        """

class ListSinksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListSinks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listsinkspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSinksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListSinks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listsinkspaginator)
        """
