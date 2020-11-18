# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for elb service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elb import ElasticLoadBalancingClient

    client: ElasticLoadBalancingClient = boto3.client("elb")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_elb.paginator import DescribeAccountLimitsPaginator, DescribeLoadBalancersPaginator
from mypy_boto3_elb.type_defs import (
    AddAvailabilityZonesOutputTypeDef,
    ApplySecurityGroupsToLoadBalancerOutputTypeDef,
    AttachLoadBalancerToSubnetsOutputTypeDef,
    ConfigureHealthCheckOutputTypeDef,
    CreateAccessPointOutputTypeDef,
    DeregisterEndPointsOutputTypeDef,
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeEndPointStateOutputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancerPoliciesOutputTypeDef,
    DescribeLoadBalancerPolicyTypesOutputTypeDef,
    DescribeTagsOutputTypeDef,
    DetachLoadBalancerFromSubnetsOutputTypeDef,
    HealthCheckTypeDef,
    InstanceTypeDef,
    ListenerTypeDef,
    LoadBalancerAttributesTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    PolicyAttributeTypeDef,
    RegisterEndPointsOutputTypeDef,
    RemoveAvailabilityZonesOutputTypeDef,
    TagKeyOnlyTypeDef,
    TagTypeDef,
)
from mypy_boto3_elb.waiter import (
    AnyInstanceInServiceWaiter,
    InstanceDeregisteredWaiter,
    InstanceInServiceWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessPointNotFoundException: Type[BotocoreClientError]
    CertificateNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyThrottleException: Type[BotocoreClientError]
    DuplicateAccessPointNameException: Type[BotocoreClientError]
    DuplicateListenerException: Type[BotocoreClientError]
    DuplicatePolicyNameException: Type[BotocoreClientError]
    DuplicateTagKeysException: Type[BotocoreClientError]
    InvalidConfigurationRequestException: Type[BotocoreClientError]
    InvalidEndPointException: Type[BotocoreClientError]
    InvalidSchemeException: Type[BotocoreClientError]
    InvalidSecurityGroupException: Type[BotocoreClientError]
    InvalidSubnetException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]
    LoadBalancerAttributeNotFoundException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]
    PolicyTypeNotFoundException: Type[BotocoreClientError]
    SubnetNotFoundException: Type[BotocoreClientError]
    TooManyAccessPointsException: Type[BotocoreClientError]
    TooManyPoliciesException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedProtocolException: Type[BotocoreClientError]


class ElasticLoadBalancingClient:
    """
    [ElasticLoadBalancing.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(self, LoadBalancerNames: List[str], Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.add_tags)
        """

    def apply_security_groups_to_load_balancer(
        self, LoadBalancerName: str, SecurityGroups: List[str]
    ) -> ApplySecurityGroupsToLoadBalancerOutputTypeDef:
        """
        [Client.apply_security_groups_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.apply_security_groups_to_load_balancer)
        """

    def attach_load_balancer_to_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> AttachLoadBalancerToSubnetsOutputTypeDef:
        """
        [Client.attach_load_balancer_to_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.attach_load_balancer_to_subnets)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.can_paginate)
        """

    def configure_health_check(
        self, LoadBalancerName: str, HealthCheck: "HealthCheckTypeDef"
    ) -> ConfigureHealthCheckOutputTypeDef:
        """
        [Client.configure_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.configure_health_check)
        """

    def create_app_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieName: str
    ) -> Dict[str, Any]:
        """
        [Client.create_app_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.create_app_cookie_stickiness_policy)
        """

    def create_lb_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None
    ) -> Dict[str, Any]:
        """
        [Client.create_lb_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.create_lb_cookie_stickiness_policy)
        """

    def create_load_balancer(
        self,
        LoadBalancerName: str,
        Listeners: List["ListenerTypeDef"],
        AvailabilityZones: List[str] = None,
        Subnets: List[str] = None,
        SecurityGroups: List[str] = None,
        Scheme: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAccessPointOutputTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer)
        """

    def create_load_balancer_listeners(
        self, LoadBalancerName: str, Listeners: List["ListenerTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_listeners)
        """

    def create_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        PolicyTypeName: str,
        PolicyAttributes: List[PolicyAttributeTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_policy)
        """

    def delete_load_balancer(self, LoadBalancerName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer)
        """

    def delete_load_balancer_listeners(
        self, LoadBalancerName: str, LoadBalancerPorts: List[int]
    ) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_listeners)
        """

    def delete_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_policy)
        """

    def deregister_instances_from_load_balancer(
        self, LoadBalancerName: str, Instances: List["InstanceTypeDef"]
    ) -> DeregisterEndPointsOutputTypeDef:
        """
        [Client.deregister_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.deregister_instances_from_load_balancer)
        """

    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_account_limits)
        """

    def describe_instance_health(
        self, LoadBalancerName: str, Instances: List["InstanceTypeDef"] = None
    ) -> DescribeEndPointStateOutputTypeDef:
        """
        [Client.describe_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_instance_health)
        """

    def describe_load_balancer_attributes(
        self, LoadBalancerName: str
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_attributes)
        """

    def describe_load_balancer_policies(
        self, LoadBalancerName: str = None, PolicyNames: List[str] = None
    ) -> DescribeLoadBalancerPoliciesOutputTypeDef:
        """
        [Client.describe_load_balancer_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policies)
        """

    def describe_load_balancer_policy_types(
        self, PolicyTypeNames: List[str] = None
    ) -> DescribeLoadBalancerPolicyTypesOutputTypeDef:
        """
        [Client.describe_load_balancer_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policy_types)
        """

    def describe_load_balancers(
        self, LoadBalancerNames: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> DescribeAccessPointsOutputTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancers)
        """

    def describe_tags(self, LoadBalancerNames: List[str]) -> DescribeTagsOutputTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.describe_tags)
        """

    def detach_load_balancer_from_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> DetachLoadBalancerFromSubnetsOutputTypeDef:
        """
        [Client.detach_load_balancer_from_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.detach_load_balancer_from_subnets)
        """

    def disable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> RemoveAvailabilityZonesOutputTypeDef:
        """
        [Client.disable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.disable_availability_zones_for_load_balancer)
        """

    def enable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> AddAvailabilityZonesOutputTypeDef:
        """
        [Client.enable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.enable_availability_zones_for_load_balancer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.generate_presigned_url)
        """

    def modify_load_balancer_attributes(
        self, LoadBalancerName: str, LoadBalancerAttributes: "LoadBalancerAttributesTypeDef"
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.modify_load_balancer_attributes)
        """

    def register_instances_with_load_balancer(
        self, LoadBalancerName: str, Instances: List["InstanceTypeDef"]
    ) -> RegisterEndPointsOutputTypeDef:
        """
        [Client.register_instances_with_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.register_instances_with_load_balancer)
        """

    def remove_tags(
        self, LoadBalancerNames: List[str], Tags: List[TagKeyOnlyTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.remove_tags)
        """

    def set_load_balancer_listener_ssl_certificate(
        self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_listener_ssl_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_listener_ssl_certificate)
        """

    def set_load_balancer_policies_for_backend_server(
        self, LoadBalancerName: str, InstancePort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_for_backend_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_for_backend_server)
        """

    def set_load_balancer_policies_of_listener(
        self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_of_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_of_listener)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> DescribeLoadBalancersPaginator:
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["any_instance_in_service"]
    ) -> AnyInstanceInServiceWaiter:
        """
        [Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_deregistered"]
    ) -> InstanceDeregisteredWaiter:
        """
        [Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_in_service"]) -> InstanceInServiceWaiter:
        """
        [Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)
        """
