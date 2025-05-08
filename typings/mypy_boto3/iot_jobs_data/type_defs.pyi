"""
Type annotations for iot-jobs-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping
else:
    from typing import Dict, List, Mapping
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "CommandParameterValueTypeDef",
    "DescribeJobExecutionRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsRequestTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "StartCommandExecutionRequestTypeDef",
    "StartCommandExecutionResponseTypeDef",
    "StartNextPendingJobExecutionRequestTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionRequestTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DescribeJobExecutionRequestTypeDef(TypedDict):
    jobId: str
    thingName: str
    includeJobDocument: NotRequired[bool]
    executionNumber: NotRequired[int]

class JobExecutionTypeDef(TypedDict):
    jobId: NotRequired[str]
    thingName: NotRequired[str]
    status: NotRequired[JobExecutionStatusType]
    statusDetails: NotRequired[Dict[str, str]]
    queuedAt: NotRequired[int]
    startedAt: NotRequired[int]
    lastUpdatedAt: NotRequired[int]
    approximateSecondsBeforeTimedOut: NotRequired[int]
    versionNumber: NotRequired[int]
    executionNumber: NotRequired[int]
    jobDocument: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetPendingJobExecutionsRequestTypeDef(TypedDict):
    thingName: str

class JobExecutionSummaryTypeDef(TypedDict):
    jobId: NotRequired[str]
    queuedAt: NotRequired[int]
    startedAt: NotRequired[int]
    lastUpdatedAt: NotRequired[int]
    versionNumber: NotRequired[int]
    executionNumber: NotRequired[int]

class JobExecutionStateTypeDef(TypedDict):
    status: NotRequired[JobExecutionStatusType]
    statusDetails: NotRequired[Dict[str, str]]
    versionNumber: NotRequired[int]

class StartNextPendingJobExecutionRequestTypeDef(TypedDict):
    thingName: str
    statusDetails: NotRequired[Mapping[str, str]]
    stepTimeoutInMinutes: NotRequired[int]

class UpdateJobExecutionRequestTypeDef(TypedDict):
    jobId: str
    thingName: str
    status: JobExecutionStatusType
    statusDetails: NotRequired[Mapping[str, str]]
    stepTimeoutInMinutes: NotRequired[int]
    expectedVersion: NotRequired[int]
    includeJobExecutionState: NotRequired[bool]
    includeJobDocument: NotRequired[bool]
    executionNumber: NotRequired[int]

class CommandParameterValueTypeDef(TypedDict):
    S: NotRequired[str]
    B: NotRequired[bool]
    I: NotRequired[int]
    L: NotRequired[int]
    D: NotRequired[float]
    BIN: NotRequired[BlobTypeDef]
    UL: NotRequired[str]

class DescribeJobExecutionResponseTypeDef(TypedDict):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCommandExecutionResponseTypeDef(TypedDict):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartNextPendingJobExecutionResponseTypeDef(TypedDict):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPendingJobExecutionsResponseTypeDef(TypedDict):
    inProgressJobs: List[JobExecutionSummaryTypeDef]
    queuedJobs: List[JobExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobExecutionResponseTypeDef(TypedDict):
    executionState: JobExecutionStateTypeDef
    jobDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCommandExecutionRequestTypeDef(TypedDict):
    targetArn: str
    commandArn: str
    parameters: NotRequired[Mapping[str, CommandParameterValueTypeDef]]
    executionTimeoutSeconds: NotRequired[int]
    clientToken: NotRequired[str]
