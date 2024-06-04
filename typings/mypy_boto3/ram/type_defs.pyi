"""
Type annotations for ram service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationRequestRequestTypeDef

    data: AcceptResourceShareInvitationRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptResourceShareInvitationRequestRequestTypeDef",
    "AcceptResourceShareInvitationResponseTypeDef",
    "AssociateResourceSharePermissionRequestRequestTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "AssociateResourceShareRequestRequestTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "AssociatedPermissionTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CreatePermissionResponseTypeDef",
    "CreatePermissionVersionRequestRequestTypeDef",
    "CreatePermissionVersionResponseTypeDef",
    "CreateResourceShareRequestRequestTypeDef",
    "CreateResourceShareResponseTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePermissionResponseTypeDef",
    "DeletePermissionVersionRequestRequestTypeDef",
    "DeletePermissionVersionResponseTypeDef",
    "DeleteResourceShareRequestRequestTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionRequestRequestTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "DisassociateResourceShareRequestRequestTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetPermissionRequestRequestTypeDef",
    "GetPermissionResponseTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourceShareAssociationsRequestRequestTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "GetResourceShareInvitationsRequestRequestTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "GetResourceSharesRequestRequestTypeDef",
    "GetResourceSharesResponseTypeDef",
    "ListPendingInvitationResourcesRequestRequestTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListPermissionAssociationsRequestRequestTypeDef",
    "ListPermissionAssociationsResponseTypeDef",
    "ListPermissionVersionsRequestRequestTypeDef",
    "ListPermissionVersionsResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListPrincipalsRequestRequestTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListReplacePermissionAssociationsWorkRequestRequestTypeDef",
    "ListReplacePermissionAssociationsWorkResponseTypeDef",
    "ListResourceSharePermissionsRequestRequestTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "ListResourceTypesRequestRequestTypeDef",
    "ListResourceTypesResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrincipalTypeDef",
    "PromotePermissionCreatedFromPolicyRequestRequestTypeDef",
    "PromotePermissionCreatedFromPolicyResponseTypeDef",
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "RejectResourceShareInvitationRequestRequestTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "ReplacePermissionAssociationsRequestRequestTypeDef",
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
    "SetDefaultPermissionVersionRequestRequestTypeDef",
    "SetDefaultPermissionVersionResponseTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateResourceShareRequestRequestTypeDef",
    "UpdateResourceShareResponseTypeDef",
)

_RequiredAcceptResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalAcceptResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptResourceShareInvitationRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class AcceptResourceShareInvitationRequestRequestTypeDef(
    _RequiredAcceptResourceShareInvitationRequestRequestTypeDef,
    _OptionalAcceptResourceShareInvitationRequestRequestTypeDef,
):
    pass

AcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "AcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
    },
)
_OptionalAssociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateResourceSharePermissionRequestRequestTypeDef",
    {
        "replace": bool,
        "clientToken": str,
        "permissionVersion": int,
    },
    total=False,
)

class AssociateResourceSharePermissionRequestRequestTypeDef(
    _RequiredAssociateResourceSharePermissionRequestRequestTypeDef,
    _OptionalAssociateResourceSharePermissionRequestRequestTypeDef,
):
    pass

AssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "AssociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResourceShareRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalAssociateResourceShareRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateResourceShareRequestRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "clientToken": str,
        "sources": List[str],
    },
    total=False,
)

class AssociateResourceShareRequestRequestTypeDef(
    _RequiredAssociateResourceShareRequestRequestTypeDef,
    _OptionalAssociateResourceShareRequestRequestTypeDef,
):
    pass

AssociateResourceShareResponseTypeDef = TypedDict(
    "AssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedPermissionTypeDef = TypedDict(
    "AssociatedPermissionTypeDef",
    {
        "arn": str,
        "permissionVersion": str,
        "defaultVersion": bool,
        "resourceType": str,
        "status": str,
        "featureSet": PermissionFeatureSetType,
        "lastUpdatedTime": datetime,
        "resourceShareArn": str,
    },
    total=False,
)

_RequiredCreatePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionRequestRequestTypeDef",
    {
        "name": str,
        "resourceType": str,
        "policyTemplate": str,
    },
)
_OptionalCreatePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePermissionRequestRequestTypeDef(
    _RequiredCreatePermissionRequestRequestTypeDef, _OptionalCreatePermissionRequestRequestTypeDef
):
    pass

CreatePermissionResponseTypeDef = TypedDict(
    "CreatePermissionResponseTypeDef",
    {
        "permission": "ResourceSharePermissionSummaryTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePermissionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "policyTemplate": str,
    },
)
_OptionalCreatePermissionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionVersionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreatePermissionVersionRequestRequestTypeDef(
    _RequiredCreatePermissionVersionRequestRequestTypeDef,
    _OptionalCreatePermissionVersionRequestRequestTypeDef,
):
    pass

CreatePermissionVersionResponseTypeDef = TypedDict(
    "CreatePermissionVersionResponseTypeDef",
    {
        "permission": "ResourceSharePermissionDetailTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceShareRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourceShareRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateResourceShareRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourceShareRequestRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "tags": List["TagTypeDef"],
        "allowExternalPrincipals": bool,
        "clientToken": str,
        "permissionArns": List[str],
        "sources": List[str],
    },
    total=False,
)

class CreateResourceShareRequestRequestTypeDef(
    _RequiredCreateResourceShareRequestRequestTypeDef,
    _OptionalCreateResourceShareRequestRequestTypeDef,
):
    pass

CreateResourceShareResponseTypeDef = TypedDict(
    "CreateResourceShareResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionRequestRequestTypeDef",
    {
        "permissionArn": str,
    },
)
_OptionalDeletePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeletePermissionRequestRequestTypeDef(
    _RequiredDeletePermissionRequestRequestTypeDef, _OptionalDeletePermissionRequestRequestTypeDef
):
    pass

DeletePermissionResponseTypeDef = TypedDict(
    "DeletePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "permissionStatus": PermissionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePermissionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": int,
    },
)
_OptionalDeletePermissionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionVersionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeletePermissionVersionRequestRequestTypeDef(
    _RequiredDeletePermissionVersionRequestRequestTypeDef,
    _OptionalDeletePermissionVersionRequestRequestTypeDef,
):
    pass

DeletePermissionVersionResponseTypeDef = TypedDict(
    "DeletePermissionVersionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "permissionStatus": PermissionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourceShareRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalDeleteResourceShareRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourceShareRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteResourceShareRequestRequestTypeDef(
    _RequiredDeleteResourceShareRequestRequestTypeDef,
    _OptionalDeleteResourceShareRequestRequestTypeDef,
):
    pass

DeleteResourceShareResponseTypeDef = TypedDict(
    "DeleteResourceShareResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
    },
)
_OptionalDisassociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateResourceSharePermissionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisassociateResourceSharePermissionRequestRequestTypeDef(
    _RequiredDisassociateResourceSharePermissionRequestRequestTypeDef,
    _OptionalDisassociateResourceSharePermissionRequestRequestTypeDef,
):
    pass

DisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "DisassociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateResourceShareRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalDisassociateResourceShareRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateResourceShareRequestRequestTypeDef",
    {
        "resourceArns": List[str],
        "principals": List[str],
        "clientToken": str,
        "sources": List[str],
    },
    total=False,
)

class DisassociateResourceShareRequestRequestTypeDef(
    _RequiredDisassociateResourceShareRequestRequestTypeDef,
    _OptionalDisassociateResourceShareRequestRequestTypeDef,
):
    pass

DisassociateResourceShareResponseTypeDef = TypedDict(
    "DisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredGetPermissionRequestRequestTypeDef",
    {
        "permissionArn": str,
    },
)
_OptionalGetPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalGetPermissionRequestRequestTypeDef",
    {
        "permissionVersion": int,
    },
    total=False,
)

class GetPermissionRequestRequestTypeDef(
    _RequiredGetPermissionRequestRequestTypeDef, _OptionalGetPermissionRequestRequestTypeDef
):
    pass

GetPermissionResponseTypeDef = TypedDict(
    "GetPermissionResponseTypeDef",
    {
        "permission": "ResourceSharePermissionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesRequestRequestTypeDef",
    {
        "resourceArns": List[str],
    },
)
_OptionalGetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesRequestRequestTypeDef",
    {
        "principal": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetResourcePoliciesRequestRequestTypeDef(
    _RequiredGetResourcePoliciesRequestRequestTypeDef,
    _OptionalGetResourcePoliciesRequestRequestTypeDef,
):
    pass

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "policies": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceShareAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceShareAssociationsRequestRequestTypeDef",
    {
        "associationType": ResourceShareAssociationTypeType,
    },
)
_OptionalGetResourceShareAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceShareAssociationsRequestRequestTypeDef",
    {
        "resourceShareArns": List[str],
        "resourceArn": str,
        "principal": str,
        "associationStatus": ResourceShareAssociationStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetResourceShareAssociationsRequestRequestTypeDef(
    _RequiredGetResourceShareAssociationsRequestRequestTypeDef,
    _OptionalGetResourceShareAssociationsRequestRequestTypeDef,
):
    pass

GetResourceShareAssociationsResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceShareInvitationsRequestRequestTypeDef = TypedDict(
    "GetResourceShareInvitationsRequestRequestTypeDef",
    {
        "resourceShareInvitationArns": List[str],
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetResourceShareInvitationsResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List["ResourceShareInvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceSharesRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceSharesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalGetResourceSharesRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceSharesRequestRequestTypeDef",
    {
        "resourceShareArns": List[str],
        "resourceShareStatus": ResourceShareStatusType,
        "name": str,
        "tagFilters": List["TagFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "permissionArn": str,
        "permissionVersion": int,
    },
    total=False,
)

class GetResourceSharesRequestRequestTypeDef(
    _RequiredGetResourceSharesRequestRequestTypeDef, _OptionalGetResourceSharesRequestRequestTypeDef
):
    pass

GetResourceSharesResponseTypeDef = TypedDict(
    "GetResourceSharesResponseTypeDef",
    {
        "resourceShares": List["ResourceShareTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPendingInvitationResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListPendingInvitationResourcesRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalListPendingInvitationResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListPendingInvitationResourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "resourceRegionScope": ResourceRegionScopeFilterType,
    },
    total=False,
)

class ListPendingInvitationResourcesRequestRequestTypeDef(
    _RequiredListPendingInvitationResourcesRequestRequestTypeDef,
    _OptionalListPendingInvitationResourcesRequestRequestTypeDef,
):
    pass

ListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "ListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionAssociationsRequestRequestTypeDef = TypedDict(
    "ListPermissionAssociationsRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": int,
        "associationStatus": ResourceShareAssociationStatusType,
        "resourceType": str,
        "featureSet": PermissionFeatureSetType,
        "defaultVersion": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPermissionAssociationsResponseTypeDef = TypedDict(
    "ListPermissionAssociationsResponseTypeDef",
    {
        "permissions": List["AssociatedPermissionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionVersionsRequestRequestTypeDef",
    {
        "permissionArn": str,
    },
)
_OptionalListPermissionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionVersionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPermissionVersionsRequestRequestTypeDef(
    _RequiredListPermissionVersionsRequestRequestTypeDef,
    _OptionalListPermissionVersionsRequestRequestTypeDef,
):
    pass

ListPermissionVersionsResponseTypeDef = TypedDict(
    "ListPermissionVersionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "resourceType": str,
        "nextToken": str,
        "maxResults": int,
        "permissionType": PermissionTypeFilterType,
    },
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalsRequestRequestTypeDef = TypedDict(
    "_RequiredListPrincipalsRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalListPrincipalsRequestRequestTypeDef = TypedDict(
    "_OptionalListPrincipalsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "principals": List[str],
        "resourceType": str,
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPrincipalsRequestRequestTypeDef(
    _RequiredListPrincipalsRequestRequestTypeDef, _OptionalListPrincipalsRequestRequestTypeDef
):
    pass

ListPrincipalsResponseTypeDef = TypedDict(
    "ListPrincipalsResponseTypeDef",
    {
        "principals": List["PrincipalTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplacePermissionAssociationsWorkRequestRequestTypeDef = TypedDict(
    "ListReplacePermissionAssociationsWorkRequestRequestTypeDef",
    {
        "workIds": List[str],
        "status": ReplacePermissionAssociationsWorkStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListReplacePermissionAssociationsWorkResponseTypeDef = TypedDict(
    "ListReplacePermissionAssociationsWorkResponseTypeDef",
    {
        "replacePermissionAssociationsWorks": List["ReplacePermissionAssociationsWorkTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceSharePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceSharePermissionsRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalListResourceSharePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceSharePermissionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListResourceSharePermissionsRequestRequestTypeDef(
    _RequiredListResourceSharePermissionsRequestRequestTypeDef,
    _OptionalListResourceSharePermissionsRequestRequestTypeDef,
):
    pass

ListResourceSharePermissionsResponseTypeDef = TypedDict(
    "ListResourceSharePermissionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceTypesRequestRequestTypeDef = TypedDict(
    "ListResourceTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "resourceRegionScope": ResourceRegionScopeFilterType,
    },
    total=False,
)

ListResourceTypesResponseTypeDef = TypedDict(
    "ListResourceTypesResponseTypeDef",
    {
        "resourceTypes": List["ServiceNameAndResourceTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
    },
)
_OptionalListResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestRequestTypeDef",
    {
        "principal": str,
        "resourceType": str,
        "resourceArns": List[str],
        "resourceShareArns": List[str],
        "nextToken": str,
        "maxResults": int,
        "resourceRegionScope": ResourceRegionScopeFilterType,
    },
    total=False,
)

class ListResourcesRequestRequestTypeDef(
    _RequiredListResourcesRequestRequestTypeDef, _OptionalListResourcesRequestRequestTypeDef
):
    pass

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
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

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

_RequiredPromotePermissionCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPromotePermissionCreatedFromPolicyRequestRequestTypeDef",
    {
        "permissionArn": str,
        "name": str,
    },
)
_OptionalPromotePermissionCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPromotePermissionCreatedFromPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PromotePermissionCreatedFromPolicyRequestRequestTypeDef(
    _RequiredPromotePermissionCreatedFromPolicyRequestRequestTypeDef,
    _OptionalPromotePermissionCreatedFromPolicyRequestRequestTypeDef,
):
    pass

PromotePermissionCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromotePermissionCreatedFromPolicyResponseTypeDef",
    {
        "permission": "ResourceSharePermissionSummaryTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)

PromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredRejectResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
    },
)
_OptionalRejectResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalRejectResourceShareInvitationRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class RejectResourceShareInvitationRequestRequestTypeDef(
    _RequiredRejectResourceShareInvitationRequestRequestTypeDef,
    _OptionalRejectResourceShareInvitationRequestRequestTypeDef,
):
    pass

RejectResourceShareInvitationResponseTypeDef = TypedDict(
    "RejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplacePermissionAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredReplacePermissionAssociationsRequestRequestTypeDef",
    {
        "fromPermissionArn": str,
        "toPermissionArn": str,
    },
)
_OptionalReplacePermissionAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalReplacePermissionAssociationsRequestRequestTypeDef",
    {
        "fromPermissionVersion": int,
        "clientToken": str,
    },
    total=False,
)

class ReplacePermissionAssociationsRequestRequestTypeDef(
    _RequiredReplacePermissionAssociationsRequestRequestTypeDef,
    _OptionalReplacePermissionAssociationsRequestRequestTypeDef,
):
    pass

ReplacePermissionAssociationsResponseTypeDef = TypedDict(
    "ReplacePermissionAssociationsResponseTypeDef",
    {
        "replacePermissionAssociationsWork": "ReplacePermissionAssociationsWorkTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplacePermissionAssociationsWorkTypeDef = TypedDict(
    "ReplacePermissionAssociationsWorkTypeDef",
    {
        "id": str,
        "fromPermissionArn": str,
        "fromPermissionVersion": str,
        "toPermissionArn": str,
        "toPermissionVersion": str,
        "status": ReplacePermissionAssociationsWorkStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": ResourceShareAssociationTypeType,
        "status": ResourceShareAssociationStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ResourceShareInvitationTypeDef = TypedDict(
    "ResourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": ResourceShareInvitationStatusType,
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "receiverArn": str,
    },
    total=False,
)

ResourceSharePermissionDetailTypeDef = TypedDict(
    "ResourceSharePermissionDetailTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "permission": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "isResourceTypeDefault": bool,
        "permissionType": PermissionTypeType,
        "featureSet": PermissionFeatureSetType,
        "status": PermissionStatusType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ResourceSharePermissionSummaryTypeDef = TypedDict(
    "ResourceSharePermissionSummaryTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "isResourceTypeDefault": bool,
        "permissionType": PermissionTypeType,
        "featureSet": PermissionFeatureSetType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ResourceShareTypeDef = TypedDict(
    "ResourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": ResourceShareStatusType,
        "statusMessage": str,
        "tags": List["TagTypeDef"],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": ResourceShareFeatureSetType,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": ResourceStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "resourceRegionScope": ResourceRegionScopeType,
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

ServiceNameAndResourceTypeTypeDef = TypedDict(
    "ServiceNameAndResourceTypeTypeDef",
    {
        "resourceType": str,
        "serviceName": str,
        "resourceRegionScope": ResourceRegionScopeType,
    },
    total=False,
)

_RequiredSetDefaultPermissionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredSetDefaultPermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": int,
    },
)
_OptionalSetDefaultPermissionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalSetDefaultPermissionVersionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class SetDefaultPermissionVersionRequestRequestTypeDef(
    _RequiredSetDefaultPermissionVersionRequestRequestTypeDef,
    _OptionalSetDefaultPermissionVersionRequestRequestTypeDef,
):
    pass

SetDefaultPermissionVersionResponseTypeDef = TypedDict(
    "SetDefaultPermissionVersionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "tagKey": str,
        "tagValues": List[str],
    },
    total=False,
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArn": str,
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredUntagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestRequestTypeDef",
    {
        "tagKeys": List[str],
    },
)
_OptionalUntagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArn": str,
    },
    total=False,
)

class UntagResourceRequestRequestTypeDef(
    _RequiredUntagResourceRequestRequestTypeDef, _OptionalUntagResourceRequestRequestTypeDef
):
    pass

_RequiredUpdateResourceShareRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
_OptionalUpdateResourceShareRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceShareRequestRequestTypeDef",
    {
        "name": str,
        "allowExternalPrincipals": bool,
        "clientToken": str,
    },
    total=False,
)

class UpdateResourceShareRequestRequestTypeDef(
    _RequiredUpdateResourceShareRequestRequestTypeDef,
    _OptionalUpdateResourceShareRequestRequestTypeDef,
):
    pass

UpdateResourceShareResponseTypeDef = TypedDict(
    "UpdateResourceShareResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
