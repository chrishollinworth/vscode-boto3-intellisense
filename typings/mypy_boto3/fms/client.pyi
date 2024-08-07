"""
Type annotations for fms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_fms import FMSClient

    client: FMSClient = boto3.client("fms")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ThirdPartyFirewallType
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
    AdminScopeTypeDef,
    AppsListDataTypeDef,
    AssociateThirdPartyFirewallResponseTypeDef,
    BatchAssociateResourceResponseTypeDef,
    BatchDisassociateResourceResponseTypeDef,
    DisassociateThirdPartyFirewallResponseTypeDef,
    GetAdminAccountResponseTypeDef,
    GetAdminScopeResponseTypeDef,
    GetAppsListResponseTypeDef,
    GetComplianceDetailResponseTypeDef,
    GetNotificationChannelResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProtectionStatusResponseTypeDef,
    GetProtocolsListResponseTypeDef,
    GetResourceSetResponseTypeDef,
    GetThirdPartyFirewallAssociationStatusResponseTypeDef,
    GetViolationDetailsResponseTypeDef,
    ListAdminAccountsForOrganizationResponseTypeDef,
    ListAdminsManagingAccountResponseTypeDef,
    ListAppsListsResponseTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListProtocolsListsResponseTypeDef,
    ListResourceSetResourcesResponseTypeDef,
    ListResourceSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThirdPartyFirewallFirewallPoliciesResponseTypeDef,
    PolicyTypeDef,
    ProtocolsListDataTypeDef,
    PutAppsListResponseTypeDef,
    PutPolicyResponseTypeDef,
    PutProtocolsListResponseTypeDef,
    PutResourceSetResponseTypeDef,
    ResourceSetTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FMSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class FMSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FMSClient exceptions.
        """

    def associate_admin_account(self, *, AdminAccount: str) -> None:
        """
        Sets a Firewall Manager default administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.associate_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#associate_admin_account)
        """

    def associate_third_party_firewall(
        self, *, ThirdPartyFirewall: ThirdPartyFirewallType
    ) -> AssociateThirdPartyFirewallResponseTypeDef:
        """
        Sets the Firewall Manager policy administrator as a tenant administrator of a
        third-party firewall service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.associate_third_party_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#associate_third_party_firewall)
        """

    def batch_associate_resource(
        self, *, ResourceSetIdentifier: str, Items: List[str]
    ) -> BatchAssociateResourceResponseTypeDef:
        """
        Associate resources to a Firewall Manager resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.batch_associate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#batch_associate_resource)
        """

    def batch_disassociate_resource(
        self, *, ResourceSetIdentifier: str, Items: List[str]
    ) -> BatchDisassociateResourceResponseTypeDef:
        """
        Disassociates resources from a Firewall Manager resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.batch_disassociate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#batch_disassociate_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#close)
        """

    def delete_apps_list(self, *, ListId: str) -> None:
        """
        Permanently deletes an Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.delete_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete_apps_list)
        """

    def delete_notification_channel(self) -> None:
        """
        Deletes an Firewall Manager association with the IAM role and the Amazon Simple
        Notification Service (SNS) topic that is used to record Firewall Manager SNS
        logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.delete_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete_notification_channel)
        """

    def delete_policy(self, *, PolicyId: str, DeleteAllPolicyResources: bool = None) -> None:
        """
        Permanently deletes an Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete_policy)
        """

    def delete_protocols_list(self, *, ListId: str) -> None:
        """
        Permanently deletes an Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.delete_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete_protocols_list)
        """

    def delete_resource_set(self, *, Identifier: str) -> None:
        """
        Deletes the specified  ResourceSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.delete_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete_resource_set)
        """

    def disassociate_admin_account(self) -> None:
        """
        Disassociates an Firewall Manager administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.disassociate_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#disassociate_admin_account)
        """

    def disassociate_third_party_firewall(
        self, *, ThirdPartyFirewall: ThirdPartyFirewallType
    ) -> DisassociateThirdPartyFirewallResponseTypeDef:
        """
        Disassociates a Firewall Manager policy administrator from a third-party
        firewall tenant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.disassociate_third_party_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#disassociate_third_party_firewall)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#generate_presigned_url)
        """

    def get_admin_account(self) -> GetAdminAccountResponseTypeDef:
        """
        Returns the Organizations account that is associated with Firewall Manager as
        the Firewall Manager default administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_admin_account)
        """

    def get_admin_scope(self, *, AdminAccount: str) -> GetAdminScopeResponseTypeDef:
        """
        Returns information about the specified account's administrative scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_admin_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_admin_scope)
        """

    def get_apps_list(self, *, ListId: str, DefaultList: bool = None) -> GetAppsListResponseTypeDef:
        """
        Returns information about the specified Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_apps_list)
        """

    def get_compliance_detail(
        self, *, PolicyId: str, MemberAccount: str
    ) -> GetComplianceDetailResponseTypeDef:
        """
        Returns detailed compliance information about the specified member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_compliance_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_compliance_detail)
        """

    def get_notification_channel(self) -> GetNotificationChannelResponseTypeDef:
        """
        Information about the Amazon Simple Notification Service (SNS) topic that is
        used to record Firewall Manager SNS logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_notification_channel)
        """

    def get_policy(self, *, PolicyId: str) -> GetPolicyResponseTypeDef:
        """
        Returns information about the specified Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_policy)
        """

    def get_protection_status(
        self,
        *,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetProtectionStatusResponseTypeDef:
        """
        If you created a Shield Advanced policy, returns policy-level attack summary
        information in the event of a potential DDoS attack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_protection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_protection_status)
        """

    def get_protocols_list(
        self, *, ListId: str, DefaultList: bool = None
    ) -> GetProtocolsListResponseTypeDef:
        """
        Returns information about the specified Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_protocols_list)
        """

    def get_resource_set(self, *, Identifier: str) -> GetResourceSetResponseTypeDef:
        """
        Gets information about a specific resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_resource_set)
        """

    def get_third_party_firewall_association_status(
        self, *, ThirdPartyFirewall: ThirdPartyFirewallType
    ) -> GetThirdPartyFirewallAssociationStatusResponseTypeDef:
        """
        The onboarding status of a Firewall Manager admin account to third-party
        firewall vendor tenant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_third_party_firewall_association_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_third_party_firewall_association_status)
        """

    def get_violation_details(
        self, *, PolicyId: str, MemberAccount: str, ResourceId: str, ResourceType: str
    ) -> GetViolationDetailsResponseTypeDef:
        """
        Retrieves violations for a resource based on the specified Firewall Manager
        policy and Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.get_violation_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get_violation_details)
        """

    def list_admin_accounts_for_organization(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAdminAccountsForOrganizationResponseTypeDef:
        """
        Returns a `AdminAccounts` object that lists the Firewall Manager administrators
        within the organization that are onboarded to Firewall Manager by
        AssociateAdminAccount.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_admin_accounts_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_admin_accounts_for_organization)
        """

    def list_admins_managing_account(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListAdminsManagingAccountResponseTypeDef:
        """
        Lists the accounts that are managing the specified Organizations member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_admins_managing_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_admins_managing_account)
        """

    def list_apps_lists(
        self, *, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListAppsListsResponseTypeDef:
        """
        Returns an array of `AppsListDataSummary` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_apps_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_apps_lists)
        """

    def list_compliance_status(
        self, *, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListComplianceStatusResponseTypeDef:
        """
        Returns an array of `PolicyComplianceStatus` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_compliance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_compliance_status)
        """

    def list_discovered_resources(
        self,
        *,
        MemberAccountIds: List[str],
        ResourceType: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListDiscoveredResourcesResponseTypeDef:
        """
        Returns an array of resources in the organization's accounts that are available
        to be associated with a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_discovered_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_discovered_resources)
        """

    def list_member_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListMemberAccountsResponseTypeDef:
        """
        Returns a `MemberAccounts` object that lists the member accounts in the
        administrator's Amazon Web Services organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_member_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_member_accounts)
        """

    def list_policies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        Returns an array of `PolicySummary` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_policies)
        """

    def list_protocols_lists(
        self, *, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListProtocolsListsResponseTypeDef:
        """
        Returns an array of `ProtocolsListDataSummary` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_protocols_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_protocols_lists)
        """

    def list_resource_set_resources(
        self, *, Identifier: str, MaxResults: int = None, NextToken: str = None
    ) -> ListResourceSetResourcesResponseTypeDef:
        """
        Returns an array of resources that are currently associated to a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_resource_set_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_resource_set_resources)
        """

    def list_resource_sets(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceSetsResponseTypeDef:
        """
        Returns an array of `ResourceSetSummary` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_resource_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_resource_sets)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags for the specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_tags_for_resource)
        """

    def list_third_party_firewall_firewall_policies(
        self, *, ThirdPartyFirewall: ThirdPartyFirewallType, MaxResults: int, NextToken: str = None
    ) -> ListThirdPartyFirewallFirewallPoliciesResponseTypeDef:
        """
        Retrieves a list of all of the third-party firewall policies that are associated
        with the third-party firewall administrator's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.list_third_party_firewall_firewall_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list_third_party_firewall_firewall_policies)
        """

    def put_admin_account(
        self, *, AdminAccount: str, AdminScope: "AdminScopeTypeDef" = None
    ) -> None:
        """
        Creates or updates an Firewall Manager administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_admin_account)
        """

    def put_apps_list(
        self, *, AppsList: "AppsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutAppsListResponseTypeDef:
        """
        Creates an Firewall Manager applications list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_apps_list)
        """

    def put_notification_channel(self, *, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        Designates the IAM role and Amazon Simple Notification Service (SNS) topic that
        Firewall Manager uses to record SNS logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_notification_channel)
        """

    def put_policy(
        self, *, Policy: "PolicyTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutPolicyResponseTypeDef:
        """
        Creates an Firewall Manager policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_policy)
        """

    def put_protocols_list(
        self, *, ProtocolsList: "ProtocolsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutProtocolsListResponseTypeDef:
        """
        Creates an Firewall Manager protocols list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_protocols_list)
        """

    def put_resource_set(
        self, *, ResourceSet: "ResourceSetTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutResourceSetResponseTypeDef:
        """
        Creates the resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.put_resource_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put_resource_set)
        """

    def tag_resource(self, *, ResourceArn: str, TagList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more tags to an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_admin_accounts_for_organization"]
    ) -> ListAdminAccountsForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListAdminAccountsForOrganization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listadminaccountsfororganizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_admins_managing_account"]
    ) -> ListAdminsManagingAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListAdminsManagingAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listadminsmanagingaccountpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps_lists"]) -> ListAppsListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListAppsLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listappslistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> ListComplianceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listcompliancestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listmemberaccountspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listpoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protocols_lists"]
    ) -> ListProtocolsListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListProtocolsLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listprotocolslistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_third_party_firewall_firewall_policies"]
    ) -> ListThirdPartyFirewallFirewallPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/fms.html#FMS.Paginator.ListThirdPartyFirewallFirewallPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listthirdpartyfirewallfirewallpoliciespaginator)
        """
