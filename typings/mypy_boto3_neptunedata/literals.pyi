"""
Type annotations for neptunedata service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/literals.html)

Usage::

    ```python
    from mypy_boto3_neptunedata.literals import ActionType

    data: ActionType = "initiateDatabaseReset"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionType",
    "EncodingType",
    "FormatType",
    "GraphSummaryTypeType",
    "IteratorTypeType",
    "ModeType",
    "OpenCypherExplainModeType",
    "ParallelismType",
    "S3BucketRegionType",
    "StatisticsAutoGenerationModeType",
)

ActionType = Literal["initiateDatabaseReset", "performDatabaseReset"]
EncodingType = Literal["gzip"]
FormatType = Literal["csv", "nquads", "ntriples", "opencypher", "rdfxml", "turtle"]
GraphSummaryTypeType = Literal["basic", "detailed"]
IteratorTypeType = Literal["AFTER_SEQUENCE_NUMBER", "AT_SEQUENCE_NUMBER", "LATEST", "TRIM_HORIZON"]
ModeType = Literal["AUTO", "NEW", "RESUME"]
OpenCypherExplainModeType = Literal["details", "dynamic", "static"]
ParallelismType = Literal["HIGH", "LOW", "MEDIUM", "OVERSUBSCRIBE"]
S3BucketRegionType = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-west-1",
    "us-west-2",
]
StatisticsAutoGenerationModeType = Literal["disableAutoCompute", "enableAutoCompute", "refresh"]
