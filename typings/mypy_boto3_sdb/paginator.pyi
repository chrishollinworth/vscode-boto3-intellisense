"""
Type annotations for sdb service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sdb import SimpleDBClient
    from mypy_boto3_sdb.paginator import (
        ListDomainsPaginator,
        SelectPaginator,
    )

    client: SimpleDBClient = boto3.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListDomainsResultTypeDef, PaginatorConfigTypeDef, SelectResultTypeDef

__all__ = ("ListDomainsPaginator", "SelectPaginator")

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/sdb.html#SimpleDB.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#listdomainspaginator)
        """

class SelectPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/sdb.html#SimpleDB.Paginator.Select)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#selectpaginator)
    """

    def paginate(
        self,
        *,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SelectResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/sdb.html#SimpleDB.Paginator.Select.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators.html#selectpaginator)
        """
