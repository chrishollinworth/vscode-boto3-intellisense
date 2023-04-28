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
    LogDeliveryStatusType,
    MonitorConfigStateType,
    MonitorProcessingStatusCodeType,
    TriangulationEventTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AvailabilityMeasurementTypeDef",
    "CreateMonitorInputRequestTypeDef",
    "CreateMonitorOutputTypeDef",
    "DeleteMonitorInputRequestTypeDef",
    "GetHealthEventInputRequestTypeDef",
    "GetHealthEventOutputTypeDef",
    "GetMonitorInputRequestTypeDef",
    "GetMonitorOutputTypeDef",
    "HealthEventTypeDef",
    "ImpactedLocationTypeDef",
    "InternetHealthTypeDef",
    "InternetMeasurementsLogDeliveryTypeDef",
    "ListHealthEventsInputRequestTypeDef",
    "ListHealthEventsOutputTypeDef",
    "ListMonitorsInputRequestTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MonitorTypeDef",
    "NetworkImpairmentTypeDef",
    "NetworkTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMeasurementTypeDef",
    "ResponseMetadataTypeDef",
    "RoundTripTimeTypeDef",
    "S3ConfigTypeDef",
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

GetHealthEventInputRequestTypeDef = TypedDict(
    "GetHealthEventInputRequestTypeDef",
    {
        "MonitorName": str,
        "EventId": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMonitorInputRequestTypeDef = TypedDict(
    "GetMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)

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
    },
    total=False,
)

class HealthEventTypeDef(_RequiredHealthEventTypeDef, _OptionalHealthEventTypeDef):
    pass

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
    },
    total=False,
)

class ImpactedLocationTypeDef(_RequiredImpactedLocationTypeDef, _OptionalImpactedLocationTypeDef):
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

ListMonitorsInputRequestTypeDef = TypedDict(
    "ListMonitorsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "MonitorStatus": str,
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
