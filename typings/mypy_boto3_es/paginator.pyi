# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for es service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_es import ElasticsearchServiceClient
    from mypy_boto3_es.paginator import (
        DescribeReservedElasticsearchInstanceOfferingsPaginator,
        DescribeReservedElasticsearchInstancesPaginator,
        GetUpgradeHistoryPaginator,
        ListElasticsearchInstanceTypesPaginator,
        ListElasticsearchVersionsPaginator,
    )

    client: ElasticsearchServiceClient = boto3.client("es")

    describe_reserved_elasticsearch_instance_offerings_paginator: DescribeReservedElasticsearchInstanceOfferingsPaginator = client.get_paginator("describe_reserved_elasticsearch_instance_offerings")
    describe_reserved_elasticsearch_instances_paginator: DescribeReservedElasticsearchInstancesPaginator = client.get_paginator("describe_reserved_elasticsearch_instances")
    get_upgrade_history_paginator: GetUpgradeHistoryPaginator = client.get_paginator("get_upgrade_history")
    list_elasticsearch_instance_types_paginator: ListElasticsearchInstanceTypesPaginator = client.get_paginator("list_elasticsearch_instance_types")
    list_elasticsearch_versions_paginator: ListElasticsearchVersionsPaginator = client.get_paginator("list_elasticsearch_versions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_es.type_defs import (
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeReservedElasticsearchInstanceOfferingsPaginator",
    "DescribeReservedElasticsearchInstancesPaginator",
    "GetUpgradeHistoryPaginator",
    "ListElasticsearchInstanceTypesPaginator",
    "ListElasticsearchVersionsPaginator",
)


class DescribeReservedElasticsearchInstanceOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
    """

    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef]:
        """
        [DescribeReservedElasticsearchInstanceOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings.paginate)
        """


class DescribeReservedElasticsearchInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
    """

    def paginate(
        self,
        ReservedElasticsearchInstanceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeReservedElasticsearchInstancesResponseTypeDef]:
        """
        [DescribeReservedElasticsearchInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances.paginate)
        """


class GetUpgradeHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
    """

    def paginate(
        self, DomainName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetUpgradeHistoryResponseTypeDef]:
        """
        [GetUpgradeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory.paginate)
        """


class ListElasticsearchInstanceTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
    """

    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListElasticsearchInstanceTypesResponseTypeDef]:
        """
        [ListElasticsearchInstanceTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes.paginate)
        """


class ListElasticsearchVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListElasticsearchVersionsResponseTypeDef]:
        """
        [ListElasticsearchVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions.paginate)
        """
