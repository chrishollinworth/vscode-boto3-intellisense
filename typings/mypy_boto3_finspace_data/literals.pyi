"""
Type annotations for finspace-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/literals.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.literals import ChangeTypeType

    data: ChangeTypeType = "APPEND"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeTypeType",
    "ColumnDataTypeType",
    "DataViewStatusType",
    "DatasetKindType",
    "DatasetStatusType",
    "ErrorCategoryType",
    "IngestionStatusType",
    "ListChangesetsPaginatorName",
    "ListDataViewsPaginatorName",
    "ListDatasetsPaginatorName",
    "locationTypeType",
)

ChangeTypeType = Literal["APPEND", "MODIFY", "REPLACE"]
ColumnDataTypeType = Literal[
    "BIGINT",
    "BINARY",
    "BOOLEAN",
    "CHAR",
    "DATE",
    "DATETIME",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "SMALLINT",
    "STRING",
    "TINYINT",
]
DataViewStatusType = Literal[
    "CANCELLED",
    "FAILED",
    "FAILED_CLEANUP_FAILED",
    "PENDING",
    "RUNNING",
    "STARTING",
    "SUCCESS",
    "TIMEOUT",
]
DatasetKindType = Literal["NON_TABULAR", "TABULAR"]
DatasetStatusType = Literal["FAILED", "PENDING", "RUNNING", "SUCCESS"]
ErrorCategoryType = Literal[
    "ACCESS_DENIED",
    "CANCELLED",
    "INTERNAL_SERVICE_EXCEPTION",
    "RESOURCE_NOT_FOUND",
    "SERVICE_QUOTA_EXCEEDED",
    "THROTTLING",
    "USER_RECOVERABLE",
    "VALIDATION",
]
IngestionStatusType = Literal["FAILED", "PENDING", "RUNNING", "STOP_REQUESTED", "SUCCESS"]
ListChangesetsPaginatorName = Literal["list_changesets"]
ListDataViewsPaginatorName = Literal["list_data_views"]
ListDatasetsPaginatorName = Literal["list_datasets"]
locationTypeType = Literal["INGESTION", "SAGEMAKER"]
