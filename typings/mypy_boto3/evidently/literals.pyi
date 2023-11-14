"""
Type annotations for evidently service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_evidently/literals.html)

Usage::

    ```python
    from mypy_boto3_evidently.literals import ChangeDirectionEnumType

    data: ChangeDirectionEnumType = "DECREASE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeDirectionEnumType",
    "EventTypeType",
    "ExperimentBaseStatType",
    "ExperimentReportNameType",
    "ExperimentResultRequestTypeType",
    "ExperimentResultResponseTypeType",
    "ExperimentStatusType",
    "ExperimentStopDesiredStateType",
    "ExperimentTypeType",
    "FeatureEvaluationStrategyType",
    "FeatureStatusType",
    "LaunchStatusType",
    "LaunchStopDesiredStateType",
    "LaunchTypeType",
    "ListExperimentsPaginatorName",
    "ListFeaturesPaginatorName",
    "ListLaunchesPaginatorName",
    "ListProjectsPaginatorName",
    "ListSegmentReferencesPaginatorName",
    "ListSegmentsPaginatorName",
    "ProjectStatusType",
    "SegmentReferenceResourceTypeType",
    "VariationValueTypeType",
)

ChangeDirectionEnumType = Literal["DECREASE", "INCREASE"]
EventTypeType = Literal["aws.evidently.custom", "aws.evidently.evaluation"]
ExperimentBaseStatType = Literal["Mean"]
ExperimentReportNameType = Literal["BayesianInference"]
ExperimentResultRequestTypeType = Literal[
    "BaseStat", "ConfidenceInterval", "PValue", "TreatmentEffect"
]
ExperimentResultResponseTypeType = Literal[
    "ConfidenceIntervalLowerBound",
    "ConfidenceIntervalUpperBound",
    "Mean",
    "PValue",
    "TreatmentEffect",
]
ExperimentStatusType = Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
ExperimentStopDesiredStateType = Literal["CANCELLED", "COMPLETED"]
ExperimentTypeType = Literal["aws.evidently.onlineab"]
FeatureEvaluationStrategyType = Literal["ALL_RULES", "DEFAULT_VARIATION"]
FeatureStatusType = Literal["AVAILABLE", "UPDATING"]
LaunchStatusType = Literal["CANCELLED", "COMPLETED", "CREATED", "RUNNING", "UPDATING"]
LaunchStopDesiredStateType = Literal["CANCELLED", "COMPLETED"]
LaunchTypeType = Literal["aws.evidently.splits"]
ListExperimentsPaginatorName = Literal["list_experiments"]
ListFeaturesPaginatorName = Literal["list_features"]
ListLaunchesPaginatorName = Literal["list_launches"]
ListProjectsPaginatorName = Literal["list_projects"]
ListSegmentReferencesPaginatorName = Literal["list_segment_references"]
ListSegmentsPaginatorName = Literal["list_segments"]
ProjectStatusType = Literal["AVAILABLE", "UPDATING"]
SegmentReferenceResourceTypeType = Literal["EXPERIMENT", "LAUNCH"]
VariationValueTypeType = Literal["BOOLEAN", "DOUBLE", "LONG", "STRING"]
