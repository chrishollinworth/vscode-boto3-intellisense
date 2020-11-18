# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for elbv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elbv2 import ElasticLoadBalancingv2Client

    client: ElasticLoadBalancingv2Client = boto3.client("elbv2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_elbv2.paginator import (
    DescribeAccountLimitsPaginator,
    DescribeListenerCertificatesPaginator,
    DescribeListenersPaginator,
    DescribeLoadBalancersPaginator,
    DescribeRulesPaginator,
    DescribeSSLPoliciesPaginator,
    DescribeTargetGroupsPaginator,
)
from mypy_boto3_elbv2.type_defs import (
    ActionTypeDef,
    AddListenerCertificatesOutputTypeDef,
    CertificateTypeDef,
    CreateListenerOutputTypeDef,
    CreateLoadBalancerOutputTypeDef,
    CreateRuleOutputTypeDef,
    CreateTargetGroupOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTagsOutputTypeDef,
    DescribeTargetGroupAttributesOutputTypeDef,
    DescribeTargetGroupsOutputTypeDef,
    DescribeTargetHealthOutputTypeDef,
    LoadBalancerAttributeTypeDef,
    MatcherTypeDef,
    ModifyListenerOutputTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    ModifyRuleOutputTypeDef,
    ModifyTargetGroupAttributesOutputTypeDef,
    ModifyTargetGroupOutputTypeDef,
    RuleConditionTypeDef,
    RulePriorityPairTypeDef,
    SetIpAddressTypeOutputTypeDef,
    SetRulePrioritiesOutputTypeDef,
    SetSecurityGroupsOutputTypeDef,
    SetSubnetsOutputTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    TargetDescriptionTypeDef,
    TargetGroupAttributeTypeDef,
)
from mypy_boto3_elbv2.waiter import (
    LoadBalancerAvailableWaiter,
    LoadBalancerExistsWaiter,
    LoadBalancersDeletedWaiter,
    TargetDeregisteredWaiter,
    TargetInServiceWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingv2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ALPNPolicyNotSupportedException: Type[BotocoreClientError]
    AllocationIdNotFoundException: Type[BotocoreClientError]
    AvailabilityZoneNotSupportedException: Type[BotocoreClientError]
    CertificateNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicateListenerException: Type[BotocoreClientError]
    DuplicateLoadBalancerNameException: Type[BotocoreClientError]
    DuplicateTagKeysException: Type[BotocoreClientError]
    DuplicateTargetGroupNameException: Type[BotocoreClientError]
    HealthUnavailableException: Type[BotocoreClientError]
    IncompatibleProtocolsException: Type[BotocoreClientError]
    InvalidConfigurationRequestException: Type[BotocoreClientError]
    InvalidLoadBalancerActionException: Type[BotocoreClientError]
    InvalidSchemeException: Type[BotocoreClientError]
    InvalidSecurityGroupException: Type[BotocoreClientError]
    InvalidSubnetException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]
    LoadBalancerNotFoundException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    PriorityInUseException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    RuleNotFoundException: Type[BotocoreClientError]
    SSLPolicyNotFoundException: Type[BotocoreClientError]
    SubnetNotFoundException: Type[BotocoreClientError]
    TargetGroupAssociationLimitException: Type[BotocoreClientError]
    TargetGroupNotFoundException: Type[BotocoreClientError]
    TooManyActionsException: Type[BotocoreClientError]
    TooManyCertificatesException: Type[BotocoreClientError]
    TooManyListenersException: Type[BotocoreClientError]
    TooManyLoadBalancersException: Type[BotocoreClientError]
    TooManyRegistrationsForTargetIdException: Type[BotocoreClientError]
    TooManyRulesException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    TooManyTargetGroupsException: Type[BotocoreClientError]
    TooManyTargetsException: Type[BotocoreClientError]
    TooManyUniqueTargetGroupsPerLoadBalancerException: Type[BotocoreClientError]
    UnsupportedProtocolException: Type[BotocoreClientError]


class ElasticLoadBalancingv2Client:
    """
    [ElasticLoadBalancingv2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_listener_certificates(
        self, ListenerArn: str, Certificates: List["CertificateTypeDef"]
    ) -> AddListenerCertificatesOutputTypeDef:
        """
        [Client.add_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_listener_certificates)
        """

    def add_tags(self, ResourceArns: List[str], Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.can_paginate)
        """

    def create_listener(
        self,
        LoadBalancerArn: str,
        DefaultActions: List["ActionTypeDef"],
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP", "GENEVE"] = None,
        Port: int = None,
        SslPolicy: str = None,
        Certificates: List["CertificateTypeDef"] = None,
        AlpnPolicy: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateListenerOutputTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_listener)
        """

    def create_load_balancer(
        self,
        Name: str,
        Subnets: List[str] = None,
        SubnetMappings: List[SubnetMappingTypeDef] = None,
        SecurityGroups: List[str] = None,
        Scheme: Literal["internet-facing", "internal"] = None,
        Tags: List["TagTypeDef"] = None,
        Type: Literal["application", "network", "gateway"] = None,
        IpAddressType: Literal["ipv4", "dualstack"] = None,
        CustomerOwnedIpv4Pool: str = None,
    ) -> CreateLoadBalancerOutputTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_load_balancer)
        """

    def create_rule(
        self,
        ListenerArn: str,
        Conditions: List["RuleConditionTypeDef"],
        Priority: int,
        Actions: List["ActionTypeDef"],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRuleOutputTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_rule)
        """

    def create_target_group(
        self,
        Name: str,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP", "GENEVE"] = None,
        ProtocolVersion: str = None,
        Port: int = None,
        VpcId: str = None,
        HealthCheckProtocol: Literal[
            "HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP", "GENEVE"
        ] = None,
        HealthCheckPort: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: "MatcherTypeDef" = None,
        TargetType: Literal["instance", "ip", "lambda"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTargetGroupOutputTypeDef:
        """
        [Client.create_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_target_group)
        """

    def delete_listener(self, ListenerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_listener)
        """

    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_load_balancer)
        """

    def delete_rule(self, RuleArn: str) -> Dict[str, Any]:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_rule)
        """

    def delete_target_group(self, TargetGroupArn: str) -> Dict[str, Any]:
        """
        [Client.delete_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_target_group)
        """

    def deregister_targets(
        self, TargetGroupArn: str, Targets: List["TargetDescriptionTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.deregister_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.deregister_targets)
        """

    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_account_limits)
        """

    def describe_listener_certificates(
        self, ListenerArn: str, Marker: str = None, PageSize: int = None
    ) -> DescribeListenerCertificatesOutputTypeDef:
        """
        [Client.describe_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listener_certificates)
        """

    def describe_listeners(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeListenersOutputTypeDef:
        """
        [Client.describe_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listeners)
        """

    def describe_load_balancer_attributes(
        self, LoadBalancerArn: str
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancer_attributes)
        """

    def describe_load_balancers(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeLoadBalancersOutputTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers)
        """

    def describe_rules(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeRulesOutputTypeDef:
        """
        [Client.describe_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_rules)
        """

    def describe_ssl_policies(
        self, Names: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> DescribeSSLPoliciesOutputTypeDef:
        """
        [Client.describe_ssl_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_ssl_policies)
        """

    def describe_tags(self, ResourceArns: List[str]) -> DescribeTagsOutputTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_tags)
        """

    def describe_target_group_attributes(
        self, TargetGroupArn: str
    ) -> DescribeTargetGroupAttributesOutputTypeDef:
        """
        [Client.describe_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_group_attributes)
        """

    def describe_target_groups(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeTargetGroupsOutputTypeDef:
        """
        [Client.describe_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_groups)
        """

    def describe_target_health(
        self, TargetGroupArn: str, Targets: List["TargetDescriptionTypeDef"] = None
    ) -> DescribeTargetHealthOutputTypeDef:
        """
        [Client.describe_target_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.generate_presigned_url)
        """

    def modify_listener(
        self,
        ListenerArn: str,
        Port: int = None,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP", "GENEVE"] = None,
        SslPolicy: str = None,
        Certificates: List["CertificateTypeDef"] = None,
        DefaultActions: List["ActionTypeDef"] = None,
        AlpnPolicy: List[str] = None,
    ) -> ModifyListenerOutputTypeDef:
        """
        [Client.modify_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_listener)
        """

    def modify_load_balancer_attributes(
        self, LoadBalancerArn: str, Attributes: List["LoadBalancerAttributeTypeDef"]
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_load_balancer_attributes)
        """

    def modify_rule(
        self,
        RuleArn: str,
        Conditions: List["RuleConditionTypeDef"] = None,
        Actions: List["ActionTypeDef"] = None,
    ) -> ModifyRuleOutputTypeDef:
        """
        [Client.modify_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_rule)
        """

    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: Literal[
            "HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP", "GENEVE"
        ] = None,
        HealthCheckPort: str = None,
        HealthCheckPath: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: "MatcherTypeDef" = None,
    ) -> ModifyTargetGroupOutputTypeDef:
        """
        [Client.modify_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group)
        """

    def modify_target_group_attributes(
        self, TargetGroupArn: str, Attributes: List["TargetGroupAttributeTypeDef"]
    ) -> ModifyTargetGroupAttributesOutputTypeDef:
        """
        [Client.modify_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group_attributes)
        """

    def register_targets(
        self, TargetGroupArn: str, Targets: List["TargetDescriptionTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.register_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.register_targets)
        """

    def remove_listener_certificates(
        self, ListenerArn: str, Certificates: List["CertificateTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.remove_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_listener_certificates)
        """

    def remove_tags(self, ResourceArns: List[str], TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_tags)
        """

    def set_ip_address_type(
        self, LoadBalancerArn: str, IpAddressType: Literal["ipv4", "dualstack"]
    ) -> SetIpAddressTypeOutputTypeDef:
        """
        [Client.set_ip_address_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_ip_address_type)
        """

    def set_rule_priorities(
        self, RulePriorities: List[RulePriorityPairTypeDef]
    ) -> SetRulePrioritiesOutputTypeDef:
        """
        [Client.set_rule_priorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_rule_priorities)
        """

    def set_security_groups(
        self, LoadBalancerArn: str, SecurityGroups: List[str]
    ) -> SetSecurityGroupsOutputTypeDef:
        """
        [Client.set_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_security_groups)
        """

    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: List[str] = None,
        SubnetMappings: List[SubnetMappingTypeDef] = None,
        IpAddressType: Literal["ipv4", "dualstack"] = None,
    ) -> SetSubnetsOutputTypeDef:
        """
        [Client.set_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_subnets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_listener_certificates"]
    ) -> DescribeListenerCertificatesPaginator:
        """
        [Paginator.DescribeListenerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_listeners"]
    ) -> DescribeListenersPaginator:
        """
        [Paginator.DescribeListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> DescribeLoadBalancersPaginator:
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_rules"]) -> DescribeRulesPaginator:
        """
        [Paginator.DescribeRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ssl_policies"]
    ) -> DescribeSSLPoliciesPaginator:
        """
        [Paginator.DescribeSSLPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_target_groups"]
    ) -> DescribeTargetGroupsPaginator:
        """
        [Paginator.DescribeTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["load_balancer_available"]
    ) -> LoadBalancerAvailableWaiter:
        """
        [Waiter.LoadBalancerAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["load_balancer_exists"]) -> LoadBalancerExistsWaiter:
        """
        [Waiter.LoadBalancerExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["load_balancers_deleted"]
    ) -> LoadBalancersDeletedWaiter:
        """
        [Waiter.LoadBalancersDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["target_deregistered"]) -> TargetDeregisteredWaiter:
        """
        [Waiter.TargetDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["target_in_service"]) -> TargetInServiceWaiter:
        """
        [Waiter.TargetInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
        """
