# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for budgets service client

Usage::

    ```python
    import boto3
    from mypy_boto3_budgets import BudgetsClient

    client: BudgetsClient = boto3.client("budgets")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_budgets.paginator import (
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)
from mypy_boto3_budgets.type_defs import (
    BudgetTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetResponseTypeDef,
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    NotificationTypeDef,
    NotificationWithSubscribersTypeDef,
    SubscriberTypeDef,
    TimePeriodTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BudgetsClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    CreationLimitExceededException: Type[Boto3ClientError]
    DuplicateRecordException: Type[Boto3ClientError]
    ExpiredNextTokenException: Type[Boto3ClientError]
    InternalErrorException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]


class BudgetsClient:
    """
    [Budgets.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.can_paginate)
        """

    def create_budget(
        self,
        AccountId: str,
        Budget: "BudgetTypeDef",
        NotificationsWithSubscribers: List[NotificationWithSubscribersTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.create_budget)
        """

    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscribers: List["SubscriberTypeDef"],
    ) -> Dict[str, Any]:
        """
        [Client.create_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.create_notification)
        """

    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.create_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.create_subscriber)
        """

    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        [Client.delete_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.delete_budget)
        """

    def delete_notification(
        self, AccountId: str, BudgetName: str, Notification: "NotificationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.delete_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.delete_notification)
        """

    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.delete_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        """

    def describe_budget(self, AccountId: str, BudgetName: str) -> DescribeBudgetResponseTypeDef:
        """
        [Client.describe_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.describe_budget)
        """

    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        [Client.describe_budget_performance_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        """

    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        [Client.describe_budgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.describe_budgets)
        """

    def describe_notifications_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        [Client.describe_notifications_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
        """

    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSubscribersForNotificationResponseTypeDef:
        """
        [Client.describe_subscribers_for_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        """

    def update_budget(self, AccountId: str, NewBudget: "BudgetTypeDef") -> Dict[str, Any]:
        """
        [Client.update_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.update_budget)
        """

    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: "NotificationTypeDef",
        NewNotification: "NotificationTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.update_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.update_notification)
        """

    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        OldSubscriber: "SubscriberTypeDef",
        NewSubscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.update_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Client.update_subscriber)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> DescribeBudgetsPaginator:
        """
        [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> DescribeNotificationsForBudgetPaginator:
        """
        [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> DescribeSubscribersForNotificationPaginator:
        """
        [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
