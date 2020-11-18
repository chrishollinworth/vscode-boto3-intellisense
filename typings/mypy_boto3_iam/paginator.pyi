# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for iam service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMClient
    from mypy_boto3_iam.paginator import (
        GetAccountAuthorizationDetailsPaginator,
        GetGroupPaginator,
        ListAccessKeysPaginator,
        ListAccountAliasesPaginator,
        ListAttachedGroupPoliciesPaginator,
        ListAttachedRolePoliciesPaginator,
        ListAttachedUserPoliciesPaginator,
        ListEntitiesForPolicyPaginator,
        ListGroupPoliciesPaginator,
        ListGroupsPaginator,
        ListGroupsForUserPaginator,
        ListInstanceProfilesPaginator,
        ListInstanceProfilesForRolePaginator,
        ListMFADevicesPaginator,
        ListPoliciesPaginator,
        ListPolicyVersionsPaginator,
        ListRolePoliciesPaginator,
        ListRolesPaginator,
        ListSSHPublicKeysPaginator,
        ListServerCertificatesPaginator,
        ListSigningCertificatesPaginator,
        ListUserPoliciesPaginator,
        ListUsersPaginator,
        ListVirtualMFADevicesPaginator,
        SimulateCustomPolicyPaginator,
        SimulatePrincipalPolicyPaginator,
    )

    client: IAMClient = boto3.client("iam")

    get_account_authorization_details_paginator: GetAccountAuthorizationDetailsPaginator = client.get_paginator("get_account_authorization_details")
    get_group_paginator: GetGroupPaginator = client.get_paginator("get_group")
    list_access_keys_paginator: ListAccessKeysPaginator = client.get_paginator("list_access_keys")
    list_account_aliases_paginator: ListAccountAliasesPaginator = client.get_paginator("list_account_aliases")
    list_attached_group_policies_paginator: ListAttachedGroupPoliciesPaginator = client.get_paginator("list_attached_group_policies")
    list_attached_role_policies_paginator: ListAttachedRolePoliciesPaginator = client.get_paginator("list_attached_role_policies")
    list_attached_user_policies_paginator: ListAttachedUserPoliciesPaginator = client.get_paginator("list_attached_user_policies")
    list_entities_for_policy_paginator: ListEntitiesForPolicyPaginator = client.get_paginator("list_entities_for_policy")
    list_group_policies_paginator: ListGroupPoliciesPaginator = client.get_paginator("list_group_policies")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_groups_for_user_paginator: ListGroupsForUserPaginator = client.get_paginator("list_groups_for_user")
    list_instance_profiles_paginator: ListInstanceProfilesPaginator = client.get_paginator("list_instance_profiles")
    list_instance_profiles_for_role_paginator: ListInstanceProfilesForRolePaginator = client.get_paginator("list_instance_profiles_for_role")
    list_mfa_devices_paginator: ListMFADevicesPaginator = client.get_paginator("list_mfa_devices")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_versions_paginator: ListPolicyVersionsPaginator = client.get_paginator("list_policy_versions")
    list_role_policies_paginator: ListRolePoliciesPaginator = client.get_paginator("list_role_policies")
    list_roles_paginator: ListRolesPaginator = client.get_paginator("list_roles")
    list_ssh_public_keys_paginator: ListSSHPublicKeysPaginator = client.get_paginator("list_ssh_public_keys")
    list_server_certificates_paginator: ListServerCertificatesPaginator = client.get_paginator("list_server_certificates")
    list_signing_certificates_paginator: ListSigningCertificatesPaginator = client.get_paginator("list_signing_certificates")
    list_user_policies_paginator: ListUserPoliciesPaginator = client.get_paginator("list_user_policies")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_virtual_mfa_devices_paginator: ListVirtualMFADevicesPaginator = client.get_paginator("list_virtual_mfa_devices")
    simulate_custom_policy_paginator: SimulateCustomPolicyPaginator = client.get_paginator("simulate_custom_policy")
    simulate_principal_policy_paginator: SimulatePrincipalPolicyPaginator = client.get_paginator("simulate_principal_policy")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iam.type_defs import (
    ContextEntryTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetGroupResponseTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListMFADevicesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesResponseTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    PaginatorConfigTypeDef,
    SimulatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetAccountAuthorizationDetailsPaginator",
    "GetGroupPaginator",
    "ListAccessKeysPaginator",
    "ListAccountAliasesPaginator",
    "ListAttachedGroupPoliciesPaginator",
    "ListAttachedRolePoliciesPaginator",
    "ListAttachedUserPoliciesPaginator",
    "ListEntitiesForPolicyPaginator",
    "ListGroupPoliciesPaginator",
    "ListGroupsPaginator",
    "ListGroupsForUserPaginator",
    "ListInstanceProfilesPaginator",
    "ListInstanceProfilesForRolePaginator",
    "ListMFADevicesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyVersionsPaginator",
    "ListRolePoliciesPaginator",
    "ListRolesPaginator",
    "ListSSHPublicKeysPaginator",
    "ListServerCertificatesPaginator",
    "ListSigningCertificatesPaginator",
    "ListUserPoliciesPaginator",
    "ListUsersPaginator",
    "ListVirtualMFADevicesPaginator",
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
)


class GetAccountAuthorizationDetailsPaginator(Boto3Paginator):
    """
    [Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)
    """

    def paginate(
        self,
        Filter: List[
            Literal["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetAccountAuthorizationDetailsResponseTypeDef]:
        """
        [GetAccountAuthorizationDetails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails.paginate)
        """


class GetGroupPaginator(Boto3Paginator):
    """
    [Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.GetGroup)
    """

    def paginate(
        self, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupResponseTypeDef]:
        """
        [GetGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.GetGroup.paginate)
        """


class ListAccessKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAccessKeys)
    """

    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessKeysResponseTypeDef]:
        """
        [ListAccessKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAccessKeys.paginate)
        """


class ListAccountAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAccountAliases)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAliasesResponseTypeDef]:
        """
        [ListAccountAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAccountAliases.paginate)
        """


class ListAttachedGroupPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)
    """

    def paginate(
        self,
        GroupName: str,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAttachedGroupPoliciesResponseTypeDef]:
        """
        [ListAttachedGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies.paginate)
        """


class ListAttachedRolePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)
    """

    def paginate(
        self, RoleName: str, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedRolePoliciesResponseTypeDef]:
        """
        [ListAttachedRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies.paginate)
        """


class ListAttachedUserPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)
    """

    def paginate(
        self, UserName: str, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedUserPoliciesResponseTypeDef]:
        """
        [ListAttachedUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies.paginate)
        """


class ListEntitiesForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)
    """

    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEntitiesForPolicyResponseTypeDef]:
        """
        [ListEntitiesForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy.paginate)
        """


class ListGroupPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)
    """

    def paginate(
        self, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupPoliciesResponseTypeDef]:
        """
        [ListGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroupPolicies.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroups)
    """

    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroups.paginate)
        """


class ListGroupsForUserPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)
    """

    def paginate(
        self, UserName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsForUserResponseTypeDef]:
        """
        [ListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListGroupsForUser.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)
    """

    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesResponseTypeDef]:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles.paginate)
        """


class ListInstanceProfilesForRolePaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)
    """

    def paginate(
        self, RoleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesForRoleResponseTypeDef]:
        """
        [ListInstanceProfilesForRole.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole.paginate)
        """


class ListMFADevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListMFADevices)
    """

    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMFADevicesResponseTypeDef]:
        """
        [ListMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListMFADevices.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListPolicies)
    """

    def paginate(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListPolicies.paginate)
        """


class ListPolicyVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)
    """

    def paginate(
        self, PolicyArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyVersionsResponseTypeDef]:
        """
        [ListPolicyVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListPolicyVersions.paginate)
        """


class ListRolePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListRolePolicies)
    """

    def paginate(
        self, RoleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRolePoliciesResponseTypeDef]:
        """
        [ListRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListRolePolicies.paginate)
        """


class ListRolesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListRoles)
    """

    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRolesResponseTypeDef]:
        """
        [ListRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListRoles.paginate)
        """


class ListSSHPublicKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)
    """

    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSSHPublicKeysResponseTypeDef]:
        """
        [ListSSHPublicKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys.paginate)
        """


class ListServerCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListServerCertificates)
    """

    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServerCertificatesResponseTypeDef]:
        """
        [ListServerCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListServerCertificates.paginate)
        """


class ListSigningCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)
    """

    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningCertificatesResponseTypeDef]:
        """
        [ListSigningCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListSigningCertificates.paginate)
        """


class ListUserPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListUserPolicies)
    """

    def paginate(
        self, UserName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserPoliciesResponseTypeDef]:
        """
        [ListUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListUserPolicies.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListUsers)
    """

    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListUsers.paginate)
        """


class ListVirtualMFADevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)
    """

    def paginate(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListVirtualMFADevicesResponseTypeDef]:
        """
        [ListVirtualMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices.paginate)
        """


class SimulateCustomPolicyPaginator(Boto3Paginator):
    """
    [Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)
    """

    def paginate(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SimulatePolicyResponseTypeDef]:
        """
        [SimulateCustomPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy.paginate)
        """


class SimulatePrincipalPolicyPaginator(Boto3Paginator):
    """
    [Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)
    """

    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SimulatePolicyResponseTypeDef]:
        """
        [SimulatePrincipalPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy.paginate)
        """
