"""
Type annotations for rbin service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rbin.client import RecycleBinClient
    from mypy_boto3_rbin.paginator import (
        ListRulesPaginator,
    )

    session = Session()
    client: RecycleBinClient = session.client("rbin")

    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListRulesRequestPaginateTypeDef, ListRulesResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRulesPaginator",)

if TYPE_CHECKING:
    _ListRulesPaginatorBase = Paginator[ListRulesResponseTypeDef]
else:
    _ListRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPaginator(_ListRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/paginator/ListRules.html#RecycleBin.Paginator.ListRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators/#listrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/paginator/ListRules.html#RecycleBin.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators/#listrulespaginator)
        """
