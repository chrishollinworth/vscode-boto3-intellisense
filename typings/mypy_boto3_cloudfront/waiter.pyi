"""
Type annotations for cloudfront service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudfront import CloudFrontClient
    from mypy_boto3_cloudfront.waiter import (
        DistributionDeployedWaiter,
        InvalidationCompletedWaiter,
        StreamingDistributionDeployedWaiter,
    )

    client: CloudFrontClient = boto3.client("cloudfront")

    distribution_deployed_waiter: DistributionDeployedWaiter = client.get_waiter("distribution_deployed")
    invalidation_completed_waiter: InvalidationCompletedWaiter = client.get_waiter("invalidation_completed")
    streaming_distribution_deployed_waiter: StreamingDistributionDeployedWaiter = client.get_waiter("streaming_distribution_deployed")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)

class DistributionDeployedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#distributiondeployedwaiter)
    """

    def wait(self, *, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#distributiondeployedwaiter)
        """

class InvalidationCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#invalidationcompletedwaiter)
    """

    def wait(
        self, *, DistributionId: str, Id: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#invalidationcompletedwaiter)
        """

class StreamingDistributionDeployedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#streamingdistributiondeployedwaiter)
    """

    def wait(self, *, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters.html#streamingdistributiondeployedwaiter)
        """
