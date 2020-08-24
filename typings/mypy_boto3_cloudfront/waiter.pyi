# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for cloudfront service client waiters.

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

from mypy_boto3_cloudfront.type_defs import WaiterConfigTypeDef

__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)


class DistributionDeployedWaiter(Boto3Waiter):
    """
    [Waiter.DistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [DistributionDeployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed.wait)
        """


class InvalidationCompletedWaiter(Boto3Waiter):
    """
    [Waiter.InvalidationCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)
    """

    def wait(self, DistributionId: str, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InvalidationCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted.wait)
        """


class StreamingDistributionDeployedWaiter(Boto3Waiter):
    """
    [Waiter.StreamingDistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)
    """

    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [StreamingDistributionDeployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed.wait)
        """
