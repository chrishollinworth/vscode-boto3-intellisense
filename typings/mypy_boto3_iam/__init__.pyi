"""
Main interface for iam service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iam import (
        Client,
        GetAccountAuthorizationDetailsPaginator,
        GetGroupPaginator,
        IAMClient,
        IAMServiceResource,
        InstanceProfileExistsWaiter,
        ListAccessKeysPaginator,
        ListAccountAliasesPaginator,
        ListAttachedGroupPoliciesPaginator,
        ListAttachedRolePoliciesPaginator,
        ListAttachedUserPoliciesPaginator,
        ListEntitiesForPolicyPaginator,
        ListGroupPoliciesPaginator,
        ListGroupsForUserPaginator,
        ListGroupsPaginator,
        ListInstanceProfilesForRolePaginator,
        ListInstanceProfilesPaginator,
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
        PolicyExistsWaiter,
        RoleExistsWaiter,
        ServiceResource,
        SimulateCustomPolicyPaginator,
        SimulatePrincipalPolicyPaginator,
        UserExistsWaiter,
    )

    session = boto3.Session()

    client: IAMClient = boto3.client("iam")
    session_client: IAMClient = session.client("iam")

    resource: IAMServiceResource = boto3.resource("iam")
    session_resource: IAMServiceResource = session.resource("iam")

    instance_profile_exists_waiter: InstanceProfileExistsWaiter = client.get_waiter("instance_profile_exists")
    policy_exists_waiter: PolicyExistsWaiter = client.get_waiter("policy_exists")
    role_exists_waiter: RoleExistsWaiter = client.get_waiter("role_exists")
    user_exists_waiter: UserExistsWaiter = client.get_waiter("user_exists")

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
from mypy_boto3_iam.client import IAMClient
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
    ListGroupsForUserPaginator,
    ListGroupsPaginator,
    ListInstanceProfilesForRolePaginator,
    ListInstanceProfilesPaginator,
    ListMFADevicesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListServerCertificatesPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from mypy_boto3_iam.service_resource import IAMServiceResource
from mypy_boto3_iam.waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
)

Client = IAMClient


ServiceResource = IAMServiceResource


__all__ = (
    "Client",
    "GetAccountAuthorizationDetailsPaginator",
    "GetGroupPaginator",
    "IAMClient",
    "IAMServiceResource",
    "InstanceProfileExistsWaiter",
    "ListAccessKeysPaginator",
    "ListAccountAliasesPaginator",
    "ListAttachedGroupPoliciesPaginator",
    "ListAttachedRolePoliciesPaginator",
    "ListAttachedUserPoliciesPaginator",
    "ListEntitiesForPolicyPaginator",
    "ListGroupPoliciesPaginator",
    "ListGroupsForUserPaginator",
    "ListGroupsPaginator",
    "ListInstanceProfilesForRolePaginator",
    "ListInstanceProfilesPaginator",
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
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "ServiceResource",
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
    "UserExistsWaiter",
)
