# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for elb service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_elb import ElasticLoadBalancingClient
    from mypy_boto3_elb.waiter import (
        AnyInstanceInServiceWaiter,
        InstanceDeregisteredWaiter,
        InstanceInServiceWaiter,
    )

    client: ElasticLoadBalancingClient = boto3.client("elb")

    any_instance_in_service_waiter: AnyInstanceInServiceWaiter = client.get_waiter("any_instance_in_service")
    instance_deregistered_waiter: InstanceDeregisteredWaiter = client.get_waiter("instance_deregistered")
    instance_in_service_waiter: InstanceInServiceWaiter = client.get_waiter("instance_in_service")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_elb.type_defs import InstanceTypeDef, WaiterConfigTypeDef

__all__ = ("AnyInstanceInServiceWaiter", "InstanceDeregisteredWaiter", "InstanceInServiceWaiter")


class AnyInstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)
    """

    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AnyInstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService.wait)
        """


class InstanceDeregisteredWaiter(Boto3Waiter):
    """
    [Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)
    """

    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceDeregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered.wait)
        """


class InstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)
    """

    def wait(
        self,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService.wait)
        """
