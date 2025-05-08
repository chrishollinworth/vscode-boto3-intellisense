"""
Type annotations for s3outposts service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointRequestTypeDef

    data: CreateEndpointRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import EndpointAccessTypeType, EndpointStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateEndpointRequestTypeDef",
    "CreateEndpointResultTypeDef",
    "DeleteEndpointRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointTypeDef",
    "FailedReasonTypeDef",
    "ListEndpointsRequestPaginateTypeDef",
    "ListEndpointsRequestTypeDef",
    "ListEndpointsResultTypeDef",
    "ListOutpostsWithS3RequestPaginateTypeDef",
    "ListOutpostsWithS3RequestTypeDef",
    "ListOutpostsWithS3ResultTypeDef",
    "ListSharedEndpointsRequestPaginateTypeDef",
    "ListSharedEndpointsRequestTypeDef",
    "ListSharedEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

class CreateEndpointRequestTypeDef(TypedDict):
    OutpostId: str
    SubnetId: str
    SecurityGroupId: str
    AccessType: NotRequired[EndpointAccessTypeType]
    CustomerOwnedIpv4Pool: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteEndpointRequestTypeDef(TypedDict):
    EndpointId: str
    OutpostId: str

class FailedReasonTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class NetworkInterfaceTypeDef(TypedDict):
    NetworkInterfaceId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEndpointsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListOutpostsWithS3RequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OutpostTypeDef(TypedDict):
    OutpostArn: NotRequired[str]
    S3OutpostArn: NotRequired[str]
    OutpostId: NotRequired[str]
    OwnerId: NotRequired[str]
    CapacityInBytes: NotRequired[int]

class ListSharedEndpointsRequestTypeDef(TypedDict):
    OutpostId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class CreateEndpointResultTypeDef(TypedDict):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointTypeDef(TypedDict):
    EndpointArn: NotRequired[str]
    OutpostsId: NotRequired[str]
    CidrBlock: NotRequired[str]
    Status: NotRequired[EndpointStatusType]
    CreationTime: NotRequired[datetime]
    NetworkInterfaces: NotRequired[List[NetworkInterfaceTypeDef]]
    VpcId: NotRequired[str]
    SubnetId: NotRequired[str]
    SecurityGroupId: NotRequired[str]
    AccessType: NotRequired[EndpointAccessTypeType]
    CustomerOwnedIpv4Pool: NotRequired[str]
    FailedReason: NotRequired[FailedReasonTypeDef]

class ListEndpointsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOutpostsWithS3RequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSharedEndpointsRequestPaginateTypeDef(TypedDict):
    OutpostId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOutpostsWithS3ResultTypeDef(TypedDict):
    Outposts: List[OutpostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEndpointsResultTypeDef(TypedDict):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSharedEndpointsResultTypeDef(TypedDict):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
