"""
Main interface for elb service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elb import (
        AnyInstanceInServiceWaiter,
        Client,
        DescribeAccountLimitsPaginator,
        DescribeLoadBalancersPaginator,
        ElasticLoadBalancingClient,
        InstanceDeregisteredWaiter,
        InstanceInServiceWaiter,
    )

    session = Session()
    client: ElasticLoadBalancingClient = session.client("elb")

    any_instance_in_service_waiter: AnyInstanceInServiceWaiter = client.get_waiter("any_instance_in_service")
    instance_deregistered_waiter: InstanceDeregisteredWaiter = client.get_waiter("instance_deregistered")
    instance_in_service_waiter: InstanceInServiceWaiter = client.get_waiter("instance_in_service")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    ```
"""

from .client import ElasticLoadBalancingClient
from .paginator import DescribeAccountLimitsPaginator, DescribeLoadBalancersPaginator
from .waiter import AnyInstanceInServiceWaiter, InstanceDeregisteredWaiter, InstanceInServiceWaiter

Client = ElasticLoadBalancingClient

__all__ = (
    "AnyInstanceInServiceWaiter",
    "Client",
    "DescribeAccountLimitsPaginator",
    "DescribeLoadBalancersPaginator",
    "ElasticLoadBalancingClient",
    "InstanceDeregisteredWaiter",
    "InstanceInServiceWaiter",
)
