"""
Type annotations for evidently service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/type_defs.html)

Usage::

    ```python
    from mypy_boto3_evidently.type_defs import BatchEvaluateFeatureRequestRequestTypeDef

    data: BatchEvaluateFeatureRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChangeDirectionEnumType,
    EventTypeType,
    ExperimentResultRequestTypeType,
    ExperimentResultResponseTypeType,
    ExperimentStatusType,
    ExperimentStopDesiredStateType,
    FeatureEvaluationStrategyType,
    FeatureStatusType,
    LaunchStatusType,
    LaunchStopDesiredStateType,
    ProjectStatusType,
    VariationValueTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchEvaluateFeatureRequestRequestTypeDef",
    "BatchEvaluateFeatureResponseTypeDef",
    "CloudWatchLogsDestinationConfigTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureRequestRequestTypeDef",
    "CreateFeatureResponseTypeDef",
    "CreateLaunchRequestRequestTypeDef",
    "CreateLaunchResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteFeatureRequestRequestTypeDef",
    "DeleteLaunchRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "EvaluateFeatureRequestRequestTypeDef",
    "EvaluateFeatureResponseTypeDef",
    "EvaluationRequestTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationRuleTypeDef",
    "EventTypeDef",
    "ExperimentExecutionTypeDef",
    "ExperimentReportTypeDef",
    "ExperimentResultsDataTypeDef",
    "ExperimentScheduleTypeDef",
    "ExperimentTypeDef",
    "FeatureSummaryTypeDef",
    "FeatureTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentResultsRequestRequestTypeDef",
    "GetExperimentResultsResponseTypeDef",
    "GetFeatureRequestRequestTypeDef",
    "GetFeatureResponseTypeDef",
    "GetLaunchRequestRequestTypeDef",
    "GetLaunchResponseTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetProjectResponseTypeDef",
    "LaunchExecutionTypeDef",
    "LaunchGroupConfigTypeDef",
    "LaunchGroupTypeDef",
    "LaunchTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeaturesRequestRequestTypeDef",
    "ListFeaturesResponseTypeDef",
    "ListLaunchesRequestRequestTypeDef",
    "ListLaunchesResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDefinitionConfigTypeDef",
    "MetricDefinitionTypeDef",
    "MetricGoalConfigTypeDef",
    "MetricGoalTypeDef",
    "MetricMonitorConfigTypeDef",
    "MetricMonitorTypeDef",
    "OnlineAbConfigTypeDef",
    "OnlineAbDefinitionTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDataDeliveryConfigTypeDef",
    "ProjectDataDeliveryTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectTypeDef",
    "PutProjectEventsRequestRequestTypeDef",
    "PutProjectEventsResponseTypeDef",
    "PutProjectEventsResultEntryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "ScheduledSplitConfigTypeDef",
    "ScheduledSplitTypeDef",
    "ScheduledSplitsLaunchConfigTypeDef",
    "ScheduledSplitsLaunchDefinitionTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "StartExperimentResponseTypeDef",
    "StartLaunchRequestRequestTypeDef",
    "StartLaunchResponseTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopExperimentResponseTypeDef",
    "StopLaunchRequestRequestTypeDef",
    "StopLaunchResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TreatmentConfigTypeDef",
    "TreatmentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateFeatureRequestRequestTypeDef",
    "UpdateFeatureResponseTypeDef",
    "UpdateLaunchRequestRequestTypeDef",
    "UpdateLaunchResponseTypeDef",
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    "UpdateProjectDataDeliveryResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "VariableValueTypeDef",
    "VariationConfigTypeDef",
    "VariationTypeDef",
)

BatchEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "BatchEvaluateFeatureRequestRequestTypeDef",
    {
        "project": str,
        "requests": List["EvaluationRequestTypeDef"],
    },
)

BatchEvaluateFeatureResponseTypeDef = TypedDict(
    "BatchEvaluateFeatureResponseTypeDef",
    {
        "results": List["EvaluationResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsDestinationConfigTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigTypeDef",
    {
        "logGroup": str,
    },
    total=False,
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "logGroup": str,
    },
    total=False,
)

_RequiredCreateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentRequestRequestTypeDef",
    {
        "metricGoals": List["MetricGoalConfigTypeDef"],
        "name": str,
        "project": str,
        "treatments": List["TreatmentConfigTypeDef"],
    },
)
_OptionalCreateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentRequestRequestTypeDef",
    {
        "description": str,
        "onlineAbConfig": "OnlineAbConfigTypeDef",
        "randomizationSalt": str,
        "samplingRate": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateExperimentRequestRequestTypeDef(
    _RequiredCreateExperimentRequestRequestTypeDef, _OptionalCreateExperimentRequestRequestTypeDef
):
    pass

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFeatureRequestRequestTypeDef",
    {
        "name": str,
        "project": str,
        "variations": List["VariationConfigTypeDef"],
    },
)
_OptionalCreateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFeatureRequestRequestTypeDef",
    {
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Dict[str, str],
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFeatureRequestRequestTypeDef(
    _RequiredCreateFeatureRequestRequestTypeDef, _OptionalCreateFeatureRequestRequestTypeDef
):
    pass

CreateFeatureResponseTypeDef = TypedDict(
    "CreateFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchRequestRequestTypeDef",
    {
        "groups": List["LaunchGroupConfigTypeDef"],
        "name": str,
        "project": str,
    },
)
_OptionalCreateLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchRequestRequestTypeDef",
    {
        "description": str,
        "metricMonitors": List["MetricMonitorConfigTypeDef"],
        "randomizationSalt": str,
        "scheduledSplitsConfig": "ScheduledSplitsLaunchConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLaunchRequestRequestTypeDef(
    _RequiredCreateLaunchRequestRequestTypeDef, _OptionalCreateLaunchRequestRequestTypeDef
):
    pass

CreateLaunchResponseTypeDef = TypedDict(
    "CreateLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "dataDelivery": "ProjectDataDeliveryConfigTypeDef",
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

DeleteFeatureRequestRequestTypeDef = TypedDict(
    "DeleteFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

DeleteLaunchRequestRequestTypeDef = TypedDict(
    "DeleteLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

_RequiredEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredEvaluateFeatureRequestRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "project": str,
    },
)
_OptionalEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalEvaluateFeatureRequestRequestTypeDef",
    {
        "evaluationContext": str,
    },
    total=False,
)

class EvaluateFeatureRequestRequestTypeDef(
    _RequiredEvaluateFeatureRequestRequestTypeDef, _OptionalEvaluateFeatureRequestRequestTypeDef
):
    pass

EvaluateFeatureResponseTypeDef = TypedDict(
    "EvaluateFeatureResponseTypeDef",
    {
        "details": str,
        "reason": str,
        "value": "VariableValueTypeDef",
        "variation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEvaluationRequestTypeDef = TypedDict(
    "_RequiredEvaluationRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
    },
)
_OptionalEvaluationRequestTypeDef = TypedDict(
    "_OptionalEvaluationRequestTypeDef",
    {
        "evaluationContext": str,
    },
    total=False,
)

class EvaluationRequestTypeDef(
    _RequiredEvaluationRequestTypeDef, _OptionalEvaluationRequestTypeDef
):
    pass

_RequiredEvaluationResultTypeDef = TypedDict(
    "_RequiredEvaluationResultTypeDef",
    {
        "entityId": str,
        "feature": str,
    },
)
_OptionalEvaluationResultTypeDef = TypedDict(
    "_OptionalEvaluationResultTypeDef",
    {
        "details": str,
        "project": str,
        "reason": str,
        "value": "VariableValueTypeDef",
        "variation": str,
    },
    total=False,
)

class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, _OptionalEvaluationResultTypeDef):
    pass

_RequiredEvaluationRuleTypeDef = TypedDict(
    "_RequiredEvaluationRuleTypeDef",
    {
        "type": str,
    },
)
_OptionalEvaluationRuleTypeDef = TypedDict(
    "_OptionalEvaluationRuleTypeDef",
    {
        "name": str,
    },
    total=False,
)

class EvaluationRuleTypeDef(_RequiredEvaluationRuleTypeDef, _OptionalEvaluationRuleTypeDef):
    pass

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "data": str,
        "timestamp": Union[datetime, str],
        "type": EventTypeType,
    },
)

ExperimentExecutionTypeDef = TypedDict(
    "ExperimentExecutionTypeDef",
    {
        "endedTime": datetime,
        "startedTime": datetime,
    },
    total=False,
)

ExperimentReportTypeDef = TypedDict(
    "ExperimentReportTypeDef",
    {
        "content": str,
        "metricName": str,
        "reportName": Literal["BayesianInference"],
        "treatmentName": str,
    },
    total=False,
)

ExperimentResultsDataTypeDef = TypedDict(
    "ExperimentResultsDataTypeDef",
    {
        "metricName": str,
        "resultStat": ExperimentResultResponseTypeType,
        "treatmentName": str,
        "values": List[float],
    },
    total=False,
)

ExperimentScheduleTypeDef = TypedDict(
    "ExperimentScheduleTypeDef",
    {
        "analysisCompleteTime": datetime,
    },
    total=False,
)

_RequiredExperimentTypeDef = TypedDict(
    "_RequiredExperimentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ExperimentStatusType,
        "type": Literal["aws.evidently.onlineab"],
    },
)
_OptionalExperimentTypeDef = TypedDict(
    "_OptionalExperimentTypeDef",
    {
        "description": str,
        "execution": "ExperimentExecutionTypeDef",
        "metricGoals": List["MetricGoalTypeDef"],
        "onlineAbDefinition": "OnlineAbDefinitionTypeDef",
        "project": str,
        "randomizationSalt": str,
        "samplingRate": int,
        "schedule": "ExperimentScheduleTypeDef",
        "statusReason": str,
        "tags": Dict[str, str],
        "treatments": List["TreatmentTypeDef"],
    },
    total=False,
)

class ExperimentTypeDef(_RequiredExperimentTypeDef, _OptionalExperimentTypeDef):
    pass

_RequiredFeatureSummaryTypeDef = TypedDict(
    "_RequiredFeatureSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
    },
)
_OptionalFeatureSummaryTypeDef = TypedDict(
    "_OptionalFeatureSummaryTypeDef",
    {
        "defaultVariation": str,
        "evaluationRules": List["EvaluationRuleTypeDef"],
        "project": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class FeatureSummaryTypeDef(_RequiredFeatureSummaryTypeDef, _OptionalFeatureSummaryTypeDef):
    pass

_RequiredFeatureTypeDef = TypedDict(
    "_RequiredFeatureTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "valueType": VariationValueTypeType,
        "variations": List["VariationTypeDef"],
    },
)
_OptionalFeatureTypeDef = TypedDict(
    "_OptionalFeatureTypeDef",
    {
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Dict[str, str],
        "evaluationRules": List["EvaluationRuleTypeDef"],
        "project": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class FeatureTypeDef(_RequiredFeatureTypeDef, _OptionalFeatureTypeDef):
    pass

GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExperimentResultsRequestRequestTypeDef = TypedDict(
    "_RequiredGetExperimentResultsRequestRequestTypeDef",
    {
        "experiment": str,
        "metricNames": List[str],
        "project": str,
        "treatmentNames": List[str],
    },
)
_OptionalGetExperimentResultsRequestRequestTypeDef = TypedDict(
    "_OptionalGetExperimentResultsRequestRequestTypeDef",
    {
        "baseStat": Literal["Mean"],
        "endTime": Union[datetime, str],
        "period": int,
        "reportNames": List[Literal["BayesianInference"]],
        "resultStats": List[ExperimentResultRequestTypeType],
        "startTime": Union[datetime, str],
    },
    total=False,
)

class GetExperimentResultsRequestRequestTypeDef(
    _RequiredGetExperimentResultsRequestRequestTypeDef,
    _OptionalGetExperimentResultsRequestRequestTypeDef,
):
    pass

GetExperimentResultsResponseTypeDef = TypedDict(
    "GetExperimentResultsResponseTypeDef",
    {
        "reports": List["ExperimentReportTypeDef"],
        "resultsData": List["ExperimentResultsDataTypeDef"],
        "timestamps": List[datetime],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFeatureRequestRequestTypeDef = TypedDict(
    "GetFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

GetFeatureResponseTypeDef = TypedDict(
    "GetFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchRequestRequestTypeDef = TypedDict(
    "GetLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

GetLaunchResponseTypeDef = TypedDict(
    "GetLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchExecutionTypeDef = TypedDict(
    "LaunchExecutionTypeDef",
    {
        "endedTime": datetime,
        "startedTime": datetime,
    },
    total=False,
)

_RequiredLaunchGroupConfigTypeDef = TypedDict(
    "_RequiredLaunchGroupConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
    },
)
_OptionalLaunchGroupConfigTypeDef = TypedDict(
    "_OptionalLaunchGroupConfigTypeDef",
    {
        "description": str,
    },
    total=False,
)

class LaunchGroupConfigTypeDef(
    _RequiredLaunchGroupConfigTypeDef, _OptionalLaunchGroupConfigTypeDef
):
    pass

_RequiredLaunchGroupTypeDef = TypedDict(
    "_RequiredLaunchGroupTypeDef",
    {
        "featureVariations": Dict[str, str],
        "name": str,
    },
)
_OptionalLaunchGroupTypeDef = TypedDict(
    "_OptionalLaunchGroupTypeDef",
    {
        "description": str,
    },
    total=False,
)

class LaunchGroupTypeDef(_RequiredLaunchGroupTypeDef, _OptionalLaunchGroupTypeDef):
    pass

_RequiredLaunchTypeDef = TypedDict(
    "_RequiredLaunchTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": LaunchStatusType,
        "type": Literal["aws.evidently.splits"],
    },
)
_OptionalLaunchTypeDef = TypedDict(
    "_OptionalLaunchTypeDef",
    {
        "description": str,
        "execution": "LaunchExecutionTypeDef",
        "groups": List["LaunchGroupTypeDef"],
        "metricMonitors": List["MetricMonitorTypeDef"],
        "project": str,
        "randomizationSalt": str,
        "scheduledSplitsDefinition": "ScheduledSplitsLaunchDefinitionTypeDef",
        "statusReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class LaunchTypeDef(_RequiredLaunchTypeDef, _OptionalLaunchTypeDef):
    pass

_RequiredListExperimentsRequestRequestTypeDef = TypedDict(
    "_RequiredListExperimentsRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListExperimentsRequestRequestTypeDef = TypedDict(
    "_OptionalListExperimentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListExperimentsRequestRequestTypeDef(
    _RequiredListExperimentsRequestRequestTypeDef, _OptionalListExperimentsRequestRequestTypeDef
):
    pass

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List["ExperimentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFeaturesRequestRequestTypeDef = TypedDict(
    "_RequiredListFeaturesRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListFeaturesRequestRequestTypeDef = TypedDict(
    "_OptionalListFeaturesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFeaturesRequestRequestTypeDef(
    _RequiredListFeaturesRequestRequestTypeDef, _OptionalListFeaturesRequestRequestTypeDef
):
    pass

ListFeaturesResponseTypeDef = TypedDict(
    "ListFeaturesResponseTypeDef",
    {
        "features": List["FeatureSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchesRequestRequestTypeDef = TypedDict(
    "_RequiredListLaunchesRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalListLaunchesRequestRequestTypeDef = TypedDict(
    "_OptionalListLaunchesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLaunchesRequestRequestTypeDef(
    _RequiredListLaunchesRequestRequestTypeDef, _OptionalListLaunchesRequestRequestTypeDef
):
    pass

ListLaunchesResponseTypeDef = TypedDict(
    "ListLaunchesResponseTypeDef",
    {
        "launches": List["LaunchTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "projects": List["ProjectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDefinitionConfigTypeDef = TypedDict(
    "MetricDefinitionConfigTypeDef",
    {
        "entityIdKey": str,
        "eventPattern": str,
        "name": str,
        "unitLabel": str,
        "valueKey": str,
    },
    total=False,
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "entityIdKey": str,
        "eventPattern": str,
        "name": str,
        "unitLabel": str,
        "valueKey": str,
    },
    total=False,
)

_RequiredMetricGoalConfigTypeDef = TypedDict(
    "_RequiredMetricGoalConfigTypeDef",
    {
        "metricDefinition": "MetricDefinitionConfigTypeDef",
    },
)
_OptionalMetricGoalConfigTypeDef = TypedDict(
    "_OptionalMetricGoalConfigTypeDef",
    {
        "desiredChange": ChangeDirectionEnumType,
    },
    total=False,
)

class MetricGoalConfigTypeDef(_RequiredMetricGoalConfigTypeDef, _OptionalMetricGoalConfigTypeDef):
    pass

_RequiredMetricGoalTypeDef = TypedDict(
    "_RequiredMetricGoalTypeDef",
    {
        "metricDefinition": "MetricDefinitionTypeDef",
    },
)
_OptionalMetricGoalTypeDef = TypedDict(
    "_OptionalMetricGoalTypeDef",
    {
        "desiredChange": ChangeDirectionEnumType,
    },
    total=False,
)

class MetricGoalTypeDef(_RequiredMetricGoalTypeDef, _OptionalMetricGoalTypeDef):
    pass

MetricMonitorConfigTypeDef = TypedDict(
    "MetricMonitorConfigTypeDef",
    {
        "metricDefinition": "MetricDefinitionConfigTypeDef",
    },
)

MetricMonitorTypeDef = TypedDict(
    "MetricMonitorTypeDef",
    {
        "metricDefinition": "MetricDefinitionTypeDef",
    },
)

OnlineAbConfigTypeDef = TypedDict(
    "OnlineAbConfigTypeDef",
    {
        "controlTreatmentName": str,
        "treatmentWeights": Dict[str, int],
    },
    total=False,
)

OnlineAbDefinitionTypeDef = TypedDict(
    "OnlineAbDefinitionTypeDef",
    {
        "controlTreatmentName": str,
        "treatmentWeights": Dict[str, int],
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

ProjectDataDeliveryConfigTypeDef = TypedDict(
    "ProjectDataDeliveryConfigTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsDestinationConfigTypeDef",
        "s3Destination": "S3DestinationConfigTypeDef",
    },
    total=False,
)

ProjectDataDeliveryTypeDef = TypedDict(
    "ProjectDataDeliveryTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsDestinationTypeDef",
        "s3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "activeExperimentCount": int,
        "activeLaunchCount": int,
        "description": str,
        "experimentCount": int,
        "featureCount": int,
        "launchCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

_RequiredProjectTypeDef = TypedDict(
    "_RequiredProjectTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
    },
)
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "activeExperimentCount": int,
        "activeLaunchCount": int,
        "dataDelivery": "ProjectDataDeliveryTypeDef",
        "description": str,
        "experimentCount": int,
        "featureCount": int,
        "launchCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass

PutProjectEventsRequestRequestTypeDef = TypedDict(
    "PutProjectEventsRequestRequestTypeDef",
    {
        "events": List["EventTypeDef"],
        "project": str,
    },
)

PutProjectEventsResponseTypeDef = TypedDict(
    "PutProjectEventsResponseTypeDef",
    {
        "eventResults": List["PutProjectEventsResultEntryTypeDef"],
        "failedEventCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProjectEventsResultEntryTypeDef = TypedDict(
    "PutProjectEventsResultEntryTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "eventId": str,
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

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

ScheduledSplitConfigTypeDef = TypedDict(
    "ScheduledSplitConfigTypeDef",
    {
        "groupWeights": Dict[str, int],
        "startTime": Union[datetime, str],
    },
)

_RequiredScheduledSplitTypeDef = TypedDict(
    "_RequiredScheduledSplitTypeDef",
    {
        "startTime": datetime,
    },
)
_OptionalScheduledSplitTypeDef = TypedDict(
    "_OptionalScheduledSplitTypeDef",
    {
        "groupWeights": Dict[str, int],
    },
    total=False,
)

class ScheduledSplitTypeDef(_RequiredScheduledSplitTypeDef, _OptionalScheduledSplitTypeDef):
    pass

ScheduledSplitsLaunchConfigTypeDef = TypedDict(
    "ScheduledSplitsLaunchConfigTypeDef",
    {
        "steps": List["ScheduledSplitConfigTypeDef"],
    },
)

ScheduledSplitsLaunchDefinitionTypeDef = TypedDict(
    "ScheduledSplitsLaunchDefinitionTypeDef",
    {
        "steps": List["ScheduledSplitTypeDef"],
    },
    total=False,
)

StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "analysisCompleteTime": Union[datetime, str],
        "experiment": str,
        "project": str,
    },
)

StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "startedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLaunchRequestRequestTypeDef = TypedDict(
    "StartLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

StartLaunchResponseTypeDef = TypedDict(
    "StartLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredStopExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
_OptionalStopExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalStopExperimentRequestRequestTypeDef",
    {
        "desiredState": ExperimentStopDesiredStateType,
        "reason": str,
    },
    total=False,
)

class StopExperimentRequestRequestTypeDef(
    _RequiredStopExperimentRequestRequestTypeDef, _OptionalStopExperimentRequestRequestTypeDef
):
    pass

StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredStopLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
_OptionalStopLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalStopLaunchRequestRequestTypeDef",
    {
        "desiredState": LaunchStopDesiredStateType,
        "reason": str,
    },
    total=False,
)

class StopLaunchRequestRequestTypeDef(
    _RequiredStopLaunchRequestRequestTypeDef, _OptionalStopLaunchRequestRequestTypeDef
):
    pass

StopLaunchResponseTypeDef = TypedDict(
    "StopLaunchResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTreatmentConfigTypeDef = TypedDict(
    "_RequiredTreatmentConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
    },
)
_OptionalTreatmentConfigTypeDef = TypedDict(
    "_OptionalTreatmentConfigTypeDef",
    {
        "description": str,
    },
    total=False,
)

class TreatmentConfigTypeDef(_RequiredTreatmentConfigTypeDef, _OptionalTreatmentConfigTypeDef):
    pass

_RequiredTreatmentTypeDef = TypedDict(
    "_RequiredTreatmentTypeDef",
    {
        "name": str,
    },
)
_OptionalTreatmentTypeDef = TypedDict(
    "_OptionalTreatmentTypeDef",
    {
        "description": str,
        "featureVariations": Dict[str, str],
    },
    total=False,
)

class TreatmentTypeDef(_RequiredTreatmentTypeDef, _OptionalTreatmentTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
_OptionalUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentRequestRequestTypeDef",
    {
        "description": str,
        "metricGoals": List["MetricGoalConfigTypeDef"],
        "onlineAbConfig": "OnlineAbConfigTypeDef",
        "randomizationSalt": str,
        "samplingRate": int,
        "treatments": List["TreatmentConfigTypeDef"],
    },
    total=False,
)

class UpdateExperimentRequestRequestTypeDef(
    _RequiredUpdateExperimentRequestRequestTypeDef, _OptionalUpdateExperimentRequestRequestTypeDef
):
    pass

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFeatureRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)
_OptionalUpdateFeatureRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureRequestRequestTypeDef",
    {
        "addOrUpdateVariations": List["VariationConfigTypeDef"],
        "defaultVariation": str,
        "description": str,
        "entityOverrides": Dict[str, str],
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "removeVariations": List[str],
    },
    total=False,
)

class UpdateFeatureRequestRequestTypeDef(
    _RequiredUpdateFeatureRequestRequestTypeDef, _OptionalUpdateFeatureRequestRequestTypeDef
):
    pass

UpdateFeatureResponseTypeDef = TypedDict(
    "UpdateFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
_OptionalUpdateLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchRequestRequestTypeDef",
    {
        "description": str,
        "groups": List["LaunchGroupConfigTypeDef"],
        "metricMonitors": List["MetricMonitorConfigTypeDef"],
        "randomizationSalt": str,
        "scheduledSplitsConfig": "ScheduledSplitsLaunchConfigTypeDef",
    },
    total=False,
)

class UpdateLaunchRequestRequestTypeDef(
    _RequiredUpdateLaunchRequestRequestTypeDef, _OptionalUpdateLaunchRequestRequestTypeDef
):
    pass

UpdateLaunchResponseTypeDef = TypedDict(
    "UpdateLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalUpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsDestinationConfigTypeDef",
        "s3Destination": "S3DestinationConfigTypeDef",
    },
    total=False,
)

class UpdateProjectDataDeliveryRequestRequestTypeDef(
    _RequiredUpdateProjectDataDeliveryRequestRequestTypeDef,
    _OptionalUpdateProjectDataDeliveryRequestRequestTypeDef,
):
    pass

UpdateProjectDataDeliveryResponseTypeDef = TypedDict(
    "UpdateProjectDataDeliveryResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "boolValue": bool,
        "doubleValue": float,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

VariationConfigTypeDef = TypedDict(
    "VariationConfigTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
)

VariationTypeDef = TypedDict(
    "VariationTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
    total=False,
)
