# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cloudfront service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudfront import CloudFrontClient
    from mypy_boto3_cloudfront.paginator import (
        ListCloudFrontOriginAccessIdentitiesPaginator,
        ListDistributionsPaginator,
        ListInvalidationsPaginator,
        ListStreamingDistributionsPaginator,
    )

    client: CloudFrontClient = boto3.client("cloudfront")

    list_cloud_front_origin_access_identities_paginator: ListCloudFrontOriginAccessIdentitiesPaginator = client.get_paginator("list_cloud_front_origin_access_identities")
    list_distributions_paginator: ListDistributionsPaginator = client.get_paginator("list_distributions")
    list_invalidations_paginator: ListInvalidationsPaginator = client.get_paginator("list_invalidations")
    list_streaming_distributions_paginator: ListStreamingDistributionsPaginator = client.get_paginator("list_streaming_distributions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloudfront.type_defs import (
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListDistributionsResultTypeDef,
    ListInvalidationsResultTypeDef,
    ListStreamingDistributionsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
)


class ListCloudFrontOriginAccessIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCloudFrontOriginAccessIdentitiesResultTypeDef]:
        """
        [ListCloudFrontOriginAccessIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities.paginate)
        """


class ListDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDistributionsResultTypeDef]:
        """
        [ListDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions.paginate)
        """


class ListInvalidationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)
    """

    def paginate(
        self, DistributionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInvalidationsResultTypeDef]:
        """
        [ListInvalidations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations.paginate)
        """


class ListStreamingDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamingDistributionsResultTypeDef]:
        """
        [ListStreamingDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions.paginate)
        """
