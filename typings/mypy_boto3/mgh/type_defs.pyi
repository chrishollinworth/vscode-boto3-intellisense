"""
Type annotations for mgh service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ApplicationStateTypeDef",
    "AssociateCreatedArtifactRequestTypeDef",
    "AssociateDiscoveredResourceRequestTypeDef",
    "AssociateSourceResourceRequestTypeDef",
    "CreateProgressUpdateStreamRequestTypeDef",
    "CreatedArtifactTypeDef",
    "DeleteProgressUpdateStreamRequestTypeDef",
    "DescribeApplicationStateRequestTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskRequestTypeDef",
    "DescribeMigrationTaskResultTypeDef",
    "DisassociateCreatedArtifactRequestTypeDef",
    "DisassociateDiscoveredResourceRequestTypeDef",
    "DisassociateSourceResourceRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "ImportMigrationTaskRequestTypeDef",
    "ListApplicationStatesRequestPaginateTypeDef",
    "ListApplicationStatesRequestTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsRequestPaginateTypeDef",
    "ListCreatedArtifactsRequestTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesRequestPaginateTypeDef",
    "ListDiscoveredResourcesRequestTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTaskUpdatesRequestPaginateTypeDef",
    "ListMigrationTaskUpdatesRequestTypeDef",
    "ListMigrationTaskUpdatesResultTypeDef",
    "ListMigrationTasksRequestPaginateTypeDef",
    "ListMigrationTasksRequestTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsRequestPaginateTypeDef",
    "ListProgressUpdateStreamsRequestTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "ListSourceResourcesRequestPaginateTypeDef",
    "ListSourceResourcesRequestTypeDef",
    "ListSourceResourcesResultTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "MigrationTaskUpdateTypeDef",
    "NotifyApplicationStateRequestTypeDef",
    "NotifyMigrationTaskStateRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "PutResourceAttributesRequestTypeDef",
    "ResourceAttributeTypeDef",
    "ResponseMetadataTypeDef",
    "SourceResourceTypeDef",
    "TaskTypeDef",
    "TimestampTypeDef",
)

class ApplicationStateTypeDef(TypedDict):
    ApplicationId: NotRequired[str]
    ApplicationStatus: NotRequired[ApplicationStatusType]
    LastUpdatedTime: NotRequired[datetime]

class CreatedArtifactTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]

class DiscoveredResourceTypeDef(TypedDict):
    ConfigurationId: str
    Description: NotRequired[str]

class SourceResourceTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    StatusDetail: NotRequired[str]

class CreateProgressUpdateStreamRequestTypeDef(TypedDict):
    ProgressUpdateStreamName: str
    DryRun: NotRequired[bool]

class DeleteProgressUpdateStreamRequestTypeDef(TypedDict):
    ProgressUpdateStreamName: str
    DryRun: NotRequired[bool]

class DescribeApplicationStateRequestTypeDef(TypedDict):
    ApplicationId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DescribeMigrationTaskRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str

class DisassociateCreatedArtifactRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifactName: str
    DryRun: NotRequired[bool]

class DisassociateDiscoveredResourceRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ConfigurationId: str
    DryRun: NotRequired[bool]

class DisassociateSourceResourceRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResourceName: str
    DryRun: NotRequired[bool]

class ImportMigrationTaskRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DryRun: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationStatesRequestTypeDef(TypedDict):
    ApplicationIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCreatedArtifactsRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDiscoveredResourcesRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMigrationTaskUpdatesRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMigrationTasksRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ResourceName: NotRequired[str]

class MigrationTaskSummaryTypeDef(TypedDict):
    ProgressUpdateStream: NotRequired[str]
    MigrationTaskName: NotRequired[str]
    Status: NotRequired[StatusType]
    ProgressPercent: NotRequired[int]
    StatusDetail: NotRequired[str]
    UpdateDateTime: NotRequired[datetime]

class ListProgressUpdateStreamsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ProgressUpdateStreamSummaryTypeDef(TypedDict):
    ProgressUpdateStreamName: NotRequired[str]

class ListSourceResourcesRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
    },
)

class TaskTypeDef(TypedDict):
    Status: StatusType
    StatusDetail: NotRequired[str]
    ProgressPercent: NotRequired[int]

TimestampTypeDef = Union[datetime, str]

class AssociateCreatedArtifactRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifact: CreatedArtifactTypeDef
    DryRun: NotRequired[bool]

class AssociateDiscoveredResourceRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DiscoveredResource: DiscoveredResourceTypeDef
    DryRun: NotRequired[bool]

class AssociateSourceResourceRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResource: SourceResourceTypeDef
    DryRun: NotRequired[bool]

class DescribeApplicationStateResultTypeDef(TypedDict):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationStatesResultTypeDef(TypedDict):
    ApplicationStateList: List[ApplicationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCreatedArtifactsResultTypeDef(TypedDict):
    CreatedArtifactList: List[CreatedArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDiscoveredResourcesResultTypeDef(TypedDict):
    DiscoveredResourceList: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSourceResourcesResultTypeDef(TypedDict):
    SourceResourceList: List[SourceResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationStatesRequestPaginateTypeDef(TypedDict):
    ApplicationIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCreatedArtifactsRequestPaginateTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDiscoveredResourcesRequestPaginateTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMigrationTaskUpdatesRequestPaginateTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMigrationTasksRequestPaginateTypeDef(TypedDict):
    ResourceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProgressUpdateStreamsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSourceResourcesRequestPaginateTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMigrationTasksResultTypeDef(TypedDict):
    MigrationTaskSummaryList: List[MigrationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProgressUpdateStreamsResultTypeDef(TypedDict):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourceAttributesRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ResourceAttributeList: Sequence[ResourceAttributeTypeDef]
    DryRun: NotRequired[bool]

class MigrationTaskTypeDef(TypedDict):
    ProgressUpdateStream: NotRequired[str]
    MigrationTaskName: NotRequired[str]
    Task: NotRequired[TaskTypeDef]
    UpdateDateTime: NotRequired[datetime]
    ResourceAttributeList: NotRequired[List[ResourceAttributeTypeDef]]

class MigrationTaskUpdateTypeDef(TypedDict):
    UpdateDateTime: NotRequired[datetime]
    UpdateType: NotRequired[Literal["MIGRATION_TASK_STATE_UPDATED"]]
    MigrationTaskState: NotRequired[TaskTypeDef]

class NotifyApplicationStateRequestTypeDef(TypedDict):
    ApplicationId: str
    Status: ApplicationStatusType
    UpdateDateTime: NotRequired[TimestampTypeDef]
    DryRun: NotRequired[bool]

class NotifyMigrationTaskStateRequestTypeDef(TypedDict):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: TaskTypeDef
    UpdateDateTime: TimestampTypeDef
    NextUpdateSeconds: int
    DryRun: NotRequired[bool]

class DescribeMigrationTaskResultTypeDef(TypedDict):
    MigrationTask: MigrationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMigrationTaskUpdatesResultTypeDef(TypedDict):
    MigrationTaskUpdateList: List[MigrationTaskUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
