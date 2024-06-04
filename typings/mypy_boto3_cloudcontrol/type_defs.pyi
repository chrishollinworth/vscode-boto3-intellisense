"""
Type annotations for cloudcontrol service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudcontrol.type_defs import CancelResourceRequestInputRequestTypeDef

    data: CancelResourceRequestInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import HandlerErrorCodeType, OperationStatusType, OperationType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelResourceRequestInputRequestTypeDef",
    "CancelResourceRequestOutputTypeDef",
    "CreateResourceInputRequestTypeDef",
    "CreateResourceOutputTypeDef",
    "DeleteResourceInputRequestTypeDef",
    "DeleteResourceOutputTypeDef",
    "GetResourceInputRequestTypeDef",
    "GetResourceOutputTypeDef",
    "GetResourceRequestStatusInputRequestTypeDef",
    "GetResourceRequestStatusOutputTypeDef",
    "ListResourceRequestsInputRequestTypeDef",
    "ListResourceRequestsOutputTypeDef",
    "ListResourcesInputRequestTypeDef",
    "ListResourcesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressEventTypeDef",
    "ResourceDescriptionTypeDef",
    "ResourceRequestStatusFilterTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateResourceInputRequestTypeDef",
    "UpdateResourceOutputTypeDef",
    "WaiterConfigTypeDef",
)

CancelResourceRequestInputRequestTypeDef = TypedDict(
    "CancelResourceRequestInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)

CancelResourceRequestOutputTypeDef = TypedDict(
    "CancelResourceRequestOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceInputRequestTypeDef = TypedDict(
    "_RequiredCreateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "DesiredState": str,
    },
)
_OptionalCreateResourceInputRequestTypeDef = TypedDict(
    "_OptionalCreateResourceInputRequestTypeDef",
    {
        "TypeVersionId": str,
        "RoleArn": str,
        "ClientToken": str,
    },
    total=False,
)

class CreateResourceInputRequestTypeDef(
    _RequiredCreateResourceInputRequestTypeDef, _OptionalCreateResourceInputRequestTypeDef
):
    pass

CreateResourceOutputTypeDef = TypedDict(
    "CreateResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourceInputRequestTypeDef = TypedDict(
    "_RequiredDeleteResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
    },
)
_OptionalDeleteResourceInputRequestTypeDef = TypedDict(
    "_OptionalDeleteResourceInputRequestTypeDef",
    {
        "TypeVersionId": str,
        "RoleArn": str,
        "ClientToken": str,
    },
    total=False,
)

class DeleteResourceInputRequestTypeDef(
    _RequiredDeleteResourceInputRequestTypeDef, _OptionalDeleteResourceInputRequestTypeDef
):
    pass

DeleteResourceOutputTypeDef = TypedDict(
    "DeleteResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceInputRequestTypeDef = TypedDict(
    "_RequiredGetResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
    },
)
_OptionalGetResourceInputRequestTypeDef = TypedDict(
    "_OptionalGetResourceInputRequestTypeDef",
    {
        "TypeVersionId": str,
        "RoleArn": str,
    },
    total=False,
)

class GetResourceInputRequestTypeDef(
    _RequiredGetResourceInputRequestTypeDef, _OptionalGetResourceInputRequestTypeDef
):
    pass

GetResourceOutputTypeDef = TypedDict(
    "GetResourceOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescription": "ResourceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceRequestStatusInputRequestTypeDef = TypedDict(
    "GetResourceRequestStatusInputRequestTypeDef",
    {
        "RequestToken": str,
    },
)

GetResourceRequestStatusOutputTypeDef = TypedDict(
    "GetResourceRequestStatusOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceRequestsInputRequestTypeDef = TypedDict(
    "ListResourceRequestsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ResourceRequestStatusFilter": "ResourceRequestStatusFilterTypeDef",
    },
    total=False,
)

ListResourceRequestsOutputTypeDef = TypedDict(
    "ListResourceRequestsOutputTypeDef",
    {
        "ResourceRequestStatusSummaries": List["ProgressEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListResourcesInputRequestTypeDef",
    {
        "TypeName": str,
    },
)
_OptionalListResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListResourcesInputRequestTypeDef",
    {
        "TypeVersionId": str,
        "RoleArn": str,
        "NextToken": str,
        "MaxResults": int,
        "ResourceModel": str,
    },
    total=False,
)

class ListResourcesInputRequestTypeDef(
    _RequiredListResourcesInputRequestTypeDef, _OptionalListResourcesInputRequestTypeDef
):
    pass

ListResourcesOutputTypeDef = TypedDict(
    "ListResourcesOutputTypeDef",
    {
        "TypeName": str,
        "ResourceDescriptions": List["ResourceDescriptionTypeDef"],
        "NextToken": str,
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

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "RequestToken": str,
        "Operation": OperationType,
        "OperationStatus": OperationStatusType,
        "EventTime": datetime,
        "ResourceModel": str,
        "StatusMessage": str,
        "ErrorCode": HandlerErrorCodeType,
        "RetryAfter": datetime,
    },
    total=False,
)

ResourceDescriptionTypeDef = TypedDict(
    "ResourceDescriptionTypeDef",
    {
        "Identifier": str,
        "Properties": str,
    },
    total=False,
)

ResourceRequestStatusFilterTypeDef = TypedDict(
    "ResourceRequestStatusFilterTypeDef",
    {
        "Operations": List[OperationType],
        "OperationStatuses": List[OperationStatusType],
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

_RequiredUpdateResourceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceInputRequestTypeDef",
    {
        "TypeName": str,
        "Identifier": str,
        "PatchDocument": str,
    },
)
_OptionalUpdateResourceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceInputRequestTypeDef",
    {
        "TypeVersionId": str,
        "RoleArn": str,
        "ClientToken": str,
    },
    total=False,
)

class UpdateResourceInputRequestTypeDef(
    _RequiredUpdateResourceInputRequestTypeDef, _OptionalUpdateResourceInputRequestTypeDef
):
    pass

UpdateResourceOutputTypeDef = TypedDict(
    "UpdateResourceOutputTypeDef",
    {
        "ProgressEvent": "ProgressEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
