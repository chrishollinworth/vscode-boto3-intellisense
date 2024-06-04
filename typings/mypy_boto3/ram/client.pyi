"""
Type annotations for ram service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ram import RAMClient

    client: RAMClient = boto3.client("ram")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    PermissionFeatureSetType,
    PermissionTypeFilterType,
    ReplacePermissionAssociationsWorkStatusType,
    ResourceOwnerType,
    ResourceRegionScopeFilterType,
    ResourceShareAssociationStatusType,
    ResourceShareAssociationTypeType,
    ResourceShareStatusType,
)
from .paginator import (
    GetResourcePoliciesPaginator,
    GetResourceShareAssociationsPaginator,
    GetResourceShareInvitationsPaginator,
    GetResourceSharesPaginator,
    ListPrincipalsPaginator,
    ListResourcesPaginator,
)
from .type_defs import (
    AcceptResourceShareInvitationResponseTypeDef,
    AssociateResourceSharePermissionResponseTypeDef,
    AssociateResourceShareResponseTypeDef,
    CreatePermissionResponseTypeDef,
    CreatePermissionVersionResponseTypeDef,
    CreateResourceShareResponseTypeDef,
    DeletePermissionResponseTypeDef,
    DeletePermissionVersionResponseTypeDef,
    DeleteResourceShareResponseTypeDef,
    DisassociateResourceSharePermissionResponseTypeDef,
    DisassociateResourceShareResponseTypeDef,
    EnableSharingWithAwsOrganizationResponseTypeDef,
    GetPermissionResponseTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourceShareAssociationsResponseTypeDef,
    GetResourceShareInvitationsResponseTypeDef,
    GetResourceSharesResponseTypeDef,
    ListPendingInvitationResourcesResponseTypeDef,
    ListPermissionAssociationsResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListPermissionVersionsResponseTypeDef,
    ListPrincipalsResponseTypeDef,
    ListReplacePermissionAssociationsWorkResponseTypeDef,
    ListResourceSharePermissionsResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListResourceTypesResponseTypeDef,
    PromotePermissionCreatedFromPolicyResponseTypeDef,
    PromoteResourceShareCreatedFromPolicyResponseTypeDef,
    RejectResourceShareInvitationResponseTypeDef,
    ReplacePermissionAssociationsResponseTypeDef,
    SetDefaultPermissionVersionResponseTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
    UpdateResourceShareResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RAMClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RAMClient exceptions.
        """

    def accept_resource_share_invitation(
        self, *, resourceShareInvitationArn: str, clientToken: str = None
    ) -> AcceptResourceShareInvitationResponseTypeDef:
        """
        Accepts an invitation to a resource share from another Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.accept_resource_share_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#accept_resource_share_invitation)
        """

    def associate_resource_share(
        self,
        *,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
        sources: List[str] = None
    ) -> AssociateResourceShareResponseTypeDef:
        """
        Adds the specified list of principals and list of resources to a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.associate_resource_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#associate_resource_share)
        """

    def associate_resource_share_permission(
        self,
        *,
        resourceShareArn: str,
        permissionArn: str,
        replace: bool = None,
        clientToken: str = None,
        permissionVersion: int = None
    ) -> AssociateResourceSharePermissionResponseTypeDef:
        """
        Adds or replaces the RAM permission for a resource type included in a resource
        share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.associate_resource_share_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#associate_resource_share_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#close)
        """

    def create_permission(
        self,
        *,
        name: str,
        resourceType: str,
        policyTemplate: str,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreatePermissionResponseTypeDef:
        """
        Creates a customer managed permission for a specified resource type that you can
        attach to resource shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.create_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#create_permission)
        """

    def create_permission_version(
        self, *, permissionArn: str, policyTemplate: str, clientToken: str = None
    ) -> CreatePermissionVersionResponseTypeDef:
        """
        Creates a new version of the specified customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.create_permission_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#create_permission_version)
        """

    def create_resource_share(
        self,
        *,
        name: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        tags: List["TagTypeDef"] = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
        permissionArns: List[str] = None,
        sources: List[str] = None
    ) -> CreateResourceShareResponseTypeDef:
        """
        Creates a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.create_resource_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#create_resource_share)
        """

    def delete_permission(
        self, *, permissionArn: str, clientToken: str = None
    ) -> DeletePermissionResponseTypeDef:
        """
        Deletes the specified customer managed permission in the Amazon Web Services
        Region in which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.delete_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#delete_permission)
        """

    def delete_permission_version(
        self, *, permissionArn: str, permissionVersion: int, clientToken: str = None
    ) -> DeletePermissionVersionResponseTypeDef:
        """
        Deletes one version of a customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.delete_permission_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#delete_permission_version)
        """

    def delete_resource_share(
        self, *, resourceShareArn: str, clientToken: str = None
    ) -> DeleteResourceShareResponseTypeDef:
        """
        Deletes the specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.delete_resource_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#delete_resource_share)
        """

    def disassociate_resource_share(
        self,
        *,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
        sources: List[str] = None
    ) -> DisassociateResourceShareResponseTypeDef:
        """
        Removes the specified principals or resources from participating in the
        specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.disassociate_resource_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#disassociate_resource_share)
        """

    def disassociate_resource_share_permission(
        self, *, resourceShareArn: str, permissionArn: str, clientToken: str = None
    ) -> DisassociateResourceSharePermissionResponseTypeDef:
        """
        Removes a managed permission from a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.disassociate_resource_share_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#disassociate_resource_share_permission)
        """

    def enable_sharing_with_aws_organization(
        self,
    ) -> EnableSharingWithAwsOrganizationResponseTypeDef:
        """
        Enables resource sharing within your organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.enable_sharing_with_aws_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#enable_sharing_with_aws_organization)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#generate_presigned_url)
        """

    def get_permission(
        self, *, permissionArn: str, permissionVersion: int = None
    ) -> GetPermissionResponseTypeDef:
        """
        Retrieves the contents of a managed permission in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.get_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#get_permission)
        """

    def get_resource_policies(
        self,
        *,
        resourceArns: List[str],
        principal: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        Retrieves the resource policies for the specified resources that you own and
        have shared.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.get_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#get_resource_policies)
        """

    def get_resource_share_associations(
        self,
        *,
        associationType: ResourceShareAssociationTypeType,
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: ResourceShareAssociationStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetResourceShareAssociationsResponseTypeDef:
        """
        Retrieves the lists of resources and principals that associated for resource
        shares that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.get_resource_share_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#get_resource_share_associations)
        """

    def get_resource_share_invitations(
        self,
        *,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetResourceShareInvitationsResponseTypeDef:
        """
        Retrieves details about invitations that you have received for resource shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.get_resource_share_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#get_resource_share_invitations)
        """

    def get_resource_shares(
        self,
        *,
        resourceOwner: ResourceOwnerType,
        resourceShareArns: List[str] = None,
        resourceShareStatus: ResourceShareStatusType = None,
        name: str = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        permissionArn: str = None,
        permissionVersion: int = None
    ) -> GetResourceSharesResponseTypeDef:
        """
        Retrieves details about the resource shares that you own or that are shared with
        you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.get_resource_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#get_resource_shares)
        """

    def list_pending_invitation_resources(
        self,
        *,
        resourceShareInvitationArn: str,
        nextToken: str = None,
        maxResults: int = None,
        resourceRegionScope: ResourceRegionScopeFilterType = None
    ) -> ListPendingInvitationResourcesResponseTypeDef:
        """
        Lists the resources in a resource share that is shared with you but for which
        the invitation is still `PENDING`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_pending_invitation_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_pending_invitation_resources)
        """

    def list_permission_associations(
        self,
        *,
        permissionArn: str = None,
        permissionVersion: int = None,
        associationStatus: ResourceShareAssociationStatusType = None,
        resourceType: str = None,
        featureSet: PermissionFeatureSetType = None,
        defaultVersion: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListPermissionAssociationsResponseTypeDef:
        """
        Lists information about the managed permission and its associations to any
        resource shares that use this managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_permission_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_permission_associations)
        """

    def list_permission_versions(
        self, *, permissionArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListPermissionVersionsResponseTypeDef:
        """
        Lists the available versions of the specified RAM permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_permission_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_permission_versions)
        """

    def list_permissions(
        self,
        *,
        resourceType: str = None,
        nextToken: str = None,
        maxResults: int = None,
        permissionType: PermissionTypeFilterType = None
    ) -> ListPermissionsResponseTypeDef:
        """
        Retrieves a list of available RAM permissions that you can use for the supported
        resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_permissions)
        """

    def list_principals(
        self,
        *,
        resourceOwner: ResourceOwnerType,
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListPrincipalsResponseTypeDef:
        """
        Lists the principals that you are sharing resources with or that are sharing
        resources with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_principals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_principals)
        """

    def list_replace_permission_associations_work(
        self,
        *,
        workIds: List[str] = None,
        status: ReplacePermissionAssociationsWorkStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListReplacePermissionAssociationsWorkResponseTypeDef:
        """
        Retrieves the current status of the asynchronous tasks performed by RAM when you
        perform the  ReplacePermissionAssociationsWork operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_replace_permission_associations_work)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_replace_permission_associations_work)
        """

    def list_resource_share_permissions(
        self, *, resourceShareArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListResourceSharePermissionsResponseTypeDef:
        """
        Lists the RAM permissions that are associated with a resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_resource_share_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_resource_share_permissions)
        """

    def list_resource_types(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        resourceRegionScope: ResourceRegionScopeFilterType = None
    ) -> ListResourceTypesResponseTypeDef:
        """
        Lists the resource types that can be shared by RAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_resource_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_resource_types)
        """

    def list_resources(
        self,
        *,
        resourceOwner: ResourceOwnerType,
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        resourceRegionScope: ResourceRegionScopeFilterType = None
    ) -> ListResourcesResponseTypeDef:
        """
        Lists the resources that you added to a resource share or the resources that are
        shared with you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#list_resources)
        """

    def promote_permission_created_from_policy(
        self, *, permissionArn: str, name: str, clientToken: str = None
    ) -> PromotePermissionCreatedFromPolicyResponseTypeDef:
        """
        When you attach a resource-based policy to a resource, RAM automatically creates
        a resource share of `featureSet`= `CREATED_FROM_POLICY` with a managed
        permission that has the same IAM permissions as the original resource-based
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.promote_permission_created_from_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#promote_permission_created_from_policy)
        """

    def promote_resource_share_created_from_policy(
        self, *, resourceShareArn: str
    ) -> PromoteResourceShareCreatedFromPolicyResponseTypeDef:
        """
        When you attach a resource-based policy to a resource, RAM automatically creates
        a resource share of `featureSet`= `CREATED_FROM_POLICY` with a managed
        permission that has the same IAM permissions as the original resource-based
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.promote_resource_share_created_from_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#promote_resource_share_created_from_policy)
        """

    def reject_resource_share_invitation(
        self, *, resourceShareInvitationArn: str, clientToken: str = None
    ) -> RejectResourceShareInvitationResponseTypeDef:
        """
        Rejects an invitation to a resource share from another Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.reject_resource_share_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#reject_resource_share_invitation)
        """

    def replace_permission_associations(
        self,
        *,
        fromPermissionArn: str,
        toPermissionArn: str,
        fromPermissionVersion: int = None,
        clientToken: str = None
    ) -> ReplacePermissionAssociationsResponseTypeDef:
        """
        Updates all resource shares that use a managed permission to a different managed
        permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.replace_permission_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#replace_permission_associations)
        """

    def set_default_permission_version(
        self, *, permissionArn: str, permissionVersion: int, clientToken: str = None
    ) -> SetDefaultPermissionVersionResponseTypeDef:
        """
        Designates the specified version number as the default version for the specified
        customer managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.set_default_permission_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#set_default_permission_version)
        """

    def tag_resource(
        self, *, tags: List["TagTypeDef"], resourceShareArn: str = None, resourceArn: str = None
    ) -> Dict[str, Any]:
        """
        Adds the specified tag keys and values to a resource share or managed
        permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#tag_resource)
        """

    def untag_resource(
        self, *, tagKeys: List[str], resourceShareArn: str = None, resourceArn: str = None
    ) -> Dict[str, Any]:
        """
        Removes the specified tag key and value pairs from the specified resource share
        or managed permission.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#untag_resource)
        """

    def update_resource_share(
        self,
        *,
        resourceShareArn: str,
        name: str = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None
    ) -> UpdateResourceShareResponseTypeDef:
        """
        Modifies some of the properties of the specified resource share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Client.update_resource_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/client.html#update_resource_share)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.GetResourcePolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#getresourcepoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_share_associations"]
    ) -> GetResourceShareAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#getresourceshareassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_share_invitations"]
    ) -> GetResourceShareInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#getresourceshareinvitationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_shares"]
    ) -> GetResourceSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.GetResourceShares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#getresourcesharespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_principals"]) -> ListPrincipalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.ListPrincipals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#listprincipalspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ram.html#RAM.Paginator.ListResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/paginators.html#listresourcespaginator)
        """
