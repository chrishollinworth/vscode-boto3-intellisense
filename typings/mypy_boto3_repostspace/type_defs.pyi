"""
Type annotations for repostspace service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_repostspace.type_defs import BatchAddRoleInputTypeDef

    data: BatchAddRoleInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import ConfigurationStatusType, RoleType, TierLevelType, VanityDomainStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BatchAddRoleInputTypeDef",
    "BatchAddRoleOutputTypeDef",
    "BatchErrorTypeDef",
    "BatchRemoveRoleInputTypeDef",
    "BatchRemoveRoleOutputTypeDef",
    "CreateSpaceInputTypeDef",
    "CreateSpaceOutputTypeDef",
    "DeleteSpaceInputTypeDef",
    "DeregisterAdminInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetSpaceInputTypeDef",
    "GetSpaceOutputTypeDef",
    "ListSpacesInputPaginateTypeDef",
    "ListSpacesInputTypeDef",
    "ListSpacesOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterAdminInputTypeDef",
    "ResponseMetadataTypeDef",
    "SendInvitesInputTypeDef",
    "SpaceDataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateSpaceInputTypeDef",
)

class BatchAddRoleInputTypeDef(TypedDict):
    accessorIds: Sequence[str]
    role: RoleType
    spaceId: str

class BatchErrorTypeDef(TypedDict):
    accessorId: str
    error: int
    message: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchRemoveRoleInputTypeDef(TypedDict):
    accessorIds: Sequence[str]
    role: RoleType
    spaceId: str

class CreateSpaceInputTypeDef(TypedDict):
    name: str
    subdomain: str
    tier: TierLevelType
    description: NotRequired[str]
    roleArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    userKMSKey: NotRequired[str]

class DeleteSpaceInputTypeDef(TypedDict):
    spaceId: str

class DeregisterAdminInputTypeDef(TypedDict):
    adminId: str
    spaceId: str

class GetSpaceInputTypeDef(TypedDict):
    spaceId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSpacesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SpaceDataTypeDef(TypedDict):
    arn: str
    configurationStatus: ConfigurationStatusType
    createDateTime: datetime
    name: str
    randomDomain: str
    spaceId: str
    status: str
    storageLimit: int
    tier: TierLevelType
    vanityDomain: str
    vanityDomainStatus: VanityDomainStatusType
    contentSize: NotRequired[int]
    deleteDateTime: NotRequired[datetime]
    description: NotRequired[str]
    userCount: NotRequired[int]
    userKMSKey: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RegisterAdminInputTypeDef(TypedDict):
    adminId: str
    spaceId: str

class SendInvitesInputTypeDef(TypedDict):
    accessorIds: Sequence[str]
    body: str
    spaceId: str
    title: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSpaceInputTypeDef(TypedDict):
    spaceId: str
    description: NotRequired[str]
    roleArn: NotRequired[str]
    tier: NotRequired[TierLevelType]

class BatchAddRoleOutputTypeDef(TypedDict):
    addedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchRemoveRoleOutputTypeDef(TypedDict):
    errors: List[BatchErrorTypeDef]
    removedAccessorIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSpaceOutputTypeDef(TypedDict):
    spaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpaceOutputTypeDef(TypedDict):
    arn: str
    clientId: str
    configurationStatus: ConfigurationStatusType
    contentSize: int
    createDateTime: datetime
    customerRoleArn: str
    deleteDateTime: datetime
    description: str
    groupAdmins: List[str]
    name: str
    randomDomain: str
    roles: Dict[str, List[RoleType]]
    spaceId: str
    status: str
    storageLimit: int
    tier: TierLevelType
    userAdmins: List[str]
    userCount: int
    userKMSKey: str
    vanityDomain: str
    vanityDomainStatus: VanityDomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpacesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpacesOutputTypeDef(TypedDict):
    spaces: List[SpaceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
