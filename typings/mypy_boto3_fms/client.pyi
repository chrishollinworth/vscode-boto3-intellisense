"""
Type annotations for fms service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_fms.client import FMSClient

    session = Session()
    client: FMSClient = session.client("fms")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAdminAccountsForOrganizationPaginator,
    ListAdminsManagingAccountPaginator,
    ListAppsListsPaginator,
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
    ListProtocolsListsPaginator,
    ListThirdPartyFirewallFirewallPoliciesPaginator,
)
from .type_defs import (
    AssociateAdminAccountRequestTypeDef,
    AssociateThirdPartyFirewallRequestTypeDef,
    AssociateThirdPartyFirewallResponseTypeDef,
    BatchAssociateResourceRequestTypeDef,
    BatchAssociateResourceResponseTypeDef,
    BatchDisassociateResourceRequestTypeDef,
    BatchDisassociateResourceResponseTypeDef,
    DeleteAppsListRequestTypeDef,
    DeletePolicyRequestTypeDef,
    DeleteProtocolsListRequestTypeDef,
    DeleteResourceSetRequestTypeDef,
    DisassociateThirdPartyFirewallRequestTypeDef,
    DisassociateThirdPartyFirewallResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAdminAccountResponseTypeDef,
    GetAdminScopeRequestTypeDef,
    GetAdminScopeResponseTypeDef,
    GetAppsListRequestTypeDef,
    GetAppsListResponseTypeDef,
    GetComplianceDetailRequestTypeDef,
    GetComplianceDetailResponseTypeDef,
    GetNotificationChannelResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    GetProtectionStatusRequestTypeDef,
    GetProtectionStatusResponseTypeDef,
    GetProtocolsListRequestTypeDef,
    GetProtocolsListResponseTypeDef,
    GetResourceSetRequestTypeDef,
    GetResourceSetResponseTypeDef,
    GetThirdPartyFirewallAssociationStatusRequestTypeDef,
    GetThirdPartyFirewallAssociationStatusResponseTypeDef,
    GetViolationDetailsRequestTypeDef,
    GetViolationDetailsResponseTypeDef,
    ListAdminAccountsForOrganizationRequestTypeDef,
    ListAdminAccountsForOrganizationResponseTypeDef,
    ListAdminsManagingAccountRequestTypeDef,
    ListAdminsManagingAccountResponseTypeDef,
    ListAppsListsRequestTypeDef,
    ListAppsListsResponseTypeDef,
    ListComplianceStatusRequestTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListDiscoveredResourcesRequestTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListMemberAccountsRequestTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListProtocolsListsRequestTypeDef,
    ListProtocolsListsResponseTypeDef,
    ListResourceSetResourcesRequestTypeDef,
    ListResourceSetResourcesResponseTypeDef,
    ListResourceSetsRequestTypeDef,
    ListResourceSetsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThirdPartyFirewallFirewallPoliciesRequestTypeDef,
    ListThirdPartyFirewallFirewallPoliciesResponseTypeDef,
    PutAdminAccountRequestTypeDef,
    PutAppsListRequestTypeDef,
    PutAppsListResponseTypeDef,
    PutNotificationChannelRequestTypeDef,
    PutPolicyRequestTypeDef,
    PutPolicyResponseTypeDef,
    PutProtocolsListRequestTypeDef,
    PutProtocolsListResponseTypeDef,
    PutResourceSetRequestTypeDef,
    PutResourceSetResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("FMSClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class FMSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FMSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#generate_presigned_url)
        """

    def associate_admin_account(
        self, **kwargs: Unpack[AssociateAdminAccountRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets a Firewall Manager default administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/associate_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#associate_admin_account)
        """

    def associate_third_party_firewall(
        self, **kwargs: Unpack[AssociateThirdPartyFirewallRequestTypeDef]
    ) -> AssociateThirdPartyFirewallResponseTypeDef:
        """
        Sets the Firewall Manager policy administrator as a tenant administrator of a
        third-party firewall service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/associate_third_party_firewall.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#associate_third_party_firewall)
        """

    def batch_associate_resource(
        self, **kwargs: Unpack[BatchAssociateResourceRequestTypeDef]
    ) -> BatchAssociateResourceResponseTypeDef:
        """
        Associate resources to a Firewall Manager resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/batch_associate_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#batch_associate_resource)
        """

    def batch_disassociate_resource(
        self, **kwargs: Unpack[BatchDisassociateResourceRequestTypeDef]
    ) -> BatchDisassociateResourceResponseTypeDef:
        """
        Disassociates resources from a Firewall Manager resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/batch_disassociate_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#batch_disassociate_resource)
        """

    def delete_apps_list(
        self, **kwargs: Unpack[DeleteAppsListRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes an Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/delete_apps_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#delete_apps_list)
        """

    def delete_notification_channel(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Firewall Manager association with the IAM role and the Amazon Simple
        Notification Service (SNS) topic that is used to record Firewall Manager SNS
        logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/delete_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#delete_notification_channel)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes an Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#delete_policy)
        """

    def delete_protocols_list(
        self, **kwargs: Unpack[DeleteProtocolsListRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes an Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/delete_protocols_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#delete_protocols_list)
        """

    def delete_resource_set(
        self, **kwargs: Unpack[DeleteResourceSetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified <a>ResourceSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/delete_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#delete_resource_set)
        """

    def disassociate_admin_account(self) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Firewall Manager administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/disassociate_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#disassociate_admin_account)
        """

    def disassociate_third_party_firewall(
        self, **kwargs: Unpack[DisassociateThirdPartyFirewallRequestTypeDef]
    ) -> DisassociateThirdPartyFirewallResponseTypeDef:
        """
        Disassociates a Firewall Manager policy administrator from a third-party
        firewall tenant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/disassociate_third_party_firewall.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#disassociate_third_party_firewall)
        """

    def get_admin_account(self) -> GetAdminAccountResponseTypeDef:
        """
        Returns the Organizations account that is associated with Firewall Manager as
        the Firewall Manager default administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_admin_account)
        """

    def get_admin_scope(
        self, **kwargs: Unpack[GetAdminScopeRequestTypeDef]
    ) -> GetAdminScopeResponseTypeDef:
        """
        Returns information about the specified account's administrative scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_admin_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_admin_scope)
        """

    def get_apps_list(
        self, **kwargs: Unpack[GetAppsListRequestTypeDef]
    ) -> GetAppsListResponseTypeDef:
        """
        Returns information about the specified Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_apps_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_apps_list)
        """

    def get_compliance_detail(
        self, **kwargs: Unpack[GetComplianceDetailRequestTypeDef]
    ) -> GetComplianceDetailResponseTypeDef:
        """
        Returns detailed compliance information about the specified member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_compliance_detail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_compliance_detail)
        """

    def get_notification_channel(self) -> GetNotificationChannelResponseTypeDef:
        """
        Information about the Amazon Simple Notification Service (SNS) topic that is
        used to record Firewall Manager SNS logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_notification_channel)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Returns information about the specified Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_policy)
        """

    def get_protection_status(
        self, **kwargs: Unpack[GetProtectionStatusRequestTypeDef]
    ) -> GetProtectionStatusResponseTypeDef:
        """
        If you created a Shield Advanced policy, returns policy-level attack summary
        information in the event of a potential DDoS attack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_protection_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_protection_status)
        """

    def get_protocols_list(
        self, **kwargs: Unpack[GetProtocolsListRequestTypeDef]
    ) -> GetProtocolsListResponseTypeDef:
        """
        Returns information about the specified Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_protocols_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_protocols_list)
        """

    def get_resource_set(
        self, **kwargs: Unpack[GetResourceSetRequestTypeDef]
    ) -> GetResourceSetResponseTypeDef:
        """
        Gets information about a specific resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_resource_set)
        """

    def get_third_party_firewall_association_status(
        self, **kwargs: Unpack[GetThirdPartyFirewallAssociationStatusRequestTypeDef]
    ) -> GetThirdPartyFirewallAssociationStatusResponseTypeDef:
        """
        The onboarding status of a Firewall Manager admin account to third-party
        firewall vendor tenant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_third_party_firewall_association_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_third_party_firewall_association_status)
        """

    def get_violation_details(
        self, **kwargs: Unpack[GetViolationDetailsRequestTypeDef]
    ) -> GetViolationDetailsResponseTypeDef:
        """
        Retrieves violations for a resource based on the specified Firewall Manager
        policy and Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_violation_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_violation_details)
        """

    def list_admin_accounts_for_organization(
        self, **kwargs: Unpack[ListAdminAccountsForOrganizationRequestTypeDef]
    ) -> ListAdminAccountsForOrganizationResponseTypeDef:
        """
        Returns a <code>AdminAccounts</code> object that lists the Firewall Manager
        administrators within the organization that are onboarded to Firewall Manager
        by <a>AssociateAdminAccount</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_admin_accounts_for_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_admin_accounts_for_organization)
        """

    def list_admins_managing_account(
        self, **kwargs: Unpack[ListAdminsManagingAccountRequestTypeDef]
    ) -> ListAdminsManagingAccountResponseTypeDef:
        """
        Lists the accounts that are managing the specified Organizations member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_admins_managing_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_admins_managing_account)
        """

    def list_apps_lists(
        self, **kwargs: Unpack[ListAppsListsRequestTypeDef]
    ) -> ListAppsListsResponseTypeDef:
        """
        Returns an array of <code>AppsListDataSummary</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_apps_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_apps_lists)
        """

    def list_compliance_status(
        self, **kwargs: Unpack[ListComplianceStatusRequestTypeDef]
    ) -> ListComplianceStatusResponseTypeDef:
        """
        Returns an array of <code>PolicyComplianceStatus</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_compliance_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_compliance_status)
        """

    def list_discovered_resources(
        self, **kwargs: Unpack[ListDiscoveredResourcesRequestTypeDef]
    ) -> ListDiscoveredResourcesResponseTypeDef:
        """
        Returns an array of resources in the organization's accounts that are available
        to be associated with a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_discovered_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_discovered_resources)
        """

    def list_member_accounts(
        self, **kwargs: Unpack[ListMemberAccountsRequestTypeDef]
    ) -> ListMemberAccountsResponseTypeDef:
        """
        Returns a <code>MemberAccounts</code> object that lists the member accounts in
        the administrator's Amazon Web Services organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_member_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_member_accounts)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Returns an array of <code>PolicySummary</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_policies)
        """

    def list_protocols_lists(
        self, **kwargs: Unpack[ListProtocolsListsRequestTypeDef]
    ) -> ListProtocolsListsResponseTypeDef:
        """
        Returns an array of <code>ProtocolsListDataSummary</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_protocols_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_protocols_lists)
        """

    def list_resource_set_resources(
        self, **kwargs: Unpack[ListResourceSetResourcesRequestTypeDef]
    ) -> ListResourceSetResourcesResponseTypeDef:
        """
        Returns an array of resources that are currently associated to a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_resource_set_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_resource_set_resources)
        """

    def list_resource_sets(
        self, **kwargs: Unpack[ListResourceSetsRequestTypeDef]
    ) -> ListResourceSetsResponseTypeDef:
        """
        Returns an array of <code>ResourceSetSummary</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_resource_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_resource_sets)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags for the specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_tags_for_resource)
        """

    def list_third_party_firewall_firewall_policies(
        self, **kwargs: Unpack[ListThirdPartyFirewallFirewallPoliciesRequestTypeDef]
    ) -> ListThirdPartyFirewallFirewallPoliciesResponseTypeDef:
        """
        Retrieves a list of all of the third-party firewall policies that are
        associated with the third-party firewall administrator's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/list_third_party_firewall_firewall_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#list_third_party_firewall_firewall_policies)
        """

    def put_admin_account(
        self, **kwargs: Unpack[PutAdminAccountRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates or updates an Firewall Manager administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_admin_account)
        """

    def put_apps_list(
        self, **kwargs: Unpack[PutAppsListRequestTypeDef]
    ) -> PutAppsListResponseTypeDef:
        """
        Creates an Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_apps_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_apps_list)
        """

    def put_notification_channel(
        self, **kwargs: Unpack[PutNotificationChannelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Designates the IAM role and Amazon Simple Notification Service (SNS) topic that
        Firewall Manager uses to record SNS logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_notification_channel)
        """

    def put_policy(self, **kwargs: Unpack[PutPolicyRequestTypeDef]) -> PutPolicyResponseTypeDef:
        """
        Creates an Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_policy)
        """

    def put_protocols_list(
        self, **kwargs: Unpack[PutProtocolsListRequestTypeDef]
    ) -> PutProtocolsListResponseTypeDef:
        """
        Creates an Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_protocols_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_protocols_list)
        """

    def put_resource_set(
        self, **kwargs: Unpack[PutResourceSetRequestTypeDef]
    ) -> PutResourceSetResponseTypeDef:
        """
        Creates the resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/put_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#put_resource_set)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_admin_accounts_for_organization"]
    ) -> ListAdminAccountsForOrganizationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_admins_managing_account"]
    ) -> ListAdminsManagingAccountPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_apps_lists"]
    ) -> ListAppsListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_compliance_status"]
    ) -> ListComplianceStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protocols_lists"]
    ) -> ListProtocolsListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_third_party_firewall_firewall_policies"]
    ) -> ListThirdPartyFirewallFirewallPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/client/#get_paginator)
        """
