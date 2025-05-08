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

class LocationStateTypeDef(TypedDict):
    AllocatedCapacity: NotRequired[int]
    AlwaysOnCapacity: NotRequired[int]
    IdleCapacity: NotRequired[int]
    LocationName: NotRequired[str]
    OnDemandCapacity: NotRequired[int]
    RequestedCapacity: NotRequired[int]
    Status: NotRequired[StreamGroupLocationStatusType]

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
    ApplicationIdentifiers: Sequence[str]
    Identifier: str

class ReplicationStatusTypeDef(TypedDict):
    Location: NotRequired[str]
    Status: NotRequired[ReplicationStatusTypeType]

class DefaultApplicationTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]

class CreateStreamSessionConnectionInputTypeDef(TypedDict):
    Identifier: str
    SignalRequest: str
    StreamSessionIdentifier: str
    ClientToken: NotRequired[str]

class DeleteApplicationInputTypeDef(TypedDict):
    Identifier: str

class DeleteStreamGroupInputTypeDef(TypedDict):
    Identifier: str

class DisassociateApplicationsInputTypeDef(TypedDict):
    ApplicationIdentifiers: Sequence[str]
    Identifier: str

class ExportFilesMetadataTypeDef(TypedDict):
    OutputUri: NotRequired[str]
    Status: NotRequired[ExportFilesStatusType]
    StatusReason: NotRequired[str]

class ExportStreamSessionFilesInputTypeDef(TypedDict):
    Identifier: str
    OutputUri: str
    StreamSessionIdentifier: str

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

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListStreamGroupsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListStreamSessionsByAccountInputTypeDef(TypedDict):
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Status: NotRequired[StreamSessionStatusType]

class ListStreamSessionsInputTypeDef(TypedDict):
    Identifier: str
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Status: NotRequired[StreamSessionStatusType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RemoveStreamGroupLocationsInputTypeDef(TypedDict):
    Identifier: str
    Locations: Sequence[str]

StartStreamSessionInputTypeDef = TypedDict(
    "StartStreamSessionInputTypeDef",
    {
        "ApplicationIdentifier": str,
        "Identifier": str,
        "Protocol": Literal["WebRTC"],
        "SignalRequest": str,
        "AdditionalEnvironmentVariables": NotRequired[Mapping[str, str]],
        "AdditionalLaunchArgs": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "ConnectionTimeoutSeconds": NotRequired[int],
        "Description": NotRequired[str],
        "Locations": NotRequired[Sequence[str]],
        "SessionLengthSeconds": NotRequired[int],
        "UserId": NotRequired[str],
    },
)

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
    ApplicationLogOutputUri: NotRequired[str]
    ApplicationLogPaths: NotRequired[Sequence[str]]
    Description: NotRequired[str]

class AddStreamGroupLocationsInputTypeDef(TypedDict):
    Identifier: str
    LocationConfigurations: Sequence[LocationConfigurationTypeDef]

class CreateStreamGroupInputTypeDef(TypedDict):
    Description: str
    StreamClass: StreamClassType
    ClientToken: NotRequired[str]
    DefaultApplicationIdentifier: NotRequired[str]
    LocationConfigurations: NotRequired[Sequence[LocationConfigurationTypeDef]]
    Tags: NotRequired[Mapping[str, str]]

class UpdateStreamGroupInputTypeDef(TypedDict):
    Identifier: str
    Description: NotRequired[str]
    LocationConfigurations: NotRequired[Sequence[LocationConfigurationTypeDef]]

class AddStreamGroupLocationsOutputTypeDef(TypedDict):
    Identifier: str
    Locations: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateApplicationsOutputTypeDef(TypedDict):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamSessionConnectionOutputTypeDef(TypedDict):
    SignalResponse: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateApplicationsOutputTypeDef(TypedDict):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationSummaryTypeDef(TypedDict):
    Arn: str
    CreatedAt: NotRequired[datetime]
    Description: NotRequired[str]
    Id: NotRequired[str]
    LastUpdatedAt: NotRequired[datetime]
    RuntimeEnvironment: NotRequired[RuntimeEnvironmentTypeDef]
    Status: NotRequired[ApplicationStatusType]

class CreateApplicationInputTypeDef(TypedDict):
    ApplicationSourceUri: str
    Description: str
    ExecutablePath: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ApplicationLogOutputUri: NotRequired[str]
    ApplicationLogPaths: NotRequired[Sequence[str]]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateApplicationOutputTypeDef(TypedDict):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(TypedDict):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationOutputTypeDef(TypedDict):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef

class StreamGroupSummaryTypeDef(TypedDict):
    Arn: str
    CreatedAt: NotRequired[datetime]
    DefaultApplication: NotRequired[DefaultApplicationTypeDef]
    Description: NotRequired[str]
    Id: NotRequired[str]
    LastUpdatedAt: NotRequired[datetime]
    Status: NotRequired[StreamGroupStatusType]
    StreamClass: NotRequired[StreamClassType]

class UpdateStreamGroupOutputTypeDef(TypedDict):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef

GetStreamSessionOutputTypeDef = TypedDict(
    "GetStreamSessionOutputTypeDef",
    {
        "AdditionalEnvironmentVariables": Dict[str, str],
        "AdditionalLaunchArgs": List[str],
        "ApplicationArn": str,
        "Arn": str,
        "ConnectionTimeoutSeconds": int,
        "CreatedAt": datetime,
        "Description": str,
        "ExportFilesMetadata": ExportFilesMetadataTypeDef,
        "LastUpdatedAt": datetime,
        "Location": str,
        "LogFileLocationUri": str,
        "Protocol": Literal["WebRTC"],
        "SessionLengthSeconds": int,
        "SignalRequest": str,
        "SignalResponse": str,
        "Status": StreamSessionStatusType,
        "StatusReason": StreamSessionStatusReasonType,
        "StreamGroupId": str,
        "UserId": str,
        "WebSdkProtocolUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartStreamSessionOutputTypeDef = TypedDict(
    "StartStreamSessionOutputTypeDef",
    {
        "AdditionalEnvironmentVariables": Dict[str, str],
        "AdditionalLaunchArgs": List[str],
        "ApplicationArn": str,
        "Arn": str,
        "ConnectionTimeoutSeconds": int,
        "CreatedAt": datetime,
        "Description": str,
        "ExportFilesMetadata": ExportFilesMetadataTypeDef,
        "LastUpdatedAt": datetime,
        "Location": str,
        "LogFileLocationUri": str,
        "Protocol": Literal["WebRTC"],
        "SessionLengthSeconds": int,
        "SignalRequest": str,
        "SignalResponse": str,
        "Status": StreamSessionStatusType,
        "StatusReason": StreamSessionStatusReasonType,
        "StreamGroupId": str,
        "UserId": str,
        "WebSdkProtocolUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StreamSessionSummaryTypeDef = TypedDict(
    "StreamSessionSummaryTypeDef",
    {
        "ApplicationArn": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ExportFilesMetadata": NotRequired[ExportFilesMetadataTypeDef],
        "LastUpdatedAt": NotRequired[datetime],
        "Location": NotRequired[str],
        "Protocol": NotRequired[Literal["WebRTC"]],
        "Status": NotRequired[StreamSessionStatusType],
        "UserId": NotRequired[str],
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

class ListApplicationsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamGroupsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamSessionsByAccountInputPaginateTypeDef(TypedDict):
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    Status: NotRequired[StreamSessionStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamSessionsInputPaginateTypeDef(TypedDict):
    Identifier: str
    ExportFilesStatus: NotRequired[ExportFilesStatusType]
    Status: NotRequired[StreamSessionStatusType]
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
