# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for elbv2 service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_elbv2 import ElasticLoadBalancingv2Client
    from mypy_boto3_elbv2.waiter import (
        LoadBalancerAvailableWaiter,
        LoadBalancerExistsWaiter,
        LoadBalancersDeletedWaiter,
        TargetDeregisteredWaiter,
        TargetInServiceWaiter,
    )

    client: ElasticLoadBalancingv2Client = boto3.client("elbv2")

    load_balancer_available_waiter: LoadBalancerAvailableWaiter = client.get_waiter("load_balancer_available")
    load_balancer_exists_waiter: LoadBalancerExistsWaiter = client.get_waiter("load_balancer_exists")
    load_balancers_deleted_waiter: LoadBalancersDeletedWaiter = client.get_waiter("load_balancers_deleted")
    target_deregistered_waiter: TargetDeregisteredWaiter = client.get_waiter("target_deregistered")
    target_in_service_waiter: TargetInServiceWaiter = client.get_waiter("target_in_service")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_elbv2.type_defs import TargetDescriptionTypeDef, WaiterConfigTypeDef

__all__ = (
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)


class LoadBalancerAvailableWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancerAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
    """

    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancerAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable.wait)
        """


class LoadBalancerExistsWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancerExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
    """

    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancerExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists.wait)
        """


class LoadBalancersDeletedWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancersDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
    """

    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancersDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted.wait)
        """


class TargetDeregisteredWaiter(Boto3Waiter):
    """
    [Waiter.TargetDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
    """

    def wait(
        self,
        TargetGroupArn: str,
        Targets: List["TargetDescriptionTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TargetDeregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered.wait)
        """


class TargetInServiceWaiter(Boto3Waiter):
    """
    [Waiter.TargetInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
    """

    def wait(
        self,
        TargetGroupArn: str,
        Targets: List["TargetDescriptionTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TargetInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService.wait)
        """
