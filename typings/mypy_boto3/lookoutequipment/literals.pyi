"""
Type annotations for lookoutequipment service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.literals import DataUploadFrequencyType

    data: DataUploadFrequencyType = "PT10M"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DataUploadFrequencyType",
    "DatasetStatusType",
    "InferenceExecutionStatusType",
    "InferenceSchedulerStatusType",
    "IngestionJobStatusType",
    "LabelRatingType",
    "LatestInferenceResultType",
    "ModelStatusType",
    "MonotonicityType",
    "StatisticalIssueStatusType",
    "TargetSamplingRateType",
)

DataUploadFrequencyType = Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"]
DatasetStatusType = Literal["ACTIVE", "CREATED", "INGESTION_IN_PROGRESS"]
InferenceExecutionStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
InferenceSchedulerStatusType = Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]
IngestionJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
LabelRatingType = Literal["ANOMALY", "NEUTRAL", "NO_ANOMALY"]
LatestInferenceResultType = Literal["ANOMALOUS", "NORMAL"]
ModelStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
MonotonicityType = Literal["DECREASING", "INCREASING", "STATIC"]
StatisticalIssueStatusType = Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"]
TargetSamplingRateType = Literal[
    "PT10M", "PT10S", "PT15M", "PT15S", "PT1H", "PT1M", "PT1S", "PT30M", "PT30S", "PT5M", "PT5S"
]
