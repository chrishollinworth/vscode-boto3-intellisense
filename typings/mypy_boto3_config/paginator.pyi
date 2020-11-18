# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for config service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_config import ConfigServiceClient
    from mypy_boto3_config.paginator import (
        DescribeAggregateComplianceByConfigRulesPaginator,
        DescribeAggregationAuthorizationsPaginator,
        DescribeComplianceByConfigRulePaginator,
        DescribeComplianceByResourcePaginator,
        DescribeConfigRuleEvaluationStatusPaginator,
        DescribeConfigRulesPaginator,
        DescribeConfigurationAggregatorSourcesStatusPaginator,
        DescribeConfigurationAggregatorsPaginator,
        DescribePendingAggregationRequestsPaginator,
        DescribeRemediationExecutionStatusPaginator,
        DescribeRetentionConfigurationsPaginator,
        GetAggregateComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByConfigRulePaginator,
        GetComplianceDetailsByResourcePaginator,
        GetResourceConfigHistoryPaginator,
        ListAggregateDiscoveredResourcesPaginator,
        ListDiscoveredResourcesPaginator,
    )

    client: ConfigServiceClient = boto3.client("config")

    describe_aggregate_compliance_by_config_rules_paginator: DescribeAggregateComplianceByConfigRulesPaginator = client.get_paginator("describe_aggregate_compliance_by_config_rules")
    describe_aggregation_authorizations_paginator: DescribeAggregationAuthorizationsPaginator = client.get_paginator("describe_aggregation_authorizations")
    describe_compliance_by_config_rule_paginator: DescribeComplianceByConfigRulePaginator = client.get_paginator("describe_compliance_by_config_rule")
    describe_compliance_by_resource_paginator: DescribeComplianceByResourcePaginator = client.get_paginator("describe_compliance_by_resource")
    describe_config_rule_evaluation_status_paginator: DescribeConfigRuleEvaluationStatusPaginator = client.get_paginator("describe_config_rule_evaluation_status")
    describe_config_rules_paginator: DescribeConfigRulesPaginator = client.get_paginator("describe_config_rules")
    describe_configuration_aggregator_sources_status_paginator: DescribeConfigurationAggregatorSourcesStatusPaginator = client.get_paginator("describe_configuration_aggregator_sources_status")
    describe_configuration_aggregators_paginator: DescribeConfigurationAggregatorsPaginator = client.get_paginator("describe_configuration_aggregators")
    describe_pending_aggregation_requests_paginator: DescribePendingAggregationRequestsPaginator = client.get_paginator("describe_pending_aggregation_requests")
    describe_remediation_execution_status_paginator: DescribeRemediationExecutionStatusPaginator = client.get_paginator("describe_remediation_execution_status")
    describe_retention_configurations_paginator: DescribeRetentionConfigurationsPaginator = client.get_paginator("describe_retention_configurations")
    get_aggregate_compliance_details_by_config_rule_paginator: GetAggregateComplianceDetailsByConfigRulePaginator = client.get_paginator("get_aggregate_compliance_details_by_config_rule")
    get_compliance_details_by_config_rule_paginator: GetComplianceDetailsByConfigRulePaginator = client.get_paginator("get_compliance_details_by_config_rule")
    get_compliance_details_by_resource_paginator: GetComplianceDetailsByResourcePaginator = client.get_paginator("get_compliance_details_by_resource")
    get_resource_config_history_paginator: GetResourceConfigHistoryPaginator = client.get_paginator("get_resource_config_history")
    list_aggregate_discovered_resources_paginator: ListAggregateDiscoveredResourcesPaginator = client.get_paginator("list_aggregate_discovered_resources")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_config.type_defs import (
    ConfigRuleComplianceFiltersTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    PaginatorConfigTypeDef,
    ResourceFiltersTypeDef,
    ResourceKeyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAggregateComplianceByConfigRulesPaginator",
    "DescribeAggregationAuthorizationsPaginator",
    "DescribeComplianceByConfigRulePaginator",
    "DescribeComplianceByResourcePaginator",
    "DescribeConfigRuleEvaluationStatusPaginator",
    "DescribeConfigRulesPaginator",
    "DescribeConfigurationAggregatorSourcesStatusPaginator",
    "DescribeConfigurationAggregatorsPaginator",
    "DescribePendingAggregationRequestsPaginator",
    "DescribeRemediationExecutionStatusPaginator",
    "DescribeRetentionConfigurationsPaginator",
    "GetAggregateComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByConfigRulePaginator",
    "GetComplianceDetailsByResourcePaginator",
    "GetResourceConfigHistoryPaginator",
    "ListAggregateDiscoveredResourcesPaginator",
    "ListDiscoveredResourcesPaginator",
)


class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
    """

    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAggregateComplianceByConfigRulesResponseTypeDef]:
        """
        [DescribeAggregateComplianceByConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules.paginate)
        """


class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregationAuthorizationsResponseTypeDef]:
        """
        [DescribeAggregationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations.paginate)
        """


class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
    """

    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeComplianceByConfigRuleResponseTypeDef]:
        """
        [DescribeComplianceByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule.paginate)
        """


class DescribeComplianceByResourcePaginator(Boto3Paginator):
    """
    [Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)
    """

    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeComplianceByResourceResponseTypeDef]:
        """
        [DescribeComplianceByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource.paginate)
        """


class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
    """

    def paginate(
        self, ConfigRuleNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRuleEvaluationStatusResponseTypeDef]:
        """
        [DescribeConfigRuleEvaluationStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus.paginate)
        """


class DescribeConfigRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)
    """

    def paginate(
        self, ConfigRuleNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRulesResponseTypeDef]:
        """
        [DescribeConfigRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules.paginate)
        """


class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
    """

    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeConfigurationAggregatorSourcesStatusResponseTypeDef]:
        """
        [DescribeConfigurationAggregatorSourcesStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus.paginate)
        """


class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)
    """

    def paginate(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeConfigurationAggregatorsResponseTypeDef]:
        """
        [DescribeConfigurationAggregators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators.paginate)
        """


class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePendingAggregationRequestsResponseTypeDef]:
        """
        [DescribePendingAggregationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests.paginate)
        """


class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
    """

    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List["ResourceKeyTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeRemediationExecutionStatusResponseTypeDef]:
        """
        [DescribeRemediationExecutionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus.paginate)
        """


class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)
    """

    def paginate(
        self,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeRetentionConfigurationsResponseTypeDef]:
        """
        [DescribeRetentionConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations.paginate)
        """


class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
    """

    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetAggregateComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [GetAggregateComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
    """

    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetComplianceDetailsByConfigRuleResponseTypeDef]:
        """
        [GetComplianceDetailsByConfigRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule.paginate)
        """


class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)
    """

    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetComplianceDetailsByResourceResponseTypeDef]:
        """
        [GetComplianceDetailsByResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource.paginate)
        """


class GetResourceConfigHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)
    """

    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: Literal["Reverse", "Forward"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetResourceConfigHistoryResponseTypeDef]:
        """
        [GetResourceConfigHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory.paginate)
        """


class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
    """

    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        Filters: ResourceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAggregateDiscoveredResourcesResponseTypeDef]:
        """
        [ListAggregateDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)
    """

    def paginate(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDiscoveredResourcesResponseTypeDef]:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources.paginate)
        """
