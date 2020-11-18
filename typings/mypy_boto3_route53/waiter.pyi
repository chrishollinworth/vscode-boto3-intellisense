# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for route53 service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_route53 import Route53Client
    from mypy_boto3_route53.waiter import (
        ResourceRecordSetsChangedWaiter,
    )

    client: Route53Client = boto3.client("route53")

    resource_record_sets_changed_waiter: ResourceRecordSetsChangedWaiter = client.get_waiter("resource_record_sets_changed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_route53.type_defs import WaiterConfigTypeDef

__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    [Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ResourceRecordSetsChanged.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged.wait)
        """
