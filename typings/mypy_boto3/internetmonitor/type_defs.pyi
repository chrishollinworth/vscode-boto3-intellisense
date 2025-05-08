"""
Type annotations for internetmonitor service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_internetmonitor.type_defs import AvailabilityMeasurementTypeDef

    data: AvailabilityMeasurementTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    HealthEventImpactTypeType,
    HealthEventStatusType,
    InternetEventStatusType,
    InternetEventTypeType,
    LocalHealthEventsConfigStatusType,
    LogDeliveryStatusType,
    MonitorConfigStateType,
    MonitorProcessingStatusCodeType,
    OperatorType,
    QueryStatusType,
    QueryTypeType,
    TriangulationEventTypeType,
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
    "AvailabilityMeasurementTypeDef",
    "ClientLocationTypeDef",
    "CreateMonitorInputTypeDef",
    "CreateMonitorOutputTypeDef",
    "DeleteMonitorInputTypeDef",
    "FilterParameterTypeDef",
    "GetHealthEventInputTypeDef",
    "GetHealthEventOutputTypeDef",
    "GetInternetEventInputTypeDef",
    "GetInternetEventOutputTypeDef",
    "GetMonitorInputTypeDef",
    "GetMonitorOutputTypeDef",
    "GetQueryResultsInputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetQueryStatusInputTypeDef",
    "GetQueryStatusOutputTypeDef",
    "HealthEventTypeDef",
    "HealthEventsConfigTypeDef",
    "ImpactedLocationTypeDef",
    "InternetEventSummaryTypeDef",
    "InternetHealthTypeDef",
    "InternetMeasurementsLogDeliveryTypeDef",
    "ListHealthEventsInputPaginateTypeDef",
    "ListHealthEventsInputTypeDef",
    "ListHealthEventsOutputTypeDef",
    "ListInternetEventsInputPaginateTypeDef",
    "ListInternetEventsInputTypeDef",
    "ListInternetEventsOutputTypeDef",
    "ListMonitorsInputPaginateTypeDef",
    "ListMonitorsInputTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LocalHealthEventsConfigTypeDef",
    "MonitorTypeDef",
    "NetworkImpairmentTypeDef",
    "NetworkTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMeasurementTypeDef",
    "QueryFieldTypeDef",
    "ResponseMetadataTypeDef",
    "RoundTripTimeTypeDef",
    "S3ConfigTypeDef",
    "StartQueryInputTypeDef",
    "StartQueryOutputTypeDef",
    "StopQueryInputTypeDef",
    "TagResourceInputTypeDef",
    "TimestampTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateMonitorInputTypeDef",
    "UpdateMonitorOutputTypeDef",
)

class AvailabilityMeasurementTypeDef(TypedDict):
    ExperienceScore: NotRequired[float]
    PercentOfTotalTrafficImpacted: NotRequired[float]
    PercentOfClientLocationImpacted: NotRequired[float]

class ClientLocationTypeDef(TypedDict):
    ASName: str
    ASNumber: int
    Country: str
    City: str
    Latitude: float
    Longitude: float
    Subdivision: NotRequired[str]
    Metro: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteMonitorInputTypeDef(TypedDict):
    MonitorName: str

class FilterParameterTypeDef(TypedDict):
    Field: NotRequired[str]
    Operator: NotRequired[OperatorType]
    Values: NotRequired[Sequence[str]]

class GetHealthEventInputTypeDef(TypedDict):
    MonitorName: str
    EventId: str
    LinkedAccountId: NotRequired[str]

class GetInternetEventInputTypeDef(TypedDict):
    EventId: str

class GetMonitorInputTypeDef(TypedDict):
    MonitorName: str
    LinkedAccountId: NotRequired[str]

class GetQueryResultsInputTypeDef(TypedDict):
    MonitorName: str
    QueryId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

QueryFieldTypeDef = TypedDict(
    "QueryFieldTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class GetQueryStatusInputTypeDef(TypedDict):
    MonitorName: str
    QueryId: str

class LocalHealthEventsConfigTypeDef(TypedDict):
    Status: NotRequired[LocalHealthEventsConfigStatusType]
    HealthScoreThreshold: NotRequired[float]
    MinTrafficImpact: NotRequired[float]

class S3ConfigTypeDef(TypedDict):
    BucketName: NotRequired[str]
    BucketPrefix: NotRequired[str]
    LogDeliveryStatus: NotRequired[LogDeliveryStatusType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListMonitorsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    MonitorStatus: NotRequired[str]
    IncludeLinkedAccounts: NotRequired[bool]

class MonitorTypeDef(TypedDict):
    MonitorName: str
    MonitorArn: str
    Status: MonitorConfigStateType
    ProcessingStatus: NotRequired[MonitorProcessingStatusCodeType]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str

class NetworkTypeDef(TypedDict):
    ASName: str
    ASNumber: int

class RoundTripTimeTypeDef(TypedDict):
    P50: NotRequired[float]
    P90: NotRequired[float]
    P95: NotRequired[float]

class StopQueryInputTypeDef(TypedDict):
    MonitorName: str
    QueryId: str

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class InternetEventSummaryTypeDef(TypedDict):
    EventId: str
    EventArn: str
    StartedAt: datetime
    ClientLocation: ClientLocationTypeDef
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    EndedAt: NotRequired[datetime]

class CreateMonitorOutputTypeDef(TypedDict):
    Arn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetInternetEventOutputTypeDef(TypedDict):
    EventId: str
    EventArn: str
    StartedAt: datetime
    EndedAt: datetime
    ClientLocation: ClientLocationTypeDef
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryStatusOutputTypeDef(TypedDict):
    Status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryOutputTypeDef(TypedDict):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitorOutputTypeDef(TypedDict):
    MonitorArn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsOutputTypeDef(TypedDict):
    Fields: List[QueryFieldTypeDef]
    Data: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class HealthEventsConfigTypeDef(TypedDict):
    AvailabilityScoreThreshold: NotRequired[float]
    PerformanceScoreThreshold: NotRequired[float]
    AvailabilityLocalHealthEventsConfig: NotRequired[LocalHealthEventsConfigTypeDef]
    PerformanceLocalHealthEventsConfig: NotRequired[LocalHealthEventsConfigTypeDef]

class InternetMeasurementsLogDeliveryTypeDef(TypedDict):
    S3Config: NotRequired[S3ConfigTypeDef]

class ListMonitorsInputPaginateTypeDef(TypedDict):
    MonitorStatus: NotRequired[str]
    IncludeLinkedAccounts: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHealthEventsInputPaginateTypeDef(TypedDict):
    MonitorName: str
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventStatus: NotRequired[HealthEventStatusType]
    LinkedAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHealthEventsInputTypeDef(TypedDict):
    MonitorName: str
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    EventStatus: NotRequired[HealthEventStatusType]
    LinkedAccountId: NotRequired[str]

class ListInternetEventsInputPaginateTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventStatus: NotRequired[str]
    EventType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInternetEventsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    EventStatus: NotRequired[str]
    EventType: NotRequired[str]

class StartQueryInputTypeDef(TypedDict):
    MonitorName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    QueryType: QueryTypeType
    FilterParameters: NotRequired[Sequence[FilterParameterTypeDef]]
    LinkedAccountId: NotRequired[str]

class ListMonitorsOutputTypeDef(TypedDict):
    Monitors: List[MonitorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class NetworkImpairmentTypeDef(TypedDict):
    Networks: List[NetworkTypeDef]
    AsPath: List[NetworkTypeDef]
    NetworkEventType: TriangulationEventTypeType

class PerformanceMeasurementTypeDef(TypedDict):
    ExperienceScore: NotRequired[float]
    PercentOfTotalTrafficImpacted: NotRequired[float]
    PercentOfClientLocationImpacted: NotRequired[float]
    RoundTripTime: NotRequired[RoundTripTimeTypeDef]

class ListInternetEventsOutputTypeDef(TypedDict):
    InternetEvents: List[InternetEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateMonitorInputTypeDef(TypedDict):
    MonitorName: str
    Resources: NotRequired[Sequence[str]]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    MaxCityNetworksToMonitor: NotRequired[int]
    InternetMeasurementsLogDelivery: NotRequired[InternetMeasurementsLogDeliveryTypeDef]
    TrafficPercentageToMonitor: NotRequired[int]
    HealthEventsConfig: NotRequired[HealthEventsConfigTypeDef]

class GetMonitorOutputTypeDef(TypedDict):
    MonitorName: str
    MonitorArn: str
    Resources: List[str]
    Status: MonitorConfigStateType
    CreatedAt: datetime
    ModifiedAt: datetime
    ProcessingStatus: MonitorProcessingStatusCodeType
    ProcessingStatusInfo: str
    Tags: Dict[str, str]
    MaxCityNetworksToMonitor: int
    InternetMeasurementsLogDelivery: InternetMeasurementsLogDeliveryTypeDef
    TrafficPercentageToMonitor: int
    HealthEventsConfig: HealthEventsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitorInputTypeDef(TypedDict):
    MonitorName: str
    ResourcesToAdd: NotRequired[Sequence[str]]
    ResourcesToRemove: NotRequired[Sequence[str]]
    Status: NotRequired[MonitorConfigStateType]
    ClientToken: NotRequired[str]
    MaxCityNetworksToMonitor: NotRequired[int]
    InternetMeasurementsLogDelivery: NotRequired[InternetMeasurementsLogDeliveryTypeDef]
    TrafficPercentageToMonitor: NotRequired[int]
    HealthEventsConfig: NotRequired[HealthEventsConfigTypeDef]

class InternetHealthTypeDef(TypedDict):
    Availability: NotRequired[AvailabilityMeasurementTypeDef]
    Performance: NotRequired[PerformanceMeasurementTypeDef]

class ImpactedLocationTypeDef(TypedDict):
    ASName: str
    ASNumber: int
    Country: str
    Status: HealthEventStatusType
    Subdivision: NotRequired[str]
    Metro: NotRequired[str]
    City: NotRequired[str]
    Latitude: NotRequired[float]
    Longitude: NotRequired[float]
    CountryCode: NotRequired[str]
    SubdivisionCode: NotRequired[str]
    ServiceLocation: NotRequired[str]
    CausedBy: NotRequired[NetworkImpairmentTypeDef]
    InternetHealth: NotRequired[InternetHealthTypeDef]
    Ipv4Prefixes: NotRequired[List[str]]

class GetHealthEventOutputTypeDef(TypedDict):
    EventArn: str
    EventId: str
    StartedAt: datetime
    EndedAt: datetime
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocationTypeDef]
    Status: HealthEventStatusType
    PercentOfTotalTrafficImpacted: float
    ImpactType: HealthEventImpactTypeType
    HealthScoreThreshold: float
    ResponseMetadata: ResponseMetadataTypeDef

class HealthEventTypeDef(TypedDict):
    EventArn: str
    EventId: str
    StartedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocationTypeDef]
    Status: HealthEventStatusType
    ImpactType: HealthEventImpactTypeType
    EndedAt: NotRequired[datetime]
    CreatedAt: NotRequired[datetime]
    PercentOfTotalTrafficImpacted: NotRequired[float]
    HealthScoreThreshold: NotRequired[float]

class ListHealthEventsOutputTypeDef(TypedDict):
    HealthEvents: List[HealthEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
