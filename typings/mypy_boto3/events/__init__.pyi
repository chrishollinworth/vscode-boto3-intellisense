"""
Main interface for events service.

Usage::

    ```python
    import boto3
    from mypy_boto3_events import (
        Client,
        EventBridgeClient,
        ListRuleNamesByTargetPaginator,
        ListRulesPaginator,
        ListTargetsByRulePaginator,
    )

    session = boto3.Session()

    client: EventBridgeClient = boto3.client("events")
    session_client: EventBridgeClient = session.client("events")

    list_rule_names_by_target_paginator: ListRuleNamesByTargetPaginator = client.get_paginator("list_rule_names_by_target")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_targets_by_rule_paginator: ListTargetsByRulePaginator = client.get_paginator("list_targets_by_rule")
    ```
"""
from .client import EventBridgeClient
from .paginator import (
    ListRuleNamesByTargetPaginator,
    ListRulesPaginator,
    ListTargetsByRulePaginator,
)

Client = EventBridgeClient

__all__ = (
    "Client",
    "EventBridgeClient",
    "ListRuleNamesByTargetPaginator",
    "ListRulesPaginator",
    "ListTargetsByRulePaginator",
)
