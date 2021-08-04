"""
Type annotations for elb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/literals.html)

Usage::

    ```python
    from mypy_boto3_elb.literals import AnyInstanceInServiceWaiterName

    data: AnyInstanceInServiceWaiterName = "any_instance_in_service"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AnyInstanceInServiceWaiterName",
    "DescribeAccountLimitsPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "InstanceDeregisteredWaiterName",
    "InstanceInServiceWaiterName",
)

AnyInstanceInServiceWaiterName = Literal["any_instance_in_service"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
InstanceDeregisteredWaiterName = Literal["instance_deregistered"]
InstanceInServiceWaiterName = Literal["instance_in_service"]
