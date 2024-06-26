"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointRequestRequestTypeDef

    data: CreateEndpointRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import EndpointAccessTypeType, EndpointStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResultTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "EndpointTypeDef",
    "FailedReasonTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResultTypeDef",
    "ListOutpostsWithS3RequestRequestTypeDef",
    "ListOutpostsWithS3ResultTypeDef",
    "ListSharedEndpointsRequestRequestTypeDef",
    "ListSharedEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

_RequiredCreateEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointRequestRequestTypeDef",
    {
        "OutpostId": str,
        "SubnetId": str,
        "SecurityGroupId": str,
    },
)
_OptionalCreateEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointRequestRequestTypeDef",
    {
        "AccessType": EndpointAccessTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)

class CreateEndpointRequestRequestTypeDef(
    _RequiredCreateEndpointRequestRequestTypeDef, _OptionalCreateEndpointRequestRequestTypeDef
):
    pass

CreateEndpointResultTypeDef = TypedDict(
    "CreateEndpointResultTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointId": str,
        "OutpostId": str,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": str,
        "OutpostsId": str,
        "CidrBlock": str,
        "Status": EndpointStatusType,
        "CreationTime": datetime,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "VpcId": str,
        "SubnetId": str,
        "SecurityGroupId": str,
        "AccessType": EndpointAccessTypeType,
        "CustomerOwnedIpv4Pool": str,
        "FailedReason": "FailedReasonTypeDef",
    },
    total=False,
)

FailedReasonTypeDef = TypedDict(
    "FailedReasonTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEndpointsResultTypeDef = TypedDict(
    "ListEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutpostsWithS3RequestRequestTypeDef = TypedDict(
    "ListOutpostsWithS3RequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOutpostsWithS3ResultTypeDef = TypedDict(
    "ListOutpostsWithS3ResultTypeDef",
    {
        "Outposts": List["OutpostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSharedEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListSharedEndpointsRequestRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalListSharedEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListSharedEndpointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListSharedEndpointsRequestRequestTypeDef(
    _RequiredListSharedEndpointsRequestRequestTypeDef,
    _OptionalListSharedEndpointsRequestRequestTypeDef,
):
    pass

ListSharedEndpointsResultTypeDef = TypedDict(
    "ListSharedEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": str,
    },
    total=False,
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostArn": str,
        "S3OutpostArn": str,
        "OutpostId": str,
        "OwnerId": str,
        "CapacityInBytes": int,
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
