"""
Type annotations for route53resolver service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53resolver.client import Route53ResolverClient
    from mypy_boto3_route53resolver.paginator import (
        ListFirewallConfigsPaginator,
        ListFirewallDomainListsPaginator,
        ListFirewallDomainsPaginator,
        ListFirewallRuleGroupAssociationsPaginator,
        ListFirewallRuleGroupsPaginator,
        ListFirewallRulesPaginator,
        ListOutpostResolversPaginator,
        ListResolverConfigsPaginator,
        ListResolverDnssecConfigsPaginator,
        ListResolverEndpointIpAddressesPaginator,
        ListResolverEndpointsPaginator,
        ListResolverQueryLogConfigAssociationsPaginator,
        ListResolverQueryLogConfigsPaginator,
        ListResolverRuleAssociationsPaginator,
        ListResolverRulesPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: Route53ResolverClient = session.client("route53resolver")

    list_firewall_configs_paginator: ListFirewallConfigsPaginator = client.get_paginator("list_firewall_configs")
    list_firewall_domain_lists_paginator: ListFirewallDomainListsPaginator = client.get_paginator("list_firewall_domain_lists")
    list_firewall_domains_paginator: ListFirewallDomainsPaginator = client.get_paginator("list_firewall_domains")
    list_firewall_rule_group_associations_paginator: ListFirewallRuleGroupAssociationsPaginator = client.get_paginator("list_firewall_rule_group_associations")
    list_firewall_rule_groups_paginator: ListFirewallRuleGroupsPaginator = client.get_paginator("list_firewall_rule_groups")
    list_firewall_rules_paginator: ListFirewallRulesPaginator = client.get_paginator("list_firewall_rules")
    list_outpost_resolvers_paginator: ListOutpostResolversPaginator = client.get_paginator("list_outpost_resolvers")
    list_resolver_configs_paginator: ListResolverConfigsPaginator = client.get_paginator("list_resolver_configs")
    list_resolver_dnssec_configs_paginator: ListResolverDnssecConfigsPaginator = client.get_paginator("list_resolver_dnssec_configs")
    list_resolver_endpoint_ip_addresses_paginator: ListResolverEndpointIpAddressesPaginator = client.get_paginator("list_resolver_endpoint_ip_addresses")
    list_resolver_endpoints_paginator: ListResolverEndpointsPaginator = client.get_paginator("list_resolver_endpoints")
    list_resolver_query_log_config_associations_paginator: ListResolverQueryLogConfigAssociationsPaginator = client.get_paginator("list_resolver_query_log_config_associations")
    list_resolver_query_log_configs_paginator: ListResolverQueryLogConfigsPaginator = client.get_paginator("list_resolver_query_log_configs")
    list_resolver_rule_associations_paginator: ListResolverRuleAssociationsPaginator = client.get_paginator("list_resolver_rule_associations")
    list_resolver_rules_paginator: ListResolverRulesPaginator = client.get_paginator("list_resolver_rules")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListFirewallConfigsRequestPaginateTypeDef,
    ListFirewallConfigsResponseTypeDef,
    ListFirewallDomainListsRequestPaginateTypeDef,
    ListFirewallDomainListsResponseTypeDef,
    ListFirewallDomainsRequestPaginateTypeDef,
    ListFirewallDomainsResponseTypeDef,
    ListFirewallRuleGroupAssociationsRequestPaginateTypeDef,
    ListFirewallRuleGroupAssociationsResponseTypeDef,
    ListFirewallRuleGroupsRequestPaginateTypeDef,
    ListFirewallRuleGroupsResponseTypeDef,
    ListFirewallRulesRequestPaginateTypeDef,
    ListFirewallRulesResponseTypeDef,
    ListOutpostResolversRequestPaginateTypeDef,
    ListOutpostResolversResponseTypeDef,
    ListResolverConfigsRequestPaginateTypeDef,
    ListResolverConfigsResponseTypeDef,
    ListResolverDnssecConfigsRequestPaginateTypeDef,
    ListResolverDnssecConfigsResponseTypeDef,
    ListResolverEndpointIpAddressesRequestPaginateTypeDef,
    ListResolverEndpointIpAddressesResponseTypeDef,
    ListResolverEndpointsRequestPaginateTypeDef,
    ListResolverEndpointsResponseTypeDef,
    ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef,
    ListResolverQueryLogConfigAssociationsResponseTypeDef,
    ListResolverQueryLogConfigsRequestPaginateTypeDef,
    ListResolverQueryLogConfigsResponseTypeDef,
    ListResolverRuleAssociationsRequestPaginateTypeDef,
    ListResolverRuleAssociationsResponseTypeDef,
    ListResolverRulesRequestPaginateTypeDef,
    ListResolverRulesResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListFirewallConfigsPaginator",
    "ListFirewallDomainListsPaginator",
    "ListFirewallDomainsPaginator",
    "ListFirewallRuleGroupAssociationsPaginator",
    "ListFirewallRuleGroupsPaginator",
    "ListFirewallRulesPaginator",
    "ListOutpostResolversPaginator",
    "ListResolverConfigsPaginator",
    "ListResolverDnssecConfigsPaginator",
    "ListResolverEndpointIpAddressesPaginator",
    "ListResolverEndpointsPaginator",
    "ListResolverQueryLogConfigAssociationsPaginator",
    "ListResolverQueryLogConfigsPaginator",
    "ListResolverRuleAssociationsPaginator",
    "ListResolverRulesPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _ListFirewallConfigsPaginatorBase = Paginator[ListFirewallConfigsResponseTypeDef]
else:
    _ListFirewallConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallConfigsPaginator(_ListFirewallConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallConfigs.html#Route53Resolver.Paginator.ListFirewallConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallConfigs.html#Route53Resolver.Paginator.ListFirewallConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallconfigspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallDomainListsPaginatorBase = Paginator[ListFirewallDomainListsResponseTypeDef]
else:
    _ListFirewallDomainListsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallDomainListsPaginator(_ListFirewallDomainListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallDomainLists.html#Route53Resolver.Paginator.ListFirewallDomainLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewalldomainlistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallDomainListsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallDomainListsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallDomainLists.html#Route53Resolver.Paginator.ListFirewallDomainLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewalldomainlistspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallDomainsPaginatorBase = Paginator[ListFirewallDomainsResponseTypeDef]
else:
    _ListFirewallDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallDomainsPaginator(_ListFirewallDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallDomains.html#Route53Resolver.Paginator.ListFirewallDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewalldomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallDomains.html#Route53Resolver.Paginator.ListFirewallDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewalldomainspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallRuleGroupAssociationsPaginatorBase = Paginator[
        ListFirewallRuleGroupAssociationsResponseTypeDef
    ]
else:
    _ListFirewallRuleGroupAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallRuleGroupAssociationsPaginator(_ListFirewallRuleGroupAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRuleGroupAssociations.html#Route53Resolver.Paginator.ListFirewallRuleGroupAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulegroupassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallRuleGroupAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallRuleGroupAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRuleGroupAssociations.html#Route53Resolver.Paginator.ListFirewallRuleGroupAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulegroupassociationspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallRuleGroupsPaginatorBase = Paginator[ListFirewallRuleGroupsResponseTypeDef]
else:
    _ListFirewallRuleGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallRuleGroupsPaginator(_ListFirewallRuleGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRuleGroups.html#Route53Resolver.Paginator.ListFirewallRuleGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallRuleGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallRuleGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRuleGroups.html#Route53Resolver.Paginator.ListFirewallRuleGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulegroupspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallRulesPaginatorBase = Paginator[ListFirewallRulesResponseTypeDef]
else:
    _ListFirewallRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallRulesPaginator(_ListFirewallRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRules.html#Route53Resolver.Paginator.ListFirewallRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListFirewallRules.html#Route53Resolver.Paginator.ListFirewallRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listfirewallrulespaginator)
        """

if TYPE_CHECKING:
    _ListOutpostResolversPaginatorBase = Paginator[ListOutpostResolversResponseTypeDef]
else:
    _ListOutpostResolversPaginatorBase = Paginator  # type: ignore[assignment]

class ListOutpostResolversPaginator(_ListOutpostResolversPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListOutpostResolvers.html#Route53Resolver.Paginator.ListOutpostResolvers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listoutpostresolverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOutpostResolversRequestPaginateTypeDef]
    ) -> PageIterator[ListOutpostResolversResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListOutpostResolvers.html#Route53Resolver.Paginator.ListOutpostResolvers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listoutpostresolverspaginator)
        """

if TYPE_CHECKING:
    _ListResolverConfigsPaginatorBase = Paginator[ListResolverConfigsResponseTypeDef]
else:
    _ListResolverConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverConfigsPaginator(_ListResolverConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverConfigs.html#Route53Resolver.Paginator.ListResolverConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverConfigs.html#Route53Resolver.Paginator.ListResolverConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverconfigspaginator)
        """

if TYPE_CHECKING:
    _ListResolverDnssecConfigsPaginatorBase = Paginator[ListResolverDnssecConfigsResponseTypeDef]
else:
    _ListResolverDnssecConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverDnssecConfigsPaginator(_ListResolverDnssecConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverDnssecConfigs.html#Route53Resolver.Paginator.ListResolverDnssecConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverdnssecconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverDnssecConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverDnssecConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverDnssecConfigs.html#Route53Resolver.Paginator.ListResolverDnssecConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverdnssecconfigspaginator)
        """

if TYPE_CHECKING:
    _ListResolverEndpointIpAddressesPaginatorBase = Paginator[
        ListResolverEndpointIpAddressesResponseTypeDef
    ]
else:
    _ListResolverEndpointIpAddressesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverEndpointIpAddressesPaginator(_ListResolverEndpointIpAddressesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverEndpointIpAddresses.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverendpointipaddressespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverEndpointIpAddressesRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverEndpointIpAddressesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverEndpointIpAddresses.html#Route53Resolver.Paginator.ListResolverEndpointIpAddresses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverendpointipaddressespaginator)
        """

if TYPE_CHECKING:
    _ListResolverEndpointsPaginatorBase = Paginator[ListResolverEndpointsResponseTypeDef]
else:
    _ListResolverEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverEndpointsPaginator(_ListResolverEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverEndpoints.html#Route53Resolver.Paginator.ListResolverEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverEndpoints.html#Route53Resolver.Paginator.ListResolverEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverendpointspaginator)
        """

if TYPE_CHECKING:
    _ListResolverQueryLogConfigAssociationsPaginatorBase = Paginator[
        ListResolverQueryLogConfigAssociationsResponseTypeDef
    ]
else:
    _ListResolverQueryLogConfigAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverQueryLogConfigAssociationsPaginator(
    _ListResolverQueryLogConfigAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverQueryLogConfigAssociations.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverquerylogconfigassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverQueryLogConfigAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverQueryLogConfigAssociations.html#Route53Resolver.Paginator.ListResolverQueryLogConfigAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverquerylogconfigassociationspaginator)
        """

if TYPE_CHECKING:
    _ListResolverQueryLogConfigsPaginatorBase = Paginator[
        ListResolverQueryLogConfigsResponseTypeDef
    ]
else:
    _ListResolverQueryLogConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverQueryLogConfigsPaginator(_ListResolverQueryLogConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverQueryLogConfigs.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverquerylogconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverQueryLogConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverQueryLogConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverQueryLogConfigs.html#Route53Resolver.Paginator.ListResolverQueryLogConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverquerylogconfigspaginator)
        """

if TYPE_CHECKING:
    _ListResolverRuleAssociationsPaginatorBase = Paginator[
        ListResolverRuleAssociationsResponseTypeDef
    ]
else:
    _ListResolverRuleAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverRuleAssociationsPaginator(_ListResolverRuleAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverRuleAssociations.html#Route53Resolver.Paginator.ListResolverRuleAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverruleassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverRuleAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverRuleAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverRuleAssociations.html#Route53Resolver.Paginator.ListResolverRuleAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverruleassociationspaginator)
        """

if TYPE_CHECKING:
    _ListResolverRulesPaginatorBase = Paginator[ListResolverRulesResponseTypeDef]
else:
    _ListResolverRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResolverRulesPaginator(_ListResolverRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverRules.html#Route53Resolver.Paginator.ListResolverRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResolverRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListResolverRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListResolverRules.html#Route53Resolver.Paginator.ListResolverRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listresolverrulespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListTagsForResource.html#Route53Resolver.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/paginator/ListTagsForResource.html#Route53Resolver.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/paginators/#listtagsforresourcepaginator)
        """
