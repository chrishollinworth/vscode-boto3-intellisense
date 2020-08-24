"""
Main interface for budgets service.

Usage::

    ```python
    import boto3
    from mypy_boto3_budgets import (
        BudgetsClient,
        Client,
        DescribeBudgetsPaginator,
        DescribeNotificationsForBudgetPaginator,
        DescribeSubscribersForNotificationPaginator,
    )

    session = boto3.Session()

    client: BudgetsClient = boto3.client("budgets")
    session_client: BudgetsClient = session.client("budgets")

    describe_budgets_paginator: DescribeBudgetsPaginator = client.get_paginator("describe_budgets")
    describe_notifications_for_budget_paginator: DescribeNotificationsForBudgetPaginator = client.get_paginator("describe_notifications_for_budget")
    describe_subscribers_for_notification_paginator: DescribeSubscribersForNotificationPaginator = client.get_paginator("describe_subscribers_for_notification")
    ```
"""
from mypy_boto3_budgets.client import BudgetsClient
from mypy_boto3_budgets.paginator import (
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)

Client = BudgetsClient


__all__ = (
    "BudgetsClient",
    "Client",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)
