"""
Type annotations for route53 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53.client import Route53Client
    from mypy_boto3_route53.paginator import (
        ListCidrBlocksPaginator,
        ListCidrCollectionsPaginator,
        ListCidrLocationsPaginator,
        ListHealthChecksPaginator,
        ListHostedZonesPaginator,
        ListQueryLoggingConfigsPaginator,
        ListResourceRecordSetsPaginator,
        ListVPCAssociationAuthorizationsPaginator,
    )

    session = Session()
    client: Route53Client = session.client("route53")

    list_cidr_blocks_paginator: ListCidrBlocksPaginator = client.get_paginator("list_cidr_blocks")
    list_cidr_collections_paginator: ListCidrCollectionsPaginator = client.get_paginator("list_cidr_collections")
    list_cidr_locations_paginator: ListCidrLocationsPaginator = client.get_paginator("list_cidr_locations")
    list_health_checks_paginator: ListHealthChecksPaginator = client.get_paginator("list_health_checks")
    list_hosted_zones_paginator: ListHostedZonesPaginator = client.get_paginator("list_hosted_zones")
    list_query_logging_configs_paginator: ListQueryLoggingConfigsPaginator = client.get_paginator("list_query_logging_configs")
    list_resource_record_sets_paginator: ListResourceRecordSetsPaginator = client.get_paginator("list_resource_record_sets")
    list_vpc_association_authorizations_paginator: ListVPCAssociationAuthorizationsPaginator = client.get_paginator("list_vpc_association_authorizations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCidrBlocksRequestPaginateTypeDef,
    ListCidrBlocksResponseTypeDef,
    ListCidrCollectionsRequestPaginateTypeDef,
    ListCidrCollectionsResponseTypeDef,
    ListCidrLocationsRequestPaginateTypeDef,
    ListCidrLocationsResponseTypeDef,
    ListHealthChecksRequestPaginateTypeDef,
    ListHealthChecksResponseTypeDef,
    ListHostedZonesRequestPaginateTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsRequestPaginateTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsRequestPaginateTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListVPCAssociationAuthorizationsRequestPaginateTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCidrBlocksPaginator",
    "ListCidrCollectionsPaginator",
    "ListCidrLocationsPaginator",
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)

if TYPE_CHECKING:
    _ListCidrBlocksPaginatorBase = Paginator[ListCidrBlocksResponseTypeDef]
else:
    _ListCidrBlocksPaginatorBase = Paginator  # type: ignore[assignment]

class ListCidrBlocksPaginator(_ListCidrBlocksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrBlocks.html#Route53.Paginator.ListCidrBlocks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrblockspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCidrBlocksRequestPaginateTypeDef]
    ) -> PageIterator[ListCidrBlocksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrBlocks.html#Route53.Paginator.ListCidrBlocks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrblockspaginator)
        """

if TYPE_CHECKING:
    _ListCidrCollectionsPaginatorBase = Paginator[ListCidrCollectionsResponseTypeDef]
else:
    _ListCidrCollectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCidrCollectionsPaginator(_ListCidrCollectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrCollections.html#Route53.Paginator.ListCidrCollections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrcollectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCidrCollectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCidrCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrCollections.html#Route53.Paginator.ListCidrCollections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrcollectionspaginator)
        """

if TYPE_CHECKING:
    _ListCidrLocationsPaginatorBase = Paginator[ListCidrLocationsResponseTypeDef]
else:
    _ListCidrLocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCidrLocationsPaginator(_ListCidrLocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrLocations.html#Route53.Paginator.ListCidrLocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrlocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCidrLocationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCidrLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListCidrLocations.html#Route53.Paginator.ListCidrLocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listcidrlocationspaginator)
        """

if TYPE_CHECKING:
    _ListHealthChecksPaginatorBase = Paginator[ListHealthChecksResponseTypeDef]
else:
    _ListHealthChecksPaginatorBase = Paginator  # type: ignore[assignment]

class ListHealthChecksPaginator(_ListHealthChecksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListHealthChecks.html#Route53.Paginator.ListHealthChecks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listhealthcheckspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHealthChecksRequestPaginateTypeDef]
    ) -> PageIterator[ListHealthChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListHealthChecks.html#Route53.Paginator.ListHealthChecks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listhealthcheckspaginator)
        """

if TYPE_CHECKING:
    _ListHostedZonesPaginatorBase = Paginator[ListHostedZonesResponseTypeDef]
else:
    _ListHostedZonesPaginatorBase = Paginator  # type: ignore[assignment]

class ListHostedZonesPaginator(_ListHostedZonesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListHostedZones.html#Route53.Paginator.ListHostedZones)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listhostedzonespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHostedZonesRequestPaginateTypeDef]
    ) -> PageIterator[ListHostedZonesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListHostedZones.html#Route53.Paginator.ListHostedZones.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listhostedzonespaginator)
        """

if TYPE_CHECKING:
    _ListQueryLoggingConfigsPaginatorBase = Paginator[ListQueryLoggingConfigsResponseTypeDef]
else:
    _ListQueryLoggingConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueryLoggingConfigsPaginator(_ListQueryLoggingConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListQueryLoggingConfigs.html#Route53.Paginator.ListQueryLoggingConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listqueryloggingconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueryLoggingConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListQueryLoggingConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListQueryLoggingConfigs.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listqueryloggingconfigspaginator)
        """

if TYPE_CHECKING:
    _ListResourceRecordSetsPaginatorBase = Paginator[ListResourceRecordSetsResponseTypeDef]
else:
    _ListResourceRecordSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceRecordSetsPaginator(_ListResourceRecordSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListResourceRecordSets.html#Route53.Paginator.ListResourceRecordSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listresourcerecordsetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceRecordSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceRecordSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListResourceRecordSets.html#Route53.Paginator.ListResourceRecordSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listresourcerecordsetspaginator)
        """

if TYPE_CHECKING:
    _ListVPCAssociationAuthorizationsPaginatorBase = Paginator[
        ListVPCAssociationAuthorizationsResponseTypeDef
    ]
else:
    _ListVPCAssociationAuthorizationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVPCAssociationAuthorizationsPaginator(_ListVPCAssociationAuthorizationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListVPCAssociationAuthorizations.html#Route53.Paginator.ListVPCAssociationAuthorizations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listvpcassociationauthorizationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVPCAssociationAuthorizationsRequestPaginateTypeDef]
    ) -> PageIterator[ListVPCAssociationAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53/paginator/ListVPCAssociationAuthorizations.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators/#listvpcassociationauthorizationspaginator)
        """
