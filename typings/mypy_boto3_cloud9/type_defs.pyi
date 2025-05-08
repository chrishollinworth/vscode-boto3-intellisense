"""
Type annotations for cloud9 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsActionType,
    ManagedCredentialsStatusType,
    MemberPermissionsType,
    PermissionsType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateEnvironmentEC2RequestTypeDef",
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipRequestTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DeleteEnvironmentMembershipRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DescribeEnvironmentMembershipsRequestPaginateTypeDef",
    "DescribeEnvironmentMembershipsRequestTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusRequestTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsRequestTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsRequestPaginateTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEnvironmentMembershipRequestTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
    "UpdateEnvironmentRequestTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateEnvironmentMembershipRequestTypeDef(TypedDict):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class EnvironmentMemberTypeDef(TypedDict):
    permissions: PermissionsType
    userId: str
    userArn: str
    environmentId: str
    lastAccess: NotRequired[datetime]

class DeleteEnvironmentMembershipRequestTypeDef(TypedDict):
    environmentId: str
    userArn: str

class DeleteEnvironmentRequestTypeDef(TypedDict):
    environmentId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeEnvironmentMembershipsRequestTypeDef(TypedDict):
    userArn: NotRequired[str]
    environmentId: NotRequired[str]
    permissions: NotRequired[Sequence[PermissionsType]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeEnvironmentStatusRequestTypeDef(TypedDict):
    environmentId: str

class DescribeEnvironmentsRequestTypeDef(TypedDict):
    environmentIds: Sequence[str]

class EnvironmentLifecycleTypeDef(TypedDict):
    status: NotRequired[EnvironmentLifecycleStatusType]
    reason: NotRequired[str]
    failureResource: NotRequired[str]

class ListEnvironmentsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateEnvironmentMembershipRequestTypeDef(TypedDict):
    environmentId: str
    userArn: str
    permissions: MemberPermissionsType

class UpdateEnvironmentRequestTypeDef(TypedDict):
    environmentId: str
    name: NotRequired[str]
    description: NotRequired[str]
    managedCredentialsAction: NotRequired[ManagedCredentialsActionType]

class CreateEnvironmentEC2RequestTypeDef(TypedDict):
    name: str
    instanceType: str
    imageId: str
    description: NotRequired[str]
    clientRequestToken: NotRequired[str]
    subnetId: NotRequired[str]
    automaticStopTimeMinutes: NotRequired[int]
    ownerArn: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    connectionType: NotRequired[ConnectionTypeType]
    dryRun: NotRequired[bool]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateEnvironmentEC2ResultTypeDef(TypedDict):
    environmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentStatusResultTypeDef(TypedDict):
    status: EnvironmentStatusType
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResultTypeDef(TypedDict):
    environmentIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentMembershipResultTypeDef(TypedDict):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsResultTypeDef(TypedDict):
    memberships: List[EnvironmentMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEnvironmentMembershipResultTypeDef(TypedDict):
    membership: EnvironmentMemberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentMembershipsRequestPaginateTypeDef(TypedDict):
    userArn: NotRequired[str]
    environmentId: NotRequired[str]
    permissions: NotRequired[Sequence[PermissionsType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "arn": str,
        "ownerArn": str,
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "lifecycle": NotRequired[EnvironmentLifecycleTypeDef],
        "managedCredentialsStatus": NotRequired[ManagedCredentialsStatusType],
    },
)

class DescribeEnvironmentsResultTypeDef(TypedDict):
    environments: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
