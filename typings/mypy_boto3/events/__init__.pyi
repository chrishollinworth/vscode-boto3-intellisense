"""
Main interface for events service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_events import (
        Client,
        EventBridgeClient,
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
