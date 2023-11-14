"""
Type annotations for iotevents service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/literals.html)

Usage::

    ```python
    from mypy_boto3_iotevents.literals import AlarmModelVersionStatusType

    data: AlarmModelVersionStatusType = "ACTIVATING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlarmModelVersionStatusType",
    "AnalysisResultLevelType",
    "AnalysisStatusType",
    "ComparisonOperatorType",
    "DetectorModelVersionStatusType",
    "EvaluationMethodType",
    "InputStatusType",
    "LoggingLevelType",
    "PayloadTypeType",
)

AlarmModelVersionStatusType = Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"]
AnalysisResultLevelType = Literal["ERROR", "INFO", "WARNING"]
AnalysisStatusType = Literal["COMPLETE", "FAILED", "RUNNING"]
ComparisonOperatorType = Literal[
    "EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "NOT_EQUAL"
]
DetectorModelVersionStatusType = Literal[
    "ACTIVATING", "ACTIVE", "DEPRECATED", "DRAFT", "FAILED", "INACTIVE", "PAUSED"
]
EvaluationMethodType = Literal["BATCH", "SERIAL"]
InputStatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
LoggingLevelType = Literal["DEBUG", "ERROR", "INFO"]
PayloadTypeType = Literal["JSON", "STRING"]
