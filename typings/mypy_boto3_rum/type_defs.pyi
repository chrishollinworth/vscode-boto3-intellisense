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

from .literals import CustomEventsStatusType, MetricDestinationType, StateEnumType, TelemetryType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppMonitorConfigurationTypeDef",
    "AppMonitorDetailsTypeDef",
    "AppMonitorSummaryTypeDef",
    "AppMonitorTypeDef",
    "BatchCreateRumMetricDefinitionsErrorTypeDef",
    "BatchCreateRumMetricDefinitionsRequestRequestTypeDef",
    "BatchCreateRumMetricDefinitionsResponseTypeDef",
    "BatchDeleteRumMetricDefinitionsErrorTypeDef",
    "BatchDeleteRumMetricDefinitionsRequestRequestTypeDef",
    "BatchDeleteRumMetricDefinitionsResponseTypeDef",
    "BatchGetRumMetricDefinitionsRequestRequestTypeDef",
    "BatchGetRumMetricDefinitionsResponseTypeDef",
    "CreateAppMonitorRequestRequestTypeDef",
    "CreateAppMonitorResponseTypeDef",
    "CustomEventsTypeDef",
    "CwLogTypeDef",
    "DataStorageTypeDef",
    "DeleteAppMonitorRequestRequestTypeDef",
    "DeleteRumMetricsDestinationRequestRequestTypeDef",
    "GetAppMonitorDataRequestRequestTypeDef",
    "GetAppMonitorDataResponseTypeDef",
    "GetAppMonitorRequestRequestTypeDef",
    "GetAppMonitorResponseTypeDef",
    "ListAppMonitorsRequestRequestTypeDef",
    "ListAppMonitorsResponseTypeDef",
    "ListRumMetricsDestinationsRequestRequestTypeDef",
    "ListRumMetricsDestinationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDefinitionRequestTypeDef",
    "MetricDefinitionTypeDef",
    "MetricDestinationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutRumEventsRequestRequestTypeDef",
    "PutRumMetricsDestinationRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "ResponseMetadataTypeDef",
    "RumEventTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppMonitorRequestRequestTypeDef",
    "UpdateRumMetricDefinitionRequestRequestTypeDef",
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
        "CustomEvents": "CustomEventsTypeDef",
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

BatchCreateRumMetricDefinitionsErrorTypeDef = TypedDict(
    "BatchCreateRumMetricDefinitionsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "MetricDefinition": "MetricDefinitionRequestTypeDef",
    },
)

_RequiredBatchCreateRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinitions": List["MetricDefinitionRequestTypeDef"],
    },
)
_OptionalBatchCreateRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateRumMetricDefinitionsRequestRequestTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

class BatchCreateRumMetricDefinitionsRequestRequestTypeDef(
    _RequiredBatchCreateRumMetricDefinitionsRequestRequestTypeDef,
    _OptionalBatchCreateRumMetricDefinitionsRequestRequestTypeDef,
):
    pass

BatchCreateRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchCreateRumMetricDefinitionsResponseTypeDef",
    {
        "Errors": List["BatchCreateRumMetricDefinitionsErrorTypeDef"],
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteRumMetricDefinitionsErrorTypeDef = TypedDict(
    "BatchDeleteRumMetricDefinitionsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "MetricDefinitionId": str,
    },
)

_RequiredBatchDeleteRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinitionIds": List[str],
    },
)
_OptionalBatchDeleteRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteRumMetricDefinitionsRequestRequestTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

class BatchDeleteRumMetricDefinitionsRequestRequestTypeDef(
    _RequiredBatchDeleteRumMetricDefinitionsRequestRequestTypeDef,
    _OptionalBatchDeleteRumMetricDefinitionsRequestRequestTypeDef,
):
    pass

BatchDeleteRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchDeleteRumMetricDefinitionsResponseTypeDef",
    {
        "Errors": List["BatchDeleteRumMetricDefinitionsErrorTypeDef"],
        "MetricDefinitionIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
    },
)
_OptionalBatchGetRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetRumMetricDefinitionsRequestRequestTypeDef",
    {
        "DestinationArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class BatchGetRumMetricDefinitionsRequestRequestTypeDef(
    _RequiredBatchGetRumMetricDefinitionsRequestRequestTypeDef,
    _OptionalBatchGetRumMetricDefinitionsRequestRequestTypeDef,
):
    pass

BatchGetRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchGetRumMetricDefinitionsResponseTypeDef",
    {
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "CustomEvents": "CustomEventsTypeDef",
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

CustomEventsTypeDef = TypedDict(
    "CustomEventsTypeDef",
    {
        "Status": CustomEventsStatusType,
    },
    total=False,
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

_RequiredDeleteRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRumMetricsDestinationRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
    },
)
_OptionalDeleteRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRumMetricsDestinationRequestRequestTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

class DeleteRumMetricsDestinationRequestRequestTypeDef(
    _RequiredDeleteRumMetricsDestinationRequestRequestTypeDef,
    _OptionalDeleteRumMetricsDestinationRequestRequestTypeDef,
):
    pass

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

_RequiredListRumMetricsDestinationsRequestRequestTypeDef = TypedDict(
    "_RequiredListRumMetricsDestinationsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
    },
)
_OptionalListRumMetricsDestinationsRequestRequestTypeDef = TypedDict(
    "_OptionalListRumMetricsDestinationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRumMetricsDestinationsRequestRequestTypeDef(
    _RequiredListRumMetricsDestinationsRequestRequestTypeDef,
    _OptionalListRumMetricsDestinationsRequestRequestTypeDef,
):
    pass

ListRumMetricsDestinationsResponseTypeDef = TypedDict(
    "ListRumMetricsDestinationsResponseTypeDef",
    {
        "Destinations": List["MetricDestinationSummaryTypeDef"],
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

_RequiredMetricDefinitionRequestTypeDef = TypedDict(
    "_RequiredMetricDefinitionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalMetricDefinitionRequestTypeDef = TypedDict(
    "_OptionalMetricDefinitionRequestTypeDef",
    {
        "DimensionKeys": Dict[str, str],
        "EventPattern": str,
        "Namespace": str,
        "UnitLabel": str,
        "ValueKey": str,
    },
    total=False,
)

class MetricDefinitionRequestTypeDef(
    _RequiredMetricDefinitionRequestTypeDef, _OptionalMetricDefinitionRequestTypeDef
):
    pass

_RequiredMetricDefinitionTypeDef = TypedDict(
    "_RequiredMetricDefinitionTypeDef",
    {
        "MetricDefinitionId": str,
        "Name": str,
    },
)
_OptionalMetricDefinitionTypeDef = TypedDict(
    "_OptionalMetricDefinitionTypeDef",
    {
        "DimensionKeys": Dict[str, str],
        "EventPattern": str,
        "Namespace": str,
        "UnitLabel": str,
        "ValueKey": str,
    },
    total=False,
)

class MetricDefinitionTypeDef(_RequiredMetricDefinitionTypeDef, _OptionalMetricDefinitionTypeDef):
    pass

MetricDestinationSummaryTypeDef = TypedDict(
    "MetricDestinationSummaryTypeDef",
    {
        "Destination": MetricDestinationType,
        "DestinationArn": str,
        "IamRoleArn": str,
    },
    total=False,
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

_RequiredPutRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredPutRumMetricsDestinationRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
    },
)
_OptionalPutRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalPutRumMetricsDestinationRequestRequestTypeDef",
    {
        "DestinationArn": str,
        "IamRoleArn": str,
    },
    total=False,
)

class PutRumMetricsDestinationRequestRequestTypeDef(
    _RequiredPutRumMetricsDestinationRequestRequestTypeDef,
    _OptionalPutRumMetricsDestinationRequestRequestTypeDef,
):
    pass

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
        "CustomEvents": "CustomEventsTypeDef",
        "CwLogEnabled": bool,
        "Domain": str,
    },
    total=False,
)

class UpdateAppMonitorRequestRequestTypeDef(
    _RequiredUpdateAppMonitorRequestRequestTypeDef, _OptionalUpdateAppMonitorRequestRequestTypeDef
):
    pass

_RequiredUpdateRumMetricDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRumMetricDefinitionRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinition": "MetricDefinitionRequestTypeDef",
        "MetricDefinitionId": str,
    },
)
_OptionalUpdateRumMetricDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRumMetricDefinitionRequestRequestTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

class UpdateRumMetricDefinitionRequestRequestTypeDef(
    _RequiredUpdateRumMetricDefinitionRequestRequestTypeDef,
    _OptionalUpdateRumMetricDefinitionRequestRequestTypeDef,
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
