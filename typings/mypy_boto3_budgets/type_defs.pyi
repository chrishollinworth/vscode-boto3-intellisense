"""
Main interface for budgets service type definitions.

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import BudgetPerformanceHistoryTypeDef

    data: BudgetPerformanceHistoryTypeDef = {...}
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
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostTypesTypeDef",
    "NotificationTypeDef",
    "SpendTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
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


SpendTypeDef = TypedDict("SpendTypeDef", {"Amount": str, "Unit": str})

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef", {"SubscriptionType": Literal["SNS", "EMAIL"], "Address": str}
)

TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef", {"Start": datetime, "End": datetime}, total=False
)

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

NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {"Notification": "NotificationTypeDef", "Subscribers": List["SubscriberTypeDef"]},
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
