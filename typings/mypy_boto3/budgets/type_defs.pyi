"""
Type annotations for budgets service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionThresholdTypeDef

    data: ActionThresholdTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ActionStatusType,
    ActionSubTypeType,
    ActionTypeType,
    ApprovalModelType,
    AutoAdjustTypeType,
    BudgetTypeType,
    ComparisonOperatorType,
    DimensionType,
    EventTypeType,
    ExecutionTypeType,
    MatchOptionType,
    MetricType,
    NotificationStateType,
    NotificationTypeType,
    SubscriptionTypeType,
    ThresholdTypeType,
    TimeUnitType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionHistoryDetailsTypeDef",
    "ActionHistoryTypeDef",
    "ActionThresholdTypeDef",
    "ActionTypeDef",
    "AutoAdjustDataOutputTypeDef",
    "AutoAdjustDataTypeDef",
    "BudgetNotificationsForAccountTypeDef",
    "BudgetOutputTypeDef",
    "BudgetPaginatorTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetUnionTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostCategoryValuesOutputTypeDef",
    "CostCategoryValuesTypeDef",
    "CostTypesTypeDef",
    "CreateBudgetActionRequestTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "CreateBudgetRequestTypeDef",
    "CreateNotificationRequestTypeDef",
    "CreateSubscriberRequestTypeDef",
    "DefinitionOutputTypeDef",
    "DefinitionTypeDef",
    "DefinitionUnionTypeDef",
    "DeleteBudgetActionRequestTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DeleteBudgetRequestTypeDef",
    "DeleteNotificationRequestTypeDef",
    "DeleteSubscriberRequestTypeDef",
    "DescribeBudgetActionHistoriesRequestPaginateTypeDef",
    "DescribeBudgetActionHistoriesRequestTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionRequestTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountRequestPaginateTypeDef",
    "DescribeBudgetActionsForAccountRequestTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetRequestPaginateTypeDef",
    "DescribeBudgetActionsForBudgetRequestTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetNotificationsForAccountRequestPaginateTypeDef",
    "DescribeBudgetNotificationsForAccountRequestTypeDef",
    "DescribeBudgetNotificationsForAccountResponseTypeDef",
    "DescribeBudgetPerformanceHistoryRequestPaginateTypeDef",
    "DescribeBudgetPerformanceHistoryRequestTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetRequestTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsRequestPaginateTypeDef",
    "DescribeBudgetsRequestTypeDef",
    "DescribeBudgetsResponsePaginatorTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetRequestPaginateTypeDef",
    "DescribeNotificationsForBudgetRequestTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationRequestPaginateTypeDef",
    "DescribeSubscribersForNotificationRequestTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionRequestTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "ExpressionDimensionValuesOutputTypeDef",
    "ExpressionDimensionValuesTypeDef",
    "ExpressionOutputTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "HistoricalOptionsTypeDef",
    "IamActionDefinitionOutputTypeDef",
    "IamActionDefinitionTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "ScpActionDefinitionOutputTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionOutputTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TagResourceRequestTypeDef",
    "TagValuesOutputTypeDef",
    "TagValuesTypeDef",
    "TimePeriodOutputTypeDef",
    "TimePeriodTypeDef",
    "TimePeriodUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBudgetActionRequestTypeDef",
    "UpdateBudgetActionResponseTypeDef",
    "UpdateBudgetRequestTypeDef",
    "UpdateNotificationRequestTypeDef",
    "UpdateSubscriberRequestTypeDef",
)

class ActionThresholdTypeDef(TypedDict):
    ActionThresholdValue: float
    ActionThresholdType: ThresholdTypeType

class SubscriberTypeDef(TypedDict):
    SubscriptionType: SubscriptionTypeType
    Address: str

class HistoricalOptionsTypeDef(TypedDict):
    BudgetAdjustmentPeriod: int
    LookBackAvailablePeriods: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class NotificationTypeDef(TypedDict):
    NotificationType: NotificationTypeType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    ThresholdType: NotRequired[ThresholdTypeType]
    NotificationState: NotRequired[NotificationStateType]

class CostTypesTypeDef(TypedDict):
    IncludeTax: NotRequired[bool]
    IncludeSubscription: NotRequired[bool]
    UseBlended: NotRequired[bool]
    IncludeRefund: NotRequired[bool]
    IncludeCredit: NotRequired[bool]
    IncludeUpfront: NotRequired[bool]
    IncludeRecurring: NotRequired[bool]
    IncludeOtherSubscription: NotRequired[bool]
    IncludeSupport: NotRequired[bool]
    IncludeDiscount: NotRequired[bool]
    UseAmortized: NotRequired[bool]

class SpendTypeDef(TypedDict):
    Amount: str
    Unit: str

class TimePeriodOutputTypeDef(TypedDict):
    Start: NotRequired[datetime]
    End: NotRequired[datetime]

class CostCategoryValuesOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]
    MatchOptions: NotRequired[List[MatchOptionType]]

class CostCategoryValuesTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class ResourceTagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class IamActionDefinitionOutputTypeDef(TypedDict):
    PolicyArn: str
    Roles: NotRequired[List[str]]
    Groups: NotRequired[List[str]]
    Users: NotRequired[List[str]]

class ScpActionDefinitionOutputTypeDef(TypedDict):
    PolicyId: str
    TargetIds: List[str]

class SsmActionDefinitionOutputTypeDef(TypedDict):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: List[str]

class IamActionDefinitionTypeDef(TypedDict):
    PolicyArn: str
    Roles: NotRequired[Sequence[str]]
    Groups: NotRequired[Sequence[str]]
    Users: NotRequired[Sequence[str]]

class ScpActionDefinitionTypeDef(TypedDict):
    PolicyId: str
    TargetIds: Sequence[str]

class SsmActionDefinitionTypeDef(TypedDict):
    ActionSubType: ActionSubTypeType
    Region: str
    InstanceIds: Sequence[str]

class DeleteBudgetActionRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str

class DeleteBudgetRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeBudgetActionRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str

class DescribeBudgetActionsForAccountRequestTypeDef(TypedDict):
    AccountId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBudgetActionsForBudgetRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBudgetNotificationsForAccountRequestTypeDef(TypedDict):
    AccountId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBudgetRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ShowFilterExpression: NotRequired[bool]

class DescribeBudgetsRequestTypeDef(TypedDict):
    AccountId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ShowFilterExpression: NotRequired[bool]

class DescribeNotificationsForBudgetRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ExecuteBudgetActionRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType

class ExpressionDimensionValuesOutputTypeDef(TypedDict):
    Key: DimensionType
    Values: List[str]
    MatchOptions: NotRequired[List[MatchOptionType]]

class ExpressionDimensionValuesTypeDef(TypedDict):
    Key: DimensionType
    Values: Sequence[str]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class TagValuesOutputTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[List[str]]
    MatchOptions: NotRequired[List[MatchOptionType]]

class TagValuesTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    MatchOptions: NotRequired[Sequence[MatchOptionType]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    ResourceTagKeys: Sequence[str]

class AutoAdjustDataOutputTypeDef(TypedDict):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: NotRequired[HistoricalOptionsTypeDef]
    LastAutoAdjustTime: NotRequired[datetime]

class AutoAdjustDataTypeDef(TypedDict):
    AutoAdjustType: AutoAdjustTypeType
    HistoricalOptions: NotRequired[HistoricalOptionsTypeDef]
    LastAutoAdjustTime: NotRequired[TimestampTypeDef]

class TimePeriodTypeDef(TypedDict):
    Start: NotRequired[TimestampTypeDef]
    End: NotRequired[TimestampTypeDef]

class BudgetNotificationsForAccountTypeDef(TypedDict):
    Notifications: NotRequired[List[NotificationTypeDef]]
    BudgetName: NotRequired[str]

class CreateNotificationRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class CreateSubscriberRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DeleteNotificationRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef

class DeleteSubscriberRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    Subscriber: SubscriberTypeDef

class DescribeSubscribersForNotificationRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NotificationWithSubscribersTypeDef(TypedDict):
    Notification: NotificationTypeDef
    Subscribers: Sequence[SubscriberTypeDef]

class UpdateNotificationRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    OldNotification: NotificationTypeDef
    NewNotification: NotificationTypeDef

class UpdateSubscriberRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    OldSubscriber: SubscriberTypeDef
    NewSubscriber: SubscriberTypeDef

class CalculatedSpendTypeDef(TypedDict):
    ActualSpend: SpendTypeDef
    ForecastedSpend: NotRequired[SpendTypeDef]

class BudgetedAndActualAmountsTypeDef(TypedDict):
    BudgetedAmount: NotRequired[SpendTypeDef]
    ActualAmount: NotRequired[SpendTypeDef]
    TimePeriod: NotRequired[TimePeriodOutputTypeDef]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationsForBudgetResponseTypeDef(TypedDict):
    Notifications: List[NotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSubscribersForNotificationResponseTypeDef(TypedDict):
    Subscribers: List[SubscriberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExecuteBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefinitionOutputTypeDef(TypedDict):
    IamActionDefinition: NotRequired[IamActionDefinitionOutputTypeDef]
    ScpActionDefinition: NotRequired[ScpActionDefinitionOutputTypeDef]
    SsmActionDefinition: NotRequired[SsmActionDefinitionOutputTypeDef]

class DefinitionTypeDef(TypedDict):
    IamActionDefinition: NotRequired[IamActionDefinitionTypeDef]
    ScpActionDefinition: NotRequired[ScpActionDefinitionTypeDef]
    SsmActionDefinition: NotRequired[SsmActionDefinitionTypeDef]

class DescribeBudgetActionsForAccountRequestPaginateTypeDef(TypedDict):
    AccountId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBudgetActionsForBudgetRequestPaginateTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBudgetNotificationsForAccountRequestPaginateTypeDef(TypedDict):
    AccountId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBudgetsRequestPaginateTypeDef(TypedDict):
    AccountId: str
    ShowFilterExpression: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeNotificationsForBudgetRequestPaginateTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSubscribersForNotificationRequestPaginateTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Notification: NotificationTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ExpressionOutputTypeDef(TypedDict):
    Or: NotRequired[List[Dict[str, Any]]]
    And: NotRequired[List[Dict[str, Any]]]
    Not: NotRequired[Dict[str, Any]]
    Dimensions: NotRequired[ExpressionDimensionValuesOutputTypeDef]
    Tags: NotRequired[TagValuesOutputTypeDef]
    CostCategories: NotRequired[CostCategoryValuesOutputTypeDef]

class ExpressionPaginatorTypeDef(TypedDict):
    Or: NotRequired[List[Dict[str, Any]]]
    And: NotRequired[List[Dict[str, Any]]]
    Not: NotRequired[Dict[str, Any]]
    Dimensions: NotRequired[ExpressionDimensionValuesOutputTypeDef]
    Tags: NotRequired[TagValuesOutputTypeDef]
    CostCategories: NotRequired[CostCategoryValuesOutputTypeDef]

class ExpressionTypeDef(TypedDict):
    Or: NotRequired[Sequence[Mapping[str, Any]]]
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Not: NotRequired[Mapping[str, Any]]
    Dimensions: NotRequired[ExpressionDimensionValuesTypeDef]
    Tags: NotRequired[TagValuesTypeDef]
    CostCategories: NotRequired[CostCategoryValuesTypeDef]

TimePeriodUnionTypeDef = Union[TimePeriodTypeDef, TimePeriodOutputTypeDef]

class DescribeBudgetNotificationsForAccountResponseTypeDef(TypedDict):
    BudgetNotificationsForAccount: List[BudgetNotificationsForAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BudgetPerformanceHistoryTypeDef(TypedDict):
    BudgetName: NotRequired[str]
    BudgetType: NotRequired[BudgetTypeType]
    CostFilters: NotRequired[Dict[str, List[str]]]
    CostTypes: NotRequired[CostTypesTypeDef]
    TimeUnit: NotRequired[TimeUnitType]
    BudgetedAndActualAmountsList: NotRequired[List[BudgetedAndActualAmountsTypeDef]]

class ActionTypeDef(TypedDict):
    ActionId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThresholdTypeDef
    Definition: DefinitionOutputTypeDef
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Status: ActionStatusType
    Subscribers: List[SubscriberTypeDef]

DefinitionUnionTypeDef = Union[DefinitionTypeDef, DefinitionOutputTypeDef]

class BudgetOutputTypeDef(TypedDict):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: NotRequired[SpendTypeDef]
    PlannedBudgetLimits: NotRequired[Dict[str, SpendTypeDef]]
    CostFilters: NotRequired[Dict[str, List[str]]]
    CostTypes: NotRequired[CostTypesTypeDef]
    TimePeriod: NotRequired[TimePeriodOutputTypeDef]
    CalculatedSpend: NotRequired[CalculatedSpendTypeDef]
    LastUpdatedTime: NotRequired[datetime]
    AutoAdjustData: NotRequired[AutoAdjustDataOutputTypeDef]
    FilterExpression: NotRequired[ExpressionOutputTypeDef]
    Metrics: NotRequired[List[MetricType]]

class BudgetPaginatorTypeDef(TypedDict):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: NotRequired[SpendTypeDef]
    PlannedBudgetLimits: NotRequired[Dict[str, SpendTypeDef]]
    CostFilters: NotRequired[Dict[str, List[str]]]
    CostTypes: NotRequired[CostTypesTypeDef]
    TimePeriod: NotRequired[TimePeriodOutputTypeDef]
    CalculatedSpend: NotRequired[CalculatedSpendTypeDef]
    LastUpdatedTime: NotRequired[datetime]
    AutoAdjustData: NotRequired[AutoAdjustDataOutputTypeDef]
    FilterExpression: NotRequired[ExpressionPaginatorTypeDef]
    Metrics: NotRequired[List[MetricType]]

class BudgetTypeDef(TypedDict):
    BudgetName: str
    TimeUnit: TimeUnitType
    BudgetType: BudgetTypeType
    BudgetLimit: NotRequired[SpendTypeDef]
    PlannedBudgetLimits: NotRequired[Mapping[str, SpendTypeDef]]
    CostFilters: NotRequired[Mapping[str, Sequence[str]]]
    CostTypes: NotRequired[CostTypesTypeDef]
    TimePeriod: NotRequired[TimePeriodTypeDef]
    CalculatedSpend: NotRequired[CalculatedSpendTypeDef]
    LastUpdatedTime: NotRequired[TimestampTypeDef]
    AutoAdjustData: NotRequired[AutoAdjustDataTypeDef]
    FilterExpression: NotRequired[ExpressionTypeDef]
    Metrics: NotRequired[Sequence[MetricType]]

class DescribeBudgetActionHistoriesRequestPaginateTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: NotRequired[TimePeriodUnionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBudgetActionHistoriesRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    TimePeriod: NotRequired[TimePeriodUnionTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBudgetPerformanceHistoryRequestPaginateTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    TimePeriod: NotRequired[TimePeriodUnionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBudgetPerformanceHistoryRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    TimePeriod: NotRequired[TimePeriodUnionTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeBudgetPerformanceHistoryResponseTypeDef(TypedDict):
    BudgetPerformanceHistory: BudgetPerformanceHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ActionHistoryDetailsTypeDef(TypedDict):
    Message: str
    Action: ActionTypeDef

class DeleteBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBudgetActionsForAccountResponseTypeDef(TypedDict):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeBudgetActionsForBudgetResponseTypeDef(TypedDict):
    Actions: List[ActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    OldAction: ActionTypeDef
    NewAction: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBudgetActionRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    NotificationType: NotificationTypeType
    ActionType: ActionTypeType
    ActionThreshold: ActionThresholdTypeDef
    Definition: DefinitionUnionTypeDef
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModelType
    Subscribers: Sequence[SubscriberTypeDef]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateBudgetActionRequestTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    NotificationType: NotRequired[NotificationTypeType]
    ActionThreshold: NotRequired[ActionThresholdTypeDef]
    Definition: NotRequired[DefinitionUnionTypeDef]
    ExecutionRoleArn: NotRequired[str]
    ApprovalModel: NotRequired[ApprovalModelType]
    Subscribers: NotRequired[Sequence[SubscriberTypeDef]]

class DescribeBudgetResponseTypeDef(TypedDict):
    Budget: BudgetOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBudgetsResponseTypeDef(TypedDict):
    Budgets: List[BudgetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeBudgetsResponsePaginatorTypeDef(TypedDict):
    Budgets: List[BudgetPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

BudgetUnionTypeDef = Union[BudgetTypeDef, BudgetOutputTypeDef]

class ActionHistoryTypeDef(TypedDict):
    Timestamp: datetime
    Status: ActionStatusType
    EventType: EventTypeType
    ActionHistoryDetails: ActionHistoryDetailsTypeDef

class CreateBudgetRequestTypeDef(TypedDict):
    AccountId: str
    Budget: BudgetUnionTypeDef
    NotificationsWithSubscribers: NotRequired[Sequence[NotificationWithSubscribersTypeDef]]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateBudgetRequestTypeDef(TypedDict):
    AccountId: str
    NewBudget: BudgetUnionTypeDef

class DescribeBudgetActionHistoriesResponseTypeDef(TypedDict):
    ActionHistories: List[ActionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
