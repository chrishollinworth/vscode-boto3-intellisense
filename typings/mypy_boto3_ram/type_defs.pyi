"""
Type annotations for ram service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationRequestTypeDef

    data: AcceptResourceShareInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    PermissionFeatureSetType,
    PermissionStatusType,
    PermissionTypeFilterType,
    PermissionTypeType,
    ReplacePermissionAssociationsWorkStatusType,
    ResourceOwnerType,
    ResourceRegionScopeFilterType,
    ResourceRegionScopeType,
    ResourceShareAssociationStatusType,
    ResourceShareAssociationTypeType,
    ResourceShareFeatureSetType,
    ResourceShareInvitationStatusType,
    ResourceShareStatusType,
    ResourceStatusType,
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
    "AcceptResourceShareInvitationRequestTypeDef",
    "AcceptResourceShareInvitationResponseTypeDef",
    "AssociateResourceSharePermissionRequestTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "AssociateResourceShareRequestTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "AssociatedPermissionTypeDef",
    "CreatePermissionRequestTypeDef",
    "CreatePermissionResponseTypeDef",
    "CreatePermissionVersionRequestTypeDef",
    "CreatePermissionVersionResponseTypeDef",
    "CreateResourceShareRequestTypeDef",
    "CreateResourceShareResponseTypeDef",
    "DeletePermissionRequestTypeDef",
    "DeletePermissionResponseTypeDef",
    "DeletePermissionVersionRequestTypeDef",
    "DeletePermissionVersionResponseTypeDef",
    "DeleteResourceShareRequestTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionRequestTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "DisassociateResourceShareRequestTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetPermissionRequestTypeDef",
    "GetPermissionResponseTypeDef",
    "GetResourcePoliciesRequestPaginateTypeDef",
    "GetResourcePoliciesRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourceShareAssociationsRequestPaginateTypeDef",
    "GetResourceShareAssociationsRequestTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "GetResourceShareInvitationsRequestPaginateTypeDef",
    "GetResourceShareInvitationsRequestTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "GetResourceSharesRequestPaginateTypeDef",
    "GetResourceSharesRequestTypeDef",
    "GetResourceSharesResponseTypeDef",
    "ListPendingInvitationResourcesRequestTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListPermissionAssociationsRequestTypeDef",
    "ListPermissionAssociationsResponseTypeDef",
    "ListPermissionVersionsRequestTypeDef",
    "ListPermissionVersionsResponseTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListPrincipalsRequestPaginateTypeDef",
    "ListPrincipalsRequestTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListReplacePermissionAssociationsWorkRequestTypeDef",
    "ListReplacePermissionAssociationsWorkResponseTypeDef",
    "ListResourceSharePermissionsRequestTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "ListResourceTypesRequestTypeDef",
    "ListResourceTypesResponseTypeDef",
    "ListResourcesRequestPaginateTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrincipalTypeDef",
    "PromotePermissionCreatedFromPolicyRequestTypeDef",
    "PromotePermissionCreatedFromPolicyResponseTypeDef",
    "PromoteResourceShareCreatedFromPolicyRequestTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "RejectResourceShareInvitationRequestTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "ReplacePermissionAssociationsRequestTypeDef",
    "ReplacePermissionAssociationsResponseTypeDef",
    "ReplacePermissionAssociationsWorkTypeDef",
    "ResourceShareAssociationTypeDef",
    "ResourceShareInvitationTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "SetDefaultPermissionVersionRequestTypeDef",
    "SetDefaultPermissionVersionResponseTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateResourceShareRequestTypeDef",
    "UpdateResourceShareResponseTypeDef",
)

class AcceptResourceShareInvitationRequestTypeDef(TypedDict):
    resourceShareInvitationArn: str
    clientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateResourceSharePermissionRequestTypeDef(TypedDict):
    resourceShareArn: str
    permissionArn: str
    replace: NotRequired[bool]
    clientToken: NotRequired[str]
    permissionVersion: NotRequired[int]

class AssociateResourceShareRequestTypeDef(TypedDict):
    resourceShareArn: str
    resourceArns: NotRequired[Sequence[str]]
    principals: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]
    sources: NotRequired[Sequence[str]]

class ResourceShareAssociationTypeDef(TypedDict):
    resourceShareArn: NotRequired[str]
    resourceShareName: NotRequired[str]
    associatedEntity: NotRequired[str]
    associationType: NotRequired[ResourceShareAssociationTypeType]
    status: NotRequired[ResourceShareAssociationStatusType]
    statusMessage: NotRequired[str]
    creationTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    external: NotRequired[bool]

class AssociatedPermissionTypeDef(TypedDict):
    arn: NotRequired[str]
    permissionVersion: NotRequired[str]
    defaultVersion: NotRequired[bool]
    resourceType: NotRequired[str]
    status: NotRequired[str]
    featureSet: NotRequired[PermissionFeatureSetType]
    lastUpdatedTime: NotRequired[datetime]
    resourceShareArn: NotRequired[str]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class CreatePermissionVersionRequestTypeDef(TypedDict):
    permissionArn: str
    policyTemplate: str
    clientToken: NotRequired[str]

class DeletePermissionRequestTypeDef(TypedDict):
    permissionArn: str
    clientToken: NotRequired[str]

class DeletePermissionVersionRequestTypeDef(TypedDict):
    permissionArn: str
    permissionVersion: int
    clientToken: NotRequired[str]

class DeleteResourceShareRequestTypeDef(TypedDict):
    resourceShareArn: str
    clientToken: NotRequired[str]

class DisassociateResourceSharePermissionRequestTypeDef(TypedDict):
    resourceShareArn: str
    permissionArn: str
    clientToken: NotRequired[str]

class DisassociateResourceShareRequestTypeDef(TypedDict):
    resourceShareArn: str
    resourceArns: NotRequired[Sequence[str]]
    principals: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]
    sources: NotRequired[Sequence[str]]

class GetPermissionRequestTypeDef(TypedDict):
    permissionArn: str
    permissionVersion: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetResourcePoliciesRequestTypeDef(TypedDict):
    resourceArns: Sequence[str]
    principal: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetResourceShareAssociationsRequestTypeDef(TypedDict):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: NotRequired[Sequence[str]]
    resourceArn: NotRequired[str]
    principal: NotRequired[str]
    associationStatus: NotRequired[ResourceShareAssociationStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetResourceShareInvitationsRequestTypeDef(TypedDict):
    resourceShareInvitationArns: NotRequired[Sequence[str]]
    resourceShareArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class TagFilterTypeDef(TypedDict):
    tagKey: NotRequired[str]
    tagValues: NotRequired[Sequence[str]]

class ListPendingInvitationResourcesRequestTypeDef(TypedDict):
    resourceShareInvitationArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    resourceRegionScope: NotRequired[ResourceRegionScopeFilterType]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "resourceGroupArn": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "resourceRegionScope": NotRequired[ResourceRegionScopeType],
    },
)

class ListPermissionAssociationsRequestTypeDef(TypedDict):
    permissionArn: NotRequired[str]
    permissionVersion: NotRequired[int]
    associationStatus: NotRequired[ResourceShareAssociationStatusType]
    resourceType: NotRequired[str]
    featureSet: NotRequired[PermissionFeatureSetType]
    defaultVersion: NotRequired[bool]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPermissionVersionsRequestTypeDef(TypedDict):
    permissionArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPermissionsRequestTypeDef(TypedDict):
    resourceType: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    permissionType: NotRequired[PermissionTypeFilterType]

class ListPrincipalsRequestTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    resourceArn: NotRequired[str]
    principals: NotRequired[Sequence[str]]
    resourceType: NotRequired[str]
    resourceShareArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "external": NotRequired[bool],
    },
)

class ListReplacePermissionAssociationsWorkRequestTypeDef(TypedDict):
    workIds: NotRequired[Sequence[str]]
    status: NotRequired[ReplacePermissionAssociationsWorkStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ReplacePermissionAssociationsWorkTypeDef = TypedDict(
    "ReplacePermissionAssociationsWorkTypeDef",
    {
        "id": NotRequired[str],
        "fromPermissionArn": NotRequired[str],
        "fromPermissionVersion": NotRequired[str],
        "toPermissionArn": NotRequired[str],
        "toPermissionVersion": NotRequired[str],
        "status": NotRequired[ReplacePermissionAssociationsWorkStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
    },
)

class ListResourceSharePermissionsRequestTypeDef(TypedDict):
    resourceShareArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListResourceTypesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    resourceRegionScope: NotRequired[ResourceRegionScopeFilterType]

class ServiceNameAndResourceTypeTypeDef(TypedDict):
    resourceType: NotRequired[str]
    serviceName: NotRequired[str]
    resourceRegionScope: NotRequired[ResourceRegionScopeType]

class ListResourcesRequestTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    principal: NotRequired[str]
    resourceType: NotRequired[str]
    resourceArns: NotRequired[Sequence[str]]
    resourceShareArns: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    resourceRegionScope: NotRequired[ResourceRegionScopeFilterType]

class PromotePermissionCreatedFromPolicyRequestTypeDef(TypedDict):
    permissionArn: str
    name: str
    clientToken: NotRequired[str]

class PromoteResourceShareCreatedFromPolicyRequestTypeDef(TypedDict):
    resourceShareArn: str

class RejectResourceShareInvitationRequestTypeDef(TypedDict):
    resourceShareInvitationArn: str
    clientToken: NotRequired[str]

class ReplacePermissionAssociationsRequestTypeDef(TypedDict):
    fromPermissionArn: str
    toPermissionArn: str
    fromPermissionVersion: NotRequired[int]
    clientToken: NotRequired[str]

class SetDefaultPermissionVersionRequestTypeDef(TypedDict):
    permissionArn: str
    permissionVersion: int
    clientToken: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    tagKeys: Sequence[str]
    resourceShareArn: NotRequired[str]
    resourceArn: NotRequired[str]

class UpdateResourceShareRequestTypeDef(TypedDict):
    resourceShareArn: str
    name: NotRequired[str]
    allowExternalPrincipals: NotRequired[bool]
    clientToken: NotRequired[str]

class AssociateResourceSharePermissionResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionVersionResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourceShareResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceSharePermissionResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSharingWithAwsOrganizationResponseTypeDef(TypedDict):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePoliciesResponseTypeDef(TypedDict):
    policies: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PromoteResourceShareCreatedFromPolicyResponseTypeDef(TypedDict):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultPermissionVersionResponseTypeDef(TypedDict):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceShareResponseTypeDef(TypedDict):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceShareResponseTypeDef(TypedDict):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceShareAssociationsResponseTypeDef(TypedDict):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ResourceShareInvitationTypeDef(TypedDict):
    resourceShareInvitationArn: NotRequired[str]
    resourceShareName: NotRequired[str]
    resourceShareArn: NotRequired[str]
    senderAccountId: NotRequired[str]
    receiverAccountId: NotRequired[str]
    invitationTimestamp: NotRequired[datetime]
    status: NotRequired[ResourceShareInvitationStatusType]
    resourceShareAssociations: NotRequired[List[ResourceShareAssociationTypeDef]]
    receiverArn: NotRequired[str]

class ListPermissionAssociationsResponseTypeDef(TypedDict):
    permissions: List[AssociatedPermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreatePermissionRequestTypeDef(TypedDict):
    name: str
    resourceType: str
    policyTemplate: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateResourceShareRequestTypeDef(TypedDict):
    name: str
    resourceArns: NotRequired[Sequence[str]]
    principals: NotRequired[Sequence[str]]
    tags: NotRequired[Sequence[TagTypeDef]]
    allowExternalPrincipals: NotRequired[bool]
    clientToken: NotRequired[str]
    permissionArns: NotRequired[Sequence[str]]
    sources: NotRequired[Sequence[str]]

class ResourceSharePermissionDetailTypeDef(TypedDict):
    arn: NotRequired[str]
    version: NotRequired[str]
    defaultVersion: NotRequired[bool]
    name: NotRequired[str]
    resourceType: NotRequired[str]
    permission: NotRequired[str]
    creationTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    isResourceTypeDefault: NotRequired[bool]
    permissionType: NotRequired[PermissionTypeType]
    featureSet: NotRequired[PermissionFeatureSetType]
    status: NotRequired[PermissionStatusType]
    tags: NotRequired[List[TagTypeDef]]

class ResourceSharePermissionSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    version: NotRequired[str]
    defaultVersion: NotRequired[bool]
    name: NotRequired[str]
    resourceType: NotRequired[str]
    status: NotRequired[str]
    creationTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    isResourceTypeDefault: NotRequired[bool]
    permissionType: NotRequired[PermissionTypeType]
    featureSet: NotRequired[PermissionFeatureSetType]
    tags: NotRequired[List[TagTypeDef]]

class ResourceShareTypeDef(TypedDict):
    resourceShareArn: NotRequired[str]
    name: NotRequired[str]
    owningAccountId: NotRequired[str]
    allowExternalPrincipals: NotRequired[bool]
    status: NotRequired[ResourceShareStatusType]
    statusMessage: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]
    creationTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    featureSet: NotRequired[ResourceShareFeatureSetType]

class TagResourceRequestTypeDef(TypedDict):
    tags: Sequence[TagTypeDef]
    resourceShareArn: NotRequired[str]
    resourceArn: NotRequired[str]

class GetResourcePoliciesRequestPaginateTypeDef(TypedDict):
    resourceArns: Sequence[str]
    principal: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourceShareAssociationsRequestPaginateTypeDef(TypedDict):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: NotRequired[Sequence[str]]
    resourceArn: NotRequired[str]
    principal: NotRequired[str]
    associationStatus: NotRequired[ResourceShareAssociationStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourceShareInvitationsRequestPaginateTypeDef(TypedDict):
    resourceShareInvitationArns: NotRequired[Sequence[str]]
    resourceShareArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrincipalsRequestPaginateTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    resourceArn: NotRequired[str]
    principals: NotRequired[Sequence[str]]
    resourceType: NotRequired[str]
    resourceShareArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcesRequestPaginateTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    principal: NotRequired[str]
    resourceType: NotRequired[str]
    resourceArns: NotRequired[Sequence[str]]
    resourceShareArns: NotRequired[Sequence[str]]
    resourceRegionScope: NotRequired[ResourceRegionScopeFilterType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourceSharesRequestPaginateTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    resourceShareArns: NotRequired[Sequence[str]]
    resourceShareStatus: NotRequired[ResourceShareStatusType]
    name: NotRequired[str]
    tagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    permissionArn: NotRequired[str]
    permissionVersion: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourceSharesRequestTypeDef(TypedDict):
    resourceOwner: ResourceOwnerType
    resourceShareArns: NotRequired[Sequence[str]]
    resourceShareStatus: NotRequired[ResourceShareStatusType]
    name: NotRequired[str]
    tagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    permissionArn: NotRequired[str]
    permissionVersion: NotRequired[int]

class ListPendingInvitationResourcesResponseTypeDef(TypedDict):
    resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourcesResponseTypeDef(TypedDict):
    resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPrincipalsResponseTypeDef(TypedDict):
    principals: List[PrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReplacePermissionAssociationsWorkResponseTypeDef(TypedDict):
    replacePermissionAssociationsWorks: List[ReplacePermissionAssociationsWorkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReplacePermissionAssociationsResponseTypeDef(TypedDict):
    replacePermissionAssociationsWork: ReplacePermissionAssociationsWorkTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceTypesResponseTypeDef(TypedDict):
    resourceTypes: List[ServiceNameAndResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AcceptResourceShareInvitationResponseTypeDef(TypedDict):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceShareInvitationsResponseTypeDef(TypedDict):
    resourceShareInvitations: List[ResourceShareInvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RejectResourceShareInvitationResponseTypeDef(TypedDict):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionVersionResponseTypeDef(TypedDict):
    permission: ResourceSharePermissionDetailTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionResponseTypeDef(TypedDict):
    permission: ResourceSharePermissionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionResponseTypeDef(TypedDict):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionVersionsResponseTypeDef(TypedDict):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPermissionsResponseTypeDef(TypedDict):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceSharePermissionsResponseTypeDef(TypedDict):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PromotePermissionCreatedFromPolicyResponseTypeDef(TypedDict):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceShareResponseTypeDef(TypedDict):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSharesResponseTypeDef(TypedDict):
    resourceShares: List[ResourceShareTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateResourceShareResponseTypeDef(TypedDict):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef
