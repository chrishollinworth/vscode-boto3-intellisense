"""
Main interface for compute-optimizer-automation service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_compute_optimizer_automation import (
        Client,
        ComputeOptimizerAutomationClient,
        ListAccountsPaginator,
        ListAutomationEventStepsPaginator,
        ListAutomationEventSummariesPaginator,
        ListAutomationEventsPaginator,
        ListAutomationRulePreviewPaginator,
        ListAutomationRulePreviewSummariesPaginator,
        ListAutomationRulesPaginator,
        ListRecommendedActionSummariesPaginator,
        ListRecommendedActionsPaginator,
    )

    session = Session()
    client: ComputeOptimizerAutomationClient = session.client("compute-optimizer-automation")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_automation_event_steps_paginator: ListAutomationEventStepsPaginator = client.get_paginator("list_automation_event_steps")
    list_automation_event_summaries_paginator: ListAutomationEventSummariesPaginator = client.get_paginator("list_automation_event_summaries")
    list_automation_events_paginator: ListAutomationEventsPaginator = client.get_paginator("list_automation_events")
    list_automation_rule_preview_paginator: ListAutomationRulePreviewPaginator = client.get_paginator("list_automation_rule_preview")
    list_automation_rule_preview_summaries_paginator: ListAutomationRulePreviewSummariesPaginator = client.get_paginator("list_automation_rule_preview_summaries")
    list_automation_rules_paginator: ListAutomationRulesPaginator = client.get_paginator("list_automation_rules")
    list_recommended_action_summaries_paginator: ListRecommendedActionSummariesPaginator = client.get_paginator("list_recommended_action_summaries")
    list_recommended_actions_paginator: ListRecommendedActionsPaginator = client.get_paginator("list_recommended_actions")
    ```
"""

from .client import ComputeOptimizerAutomationClient
from .paginator import (
    ListAccountsPaginator,
    ListAutomationEventsPaginator,
    ListAutomationEventStepsPaginator,
    ListAutomationEventSummariesPaginator,
    ListAutomationRulePreviewPaginator,
    ListAutomationRulePreviewSummariesPaginator,
    ListAutomationRulesPaginator,
    ListRecommendedActionsPaginator,
    ListRecommendedActionSummariesPaginator,
)

Client = ComputeOptimizerAutomationClient

__all__ = (
    "Client",
    "ComputeOptimizerAutomationClient",
    "ListAccountsPaginator",
    "ListAutomationEventStepsPaginator",
    "ListAutomationEventSummariesPaginator",
    "ListAutomationEventsPaginator",
    "ListAutomationRulePreviewPaginator",
    "ListAutomationRulePreviewSummariesPaginator",
    "ListAutomationRulesPaginator",
    "ListRecommendedActionSummariesPaginator",
    "ListRecommendedActionsPaginator",
)
