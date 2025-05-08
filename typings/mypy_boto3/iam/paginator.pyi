"""
Type annotations for iam service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

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
        SimulateCustomPolicyPaginator,
        SimulatePrincipalPolicyPaginator,
    )

    session = Session()
    client: IAMClient = session.client("iam")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAccountAuthorizationDetailsRequestPaginateTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetGroupRequestPaginateTypeDef,
    GetGroupResponseTypeDef,
    ListAccessKeysRequestPaginateTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesRequestPaginateTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesRequestPaginateTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesRequestPaginateTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesRequestPaginateTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyRequestPaginateTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesRequestPaginateTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserRequestPaginateTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsRequestPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleRequestPaginateTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesRequestPaginateTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListInstanceProfileTagsRequestPaginateTypeDef,
    ListInstanceProfileTagsResponseTypeDef,
    ListMFADevicesRequestPaginateTypeDef,
    ListMFADevicesResponseTypeDef,
    ListMFADeviceTagsRequestPaginateTypeDef,
    ListMFADeviceTagsResponseTypeDef,
    ListOpenIDConnectProviderTagsRequestPaginateTypeDef,
    ListOpenIDConnectProviderTagsResponseTypeDef,
    ListPoliciesRequestPaginateTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyTagsRequestPaginateTypeDef,
    ListPolicyTagsResponseTypeDef,
    ListPolicyVersionsRequestPaginateTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesRequestPaginateTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesRequestPaginateTypeDef,
    ListRolesResponseTypeDef,
    ListRoleTagsRequestPaginateTypeDef,
    ListRoleTagsResponseTypeDef,
    ListSAMLProviderTagsRequestPaginateTypeDef,
    ListSAMLProviderTagsResponseTypeDef,
    ListServerCertificatesRequestPaginateTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListServerCertificateTagsRequestPaginateTypeDef,
    ListServerCertificateTagsResponseTypeDef,
    ListSigningCertificatesRequestPaginateTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListSSHPublicKeysRequestPaginateTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListUserPoliciesRequestPaginateTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersRequestPaginateTypeDef,
    ListUsersResponseTypeDef,
    ListUserTagsRequestPaginateTypeDef,
    ListUserTagsResponseTypeDef,
    ListVirtualMFADevicesRequestPaginateTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    SimulateCustomPolicyRequestPaginateTypeDef,
    SimulatePolicyResponseTypeDef,
    SimulatePrincipalPolicyRequestPaginateTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
)

if TYPE_CHECKING:
    _GetAccountAuthorizationDetailsPaginatorBase = Paginator[
        GetAccountAuthorizationDetailsResponseTypeDef
    ]
else:
    _GetAccountAuthorizationDetailsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAccountAuthorizationDetailsPaginator(_GetAccountAuthorizationDetailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/GetAccountAuthorizationDetails.html#IAM.Paginator.GetAccountAuthorizationDetails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#getaccountauthorizationdetailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAccountAuthorizationDetailsRequestPaginateTypeDef]
    ) -> PageIterator[GetAccountAuthorizationDetailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/GetAccountAuthorizationDetails.html#IAM.Paginator.GetAccountAuthorizationDetails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#getaccountauthorizationdetailspaginator)
        """

if TYPE_CHECKING:
    _GetGroupPaginatorBase = Paginator[GetGroupResponseTypeDef]
else:
    _GetGroupPaginatorBase = Paginator  # type: ignore[assignment]

class GetGroupPaginator(_GetGroupPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/GetGroup.html#IAM.Paginator.GetGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#getgrouppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetGroupRequestPaginateTypeDef]
    ) -> PageIterator[GetGroupResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/GetGroup.html#IAM.Paginator.GetGroup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#getgrouppaginator)
        """

if TYPE_CHECKING:
    _ListAccessKeysPaginatorBase = Paginator[ListAccessKeysResponseTypeDef]
else:
    _ListAccessKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessKeysPaginator(_ListAccessKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAccessKeys.html#IAM.Paginator.ListAccessKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listaccesskeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAccessKeys.html#IAM.Paginator.ListAccessKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listaccesskeyspaginator)
        """

if TYPE_CHECKING:
    _ListAccountAliasesPaginatorBase = Paginator[ListAccountAliasesResponseTypeDef]
else:
    _ListAccountAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountAliasesPaginator(_ListAccountAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAccountAliases.html#IAM.Paginator.ListAccountAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listaccountaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAccountAliases.html#IAM.Paginator.ListAccountAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listaccountaliasespaginator)
        """

if TYPE_CHECKING:
    _ListAttachedGroupPoliciesPaginatorBase = Paginator[ListAttachedGroupPoliciesResponseTypeDef]
else:
    _ListAttachedGroupPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttachedGroupPoliciesPaginator(_ListAttachedGroupPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedGroupPolicies.html#IAM.Paginator.ListAttachedGroupPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattachedgrouppoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttachedGroupPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAttachedGroupPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedGroupPolicies.html#IAM.Paginator.ListAttachedGroupPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattachedgrouppoliciespaginator)
        """

if TYPE_CHECKING:
    _ListAttachedRolePoliciesPaginatorBase = Paginator[ListAttachedRolePoliciesResponseTypeDef]
else:
    _ListAttachedRolePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttachedRolePoliciesPaginator(_ListAttachedRolePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedRolePolicies.html#IAM.Paginator.ListAttachedRolePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattachedrolepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttachedRolePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAttachedRolePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedRolePolicies.html#IAM.Paginator.ListAttachedRolePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattachedrolepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListAttachedUserPoliciesPaginatorBase = Paginator[ListAttachedUserPoliciesResponseTypeDef]
else:
    _ListAttachedUserPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttachedUserPoliciesPaginator(_ListAttachedUserPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedUserPolicies.html#IAM.Paginator.ListAttachedUserPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattacheduserpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttachedUserPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAttachedUserPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAttachedUserPolicies.html#IAM.Paginator.ListAttachedUserPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listattacheduserpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListEntitiesForPolicyPaginatorBase = Paginator[ListEntitiesForPolicyResponseTypeDef]
else:
    _ListEntitiesForPolicyPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntitiesForPolicyPaginator(_ListEntitiesForPolicyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListEntitiesForPolicy.html#IAM.Paginator.ListEntitiesForPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listentitiesforpolicypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntitiesForPolicyRequestPaginateTypeDef]
    ) -> PageIterator[ListEntitiesForPolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListEntitiesForPolicy.html#IAM.Paginator.ListEntitiesForPolicy.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listentitiesforpolicypaginator)
        """

if TYPE_CHECKING:
    _ListGroupPoliciesPaginatorBase = Paginator[ListGroupPoliciesResponseTypeDef]
else:
    _ListGroupPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupPoliciesPaginator(_ListGroupPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroupPolicies.html#IAM.Paginator.ListGroupPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgrouppoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroupPolicies.html#IAM.Paginator.ListGroupPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgrouppoliciespaginator)
        """

if TYPE_CHECKING:
    _ListGroupsForUserPaginatorBase = Paginator[ListGroupsForUserResponseTypeDef]
else:
    _ListGroupsForUserPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsForUserPaginator(_ListGroupsForUserPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroupsForUser.html#IAM.Paginator.ListGroupsForUser)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgroupsforuserpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsForUserRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsForUserResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroupsForUser.html#IAM.Paginator.ListGroupsForUser.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgroupsforuserpaginator)
        """

if TYPE_CHECKING:
    _ListGroupsPaginatorBase = Paginator[ListGroupsResponseTypeDef]
else:
    _ListGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGroupsPaginator(_ListGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroups.html#IAM.Paginator.ListGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListGroups.html#IAM.Paginator.ListGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listgroupspaginator)
        """

if TYPE_CHECKING:
    _ListInstanceProfileTagsPaginatorBase = Paginator[ListInstanceProfileTagsResponseTypeDef]
else:
    _ListInstanceProfileTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceProfileTagsPaginator(_ListInstanceProfileTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfileTags.html#IAM.Paginator.ListInstanceProfileTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofiletagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceProfileTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceProfileTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfileTags.html#IAM.Paginator.ListInstanceProfileTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofiletagspaginator)
        """

if TYPE_CHECKING:
    _ListInstanceProfilesForRolePaginatorBase = Paginator[
        ListInstanceProfilesForRoleResponseTypeDef
    ]
else:
    _ListInstanceProfilesForRolePaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceProfilesForRolePaginator(_ListInstanceProfilesForRolePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfilesForRole.html#IAM.Paginator.ListInstanceProfilesForRole)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofilesforrolepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceProfilesForRoleRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceProfilesForRoleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfilesForRole.html#IAM.Paginator.ListInstanceProfilesForRole.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofilesforrolepaginator)
        """

if TYPE_CHECKING:
    _ListInstanceProfilesPaginatorBase = Paginator[ListInstanceProfilesResponseTypeDef]
else:
    _ListInstanceProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceProfilesPaginator(_ListInstanceProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfiles.html#IAM.Paginator.ListInstanceProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListInstanceProfiles.html#IAM.Paginator.ListInstanceProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listinstanceprofilespaginator)
        """

if TYPE_CHECKING:
    _ListMFADeviceTagsPaginatorBase = Paginator[ListMFADeviceTagsResponseTypeDef]
else:
    _ListMFADeviceTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMFADeviceTagsPaginator(_ListMFADeviceTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListMFADeviceTags.html#IAM.Paginator.ListMFADeviceTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listmfadevicetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMFADeviceTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListMFADeviceTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListMFADeviceTags.html#IAM.Paginator.ListMFADeviceTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listmfadevicetagspaginator)
        """

if TYPE_CHECKING:
    _ListMFADevicesPaginatorBase = Paginator[ListMFADevicesResponseTypeDef]
else:
    _ListMFADevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMFADevicesPaginator(_ListMFADevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListMFADevices.html#IAM.Paginator.ListMFADevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listmfadevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMFADevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListMFADevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListMFADevices.html#IAM.Paginator.ListMFADevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listmfadevicespaginator)
        """

if TYPE_CHECKING:
    _ListOpenIDConnectProviderTagsPaginatorBase = Paginator[
        ListOpenIDConnectProviderTagsResponseTypeDef
    ]
else:
    _ListOpenIDConnectProviderTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpenIDConnectProviderTagsPaginator(_ListOpenIDConnectProviderTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListOpenIDConnectProviderTags.html#IAM.Paginator.ListOpenIDConnectProviderTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listopenidconnectprovidertagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpenIDConnectProviderTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListOpenIDConnectProviderTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListOpenIDConnectProviderTags.html#IAM.Paginator.ListOpenIDConnectProviderTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listopenidconnectprovidertagspaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesResponseTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicies.html#IAM.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicies.html#IAM.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyTagsPaginatorBase = Paginator[ListPolicyTagsResponseTypeDef]
else:
    _ListPolicyTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyTagsPaginator(_ListPolicyTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicyTags.html#IAM.Paginator.ListPolicyTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpolicytagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicyTags.html#IAM.Paginator.ListPolicyTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpolicytagspaginator)
        """

if TYPE_CHECKING:
    _ListPolicyVersionsPaginatorBase = Paginator[ListPolicyVersionsResponseTypeDef]
else:
    _ListPolicyVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyVersionsPaginator(_ListPolicyVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicyVersions.html#IAM.Paginator.ListPolicyVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpolicyversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListPolicyVersions.html#IAM.Paginator.ListPolicyVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listpolicyversionspaginator)
        """

if TYPE_CHECKING:
    _ListRolePoliciesPaginatorBase = Paginator[ListRolePoliciesResponseTypeDef]
else:
    _ListRolePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRolePoliciesPaginator(_ListRolePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRolePolicies.html#IAM.Paginator.ListRolePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listrolepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRolePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListRolePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRolePolicies.html#IAM.Paginator.ListRolePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listrolepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListRoleTagsPaginatorBase = Paginator[ListRoleTagsResponseTypeDef]
else:
    _ListRoleTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRoleTagsPaginator(_ListRoleTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRoleTags.html#IAM.Paginator.ListRoleTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listroletagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRoleTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListRoleTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRoleTags.html#IAM.Paginator.ListRoleTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listroletagspaginator)
        """

if TYPE_CHECKING:
    _ListRolesPaginatorBase = Paginator[ListRolesResponseTypeDef]
else:
    _ListRolesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRolesPaginator(_ListRolesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRoles.html#IAM.Paginator.ListRoles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listrolespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRolesRequestPaginateTypeDef]
    ) -> PageIterator[ListRolesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListRoles.html#IAM.Paginator.ListRoles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listrolespaginator)
        """

if TYPE_CHECKING:
    _ListSAMLProviderTagsPaginatorBase = Paginator[ListSAMLProviderTagsResponseTypeDef]
else:
    _ListSAMLProviderTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSAMLProviderTagsPaginator(_ListSAMLProviderTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSAMLProviderTags.html#IAM.Paginator.ListSAMLProviderTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsamlprovidertagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSAMLProviderTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListSAMLProviderTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSAMLProviderTags.html#IAM.Paginator.ListSAMLProviderTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsamlprovidertagspaginator)
        """

if TYPE_CHECKING:
    _ListSSHPublicKeysPaginatorBase = Paginator[ListSSHPublicKeysResponseTypeDef]
else:
    _ListSSHPublicKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListSSHPublicKeysPaginator(_ListSSHPublicKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSSHPublicKeys.html#IAM.Paginator.ListSSHPublicKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsshpublickeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSSHPublicKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListSSHPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSSHPublicKeys.html#IAM.Paginator.ListSSHPublicKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsshpublickeyspaginator)
        """

if TYPE_CHECKING:
    _ListServerCertificateTagsPaginatorBase = Paginator[ListServerCertificateTagsResponseTypeDef]
else:
    _ListServerCertificateTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServerCertificateTagsPaginator(_ListServerCertificateTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListServerCertificateTags.html#IAM.Paginator.ListServerCertificateTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listservercertificatetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServerCertificateTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListServerCertificateTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListServerCertificateTags.html#IAM.Paginator.ListServerCertificateTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listservercertificatetagspaginator)
        """

if TYPE_CHECKING:
    _ListServerCertificatesPaginatorBase = Paginator[ListServerCertificatesResponseTypeDef]
else:
    _ListServerCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServerCertificatesPaginator(_ListServerCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListServerCertificates.html#IAM.Paginator.ListServerCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listservercertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServerCertificatesRequestPaginateTypeDef]
    ) -> PageIterator[ListServerCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListServerCertificates.html#IAM.Paginator.ListServerCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listservercertificatespaginator)
        """

if TYPE_CHECKING:
    _ListSigningCertificatesPaginatorBase = Paginator[ListSigningCertificatesResponseTypeDef]
else:
    _ListSigningCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSigningCertificatesPaginator(_ListSigningCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSigningCertificates.html#IAM.Paginator.ListSigningCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsigningcertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSigningCertificatesRequestPaginateTypeDef]
    ) -> PageIterator[ListSigningCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListSigningCertificates.html#IAM.Paginator.ListSigningCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listsigningcertificatespaginator)
        """

if TYPE_CHECKING:
    _ListUserPoliciesPaginatorBase = Paginator[ListUserPoliciesResponseTypeDef]
else:
    _ListUserPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserPoliciesPaginator(_ListUserPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUserPolicies.html#IAM.Paginator.ListUserPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listuserpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListUserPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUserPolicies.html#IAM.Paginator.ListUserPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listuserpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListUserTagsPaginatorBase = Paginator[ListUserTagsResponseTypeDef]
else:
    _ListUserTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUserTagsPaginator(_ListUserTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUserTags.html#IAM.Paginator.ListUserTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listusertagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUserTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListUserTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUserTags.html#IAM.Paginator.ListUserTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listusertagspaginator)
        """

if TYPE_CHECKING:
    _ListUsersPaginatorBase = Paginator[ListUsersResponseTypeDef]
else:
    _ListUsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsersPaginator(_ListUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUsers.html#IAM.Paginator.ListUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsersRequestPaginateTypeDef]
    ) -> PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListUsers.html#IAM.Paginator.ListUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listuserspaginator)
        """

if TYPE_CHECKING:
    _ListVirtualMFADevicesPaginatorBase = Paginator[ListVirtualMFADevicesResponseTypeDef]
else:
    _ListVirtualMFADevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualMFADevicesPaginator(_ListVirtualMFADevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListVirtualMFADevices.html#IAM.Paginator.ListVirtualMFADevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listvirtualmfadevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualMFADevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListVirtualMFADevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListVirtualMFADevices.html#IAM.Paginator.ListVirtualMFADevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#listvirtualmfadevicespaginator)
        """

if TYPE_CHECKING:
    _SimulateCustomPolicyPaginatorBase = Paginator[SimulatePolicyResponseTypeDef]
else:
    _SimulateCustomPolicyPaginatorBase = Paginator  # type: ignore[assignment]

class SimulateCustomPolicyPaginator(_SimulateCustomPolicyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/SimulateCustomPolicy.html#IAM.Paginator.SimulateCustomPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#simulatecustompolicypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SimulateCustomPolicyRequestPaginateTypeDef]
    ) -> PageIterator[SimulatePolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/SimulateCustomPolicy.html#IAM.Paginator.SimulateCustomPolicy.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#simulatecustompolicypaginator)
        """

if TYPE_CHECKING:
    _SimulatePrincipalPolicyPaginatorBase = Paginator[SimulatePolicyResponseTypeDef]
else:
    _SimulatePrincipalPolicyPaginatorBase = Paginator  # type: ignore[assignment]

class SimulatePrincipalPolicyPaginator(_SimulatePrincipalPolicyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/SimulatePrincipalPolicy.html#IAM.Paginator.SimulatePrincipalPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#simulateprincipalpolicypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SimulatePrincipalPolicyRequestPaginateTypeDef]
    ) -> PageIterator[SimulatePolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/SimulatePrincipalPolicy.html#IAM.Paginator.SimulatePrincipalPolicy.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/paginators/#simulateprincipalpolicypaginator)
        """
