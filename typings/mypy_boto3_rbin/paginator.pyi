"""
Type annotations for rbin service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rbin import RecycleBinClient
    from mypy_boto3_rbin.paginator import (
        ListRulesPaginator,
    )

    client: RecycleBinClient = boto3.client("rbin")

    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import LockStateType, ResourceTypeType
from .type_defs import ListRulesResponseTypeDef, PaginatorConfigTypeDef, ResourceTagTypeDef

__all__ = ("ListRulesPaginator",)

class ListRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rbin.html#RecycleBin.Paginator.ListRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html#listrulespaginator)
    """

    def paginate(
        self,
        *,
        ResourceType: ResourceTypeType,
        ResourceTags: List["ResourceTagTypeDef"] = None,
        LockState: LockStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/rbin.html#RecycleBin.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html#listrulespaginator)
        """
