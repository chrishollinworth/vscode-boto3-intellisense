"""
Main interface for budgets service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_budgets import (
        BudgetsClient,
        Client,
        DescribeBudgetActionHistoriesPaginator,
        DescribeBudgetActionsForAccountPaginator,
        DescribeBudgetActionsForBudgetPaginator,
        DescribeBudgetNotificationsForAccountPaginator,
        DescribeBudgetPerformanceHistoryPaginator,
        DescribeBudgetsPaginator,
        DescribeNotificationsForBudgetPaginator,
        DescribeSubscribersForNotificationPaginator,
    )

    session = Session()
    client: BudgetsClient = session.client("budgets")

    describe_budget_action_histories_paginator: DescribeBudgetActionHistoriesPaginator = client.get_paginator("describe_budget_action_histories")
    describe_budget_actions_for_account_paginator: DescribeBudgetActionsForAccountPaginator = client.get_paginator("describe_budget_actions_for_account")
    describe_budget_actions_for_budget_paginator: DescribeBudgetActionsForBudgetPaginator = client.get_paginator("describe_budget_actions_for_budget")
    describe_budget_notifications_for_account_paginator: DescribeBudgetNotificationsForAccountPaginator = client.get_paginator("describe_budget_notifications_for_account")
    describe_budget_performance_history_paginator: DescribeBudgetPerformanceHistoryPaginator = client.get_paginator("describe_budget_performance_history")
    describe_budgets_paginator: DescribeBudgetsPaginator = client.get_paginator("describe_budgets")
    describe_notifications_for_budget_paginator: DescribeNotificationsForBudgetPaginator = client.get_paginator("describe_notifications_for_budget")
    describe_subscribers_for_notification_paginator: DescribeSubscribersForNotificationPaginator = client.get_paginator("describe_subscribers_for_notification")
    ```
"""

from .client import BudgetsClient
from .paginator import (
    DescribeBudgetActionHistoriesPaginator,
    DescribeBudgetActionsForAccountPaginator,
    DescribeBudgetActionsForBudgetPaginator,
    DescribeBudgetNotificationsForAccountPaginator,
    DescribeBudgetPerformanceHistoryPaginator,
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)

Client = BudgetsClient

__all__ = (
    "BudgetsClient",
    "Client",
    "DescribeBudgetActionHistoriesPaginator",
    "DescribeBudgetActionsForAccountPaginator",
    "DescribeBudgetActionsForBudgetPaginator",
    "DescribeBudgetNotificationsForAccountPaginator",
    "DescribeBudgetPerformanceHistoryPaginator",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)
