# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for organizations service client

Usage::

    ```python
    import boto3
    from mypy_boto3_organizations import OrganizationsClient

    client: OrganizationsClient = boto3.client("organizations")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_organizations.paginator import (
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
from mypy_boto3_organizations.type_defs import (
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
    AccountAlreadyRegisteredException: Type[BotocoreClientError]
    AccountNotFoundException: Type[BotocoreClientError]
    AccountNotRegisteredException: Type[BotocoreClientError]
    AccountOwnerNotVerifiedException: Type[BotocoreClientError]
    AlreadyInOrganizationException: Type[BotocoreClientError]
    ChildNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
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
    RootNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SourceParentNotFoundException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedAPIEndpointException: Type[BotocoreClientError]


class OrganizationsClient:
    """
    [Organizations.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_handshake(self, HandshakeId: str) -> AcceptHandshakeResponseTypeDef:
        """
        [Client.accept_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.accept_handshake)
        """

    def attach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.attach_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.can_paginate)
        """

    def cancel_handshake(self, HandshakeId: str) -> CancelHandshakeResponseTypeDef:
        """
        [Client.cancel_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        """

    def create_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.create_account)
        """

    def create_gov_cloud_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        [Client.create_gov_cloud_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        """

    def create_organization(
        self, FeatureSet: Literal["ALL", "CONSOLIDATED_BILLING"] = None
    ) -> CreateOrganizationResponseTypeDef:
        """
        [Client.create_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.create_organization)
        """

    def create_organizational_unit(
        self, ParentId: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        [Client.create_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        """

    def create_policy(
        self,
        Content: str,
        Description: str,
        Name: str,
        Type: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.create_policy)
        """

    def decline_handshake(self, HandshakeId: str) -> DeclineHandshakeResponseTypeDef:
        """
        [Client.decline_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.decline_handshake)
        """

    def delete_organization(self) -> None:
        """
        [Client.delete_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.delete_organization)
        """

    def delete_organizational_unit(self, OrganizationalUnitId: str) -> None:
        """
        [Client.delete_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        """

    def delete_policy(self, PolicyId: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.delete_policy)
        """

    def deregister_delegated_administrator(self, AccountId: str, ServicePrincipal: str) -> None:
        """
        [Client.deregister_delegated_administrator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.deregister_delegated_administrator)
        """

    def describe_account(self, AccountId: str) -> DescribeAccountResponseTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_account)
        """

    def describe_create_account_status(
        self, CreateAccountRequestId: str
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        [Client.describe_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        """

    def describe_effective_policy(
        self,
        PolicyType: Literal["TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"],
        TargetId: str = None,
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        [Client.describe_effective_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        """

    def describe_handshake(self, HandshakeId: str) -> DescribeHandshakeResponseTypeDef:
        """
        [Client.describe_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_handshake)
        """

    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        [Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_organization)
        """

    def describe_organizational_unit(
        self, OrganizationalUnitId: str
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        [Client.describe_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        """

    def describe_policy(self, PolicyId: str) -> DescribePolicyResponseTypeDef:
        """
        [Client.describe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.describe_policy)
        """

    def detach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.detach_policy)
        """

    def disable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.disable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        """

    def disable_policy_type(
        self,
        RootId: str,
        PolicyType: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        [Client.disable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        """

    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        [Client.enable_all_features documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.enable_all_features)
        """

    def enable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.enable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        """

    def enable_policy_type(
        self,
        RootId: str,
        PolicyType: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        [Client.enable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.enable_policy_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        """

    def invite_account_to_organization(
        self, Target: "HandshakePartyTypeDef", Notes: str = None, Tags: List["TagTypeDef"] = None
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        [Client.invite_account_to_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        """

    def leave_organization(self) -> None:
        """
        [Client.leave_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.leave_organization)
        """

    def list_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_accounts)
        """

    def list_accounts_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsForParentResponseTypeDef:
        """
        [Client.list_accounts_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        """

    def list_aws_service_access_for_organization(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        [Client.list_aws_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        """

    def list_children(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListChildrenResponseTypeDef:
        """
        [Client.list_children documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_children)
        """

    def list_create_account_status(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        [Client.list_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        """

    def list_delegated_administrators(
        self, ServicePrincipal: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedAdministratorsResponseTypeDef:
        """
        [Client.list_delegated_administrators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_delegated_administrators)
        """

    def list_delegated_services_for_account(
        self, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDelegatedServicesForAccountResponseTypeDef:
        """
        [Client.list_delegated_services_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_delegated_services_for_account)
        """

    def list_handshakes_for_account(
        self, Filter: HandshakeFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        [Client.list_handshakes_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        """

    def list_handshakes_for_organization(
        self, Filter: HandshakeFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        [Client.list_handshakes_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        """

    def list_organizational_units_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        [Client.list_organizational_units_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        """

    def list_parents(
        self, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListParentsResponseTypeDef:
        """
        [Client.list_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_parents)
        """

    def list_policies(
        self,
        Filter: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_policies)
        """

    def list_policies_for_target(
        self,
        TargetId: str,
        Filter: Literal[
            "SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"
        ],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        [Client.list_policies_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        """

    def list_roots(self, NextToken: str = None, MaxResults: int = None) -> ListRootsResponseTypeDef:
        """
        [Client.list_roots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_roots)
        """

    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        """

    def move_account(self, AccountId: str, SourceParentId: str, DestinationParentId: str) -> None:
        """
        [Client.move_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.move_account)
        """

    def register_delegated_administrator(self, AccountId: str, ServicePrincipal: str) -> None:
        """
        [Client.register_delegated_administrator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.register_delegated_administrator)
        """

    def remove_account_from_organization(self, AccountId: str) -> None:
        """
        [Client.remove_account_from_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        """

    def tag_resource(self, ResourceId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.tag_resource)
        """

    def untag_resource(self, ResourceId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.untag_resource)
        """

    def update_organizational_unit(
        self, OrganizationalUnitId: str, Name: str = None
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        [Client.update_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        """

    def update_policy(
        self, PolicyId: str, Name: str = None, Description: str = None, Content: str = None
    ) -> UpdatePolicyResponseTypeDef:
        """
        [Client.update_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Client.update_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> ListAWSServiceAccessForOrganizationPaginator:
        """
        [Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> ListAccountsForParentPaginator:
        """
        [Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_children"]) -> ListChildrenPaginator:
        """
        [Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListChildren)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> ListCreateAccountStatusPaginator:
        """
        [Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_administrators"]
    ) -> ListDelegatedAdministratorsPaginator:
        """
        [Paginator.ListDelegatedAdministrators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedAdministrators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_services_for_account"]
    ) -> ListDelegatedServicesForAccountPaginator:
        """
        [Paginator.ListDelegatedServicesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListDelegatedServicesForAccount)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> ListHandshakesForAccountPaginator:
        """
        [Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> ListHandshakesForOrganizationPaginator:
        """
        [Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> ListOrganizationalUnitsForParentPaginator:
        """
        [Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parents"]) -> ListParentsPaginator:
        """
        [Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListParents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> ListPoliciesForTargetPaginator:
        """
        [Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_roots"]) -> ListRootsPaginator:
        """
        [Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListRoots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
        """
