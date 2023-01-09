"""
Type annotations for network-firewall service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_network_firewall import NetworkFirewallClient

    client: NetworkFirewallClient = boto3.client("network-firewall")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ResourceManagedStatusType, ResourceManagedTypeType, RuleGroupTypeType
from .paginator import (
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFirewallPolicyResponseTypeDef,
    AssociateSubnetsResponseTypeDef,
    CreateFirewallPolicyResponseTypeDef,
    CreateFirewallResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    DeleteFirewallPolicyResponseTypeDef,
    DeleteFirewallResponseTypeDef,
    DeleteRuleGroupResponseTypeDef,
    DescribeFirewallPolicyResponseTypeDef,
    DescribeFirewallResponseTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRuleGroupMetadataResponseTypeDef,
    DescribeRuleGroupResponseTypeDef,
    DisassociateSubnetsResponseTypeDef,
    EncryptionConfigurationTypeDef,
    FirewallPolicyTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigurationTypeDef,
    RuleGroupTypeDef,
    SourceMetadataTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    UpdateFirewallDeleteProtectionResponseTypeDef,
    UpdateFirewallDescriptionResponseTypeDef,
    UpdateFirewallEncryptionConfigurationResponseTypeDef,
    UpdateFirewallPolicyChangeProtectionResponseTypeDef,
    UpdateFirewallPolicyResponseTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateSubnetChangeProtectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NetworkFirewallClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourcePolicyException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LogDestinationPermissionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceOwnerCheckException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class NetworkFirewallClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkFirewallClient exceptions.
        """
    def associate_firewall_policy(
        self,
        *,
        FirewallPolicyArn: str,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> AssociateFirewallPolicyResponseTypeDef:
        """
        Associates a  FirewallPolicy to a  Firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.associate_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_firewall_policy)
        """
    def associate_subnets(
        self,
        *,
        SubnetMappings: List["SubnetMappingTypeDef"],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> AssociateSubnetsResponseTypeDef:
        """
        Associates the specified subnets in the Amazon VPC to the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.associate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_subnets)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#close)
        """
    def create_firewall(
        self,
        *,
        FirewallName: str,
        FirewallPolicyArn: str,
        VpcId: str,
        SubnetMappings: List["SubnetMappingTypeDef"],
        DeleteProtection: bool = None,
        SubnetChangeProtection: bool = None,
        FirewallPolicyChangeProtection: bool = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None
    ) -> CreateFirewallResponseTypeDef:
        """
        Creates an Network Firewall  Firewall and accompanying  FirewallStatus for a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall)
        """
    def create_firewall_policy(
        self,
        *,
        FirewallPolicyName: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None
    ) -> CreateFirewallPolicyResponseTypeDef:
        """
        Creates the firewall policy for the firewall according to the specifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall_policy)
        """
    def create_rule_group(
        self,
        *,
        RuleGroupName: str,
        Type: RuleGroupTypeType,
        Capacity: int,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None,
        SourceMetadata: "SourceMetadataTypeDef" = None
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates the specified stateless or stateful rule group, which includes the rules
        for network traffic inspection, a capacity setting, and tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_rule_group)
        """
    def delete_firewall(
        self, *, FirewallName: str = None, FirewallArn: str = None
    ) -> DeleteFirewallResponseTypeDef:
        """
        Deletes the specified  Firewall and its  FirewallStatus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall)
        """
    def delete_firewall_policy(
        self, *, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DeleteFirewallPolicyResponseTypeDef:
        """
        Deletes the specified  FirewallPolicy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall_policy)
        """
    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes a resource policy that you created in a  PutResourcePolicy request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_resource_policy)
        """
    def delete_rule_group(
        self, *, RuleGroupName: str = None, RuleGroupArn: str = None, Type: RuleGroupTypeType = None
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        Deletes the specified  RuleGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_rule_group)
        """
    def describe_firewall(
        self, *, FirewallName: str = None, FirewallArn: str = None
    ) -> DescribeFirewallResponseTypeDef:
        """
        Returns the data objects for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall)
        """
    def describe_firewall_policy(
        self, *, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DescribeFirewallPolicyResponseTypeDef:
        """
        Returns the data objects for the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall_policy)
        """
    def describe_logging_configuration(
        self, *, FirewallArn: str = None, FirewallName: str = None
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Returns the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_logging_configuration)
        """
    def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves a resource policy that you created in a  PutResourcePolicy request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_resource_policy)
        """
    def describe_rule_group(
        self, *, RuleGroupName: str = None, RuleGroupArn: str = None, Type: RuleGroupTypeType = None
    ) -> DescribeRuleGroupResponseTypeDef:
        """
        Returns the data objects for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_rule_group)
        """
    def describe_rule_group_metadata(
        self, *, RuleGroupName: str = None, RuleGroupArn: str = None, Type: RuleGroupTypeType = None
    ) -> DescribeRuleGroupMetadataResponseTypeDef:
        """
        High-level information about a rule group, returned by operations like create
        and describe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_rule_group_metadata)
        """
    def disassociate_subnets(
        self,
        *,
        SubnetIds: List[str],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> DisassociateSubnetsResponseTypeDef:
        """
        Removes the specified subnet associations from the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.disassociate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#disassociate_subnets)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#generate_presigned_url)
        """
    def list_firewall_policies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListFirewallPoliciesResponseTypeDef:
        """
        Retrieves the metadata for the firewall policies that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewall_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewall_policies)
        """
    def list_firewalls(
        self, *, NextToken: str = None, VpcIds: List[str] = None, MaxResults: int = None
    ) -> ListFirewallsResponseTypeDef:
        """
        Retrieves the metadata for the firewalls that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewalls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewalls)
        """
    def list_rule_groups(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Scope: ResourceManagedStatusType = None,
        ManagedType: ResourceManagedTypeType = None,
        Type: RuleGroupTypeType = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves the metadata for the rule groups that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_rule_groups)
        """
    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_tags_for_resource)
        """
    def put_resource_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        Creates or updates an IAM policy for your rule group or firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#put_resource_policy)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#untag_resource)
        """
    def update_firewall_delete_protection(
        self,
        *,
        DeleteProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateFirewallDeleteProtectionResponseTypeDef:
        """
        Modifies the flag, `DeleteProtection` , which indicates whether it is possible
        to delete the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_delete_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_delete_protection)
        """
    def update_firewall_description(
        self,
        *,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
        Description: str = None
    ) -> UpdateFirewallDescriptionResponseTypeDef:
        """
        Modifies the description for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_description)
        """
    def update_firewall_encryption_configuration(
        self,
        *,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None
    ) -> UpdateFirewallEncryptionConfigurationResponseTypeDef:
        """
        A complex type that contains settings for encryption of your firewall resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_encryption_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_encryption_configuration)
        """
    def update_firewall_policy(
        self,
        *,
        UpdateToken: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        FirewallPolicyArn: str = None,
        FirewallPolicyName: str = None,
        Description: str = None,
        DryRun: bool = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None
    ) -> UpdateFirewallPolicyResponseTypeDef:
        """
        Updates the properties of the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy)
        """
    def update_firewall_policy_change_protection(
        self,
        *,
        FirewallPolicyChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
        """
        Modifies the flag, `ChangeProtection` , which indicates whether it is possible
        to change the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy_change_protection)
        """
    def update_logging_configuration(
        self,
        *,
        FirewallArn: str = None,
        FirewallName: str = None,
        LoggingConfiguration: "LoggingConfigurationTypeDef" = None
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Sets the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_logging_configuration)
        """
    def update_rule_group(
        self,
        *,
        UpdateToken: str,
        RuleGroupArn: str = None,
        RuleGroupName: str = None,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Type: RuleGroupTypeType = None,
        Description: str = None,
        DryRun: bool = None,
        EncryptionConfiguration: "EncryptionConfigurationTypeDef" = None,
        SourceMetadata: "SourceMetadataTypeDef" = None
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the rule settings for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_rule_group)
        """
    def update_subnet_change_protection(
        self,
        *,
        SubnetChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None
    ) -> UpdateSubnetChangeProtectionResponseTypeDef:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/network-
        firewall-2020-11-12/UpdateSubnetChangeProtection>`_ **Request Syntax** response
        = client.update_subnet_change_protection( UpdateToken='string',
        FirewallArn='string', FirewallName='string',...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Client.update_subnet_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_subnet_change_protection)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_policies"]
    ) -> ListFirewallPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallpoliciespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_firewalls"]) -> ListFirewallsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_rule_groups"]) -> ListRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listrulegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtagsforresourcepaginator)
        """
