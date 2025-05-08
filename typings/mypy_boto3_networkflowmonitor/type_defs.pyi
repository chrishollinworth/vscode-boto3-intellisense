"""
Type annotations for networkflowmonitor service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkflowmonitor/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_networkflowmonitor.type_defs import MonitorLocalResourceTypeDef

    data: MonitorLocalResourceTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DestinationCategoryType,
    MetricUnitType,
    MonitorLocalResourceTypeType,
    MonitorMetricType,
    MonitorRemoteResourceTypeType,
    MonitorStatusType,
    QueryStatusType,
    ScopeStatusType,
    WorkloadInsightsMetricType,
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
    "CreateMonitorInputTypeDef",
    "CreateMonitorOutputTypeDef",
    "CreateScopeInputTypeDef",
    "CreateScopeOutputTypeDef",
    "DeleteMonitorInputTypeDef",
    "DeleteScopeInputTypeDef",
    "GetMonitorInputTypeDef",
    "GetMonitorOutputTypeDef",
    "GetQueryResultsMonitorTopContributorsInputPaginateTypeDef",
    "GetQueryResultsMonitorTopContributorsInputTypeDef",
    "GetQueryResultsMonitorTopContributorsOutputTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef",
    "GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef",
    "GetQueryStatusMonitorTopContributorsInputTypeDef",
    "GetQueryStatusMonitorTopContributorsOutputTypeDef",
    "GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef",
    "GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef",
    "GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef",
    "GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef",
    "GetScopeInputTypeDef",
    "GetScopeOutputTypeDef",
    "KubernetesMetadataTypeDef",
    "ListMonitorsInputPaginateTypeDef",
    "ListMonitorsInputTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListScopesInputPaginateTypeDef",
    "ListScopesInputTypeDef",
    "ListScopesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MonitorLocalResourceTypeDef",
    "MonitorRemoteResourceTypeDef",
    "MonitorSummaryTypeDef",
    "MonitorTopContributorsRowTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ScopeSummaryTypeDef",
    "StartQueryMonitorTopContributorsInputTypeDef",
    "StartQueryMonitorTopContributorsOutputTypeDef",
    "StartQueryWorkloadInsightsTopContributorsDataInputTypeDef",
    "StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef",
    "StartQueryWorkloadInsightsTopContributorsInputTypeDef",
    "StartQueryWorkloadInsightsTopContributorsOutputTypeDef",
    "StopQueryMonitorTopContributorsInputTypeDef",
    "StopQueryWorkloadInsightsTopContributorsDataInputTypeDef",
    "StopQueryWorkloadInsightsTopContributorsInputTypeDef",
    "TagResourceInputTypeDef",
    "TargetIdTypeDef",
    "TargetIdentifierTypeDef",
    "TargetResourceTypeDef",
    "TimestampTypeDef",
    "TraversedComponentTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateMonitorInputTypeDef",
    "UpdateMonitorOutputTypeDef",
    "UpdateScopeInputTypeDef",
    "UpdateScopeOutputTypeDef",
    "WorkloadInsightsTopContributorsDataPointTypeDef",
    "WorkloadInsightsTopContributorsRowTypeDef",
)

MonitorLocalResourceTypeDef = TypedDict(
    "MonitorLocalResourceTypeDef",
    {
        "type": MonitorLocalResourceTypeType,
        "identifier": str,
    },
)
MonitorRemoteResourceTypeDef = TypedDict(
    "MonitorRemoteResourceTypeDef",
    {
        "type": MonitorRemoteResourceTypeType,
        "identifier": str,
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteMonitorInputTypeDef(TypedDict):
    monitorName: str

class DeleteScopeInputTypeDef(TypedDict):
    scopeId: str

class GetMonitorInputTypeDef(TypedDict):
    monitorName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetQueryResultsMonitorTopContributorsInputTypeDef(TypedDict):
    monitorName: str
    queryId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef(TypedDict):
    scopeId: str
    queryId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class WorkloadInsightsTopContributorsDataPointTypeDef(TypedDict):
    timestamps: List[datetime]
    values: List[float]
    label: str

class GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef(TypedDict):
    scopeId: str
    queryId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class WorkloadInsightsTopContributorsRowTypeDef(TypedDict):
    accountId: NotRequired[str]
    localSubnetId: NotRequired[str]
    localAz: NotRequired[str]
    localVpcId: NotRequired[str]
    localRegion: NotRequired[str]
    remoteIdentifier: NotRequired[str]
    value: NotRequired[int]
    localSubnetArn: NotRequired[str]
    localVpcArn: NotRequired[str]

class GetQueryStatusMonitorTopContributorsInputTypeDef(TypedDict):
    monitorName: str
    queryId: str

class GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef(TypedDict):
    scopeId: str
    queryId: str

class GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef(TypedDict):
    scopeId: str
    queryId: str

class GetScopeInputTypeDef(TypedDict):
    scopeId: str

class KubernetesMetadataTypeDef(TypedDict):
    localServiceName: NotRequired[str]
    localPodName: NotRequired[str]
    localPodNamespace: NotRequired[str]
    remoteServiceName: NotRequired[str]
    remotePodName: NotRequired[str]
    remotePodNamespace: NotRequired[str]

class ListMonitorsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    monitorStatus: NotRequired[MonitorStatusType]

class MonitorSummaryTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType

class ListScopesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ScopeSummaryTypeDef(TypedDict):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class TraversedComponentTypeDef(TypedDict):
    componentId: NotRequired[str]
    componentType: NotRequired[str]
    componentArn: NotRequired[str]
    serviceName: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class StopQueryMonitorTopContributorsInputTypeDef(TypedDict):
    monitorName: str
    queryId: str

class StopQueryWorkloadInsightsTopContributorsDataInputTypeDef(TypedDict):
    scopeId: str
    queryId: str

class StopQueryWorkloadInsightsTopContributorsInputTypeDef(TypedDict):
    scopeId: str
    queryId: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TargetIdTypeDef(TypedDict):
    accountId: NotRequired[str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateMonitorInputTypeDef(TypedDict):
    monitorName: str
    localResources: Sequence[MonitorLocalResourceTypeDef]
    scopeArn: str
    remoteResources: NotRequired[Sequence[MonitorRemoteResourceTypeDef]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateMonitorInputTypeDef(TypedDict):
    monitorName: str
    localResourcesToAdd: NotRequired[Sequence[MonitorLocalResourceTypeDef]]
    localResourcesToRemove: NotRequired[Sequence[MonitorLocalResourceTypeDef]]
    remoteResourcesToAdd: NotRequired[Sequence[MonitorRemoteResourceTypeDef]]
    remoteResourcesToRemove: NotRequired[Sequence[MonitorRemoteResourceTypeDef]]
    clientToken: NotRequired[str]

class CreateMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScopeOutputTypeDef(TypedDict):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryStatusMonitorTopContributorsOutputTypeDef(TypedDict):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef(TypedDict):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef(TypedDict):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryMonitorTopContributorsOutputTypeDef(TypedDict):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef(TypedDict):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryWorkloadInsightsTopContributorsOutputTypeDef(TypedDict):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScopeOutputTypeDef(TypedDict):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsMonitorTopContributorsInputPaginateTypeDef(TypedDict):
    monitorName: str
    queryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef(TypedDict):
    scopeId: str
    queryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef(TypedDict):
    scopeId: str
    queryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorsInputPaginateTypeDef(TypedDict):
    monitorStatus: NotRequired[MonitorStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListScopesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef(TypedDict):
    unit: MetricUnitType
    datapoints: List[WorkloadInsightsTopContributorsDataPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef(TypedDict):
    topContributors: List[WorkloadInsightsTopContributorsRowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMonitorsOutputTypeDef(TypedDict):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListScopesOutputTypeDef(TypedDict):
    scopes: List[ScopeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MonitorTopContributorsRowTypeDef(TypedDict):
    localIp: NotRequired[str]
    snatIp: NotRequired[str]
    localInstanceId: NotRequired[str]
    localVpcId: NotRequired[str]
    localRegion: NotRequired[str]
    localAz: NotRequired[str]
    localSubnetId: NotRequired[str]
    targetPort: NotRequired[int]
    destinationCategory: NotRequired[DestinationCategoryType]
    remoteVpcId: NotRequired[str]
    remoteRegion: NotRequired[str]
    remoteAz: NotRequired[str]
    remoteSubnetId: NotRequired[str]
    remoteInstanceId: NotRequired[str]
    remoteIp: NotRequired[str]
    dnatIp: NotRequired[str]
    value: NotRequired[int]
    traversedConstructs: NotRequired[List[TraversedComponentTypeDef]]
    kubernetesMetadata: NotRequired[KubernetesMetadataTypeDef]
    localInstanceArn: NotRequired[str]
    localSubnetArn: NotRequired[str]
    localVpcArn: NotRequired[str]
    remoteInstanceArn: NotRequired[str]
    remoteSubnetArn: NotRequired[str]
    remoteVpcArn: NotRequired[str]

class StartQueryMonitorTopContributorsInputTypeDef(TypedDict):
    monitorName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: MonitorMetricType
    destinationCategory: DestinationCategoryType
    limit: NotRequired[int]

class StartQueryWorkloadInsightsTopContributorsDataInputTypeDef(TypedDict):
    scopeId: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType

class StartQueryWorkloadInsightsTopContributorsInputTypeDef(TypedDict):
    scopeId: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType
    limit: NotRequired[int]

class TargetIdentifierTypeDef(TypedDict):
    targetId: TargetIdTypeDef
    targetType: Literal["ACCOUNT"]

class GetQueryResultsMonitorTopContributorsOutputTypeDef(TypedDict):
    unit: MetricUnitType
    topContributors: List[MonitorTopContributorsRowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TargetResourceTypeDef(TypedDict):
    targetIdentifier: TargetIdentifierTypeDef
    region: str

class CreateScopeInputTypeDef(TypedDict):
    targets: Sequence[TargetResourceTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class GetScopeOutputTypeDef(TypedDict):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    targets: List[TargetResourceTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScopeInputTypeDef(TypedDict):
    scopeId: str
    resourcesToAdd: NotRequired[Sequence[TargetResourceTypeDef]]
    resourcesToDelete: NotRequired[Sequence[TargetResourceTypeDef]]
