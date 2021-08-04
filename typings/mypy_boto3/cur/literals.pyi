"""
Type annotations for cur service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/literals.html)

Usage::

    ```python
    from mypy_boto3_cur.literals import AWSRegionType

    data: AWSRegionType = "af-south-1"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AWSRegionType",
    "AdditionalArtifactType",
    "CompressionFormatType",
    "DescribeReportDefinitionsPaginatorName",
    "ReportFormatType",
    "ReportVersioningType",
    "SchemaElementType",
    "TimeUnitType",
)

AWSRegionType = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
AdditionalArtifactType = Literal["ATHENA", "QUICKSIGHT", "REDSHIFT"]
CompressionFormatType = Literal["GZIP", "Parquet", "ZIP"]
DescribeReportDefinitionsPaginatorName = Literal["describe_report_definitions"]
ReportFormatType = Literal["Parquet", "textORcsv"]
ReportVersioningType = Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"]
SchemaElementType = Literal["RESOURCES"]
TimeUnitType = Literal["DAILY", "HOURLY", "MONTHLY"]
