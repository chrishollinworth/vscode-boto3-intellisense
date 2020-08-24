"""
Main interface for ram service type definitions.

Usage::

    ```python
    from mypy_boto3_ram.type_defs import PrincipalTypeDef

    data: PrincipalTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "PrincipalTypeDef",
    "ResourceShareAssociationTypeDef",
    "ResourceShareInvitationTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "ResourceTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "TagTypeDef",
    "AcceptResourceShareInvitationResponseTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "CreateResourceShareResponseTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetPermissionResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "GetResourceSharesResponseTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "ListResourceTypesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "TagFilterTypeDef",
    "UpdateResourceShareResponseTypeDef",
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

ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
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
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
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
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List["TagTypeDef"],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
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
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ServiceNameAndResourceTypeTypeDef = TypedDict(
    "ServiceNameAndResourceTypeTypeDef", {"resourceType": str, "serviceName": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

AcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "AcceptResourceShareInvitationResponseTypeDef",
    {"resourceShareInvitation": "ResourceShareInvitationTypeDef", "clientToken": str},
    total=False,
)

AssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "AssociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)

AssociateResourceShareResponseTypeDef = TypedDict(
    "AssociateResourceShareResponseTypeDef",
    {"resourceShareAssociations": List["ResourceShareAssociationTypeDef"], "clientToken": str},
    total=False,
)

CreateResourceShareResponseTypeDef = TypedDict(
    "CreateResourceShareResponseTypeDef",
    {"resourceShare": "ResourceShareTypeDef", "clientToken": str},
    total=False,
)

DeleteResourceShareResponseTypeDef = TypedDict(
    "DeleteResourceShareResponseTypeDef", {"returnValue": bool, "clientToken": str}, total=False
)

DisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "DisassociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)

DisassociateResourceShareResponseTypeDef = TypedDict(
    "DisassociateResourceShareResponseTypeDef",
    {"resourceShareAssociations": List["ResourceShareAssociationTypeDef"], "clientToken": str},
    total=False,
)

EnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "EnableSharingWithAwsOrganizationResponseTypeDef", {"returnValue": bool}, total=False
)

GetPermissionResponseTypeDef = TypedDict(
    "GetPermissionResponseTypeDef",
    {"permission": "ResourceSharePermissionDetailTypeDef"},
    total=False,
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef", {"policies": List[str], "nextToken": str}, total=False
)

GetResourceShareAssociationsResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseTypeDef",
    {"resourceShareAssociations": List["ResourceShareAssociationTypeDef"], "nextToken": str},
    total=False,
)

GetResourceShareInvitationsResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseTypeDef",
    {"resourceShareInvitations": List["ResourceShareInvitationTypeDef"], "nextToken": str},
    total=False,
)

GetResourceSharesResponseTypeDef = TypedDict(
    "GetResourceSharesResponseTypeDef",
    {"resourceShares": List["ResourceShareTypeDef"], "nextToken": str},
    total=False,
)

ListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "ListPendingInvitationResourcesResponseTypeDef",
    {"resources": List["ResourceTypeDef"], "nextToken": str},
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {"permissions": List["ResourceSharePermissionSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListPrincipalsResponseTypeDef = TypedDict(
    "ListPrincipalsResponseTypeDef",
    {"principals": List["PrincipalTypeDef"], "nextToken": str},
    total=False,
)

ListResourceSharePermissionsResponseTypeDef = TypedDict(
    "ListResourceSharePermissionsResponseTypeDef",
    {"permissions": List["ResourceSharePermissionSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListResourceTypesResponseTypeDef = TypedDict(
    "ListResourceTypesResponseTypeDef",
    {"resourceTypes": List["ServiceNameAndResourceTypeTypeDef"], "nextToken": str},
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {"resources": List["ResourceTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef", {"returnValue": bool}, total=False
)

RejectResourceShareInvitationResponseTypeDef = TypedDict(
    "RejectResourceShareInvitationResponseTypeDef",
    {"resourceShareInvitation": "ResourceShareInvitationTypeDef", "clientToken": str},
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef", {"tagKey": str, "tagValues": List[str]}, total=False
)

UpdateResourceShareResponseTypeDef = TypedDict(
    "UpdateResourceShareResponseTypeDef",
    {"resourceShare": "ResourceShareTypeDef", "clientToken": str},
    total=False,
)
