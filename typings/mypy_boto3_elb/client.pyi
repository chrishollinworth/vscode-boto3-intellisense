"""
Type annotations for elb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elb.client import ElasticLoadBalancingClient

    session = Session()
    client: ElasticLoadBalancingClient = session.client("elb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import DescribeAccountLimitsPaginator, DescribeLoadBalancersPaginator
from .type_defs import (
    AddAvailabilityZonesInputTypeDef,
    AddAvailabilityZonesOutputTypeDef,
    AddTagsInputTypeDef,
    ApplySecurityGroupsToLoadBalancerInputTypeDef,
    ApplySecurityGroupsToLoadBalancerOutputTypeDef,
    AttachLoadBalancerToSubnetsInputTypeDef,
    AttachLoadBalancerToSubnetsOutputTypeDef,
    ConfigureHealthCheckInputTypeDef,
    ConfigureHealthCheckOutputTypeDef,
    CreateAccessPointInputTypeDef,
    CreateAccessPointOutputTypeDef,
    CreateAppCookieStickinessPolicyInputTypeDef,
    CreateLBCookieStickinessPolicyInputTypeDef,
    CreateLoadBalancerListenerInputTypeDef,
    CreateLoadBalancerPolicyInputTypeDef,
    DeleteAccessPointInputTypeDef,
    DeleteLoadBalancerListenerInputTypeDef,
    DeleteLoadBalancerPolicyInputTypeDef,
    DeregisterEndPointsInputTypeDef,
    DeregisterEndPointsOutputTypeDef,
    DescribeAccessPointsInputTypeDef,
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsInputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeEndPointStateInputTypeDef,
    DescribeEndPointStateOutputTypeDef,
    DescribeLoadBalancerAttributesInputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancerPoliciesInputTypeDef,
    DescribeLoadBalancerPoliciesOutputTypeDef,
    DescribeLoadBalancerPolicyTypesInputTypeDef,
    DescribeLoadBalancerPolicyTypesOutputTypeDef,
    DescribeTagsInputTypeDef,
    DescribeTagsOutputTypeDef,
    DetachLoadBalancerFromSubnetsInputTypeDef,
    DetachLoadBalancerFromSubnetsOutputTypeDef,
    ModifyLoadBalancerAttributesInputTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    RegisterEndPointsInputTypeDef,
    RegisterEndPointsOutputTypeDef,
    RemoveAvailabilityZonesInputTypeDef,
    RemoveAvailabilityZonesOutputTypeDef,
    RemoveTagsInputTypeDef,
    SetLoadBalancerListenerSSLCertificateInputTypeDef,
    SetLoadBalancerPoliciesForBackendServerInputTypeDef,
    SetLoadBalancerPoliciesOfListenerInputTypeDef,
)
from .waiter import AnyInstanceInServiceWaiter, InstanceDeregisteredWaiter, InstanceInServiceWaiter

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

__all__ = ("ElasticLoadBalancingClient",)

class Exceptions(BaseClientExceptions):
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

class ElasticLoadBalancingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElasticLoadBalancingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#generate_presigned_url)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/add_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#add_tags)
        """

    def apply_security_groups_to_load_balancer(
        self, **kwargs: Unpack[ApplySecurityGroupsToLoadBalancerInputTypeDef]
    ) -> ApplySecurityGroupsToLoadBalancerOutputTypeDef:
        """
        Associates one or more security groups with your load balancer in a virtual
        private cloud (VPC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/apply_security_groups_to_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#apply_security_groups_to_load_balancer)
        """

    def attach_load_balancer_to_subnets(
        self, **kwargs: Unpack[AttachLoadBalancerToSubnetsInputTypeDef]
    ) -> AttachLoadBalancerToSubnetsOutputTypeDef:
        """
        Adds one or more subnets to the set of configured subnets for the specified
        load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/attach_load_balancer_to_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#attach_load_balancer_to_subnets)
        """

    def configure_health_check(
        self, **kwargs: Unpack[ConfigureHealthCheckInputTypeDef]
    ) -> ConfigureHealthCheckOutputTypeDef:
        """
        Specifies the health check settings to use when evaluating the health state of
        your EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/configure_health_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#configure_health_check)
        """

    def create_app_cookie_stickiness_policy(
        self, **kwargs: Unpack[CreateAppCookieStickinessPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Generates a stickiness policy with sticky session lifetimes that follow that of
        an application-generated cookie.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/create_app_cookie_stickiness_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#create_app_cookie_stickiness_policy)
        """

    def create_lb_cookie_stickiness_policy(
        self, **kwargs: Unpack[CreateLBCookieStickinessPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Generates a stickiness policy with sticky session lifetimes controlled by the
        lifetime of the browser (user-agent) or a specified expiration period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/create_lb_cookie_stickiness_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#create_lb_cookie_stickiness_policy)
        """

    def create_load_balancer(
        self, **kwargs: Unpack[CreateAccessPointInputTypeDef]
    ) -> CreateAccessPointOutputTypeDef:
        """
        Creates a Classic Load Balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/create_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#create_load_balancer)
        """

    def create_load_balancer_listeners(
        self, **kwargs: Unpack[CreateLoadBalancerListenerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates one or more listeners for the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/create_load_balancer_listeners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#create_load_balancer_listeners)
        """

    def create_load_balancer_policy(
        self, **kwargs: Unpack[CreateLoadBalancerPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a policy with the specified attributes for the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/create_load_balancer_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#create_load_balancer_policy)
        """

    def delete_load_balancer(
        self, **kwargs: Unpack[DeleteAccessPointInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/delete_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#delete_load_balancer)
        """

    def delete_load_balancer_listeners(
        self, **kwargs: Unpack[DeleteLoadBalancerListenerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified listeners from the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/delete_load_balancer_listeners.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#delete_load_balancer_listeners)
        """

    def delete_load_balancer_policy(
        self, **kwargs: Unpack[DeleteLoadBalancerPolicyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified policy from the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/delete_load_balancer_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#delete_load_balancer_policy)
        """

    def deregister_instances_from_load_balancer(
        self, **kwargs: Unpack[DeregisterEndPointsInputTypeDef]
    ) -> DeregisterEndPointsOutputTypeDef:
        """
        Deregisters the specified instances from the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/deregister_instances_from_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#deregister_instances_from_load_balancer)
        """

    def describe_account_limits(
        self, **kwargs: Unpack[DescribeAccountLimitsInputTypeDef]
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        Describes the current Elastic Load Balancing resource limits for your AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_account_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_account_limits)
        """

    def describe_instance_health(
        self, **kwargs: Unpack[DescribeEndPointStateInputTypeDef]
    ) -> DescribeEndPointStateOutputTypeDef:
        """
        Describes the state of the specified instances with respect to the specified
        load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_instance_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_instance_health)
        """

    def describe_load_balancer_attributes(
        self, **kwargs: Unpack[DescribeLoadBalancerAttributesInputTypeDef]
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        Describes the attributes for the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_load_balancer_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_load_balancer_attributes)
        """

    def describe_load_balancer_policies(
        self, **kwargs: Unpack[DescribeLoadBalancerPoliciesInputTypeDef]
    ) -> DescribeLoadBalancerPoliciesOutputTypeDef:
        """
        Describes the specified policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_load_balancer_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_load_balancer_policies)
        """

    def describe_load_balancer_policy_types(
        self, **kwargs: Unpack[DescribeLoadBalancerPolicyTypesInputTypeDef]
    ) -> DescribeLoadBalancerPolicyTypesOutputTypeDef:
        """
        Describes the specified load balancer policy types or all load balancer policy
        types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_load_balancer_policy_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_load_balancer_policy_types)
        """

    def describe_load_balancers(
        self, **kwargs: Unpack[DescribeAccessPointsInputTypeDef]
    ) -> DescribeAccessPointsOutputTypeDef:
        """
        Describes the specified the load balancers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_load_balancers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_load_balancers)
        """

    def describe_tags(
        self, **kwargs: Unpack[DescribeTagsInputTypeDef]
    ) -> DescribeTagsOutputTypeDef:
        """
        Describes the tags associated with the specified load balancers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/describe_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#describe_tags)
        """

    def detach_load_balancer_from_subnets(
        self, **kwargs: Unpack[DetachLoadBalancerFromSubnetsInputTypeDef]
    ) -> DetachLoadBalancerFromSubnetsOutputTypeDef:
        """
        Removes the specified subnets from the set of configured subnets for the load
        balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/detach_load_balancer_from_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#detach_load_balancer_from_subnets)
        """

    def disable_availability_zones_for_load_balancer(
        self, **kwargs: Unpack[RemoveAvailabilityZonesInputTypeDef]
    ) -> RemoveAvailabilityZonesOutputTypeDef:
        """
        Removes the specified Availability Zones from the set of Availability Zones for
        the specified load balancer in EC2-Classic or a default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/disable_availability_zones_for_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#disable_availability_zones_for_load_balancer)
        """

    def enable_availability_zones_for_load_balancer(
        self, **kwargs: Unpack[AddAvailabilityZonesInputTypeDef]
    ) -> AddAvailabilityZonesOutputTypeDef:
        """
        Adds the specified Availability Zones to the set of Availability Zones for the
        specified load balancer in EC2-Classic or a default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/enable_availability_zones_for_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#enable_availability_zones_for_load_balancer)
        """

    def modify_load_balancer_attributes(
        self, **kwargs: Unpack[ModifyLoadBalancerAttributesInputTypeDef]
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        Modifies the attributes of the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/modify_load_balancer_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#modify_load_balancer_attributes)
        """

    def register_instances_with_load_balancer(
        self, **kwargs: Unpack[RegisterEndPointsInputTypeDef]
    ) -> RegisterEndPointsOutputTypeDef:
        """
        Adds the specified instances to the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/register_instances_with_load_balancer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#register_instances_with_load_balancer)
        """

    def remove_tags(self, **kwargs: Unpack[RemoveTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/remove_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#remove_tags)
        """

    def set_load_balancer_listener_ssl_certificate(
        self, **kwargs: Unpack[SetLoadBalancerListenerSSLCertificateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the certificate that terminates the specified listener's SSL connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/set_load_balancer_listener_ssl_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#set_load_balancer_listener_ssl_certificate)
        """

    def set_load_balancer_policies_for_backend_server(
        self, **kwargs: Unpack[SetLoadBalancerPoliciesForBackendServerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Replaces the set of policies associated with the specified port on which the
        EC2 instance is listening with a new set of policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/set_load_balancer_policies_for_backend_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#set_load_balancer_policies_for_backend_server)
        """

    def set_load_balancer_policies_of_listener(
        self, **kwargs: Unpack[SetLoadBalancerPoliciesOfListenerInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Replaces the current set of policies for the specified load balancer port with
        the specified set of policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/set_load_balancer_policies_of_listener.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#set_load_balancer_policies_of_listener)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_load_balancers"]
    ) -> DescribeLoadBalancersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["any_instance_in_service"]
    ) -> AnyInstanceInServiceWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_deregistered"]
    ) -> InstanceDeregisteredWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_in_service"]
    ) -> InstanceInServiceWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/client/#get_waiter)
        """
