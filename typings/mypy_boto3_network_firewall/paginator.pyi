"""
Type annotations for network-firewall service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_network_firewall import NetworkFirewallClient
    from mypy_boto3_network_firewall.paginator import (
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListRuleGroupsPaginator,
        ListTLSInspectionConfigurationsPaginator,
        ListTagsForResourcePaginator,
    )

    client: NetworkFirewallClient = boto3.client("network-firewall")

    list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
    list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_tls_inspection_configurations_paginator: ListTLSInspectionConfigurationsPaginator = client.get_paginator("list_tls_inspection_configurations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ResourceManagedStatusType, ResourceManagedTypeType, RuleGroupTypeType
from .type_defs import (
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTLSInspectionConfigurationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListRuleGroupsPaginator",
    "ListTLSInspectionConfigurationsPaginator",
    "ListTagsForResourcePaginator",
)

class ListFirewallPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallpoliciespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallpoliciespaginator)
        """

class ListFirewallsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallspaginator)
    """

    def paginate(
        self, *, VpcIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFirewallsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallspaginator)
        """

class ListRuleGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listrulegroupspaginator)
    """

    def paginate(
        self,
        *,
        Scope: ResourceManagedStatusType = None,
        ManagedType: ResourceManagedTypeType = None,
        Type: RuleGroupTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRuleGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listrulegroupspaginator)
        """

class ListTLSInspectionConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtlsinspectionconfigurationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTLSInspectionConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtlsinspectionconfigurationspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtagsforresourcepaginator)
        """
