"""
Type annotations for route53domains service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53domains.client import Route53DomainsClient
    from mypy_boto3_route53domains.paginator import (
        ListDomainsPaginator,
        ListOperationsPaginator,
        ListPricesPaginator,
        ViewBillingPaginator,
    )

    session = Session()
    client: Route53DomainsClient = session.client("route53domains")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_prices_paginator: ListPricesPaginator = client.get_paginator("list_prices")
    view_billing_paginator: ViewBillingPaginator = client.get_paginator("view_billing")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDomainsRequestPaginateTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsRequestPaginateTypeDef,
    ListOperationsResponseTypeDef,
    ListPricesRequestPaginateTypeDef,
    ListPricesResponseTypeDef,
    ViewBillingRequestPaginateTypeDef,
    ViewBillingResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDomainsPaginator",
    "ListOperationsPaginator",
    "ListPricesPaginator",
    "ViewBillingPaginator",
)

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsResponseTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListDomains.html#Route53Domains.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListDomains.html#Route53Domains.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListOperationsPaginatorBase = Paginator[ListOperationsResponseTypeDef]
else:
    _ListOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOperationsPaginator(_ListOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListOperations.html#Route53Domains.Paginator.ListOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListOperations.html#Route53Domains.Paginator.ListOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listoperationspaginator)
        """

if TYPE_CHECKING:
    _ListPricesPaginatorBase = Paginator[ListPricesResponseTypeDef]
else:
    _ListPricesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPricesPaginator(_ListPricesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListPrices.html#Route53Domains.Paginator.ListPrices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listpricespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPricesRequestPaginateTypeDef]
    ) -> PageIterator[ListPricesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ListPrices.html#Route53Domains.Paginator.ListPrices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#listpricespaginator)
        """

if TYPE_CHECKING:
    _ViewBillingPaginatorBase = Paginator[ViewBillingResponseTypeDef]
else:
    _ViewBillingPaginatorBase = Paginator  # type: ignore[assignment]

class ViewBillingPaginator(_ViewBillingPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ViewBilling.html#Route53Domains.Paginator.ViewBilling)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#viewbillingpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ViewBillingRequestPaginateTypeDef]
    ) -> PageIterator[ViewBillingResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains/paginator/ViewBilling.html#Route53Domains.Paginator.ViewBilling.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/paginators/#viewbillingpaginator)
        """
