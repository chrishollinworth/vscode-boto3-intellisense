"""
Type annotations for cloudcontrol service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudcontrol import CloudControlApiClient
    from mypy_boto3_cloudcontrol.waiter import (
        ResourceRequestSuccessWaiter,
    )

    client: CloudControlApiClient = boto3.client("cloudcontrol")

    resource_request_success_waiter: ResourceRequestSuccessWaiter = client.get_waiter("resource_request_success")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("ResourceRequestSuccessWaiter",)

class ResourceRequestSuccessWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudcontrol.html#CloudControlApi.Waiter.ResourceRequestSuccess)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters.html#resourcerequestsuccesswaiter)
    """

    def wait(self, *, RequestToken: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cloudcontrol.html#CloudControlApi.Waiter.ResourceRequestSuccess.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/waiters.html#resourcerequestsuccesswaiter)
        """
