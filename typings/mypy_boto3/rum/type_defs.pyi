"""
Type annotations for rum service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rum.type_defs import AppMonitorConfigurationTypeDef

    data: AppMonitorConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import StateEnumType, TelemetryType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppMonitorConfigurationTypeDef",
    "AppMonitorDetailsTypeDef",
    "AppMonitorSummaryTypeDef",
    "AppMonitorTypeDef",
    "CreateAppMonitorRequestRequestTypeDef",
    "CreateAppMonitorResponseTypeDef",
    "CwLogTypeDef",
    "DataStorageTypeDef",
    "DeleteAppMonitorRequestRequestTypeDef",
    "GetAppMonitorDataRequestRequestTypeDef",
    "GetAppMonitorDataResponseTypeDef",
    "GetAppMonitorRequestRequestTypeDef",
    "GetAppMonitorResponseTypeDef",
    "ListAppMonitorsRequestRequestTypeDef",
    "ListAppMonitorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutRumEventsRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RumEventTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppMonitorRequestRequestTypeDef",
    "UserDetailsTypeDef",
)

AppMonitorConfigurationTypeDef = TypedDict(
    "AppMonitorConfigurationTypeDef",
    {
        "AllowCookies": bool,
        "EnableXRay": bool,
        "ExcludedPages": List[str],
        "FavoritePages": List[str],
        "GuestRoleArn": str,
        "IdentityPoolId": str,
        "IncludedPages": List[str],
        "SessionSampleRate": float,
        "Telemetries": List[TelemetryType],
    },
    total=False,
)

AppMonitorDetailsTypeDef = TypedDict(
    "AppMonitorDetailsTypeDef",
    {
        "id": str,
        "name": str,
        "version": str,
    },
    total=False,
)

AppMonitorSummaryTypeDef = TypedDict(
    "AppMonitorSummaryTypeDef",
    {
        "Created": str,
        "Id": str,
        "LastModified": str,
        "Name": str,
        "State": StateEnumType,
    },
    total=False,
)

AppMonitorTypeDef = TypedDict(
    "AppMonitorTypeDef",
    {
        "AppMonitorConfiguration": "AppMonitorConfigurationTypeDef",
        "Created": str,
        "DataStorage": "DataStorageTypeDef",
        "Domain": str,
        "Id": str,
        "LastModified": str,
        "Name": str,
        "State": StateEnumType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAppMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppMonitorRequestRequestTypeDef",
    {
        "Domain": str,
        "Name": str,
    },
)
_OptionalCreateAppMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppMonitorRequestRequestTypeDef",
    {
        "AppMonitorConfiguration": "AppMonitorConfigurationTypeDef",
        "CwLogEnabled": bool,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAppMonitorRequestRequestTypeDef(
    _RequiredCreateAppMonitorRequestRequestTypeDef, _OptionalCreateAppMonitorRequestRequestTypeDef
):
    pass

CreateAppMonitorResponseTypeDef = TypedDict(
    "CreateAppMonitorResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CwLogTypeDef = TypedDict(
    "CwLogTypeDef",
    {
        "CwLogEnabled": bool,
        "CwLogGroup": str,
    },
    total=False,
)

DataStorageTypeDef = TypedDict(
    "DataStorageTypeDef",
    {
        "CwLog": "CwLogTypeDef",
    },
    total=False,
)

DeleteAppMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredGetAppMonitorDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetAppMonitorDataRequestRequestTypeDef",
    {
        "Name": str,
        "TimeRange": "TimeRangeTypeDef",
    },
)
_OptionalGetAppMonitorDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetAppMonitorDataRequestRequestTypeDef",
    {
        "Filters": List["QueryFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetAppMonitorDataRequestRequestTypeDef(
    _RequiredGetAppMonitorDataRequestRequestTypeDef, _OptionalGetAppMonitorDataRequestRequestTypeDef
):
    pass

GetAppMonitorDataResponseTypeDef = TypedDict(
    "GetAppMonitorDataResponseTypeDef",
    {
        "Events": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppMonitorRequestRequestTypeDef = TypedDict(
    "GetAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetAppMonitorResponseTypeDef = TypedDict(
    "GetAppMonitorResponseTypeDef",
    {
        "AppMonitor": "AppMonitorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppMonitorsRequestRequestTypeDef = TypedDict(
    "ListAppMonitorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAppMonitorsResponseTypeDef = TypedDict(
    "ListAppMonitorsResponseTypeDef",
    {
        "AppMonitorSummaries": List["AppMonitorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutRumEventsRequestRequestTypeDef = TypedDict(
    "PutRumEventsRequestRequestTypeDef",
    {
        "AppMonitorDetails": "AppMonitorDetailsTypeDef",
        "BatchId": str,
        "Id": str,
        "RumEvents": List["RumEventTypeDef"],
        "UserDetails": "UserDetailsTypeDef",
    },
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
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

_RequiredRumEventTypeDef = TypedDict(
    "_RequiredRumEventTypeDef",
    {
        "details": str,
        "id": str,
        "timestamp": Union[datetime, str],
        "type": str,
    },
)
_OptionalRumEventTypeDef = TypedDict(
    "_OptionalRumEventTypeDef",
    {
        "metadata": str,
    },
    total=False,
)

class RumEventTypeDef(_RequiredRumEventTypeDef, _OptionalRumEventTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

_RequiredTimeRangeTypeDef = TypedDict(
    "_RequiredTimeRangeTypeDef",
    {
        "After": int,
    },
)
_OptionalTimeRangeTypeDef = TypedDict(
    "_OptionalTimeRangeTypeDef",
    {
        "Before": int,
    },
    total=False,
)

class TimeRangeTypeDef(_RequiredTimeRangeTypeDef, _OptionalTimeRangeTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAppMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateAppMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppMonitorRequestRequestTypeDef",
    {
        "AppMonitorConfiguration": "AppMonitorConfigurationTypeDef",
        "CwLogEnabled": bool,
        "Domain": str,
    },
    total=False,
)

class UpdateAppMonitorRequestRequestTypeDef(
    _RequiredUpdateAppMonitorRequestRequestTypeDef, _OptionalUpdateAppMonitorRequestRequestTypeDef
):
    pass

UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "sessionId": str,
        "userId": str,
    },
    total=False,
)
