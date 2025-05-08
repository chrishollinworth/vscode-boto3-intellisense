"""
Main interface for iam service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
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
        ListInstanceProfileTagsPaginator,
        ListInstanceProfilesForRolePaginator,
        ListInstanceProfilesPaginator,
        ListMFADeviceTagsPaginator,
        ListMFADevicesPaginator,
        ListOpenIDConnectProviderTagsPaginator,
        ListPoliciesPaginator,
        ListPolicyTagsPaginator,
        ListPolicyVersionsPaginator,
        ListRolePoliciesPaginator,
        ListRoleTagsPaginator,
        ListRolesPaginator,
        ListSAMLProviderTagsPaginator,
        ListSSHPublicKeysPaginator,
        ListServerCertificateTagsPaginator,
        ListServerCertificatesPaginator,
        ListSigningCertificatesPaginator,
        ListUserPoliciesPaginator,
        ListUserTagsPaginator,
        ListUsersPaginator,
        ListVirtualMFADevicesPaginator,
        PolicyExistsWaiter,
        RoleExistsWaiter,
        ServiceResource,
        SimulateCustomPolicyPaginator,
        SimulatePrincipalPolicyPaginator,
        UserExistsWaiter,
    )

    session = Session()
    client: IAMClient = session.client("iam")

    resource: IAMServiceResource = session.resource("iam")

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
    list_groups_for_user_paginator: ListGroupsForUserPaginator = client.get_paginator("list_groups_for_user")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_instance_profile_tags_paginator: ListInstanceProfileTagsPaginator = client.get_paginator("list_instance_profile_tags")
    list_instance_profiles_for_role_paginator: ListInstanceProfilesForRolePaginator = client.get_paginator("list_instance_profiles_for_role")
    list_instance_profiles_paginator: ListInstanceProfilesPaginator = client.get_paginator("list_instance_profiles")
    list_mfa_device_tags_paginator: ListMFADeviceTagsPaginator = client.get_paginator("list_mfa_device_tags")
    list_mfa_devices_paginator: ListMFADevicesPaginator = client.get_paginator("list_mfa_devices")
    list_open_id_connect_provider_tags_paginator: ListOpenIDConnectProviderTagsPaginator = client.get_paginator("list_open_id_connect_provider_tags")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_tags_paginator: ListPolicyTagsPaginator = client.get_paginator("list_policy_tags")
    list_policy_versions_paginator: ListPolicyVersionsPaginator = client.get_paginator("list_policy_versions")
    list_role_policies_paginator: ListRolePoliciesPaginator = client.get_paginator("list_role_policies")
    list_role_tags_paginator: ListRoleTagsPaginator = client.get_paginator("list_role_tags")
    list_roles_paginator: ListRolesPaginator = client.get_paginator("list_roles")
    list_saml_provider_tags_paginator: ListSAMLProviderTagsPaginator = client.get_paginator("list_saml_provider_tags")
    list_ssh_public_keys_paginator: ListSSHPublicKeysPaginator = client.get_paginator("list_ssh_public_keys")
    list_server_certificate_tags_paginator: ListServerCertificateTagsPaginator = client.get_paginator("list_server_certificate_tags")
    list_server_certificates_paginator: ListServerCertificatesPaginator = client.get_paginator("list_server_certificates")
    list_signing_certificates_paginator: ListSigningCertificatesPaginator = client.get_paginator("list_signing_certificates")
    list_user_policies_paginator: ListUserPoliciesPaginator = client.get_paginator("list_user_policies")
    list_user_tags_paginator: ListUserTagsPaginator = client.get_paginator("list_user_tags")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    list_virtual_mfa_devices_paginator: ListVirtualMFADevicesPaginator = client.get_paginator("list_virtual_mfa_devices")
    simulate_custom_policy_paginator: SimulateCustomPolicyPaginator = client.get_paginator("simulate_custom_policy")
    simulate_principal_policy_paginator: SimulatePrincipalPolicyPaginator = client.get_paginator("simulate_principal_policy")
    ```
"""

from .client import IAMClient
from .paginator import (
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
    ListInstanceProfileTagsPaginator,
    ListMFADevicesPaginator,
    ListMFADeviceTagsPaginator,
    ListOpenIDConnectProviderTagsPaginator,
    ListPoliciesPaginator,
    ListPolicyTagsPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListRoleTagsPaginator,
    ListSAMLProviderTagsPaginator,
    ListServerCertificatesPaginator,
    ListServerCertificateTagsPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListUserTagsPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from .waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
)

try:
    from .service_resource import IAMServiceResource
except ImportError:
    from builtins import object as IAMServiceResource  # type: ignore[assignment]

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
    "ListInstanceProfileTagsPaginator",
    "ListInstanceProfilesForRolePaginator",
    "ListInstanceProfilesPaginator",
    "ListMFADeviceTagsPaginator",
    "ListMFADevicesPaginator",
    "ListOpenIDConnectProviderTagsPaginator",
    "ListPoliciesPaginator",
    "ListPolicyTagsPaginator",
    "ListPolicyVersionsPaginator",
    "ListRolePoliciesPaginator",
    "ListRoleTagsPaginator",
    "ListRolesPaginator",
    "ListSAMLProviderTagsPaginator",
    "ListSSHPublicKeysPaginator",
    "ListServerCertificateTagsPaginator",
    "ListServerCertificatesPaginator",
    "ListSigningCertificatesPaginator",
    "ListUserPoliciesPaginator",
    "ListUserTagsPaginator",
    "ListUsersPaginator",
    "ListVirtualMFADevicesPaginator",
    "PolicyExistsWaiter",
    "RoleExistsWaiter",
    "ServiceResource",
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
    "UserExistsWaiter",
)
