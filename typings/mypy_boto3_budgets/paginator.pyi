# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for budgets service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_budgets import BudgetsClient
    from mypy_boto3_budgets.paginator import (
        DescribeBudgetActionHistoriesPaginator,
        DescribeBudgetActionsForAccountPaginator,
        DescribeBudgetActionsForBudgetPaginator,
        DescribeBudgetPerformanceHistoryPaginator,
        DescribeBudgetsPaginator,
        DescribeNotificationsForBudgetPaginator,
        DescribeSubscribersForNotificationPaginator,
    )

    client: BudgetsClient = boto3.client("budgets")

    describe_budget_action_histories_paginator: DescribeBudgetActionHistoriesPaginator = client.get_paginator("describe_budget_action_histories")
    describe_budget_actions_for_account_paginator: DescribeBudgetActionsForAccountPaginator = client.get_paginator("describe_budget_actions_for_account")
    describe_budget_actions_for_budget_paginator: DescribeBudgetActionsForBudgetPaginator = client.get_paginator("describe_budget_actions_for_budget")
    describe_budget_performance_history_paginator: DescribeBudgetPerformanceHistoryPaginator = client.get_paginator("describe_budget_performance_history")
    describe_budgets_paginator: DescribeBudgetsPaginator = client.get_paginator("describe_budgets")
    describe_notifications_for_budget_paginator: DescribeNotificationsForBudgetPaginator = client.get_paginator("describe_notifications_for_budget")
    describe_subscribers_for_notification_paginator: DescribeSubscribersForNotificationPaginator = client.get_paginator("describe_subscribers_for_notification")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_budgets.type_defs import (
    DescribeBudgetActionHistoriesResponseTypeDef,
    DescribeBudgetActionsForAccountResponseTypeDef,
    DescribeBudgetActionsForBudgetResponseTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    NotificationTypeDef,
    PaginatorConfigTypeDef,
    TimePeriodTypeDef,
)

__all__ = (
    "DescribeBudgetActionHistoriesPaginator",
    "DescribeBudgetActionsForAccountPaginator",
    "DescribeBudgetActionsForBudgetPaginator",
    "DescribeBudgetPerformanceHistoryPaginator",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)


class DescribeBudgetActionHistoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgetActionHistories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)
    """

    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBudgetActionHistoriesResponseTypeDef]:
        """
        [DescribeBudgetActionHistories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories.paginate)
        """


class DescribeBudgetActionsForAccountPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgetActionsForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)
    """

    def paginate(
        self, AccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetActionsForAccountResponseTypeDef]:
        """
        [DescribeBudgetActionsForAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount.paginate)
        """


class DescribeBudgetActionsForBudgetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgetActionsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)
    """

    def paginate(
        self, AccountId: str, BudgetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetActionsForBudgetResponseTypeDef]:
        """
        [DescribeBudgetActionsForBudget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget.paginate)
        """


class DescribeBudgetPerformanceHistoryPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgetPerformanceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)
    """

    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBudgetPerformanceHistoryResponseTypeDef]:
        """
        [DescribeBudgetPerformanceHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory.paginate)
        """


class DescribeBudgetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
    """

    def paginate(
        self, AccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetsResponseTypeDef]:
        """
        [DescribeBudgets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets.paginate)
        """


class DescribeNotificationsForBudgetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
    """

    def paginate(
        self, AccountId: str, BudgetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationsForBudgetResponseTypeDef]:
        """
        [DescribeNotificationsForBudget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget.paginate)
        """


class DescribeSubscribersForNotificationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
    """

    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSubscribersForNotificationResponseTypeDef]:
        """
        [DescribeSubscribersForNotification.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification.paginate)
        """
