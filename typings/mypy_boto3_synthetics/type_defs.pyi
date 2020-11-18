"""
Main interface for synthetics service type definitions.

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import CanaryCodeOutputTypeDef

    data: CanaryCodeOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CanaryCodeOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "ResponseMetadata",
    "RuntimeVersionTypeDef",
    "VpcConfigOutputTypeDef",
    "CanaryCodeInputTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryScheduleInputTypeDef",
    "CreateCanaryResponseTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "VpcConfigInputTypeDef",
)

CanaryCodeOutputTypeDef = TypedDict(
    "CanaryCodeOutputTypeDef",
    {"SourceLocationArn": str, "Handler": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CanaryLastRunTypeDef = TypedDict(
    "CanaryLastRunTypeDef", {"CanaryName": str, "LastRun": "CanaryRunTypeDef"}, total=False
)

CanaryRunConfigOutputTypeDef = TypedDict(
    "CanaryRunConfigOutputTypeDef",
    {
        "TimeoutInSeconds": int,
        "MemoryInMB": int,
        "ActiveTracing": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CanaryRunStatusTypeDef = TypedDict(
    "CanaryRunStatusTypeDef",
    {
        "State": Literal["RUNNING", "PASSED", "FAILED"],
        "StateReason": str,
        "StateReasonCode": Literal["CANARY_FAILURE", "EXECUTION_FAILURE"],
    },
    total=False,
)

CanaryRunTimelineTypeDef = TypedDict(
    "CanaryRunTimelineTypeDef", {"Started": datetime, "Completed": datetime}, total=False
)

CanaryRunTypeDef = TypedDict(
    "CanaryRunTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "CanaryRunStatusTypeDef",
        "Timeline": "CanaryRunTimelineTypeDef",
        "ArtifactS3Location": str,
    },
    total=False,
)

CanaryScheduleOutputTypeDef = TypedDict(
    "CanaryScheduleOutputTypeDef",
    {"Expression": str, "DurationInSeconds": int, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CanaryStatusTypeDef = TypedDict(
    "CanaryStatusTypeDef",
    {
        "State": Literal[
            "CREATING",
            "READY",
            "STARTING",
            "RUNNING",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
            "DELETING",
        ],
        "StateReason": str,
        "StateReasonCode": Literal["INVALID_PERMISSIONS"],
    },
    total=False,
)

CanaryTimelineTypeDef = TypedDict(
    "CanaryTimelineTypeDef",
    {
        "Created": datetime,
        "LastModified": datetime,
        "LastStarted": datetime,
        "LastStopped": datetime,
    },
    total=False,
)

CanaryTypeDef = TypedDict(
    "CanaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Code": "CanaryCodeOutputTypeDef",
        "ExecutionRoleArn": str,
        "Schedule": "CanaryScheduleOutputTypeDef",
        "RunConfig": "CanaryRunConfigOutputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "Status": "CanaryStatusTypeDef",
        "Timeline": "CanaryTimelineTypeDef",
        "ArtifactS3Location": str,
        "EngineArn": str,
        "RuntimeVersion": str,
        "VpcConfig": "VpcConfigOutputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RuntimeVersionTypeDef = TypedDict(
    "RuntimeVersionTypeDef",
    {"VersionName": str, "Description": str, "ReleaseDate": datetime, "DeprecationDate": datetime},
    total=False,
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredCanaryCodeInputTypeDef = TypedDict("_RequiredCanaryCodeInputTypeDef", {"Handler": str})
_OptionalCanaryCodeInputTypeDef = TypedDict(
    "_OptionalCanaryCodeInputTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3Version": str, "ZipFile": Union[bytes, IO[bytes]]},
    total=False,
)


class CanaryCodeInputTypeDef(_RequiredCanaryCodeInputTypeDef, _OptionalCanaryCodeInputTypeDef):
    pass


CanaryRunConfigInputTypeDef = TypedDict(
    "CanaryRunConfigInputTypeDef",
    {
        "TimeoutInSeconds": int,
        "MemoryInMB": int,
        "ActiveTracing": bool,
        "EnvironmentVariables": Dict[str, str],
    },
    total=False,
)

_RequiredCanaryScheduleInputTypeDef = TypedDict(
    "_RequiredCanaryScheduleInputTypeDef", {"Expression": str}
)
_OptionalCanaryScheduleInputTypeDef = TypedDict(
    "_OptionalCanaryScheduleInputTypeDef", {"DurationInSeconds": int}, total=False
)


class CanaryScheduleInputTypeDef(
    _RequiredCanaryScheduleInputTypeDef, _OptionalCanaryScheduleInputTypeDef
):
    pass


CreateCanaryResponseTypeDef = TypedDict(
    "CreateCanaryResponseTypeDef", {"Canary": "CanaryTypeDef"}, total=False
)

DescribeCanariesLastRunResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseTypeDef",
    {"CanariesLastRun": List["CanaryLastRunTypeDef"], "NextToken": str},
    total=False,
)

DescribeCanariesResponseTypeDef = TypedDict(
    "DescribeCanariesResponseTypeDef",
    {"Canaries": List["CanaryTypeDef"], "NextToken": str},
    total=False,
)

DescribeRuntimeVersionsResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseTypeDef",
    {"RuntimeVersions": List["RuntimeVersionTypeDef"], "NextToken": str},
    total=False,
)

GetCanaryResponseTypeDef = TypedDict(
    "GetCanaryResponseTypeDef", {"Canary": "CanaryTypeDef"}, total=False
)

GetCanaryRunsResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseTypeDef",
    {"CanaryRuns": List["CanaryRunTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

VpcConfigInputTypeDef = TypedDict(
    "VpcConfigInputTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}, total=False
)
