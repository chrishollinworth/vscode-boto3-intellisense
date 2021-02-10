"""
Main interface for network-firewall service client

Usage::

    ```python
    import boto3
    from mypy_boto3_network_firewall import NetworkFirewallClient

    client: NetworkFirewallClient = boto3.client("network-firewall")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_network_firewall.paginator import (
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_network_firewall.type_defs import (
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
    DescribeRuleGroupResponseTypeDef,
    DisassociateSubnetsResponseTypeDef,
    FirewallPolicyTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigurationTypeDef,
    RuleGroupTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    UpdateFirewallDeleteProtectionResponseTypeDef,
    UpdateFirewallDescriptionResponseTypeDef,
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


class NetworkFirewallClient:
    """
    [NetworkFirewall.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_firewall_policy(
        self,
        FirewallPolicyArn: str,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> AssociateFirewallPolicyResponseTypeDef:
        """
        [Client.associate_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.associate_firewall_policy)
        """

    def associate_subnets(
        self,
        SubnetMappings: List["SubnetMappingTypeDef"],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> AssociateSubnetsResponseTypeDef:
        """
        [Client.associate_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.associate_subnets)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.can_paginate)
        """

    def create_firewall(
        self,
        FirewallName: str,
        FirewallPolicyArn: str,
        VpcId: str,
        SubnetMappings: List["SubnetMappingTypeDef"],
        DeleteProtection: bool = None,
        SubnetChangeProtection: bool = None,
        FirewallPolicyChangeProtection: bool = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateFirewallResponseTypeDef:
        """
        [Client.create_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall)
        """

    def create_firewall_policy(
        self,
        FirewallPolicyName: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateFirewallPolicyResponseTypeDef:
        """
        [Client.create_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall_policy)
        """

    def create_rule_group(
        self,
        RuleGroupName: str,
        Type: Literal["STATELESS", "STATEFUL"],
        Capacity: int,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.create_rule_group)
        """

    def delete_firewall(
        self, FirewallName: str = None, FirewallArn: str = None
    ) -> DeleteFirewallResponseTypeDef:
        """
        [Client.delete_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall)
        """

    def delete_firewall_policy(
        self, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DeleteFirewallPolicyResponseTypeDef:
        """
        [Client.delete_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall_policy)
        """

    def delete_resource_policy(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.delete_resource_policy)
        """

    def delete_rule_group(
        self,
        RuleGroupName: str = None,
        RuleGroupArn: str = None,
        Type: Literal["STATELESS", "STATEFUL"] = None,
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.delete_rule_group)
        """

    def describe_firewall(
        self, FirewallName: str = None, FirewallArn: str = None
    ) -> DescribeFirewallResponseTypeDef:
        """
        [Client.describe_firewall documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall)
        """

    def describe_firewall_policy(
        self, FirewallPolicyName: str = None, FirewallPolicyArn: str = None
    ) -> DescribeFirewallPolicyResponseTypeDef:
        """
        [Client.describe_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall_policy)
        """

    def describe_logging_configuration(
        self, FirewallArn: str = None, FirewallName: str = None
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        [Client.describe_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.describe_logging_configuration)
        """

    def describe_resource_policy(self, ResourceArn: str) -> DescribeResourcePolicyResponseTypeDef:
        """
        [Client.describe_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.describe_resource_policy)
        """

    def describe_rule_group(
        self,
        RuleGroupName: str = None,
        RuleGroupArn: str = None,
        Type: Literal["STATELESS", "STATEFUL"] = None,
    ) -> DescribeRuleGroupResponseTypeDef:
        """
        [Client.describe_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group)
        """

    def disassociate_subnets(
        self,
        SubnetIds: List[str],
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> DisassociateSubnetsResponseTypeDef:
        """
        [Client.disassociate_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.disassociate_subnets)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.generate_presigned_url)
        """

    def list_firewall_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListFirewallPoliciesResponseTypeDef:
        """
        [Client.list_firewall_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewall_policies)
        """

    def list_firewalls(
        self, NextToken: str = None, VpcIds: List[str] = None, MaxResults: int = None
    ) -> ListFirewallsResponseTypeDef:
        """
        [Client.list_firewalls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewalls)
        """

    def list_rule_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.list_rule_groups)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.list_tags_for_resource)
        """

    def put_resource_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.put_resource_policy)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.untag_resource)
        """

    def update_firewall_delete_protection(
        self,
        DeleteProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> UpdateFirewallDeleteProtectionResponseTypeDef:
        """
        [Client.update_firewall_delete_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_delete_protection)
        """

    def update_firewall_description(
        self,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
        Description: str = None,
    ) -> UpdateFirewallDescriptionResponseTypeDef:
        """
        [Client.update_firewall_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_description)
        """

    def update_firewall_policy(
        self,
        UpdateToken: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        FirewallPolicyArn: str = None,
        FirewallPolicyName: str = None,
        Description: str = None,
        DryRun: bool = None,
    ) -> UpdateFirewallPolicyResponseTypeDef:
        """
        [Client.update_firewall_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy)
        """

    def update_firewall_policy_change_protection(
        self,
        FirewallPolicyChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
        """
        [Client.update_firewall_policy_change_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy_change_protection)
        """

    def update_logging_configuration(
        self,
        FirewallArn: str = None,
        FirewallName: str = None,
        LoggingConfiguration: "LoggingConfigurationTypeDef" = None,
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        [Client.update_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_logging_configuration)
        """

    def update_rule_group(
        self,
        UpdateToken: str,
        RuleGroupArn: str = None,
        RuleGroupName: str = None,
        RuleGroup: "RuleGroupTypeDef" = None,
        Rules: str = None,
        Type: Literal["STATELESS", "STATEFUL"] = None,
        Description: str = None,
        DryRun: bool = None,
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_rule_group)
        """

    def update_subnet_change_protection(
        self,
        SubnetChangeProtection: bool,
        UpdateToken: str = None,
        FirewallArn: str = None,
        FirewallName: str = None,
    ) -> UpdateSubnetChangeProtectionResponseTypeDef:
        """
        [Client.update_subnet_change_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Client.update_subnet_change_protection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_policies"]
    ) -> ListFirewallPoliciesPaginator:
        """
        [Paginator.ListFirewallPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_firewalls"]) -> ListFirewallsPaginator:
        """
        [Paginator.ListFirewalls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rule_groups"]) -> ListRuleGroupsPaginator:
        """
        [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
        """
