"""
Type annotations for config service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_config import ConfigServiceClient
    from mypy_boto3_config.paginator import (
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
        ListDiscoveredResourcesPaginator,
        ListResourceEvaluationsPaginator,
        ListTagsForResourcePaginator,
        SelectAggregateResourceConfigPaginator,
        SelectResourceConfigPaginator,
    )

    client: ConfigServiceClient = boto3.client("config")

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
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_resource_evaluations_paginator: ListResourceEvaluationsPaginator = client.get_paginator("list_resource_evaluations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    select_aggregate_resource_config_paginator: SelectAggregateResourceConfigPaginator = client.get_paginator("select_aggregate_resource_config")
    select_resource_config_paginator: SelectResourceConfigPaginator = client.get_paginator("select_resource_config")
    ```
"""

from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AggregatedSourceStatusTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ResourceTypeType,
)
from .type_defs import (
    AggregateConformancePackComplianceFiltersTypeDef,
    ConfigRuleComplianceFiltersTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregateComplianceByConformancePacksResponseTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesFiltersTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribeConformancePacksResponseTypeDef,
    DescribeConformancePackStatusResponseTypeDef,
    DescribeOrganizationConfigRulesResponseTypeDef,
    DescribeOrganizationConfigRuleStatusesResponseTypeDef,
    DescribeOrganizationConformancePacksResponseTypeDef,
    DescribeOrganizationConformancePackStatusesResponseTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetConformancePackComplianceSummaryResponseTypeDef,
    GetOrganizationConfigRuleDetailedStatusResponseTypeDef,
    GetOrganizationConformancePackDetailedStatusResponseTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListResourceEvaluationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OrganizationResourceDetailedStatusFiltersTypeDef,
    PaginatorConfigTypeDef,
    ResourceEvaluationFiltersTypeDef,
    ResourceFiltersTypeDef,
    ResourceKeyTypeDef,
    SelectAggregateResourceConfigResponseTypeDef,
    SelectResourceConfigResponseTypeDef,
    StatusDetailFiltersTypeDef,
)

__all__ = (
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
    "ListDiscoveredResourcesPaginator",
    "ListResourceEvaluationsPaginator",
    "ListTagsForResourcePaginator",
    "SelectAggregateResourceConfigPaginator",
    "SelectResourceConfigPaginator",
)

class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconfigrulespaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: "ConfigRuleComplianceFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregateComplianceByConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconfigrulespaginator)
        """

class DescribeAggregateComplianceByConformancePacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConformancePacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconformancepackspaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorName: str,
        Filters: "AggregateConformancePackComplianceFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregateComplianceByConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConformancePacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregatecompliancebyconformancepackspaginator)
        """

class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregationauthorizationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregationAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeaggregationauthorizationspaginator)
        """

class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyconfigrulepaginator)
    """

    def paginate(
        self,
        *,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[ComplianceTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComplianceByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyconfigrulepaginator)
        """

class DescribeComplianceByResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[ComplianceTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComplianceByResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describecompliancebyresourcepaginator)
        """

class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigruleevaluationstatuspaginator)
    """

    def paginate(
        self, *, ConfigRuleNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRuleEvaluationStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigruleevaluationstatuspaginator)
        """

class DescribeConfigRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigrulespaginator)
    """

    def paginate(
        self,
        *,
        ConfigRuleNames: List[str] = None,
        Filters: "DescribeConfigRulesFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigrulespaginator)
        """

class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorsourcesstatuspaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[AggregatedSourceStatusTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigurationAggregatorSourcesStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorsourcesstatuspaginator)
        """

class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorspaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigurationAggregatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconfigurationaggregatorspaginator)
        """

class DescribeConformancePackStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConformancePackStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackstatuspaginator)
    """

    def paginate(
        self,
        *,
        ConformancePackNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConformancePackStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConformancePackStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackstatuspaginator)
        """

class DescribeConformancePacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConformancePacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackspaginator)
    """

    def paginate(
        self,
        *,
        ConformancePackNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeConformancePacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeconformancepackspaginator)
        """

class DescribeOrganizationConfigRuleStatusesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRuleStatuses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulestatusespaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConfigRuleNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrganizationConfigRuleStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRuleStatuses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulestatusespaginator)
        """

class DescribeOrganizationConfigRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulespaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConfigRuleNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrganizationConfigRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConfigRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconfigrulespaginator)
        """

class DescribeOrganizationConformancePackStatusesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePackStatuses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackstatusespaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConformancePackNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrganizationConformancePackStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePackStatuses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackstatusespaginator)
        """

class DescribeOrganizationConformancePacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackspaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConformancePackNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrganizationConformancePacksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeOrganizationConformancePacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeorganizationconformancepackspaginator)
        """

class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describependingaggregationrequestspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePendingAggregationRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describependingaggregationrequestspaginator)
        """

class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeremediationexecutionstatuspaginator)
    """

    def paginate(
        self,
        *,
        ConfigRuleName: str,
        ResourceKeys: List["ResourceKeyTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRemediationExecutionStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeremediationexecutionstatuspaginator)
        """

class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeretentionconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRetentionConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#describeretentionconfigurationspaginator)
        """

class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getaggregatecompliancedetailsbyconfigrulepaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: ComplianceTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAggregateComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getaggregatecompliancedetailsbyconfigrulepaginator)
        """

class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyconfigrulepaginator)
    """

    def paginate(
        self,
        *,
        ConfigRuleName: str,
        ComplianceTypes: List[ComplianceTypeType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyconfigrulepaginator)
        """

class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyresourcepaginator)
    """

    def paginate(
        self,
        *,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[ComplianceTypeType] = None,
        ResourceEvaluationId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetComplianceDetailsByResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getcompliancedetailsbyresourcepaginator)
        """

class GetConformancePackComplianceSummaryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetConformancePackComplianceSummary)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getconformancepackcompliancesummarypaginator)
    """

    def paginate(
        self, *, ConformancePackNames: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConformancePackComplianceSummaryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetConformancePackComplianceSummary.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getconformancepackcompliancesummarypaginator)
        """

class GetOrganizationConfigRuleDetailedStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetOrganizationConfigRuleDetailedStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconfigruledetailedstatuspaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConfigRuleName: str,
        Filters: "StatusDetailFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOrganizationConfigRuleDetailedStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetOrganizationConfigRuleDetailedStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconfigruledetailedstatuspaginator)
        """

class GetOrganizationConformancePackDetailedStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetOrganizationConformancePackDetailedStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconformancepackdetailedstatuspaginator)
    """

    def paginate(
        self,
        *,
        OrganizationConformancePackName: str,
        Filters: "OrganizationResourceDetailedStatusFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOrganizationConformancePackDetailedStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetOrganizationConformancePackDetailedStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getorganizationconformancepackdetailedstatuspaginator)
        """

class GetResourceConfigHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getresourceconfighistorypaginator)
    """

    def paginate(
        self,
        *,
        resourceType: ResourceTypeType,
        resourceId: str,
        laterTime: Union[datetime, str] = None,
        earlierTime: Union[datetime, str] = None,
        chronologicalOrder: ChronologicalOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceConfigHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#getresourceconfighistorypaginator)
        """

class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listaggregatediscoveredresourcespaginator)
    """

    def paginate(
        self,
        *,
        ConfigurationAggregatorName: str,
        ResourceType: ResourceTypeType,
        Filters: "ResourceFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAggregateDiscoveredResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listaggregatediscoveredresourcespaginator)
        """

class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listdiscoveredresourcespaginator)
    """

    def paginate(
        self,
        *,
        resourceType: ResourceTypeType,
        resourceIds: List[str] = None,
        resourceName: str = None,
        includeDeletedResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDiscoveredResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listdiscoveredresourcespaginator)
        """

class ListResourceEvaluationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListResourceEvaluations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listresourceevaluationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: "ResourceEvaluationFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListResourceEvaluations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listresourceevaluationspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#listtagsforresourcepaginator)
        """

class SelectAggregateResourceConfigPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.SelectAggregateResourceConfig)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectaggregateresourceconfigpaginator)
    """

    def paginate(
        self,
        *,
        Expression: str,
        ConfigurationAggregatorName: str,
        MaxResults: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SelectAggregateResourceConfigResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.SelectAggregateResourceConfig.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectaggregateresourceconfigpaginator)
        """

class SelectResourceConfigPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.SelectResourceConfig)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectresourceconfigpaginator)
    """

    def paginate(
        self, *, Expression: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SelectResourceConfigResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/config.html#ConfigService.Paginator.SelectResourceConfig.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/paginators.html#selectresourceconfigpaginator)
        """
