# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
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

from botocore.client import ClientMeta

from mypy_boto3_budgets.paginator import (
    DescribeBudgetActionHistoriesPaginator,
    DescribeBudgetActionsForAccountPaginator,
    DescribeBudgetActionsForBudgetPaginator,
    DescribeBudgetPerformanceHistoryPaginator,
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)
from mypy_boto3_budgets.type_defs import (
    ActionThresholdTypeDef,
    BudgetTypeDef,
    CreateBudgetActionResponseTypeDef,
    DefinitionTypeDef,
    DeleteBudgetActionResponseTypeDef,
    DescribeBudgetActionHistoriesResponseTypeDef,
    DescribeBudgetActionResponseTypeDef,
    DescribeBudgetActionsForAccountResponseTypeDef,
    DescribeBudgetActionsForBudgetResponseTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetResponseTypeDef,
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    ExecuteBudgetActionResponseTypeDef,
    NotificationTypeDef,
    NotificationWithSubscribersTypeDef,
    SubscriberTypeDef,
    TimePeriodTypeDef,
    UpdateBudgetActionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BudgetsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreationLimitExceededException: Type[BotocoreClientError]
    DuplicateRecordException: Type[BotocoreClientError]
    ExpiredNextTokenException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLockedException: Type[BotocoreClientError]


class BudgetsClient:
    """
    [Budgets.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.can_paginate)
        """

    def create_budget(
        self,
        AccountId: str,
        Budget: "BudgetTypeDef",
        NotificationsWithSubscribers: List[NotificationWithSubscribersTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.create_budget)
        """

    def create_budget_action(
        self,
        AccountId: str,
        BudgetName: str,
        NotificationType: Literal["ACTUAL", "FORECASTED"],
        ActionType: Literal["APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"],
        ActionThreshold: "ActionThresholdTypeDef",
        Definition: "DefinitionTypeDef",
        ExecutionRoleArn: str,
        ApprovalModel: Literal["AUTOMATIC", "MANUAL"],
        Subscribers: List["SubscriberTypeDef"],
    ) -> CreateBudgetActionResponseTypeDef:
        """
        [Client.create_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.create_budget_action)
        """

    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscribers: List["SubscriberTypeDef"],
    ) -> Dict[str, Any]:
        """
        [Client.create_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.create_notification)
        """

    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.create_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.create_subscriber)
        """

    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        [Client.delete_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.delete_budget)
        """

    def delete_budget_action(
        self, AccountId: str, BudgetName: str, ActionId: str
    ) -> DeleteBudgetActionResponseTypeDef:
        """
        [Client.delete_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.delete_budget_action)
        """

    def delete_notification(
        self, AccountId: str, BudgetName: str, Notification: "NotificationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.delete_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.delete_notification)
        """

    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.delete_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        """

    def describe_budget(self, AccountId: str, BudgetName: str) -> DescribeBudgetResponseTypeDef:
        """
        [Client.describe_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget)
        """

    def describe_budget_action(
        self, AccountId: str, BudgetName: str, ActionId: str
    ) -> DescribeBudgetActionResponseTypeDef:
        """
        [Client.describe_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget_action)
        """

    def describe_budget_action_histories(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBudgetActionHistoriesResponseTypeDef:
        """
        [Client.describe_budget_action_histories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget_action_histories)
        """

    def describe_budget_actions_for_account(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForAccountResponseTypeDef:
        """
        [Client.describe_budget_actions_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_account)
        """

    def describe_budget_actions_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForBudgetResponseTypeDef:
        """
        [Client.describe_budget_actions_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_budget)
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
        [Client.describe_budget_performance_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        """

    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        [Client.describe_budgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_budgets)
        """

    def describe_notifications_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        [Client.describe_notifications_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
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
        [Client.describe_subscribers_for_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        """

    def execute_budget_action(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        ExecutionType: Literal[
            "APPROVE_BUDGET_ACTION",
            "RETRY_BUDGET_ACTION",
            "REVERSE_BUDGET_ACTION",
            "RESET_BUDGET_ACTION",
        ],
    ) -> ExecuteBudgetActionResponseTypeDef:
        """
        [Client.execute_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.execute_budget_action)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        """

    def update_budget(self, AccountId: str, NewBudget: "BudgetTypeDef") -> Dict[str, Any]:
        """
        [Client.update_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.update_budget)
        """

    def update_budget_action(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        NotificationType: Literal["ACTUAL", "FORECASTED"] = None,
        ActionThreshold: "ActionThresholdTypeDef" = None,
        Definition: "DefinitionTypeDef" = None,
        ExecutionRoleArn: str = None,
        ApprovalModel: Literal["AUTOMATIC", "MANUAL"] = None,
        Subscribers: List["SubscriberTypeDef"] = None,
    ) -> UpdateBudgetActionResponseTypeDef:
        """
        [Client.update_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.update_budget_action)
        """

    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: "NotificationTypeDef",
        NewNotification: "NotificationTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.update_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.update_notification)
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
        [Client.update_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Client.update_subscriber)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_action_histories"]
    ) -> DescribeBudgetActionHistoriesPaginator:
        """
        [Paginator.DescribeBudgetActionHistories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_account"]
    ) -> DescribeBudgetActionsForAccountPaginator:
        """
        [Paginator.DescribeBudgetActionsForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_budget"]
    ) -> DescribeBudgetActionsForBudgetPaginator:
        """
        [Paginator.DescribeBudgetActionsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_performance_history"]
    ) -> DescribeBudgetPerformanceHistoryPaginator:
        """
        [Paginator.DescribeBudgetPerformanceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> DescribeBudgetsPaginator:
        """
        [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> DescribeNotificationsForBudgetPaginator:
        """
        [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> DescribeSubscribersForNotificationPaginator:
        """
        [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
        """
