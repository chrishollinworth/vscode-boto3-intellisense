# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for events service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_events import EventBridgeClient
    from mypy_boto3_events.paginator import (
        ListRuleNamesByTargetPaginator,
        ListRulesPaginator,
        ListTargetsByRulePaginator,
    )

    client: EventBridgeClient = boto3.client("events")

    list_rule_names_by_target_paginator: ListRuleNamesByTargetPaginator = client.get_paginator("list_rule_names_by_target")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_targets_by_rule_paginator: ListTargetsByRulePaginator = client.get_paginator("list_targets_by_rule")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_events.type_defs import (
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
    """

    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRuleNamesByTargetResponseTypeDef]:
        """
        [ListRuleNamesByTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRules)
    """

    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRulesResponseTypeDef]:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListRules.paginate)
        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
    """

    def paginate(
        self, Rule: str, EventBusName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsByRuleResponseTypeDef]:
        """
        [ListTargetsByRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        """
