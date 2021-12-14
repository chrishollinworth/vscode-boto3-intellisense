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
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListRulesResponseTypeDef, PaginatorConfigTypeDef, ResourceTagTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListRulesPaginator",)

class ListRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rbin.html#RecycleBin.Paginator.ListRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html#listrulespaginator)
    """

    def paginate(
        self,
        *,
        ResourceType: Literal["EBS_SNAPSHOT"],
        ResourceTags: List["ResourceTagTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/rbin.html#RecycleBin.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html#listrulespaginator)
        """
