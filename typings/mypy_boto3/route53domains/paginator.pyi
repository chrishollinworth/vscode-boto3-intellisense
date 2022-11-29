"""
Type annotations for route53domains service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53domains import Route53DomainsClient
    from mypy_boto3_route53domains.paginator import (
        ListDomainsPaginator,
        ListOperationsPaginator,
        ListPricesPaginator,
        ViewBillingPaginator,
    )

    client: Route53DomainsClient = boto3.client("route53domains")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_prices_paginator: ListPricesPaginator = client.get_paginator("list_prices")
    view_billing_paginator: ViewBillingPaginator = client.get_paginator("view_billing")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterConditionTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListPricesResponseTypeDef,
    PaginatorConfigTypeDef,
    SortConditionTypeDef,
    ViewBillingResponseTypeDef,
)

__all__ = (
    "ListDomainsPaginator",
    "ListOperationsPaginator",
    "ListPricesPaginator",
    "ViewBillingPaginator",
)

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listdomainspaginator)
    """

    def paginate(
        self,
        *,
        FilterConditions: List["FilterConditionTypeDef"] = None,
        SortCondition: "SortConditionTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listdomainspaginator)
        """

class ListOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listoperationspaginator)
    """

    def paginate(
        self,
        *,
        SubmittedSince: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listoperationspaginator)
        """

class ListPricesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListPrices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listpricespaginator)
    """

    def paginate(
        self, *, Tld: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPricesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ListPrices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#listpricespaginator)
        """

class ViewBillingPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#viewbillingpaginator)
    """

    def paginate(
        self,
        *,
        Start: Union[datetime, str] = None,
        End: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ViewBillingResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators.html#viewbillingpaginator)
        """
