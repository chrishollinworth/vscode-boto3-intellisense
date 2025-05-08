"""
Type annotations for cloudfront service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudfront.client import CloudFrontClient
    from mypy_boto3_cloudfront.waiter import (
        DistributionDeployedWaiter,
        InvalidationCompletedWaiter,
        InvalidationForDistributionTenantCompletedWaiter,
        StreamingDistributionDeployedWaiter,
    )

    session = Session()
    client: CloudFrontClient = session.client("cloudfront")

    distribution_deployed_waiter: DistributionDeployedWaiter = client.get_waiter("distribution_deployed")
    invalidation_completed_waiter: InvalidationCompletedWaiter = client.get_waiter("invalidation_completed")
    invalidation_for_distribution_tenant_completed_waiter: InvalidationForDistributionTenantCompletedWaiter = client.get_waiter("invalidation_for_distribution_tenant_completed")
    streaming_distribution_deployed_waiter: StreamingDistributionDeployedWaiter = client.get_waiter("streaming_distribution_deployed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetDistributionRequestWaitTypeDef,
    GetInvalidationForDistributionTenantRequestWaitTypeDef,
    GetInvalidationRequestWaitTypeDef,
    GetStreamingDistributionRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "InvalidationForDistributionTenantCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)

class DistributionDeployedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/DistributionDeployed.html#CloudFront.Waiter.DistributionDeployed)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#distributiondeployedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetDistributionRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/DistributionDeployed.html#CloudFront.Waiter.DistributionDeployed.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#distributiondeployedwaiter)
        """

class InvalidationCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/InvalidationCompleted.html#CloudFront.Waiter.InvalidationCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#invalidationcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetInvalidationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/InvalidationCompleted.html#CloudFront.Waiter.InvalidationCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#invalidationcompletedwaiter)
        """

class InvalidationForDistributionTenantCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/InvalidationForDistributionTenantCompleted.html#CloudFront.Waiter.InvalidationForDistributionTenantCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#invalidationfordistributiontenantcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetInvalidationForDistributionTenantRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/InvalidationForDistributionTenantCompleted.html#CloudFront.Waiter.InvalidationForDistributionTenantCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#invalidationfordistributiontenantcompletedwaiter)
        """

class StreamingDistributionDeployedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/StreamingDistributionDeployed.html#CloudFront.Waiter.StreamingDistributionDeployed)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#streamingdistributiondeployedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetStreamingDistributionRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/waiter/StreamingDistributionDeployed.html#CloudFront.Waiter.StreamingDistributionDeployed.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/waiters/#streamingdistributiondeployedwaiter)
        """
