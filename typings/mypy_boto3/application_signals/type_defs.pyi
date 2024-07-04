"""
Type annotations for application-signals service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_signals/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_signals.type_defs import BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef

    data: BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DurationUnitType,
    ServiceLevelIndicatorComparisonOperatorType,
    ServiceLevelIndicatorMetricTypeType,
    ServiceLevelObjectiveBudgetStatusType,
    StandardUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef",
    "BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    "CalendarIntervalTypeDef",
    "CreateServiceLevelObjectiveInputRequestTypeDef",
    "CreateServiceLevelObjectiveOutputTypeDef",
    "DeleteServiceLevelObjectiveInputRequestTypeDef",
    "DimensionTypeDef",
    "GetServiceInputRequestTypeDef",
    "GetServiceLevelObjectiveInputRequestTypeDef",
    "GetServiceLevelObjectiveOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GoalTypeDef",
    "IntervalTypeDef",
    "ListServiceDependenciesInputRequestTypeDef",
    "ListServiceDependenciesOutputTypeDef",
    "ListServiceDependentsInputRequestTypeDef",
    "ListServiceDependentsOutputTypeDef",
    "ListServiceLevelObjectivesInputRequestTypeDef",
    "ListServiceLevelObjectivesOutputTypeDef",
    "ListServiceOperationsInputRequestTypeDef",
    "ListServiceOperationsOutputTypeDef",
    "ListServicesInputRequestTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDataQueryTypeDef",
    "MetricReferenceTypeDef",
    "MetricStatTypeDef",
    "MetricTypeDef",
    "PaginatorConfigTypeDef",
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
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateServiceLevelObjectiveInputRequestTypeDef",
    "UpdateServiceLevelObjectiveOutputTypeDef",
)

BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef = TypedDict(
    "BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef",
    {
        "Timestamp": Union[datetime, str],
        "SloIds": List[str],
    },
)

BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef = TypedDict(
    "BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    {
        "Timestamp": datetime,
        "Reports": List["ServiceLevelObjectiveBudgetReportTypeDef"],
        "Errors": List["ServiceLevelObjectiveBudgetReportErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalendarIntervalTypeDef = TypedDict(
    "CalendarIntervalTypeDef",
    {
        "StartTime": datetime,
        "DurationUnit": DurationUnitType,
        "Duration": int,
    },
)

_RequiredCreateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "_RequiredCreateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Name": str,
        "SliConfig": "ServiceLevelIndicatorConfigTypeDef",
    },
)
_OptionalCreateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "_OptionalCreateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Description": str,
        "Goal": "GoalTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateServiceLevelObjectiveInputRequestTypeDef(
    _RequiredCreateServiceLevelObjectiveInputRequestTypeDef,
    _OptionalCreateServiceLevelObjectiveInputRequestTypeDef,
):
    pass

CreateServiceLevelObjectiveOutputTypeDef = TypedDict(
    "CreateServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": "ServiceLevelObjectiveTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "DeleteServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

GetServiceInputRequestTypeDef = TypedDict(
    "GetServiceInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "KeyAttributes": Dict[str, str],
    },
)

GetServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "GetServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceLevelObjectiveOutputTypeDef = TypedDict(
    "GetServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": "ServiceLevelObjectiveTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceOutputTypeDef = TypedDict(
    "GetServiceOutputTypeDef",
    {
        "Service": "ServiceTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GoalTypeDef = TypedDict(
    "GoalTypeDef",
    {
        "Interval": "IntervalTypeDef",
        "AttainmentGoal": float,
        "WarningThreshold": float,
    },
    total=False,
)

IntervalTypeDef = TypedDict(
    "IntervalTypeDef",
    {
        "RollingInterval": "RollingIntervalTypeDef",
        "CalendarInterval": "CalendarIntervalTypeDef",
    },
    total=False,
)

_RequiredListServiceDependenciesInputRequestTypeDef = TypedDict(
    "_RequiredListServiceDependenciesInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "KeyAttributes": Dict[str, str],
    },
)
_OptionalListServiceDependenciesInputRequestTypeDef = TypedDict(
    "_OptionalListServiceDependenciesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServiceDependenciesInputRequestTypeDef(
    _RequiredListServiceDependenciesInputRequestTypeDef,
    _OptionalListServiceDependenciesInputRequestTypeDef,
):
    pass

ListServiceDependenciesOutputTypeDef = TypedDict(
    "ListServiceDependenciesOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceDependencies": List["ServiceDependencyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceDependentsInputRequestTypeDef = TypedDict(
    "_RequiredListServiceDependentsInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "KeyAttributes": Dict[str, str],
    },
)
_OptionalListServiceDependentsInputRequestTypeDef = TypedDict(
    "_OptionalListServiceDependentsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServiceDependentsInputRequestTypeDef(
    _RequiredListServiceDependentsInputRequestTypeDef,
    _OptionalListServiceDependentsInputRequestTypeDef,
):
    pass

ListServiceDependentsOutputTypeDef = TypedDict(
    "ListServiceDependentsOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceDependents": List["ServiceDependentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceLevelObjectivesInputRequestTypeDef = TypedDict(
    "ListServiceLevelObjectivesInputRequestTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "OperationName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListServiceLevelObjectivesOutputTypeDef = TypedDict(
    "ListServiceLevelObjectivesOutputTypeDef",
    {
        "SloSummaries": List["ServiceLevelObjectiveSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceOperationsInputRequestTypeDef = TypedDict(
    "_RequiredListServiceOperationsInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "KeyAttributes": Dict[str, str],
    },
)
_OptionalListServiceOperationsInputRequestTypeDef = TypedDict(
    "_OptionalListServiceOperationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServiceOperationsInputRequestTypeDef(
    _RequiredListServiceOperationsInputRequestTypeDef,
    _OptionalListServiceOperationsInputRequestTypeDef,
):
    pass

ListServiceOperationsOutputTypeDef = TypedDict(
    "ListServiceOperationsOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceOperations": List["ServiceOperationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicesInputRequestTypeDef = TypedDict(
    "_RequiredListServicesInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalListServicesInputRequestTypeDef = TypedDict(
    "_OptionalListServicesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServicesInputRequestTypeDef(
    _RequiredListServicesInputRequestTypeDef, _OptionalListServicesInputRequestTypeDef
):
    pass

ListServicesOutputTypeDef = TypedDict(
    "ListServicesOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceSummaries": List["ServiceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMetricDataQueryTypeDef = TypedDict(
    "_RequiredMetricDataQueryTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": "MetricStatTypeDef",
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
        "AccountId": str,
    },
    total=False,
)

class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, _OptionalMetricDataQueryTypeDef):
    pass

_RequiredMetricReferenceTypeDef = TypedDict(
    "_RequiredMetricReferenceTypeDef",
    {
        "Namespace": str,
        "MetricType": str,
        "MetricName": str,
    },
)
_OptionalMetricReferenceTypeDef = TypedDict(
    "_OptionalMetricReferenceTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)

class MetricReferenceTypeDef(_RequiredMetricReferenceTypeDef, _OptionalMetricReferenceTypeDef):
    pass

_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef",
    {
        "Metric": "MetricTypeDef",
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": StandardUnitType,
    },
    total=False,
)

class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
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

RollingIntervalTypeDef = TypedDict(
    "RollingIntervalTypeDef",
    {
        "DurationUnit": DurationUnitType,
        "Duration": int,
    },
)

ServiceDependencyTypeDef = TypedDict(
    "ServiceDependencyTypeDef",
    {
        "OperationName": str,
        "DependencyKeyAttributes": Dict[str, str],
        "DependencyOperationName": str,
        "MetricReferences": List["MetricReferenceTypeDef"],
    },
)

_RequiredServiceDependentTypeDef = TypedDict(
    "_RequiredServiceDependentTypeDef",
    {
        "DependentKeyAttributes": Dict[str, str],
        "MetricReferences": List["MetricReferenceTypeDef"],
    },
)
_OptionalServiceDependentTypeDef = TypedDict(
    "_OptionalServiceDependentTypeDef",
    {
        "OperationName": str,
        "DependentOperationName": str,
    },
    total=False,
)

class ServiceDependentTypeDef(_RequiredServiceDependentTypeDef, _OptionalServiceDependentTypeDef):
    pass

ServiceLevelIndicatorConfigTypeDef = TypedDict(
    "ServiceLevelIndicatorConfigTypeDef",
    {
        "SliMetricConfig": "ServiceLevelIndicatorMetricConfigTypeDef",
        "MetricThreshold": float,
        "ComparisonOperator": ServiceLevelIndicatorComparisonOperatorType,
    },
)

ServiceLevelIndicatorMetricConfigTypeDef = TypedDict(
    "ServiceLevelIndicatorMetricConfigTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "OperationName": str,
        "MetricType": ServiceLevelIndicatorMetricTypeType,
        "Statistic": str,
        "PeriodSeconds": int,
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
    },
    total=False,
)

_RequiredServiceLevelIndicatorMetricTypeDef = TypedDict(
    "_RequiredServiceLevelIndicatorMetricTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
    },
)
_OptionalServiceLevelIndicatorMetricTypeDef = TypedDict(
    "_OptionalServiceLevelIndicatorMetricTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "OperationName": str,
        "MetricType": ServiceLevelIndicatorMetricTypeType,
    },
    total=False,
)

class ServiceLevelIndicatorMetricTypeDef(
    _RequiredServiceLevelIndicatorMetricTypeDef, _OptionalServiceLevelIndicatorMetricTypeDef
):
    pass

ServiceLevelIndicatorTypeDef = TypedDict(
    "ServiceLevelIndicatorTypeDef",
    {
        "SliMetric": "ServiceLevelIndicatorMetricTypeDef",
        "MetricThreshold": float,
        "ComparisonOperator": ServiceLevelIndicatorComparisonOperatorType,
    },
)

ServiceLevelObjectiveBudgetReportErrorTypeDef = TypedDict(
    "ServiceLevelObjectiveBudgetReportErrorTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

_RequiredServiceLevelObjectiveBudgetReportTypeDef = TypedDict(
    "_RequiredServiceLevelObjectiveBudgetReportTypeDef",
    {
        "Arn": str,
        "Name": str,
        "BudgetStatus": ServiceLevelObjectiveBudgetStatusType,
    },
)
_OptionalServiceLevelObjectiveBudgetReportTypeDef = TypedDict(
    "_OptionalServiceLevelObjectiveBudgetReportTypeDef",
    {
        "Attainment": float,
        "TotalBudgetSeconds": int,
        "BudgetSecondsRemaining": int,
        "Sli": "ServiceLevelIndicatorTypeDef",
        "Goal": "GoalTypeDef",
    },
    total=False,
)

class ServiceLevelObjectiveBudgetReportTypeDef(
    _RequiredServiceLevelObjectiveBudgetReportTypeDef,
    _OptionalServiceLevelObjectiveBudgetReportTypeDef,
):
    pass

_RequiredServiceLevelObjectiveSummaryTypeDef = TypedDict(
    "_RequiredServiceLevelObjectiveSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
)
_OptionalServiceLevelObjectiveSummaryTypeDef = TypedDict(
    "_OptionalServiceLevelObjectiveSummaryTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "OperationName": str,
        "CreatedTime": datetime,
    },
    total=False,
)

class ServiceLevelObjectiveSummaryTypeDef(
    _RequiredServiceLevelObjectiveSummaryTypeDef, _OptionalServiceLevelObjectiveSummaryTypeDef
):
    pass

_RequiredServiceLevelObjectiveTypeDef = TypedDict(
    "_RequiredServiceLevelObjectiveTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Sli": "ServiceLevelIndicatorTypeDef",
        "Goal": "GoalTypeDef",
    },
)
_OptionalServiceLevelObjectiveTypeDef = TypedDict(
    "_OptionalServiceLevelObjectiveTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ServiceLevelObjectiveTypeDef(
    _RequiredServiceLevelObjectiveTypeDef, _OptionalServiceLevelObjectiveTypeDef
):
    pass

ServiceOperationTypeDef = TypedDict(
    "ServiceOperationTypeDef",
    {
        "Name": str,
        "MetricReferences": List["MetricReferenceTypeDef"],
    },
)

_RequiredServiceSummaryTypeDef = TypedDict(
    "_RequiredServiceSummaryTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "MetricReferences": List["MetricReferenceTypeDef"],
    },
)
_OptionalServiceSummaryTypeDef = TypedDict(
    "_OptionalServiceSummaryTypeDef",
    {
        "AttributeMaps": List[Dict[str, str]],
    },
    total=False,
)

class ServiceSummaryTypeDef(_RequiredServiceSummaryTypeDef, _OptionalServiceSummaryTypeDef):
    pass

_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "MetricReferences": List["MetricReferenceTypeDef"],
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "AttributeMaps": List[Dict[str, str]],
    },
    total=False,
)

class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Description": str,
        "SliConfig": "ServiceLevelIndicatorConfigTypeDef",
        "Goal": "GoalTypeDef",
    },
    total=False,
)

class UpdateServiceLevelObjectiveInputRequestTypeDef(
    _RequiredUpdateServiceLevelObjectiveInputRequestTypeDef,
    _OptionalUpdateServiceLevelObjectiveInputRequestTypeDef,
):
    pass

UpdateServiceLevelObjectiveOutputTypeDef = TypedDict(
    "UpdateServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": "ServiceLevelObjectiveTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
