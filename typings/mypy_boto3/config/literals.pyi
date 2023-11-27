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
    "EvaluationModeType",
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
    "ListResourceEvaluationsPaginatorName",
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
    "RecordingFrequencyType",
    "RecordingStrategyTypeType",
    "RemediationExecutionStateType",
    "RemediationExecutionStepStateType",
    "RemediationTargetTypeType",
    "ResourceConfigurationSchemaTypeType",
    "ResourceCountGroupKeyType",
    "ResourceEvaluationStatusType",
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
EvaluationModeType = Literal["DETECTIVE", "PROACTIVE"]
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
ListResourceEvaluationsPaginatorName = Literal["list_resource_evaluations"]
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
RecordingFrequencyType = Literal["CONTINUOUS", "DAILY"]
RecordingStrategyTypeType = Literal[
    "ALL_SUPPORTED_RESOURCE_TYPES", "EXCLUSION_BY_RESOURCE_TYPES", "INCLUSION_BY_RESOURCE_TYPES"
]
RemediationExecutionStateType = Literal["FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
RemediationExecutionStepStateType = Literal["FAILED", "PENDING", "SUCCEEDED"]
RemediationTargetTypeType = Literal["SSM_DOCUMENT"]
ResourceConfigurationSchemaTypeType = Literal["CFN_RESOURCE_SCHEMA"]
ResourceCountGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION", "RESOURCE_TYPE"]
ResourceEvaluationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ResourceTypeType = Literal[
    "AWS::ACM::Certificate",
    "AWS::ACMPCA::CertificateAuthority",
    "AWS::ACMPCA::CertificateAuthorityActivation",
    "AWS::APS::RuleGroupsNamespace",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::AmazonMQ::Broker",
    "AWS::Amplify::App",
    "AWS::Amplify::Branch",
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::ApiGatewayV2::Api",
    "AWS::ApiGatewayV2::Stage",
    "AWS::AppConfig::Application",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::AppConfig::Environment",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::AppFlow::Flow",
    "AWS::AppIntegrations::EventIntegration",
    "AWS::AppMesh::GatewayRoute",
    "AWS::AppMesh::Mesh",
    "AWS::AppMesh::Route",
    "AWS::AppMesh::VirtualGateway",
    "AWS::AppMesh::VirtualNode",
    "AWS::AppMesh::VirtualRouter",
    "AWS::AppMesh::VirtualService",
    "AWS::AppRunner::Service",
    "AWS::AppRunner::VpcConnector",
    "AWS::AppStream::Application",
    "AWS::AppStream::DirectoryConfig",
    "AWS::AppStream::Stack",
    "AWS::AppSync::GraphQLApi",
    "AWS::Athena::DataCatalog",
    "AWS::Athena::PreparedStatement",
    "AWS::Athena::WorkGroup",
    "AWS::AuditManager::Assessment",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::AutoScaling::WarmPool",
    "AWS::Backup::BackupPlan",
    "AWS::Backup::BackupSelection",
    "AWS::Backup::BackupVault",
    "AWS::Backup::RecoveryPoint",
    "AWS::Backup::ReportPlan",
    "AWS::Batch::ComputeEnvironment",
    "AWS::Batch::JobQueue",
    "AWS::Batch::SchedulingPolicy",
    "AWS::Budgets::BudgetsAction",
    "AWS::Cassandra::Keyspace",
    "AWS::Cloud9::EnvironmentEC2",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::CloudWatch::MetricStream",
    "AWS::CodeArtifact::Repository",
    "AWS::CodeBuild::Project",
    "AWS::CodeBuild::ReportGroup",
    "AWS::CodeDeploy::Application",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CodeGuruProfiler::ProfilingGroup",
    "AWS::CodeGuruReviewer::RepositoryAssociation",
    "AWS::CodePipeline::Pipeline",
    "AWS::Config::ConformancePackCompliance",
    "AWS::Config::ResourceCompliance",
    "AWS::Connect::Instance",
    "AWS::Connect::PhoneNumber",
    "AWS::Connect::QuickConnect",
    "AWS::CustomerProfiles::Domain",
    "AWS::CustomerProfiles::ObjectType",
    "AWS::DMS::Certificate",
    "AWS::DMS::Endpoint",
    "AWS::DMS::EventSubscription",
    "AWS::DMS::ReplicationSubnetGroup",
    "AWS::DataSync::LocationEFS",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::DataSync::LocationFSxWindows",
    "AWS::DataSync::LocationHDFS",
    "AWS::DataSync::LocationNFS",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::DataSync::LocationS3",
    "AWS::DataSync::LocationSMB",
    "AWS::DataSync::Task",
    "AWS::Detective::Graph",
    "AWS::DeviceFarm::InstanceProfile",
    "AWS::DeviceFarm::Project",
    "AWS::DeviceFarm::TestGridProject",
    "AWS::DynamoDB::Table",
    "AWS::EC2::CapacityReservation",
    "AWS::EC2::CarrierGateway",
    "AWS::EC2::ClientVpnEndpoint",
    "AWS::EC2::CustomerGateway",
    "AWS::EC2::DHCPOptions",
    "AWS::EC2::EC2Fleet",
    "AWS::EC2::EIP",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::FlowLog",
    "AWS::EC2::Host",
    "AWS::EC2::IPAM",
    "AWS::EC2::IPAMPool",
    "AWS::EC2::IPAMScope",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::LaunchTemplate",
    "AWS::EC2::NatGateway",
    "AWS::EC2::NetworkAcl",
    "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
    "AWS::EC2::NetworkInsightsPath",
    "AWS::EC2::NetworkInterface",
    "AWS::EC2::PrefixList",
    "AWS::EC2::RegisteredHAInstance",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::SpotFleet",
    "AWS::EC2::Subnet",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::EC2::TrafficMirrorFilter",
    "AWS::EC2::TrafficMirrorSession",
    "AWS::EC2::TrafficMirrorTarget",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::EC2::TransitGatewayConnect",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::EC2::VPC",
    "AWS::EC2::VPCEndpoint",
    "AWS::EC2::VPCEndpointService",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNGateway",
    "AWS::EC2::Volume",
    "AWS::ECR::PublicRepository",
    "AWS::ECR::PullThroughCacheRule",
    "AWS::ECR::RegistryPolicy",
    "AWS::ECR::Repository",
    "AWS::ECS::CapacityProvider",
    "AWS::ECS::Cluster",
    "AWS::ECS::Service",
    "AWS::ECS::TaskDefinition",
    "AWS::ECS::TaskSet",
    "AWS::EFS::AccessPoint",
    "AWS::EFS::FileSystem",
    "AWS::EKS::Addon",
    "AWS::EKS::Cluster",
    "AWS::EKS::FargateProfile",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::EMR::SecurityConfiguration",
    "AWS::ElasticBeanstalk::Application",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::Elasticsearch::Domain",
    "AWS::EventSchemas::Discoverer",
    "AWS::EventSchemas::Registry",
    "AWS::EventSchemas::RegistryPolicy",
    "AWS::EventSchemas::Schema",
    "AWS::Events::ApiDestination",
    "AWS::Events::Archive",
    "AWS::Events::Connection",
    "AWS::Events::Endpoint",
    "AWS::Events::EventBus",
    "AWS::Events::Rule",
    "AWS::Evidently::Launch",
    "AWS::Evidently::Project",
    "AWS::FIS::ExperimentTemplate",
    "AWS::Forecast::Dataset",
    "AWS::Forecast::DatasetGroup",
    "AWS::FraudDetector::EntityType",
    "AWS::FraudDetector::Label",
    "AWS::FraudDetector::Outcome",
    "AWS::FraudDetector::Variable",
    "AWS::GlobalAccelerator::Accelerator",
    "AWS::GlobalAccelerator::EndpointGroup",
    "AWS::GlobalAccelerator::Listener",
    "AWS::Glue::Classifier",
    "AWS::Glue::Job",
    "AWS::Glue::MLTransform",
    "AWS::GreengrassV2::ComponentVersion",
    "AWS::GroundStation::Config",
    "AWS::GroundStation::MissionProfile",
    "AWS::GuardDuty::Detector",
    "AWS::GuardDuty::Filter",
    "AWS::GuardDuty::IPSet",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::HealthLake::FHIRDatastore",
    "AWS::IAM::Group",
    "AWS::IAM::InstanceProfile",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::SAMLProvider",
    "AWS::IAM::ServerCertificate",
    "AWS::IAM::User",
    "AWS::IVS::Channel",
    "AWS::IVS::PlaybackKeyPair",
    "AWS::IVS::RecordingConfiguration",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::InspectorV2::Filter",
    "AWS::IoT::AccountAuditConfiguration",
    "AWS::IoT::Authorizer",
    "AWS::IoT::CACertificate",
    "AWS::IoT::CustomMetric",
    "AWS::IoT::Dimension",
    "AWS::IoT::FleetMetric",
    "AWS::IoT::JobTemplate",
    "AWS::IoT::MitigationAction",
    "AWS::IoT::Policy",
    "AWS::IoT::ProvisioningTemplate",
    "AWS::IoT::RoleAlias",
    "AWS::IoT::ScheduledAudit",
    "AWS::IoT::SecurityProfile",
    "AWS::IoTAnalytics::Channel",
    "AWS::IoTAnalytics::Dataset",
    "AWS::IoTAnalytics::Datastore",
    "AWS::IoTAnalytics::Pipeline",
    "AWS::IoTEvents::AlarmModel",
    "AWS::IoTEvents::DetectorModel",
    "AWS::IoTEvents::Input",
    "AWS::IoTSiteWise::AssetModel",
    "AWS::IoTSiteWise::Dashboard",
    "AWS::IoTSiteWise::Gateway",
    "AWS::IoTSiteWise::Portal",
    "AWS::IoTSiteWise::Project",
    "AWS::IoTTwinMaker::ComponentType",
    "AWS::IoTTwinMaker::Entity",
    "AWS::IoTTwinMaker::Scene",
    "AWS::IoTTwinMaker::SyncJob",
    "AWS::IoTTwinMaker::Workspace",
    "AWS::IoTWireless::FuotaTask",
    "AWS::IoTWireless::MulticastGroup",
    "AWS::IoTWireless::ServiceProfile",
    "AWS::KMS::Key",
    "AWS::KafkaConnect::Connector",
    "AWS::Kendra::Index",
    "AWS::Kinesis::Stream",
    "AWS::Kinesis::StreamConsumer",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::KinesisVideo::SignalingChannel",
    "AWS::KinesisVideo::Stream",
    "AWS::Lambda::CodeSigningConfig",
    "AWS::Lambda::Function",
    "AWS::Lex::Bot",
    "AWS::Lex::BotAlias",
    "AWS::Lightsail::Bucket",
    "AWS::Lightsail::Certificate",
    "AWS::Lightsail::Disk",
    "AWS::Lightsail::StaticIp",
    "AWS::Logs::Destination",
    "AWS::LookoutMetrics::Alert",
    "AWS::LookoutVision::Project",
    "AWS::MSK::BatchScramSecret",
    "AWS::MSK::Cluster",
    "AWS::MSK::Configuration",
    "AWS::MediaConnect::FlowEntitlement",
    "AWS::MediaConnect::FlowSource",
    "AWS::MediaConnect::FlowVpcInterface",
    "AWS::MediaPackage::PackagingConfiguration",
    "AWS::MediaPackage::PackagingGroup",
    "AWS::MediaTailor::PlaybackConfiguration",
    "AWS::NetworkFirewall::Firewall",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::NetworkManager::ConnectPeer",
    "AWS::NetworkManager::CustomerGatewayAssociation",
    "AWS::NetworkManager::Device",
    "AWS::NetworkManager::GlobalNetwork",
    "AWS::NetworkManager::Link",
    "AWS::NetworkManager::LinkAssociation",
    "AWS::NetworkManager::Site",
    "AWS::NetworkManager::TransitGatewayRegistration",
    "AWS::OpenSearch::Domain",
    "AWS::Panorama::Package",
    "AWS::Personalize::Dataset",
    "AWS::Personalize::DatasetGroup",
    "AWS::Personalize::Schema",
    "AWS::Personalize::Solution",
    "AWS::Pinpoint::App",
    "AWS::Pinpoint::ApplicationSettings",
    "AWS::Pinpoint::Campaign",
    "AWS::Pinpoint::EmailChannel",
    "AWS::Pinpoint::EmailTemplate",
    "AWS::Pinpoint::EventStream",
    "AWS::Pinpoint::InAppTemplate",
    "AWS::Pinpoint::Segment",
    "AWS::QLDB::Ledger",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::RDS::GlobalCluster",
    "AWS::RUM::AppMonitor",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSnapshot",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::EventSubscription",
    "AWS::Redshift::ScheduledAction",
    "AWS::ResilienceHub::App",
    "AWS::ResilienceHub::ResiliencyPolicy",
    "AWS::ResourceExplorer2::Index",
    "AWS::RoboMaker::RobotApplication",
    "AWS::RoboMaker::RobotApplicationVersion",
    "AWS::RoboMaker::SimulationApplication",
    "AWS::Route53::HostedZone",
    "AWS::Route53RecoveryControl::Cluster",
    "AWS::Route53RecoveryControl::ControlPanel",
    "AWS::Route53RecoveryControl::RoutingControl",
    "AWS::Route53RecoveryControl::SafetyRule",
    "AWS::Route53RecoveryReadiness::Cell",
    "AWS::Route53RecoveryReadiness::ReadinessCheck",
    "AWS::Route53RecoveryReadiness::RecoveryGroup",
    "AWS::Route53RecoveryReadiness::ResourceSet",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::S3::AccessPoint",
    "AWS::S3::AccountPublicAccessBlock",
    "AWS::S3::Bucket",
    "AWS::S3::MultiRegionAccessPoint",
    "AWS::S3::StorageLens",
    "AWS::SES::ConfigurationSet",
    "AWS::SES::ContactList",
    "AWS::SES::ReceiptFilter",
    "AWS::SES::ReceiptRuleSet",
    "AWS::SES::Template",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SSM::AssociationCompliance",
    "AWS::SSM::FileData",
    "AWS::SSM::ManagedInstanceInventory",
    "AWS::SSM::PatchCompliance",
    "AWS::SageMaker::AppImageConfig",
    "AWS::SageMaker::CodeRepository",
    "AWS::SageMaker::Domain",
    "AWS::SageMaker::FeatureGroup",
    "AWS::SageMaker::Image",
    "AWS::SageMaker::Model",
    "AWS::SageMaker::NotebookInstanceLifecycleConfig",
    "AWS::SageMaker::Workteam",
    "AWS::SecretsManager::Secret",
    "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
    "AWS::ServiceCatalog::Portfolio",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::ServiceDiscovery::Instance",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::ServiceDiscovery::Service",
    "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection",
    "AWS::Signer::SigningProfile",
    "AWS::StepFunctions::Activity",
    "AWS::StepFunctions::StateMachine",
    "AWS::Transfer::Agreement",
    "AWS::Transfer::Certificate",
    "AWS::Transfer::Connector",
    "AWS::Transfer::Workflow",
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
