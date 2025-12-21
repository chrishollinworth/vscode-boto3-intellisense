"""
Main interface for network-firewall service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_network_firewall import (
        Client,
        GetAnalysisReportResultsPaginator,
        ListAnalysisReportsPaginator,
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListFlowOperationResultsPaginator,
        ListFlowOperationsPaginator,
        ListProxiesPaginator,
        ListProxyConfigurationsPaginator,
        ListProxyRuleGroupsPaginator,
        ListRuleGroupsPaginator,
        ListTLSInspectionConfigurationsPaginator,
        ListTagsForResourcePaginator,
        ListVpcEndpointAssociationsPaginator,
        NetworkFirewallClient,
    )

    session = Session()
    client: NetworkFirewallClient = session.client("network-firewall")

    get_analysis_report_results_paginator: GetAnalysisReportResultsPaginator = client.get_paginator("get_analysis_report_results")
    list_analysis_reports_paginator: ListAnalysisReportsPaginator = client.get_paginator("list_analysis_reports")
    list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
    list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
    list_flow_operation_results_paginator: ListFlowOperationResultsPaginator = client.get_paginator("list_flow_operation_results")
    list_flow_operations_paginator: ListFlowOperationsPaginator = client.get_paginator("list_flow_operations")
    list_proxies_paginator: ListProxiesPaginator = client.get_paginator("list_proxies")
    list_proxy_configurations_paginator: ListProxyConfigurationsPaginator = client.get_paginator("list_proxy_configurations")
    list_proxy_rule_groups_paginator: ListProxyRuleGroupsPaginator = client.get_paginator("list_proxy_rule_groups")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_tls_inspection_configurations_paginator: ListTLSInspectionConfigurationsPaginator = client.get_paginator("list_tls_inspection_configurations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_vpc_endpoint_associations_paginator: ListVpcEndpointAssociationsPaginator = client.get_paginator("list_vpc_endpoint_associations")
    ```
"""

from .client import NetworkFirewallClient
from .paginator import (
    GetAnalysisReportResultsPaginator,
    ListAnalysisReportsPaginator,
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListFlowOperationResultsPaginator,
    ListFlowOperationsPaginator,
    ListProxiesPaginator,
    ListProxyConfigurationsPaginator,
    ListProxyRuleGroupsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
    ListTLSInspectionConfigurationsPaginator,
    ListVpcEndpointAssociationsPaginator,
)

Client = NetworkFirewallClient

__all__ = (
    "Client",
    "GetAnalysisReportResultsPaginator",
    "ListAnalysisReportsPaginator",
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListFlowOperationResultsPaginator",
    "ListFlowOperationsPaginator",
    "ListProxiesPaginator",
    "ListProxyConfigurationsPaginator",
    "ListProxyRuleGroupsPaginator",
    "ListRuleGroupsPaginator",
    "ListTLSInspectionConfigurationsPaginator",
    "ListTagsForResourcePaginator",
    "ListVpcEndpointAssociationsPaginator",
    "NetworkFirewallClient",
)
