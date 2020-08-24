"""
Main interface for config service type definitions.

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef

    data: AccountAggregationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAggregationSourceTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "AggregateComplianceCountTypeDef",
    "AggregateEvaluationResultTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "ComplianceContributorCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "ConfigRuleTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationTypeDef",
    "ExecutionControlsTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GroupedResourceCountTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "PendingAggregationRequestTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceCountTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeTypeDef",
    "SourceDetailTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StaticValueTypeDef",
    "TagTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutEvaluationsResponseTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceFiltersTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "StatusDetailFiltersTypeDef",
)

_RequiredAccountAggregationSourceTypeDef = TypedDict(
    "_RequiredAccountAggregationSourceTypeDef", {"AccountIds": List[str]}
)
_OptionalAccountAggregationSourceTypeDef = TypedDict(
    "_OptionalAccountAggregationSourceTypeDef",
    {"AllAwsRegions": bool, "AwsRegions": List[str]},
    total=False,
)


class AccountAggregationSourceTypeDef(
    _RequiredAccountAggregationSourceTypeDef, _OptionalAccountAggregationSourceTypeDef
):
    pass


AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {"ConfigRuleName": str, "Compliance": "ComplianceTypeDef", "AccountId": str, "AwsRegion": str},
    total=False,
)

AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {"GroupName": str, "ComplianceSummary": "ComplianceSummaryTypeDef"},
    total=False,
)

AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

_RequiredAggregateResourceIdentifierTypeDef = TypedDict(
    "_RequiredAggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": Literal[
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
    },
)
_OptionalAggregateResourceIdentifierTypeDef = TypedDict(
    "_OptionalAggregateResourceIdentifierTypeDef", {"ResourceName": str}, total=False
)


class AggregateResourceIdentifierTypeDef(
    _RequiredAggregateResourceIdentifierTypeDef, _OptionalAggregateResourceIdentifierTypeDef
):
    pass


AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": str,
        "SourceType": Literal["ACCOUNT", "ORGANIZATION"],
        "AwsRegion": str,
        "LastUpdateStatus": Literal["FAILED", "SUCCEEDED", "OUTDATED"],
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)

AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "arn": str,
        "resourceType": Literal[
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
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {"ConfigRuleName": str, "Compliance": "ComplianceTypeDef"},
    total=False,
)

ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {"ResourceType": str, "ResourceId": str, "Compliance": "ComplianceTypeDef"},
    total=False,
)

ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef", {"CappedCount": int, "CapExceeded": bool}, total=False
)

ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {"ResourceType": str, "ComplianceSummary": "ComplianceSummaryTypeDef"},
    total=False,
)

ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": "ComplianceContributorCountTypeDef",
        "NonCompliantResourceCount": "ComplianceContributorCountTypeDef",
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ComplianceContributorCount": "ComplianceContributorCountTypeDef",
    },
    total=False,
)

ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)

ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastDeactivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)

_RequiredConfigRuleTypeDef = TypedDict("_RequiredConfigRuleTypeDef", {"Source": "SourceTypeDef"})
_OptionalConfigRuleTypeDef = TypedDict(
    "_OptionalConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": "ScopeTypeDef",
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ConfigRuleState": Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"],
        "CreatedBy": str,
    },
    total=False,
)


class ConfigRuleTypeDef(_RequiredConfigRuleTypeDef, _OptionalConfigRuleTypeDef):
    pass


ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    },
    total=False,
)

ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": Literal["Success", "Failure", "Not_Applicable"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List["AccountAggregationSourceTypeDef"],
        "OrganizationAggregationSource": "OrganizationAggregationSourceTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": Literal[
            "OK",
            "ResourceDiscovered",
            "ResourceNotRecorded",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
        ],
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": Literal[
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
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List["RelationshipTypeDef"],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": Literal["Pending", "Success", "Failure"],
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {"name": str, "roleARN": str, "recordingGroup": "RecordingGroupTypeDef"},
    total=False,
)

ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": Literal["COMPLIANT", "NON_COMPLIANT"],
    },
)

_RequiredConformancePackDetailTypeDef = TypedDict(
    "_RequiredConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
        "DeliveryS3Bucket": str,
    },
)
_OptionalConformancePackDetailTypeDef = TypedDict(
    "_OptionalConformancePackDetailTypeDef",
    {
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)


class ConformancePackDetailTypeDef(
    _RequiredConformancePackDetailTypeDef, _OptionalConformancePackDetailTypeDef
):
    pass


_RequiredConformancePackEvaluationResultTypeDef = TypedDict(
    "_RequiredConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
    },
)
_OptionalConformancePackEvaluationResultTypeDef = TypedDict(
    "_OptionalConformancePackEvaluationResultTypeDef", {"Annotation": str}, total=False
)


class ConformancePackEvaluationResultTypeDef(
    _RequiredConformancePackEvaluationResultTypeDef, _OptionalConformancePackEvaluationResultTypeDef
):
    pass


ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef", {"ParameterName": str, "ParameterValue": str}
)

ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {"ConfigRuleName": str, "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)

_RequiredConformancePackStatusDetailTypeDef = TypedDict(
    "_RequiredConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
        ],
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
    },
)
_OptionalConformancePackStatusDetailTypeDef = TypedDict(
    "_OptionalConformancePackStatusDetailTypeDef",
    {"ConformancePackStatusReason": str, "LastUpdateCompletedTime": datetime},
    total=False,
)


class ConformancePackStatusDetailTypeDef(
    _RequiredConformancePackStatusDetailTypeDef, _OptionalConformancePackStatusDetailTypeDef
):
    pass


DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configHistoryDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configStreamDeliveryInfo": "ConfigStreamDeliveryInfoTypeDef",
    },
    total=False,
)

DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": "ConfigSnapshotDeliveryPropertiesTypeDef",
    },
    total=False,
)

EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": "EvaluationResultQualifierTypeDef",
        "OrderingTimestamp": datetime,
    },
    total=False,
)

EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)

_RequiredEvaluationTypeDef = TypedDict(
    "_RequiredEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "OrderingTimestamp": datetime,
    },
)
_OptionalEvaluationTypeDef = TypedDict(
    "_OptionalEvaluationTypeDef", {"Annotation": str}, total=False
)


class EvaluationTypeDef(_RequiredEvaluationTypeDef, _OptionalEvaluationTypeDef):
    pass


ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef", {"SsmControls": "SsmControlsTypeDef"}, total=False
)

FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {"FailureMessage": str, "FailedItems": List["RemediationExceptionResourceKeyTypeDef"]},
    total=False,
)

FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {"FailureMessage": str, "FailedItems": List["RemediationConfigurationTypeDef"]},
    total=False,
)

FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {"FailureMessage": str, "FailedItems": List["RemediationExceptionTypeDef"]},
    total=False,
)

FieldInfoTypeDef = TypedDict("FieldInfoTypeDef", {"Name": str}, total=False)

GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef", {"GroupName": str, "ResourceCount": int}
)

_RequiredMemberAccountStatusTypeDef = TypedDict(
    "_RequiredMemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
)
_OptionalMemberAccountStatusTypeDef = TypedDict(
    "_OptionalMemberAccountStatusTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "LastUpdateTime": datetime},
    total=False,
)


class MemberAccountStatusTypeDef(
    _RequiredMemberAccountStatusTypeDef, _OptionalMemberAccountStatusTypeDef
):
    pass


_RequiredOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredOrganizationAggregationSourceTypeDef", {"RoleArn": str}
)
_OptionalOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalOrganizationAggregationSourceTypeDef",
    {"AwsRegions": List[str], "AllAwsRegions": bool},
    total=False,
)


class OrganizationAggregationSourceTypeDef(
    _RequiredOrganizationAggregationSourceTypeDef, _OptionalOrganizationAggregationSourceTypeDef
):
    pass


_RequiredOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
)
_OptionalOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleStatusTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "LastUpdateTime": datetime},
    total=False,
)


class OrganizationConfigRuleStatusTypeDef(
    _RequiredOrganizationConfigRuleStatusTypeDef, _OptionalOrganizationConfigRuleStatusTypeDef
):
    pass


_RequiredOrganizationConfigRuleTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleTypeDef",
    {"OrganizationConfigRuleName": str, "OrganizationConfigRuleArn": str},
)
_OptionalOrganizationConfigRuleTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleTypeDef",
    {
        "OrganizationManagedRuleMetadata": "OrganizationManagedRuleMetadataTypeDef",
        "OrganizationCustomRuleMetadata": "OrganizationCustomRuleMetadataTypeDef",
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)


class OrganizationConfigRuleTypeDef(
    _RequiredOrganizationConfigRuleTypeDef, _OptionalOrganizationConfigRuleTypeDef
):
    pass


_RequiredOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
)
_OptionalOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackDetailedStatusTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "LastUpdateTime": datetime},
    total=False,
)


class OrganizationConformancePackDetailedStatusTypeDef(
    _RequiredOrganizationConformancePackDetailedStatusTypeDef,
    _OptionalOrganizationConformancePackDetailedStatusTypeDef,
):
    pass


_RequiredOrganizationConformancePackStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
)
_OptionalOrganizationConformancePackStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackStatusTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "LastUpdateTime": datetime},
    total=False,
)


class OrganizationConformancePackStatusTypeDef(
    _RequiredOrganizationConformancePackStatusTypeDef,
    _OptionalOrganizationConformancePackStatusTypeDef,
):
    pass


_RequiredOrganizationConformancePackTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "DeliveryS3Bucket": str,
        "LastUpdateTime": datetime,
    },
)
_OptionalOrganizationConformancePackTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackTypeDef",
    {
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "ExcludedAccounts": List[str],
    },
    total=False,
)


class OrganizationConformancePackTypeDef(
    _RequiredOrganizationConformancePackTypeDef, _OptionalOrganizationConformancePackTypeDef
):
    pass


_RequiredOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[
            Literal[
                "ConfigurationItemChangeNotification",
                "OversizedConfigurationItemChangeNotification",
                "ScheduledNotification",
            ]
        ],
    },
)
_OptionalOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationCustomRuleMetadataTypeDef(
    _RequiredOrganizationCustomRuleMetadataTypeDef, _OptionalOrganizationCustomRuleMetadataTypeDef
):
    pass


_RequiredOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationManagedRuleMetadataTypeDef", {"RuleIdentifier": str}
)
_OptionalOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)


class OrganizationManagedRuleMetadataTypeDef(
    _RequiredOrganizationManagedRuleMetadataTypeDef, _OptionalOrganizationManagedRuleMetadataTypeDef
):
    pass


PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {"RequesterAccountId": str, "RequesterAwsRegion": str},
    total=False,
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef", {"SelectFields": List["FieldInfoTypeDef"]}, total=False
)

RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[
            Literal[
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
            ]
        ],
    },
    total=False,
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": Literal[
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
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)

_RequiredRemediationConfigurationTypeDef = TypedDict(
    "_RequiredRemediationConfigurationTypeDef",
    {"ConfigRuleName": str, "TargetType": Literal["SSM_DOCUMENT"], "TargetId": str},
)
_OptionalRemediationConfigurationTypeDef = TypedDict(
    "_OptionalRemediationConfigurationTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Dict[str, "RemediationParameterValueTypeDef"],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": "ExecutionControlsTypeDef",
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)


class RemediationConfigurationTypeDef(
    _RequiredRemediationConfigurationTypeDef, _OptionalRemediationConfigurationTypeDef
):
    pass


RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef", {"ResourceType": str, "ResourceId": str}, total=False
)

_RequiredRemediationExceptionTypeDef = TypedDict(
    "_RequiredRemediationExceptionTypeDef",
    {"ConfigRuleName": str, "ResourceType": str, "ResourceId": str},
)
_OptionalRemediationExceptionTypeDef = TypedDict(
    "_OptionalRemediationExceptionTypeDef",
    {"Message": str, "ExpirationTime": datetime},
    total=False,
)


class RemediationExceptionTypeDef(
    _RequiredRemediationExceptionTypeDef, _OptionalRemediationExceptionTypeDef
):
    pass


RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": "ResourceKeyTypeDef",
        "State": Literal["QUEUED", "IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StepDetails": List["RemediationExecutionStepTypeDef"],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": str,
        "State": Literal["SUCCEEDED", "PENDING", "FAILED"],
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {"ResourceValue": "ResourceValueTypeDef", "StaticValue": "StaticValueTypeDef"},
    total=False,
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": Literal[
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
        "count": int,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": Literal[
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
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)

ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": Literal[
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
        "resourceId": str,
    },
)

ResourceValueTypeDef = TypedDict("ResourceValueTypeDef", {"Value": Literal["RESOURCE_ID"]})

RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef", {"Name": str, "RetentionPeriodInDays": int}
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": Literal["aws.config"],
        "MessageType": Literal[
            "ConfigurationItemChangeNotification",
            "ConfigurationSnapshotDeliveryCompleted",
            "ScheduledNotification",
            "OversizedConfigurationItemChangeNotification",
        ],
        "MaximumExecutionFrequency": Literal[
            "One_Hour", "Three_Hours", "Six_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ],
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef", {"Owner": Literal["CUSTOM_LAMBDA", "AWS"], "SourceIdentifier": str}
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef", {"SourceDetails": List["SourceDetailTypeDef"]}, total=False
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {"ConcurrentExecutionRatePercentage": int, "ErrorPercentage": int},
    total=False,
)

StaticValueTypeDef = TypedDict("StaticValueTypeDef", {"Values": List[str]})

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

BatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "UnprocessedResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
    },
    total=False,
)

BatchGetResourceConfigResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "unprocessedResourceKeys": List["ResourceKeyTypeDef"],
    },
    total=False,
)

ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ],
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef", {"AccountId": str, "AwsRegion": str}, total=False
)

ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {"ConfigRuleNames": List[str], "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"]},
    total=False,
)

ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": Literal["COMPLIANT", "NON_COMPLIANT"],
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)

DeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List["FailedDeleteRemediationExceptionsBatchTypeDef"]},
    total=False,
)

DeliverConfigSnapshotResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseTypeDef", {"configSnapshotId": str}, total=False
)

DescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List["AggregateComplianceByConfigRuleTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseTypeDef",
    {"AggregationAuthorizations": List["AggregationAuthorizationTypeDef"], "NextToken": str},
    total=False,
)

DescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseTypeDef",
    {"ComplianceByConfigRules": List["ComplianceByConfigRuleTypeDef"], "NextToken": str},
    total=False,
)

DescribeComplianceByResourceResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseTypeDef",
    {"ComplianceByResources": List["ComplianceByResourceTypeDef"], "NextToken": str},
    total=False,
)

DescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    {"ConfigRulesEvaluationStatus": List["ConfigRuleEvaluationStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeConfigRulesResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseTypeDef",
    {"ConfigRules": List["ConfigRuleTypeDef"], "NextToken": str},
    total=False,
)

DescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {"AggregatedSourceStatusList": List["AggregatedSourceStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseTypeDef",
    {"ConfigurationAggregators": List["ConfigurationAggregatorTypeDef"], "NextToken": str},
    total=False,
)

DescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    {"ConfigurationRecordersStatus": List["ConfigurationRecorderStatusTypeDef"]},
    total=False,
)

DescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseTypeDef",
    {"ConfigurationRecorders": List["ConfigurationRecorderTypeDef"]},
    total=False,
)

_RequiredDescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "_RequiredDescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List["ConformancePackRuleComplianceTypeDef"],
    },
)
_OptionalDescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "_OptionalDescribeConformancePackComplianceResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeConformancePackComplianceResponseTypeDef(
    _RequiredDescribeConformancePackComplianceResponseTypeDef,
    _OptionalDescribeConformancePackComplianceResponseTypeDef,
):
    pass


DescribeConformancePackStatusResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseTypeDef",
    {"ConformancePackStatusDetails": List["ConformancePackStatusDetailTypeDef"], "NextToken": str},
    total=False,
)

DescribeConformancePacksResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseTypeDef",
    {"ConformancePackDetails": List["ConformancePackDetailTypeDef"], "NextToken": str},
    total=False,
)

DescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseTypeDef",
    {"DeliveryChannelsStatus": List["DeliveryChannelStatusTypeDef"]},
    total=False,
)

DescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseTypeDef",
    {"DeliveryChannels": List["DeliveryChannelTypeDef"]},
    total=False,
)

DescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List["OrganizationConfigRuleStatusTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseTypeDef",
    {"OrganizationConfigRules": List["OrganizationConfigRuleTypeDef"], "NextToken": str},
    total=False,
)

DescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List["OrganizationConformancePackStatusTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseTypeDef",
    {"OrganizationConformancePacks": List["OrganizationConformancePackTypeDef"], "NextToken": str},
    total=False,
)

DescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseTypeDef",
    {"PendingAggregationRequests": List["PendingAggregationRequestTypeDef"], "NextToken": str},
    total=False,
)

DescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseTypeDef",
    {"RemediationConfigurations": List["RemediationConfigurationTypeDef"]},
    total=False,
)

DescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseTypeDef",
    {"RemediationExceptions": List["RemediationExceptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseTypeDef",
    {"RemediationExecutionStatuses": List["RemediationExecutionStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseTypeDef",
    {"RetentionConfigurations": List["RetentionConfigurationTypeDef"], "NextToken": str},
    total=False,
)

GetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {"AggregateEvaluationResults": List["AggregateEvaluationResultTypeDef"], "NextToken": str},
    total=False,
)

GetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List["AggregateComplianceCountTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredGetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_RequiredGetAggregateDiscoveredResourceCountsResponseTypeDef",
    {"TotalDiscoveredResources": int},
)
_OptionalGetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "_OptionalGetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "GroupByKey": str,
        "GroupedResourceCounts": List["GroupedResourceCountTypeDef"],
        "NextToken": str,
    },
    total=False,
)


class GetAggregateDiscoveredResourceCountsResponseTypeDef(
    _RequiredGetAggregateDiscoveredResourceCountsResponseTypeDef,
    _OptionalGetAggregateDiscoveredResourceCountsResponseTypeDef,
):
    pass


GetAggregateResourceConfigResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseTypeDef",
    {"ConfigurationItem": "ConfigurationItemTypeDef"},
    total=False,
)

GetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    {"EvaluationResults": List["EvaluationResultTypeDef"], "NextToken": str},
    total=False,
)

GetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseTypeDef",
    {"EvaluationResults": List["EvaluationResultTypeDef"], "NextToken": str},
    total=False,
)

GetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    {"ComplianceSummary": "ComplianceSummaryTypeDef"},
    total=False,
)

GetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    {"ComplianceSummariesByResourceType": List["ComplianceSummaryByResourceTypeTypeDef"]},
    total=False,
)

_RequiredGetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceDetailsResponseTypeDef", {"ConformancePackName": str}
)
_OptionalGetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackRuleEvaluationResults": List["ConformancePackEvaluationResultTypeDef"],
        "NextToken": str,
    },
    total=False,
)


class GetConformancePackComplianceDetailsResponseTypeDef(
    _RequiredGetConformancePackComplianceDetailsResponseTypeDef,
    _OptionalGetConformancePackComplianceDetailsResponseTypeDef,
):
    pass


GetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List["ConformancePackComplianceSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List["ResourceCountTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {"OrganizationConfigRuleDetailedStatus": List["MemberAccountStatusTypeDef"], "NextToken": str},
    total=False,
)

GetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            "OrganizationConformancePackDetailedStatusTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

GetResourceConfigHistoryResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseTypeDef",
    {"configurationItems": List["ConfigurationItemTypeDef"], "nextToken": str},
    total=False,
)

ListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    {"ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"], "NextToken": str},
    total=False,
)

ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {"resourceIdentifiers": List["ResourceIdentifierTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "Status": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutAggregationAuthorizationResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseTypeDef",
    {"AggregationAuthorization": "AggregationAuthorizationTypeDef"},
    total=False,
)

PutConfigurationAggregatorResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseTypeDef",
    {"ConfigurationAggregator": "ConfigurationAggregatorTypeDef"},
    total=False,
)

PutConformancePackResponseTypeDef = TypedDict(
    "PutConformancePackResponseTypeDef", {"ConformancePackArn": str}, total=False
)

PutEvaluationsResponseTypeDef = TypedDict(
    "PutEvaluationsResponseTypeDef", {"FailedEvaluations": List["EvaluationTypeDef"]}, total=False
)

PutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseTypeDef", {"OrganizationConfigRuleArn": str}, total=False
)

PutOrganizationConformancePackResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseTypeDef",
    {"OrganizationConformancePackArn": str},
    total=False,
)

PutRemediationConfigurationsResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseTypeDef",
    {"FailedBatches": List["FailedRemediationBatchTypeDef"]},
    total=False,
)

PutRemediationExceptionsResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseTypeDef",
    {"FailedBatches": List["FailedRemediationExceptionBatchTypeDef"]},
    total=False,
)

PutRetentionConfigurationResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseTypeDef",
    {"RetentionConfiguration": "RetentionConfigurationTypeDef"},
    total=False,
)

ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": Literal[
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
        "AccountId": str,
        "Region": str,
    },
    total=False,
)

ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {"AccountId": str, "ResourceId": str, "ResourceName": str, "Region": str},
    total=False,
)

SelectAggregateResourceConfigResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseTypeDef",
    {"Results": List[str], "QueryInfo": "QueryInfoTypeDef", "NextToken": str},
    total=False,
)

SelectResourceConfigResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseTypeDef",
    {"Results": List[str], "QueryInfo": "QueryInfoTypeDef", "NextToken": str},
    total=False,
)

StartRemediationExecutionResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseTypeDef",
    {"FailureMessage": str, "FailedItems": List["ResourceKeyTypeDef"]},
    total=False,
)

StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": str,
        "MemberAccountRuleStatus": Literal[
            "CREATE_SUCCESSFUL",
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "DELETE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
        ],
    },
    total=False,
)
