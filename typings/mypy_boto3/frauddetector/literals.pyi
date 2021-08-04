"""
Type annotations for frauddetector service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/literals.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.literals import AsyncJobStatusType

    data: AsyncJobStatusType = "CANCEL_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AsyncJobStatusType",
    "DataSourceType",
    "DataTypeType",
    "DetectorVersionStatusType",
    "LanguageType",
    "ModelEndpointStatusType",
    "ModelInputDataFormatType",
    "ModelOutputDataFormatType",
    "ModelSourceType",
    "ModelTypeEnumType",
    "ModelVersionStatusType",
    "RuleExecutionModeType",
    "TrainingDataSourceEnumType",
)

AsyncJobStatusType = Literal[
    "CANCELED",
    "CANCEL_IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "IN_PROGRESS",
    "IN_PROGRESS_INITIALIZING",
]
DataSourceType = Literal["EVENT", "EXTERNAL_MODEL_SCORE", "MODEL_SCORE"]
DataTypeType = Literal["BOOLEAN", "FLOAT", "INTEGER", "STRING"]
DetectorVersionStatusType = Literal["ACTIVE", "DRAFT", "INACTIVE"]
LanguageType = Literal["DETECTORPL"]
ModelEndpointStatusType = Literal["ASSOCIATED", "DISSOCIATED"]
ModelInputDataFormatType = Literal["APPLICATION_JSON", "TEXT_CSV"]
ModelOutputDataFormatType = Literal["APPLICATION_JSONLINES", "TEXT_CSV"]
ModelSourceType = Literal["SAGEMAKER"]
ModelTypeEnumType = Literal["ONLINE_FRAUD_INSIGHTS"]
ModelVersionStatusType = Literal["ACTIVE", "INACTIVE", "TRAINING_CANCELLED"]
RuleExecutionModeType = Literal["ALL_MATCHED", "FIRST_MATCHED"]
TrainingDataSourceEnumType = Literal["EXTERNAL_EVENTS"]
