"""
Type annotations for route53 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_route53 import Route53Client
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

    client: Route53Client = boto3.client("route53")

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListCidrBlocksResponseTypeDef,
    ListCidrCollectionsResponseTypeDef,
    ListCidrLocationsResponseTypeDef,
    ListHealthChecksResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

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

class ListCidrBlocksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrBlocks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrblockspaginator)
    """

    def paginate(
        self,
        *,
        CollectionId: str,
        LocationName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCidrBlocksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrBlocks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrblockspaginator)
        """

class ListCidrCollectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrCollections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrcollectionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCidrCollectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrCollections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrcollectionspaginator)
        """

class ListCidrLocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrLocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrlocationspaginator)
    """

    def paginate(
        self, *, CollectionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCidrLocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListCidrLocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrlocationspaginator)
        """

class ListHealthChecksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhealthcheckspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHealthChecksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListHealthChecks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhealthcheckspaginator)
        """

class ListHostedZonesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListHostedZones)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhostedzonespaginator)
    """

    def paginate(
        self, *, DelegationSetId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHostedZonesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListHostedZones.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhostedzonespaginator)
        """

class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listqueryloggingconfigspaginator)
    """

    def paginate(
        self, *, HostedZoneId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryLoggingConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listqueryloggingconfigspaginator)
        """

class ListResourceRecordSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listresourcerecordsetspaginator)
    """

    def paginate(
        self, *, HostedZoneId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceRecordSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listresourcerecordsetspaginator)
        """

class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listvpcassociationauthorizationspaginator)
    """

    def paginate(
        self,
        *,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVPCAssociationAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listvpcassociationauthorizationspaginator)
        """
