"""
Type annotations for es service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_es.client import ElasticsearchServiceClient
    from mypy_boto3_es.paginator import (
        DescribeReservedElasticsearchInstanceOfferingsPaginator,
        DescribeReservedElasticsearchInstancesPaginator,
        GetUpgradeHistoryPaginator,
        ListElasticsearchInstanceTypesPaginator,
        ListElasticsearchVersionsPaginator,
    )

    session = Session()
    client: ElasticsearchServiceClient = session.client("es")

    describe_reserved_elasticsearch_instance_offerings_paginator: DescribeReservedElasticsearchInstanceOfferingsPaginator = client.get_paginator("describe_reserved_elasticsearch_instance_offerings")
    describe_reserved_elasticsearch_instances_paginator: DescribeReservedElasticsearchInstancesPaginator = client.get_paginator("describe_reserved_elasticsearch_instances")
    get_upgrade_history_paginator: GetUpgradeHistoryPaginator = client.get_paginator("get_upgrade_history")
    list_elasticsearch_instance_types_paginator: ListElasticsearchInstanceTypesPaginator = client.get_paginator("list_elasticsearch_instance_types")
    list_elasticsearch_versions_paginator: ListElasticsearchVersionsPaginator = client.get_paginator("list_elasticsearch_versions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeReservedElasticsearchInstanceOfferingsRequestPaginateTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesRequestPaginateTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    GetUpgradeHistoryRequestPaginateTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    ListElasticsearchInstanceTypesRequestPaginateTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsRequestPaginateTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeReservedElasticsearchInstanceOfferingsPaginator",
    "DescribeReservedElasticsearchInstancesPaginator",
    "GetUpgradeHistoryPaginator",
    "ListElasticsearchInstanceTypesPaginator",
    "ListElasticsearchVersionsPaginator",
)

if TYPE_CHECKING:
    _DescribeReservedElasticsearchInstanceOfferingsPaginatorBase = Paginator[
        DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef
    ]
else:
    _DescribeReservedElasticsearchInstanceOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedElasticsearchInstanceOfferingsPaginator(
    _DescribeReservedElasticsearchInstanceOfferingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/DescribeReservedElasticsearchInstanceOfferings.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#describereservedelasticsearchinstanceofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedElasticsearchInstanceOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/DescribeReservedElasticsearchInstanceOfferings.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#describereservedelasticsearchinstanceofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedElasticsearchInstancesPaginatorBase = Paginator[
        DescribeReservedElasticsearchInstancesResponseTypeDef
    ]
else:
    _DescribeReservedElasticsearchInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedElasticsearchInstancesPaginator(
    _DescribeReservedElasticsearchInstancesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/DescribeReservedElasticsearchInstances.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#describereservedelasticsearchinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedElasticsearchInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedElasticsearchInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/DescribeReservedElasticsearchInstances.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#describereservedelasticsearchinstancespaginator)
        """

if TYPE_CHECKING:
    _GetUpgradeHistoryPaginatorBase = Paginator[GetUpgradeHistoryResponseTypeDef]
else:
    _GetUpgradeHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetUpgradeHistoryPaginator(_GetUpgradeHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/GetUpgradeHistory.html#ElasticsearchService.Paginator.GetUpgradeHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#getupgradehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetUpgradeHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetUpgradeHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/GetUpgradeHistory.html#ElasticsearchService.Paginator.GetUpgradeHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#getupgradehistorypaginator)
        """

if TYPE_CHECKING:
    _ListElasticsearchInstanceTypesPaginatorBase = Paginator[
        ListElasticsearchInstanceTypesResponseTypeDef
    ]
else:
    _ListElasticsearchInstanceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListElasticsearchInstanceTypesPaginator(_ListElasticsearchInstanceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/ListElasticsearchInstanceTypes.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#listelasticsearchinstancetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListElasticsearchInstanceTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListElasticsearchInstanceTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/ListElasticsearchInstanceTypes.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#listelasticsearchinstancetypespaginator)
        """

if TYPE_CHECKING:
    _ListElasticsearchVersionsPaginatorBase = Paginator[ListElasticsearchVersionsResponseTypeDef]
else:
    _ListElasticsearchVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListElasticsearchVersionsPaginator(_ListElasticsearchVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/ListElasticsearchVersions.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#listelasticsearchversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListElasticsearchVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListElasticsearchVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/paginator/ListElasticsearchVersions.html#ElasticsearchService.Paginator.ListElasticsearchVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/paginators/#listelasticsearchversionspaginator)
        """
