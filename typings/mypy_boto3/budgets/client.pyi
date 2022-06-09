"""
Type annotations for budgets service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_budgets import BudgetsClient

    client: BudgetsClient = boto3.client("budgets")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ActionTypeType, ApprovalModelType, ExecutionTypeType, NotificationTypeType
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
from .type_defs import (
    ActionThresholdTypeDef,
    BudgetTypeDef,
    CreateBudgetActionResponseTypeDef,
    DefinitionTypeDef,
    DeleteBudgetActionResponseTypeDef,
    DescribeBudgetActionHistoriesResponseTypeDef,
    DescribeBudgetActionResponseTypeDef,
    DescribeBudgetActionsForAccountResponseTypeDef,
    DescribeBudgetActionsForBudgetResponseTypeDef,
    DescribeBudgetNotificationsForAccountResponseTypeDef,
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

class BudgetsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BudgetsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#can_paginate)
        """
    def create_budget(
        self,
        *,
        AccountId: str,
        Budget: "BudgetTypeDef",
        NotificationsWithSubscribers: List["NotificationWithSubscribersTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a budget and, if included, notifications and subscribers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.create_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create_budget)
        """
    def create_budget_action(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        NotificationType: NotificationTypeType,
        ActionType: ActionTypeType,
        ActionThreshold: "ActionThresholdTypeDef",
        Definition: "DefinitionTypeDef",
        ExecutionRoleArn: str,
        ApprovalModel: ApprovalModelType,
        Subscribers: List["SubscriberTypeDef"]
    ) -> CreateBudgetActionResponseTypeDef:
        """
        Creates a budget action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.create_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create_budget_action)
        """
    def create_notification(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscribers: List["SubscriberTypeDef"]
    ) -> Dict[str, Any]:
        """
        Creates a notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.create_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create_notification)
        """
    def create_subscriber(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates a subscriber.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.create_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create_subscriber)
        """
    def delete_budget(self, *, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        Deletes a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.delete_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete_budget)
        """
    def delete_budget_action(
        self, *, AccountId: str, BudgetName: str, ActionId: str
    ) -> DeleteBudgetActionResponseTypeDef:
        """
        Deletes a budget action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.delete_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete_budget_action)
        """
    def delete_notification(
        self, *, AccountId: str, BudgetName: str, Notification: "NotificationTypeDef"
    ) -> Dict[str, Any]:
        """
        Deletes a notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.delete_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete_notification)
        """
    def delete_subscriber(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef"
    ) -> Dict[str, Any]:
        """
        Deletes a subscriber.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete_subscriber)
        """
    def describe_budget(self, *, AccountId: str, BudgetName: str) -> DescribeBudgetResponseTypeDef:
        """
        Describes a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget)
        """
    def describe_budget_action(
        self, *, AccountId: str, BudgetName: str, ActionId: str
    ) -> DescribeBudgetActionResponseTypeDef:
        """
        Describes a budget action detail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_action)
        """
    def describe_budget_action_histories(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeBudgetActionHistoriesResponseTypeDef:
        """
        Describes a budget action history detail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_action_histories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_action_histories)
        """
    def describe_budget_actions_for_account(
        self, *, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForAccountResponseTypeDef:
        """
        Describes all of the budget actions for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_actions_for_account)
        """
    def describe_budget_actions_for_budget(
        self, *, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForBudgetResponseTypeDef:
        """
        Describes all of the budget actions for a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_actions_for_budget)
        """
    def describe_budget_notifications_for_account(
        self, *, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetNotificationsForAccountResponseTypeDef:
        """
        Lists the budget names and notifications that are associated with an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_notifications_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_notifications_for_account)
        """
    def describe_budget_performance_history(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        Describes the history for `DAILY` , `MONTHLY` , and `QUARTERLY` budgets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budget_performance_history)
        """
    def describe_budgets(
        self, *, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        Lists the budgets that are associated with an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_budgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_budgets)
        """
    def describe_notifications_for_budget(
        self, *, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        Lists the notifications that are associated with a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_notifications_for_budget)
        """
    def describe_subscribers_for_notification(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeSubscribersForNotificationResponseTypeDef:
        """
        Lists the subscribers that are associated with a notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe_subscribers_for_notification)
        """
    def execute_budget_action(
        self, *, AccountId: str, BudgetName: str, ActionId: str, ExecutionType: ExecutionTypeType
    ) -> ExecuteBudgetActionResponseTypeDef:
        """
        Executes a budget action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.execute_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#execute_budget_action)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#generate_presigned_url)
        """
    def update_budget(self, *, AccountId: str, NewBudget: "BudgetTypeDef") -> Dict[str, Any]:
        """
        Updates a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.update_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update_budget)
        """
    def update_budget_action(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        NotificationType: NotificationTypeType = None,
        ActionThreshold: "ActionThresholdTypeDef" = None,
        Definition: "DefinitionTypeDef" = None,
        ExecutionRoleArn: str = None,
        ApprovalModel: ApprovalModelType = None,
        Subscribers: List["SubscriberTypeDef"] = None
    ) -> UpdateBudgetActionResponseTypeDef:
        """
        Updates a budget action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.update_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update_budget_action)
        """
    def update_notification(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        OldNotification: "NotificationTypeDef",
        NewNotification: "NotificationTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates a notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.update_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update_notification)
        """
    def update_subscriber(
        self,
        *,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        OldSubscriber: "SubscriberTypeDef",
        NewSubscriber: "SubscriberTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates a subscriber.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Client.update_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update_subscriber)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_action_histories"]
    ) -> DescribeBudgetActionHistoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionhistoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_account"]
    ) -> DescribeBudgetActionsForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionsforaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_budget"]
    ) -> DescribeBudgetActionsForBudgetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionsforbudgetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_notifications_for_account"]
    ) -> DescribeBudgetNotificationsForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetNotificationsForAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetnotificationsforaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_performance_history"]
    ) -> DescribeBudgetPerformanceHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetperformancehistorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> DescribeBudgetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> DescribeNotificationsForBudgetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describenotificationsforbudgetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> DescribeSubscribersForNotificationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describesubscribersfornotificationpaginator)
        """
