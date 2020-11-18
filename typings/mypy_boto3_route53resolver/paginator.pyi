# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for route53resolver service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_route53resolver import Route53ResolverClient
    from mypy_boto3_route53resolver.paginator import (
        ListResolverEndpointIpAddressesPaginator,
        ListResolverEndpointsPaginator,
        ListResolverQueryLogConfigAssociationsPaginator,
        ListResolverQueryLogConfigsPaginator,
        ListResolverRuleAssociationsPaginator,
        ListResolverRulesPaginator,
        ListTagsForResourcePaginator,
    )

    client: Route53ResolverClient = boto3.client("route53resolver")

    list_resolver_endpoint_ip_addresses_paginator: ListResolverEndpointIpAddressesPaginator = client.get_paginator("list_resolver_endpoint_ip_addresses")
    list_resolver_endpoints_paginator: ListResolverEndpointsPaginator = client.get_paginator("list_resolver_endpoints")
    list_resolver_query_log_config_associations_paginator: ListResolverQueryLogConfigAssociationsPaginator = client.get_paginator("list_resolver_query_log_config_associations")
    list_resolver_query_log_configs_paginator: ListResolverQueryLogConfigsPaginator = client.get_paginator("list_resolver_query_log_configs")
    list_resolver_rule_associations_paginator: ListResolverRuleAssociationsPaginator = client.get_paginator("list_resolver_rule_associations")
    list_resolver_rules_paginator: ListResolverRulesPaginator = client.get_paginator("list_resolver_rules")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_route53resolver.type_defs import (
    FilterTypeDef,
    ListResolverEndpointIpAddressesResponseTypeDef,
    ListResolverEndpointsResponseTypeDef,
    ListResolverQueryLogConfigAssociationsResponseTypeDef,
    ListResolverQueryLogConfigsResponseTypeDef,
    ListResolverRuleAssociationsResponseTypeDef,
    ListResolverRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListResolverEndpointIpAddressesPaginator",
    "ListResolverEndpointsPaginator",
    "ListResolverQueryLogConfigAssociationsPaginator",
    "ListResolverQueryLogConfigsPaginator",
    "ListResolverRuleAssociationsPaginator",
    "ListResolverRulesPaginator",
    "ListTagsForResourcePaginator",
)


class ListResolverEndpointIpAddressesPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverEndpointIpAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses)
    """

    def paginate(
        self, ResolverEndpointId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolverEndpointIpAddressesResponseTypeDef]:
        """
        [ListResolverEndpointIpAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses.paginate)
        """


class ListResolverEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpoints)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolverEndpointsResponseTypeDef]:
        """
        [ListResolverEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverEndpoints.paginate)
        """


class ListResolverQueryLogConfigAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverQueryLogConfigAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListResolverQueryLogConfigAssociationsResponseTypeDef]:
        """
        [ListResolverQueryLogConfigAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations.paginate)
        """


class ListResolverQueryLogConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverQueryLogConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListResolverQueryLogConfigsResponseTypeDef]:
        """
        [ListResolverQueryLogConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs.paginate)
        """


class ListResolverRuleAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverRuleAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRuleAssociations)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolverRuleAssociationsResponseTypeDef]:
        """
        [ListResolverRuleAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRuleAssociations.paginate)
        """


class ListResolverRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListResolverRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRules)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolverRulesResponseTypeDef]:
        """
        [ListResolverRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListResolverRules.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource.paginate)
        """
