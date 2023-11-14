"""
Type annotations for databrew service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/literals.html)

Usage::

    ```python
    from mypy_boto3_databrew.literals import AnalyticsModeType

    data: AnalyticsModeType = "DISABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnalyticsModeType",
    "CompressionFormatType",
    "DatabaseOutputModeType",
    "EncryptionModeType",
    "InputFormatType",
    "JobRunStateType",
    "JobTypeType",
    "ListDatasetsPaginatorName",
    "ListJobRunsPaginatorName",
    "ListJobsPaginatorName",
    "ListProjectsPaginatorName",
    "ListRecipeVersionsPaginatorName",
    "ListRecipesPaginatorName",
    "ListRulesetsPaginatorName",
    "ListSchedulesPaginatorName",
    "LogSubscriptionType",
    "OrderType",
    "OrderedByType",
    "OutputFormatType",
    "ParameterTypeType",
    "SampleModeType",
    "SampleTypeType",
    "SessionStatusType",
    "SourceType",
    "ThresholdTypeType",
    "ThresholdUnitType",
    "ValidationModeType",
)

AnalyticsModeType = Literal["DISABLE", "ENABLE"]
CompressionFormatType = Literal[
    "BROTLI", "BZIP2", "DEFLATE", "GZIP", "LZ4", "LZO", "SNAPPY", "ZLIB", "ZSTD"
]
DatabaseOutputModeType = Literal["NEW_TABLE"]
EncryptionModeType = Literal["SSE-KMS", "SSE-S3"]
InputFormatType = Literal["CSV", "EXCEL", "JSON", "ORC", "PARQUET"]
JobRunStateType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
JobTypeType = Literal["PROFILE", "RECIPE"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListJobRunsPaginatorName = Literal["list_job_runs"]
ListJobsPaginatorName = Literal["list_jobs"]
ListProjectsPaginatorName = Literal["list_projects"]
ListRecipeVersionsPaginatorName = Literal["list_recipe_versions"]
ListRecipesPaginatorName = Literal["list_recipes"]
ListRulesetsPaginatorName = Literal["list_rulesets"]
ListSchedulesPaginatorName = Literal["list_schedules"]
LogSubscriptionType = Literal["DISABLE", "ENABLE"]
OrderType = Literal["ASCENDING", "DESCENDING"]
OrderedByType = Literal["LAST_MODIFIED_DATE"]
OutputFormatType = Literal[
    "AVRO", "CSV", "GLUEPARQUET", "JSON", "ORC", "PARQUET", "TABLEAUHYPER", "XML"
]
ParameterTypeType = Literal["Datetime", "Number", "String"]
SampleModeType = Literal["CUSTOM_ROWS", "FULL_DATASET"]
SampleTypeType = Literal["FIRST_N", "LAST_N", "RANDOM"]
SessionStatusType = Literal[
    "ASSIGNED",
    "FAILED",
    "INITIALIZING",
    "PROVISIONING",
    "READY",
    "RECYCLING",
    "ROTATING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
]
SourceType = Literal["DATA-CATALOG", "DATABASE", "S3"]
ThresholdTypeType = Literal[
    "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
ThresholdUnitType = Literal["COUNT", "PERCENTAGE"]
ValidationModeType = Literal["CHECK_ALL"]
