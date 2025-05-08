"""
Type annotations for events service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_events.client import EventBridgeClient
    from mypy_boto3_events.paginator import (
        ListRuleNamesByTargetPaginator,
        ListRulesPaginator,
        ListTargetsByRulePaginator,
    )

    session = Session()
    client: EventBridgeClient = session.client("events")

    list_rule_names_by_target_paginator: ListRuleNamesByTargetPaginator = client.get_paginator("list_rule_names_by_target")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_targets_by_rule_paginator: ListTargetsByRulePaginator = client.get_paginator("list_targets_by_rule")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListRuleNamesByTargetRequestPaginateTypeDef,
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesRequestPaginateTypeDef,
    ListRulesResponseTypeDef,
    ListTargetsByRuleRequestPaginateTypeDef,
    ListTargetsByRuleResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")

if TYPE_CHECKING:
    _ListRuleNamesByTargetPaginatorBase = Paginator[ListRuleNamesByTargetResponseTypeDef]
else:
    _ListRuleNamesByTargetPaginatorBase = Paginator  # type: ignore[assignment]

class ListRuleNamesByTargetPaginator(_ListRuleNamesByTargetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListRuleNamesByTarget.html#EventBridge.Paginator.ListRuleNamesByTarget)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listrulenamesbytargetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRuleNamesByTargetRequestPaginateTypeDef]
    ) -> PageIterator[ListRuleNamesByTargetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListRuleNamesByTarget.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listrulenamesbytargetpaginator)
        """

if TYPE_CHECKING:
    _ListRulesPaginatorBase = Paginator[ListRulesResponseTypeDef]
else:
    _ListRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPaginator(_ListRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListRules.html#EventBridge.Paginator.ListRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListRules.html#EventBridge.Paginator.ListRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listrulespaginator)
        """

if TYPE_CHECKING:
    _ListTargetsByRulePaginatorBase = Paginator[ListTargetsByRuleResponseTypeDef]
else:
    _ListTargetsByRulePaginatorBase = Paginator  # type: ignore[assignment]

class ListTargetsByRulePaginator(_ListTargetsByRulePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListTargetsByRule.html#EventBridge.Paginator.ListTargetsByRule)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listtargetsbyrulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTargetsByRuleRequestPaginateTypeDef]
    ) -> PageIterator[ListTargetsByRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events/paginator/ListTargetsByRule.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/paginators/#listtargetsbyrulepaginator)
        """
