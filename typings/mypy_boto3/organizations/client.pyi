"""
Type annotations for organizations service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_organizations.client import OrganizationsClient

    session = Session()
    client: OrganizationsClient = session.client("organizations")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListAWSServiceAccessForOrganizationPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListDelegatedAdministratorsPaginator,
    ListDelegatedServicesForAccountPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
)
from .type_defs import (
    AcceptHandshakeRequestTypeDef,
    AcceptHandshakeResponseTypeDef,
    AttachPolicyRequestTypeDef,
    CancelHandshakeRequestTypeDef,
    CancelHandshakeResponseTypeDef,
    CloseAccountRequestTypeDef,
    CreateAccountRequestTypeDef,
    CreateAccountResponseTypeDef,
    CreateGovCloudAccountRequestTypeDef,
    CreateGovCloudAccountResponseTypeDef,
    CreateOrganizationalUnitRequestTypeDef,
    CreateOrganizationalUnitResponseTypeDef,
    CreateOrganizationRequestTypeDef,
    CreateOrganizationResponseTypeDef,
    CreatePolicyRequestTypeDef,
    CreatePolicyResponseTypeDef,
    DeclineHandshakeRequestTypeDef,
    DeclineHandshakeResponseTypeDef,
    DeleteOrganizationalUnitRequestTypeDef,
    DeletePolicyRequestTypeDef,
    DeregisterDelegatedAdministratorRequestTypeDef,
    DescribeAccountRequestTypeDef,
    DescribeAccountResponseTypeDef,
    DescribeCreateAccountStatusRequestTypeDef,
    DescribeCreateAccountStatusResponseTypeDef,
    DescribeEffectivePolicyRequestTypeDef,
    DescribeEffectivePolicyResponseTypeDef,
    DescribeHandshakeRequestTypeDef,
    DescribeHandshakeResponseTypeDef,
    DescribeOrganizationalUnitRequestTypeDef,
    DescribeOrganizationalUnitResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribePolicyRequestTypeDef,
    DescribePolicyResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DetachPolicyRequestTypeDef,
    DisableAWSServiceAccessRequestTypeDef,
    DisablePolicyTypeRequestTypeDef,
    DisablePolicyTypeResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableAllFeaturesResponseTypeDef,
    EnableAWSServiceAccessRequestTypeDef,
    EnablePolicyTypeRequestTypeDef,
    EnablePolicyTypeResponseTypeDef,
    InviteAccountToOrganizationRequestTypeDef,
    InviteAccountToOrganizationResponseTypeDef,
    ListAccountsForParentRequestTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsRequestTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationRequestTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenRequestTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusRequestTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsRequestTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountRequestTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountRequestTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationRequestTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentRequestTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsRequestTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetRequestTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsRequestTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyRequestTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    MoveAccountRequestTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RegisterDelegatedAdministratorRequestTypeDef,
    RemoveAccountFromOrganizationRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateOrganizationalUnitRequestTypeDef,
    UpdateOrganizationalUnitResponseTypeDef,
    UpdatePolicyRequestTypeDef,
    UpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("OrganizationsClient",)

class Exceptions(BaseClientExceptions):
    AWSOrganizationsNotInUseException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    AccountAlreadyClosedException: Type[BotocoreClientError]
    AccountAlreadyRegisteredException: Type[BotocoreClientError]
    AccountNotFoundException: Type[BotocoreClientError]
    AccountNotRegisteredException: Type[BotocoreClientError]
    AccountOwnerNotVerifiedException: Type[BotocoreClientError]
    AlreadyInOrganizationException: Type[BotocoreClientError]
    ChildNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    CreateAccountStatusNotFoundException: Type[BotocoreClientError]
    DestinationParentNotFoundException: Type[BotocoreClientError]
    DuplicateAccountException: Type[BotocoreClientError]
    DuplicateHandshakeException: Type[BotocoreClientError]
    DuplicateOrganizationalUnitException: Type[BotocoreClientError]
    DuplicatePolicyAttachmentException: Type[BotocoreClientError]
    DuplicatePolicyException: Type[BotocoreClientError]
    EffectivePolicyNotFoundException: Type[BotocoreClientError]
    FinalizingOrganizationException: Type[BotocoreClientError]
    HandshakeAlreadyInStateException: Type[BotocoreClientError]
    HandshakeConstraintViolationException: Type[BotocoreClientError]
    HandshakeNotFoundException: Type[BotocoreClientError]
    InvalidHandshakeTransitionException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    MasterCannotLeaveOrganizationException: Type[BotocoreClientError]
    OrganizationNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotFoundException: Type[BotocoreClientError]
    ParentNotFoundException: Type[BotocoreClientError]
    PolicyChangesInProgressException: Type[BotocoreClientError]
    PolicyInUseException: Type[BotocoreClientError]
    PolicyNotAttachedException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]
    PolicyTypeAlreadyEnabledException: Type[BotocoreClientError]
    PolicyTypeNotAvailableForOrganizationException: Type[BotocoreClientError]
    PolicyTypeNotEnabledException: Type[BotocoreClientError]
    ResourcePolicyNotFoundException: Type[BotocoreClientError]
    RootNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SourceParentNotFoundException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedAPIEndpointException: Type[BotocoreClientError]

class OrganizationsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OrganizationsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#generate_presigned_url)
        """

    def accept_handshake(
        self, **kwargs: Unpack[AcceptHandshakeRequestTypeDef]
    ) -> AcceptHandshakeResponseTypeDef:
        """
        Sends a response to the originator of a handshake agreeing to the action
        proposed by the handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/accept_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#accept_handshake)
        """

    def attach_policy(
        self, **kwargs: Unpack[AttachPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a policy to a root, an organizational unit (OU), or an individual
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/attach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#attach_policy)
        """

    def cancel_handshake(
        self, **kwargs: Unpack[CancelHandshakeRequestTypeDef]
    ) -> CancelHandshakeResponseTypeDef:
        """
        Cancels a handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/cancel_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#cancel_handshake)
        """

    def close_account(
        self, **kwargs: Unpack[CloseAccountRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Closes an Amazon Web Services member account within an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/close_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#close_account)
        """

    def create_account(
        self, **kwargs: Unpack[CreateAccountRequestTypeDef]
    ) -> CreateAccountResponseTypeDef:
        """
        Creates an Amazon Web Services account that is automatically a member of the
        organization whose credentials made the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/create_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_account)
        """

    def create_gov_cloud_account(
        self, **kwargs: Unpack[CreateGovCloudAccountRequestTypeDef]
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        This action is available if all of the following are true:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/create_gov_cloud_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_gov_cloud_account)
        """

    def create_organization(
        self, **kwargs: Unpack[CreateOrganizationRequestTypeDef]
    ) -> CreateOrganizationResponseTypeDef:
        """
        Creates an Amazon Web Services organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/create_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_organization)
        """

    def create_organizational_unit(
        self, **kwargs: Unpack[CreateOrganizationalUnitRequestTypeDef]
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        Creates an organizational unit (OU) within a root or parent OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/create_organizational_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_organizational_unit)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyRequestTypeDef]
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates a policy of a specified type that you can attach to a root, an
        organizational unit (OU), or an individual Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_policy)
        """

    def decline_handshake(
        self, **kwargs: Unpack[DeclineHandshakeRequestTypeDef]
    ) -> DeclineHandshakeResponseTypeDef:
        """
        Declines a handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/decline_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#decline_handshake)
        """

    def delete_organization(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/delete_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_organization)
        """

    def delete_organizational_unit(
        self, **kwargs: Unpack[DeleteOrganizationalUnitRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an organizational unit (OU) from a root or another OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/delete_organizational_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_organizational_unit)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_policy)
        """

    def delete_resource_policy(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_resource_policy)
        """

    def deregister_delegated_administrator(
        self, **kwargs: Unpack[DeregisterDelegatedAdministratorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified member Amazon Web Services account as a delegated
        administrator for the specified Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/deregister_delegated_administrator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#deregister_delegated_administrator)
        """

    def describe_account(
        self, **kwargs: Unpack[DescribeAccountRequestTypeDef]
    ) -> DescribeAccountResponseTypeDef:
        """
        Retrieves Organizations-related information about the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_account)
        """

    def describe_create_account_status(
        self, **kwargs: Unpack[DescribeCreateAccountStatusRequestTypeDef]
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        Retrieves the current status of an asynchronous request to create an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_create_account_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_create_account_status)
        """

    def describe_effective_policy(
        self, **kwargs: Unpack[DescribeEffectivePolicyRequestTypeDef]
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        Returns the contents of the effective policy for specified policy type and
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_effective_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_effective_policy)
        """

    def describe_handshake(
        self, **kwargs: Unpack[DescribeHandshakeRequestTypeDef]
    ) -> DescribeHandshakeResponseTypeDef:
        """
        Retrieves information about a previously requested handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_handshake)
        """

    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        Retrieves information about the organization that the user's account belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_organization)
        """

    def describe_organizational_unit(
        self, **kwargs: Unpack[DescribeOrganizationalUnitRequestTypeDef]
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        Retrieves information about an organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_organizational_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_organizational_unit)
        """

    def describe_policy(
        self, **kwargs: Unpack[DescribePolicyRequestTypeDef]
    ) -> DescribePolicyResponseTypeDef:
        """
        Retrieves information about a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_policy)
        """

    def describe_resource_policy(self) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves information about a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/describe_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_resource_policy)
        """

    def detach_policy(
        self, **kwargs: Unpack[DetachPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a policy from a target root, organizational unit (OU), or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/detach_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#detach_policy)
        """

    def disable_aws_service_access(
        self, **kwargs: Unpack[DisableAWSServiceAccessRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables the integration of an Amazon Web Services service (the service that is
        specified by <code>ServicePrincipal</code>) with Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/disable_aws_service_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#disable_aws_service_access)
        """

    def disable_policy_type(
        self, **kwargs: Unpack[DisablePolicyTypeRequestTypeDef]
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        Disables an organizational policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/disable_policy_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#disable_policy_type)
        """

    def enable_aws_service_access(
        self, **kwargs: Unpack[EnableAWSServiceAccessRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Provides an Amazon Web Services service (the service that is specified by
        <code>ServicePrincipal</code>) with permissions to view the structure of an
        organization, create a <a
        href="https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html">service-linked
        role</a> in all th...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/enable_aws_service_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_aws_service_access)
        """

    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        Enables all features in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/enable_all_features.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_all_features)
        """

    def enable_policy_type(
        self, **kwargs: Unpack[EnablePolicyTypeRequestTypeDef]
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        Enables a policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/enable_policy_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_policy_type)
        """

    def invite_account_to_organization(
        self, **kwargs: Unpack[InviteAccountToOrganizationRequestTypeDef]
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        Sends an invitation to another account to join your organization as a member
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/invite_account_to_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#invite_account_to_organization)
        """

    def leave_organization(self) -> EmptyResponseMetadataTypeDef:
        """
        Removes a member account from its parent organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/leave_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#leave_organization)
        """

    def list_aws_service_access_for_organization(
        self, **kwargs: Unpack[ListAWSServiceAccessForOrganizationRequestTypeDef]
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        Returns a list of the Amazon Web Services services that you enabled to
        integrate with your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_aws_service_access_for_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_aws_service_access_for_organization)
        """

    def list_accounts(
        self, **kwargs: Unpack[ListAccountsRequestTypeDef]
    ) -> ListAccountsResponseTypeDef:
        """
        Lists all the accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_accounts)
        """

    def list_accounts_for_parent(
        self, **kwargs: Unpack[ListAccountsForParentRequestTypeDef]
    ) -> ListAccountsForParentResponseTypeDef:
        """
        Lists the accounts in an organization that are contained by the specified
        target root or organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_accounts_for_parent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_accounts_for_parent)
        """

    def list_children(
        self, **kwargs: Unpack[ListChildrenRequestTypeDef]
    ) -> ListChildrenResponseTypeDef:
        """
        Lists all of the organizational units (OUs) or accounts that are contained in
        the specified parent OU or root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_children.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_children)
        """

    def list_create_account_status(
        self, **kwargs: Unpack[ListCreateAccountStatusRequestTypeDef]
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        Lists the account creation requests that match the specified status that is
        currently being tracked for the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_create_account_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_create_account_status)
        """

    def list_delegated_administrators(
        self, **kwargs: Unpack[ListDelegatedAdministratorsRequestTypeDef]
    ) -> ListDelegatedAdministratorsResponseTypeDef:
        """
        Lists the Amazon Web Services accounts that are designated as delegated
        administrators in this organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_delegated_administrators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_delegated_administrators)
        """

    def list_delegated_services_for_account(
        self, **kwargs: Unpack[ListDelegatedServicesForAccountRequestTypeDef]
    ) -> ListDelegatedServicesForAccountResponseTypeDef:
        """
        List the Amazon Web Services services for which the specified account is a
        delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_delegated_services_for_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_delegated_services_for_account)
        """

    def list_handshakes_for_account(
        self, **kwargs: Unpack[ListHandshakesForAccountRequestTypeDef]
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        Lists the current handshakes that are associated with the account of the
        requesting user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_handshakes_for_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_handshakes_for_account)
        """

    def list_handshakes_for_organization(
        self, **kwargs: Unpack[ListHandshakesForOrganizationRequestTypeDef]
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        Lists the handshakes that are associated with the organization that the
        requesting user is part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_handshakes_for_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_handshakes_for_organization)
        """

    def list_organizational_units_for_parent(
        self, **kwargs: Unpack[ListOrganizationalUnitsForParentRequestTypeDef]
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        Lists the organizational units (OUs) in a parent organizational unit or root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_organizational_units_for_parent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_organizational_units_for_parent)
        """

    def list_parents(
        self, **kwargs: Unpack[ListParentsRequestTypeDef]
    ) -> ListParentsResponseTypeDef:
        """
        Lists the root or organizational units (OUs) that serve as the immediate parent
        of the specified child OU or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_parents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_parents)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Retrieves the list of all policies in an organization of a specified type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_policies)
        """

    def list_policies_for_target(
        self, **kwargs: Unpack[ListPoliciesForTargetRequestTypeDef]
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        Lists the policies that are directly attached to the specified target root,
        organizational unit (OU), or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_policies_for_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_policies_for_target)
        """

    def list_roots(self, **kwargs: Unpack[ListRootsRequestTypeDef]) -> ListRootsResponseTypeDef:
        """
        Lists the roots that are defined in the current organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_roots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_roots)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, **kwargs: Unpack[ListTargetsForPolicyRequestTypeDef]
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        Lists all the roots, organizational units (OUs), and accounts that the
        specified policy is attached to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/list_targets_for_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_targets_for_policy)
        """

    def move_account(
        self, **kwargs: Unpack[MoveAccountRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Moves an account from its current source parent root or organizational unit
        (OU) to the specified destination parent root or OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/move_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#move_account)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#put_resource_policy)
        """

    def register_delegated_administrator(
        self, **kwargs: Unpack[RegisterDelegatedAdministratorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the specified member account to administer the Organizations features
        of the specified Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/register_delegated_administrator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#register_delegated_administrator)
        """

    def remove_account_from_organization(
        self, **kwargs: Unpack[RemoveAccountFromOrganizationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified account from the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/remove_account_from_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#remove_account_from_organization)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes any tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#untag_resource)
        """

    def update_organizational_unit(
        self, **kwargs: Unpack[UpdateOrganizationalUnitRequestTypeDef]
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        Renames the specified organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/update_organizational_unit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#update_organizational_unit)
        """

    def update_policy(
        self, **kwargs: Unpack[UpdatePolicyRequestTypeDef]
    ) -> UpdatePolicyResponseTypeDef:
        """
        Updates an existing policy with a new name, description, or content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/update_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#update_policy)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> ListAWSServiceAccessForOrganizationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> ListAccountsForParentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accounts"]
    ) -> ListAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_children"]
    ) -> ListChildrenPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_create_account_status"]
    ) -> ListCreateAccountStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_delegated_administrators"]
    ) -> ListDelegatedAdministratorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_delegated_services_for_account"]
    ) -> ListDelegatedServicesForAccountPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> ListHandshakesForAccountPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> ListHandshakesForOrganizationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> ListOrganizationalUnitsForParentPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_parents"]
    ) -> ListParentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies_for_target"]
    ) -> ListPoliciesForTargetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_roots"]
    ) -> ListRootsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """
