"""
Type annotations for elbv2 service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html)

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

from .type_defs import TargetDescriptionTypeDef, WaiterConfigTypeDef

__all__ = (
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)

class LoadBalancerAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalanceravailablewaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalanceravailablewaiter)
        """

class LoadBalancerExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalancerexistswaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalancerexistswaiter)
        """

class LoadBalancersDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalancersdeletedwaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#loadbalancersdeletedwaiter)
        """

class TargetDeregisteredWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#targetderegisteredwaiter)
    """

    def wait(
        self,
        *,
        TargetGroupArn: str,
        Targets: List["TargetDescriptionTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#targetderegisteredwaiter)
        """

class TargetInServiceWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#targetinservicewaiter)
    """

    def wait(
        self,
        *,
        TargetGroupArn: str,
        Targets: List["TargetDescriptionTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters.html#targetinservicewaiter)
        """
