"""
Type annotations for network-firewall service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_network_firewall.client import NetworkFirewallClient
    from mypy_boto3_network_firewall.paginator import (
        GetAnalysisReportResultsPaginator,
        ListAnalysisReportsPaginator,
        ListFirewallPoliciesPaginator,
        ListFirewallsPaginator,
        ListFlowOperationResultsPaginator,
        ListFlowOperationsPaginator,
        ListRuleGroupsPaginator,
        ListTLSInspectionConfigurationsPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: NetworkFirewallClient = session.client("network-firewall")

    get_analysis_report_results_paginator: GetAnalysisReportResultsPaginator = client.get_paginator("get_analysis_report_results")
    list_analysis_reports_paginator: ListAnalysisReportsPaginator = client.get_paginator("list_analysis_reports")
    list_firewall_policies_paginator: ListFirewallPoliciesPaginator = client.get_paginator("list_firewall_policies")
    list_firewalls_paginator: ListFirewallsPaginator = client.get_paginator("list_firewalls")
    list_flow_operation_results_paginator: ListFlowOperationResultsPaginator = client.get_paginator("list_flow_operation_results")
    list_flow_operations_paginator: ListFlowOperationsPaginator = client.get_paginator("list_flow_operations")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_tls_inspection_configurations_paginator: ListTLSInspectionConfigurationsPaginator = client.get_paginator("list_tls_inspection_configurations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAnalysisReportResultsRequestPaginateTypeDef,
    GetAnalysisReportResultsResponseTypeDef,
    ListAnalysisReportsRequestPaginateTypeDef,
    ListAnalysisReportsResponseTypeDef,
    ListFirewallPoliciesRequestPaginateTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsRequestPaginateTypeDef,
    ListFirewallsResponseTypeDef,
    ListFlowOperationResultsRequestPaginateTypeDef,
    ListFlowOperationResultsResponseTypeDef,
    ListFlowOperationsRequestPaginateTypeDef,
    ListFlowOperationsResponseTypeDef,
    ListRuleGroupsRequestPaginateTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTLSInspectionConfigurationsRequestPaginateTypeDef,
    ListTLSInspectionConfigurationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetAnalysisReportResultsPaginator",
    "ListAnalysisReportsPaginator",
    "ListFirewallPoliciesPaginator",
    "ListFirewallsPaginator",
    "ListFlowOperationResultsPaginator",
    "ListFlowOperationsPaginator",
    "ListRuleGroupsPaginator",
    "ListTLSInspectionConfigurationsPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _GetAnalysisReportResultsPaginatorBase = Paginator[GetAnalysisReportResultsResponseTypeDef]
else:
    _GetAnalysisReportResultsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnalysisReportResultsPaginator(_GetAnalysisReportResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/GetAnalysisReportResults.html#NetworkFirewall.Paginator.GetAnalysisReportResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#getanalysisreportresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnalysisReportResultsRequestPaginateTypeDef]
    ) -> PageIterator[GetAnalysisReportResultsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/GetAnalysisReportResults.html#NetworkFirewall.Paginator.GetAnalysisReportResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#getanalysisreportresultspaginator)
        """

if TYPE_CHECKING:
    _ListAnalysisReportsPaginatorBase = Paginator[ListAnalysisReportsResponseTypeDef]
else:
    _ListAnalysisReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnalysisReportsPaginator(_ListAnalysisReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListAnalysisReports.html#NetworkFirewall.Paginator.ListAnalysisReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listanalysisreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnalysisReportsRequestPaginateTypeDef]
    ) -> PageIterator[ListAnalysisReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListAnalysisReports.html#NetworkFirewall.Paginator.ListAnalysisReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listanalysisreportspaginator)
        """

if TYPE_CHECKING:
    _ListFirewallPoliciesPaginatorBase = Paginator[ListFirewallPoliciesResponseTypeDef]
else:
    _ListFirewallPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallPoliciesPaginator(_ListFirewallPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFirewallPolicies.html#NetworkFirewall.Paginator.ListFirewallPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listfirewallpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFirewallPolicies.html#NetworkFirewall.Paginator.ListFirewallPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listfirewallpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListFirewallsPaginatorBase = Paginator[ListFirewallsResponseTypeDef]
else:
    _ListFirewallsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFirewallsPaginator(_ListFirewallsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFirewalls.html#NetworkFirewall.Paginator.ListFirewalls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listfirewallspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFirewallsRequestPaginateTypeDef]
    ) -> PageIterator[ListFirewallsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFirewalls.html#NetworkFirewall.Paginator.ListFirewalls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listfirewallspaginator)
        """

if TYPE_CHECKING:
    _ListFlowOperationResultsPaginatorBase = Paginator[ListFlowOperationResultsResponseTypeDef]
else:
    _ListFlowOperationResultsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowOperationResultsPaginator(_ListFlowOperationResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFlowOperationResults.html#NetworkFirewall.Paginator.ListFlowOperationResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listflowoperationresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowOperationResultsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowOperationResultsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFlowOperationResults.html#NetworkFirewall.Paginator.ListFlowOperationResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listflowoperationresultspaginator)
        """

if TYPE_CHECKING:
    _ListFlowOperationsPaginatorBase = Paginator[ListFlowOperationsResponseTypeDef]
else:
    _ListFlowOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowOperationsPaginator(_ListFlowOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFlowOperations.html#NetworkFirewall.Paginator.ListFlowOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listflowoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListFlowOperations.html#NetworkFirewall.Paginator.ListFlowOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listflowoperationspaginator)
        """

if TYPE_CHECKING:
    _ListRuleGroupsPaginatorBase = Paginator[ListRuleGroupsResponseTypeDef]
else:
    _ListRuleGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRuleGroupsPaginator(_ListRuleGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListRuleGroups.html#NetworkFirewall.Paginator.ListRuleGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listrulegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRuleGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListRuleGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListRuleGroups.html#NetworkFirewall.Paginator.ListRuleGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listrulegroupspaginator)
        """

if TYPE_CHECKING:
    _ListTLSInspectionConfigurationsPaginatorBase = Paginator[
        ListTLSInspectionConfigurationsResponseTypeDef
    ]
else:
    _ListTLSInspectionConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTLSInspectionConfigurationsPaginator(_ListTLSInspectionConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListTLSInspectionConfigurations.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listtlsinspectionconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTLSInspectionConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListTLSInspectionConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListTLSInspectionConfigurations.html#NetworkFirewall.Paginator.ListTLSInspectionConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listtlsinspectionconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListTagsForResource.html#NetworkFirewall.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall/paginator/ListTagsForResource.html#NetworkFirewall.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators/#listtagsforresourcepaginator)
        """
