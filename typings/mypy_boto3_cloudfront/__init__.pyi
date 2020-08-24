"""
Main interface for cloudfront service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudfront import (
        Client,
        CloudFrontClient,
        DistributionDeployedWaiter,
        InvalidationCompletedWaiter,
        ListCloudFrontOriginAccessIdentitiesPaginator,
        ListDistributionsPaginator,
        ListInvalidationsPaginator,
        ListStreamingDistributionsPaginator,
        StreamingDistributionDeployedWaiter,
    )

    session = boto3.Session()

    client: CloudFrontClient = boto3.client("cloudfront")
    session_client: CloudFrontClient = session.client("cloudfront")

    distribution_deployed_waiter: DistributionDeployedWaiter = client.get_waiter("distribution_deployed")
    invalidation_completed_waiter: InvalidationCompletedWaiter = client.get_waiter("invalidation_completed")
    streaming_distribution_deployed_waiter: StreamingDistributionDeployedWaiter = client.get_waiter("streaming_distribution_deployed")

    list_cloud_front_origin_access_identities_paginator: ListCloudFrontOriginAccessIdentitiesPaginator = client.get_paginator("list_cloud_front_origin_access_identities")
    list_distributions_paginator: ListDistributionsPaginator = client.get_paginator("list_distributions")
    list_invalidations_paginator: ListInvalidationsPaginator = client.get_paginator("list_invalidations")
    list_streaming_distributions_paginator: ListStreamingDistributionsPaginator = client.get_paginator("list_streaming_distributions")
    ```
"""
from mypy_boto3_cloudfront.client import CloudFrontClient
from mypy_boto3_cloudfront.paginator import (
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListStreamingDistributionsPaginator,
)
from mypy_boto3_cloudfront.waiter import (
    DistributionDeployedWaiter,
    InvalidationCompletedWaiter,
    StreamingDistributionDeployedWaiter,
)

Client = CloudFrontClient


__all__ = (
    "Client",
    "CloudFrontClient",
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
    "StreamingDistributionDeployedWaiter",
)
