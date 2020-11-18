"""
Main interface for network-firewall service.

Usage::

    ```python
    import boto3
    from mypy_boto3_network_firewall import (
        Client,
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListRuleGroupsPaginator,
        ListTagsForResourcePaginator,
        NetworkFirewallClient,
    )

    session = boto3.Session()

    client: NetworkFirewallClient = boto3.client("network-firewall")
    session_client: NetworkFirewallClient = session.client("network-firewall")

    list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
    list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from mypy_boto3_network_firewall.client import NetworkFirewallClient
from mypy_boto3_network_firewall.paginator import (
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
)

Client = NetworkFirewallClient


__all__ = (
    "Client",
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListRuleGroupsPaginator",
    "ListTagsForResourcePaginator",
    "NetworkFirewallClient",
)
