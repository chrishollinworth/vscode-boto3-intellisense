"""
Type annotations for budgets service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs.html)

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef

    data: ActionHistoryDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    BudgetTypeType,
    ComparisonOperatorType,
    EventTypeType,
    ExecutionTypeType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
)

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
    "CreateBudgetActionRequestRequestTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "CreateNotificationRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "DefinitionTypeDef",
    "DeleteBudgetActionRequestRequestTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "DeleteNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "DescribeBudgetActionHistoriesRequestRequestTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionRequestRequestTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountRequestRequestTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetRequestRequestTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetRequestRequestTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsRequestRequestTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetRequestRequestTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationRequestRequestTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionRequestRequestTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "UpdateBudgetActionRequestRequestTypeDef",
    "UpdateBudgetActionResponseTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "UpdateNotificationRequestRequestTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
)

ActionHistoryDetailsTypeDef = TypedDict(
    "ActionHistoryDetailsTypeDef",
    {
        "Message": str,
        "Action": "ActionTypeDef",
    },
)

ActionHistoryTypeDef = TypedDict(
    "ActionHistoryTypeDef",
    {
        "Timestamp": datetime,
        "Status": ActionStatusType,
        "EventType": EventTypeType,
        "ActionHistoryDetails": "ActionHistoryDetailsTypeDef",
    },
)

ActionThresholdTypeDef = TypedDict(
    "ActionThresholdTypeDef",
    {
        "ActionThresholdValue": float,
        "ActionThresholdType": ThresholdTypeType,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Status": ActionStatusType,
        "Subscribers": List["SubscriberTypeDef"],
    },
)

BudgetPerformanceHistoryTypeDef = TypedDict(
    "BudgetPerformanceHistoryTypeDef",
    {
        "BudgetName": str,
        "BudgetType": BudgetTypeType,
        "CostFilters": Dict[str, List[str]],
        "CostTypes": "CostTypesTypeDef",
        "TimeUnit": TimeUnitType,
        "BudgetedAndActualAmountsList": List["BudgetedAndActualAmountsTypeDef"],
    },
    total=False,
)

_RequiredBudgetTypeDef = TypedDict(
    "_RequiredBudgetTypeDef",
    {
        "BudgetName": str,
        "TimeUnit": TimeUnitType,
        "BudgetType": BudgetTypeType,
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
        "LastUpdatedTime": Union[datetime, str],
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
    "_RequiredCalculatedSpendTypeDef",
    {
        "ActualSpend": "SpendTypeDef",
    },
)
_OptionalCalculatedSpendTypeDef = TypedDict(
    "_OptionalCalculatedSpendTypeDef",
    {
        "ForecastedSpend": "SpendTypeDef",
    },
    total=False,
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

CreateBudgetActionRequestRequestTypeDef = TypedDict(
    "CreateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "NotificationType": NotificationTypeType,
        "ActionType": ActionTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": List["SubscriberTypeDef"],
    },
)

CreateBudgetActionResponseTypeDef = TypedDict(
    "CreateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBudgetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "Budget": "BudgetTypeDef",
    },
)
_OptionalCreateBudgetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBudgetRequestRequestTypeDef",
    {
        "NotificationsWithSubscribers": List["NotificationWithSubscribersTypeDef"],
    },
    total=False,
)

class CreateBudgetRequestRequestTypeDef(
    _RequiredCreateBudgetRequestRequestTypeDef, _OptionalCreateBudgetRequestRequestTypeDef
):
    pass

CreateNotificationRequestRequestTypeDef = TypedDict(
    "CreateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscribers": List["SubscriberTypeDef"],
    },
)

CreateSubscriberRequestRequestTypeDef = TypedDict(
    "CreateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
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

DeleteBudgetActionRequestRequestTypeDef = TypedDict(
    "DeleteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DeleteBudgetActionResponseTypeDef = TypedDict(
    "DeleteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DeleteNotificationRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
    },
)

DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "Subscriber": "SubscriberTypeDef",
    },
)

_RequiredDescribeBudgetActionHistoriesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionHistoriesRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
_OptionalDescribeBudgetActionHistoriesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionHistoriesRequestRequestTypeDef",
    {
        "TimePeriod": "TimePeriodTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeBudgetActionHistoriesRequestRequestTypeDef(
    _RequiredDescribeBudgetActionHistoriesRequestRequestTypeDef,
    _OptionalDescribeBudgetActionHistoriesRequestRequestTypeDef,
):
    pass

DescribeBudgetActionHistoriesResponseTypeDef = TypedDict(
    "DescribeBudgetActionHistoriesResponseTypeDef",
    {
        "ActionHistories": List["ActionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetActionRequestRequestTypeDef = TypedDict(
    "DescribeBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)

DescribeBudgetActionResponseTypeDef = TypedDict(
    "DescribeBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetActionsForAccountRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalDescribeBudgetActionsForAccountRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForAccountRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeBudgetActionsForAccountRequestRequestTypeDef(
    _RequiredDescribeBudgetActionsForAccountRequestRequestTypeDef,
    _OptionalDescribeBudgetActionsForAccountRequestRequestTypeDef,
):
    pass

DescribeBudgetActionsForAccountResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForAccountResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetActionsForBudgetRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetActionsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeBudgetActionsForBudgetRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetActionsForBudgetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeBudgetActionsForBudgetRequestRequestTypeDef(
    _RequiredDescribeBudgetActionsForBudgetRequestRequestTypeDef,
    _OptionalDescribeBudgetActionsForBudgetRequestRequestTypeDef,
):
    pass

DescribeBudgetActionsForBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    {
        "Actions": List["ActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetPerformanceHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeBudgetPerformanceHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetPerformanceHistoryRequestRequestTypeDef",
    {
        "TimePeriod": "TimePeriodTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeBudgetPerformanceHistoryRequestRequestTypeDef(
    _RequiredDescribeBudgetPerformanceHistoryRequestRequestTypeDef,
    _OptionalDescribeBudgetPerformanceHistoryRequestRequestTypeDef,
):
    pass

DescribeBudgetPerformanceHistoryResponseTypeDef = TypedDict(
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    {
        "BudgetPerformanceHistory": "BudgetPerformanceHistoryTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBudgetRequestRequestTypeDef = TypedDict(
    "DescribeBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)

DescribeBudgetResponseTypeDef = TypedDict(
    "DescribeBudgetResponseTypeDef",
    {
        "Budget": "BudgetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeBudgetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeBudgetsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalDescribeBudgetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeBudgetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeBudgetsRequestRequestTypeDef(
    _RequiredDescribeBudgetsRequestRequestTypeDef, _OptionalDescribeBudgetsRequestRequestTypeDef
):
    pass

DescribeBudgetsResponseTypeDef = TypedDict(
    "DescribeBudgetsResponseTypeDef",
    {
        "Budgets": List["BudgetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeNotificationsForBudgetRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeNotificationsForBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
    },
)
_OptionalDescribeNotificationsForBudgetRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeNotificationsForBudgetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeNotificationsForBudgetRequestRequestTypeDef(
    _RequiredDescribeNotificationsForBudgetRequestRequestTypeDef,
    _OptionalDescribeNotificationsForBudgetRequestRequestTypeDef,
):
    pass

DescribeNotificationsForBudgetResponseTypeDef = TypedDict(
    "DescribeNotificationsForBudgetResponseTypeDef",
    {
        "Notifications": List["NotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSubscribersForNotificationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSubscribersForNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
    },
)
_OptionalDescribeSubscribersForNotificationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSubscribersForNotificationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeSubscribersForNotificationRequestRequestTypeDef(
    _RequiredDescribeSubscribersForNotificationRequestRequestTypeDef,
    _OptionalDescribeSubscribersForNotificationRequestRequestTypeDef,
):
    pass

DescribeSubscribersForNotificationResponseTypeDef = TypedDict(
    "DescribeSubscribersForNotificationResponseTypeDef",
    {
        "Subscribers": List["SubscriberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteBudgetActionRequestRequestTypeDef = TypedDict(
    "ExecuteBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
    },
)

ExecuteBudgetActionResponseTypeDef = TypedDict(
    "ExecuteBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
        "ExecutionType": ExecutionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIamActionDefinitionTypeDef = TypedDict(
    "_RequiredIamActionDefinitionTypeDef",
    {
        "PolicyArn": str,
    },
)
_OptionalIamActionDefinitionTypeDef = TypedDict(
    "_OptionalIamActionDefinitionTypeDef",
    {
        "Roles": List[str],
        "Groups": List[str],
        "Users": List[str],
    },
    total=False,
)

class IamActionDefinitionTypeDef(
    _RequiredIamActionDefinitionTypeDef, _OptionalIamActionDefinitionTypeDef
):
    pass

_RequiredNotificationTypeDef = TypedDict(
    "_RequiredNotificationTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
    },
)
_OptionalNotificationTypeDef = TypedDict(
    "_OptionalNotificationTypeDef",
    {
        "ThresholdType": ThresholdTypeType,
        "NotificationState": NotificationStateType,
    },
    total=False,
)

class NotificationTypeDef(_RequiredNotificationTypeDef, _OptionalNotificationTypeDef):
    pass

NotificationWithSubscribersTypeDef = TypedDict(
    "NotificationWithSubscribersTypeDef",
    {
        "Notification": "NotificationTypeDef",
        "Subscribers": List["SubscriberTypeDef"],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ScpActionDefinitionTypeDef = TypedDict(
    "ScpActionDefinitionTypeDef",
    {
        "PolicyId": str,
        "TargetIds": List[str],
    },
)

SpendTypeDef = TypedDict(
    "SpendTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
)

SsmActionDefinitionTypeDef = TypedDict(
    "SsmActionDefinitionTypeDef",
    {
        "ActionSubType": ActionSubTypeType,
        "Region": str,
        "InstanceIds": List[str],
    },
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "SubscriptionType": SubscriptionTypeType,
        "Address": str,
    },
)

TimePeriodTypeDef = TypedDict(
    "TimePeriodTypeDef",
    {
        "Start": Union[datetime, str],
        "End": Union[datetime, str],
    },
    total=False,
)

_RequiredUpdateBudgetActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBudgetActionRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "ActionId": str,
    },
)
_OptionalUpdateBudgetActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBudgetActionRequestRequestTypeDef",
    {
        "NotificationType": NotificationTypeType,
        "ActionThreshold": "ActionThresholdTypeDef",
        "Definition": "DefinitionTypeDef",
        "ExecutionRoleArn": str,
        "ApprovalModel": ApprovalModelType,
        "Subscribers": List["SubscriberTypeDef"],
    },
    total=False,
)

class UpdateBudgetActionRequestRequestTypeDef(
    _RequiredUpdateBudgetActionRequestRequestTypeDef,
    _OptionalUpdateBudgetActionRequestRequestTypeDef,
):
    pass

UpdateBudgetActionResponseTypeDef = TypedDict(
    "UpdateBudgetActionResponseTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldAction": "ActionTypeDef",
        "NewAction": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBudgetRequestRequestTypeDef = TypedDict(
    "UpdateBudgetRequestRequestTypeDef",
    {
        "AccountId": str,
        "NewBudget": "BudgetTypeDef",
    },
)

UpdateNotificationRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "OldNotification": "NotificationTypeDef",
        "NewNotification": "NotificationTypeDef",
    },
)

UpdateSubscriberRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberRequestRequestTypeDef",
    {
        "AccountId": str,
        "BudgetName": str,
        "Notification": "NotificationTypeDef",
        "OldSubscriber": "SubscriberTypeDef",
        "NewSubscriber": "SubscriberTypeDef",
    },
)
