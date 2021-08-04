"""
Type annotations for synthetics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import BaseScreenshotTypeDef

    data: BaseScreenshotTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import CanaryRunStateReasonCodeType, CanaryRunStateType, CanaryStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BaseScreenshotTypeDef",
    "CanaryCodeInputTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "CreateCanaryRequestRequestTypeDef",
    "CreateCanaryResponseTypeDef",
    "DeleteCanaryRequestRequestTypeDef",
    "DescribeCanariesLastRunRequestRequestTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesRequestRequestTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "GetCanaryRequestRequestTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsRequestRequestTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeVersionTypeDef",
    "StartCanaryRequestRequestTypeDef",
    "StopCanaryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCanaryRequestRequestTypeDef",
    "VisualReferenceInputTypeDef",
    "VisualReferenceOutputTypeDef",
    "VpcConfigInputTypeDef",
    "VpcConfigOutputTypeDef",
)

_RequiredBaseScreenshotTypeDef = TypedDict(
    "_RequiredBaseScreenshotTypeDef",
    {
        "ScreenshotName": str,
    },
)
_OptionalBaseScreenshotTypeDef = TypedDict(
    "_OptionalBaseScreenshotTypeDef",
    {
        "IgnoreCoordinates": List[str],
    },
    total=False,
)

class BaseScreenshotTypeDef(_RequiredBaseScreenshotTypeDef, _OptionalBaseScreenshotTypeDef):
    pass

_RequiredCanaryCodeInputTypeDef = TypedDict(
    "_RequiredCanaryCodeInputTypeDef",
    {
        "Handler": str,
    },
)
_OptionalCanaryCodeInputTypeDef = TypedDict(
    "_OptionalCanaryCodeInputTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3Version": str,
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class CanaryCodeInputTypeDef(_RequiredCanaryCodeInputTypeDef, _OptionalCanaryCodeInputTypeDef):
    pass

CanaryCodeOutputTypeDef = TypedDict(
    "CanaryCodeOutputTypeDef",
    {
        "SourceLocationArn": str,
        "Handler": str,
    },
    total=False,
)

CanaryLastRunTypeDef = TypedDict(
    "CanaryLastRunTypeDef",
    {
        "CanaryName": str,
        "LastRun": "CanaryRunTypeDef",
    },
    total=False,
)

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

CanaryRunConfigOutputTypeDef = TypedDict(
    "CanaryRunConfigOutputTypeDef",
    {
        "TimeoutInSeconds": int,
        "MemoryInMB": int,
        "ActiveTracing": bool,
    },
    total=False,
)

CanaryRunStatusTypeDef = TypedDict(
    "CanaryRunStatusTypeDef",
    {
        "State": CanaryRunStateType,
        "StateReason": str,
        "StateReasonCode": CanaryRunStateReasonCodeType,
    },
    total=False,
)

CanaryRunTimelineTypeDef = TypedDict(
    "CanaryRunTimelineTypeDef",
    {
        "Started": datetime,
        "Completed": datetime,
    },
    total=False,
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

_RequiredCanaryScheduleInputTypeDef = TypedDict(
    "_RequiredCanaryScheduleInputTypeDef",
    {
        "Expression": str,
    },
)
_OptionalCanaryScheduleInputTypeDef = TypedDict(
    "_OptionalCanaryScheduleInputTypeDef",
    {
        "DurationInSeconds": int,
    },
    total=False,
)

class CanaryScheduleInputTypeDef(
    _RequiredCanaryScheduleInputTypeDef, _OptionalCanaryScheduleInputTypeDef
):
    pass

CanaryScheduleOutputTypeDef = TypedDict(
    "CanaryScheduleOutputTypeDef",
    {
        "Expression": str,
        "DurationInSeconds": int,
    },
    total=False,
)

CanaryStatusTypeDef = TypedDict(
    "CanaryStatusTypeDef",
    {
        "State": CanaryStateType,
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
        "VisualReference": "VisualReferenceOutputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateCanaryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "Code": "CanaryCodeInputTypeDef",
        "ArtifactS3Location": str,
        "ExecutionRoleArn": str,
        "Schedule": "CanaryScheduleInputTypeDef",
        "RuntimeVersion": str,
    },
)
_OptionalCreateCanaryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCanaryRequestRequestTypeDef",
    {
        "RunConfig": "CanaryRunConfigInputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "VpcConfig": "VpcConfigInputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCanaryRequestRequestTypeDef(
    _RequiredCreateCanaryRequestRequestTypeDef, _OptionalCreateCanaryRequestRequestTypeDef
):
    pass

CreateCanaryResponseTypeDef = TypedDict(
    "CreateCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCanaryRequestRequestTypeDef = TypedDict(
    "DeleteCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeCanariesLastRunRequestRequestTypeDef = TypedDict(
    "DescribeCanariesLastRunRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeCanariesLastRunResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseTypeDef",
    {
        "CanariesLastRun": List["CanaryLastRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCanariesRequestRequestTypeDef = TypedDict(
    "DescribeCanariesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeCanariesResponseTypeDef = TypedDict(
    "DescribeCanariesResponseTypeDef",
    {
        "Canaries": List["CanaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeVersionsRequestRequestTypeDef = TypedDict(
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRuntimeVersionsResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseTypeDef",
    {
        "RuntimeVersions": List["RuntimeVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCanaryRequestRequestTypeDef = TypedDict(
    "GetCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetCanaryResponseTypeDef = TypedDict(
    "GetCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCanaryRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCanaryRunsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetCanaryRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCanaryRunsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetCanaryRunsRequestRequestTypeDef(
    _RequiredGetCanaryRunsRequestRequestTypeDef, _OptionalGetCanaryRunsRequestRequestTypeDef
):
    pass

GetCanaryRunsResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseTypeDef",
    {
        "CanaryRuns": List["CanaryRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
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
    {
        "VersionName": str,
        "Description": str,
        "ReleaseDate": datetime,
        "DeprecationDate": datetime,
    },
    total=False,
)

StartCanaryRequestRequestTypeDef = TypedDict(
    "StartCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopCanaryRequestRequestTypeDef = TypedDict(
    "StopCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateCanaryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCanaryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCanaryRequestRequestTypeDef",
    {
        "Code": "CanaryCodeInputTypeDef",
        "ExecutionRoleArn": str,
        "RuntimeVersion": str,
        "Schedule": "CanaryScheduleInputTypeDef",
        "RunConfig": "CanaryRunConfigInputTypeDef",
        "SuccessRetentionPeriodInDays": int,
        "FailureRetentionPeriodInDays": int,
        "VpcConfig": "VpcConfigInputTypeDef",
        "VisualReference": "VisualReferenceInputTypeDef",
    },
    total=False,
)

class UpdateCanaryRequestRequestTypeDef(
    _RequiredUpdateCanaryRequestRequestTypeDef, _OptionalUpdateCanaryRequestRequestTypeDef
):
    pass

_RequiredVisualReferenceInputTypeDef = TypedDict(
    "_RequiredVisualReferenceInputTypeDef",
    {
        "BaseCanaryRunId": str,
    },
)
_OptionalVisualReferenceInputTypeDef = TypedDict(
    "_OptionalVisualReferenceInputTypeDef",
    {
        "BaseScreenshots": List["BaseScreenshotTypeDef"],
    },
    total=False,
)

class VisualReferenceInputTypeDef(
    _RequiredVisualReferenceInputTypeDef, _OptionalVisualReferenceInputTypeDef
):
    pass

VisualReferenceOutputTypeDef = TypedDict(
    "VisualReferenceOutputTypeDef",
    {
        "BaseScreenshots": List["BaseScreenshotTypeDef"],
        "BaseCanaryRunId": str,
    },
    total=False,
)

VpcConfigInputTypeDef = TypedDict(
    "VpcConfigInputTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)
