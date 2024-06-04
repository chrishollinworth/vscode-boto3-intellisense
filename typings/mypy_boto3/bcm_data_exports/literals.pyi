"""
Type annotations for bcm-data-exports service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/literals.html)

Usage::

    ```python
    from mypy_boto3_bcm_data_exports.literals import CompressionOptionType

    data: CompressionOptionType = "GZIP"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CompressionOptionType",
    "ExecutionStatusCodeType",
    "ExecutionStatusReasonType",
    "ExportStatusCodeType",
    "FormatOptionType",
    "FrequencyOptionType",
    "ListExecutionsPaginatorName",
    "ListExportsPaginatorName",
    "ListTablesPaginatorName",
    "OverwriteOptionType",
    "S3OutputTypeType",
)

CompressionOptionType = Literal["GZIP", "PARQUET"]
ExecutionStatusCodeType = Literal[
    "DELIVERY_FAILURE",
    "DELIVERY_IN_PROCESS",
    "DELIVERY_SUCCESS",
    "INITIATION_IN_PROCESS",
    "QUERY_FAILURE",
    "QUERY_IN_PROCESS",
    "QUERY_QUEUED",
]
ExecutionStatusReasonType = Literal[
    "BILL_OWNER_CHANGED", "INSUFFICIENT_PERMISSION", "INTERNAL_FAILURE"
]
ExportStatusCodeType = Literal["HEALTHY", "UNHEALTHY"]
FormatOptionType = Literal["PARQUET", "TEXT_OR_CSV"]
FrequencyOptionType = Literal["SYNCHRONOUS"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListExportsPaginatorName = Literal["list_exports"]
ListTablesPaginatorName = Literal["list_tables"]
OverwriteOptionType = Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"]
S3OutputTypeType = Literal["CUSTOM"]
