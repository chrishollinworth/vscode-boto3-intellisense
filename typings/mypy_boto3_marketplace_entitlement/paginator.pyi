"""
Type annotations for marketplace-entitlement service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_marketplace_entitlement import MarketplaceEntitlementServiceClient
    from mypy_boto3_marketplace_entitlement.paginator import (
        GetEntitlementsPaginator,
    )

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")

    get_entitlements_paginator: GetEntitlementsPaginator = client.get_paginator("get_entitlements")
    ```
"""

from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import GetEntitlementFilterNameType
from .type_defs import GetEntitlementsResultTypeDef, PaginatorConfigTypeDef

__all__ = ("GetEntitlementsPaginator",)

class GetEntitlementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/paginators.html#getentitlementspaginator)
    """

    def paginate(
        self,
        *,
        ProductCode: str,
        Filter: Dict[GetEntitlementFilterNameType, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetEntitlementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/paginators.html#getentitlementspaginator)
        """
