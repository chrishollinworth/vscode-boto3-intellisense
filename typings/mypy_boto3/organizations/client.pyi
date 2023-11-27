"""
Type annotations for organizations service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_organizations import OrganizationsClient

    client: OrganizationsClient = boto3.client("organizations")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ChildTypeType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    PolicyTypeType,
)
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
    AcceptHandshakeResponseTypeDef,
    CancelHandshakeResponseTypeDef,
    CreateAccountResponseTypeDef,
    CreateGovCloudAccountResponseTypeDef,
    CreateOrganizationalUnitResponseTypeDef,
    CreateOrganizationResponseTypeDef,
    CreatePolicyResponseTypeDef,
    DeclineHandshakeResponseTypeDef,
    DescribeAccountResponseTypeDef,
    DescribeCreateAccountStatusResponseTypeDef,
    DescribeEffectivePolicyResponseTypeDef,
    DescribeHandshakeResponseTypeDef,
    DescribeOrganizationalUnitResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribePolicyResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DisablePolicyTypeResponseTypeDef,
    EnableAllFeaturesResponseTypeDef,
    EnablePolicyTypeResponseTypeDef,
    HandshakeFilterTypeDef,
    HandshakePartyTypeDef,
    InviteAccountToOrganizationResponseTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    TagTypeDef,
    UpdateOrganizationalUnitResponseTypeDef,
    UpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OrganizationsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OrganizationsClient exceptions.
        """
    def accept_handshake(self, *, HandshakeId: str) -> AcceptHandshakeResponseTypeDef:
        """
        Sends a response to the originator of a handshake agreeing to the action
        proposed by the handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.accept_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#accept_handshake)
        """
    def attach_policy(self, *, PolicyId: str, TargetId: str) -> None:
        """
        Attaches a policy to a root, an organizational unit (OU), or an individual
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#attach_policy)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#can_paginate)
        """
    def cancel_handshake(self, *, HandshakeId: str) -> CancelHandshakeResponseTypeDef:
        """
        Cancels a handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#cancel_handshake)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#close)
        """
    def close_account(self, *, AccountId: str) -> None:
        """
        Closes an Amazon Web Services member account within an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.close_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#close_account)
        """
    def create_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: IAMUserAccessToBillingType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccountResponseTypeDef:
        """
        Creates an Amazon Web Services account that is automatically a member of the
        organization whose credentials made the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.create_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_account)
        """
    def create_gov_cloud_account(
        self,
        *,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: IAMUserAccessToBillingType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        This action is available if all of the following are true * You're authorized to
        create accounts in the Amazon Web Services GovCloud (US) Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_gov_cloud_account)
        """
    def create_organization(
        self, *, FeatureSet: OrganizationFeatureSetType = None
    ) -> CreateOrganizationResponseTypeDef:
        """
        Creates an Amazon Web Services organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.create_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_organization)
        """
    def create_organizational_unit(
        self, *, ParentId: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        Creates an organizational unit (OU) within a root or parent OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_organizational_unit)
        """
    def create_policy(
        self,
        *,
        Content: str,
        Description: str,
        Name: str,
        Type: PolicyTypeType,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates a policy of a specified type that you can attach to a root, an
        organizational unit (OU), or an individual Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#create_policy)
        """
    def decline_handshake(self, *, HandshakeId: str) -> DeclineHandshakeResponseTypeDef:
        """
        Declines a handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.decline_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#decline_handshake)
        """
    def delete_organization(self) -> None:
        """
        Deletes the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.delete_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_organization)
        """
    def delete_organizational_unit(self, *, OrganizationalUnitId: str) -> None:
        """
        Deletes an organizational unit (OU) from a root or another OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_organizational_unit)
        """
    def delete_policy(self, *, PolicyId: str) -> None:
        """
        Deletes the specified policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_policy)
        """
    def delete_resource_policy(self) -> None:
        """
        Deletes the resource policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#delete_resource_policy)
        """
    def deregister_delegated_administrator(self, *, AccountId: str, ServicePrincipal: str) -> None:
        """
        Removes the specified member Amazon Web Services account as a delegated
        administrator for the specified Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.deregister_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#deregister_delegated_administrator)
        """
    def describe_account(self, *, AccountId: str) -> DescribeAccountResponseTypeDef:
        """
        Retrieves Organizations-related information about the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_account)
        """
    def describe_create_account_status(
        self, *, CreateAccountRequestId: str
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        Retrieves the current status of an asynchronous request to create an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_create_account_status)
        """
    def describe_effective_policy(
        self, *, PolicyType: EffectivePolicyTypeType, TargetId: str = None
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        Returns the contents of the effective policy for specified policy type and
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_effective_policy)
        """
    def describe_handshake(self, *, HandshakeId: str) -> DescribeHandshakeResponseTypeDef:
        """
        Retrieves information about a previously requested handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_handshake)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_handshake)
        """
    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        Retrieves information about the organization that the user's account belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_organization)
        """
    def describe_organizational_unit(
        self, *, OrganizationalUnitId: str
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        Retrieves information about an organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_organizational_unit)
        """
    def describe_policy(self, *, PolicyId: str) -> DescribePolicyResponseTypeDef:
        """
        Retrieves information about a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_policy)
        """
    def describe_resource_policy(self) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves information about a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#describe_resource_policy)
        """
    def detach_policy(self, *, PolicyId: str, TargetId: str) -> None:
        """
        Detaches a policy from a target root, organizational unit (OU), or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#detach_policy)
        """
    def disable_aws_service_access(self, *, ServicePrincipal: str) -> None:
        """
        Disables the integration of an Amazon Web Services service (the service that is
        specified by `ServicePrincipal`) with Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#disable_aws_service_access)
        """
    def disable_policy_type(
        self, *, RootId: str, PolicyType: PolicyTypeType
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        Disables an organizational policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#disable_policy_type)
        """
    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        Enables all features in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.enable_all_features)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_all_features)
        """
    def enable_aws_service_access(self, *, ServicePrincipal: str) -> None:
        """
        Enables the integration of an Amazon Web Services service (the service that is
        specified by `ServicePrincipal`) with Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_aws_service_access)
        """
    def enable_policy_type(
        self, *, RootId: str, PolicyType: PolicyTypeType
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        Enables a policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.enable_policy_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#enable_policy_type)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#generate_presigned_url)
        """
    def invite_account_to_organization(
        self, *, Target: "HandshakePartyTypeDef", Notes: str = None, Tags: List["TagTypeDef"] = None
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        Sends an invitation to another account to join your organization as a member
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#invite_account_to_organization)
        """
    def leave_organization(self) -> None:
        """
        Removes a member account from its parent organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.leave_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#leave_organization)
        """
    def list_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        Lists all the accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_accounts)
        """
    def list_accounts_for_parent(
        self, *, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsForParentResponseTypeDef:
        """
        Lists the accounts in an organization that are contained by the specified target
        root or organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_accounts_for_parent)
        """
    def list_aws_service_access_for_organization(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        Returns a list of the Amazon Web Services services that you enabled to integrate
        with your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_aws_service_access_for_organization)
        """
    def list_children(
        self,
        *,
        ParentId: str,
        ChildType: ChildTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListChildrenResponseTypeDef:
        """
        Lists all of the organizational units (OUs) or accounts that are contained in
        the specified parent OU or root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_children)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_children)
        """
    def list_create_account_status(
        self,
        *,
        States: List[CreateAccountStateType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        Lists the account creation requests that match the specified status that is
        currently being tracked for the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_create_account_status)
        """
    def list_delegated_administrators(
        self, *, ServicePrincipal: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedAdministratorsResponseTypeDef:
        """
        Lists the Amazon Web Services accounts that are designated as delegated
        administrators in this organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_delegated_administrators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_delegated_administrators)
        """
    def list_delegated_services_for_account(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedServicesForAccountResponseTypeDef:
        """
        List the Amazon Web Services services for which the specified account is a
        delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_delegated_services_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_delegated_services_for_account)
        """
    def list_handshakes_for_account(
        self,
        *,
        Filter: "HandshakeFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        Lists the current handshakes that are associated with the account of the
        requesting user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_handshakes_for_account)
        """
    def list_handshakes_for_organization(
        self,
        *,
        Filter: "HandshakeFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        Lists the handshakes that are associated with the organization that the
        requesting user is part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_handshakes_for_organization)
        """
    def list_organizational_units_for_parent(
        self, *, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        Lists the organizational units (OUs) in a parent organizational unit or root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_organizational_units_for_parent)
        """
    def list_parents(
        self, *, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListParentsResponseTypeDef:
        """
        Lists the root or organizational units (OUs) that serve as the immediate parent
        of the specified child OU or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_parents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_parents)
        """
    def list_policies(
        self, *, Filter: PolicyTypeType, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        Retrieves the list of all policies in an organization of a specified type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_policies)
        """
    def list_policies_for_target(
        self,
        *,
        TargetId: str,
        Filter: PolicyTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        Lists the policies that are directly attached to the specified target root,
        organizational unit (OU), or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_policies_for_target)
        """
    def list_roots(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListRootsResponseTypeDef:
        """
        Lists the roots that are defined in the current organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_roots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_roots)
        """
    def list_tags_for_resource(
        self, *, ResourceId: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_tags_for_resource)
        """
    def list_targets_for_policy(
        self, *, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        Lists all the roots, organizational units (OUs), and accounts that the specified
        policy is attached to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#list_targets_for_policy)
        """
    def move_account(
        self, *, AccountId: str, SourceParentId: str, DestinationParentId: str
    ) -> None:
        """
        Moves an account from its current source parent root or organizational unit (OU)
        to the specified destination parent root or OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.move_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#move_account)
        """
    def put_resource_policy(
        self, *, Content: str, Tags: List["TagTypeDef"] = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#put_resource_policy)
        """
    def register_delegated_administrator(self, *, AccountId: str, ServicePrincipal: str) -> None:
        """
        Enables the specified member account to administer the Organizations features of
        the specified Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.register_delegated_administrator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#register_delegated_administrator)
        """
    def remove_account_from_organization(self, *, AccountId: str) -> None:
        """
        Removes the specified account from the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#remove_account_from_organization)
        """
    def tag_resource(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceId: str, TagKeys: List[str]) -> None:
        """
        Removes any tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#untag_resource)
        """
    def update_organizational_unit(
        self, *, OrganizationalUnitId: str, Name: str = None
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        Renames the specified organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#update_organizational_unit)
        """
    def update_policy(
        self, *, PolicyId: str, Name: str = None, Description: str = None, Content: str = None
    ) -> UpdatePolicyResponseTypeDef:
        """
        Updates an existing policy with a new name, description, or content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Client.update_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/client.html#update_policy)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> ListAWSServiceAccessForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listawsserviceaccessfororganizationpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> ListAccountsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listaccountsforparentpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_children"]) -> ListChildrenPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListChildren)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listchildrenpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> ListCreateAccountStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listcreateaccountstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_administrators"]
    ) -> ListDelegatedAdministratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedadministratorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_services_for_account"]
    ) -> ListDelegatedServicesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listdelegatedservicesforaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> ListHandshakesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesforaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> ListHandshakesForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listhandshakesfororganizationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> ListOrganizationalUnitsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listorganizationalunitsforparentpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_parents"]) -> ListParentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListParents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listparentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> ListPoliciesForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listpoliciesfortargetpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_roots"]) -> ListRootsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListRoots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listrootspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/paginators.html#listtargetsforpolicypaginator)
        """
