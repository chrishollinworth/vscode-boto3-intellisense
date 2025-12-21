"""
Main interface for securityhub service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_securityhub import (
        Client,
        DescribeActionTargetsPaginator,
        DescribeProductsPaginator,
        DescribeProductsV2Paginator,
        DescribeStandardsControlsPaginator,
        DescribeStandardsPaginator,
        GetEnabledStandardsPaginator,
        GetFindingHistoryPaginator,
        GetFindingsPaginator,
        GetFindingsTrendsV2Paginator,
        GetFindingsV2Paginator,
        GetInsightsPaginator,
        GetResourcesTrendsV2Paginator,
        GetResourcesV2Paginator,
        ListAggregatorsV2Paginator,
        ListConfigurationPoliciesPaginator,
        ListConfigurationPolicyAssociationsPaginator,
        ListEnabledProductsForImportPaginator,
        ListFindingAggregatorsPaginator,
        ListInvitationsPaginator,
        ListMembersPaginator,
        ListOrganizationAdminAccountsPaginator,
        ListSecurityControlDefinitionsPaginator,
        ListStandardsControlAssociationsPaginator,
        SecurityHubClient,
    )

    session = Session()
    client: SecurityHubClient = session.client("securityhub")

    describe_action_targets_paginator: DescribeActionTargetsPaginator = client.get_paginator("describe_action_targets")
    describe_products_paginator: DescribeProductsPaginator = client.get_paginator("describe_products")
    describe_products_v2_paginator: DescribeProductsV2Paginator = client.get_paginator("describe_products_v2")
    describe_standards_controls_paginator: DescribeStandardsControlsPaginator = client.get_paginator("describe_standards_controls")
    describe_standards_paginator: DescribeStandardsPaginator = client.get_paginator("describe_standards")
    get_enabled_standards_paginator: GetEnabledStandardsPaginator = client.get_paginator("get_enabled_standards")
    get_finding_history_paginator: GetFindingHistoryPaginator = client.get_paginator("get_finding_history")
    get_findings_paginator: GetFindingsPaginator = client.get_paginator("get_findings")
    get_findings_trends_v2_paginator: GetFindingsTrendsV2Paginator = client.get_paginator("get_findings_trends_v2")
    get_findings_v2_paginator: GetFindingsV2Paginator = client.get_paginator("get_findings_v2")
    get_insights_paginator: GetInsightsPaginator = client.get_paginator("get_insights")
    get_resources_trends_v2_paginator: GetResourcesTrendsV2Paginator = client.get_paginator("get_resources_trends_v2")
    get_resources_v2_paginator: GetResourcesV2Paginator = client.get_paginator("get_resources_v2")
    list_aggregators_v2_paginator: ListAggregatorsV2Paginator = client.get_paginator("list_aggregators_v2")
    list_configuration_policies_paginator: ListConfigurationPoliciesPaginator = client.get_paginator("list_configuration_policies")
    list_configuration_policy_associations_paginator: ListConfigurationPolicyAssociationsPaginator = client.get_paginator("list_configuration_policy_associations")
    list_enabled_products_for_import_paginator: ListEnabledProductsForImportPaginator = client.get_paginator("list_enabled_products_for_import")
    list_finding_aggregators_paginator: ListFindingAggregatorsPaginator = client.get_paginator("list_finding_aggregators")
    list_invitations_paginator: ListInvitationsPaginator = client.get_paginator("list_invitations")
    list_members_paginator: ListMembersPaginator = client.get_paginator("list_members")
    list_organization_admin_accounts_paginator: ListOrganizationAdminAccountsPaginator = client.get_paginator("list_organization_admin_accounts")
    list_security_control_definitions_paginator: ListSecurityControlDefinitionsPaginator = client.get_paginator("list_security_control_definitions")
    list_standards_control_associations_paginator: ListStandardsControlAssociationsPaginator = client.get_paginator("list_standards_control_associations")
    ```
"""

from .client import SecurityHubClient
from .paginator import (
    DescribeActionTargetsPaginator,
    DescribeProductsPaginator,
    DescribeProductsV2Paginator,
    DescribeStandardsControlsPaginator,
    DescribeStandardsPaginator,
    GetEnabledStandardsPaginator,
    GetFindingHistoryPaginator,
    GetFindingsPaginator,
    GetFindingsTrendsV2Paginator,
    GetFindingsV2Paginator,
    GetInsightsPaginator,
    GetResourcesTrendsV2Paginator,
    GetResourcesV2Paginator,
    ListAggregatorsV2Paginator,
    ListConfigurationPoliciesPaginator,
    ListConfigurationPolicyAssociationsPaginator,
    ListEnabledProductsForImportPaginator,
    ListFindingAggregatorsPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListSecurityControlDefinitionsPaginator,
    ListStandardsControlAssociationsPaginator,
)

Client = SecurityHubClient

__all__ = (
    "Client",
    "DescribeActionTargetsPaginator",
    "DescribeProductsPaginator",
    "DescribeProductsV2Paginator",
    "DescribeStandardsControlsPaginator",
    "DescribeStandardsPaginator",
    "GetEnabledStandardsPaginator",
    "GetFindingHistoryPaginator",
    "GetFindingsPaginator",
    "GetFindingsTrendsV2Paginator",
    "GetFindingsV2Paginator",
    "GetInsightsPaginator",
    "GetResourcesTrendsV2Paginator",
    "GetResourcesV2Paginator",
    "ListAggregatorsV2Paginator",
    "ListConfigurationPoliciesPaginator",
    "ListConfigurationPolicyAssociationsPaginator",
    "ListEnabledProductsForImportPaginator",
    "ListFindingAggregatorsPaginator",
    "ListInvitationsPaginator",
    "ListMembersPaginator",
    "ListOrganizationAdminAccountsPaginator",
    "ListSecurityControlDefinitionsPaginator",
    "ListStandardsControlAssociationsPaginator",
    "SecurityHubClient",
)
