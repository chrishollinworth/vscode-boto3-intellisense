"""
Type annotations for config service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/literals.html)

Usage::

    ```python
    from mypy_boto3_config.literals import AggregateConformancePackComplianceSummaryGroupKeyType

    data: AggregateConformancePackComplianceSummaryGroupKeyType = "ACCOUNT_ID"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggregateConformancePackComplianceSummaryGroupKeyType",
    "AggregatedSourceStatusTypeType",
    "AggregatedSourceTypeType",
    "ChronologicalOrderType",
    "ComplianceTypeType",
    "ConfigRuleComplianceSummaryGroupKeyType",
    "ConfigRuleStateType",
    "ConfigurationItemStatusType",
    "ConformancePackComplianceTypeType",
    "ConformancePackStateType",
    "DeliveryStatusType",
    "DescribeAggregateComplianceByConfigRulesPaginatorName",
    "DescribeAggregateComplianceByConformancePacksPaginatorName",
    "DescribeAggregationAuthorizationsPaginatorName",
    "DescribeComplianceByConfigRulePaginatorName",
    "DescribeComplianceByResourcePaginatorName",
    "DescribeConfigRuleEvaluationStatusPaginatorName",
    "DescribeConfigRulesPaginatorName",
    "DescribeConfigurationAggregatorSourcesStatusPaginatorName",
    "DescribeConfigurationAggregatorsPaginatorName",
    "DescribeConformancePackStatusPaginatorName",
    "DescribeConformancePacksPaginatorName",
    "DescribeOrganizationConfigRuleStatusesPaginatorName",
    "DescribeOrganizationConfigRulesPaginatorName",
    "DescribeOrganizationConformancePackStatusesPaginatorName",
    "DescribeOrganizationConformancePacksPaginatorName",
    "DescribePendingAggregationRequestsPaginatorName",
    "DescribeRemediationExecutionStatusPaginatorName",
    "DescribeRetentionConfigurationsPaginatorName",
    "EventSourceType",
    "GetAggregateComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByResourcePaginatorName",
    "GetConformancePackComplianceSummaryPaginatorName",
    "GetOrganizationConfigRuleDetailedStatusPaginatorName",
    "GetOrganizationConformancePackDetailedStatusPaginatorName",
    "GetResourceConfigHistoryPaginatorName",
    "ListAggregateDiscoveredResourcesPaginatorName",
    "ListDiscoveredResourcesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MaximumExecutionFrequencyType",
    "MemberAccountRuleStatusType",
    "MessageTypeType",
    "OrganizationConfigRuleTriggerTypeNoSNType",
    "OrganizationConfigRuleTriggerTypeType",
    "OrganizationResourceDetailedStatusType",
    "OrganizationResourceStatusType",
    "OrganizationRuleStatusType",
    "OwnerType",
    "RecorderStatusType",
    "RemediationExecutionStateType",
    "RemediationExecutionStepStateType",
    "RemediationTargetTypeType",
    "ResourceCountGroupKeyType",
    "ResourceTypeType",
    "ResourceValueTypeType",
    "SelectAggregateResourceConfigPaginatorName",
    "SelectResourceConfigPaginatorName",
    "SortByType",
    "SortOrderType",
)

AggregateConformancePackComplianceSummaryGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION"]
AggregatedSourceStatusTypeType = Literal["FAILED", "OUTDATED", "SUCCEEDED"]
AggregatedSourceTypeType = Literal["ACCOUNT", "ORGANIZATION"]
ChronologicalOrderType = Literal["Forward", "Reverse"]
ComplianceTypeType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
ConfigRuleComplianceSummaryGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION"]
ConfigRuleStateType = Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"]
ConfigurationItemStatusType = Literal[
    "OK",
    "ResourceDeleted",
    "ResourceDeletedNotRecorded",
    "ResourceDiscovered",
    "ResourceNotRecorded",
]
ConformancePackComplianceTypeType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
ConformancePackStateType = Literal[
    "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
DeliveryStatusType = Literal["Failure", "Not_Applicable", "Success"]
DescribeAggregateComplianceByConfigRulesPaginatorName = Literal[
    "describe_aggregate_compliance_by_config_rules"
]
DescribeAggregateComplianceByConformancePacksPaginatorName = Literal[
    "describe_aggregate_compliance_by_conformance_packs"
]
DescribeAggregationAuthorizationsPaginatorName = Literal["describe_aggregation_authorizations"]
DescribeComplianceByConfigRulePaginatorName = Literal["describe_compliance_by_config_rule"]
DescribeComplianceByResourcePaginatorName = Literal["describe_compliance_by_resource"]
DescribeConfigRuleEvaluationStatusPaginatorName = Literal["describe_config_rule_evaluation_status"]
DescribeConfigRulesPaginatorName = Literal["describe_config_rules"]
DescribeConfigurationAggregatorSourcesStatusPaginatorName = Literal[
    "describe_configuration_aggregator_sources_status"
]
DescribeConfigurationAggregatorsPaginatorName = Literal["describe_configuration_aggregators"]
DescribeConformancePackStatusPaginatorName = Literal["describe_conformance_pack_status"]
DescribeConformancePacksPaginatorName = Literal["describe_conformance_packs"]
DescribeOrganizationConfigRuleStatusesPaginatorName = Literal[
    "describe_organization_config_rule_statuses"
]
DescribeOrganizationConfigRulesPaginatorName = Literal["describe_organization_config_rules"]
DescribeOrganizationConformancePackStatusesPaginatorName = Literal[
    "describe_organization_conformance_pack_statuses"
]
DescribeOrganizationConformancePacksPaginatorName = Literal[
    "describe_organization_conformance_packs"
]
DescribePendingAggregationRequestsPaginatorName = Literal["describe_pending_aggregation_requests"]
DescribeRemediationExecutionStatusPaginatorName = Literal["describe_remediation_execution_status"]
DescribeRetentionConfigurationsPaginatorName = Literal["describe_retention_configurations"]
EventSourceType = Literal["aws.config"]
GetAggregateComplianceDetailsByConfigRulePaginatorName = Literal[
    "get_aggregate_compliance_details_by_config_rule"
]
GetComplianceDetailsByConfigRulePaginatorName = Literal["get_compliance_details_by_config_rule"]
GetComplianceDetailsByResourcePaginatorName = Literal["get_compliance_details_by_resource"]
GetConformancePackComplianceSummaryPaginatorName = Literal[
    "get_conformance_pack_compliance_summary"
]
GetOrganizationConfigRuleDetailedStatusPaginatorName = Literal[
    "get_organization_config_rule_detailed_status"
]
GetOrganizationConformancePackDetailedStatusPaginatorName = Literal[
    "get_organization_conformance_pack_detailed_status"
]
GetResourceConfigHistoryPaginatorName = Literal["get_resource_config_history"]
ListAggregateDiscoveredResourcesPaginatorName = Literal["list_aggregate_discovered_resources"]
ListDiscoveredResourcesPaginatorName = Literal["list_discovered_resources"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MaximumExecutionFrequencyType = Literal[
    "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
]
MemberAccountRuleStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
MessageTypeType = Literal[
    "ConfigurationItemChangeNotification",
    "ConfigurationSnapshotDeliveryCompleted",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationConfigRuleTriggerTypeNoSNType = Literal[
    "ConfigurationItemChangeNotification", "OversizedConfigurationItemChangeNotification"
]
OrganizationConfigRuleTriggerTypeType = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationResourceDetailedStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationResourceStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationRuleStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OwnerType = Literal["AWS", "CUSTOM_LAMBDA", "CUSTOM_POLICY"]
RecorderStatusType = Literal["Failure", "Pending", "Success"]
RemediationExecutionStateType = Literal["FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
RemediationExecutionStepStateType = Literal["FAILED", "PENDING", "SUCCEEDED"]
RemediationTargetTypeType = Literal["SSM_DOCUMENT"]
ResourceCountGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION", "RESOURCE_TYPE"]
ResourceTypeType = Literal[
    "AWS::ACM::Certificate",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::ApiGatewayV2::Api",
    "AWS::ApiGatewayV2::Stage",
    "AWS::AppConfig::Application",
    "AWS::AppSync::GraphQLApi",
    "AWS::Athena::DataCatalog",
    "AWS::Athena::WorkGroup",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::Backup::BackupPlan",
    "AWS::Backup::BackupSelection",
    "AWS::Backup::BackupVault",
    "AWS::Backup::RecoveryPoint",
    "AWS::Batch::ComputeEnvironment",
    "AWS::Batch::JobQueue",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::CodeBuild::Project",
    "AWS::CodeDeploy::Application",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CodePipeline::Pipeline",
    "AWS::Config::ConformancePackCompliance",
    "AWS::Config::ResourceCompliance",
    "AWS::DMS::Certificate",
    "AWS::DMS::EventSubscription",
    "AWS::DMS::ReplicationSubnetGroup",
    "AWS::DataSync::LocationEFS",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::DataSync::LocationNFS",
    "AWS::DataSync::LocationS3",
    "AWS::DataSync::LocationSMB",
    "AWS::DataSync::Task",
    "AWS::Detective::Graph",
    "AWS::DynamoDB::Table",
    "AWS::EC2::CustomerGateway",
    "AWS::EC2::EIP",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::FlowLog",
    "AWS::EC2::Host",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::LaunchTemplate",
    "AWS::EC2::NatGateway",
    "AWS::EC2::NetworkAcl",
    "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
    "AWS::EC2::NetworkInterface",
    "AWS::EC2::RegisteredHAInstance",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::Subnet",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::EC2::VPC",
    "AWS::EC2::VPCEndpoint",
    "AWS::EC2::VPCEndpointService",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNGateway",
    "AWS::EC2::Volume",
    "AWS::ECR::PublicRepository",
    "AWS::ECR::Repository",
    "AWS::ECS::Cluster",
    "AWS::ECS::Service",
    "AWS::ECS::TaskDefinition",
    "AWS::EFS::AccessPoint",
    "AWS::EFS::FileSystem",
    "AWS::EKS::Cluster",
    "AWS::EKS::FargateProfile",
    "AWS::EMR::SecurityConfiguration",
    "AWS::ElasticBeanstalk::Application",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::Elasticsearch::Domain",
    "AWS::GlobalAccelerator::Accelerator",
    "AWS::GlobalAccelerator::EndpointGroup",
    "AWS::GlobalAccelerator::Listener",
    "AWS::Glue::Job",
    "AWS::GuardDuty::Detector",
    "AWS::GuardDuty::IPSet",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::IAM::Group",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::User",
    "AWS::KMS::Key",
    "AWS::Kinesis::Stream",
    "AWS::Kinesis::StreamConsumer",
    "AWS::Lambda::Function",
    "AWS::MSK::Cluster",
    "AWS::NetworkFirewall::Firewall",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::OpenSearch::Domain",
    "AWS::QLDB::Ledger",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSnapshot",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::EventSubscription",
    "AWS::Route53::HostedZone",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::S3::AccountPublicAccessBlock",
    "AWS::S3::Bucket",
    "AWS::SES::ConfigurationSet",
    "AWS::SES::ContactList",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SSM::AssociationCompliance",
    "AWS::SSM::FileData",
    "AWS::SSM::ManagedInstanceInventory",
    "AWS::SSM::PatchCompliance",
    "AWS::SageMaker::CodeRepository",
    "AWS::SageMaker::Model",
    "AWS::SageMaker::NotebookInstanceLifecycleConfig",
    "AWS::SageMaker::Workteam",
    "AWS::SecretsManager::Secret",
    "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
    "AWS::ServiceCatalog::Portfolio",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::ServiceDiscovery::Service",
    "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection",
    "AWS::StepFunctions::Activity",
    "AWS::StepFunctions::StateMachine",
    "AWS::WAF::RateBasedRule",
    "AWS::WAF::Rule",
    "AWS::WAF::RuleGroup",
    "AWS::WAF::WebACL",
    "AWS::WAFRegional::RateBasedRule",
    "AWS::WAFRegional::Rule",
    "AWS::WAFRegional::RuleGroup",
    "AWS::WAFRegional::WebACL",
    "AWS::WAFv2::IPSet",
    "AWS::WAFv2::ManagedRuleSet",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::WAFv2::RuleGroup",
    "AWS::WAFv2::WebACL",
    "AWS::WorkSpaces::ConnectionAlias",
    "AWS::WorkSpaces::Workspace",
    "AWS::XRay::EncryptionConfig",
]
ResourceValueTypeType = Literal["RESOURCE_ID"]
SelectAggregateResourceConfigPaginatorName = Literal["select_aggregate_resource_config"]
SelectResourceConfigPaginatorName = Literal["select_resource_config"]
SortByType = Literal["SCORE"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
