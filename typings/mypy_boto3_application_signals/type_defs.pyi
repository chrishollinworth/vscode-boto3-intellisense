"""
Type annotations for application-signals service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_application_signals.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DurationUnitType,
    EvaluationTypeType,
    MetricSourceTypeType,
    ServiceLevelIndicatorComparisonOperatorType,
    ServiceLevelIndicatorMetricTypeType,
    ServiceLevelObjectiveBudgetStatusType,
    StandardUnitType,
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
    "BatchGetServiceLevelObjectiveBudgetReportInputTypeDef",
    "BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    "BatchUpdateExclusionWindowsErrorTypeDef",
    "BatchUpdateExclusionWindowsInputTypeDef",
    "BatchUpdateExclusionWindowsOutputTypeDef",
    "BurnRateConfigurationTypeDef",
    "CalendarIntervalOutputTypeDef",
    "CalendarIntervalTypeDef",
    "CreateServiceLevelObjectiveInputTypeDef",
    "CreateServiceLevelObjectiveOutputTypeDef",
    "DeleteServiceLevelObjectiveInputTypeDef",
    "DependencyConfigOutputTypeDef",
    "DependencyConfigTypeDef",
    "DependencyConfigUnionTypeDef",
    "DimensionTypeDef",
    "ExclusionWindowOutputTypeDef",
    "ExclusionWindowTypeDef",
    "ExclusionWindowUnionTypeDef",
    "GetServiceInputTypeDef",
    "GetServiceLevelObjectiveInputTypeDef",
    "GetServiceLevelObjectiveOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GoalOutputTypeDef",
    "GoalTypeDef",
    "GoalUnionTypeDef",
    "IntervalOutputTypeDef",
    "IntervalTypeDef",
    "ListServiceDependenciesInputPaginateTypeDef",
    "ListServiceDependenciesInputTypeDef",
    "ListServiceDependenciesOutputTypeDef",
    "ListServiceDependentsInputPaginateTypeDef",
    "ListServiceDependentsInputTypeDef",
    "ListServiceDependentsOutputTypeDef",
    "ListServiceLevelObjectiveExclusionWindowsInputPaginateTypeDef",
    "ListServiceLevelObjectiveExclusionWindowsInputTypeDef",
    "ListServiceLevelObjectiveExclusionWindowsOutputTypeDef",
    "ListServiceLevelObjectivesInputPaginateTypeDef",
    "ListServiceLevelObjectivesInputTypeDef",
    "ListServiceLevelObjectivesOutputTypeDef",
    "ListServiceOperationsInputPaginateTypeDef",
    "ListServiceOperationsInputTypeDef",
    "ListServiceOperationsOutputTypeDef",
    "ListServicesInputPaginateTypeDef",
    "ListServicesInputTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDataQueryOutputTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataQueryUnionTypeDef",
    "MetricOutputTypeDef",
    "MetricReferenceTypeDef",
    "MetricStatOutputTypeDef",
    "MetricStatTypeDef",
    "MetricStatUnionTypeDef",
    "MetricTypeDef",
    "MetricUnionTypeDef",
    "MonitoredRequestCountMetricDataQueriesOutputTypeDef",
    "MonitoredRequestCountMetricDataQueriesTypeDef",
    "MonitoredRequestCountMetricDataQueriesUnionTypeDef",
    "PaginatorConfigTypeDef",
    "RecurrenceRuleTypeDef",
    "RequestBasedServiceLevelIndicatorConfigTypeDef",
    "RequestBasedServiceLevelIndicatorMetricConfigTypeDef",
    "RequestBasedServiceLevelIndicatorMetricTypeDef",
    "RequestBasedServiceLevelIndicatorTypeDef",
    "ResponseMetadataTypeDef",
    "RollingIntervalTypeDef",
    "ServiceDependencyTypeDef",
    "ServiceDependentTypeDef",
    "ServiceLevelIndicatorConfigTypeDef",
    "ServiceLevelIndicatorMetricConfigTypeDef",
    "ServiceLevelIndicatorMetricTypeDef",
    "ServiceLevelIndicatorTypeDef",
    "ServiceLevelObjectiveBudgetReportErrorTypeDef",
    "ServiceLevelObjectiveBudgetReportTypeDef",
    "ServiceLevelObjectiveSummaryTypeDef",
    "ServiceLevelObjectiveTypeDef",
    "ServiceOperationTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateServiceLevelObjectiveInputTypeDef",
    "UpdateServiceLevelObjectiveOutputTypeDef",
    "WindowTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ServiceLevelObjectiveBudgetReportErrorTypeDef(TypedDict):
    Name: str
    Arn: str
    ErrorCode: str
    ErrorMessage: str

class BatchUpdateExclusionWindowsErrorTypeDef(TypedDict):
    SloId: str
    ErrorCode: str
    ErrorMessage: str

class BurnRateConfigurationTypeDef(TypedDict):
    LookBackWindowMinutes: int

class CalendarIntervalOutputTypeDef(TypedDict):
    StartTime: datetime
    DurationUnit: DurationUnitType
    Duration: int

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteServiceLevelObjectiveInputTypeDef(TypedDict):
    Id: str

class DependencyConfigOutputTypeDef(TypedDict):
    DependencyKeyAttributes: Dict[str, str]
    DependencyOperationName: str

class DependencyConfigTypeDef(TypedDict):
    DependencyKeyAttributes: Mapping[str, str]
    DependencyOperationName: str

class DimensionTypeDef(TypedDict):
    Name: str
    Value: str

class RecurrenceRuleTypeDef(TypedDict):
    Expression: str

class WindowTypeDef(TypedDict):
    DurationUnit: DurationUnitType
    Duration: int

class GetServiceLevelObjectiveInputTypeDef(TypedDict):
    Id: str

class RollingIntervalTypeDef(TypedDict):
    DurationUnit: DurationUnitType
    Duration: int

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListServiceLevelObjectiveExclusionWindowsInputTypeDef(TypedDict):
    Id: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class BatchGetServiceLevelObjectiveBudgetReportInputTypeDef(TypedDict):
    Timestamp: TimestampTypeDef
    SloIds: Sequence[str]

class CalendarIntervalTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    DurationUnit: DurationUnitType
    Duration: int

class GetServiceInputTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]

class ListServiceDependenciesInputTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListServiceDependentsInputTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListServiceOperationsInputTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListServicesInputTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    IncludeLinkedAccounts: NotRequired[bool]
    AwsAccountId: NotRequired[str]

class BatchUpdateExclusionWindowsOutputTypeDef(TypedDict):
    SloIds: List[str]
    Errors: List[BatchUpdateExclusionWindowsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ServiceLevelObjectiveSummaryTypeDef(TypedDict):
    Arn: str
    Name: str
    KeyAttributes: NotRequired[Dict[str, str]]
    OperationName: NotRequired[str]
    DependencyConfig: NotRequired[DependencyConfigOutputTypeDef]
    CreatedTime: NotRequired[datetime]
    EvaluationType: NotRequired[EvaluationTypeType]
    MetricSourceType: NotRequired[MetricSourceTypeType]

DependencyConfigUnionTypeDef = Union[DependencyConfigTypeDef, DependencyConfigOutputTypeDef]

class MetricOutputTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[List[DimensionTypeDef]]

class MetricReferenceTypeDef(TypedDict):
    Namespace: str
    MetricType: str
    MetricName: str
    Dimensions: NotRequired[List[DimensionTypeDef]]
    AccountId: NotRequired[str]

class MetricTypeDef(TypedDict):
    Namespace: NotRequired[str]
    MetricName: NotRequired[str]
    Dimensions: NotRequired[Sequence[DimensionTypeDef]]

class ExclusionWindowOutputTypeDef(TypedDict):
    Window: WindowTypeDef
    StartTime: NotRequired[datetime]
    RecurrenceRule: NotRequired[RecurrenceRuleTypeDef]
    Reason: NotRequired[str]

class ExclusionWindowTypeDef(TypedDict):
    Window: WindowTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    RecurrenceRule: NotRequired[RecurrenceRuleTypeDef]
    Reason: NotRequired[str]

class IntervalOutputTypeDef(TypedDict):
    RollingInterval: NotRequired[RollingIntervalTypeDef]
    CalendarInterval: NotRequired[CalendarIntervalOutputTypeDef]

class ListServiceDependenciesInputPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceDependentsInputPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceLevelObjectiveExclusionWindowsInputPaginateTypeDef(TypedDict):
    Id: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceOperationsInputPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesInputPaginateTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IncludeLinkedAccounts: NotRequired[bool]
    AwsAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class IntervalTypeDef(TypedDict):
    RollingInterval: NotRequired[RollingIntervalTypeDef]
    CalendarInterval: NotRequired[CalendarIntervalTypeDef]

class ListServiceLevelObjectivesOutputTypeDef(TypedDict):
    SloSummaries: List[ServiceLevelObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceLevelObjectivesInputPaginateTypeDef(TypedDict):
    KeyAttributes: NotRequired[Mapping[str, str]]
    OperationName: NotRequired[str]
    DependencyConfig: NotRequired[DependencyConfigUnionTypeDef]
    MetricSourceTypes: NotRequired[Sequence[MetricSourceTypeType]]
    IncludeLinkedAccounts: NotRequired[bool]
    SloOwnerAwsAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceLevelObjectivesInputTypeDef(TypedDict):
    KeyAttributes: NotRequired[Mapping[str, str]]
    OperationName: NotRequired[str]
    DependencyConfig: NotRequired[DependencyConfigUnionTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    MetricSourceTypes: NotRequired[Sequence[MetricSourceTypeType]]
    IncludeLinkedAccounts: NotRequired[bool]
    SloOwnerAwsAccountId: NotRequired[str]

class MetricStatOutputTypeDef(TypedDict):
    Metric: MetricOutputTypeDef
    Period: int
    Stat: str
    Unit: NotRequired[StandardUnitType]

class ServiceDependencyTypeDef(TypedDict):
    OperationName: str
    DependencyKeyAttributes: Dict[str, str]
    DependencyOperationName: str
    MetricReferences: List[MetricReferenceTypeDef]

class ServiceDependentTypeDef(TypedDict):
    DependentKeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    OperationName: NotRequired[str]
    DependentOperationName: NotRequired[str]

class ServiceOperationTypeDef(TypedDict):
    Name: str
    MetricReferences: List[MetricReferenceTypeDef]

class ServiceSummaryTypeDef(TypedDict):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: NotRequired[List[Dict[str, str]]]

class ServiceTypeDef(TypedDict):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: NotRequired[List[Dict[str, str]]]
    LogGroupReferences: NotRequired[List[Dict[str, str]]]

MetricUnionTypeDef = Union[MetricTypeDef, MetricOutputTypeDef]

class ListServiceLevelObjectiveExclusionWindowsOutputTypeDef(TypedDict):
    ExclusionWindows: List[ExclusionWindowOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ExclusionWindowUnionTypeDef = Union[ExclusionWindowTypeDef, ExclusionWindowOutputTypeDef]

class GoalOutputTypeDef(TypedDict):
    Interval: NotRequired[IntervalOutputTypeDef]
    AttainmentGoal: NotRequired[float]
    WarningThreshold: NotRequired[float]

class GoalTypeDef(TypedDict):
    Interval: NotRequired[IntervalTypeDef]
    AttainmentGoal: NotRequired[float]
    WarningThreshold: NotRequired[float]

class MetricDataQueryOutputTypeDef(TypedDict):
    Id: str
    MetricStat: NotRequired[MetricStatOutputTypeDef]
    Expression: NotRequired[str]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]
    Period: NotRequired[int]
    AccountId: NotRequired[str]

class ListServiceDependenciesOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime
    ServiceDependencies: List[ServiceDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceDependentsOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime
    ServiceDependents: List[ServiceDependentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceOperationsOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime
    ServiceOperations: List[ServiceOperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServicesOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime
    ServiceSummaries: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetServiceOutputTypeDef(TypedDict):
    Service: ServiceTypeDef
    StartTime: datetime
    EndTime: datetime
    LogGroupReferences: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatTypeDef(TypedDict):
    Metric: MetricUnionTypeDef
    Period: int
    Stat: str
    Unit: NotRequired[StandardUnitType]

class BatchUpdateExclusionWindowsInputTypeDef(TypedDict):
    SloIds: Sequence[str]
    AddExclusionWindows: NotRequired[Sequence[ExclusionWindowUnionTypeDef]]
    RemoveExclusionWindows: NotRequired[Sequence[ExclusionWindowUnionTypeDef]]

GoalUnionTypeDef = Union[GoalTypeDef, GoalOutputTypeDef]

class MonitoredRequestCountMetricDataQueriesOutputTypeDef(TypedDict):
    GoodCountMetric: NotRequired[List[MetricDataQueryOutputTypeDef]]
    BadCountMetric: NotRequired[List[MetricDataQueryOutputTypeDef]]

class ServiceLevelIndicatorMetricTypeDef(TypedDict):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]
    KeyAttributes: NotRequired[Dict[str, str]]
    OperationName: NotRequired[str]
    MetricType: NotRequired[ServiceLevelIndicatorMetricTypeType]
    DependencyConfig: NotRequired[DependencyConfigOutputTypeDef]

MetricStatUnionTypeDef = Union[MetricStatTypeDef, MetricStatOutputTypeDef]

class RequestBasedServiceLevelIndicatorMetricTypeDef(TypedDict):
    TotalRequestCountMetric: List[MetricDataQueryOutputTypeDef]
    MonitoredRequestCountMetric: MonitoredRequestCountMetricDataQueriesOutputTypeDef
    KeyAttributes: NotRequired[Dict[str, str]]
    OperationName: NotRequired[str]
    MetricType: NotRequired[ServiceLevelIndicatorMetricTypeType]
    DependencyConfig: NotRequired[DependencyConfigOutputTypeDef]

class ServiceLevelIndicatorTypeDef(TypedDict):
    SliMetric: ServiceLevelIndicatorMetricTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType

class MetricDataQueryTypeDef(TypedDict):
    Id: str
    MetricStat: NotRequired[MetricStatUnionTypeDef]
    Expression: NotRequired[str]
    Label: NotRequired[str]
    ReturnData: NotRequired[bool]
    Period: NotRequired[int]
    AccountId: NotRequired[str]

class RequestBasedServiceLevelIndicatorTypeDef(TypedDict):
    RequestBasedSliMetric: RequestBasedServiceLevelIndicatorMetricTypeDef
    MetricThreshold: NotRequired[float]
    ComparisonOperator: NotRequired[ServiceLevelIndicatorComparisonOperatorType]

MetricDataQueryUnionTypeDef = Union[MetricDataQueryTypeDef, MetricDataQueryOutputTypeDef]

class ServiceLevelObjectiveBudgetReportTypeDef(TypedDict):
    Arn: str
    Name: str
    BudgetStatus: ServiceLevelObjectiveBudgetStatusType
    EvaluationType: NotRequired[EvaluationTypeType]
    Attainment: NotRequired[float]
    TotalBudgetSeconds: NotRequired[int]
    BudgetSecondsRemaining: NotRequired[int]
    TotalBudgetRequests: NotRequired[int]
    BudgetRequestsRemaining: NotRequired[int]
    Sli: NotRequired[ServiceLevelIndicatorTypeDef]
    RequestBasedSli: NotRequired[RequestBasedServiceLevelIndicatorTypeDef]
    Goal: NotRequired[GoalOutputTypeDef]

class ServiceLevelObjectiveTypeDef(TypedDict):
    Arn: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Goal: GoalOutputTypeDef
    Description: NotRequired[str]
    Sli: NotRequired[ServiceLevelIndicatorTypeDef]
    RequestBasedSli: NotRequired[RequestBasedServiceLevelIndicatorTypeDef]
    EvaluationType: NotRequired[EvaluationTypeType]
    BurnRateConfigurations: NotRequired[List[BurnRateConfigurationTypeDef]]
    MetricSourceType: NotRequired[MetricSourceTypeType]

class MonitoredRequestCountMetricDataQueriesTypeDef(TypedDict):
    GoodCountMetric: NotRequired[Sequence[MetricDataQueryUnionTypeDef]]
    BadCountMetric: NotRequired[Sequence[MetricDataQueryTypeDef]]

class ServiceLevelIndicatorMetricConfigTypeDef(TypedDict):
    KeyAttributes: NotRequired[Mapping[str, str]]
    OperationName: NotRequired[str]
    MetricType: NotRequired[ServiceLevelIndicatorMetricTypeType]
    Statistic: NotRequired[str]
    PeriodSeconds: NotRequired[int]
    MetricDataQueries: NotRequired[Sequence[MetricDataQueryUnionTypeDef]]
    DependencyConfig: NotRequired[DependencyConfigUnionTypeDef]

class BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef(TypedDict):
    Timestamp: datetime
    Reports: List[ServiceLevelObjectiveBudgetReportTypeDef]
    Errors: List[ServiceLevelObjectiveBudgetReportErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceLevelObjectiveOutputTypeDef(TypedDict):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceLevelObjectiveOutputTypeDef(TypedDict):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceLevelObjectiveOutputTypeDef(TypedDict):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

MonitoredRequestCountMetricDataQueriesUnionTypeDef = Union[
    MonitoredRequestCountMetricDataQueriesTypeDef,
    MonitoredRequestCountMetricDataQueriesOutputTypeDef,
]

class ServiceLevelIndicatorConfigTypeDef(TypedDict):
    SliMetricConfig: ServiceLevelIndicatorMetricConfigTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType

class RequestBasedServiceLevelIndicatorMetricConfigTypeDef(TypedDict):
    KeyAttributes: NotRequired[Mapping[str, str]]
    OperationName: NotRequired[str]
    MetricType: NotRequired[ServiceLevelIndicatorMetricTypeType]
    TotalRequestCountMetric: NotRequired[Sequence[MetricDataQueryUnionTypeDef]]
    MonitoredRequestCountMetric: NotRequired[MonitoredRequestCountMetricDataQueriesUnionTypeDef]
    DependencyConfig: NotRequired[DependencyConfigUnionTypeDef]

class RequestBasedServiceLevelIndicatorConfigTypeDef(TypedDict):
    RequestBasedSliMetricConfig: RequestBasedServiceLevelIndicatorMetricConfigTypeDef
    MetricThreshold: NotRequired[float]
    ComparisonOperator: NotRequired[ServiceLevelIndicatorComparisonOperatorType]

class CreateServiceLevelObjectiveInputTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    SliConfig: NotRequired[ServiceLevelIndicatorConfigTypeDef]
    RequestBasedSliConfig: NotRequired[RequestBasedServiceLevelIndicatorConfigTypeDef]
    Goal: NotRequired[GoalUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    BurnRateConfigurations: NotRequired[Sequence[BurnRateConfigurationTypeDef]]

class UpdateServiceLevelObjectiveInputTypeDef(TypedDict):
    Id: str
    Description: NotRequired[str]
    SliConfig: NotRequired[ServiceLevelIndicatorConfigTypeDef]
    RequestBasedSliConfig: NotRequired[RequestBasedServiceLevelIndicatorConfigTypeDef]
    Goal: NotRequired[GoalUnionTypeDef]
    BurnRateConfigurations: NotRequired[Sequence[BurnRateConfigurationTypeDef]]
