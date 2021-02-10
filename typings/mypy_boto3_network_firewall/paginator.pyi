"""
Main interface for network-firewall service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_network_firewall import NetworkFirewallClient
    from mypy_boto3_network_firewall.paginator import (
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListRuleGroupsPaginator,
        ListTagsForResourcePaginator,
    )

    client: NetworkFirewallClient = boto3.client("network-firewall")

    list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
    list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_network_firewall.type_defs import (
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListRuleGroupsPaginator",
    "ListTagsForResourcePaginator",
)


class ListFirewallPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListFirewallPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallPoliciesResponseTypeDef]:
        """
        [ListFirewallPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies.paginate)
        """


class ListFirewallsPaginator(Boto3Paginator):
    """
    [Paginator.ListFirewalls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
    """

    def paginate(
        self, VpcIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallsResponseTypeDef]:
        """
        [ListFirewalls.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls.paginate)
        """


class ListRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRuleGroupsResponseTypeDef]:
        """
        [ListRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource.paginate)
        """
