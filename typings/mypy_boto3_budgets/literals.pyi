"""
Type annotations for budgets service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/literals.html)

Usage::

    ```python
    from mypy_boto3_budgets.literals import ActionStatusType

    data: ActionStatusType = "EXECUTION_FAILURE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionStatusType",
    "ActionSubTypeType",
    "ActionTypeType",
    "ApprovalModelType",
    "BudgetTypeType",
    "ComparisonOperatorType",
    "DescribeBudgetActionHistoriesPaginatorName",
    "DescribeBudgetActionsForAccountPaginatorName",
    "DescribeBudgetActionsForBudgetPaginatorName",
    "DescribeBudgetPerformanceHistoryPaginatorName",
    "DescribeBudgetsPaginatorName",
    "DescribeNotificationsForBudgetPaginatorName",
    "DescribeSubscribersForNotificationPaginatorName",
    "EventTypeType",
    "ExecutionTypeType",
    "NotificationStateType",
    "NotificationTypeType",
    "SubscriptionTypeType",
    "ThresholdTypeType",
    "TimeUnitType",
)

ActionStatusType = Literal[
    "EXECUTION_FAILURE",
    "EXECUTION_IN_PROGRESS",
    "EXECUTION_SUCCESS",
    "PENDING",
    "RESET_FAILURE",
    "RESET_IN_PROGRESS",
    "REVERSE_FAILURE",
    "REVERSE_IN_PROGRESS",
    "REVERSE_SUCCESS",
    "STANDBY",
]
ActionSubTypeType = Literal["STOP_EC2_INSTANCES", "STOP_RDS_INSTANCES"]
ActionTypeType = Literal["APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"]
ApprovalModelType = Literal["AUTOMATIC", "MANUAL"]
BudgetTypeType = Literal[
    "COST",
    "RI_COVERAGE",
    "RI_UTILIZATION",
    "SAVINGS_PLANS_COVERAGE",
    "SAVINGS_PLANS_UTILIZATION",
    "USAGE",
]
ComparisonOperatorType = Literal["EQUAL_TO", "GREATER_THAN", "LESS_THAN"]
DescribeBudgetActionHistoriesPaginatorName = Literal["describe_budget_action_histories"]
DescribeBudgetActionsForAccountPaginatorName = Literal["describe_budget_actions_for_account"]
DescribeBudgetActionsForBudgetPaginatorName = Literal["describe_budget_actions_for_budget"]
DescribeBudgetPerformanceHistoryPaginatorName = Literal["describe_budget_performance_history"]
DescribeBudgetsPaginatorName = Literal["describe_budgets"]
DescribeNotificationsForBudgetPaginatorName = Literal["describe_notifications_for_budget"]
DescribeSubscribersForNotificationPaginatorName = Literal["describe_subscribers_for_notification"]
EventTypeType = Literal[
    "CREATE_ACTION", "DELETE_ACTION", "EXECUTE_ACTION", "SYSTEM", "UPDATE_ACTION"
]
ExecutionTypeType = Literal[
    "APPROVE_BUDGET_ACTION", "RESET_BUDGET_ACTION", "RETRY_BUDGET_ACTION", "REVERSE_BUDGET_ACTION"
]
NotificationStateType = Literal["ALARM", "OK"]
NotificationTypeType = Literal["ACTUAL", "FORECASTED"]
SubscriptionTypeType = Literal["EMAIL", "SNS"]
ThresholdTypeType = Literal["ABSOLUTE_VALUE", "PERCENTAGE"]
TimeUnitType = Literal["ANNUALLY", "DAILY", "MONTHLY", "QUARTERLY"]
