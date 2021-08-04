"""
Type annotations for securityhub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdminStatusType,
    AwsIamAccessKeyStatusType,
    ComplianceStatusType,
    ControlStatusType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    PartitionType,
    RecordStateType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsStatusType,
    StringFilterComparisonType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    VerificationStateType,
    WorkflowStateType,
    WorkflowStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiCallActionTypeDef",
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
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
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
    "AwsRdsEventSubscriptionDetailsTypeDef",
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
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
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
    "AwsSsmComplianceSummaryTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "BatchDisableStandardsRequestRequestTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsRequestRequestTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "BatchImportFindingsRequestRequestTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateFindingsRequestRequestTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "CellTypeDef",
    "CidrBlockAssociationTypeDef",
    "CityTypeDef",
    "ClassificationResultTypeDef",
    "ClassificationStatusTypeDef",
    "ComplianceTypeDef",
    "ContainerDetailsTypeDef",
    "CountryTypeDef",
    "CreateActionTargetRequestRequestTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateInsightRequestRequestTypeDef",
    "CreateInsightResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "CvssTypeDef",
    "DataClassificationDetailsTypeDef",
    "DateFilterTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteActionTargetRequestRequestTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DeleteInsightResponseTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeActionTargetsRequestRequestTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribeProductsRequestRequestTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsRequestRequestTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "DescribeStandardsRequestRequestTypeDef",
    "DescribeStandardsResponseTypeDef",
    "DisableImportFindingsForProductRequestRequestTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "DnsRequestActionTypeDef",
    "EnableImportFindingsForProductRequestRequestTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EnableSecurityHubRequestRequestTypeDef",
    "FindingProviderFieldsTypeDef",
    "FindingProviderSeverityTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetEnabledStandardsRequestRequestTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInsightResultsRequestRequestTypeDef",
    "GetInsightResultsResponseTypeDef",
    "GetInsightsRequestRequestTypeDef",
    "GetInsightsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "IcmpTypeCodeTypeDef",
    "ImportFindingsErrorTypeDef",
    "InsightResultValueTypeDef",
    "InsightResultsTypeDef",
    "InsightTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "IpFilterTypeDef",
    "IpOrganizationDetailsTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "KeywordFilterTypeDef",
    "ListEnabledProductsForImportRequestRequestTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoadBalancerStateTypeDef",
    "MalwareTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkHeaderTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkPathComponentTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "NoteUpdateTypeDef",
    "NumberFilterTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PatchSummaryTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PortRangeFromToTypeDef",
    "PortRangeTypeDef",
    "ProcessDetailsTypeDef",
    "ProductTypeDef",
    "RangeTypeDef",
    "RecommendationTypeDef",
    "RecordTypeDef",
    "RelatedFindingTypeDef",
    "RemediationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ResultTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SensitiveDataResultTypeDef",
    "SeverityTypeDef",
    "SeverityUpdateTypeDef",
    "SoftwarePackageTypeDef",
    "SortCriterionTypeDef",
    "StandardTypeDef",
    "StandardsControlTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatusReasonTypeDef",
    "StringFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActionTargetRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "UpdateInsightRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    "UpdateStandardsControlRequestRequestTypeDef",
    "VulnerabilityTypeDef",
    "VulnerabilityVendorTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "WorkflowTypeDef",
    "WorkflowUpdateTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "AdministratorId": str,
        "InvitationId": str,
    },
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "MasterId": str,
        "InvitationId": str,
    },
)

_RequiredAccountDetailsTypeDef = TypedDict(
    "_RequiredAccountDetailsTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalAccountDetailsTypeDef = TypedDict(
    "_OptionalAccountDetailsTypeDef",
    {
        "Email": str,
    },
    total=False,
)

class AccountDetailsTypeDef(_RequiredAccountDetailsTypeDef, _OptionalAccountDetailsTypeDef):
    pass

ActionLocalIpDetailsTypeDef = TypedDict(
    "ActionLocalIpDetailsTypeDef",
    {
        "IpAddressV4": str,
    },
    total=False,
)

ActionLocalPortDetailsTypeDef = TypedDict(
    "ActionLocalPortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

ActionRemoteIpDetailsTypeDef = TypedDict(
    "ActionRemoteIpDetailsTypeDef",
    {
        "IpAddressV4": str,
        "Organization": "IpOrganizationDetailsTypeDef",
        "Country": "CountryTypeDef",
        "City": "CityTypeDef",
        "GeoLocation": "GeoLocationTypeDef",
    },
    total=False,
)

ActionRemotePortDetailsTypeDef = TypedDict(
    "ActionRemotePortDetailsTypeDef",
    {
        "Port": int,
        "PortName": str,
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ActionTargetArn": str,
        "Name": str,
        "Description": str,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": str,
        "NetworkConnectionAction": "NetworkConnectionActionTypeDef",
        "AwsApiCallAction": "AwsApiCallActionTypeDef",
        "DnsRequestAction": "DnsRequestActionTypeDef",
        "PortProbeAction": "PortProbeActionTypeDef",
    },
    total=False,
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AccountId": str,
        "Status": AdminStatusType,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
    },
    total=False,
)

AwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": str,
        "ServiceName": str,
        "CallerType": str,
        "RemoteIpDetails": "ActionRemoteIpDetailsTypeDef",
        "DomainDetails": "AwsApiCallActionDomainDetailsTypeDef",
        "AffectedResources": Dict[str, str],
        "FirstSeen": str,
        "LastSeen": str,
    },
    total=False,
)

AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef",
    {
        "Format": str,
        "DestinationArn": str,
    },
    total=False,
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
    "AwsApiGatewayEndpointConfigurationTypeDef",
    {
        "Types": List[str],
    },
    total=False,
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
        "ClientCertificateId": str,
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
    {
        "Name": str,
        "OId": str,
    },
    total=False,
)

AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": str,
    },
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
    {
        "Name": str,
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
    total=False,
)

AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {
        "Items": List["AwsCloudFrontDistributionCacheBehaviorTypeDef"],
    },
    total=False,
)

AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": str,
    },
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
    {
        "Bucket": str,
        "Enabled": bool,
        "IncludeCookies": bool,
        "Prefix": str,
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {
        "Items": List[int],
        "Quantity": int,
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {
        "StatusCodes": "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {
        "FailoverCriteria": "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    },
    total=False,
)

AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {
        "Items": List["AwsCloudFrontDistributionOriginGroupTypeDef"],
    },
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
    {
        "OriginAccessIdentity": str,
    },
    total=False,
)

AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": List["AwsCloudFrontDistributionOriginItemTypeDef"],
    },
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
    {
        "Credential": str,
        "CredentialProvider": str,
    },
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
    {
        "Type": str,
        "Location": str,
        "GitCloneDepth": int,
        "InsecureSsl": bool,
    },
    total=False,
)

AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {
        "VpcId": str,
        "Subnets": List[str],
        "SecurityGroupIds": List[str],
    },
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
    {
        "AttributeName": str,
        "AttributeType": str,
    },
    total=False,
)

AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {
        "BillingMode": str,
        "LastUpdateToPayPerRequestDateTime": str,
    },
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
    "AwsDynamoDbTableKeySchemaTypeDef",
    {
        "AttributeName": str,
        "KeyType": str,
    },
    total=False,
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
    {
        "NonKeyAttributes": List[str],
        "ProjectionType": str,
    },
    total=False,
)

AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
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
    {
        "InaccessibleEncryptionDateTime": str,
        "Status": str,
        "SseType": str,
        "KmsMasterKeyArn": str,
    },
    total=False,
)

AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": str,
    },
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
        "NetworkInterfaces": List["AwsEc2InstanceNetworkInterfacesDetailsTypeDef"],
    },
    total=False,
)

AwsEc2InstanceNetworkInterfacesDetailsTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    {
        "NetworkInterfaceId": str,
    },
    total=False,
)

AwsEc2NetworkAclAssociationTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": str,
        "NetworkAclId": str,
        "SubnetId": str,
    },
    total=False,
)

AwsEc2NetworkAclDetailsTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsTypeDef",
    {
        "IsDefault": bool,
        "NetworkAclId": str,
        "OwnerId": str,
        "VpcId": str,
        "Associations": List["AwsEc2NetworkAclAssociationTypeDef"],
        "Entries": List["AwsEc2NetworkAclEntryTypeDef"],
    },
    total=False,
)

AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeFromToTypeDef",
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
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
        "IpV6Addresses": List["AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef"],
        "PrivateIpAddresses": List["AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef"],
        "PublicDnsName": str,
        "PublicIp": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    {
        "IpV6Address": str,
    },
    total=False,
)

AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    {
        "PrivateIpAddress": str,
        "PrivateDnsName": str,
    },
    total=False,
)

AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
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
    "AwsEc2SecurityGroupIpRangeTypeDef",
    {
        "CidrIp": str,
    },
    total=False,
)

AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    {
        "CidrIpv6": str,
    },
    total=False,
)

AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    {
        "PrefixListId": str,
    },
    total=False,
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

AwsEc2SubnetDetailsTypeDef = TypedDict(
    "AwsEc2SubnetDetailsTypeDef",
    {
        "AssignIpv6AddressOnCreation": bool,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "MapPublicIpOnLaunch": bool,
        "OwnerId": str,
        "State": str,
        "SubnetArn": str,
        "SubnetId": str,
        "VpcId": str,
        "Ipv6CidrBlockAssociationSet": List["Ipv6CidrBlockAssociationTypeDef"],
    },
    total=False,
)

AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {
        "AttachTime": str,
        "DeleteOnTermination": bool,
        "InstanceId": str,
        "Status": str,
    },
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

AwsEcsClusterClusterSettingsDetailsTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsClusterConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsTypeDef",
    {
        "ExecuteCommandConfiguration": "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    },
    total=False,
)

AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    {
        "KmsKeyId": str,
        "LogConfiguration": "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
        "Logging": str,
    },
    total=False,
)

AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    {
        "CloudWatchEncryptionEnabled": bool,
        "CloudWatchLogGroupName": str,
        "S3BucketName": str,
        "S3EncryptionEnabled": bool,
        "S3KeyPrefix": str,
    },
    total=False,
)

AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
    total=False,
)

AwsEcsClusterDetailsTypeDef = TypedDict(
    "AwsEcsClusterDetailsTypeDef",
    {
        "CapacityProviders": List[str],
        "ClusterSettings": List["AwsEcsClusterClusterSettingsDetailsTypeDef"],
        "Configuration": "AwsEcsClusterConfigurationDetailsTypeDef",
        "DefaultCapacityProviderStrategy": List[
            "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef"
        ],
    },
    total=False,
)

AwsEcsServiceCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": int,
        "CapacityProvider": str,
        "Weight": int,
    },
    total=False,
)

AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    {
        "Enable": bool,
        "Rollback": bool,
    },
    total=False,
)

AwsEcsServiceDeploymentConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    {
        "DeploymentCircuitBreaker": "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
        "MaximumPercent": int,
        "MinimumHealthyPercent": int,
    },
    total=False,
)

AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": str,
    },
    total=False,
)

AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": List["AwsEcsServiceCapacityProviderStrategyDetailsTypeDef"],
        "Cluster": str,
        "DeploymentConfiguration": "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
        "DeploymentController": "AwsEcsServiceDeploymentControllerDetailsTypeDef",
        "DesiredCount": int,
        "EnableEcsManagedTags": bool,
        "EnableExecuteCommand": bool,
        "HealthCheckGracePeriodSeconds": int,
        "LaunchType": str,
        "LoadBalancers": List["AwsEcsServiceLoadBalancersDetailsTypeDef"],
        "Name": str,
        "NetworkConfiguration": "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
        "PlacementConstraints": List["AwsEcsServicePlacementConstraintsDetailsTypeDef"],
        "PlacementStrategies": List["AwsEcsServicePlacementStrategiesDetailsTypeDef"],
        "PlatformVersion": str,
        "PropagateTags": str,
        "Role": str,
        "SchedulingStrategy": str,
        "ServiceArn": str,
        "ServiceName": str,
        "ServiceRegistries": List["AwsEcsServiceServiceRegistriesDetailsTypeDef"],
        "TaskDefinition": str,
    },
    total=False,
)

AwsEcsServiceLoadBalancersDetailsTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "LoadBalancerName": str,
        "TargetGroupArn": str,
    },
    total=False,
)

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    {
        "AssignPublicIp": str,
        "SecurityGroups": List[str],
        "Subnets": List[str],
    },
    total=False,
)

AwsEcsServiceNetworkConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    {
        "AwsVpcConfiguration": "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    },
    total=False,
)

AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
    total=False,
)

AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": str,
        "Type": str,
    },
    total=False,
)

AwsEcsServiceServiceRegistriesDetailsTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    {
        "ContainerName": str,
        "ContainerPort": int,
        "Port": int,
        "RegistryArn": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    {
        "Condition": str,
        "ContainerName": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    {
        "Command": List[str],
        "Cpu": int,
        "DependsOn": List["AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef"],
        "DisableNetworking": bool,
        "DnsSearchDomains": List[str],
        "DnsServers": List[str],
        "DockerLabels": Dict[str, str],
        "DockerSecurityOptions": List[str],
        "EntryPoint": List[str],
        "Environment": List["AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef"],
        "EnvironmentFiles": List[
            "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef"
        ],
        "Essential": bool,
        "ExtraHosts": List["AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef"],
        "FirelensConfiguration": "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
        "HealthCheck": "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
        "Hostname": str,
        "Image": str,
        "Interactive": bool,
        "Links": List[str],
        "LinuxParameters": "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
        "LogConfiguration": "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
        "Memory": int,
        "MemoryReservation": int,
        "MountPoints": List["AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef"],
        "Name": str,
        "PortMappings": List["AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef"],
        "Privileged": bool,
        "PseudoTerminal": bool,
        "ReadonlyRootFilesystem": bool,
        "RepositoryCredentials": "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
        "ResourceRequirements": List[
            "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef"
        ],
        "Secrets": List["AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef"],
        "StartTimeout": int,
        "StopTimeout": int,
        "SystemControls": List[
            "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef"
        ],
        "Ulimits": List["AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef"],
        "User": str,
        "VolumesFrom": List["AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef"],
        "WorkingDirectory": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    {
        "Hostname": str,
        "IpAddress": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": Dict[str, str],
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    {
        "Command": List[str],
        "Interval": int,
        "Retries": int,
        "StartPeriod": int,
        "Timeout": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    {
        "Add": List[str],
        "Drop": List[str],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    {
        "Capabilities": "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
        "Devices": List[
            "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef"
        ],
        "InitProcessEnabled": bool,
        "MaxSwap": int,
        "SharedMemorySize": int,
        "Swappiness": int,
        "Tmpfs": List["AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef"],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    {
        "ContainerPath": str,
        "HostPath": str,
        "Permissions": List[str],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    {
        "ContainerPath": str,
        "MountOptions": List[str],
        "Size": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    {
        "LogDriver": str,
        "Options": Dict[str, str],
        "SecretOptions": List[
            "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef"
        ],
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    {
        "Name": str,
        "ValueFrom": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": str,
        "ReadOnly": bool,
        "SourceVolume": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": int,
        "HostPort": int,
        "Protocol": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    {
        "CredentialsParameter": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    {
        "Name": str,
        "ValueFrom": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    {
        "Namespace": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    {
        "HardLimit": int,
        "Name": str,
        "SoftLimit": int,
    },
    total=False,
)

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": bool,
        "SourceContainer": str,
    },
    total=False,
)

AwsEcsTaskDefinitionDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsTypeDef",
    {
        "ContainerDefinitions": List["AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef"],
        "Cpu": str,
        "ExecutionRoleArn": str,
        "Family": str,
        "InferenceAccelerators": List["AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef"],
        "IpcMode": str,
        "Memory": str,
        "NetworkMode": str,
        "PidMode": str,
        "PlacementConstraints": List["AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef"],
        "ProxyConfiguration": "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
        "RequiresCompatibilities": List[str],
        "TaskRoleArn": str,
        "Volumes": List["AwsEcsTaskDefinitionVolumesDetailsTypeDef"],
    },
    total=False,
)

AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    {
        "DeviceName": str,
        "DeviceType": str,
    },
    total=False,
)

AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": str,
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": str,
        "ProxyConfigurationProperties": List[
            "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef"
        ],
        "Type": str,
    },
    total=False,
)

AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    {
        "DockerVolumeConfiguration": "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
        "EfsVolumeConfiguration": "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
        "Host": "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
        "Name": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    {
        "Autoprovision": bool,
        "Driver": str,
        "DriverOpts": Dict[str, str],
        "Labels": Dict[str, str],
        "Scope": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    {
        "AccessPointId": str,
        "Iam": str,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    {
        "AuthorizationConfig": "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
        "FilesystemId": str,
        "RootDirectory": str,
        "TransitEncryption": str,
        "TransitEncryptionPort": int,
    },
    total=False,
)

AwsEcsTaskDefinitionVolumesHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    {
        "SourcePath": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentDetailsTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    {
        "ApplicationName": str,
        "Cname": str,
        "DateCreated": str,
        "DateUpdated": str,
        "Description": str,
        "EndpointUrl": str,
        "EnvironmentArn": str,
        "EnvironmentId": str,
        "EnvironmentLinks": List["AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef"],
        "EnvironmentName": str,
        "OptionSettings": List["AwsElasticBeanstalkEnvironmentOptionSettingTypeDef"],
        "PlatformArn": str,
        "SolutionStackName": str,
        "Status": str,
        "Tier": "AwsElasticBeanstalkEnvironmentTierTypeDef",
        "VersionLabel": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    {
        "EnvironmentName": str,
        "LinkName": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentOptionSettingTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    {
        "Namespace": str,
        "OptionName": str,
        "ResourceName": str,
        "Value": str,
    },
    total=False,
)

AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": str,
        "Type": str,
        "Version": str,
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
        "ElasticsearchClusterConfig": "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
        "EncryptionAtRestOptions": "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
        "LogPublishingOptions": "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
        "ServiceSoftwareOptions": "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
        "VPCOptions": "AwsElasticsearchDomainVPCOptionsTypeDef",
    },
    total=False,
)

AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": str,
    },
    total=False,
)

AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    {
        "DedicatedMasterCount": int,
        "DedicatedMasterEnabled": bool,
        "DedicatedMasterType": str,
        "InstanceCount": int,
        "InstanceType": str,
        "ZoneAwarenessConfig": "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
        "ZoneAwarenessEnabled": bool,
    },
    total=False,
)

AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)

AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
    total=False,
)

AwsElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    {
        "IndexSlowLogs": "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
        "SearchSlowLogs": "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
        "AuditLogs": "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    },
    total=False,
)

AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AwsElasticsearchDomainServiceSoftwareOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    {
        "AutomatedUpdateDate": str,
        "Cancellable": bool,
        "CurrentVersion": str,
        "Description": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "UpdateStatus": str,
    },
    total=False,
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
    "AwsElbAppCookieStickinessPolicyTypeDef",
    {
        "CookieName": str,
        "PolicyName": str,
    },
    total=False,
)

AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {
        "CookieExpirationPeriod": int,
        "PolicyName": str,
    },
    total=False,
)

AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {
        "EmitInterval": int,
        "Enabled": bool,
        "S3BucketName": str,
        "S3BucketPrefix": str,
    },
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
    {
        "InstancePort": int,
        "PolicyNames": List[str],
    },
    total=False,
)

AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    {
        "Enabled": bool,
        "Timeout": int,
    },
    total=False,
)

AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
    total=False,
)

AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
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
    "AwsElbLoadBalancerInstanceTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {
        "Listener": "AwsElbLoadBalancerListenerTypeDef",
        "PolicyNames": List[str],
    },
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
    {
        "GroupName": str,
        "OwnerAlias": str,
    },
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
        "Status": AwsIamAccessKeyStatusType,
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
    {
        "MfaAuthenticated": bool,
        "CreationDate": str,
    },
    total=False,
)

AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": str,
        "PrincipalId": str,
        "Arn": str,
        "AccountId": str,
        "UserName": str,
    },
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
    "AwsIamAttachedManagedPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyArn": str,
    },
    total=False,
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

AwsIamGroupPolicyTypeDef = TypedDict(
    "AwsIamGroupPolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

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
    {
        "PermissionsBoundaryArn": str,
        "PermissionsBoundaryType": str,
    },
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
    {
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": str,
    },
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

AwsIamRolePolicyTypeDef = TypedDict(
    "AwsIamRolePolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

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

AwsIamUserPolicyTypeDef = TypedDict(
    "AwsIamUserPolicyTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

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
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ZipFile": str,
    },
    total=False,
)

AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    {
        "TargetArn": str,
    },
    total=False,
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
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": "AwsLambdaFunctionEnvironmentErrorTypeDef",
    },
    total=False,
)

AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef",
    {
        "Arn": str,
        "CodeSize": int,
    },
    total=False,
)

AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef",
    {
        "Mode": str,
    },
    total=False,
)

AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VpcId": str,
    },
    total=False,
)

AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {
        "Version": int,
        "CompatibleRuntimes": List[str],
        "CreatedDate": str,
    },
    total=False,
)

AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    {
        "RoleArn": str,
        "Status": str,
    },
    total=False,
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
    {
        "DbClusterOptionGroupName": str,
        "Status": str,
    },
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
    {
        "Domain": str,
        "Status": str,
        "Fqdn": str,
        "IamRoleName": str,
    },
    total=False,
)

AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {
        "RoleArn": str,
        "FeatureName": str,
        "Status": str,
    },
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
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
    total=False,
)

AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {
        "DbParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
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
    "AwsRdsDbProcessorFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
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
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
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

AwsRdsEventSubscriptionDetailsTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsTypeDef",
    {
        "CustSubscriptionId": str,
        "CustomerAwsId": str,
        "Enabled": bool,
        "EventCategoriesList": List[str],
        "EventSubscriptionArn": str,
        "SnsTopicArn": str,
        "SourceIdsList": List[str],
        "SourceType": str,
        "Status": str,
        "SubscriptionCreationTime": str,
    },
    total=False,
)

AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": List[str],
        "LogTypesToDisable": List[str],
    },
    total=False,
)

AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {
        "NodeRole": str,
        "PrivateIpAddress": str,
        "PublicIpAddress": str,
    },
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
    {
        "ParameterName": str,
        "ParameterApplyStatus": str,
        "ParameterApplyErrorDescription": str,
    },
    total=False,
)

AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Status": str,
    },
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
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    {
        "ElasticIp": str,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "Status": str,
    },
    total=False,
)

AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef",
    {
        "ApplyStatus": str,
        "IamRoleArn": str,
    },
    total=False,
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
    {
        "AllowCancelResize": bool,
        "ResizeType": str,
    },
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
    {
        "Status": str,
        "VpcSecurityGroupId": str,
    },
    total=False,
)

AwsS3AccountPublicAccessBlockDetailsTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    {
        "BlockPublicAcls": bool,
        "BlockPublicPolicy": bool,
        "IgnorePublicAcls": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    {
        "Rules": List["AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef"],
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef = (
    TypedDict(
        "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        {
            "DaysAfterInitiation": int,
        },
        total=False,
    )
)

AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    {
        "AbortIncompleteMultipartUpload": "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        "ExpirationDate": str,
        "ExpirationInDays": int,
        "ExpiredObjectDeleteMarker": bool,
        "Filter": "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
        "ID": str,
        "NoncurrentVersionExpirationInDays": int,
        "NoncurrentVersionTransitions": List[
            "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef"
        ],
        "Prefix": str,
        "Status": str,
        "Transitions": List[
            "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef"
        ],
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    {
        "Predicate": "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": List[
            "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef"
        ],
        "Prefix": str,
        "Tag": "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
        "Type": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": str,
        "Tag": "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
        "Type": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    {
        "Days": int,
        "StorageClass": str,
    },
    total=False,
)

AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    {
        "Date": str,
        "Days": int,
        "StorageClass": str,
    },
    total=False,
)

AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": str,
        "OwnerName": str,
        "CreatedAt": str,
        "ServerSideEncryptionConfiguration": "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
        "BucketLifecycleConfiguration": "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
        "PublicAccessBlockConfiguration": "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    },
    total=False,
)

AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": str,
        "KMSMasterKeyID": str,
    },
    total=False,
)

AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": List["AwsS3BucketServerSideEncryptionRuleTypeDef"],
    },
    total=False,
)

AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    },
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
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    {
        "AutomaticallyAfterDays": int,
    },
    total=False,
)

AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": List["StringFilterTypeDef"],
        "AwsAccountId": List["StringFilterTypeDef"],
        "Id": List["StringFilterTypeDef"],
        "GeneratorId": List["StringFilterTypeDef"],
        "Region": List["StringFilterTypeDef"],
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
        "ResourceAwsIamAccessKeyPrincipalName": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyStatus": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyCreatedAt": List["DateFilterTypeDef"],
        "ResourceAwsIamUserUserName": List["StringFilterTypeDef"],
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
        "FindingProviderFieldsConfidence": List["NumberFilterTypeDef"],
        "FindingProviderFieldsCriticality": List["NumberFilterTypeDef"],
        "FindingProviderFieldsRelatedFindingsId": List["StringFilterTypeDef"],
        "FindingProviderFieldsRelatedFindingsProductArn": List["StringFilterTypeDef"],
        "FindingProviderFieldsSeverityLabel": List["StringFilterTypeDef"],
        "FindingProviderFieldsSeverityOriginal": List["StringFilterTypeDef"],
        "FindingProviderFieldsTypes": List["StringFilterTypeDef"],
    },
    total=False,
)

AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)

_RequiredAwsSecurityFindingTypeDef = TypedDict(
    "_RequiredAwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": List["ResourceTypeDef"],
    },
)
_OptionalAwsSecurityFindingTypeDef = TypedDict(
    "_OptionalAwsSecurityFindingTypeDef",
    {
        "ProductName": str,
        "CompanyName": str,
        "Region": str,
        "Types": List[str],
        "FirstObservedAt": str,
        "LastObservedAt": str,
        "Severity": "SeverityTypeDef",
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
        "VerificationState": VerificationStateType,
        "WorkflowState": WorkflowStateType,
        "Workflow": "WorkflowTypeDef",
        "RecordState": RecordStateType,
        "RelatedFindings": List["RelatedFindingTypeDef"],
        "Note": "NoteTypeDef",
        "Vulnerabilities": List["VulnerabilityTypeDef"],
        "PatchSummary": "PatchSummaryTypeDef",
        "Action": "ActionTypeDef",
        "FindingProviderFields": "FindingProviderFieldsTypeDef",
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
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": str,
        "Protocol": str,
    },
    total=False,
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

AwsSsmComplianceSummaryTypeDef = TypedDict(
    "AwsSsmComplianceSummaryTypeDef",
    {
        "Status": str,
        "CompliantCriticalCount": int,
        "CompliantHighCount": int,
        "CompliantMediumCount": int,
        "ExecutionType": str,
        "NonCompliantCriticalCount": int,
        "CompliantInformationalCount": int,
        "NonCompliantInformationalCount": int,
        "CompliantUnspecifiedCount": int,
        "NonCompliantLowCount": int,
        "NonCompliantHighCount": int,
        "CompliantLowCount": int,
        "ComplianceType": str,
        "PatchBaselineId": str,
        "OverallSeverity": str,
        "NonCompliantMediumCount": int,
        "NonCompliantUnspecifiedCount": int,
        "PatchGroup": str,
    },
    total=False,
)

AwsSsmPatchComplianceDetailsTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsTypeDef",
    {
        "Patch": "AwsSsmPatchTypeDef",
    },
    total=False,
)

AwsSsmPatchTypeDef = TypedDict(
    "AwsSsmPatchTypeDef",
    {
        "ComplianceSummary": "AwsSsmComplianceSummaryTypeDef",
    },
    total=False,
)

AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {
        "Name": str,
        "DefaultAction": str,
        "Rules": List["AwsWafWebAclRuleTypeDef"],
        "WebAclId": str,
    },
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

BatchDisableStandardsRequestRequestTypeDef = TypedDict(
    "BatchDisableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": List[str],
    },
)

BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEnableStandardsRequestRequestTypeDef = TypedDict(
    "BatchEnableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionRequests": List["StandardsSubscriptionRequestTypeDef"],
    },
)

BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchImportFindingsRequestRequestTypeDef = TypedDict(
    "BatchImportFindingsRequestRequestTypeDef",
    {
        "Findings": List["AwsSecurityFindingTypeDef"],
    },
)

BatchImportFindingsResponseTypeDef = TypedDict(
    "BatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List["ImportFindingsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateFindingsRequestRequestTypeDef",
    {
        "FindingIdentifiers": List["AwsSecurityFindingIdentifierTypeDef"],
    },
)
_OptionalBatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateFindingsRequestRequestTypeDef",
    {
        "Note": "NoteUpdateTypeDef",
        "Severity": "SeverityUpdateTypeDef",
        "VerificationState": VerificationStateType,
        "Confidence": int,
        "Criticality": int,
        "Types": List[str],
        "UserDefinedFields": Dict[str, str],
        "Workflow": "WorkflowUpdateTypeDef",
        "RelatedFindings": List["RelatedFindingTypeDef"],
    },
    total=False,
)

class BatchUpdateFindingsRequestRequestTypeDef(
    _RequiredBatchUpdateFindingsRequestRequestTypeDef,
    _OptionalBatchUpdateFindingsRequestRequestTypeDef,
):
    pass

BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List["AwsSecurityFindingIdentifierTypeDef"],
        "UnprocessedFindings": List["BatchUpdateFindingsUnprocessedFindingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": "AwsSecurityFindingIdentifierTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "Column": int,
        "Row": int,
        "ColumnName": str,
        "CellReference": str,
    },
    total=False,
)

CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "CidrBlock": str,
        "CidrBlockState": str,
    },
    total=False,
)

CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": str,
    },
    total=False,
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "MimeType": str,
        "SizeClassified": int,
        "AdditionalOccurrences": bool,
        "Status": "ClassificationStatusTypeDef",
        "SensitiveData": List["SensitiveDataResultTypeDef"],
        "CustomDataIdentifiers": "CustomDataIdentifiersResultTypeDef",
    },
    total=False,
)

ClassificationStatusTypeDef = TypedDict(
    "ClassificationStatusTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": ComplianceStatusType,
        "RelatedRequirements": List[str],
        "StatusReasons": List["StatusReasonTypeDef"],
    },
    total=False,
)

ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {
        "Name": str,
        "ImageId": str,
        "ImageName": str,
        "LaunchedAt": str,
    },
    total=False,
)

CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": str,
        "CountryName": str,
    },
    total=False,
)

CreateActionTargetRequestRequestTypeDef = TypedDict(
    "CreateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Id": str,
    },
)

CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInsightRequestRequestTypeDef = TypedDict(
    "CreateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "GroupByAttribute": str,
    },
)

CreateInsightResponseTypeDef = TypedDict(
    "CreateInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "AccountDetails": List["AccountDetailsTypeDef"],
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDataIdentifiersDetectionsTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsTypeDef",
    {
        "Count": int,
        "Arn": str,
        "Name": str,
        "Occurrences": "OccurrencesTypeDef",
    },
    total=False,
)

CustomDataIdentifiersResultTypeDef = TypedDict(
    "CustomDataIdentifiersResultTypeDef",
    {
        "Detections": List["CustomDataIdentifiersDetectionsTypeDef"],
        "TotalCount": int,
    },
    total=False,
)

CvssTypeDef = TypedDict(
    "CvssTypeDef",
    {
        "Version": str,
        "BaseScore": float,
        "BaseVector": str,
    },
    total=False,
)

DataClassificationDetailsTypeDef = TypedDict(
    "DataClassificationDetailsTypeDef",
    {
        "DetailedResultsLocation": str,
        "Result": "ClassificationResultTypeDef",
    },
    total=False,
)

DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "Start": str,
        "End": str,
        "DateRange": "DateRangeTypeDef",
    },
    total=False,
)

DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
    total=False,
)

DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActionTargetRequestRequestTypeDef = TypedDict(
    "DeleteActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)

DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

DeleteInsightResponseTypeDef = TypedDict(
    "DeleteInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeActionTargetsRequestRequestTypeDef",
    {
        "ActionTargetArns": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeActionTargetsResponseTypeDef = TypedDict(
    "DescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List["ActionTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubArn": str,
    },
    total=False,
)

DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubArn": str,
        "SubscribedAt": str,
        "AutoEnableControls": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductsRequestRequestTypeDef = TypedDict(
    "DescribeProductsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ProductArn": str,
    },
    total=False,
)

DescribeProductsResponseTypeDef = TypedDict(
    "DescribeProductsResponseTypeDef",
    {
        "Products": List["ProductTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStandardsControlsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArn": str,
    },
)
_OptionalDescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStandardsControlsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeStandardsControlsRequestRequestTypeDef(
    _RequiredDescribeStandardsControlsRequestRequestTypeDef,
    _OptionalDescribeStandardsControlsRequestRequestTypeDef,
):
    pass

DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {
        "Controls": List["StandardsControlTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStandardsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {
        "Standards": List["StandardTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "DisableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductSubscriptionArn": str,
    },
)

DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": str,
        "Protocol": str,
        "Blocked": bool,
    },
    total=False,
)

EnableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "EnableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductArn": str,
    },
)

EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef",
    {
        "ProductSubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)

EnableSecurityHubRequestRequestTypeDef = TypedDict(
    "EnableSecurityHubRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "EnableDefaultStandards": bool,
    },
    total=False,
)

FindingProviderFieldsTypeDef = TypedDict(
    "FindingProviderFieldsTypeDef",
    {
        "Confidence": int,
        "Criticality": int,
        "RelatedFindings": List["RelatedFindingTypeDef"],
        "Severity": "FindingProviderSeverityTypeDef",
        "Types": List[str],
    },
    total=False,
)

FindingProviderSeverityTypeDef = TypedDict(
    "FindingProviderSeverityTypeDef",
    {
        "Label": SeverityLabelType,
        "Original": str,
    },
    total=False,
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lon": float,
        "Lat": float,
    },
    total=False,
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnabledStandardsRequestRequestTypeDef = TypedDict(
    "GetEnabledStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List["StandardsSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "SortCriteria": List["SortCriterionTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List["AwsSecurityFindingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightResultsRequestRequestTypeDef = TypedDict(
    "GetInsightResultsRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)

GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef",
    {
        "InsightResults": "InsightResultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightsRequestRequestTypeDef = TypedDict(
    "GetInsightsRequestRequestTypeDef",
    {
        "InsightArns": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "Insights": List["InsightTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": "InvitationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": int,
        "Type": int,
    },
    total=False,
)

ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef",
    {
        "GroupByAttributeValue": str,
        "Count": int,
    },
)

InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List["InsightResultValueTypeDef"],
    },
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
    {
        "AccountId": str,
        "InvitationId": str,
        "InvitedAt": datetime,
        "MemberStatus": str,
    },
    total=False,
)

InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "AccountIds": List[str],
    },
)

InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List["ResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpFilterTypeDef = TypedDict(
    "IpFilterTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

IpOrganizationDetailsTypeDef = TypedDict(
    "IpOrganizationDetailsTypeDef",
    {
        "Asn": int,
        "AsnOrg": str,
        "Isp": str,
        "Org": str,
    },
    total=False,
)

Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "CidrBlockState": str,
    },
    total=False,
)

KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)

ListEnabledProductsForImportRequestRequestTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {
        "ProductSubscriptions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "OnlyAssociated": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List["MemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List["AdminAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": str,
        "Reason": str,
    },
    total=False,
)

_RequiredMalwareTypeDef = TypedDict(
    "_RequiredMalwareTypeDef",
    {
        "Name": str,
    },
)
_OptionalMalwareTypeDef = TypedDict(
    "_OptionalMalwareTypeDef",
    {
        "Type": MalwareTypeType,
        "Path": str,
        "State": MalwareStateType,
    },
    total=False,
)

class MalwareTypeDef(_RequiredMalwareTypeDef, _OptionalMalwareTypeDef):
    pass

MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparison": MapFilterComparisonType,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": str,
        "Email": str,
        "MasterId": str,
        "AdministratorId": str,
        "MemberStatus": str,
        "InvitedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": str,
        "RemoteIpDetails": "ActionRemoteIpDetailsTypeDef",
        "RemotePortDetails": "ActionRemotePortDetailsTypeDef",
        "LocalPortDetails": "ActionLocalPortDetailsTypeDef",
        "Protocol": str,
        "Blocked": bool,
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
    {
        "Address": List[str],
        "PortRanges": List["PortRangeTypeDef"],
    },
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
        "Direction": NetworkDirectionType,
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

NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)

NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)

NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "Gte": float,
        "Lte": float,
        "Eq": float,
    },
    total=False,
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "LineRanges": List["RangeTypeDef"],
        "OffsetRanges": List["RangeTypeDef"],
        "Pages": List["PageTypeDef"],
        "Records": List["RecordTypeDef"],
        "Cells": List["CellTypeDef"],
    },
    total=False,
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageNumber": int,
        "LineRange": "RangeTypeDef",
        "OffsetRange": "RangeTypeDef",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPatchSummaryTypeDef = TypedDict(
    "_RequiredPatchSummaryTypeDef",
    {
        "Id": str,
    },
)
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

PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "PortProbeDetails": List["PortProbeDetailTypeDef"],
        "Blocked": bool,
    },
    total=False,
)

PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": "ActionLocalPortDetailsTypeDef",
        "LocalIpDetails": "ActionLocalIpDetailsTypeDef",
        "RemoteIpDetails": "ActionRemoteIpDetailsTypeDef",
    },
    total=False,
)

PortRangeFromToTypeDef = TypedDict(
    "PortRangeFromToTypeDef",
    {
        "From": int,
        "To": int,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "Begin": int,
        "End": int,
    },
    total=False,
)

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

_RequiredProductTypeDef = TypedDict(
    "_RequiredProductTypeDef",
    {
        "ProductArn": str,
    },
)
_OptionalProductTypeDef = TypedDict(
    "_OptionalProductTypeDef",
    {
        "ProductName": str,
        "CompanyName": str,
        "Description": str,
        "Categories": List[str],
        "IntegrationTypes": List[IntegrationTypeType],
        "MarketplaceUrl": str,
        "ActivationUrl": str,
        "ProductSubscriptionResourcePolicy": str,
    },
    total=False,
)

class ProductTypeDef(_RequiredProductTypeDef, _OptionalProductTypeDef):
    pass

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Start": int,
        "End": int,
        "StartColumn": int,
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": str,
        "Url": str,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "JsonPath": str,
        "RecordIndex": int,
    },
    total=False,
)

RelatedFindingTypeDef = TypedDict(
    "RelatedFindingTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "Recommendation": "RecommendationTypeDef",
    },
    total=False,
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
        "AwsEc2Subnet": "AwsEc2SubnetDetailsTypeDef",
        "AwsEc2NetworkAcl": "AwsEc2NetworkAclDetailsTypeDef",
        "AwsElbv2LoadBalancer": "AwsElbv2LoadBalancerDetailsTypeDef",
        "AwsElasticBeanstalkEnvironment": "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
        "AwsElasticsearchDomain": "AwsElasticsearchDomainDetailsTypeDef",
        "AwsS3Bucket": "AwsS3BucketDetailsTypeDef",
        "AwsS3AccountPublicAccessBlock": "AwsS3AccountPublicAccessBlockDetailsTypeDef",
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
        "AwsSsmPatchCompliance": "AwsSsmPatchComplianceDetailsTypeDef",
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
        "AwsEcsCluster": "AwsEcsClusterDetailsTypeDef",
        "AwsEcsTaskDefinition": "AwsEcsTaskDefinitionDetailsTypeDef",
        "Container": "ContainerDetailsTypeDef",
        "Other": Dict[str, str],
        "AwsRdsEventSubscription": "AwsRdsEventSubscriptionDetailsTypeDef",
        "AwsEcsService": "AwsEcsServiceDetailsTypeDef",
    },
    total=False,
)

_RequiredResourceTypeDef = TypedDict(
    "_RequiredResourceTypeDef",
    {
        "Type": str,
        "Id": str,
    },
)
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "Partition": PartitionType,
        "Region": str,
        "ResourceRole": str,
        "Tags": Dict[str, str],
        "DataClassification": "DataClassificationDetailsTypeDef",
        "Details": "ResourceDetailsTypeDef",
    },
    total=False,
)

class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "AccountId": str,
        "ProcessingResult": str,
    },
    total=False,
)

SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": int,
        "Type": str,
        "Occurrences": "OccurrencesTypeDef",
    },
    total=False,
)

SensitiveDataResultTypeDef = TypedDict(
    "SensitiveDataResultTypeDef",
    {
        "Category": str,
        "Detections": List["SensitiveDataDetectionsTypeDef"],
        "TotalCount": int,
    },
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": float,
        "Label": SeverityLabelType,
        "Normalized": int,
        "Original": str,
    },
    total=False,
)

SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": int,
        "Product": float,
        "Label": SeverityLabelType,
    },
    total=False,
)

SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {
        "Name": str,
        "Version": str,
        "Epoch": str,
        "Release": str,
        "Architecture": str,
    },
    total=False,
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "Field": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {
        "StandardsArn": str,
        "Name": str,
        "Description": str,
        "EnabledByDefault": bool,
    },
    total=False,
)

StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": ControlStatusType,
        "DisabledReason": str,
        "ControlStatusUpdatedAt": datetime,
        "ControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "RelatedRequirements": List[str],
    },
    total=False,
)

_RequiredStandardsSubscriptionRequestTypeDef = TypedDict(
    "_RequiredStandardsSubscriptionRequestTypeDef",
    {
        "StandardsArn": str,
    },
)
_OptionalStandardsSubscriptionRequestTypeDef = TypedDict(
    "_OptionalStandardsSubscriptionRequestTypeDef",
    {
        "StandardsInput": Dict[str, str],
    },
    total=False,
)

class StandardsSubscriptionRequestTypeDef(
    _RequiredStandardsSubscriptionRequestTypeDef, _OptionalStandardsSubscriptionRequestTypeDef
):
    pass

StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": StandardsStatusType,
    },
)

_RequiredStatusReasonTypeDef = TypedDict(
    "_RequiredStatusReasonTypeDef",
    {
        "ReasonCode": str,
    },
)
_OptionalStatusReasonTypeDef = TypedDict(
    "_OptionalStatusReasonTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class StatusReasonTypeDef(_RequiredStatusReasonTypeDef, _OptionalStatusReasonTypeDef):
    pass

StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": str,
        "Comparison": StringFilterComparisonType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": ThreatIntelIndicatorTypeType,
        "Value": str,
        "Category": ThreatIntelIndicatorCategoryType,
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateActionTargetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)
_OptionalUpdateActionTargetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateActionTargetRequestRequestTypeDef(
    _RequiredUpdateActionTargetRequestRequestTypeDef,
    _OptionalUpdateActionTargetRequestRequestTypeDef,
):
    pass

_RequiredUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFindingsRequestRequestTypeDef",
    {
        "Filters": "AwsSecurityFindingFiltersTypeDef",
    },
)
_OptionalUpdateFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFindingsRequestRequestTypeDef",
    {
        "Note": "NoteUpdateTypeDef",
        "RecordState": RecordStateType,
    },
    total=False,
)

class UpdateFindingsRequestRequestTypeDef(
    _RequiredUpdateFindingsRequestRequestTypeDef, _OptionalUpdateFindingsRequestRequestTypeDef
):
    pass

_RequiredUpdateInsightRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
_OptionalUpdateInsightRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": "AwsSecurityFindingFiltersTypeDef",
        "GroupByAttribute": str,
    },
    total=False,
)

class UpdateInsightRequestRequestTypeDef(
    _RequiredUpdateInsightRequestRequestTypeDef, _OptionalUpdateInsightRequestRequestTypeDef
):
    pass

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
    },
)

UpdateSecurityHubConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    {
        "AutoEnableControls": bool,
    },
    total=False,
)

_RequiredUpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStandardsControlRequestRequestTypeDef",
    {
        "StandardsControlArn": str,
    },
)
_OptionalUpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStandardsControlRequestRequestTypeDef",
    {
        "ControlStatus": ControlStatusType,
        "DisabledReason": str,
    },
    total=False,
)

class UpdateStandardsControlRequestRequestTypeDef(
    _RequiredUpdateStandardsControlRequestRequestTypeDef,
    _OptionalUpdateStandardsControlRequestRequestTypeDef,
):
    pass

_RequiredVulnerabilityTypeDef = TypedDict(
    "_RequiredVulnerabilityTypeDef",
    {
        "Id": str,
    },
)
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
    "_RequiredVulnerabilityVendorTypeDef",
    {
        "Name": str,
    },
)
_OptionalVulnerabilityVendorTypeDef = TypedDict(
    "_OptionalVulnerabilityVendorTypeDef",
    {
        "Url": str,
        "VendorSeverity": str,
        "VendorCreatedAt": str,
        "VendorUpdatedAt": str,
    },
    total=False,
)

class VulnerabilityVendorTypeDef(
    _RequiredVulnerabilityVendorTypeDef, _OptionalVulnerabilityVendorTypeDef
):
    pass

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": str,
    },
    total=False,
)

WafExcludedRuleTypeDef = TypedDict(
    "WafExcludedRuleTypeDef",
    {
        "RuleId": str,
    },
    total=False,
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": str,
    },
    total=False,
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Status": WorkflowStatusType,
    },
    total=False,
)

WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {
        "Status": WorkflowStatusType,
    },
    total=False,
)
