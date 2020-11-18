"""
Main interface for securityhub service type definitions.

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import ActionTargetTypeDef

    data: ActionTargetTypeDef = {...}
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
    "ActionTargetTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "AwsSecurityFindingTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "CidrBlockAssociationTypeDef",
    "ComplianceTypeDef",
    "ContainerDetailsTypeDef",
    "CvssTypeDef",
    "DateFilterTypeDef",
    "DateRangeTypeDef",
    "ImportFindingsErrorTypeDef",
    "InsightResultValueTypeDef",
    "InsightResultsTypeDef",
    "InsightTypeDef",
    "InvitationTypeDef",
    "IpFilterTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "KeywordFilterTypeDef",
    "LoadBalancerStateTypeDef",
    "MalwareTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkHeaderTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkPathComponentTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "NumberFilterTypeDef",
    "PatchSummaryTypeDef",
    "PortRangeTypeDef",
    "ProcessDetailsTypeDef",
    "ProductTypeDef",
    "RecommendationTypeDef",
    "RelatedFindingTypeDef",
    "RemediationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResultTypeDef",
    "SeverityTypeDef",
    "SoftwarePackageTypeDef",
    "StandardTypeDef",
    "StandardsControlTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatusReasonTypeDef",
    "StringFilterTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "VulnerabilityTypeDef",
    "VulnerabilityVendorTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "WorkflowTypeDef",
    "AccountDetailsTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateInsightResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "DescribeStandardsResponseTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInsightResultsResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersResponseTypeDef",
    "InviteMembersResponseTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NoteUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "SeverityUpdateTypeDef",
    "SortCriterionTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "WorkflowUpdateTypeDef",
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef", {"ActionTargetArn": str, "Name": str, "Description": str}
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef", {"ZoneName": str, "SubnetId": str}, total=False
)

AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef", {"Format": str, "DestinationArn": str}, total=False
)

AwsApiGatewayCanarySettingsTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsTypeDef",
    {
        "PercentTraffic": float,
        "DeploymentId": str,
        "StageVariableOverrides": Dict[str, str],
        "UseStageCache": bool,
    },
    total=False,
)

AwsApiGatewayEndpointConfigurationTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationTypeDef", {"Types": List[str]}, total=False
)

AwsApiGatewayMethodSettingsTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsTypeDef",
    {
        "MetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
        "CachingEnabled": bool,
        "CacheTtlInSeconds": int,
        "CacheDataEncrypted": bool,
        "RequireAuthorizationForCacheControl": bool,
        "UnauthorizedCacheControlHeaderStrategy": str,
        "HttpMethod": str,
        "ResourcePath": str,
    },
    total=False,
)

AwsApiGatewayRestApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedDate": str,
        "Version": str,
        "BinaryMediaTypes": List[str],
        "MinimumCompressionSize": int,
        "ApiKeySource": str,
        "EndpointConfiguration": "AwsApiGatewayEndpointConfigurationTypeDef",
    },
    total=False,
)

AwsApiGatewayStageDetailsTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsTypeDef",
    {
        "DeploymentId": str,
        "ClientCertificateId": str,
        "StageName": str,
        "Description": str,
        "CacheClusterEnabled": bool,
        "CacheClusterSize": str,
        "CacheClusterStatus": str,
        "MethodSettings": List["AwsApiGatewayMethodSettingsTypeDef"],
        "Variables": Dict[str, str],
        "DocumentationVersion": str,
        "AccessLogSettings": "AwsApiGatewayAccessLogSettingsTypeDef",
        "CanarySettings": "AwsApiGatewayCanarySettingsTypeDef",
        "TracingEnabled": bool,
        "CreatedDate": str,
        "LastUpdatedDate": str,
        "WebAclArn": str,
    },
    total=False,
)

AwsApiGatewayV2ApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CreatedDate": str,
        "Description": str,
        "Version": str,
        "Name": str,
        "ProtocolType": str,
        "RouteSelectionExpression": str,
        "CorsConfiguration": "AwsCorsConfigurationTypeDef",
    },
    total=False,
)

AwsApiGatewayV2RouteSettingsTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsTypeDef",
    {
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": str,
        "DataTraceEnabled": bool,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

AwsApiGatewayV2StageDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsTypeDef",
    {
        "CreatedDate": str,
        "Description": str,
        "DefaultRouteSettings": "AwsApiGatewayV2RouteSettingsTypeDef",
        "DeploymentId": str,
        "LastUpdatedDate": str,
        "RouteSettings": "AwsApiGatewayV2RouteSettingsTypeDef",
        "StageName": str,
        "StageVariables": Dict[str, str],
        "AccessLogSettings": "AwsApiGatewayAccessLogSettingsTypeDef",
        "AutoDeploy": bool,
        "LastDeploymentStatusMessage": str,
        "ApiGatewayManaged": bool,
    },
    total=False,
)

AwsAutoScalingAutoScalingGroupDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LoadBalancerNames": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "CreatedTime": str,
    },
    total=False,
)

AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": str,
        "DomainName": str,
        "DomainValidationOptions": List[
            "AwsCertificateManagerCertificateDomainValidationOptionTypeDef"
        ],
        "ExtendedKeyUsages": List["AwsCertificateManagerCertificateExtendedKeyUsageTypeDef"],
        "FailureReason": str,
        "ImportedAt": str,
        "InUseBy": List[str],
        "IssuedAt": str,
        "Issuer": str,
        "KeyAlgorithm": str,
        "KeyUsages": List["AwsCertificateManagerCertificateKeyUsageTypeDef"],
        "NotAfter": str,
        "NotBefore": str,
        "Options": "AwsCertificateManagerCertificateOptionsTypeDef",
        "RenewalEligibility": str,
        "RenewalSummary": "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
        "Serial": str,
        "SignatureAlgorithm": str,
        "Status": str,
        "Subject": str,
        "SubjectAlternativeNames": List[str],
        "Type": str,
    },
    total=False,
)

AwsCertificateManagerCertificateDomainValidationOptionTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    {
        "DomainName": str,
        "ResourceRecord": "AwsCertificateManagerCertificateResourceRecordTypeDef",
        "ValidationDomain": str,
        "ValidationEmails": List[str],
        "ValidationMethod": str,
        "ValidationStatus": str,
    },
    total=False,
)

AwsCertificateManagerCertificateExtendedKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    {"Name": str, "OId": str},
    total=False,
)

AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef", {"Name": str}, total=False
)

AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": str},
    total=False,
)

AwsCertificateManagerCertificateRenewalSummaryTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    {
        "DomainValidationOptions": List[
            "AwsCertificateManagerCertificateDomainValidationOptionTypeDef"
        ],
        "RenewalStatus": str,
        "RenewalStatusReason": str,
        "UpdatedAt": str,
    },
    total=False,
)

AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)

AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef", {"ViewerProtocolPolicy": str}, total=False
)

AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {"Items": List["AwsCloudFrontDistributionCacheBehaviorTypeDef"]},
    total=False,
)

AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {"ViewerProtocolPolicy": str},
    total=False,
)

AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "CacheBehaviors": "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
        "DefaultCacheBehavior": "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
        "DefaultRootObject": str,
        "DomainName": str,
        "ETag": str,
        "LastModifiedTime": str,
        "Logging": "AwsCloudFrontDistributionLoggingTypeDef",
        "Origins": "AwsCloudFrontDistributionOriginsTypeDef",
        "OriginGroups": "AwsCloudFrontDistributionOriginGroupsTypeDef",
        "Status": str,
        "WebAclId": str,
    },
    total=False,
)

AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {"Bucket": str, "Enabled": bool, "IncludeCookies": bool, "Prefix": str},
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {"Items": List[int], "Quantity": int},
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {"StatusCodes": "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef"},
    total=False,
)

AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {"FailoverCriteria": "AwsCloudFrontDistributionOriginGroupFailoverTypeDef"},
    total=False,
)

AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {"Items": List["AwsCloudFrontDistributionOriginGroupTypeDef"]},
    total=False,
)

AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {
        "DomainName": str,
        "Id": str,
        "OriginPath": str,
        "S3OriginConfig": "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    },
    total=False,
)

AwsCloudFrontDistributionOriginS3OriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    {"OriginAccessIdentity": str},
    total=False,
)

AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {"Items": List["AwsCloudFrontDistributionOriginItemTypeDef"]},
    total=False,
)

AwsCloudTrailTrailDetailsTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "HasCustomEventSelectors": bool,
        "HomeRegion": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "IsOrganizationTrail": bool,
        "KmsKeyId": str,
        "LogFileValidationEnabled": bool,
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicArn": str,
        "SnsTopicName": str,
        "TrailArn": str,
    },
    total=False,
)

AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": str,
        "Environment": "AwsCodeBuildProjectEnvironmentTypeDef",
        "Name": str,
        "Source": "AwsCodeBuildProjectSourceTypeDef",
        "ServiceRole": str,
        "VpcConfig": "AwsCodeBuildProjectVpcConfigTypeDef",
    },
    total=False,
)

AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {"Credential": str, "CredentialProvider": str},
    total=False,
)

AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "ImagePullCredentialsType": str,
        "RegistryCredential": "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
        "Type": str,
    },
    total=False,
)

AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {"Type": str, "Location": str, "GitCloneDepth": int, "InsecureSsl": bool},
    total=False,
)

AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {"VpcId": str, "Subnets": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

AwsCorsConfigurationTypeDef = TypedDict(
    "AwsCorsConfigurationTypeDef",
    {
        "AllowOrigins": List[str],
        "AllowCredentials": bool,
        "ExposeHeaders": List[str],
        "MaxAge": int,
        "AllowMethods": List[str],
        "AllowHeaders": List[str],
    },
    total=False,
)

AwsDynamoDbTableAttributeDefinitionTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    {"AttributeName": str, "AttributeType": str},
    total=False,
)

AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {"BillingMode": str, "LastUpdateToPayPerRequestDateTime": str},
    total=False,
)

AwsDynamoDbTableDetailsTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsTypeDef",
    {
        "AttributeDefinitions": List["AwsDynamoDbTableAttributeDefinitionTypeDef"],
        "BillingModeSummary": "AwsDynamoDbTableBillingModeSummaryTypeDef",
        "CreationDateTime": str,
        "GlobalSecondaryIndexes": List["AwsDynamoDbTableGlobalSecondaryIndexTypeDef"],
        "GlobalTableVersion": str,
        "ItemCount": int,
        "KeySchema": List["AwsDynamoDbTableKeySchemaTypeDef"],
        "LatestStreamArn": str,
        "LatestStreamLabel": str,
        "LocalSecondaryIndexes": List["AwsDynamoDbTableLocalSecondaryIndexTypeDef"],
        "ProvisionedThroughput": "AwsDynamoDbTableProvisionedThroughputTypeDef",
        "Replicas": List["AwsDynamoDbTableReplicaTypeDef"],
        "RestoreSummary": "AwsDynamoDbTableRestoreSummaryTypeDef",
        "SseDescription": "AwsDynamoDbTableSseDescriptionTypeDef",
        "StreamSpecification": "AwsDynamoDbTableStreamSpecificationTypeDef",
        "TableId": str,
        "TableName": str,
        "TableSizeBytes": int,
        "TableStatus": str,
    },
    total=False,
)

AwsDynamoDbTableGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    {
        "Backfilling": bool,
        "IndexArn": str,
        "IndexName": str,
        "IndexSizeBytes": int,
        "IndexStatus": str,
        "ItemCount": int,
        "KeySchema": List["AwsDynamoDbTableKeySchemaTypeDef"],
        "Projection": "AwsDynamoDbTableProjectionTypeDef",
        "ProvisionedThroughput": "AwsDynamoDbTableProvisionedThroughputTypeDef",
    },
    total=False,
)

AwsDynamoDbTableKeySchemaTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaTypeDef", {"AttributeName": str, "KeyType": str}, total=False
)

AwsDynamoDbTableLocalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    {
        "IndexArn": str,
        "IndexName": str,
        "KeySchema": List["AwsDynamoDbTableKeySchemaTypeDef"],
        "Projection": "AwsDynamoDbTableProjectionTypeDef",
    },
    total=False,
)

AwsDynamoDbTableProjectionTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionTypeDef",
    {"NonKeyAttributes": List[str], "ProjectionType": str},
    total=False,
)

AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef", {"ReadCapacityUnits": int}, total=False
)

AwsDynamoDbTableProvisionedThroughputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    {
        "LastDecreaseDateTime": str,
        "LastIncreaseDateTime": str,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    },
    total=False,
)

AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": List["AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef"],
        "KmsMasterKeyId": str,
        "ProvisionedThroughputOverride": "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
        "RegionName": str,
        "ReplicaStatus": str,
        "ReplicaStatusDescription": str,
    },
    total=False,
)

AwsDynamoDbTableRestoreSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": str,
        "RestoreInProgress": bool,
    },
    total=False,
)

AwsDynamoDbTableSseDescriptionTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionTypeDef",
    {"InaccessibleEncryptionDateTime": str, "Status": str, "SseType": str, "KmsMasterKeyArn": str},
    total=False,
)

AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {"StreamEnabled": bool, "StreamViewType": str},
    total=False,
)

AwsEc2EipDetailsTypeDef = TypedDict(
    "AwsEc2EipDetailsTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": str,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": "AwsEc2NetworkInterfaceAttachmentTypeDef",
        "NetworkInterfaceId": str,
        "SecurityGroups": List["AwsEc2NetworkInterfaceSecurityGroupTypeDef"],
        "SourceDestCheck": bool,
    },
    total=False,
)

AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef", {"GroupName": str, "GroupId": str}, total=False
)

AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
        "OwnerId": str,
        "VpcId": str,
        "IpPermissions": List["AwsEc2SecurityGroupIpPermissionTypeDef"],
        "IpPermissionsEgress": List["AwsEc2SecurityGroupIpPermissionTypeDef"],
    },
    total=False,
)

AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "UserIdGroupPairs": List["AwsEc2SecurityGroupUserIdGroupPairTypeDef"],
        "IpRanges": List["AwsEc2SecurityGroupIpRangeTypeDef"],
        "Ipv6Ranges": List["AwsEc2SecurityGroupIpv6RangeTypeDef"],
        "PrefixListIds": List["AwsEc2SecurityGroupPrefixListIdTypeDef"],
    },
    total=False,
)

AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef", {"CidrIp": str}, total=False
)

AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef", {"CidrIpv6": str}, total=False
)

AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef", {"PrefixListId": str}, total=False
)

AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {"AttachTime": str, "DeleteOnTermination": bool, "InstanceId": str, "Status": str},
    total=False,
)

AwsEc2VolumeDetailsTypeDef = TypedDict(
    "AwsEc2VolumeDetailsTypeDef",
    {
        "CreateTime": str,
        "Encrypted": bool,
        "Size": int,
        "SnapshotId": str,
        "Status": str,
        "KmsKeyId": str,
        "Attachments": List["AwsEc2VolumeAttachmentTypeDef"],
    },
    total=False,
)

AwsEc2VpcDetailsTypeDef = TypedDict(
    "AwsEc2VpcDetailsTypeDef",
    {
        "CidrBlockAssociationSet": List["CidrBlockAssociationTypeDef"],
        "Ipv6CidrBlockAssociationSet": List["Ipv6CidrBlockAssociationTypeDef"],
        "DhcpOptionsId": str,
        "State": str,
    },
    total=False,
)

AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": str,
        "DomainEndpointOptions": "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
        "DomainId": str,
        "DomainName": str,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "ElasticsearchVersion": str,
        "EncryptionAtRestOptions": "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
        "VPCOptions": "AwsElasticsearchDomainVPCOptionsTypeDef",
    },
    total=False,
)

AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": str},
    total=False,
)

AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef", {"Enabled": bool}, total=False
)

AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VPCId": str,
    },
    total=False,
)

AwsElbAppCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyTypeDef", {"CookieName": str, "PolicyName": str}, total=False
)

AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {"CookieExpirationPeriod": int, "PolicyName": str},
    total=False,
)

AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {"EmitInterval": int, "Enabled": bool, "S3BucketName": str, "S3BucketPrefix": str},
    total=False,
)

AwsElbLoadBalancerAttributesTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesTypeDef",
    {
        "AccessLog": "AwsElbLoadBalancerAccessLogTypeDef",
        "ConnectionDraining": "AwsElbLoadBalancerConnectionDrainingTypeDef",
        "ConnectionSettings": "AwsElbLoadBalancerConnectionSettingsTypeDef",
        "CrossZoneLoadBalancing": "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    },
    total=False,
)

AwsElbLoadBalancerBackendServerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)

AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef", {"Enabled": bool, "Timeout": int}, total=False
)

AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef", {"IdleTimeout": int}, total=False
)

AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef", {"Enabled": bool}, total=False
)

AwsElbLoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackendServerDescriptions": List["AwsElbLoadBalancerBackendServerDescriptionTypeDef"],
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "CreatedTime": str,
        "DnsName": str,
        "HealthCheck": "AwsElbLoadBalancerHealthCheckTypeDef",
        "Instances": List["AwsElbLoadBalancerInstanceTypeDef"],
        "ListenerDescriptions": List["AwsElbLoadBalancerListenerDescriptionTypeDef"],
        "LoadBalancerAttributes": "AwsElbLoadBalancerAttributesTypeDef",
        "LoadBalancerName": str,
        "Policies": "AwsElbLoadBalancerPoliciesTypeDef",
        "Scheme": str,
        "SecurityGroups": List[str],
        "SourceSecurityGroup": "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
        "Subnets": List[str],
        "VpcId": str,
    },
    total=False,
)

AwsElbLoadBalancerHealthCheckTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckTypeDef",
    {
        "HealthyThreshold": int,
        "Interval": int,
        "Target": str,
        "Timeout": int,
        "UnhealthyThreshold": int,
    },
    total=False,
)

AwsElbLoadBalancerInstanceTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceTypeDef", {"InstanceId": str}, total=False
)

AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {"Listener": "AwsElbLoadBalancerListenerTypeDef", "PolicyNames": List[str]},
    total=False,
)

AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": int,
        "InstanceProtocol": str,
        "LoadBalancerPort": int,
        "Protocol": str,
        "SslCertificateId": str,
    },
    total=False,
)

AwsElbLoadBalancerPoliciesTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List["AwsElbAppCookieStickinessPolicyTypeDef"],
        "LbCookieStickinessPolicies": List["AwsElbLbCookieStickinessPolicyTypeDef"],
        "OtherPolicies": List[str],
    },
    total=False,
)

AwsElbLoadBalancerSourceSecurityGroupTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    {"GroupName": str, "OwnerAlias": str},
    total=False,
)

AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": "LoadBalancerStateTypeDef",
        "Type": str,
        "VpcId": str,
    },
    total=False,
)

AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "CreatedAt": str,
        "PrincipalId": str,
        "PrincipalType": str,
        "PrincipalName": str,
        "AccountId": str,
        "AccessKeyId": str,
        "SessionContext": "AwsIamAccessKeySessionContextTypeDef",
    },
    total=False,
)

AwsIamAccessKeySessionContextAttributesTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    {"MfaAuthenticated": bool, "CreationDate": str},
    total=False,
)

AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {"Type": str, "PrincipalId": str, "Arn": str, "AccountId": str, "UserName": str},
    total=False,
)

AwsIamAccessKeySessionContextTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextTypeDef",
    {
        "Attributes": "AwsIamAccessKeySessionContextAttributesTypeDef",
        "SessionIssuer": "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    },
    total=False,
)

AwsIamAttachedManagedPolicyTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyTypeDef", {"PolicyName": str, "PolicyArn": str}, total=False
)

AwsIamGroupDetailsTypeDef = TypedDict(
    "AwsIamGroupDetailsTypeDef",
    {
        "AttachedManagedPolicies": List["AwsIamAttachedManagedPolicyTypeDef"],
        "CreateDate": str,
        "GroupId": str,
        "GroupName": str,
        "GroupPolicyList": List["AwsIamGroupPolicyTypeDef"],
        "Path": str,
    },
    total=False,
)

AwsIamGroupPolicyTypeDef = TypedDict("AwsIamGroupPolicyTypeDef", {"PolicyName": str}, total=False)

AwsIamInstanceProfileRoleTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleTypeDef",
    {
        "Arn": str,
        "AssumeRolePolicyDocument": str,
        "CreateDate": str,
        "Path": str,
        "RoleId": str,
        "RoleName": str,
    },
    total=False,
)

AwsIamInstanceProfileTypeDef = TypedDict(
    "AwsIamInstanceProfileTypeDef",
    {
        "Arn": str,
        "CreateDate": str,
        "InstanceProfileId": str,
        "InstanceProfileName": str,
        "Path": str,
        "Roles": List["AwsIamInstanceProfileRoleTypeDef"],
    },
    total=False,
)

AwsIamPermissionsBoundaryTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryArn": str, "PermissionsBoundaryType": str},
    total=False,
)

AwsIamPolicyDetailsTypeDef = TypedDict(
    "AwsIamPolicyDetailsTypeDef",
    {
        "AttachmentCount": int,
        "CreateDate": str,
        "DefaultVersionId": str,
        "Description": str,
        "IsAttachable": bool,
        "Path": str,
        "PermissionsBoundaryUsageCount": int,
        "PolicyId": str,
        "PolicyName": str,
        "PolicyVersionList": List["AwsIamPolicyVersionTypeDef"],
        "UpdateDate": str,
    },
    total=False,
)

AwsIamPolicyVersionTypeDef = TypedDict(
    "AwsIamPolicyVersionTypeDef",
    {"VersionId": str, "IsDefaultVersion": bool, "CreateDate": str},
    total=False,
)

AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "AttachedManagedPolicies": List["AwsIamAttachedManagedPolicyTypeDef"],
        "CreateDate": str,
        "InstanceProfileList": List["AwsIamInstanceProfileTypeDef"],
        "PermissionsBoundary": "AwsIamPermissionsBoundaryTypeDef",
        "RoleId": str,
        "RoleName": str,
        "RolePolicyList": List["AwsIamRolePolicyTypeDef"],
        "MaxSessionDuration": int,
        "Path": str,
    },
    total=False,
)

AwsIamRolePolicyTypeDef = TypedDict("AwsIamRolePolicyTypeDef", {"PolicyName": str}, total=False)

AwsIamUserDetailsTypeDef = TypedDict(
    "AwsIamUserDetailsTypeDef",
    {
        "AttachedManagedPolicies": List["AwsIamAttachedManagedPolicyTypeDef"],
        "CreateDate": str,
        "GroupList": List[str],
        "Path": str,
        "PermissionsBoundary": "AwsIamPermissionsBoundaryTypeDef",
        "UserId": str,
        "UserName": str,
        "UserPolicyList": List["AwsIamUserPolicyTypeDef"],
    },
    total=False,
)

AwsIamUserPolicyTypeDef = TypedDict("AwsIamUserPolicyTypeDef", {"PolicyName": str}, total=False)

AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": str,
        "CreationDate": float,
        "KeyId": str,
        "KeyManager": str,
        "KeyState": str,
        "Origin": str,
        "Description": str,
    },
    total=False,
)

AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": str},
    total=False,
)

AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": "AwsLambdaFunctionCodeTypeDef",
        "CodeSha256": str,
        "DeadLetterConfig": "AwsLambdaFunctionDeadLetterConfigTypeDef",
        "Environment": "AwsLambdaFunctionEnvironmentTypeDef",
        "FunctionName": str,
        "Handler": str,
        "KmsKeyArn": str,
        "LastModified": str,
        "Layers": List["AwsLambdaFunctionLayerTypeDef"],
        "MasterArn": str,
        "MemorySize": int,
        "RevisionId": str,
        "Role": str,
        "Runtime": str,
        "Timeout": int,
        "TracingConfig": "AwsLambdaFunctionTracingConfigTypeDef",
        "VpcConfig": "AwsLambdaFunctionVpcConfigTypeDef",
        "Version": str,
    },
    total=False,
)

AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef", {"ErrorCode": str, "Message": str}, total=False
)

AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": "AwsLambdaFunctionEnvironmentErrorTypeDef"},
    total=False,
)

AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef", {"Mode": str}, total=False
)

AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "SubnetIds": List[str], "VpcId": str},
    total=False,
)

AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {"Version": int, "CompatibleRuntimes": List[str], "CreatedDate": str},
    total=False,
)

AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef", {"RoleArn": str, "Status": str}, total=False
)

AwsRdsDbClusterDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DatabaseName": str,
        "Status": str,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "CustomEndpoints": List[str],
        "MultiAz": bool,
        "Engine": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReadReplicaIdentifiers": List[str],
        "VpcSecurityGroups": List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "AssociatedRoles": List["AwsRdsDbClusterAssociatedRoleTypeDef"],
        "ClusterCreateTime": str,
        "EnabledCloudWatchLogsExports": List[str],
        "EngineMode": str,
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamStatus": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
        "DomainMemberships": List["AwsRdsDbDomainMembershipTypeDef"],
        "DbClusterParameterGroup": str,
        "DbSubnetGroup": str,
        "DbClusterOptionGroupMemberships": List["AwsRdsDbClusterOptionGroupMembershipTypeDef"],
        "DbClusterIdentifier": str,
        "DbClusterMembers": List["AwsRdsDbClusterMemberTypeDef"],
        "IamDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

AwsRdsDbClusterMemberTypeDef = TypedDict(
    "AwsRdsDbClusterMemberTypeDef",
    {
        "IsClusterWriter": bool,
        "PromotionTier": int,
        "DbInstanceIdentifier": str,
        "DbClusterParameterGroupStatus": str,
    },
    total=False,
)

AwsRdsDbClusterOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    {"DbClusterOptionGroupName": str, "Status": str},
    total=False,
)

AwsRdsDbClusterSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    {
        "AvailabilityZones": List[str],
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterIdentifier": str,
        "DbClusterSnapshotIdentifier": str,
        "IamDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

AwsRdsDbDomainMembershipTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipTypeDef",
    {"Domain": str, "Status": str, "Fqdn": str, "IamRoleName": str},
    total=False,
)

AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {"RoleArn": str, "FeatureName": str, "Status": str},
    total=False,
)

AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": List["AwsRdsDbInstanceAssociatedRoleTypeDef"],
        "CACertificateIdentifier": str,
        "DBClusterIdentifier": str,
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "DbInstancePort": int,
        "DbiResourceId": str,
        "DBName": str,
        "DeletionProtection": bool,
        "Endpoint": "AwsRdsDbInstanceEndpointTypeDef",
        "Engine": str,
        "EngineVersion": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "InstanceCreateTime": str,
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "StorageEncrypted": bool,
        "TdeCredentialArn": str,
        "VpcSecurityGroups": List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"],
        "MultiAz": bool,
        "EnhancedMonitoringResourceArn": str,
        "DbInstanceStatus": str,
        "MasterUsername": str,
        "AllocatedStorage": int,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DbSecurityGroups": List[str],
        "DbParameterGroups": List["AwsRdsDbParameterGroupTypeDef"],
        "AvailabilityZone": str,
        "DbSubnetGroup": "AwsRdsDbSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "AwsRdsDbPendingModifiedValuesTypeDef",
        "LatestRestorableTime": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List["AwsRdsDbOptionGroupMembershipTypeDef"],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "StatusInfos": List["AwsRdsDbStatusInfoTypeDef"],
        "StorageType": str,
        "DomainMemberships": List["AwsRdsDbDomainMembershipTypeDef"],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "Timezone": str,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKmsKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudWatchLogsExports": List[str],
        "ProcessorFeatures": List["AwsRdsDbProcessorFeatureTypeDef"],
        "ListenerEndpoint": "AwsRdsDbInstanceEndpointTypeDef",
        "MaxAllocatedStorage": int,
    },
    total=False,
)

AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)

AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef", {"OptionGroupName": str, "Status": str}, total=False
)

AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {"DbParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)

AwsRdsDbPendingModifiedValuesTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesTypeDef",
    {
        "DbInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DbInstanceIdentifier": str,
        "StorageType": str,
        "CaCertificateIdentifier": str,
        "DbSubnetGroupName": str,
        "PendingCloudWatchLogsExports": "AwsRdsPendingCloudWatchLogsExportsTypeDef",
        "ProcessorFeatures": List["AwsRdsDbProcessorFeatureTypeDef"],
    },
    total=False,
)

AwsRdsDbProcessorFeatureTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureTypeDef", {"Name": str, "Value": str}, total=False
)

AwsRdsDbSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsTypeDef",
    {
        "DbSnapshotIdentifier": str,
        "DbInstanceIdentifier": str,
        "SnapshotCreateTime": str,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": str,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDbSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "Timezone": str,
        "IamDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List["AwsRdsDbProcessorFeatureTypeDef"],
        "DbiResourceId": str,
    },
    total=False,
)

AwsRdsDbStatusInfoTypeDef = TypedDict(
    "AwsRdsDbStatusInfoTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)

AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef", {"Name": str}, total=False
)

AwsRdsDbSubnetGroupSubnetTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

AwsRdsDbSubnetGroupTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupTypeDef",
    {
        "DbSubnetGroupName": str,
        "DbSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["AwsRdsDbSubnetGroupSubnetTypeDef"],
        "DbSubnetGroupArn": str,
    },
    total=False,
)

AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)

AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {"NodeRole": str, "PrivateIpAddress": str, "PublicIpAddress": str},
    total=False,
)

AwsRedshiftClusterClusterParameterGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    {
        "ClusterParameterStatusList": List["AwsRedshiftClusterClusterParameterStatusTypeDef"],
        "ParameterApplyStatus": str,
        "ParameterGroupName": str,
    },
    total=False,
)

AwsRedshiftClusterClusterParameterStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    {"ParameterName": str, "ParameterApplyStatus": str, "ParameterApplyErrorDescription": str},
    total=False,
)

AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {"ClusterSecurityGroupName": str, "Status": str},
    total=False,
)

AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "ManualSnapshotRetentionPeriod": int,
        "RetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

AwsRedshiftClusterDeferredMaintenanceWindowTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceEndTime": str,
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": str,
    },
    total=False,
)

AwsRedshiftClusterDetailsTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsTypeDef",
    {
        "AllowVersionUpgrade": bool,
        "AutomatedSnapshotRetentionPeriod": int,
        "AvailabilityZone": str,
        "ClusterAvailabilityStatus": str,
        "ClusterCreateTime": str,
        "ClusterIdentifier": str,
        "ClusterNodes": List["AwsRedshiftClusterClusterNodeTypeDef"],
        "ClusterParameterGroups": List["AwsRedshiftClusterClusterParameterGroupTypeDef"],
        "ClusterPublicKey": str,
        "ClusterRevisionNumber": str,
        "ClusterSecurityGroups": List["AwsRedshiftClusterClusterSecurityGroupTypeDef"],
        "ClusterSnapshotCopyStatus": "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
        "ClusterStatus": str,
        "ClusterSubnetGroupName": str,
        "ClusterVersion": str,
        "DBName": str,
        "DeferredMaintenanceWindows": List["AwsRedshiftClusterDeferredMaintenanceWindowTypeDef"],
        "ElasticIpStatus": "AwsRedshiftClusterElasticIpStatusTypeDef",
        "ElasticResizeNumberOfNodeOptions": str,
        "Encrypted": bool,
        "Endpoint": "AwsRedshiftClusterEndpointTypeDef",
        "EnhancedVpcRouting": bool,
        "ExpectedNextSnapshotScheduleTime": str,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "HsmStatus": "AwsRedshiftClusterHsmStatusTypeDef",
        "IamRoles": List["AwsRedshiftClusterIamRoleTypeDef"],
        "KmsKeyId": str,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "MasterUsername": str,
        "NextMaintenanceWindowStartTime": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PendingActions": List[str],
        "PendingModifiedValues": "AwsRedshiftClusterPendingModifiedValuesTypeDef",
        "PreferredMaintenanceWindow": str,
        "PubliclyAccessible": bool,
        "ResizeInfo": "AwsRedshiftClusterResizeInfoTypeDef",
        "RestoreStatus": "AwsRedshiftClusterRestoreStatusTypeDef",
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": str,
        "VpcId": str,
        "VpcSecurityGroups": List["AwsRedshiftClusterVpcSecurityGroupTypeDef"],
    },
    total=False,
)

AwsRedshiftClusterElasticIpStatusTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusTypeDef", {"ElasticIp": str, "Status": str}, total=False
)

AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef", {"Address": str, "Port": int}, total=False
)

AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {"HsmClientCertificateIdentifier": str, "HsmConfigurationIdentifier": str, "Status": str},
    total=False,
)

AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef", {"ApplyStatus": str, "IamRoleArn": str}, total=False
)

AwsRedshiftClusterPendingModifiedValuesTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "ClusterType": str,
        "ClusterVersion": str,
        "EncryptionType": str,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
    },
    total=False,
)

AwsRedshiftClusterResizeInfoTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoTypeDef",
    {"AllowCancelResize": bool, "ResizeType": str},
    total=False,
)

AwsRedshiftClusterRestoreStatusTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ProgressInMegaBytes": int,
        "SnapshotSizeInMegaBytes": int,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterVpcSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    {"Status": str, "VpcSecurityGroupId": str},
    total=False,
)

AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": str,
        "OwnerName": str,
        "CreatedAt": str,
        "ServerSideEncryptionConfiguration": "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    },
    total=False,
)

AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": str, "KMSMasterKeyID": str},
    total=False,
)

AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {"Rules": List["AwsS3BucketServerSideEncryptionRuleTypeDef"]},
    total=False,
)

AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {"ApplyServerSideEncryptionByDefault": "AwsS3BucketServerSideEncryptionByDefaultTypeDef"},
    total=False,
)

AwsS3ObjectDetailsTypeDef = TypedDict(
    "AwsS3ObjectDetailsTypeDef",
    {
        "LastModified": str,
        "ETag": str,
        "VersionId": str,
        "ContentType": str,
        "ServerSideEncryption": str,
        "SSEKMSKeyId": str,
    },
    total=False,
)

AwsSecretsManagerSecretDetailsTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsTypeDef",
    {
        "RotationRules": "AwsSecretsManagerSecretRotationRulesTypeDef",
        "RotationOccurredWithinFrequency": bool,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaArn": str,
        "Deleted": bool,
        "Name": str,
        "Description": str,
    },
    total=False,
)

AwsSecretsManagerSecretRotationRulesTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesTypeDef", {"AutomaticallyAfterDays": int}, total=False
)

AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": List["StringFilterTypeDef"],
        "AwsAccountId": List["StringFilterTypeDef"],
        "Id": List["StringFilterTypeDef"],
        "GeneratorId": List["StringFilterTypeDef"],
        "Type": List["StringFilterTypeDef"],
        "FirstObservedAt": List["DateFilterTypeDef"],
        "LastObservedAt": List["DateFilterTypeDef"],
        "CreatedAt": List["DateFilterTypeDef"],
        "UpdatedAt": List["DateFilterTypeDef"],
        "SeverityProduct": List["NumberFilterTypeDef"],
        "SeverityNormalized": List["NumberFilterTypeDef"],
        "SeverityLabel": List["StringFilterTypeDef"],
        "Confidence": List["NumberFilterTypeDef"],
        "Criticality": List["NumberFilterTypeDef"],
        "Title": List["StringFilterTypeDef"],
        "Description": List["StringFilterTypeDef"],
        "RecommendationText": List["StringFilterTypeDef"],
        "SourceUrl": List["StringFilterTypeDef"],
        "ProductFields": List["MapFilterTypeDef"],
        "ProductName": List["StringFilterTypeDef"],
        "CompanyName": List["StringFilterTypeDef"],
        "UserDefinedFields": List["MapFilterTypeDef"],
        "MalwareName": List["StringFilterTypeDef"],
        "MalwareType": List["StringFilterTypeDef"],
        "MalwarePath": List["StringFilterTypeDef"],
        "MalwareState": List["StringFilterTypeDef"],
        "NetworkDirection": List["StringFilterTypeDef"],
        "NetworkProtocol": List["StringFilterTypeDef"],
        "NetworkSourceIpV4": List["IpFilterTypeDef"],
        "NetworkSourceIpV6": List["IpFilterTypeDef"],
        "NetworkSourcePort": List["NumberFilterTypeDef"],
        "NetworkSourceDomain": List["StringFilterTypeDef"],
        "NetworkSourceMac": List["StringFilterTypeDef"],
        "NetworkDestinationIpV4": List["IpFilterTypeDef"],
        "NetworkDestinationIpV6": List["IpFilterTypeDef"],
        "NetworkDestinationPort": List["NumberFilterTypeDef"],
        "NetworkDestinationDomain": List["StringFilterTypeDef"],
        "ProcessName": List["StringFilterTypeDef"],
        "ProcessPath": List["StringFilterTypeDef"],
        "ProcessPid": List["NumberFilterTypeDef"],
        "ProcessParentPid": List["NumberFilterTypeDef"],
        "ProcessLaunchedAt": List["DateFilterTypeDef"],
        "ProcessTerminatedAt": List["DateFilterTypeDef"],
        "ThreatIntelIndicatorType": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorValue": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorCategory": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorLastObservedAt": List["DateFilterTypeDef"],
        "ThreatIntelIndicatorSource": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorSourceUrl": List["StringFilterTypeDef"],
        "ResourceType": List["StringFilterTypeDef"],
        "ResourceId": List["StringFilterTypeDef"],
        "ResourcePartition": List["StringFilterTypeDef"],
        "ResourceRegion": List["StringFilterTypeDef"],
        "ResourceTags": List["MapFilterTypeDef"],
        "ResourceAwsEc2InstanceType": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceImageId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceIpV4Addresses": List["IpFilterTypeDef"],
        "ResourceAwsEc2InstanceIpV6Addresses": List["IpFilterTypeDef"],
        "ResourceAwsEc2InstanceKeyName": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceVpcId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceSubnetId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceLaunchedAt": List["DateFilterTypeDef"],
        "ResourceAwsS3BucketOwnerId": List["StringFilterTypeDef"],
        "ResourceAwsS3BucketOwnerName": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyUserName": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyStatus": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyCreatedAt": List["DateFilterTypeDef"],
        "ResourceContainerName": List["StringFilterTypeDef"],
        "ResourceContainerImageId": List["StringFilterTypeDef"],
        "ResourceContainerImageName": List["StringFilterTypeDef"],
        "ResourceContainerLaunchedAt": List["DateFilterTypeDef"],
        "ResourceDetailsOther": List["MapFilterTypeDef"],
        "ComplianceStatus": List["StringFilterTypeDef"],
        "VerificationState": List["StringFilterTypeDef"],
        "WorkflowState": List["StringFilterTypeDef"],
        "WorkflowStatus": List["StringFilterTypeDef"],
        "RecordState": List["StringFilterTypeDef"],
        "RelatedFindingsProductArn": List["StringFilterTypeDef"],
        "RelatedFindingsId": List["StringFilterTypeDef"],
        "NoteText": List["StringFilterTypeDef"],
        "NoteUpdatedAt": List["DateFilterTypeDef"],
        "NoteUpdatedBy": List["StringFilterTypeDef"],
        "Keyword": List["KeywordFilterTypeDef"],
    },
    total=False,
)

AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef", {"Id": str, "ProductArn": str}
)

_RequiredAwsSecurityFindingTypeDef = TypedDict(
    "_RequiredAwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "Types": List[str],
        "CreatedAt": str,
        "UpdatedAt": str,
        "Severity": "SeverityTypeDef",
        "Title": str,
        "Description": str,
        "Resources": List["ResourceTypeDef"],
    },
)
_OptionalAwsSecurityFindingTypeDef = TypedDict(
    "_OptionalAwsSecurityFindingTypeDef",
    {
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "Confidence": int,
        "Criticality": int,
        "Remediation": "RemediationTypeDef",
        "SourceUrl": str,
        "ProductFields": Dict[str, str],
        "UserDefinedFields": Dict[str, str],
        "Malware": List["MalwareTypeDef"],
        "Network": "NetworkTypeDef",
        "NetworkPath": List["NetworkPathComponentTypeDef"],
        "Process": "ProcessDetailsTypeDef",
        "ThreatIntelIndicators": List["ThreatIntelIndicatorTypeDef"],
        "Compliance": "ComplianceTypeDef",
        "VerificationState": Literal[
            "UNKNOWN", "TRUE_POSITIVE", "FALSE_POSITIVE", "BENIGN_POSITIVE"
        ],
        "WorkflowState": Literal["NEW", "ASSIGNED", "IN_PROGRESS", "DEFERRED", "RESOLVED"],
        "Workflow": "WorkflowTypeDef",
        "RecordState": Literal["ACTIVE", "ARCHIVED"],
        "RelatedFindings": List["RelatedFindingTypeDef"],
        "Note": "NoteTypeDef",
        "Vulnerabilities": List["VulnerabilityTypeDef"],
        "PatchSummary": "PatchSummaryTypeDef",
    },
    total=False,
)


class AwsSecurityFindingTypeDef(
    _RequiredAwsSecurityFindingTypeDef, _OptionalAwsSecurityFindingTypeDef
):
    pass


AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": str,
        "Subscription": List["AwsSnsTopicSubscriptionTypeDef"],
        "TopicName": str,
        "Owner": str,
    },
    total=False,
)

AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef", {"Endpoint": str, "Protocol": str}, total=False
)

AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": int,
        "KmsMasterKeyId": str,
        "QueueName": str,
        "DeadLetterTargetArn": str,
    },
    total=False,
)

AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {"Name": str, "DefaultAction": str, "Rules": List["AwsWafWebAclRuleTypeDef"], "WebAclId": str},
    total=False,
)

AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": "WafActionTypeDef",
        "ExcludedRules": List["WafExcludedRuleTypeDef"],
        "OverrideAction": "WafOverrideActionTypeDef",
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)

BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": "AwsSecurityFindingIdentifierTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {"AssociationId": str, "CidrBlock": str, "CidrBlockState": str},
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": Literal["PASSED", "WARNING", "FAILED", "NOT_AVAILABLE"],
        "RelatedRequirements": List[str],
        "StatusReasons": List["StatusReasonTypeDef"],
    },
    total=False,
)

ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {"Name": str, "ImageId": str, "ImageName": str, "LaunchedAt": str},
    total=False,
)

CvssTypeDef = TypedDict(
    "CvssTypeDef", {"Version": str, "BaseScore": float, "BaseVector": str}, total=False
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef", {"Start": str, "End": str, "DateRange": "DateRangeTypeDef"}, total=False
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef", {"Value": int, "Unit": Literal["DAYS"]}, total=False
)

ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef", {"Id": str, "ErrorCode": str, "ErrorMessage": str}
)

InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef", {"GroupByAttributeValue": str, "Count": int}
)

InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {"InsightArn": str, "GroupByAttribute": str, "ResultValues": List["InsightResultValueTypeDef"]},
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "GroupByAttribute": str,
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {"AccountId": str, "InvitationId": str, "InvitedAt": datetime, "MemberStatus": str},
    total=False,
)

IpFilterTypeDef = TypedDict("IpFilterTypeDef", {"Cidr": str}, total=False)

Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {"AssociationId": str, "Ipv6CidrBlock": str, "CidrBlockState": str},
    total=False,
)

KeywordFilterTypeDef = TypedDict("KeywordFilterTypeDef", {"Value": str}, total=False)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef", {"Code": str, "Reason": str}, total=False
)

_RequiredMalwareTypeDef = TypedDict("_RequiredMalwareTypeDef", {"Name": str})
_OptionalMalwareTypeDef = TypedDict(
    "_OptionalMalwareTypeDef",
    {
        "Type": Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "SPYWARE",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "TROJAN",
            "VIRUS",
            "WORM",
        ],
        "Path": str,
        "State": Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"],
    },
    total=False,
)


class MalwareTypeDef(_RequiredMalwareTypeDef, _OptionalMalwareTypeDef):
    pass


MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {"Key": str, "Value": str, "Comparison": Literal["EQUALS", "NOT_EQUALS"]},
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": str,
        "Destination": "NetworkPathComponentDetailsTypeDef",
        "Source": "NetworkPathComponentDetailsTypeDef",
    },
    total=False,
)

NetworkPathComponentDetailsTypeDef = TypedDict(
    "NetworkPathComponentDetailsTypeDef",
    {"Address": List[str], "PortRanges": List["PortRangeTypeDef"]},
    total=False,
)

NetworkPathComponentTypeDef = TypedDict(
    "NetworkPathComponentTypeDef",
    {
        "ComponentId": str,
        "ComponentType": str,
        "Egress": "NetworkHeaderTypeDef",
        "Ingress": "NetworkHeaderTypeDef",
    },
    total=False,
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": Literal["IN", "OUT"],
        "Protocol": str,
        "OpenPortRange": "PortRangeTypeDef",
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

NoteTypeDef = TypedDict("NoteTypeDef", {"Text": str, "UpdatedBy": str, "UpdatedAt": str})

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef", {"Gte": float, "Lte": float, "Eq": float}, total=False
)

_RequiredPatchSummaryTypeDef = TypedDict("_RequiredPatchSummaryTypeDef", {"Id": str})
_OptionalPatchSummaryTypeDef = TypedDict(
    "_OptionalPatchSummaryTypeDef",
    {
        "InstalledCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "InstalledOtherCount": int,
        "InstalledRejectedCount": int,
        "InstalledPendingReboot": int,
        "OperationStartTime": str,
        "OperationEndTime": str,
        "RebootOption": str,
        "Operation": str,
    },
    total=False,
)


class PatchSummaryTypeDef(_RequiredPatchSummaryTypeDef, _OptionalPatchSummaryTypeDef):
    pass


PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"Begin": int, "End": int}, total=False)

ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": str,
        "Path": str,
        "Pid": int,
        "ParentPid": int,
        "LaunchedAt": str,
        "TerminatedAt": str,
    },
    total=False,
)

_RequiredProductTypeDef = TypedDict("_RequiredProductTypeDef", {"ProductArn": str})
_OptionalProductTypeDef = TypedDict(
    "_OptionalProductTypeDef",
    {
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "IntegrationTypes": List[
            Literal["SEND_FINDINGS_TO_SECURITY_HUB", "RECEIVE_FINDINGS_FROM_SECURITY_HUB"]
        ],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
    total=False,
)


class ProductTypeDef(_RequiredProductTypeDef, _OptionalProductTypeDef):
    pass


RecommendationTypeDef = TypedDict("RecommendationTypeDef", {"Text": str, "Url": str}, total=False)

RelatedFindingTypeDef = TypedDict("RelatedFindingTypeDef", {"ProductArn": str, "Id": str})

RemediationTypeDef = TypedDict(
    "RemediationTypeDef", {"Recommendation": "RecommendationTypeDef"}, total=False
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
        "AwsCodeBuildProject": "AwsCodeBuildProjectDetailsTypeDef",
        "AwsCloudFrontDistribution": "AwsCloudFrontDistributionDetailsTypeDef",
        "AwsEc2Instance": "AwsEc2InstanceDetailsTypeDef",
        "AwsEc2NetworkInterface": "AwsEc2NetworkInterfaceDetailsTypeDef",
        "AwsEc2SecurityGroup": "AwsEc2SecurityGroupDetailsTypeDef",
        "AwsEc2Volume": "AwsEc2VolumeDetailsTypeDef",
        "AwsEc2Vpc": "AwsEc2VpcDetailsTypeDef",
        "AwsEc2Eip": "AwsEc2EipDetailsTypeDef",
        "AwsElbv2LoadBalancer": "AwsElbv2LoadBalancerDetailsTypeDef",
        "AwsElasticsearchDomain": "AwsElasticsearchDomainDetailsTypeDef",
        "AwsS3Bucket": "AwsS3BucketDetailsTypeDef",
        "AwsS3Object": "AwsS3ObjectDetailsTypeDef",
        "AwsSecretsManagerSecret": "AwsSecretsManagerSecretDetailsTypeDef",
        "AwsIamAccessKey": "AwsIamAccessKeyDetailsTypeDef",
        "AwsIamUser": "AwsIamUserDetailsTypeDef",
        "AwsIamPolicy": "AwsIamPolicyDetailsTypeDef",
        "AwsApiGatewayV2Stage": "AwsApiGatewayV2StageDetailsTypeDef",
        "AwsApiGatewayV2Api": "AwsApiGatewayV2ApiDetailsTypeDef",
        "AwsDynamoDbTable": "AwsDynamoDbTableDetailsTypeDef",
        "AwsApiGatewayStage": "AwsApiGatewayStageDetailsTypeDef",
        "AwsApiGatewayRestApi": "AwsApiGatewayRestApiDetailsTypeDef",
        "AwsCloudTrailTrail": "AwsCloudTrailTrailDetailsTypeDef",
        "AwsCertificateManagerCertificate": "AwsCertificateManagerCertificateDetailsTypeDef",
        "AwsRedshiftCluster": "AwsRedshiftClusterDetailsTypeDef",
        "AwsElbLoadBalancer": "AwsElbLoadBalancerDetailsTypeDef",
        "AwsIamGroup": "AwsIamGroupDetailsTypeDef",
        "AwsIamRole": "AwsIamRoleDetailsTypeDef",
        "AwsKmsKey": "AwsKmsKeyDetailsTypeDef",
        "AwsLambdaFunction": "AwsLambdaFunctionDetailsTypeDef",
        "AwsLambdaLayerVersion": "AwsLambdaLayerVersionDetailsTypeDef",
        "AwsRdsDbInstance": "AwsRdsDbInstanceDetailsTypeDef",
        "AwsSnsTopic": "AwsSnsTopicDetailsTypeDef",
        "AwsSqsQueue": "AwsSqsQueueDetailsTypeDef",
        "AwsWafWebAcl": "AwsWafWebAclDetailsTypeDef",
        "AwsRdsDbSnapshot": "AwsRdsDbSnapshotDetailsTypeDef",
        "AwsRdsDbClusterSnapshot": "AwsRdsDbClusterSnapshotDetailsTypeDef",
        "AwsRdsDbCluster": "AwsRdsDbClusterDetailsTypeDef",
        "Container": "ContainerDetailsTypeDef",
        "Other": Dict[str, str],
    },
    total=False,
)

_RequiredResourceTypeDef = TypedDict("_RequiredResourceTypeDef", {"Type": str, "Id": str})
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "Partition": Literal["aws", "aws-cn", "aws-us-gov"],
        "Region": str,
        "ResourceRole": str,
        "Tags": Dict[str, str],
        "Details": "ResourceDetailsTypeDef",
    },
    total=False,
)


class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass


ResultTypeDef = TypedDict("ResultTypeDef", {"AccountId": str, "ProcessingResult": str}, total=False)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": float,
        "Label": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"],
        "Normalized": int,
        "Original": str,
    },
    total=False,
)

SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {"Name": str, "Version": str, "Epoch": str, "Release": str, "Architecture": str},
    total=False,
)

StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {"StandardsArn": str, "Name": str, "Description": str, "EnabledByDefault": bool},
    total=False,
)

StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": Literal["ENABLED", "DISABLED"],
        "DisabledReason": str,
        "ControlStatusUpdatedAt": datetime,
        "ControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        "RelatedRequirements": List[str],
    },
    total=False,
)

StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": Literal["PENDING", "READY", "FAILED", "DELETING", "INCOMPLETE"],
    },
)

_RequiredStatusReasonTypeDef = TypedDict("_RequiredStatusReasonTypeDef", {"ReasonCode": str})
_OptionalStatusReasonTypeDef = TypedDict(
    "_OptionalStatusReasonTypeDef", {"Description": str}, total=False
)


class StatusReasonTypeDef(_RequiredStatusReasonTypeDef, _OptionalStatusReasonTypeDef):
    pass


StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {"Value": str, "Comparison": Literal["EQUALS", "PREFIX", "NOT_EQUALS", "PREFIX_NOT_EQUALS"]},
    total=False,
)

ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ],
        "Value": str,
        "Category": Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ],
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

_RequiredVulnerabilityTypeDef = TypedDict("_RequiredVulnerabilityTypeDef", {"Id": str})
_OptionalVulnerabilityTypeDef = TypedDict(
    "_OptionalVulnerabilityTypeDef",
    {
        "VulnerablePackages": List["SoftwarePackageTypeDef"],
        "Cvss": List["CvssTypeDef"],
        "RelatedVulnerabilities": List[str],
        "Vendor": "VulnerabilityVendorTypeDef",
        "ReferenceUrls": List[str],
    },
    total=False,
)


class VulnerabilityTypeDef(_RequiredVulnerabilityTypeDef, _OptionalVulnerabilityTypeDef):
    pass


_RequiredVulnerabilityVendorTypeDef = TypedDict(
    "_RequiredVulnerabilityVendorTypeDef", {"Name": str}
)
_OptionalVulnerabilityVendorTypeDef = TypedDict(
    "_OptionalVulnerabilityVendorTypeDef",
    {"Url": str, "VendorSeverity": str, "VendorCreatedAt": str, "VendorUpdatedAt": str},
    total=False,
)


class VulnerabilityVendorTypeDef(
    _RequiredVulnerabilityVendorTypeDef, _OptionalVulnerabilityVendorTypeDef
):
    pass


WafActionTypeDef = TypedDict("WafActionTypeDef", {"Type": str}, total=False)

WafExcludedRuleTypeDef = TypedDict("WafExcludedRuleTypeDef", {"RuleId": str}, total=False)

WafOverrideActionTypeDef = TypedDict("WafOverrideActionTypeDef", {"Type": str}, total=False)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef", {"Status": Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]}, total=False
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef", {"AccountId": str, "Email": str}, total=False
)

BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {"StandardsSubscriptions": List["StandardsSubscriptionTypeDef"]},
    total=False,
)

BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {"StandardsSubscriptions": List["StandardsSubscriptionTypeDef"]},
    total=False,
)

_RequiredBatchImportFindingsResponseTypeDef = TypedDict(
    "_RequiredBatchImportFindingsResponseTypeDef", {"FailedCount": int, "SuccessCount": int}
)
_OptionalBatchImportFindingsResponseTypeDef = TypedDict(
    "_OptionalBatchImportFindingsResponseTypeDef",
    {"FailedFindings": List["ImportFindingsErrorTypeDef"]},
    total=False,
)


class BatchImportFindingsResponseTypeDef(
    _RequiredBatchImportFindingsResponseTypeDef, _OptionalBatchImportFindingsResponseTypeDef
):
    pass


BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List["AwsSecurityFindingIdentifierTypeDef"],
        "UnprocessedFindings": List["BatchUpdateFindingsUnprocessedFindingTypeDef"],
    },
)

CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef", {"ActionTargetArn": str}
)

CreateInsightResponseTypeDef = TypedDict("CreateInsightResponseTypeDef", {"InsightArn": str})

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef", {"UnprocessedAccounts": List["ResultTypeDef"]}, total=False
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef", {"UnprocessedAccounts": List["ResultTypeDef"]}, total=False
)

DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef", {"ActionTargetArn": str}
)

DeleteInsightResponseTypeDef = TypedDict("DeleteInsightResponseTypeDef", {"InsightArn": str})

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef", {"UnprocessedAccounts": List["ResultTypeDef"]}, total=False
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef", {"UnprocessedAccounts": List["ResultTypeDef"]}, total=False
)

_RequiredDescribeActionTargetsResponseTypeDef = TypedDict(
    "_RequiredDescribeActionTargetsResponseTypeDef", {"ActionTargets": List["ActionTargetTypeDef"]}
)
_OptionalDescribeActionTargetsResponseTypeDef = TypedDict(
    "_OptionalDescribeActionTargetsResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeActionTargetsResponseTypeDef(
    _RequiredDescribeActionTargetsResponseTypeDef, _OptionalDescribeActionTargetsResponseTypeDef
):
    pass


DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {"HubArn": str, "SubscribedAt": str, "AutoEnableControls": bool},
    total=False,
)

_RequiredDescribeProductsResponseTypeDef = TypedDict(
    "_RequiredDescribeProductsResponseTypeDef", {"Products": List["ProductTypeDef"]}
)
_OptionalDescribeProductsResponseTypeDef = TypedDict(
    "_OptionalDescribeProductsResponseTypeDef", {"NextToken": str}, total=False
)


class DescribeProductsResponseTypeDef(
    _RequiredDescribeProductsResponseTypeDef, _OptionalDescribeProductsResponseTypeDef
):
    pass


DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {"Controls": List["StandardsControlTypeDef"], "NextToken": str},
    total=False,
)

DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {"Standards": List["StandardTypeDef"], "NextToken": str},
    total=False,
)

EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef", {"ProductSubscriptionArn": str}, total=False
)

GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {"StandardsSubscriptions": List["StandardsSubscriptionTypeDef"], "NextToken": str},
    total=False,
)

_RequiredGetFindingsResponseTypeDef = TypedDict(
    "_RequiredGetFindingsResponseTypeDef", {"Findings": List["AwsSecurityFindingTypeDef"]}
)
_OptionalGetFindingsResponseTypeDef = TypedDict(
    "_OptionalGetFindingsResponseTypeDef", {"NextToken": str}, total=False
)


class GetFindingsResponseTypeDef(
    _RequiredGetFindingsResponseTypeDef, _OptionalGetFindingsResponseTypeDef
):
    pass


GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef", {"InsightResults": "InsightResultsTypeDef"}
)

_RequiredGetInsightsResponseTypeDef = TypedDict(
    "_RequiredGetInsightsResponseTypeDef", {"Insights": List["InsightTypeDef"]}
)
_OptionalGetInsightsResponseTypeDef = TypedDict(
    "_OptionalGetInsightsResponseTypeDef", {"NextToken": str}, total=False
)


class GetInsightsResponseTypeDef(
    _RequiredGetInsightsResponseTypeDef, _OptionalGetInsightsResponseTypeDef
):
    pass


GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef", {"InvitationsCount": int}, total=False
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef", {"Master": "InvitationTypeDef"}, total=False
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {"Members": List["MemberTypeDef"], "UnprocessedAccounts": List["ResultTypeDef"]},
    total=False,
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef", {"UnprocessedAccounts": List["ResultTypeDef"]}, total=False
)

ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {"ProductSubscriptions": List[str], "NextToken": str},
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"Invitations": List["InvitationTypeDef"], "NextToken": str},
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef", {"Members": List["MemberTypeDef"], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

NoteUpdateTypeDef = TypedDict("NoteUpdateTypeDef", {"Text": str, "UpdatedBy": str})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": int,
        "Product": float,
        "Label": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"],
    },
    total=False,
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef", {"Field": str, "SortOrder": Literal["asc", "desc"]}, total=False
)

_RequiredStandardsSubscriptionRequestTypeDef = TypedDict(
    "_RequiredStandardsSubscriptionRequestTypeDef", {"StandardsArn": str}
)
_OptionalStandardsSubscriptionRequestTypeDef = TypedDict(
    "_OptionalStandardsSubscriptionRequestTypeDef", {"StandardsInput": Dict[str, str]}, total=False
)


class StandardsSubscriptionRequestTypeDef(
    _RequiredStandardsSubscriptionRequestTypeDef, _OptionalStandardsSubscriptionRequestTypeDef
):
    pass


WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {"Status": Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]},
    total=False,
)
