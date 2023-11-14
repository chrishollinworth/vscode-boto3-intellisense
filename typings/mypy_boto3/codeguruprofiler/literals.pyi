"""
Type annotations for codeguruprofiler service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.literals import ActionGroupType

    data: ActionGroupType = "agentPermissions"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionGroupType",
    "AgentParameterFieldType",
    "AggregationPeriodType",
    "ComputePlatformType",
    "EventPublisherType",
    "FeedbackTypeType",
    "ListProfileTimesPaginatorName",
    "MetadataFieldType",
    "MetricTypeType",
    "OrderByType",
)

ActionGroupType = Literal["agentPermissions"]
AgentParameterFieldType = Literal[
    "MaxStackDepth",
    "MemoryUsageLimitPercent",
    "MinimumTimeForReportingInMilliseconds",
    "ReportingIntervalInMilliseconds",
    "SamplingIntervalInMilliseconds",
]
AggregationPeriodType = Literal["P1D", "PT1H", "PT5M"]
ComputePlatformType = Literal["AWSLambda", "Default"]
EventPublisherType = Literal["AnomalyDetection"]
FeedbackTypeType = Literal["Negative", "Positive"]
ListProfileTimesPaginatorName = Literal["list_profile_times"]
MetadataFieldType = Literal[
    "AgentId",
    "AwsRequestId",
    "ComputePlatform",
    "ExecutionEnvironment",
    "LambdaFunctionArn",
    "LambdaMemoryLimitInMB",
    "LambdaPreviousExecutionTimeInMilliseconds",
    "LambdaRemainingTimeInMilliseconds",
    "LambdaTimeGapBetweenInvokesInMilliseconds",
]
MetricTypeType = Literal["AggregatedRelativeTotalTime"]
OrderByType = Literal["TimestampAscending", "TimestampDescending"]
