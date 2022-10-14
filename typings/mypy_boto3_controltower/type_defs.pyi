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

from .literals import ControlOperationStatusType, ControlOperationTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ControlOperationTypeDef",
    "DisableControlInputRequestTypeDef",
    "DisableControlOutputTypeDef",
    "EnableControlInputRequestTypeDef",
    "EnableControlOutputTypeDef",
    "EnabledControlSummaryTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetControlOperationOutputTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
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

EnableControlInputRequestTypeDef = TypedDict(
    "EnableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)

EnableControlOutputTypeDef = TypedDict(
    "EnableControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnabledControlSummaryTypeDef = TypedDict(
    "EnabledControlSummaryTypeDef",
    {
        "controlIdentifier": str,
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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
