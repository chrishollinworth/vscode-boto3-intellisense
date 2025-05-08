"""
Type annotations for ram service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ram.client import RAMClient

    session = Session()
    client: RAMClient = session.client("ram")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetResourcePoliciesPaginator,
    GetResourceShareAssociationsPaginator,
    GetResourceShareInvitationsPaginator,
    GetResourceSharesPaginator,
    ListPrincipalsPaginator,
    ListResourcesPaginator,
)
from .type_defs import (
    AcceptResourceShareInvitationRequestTypeDef,
    AcceptResourceShareInvitationResponseTypeDef,
    AssociateResourceSharePermissionRequestTypeDef,
    AssociateResourceSharePermissionResponseTypeDef,
    AssociateResourceShareRequestTypeDef,
    AssociateResourceShareResponseTypeDef,
    CreatePermissionRequestTypeDef,
    CreatePermissionResponseTypeDef,
    CreatePermissionVersionRequestTypeDef,
    CreatePermissionVersionResponseTypeDef,
    CreateResourceShareRequestTypeDef,
    CreateResourceShareResponseTypeDef,
    DeletePermissionRequestTypeDef,
    DeletePermissionResponseTypeDef,
    DeletePermissionVersionRequestTypeDef,
    DeletePermissionVersionResponseTypeDef,
    DeleteResourceShareRequestTypeDef,
    DeleteResourceShareResponseTypeDef,
    DisassociateResourceSharePermissionRequestTypeDef,
    DisassociateResourceSharePermissionResponseTypeDef,
    DisassociateResourceShareRequestTypeDef,
    DisassociateResourceShareResponseTypeDef,
    EnableSharingWithAwsOrganizationResponseTypeDef,
    GetPermissionRequestTypeDef,
    GetPermissionResponseTypeDef,
    GetResourcePoliciesRequestTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourceShareAssociationsRequestTypeDef,
    GetResourceShareAssociationsResponseTypeDef,
    GetResourceShareInvitationsRequestTypeDef,
    GetResourceShareInvitationsResponseTypeDef,
    GetResourceSharesRequestTypeDef,
    GetResourceSharesResponseTypeDef,
    ListPendingInvitationResourcesRequestTypeDef,
    ListPendingInvitationResourcesResponseTypeDef,
    ListPermissionAssociationsRequestTypeDef,
    ListPermissionAssociationsResponseTypeDef,
    ListPermissionsRequestTypeDef,
    ListPermissionsResponseTypeDef,
    ListPermissionVersionsRequestTypeDef,
    ListPermissionVersionsResponseTypeDef,
    ListPrincipalsRequestTypeDef,
    ListPrincipalsResponseTypeDef,
    ListReplacePermissionAssociationsWorkRequestTypeDef,
    ListReplacePermissionAssociationsWorkResponseTypeDef,
    ListResourceSharePermissionsRequestTypeDef,
    ListResourceSharePermissionsResponseTypeDef,
    ListResourcesRequestTypeDef,
    ListResourcesResponseTypeDef,
    ListResourceTypesRequestTypeDef,
    ListResourceTypesResponseTypeDef,
    PromotePermissionCreatedFromPolicyRequestTypeDef,
    PromotePermissionCreatedFromPolicyResponseTypeDef,
    PromoteResourceShareCreatedFromPolicyRequestTypeDef,
    PromoteResourceShareCreatedFromPolicyResponseTypeDef,
    RejectResourceShareInvitationRequestTypeDef,
    RejectResourceShareInvitationResponseTypeDef,
    ReplacePermissionAssociationsRequestTypeDef,
    ReplacePermissionAssociationsResponseTypeDef,
    SetDefaultPermissionVersionRequestTypeDef,
    SetDefaultPermissionVersionResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateResourceShareRequestTypeDef,
    UpdateResourceShareResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("RAMClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InvalidClientTokenException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPolicyException: Type[BotocoreClientError]
    InvalidResourceTypeException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    MalformedArnException: Type[BotocoreClientError]
    MalformedPolicyTemplateException: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    PermissionAlreadyExistsException: Type[BotocoreClientError]
    PermissionLimitExceededException: Type[BotocoreClientError]
    PermissionVersionsLimitExceededException: Type[BotocoreClientError]
    ResourceArnNotFoundException: Type[BotocoreClientError]
    ResourceShareInvitationAlreadyAcceptedException: Type[BotocoreClientError]
    ResourceShareInvitationAlreadyRejectedException: Type[BotocoreClientError]
    ResourceShareInvitationArnNotFoundException: Type[BotocoreClientError]
    ResourceShareInvitationExpiredException: Type[BotocoreClientError]
    ResourceShareLimitExceededException: Type[BotocoreClientError]
    ServerInternalException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    TagPolicyViolationException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnknownResourceException: Type[BotocoreClientError]
    UnmatchedPolicyPermissionException: Type[BotocoreClientError]

class RAMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RAMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html#RAM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#generate_presigned_url)
        """

    def accept_resource_share_invitation(
        self, **kwargs: Unpack[AcceptResourceShareInvitationRequestTypeDef]
    ) -> AcceptResourceShareInvitationResponseTypeDef:
        """
        Accepts an invitation to a resource share from another Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/accept_resource_share_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#accept_resource_share_invitation)
        """

    def associate_resource_share(
        self, **kwargs: Unpack[AssociateResourceShareRequestTypeDef]
    ) -> AssociateResourceShareResponseTypeDef:
        """
        Adds the specified list of principals and list of resources to a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/associate_resource_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#associate_resource_share)
        """

    def associate_resource_share_permission(
        self, **kwargs: Unpack[AssociateResourceSharePermissionRequestTypeDef]
    ) -> AssociateResourceSharePermissionResponseTypeDef:
        """
        Adds or replaces the RAM permission for a resource type included in a resource
        share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/associate_resource_share_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#associate_resource_share_permission)
        """

    def create_permission(
        self, **kwargs: Unpack[CreatePermissionRequestTypeDef]
    ) -> CreatePermissionResponseTypeDef:
        """
        Creates a customer managed permission for a specified resource type that you
        can attach to resource shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#create_permission)
        """

    def create_permission_version(
        self, **kwargs: Unpack[CreatePermissionVersionRequestTypeDef]
    ) -> CreatePermissionVersionResponseTypeDef:
        """
        Creates a new version of the specified customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_permission_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#create_permission_version)
        """

    def create_resource_share(
        self, **kwargs: Unpack[CreateResourceShareRequestTypeDef]
    ) -> CreateResourceShareResponseTypeDef:
        """
        Creates a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/create_resource_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#create_resource_share)
        """

    def delete_permission(
        self, **kwargs: Unpack[DeletePermissionRequestTypeDef]
    ) -> DeletePermissionResponseTypeDef:
        """
        Deletes the specified customer managed permission in the Amazon Web Services
        Region in which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/delete_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#delete_permission)
        """

    def delete_permission_version(
        self, **kwargs: Unpack[DeletePermissionVersionRequestTypeDef]
    ) -> DeletePermissionVersionResponseTypeDef:
        """
        Deletes one version of a customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/delete_permission_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#delete_permission_version)
        """

    def delete_resource_share(
        self, **kwargs: Unpack[DeleteResourceShareRequestTypeDef]
    ) -> DeleteResourceShareResponseTypeDef:
        """
        Deletes the specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/delete_resource_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#delete_resource_share)
        """

    def disassociate_resource_share(
        self, **kwargs: Unpack[DisassociateResourceShareRequestTypeDef]
    ) -> DisassociateResourceShareResponseTypeDef:
        """
        Removes the specified principals or resources from participating in the
        specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/disassociate_resource_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#disassociate_resource_share)
        """

    def disassociate_resource_share_permission(
        self, **kwargs: Unpack[DisassociateResourceSharePermissionRequestTypeDef]
    ) -> DisassociateResourceSharePermissionResponseTypeDef:
        """
        Removes a managed permission from a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/disassociate_resource_share_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#disassociate_resource_share_permission)
        """

    def enable_sharing_with_aws_organization(
        self,
    ) -> EnableSharingWithAwsOrganizationResponseTypeDef:
        """
        Enables resource sharing within your organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/enable_sharing_with_aws_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#enable_sharing_with_aws_organization)
        """

    def get_permission(
        self, **kwargs: Unpack[GetPermissionRequestTypeDef]
    ) -> GetPermissionResponseTypeDef:
        """
        Retrieves the contents of a managed permission in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_permission)
        """

    def get_resource_policies(
        self, **kwargs: Unpack[GetResourcePoliciesRequestTypeDef]
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        Retrieves the resource policies for the specified resources that you own and
        have shared.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_resource_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_resource_policies)
        """

    def get_resource_share_associations(
        self, **kwargs: Unpack[GetResourceShareAssociationsRequestTypeDef]
    ) -> GetResourceShareAssociationsResponseTypeDef:
        """
        Retrieves the lists of resources and principals that associated for resource
        shares that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_resource_share_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_resource_share_associations)
        """

    def get_resource_share_invitations(
        self, **kwargs: Unpack[GetResourceShareInvitationsRequestTypeDef]
    ) -> GetResourceShareInvitationsResponseTypeDef:
        """
        Retrieves details about invitations that you have received for resource shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_resource_share_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_resource_share_invitations)
        """

    def get_resource_shares(
        self, **kwargs: Unpack[GetResourceSharesRequestTypeDef]
    ) -> GetResourceSharesResponseTypeDef:
        """
        Retrieves details about the resource shares that you own or that are shared
        with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_resource_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_resource_shares)
        """

    def list_pending_invitation_resources(
        self, **kwargs: Unpack[ListPendingInvitationResourcesRequestTypeDef]
    ) -> ListPendingInvitationResourcesResponseTypeDef:
        """
        Lists the resources in a resource share that is shared with you but for which
        the invitation is still <code>PENDING</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_pending_invitation_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_pending_invitation_resources)
        """

    def list_permission_associations(
        self, **kwargs: Unpack[ListPermissionAssociationsRequestTypeDef]
    ) -> ListPermissionAssociationsResponseTypeDef:
        """
        Lists information about the managed permission and its associations to any
        resource shares that use this managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_permission_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_permission_associations)
        """

    def list_permission_versions(
        self, **kwargs: Unpack[ListPermissionVersionsRequestTypeDef]
    ) -> ListPermissionVersionsResponseTypeDef:
        """
        Lists the available versions of the specified RAM permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_permission_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_permission_versions)
        """

    def list_permissions(
        self, **kwargs: Unpack[ListPermissionsRequestTypeDef]
    ) -> ListPermissionsResponseTypeDef:
        """
        Retrieves a list of available RAM permissions that you can use for the
        supported resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_permissions)
        """

    def list_principals(
        self, **kwargs: Unpack[ListPrincipalsRequestTypeDef]
    ) -> ListPrincipalsResponseTypeDef:
        """
        Lists the principals that you are sharing resources with or that are sharing
        resources with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_principals.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_principals)
        """

    def list_replace_permission_associations_work(
        self, **kwargs: Unpack[ListReplacePermissionAssociationsWorkRequestTypeDef]
    ) -> ListReplacePermissionAssociationsWorkResponseTypeDef:
        """
        Retrieves the current status of the asynchronous tasks performed by RAM when
        you perform the <a>ReplacePermissionAssociationsWork</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_replace_permission_associations_work.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_replace_permission_associations_work)
        """

    def list_resource_share_permissions(
        self, **kwargs: Unpack[ListResourceSharePermissionsRequestTypeDef]
    ) -> ListResourceSharePermissionsResponseTypeDef:
        """
        Lists the RAM permissions that are associated with a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_resource_share_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_resource_share_permissions)
        """

    def list_resource_types(
        self, **kwargs: Unpack[ListResourceTypesRequestTypeDef]
    ) -> ListResourceTypesResponseTypeDef:
        """
        Lists the resource types that can be shared by RAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_resource_types)
        """

    def list_resources(
        self, **kwargs: Unpack[ListResourcesRequestTypeDef]
    ) -> ListResourcesResponseTypeDef:
        """
        Lists the resources that you added to a resource share or the resources that
        are shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/list_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#list_resources)
        """

    def promote_permission_created_from_policy(
        self, **kwargs: Unpack[PromotePermissionCreatedFromPolicyRequestTypeDef]
    ) -> PromotePermissionCreatedFromPolicyResponseTypeDef:
        """
        When you attach a resource-based policy to a resource, RAM automatically
        creates a resource share of
        <code>featureSet</code>=<code>CREATED_FROM_POLICY</code> with a managed
        permission that has the same IAM permissions as the original resource-based
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/promote_permission_created_from_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#promote_permission_created_from_policy)
        """

    def promote_resource_share_created_from_policy(
        self, **kwargs: Unpack[PromoteResourceShareCreatedFromPolicyRequestTypeDef]
    ) -> PromoteResourceShareCreatedFromPolicyResponseTypeDef:
        """
        When you attach a resource-based policy to a resource, RAM automatically
        creates a resource share of
        <code>featureSet</code>=<code>CREATED_FROM_POLICY</code> with a managed
        permission that has the same IAM permissions as the original resource-based
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/promote_resource_share_created_from_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#promote_resource_share_created_from_policy)
        """

    def reject_resource_share_invitation(
        self, **kwargs: Unpack[RejectResourceShareInvitationRequestTypeDef]
    ) -> RejectResourceShareInvitationResponseTypeDef:
        """
        Rejects an invitation to a resource share from another Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/reject_resource_share_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#reject_resource_share_invitation)
        """

    def replace_permission_associations(
        self, **kwargs: Unpack[ReplacePermissionAssociationsRequestTypeDef]
    ) -> ReplacePermissionAssociationsResponseTypeDef:
        """
        Updates all resource shares that use a managed permission to a different
        managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/replace_permission_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#replace_permission_associations)
        """

    def set_default_permission_version(
        self, **kwargs: Unpack[SetDefaultPermissionVersionRequestTypeDef]
    ) -> SetDefaultPermissionVersionResponseTypeDef:
        """
        Designates the specified version number as the default version for the
        specified customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/set_default_permission_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#set_default_permission_version)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tag keys and values to a resource share or managed
        permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tag key and value pairs from the specified resource share
        or managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#untag_resource)
        """

    def update_resource_share(
        self, **kwargs: Unpack[UpdateResourceShareRequestTypeDef]
    ) -> UpdateResourceShareResponseTypeDef:
        """
        Modifies some of the properties of the specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/update_resource_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#update_resource_share)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_share_associations"]
    ) -> GetResourceShareAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_share_invitations"]
    ) -> GetResourceShareInvitationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_shares"]
    ) -> GetResourceSharesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_principals"]
    ) -> ListPrincipalsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resources"]
    ) -> ListResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/client/#get_paginator)
        """
