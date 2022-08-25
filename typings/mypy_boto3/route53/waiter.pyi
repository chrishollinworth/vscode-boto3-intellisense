"""
Type annotations for route53 service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters.html)

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

from .type_defs import WaiterConfigTypeDef

__all__ = ("ResourceRecordSetsChangedWaiter",)

class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters.html#resourcerecordsetschangedwaiter)
    """

    def wait(self, *, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters.html#resourcerecordsetschangedwaiter)
        """
