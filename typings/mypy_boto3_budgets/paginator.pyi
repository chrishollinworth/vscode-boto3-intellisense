"""
Type annotations for budgets service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_budgets.client import BudgetsClient
    from mypy_boto3_budgets.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBudgetActionHistoriesRequestPaginateTypeDef,
    DescribeBudgetActionHistoriesResponseTypeDef,
    DescribeBudgetActionsForAccountRequestPaginateTypeDef,
    DescribeBudgetActionsForAccountResponseTypeDef,
    DescribeBudgetActionsForBudgetRequestPaginateTypeDef,
    DescribeBudgetActionsForBudgetResponseTypeDef,
    DescribeBudgetNotificationsForAccountRequestPaginateTypeDef,
    DescribeBudgetNotificationsForAccountResponseTypeDef,
    DescribeBudgetPerformanceHistoryRequestPaginateTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetsRequestPaginateTypeDef,
    DescribeBudgetsResponsePaginatorTypeDef,
    DescribeNotificationsForBudgetRequestPaginateTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationRequestPaginateTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBudgetActionHistoriesPaginator",
    "DescribeBudgetActionsForAccountPaginator",
    "DescribeBudgetActionsForBudgetPaginator",
    "DescribeBudgetNotificationsForAccountPaginator",
    "DescribeBudgetPerformanceHistoryPaginator",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)

if TYPE_CHECKING:
    _DescribeBudgetActionHistoriesPaginatorBase = Paginator[
        DescribeBudgetActionHistoriesResponseTypeDef
    ]
else:
    _DescribeBudgetActionHistoriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetActionHistoriesPaginator(_DescribeBudgetActionHistoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionHistories.html#Budgets.Paginator.DescribeBudgetActionHistories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionhistoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetActionHistoriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetActionHistoriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionHistories.html#Budgets.Paginator.DescribeBudgetActionHistories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionhistoriespaginator)
        """

if TYPE_CHECKING:
    _DescribeBudgetActionsForAccountPaginatorBase = Paginator[
        DescribeBudgetActionsForAccountResponseTypeDef
    ]
else:
    _DescribeBudgetActionsForAccountPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetActionsForAccountPaginator(_DescribeBudgetActionsForAccountPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionsForAccount.html#Budgets.Paginator.DescribeBudgetActionsForAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionsforaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetActionsForAccountRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetActionsForAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionsForAccount.html#Budgets.Paginator.DescribeBudgetActionsForAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionsforaccountpaginator)
        """

if TYPE_CHECKING:
    _DescribeBudgetActionsForBudgetPaginatorBase = Paginator[
        DescribeBudgetActionsForBudgetResponseTypeDef
    ]
else:
    _DescribeBudgetActionsForBudgetPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetActionsForBudgetPaginator(_DescribeBudgetActionsForBudgetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionsForBudget.html#Budgets.Paginator.DescribeBudgetActionsForBudget)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionsforbudgetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetActionsForBudgetRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetActionsForBudgetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetActionsForBudget.html#Budgets.Paginator.DescribeBudgetActionsForBudget.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetactionsforbudgetpaginator)
        """

if TYPE_CHECKING:
    _DescribeBudgetNotificationsForAccountPaginatorBase = Paginator[
        DescribeBudgetNotificationsForAccountResponseTypeDef
    ]
else:
    _DescribeBudgetNotificationsForAccountPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetNotificationsForAccountPaginator(
    _DescribeBudgetNotificationsForAccountPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetNotificationsForAccount.html#Budgets.Paginator.DescribeBudgetNotificationsForAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetnotificationsforaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetNotificationsForAccountRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetNotificationsForAccountResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetNotificationsForAccount.html#Budgets.Paginator.DescribeBudgetNotificationsForAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetnotificationsforaccountpaginator)
        """

if TYPE_CHECKING:
    _DescribeBudgetPerformanceHistoryPaginatorBase = Paginator[
        DescribeBudgetPerformanceHistoryResponseTypeDef
    ]
else:
    _DescribeBudgetPerformanceHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetPerformanceHistoryPaginator(_DescribeBudgetPerformanceHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetPerformanceHistory.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetperformancehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetPerformanceHistoryRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetPerformanceHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgetPerformanceHistory.html#Budgets.Paginator.DescribeBudgetPerformanceHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetperformancehistorypaginator)
        """

if TYPE_CHECKING:
    _DescribeBudgetsPaginatorBase = Paginator[DescribeBudgetsResponsePaginatorTypeDef]
else:
    _DescribeBudgetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBudgetsPaginator(_DescribeBudgetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgets.html#Budgets.Paginator.DescribeBudgets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBudgetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBudgetsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeBudgets.html#Budgets.Paginator.DescribeBudgets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describebudgetspaginator)
        """

if TYPE_CHECKING:
    _DescribeNotificationsForBudgetPaginatorBase = Paginator[
        DescribeNotificationsForBudgetResponseTypeDef
    ]
else:
    _DescribeNotificationsForBudgetPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNotificationsForBudgetPaginator(_DescribeNotificationsForBudgetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeNotificationsForBudget.html#Budgets.Paginator.DescribeNotificationsForBudget)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describenotificationsforbudgetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNotificationsForBudgetRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNotificationsForBudgetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeNotificationsForBudget.html#Budgets.Paginator.DescribeNotificationsForBudget.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describenotificationsforbudgetpaginator)
        """

if TYPE_CHECKING:
    _DescribeSubscribersForNotificationPaginatorBase = Paginator[
        DescribeSubscribersForNotificationResponseTypeDef
    ]
else:
    _DescribeSubscribersForNotificationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSubscribersForNotificationPaginator(_DescribeSubscribersForNotificationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeSubscribersForNotification.html#Budgets.Paginator.DescribeSubscribersForNotification)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describesubscribersfornotificationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubscribersForNotificationRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSubscribersForNotificationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets/paginator/DescribeSubscribersForNotification.html#Budgets.Paginator.DescribeSubscribersForNotification.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators/#describesubscribersfornotificationpaginator)
        """
