"""
Type annotations for lookoutmetrics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.literals import AggregationFunctionType

    data: AggregationFunctionType = "AVG"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregationFunctionType",
    "AlertStatusType",
    "AlertTypeType",
    "AnomalyDetectionTaskStatusType",
    "AnomalyDetectorFailureTypeType",
    "AnomalyDetectorStatusType",
    "CSVFileCompressionType",
    "ConfidenceType",
    "FrequencyType",
    "JsonFileCompressionType",
    "RelationshipTypeType",
    "SnsFormatType",
)

AggregationFunctionType = Literal["AVG", "SUM"]
AlertStatusType = Literal["ACTIVE", "INACTIVE"]
AlertTypeType = Literal["LAMBDA", "SNS"]
AnomalyDetectionTaskStatusType = Literal[
    "COMPLETED", "FAILED", "FAILED_TO_SCHEDULE", "IN_PROGRESS", "PENDING"
]
AnomalyDetectorFailureTypeType = Literal[
    "ACTIVATION_FAILURE", "BACK_TEST_ACTIVATION_FAILURE", "DEACTIVATION_FAILURE", "DELETION_FAILURE"
]
AnomalyDetectorStatusType = Literal[
    "ACTIVATING",
    "ACTIVE",
    "BACK_TEST_ACTIVATING",
    "BACK_TEST_ACTIVE",
    "BACK_TEST_COMPLETE",
    "DEACTIVATED",
    "DEACTIVATING",
    "DELETING",
    "FAILED",
    "INACTIVE",
    "LEARNING",
]
CSVFileCompressionType = Literal["GZIP", "NONE"]
ConfidenceType = Literal["HIGH", "LOW", "NONE"]
FrequencyType = Literal["P1D", "PT10M", "PT1H", "PT5M"]
JsonFileCompressionType = Literal["GZIP", "NONE"]
RelationshipTypeType = Literal["CAUSE_OF_INPUT_ANOMALY_GROUP", "EFFECT_OF_INPUT_ANOMALY_GROUP"]
SnsFormatType = Literal["JSON", "LONG_TEXT", "SHORT_TEXT"]
