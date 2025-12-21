"""
Type annotations for repostspace service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_repostspace.type_defs import BatchAddChannelRoleToAccessorsInputTypeDef

    data: BatchAddChannelRoleToAccessorsInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ChannelRoleType,
    ChannelStatusType,
    ConfigurationStatusType,
    FeatureEnableParameterType,
    FeatureEnableStatusType,
    RoleType,
    TierLevelType,
    VanityDomainStatusType,
)

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
    "BatchAddChannelRoleToAccessorsInputTypeDef",
    "BatchAddChannelRoleToAccessorsOutputTypeDef",
    "BatchAddRoleInputTypeDef",
    "BatchAddRoleOutputTypeDef",
    "BatchErrorTypeDef",
    "BatchRemoveChannelRoleFromAccessorsInputTypeDef",
    "BatchRemoveChannelRoleFromAccessorsOutputTypeDef",
    "BatchRemoveRoleInputTypeDef",
    "BatchRemoveRoleOutputTypeDef",
    "ChannelDataTypeDef",
    "CreateChannelInputTypeDef",
    "CreateChannelOutputTypeDef",
    "CreateSpaceInputTypeDef",
    "CreateSpaceOutputTypeDef",
    "DeleteSpaceInputTypeDef",
    "DeregisterAdminInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChannelInputTypeDef",
    "GetChannelInputWaitExtraTypeDef",
    "GetChannelInputWaitTypeDef",
    "GetChannelOutputTypeDef",
    "GetSpaceInputTypeDef",
    "GetSpaceInputWaitExtraTypeDef",
    "GetSpaceInputWaitTypeDef",
    "GetSpaceOutputTypeDef",
    "ListChannelsInputPaginateTypeDef",
    "ListChannelsInputTypeDef",
    "ListChannelsOutputTypeDef",
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
    "SupportedEmailDomainsParametersTypeDef",
    "SupportedEmailDomainsStatusTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelInputTypeDef",
    "UpdateSpaceInputTypeDef",
    "WaiterConfigTypeDef",
)

class BatchAddChannelRoleToAccessorsInputTypeDef(TypedDict):
    spaceId: str
    channelId: str
    accessorIds: Sequence[str]
    channelRole: ChannelRoleType

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

class BatchAddRoleInputTypeDef(TypedDict):
    spaceId: str
    accessorIds: Sequence[str]
    role: RoleType

class BatchRemoveChannelRoleFromAccessorsInputTypeDef(TypedDict):
    spaceId: str
    channelId: str
    accessorIds: Sequence[str]
    channelRole: ChannelRoleType

class BatchRemoveRoleInputTypeDef(TypedDict):
    spaceId: str
    accessorIds: Sequence[str]
    role: RoleType

class ChannelDataTypeDef(TypedDict):
    spaceId: str
    channelId: str
    channelName: str
    createDateTime: datetime
    channelStatus: ChannelStatusType
    userCount: int
    groupCount: int
    channelDescription: NotRequired[str]
    deleteDateTime: NotRequired[datetime]

class CreateChannelInputTypeDef(TypedDict):
    spaceId: str
    channelName: str
    channelDescription: NotRequired[str]

class SupportedEmailDomainsParametersTypeDef(TypedDict):
    enabled: NotRequired[FeatureEnableParameterType]
    allowedDomains: NotRequired[Sequence[str]]

class DeleteSpaceInputTypeDef(TypedDict):
    spaceId: str

class DeregisterAdminInputTypeDef(TypedDict):
    spaceId: str
    adminId: str

class GetChannelInputTypeDef(TypedDict):
    spaceId: str
    channelId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetSpaceInputTypeDef(TypedDict):
    spaceId: str

class SupportedEmailDomainsStatusTypeDef(TypedDict):
    enabled: NotRequired[FeatureEnableStatusType]
    allowedDomains: NotRequired[List[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChannelsInputTypeDef(TypedDict):
    spaceId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSpacesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RegisterAdminInputTypeDef(TypedDict):
    spaceId: str
    adminId: str

class SendInvitesInputTypeDef(TypedDict):
    spaceId: str
    accessorIds: Sequence[str]
    title: str
    body: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateChannelInputTypeDef(TypedDict):
    spaceId: str
    channelId: str
    channelName: str
    channelDescription: NotRequired[str]

class BatchAddChannelRoleToAccessorsOutputTypeDef(TypedDict):
    addedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAddRoleOutputTypeDef(TypedDict):
    addedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchRemoveChannelRoleFromAccessorsOutputTypeDef(TypedDict):
    removedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchRemoveRoleOutputTypeDef(TypedDict):
    removedAccessorIds: List[str]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelOutputTypeDef(TypedDict):
    channelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSpaceOutputTypeDef(TypedDict):
    spaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelOutputTypeDef(TypedDict):
    spaceId: str
    channelId: str
    channelName: str
    channelDescription: str
    createDateTime: datetime
    deleteDateTime: datetime
    channelRoles: Dict[str, List[ChannelRoleType]]
    channelStatus: ChannelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsOutputTypeDef(TypedDict):
    channels: List[ChannelDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateSpaceInputTypeDef(TypedDict):
    name: str
    subdomain: str
    tier: TierLevelType
    description: NotRequired[str]
    userKMSKey: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    roleArn: NotRequired[str]
    supportedEmailDomains: NotRequired[SupportedEmailDomainsParametersTypeDef]

class UpdateSpaceInputTypeDef(TypedDict):
    spaceId: str
    description: NotRequired[str]
    tier: NotRequired[TierLevelType]
    roleArn: NotRequired[str]
    supportedEmailDomains: NotRequired[SupportedEmailDomainsParametersTypeDef]

class GetChannelInputWaitExtraTypeDef(TypedDict):
    spaceId: str
    channelId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetChannelInputWaitTypeDef(TypedDict):
    spaceId: str
    channelId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetSpaceInputWaitExtraTypeDef(TypedDict):
    spaceId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetSpaceInputWaitTypeDef(TypedDict):
    spaceId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetSpaceOutputTypeDef(TypedDict):
    spaceId: str
    arn: str
    name: str
    status: str
    configurationStatus: ConfigurationStatusType
    clientId: str
    identityStoreId: str
    applicationArn: str
    description: str
    vanityDomainStatus: VanityDomainStatusType
    vanityDomain: str
    randomDomain: str
    customerRoleArn: str
    createDateTime: datetime
    deleteDateTime: datetime
    tier: TierLevelType
    storageLimit: int
    userAdmins: List[str]
    groupAdmins: List[str]
    roles: Dict[str, List[RoleType]]
    userKMSKey: str
    userCount: int
    contentSize: int
    supportedEmailDomains: SupportedEmailDomainsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpaceDataTypeDef(TypedDict):
    spaceId: str
    arn: str
    name: str
    status: str
    configurationStatus: ConfigurationStatusType
    vanityDomainStatus: VanityDomainStatusType
    vanityDomain: str
    randomDomain: str
    tier: TierLevelType
    storageLimit: int
    createDateTime: datetime
    description: NotRequired[str]
    deleteDateTime: NotRequired[datetime]
    userKMSKey: NotRequired[str]
    userCount: NotRequired[int]
    contentSize: NotRequired[int]
    supportedEmailDomains: NotRequired[SupportedEmailDomainsStatusTypeDef]

class ListChannelsInputPaginateTypeDef(TypedDict):
    spaceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpacesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpacesOutputTypeDef(TypedDict):
    spaces: List[SpaceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
