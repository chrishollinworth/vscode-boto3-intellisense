"""
Type annotations for gameliftstreams service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_gameliftstreams.type_defs import LocationConfigurationTypeDef

    data: LocationConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ApplicationStatusReasonType,
    ApplicationStatusType,
    ExportFilesStatusType,
    ReplicationStatusTypeType,
    RuntimeEnvironmentTypeType,
    StreamClassType,
    StreamGroupLocationStatusType,
    StreamGroupStatusReasonType,
    StreamGroupStatusType,
    StreamSessionStatusReasonType,
    StreamSessionStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddStreamGroupLocationsInputTypeDef",
    "AddStreamGroupLocationsOutputTypeDef",
    "ApplicationSummaryTypeDef",
    "AssociateApplicationsInputTypeDef",
    "AssociateApplicationsOutputTypeDef",
    "CreateApplicationInputTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateStreamGroupInputTypeDef",
    "CreateStreamGroupOutputTypeDef",
    "CreateStreamSessionConnectionInputTypeDef",
    "CreateStreamSessionConnectionOutputTypeDef",
    "DefaultApplicationTypeDef",
    "DeleteApplicationInputTypeDef",
    "DeleteStreamGroupInputTypeDef",
    "DisassociateApplicationsInputTypeDef",
    "DisassociateApplicationsOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportFilesMetadataTypeDef",
    "ExportStreamSessionFilesInputTypeDef",
    "GetApplicationInputTypeDef",
    "GetApplicationInputWaitExtraTypeDef",
    "GetApplicationInputWaitTypeDef",
    "GetApplicationOutputTypeDef",
    "GetStreamGroupInputTypeDef",
    "GetStreamGroupInputWaitExtraTypeDef",
    "GetStreamGroupInputWaitTypeDef",
    "GetStreamGroupOutputTypeDef",
    "GetStreamSessionInputTypeDef",
    "GetStreamSessionInputWaitTypeDef",
    "GetStreamSessionOutputTypeDef",
    "ListApplicationsInputPaginateTypeDef",
    "ListApplicationsInputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListStreamGroupsInputPaginateTypeDef",
    "ListStreamGroupsInputTypeDef",
    "ListStreamGroupsOutputTypeDef",
    "ListStreamSessionsByAccountInputPaginateTypeDef",
    "ListStreamSessionsByAccountInputTypeDef",
    "ListStreamSessionsByAccountOutputTypeDef",
    "ListStreamSessionsInputPaginateTypeDef",
    "ListStreamSessionsInputTypeDef",
    "ListStreamSessionsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationConfigurationTypeDef",
    "LocationStateTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceStatsConfigurationTypeDef",
    "RemoveStreamGroupLocationsInputTypeDef",
    "ReplicationStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeEnvironmentTypeDef",
    "StartStreamSessionInputTypeDef",
    "StartStreamSessionOutputTypeDef",
    "StreamGroupSummaryTypeDef",
    "StreamSessionSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TerminateStreamSessionInputTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationInputTypeDef",
    "UpdateApplicationOutputTypeDef",
    "UpdateStreamGroupInputTypeDef",
    "UpdateStreamGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)

class LocationConfigurationTypeDef(TypedDict):
    LocationName: str
    AlwaysOnCapacity: NotRequired[int]
    OnDemandCapacity: NotRequired[int]
    TargetIdleCapacity: NotRequired[int]
    MaximumCapacity: NotRequired[int]

class LocationStateTypeDef(TypedDict):
    LocationName: NotRequired[str]
    Status: NotRequired[StreamGroupLocationStatusType]
    AlwaysOnCapacity: NotRequired[int]
    OnDemandCapacity: NotRequired[int]
    TargetIdleCapacity: NotRequired[int]
    MaximumCapacity: NotRequired[int]
    RequestedCapacity: NotRequired[int]
    AllocatedCapacity: NotRequired[int]
    IdleCapacity: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

RuntimeEnvironmentTypeDef = TypedDict(
    "RuntimeEnvironmentTypeDef",
    {
        "Type": RuntimeEnvironmentTypeType,
        "Version": str,
    },
)

class AssociateApplicationsInputTypeDef(TypedDict):
    Identifier: str
    ApplicationIdentifiers: Sequence[str]

class ReplicationStatusTypeDef(TypedDict):
    Location: NotRequired[str]
    Status: NotRequired[ReplicationStatusTypeType]

class DefaultApplicationTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]

class CreateStreamSessionConnectionInputTypeDef(TypedDict):
    Identifier: str
    StreamSessionIdentifier: str
    SignalRequest: str
    ClientToken: NotRequired[str]

class DeleteApplicationInputTypeDef(TypedDict):
    Identifier: str

class DeleteStreamGroupInputTypeDef(TypedDict):
    Identifier: str

class DisassociateApplicationsInputTypeDef(TypedDict):
    Identifier: str
    ApplicationIdentifiers: Sequence[str]

class ExportFilesMetadataTypeDef(TypedDict):
    Status: NotRequired[ExportFilesStatusType]
    StatusReason: NotRequired[str]
    OutputUri: NotRequired[str]

class ExportStreamSessionFilesInputTypeDef(TypedDict):
    Identifier: str
    StreamSessionIdentifier: str
    OutputUri: str

class GetApplicationInputTypeDef(TypedDict):
    Identifier: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetStreamGroupInputTypeDef(TypedDict):
    Identifier: str

class GetStreamSessionInputTypeDef(TypedDict):
    Identifier: str
    StreamSessionIdentifier: str

class PerformanceStatsConfigurationTypeDef(TypedDict):
    SharedWithClient: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListStreamGroupsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListStreamSessionsByAccountInputTypeDef(TypedDict):
    Status: NotRequired[StreamSessionStatusType]
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListStreamSessionsInputTypeDef(TypedDict):
    Identifier: str
    Status: NotRequired[StreamSessionStatusType]
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RemoveStreamGroupLocationsInputTypeDef(TypedDict):
    Identifier: str
    Locations: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class TerminateStreamSessionInputTypeDef(TypedDict):
    Identifier: str
    StreamSessionIdentifier: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationInputTypeDef(TypedDict):
    Identifier: str
    Description: NotRequired[str]
    ApplicationLogPaths: NotRequired[Sequence[str]]
    ApplicationLogOutputUri: NotRequired[str]

class AddStreamGroupLocationsInputTypeDef(TypedDict):
    Identifier: str
    LocationConfigurations: Sequence[LocationConfigurationTypeDef]

class CreateStreamGroupInputTypeDef(TypedDict):
    Description: str
    StreamClass: StreamClassType
    DefaultApplicationIdentifier: NotRequired[str]
    LocationConfigurations: NotRequired[Sequence[LocationConfigurationTypeDef]]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]

class UpdateStreamGroupInputTypeDef(TypedDict):
    Identifier: str
    LocationConfigurations: NotRequired[Sequence[LocationConfigurationTypeDef]]
    Description: NotRequired[str]
    DefaultApplicationIdentifier: NotRequired[str]

class AddStreamGroupLocationsOutputTypeDef(TypedDict):
    Identifier: str
    Locations: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateApplicationsOutputTypeDef(TypedDict):
    Arn: str
    ApplicationArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamSessionConnectionOutputTypeDef(TypedDict):
    SignalResponse: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateApplicationsOutputTypeDef(TypedDict):
    Arn: str
    ApplicationArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationSummaryTypeDef(TypedDict):
    Arn: str
    Id: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[ApplicationStatusType]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    RuntimeEnvironment: NotRequired[RuntimeEnvironmentTypeDef]

class CreateApplicationInputTypeDef(TypedDict):
    Description: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ExecutablePath: str
    ApplicationSourceUri: str
    ApplicationLogPaths: NotRequired[Sequence[str]]
    ApplicationLogOutputUri: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]

class CreateApplicationOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ExecutablePath: str
    ApplicationLogPaths: List[str]
    ApplicationLogOutputUri: str
    ApplicationSourceUri: str
    Id: str
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    AssociatedStreamGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ExecutablePath: str
    ApplicationLogPaths: List[str]
    ApplicationLogOutputUri: str
    ApplicationSourceUri: str
    Id: str
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    AssociatedStreamGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ExecutablePath: str
    ApplicationLogPaths: List[str]
    ApplicationLogOutputUri: str
    ApplicationSourceUri: str
    Id: str
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    AssociatedStreamGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    DefaultApplication: DefaultApplicationTypeDef
    LocationStates: List[LocationStateTypeDef]
    StreamClass: StreamClassType
    Id: str
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    LastUpdatedAt: datetime
    CreatedAt: datetime
    ExpiresAt: datetime
    AssociatedApplications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    DefaultApplication: DefaultApplicationTypeDef
    LocationStates: List[LocationStateTypeDef]
    StreamClass: StreamClassType
    Id: str
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    LastUpdatedAt: datetime
    CreatedAt: datetime
    ExpiresAt: datetime
    AssociatedApplications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StreamGroupSummaryTypeDef(TypedDict):
    Arn: str
    Id: NotRequired[str]
    Description: NotRequired[str]
    DefaultApplication: NotRequired[DefaultApplicationTypeDef]
    StreamClass: NotRequired[StreamClassType]
    Status: NotRequired[StreamGroupStatusType]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    ExpiresAt: NotRequired[datetime]

class UpdateStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    Description: str
    DefaultApplication: DefaultApplicationTypeDef
    LocationStates: List[LocationStateTypeDef]
    StreamClass: StreamClassType
    Id: str
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    LastUpdatedAt: datetime
    CreatedAt: datetime
    ExpiresAt: datetime
    AssociatedApplications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

StreamSessionSummaryTypeDef = TypedDict(
    "StreamSessionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "UserId": NotRequired[str],
        "Status": NotRequired[StreamSessionStatusType],
        "StatusReason": NotRequired[StreamSessionStatusReasonType],
        "Protocol": NotRequired[Literal["WebRTC"]],
        "LastUpdatedAt": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "ApplicationArn": NotRequired[str],
        "ExportFilesMetadata": NotRequired[ExportFilesMetadataTypeDef],
        "Location": NotRequired[str],
    },
)

class GetApplicationInputWaitExtraTypeDef(TypedDict):
    Identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetApplicationInputWaitTypeDef(TypedDict):
    Identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetStreamGroupInputWaitExtraTypeDef(TypedDict):
    Identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetStreamGroupInputWaitTypeDef(TypedDict):
    Identifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetStreamSessionInputWaitTypeDef(TypedDict):
    Identifier: str
    StreamSessionIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

GetStreamSessionOutputTypeDef = TypedDict(
    "GetStreamSessionOutputTypeDef",
    {
        "Arn": str,
        "Description": str,
        "StreamGroupId": str,
        "UserId": str,
        "Status": StreamSessionStatusType,
        "StatusReason": StreamSessionStatusReasonType,
        "Protocol": Literal["WebRTC"],
        "Location": str,
        "SignalRequest": str,
        "SignalResponse": str,
        "ConnectionTimeoutSeconds": int,
        "SessionLengthSeconds": int,
        "AdditionalLaunchArgs": List[str],
        "AdditionalEnvironmentVariables": Dict[str, str],
        "PerformanceStatsConfiguration": PerformanceStatsConfigurationTypeDef,
        "LogFileLocationUri": str,
        "WebSdkProtocolUrl": str,
        "LastUpdatedAt": datetime,
        "CreatedAt": datetime,
        "ApplicationArn": str,
        "ExportFilesMetadata": ExportFilesMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartStreamSessionInputTypeDef = TypedDict(
    "StartStreamSessionInputTypeDef",
    {
        "Identifier": str,
        "Protocol": Literal["WebRTC"],
        "SignalRequest": str,
        "ApplicationIdentifier": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "UserId": NotRequired[str],
        "Locations": NotRequired[Sequence[str]],
        "ConnectionTimeoutSeconds": NotRequired[int],
        "SessionLengthSeconds": NotRequired[int],
        "AdditionalLaunchArgs": NotRequired[Sequence[str]],
        "AdditionalEnvironmentVariables": NotRequired[Mapping[str, str]],
        "PerformanceStatsConfiguration": NotRequired[PerformanceStatsConfigurationTypeDef],
    },
)
StartStreamSessionOutputTypeDef = TypedDict(
    "StartStreamSessionOutputTypeDef",
    {
        "Arn": str,
        "Description": str,
        "StreamGroupId": str,
        "UserId": str,
        "Status": StreamSessionStatusType,
        "StatusReason": StreamSessionStatusReasonType,
        "Protocol": Literal["WebRTC"],
        "Location": str,
        "SignalRequest": str,
        "SignalResponse": str,
        "ConnectionTimeoutSeconds": int,
        "SessionLengthSeconds": int,
        "AdditionalLaunchArgs": List[str],
        "AdditionalEnvironmentVariables": Dict[str, str],
        "PerformanceStatsConfiguration": PerformanceStatsConfigurationTypeDef,
        "LogFileLocationUri": str,
        "WebSdkProtocolUrl": str,
        "LastUpdatedAt": datetime,
        "CreatedAt": datetime,
        "ApplicationArn": str,
        "ExportFilesMetadata": ExportFilesMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListApplicationsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamGroupsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamSessionsByAccountInputPaginateTypeDef(TypedDict):
    Status: NotRequired[StreamSessionStatusType]
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamSessionsInputPaginateTypeDef(TypedDict):
    Identifier: str
    Status: NotRequired[StreamSessionStatusType]
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationsOutputTypeDef(TypedDict):
    Items: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStreamGroupsOutputTypeDef(TypedDict):
    Items: List[StreamGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStreamSessionsByAccountOutputTypeDef(TypedDict):
    Items: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStreamSessionsOutputTypeDef(TypedDict):
    Items: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
