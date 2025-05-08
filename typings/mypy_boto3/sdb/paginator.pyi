"""
Type annotations for sdb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sdb.client import SimpleDBClient
    from mypy_boto3_sdb.paginator import (
        ListDomainsPaginator,
        SelectPaginator,
    )

    session = Session()
    client: SimpleDBClient = session.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDomainsRequestPaginateTypeDef,
    ListDomainsResultTypeDef,
    SelectRequestPaginateTypeDef,
    SelectResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListDomainsPaginator", "SelectPaginator")

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsResultTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/paginator/ListDomains.html#SimpleDB.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/paginator/ListDomains.html#SimpleDB.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _SelectPaginatorBase = Paginator[SelectResultTypeDef]
else:
    _SelectPaginatorBase = Paginator  # type: ignore[assignment]

class SelectPaginator(_SelectPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/paginator/Select.html#SimpleDB.Paginator.Select)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators/#selectpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SelectRequestPaginateTypeDef]
    ) -> PageIterator[SelectResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb/paginator/Select.html#SimpleDB.Paginator.Select.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/paginators/#selectpaginator)
        """
