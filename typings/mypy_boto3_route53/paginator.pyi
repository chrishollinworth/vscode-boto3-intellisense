# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for route53 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_route53 import Route53Client
    from mypy_boto3_route53.paginator import (
        ListHealthChecksPaginator,
        ListHostedZonesPaginator,
        ListQueryLoggingConfigsPaginator,
        ListResourceRecordSetsPaginator,
        ListVPCAssociationAuthorizationsPaginator,
    )

    client: Route53Client = boto3.client("route53")

    list_health_checks_paginator: ListHealthChecksPaginator = client.get_paginator("list_health_checks")
    list_hosted_zones_paginator: ListHostedZonesPaginator = client.get_paginator("list_hosted_zones")
    list_query_logging_configs_paginator: ListQueryLoggingConfigsPaginator = client.get_paginator("list_query_logging_configs")
    list_resource_record_sets_paginator: ListResourceRecordSetsPaginator = client.get_paginator("list_resource_record_sets")
    list_vpc_association_authorizations_paginator: ListVPCAssociationAuthorizationsPaginator = client.get_paginator("list_vpc_association_authorizations")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_route53.type_defs import (
    ListHealthChecksResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)


class ListHealthChecksPaginator(Boto3Paginator):
    """
    [Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHealthChecksResponseTypeDef]:
        """
        [ListHealthChecks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHealthChecks.paginate)
        """


class ListHostedZonesPaginator(Boto3Paginator):
    """
    [Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHostedZones)
    """

    def paginate(
        self, DelegationSetId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHostedZonesResponseTypeDef]:
        """
        [ListHostedZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHostedZones.paginate)
        """


class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
    """

    def paginate(
        self, HostedZoneId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryLoggingConfigsResponseTypeDef]:
        """
        [ListQueryLoggingConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        """


class ListResourceRecordSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
    """

    def paginate(
        self, HostedZoneId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceRecordSetsResponseTypeDef]:
        """
        [ListResourceRecordSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets.paginate)
        """


class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    """
    [Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
    """

    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListVPCAssociationAuthorizationsResponseTypeDef]:
        """
        [ListVPCAssociationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        """
