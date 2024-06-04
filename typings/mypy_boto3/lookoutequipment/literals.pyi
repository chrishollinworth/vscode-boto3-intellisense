"""
Type annotations for lookoutequipment service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.literals import AutoPromotionResultType

    data: AutoPromotionResultType = "MODEL_NOT_PROMOTED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutoPromotionResultType",
    "DataUploadFrequencyType",
    "DatasetStatusType",
    "InferenceDataImportStrategyType",
    "InferenceExecutionStatusType",
    "InferenceSchedulerStatusType",
    "IngestionJobStatusType",
    "LabelRatingType",
    "LatestInferenceResultType",
    "ModelPromoteModeType",
    "ModelQualityType",
    "ModelStatusType",
    "ModelVersionSourceTypeType",
    "ModelVersionStatusType",
    "MonotonicityType",
    "RetrainingSchedulerStatusType",
    "StatisticalIssueStatusType",
    "TargetSamplingRateType",
)

AutoPromotionResultType = Literal[
    "MODEL_NOT_PROMOTED",
    "MODEL_PROMOTED",
    "RETRAINING_CANCELLED",
    "RETRAINING_CUSTOMER_ERROR",
    "RETRAINING_INTERNAL_ERROR",
]
DataUploadFrequencyType = Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"]
DatasetStatusType = Literal["ACTIVE", "CREATED", "IMPORT_IN_PROGRESS", "INGESTION_IN_PROGRESS"]
InferenceDataImportStrategyType = Literal["ADD_WHEN_EMPTY", "NO_IMPORT", "OVERWRITE"]
InferenceExecutionStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
InferenceSchedulerStatusType = Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]
IngestionJobStatusType = Literal["FAILED", "IMPORT_IN_PROGRESS", "IN_PROGRESS", "SUCCESS"]
LabelRatingType = Literal["ANOMALY", "NEUTRAL", "NO_ANOMALY"]
LatestInferenceResultType = Literal["ANOMALOUS", "NORMAL"]
ModelPromoteModeType = Literal["MANAGED", "MANUAL"]
ModelQualityType = Literal[
    "CANNOT_DETERMINE_QUALITY", "POOR_QUALITY_DETECTED", "QUALITY_THRESHOLD_MET"
]
ModelStatusType = Literal["FAILED", "IMPORT_IN_PROGRESS", "IN_PROGRESS", "SUCCESS"]
ModelVersionSourceTypeType = Literal["IMPORT", "RETRAINING", "TRAINING"]
ModelVersionStatusType = Literal[
    "CANCELED", "FAILED", "IMPORT_IN_PROGRESS", "IN_PROGRESS", "SUCCESS"
]
MonotonicityType = Literal["DECREASING", "INCREASING", "STATIC"]
RetrainingSchedulerStatusType = Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]
StatisticalIssueStatusType = Literal["NO_ISSUE_DETECTED", "POTENTIAL_ISSUE_DETECTED"]
TargetSamplingRateType = Literal[
    "PT10M", "PT10S", "PT15M", "PT15S", "PT1H", "PT1M", "PT1S", "PT30M", "PT30S", "PT5M", "PT5S"
]
