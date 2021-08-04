"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionRequestRequestTypeDef

    data: DescribeJobExecutionRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DescribeJobExecutionRequestRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsRequestRequestTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "StartNextPendingJobExecutionRequestRequestTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionRequestRequestTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

_RequiredDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeJobExecutionRequestRequestTypeDef",
    {
        "includeJobDocument": bool,
        "executionNumber": int,
    },
    total=False,
)

class DescribeJobExecutionRequestRequestTypeDef(
    _RequiredDescribeJobExecutionRequestRequestTypeDef,
    _OptionalDescribeJobExecutionRequestRequestTypeDef,
):
    pass

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPendingJobExecutionsRequestRequestTypeDef = TypedDict(
    "GetPendingJobExecutionsRequestRequestTypeDef",
    {
        "thingName": str,
    },
)

GetPendingJobExecutionsResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List["JobExecutionSummaryTypeDef"],
        "queuedJobs": List["JobExecutionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobExecutionStateTypeDef = TypedDict(
    "JobExecutionStateTypeDef",
    {
        "status": JobExecutionStatusType,
        "statusDetails": Dict[str, str],
        "versionNumber": int,
    },
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "jobId": str,
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "versionNumber": int,
        "executionNumber": int,
    },
    total=False,
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
        "statusDetails": Dict[str, str],
        "queuedAt": int,
        "startedAt": int,
        "lastUpdatedAt": int,
        "approximateSecondsBeforeTimedOut": int,
        "versionNumber": int,
        "executionNumber": int,
        "jobDocument": str,
    },
    total=False,
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

_RequiredStartNextPendingJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartNextPendingJobExecutionRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalStartNextPendingJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartNextPendingJobExecutionRequestRequestTypeDef",
    {
        "statusDetails": Dict[str, str],
        "stepTimeoutInMinutes": int,
    },
    total=False,
)

class StartNextPendingJobExecutionRequestRequestTypeDef(
    _RequiredStartNextPendingJobExecutionRequestRequestTypeDef,
    _OptionalStartNextPendingJobExecutionRequestRequestTypeDef,
):
    pass

StartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
    },
)
_OptionalUpdateJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobExecutionRequestRequestTypeDef",
    {
        "statusDetails": Dict[str, str],
        "stepTimeoutInMinutes": int,
        "expectedVersion": int,
        "includeJobExecutionState": bool,
        "includeJobDocument": bool,
        "executionNumber": int,
    },
    total=False,
)

class UpdateJobExecutionRequestRequestTypeDef(
    _RequiredUpdateJobExecutionRequestRequestTypeDef,
    _OptionalUpdateJobExecutionRequestRequestTypeDef,
):
    pass

UpdateJobExecutionResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseTypeDef",
    {
        "executionState": "JobExecutionStateTypeDef",
        "jobDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
