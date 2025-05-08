"""
Main interface for config service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_config/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_config import (
        Client,
        ConfigServiceClient,
        DescribeAggregateComplianceByConfigRulesPaginator,
        DescribeAggregateComplianceByConformancePacksPaginator,
        DescribeAggregationAuthorizationsPaginator,
        DescribeComplianceByConfigRulePaginator,
        DescribeComplianceByResourcePaginator,
        DescribeConfigRuleEvaluationStatusPaginator,
        DescribeConfigRulesPaginator,
        DescribeConfigurationAggregatorSourcesStatusPaginator,
        DescribeConfigurationAggregatorsPaginator,
        DescribeConformancePackStatusPaginator,
        DescribeConformancePacksPaginator,
        DescribeOrganizationConfigRuleStatusesPaginator,
        DescribeOrganizationConfigRulesPaginator,
        DescribeOrganizationConformancePackStatusesPaginator,
        DescribeOrganizationConformancePacksPaginator,
        DescribePendingAggregationRequestsPaginator,
        DescribeRemediationExecutionStatusPaginator,
        DescribeRetentionConfigurationsPaginator,
        GetAggregateComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByResourcePaginator,
        GetConformancePackComplianceSummaryPaginator,
        GetOrganizationConfigRuleDetailedStatusPaginator,
        GetOrganizationConformancePackDetailedStatusPaginator,
        GetResourceConfigHistoryPaginator,
        ListAggregateDiscoveredResourcesPaginator,
        ListConfigurationRecordersPaginator,
        ListDiscoveredResourcesPaginator,
        ListResourceEvaluationsPaginator,
        ListTagsForResourcePaginator,
        SelectAggregateResourceConfigPaginator,
        SelectResourceConfigPaginator,
    )

    session = Session()
    client: ConfigServiceClient = session.client("config")

    describe_aggregate_compliance_by_config_rules_paginator: DescribeAggregateComplianceByConfigRulesPaginator = client.get_paginator("describe_aggregate_compliance_by_config_rules")
    describe_aggregate_compliance_by_conformance_packs_paginator: DescribeAggregateComplianceByConformancePacksPaginator = client.get_paginator("describe_aggregate_compliance_by_conformance_packs")
    describe_aggregation_authorizations_paginator: DescribeAggregationAuthorizationsPaginator = client.get_paginator("describe_aggregation_authorizations")
    describe_compliance_by_config_rule_paginator: DescribeComplianceByConfigRulePaginator = client.get_paginator("describe_compliance_by_config_rule")
    describe_compliance_by_resource_paginator: DescribeComplianceByResourcePaginator = client.get_paginator("describe_compliance_by_resource")
    describe_config_rule_evaluation_status_paginator: DescribeConfigRuleEvaluationStatusPaginator = client.get_paginator("describe_config_rule_evaluation_status")
    describe_config_rules_paginator: DescribeConfigRulesPaginator = client.get_paginator("describe_config_rules")
    describe_configuration_aggregator_sources_status_paginator: DescribeConfigurationAggregatorSourcesStatusPaginator = client.get_paginator("describe_configuration_aggregator_sources_status")
    describe_configuration_aggregators_paginator: DescribeConfigurationAggregatorsPaginator = client.get_paginator("describe_configuration_aggregators")
    describe_conformance_pack_status_paginator: DescribeConformancePackStatusPaginator = client.get_paginator("describe_conformance_pack_status")
    describe_conformance_packs_paginator: DescribeConformancePacksPaginator = client.get_paginator("describe_conformance_packs")
    describe_organization_config_rule_statuses_paginator: DescribeOrganizationConfigRuleStatusesPaginator = client.get_paginator("describe_organization_config_rule_statuses")
    describe_organization_config_rules_paginator: DescribeOrganizationConfigRulesPaginator = client.get_paginator("describe_organization_config_rules")
    describe_organization_conformance_pack_statuses_paginator: DescribeOrganizationConformancePackStatusesPaginator = client.get_paginator("describe_organization_conformance_pack_statuses")
    describe_organization_conformance_packs_paginator: DescribeOrganizationConformancePacksPaginator = client.get_paginator("describe_organization_conformance_packs")
    describe_pending_aggregation_requests_paginator: DescribePendingAggregationRequestsPaginator = client.get_paginator("describe_pending_aggregation_requests")
    describe_remediation_execution_status_paginator: DescribeRemediationExecutionStatusPaginator = client.get_paginator("describe_remediation_execution_status")
    describe_retention_configurations_paginator: DescribeRetentionConfigurationsPaginator = client.get_paginator("describe_retention_configurations")
    get_aggregate_compliance_details_by_config_rule_paginator: GetAggregateComplianceDetailsByConfigRulePaginator = client.get_paginator("get_aggregate_compliance_details_by_config_rule")
    get_compliance_details_by_config_rule_paginator: GetComplianceDetailsByConfigRulePaginator = client.get_paginator("get_compliance_details_by_config_rule")
    get_compliance_details_by_resource_paginator: GetComplianceDetailsByResourcePaginator = client.get_paginator("get_compliance_details_by_resource")
    get_conformance_pack_compliance_summary_paginator: GetConformancePackComplianceSummaryPaginator = client.get_paginator("get_conformance_pack_compliance_summary")
    get_organization_config_rule_detailed_status_paginator: GetOrganizationConfigRuleDetailedStatusPaginator = client.get_paginator("get_organization_config_rule_detailed_status")
    get_organization_conformance_pack_detailed_status_paginator: GetOrganizationConformancePackDetailedStatusPaginator = client.get_paginator("get_organization_conformance_pack_detailed_status")
    get_resource_config_history_paginator: GetResourceConfigHistoryPaginator = client.get_paginator("get_resource_config_history")
    list_aggregate_discovered_resources_paginator: ListAggregateDiscoveredResourcesPaginator = client.get_paginator("list_aggregate_discovered_resources")
    list_configuration_recorders_paginator: ListConfigurationRecordersPaginator = client.get_paginator("list_configuration_recorders")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_resource_evaluations_paginator: ListResourceEvaluationsPaginator = client.get_paginator("list_resource_evaluations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    select_aggregate_resource_config_paginator: SelectAggregateResourceConfigPaginator = client.get_paginator("select_aggregate_resource_config")
    select_resource_config_paginator: SelectResourceConfigPaginator = client.get_paginator("select_resource_config")
    ```
"""

from .client import ConfigServiceClient
from .paginator import (
    DescribeAggregateComplianceByConfigRulesPaginator,
    DescribeAggregateComplianceByConformancePacksPaginator,
    DescribeAggregationAuthorizationsPaginator,
    DescribeComplianceByConfigRulePaginator,
    DescribeComplianceByResourcePaginator,
    DescribeConfigRuleEvaluationStatusPaginator,
    DescribeConfigRulesPaginator,
    DescribeConfigurationAggregatorSourcesStatusPaginator,
    DescribeConfigurationAggregatorsPaginator,
    DescribeConformancePacksPaginator,
    DescribeConformancePackStatusPaginator,
    DescribeOrganizationConfigRulesPaginator,
    DescribeOrganizationConfigRuleStatusesPaginator,
    DescribeOrganizationConformancePacksPaginator,
    DescribeOrganizationConformancePackStatusesPaginator,
    DescribePendingAggregationRequestsPaginator,
    DescribeRemediationExecutionStatusPaginator,
    DescribeRetentionConfigurationsPaginator,
    GetAggregateComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByResourcePaginator,
    GetConformancePackComplianceSummaryPaginator,
    GetOrganizationConfigRuleDetailedStatusPaginator,
    GetOrganizationConformancePackDetailedStatusPaginator,
    GetResourceConfigHistoryPaginator,
    ListAggregateDiscoveredResourcesPaginator,
    ListConfigurationRecordersPaginator,
    ListDiscoveredResourcesPaginator,
    ListResourceEvaluationsPaginator,
    ListTagsForResourcePaginator,
    SelectAggregateResourceConfigPaginator,
    SelectResourceConfigPaginator,
)

Client = ConfigServiceClient

__all__ = (
    "Client",
    "ConfigServiceClient",
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregateComplianceByConformancePacksPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribeConformancePackStatusPaginator",
    "DescribeConformancePacksPaginator",
    "DescribeOrganizationConfigRuleStatusesPaginator",
    "DescribeOrganizationConfigRulesPaginator",
    "DescribeOrganizationConformancePackStatusesPaginator",
    "DescribeOrganizationConformancePacksPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetConformancePackComplianceSummaryPaginator",
    "GetOrganizationConfigRuleDetailedStatusPaginator",
    "GetOrganizationConformancePackDetailedStatusPaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListConfigurationRecordersPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListResourceEvaluationsPaginator",
    "ListTagsForResourcePaginator",
    "SelectAggregateResourceConfigPaginator",
    "SelectResourceConfigPaginator",
)
