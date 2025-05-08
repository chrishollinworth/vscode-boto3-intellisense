"""
Type annotations for elbv2 service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elbv2.client import ElasticLoadBalancingv2Client
    from mypy_boto3_elbv2.waiter import (
        LoadBalancerAvailableWaiter,
        LoadBalancerExistsWaiter,
        LoadBalancersDeletedWaiter,
        TargetDeregisteredWaiter,
        TargetInServiceWaiter,
    )

    session = Session()
    client: ElasticLoadBalancingv2Client = session.client("elbv2")

    load_balancer_available_waiter: LoadBalancerAvailableWaiter = client.get_waiter("load_balancer_available")
    load_balancer_exists_waiter: LoadBalancerExistsWaiter = client.get_waiter("load_balancer_exists")
    load_balancers_deleted_waiter: LoadBalancersDeletedWaiter = client.get_waiter("load_balancers_deleted")
    target_deregistered_waiter: TargetDeregisteredWaiter = client.get_waiter("target_deregistered")
    target_in_service_waiter: TargetInServiceWaiter = client.get_waiter("target_in_service")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeLoadBalancersInputWaitExtraExtraTypeDef,
    DescribeLoadBalancersInputWaitExtraTypeDef,
    DescribeLoadBalancersInputWaitTypeDef,
    DescribeTargetHealthInputWaitExtraTypeDef,
    DescribeTargetHealthInputWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)

class LoadBalancerAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancerAvailable.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalanceravailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancersInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancerAvailable.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalanceravailablewaiter)
        """

class LoadBalancerExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancerExists.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalancerexistswaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancersInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancerExists.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalancerexistswaiter)
        """

class LoadBalancersDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancersDeleted.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalancersdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancersInputWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/LoadBalancersDeleted.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#loadbalancersdeletedwaiter)
        """

class TargetDeregisteredWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/TargetDeregistered.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#targetderegisteredwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTargetHealthInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/TargetDeregistered.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#targetderegisteredwaiter)
        """

class TargetInServiceWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/TargetInService.html#ElasticLoadBalancingv2.Waiter.TargetInService)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#targetinservicewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTargetHealthInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2/waiter/TargetInService.html#ElasticLoadBalancingv2.Waiter.TargetInService.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/waiters/#targetinservicewaiter)
        """
