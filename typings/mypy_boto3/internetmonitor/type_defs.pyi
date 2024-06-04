"""
Type annotations for internetmonitor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_internetmonitor.type_defs import AvailabilityMeasurementTypeDef

    data: AvailabilityMeasurementTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AvailabilityMeasurementTypeDef",
    "ClientLocationTypeDef",
    "CreateMonitorInputRequestTypeDef",
    "CreateMonitorOutputTypeDef",
    "DeleteMonitorInputRequestTypeDef",
    "FilterParameterTypeDef",
    "GetHealthEventInputRequestTypeDef",
    "GetHealthEventOutputTypeDef",
    "GetInternetEventInputRequestTypeDef",
    "GetInternetEventOutputTypeDef",
    "GetMonitorInputRequestTypeDef",
    "GetMonitorOutputTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetQueryStatusInputRequestTypeDef",
    "GetQueryStatusOutputTypeDef",
    "HealthEventTypeDef",
    "HealthEventsConfigTypeDef",
    "ImpactedLocationTypeDef",
    "InternetEventSummaryTypeDef",
    "InternetHealthTypeDef",
    "InternetMeasurementsLogDeliveryTypeDef",
    "ListHealthEventsInputRequestTypeDef",
    "ListHealthEventsOutputTypeDef",
    "ListInternetEventsInputRequestTypeDef",
    "ListInternetEventsOutputTypeDef",
    "ListMonitorsInputRequestTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
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
    "StartQueryInputRequestTypeDef",
    "StartQueryOutputTypeDef",
    "StopQueryInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateMonitorInputRequestTypeDef",
    "UpdateMonitorOutputTypeDef",
)

AvailabilityMeasurementTypeDef = TypedDict(
    "AvailabilityMeasurementTypeDef",
    {
        "ExperienceScore": float,
        "PercentOfTotalTrafficImpacted": float,
        "PercentOfClientLocationImpacted": float,
    },
    total=False,
)

_RequiredClientLocationTypeDef = TypedDict(
    "_RequiredClientLocationTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
        "Country": str,
        "City": str,
        "Latitude": float,
        "Longitude": float,
    },
)
_OptionalClientLocationTypeDef = TypedDict(
    "_OptionalClientLocationTypeDef",
    {
        "Subdivision": str,
        "Metro": str,
    },
    total=False,
)

class ClientLocationTypeDef(_RequiredClientLocationTypeDef, _OptionalClientLocationTypeDef):
    pass

_RequiredCreateMonitorInputRequestTypeDef = TypedDict(
    "_RequiredCreateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
_OptionalCreateMonitorInputRequestTypeDef = TypedDict(
    "_OptionalCreateMonitorInputRequestTypeDef",
    {
        "Resources": List[str],
        "ClientToken": str,
        "Tags": Dict[str, str],
        "MaxCityNetworksToMonitor": int,
        "InternetMeasurementsLogDelivery": "InternetMeasurementsLogDeliveryTypeDef",
        "TrafficPercentageToMonitor": int,
        "HealthEventsConfig": "HealthEventsConfigTypeDef",
    },
    total=False,
)

class CreateMonitorInputRequestTypeDef(
    _RequiredCreateMonitorInputRequestTypeDef, _OptionalCreateMonitorInputRequestTypeDef
):
    pass

CreateMonitorOutputTypeDef = TypedDict(
    "CreateMonitorOutputTypeDef",
    {
        "Arn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMonitorInputRequestTypeDef = TypedDict(
    "DeleteMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)

FilterParameterTypeDef = TypedDict(
    "FilterParameterTypeDef",
    {
        "Field": str,
        "Operator": OperatorType,
        "Values": List[str],
    },
    total=False,
)

_RequiredGetHealthEventInputRequestTypeDef = TypedDict(
    "_RequiredGetHealthEventInputRequestTypeDef",
    {
        "MonitorName": str,
        "EventId": str,
    },
)
_OptionalGetHealthEventInputRequestTypeDef = TypedDict(
    "_OptionalGetHealthEventInputRequestTypeDef",
    {
        "LinkedAccountId": str,
    },
    total=False,
)

class GetHealthEventInputRequestTypeDef(
    _RequiredGetHealthEventInputRequestTypeDef, _OptionalGetHealthEventInputRequestTypeDef
):
    pass

GetHealthEventOutputTypeDef = TypedDict(
    "GetHealthEventOutputTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List["ImpactedLocationTypeDef"],
        "Status": HealthEventStatusType,
        "PercentOfTotalTrafficImpacted": float,
        "ImpactType": HealthEventImpactTypeType,
        "HealthScoreThreshold": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInternetEventInputRequestTypeDef = TypedDict(
    "GetInternetEventInputRequestTypeDef",
    {
        "EventId": str,
    },
)

GetInternetEventOutputTypeDef = TypedDict(
    "GetInternetEventOutputTypeDef",
    {
        "EventId": str,
        "EventArn": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "ClientLocation": "ClientLocationTypeDef",
        "EventType": InternetEventTypeType,
        "EventStatus": InternetEventStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMonitorInputRequestTypeDef = TypedDict(
    "_RequiredGetMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
_OptionalGetMonitorInputRequestTypeDef = TypedDict(
    "_OptionalGetMonitorInputRequestTypeDef",
    {
        "LinkedAccountId": str,
    },
    total=False,
)

class GetMonitorInputRequestTypeDef(
    _RequiredGetMonitorInputRequestTypeDef, _OptionalGetMonitorInputRequestTypeDef
):
    pass

GetMonitorOutputTypeDef = TypedDict(
    "GetMonitorOutputTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Resources": List[str],
        "Status": MonitorConfigStateType,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "ProcessingStatus": MonitorProcessingStatusCodeType,
        "ProcessingStatusInfo": str,
        "Tags": Dict[str, str],
        "MaxCityNetworksToMonitor": int,
        "InternetMeasurementsLogDelivery": "InternetMeasurementsLogDeliveryTypeDef",
        "TrafficPercentageToMonitor": int,
        "HealthEventsConfig": "HealthEventsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsInputRequestTypeDef = TypedDict(
    "_RequiredGetQueryResultsInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)
_OptionalGetQueryResultsInputRequestTypeDef = TypedDict(
    "_OptionalGetQueryResultsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetQueryResultsInputRequestTypeDef(
    _RequiredGetQueryResultsInputRequestTypeDef, _OptionalGetQueryResultsInputRequestTypeDef
):
    pass

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "Fields": List["QueryFieldTypeDef"],
        "Data": List[List[str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryStatusInputRequestTypeDef = TypedDict(
    "GetQueryStatusInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)

GetQueryStatusOutputTypeDef = TypedDict(
    "GetQueryStatusOutputTypeDef",
    {
        "Status": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHealthEventTypeDef = TypedDict(
    "_RequiredHealthEventTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List["ImpactedLocationTypeDef"],
        "Status": HealthEventStatusType,
        "ImpactType": HealthEventImpactTypeType,
    },
)
_OptionalHealthEventTypeDef = TypedDict(
    "_OptionalHealthEventTypeDef",
    {
        "EndedAt": datetime,
        "CreatedAt": datetime,
        "PercentOfTotalTrafficImpacted": float,
        "HealthScoreThreshold": float,
    },
    total=False,
)

class HealthEventTypeDef(_RequiredHealthEventTypeDef, _OptionalHealthEventTypeDef):
    pass

HealthEventsConfigTypeDef = TypedDict(
    "HealthEventsConfigTypeDef",
    {
        "AvailabilityScoreThreshold": float,
        "PerformanceScoreThreshold": float,
        "AvailabilityLocalHealthEventsConfig": "LocalHealthEventsConfigTypeDef",
        "PerformanceLocalHealthEventsConfig": "LocalHealthEventsConfigTypeDef",
    },
    total=False,
)

_RequiredImpactedLocationTypeDef = TypedDict(
    "_RequiredImpactedLocationTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
        "Country": str,
        "Status": HealthEventStatusType,
    },
)
_OptionalImpactedLocationTypeDef = TypedDict(
    "_OptionalImpactedLocationTypeDef",
    {
        "Subdivision": str,
        "Metro": str,
        "City": str,
        "Latitude": float,
        "Longitude": float,
        "CountryCode": str,
        "SubdivisionCode": str,
        "ServiceLocation": str,
        "CausedBy": "NetworkImpairmentTypeDef",
        "InternetHealth": "InternetHealthTypeDef",
        "Ipv4Prefixes": List[str],
    },
    total=False,
)

class ImpactedLocationTypeDef(_RequiredImpactedLocationTypeDef, _OptionalImpactedLocationTypeDef):
    pass

_RequiredInternetEventSummaryTypeDef = TypedDict(
    "_RequiredInternetEventSummaryTypeDef",
    {
        "EventId": str,
        "EventArn": str,
        "StartedAt": datetime,
        "ClientLocation": "ClientLocationTypeDef",
        "EventType": InternetEventTypeType,
        "EventStatus": InternetEventStatusType,
    },
)
_OptionalInternetEventSummaryTypeDef = TypedDict(
    "_OptionalInternetEventSummaryTypeDef",
    {
        "EndedAt": datetime,
    },
    total=False,
)

class InternetEventSummaryTypeDef(
    _RequiredInternetEventSummaryTypeDef, _OptionalInternetEventSummaryTypeDef
):
    pass

InternetHealthTypeDef = TypedDict(
    "InternetHealthTypeDef",
    {
        "Availability": "AvailabilityMeasurementTypeDef",
        "Performance": "PerformanceMeasurementTypeDef",
    },
    total=False,
)

InternetMeasurementsLogDeliveryTypeDef = TypedDict(
    "InternetMeasurementsLogDeliveryTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
    },
    total=False,
)

_RequiredListHealthEventsInputRequestTypeDef = TypedDict(
    "_RequiredListHealthEventsInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
_OptionalListHealthEventsInputRequestTypeDef = TypedDict(
    "_OptionalListHealthEventsInputRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
        "EventStatus": HealthEventStatusType,
        "LinkedAccountId": str,
    },
    total=False,
)

class ListHealthEventsInputRequestTypeDef(
    _RequiredListHealthEventsInputRequestTypeDef, _OptionalListHealthEventsInputRequestTypeDef
):
    pass

ListHealthEventsOutputTypeDef = TypedDict(
    "ListHealthEventsOutputTypeDef",
    {
        "HealthEvents": List["HealthEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInternetEventsInputRequestTypeDef = TypedDict(
    "ListInternetEventsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventStatus": str,
        "EventType": str,
    },
    total=False,
)

ListInternetEventsOutputTypeDef = TypedDict(
    "ListInternetEventsOutputTypeDef",
    {
        "InternetEvents": List["InternetEventSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitorsInputRequestTypeDef = TypedDict(
    "ListMonitorsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "MonitorStatus": str,
        "IncludeLinkedAccounts": bool,
    },
    total=False,
)

ListMonitorsOutputTypeDef = TypedDict(
    "ListMonitorsOutputTypeDef",
    {
        "Monitors": List["MonitorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalHealthEventsConfigTypeDef = TypedDict(
    "LocalHealthEventsConfigTypeDef",
    {
        "Status": LocalHealthEventsConfigStatusType,
        "HealthScoreThreshold": float,
        "MinTrafficImpact": float,
    },
    total=False,
)

_RequiredMonitorTypeDef = TypedDict(
    "_RequiredMonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
    },
)
_OptionalMonitorTypeDef = TypedDict(
    "_OptionalMonitorTypeDef",
    {
        "ProcessingStatus": MonitorProcessingStatusCodeType,
    },
    total=False,
)

class MonitorTypeDef(_RequiredMonitorTypeDef, _OptionalMonitorTypeDef):
    pass

NetworkImpairmentTypeDef = TypedDict(
    "NetworkImpairmentTypeDef",
    {
        "Networks": List["NetworkTypeDef"],
        "AsPath": List["NetworkTypeDef"],
        "NetworkEventType": TriangulationEventTypeType,
    },
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PerformanceMeasurementTypeDef = TypedDict(
    "PerformanceMeasurementTypeDef",
    {
        "ExperienceScore": float,
        "PercentOfTotalTrafficImpacted": float,
        "PercentOfClientLocationImpacted": float,
        "RoundTripTime": "RoundTripTimeTypeDef",
    },
    total=False,
)

QueryFieldTypeDef = TypedDict(
    "QueryFieldTypeDef",
    {
        "Name": str,
        "Type": str,
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

RoundTripTimeTypeDef = TypedDict(
    "RoundTripTimeTypeDef",
    {
        "P50": float,
        "P90": float,
        "P95": float,
    },
    total=False,
)

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
        "LogDeliveryStatus": LogDeliveryStatusType,
    },
    total=False,
)

_RequiredStartQueryInputRequestTypeDef = TypedDict(
    "_RequiredStartQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "QueryType": QueryTypeType,
    },
)
_OptionalStartQueryInputRequestTypeDef = TypedDict(
    "_OptionalStartQueryInputRequestTypeDef",
    {
        "FilterParameters": List["FilterParameterTypeDef"],
        "LinkedAccountId": str,
    },
    total=False,
)

class StartQueryInputRequestTypeDef(
    _RequiredStartQueryInputRequestTypeDef, _OptionalStartQueryInputRequestTypeDef
):
    pass

StartQueryOutputTypeDef = TypedDict(
    "StartQueryOutputTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryInputRequestTypeDef = TypedDict(
    "StopQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateMonitorInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
_OptionalUpdateMonitorInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMonitorInputRequestTypeDef",
    {
        "ResourcesToAdd": List[str],
        "ResourcesToRemove": List[str],
        "Status": MonitorConfigStateType,
        "ClientToken": str,
        "MaxCityNetworksToMonitor": int,
        "InternetMeasurementsLogDelivery": "InternetMeasurementsLogDeliveryTypeDef",
        "TrafficPercentageToMonitor": int,
        "HealthEventsConfig": "HealthEventsConfigTypeDef",
    },
    total=False,
)

class UpdateMonitorInputRequestTypeDef(
    _RequiredUpdateMonitorInputRequestTypeDef, _OptionalUpdateMonitorInputRequestTypeDef
):
    pass

UpdateMonitorOutputTypeDef = TypedDict(
    "UpdateMonitorOutputTypeDef",
    {
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
