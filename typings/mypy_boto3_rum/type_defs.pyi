"""
Type annotations for rum service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_rum.type_defs import AppMonitorConfigurationOutputTypeDef

    data: AppMonitorConfigurationOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CustomEventsStatusType,
    DeobfuscationStatusType,
    MetricDestinationType,
    StateEnumType,
    TelemetryType,
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
    "AppMonitorConfigurationOutputTypeDef",
    "AppMonitorConfigurationTypeDef",
    "AppMonitorConfigurationUnionTypeDef",
    "AppMonitorDetailsTypeDef",
    "AppMonitorSummaryTypeDef",
    "AppMonitorTypeDef",
    "BatchCreateRumMetricDefinitionsErrorTypeDef",
    "BatchCreateRumMetricDefinitionsRequestTypeDef",
    "BatchCreateRumMetricDefinitionsResponseTypeDef",
    "BatchDeleteRumMetricDefinitionsErrorTypeDef",
    "BatchDeleteRumMetricDefinitionsRequestTypeDef",
    "BatchDeleteRumMetricDefinitionsResponseTypeDef",
    "BatchGetRumMetricDefinitionsRequestPaginateTypeDef",
    "BatchGetRumMetricDefinitionsRequestTypeDef",
    "BatchGetRumMetricDefinitionsResponseTypeDef",
    "CreateAppMonitorRequestTypeDef",
    "CreateAppMonitorResponseTypeDef",
    "CustomEventsTypeDef",
    "CwLogTypeDef",
    "DataStorageTypeDef",
    "DeleteAppMonitorRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteRumMetricsDestinationRequestTypeDef",
    "DeobfuscationConfigurationTypeDef",
    "GetAppMonitorDataRequestPaginateTypeDef",
    "GetAppMonitorDataRequestTypeDef",
    "GetAppMonitorDataResponseTypeDef",
    "GetAppMonitorRequestTypeDef",
    "GetAppMonitorResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "JavaScriptSourceMapsTypeDef",
    "ListAppMonitorsRequestPaginateTypeDef",
    "ListAppMonitorsRequestTypeDef",
    "ListAppMonitorsResponseTypeDef",
    "ListRumMetricsDestinationsRequestPaginateTypeDef",
    "ListRumMetricsDestinationsRequestTypeDef",
    "ListRumMetricsDestinationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDefinitionRequestOutputTypeDef",
    "MetricDefinitionRequestTypeDef",
    "MetricDefinitionRequestUnionTypeDef",
    "MetricDefinitionTypeDef",
    "MetricDestinationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutRumEventsRequestTypeDef",
    "PutRumMetricsDestinationRequestTypeDef",
    "QueryFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RumEventTypeDef",
    "TagResourceRequestTypeDef",
    "TimeRangeTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppMonitorRequestTypeDef",
    "UpdateRumMetricDefinitionRequestTypeDef",
    "UserDetailsTypeDef",
)

class AppMonitorConfigurationOutputTypeDef(TypedDict):
    AllowCookies: NotRequired[bool]
    EnableXRay: NotRequired[bool]
    ExcludedPages: NotRequired[List[str]]
    FavoritePages: NotRequired[List[str]]
    GuestRoleArn: NotRequired[str]
    IdentityPoolId: NotRequired[str]
    IncludedPages: NotRequired[List[str]]
    SessionSampleRate: NotRequired[float]
    Telemetries: NotRequired[List[TelemetryType]]

class AppMonitorConfigurationTypeDef(TypedDict):
    AllowCookies: NotRequired[bool]
    EnableXRay: NotRequired[bool]
    ExcludedPages: NotRequired[Sequence[str]]
    FavoritePages: NotRequired[Sequence[str]]
    GuestRoleArn: NotRequired[str]
    IdentityPoolId: NotRequired[str]
    IncludedPages: NotRequired[Sequence[str]]
    SessionSampleRate: NotRequired[float]
    Telemetries: NotRequired[Sequence[TelemetryType]]

AppMonitorDetailsTypeDef = TypedDict(
    "AppMonitorDetailsTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
    },
)

class AppMonitorSummaryTypeDef(TypedDict):
    Created: NotRequired[str]
    Id: NotRequired[str]
    LastModified: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[StateEnumType]

class CustomEventsTypeDef(TypedDict):
    Status: NotRequired[CustomEventsStatusType]

class MetricDefinitionRequestOutputTypeDef(TypedDict):
    Name: str
    DimensionKeys: NotRequired[Dict[str, str]]
    EventPattern: NotRequired[str]
    Namespace: NotRequired[str]
    UnitLabel: NotRequired[str]
    ValueKey: NotRequired[str]

class MetricDefinitionTypeDef(TypedDict):
    MetricDefinitionId: str
    Name: str
    DimensionKeys: NotRequired[Dict[str, str]]
    EventPattern: NotRequired[str]
    Namespace: NotRequired[str]
    UnitLabel: NotRequired[str]
    ValueKey: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDeleteRumMetricDefinitionsErrorTypeDef(TypedDict):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinitionId: str

class BatchDeleteRumMetricDefinitionsRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitionIds: Sequence[str]
    DestinationArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class BatchGetRumMetricDefinitionsRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class CwLogTypeDef(TypedDict):
    CwLogEnabled: NotRequired[bool]
    CwLogGroup: NotRequired[str]

class DeleteAppMonitorRequestTypeDef(TypedDict):
    Name: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    Name: str
    PolicyRevisionId: NotRequired[str]

class DeleteRumMetricsDestinationRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: NotRequired[str]

class JavaScriptSourceMapsTypeDef(TypedDict):
    Status: DeobfuscationStatusType
    S3Uri: NotRequired[str]

class QueryFilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class TimeRangeTypeDef(TypedDict):
    After: int
    Before: NotRequired[int]

class GetAppMonitorRequestTypeDef(TypedDict):
    Name: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    Name: str

class ListAppMonitorsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRumMetricsDestinationsRequestTypeDef(TypedDict):
    AppMonitorName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class MetricDestinationSummaryTypeDef(TypedDict):
    Destination: NotRequired[MetricDestinationType]
    DestinationArn: NotRequired[str]
    IamRoleArn: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class MetricDefinitionRequestTypeDef(TypedDict):
    Name: str
    DimensionKeys: NotRequired[Mapping[str, str]]
    EventPattern: NotRequired[str]
    Namespace: NotRequired[str]
    UnitLabel: NotRequired[str]
    ValueKey: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    Name: str
    PolicyDocument: str
    PolicyRevisionId: NotRequired[str]

class UserDetailsTypeDef(TypedDict):
    sessionId: NotRequired[str]
    userId: NotRequired[str]

class PutRumMetricsDestinationRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: NotRequired[str]
    IamRoleArn: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

AppMonitorConfigurationUnionTypeDef = Union[
    AppMonitorConfigurationTypeDef, AppMonitorConfigurationOutputTypeDef
]

class BatchCreateRumMetricDefinitionsErrorTypeDef(TypedDict):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinition: MetricDefinitionRequestOutputTypeDef

class BatchGetRumMetricDefinitionsResponseTypeDef(TypedDict):
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateAppMonitorResponseTypeDef(TypedDict):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(TypedDict):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppMonitorDataResponseTypeDef(TypedDict):
    Events: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetResourcePolicyResponseTypeDef(TypedDict):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppMonitorsResponseTypeDef(TypedDict):
    AppMonitorSummaries: List[AppMonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteRumMetricDefinitionsResponseTypeDef(TypedDict):
    Errors: List[BatchDeleteRumMetricDefinitionsErrorTypeDef]
    MetricDefinitionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRumMetricDefinitionsRequestPaginateTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAppMonitorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRumMetricsDestinationsRequestPaginateTypeDef(TypedDict):
    AppMonitorName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DataStorageTypeDef(TypedDict):
    CwLog: NotRequired[CwLogTypeDef]

class DeobfuscationConfigurationTypeDef(TypedDict):
    JavaScriptSourceMaps: NotRequired[JavaScriptSourceMapsTypeDef]

class GetAppMonitorDataRequestPaginateTypeDef(TypedDict):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: NotRequired[Sequence[QueryFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAppMonitorDataRequestTypeDef(TypedDict):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: NotRequired[Sequence[QueryFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRumMetricsDestinationsResponseTypeDef(TypedDict):
    Destinations: List[MetricDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MetricDefinitionRequestUnionTypeDef = Union[
    MetricDefinitionRequestTypeDef, MetricDefinitionRequestOutputTypeDef
]
RumEventTypeDef = TypedDict(
    "RumEventTypeDef",
    {
        "details": str,
        "id": str,
        "timestamp": TimestampTypeDef,
        "type": str,
        "metadata": NotRequired[str],
    },
)

class BatchCreateRumMetricDefinitionsResponseTypeDef(TypedDict):
    Errors: List[BatchCreateRumMetricDefinitionsErrorTypeDef]
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AppMonitorTypeDef(TypedDict):
    AppMonitorConfiguration: NotRequired[AppMonitorConfigurationOutputTypeDef]
    Created: NotRequired[str]
    CustomEvents: NotRequired[CustomEventsTypeDef]
    DataStorage: NotRequired[DataStorageTypeDef]
    DeobfuscationConfiguration: NotRequired[DeobfuscationConfigurationTypeDef]
    Domain: NotRequired[str]
    DomainList: NotRequired[List[str]]
    Id: NotRequired[str]
    LastModified: NotRequired[str]
    Name: NotRequired[str]
    State: NotRequired[StateEnumType]
    Tags: NotRequired[Dict[str, str]]

class CreateAppMonitorRequestTypeDef(TypedDict):
    Name: str
    AppMonitorConfiguration: NotRequired[AppMonitorConfigurationUnionTypeDef]
    CustomEvents: NotRequired[CustomEventsTypeDef]
    CwLogEnabled: NotRequired[bool]
    DeobfuscationConfiguration: NotRequired[DeobfuscationConfigurationTypeDef]
    Domain: NotRequired[str]
    DomainList: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class UpdateAppMonitorRequestTypeDef(TypedDict):
    Name: str
    AppMonitorConfiguration: NotRequired[AppMonitorConfigurationUnionTypeDef]
    CustomEvents: NotRequired[CustomEventsTypeDef]
    CwLogEnabled: NotRequired[bool]
    DeobfuscationConfiguration: NotRequired[DeobfuscationConfigurationTypeDef]
    Domain: NotRequired[str]
    DomainList: NotRequired[Sequence[str]]

class BatchCreateRumMetricDefinitionsRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitions: Sequence[MetricDefinitionRequestUnionTypeDef]
    DestinationArn: NotRequired[str]

class UpdateRumMetricDefinitionRequestTypeDef(TypedDict):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinition: MetricDefinitionRequestUnionTypeDef
    MetricDefinitionId: str
    DestinationArn: NotRequired[str]

class PutRumEventsRequestTypeDef(TypedDict):
    AppMonitorDetails: AppMonitorDetailsTypeDef
    BatchId: str
    Id: str
    RumEvents: Sequence[RumEventTypeDef]
    UserDetails: UserDetailsTypeDef
    Alias: NotRequired[str]

class GetAppMonitorResponseTypeDef(TypedDict):
    AppMonitor: AppMonitorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
