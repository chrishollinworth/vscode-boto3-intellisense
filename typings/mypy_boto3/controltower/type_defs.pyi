"""
Type annotations for controltower service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/type_defs.html)

Usage::

    ```python
    from mypy_boto3_controltower.type_defs import ControlOperationTypeDef

    data: ControlOperationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ControlOperationStatusType,
    ControlOperationTypeType,
    DriftStatusType,
    EnablementStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ControlOperationTypeDef",
    "DisableControlInputRequestTypeDef",
    "DisableControlOutputTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnableControlInputRequestTypeDef",
    "EnableControlOutputTypeDef",
    "EnabledControlDetailsTypeDef",
    "EnabledControlSummaryTypeDef",
    "EnablementStatusSummaryTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetControlOperationOutputTypeDef",
    "GetEnabledControlInputRequestTypeDef",
    "GetEnabledControlOutputTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegionTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
)

ControlOperationTypeDef = TypedDict(
    "ControlOperationTypeDef",
    {
        "endTime": datetime,
        "operationType": ControlOperationTypeType,
        "startTime": datetime,
        "status": ControlOperationStatusType,
        "statusMessage": str,
    },
    total=False,
)

DisableControlInputRequestTypeDef = TypedDict(
    "DisableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)

DisableControlOutputTypeDef = TypedDict(
    "DisableControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DriftStatusSummaryTypeDef = TypedDict(
    "DriftStatusSummaryTypeDef",
    {
        "driftStatus": DriftStatusType,
    },
    total=False,
)

_RequiredEnableControlInputRequestTypeDef = TypedDict(
    "_RequiredEnableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)
_OptionalEnableControlInputRequestTypeDef = TypedDict(
    "_OptionalEnableControlInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class EnableControlInputRequestTypeDef(
    _RequiredEnableControlInputRequestTypeDef, _OptionalEnableControlInputRequestTypeDef
):
    pass

EnableControlOutputTypeDef = TypedDict(
    "EnableControlOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnabledControlDetailsTypeDef = TypedDict(
    "EnabledControlDetailsTypeDef",
    {
        "arn": str,
        "controlIdentifier": str,
        "driftStatusSummary": "DriftStatusSummaryTypeDef",
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
        "targetRegions": List["RegionTypeDef"],
    },
    total=False,
)

EnabledControlSummaryTypeDef = TypedDict(
    "EnabledControlSummaryTypeDef",
    {
        "arn": str,
        "controlIdentifier": str,
        "driftStatusSummary": "DriftStatusSummaryTypeDef",
        "statusSummary": "EnablementStatusSummaryTypeDef",
        "targetIdentifier": str,
    },
    total=False,
)

EnablementStatusSummaryTypeDef = TypedDict(
    "EnablementStatusSummaryTypeDef",
    {
        "lastOperationIdentifier": str,
        "status": EnablementStatusType,
    },
    total=False,
)

GetControlOperationInputRequestTypeDef = TypedDict(
    "GetControlOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)

GetControlOperationOutputTypeDef = TypedDict(
    "GetControlOperationOutputTypeDef",
    {
        "controlOperation": "ControlOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnabledControlInputRequestTypeDef = TypedDict(
    "GetEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
    },
)

GetEnabledControlOutputTypeDef = TypedDict(
    "GetEnabledControlOutputTypeDef",
    {
        "enabledControlDetails": "EnabledControlDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnabledControlsInputRequestTypeDef = TypedDict(
    "_RequiredListEnabledControlsInputRequestTypeDef",
    {
        "targetIdentifier": str,
    },
)
_OptionalListEnabledControlsInputRequestTypeDef = TypedDict(
    "_OptionalListEnabledControlsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEnabledControlsInputRequestTypeDef(
    _RequiredListEnabledControlsInputRequestTypeDef, _OptionalListEnabledControlsInputRequestTypeDef
):
    pass

ListEnabledControlsOutputTypeDef = TypedDict(
    "ListEnabledControlsOutputTypeDef",
    {
        "enabledControls": List["EnabledControlSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
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

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "name": str,
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
