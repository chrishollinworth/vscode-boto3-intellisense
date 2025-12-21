"""
Type annotations for mwaa-serverless service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mwaa_serverless.type_defs import DefinitionS3LocationTypeDef

    data: DefinitionS3LocationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    EncryptionTypeType,
    RunTypeType,
    TaskInstanceStatusType,
    WorkflowRunStatusType,
    WorkflowStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateWorkflowRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DefinitionS3LocationTypeDef",
    "DeleteWorkflowRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetTaskInstanceRequestTypeDef",
    "GetTaskInstanceResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskInstancesRequestPaginateTypeDef",
    "ListTaskInstancesRequestTypeDef",
    "ListTaskInstancesResponseTypeDef",
    "ListWorkflowRunsRequestPaginateTypeDef",
    "ListWorkflowRunsRequestTypeDef",
    "ListWorkflowRunsResponseTypeDef",
    "ListWorkflowVersionsRequestPaginateTypeDef",
    "ListWorkflowVersionsRequestTypeDef",
    "ListWorkflowVersionsResponseTypeDef",
    "ListWorkflowsRequestPaginateTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RunDetailSummaryTypeDef",
    "ScheduleConfigurationTypeDef",
    "StartWorkflowRunRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopWorkflowRunRequestTypeDef",
    "StopWorkflowRunResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TaskInstanceSummaryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateWorkflowRequestTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "WorkflowRunDetailTypeDef",
    "WorkflowRunSummaryTypeDef",
    "WorkflowSummaryTypeDef",
    "WorkflowVersionSummaryTypeDef",
)

class DefinitionS3LocationTypeDef(TypedDict):
    Bucket: str
    ObjectKey: str
    VersionId: NotRequired[str]

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "Type": EncryptionTypeType,
        "KmsKeyId": NotRequired[str],
    },
)

class LoggingConfigurationTypeDef(TypedDict):
    LogGroupName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteWorkflowRequestTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: NotRequired[str]

class GetTaskInstanceRequestTypeDef(TypedDict):
    WorkflowArn: str
    TaskInstanceId: str
    RunId: str

class GetWorkflowRequestTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: NotRequired[str]

class NetworkConfigurationOutputTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]

class ScheduleConfigurationTypeDef(TypedDict):
    CronExpression: NotRequired[str]

class GetWorkflowRunRequestTypeDef(TypedDict):
    WorkflowArn: str
    RunId: str

class WorkflowRunDetailTypeDef(TypedDict):
    WorkflowArn: NotRequired[str]
    WorkflowVersion: NotRequired[str]
    RunId: NotRequired[str]
    RunType: NotRequired[RunTypeType]
    StartedOn: NotRequired[datetime]
    CreatedAt: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    ModifiedAt: NotRequired[datetime]
    Duration: NotRequired[int]
    ErrorMessage: NotRequired[str]
    TaskInstances: NotRequired[List[str]]
    RunState: NotRequired[WorkflowRunStatusType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTaskInstancesRequestTypeDef(TypedDict):
    WorkflowArn: str
    RunId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TaskInstanceSummaryTypeDef(TypedDict):
    WorkflowArn: NotRequired[str]
    WorkflowVersion: NotRequired[str]
    RunId: NotRequired[str]
    TaskInstanceId: NotRequired[str]
    Status: NotRequired[TaskInstanceStatusType]
    DurationInSeconds: NotRequired[int]
    OperatorName: NotRequired[str]

class ListWorkflowRunsRequestTypeDef(TypedDict):
    WorkflowArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    WorkflowVersion: NotRequired[str]

class ListWorkflowVersionsRequestTypeDef(TypedDict):
    WorkflowArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListWorkflowsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class WorkflowSummaryTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    ModifiedAt: NotRequired[datetime]
    WorkflowStatus: NotRequired[WorkflowStatusType]
    TriggerMode: NotRequired[str]

class NetworkConfigurationTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]

class RunDetailSummaryTypeDef(TypedDict):
    Status: NotRequired[WorkflowRunStatusType]
    CreatedOn: NotRequired[datetime]
    StartedAt: NotRequired[datetime]
    EndedAt: NotRequired[datetime]

class StartWorkflowRunRequestTypeDef(TypedDict):
    WorkflowArn: str
    ClientToken: NotRequired[str]
    OverrideParameters: NotRequired[Mapping[str, Mapping[str, Any]]]
    WorkflowVersion: NotRequired[str]

class StopWorkflowRunRequestTypeDef(TypedDict):
    WorkflowArn: str
    RunId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateWorkflowResponseTypeDef(TypedDict):
    WorkflowArn: str
    CreatedAt: datetime
    RevisionId: str
    WorkflowStatus: WorkflowStatusType
    WorkflowVersion: str
    IsLatestVersion: bool
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowResponseTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaskInstanceResponseTypeDef(TypedDict):
    WorkflowArn: str
    RunId: str
    TaskInstanceId: str
    WorkflowVersion: str
    Status: TaskInstanceStatusType
    DurationInSeconds: int
    OperatorName: str
    ModifiedAt: datetime
    EndedAt: datetime
    StartedAt: datetime
    AttemptNumber: int
    ErrorMessage: str
    TaskId: str
    LogStream: str
    Xcom: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkflowRunResponseTypeDef(TypedDict):
    RunId: str
    Status: WorkflowRunStatusType
    StartedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopWorkflowRunResponseTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: str
    RunId: str
    Status: WorkflowRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowResponseTypeDef(TypedDict):
    WorkflowArn: str
    ModifiedAt: datetime
    WorkflowVersion: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowResponseTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: str
    Name: str
    Description: str
    CreatedAt: datetime
    ModifiedAt: datetime
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    LoggingConfiguration: LoggingConfigurationTypeDef
    EngineVersion: int
    WorkflowStatus: WorkflowStatusType
    DefinitionS3Location: DefinitionS3LocationTypeDef
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    RoleArn: str
    NetworkConfiguration: NetworkConfigurationOutputTypeDef
    TriggerMode: str
    WorkflowDefinition: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowVersionSummaryTypeDef(TypedDict):
    WorkflowVersion: str
    WorkflowArn: str
    IsLatestVersion: NotRequired[bool]
    CreatedAt: NotRequired[datetime]
    ModifiedAt: NotRequired[datetime]
    DefinitionS3Location: NotRequired[DefinitionS3LocationTypeDef]
    ScheduleConfiguration: NotRequired[ScheduleConfigurationTypeDef]
    TriggerMode: NotRequired[str]

class GetWorkflowRunResponseTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: str
    RunId: str
    RunType: RunTypeType
    OverrideParameters: Dict[str, Dict[str, Any]]
    RunDetail: WorkflowRunDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTaskInstancesRequestPaginateTypeDef(TypedDict):
    WorkflowArn: str
    RunId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowRunsRequestPaginateTypeDef(TypedDict):
    WorkflowArn: str
    WorkflowVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowVersionsRequestPaginateTypeDef(TypedDict):
    WorkflowArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaskInstancesResponseTypeDef(TypedDict):
    TaskInstances: List[TaskInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkflowsResponseTypeDef(TypedDict):
    Workflows: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]

class WorkflowRunSummaryTypeDef(TypedDict):
    RunId: NotRequired[str]
    WorkflowArn: NotRequired[str]
    WorkflowVersion: NotRequired[str]
    RunType: NotRequired[RunTypeType]
    RunDetailSummary: NotRequired[RunDetailSummaryTypeDef]

class ListWorkflowVersionsResponseTypeDef(TypedDict):
    WorkflowVersions: List[WorkflowVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateWorkflowRequestTypeDef(TypedDict):
    Name: str
    DefinitionS3Location: DefinitionS3LocationTypeDef
    RoleArn: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    LoggingConfiguration: NotRequired[LoggingConfigurationTypeDef]
    EngineVersion: NotRequired[int]
    NetworkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    TriggerMode: NotRequired[str]

class UpdateWorkflowRequestTypeDef(TypedDict):
    WorkflowArn: str
    DefinitionS3Location: DefinitionS3LocationTypeDef
    RoleArn: str
    Description: NotRequired[str]
    LoggingConfiguration: NotRequired[LoggingConfigurationTypeDef]
    EngineVersion: NotRequired[int]
    NetworkConfiguration: NotRequired[NetworkConfigurationUnionTypeDef]
    TriggerMode: NotRequired[str]

class ListWorkflowRunsResponseTypeDef(TypedDict):
    WorkflowRuns: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
