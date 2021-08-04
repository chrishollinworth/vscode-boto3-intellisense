"""
Type annotations for ram service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/literals.html)

Usage::

    ```python
    from mypy_boto3_ram.literals import GetResourcePoliciesPaginatorName

    data: GetResourcePoliciesPaginatorName = "get_resource_policies"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetResourcePoliciesPaginatorName",
    "GetResourceShareAssociationsPaginatorName",
    "GetResourceShareInvitationsPaginatorName",
    "GetResourceSharesPaginatorName",
    "ListPrincipalsPaginatorName",
    "ListResourcesPaginatorName",
    "ResourceOwnerType",
    "ResourceShareAssociationStatusType",
    "ResourceShareAssociationTypeType",
    "ResourceShareFeatureSetType",
    "ResourceShareInvitationStatusType",
    "ResourceShareStatusType",
    "ResourceStatusType",
)

GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
GetResourceShareAssociationsPaginatorName = Literal["get_resource_share_associations"]
GetResourceShareInvitationsPaginatorName = Literal["get_resource_share_invitations"]
GetResourceSharesPaginatorName = Literal["get_resource_shares"]
ListPrincipalsPaginatorName = Literal["list_principals"]
ListResourcesPaginatorName = Literal["list_resources"]
ResourceOwnerType = Literal["OTHER-ACCOUNTS", "SELF"]
ResourceShareAssociationStatusType = Literal[
    "ASSOCIATED", "ASSOCIATING", "DISASSOCIATED", "DISASSOCIATING", "FAILED"
]
ResourceShareAssociationTypeType = Literal["PRINCIPAL", "RESOURCE"]
ResourceShareFeatureSetType = Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"]
ResourceShareInvitationStatusType = Literal["ACCEPTED", "EXPIRED", "PENDING", "REJECTED"]
ResourceShareStatusType = Literal["ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
ResourceStatusType = Literal[
    "AVAILABLE", "LIMIT_EXCEEDED", "PENDING", "UNAVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE"
]
