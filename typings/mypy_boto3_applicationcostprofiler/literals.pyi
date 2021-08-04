"""
Type annotations for applicationcostprofiler service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/literals.html)

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.literals import FormatType

    data: FormatType = "CSV"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "FormatType",
    "ListReportDefinitionsPaginatorName",
    "ReportFrequencyType",
    "S3BucketRegionType",
)

FormatType = Literal["CSV", "PARQUET"]
ListReportDefinitionsPaginatorName = Literal["list_report_definitions"]
ReportFrequencyType = Literal["ALL", "DAILY", "MONTHLY"]
S3BucketRegionType = Literal["af-south-1", "ap-east-1", "eu-south-1", "me-south-1"]
