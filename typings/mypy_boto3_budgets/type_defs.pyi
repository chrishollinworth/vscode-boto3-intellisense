"""
Main interface for budgets service type definitions.

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef

    data: ActionHistoryDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionHistoryDetailsTypeDef",
    "ActionHistoryTypeDef",
    "ActionThresholdTypeDef",
    "ActionTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostTypesTypeDef",
    "DefinitionTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateBudgetActionResponseTypeDef",
)

ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef", {"Message": str, "Action": "ActionTypeDef"}
)

ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": Literal[
            "STANDBY",
            "PENDING",
            "EXECUTION_IN_PROGRESS",
            "EXECUTION_SUCCESS",
            "EXECUTION_FAILURE",
            "REVERSE_IN_PROGRESS",
            "REVERSE_SUCCESS",
            "REVERSE_FAILURE",
            "RESET_IN_PROGRESS",
            "RESET_FAILURE",
        ],
        "EventType": Literal[
            "SYSTEM", "CREATE_ACTION", "DELETE_ACTION", "UPDATE_ACTION", "EXECUTE_ACTION"
        ],
        "ActionHistoryDetails": "ActionHistoryDetailsTypeDef",
    },
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {"ActionThresholdValue": float, "ActionThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"]},
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ActionType": Literal["APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"],
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": Literal["AUTOMATIC", "MANUAL"],
        "Status": Literal[
            "STANDBY",
            "PENDING",
            "EXECUTION_IN_PROGRESS",
            "EXECUTION_SUCCESS",
            "EXECUTION_FAILURE",
            "REVERSE_IN_PROGRESS",
            "REVERSE_SUCCESS",
            "REVERSE_FAILURE",
            "RESET_IN_PROGRESS",
            "RESET_FAILURE",
        ],
        "Subscribers": List["SubscriberTypeDef"],
    },
)

BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": str,
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": "CostTypesTypeDef",
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "BudgetedAndActualAmountsList": List["BudgetedAndActualAmountsTypeDef"],
    },
    total=False,
)

_RequiredBudgetTypeDef = TypedDict(
    "_RequiredBudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": Literal["DAILY", "MONTHLY", "QUARTERLY", "ANNUALLY"],
        "BudgetType": Literal[
            "USAGE",
            "COST",
            "RI_UTILIZATION",
            "RI_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
        ],
    },
)
_OptionalBudgetTypeDef = TypedDict(
    "_OptionalBudgetTypeDef",
    {
        "BudgetLimit": "SpendTypeDef",
        "PlannedBudgetLimits": Dict[str, "SpendTypeDef"],
        "CostFilters": Dict[str, List[str]],
        "CostTypes": "CostTypesTypeDef",
        "TimePeriod": "TimePeriodTypeDef",
        "CalculatedSpend": "CalculatedSpendTypeDef",
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class BudgetTypeDef(_RequiredBudgetTypeDef, _OptionalBudgetTypeDef):
    pass


BudgetedAndActualAmountsTypeDef = TypedDict(
    "BudgetedAndActualAmountsTypeDef",
    {
        "BudgetedAmount": "SpendTypeDef",
        "ActualAmount": "SpendTypeDef",
        "TimePeriod": "TimePeriodTypeDef",
    },
    total=False,
)

_RequiredCalculatedSpendTypeDef = TypedDict(
    "_RequiredCalculatedSpendTypeDef", {"ActualSpend": "SpendTypeDef"}
)
_OptionalCalculatedSpendTypeDef = TypedDict(
    "_OptionalCalculatedSpendTypeDef", {"ForecastedSpend": "SpendTypeDef"}, total=False
)


class CalculatedSpendTypeDef(_RequiredCalculatedSpendTypeDef, _OptionalCalculatedSpendTypeDef):
    pass


CostTypesTypeDef = TypedDict(
    "CostTypesTypeDef",
    {
        "IncludeTax": bool,
        "IncludeSubscription": bool,
        "UseBlended": bool,
        "IncludeRefund": bool,
        "IncludeCredit": bool,
        "IncludeUpfront": bool,
        "IncludeRecurring": bool,
        "IncludeOtherSubscription": bool,
        "IncludeSupport": bool,
        "IncludeDiscount": bool,
        "UseAmortized": bool,
    },
    total=False,
)

DefinitionTypeDef = TypedDict(
    "DefinitionTypeDef",
    {
        "IamActionDefinition": "IamActionDefinitionTypeDef",
        "ScpActionDefinition": "ScpActionDefinitionTypeDef",
        "SsmActionDefinition": "SsmActionDefinitionTypeDef",
    },
    total=False,
)

_RequiredIamActionDefinitionTypeDef = TypedDict(
    "_RequiredIamActionDefinitionTypeDef", {"PolicyArn": str}
)
_OptionalIamActionDefinitionTypeDef = TypedDict(
    "_OptionalIamActionDefinitionTypeDef",
    {"Roles": List[str], "Groups": List[str], "Users": List[str]},
    total=False,
)


class IamActionDefinitionTypeDef(
    _RequiredIamActionDefinitionTypeDef, _OptionalIamActionDefinitionTypeDef
):
    pass


_RequiredNotificationTypeDef = TypedDict(
    "_RequiredNotificationTypeDef",
    {
        "NotificationType": Literal["ACTUAL", "FORECASTED"],
        "ComparisonOperator": Literal["GREATER_THAN", "LESS_THAN", "EQUAL_TO"],
        "Threshold": float,
    },
)
_OptionalNotificationTypeDef = TypedDict(
    "_OptionalNotificationTypeDef",
    {
        "ThresholdType": Literal["PERCENTAGE", "ABSOLUTE_VALUE"],
        "NotificationState": Literal["OK", "ALARM"],
    },
    total=False,
)


class NotificationTypeDef(_RequiredNotificationTypeDef, _OptionalNotificationTypeDef):
    pass


ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef", {"PolicyId": str, "TargetIds": List[str]}
)

SpendTypeDef = TypedDict("SpendTypeDef", {"Amount": str, "Unit": str})

SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": Literal["STOP_EC2_INSTANCES", "STOP_RDS_INSTANCES"],
        "Region": str,
        "InstanceIds": List[str],
    },
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef", {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str}
)

TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef", {"Start": datetime, "End": datetime}, total=False
)

CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef", {"AccountId": str, "BudgetName": str, "ActionId": str}
)

DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {"AccountId": str, "BudgetName": str, "Action": "ActionTypeDef"},
)

_RequiredDescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionHistoriesResponseTypeDef",
    {"ActionHistories": List["ActionHistoryTypeDef"]},
)
_OptionalDescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionHistoriesResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeBudgetActionHistoriesResponseTypeDef(
    _RequiredDescribeBudgetActionHistoriesResponseTypeDef,
    _OptionalDescribeBudgetActionHistoriesResponseTypeDef,
):
    pass


DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {"AccountId": str, "BudgetName": str, "Action": "ActionTypeDef"},
)

_RequiredDescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForAccountResponseTypeDef", {"Actions": List["ActionTypeDef"]}
)
_OptionalDescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForAccountResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeBudgetActionsForAccountResponseTypeDef(
    _RequiredDescribeBudgetActionsForAccountResponseTypeDef,
    _OptionalDescribeBudgetActionsForAccountResponseTypeDef,
):
    pass


_RequiredDescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForBudgetResponseTypeDef", {"Actions": List["ActionTypeDef"]}
)
_OptionalDescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForBudgetResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeBudgetActionsForBudgetResponseTypeDef(
    _RequiredDescribeBudgetActionsForBudgetResponseTypeDef,
    _OptionalDescribeBudgetActionsForBudgetResponseTypeDef,
):
    pass


DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {"BudgetPerformanceHistory": "BudgetPerformanceHistoryTypeDef", "NextToken": str},
    total=False,
)

DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef", {"Budget": "BudgetTypeDef"}, total=False
)

DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {"Budgets": List["BudgetTypeDef"], "NextToken": str},
    total=False,
)

DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {"Notifications": List["NotificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {"Subscribers": List["SubscriberTypeDef"], "NextToken": str},
    total=False,
)

ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": Literal[
            "APPROVE_BUDGET_ACTION",
            "RETRY_BUDGET_ACTION",
            "REVERSE_BUDGET_ACTION",
            "RESET_BUDGET_ACTION",
        ],
    },
)

NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {"Notification": "NotificationTypeDef", "Subscribers": List["SubscriberTypeDef"]},
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": "ActionTypeDef",
        "NewAction": "ActionTypeDef",
    },
)
