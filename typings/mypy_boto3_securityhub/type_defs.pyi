"""
Type annotations for securityhub service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AcceptAdministratorInvitationRequestTypeDef

    data: AcceptAdministratorInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActorSessionMfaStatusType,
    AdminStatusType,
    AssociationStatusType,
    AssociationTypeType,
    AutoEnableStandardsType,
    AwsIamAccessKeyStatusType,
    AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
    ComplianceStatusType,
    ConfigurationPolicyAssociationStatusType,
    ConnectionDirectionType,
    ControlFindingGeneratorType,
    ControlStatusType,
    FindingHistoryUpdateSourceTypeType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    OrganizationConfigurationConfigurationTypeType,
    OrganizationConfigurationStatusType,
    ParameterValueTypeType,
    PartitionType,
    RecordStateType,
    RegionAvailabilityStatusType,
    RuleStatusType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsControlsUpdatableType,
    StandardsStatusType,
    StatusReasonCodeType,
    StringFilterComparisonType,
    TargetTypeType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    UnprocessedErrorCodeType,
    UpdateStatusType,
    VerificationStateType,
    VulnerabilityExploitAvailableType,
    VulnerabilityFixAvailableType,
    WorkflowStateType,
    WorkflowStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptAdministratorInvitationRequestTypeDef",
    "AcceptInvitationRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "ActionOutputTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "ActionUnionTypeDef",
    "ActorSessionTypeDef",
    "ActorTypeDef",
    "ActorUserTypeDef",
    "AdjustmentTypeDef",
    "AdminAccountTypeDef",
    "AssociatedStandardTypeDef",
    "AssociationFiltersTypeDef",
    "AssociationSetDetailsTypeDef",
    "AssociationStateDetailsTypeDef",
    "AutomationRulesActionOutputTypeDef",
    "AutomationRulesActionTypeDef",
    "AutomationRulesActionUnionTypeDef",
    "AutomationRulesConfigTypeDef",
    "AutomationRulesFindingFieldsUpdateOutputTypeDef",
    "AutomationRulesFindingFieldsUpdateTypeDef",
    "AutomationRulesFindingFieldsUpdateUnionTypeDef",
    "AutomationRulesFindingFiltersOutputTypeDef",
    "AutomationRulesFindingFiltersTypeDef",
    "AutomationRulesFindingFiltersUnionTypeDef",
    "AutomationRulesMetadataTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsAmazonMqBrokerDetailsOutputTypeDef",
    "AwsAmazonMqBrokerDetailsTypeDef",
    "AwsAmazonMqBrokerDetailsUnionTypeDef",
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef",
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiCallActionOutputTypeDef",
    "AwsApiCallActionTypeDef",
    "AwsApiCallActionUnionTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsOutputTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayCanarySettingsUnionTypeDef",
    "AwsApiGatewayEndpointConfigurationOutputTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayEndpointConfigurationUnionTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsApiGatewayRestApiDetailsOutputTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayRestApiDetailsUnionTypeDef",
    "AwsApiGatewayStageDetailsOutputTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayStageDetailsUnionTypeDef",
    "AwsApiGatewayV2ApiDetailsOutputTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsUnionTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsApiGatewayV2StageDetailsOutputTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsApiGatewayV2StageDetailsUnionTypeDef",
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    "AwsAppSyncGraphQlApiDetailsOutputTypeDef",
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    "AwsAppSyncGraphQlApiDetailsUnionTypeDef",
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    "AwsAthenaWorkGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef",
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef",
    "AwsBackupBackupPlanDetailsOutputTypeDef",
    "AwsBackupBackupPlanDetailsTypeDef",
    "AwsBackupBackupPlanDetailsUnionTypeDef",
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    "AwsBackupBackupPlanRuleDetailsOutputTypeDef",
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    "AwsBackupBackupPlanRuleDetailsUnionTypeDef",
    "AwsBackupBackupVaultDetailsOutputTypeDef",
    "AwsBackupBackupVaultDetailsTypeDef",
    "AwsBackupBackupVaultDetailsUnionTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsOutputTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsUnionTypeDef",
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    "AwsBackupRecoveryPointDetailsTypeDef",
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsUnionTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFormationStackDetailsOutputTypeDef",
    "AwsCloudFormationStackDetailsTypeDef",
    "AwsCloudFormationStackDetailsUnionTypeDef",
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDetailsOutputTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsCloudFrontDistributionDetailsUnionTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCloudFrontDistributionOriginGroupUnionTypeDef",
    "AwsCloudFrontDistributionOriginGroupsOutputTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsCloudFrontDistributionOriginGroupsUnionTypeDef",
    "AwsCloudFrontDistributionOriginItemOutputTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginItemUnionTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef",
    "AwsCloudFrontDistributionOriginsOutputTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudFrontDistributionOriginsUnionTypeDef",
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCloudWatchAlarmDetailsOutputTypeDef",
    "AwsCloudWatchAlarmDetailsTypeDef",
    "AwsCloudWatchAlarmDetailsUnionTypeDef",
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    "AwsCodeBuildProjectDetailsOutputTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsCodeBuildProjectDetailsUnionTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectEnvironmentUnionTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigOutputTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCodeBuildProjectVpcConfigUnionTypeDef",
    "AwsCorsConfigurationOutputTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsCorsConfigurationUnionTypeDef",
    "AwsDmsEndpointDetailsTypeDef",
    "AwsDmsReplicationInstanceDetailsOutputTypeDef",
    "AwsDmsReplicationInstanceDetailsTypeDef",
    "AwsDmsReplicationInstanceDetailsUnionTypeDef",
    "AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef",
    "AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef",
    "AwsDmsReplicationTaskDetailsTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableDetailsOutputTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsDynamoDbTableDetailsUnionTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef",
    "AwsDynamoDbTableProjectionOutputTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProjectionUnionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaOutputTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsDynamoDbTableReplicaUnionTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointDetailsOutputTypeDef",
    "AwsEc2ClientVpnEndpointDetailsTypeDef",
    "AwsEc2ClientVpnEndpointDetailsUnionTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceDetailsOutputTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2InstanceDetailsUnionTypeDef",
    "AwsEc2InstanceMetadataOptionsTypeDef",
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    "AwsEc2LaunchTemplateDataDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDetailsOutputTypeDef",
    "AwsEc2LaunchTemplateDetailsTypeDef",
    "AwsEc2LaunchTemplateDetailsUnionTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "AwsEc2NetworkAclDetailsOutputTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2NetworkAclDetailsUnionTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceDetailsOutputTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2NetworkInterfaceDetailsUnionTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2RouteTableDetailsOutputTypeDef",
    "AwsEc2RouteTableDetailsTypeDef",
    "AwsEc2RouteTableDetailsUnionTypeDef",
    "AwsEc2SecurityGroupDetailsOutputTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2SecurityGroupDetailsUnionTypeDef",
    "AwsEc2SecurityGroupIpPermissionOutputTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupIpPermissionUnionTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2SubnetDetailsOutputTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2SubnetDetailsUnionTypeDef",
    "AwsEc2TransitGatewayDetailsOutputTypeDef",
    "AwsEc2TransitGatewayDetailsTypeDef",
    "AwsEc2TransitGatewayDetailsUnionTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "AwsEc2VolumeDetailsOutputTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VolumeDetailsUnionTypeDef",
    "AwsEc2VpcDetailsOutputTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEc2VpcDetailsUnionTypeDef",
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    "AwsEc2VpcEndpointServiceDetailsUnionTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsUnionTypeDef",
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef",
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    "AwsEc2VpnConnectionDetailsTypeDef",
    "AwsEc2VpnConnectionDetailsUnionTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsUnionTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    "AwsEcrContainerImageDetailsOutputTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcrContainerImageDetailsUnionTypeDef",
    "AwsEcrRepositoryDetailsTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsClusterDetailsOutputTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsClusterDetailsUnionTypeDef",
    "AwsEcsContainerDetailsOutputTypeDef",
    "AwsEcsContainerDetailsTypeDef",
    "AwsEcsContainerDetailsUnionTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceDetailsOutputTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsServiceDetailsUnionTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsEcsTaskDetailsOutputTypeDef",
    "AwsEcsTaskDetailsTypeDef",
    "AwsEcsTaskDetailsUnionTypeDef",
    "AwsEcsTaskVolumeDetailsTypeDef",
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    "AwsEfsAccessPointDetailsOutputTypeDef",
    "AwsEfsAccessPointDetailsTypeDef",
    "AwsEfsAccessPointDetailsUnionTypeDef",
    "AwsEfsAccessPointPosixUserDetailsOutputTypeDef",
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    "AwsEfsAccessPointPosixUserDetailsUnionTypeDef",
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    "AwsEksClusterDetailsOutputTypeDef",
    "AwsEksClusterDetailsTypeDef",
    "AwsEksClusterDetailsUnionTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef",
    "AwsEksClusterLoggingDetailsOutputTypeDef",
    "AwsEksClusterLoggingDetailsTypeDef",
    "AwsEksClusterLoggingDetailsUnionTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDetailsOutputTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElasticsearchDomainDetailsUnionTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsOutputTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsUnionTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    "AwsElbLoadBalancerAttributesOutputTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerAttributesUnionTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerDetailsOutputTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsElbLoadBalancerDetailsUnionTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerListenerDescriptionOutputTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbLoadBalancerListenerDescriptionUnionTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbLoadBalancerPoliciesOutputTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerPoliciesUnionTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbv2LoadBalancerAttributeTypeDef",
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsElbv2LoadBalancerDetailsUnionTypeDef",
    "AwsEventSchemasRegistryDetailsTypeDef",
    "AwsEventsEndpointDetailsOutputTypeDef",
    "AwsEventsEndpointDetailsTypeDef",
    "AwsEventsEndpointDetailsUnionTypeDef",
    "AwsEventsEndpointEventBusesDetailsTypeDef",
    "AwsEventsEndpointReplicationConfigDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef",
    "AwsEventsEventbusDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    "AwsGuardDutyDetectorDetailsOutputTypeDef",
    "AwsGuardDutyDetectorDetailsTypeDef",
    "AwsGuardDutyDetectorDetailsUnionTypeDef",
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupDetailsOutputTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamGroupDetailsUnionTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileOutputTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamInstanceProfileUnionTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyDetailsOutputTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamPolicyDetailsUnionTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRoleDetailsOutputTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsIamRoleDetailsUnionTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserDetailsOutputTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsIamUserDetailsUnionTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKinesisStreamDetailsTypeDef",
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionDetailsOutputTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsLambdaFunctionDetailsUnionTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionEnvironmentOutputTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionEnvironmentUnionTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigOutputTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaFunctionVpcConfigUnionTypeDef",
    "AwsLambdaLayerVersionDetailsOutputTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsLambdaLayerVersionDetailsUnionTypeDef",
    "AwsMountPointTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef",
    "AwsMskClusterClusterInfoDetailsOutputTypeDef",
    "AwsMskClusterClusterInfoDetailsTypeDef",
    "AwsMskClusterClusterInfoDetailsUnionTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef",
    "AwsMskClusterDetailsOutputTypeDef",
    "AwsMskClusterDetailsTypeDef",
    "AwsMskClusterDetailsUnionTypeDef",
    "AwsNetworkFirewallFirewallDetailsOutputTypeDef",
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    "AwsNetworkFirewallFirewallDetailsUnionTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsUnionTypeDef",
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    "AwsOpenSearchServiceDomainDetailsUnionTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterDetailsOutputTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterDetailsUnionTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef",
    "AwsRdsDbClusterSnapshotDetailsOutputTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbClusterSnapshotDetailsUnionTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceDetailsOutputTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsRdsDbInstanceDetailsUnionTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbPendingModifiedValuesOutputTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbPendingModifiedValuesUnionTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbSecurityGroupDetailsOutputTypeDef",
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    "AwsRdsDbSecurityGroupDetailsUnionTypeDef",
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    "AwsRdsDbSnapshotDetailsOutputTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbSnapshotDetailsUnionTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsDbSubnetGroupOutputTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRdsDbSubnetGroupUnionTypeDef",
    "AwsRdsEventSubscriptionDetailsOutputTypeDef",
    "AwsRdsEventSubscriptionDetailsTypeDef",
    "AwsRdsEventSubscriptionDetailsUnionTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsOutputTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsUnionTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterGroupOutputTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRedshiftClusterClusterParameterGroupUnionTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterDetailsOutputTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRedshiftClusterDetailsUnionTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterLoggingStatusTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsRoute53HostedZoneConfigDetailsTypeDef",
    "AwsRoute53HostedZoneDetailsOutputTypeDef",
    "AwsRoute53HostedZoneDetailsTypeDef",
    "AwsRoute53HostedZoneDetailsUnionTypeDef",
    "AwsRoute53HostedZoneObjectDetailsTypeDef",
    "AwsRoute53HostedZoneVpcDetailsTypeDef",
    "AwsRoute53QueryLoggingConfigDetailsTypeDef",
    "AwsS3AccessPointDetailsTypeDef",
    "AwsS3AccessPointVpcConfigurationDetailsTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    "AwsS3BucketDetailsOutputTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsS3BucketDetailsUnionTypeDef",
    "AwsS3BucketLoggingConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    "AwsS3BucketNotificationConfigurationDetailUnionTypeDef",
    "AwsS3BucketNotificationConfigurationFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    "AwsS3BucketNotificationConfigurationFilterUnionTypeDef",
    "AwsS3BucketNotificationConfigurationOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef",
    "AwsS3BucketNotificationConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationUnionTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    "AwsS3BucketObjectLockConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationOutputTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationTypeDef",
    "AwsS3BucketWebsiteConfigurationUnionTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSageMakerNotebookInstanceDetailsOutputTypeDef",
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    "AwsSageMakerNotebookInstanceDetailsUnionTypeDef",
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "AwsSecurityFindingFiltersOutputTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "AwsSecurityFindingFiltersUnionTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "AwsSecurityFindingOutputTypeDef",
    "AwsSecurityFindingTypeDef",
    "AwsSecurityFindingUnionTypeDef",
    "AwsSnsTopicDetailsOutputTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSnsTopicDetailsUnionTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineDetailsTypeDef",
    "AwsStepFunctionStateMachineDetailsUnionTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef",
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRateBasedRuleDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsUnionTypeDef",
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsOutputTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsUnionTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRuleDetailsOutputTypeDef",
    "AwsWafRegionalRuleDetailsTypeDef",
    "AwsWafRegionalRuleDetailsUnionTypeDef",
    "AwsWafRegionalRuleGroupDetailsOutputTypeDef",
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    "AwsWafRegionalRuleGroupDetailsUnionTypeDef",
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    "AwsWafRegionalWebAclDetailsOutputTypeDef",
    "AwsWafRegionalWebAclDetailsTypeDef",
    "AwsWafRegionalWebAclDetailsUnionTypeDef",
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    "AwsWafRuleDetailsOutputTypeDef",
    "AwsWafRuleDetailsTypeDef",
    "AwsWafRuleDetailsUnionTypeDef",
    "AwsWafRuleGroupDetailsOutputTypeDef",
    "AwsWafRuleGroupDetailsTypeDef",
    "AwsWafRuleGroupDetailsUnionTypeDef",
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    "AwsWafRuleGroupRulesDetailsTypeDef",
    "AwsWafRulePredicateListDetailsTypeDef",
    "AwsWafWebAclDetailsOutputTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafWebAclDetailsUnionTypeDef",
    "AwsWafWebAclRuleOutputTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsWafWebAclRuleUnionTypeDef",
    "AwsWafv2ActionAllowDetailsOutputTypeDef",
    "AwsWafv2ActionAllowDetailsTypeDef",
    "AwsWafv2ActionAllowDetailsUnionTypeDef",
    "AwsWafv2ActionBlockDetailsOutputTypeDef",
    "AwsWafv2ActionBlockDetailsTypeDef",
    "AwsWafv2ActionBlockDetailsUnionTypeDef",
    "AwsWafv2CustomHttpHeaderTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsOutputTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsUnionTypeDef",
    "AwsWafv2CustomResponseDetailsOutputTypeDef",
    "AwsWafv2CustomResponseDetailsTypeDef",
    "AwsWafv2CustomResponseDetailsUnionTypeDef",
    "AwsWafv2RuleGroupDetailsOutputTypeDef",
    "AwsWafv2RuleGroupDetailsTypeDef",
    "AwsWafv2RuleGroupDetailsUnionTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsOutputTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsUnionTypeDef",
    "AwsWafv2RulesActionCountDetailsOutputTypeDef",
    "AwsWafv2RulesActionCountDetailsTypeDef",
    "AwsWafv2RulesActionCountDetailsUnionTypeDef",
    "AwsWafv2RulesActionDetailsOutputTypeDef",
    "AwsWafv2RulesActionDetailsTypeDef",
    "AwsWafv2RulesActionDetailsUnionTypeDef",
    "AwsWafv2RulesDetailsOutputTypeDef",
    "AwsWafv2RulesDetailsTypeDef",
    "AwsWafv2RulesDetailsUnionTypeDef",
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    "AwsWafv2WebAclActionDetailsOutputTypeDef",
    "AwsWafv2WebAclActionDetailsTypeDef",
    "AwsWafv2WebAclActionDetailsUnionTypeDef",
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    "AwsWafv2WebAclDetailsOutputTypeDef",
    "AwsWafv2WebAclDetailsTypeDef",
    "AwsWafv2WebAclDetailsUnionTypeDef",
    "AwsXrayEncryptionConfigDetailsTypeDef",
    "BatchDeleteAutomationRulesRequestTypeDef",
    "BatchDeleteAutomationRulesResponseTypeDef",
    "BatchDisableStandardsRequestTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsRequestTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "BatchGetAutomationRulesRequestTypeDef",
    "BatchGetAutomationRulesResponseTypeDef",
    "BatchGetConfigurationPolicyAssociationsRequestTypeDef",
    "BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    "BatchGetSecurityControlsRequestTypeDef",
    "BatchGetSecurityControlsResponseTypeDef",
    "BatchGetStandardsControlAssociationsRequestTypeDef",
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    "BatchImportFindingsRequestTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateAutomationRulesRequestTypeDef",
    "BatchUpdateAutomationRulesResponseTypeDef",
    "BatchUpdateFindingsRequestTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "BatchUpdateStandardsControlAssociationsRequestTypeDef",
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    "BooleanConfigurationOptionsTypeDef",
    "BooleanFilterTypeDef",
    "CellTypeDef",
    "CidrBlockAssociationTypeDef",
    "CityTypeDef",
    "ClassificationResultOutputTypeDef",
    "ClassificationResultTypeDef",
    "ClassificationResultUnionTypeDef",
    "ClassificationStatusTypeDef",
    "CloudWatchLogsLogGroupArnConfigDetailsTypeDef",
    "CodeVulnerabilitiesFilePathTypeDef",
    "ComplianceOutputTypeDef",
    "ComplianceTypeDef",
    "ComplianceUnionTypeDef",
    "ConfigurationOptionsTypeDef",
    "ConfigurationPolicyAssociationSummaryTypeDef",
    "ConfigurationPolicyAssociationTypeDef",
    "ConfigurationPolicySummaryTypeDef",
    "ContainerDetailsOutputTypeDef",
    "ContainerDetailsTypeDef",
    "ContainerDetailsUnionTypeDef",
    "CountryTypeDef",
    "CreateActionTargetRequestTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateAutomationRuleRequestTypeDef",
    "CreateAutomationRuleResponseTypeDef",
    "CreateConfigurationPolicyRequestTypeDef",
    "CreateConfigurationPolicyResponseTypeDef",
    "CreateFindingAggregatorRequestTypeDef",
    "CreateFindingAggregatorResponseTypeDef",
    "CreateInsightRequestTypeDef",
    "CreateInsightResponseTypeDef",
    "CreateMembersRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "CustomDataIdentifiersDetectionsOutputTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "CustomDataIdentifiersDetectionsUnionTypeDef",
    "CustomDataIdentifiersResultOutputTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "CustomDataIdentifiersResultUnionTypeDef",
    "CvssOutputTypeDef",
    "CvssTypeDef",
    "CvssUnionTypeDef",
    "DataClassificationDetailsOutputTypeDef",
    "DataClassificationDetailsTypeDef",
    "DataClassificationDetailsUnionTypeDef",
    "DateFilterTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteActionTargetRequestTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteConfigurationPolicyRequestTypeDef",
    "DeleteFindingAggregatorRequestTypeDef",
    "DeleteInsightRequestTypeDef",
    "DeleteInsightResponseTypeDef",
    "DeleteInvitationsRequestTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeActionTargetsRequestPaginateTypeDef",
    "DescribeActionTargetsRequestTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubRequestTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribeProductsRequestPaginateTypeDef",
    "DescribeProductsRequestTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsRequestPaginateTypeDef",
    "DescribeStandardsControlsRequestTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "DescribeStandardsRequestPaginateTypeDef",
    "DescribeStandardsRequestTypeDef",
    "DescribeStandardsResponseTypeDef",
    "DetectionOutputTypeDef",
    "DetectionTypeDef",
    "DetectionUnionTypeDef",
    "DisableImportFindingsForProductRequestTypeDef",
    "DisableOrganizationAdminAccountRequestTypeDef",
    "DisassociateMembersRequestTypeDef",
    "DnsRequestActionTypeDef",
    "DoubleConfigurationOptionsTypeDef",
    "EnableImportFindingsForProductRequestTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "EnableOrganizationAdminAccountRequestTypeDef",
    "EnableSecurityHubRequestTypeDef",
    "EnumConfigurationOptionsTypeDef",
    "EnumListConfigurationOptionsTypeDef",
    "FilePathsTypeDef",
    "FindingAggregatorTypeDef",
    "FindingHistoryRecordTypeDef",
    "FindingHistoryUpdateSourceTypeDef",
    "FindingHistoryUpdateTypeDef",
    "FindingProviderFieldsOutputTypeDef",
    "FindingProviderFieldsTypeDef",
    "FindingProviderFieldsUnionTypeDef",
    "FindingProviderSeverityTypeDef",
    "FirewallPolicyDetailsOutputTypeDef",
    "FirewallPolicyDetailsTypeDef",
    "FirewallPolicyDetailsUnionTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    "GeneratorDetailsOutputTypeDef",
    "GeneratorDetailsTypeDef",
    "GeneratorDetailsUnionTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetConfigurationPolicyAssociationRequestTypeDef",
    "GetConfigurationPolicyAssociationResponseTypeDef",
    "GetConfigurationPolicyRequestTypeDef",
    "GetConfigurationPolicyResponseTypeDef",
    "GetEnabledStandardsRequestPaginateTypeDef",
    "GetEnabledStandardsRequestTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "GetFindingAggregatorRequestTypeDef",
    "GetFindingAggregatorResponseTypeDef",
    "GetFindingHistoryRequestPaginateTypeDef",
    "GetFindingHistoryRequestTypeDef",
    "GetFindingHistoryResponseTypeDef",
    "GetFindingsRequestPaginateTypeDef",
    "GetFindingsRequestTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInsightResultsRequestTypeDef",
    "GetInsightResultsResponseTypeDef",
    "GetInsightsRequestPaginateTypeDef",
    "GetInsightsRequestTypeDef",
    "GetInsightsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GetSecurityControlDefinitionRequestTypeDef",
    "GetSecurityControlDefinitionResponseTypeDef",
    "IcmpTypeCodeTypeDef",
    "ImportFindingsErrorTypeDef",
    "IndicatorOutputTypeDef",
    "IndicatorTypeDef",
    "IndicatorUnionTypeDef",
    "InsightResultValueTypeDef",
    "InsightResultsTypeDef",
    "InsightTypeDef",
    "IntegerConfigurationOptionsTypeDef",
    "IntegerListConfigurationOptionsTypeDef",
    "InvitationTypeDef",
    "InviteMembersRequestTypeDef",
    "InviteMembersResponseTypeDef",
    "IpFilterTypeDef",
    "IpOrganizationDetailsTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "KeywordFilterTypeDef",
    "ListAutomationRulesRequestTypeDef",
    "ListAutomationRulesResponseTypeDef",
    "ListConfigurationPoliciesRequestPaginateTypeDef",
    "ListConfigurationPoliciesRequestTypeDef",
    "ListConfigurationPoliciesResponseTypeDef",
    "ListConfigurationPolicyAssociationsRequestPaginateTypeDef",
    "ListConfigurationPolicyAssociationsRequestTypeDef",
    "ListConfigurationPolicyAssociationsResponseTypeDef",
    "ListEnabledProductsForImportRequestPaginateTypeDef",
    "ListEnabledProductsForImportRequestTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListFindingAggregatorsRequestPaginateTypeDef",
    "ListFindingAggregatorsRequestTypeDef",
    "ListFindingAggregatorsResponseTypeDef",
    "ListInvitationsRequestPaginateTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestPaginateTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListSecurityControlDefinitionsRequestPaginateTypeDef",
    "ListSecurityControlDefinitionsRequestTypeDef",
    "ListSecurityControlDefinitionsResponseTypeDef",
    "ListStandardsControlAssociationsRequestPaginateTypeDef",
    "ListStandardsControlAssociationsRequestTypeDef",
    "ListStandardsControlAssociationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoadBalancerStateTypeDef",
    "MalwareTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkAutonomousSystemTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkConnectionTypeDef",
    "NetworkEndpointTypeDef",
    "NetworkGeoLocationTypeDef",
    "NetworkHeaderOutputTypeDef",
    "NetworkHeaderTypeDef",
    "NetworkHeaderUnionTypeDef",
    "NetworkPathComponentDetailsOutputTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkPathComponentDetailsUnionTypeDef",
    "NetworkPathComponentOutputTypeDef",
    "NetworkPathComponentTypeDef",
    "NetworkPathComponentUnionTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "NoteUpdateTypeDef",
    "NumberFilterTypeDef",
    "OccurrencesOutputTypeDef",
    "OccurrencesTypeDef",
    "OccurrencesUnionTypeDef",
    "OrganizationConfigurationTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConfigurationOutputTypeDef",
    "ParameterConfigurationTypeDef",
    "ParameterConfigurationUnionTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterValueOutputTypeDef",
    "ParameterValueTypeDef",
    "ParameterValueUnionTypeDef",
    "PatchSummaryTypeDef",
    "PolicyOutputTypeDef",
    "PolicyTypeDef",
    "PolicyUnionTypeDef",
    "PortProbeActionOutputTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeActionUnionTypeDef",
    "PortProbeDetailTypeDef",
    "PortRangeFromToTypeDef",
    "PortRangeTypeDef",
    "ProcessDetailsTypeDef",
    "ProductTypeDef",
    "PropagatingVgwSetDetailsTypeDef",
    "RangeTypeDef",
    "RecommendationTypeDef",
    "RecordTypeDef",
    "RelatedFindingTypeDef",
    "RemediationTypeDef",
    "ResourceDetailsOutputTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceDetailsUnionTypeDef",
    "ResourceOutputTypeDef",
    "ResourceTypeDef",
    "ResourceUnionTypeDef",
    "ResponseMetadataTypeDef",
    "ResultTypeDef",
    "RouteSetDetailsTypeDef",
    "RuleGroupDetailsOutputTypeDef",
    "RuleGroupDetailsTypeDef",
    "RuleGroupDetailsUnionTypeDef",
    "RuleGroupSourceCustomActionsDetailsOutputTypeDef",
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    "RuleGroupSourceCustomActionsDetailsUnionTypeDef",
    "RuleGroupSourceListDetailsOutputTypeDef",
    "RuleGroupSourceListDetailsTypeDef",
    "RuleGroupSourceListDetailsUnionTypeDef",
    "RuleGroupSourceOutputTypeDef",
    "RuleGroupSourceStatefulRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    "RuleGroupSourceStatefulRulesDetailsUnionTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionOutputTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionUnionTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef",
    "RuleGroupSourceStatelessRulesDetailsOutputTypeDef",
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    "RuleGroupSourceStatelessRulesDetailsUnionTypeDef",
    "RuleGroupSourceTypeDef",
    "RuleGroupSourceUnionTypeDef",
    "RuleGroupVariablesIpSetsDetailsOutputTypeDef",
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    "RuleGroupVariablesIpSetsDetailsUnionTypeDef",
    "RuleGroupVariablesOutputTypeDef",
    "RuleGroupVariablesPortSetsDetailsOutputTypeDef",
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    "RuleGroupVariablesPortSetsDetailsUnionTypeDef",
    "RuleGroupVariablesTypeDef",
    "RuleGroupVariablesUnionTypeDef",
    "SecurityControlCustomParameterOutputTypeDef",
    "SecurityControlCustomParameterTypeDef",
    "SecurityControlDefinitionTypeDef",
    "SecurityControlParameterOutputTypeDef",
    "SecurityControlParameterTypeDef",
    "SecurityControlParameterUnionTypeDef",
    "SecurityControlTypeDef",
    "SecurityControlsConfigurationOutputTypeDef",
    "SecurityControlsConfigurationTypeDef",
    "SecurityHubPolicyOutputTypeDef",
    "SecurityHubPolicyTypeDef",
    "SensitiveDataDetectionsOutputTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SensitiveDataDetectionsUnionTypeDef",
    "SensitiveDataResultOutputTypeDef",
    "SensitiveDataResultTypeDef",
    "SensitiveDataResultUnionTypeDef",
    "SequenceOutputTypeDef",
    "SequenceTypeDef",
    "SequenceUnionTypeDef",
    "SeverityTypeDef",
    "SeverityUpdateTypeDef",
    "SignalOutputTypeDef",
    "SignalTypeDef",
    "SignalUnionTypeDef",
    "SoftwarePackageTypeDef",
    "SortCriterionTypeDef",
    "StandardTypeDef",
    "StandardsControlAssociationDetailTypeDef",
    "StandardsControlAssociationIdTypeDef",
    "StandardsControlAssociationSummaryTypeDef",
    "StandardsControlAssociationUpdateTypeDef",
    "StandardsControlTypeDef",
    "StandardsManagedByTypeDef",
    "StandardsStatusReasonTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "StandardsSubscriptionTypeDef",
    "StartConfigurationPolicyAssociationRequestTypeDef",
    "StartConfigurationPolicyAssociationResponseTypeDef",
    "StartConfigurationPolicyDisassociationRequestTypeDef",
    "StatelessCustomActionDefinitionOutputTypeDef",
    "StatelessCustomActionDefinitionTypeDef",
    "StatelessCustomActionDefinitionUnionTypeDef",
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    "StatelessCustomPublishMetricActionOutputTypeDef",
    "StatelessCustomPublishMetricActionTypeDef",
    "StatelessCustomPublishMetricActionUnionTypeDef",
    "StatusReasonTypeDef",
    "StringConfigurationOptionsTypeDef",
    "StringFilterTypeDef",
    "StringListConfigurationOptionsTypeDef",
    "TagResourceRequestTypeDef",
    "TargetTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "ThreatOutputTypeDef",
    "ThreatTypeDef",
    "ThreatUnionTypeDef",
    "TimestampTypeDef",
    "UnprocessedAutomationRuleTypeDef",
    "UnprocessedConfigurationPolicyAssociationTypeDef",
    "UnprocessedSecurityControlTypeDef",
    "UnprocessedStandardsControlAssociationTypeDef",
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateActionTargetRequestTypeDef",
    "UpdateAutomationRulesRequestItemTypeDef",
    "UpdateConfigurationPolicyRequestTypeDef",
    "UpdateConfigurationPolicyResponseTypeDef",
    "UpdateFindingAggregatorRequestTypeDef",
    "UpdateFindingAggregatorResponseTypeDef",
    "UpdateFindingsRequestTypeDef",
    "UpdateInsightRequestTypeDef",
    "UpdateOrganizationConfigurationRequestTypeDef",
    "UpdateSecurityControlRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestTypeDef",
    "UpdateStandardsControlRequestTypeDef",
    "UserAccountTypeDef",
    "VolumeMountTypeDef",
    "VpcInfoCidrBlockSetDetailsTypeDef",
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    "VpcInfoPeeringOptionsDetailsTypeDef",
    "VulnerabilityCodeVulnerabilitiesOutputTypeDef",
    "VulnerabilityCodeVulnerabilitiesTypeDef",
    "VulnerabilityCodeVulnerabilitiesUnionTypeDef",
    "VulnerabilityOutputTypeDef",
    "VulnerabilityTypeDef",
    "VulnerabilityUnionTypeDef",
    "VulnerabilityVendorTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "WorkflowTypeDef",
    "WorkflowUpdateTypeDef",
)

class AcceptAdministratorInvitationRequestTypeDef(TypedDict):
    AdministratorId: str
    InvitationId: str

class AcceptInvitationRequestTypeDef(TypedDict):
    MasterId: str
    InvitationId: str

class AccountDetailsTypeDef(TypedDict):
    AccountId: str
    Email: NotRequired[str]

class ActionLocalIpDetailsTypeDef(TypedDict):
    IpAddressV4: NotRequired[str]

class ActionLocalPortDetailsTypeDef(TypedDict):
    Port: NotRequired[int]
    PortName: NotRequired[str]

DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)

class CityTypeDef(TypedDict):
    CityName: NotRequired[str]

class CountryTypeDef(TypedDict):
    CountryCode: NotRequired[str]
    CountryName: NotRequired[str]

class GeoLocationTypeDef(TypedDict):
    Lon: NotRequired[float]
    Lat: NotRequired[float]

class IpOrganizationDetailsTypeDef(TypedDict):
    Asn: NotRequired[int]
    AsnOrg: NotRequired[str]
    Isp: NotRequired[str]
    Org: NotRequired[str]

class ActionRemotePortDetailsTypeDef(TypedDict):
    Port: NotRequired[int]
    PortName: NotRequired[str]

class ActionTargetTypeDef(TypedDict):
    ActionTargetArn: str
    Name: str
    Description: str

class ActorSessionTypeDef(TypedDict):
    Uid: NotRequired[str]
    MfaStatus: NotRequired[ActorSessionMfaStatusType]
    CreatedTime: NotRequired[int]
    Issuer: NotRequired[str]

class UserAccountTypeDef(TypedDict):
    Uid: NotRequired[str]
    Name: NotRequired[str]

class AdjustmentTypeDef(TypedDict):
    Metric: NotRequired[str]
    Reason: NotRequired[str]

class AdminAccountTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Status: NotRequired[AdminStatusType]

class AssociatedStandardTypeDef(TypedDict):
    StandardsId: NotRequired[str]

class AssociationFiltersTypeDef(TypedDict):
    ConfigurationPolicyId: NotRequired[str]
    AssociationType: NotRequired[AssociationTypeType]
    AssociationStatus: NotRequired[ConfigurationPolicyAssociationStatusType]

class AssociationStateDetailsTypeDef(TypedDict):
    State: NotRequired[str]
    StatusMessage: NotRequired[str]

NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)

class RelatedFindingTypeDef(TypedDict):
    ProductArn: str
    Id: str

class SeverityUpdateTypeDef(TypedDict):
    Normalized: NotRequired[int]
    Product: NotRequired[float]
    Label: NotRequired[SeverityLabelType]

class WorkflowUpdateTypeDef(TypedDict):
    Status: NotRequired[WorkflowStatusType]

class MapFilterTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]
    Comparison: NotRequired[MapFilterComparisonType]

class NumberFilterTypeDef(TypedDict):
    Gte: NotRequired[float]
    Lte: NotRequired[float]
    Eq: NotRequired[float]
    Gt: NotRequired[float]
    Lt: NotRequired[float]

class StringFilterTypeDef(TypedDict):
    Value: NotRequired[str]
    Comparison: NotRequired[StringFilterComparisonType]

class AutomationRulesMetadataTypeDef(TypedDict):
    RuleArn: NotRequired[str]
    RuleStatus: NotRequired[RuleStatusType]
    RuleOrder: NotRequired[int]
    RuleName: NotRequired[str]
    Description: NotRequired[str]
    IsTerminal: NotRequired[bool]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    CreatedBy: NotRequired[str]

class AvailabilityZoneTypeDef(TypedDict):
    ZoneName: NotRequired[str]
    SubnetId: NotRequired[str]

class AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef(TypedDict):
    KmsKeyId: NotRequired[str]
    UseAwsOwnedKey: NotRequired[bool]

class AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef(TypedDict):
    Hosts: NotRequired[List[str]]
    RoleBase: NotRequired[str]
    RoleName: NotRequired[str]
    RoleSearchMatching: NotRequired[str]
    RoleSearchSubtree: NotRequired[bool]
    ServiceAccountUsername: NotRequired[str]
    UserBase: NotRequired[str]
    UserRoleName: NotRequired[str]
    UserSearchMatching: NotRequired[str]
    UserSearchSubtree: NotRequired[bool]

class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef(TypedDict):
    DayOfWeek: NotRequired[str]
    TimeOfDay: NotRequired[str]
    TimeZone: NotRequired[str]

class AwsAmazonMqBrokerUsersDetailsTypeDef(TypedDict):
    PendingChange: NotRequired[str]
    Username: NotRequired[str]

class AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef(TypedDict):
    Hosts: NotRequired[Sequence[str]]
    RoleBase: NotRequired[str]
    RoleName: NotRequired[str]
    RoleSearchMatching: NotRequired[str]
    RoleSearchSubtree: NotRequired[bool]
    ServiceAccountUsername: NotRequired[str]
    UserBase: NotRequired[str]
    UserRoleName: NotRequired[str]
    UserSearchMatching: NotRequired[str]
    UserSearchSubtree: NotRequired[bool]

class AwsAmazonMqBrokerLogsPendingDetailsTypeDef(TypedDict):
    Audit: NotRequired[bool]
    General: NotRequired[bool]

class AwsApiCallActionDomainDetailsTypeDef(TypedDict):
    Domain: NotRequired[str]

class AwsApiGatewayAccessLogSettingsTypeDef(TypedDict):
    Format: NotRequired[str]
    DestinationArn: NotRequired[str]

class AwsApiGatewayCanarySettingsOutputTypeDef(TypedDict):
    PercentTraffic: NotRequired[float]
    DeploymentId: NotRequired[str]
    StageVariableOverrides: NotRequired[Dict[str, str]]
    UseStageCache: NotRequired[bool]

class AwsApiGatewayCanarySettingsTypeDef(TypedDict):
    PercentTraffic: NotRequired[float]
    DeploymentId: NotRequired[str]
    StageVariableOverrides: NotRequired[Mapping[str, str]]
    UseStageCache: NotRequired[bool]

class AwsApiGatewayEndpointConfigurationOutputTypeDef(TypedDict):
    Types: NotRequired[List[str]]

class AwsApiGatewayEndpointConfigurationTypeDef(TypedDict):
    Types: NotRequired[Sequence[str]]

class AwsApiGatewayMethodSettingsTypeDef(TypedDict):
    MetricsEnabled: NotRequired[bool]
    LoggingLevel: NotRequired[str]
    DataTraceEnabled: NotRequired[bool]
    ThrottlingBurstLimit: NotRequired[int]
    ThrottlingRateLimit: NotRequired[float]
    CachingEnabled: NotRequired[bool]
    CacheTtlInSeconds: NotRequired[int]
    CacheDataEncrypted: NotRequired[bool]
    RequireAuthorizationForCacheControl: NotRequired[bool]
    UnauthorizedCacheControlHeaderStrategy: NotRequired[str]
    HttpMethod: NotRequired[str]
    ResourcePath: NotRequired[str]

class AwsCorsConfigurationOutputTypeDef(TypedDict):
    AllowOrigins: NotRequired[List[str]]
    AllowCredentials: NotRequired[bool]
    ExposeHeaders: NotRequired[List[str]]
    MaxAge: NotRequired[int]
    AllowMethods: NotRequired[List[str]]
    AllowHeaders: NotRequired[List[str]]

class AwsApiGatewayV2RouteSettingsTypeDef(TypedDict):
    DetailedMetricsEnabled: NotRequired[bool]
    LoggingLevel: NotRequired[str]
    DataTraceEnabled: NotRequired[bool]
    ThrottlingBurstLimit: NotRequired[int]
    ThrottlingRateLimit: NotRequired[float]

class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef(TypedDict):
    AuthorizerResultTtlInSeconds: NotRequired[int]
    AuthorizerUri: NotRequired[str]
    IdentityValidationExpression: NotRequired[str]

class AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef(TypedDict):
    AuthTtL: NotRequired[int]
    ClientId: NotRequired[str]
    IatTtL: NotRequired[int]
    Issuer: NotRequired[str]

class AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef(TypedDict):
    AppIdClientRegex: NotRequired[str]
    AwsRegion: NotRequired[str]
    DefaultAction: NotRequired[str]
    UserPoolId: NotRequired[str]

class AwsAppSyncGraphQlApiLogConfigDetailsTypeDef(TypedDict):
    CloudWatchLogsRoleArn: NotRequired[str]
    ExcludeVerboseContent: NotRequired[bool]
    FieldLogLevel: NotRequired[str]

class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef(
    TypedDict
):
    EncryptionOption: NotRequired[str]
    KmsKey: NotRequired[str]

class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef(TypedDict):
    Value: NotRequired[str]

class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef(TypedDict):
    LaunchTemplateId: NotRequired[str]
    LaunchTemplateName: NotRequired[str]
    Version: NotRequired[str]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef(
    TypedDict
):
    OnDemandAllocationStrategy: NotRequired[str]
    OnDemandBaseCapacity: NotRequired[int]
    OnDemandPercentageAboveBaseCapacity: NotRequired[int]
    SpotAllocationStrategy: NotRequired[str]
    SpotInstancePools: NotRequired[int]
    SpotMaxPrice: NotRequired[str]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    TypedDict
):
    LaunchTemplateId: NotRequired[str]
    LaunchTemplateName: NotRequired[str]
    Version: NotRequired[str]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef(
    TypedDict
):
    InstanceType: NotRequired[str]
    WeightedCapacity: NotRequired[str]

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef(TypedDict):
    DeleteOnTermination: NotRequired[bool]
    Encrypted: NotRequired[bool]
    Iops: NotRequired[int]
    SnapshotId: NotRequired[str]
    VolumeSize: NotRequired[int]
    VolumeType: NotRequired[str]

class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef(TypedDict):
    HttpEndpoint: NotRequired[str]
    HttpPutResponseHopLimit: NotRequired[int]
    HttpTokens: NotRequired[str]

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef(TypedDict):
    BackupOptions: NotRequired[Dict[str, str]]
    ResourceType: NotRequired[str]

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef(TypedDict):
    BackupOptions: NotRequired[Mapping[str, str]]
    ResourceType: NotRequired[str]

class AwsBackupBackupPlanLifecycleDetailsTypeDef(TypedDict):
    DeleteAfterDays: NotRequired[int]
    MoveToColdStorageAfterDays: NotRequired[int]

class AwsBackupBackupVaultNotificationsDetailsOutputTypeDef(TypedDict):
    BackupVaultEvents: NotRequired[List[str]]
    SnsTopicArn: NotRequired[str]

class AwsBackupBackupVaultNotificationsDetailsTypeDef(TypedDict):
    BackupVaultEvents: NotRequired[Sequence[str]]
    SnsTopicArn: NotRequired[str]

class AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef(TypedDict):
    DeleteAt: NotRequired[str]
    MoveToColdStorageAt: NotRequired[str]

class AwsBackupRecoveryPointCreatedByDetailsTypeDef(TypedDict):
    BackupPlanArn: NotRequired[str]
    BackupPlanId: NotRequired[str]
    BackupPlanVersion: NotRequired[str]
    BackupRuleId: NotRequired[str]

class AwsBackupRecoveryPointLifecycleDetailsTypeDef(TypedDict):
    DeleteAfterDays: NotRequired[int]
    MoveToColdStorageAfterDays: NotRequired[int]

class AwsCertificateManagerCertificateExtendedKeyUsageTypeDef(TypedDict):
    Name: NotRequired[str]
    OId: NotRequired[str]

class AwsCertificateManagerCertificateKeyUsageTypeDef(TypedDict):
    Name: NotRequired[str]

class AwsCertificateManagerCertificateOptionsTypeDef(TypedDict):
    CertificateTransparencyLoggingPreference: NotRequired[str]

AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

class AwsCloudFormationStackDriftInformationDetailsTypeDef(TypedDict):
    StackDriftStatus: NotRequired[str]

class AwsCloudFormationStackOutputsDetailsTypeDef(TypedDict):
    Description: NotRequired[str]
    OutputKey: NotRequired[str]
    OutputValue: NotRequired[str]

class AwsCloudFrontDistributionCacheBehaviorTypeDef(TypedDict):
    ViewerProtocolPolicy: NotRequired[str]

class AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef(TypedDict):
    ViewerProtocolPolicy: NotRequired[str]

class AwsCloudFrontDistributionLoggingTypeDef(TypedDict):
    Bucket: NotRequired[str]
    Enabled: NotRequired[bool]
    IncludeCookies: NotRequired[bool]
    Prefix: NotRequired[str]

class AwsCloudFrontDistributionViewerCertificateTypeDef(TypedDict):
    AcmCertificateArn: NotRequired[str]
    Certificate: NotRequired[str]
    CertificateSource: NotRequired[str]
    CloudFrontDefaultCertificate: NotRequired[bool]
    IamCertificateId: NotRequired[str]
    MinimumProtocolVersion: NotRequired[str]
    SslSupportMethod: NotRequired[str]

class AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef(TypedDict):
    Items: NotRequired[List[str]]
    Quantity: NotRequired[int]

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef(TypedDict):
    Items: NotRequired[List[int]]
    Quantity: NotRequired[int]

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef(TypedDict):
    Items: NotRequired[Sequence[int]]
    Quantity: NotRequired[int]

class AwsCloudFrontDistributionOriginS3OriginConfigTypeDef(TypedDict):
    OriginAccessIdentity: NotRequired[str]

class AwsCloudFrontDistributionOriginSslProtocolsTypeDef(TypedDict):
    Items: NotRequired[Sequence[str]]
    Quantity: NotRequired[int]

class AwsCloudTrailTrailDetailsTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[str]
    CloudWatchLogsRoleArn: NotRequired[str]
    HasCustomEventSelectors: NotRequired[bool]
    HomeRegion: NotRequired[str]
    IncludeGlobalServiceEvents: NotRequired[bool]
    IsMultiRegionTrail: NotRequired[bool]
    IsOrganizationTrail: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    LogFileValidationEnabled: NotRequired[bool]
    Name: NotRequired[str]
    S3BucketName: NotRequired[str]
    S3KeyPrefix: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    SnsTopicName: NotRequired[str]
    TrailArn: NotRequired[str]

class AwsCloudWatchAlarmDimensionsDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

AwsCodeBuildProjectArtifactsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    {
        "ArtifactIdentifier": NotRequired[str],
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceType": NotRequired[str],
        "OverrideArtifactName": NotRequired[bool],
        "Packaging": NotRequired[str],
        "Path": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Location": NotRequired[str],
        "GitCloneDepth": NotRequired[int],
        "InsecureSsl": NotRequired[bool],
    },
)

class AwsCodeBuildProjectVpcConfigOutputTypeDef(TypedDict):
    VpcId: NotRequired[str]
    Subnets: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]

AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

class AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef(TypedDict):
    Credential: NotRequired[str]
    CredentialProvider: NotRequired[str]

class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef(TypedDict):
    GroupName: NotRequired[str]
    Status: NotRequired[str]
    StreamName: NotRequired[str]

class AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef(TypedDict):
    EncryptionDisabled: NotRequired[bool]
    Location: NotRequired[str]
    Status: NotRequired[str]

class AwsCodeBuildProjectVpcConfigTypeDef(TypedDict):
    VpcId: NotRequired[str]
    Subnets: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]

class AwsCorsConfigurationTypeDef(TypedDict):
    AllowOrigins: NotRequired[Sequence[str]]
    AllowCredentials: NotRequired[bool]
    ExposeHeaders: NotRequired[Sequence[str]]
    MaxAge: NotRequired[int]
    AllowMethods: NotRequired[Sequence[str]]
    AllowHeaders: NotRequired[Sequence[str]]

class AwsDmsEndpointDetailsTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    DatabaseName: NotRequired[str]
    EndpointArn: NotRequired[str]
    EndpointIdentifier: NotRequired[str]
    EndpointType: NotRequired[str]
    EngineName: NotRequired[str]
    ExternalId: NotRequired[str]
    ExtraConnectionAttributes: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    SslMode: NotRequired[str]
    Username: NotRequired[str]

class AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef(TypedDict):
    ReplicationSubnetGroupIdentifier: NotRequired[str]

class AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]

class AwsDmsReplicationTaskDetailsTypeDef(TypedDict):
    CdcStartPosition: NotRequired[str]
    CdcStartTime: NotRequired[str]
    CdcStopPosition: NotRequired[str]
    MigrationType: NotRequired[str]
    Id: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    ReplicationInstanceArn: NotRequired[str]
    ReplicationTaskIdentifier: NotRequired[str]
    ReplicationTaskSettings: NotRequired[str]
    SourceEndpointArn: NotRequired[str]
    TableMappings: NotRequired[str]
    TargetEndpointArn: NotRequired[str]
    TaskData: NotRequired[str]

class AwsDynamoDbTableAttributeDefinitionTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeType: NotRequired[str]

class AwsDynamoDbTableBillingModeSummaryTypeDef(TypedDict):
    BillingMode: NotRequired[str]
    LastUpdateToPayPerRequestDateTime: NotRequired[str]

class AwsDynamoDbTableKeySchemaTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    KeyType: NotRequired[str]

class AwsDynamoDbTableProvisionedThroughputTypeDef(TypedDict):
    LastDecreaseDateTime: NotRequired[str]
    LastIncreaseDateTime: NotRequired[str]
    NumberOfDecreasesToday: NotRequired[int]
    ReadCapacityUnits: NotRequired[int]
    WriteCapacityUnits: NotRequired[int]

class AwsDynamoDbTableRestoreSummaryTypeDef(TypedDict):
    SourceBackupArn: NotRequired[str]
    SourceTableArn: NotRequired[str]
    RestoreDateTime: NotRequired[str]
    RestoreInProgress: NotRequired[bool]

class AwsDynamoDbTableSseDescriptionTypeDef(TypedDict):
    InaccessibleEncryptionDateTime: NotRequired[str]
    Status: NotRequired[str]
    SseType: NotRequired[str]
    KmsMasterKeyArn: NotRequired[str]

class AwsDynamoDbTableStreamSpecificationTypeDef(TypedDict):
    StreamEnabled: NotRequired[bool]
    StreamViewType: NotRequired[str]

class AwsDynamoDbTableProjectionOutputTypeDef(TypedDict):
    NonKeyAttributes: NotRequired[List[str]]
    ProjectionType: NotRequired[str]

class AwsDynamoDbTableProjectionTypeDef(TypedDict):
    NonKeyAttributes: NotRequired[Sequence[str]]
    ProjectionType: NotRequired[str]

class AwsDynamoDbTableProvisionedThroughputOverrideTypeDef(TypedDict):
    ReadCapacityUnits: NotRequired[int]

class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef(TypedDict):
    DirectoryId: NotRequired[str]

class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef(TypedDict):
    SamlProviderArn: NotRequired[str]
    SelfServiceSamlProviderArn: NotRequired[str]

class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef(TypedDict):
    ClientRootCertificateChain: NotRequired[str]

class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]

class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    BannerText: NotRequired[str]

class AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    CloudwatchLogGroup: NotRequired[str]
    CloudwatchLogStream: NotRequired[str]

class AwsEc2EipDetailsTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    PublicIp: NotRequired[str]
    AllocationId: NotRequired[str]
    AssociationId: NotRequired[str]
    Domain: NotRequired[str]
    PublicIpv4Pool: NotRequired[str]
    NetworkBorderGroup: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    NetworkInterfaceOwnerId: NotRequired[str]
    PrivateIpAddress: NotRequired[str]

class AwsEc2InstanceMetadataOptionsTypeDef(TypedDict):
    HttpEndpoint: NotRequired[str]
    HttpProtocolIpv6: NotRequired[str]
    HttpPutResponseHopLimit: NotRequired[int]
    HttpTokens: NotRequired[str]
    InstanceMetadataTags: NotRequired[str]

class AwsEc2InstanceMonitoringDetailsTypeDef(TypedDict):
    State: NotRequired[str]

class AwsEc2InstanceNetworkInterfacesDetailsTypeDef(TypedDict):
    NetworkInterfaceId: NotRequired[str]

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef(TypedDict):
    DeleteOnTermination: NotRequired[bool]
    Encrypted: NotRequired[bool]
    Iops: NotRequired[int]
    KmsKeyId: NotRequired[str]
    SnapshotId: NotRequired[str]
    Throughput: NotRequired[int]
    VolumeSize: NotRequired[int]
    VolumeType: NotRequired[str]

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef(
    TypedDict
):
    CapacityReservationId: NotRequired[str]
    CapacityReservationResourceGroupArn: NotRequired[str]

class AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef(TypedDict):
    CoreCount: NotRequired[int]
    ThreadsPerCore: NotRequired[int]

class AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef(TypedDict):
    CpuCredits: NotRequired[str]

AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
    },
)

class AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef(TypedDict):
    Configured: NotRequired[bool]

class AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef(TypedDict):
    LicenseConfigurationArn: NotRequired[str]

class AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef(TypedDict):
    AutoRecovery: NotRequired[str]

class AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef(TypedDict):
    HttpEndpoint: NotRequired[str]
    HttpProtocolIpv6: NotRequired[str]
    HttpTokens: NotRequired[str]
    HttpPutResponseHopLimit: NotRequired[int]
    InstanceMetadataTags: NotRequired[str]

class AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsEc2LaunchTemplateDataPlacementDetailsTypeDef(TypedDict):
    Affinity: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    GroupName: NotRequired[str]
    HostId: NotRequired[str]
    HostResourceGroupArn: NotRequired[str]
    PartitionNumber: NotRequired[int]
    SpreadDomain: NotRequired[str]
    Tenancy: NotRequired[str]

class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef(TypedDict):
    EnableResourceNameDnsAAAARecord: NotRequired[bool]
    EnableResourceNameDnsARecord: NotRequired[bool]
    HostnameType: NotRequired[str]

class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef(TypedDict):
    BlockDurationMinutes: NotRequired[int]
    InstanceInterruptionBehavior: NotRequired[str]
    MaxPrice: NotRequired[str]
    SpotInstanceType: NotRequired[str]
    ValidUntil: NotRequired[str]

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef(TypedDict):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef(
    TypedDict
):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef(TypedDict):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef(TypedDict):
    Max: NotRequired[float]
    Min: NotRequired[float]

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef(TypedDict):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef(TypedDict):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef(TypedDict):
    Max: NotRequired[float]
    Min: NotRequired[float]

class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef(TypedDict):
    Max: NotRequired[int]
    Min: NotRequired[int]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef(TypedDict):
    Ipv4Prefix: NotRequired[str]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef(TypedDict):
    Ipv6Address: NotRequired[str]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef(TypedDict):
    Ipv6Prefix: NotRequired[str]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef(TypedDict):
    Primary: NotRequired[bool]
    PrivateIpAddress: NotRequired[str]

class AwsEc2NetworkAclAssociationTypeDef(TypedDict):
    NetworkAclAssociationId: NotRequired[str]
    NetworkAclId: NotRequired[str]
    SubnetId: NotRequired[str]

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)

class PortRangeFromToTypeDef(TypedDict):
    From: NotRequired[int]
    To: NotRequired[int]

class AwsEc2NetworkInterfaceAttachmentTypeDef(TypedDict):
    AttachTime: NotRequired[str]
    AttachmentId: NotRequired[str]
    DeleteOnTermination: NotRequired[bool]
    DeviceIndex: NotRequired[int]
    InstanceId: NotRequired[str]
    InstanceOwnerId: NotRequired[str]
    Status: NotRequired[str]

class AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef(TypedDict):
    IpV6Address: NotRequired[str]

class AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef(TypedDict):
    PrivateIpAddress: NotRequired[str]
    PrivateDnsName: NotRequired[str]

class AwsEc2NetworkInterfaceSecurityGroupTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupId: NotRequired[str]

class PropagatingVgwSetDetailsTypeDef(TypedDict):
    GatewayId: NotRequired[str]

class RouteSetDetailsTypeDef(TypedDict):
    CarrierGatewayId: NotRequired[str]
    CoreNetworkArn: NotRequired[str]
    DestinationCidrBlock: NotRequired[str]
    DestinationIpv6CidrBlock: NotRequired[str]
    DestinationPrefixListId: NotRequired[str]
    EgressOnlyInternetGatewayId: NotRequired[str]
    GatewayId: NotRequired[str]
    InstanceId: NotRequired[str]
    InstanceOwnerId: NotRequired[str]
    LocalGatewayId: NotRequired[str]
    NatGatewayId: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    Origin: NotRequired[str]
    State: NotRequired[str]
    TransitGatewayId: NotRequired[str]
    VpcPeeringConnectionId: NotRequired[str]

class AwsEc2SecurityGroupIpRangeTypeDef(TypedDict):
    CidrIp: NotRequired[str]

class AwsEc2SecurityGroupIpv6RangeTypeDef(TypedDict):
    CidrIpv6: NotRequired[str]

class AwsEc2SecurityGroupPrefixListIdTypeDef(TypedDict):
    PrefixListId: NotRequired[str]

class AwsEc2SecurityGroupUserIdGroupPairTypeDef(TypedDict):
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]
    PeeringStatus: NotRequired[str]
    UserId: NotRequired[str]
    VpcId: NotRequired[str]
    VpcPeeringConnectionId: NotRequired[str]

class Ipv6CidrBlockAssociationTypeDef(TypedDict):
    AssociationId: NotRequired[str]
    Ipv6CidrBlock: NotRequired[str]
    CidrBlockState: NotRequired[str]

class AwsEc2TransitGatewayDetailsOutputTypeDef(TypedDict):
    Id: NotRequired[str]
    Description: NotRequired[str]
    DefaultRouteTablePropagation: NotRequired[str]
    AutoAcceptSharedAttachments: NotRequired[str]
    DefaultRouteTableAssociation: NotRequired[str]
    TransitGatewayCidrBlocks: NotRequired[List[str]]
    AssociationDefaultRouteTableId: NotRequired[str]
    PropagationDefaultRouteTableId: NotRequired[str]
    VpnEcmpSupport: NotRequired[str]
    DnsSupport: NotRequired[str]
    MulticastSupport: NotRequired[str]
    AmazonSideAsn: NotRequired[int]

class AwsEc2TransitGatewayDetailsTypeDef(TypedDict):
    Id: NotRequired[str]
    Description: NotRequired[str]
    DefaultRouteTablePropagation: NotRequired[str]
    AutoAcceptSharedAttachments: NotRequired[str]
    DefaultRouteTableAssociation: NotRequired[str]
    TransitGatewayCidrBlocks: NotRequired[Sequence[str]]
    AssociationDefaultRouteTableId: NotRequired[str]
    PropagationDefaultRouteTableId: NotRequired[str]
    VpnEcmpSupport: NotRequired[str]
    DnsSupport: NotRequired[str]
    MulticastSupport: NotRequired[str]
    AmazonSideAsn: NotRequired[int]

class AwsEc2VolumeAttachmentTypeDef(TypedDict):
    AttachTime: NotRequired[str]
    DeleteOnTermination: NotRequired[bool]
    InstanceId: NotRequired[str]
    Status: NotRequired[str]

class CidrBlockAssociationTypeDef(TypedDict):
    AssociationId: NotRequired[str]
    CidrBlock: NotRequired[str]
    CidrBlockState: NotRequired[str]

class AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef(TypedDict):
    ServiceType: NotRequired[str]

class AwsEc2VpcPeeringConnectionStatusDetailsTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]

class VpcInfoCidrBlockSetDetailsTypeDef(TypedDict):
    CidrBlock: NotRequired[str]

class VpcInfoIpv6CidrBlockSetDetailsTypeDef(TypedDict):
    Ipv6CidrBlock: NotRequired[str]

class VpcInfoPeeringOptionsDetailsTypeDef(TypedDict):
    AllowDnsResolutionFromRemoteVpc: NotRequired[bool]
    AllowEgressFromLocalClassicLinkToRemoteVpc: NotRequired[bool]
    AllowEgressFromLocalVpcToRemoteClassicLink: NotRequired[bool]

class AwsEc2VpnConnectionRoutesDetailsTypeDef(TypedDict):
    DestinationCidrBlock: NotRequired[str]
    State: NotRequired[str]

class AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef(TypedDict):
    AcceptedRouteCount: NotRequired[int]
    CertificateArn: NotRequired[str]
    LastStatusChange: NotRequired[str]
    OutsideIpAddress: NotRequired[str]
    Status: NotRequired[str]
    StatusMessage: NotRequired[str]

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef(TypedDict):
    DpdTimeoutSeconds: NotRequired[int]
    IkeVersions: NotRequired[List[str]]
    OutsideIpAddress: NotRequired[str]
    Phase1DhGroupNumbers: NotRequired[List[int]]
    Phase1EncryptionAlgorithms: NotRequired[List[str]]
    Phase1IntegrityAlgorithms: NotRequired[List[str]]
    Phase1LifetimeSeconds: NotRequired[int]
    Phase2DhGroupNumbers: NotRequired[List[int]]
    Phase2EncryptionAlgorithms: NotRequired[List[str]]
    Phase2IntegrityAlgorithms: NotRequired[List[str]]
    Phase2LifetimeSeconds: NotRequired[int]
    PreSharedKey: NotRequired[str]
    RekeyFuzzPercentage: NotRequired[int]
    RekeyMarginTimeSeconds: NotRequired[int]
    ReplayWindowSize: NotRequired[int]
    TunnelInsideCidr: NotRequired[str]

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef(TypedDict):
    DpdTimeoutSeconds: NotRequired[int]
    IkeVersions: NotRequired[Sequence[str]]
    OutsideIpAddress: NotRequired[str]
    Phase1DhGroupNumbers: NotRequired[Sequence[int]]
    Phase1EncryptionAlgorithms: NotRequired[Sequence[str]]
    Phase1IntegrityAlgorithms: NotRequired[Sequence[str]]
    Phase1LifetimeSeconds: NotRequired[int]
    Phase2DhGroupNumbers: NotRequired[Sequence[int]]
    Phase2EncryptionAlgorithms: NotRequired[Sequence[str]]
    Phase2IntegrityAlgorithms: NotRequired[Sequence[str]]
    Phase2LifetimeSeconds: NotRequired[int]
    PreSharedKey: NotRequired[str]
    RekeyFuzzPercentage: NotRequired[int]
    RekeyMarginTimeSeconds: NotRequired[int]
    ReplayWindowSize: NotRequired[int]
    TunnelInsideCidr: NotRequired[str]

class AwsEcrContainerImageDetailsOutputTypeDef(TypedDict):
    RegistryId: NotRequired[str]
    RepositoryName: NotRequired[str]
    Architecture: NotRequired[str]
    ImageDigest: NotRequired[str]
    ImageTags: NotRequired[List[str]]
    ImagePublishedAt: NotRequired[str]

class AwsEcrContainerImageDetailsTypeDef(TypedDict):
    RegistryId: NotRequired[str]
    RepositoryName: NotRequired[str]
    Architecture: NotRequired[str]
    ImageDigest: NotRequired[str]
    ImageTags: NotRequired[Sequence[str]]
    ImagePublishedAt: NotRequired[str]

class AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef(TypedDict):
    ScanOnPush: NotRequired[bool]

class AwsEcrRepositoryLifecyclePolicyDetailsTypeDef(TypedDict):
    LifecyclePolicyText: NotRequired[str]
    RegistryId: NotRequired[str]

class AwsEcsClusterClusterSettingsDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef(
    TypedDict
):
    CloudWatchEncryptionEnabled: NotRequired[bool]
    CloudWatchLogGroupName: NotRequired[str]
    S3BucketName: NotRequired[str]
    S3EncryptionEnabled: NotRequired[bool]
    S3KeyPrefix: NotRequired[str]

class AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef(TypedDict):
    Base: NotRequired[int]
    CapacityProvider: NotRequired[str]
    Weight: NotRequired[int]

class AwsMountPointTypeDef(TypedDict):
    SourceVolume: NotRequired[str]
    ContainerPath: NotRequired[str]

class AwsEcsServiceCapacityProviderStrategyDetailsTypeDef(TypedDict):
    Base: NotRequired[int]
    CapacityProvider: NotRequired[str]
    Weight: NotRequired[int]

class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef(TypedDict):
    Enable: NotRequired[bool]
    Rollback: NotRequired[bool]

AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)

class AwsEcsServiceLoadBalancersDetailsTypeDef(TypedDict):
    ContainerName: NotRequired[str]
    ContainerPort: NotRequired[int]
    LoadBalancerName: NotRequired[str]
    TargetGroupArn: NotRequired[str]

AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AwsEcsServiceServiceRegistriesDetailsTypeDef(TypedDict):
    ContainerName: NotRequired[str]
    ContainerPort: NotRequired[int]
    Port: NotRequired[int]
    RegistryArn: NotRequired[str]

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef(TypedDict):
    AssignPublicIp: NotRequired[str]
    SecurityGroups: NotRequired[List[str]]
    Subnets: NotRequired[List[str]]

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef(TypedDict):
    AssignPublicIp: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]
    Subnets: NotRequired[Sequence[str]]

class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef(TypedDict):
    Condition: NotRequired[str]
    ContainerName: NotRequired[str]

class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef(TypedDict):
    Hostname: NotRequired[str]
    IpAddress: NotRequired[str]

AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef",
    {
        "Options": NotRequired[Dict[str, str]],
        "Type": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef(TypedDict):
    Command: NotRequired[List[str]]
    Interval: NotRequired[int]
    Retries: NotRequired[int]
    StartPeriod: NotRequired[int]
    Timeout: NotRequired[int]

AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "SourceVolume": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": NotRequired[int],
        "HostPort": NotRequired[int],
        "Protocol": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef(TypedDict):
    CredentialsParameter: NotRequired[str]

AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    ValueFrom: NotRequired[str]

class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef(TypedDict):
    Namespace: NotRequired[str]
    Value: NotRequired[str]

class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef(TypedDict):
    HardLimit: NotRequired[int]
    Name: NotRequired[str]
    SoftLimit: NotRequired[int]

AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": NotRequired[bool],
        "SourceContainer": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef(TypedDict):
    Command: NotRequired[Sequence[str]]
    Interval: NotRequired[int]
    Retries: NotRequired[int]
    StartPeriod: NotRequired[int]
    Timeout: NotRequired[int]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef(
    TypedDict
):
    Add: NotRequired[List[str]]
    Drop: NotRequired[List[str]]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef(TypedDict):
    Add: NotRequired[Sequence[str]]
    Drop: NotRequired[Sequence[str]]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef(TypedDict):
    ContainerPath: NotRequired[str]
    HostPath: NotRequired[str]
    Permissions: NotRequired[List[str]]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef(TypedDict):
    ContainerPath: NotRequired[str]
    MountOptions: NotRequired[List[str]]
    Size: NotRequired[int]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef(TypedDict):
    ContainerPath: NotRequired[str]
    HostPath: NotRequired[str]
    Permissions: NotRequired[Sequence[str]]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef(TypedDict):
    ContainerPath: NotRequired[str]
    MountOptions: NotRequired[Sequence[str]]
    Size: NotRequired[int]

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef(
    TypedDict
):
    Name: NotRequired[str]
    ValueFrom: NotRequired[str]

class AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef(TypedDict):
    DeviceName: NotRequired[str]
    DeviceType: NotRequired[str]

AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef(TypedDict):
    Autoprovision: NotRequired[bool]
    Driver: NotRequired[str]
    DriverOpts: NotRequired[Dict[str, str]]
    Labels: NotRequired[Dict[str, str]]
    Scope: NotRequired[str]

class AwsEcsTaskDefinitionVolumesHostDetailsTypeDef(TypedDict):
    SourcePath: NotRequired[str]

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef(TypedDict):
    Autoprovision: NotRequired[bool]
    Driver: NotRequired[str]
    DriverOpts: NotRequired[Mapping[str, str]]
    Labels: NotRequired[Mapping[str, str]]
    Scope: NotRequired[str]

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef(TypedDict):
    AccessPointId: NotRequired[str]
    Iam: NotRequired[str]

class AwsEcsTaskVolumeHostDetailsTypeDef(TypedDict):
    SourcePath: NotRequired[str]

class AwsEfsAccessPointPosixUserDetailsOutputTypeDef(TypedDict):
    Gid: NotRequired[str]
    SecondaryGids: NotRequired[List[str]]
    Uid: NotRequired[str]

class AwsEfsAccessPointPosixUserDetailsTypeDef(TypedDict):
    Gid: NotRequired[str]
    SecondaryGids: NotRequired[Sequence[str]]
    Uid: NotRequired[str]

class AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef(TypedDict):
    OwnerGid: NotRequired[str]
    OwnerUid: NotRequired[str]
    Permissions: NotRequired[str]

class AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]
    EndpointPublicAccess: NotRequired[bool]

class AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Types: NotRequired[List[str]]

class AwsEksClusterLoggingClusterLoggingDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Types: NotRequired[Sequence[str]]

class AwsEksClusterResourcesVpcConfigDetailsTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]
    EndpointPublicAccess: NotRequired[bool]

class AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    LinkName: NotRequired[str]

class AwsElasticBeanstalkEnvironmentOptionSettingTypeDef(TypedDict):
    Namespace: NotRequired[str]
    OptionName: NotRequired[str]
    ResourceName: NotRequired[str]
    Value: NotRequired[str]

AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)

class AwsElasticsearchDomainDomainEndpointOptionsTypeDef(TypedDict):
    EnforceHTTPS: NotRequired[bool]
    TLSSecurityPolicy: NotRequired[str]

class AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    KmsKeyId: NotRequired[str]

class AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsElasticsearchDomainServiceSoftwareOptionsTypeDef(TypedDict):
    AutomatedUpdateDate: NotRequired[str]
    Cancellable: NotRequired[bool]
    CurrentVersion: NotRequired[str]
    Description: NotRequired[str]
    NewVersion: NotRequired[str]
    UpdateAvailable: NotRequired[bool]
    UpdateStatus: NotRequired[str]

class AwsElasticsearchDomainVPCOptionsOutputTypeDef(TypedDict):
    AvailabilityZones: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]
    VPCId: NotRequired[str]

class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef(TypedDict):
    AvailabilityZoneCount: NotRequired[int]

class AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[str]
    Enabled: NotRequired[bool]

class AwsElasticsearchDomainVPCOptionsTypeDef(TypedDict):
    AvailabilityZones: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]
    VPCId: NotRequired[str]

class AwsElbAppCookieStickinessPolicyTypeDef(TypedDict):
    CookieName: NotRequired[str]
    PolicyName: NotRequired[str]

class AwsElbLbCookieStickinessPolicyTypeDef(TypedDict):
    CookieExpirationPeriod: NotRequired[int]
    PolicyName: NotRequired[str]

class AwsElbLoadBalancerAccessLogTypeDef(TypedDict):
    EmitInterval: NotRequired[int]
    Enabled: NotRequired[bool]
    S3BucketName: NotRequired[str]
    S3BucketPrefix: NotRequired[str]

class AwsElbLoadBalancerAdditionalAttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class AwsElbLoadBalancerConnectionDrainingTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Timeout: NotRequired[int]

class AwsElbLoadBalancerConnectionSettingsTypeDef(TypedDict):
    IdleTimeout: NotRequired[int]

class AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef(TypedDict):
    InstancePort: NotRequired[int]
    PolicyNames: NotRequired[List[str]]

class AwsElbLoadBalancerBackendServerDescriptionTypeDef(TypedDict):
    InstancePort: NotRequired[int]
    PolicyNames: NotRequired[Sequence[str]]

class AwsElbLoadBalancerHealthCheckTypeDef(TypedDict):
    HealthyThreshold: NotRequired[int]
    Interval: NotRequired[int]
    Target: NotRequired[str]
    Timeout: NotRequired[int]
    UnhealthyThreshold: NotRequired[int]

class AwsElbLoadBalancerInstanceTypeDef(TypedDict):
    InstanceId: NotRequired[str]

class AwsElbLoadBalancerSourceSecurityGroupTypeDef(TypedDict):
    GroupName: NotRequired[str]
    OwnerAlias: NotRequired[str]

AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": NotRequired[int],
        "InstanceProtocol": NotRequired[str],
        "LoadBalancerPort": NotRequired[int],
        "Protocol": NotRequired[str],
        "SslCertificateId": NotRequired[str],
    },
)

class AwsElbv2LoadBalancerAttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class LoadBalancerStateTypeDef(TypedDict):
    Code: NotRequired[str]
    Reason: NotRequired[str]

class AwsEventSchemasRegistryDetailsTypeDef(TypedDict):
    Description: NotRequired[str]
    RegistryArn: NotRequired[str]
    RegistryName: NotRequired[str]

class AwsEventsEndpointEventBusesDetailsTypeDef(TypedDict):
    EventBusArn: NotRequired[str]

class AwsEventsEndpointReplicationConfigDetailsTypeDef(TypedDict):
    State: NotRequired[str]

class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef(TypedDict):
    HealthCheck: NotRequired[str]

class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef(TypedDict):
    Route: NotRequired[str]

class AwsEventsEventbusDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Policy: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef(TypedDict):
    Status: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef(TypedDict):
    Status: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef(TypedDict):
    Status: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef(TypedDict):
    Status: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef(TypedDict):
    Status: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef(
    TypedDict
):
    Reason: NotRequired[str]
    Status: NotRequired[str]

class AwsGuardDutyDetectorFeaturesDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Status: NotRequired[str]

class AwsIamAccessKeySessionContextAttributesTypeDef(TypedDict):
    MfaAuthenticated: NotRequired[bool]
    CreationDate: NotRequired[str]

AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Arn": NotRequired[str],
        "AccountId": NotRequired[str],
        "UserName": NotRequired[str],
    },
)

class AwsIamAttachedManagedPolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]
    PolicyArn: NotRequired[str]

class AwsIamGroupPolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]

class AwsIamInstanceProfileRoleTypeDef(TypedDict):
    Arn: NotRequired[str]
    AssumeRolePolicyDocument: NotRequired[str]
    CreateDate: NotRequired[str]
    Path: NotRequired[str]
    RoleId: NotRequired[str]
    RoleName: NotRequired[str]

class AwsIamPermissionsBoundaryTypeDef(TypedDict):
    PermissionsBoundaryArn: NotRequired[str]
    PermissionsBoundaryType: NotRequired[str]

class AwsIamPolicyVersionTypeDef(TypedDict):
    VersionId: NotRequired[str]
    IsDefaultVersion: NotRequired[bool]
    CreateDate: NotRequired[str]

class AwsIamRolePolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]

class AwsIamUserPolicyTypeDef(TypedDict):
    PolicyName: NotRequired[str]

class AwsKinesisStreamStreamEncryptionDetailsTypeDef(TypedDict):
    EncryptionType: NotRequired[str]
    KeyId: NotRequired[str]

class AwsKmsKeyDetailsTypeDef(TypedDict):
    AWSAccountId: NotRequired[str]
    CreationDate: NotRequired[float]
    KeyId: NotRequired[str]
    KeyManager: NotRequired[str]
    KeyState: NotRequired[str]
    Origin: NotRequired[str]
    Description: NotRequired[str]
    KeyRotationStatus: NotRequired[bool]

class AwsLambdaFunctionCodeTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3ObjectVersion: NotRequired[str]
    ZipFile: NotRequired[str]

class AwsLambdaFunctionDeadLetterConfigTypeDef(TypedDict):
    TargetArn: NotRequired[str]

class AwsLambdaFunctionLayerTypeDef(TypedDict):
    Arn: NotRequired[str]
    CodeSize: NotRequired[int]

class AwsLambdaFunctionTracingConfigTypeDef(TypedDict):
    Mode: NotRequired[str]

class AwsLambdaFunctionVpcConfigOutputTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]
    VpcId: NotRequired[str]

class AwsLambdaFunctionEnvironmentErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class AwsLambdaFunctionVpcConfigTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]
    VpcId: NotRequired[str]

class AwsLambdaLayerVersionDetailsOutputTypeDef(TypedDict):
    Version: NotRequired[int]
    CompatibleRuntimes: NotRequired[List[str]]
    CreatedDate: NotRequired[str]

class AwsLambdaLayerVersionDetailsTypeDef(TypedDict):
    Version: NotRequired[int]
    CompatibleRuntimes: NotRequired[Sequence[str]]
    CreatedDate: NotRequired[str]

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef(TypedDict):
    CertificateAuthorityArnList: NotRequired[List[str]]
    Enabled: NotRequired[bool]

class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef(TypedDict):
    CertificateAuthorityArnList: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]

class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef(TypedDict):
    DataVolumeKMSKeyId: NotRequired[str]

class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef(TypedDict):
    InCluster: NotRequired[bool]
    ClientBroker: NotRequired[str]

class AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef(TypedDict):
    SubnetId: NotRequired[str]

class AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef(TypedDict):
    MasterUserArn: NotRequired[str]
    MasterUserName: NotRequired[str]
    MasterUserPassword: NotRequired[str]

class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef(TypedDict):
    AvailabilityZoneCount: NotRequired[int]

class AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef(TypedDict):
    CustomEndpointCertificateArn: NotRequired[str]
    CustomEndpointEnabled: NotRequired[bool]
    EnforceHTTPS: NotRequired[bool]
    CustomEndpoint: NotRequired[str]
    TLSSecurityPolicy: NotRequired[str]

class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    KmsKeyId: NotRequired[str]

class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef(TypedDict):
    AutomatedUpdateDate: NotRequired[str]
    Cancellable: NotRequired[bool]
    CurrentVersion: NotRequired[str]
    Description: NotRequired[str]
    NewVersion: NotRequired[str]
    UpdateAvailable: NotRequired[bool]
    UpdateStatus: NotRequired[str]
    OptionalDeployment: NotRequired[bool]

class AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]

class AwsOpenSearchServiceDomainLogPublishingOptionTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[str]
    Enabled: NotRequired[bool]

class AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef(TypedDict):
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]

class AwsRdsDbClusterAssociatedRoleTypeDef(TypedDict):
    RoleArn: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbClusterMemberTypeDef(TypedDict):
    IsClusterWriter: NotRequired[bool]
    PromotionTier: NotRequired[int]
    DbInstanceIdentifier: NotRequired[str]
    DbClusterParameterGroupStatus: NotRequired[str]

class AwsRdsDbClusterOptionGroupMembershipTypeDef(TypedDict):
    DbClusterOptionGroupName: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbDomainMembershipTypeDef(TypedDict):
    Domain: NotRequired[str]
    Status: NotRequired[str]
    Fqdn: NotRequired[str]
    IamRoleName: NotRequired[str]

class AwsRdsDbInstanceVpcSecurityGroupTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeValues: NotRequired[List[str]]

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeValues: NotRequired[Sequence[str]]

class AwsRdsDbInstanceAssociatedRoleTypeDef(TypedDict):
    RoleArn: NotRequired[str]
    FeatureName: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbInstanceEndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]
    HostedZoneId: NotRequired[str]

class AwsRdsDbOptionGroupMembershipTypeDef(TypedDict):
    OptionGroupName: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbParameterGroupTypeDef(TypedDict):
    DbParameterGroupName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]

class AwsRdsDbProcessorFeatureTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class AwsRdsDbStatusInfoTypeDef(TypedDict):
    StatusType: NotRequired[str]
    Normal: NotRequired[bool]
    Status: NotRequired[str]
    Message: NotRequired[str]

class AwsRdsPendingCloudWatchLogsExportsOutputTypeDef(TypedDict):
    LogTypesToEnable: NotRequired[List[str]]
    LogTypesToDisable: NotRequired[List[str]]

class AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef(TypedDict):
    Ec2SecurityGroupId: NotRequired[str]
    Ec2SecurityGroupName: NotRequired[str]
    Ec2SecurityGroupOwnerId: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbSecurityGroupIpRangeTypeDef(TypedDict):
    CidrIp: NotRequired[str]
    Status: NotRequired[str]

class AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]

class AwsRdsEventSubscriptionDetailsOutputTypeDef(TypedDict):
    CustSubscriptionId: NotRequired[str]
    CustomerAwsId: NotRequired[str]
    Enabled: NotRequired[bool]
    EventCategoriesList: NotRequired[List[str]]
    EventSubscriptionArn: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    SourceIdsList: NotRequired[List[str]]
    SourceType: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionCreationTime: NotRequired[str]

class AwsRdsEventSubscriptionDetailsTypeDef(TypedDict):
    CustSubscriptionId: NotRequired[str]
    CustomerAwsId: NotRequired[str]
    Enabled: NotRequired[bool]
    EventCategoriesList: NotRequired[Sequence[str]]
    EventSubscriptionArn: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    SourceIdsList: NotRequired[Sequence[str]]
    SourceType: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionCreationTime: NotRequired[str]

class AwsRdsPendingCloudWatchLogsExportsTypeDef(TypedDict):
    LogTypesToEnable: NotRequired[Sequence[str]]
    LogTypesToDisable: NotRequired[Sequence[str]]

class AwsRedshiftClusterClusterNodeTypeDef(TypedDict):
    NodeRole: NotRequired[str]
    PrivateIpAddress: NotRequired[str]
    PublicIpAddress: NotRequired[str]

class AwsRedshiftClusterClusterParameterStatusTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]
    ParameterApplyErrorDescription: NotRequired[str]

class AwsRedshiftClusterClusterSecurityGroupTypeDef(TypedDict):
    ClusterSecurityGroupName: NotRequired[str]
    Status: NotRequired[str]

class AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef(TypedDict):
    DestinationRegion: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    RetentionPeriod: NotRequired[int]
    SnapshotCopyGrantName: NotRequired[str]

class AwsRedshiftClusterDeferredMaintenanceWindowTypeDef(TypedDict):
    DeferMaintenanceEndTime: NotRequired[str]
    DeferMaintenanceIdentifier: NotRequired[str]
    DeferMaintenanceStartTime: NotRequired[str]

class AwsRedshiftClusterElasticIpStatusTypeDef(TypedDict):
    ElasticIp: NotRequired[str]
    Status: NotRequired[str]

class AwsRedshiftClusterEndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]

class AwsRedshiftClusterHsmStatusTypeDef(TypedDict):
    HsmClientCertificateIdentifier: NotRequired[str]
    HsmConfigurationIdentifier: NotRequired[str]
    Status: NotRequired[str]

class AwsRedshiftClusterIamRoleTypeDef(TypedDict):
    ApplyStatus: NotRequired[str]
    IamRoleArn: NotRequired[str]

class AwsRedshiftClusterLoggingStatusTypeDef(TypedDict):
    BucketName: NotRequired[str]
    LastFailureMessage: NotRequired[str]
    LastFailureTime: NotRequired[str]
    LastSuccessfulDeliveryTime: NotRequired[str]
    LoggingEnabled: NotRequired[bool]
    S3KeyPrefix: NotRequired[str]

class AwsRedshiftClusterPendingModifiedValuesTypeDef(TypedDict):
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    ClusterIdentifier: NotRequired[str]
    ClusterType: NotRequired[str]
    ClusterVersion: NotRequired[str]
    EncryptionType: NotRequired[str]
    EnhancedVpcRouting: NotRequired[bool]
    MaintenanceTrackName: NotRequired[str]
    MasterUserPassword: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    PubliclyAccessible: NotRequired[bool]

class AwsRedshiftClusterResizeInfoTypeDef(TypedDict):
    AllowCancelResize: NotRequired[bool]
    ResizeType: NotRequired[str]

class AwsRedshiftClusterRestoreStatusTypeDef(TypedDict):
    CurrentRestoreRateInMegaBytesPerSecond: NotRequired[float]
    ElapsedTimeInSeconds: NotRequired[int]
    EstimatedTimeToCompletionInSeconds: NotRequired[int]
    ProgressInMegaBytes: NotRequired[int]
    SnapshotSizeInMegaBytes: NotRequired[int]
    Status: NotRequired[str]

class AwsRedshiftClusterVpcSecurityGroupTypeDef(TypedDict):
    Status: NotRequired[str]
    VpcSecurityGroupId: NotRequired[str]

class AwsRoute53HostedZoneConfigDetailsTypeDef(TypedDict):
    Comment: NotRequired[str]

class AwsRoute53HostedZoneVpcDetailsTypeDef(TypedDict):
    Id: NotRequired[str]
    Region: NotRequired[str]

class CloudWatchLogsLogGroupArnConfigDetailsTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[str]
    HostedZoneId: NotRequired[str]
    Id: NotRequired[str]

class AwsS3AccessPointVpcConfigurationDetailsTypeDef(TypedDict):
    VpcId: NotRequired[str]

class AwsS3AccountPublicAccessBlockDetailsTypeDef(TypedDict):
    BlockPublicAcls: NotRequired[bool]
    BlockPublicPolicy: NotRequired[bool]
    IgnorePublicAcls: NotRequired[bool]
    RestrictPublicBuckets: NotRequired[bool]

class AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef(
    TypedDict
):
    DaysAfterInitiation: NotRequired[int]

class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef(
    TypedDict
):
    Days: NotRequired[int]
    StorageClass: NotRequired[str]

class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef(TypedDict):
    Date: NotRequired[str]
    Days: NotRequired[int]
    StorageClass: NotRequired[str]

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef(
    TypedDict
):
    Key: NotRequired[str]
    Value: NotRequired[str]

class AwsS3BucketBucketVersioningConfigurationTypeDef(TypedDict):
    IsMfaDeleteEnabled: NotRequired[bool]
    Status: NotRequired[str]

class AwsS3BucketLoggingConfigurationTypeDef(TypedDict):
    DestinationBucketName: NotRequired[str]
    LogFilePrefix: NotRequired[str]

class AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef(TypedDict):
    Name: NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType]
    Value: NotRequired[str]

class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef(TypedDict):
    Days: NotRequired[int]
    Mode: NotRequired[str]
    Years: NotRequired[int]

class AwsS3BucketServerSideEncryptionByDefaultTypeDef(TypedDict):
    SSEAlgorithm: NotRequired[str]
    KMSMasterKeyID: NotRequired[str]

AwsS3BucketWebsiteConfigurationRedirectToTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    {
        "Hostname": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)

class AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef(TypedDict):
    HttpErrorCodeReturnedEquals: NotRequired[str]
    KeyPrefixEquals: NotRequired[str]

AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    {
        "Hostname": NotRequired[str],
        "HttpRedirectCode": NotRequired[str],
        "Protocol": NotRequired[str],
        "ReplaceKeyPrefixWith": NotRequired[str],
        "ReplaceKeyWith": NotRequired[str],
    },
)

class AwsS3ObjectDetailsTypeDef(TypedDict):
    LastModified: NotRequired[str]
    ETag: NotRequired[str]
    VersionId: NotRequired[str]
    ContentType: NotRequired[str]
    ServerSideEncryption: NotRequired[str]
    SSEKMSKeyId: NotRequired[str]

class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef(TypedDict):
    MinimumInstanceMetadataServiceVersion: NotRequired[str]

class AwsSecretsManagerSecretRotationRulesTypeDef(TypedDict):
    AutomaticallyAfterDays: NotRequired[int]

class BooleanFilterTypeDef(TypedDict):
    Value: NotRequired[bool]

class IpFilterTypeDef(TypedDict):
    Cidr: NotRequired[str]

class KeywordFilterTypeDef(TypedDict):
    Value: NotRequired[str]

class AwsSecurityFindingIdentifierTypeDef(TypedDict):
    Id: str
    ProductArn: str

class GeneratorDetailsOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Labels: NotRequired[List[str]]

MalwareTypeDef = TypedDict(
    "MalwareTypeDef",
    {
        "Name": str,
        "Type": NotRequired[MalwareTypeType],
        "Path": NotRequired[str],
        "State": NotRequired[MalwareStateType],
    },
)
NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)

class PatchSummaryTypeDef(TypedDict):
    Id: str
    InstalledCount: NotRequired[int]
    MissingCount: NotRequired[int]
    FailedCount: NotRequired[int]
    InstalledOtherCount: NotRequired[int]
    InstalledRejectedCount: NotRequired[int]
    InstalledPendingReboot: NotRequired[int]
    OperationStartTime: NotRequired[str]
    OperationEndTime: NotRequired[str]
    RebootOption: NotRequired[str]
    Operation: NotRequired[str]

class ProcessDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Path: NotRequired[str]
    Pid: NotRequired[int]
    ParentPid: NotRequired[int]
    LaunchedAt: NotRequired[str]
    TerminatedAt: NotRequired[str]

class SeverityTypeDef(TypedDict):
    Product: NotRequired[float]
    Label: NotRequired[SeverityLabelType]
    Normalized: NotRequired[int]
    Original: NotRequired[str]

ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": NotRequired[ThreatIntelIndicatorTypeType],
        "Value": NotRequired[str],
        "Category": NotRequired[ThreatIntelIndicatorCategoryType],
        "LastObservedAt": NotRequired[str],
        "Source": NotRequired[str],
        "SourceUrl": NotRequired[str],
    },
)

class WorkflowTypeDef(TypedDict):
    Status: NotRequired[WorkflowStatusType]

AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)

class AwsSqsQueueDetailsTypeDef(TypedDict):
    KmsDataKeyReusePeriodSeconds: NotRequired[int]
    KmsMasterKeyId: NotRequired[str]
    QueueName: NotRequired[str]
    DeadLetterTargetArn: NotRequired[str]

class AwsSsmComplianceSummaryTypeDef(TypedDict):
    Status: NotRequired[str]
    CompliantCriticalCount: NotRequired[int]
    CompliantHighCount: NotRequired[int]
    CompliantMediumCount: NotRequired[int]
    ExecutionType: NotRequired[str]
    NonCompliantCriticalCount: NotRequired[int]
    CompliantInformationalCount: NotRequired[int]
    NonCompliantInformationalCount: NotRequired[int]
    CompliantUnspecifiedCount: NotRequired[int]
    NonCompliantLowCount: NotRequired[int]
    NonCompliantHighCount: NotRequired[int]
    CompliantLowCount: NotRequired[int]
    ComplianceType: NotRequired[str]
    PatchBaselineId: NotRequired[str]
    OverallSeverity: NotRequired[str]
    NonCompliantMediumCount: NotRequired[int]
    NonCompliantUnspecifiedCount: NotRequired[int]
    PatchGroup: NotRequired[str]

class AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef(
    TypedDict
):
    LogGroupArn: NotRequired[str]

AwsWafRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)

class WafExcludedRuleTypeDef(TypedDict):
    RuleId: NotRequired[str]

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)

class AwsWafv2CustomHttpHeaderTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class AwsWafv2VisibilityConfigDetailsTypeDef(TypedDict):
    CloudWatchMetricsEnabled: NotRequired[bool]
    MetricName: NotRequired[str]
    SampledRequestsEnabled: NotRequired[bool]

class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef(TypedDict):
    ImmunityTime: NotRequired[int]

AwsXrayEncryptionConfigDetailsTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class BatchDeleteAutomationRulesRequestTypeDef(TypedDict):
    AutomationRulesArns: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UnprocessedAutomationRuleTypeDef(TypedDict):
    RuleArn: NotRequired[str]
    ErrorCode: NotRequired[int]
    ErrorMessage: NotRequired[str]

class BatchDisableStandardsRequestTypeDef(TypedDict):
    StandardsSubscriptionArns: Sequence[str]

class StandardsSubscriptionRequestTypeDef(TypedDict):
    StandardsArn: str
    StandardsInput: NotRequired[Mapping[str, str]]

class BatchGetAutomationRulesRequestTypeDef(TypedDict):
    AutomationRulesArns: Sequence[str]

class ConfigurationPolicyAssociationSummaryTypeDef(TypedDict):
    ConfigurationPolicyId: NotRequired[str]
    TargetId: NotRequired[str]
    TargetType: NotRequired[TargetTypeType]
    AssociationType: NotRequired[AssociationTypeType]
    UpdatedAt: NotRequired[datetime]
    AssociationStatus: NotRequired[ConfigurationPolicyAssociationStatusType]
    AssociationStatusMessage: NotRequired[str]

class BatchGetSecurityControlsRequestTypeDef(TypedDict):
    SecurityControlIds: Sequence[str]

class UnprocessedSecurityControlTypeDef(TypedDict):
    SecurityControlId: str
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: NotRequired[str]

class StandardsControlAssociationIdTypeDef(TypedDict):
    SecurityControlId: str
    StandardsArn: str

class StandardsControlAssociationDetailTypeDef(TypedDict):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: NotRequired[List[str]]
    UpdatedAt: NotRequired[datetime]
    UpdatedReason: NotRequired[str]
    StandardsControlTitle: NotRequired[str]
    StandardsControlDescription: NotRequired[str]
    StandardsControlArns: NotRequired[List[str]]

class ImportFindingsErrorTypeDef(TypedDict):
    Id: str
    ErrorCode: str
    ErrorMessage: str

class StandardsControlAssociationUpdateTypeDef(TypedDict):
    StandardsArn: str
    SecurityControlId: str
    AssociationStatus: AssociationStatusType
    UpdatedReason: NotRequired[str]

class BooleanConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[bool]

class CellTypeDef(TypedDict):
    Column: NotRequired[int]
    Row: NotRequired[int]
    ColumnName: NotRequired[str]
    CellReference: NotRequired[str]

class ClassificationStatusTypeDef(TypedDict):
    Code: NotRequired[str]
    Reason: NotRequired[str]

class CodeVulnerabilitiesFilePathTypeDef(TypedDict):
    EndLine: NotRequired[int]
    FileName: NotRequired[str]
    FilePath: NotRequired[str]
    StartLine: NotRequired[int]

class SecurityControlParameterOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[List[str]]

class StatusReasonTypeDef(TypedDict):
    ReasonCode: str
    Description: NotRequired[str]

class DoubleConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[float]
    Min: NotRequired[float]
    Max: NotRequired[float]

class EnumConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    AllowedValues: NotRequired[List[str]]

class EnumListConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[List[str]]
    MaxItems: NotRequired[int]
    AllowedValues: NotRequired[List[str]]

class IntegerConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[int]
    Min: NotRequired[int]
    Max: NotRequired[int]

class IntegerListConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[List[int]]
    Min: NotRequired[int]
    Max: NotRequired[int]
    MaxItems: NotRequired[int]

class StringConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    Re2Expression: NotRequired[str]
    ExpressionDescription: NotRequired[str]

class StringListConfigurationOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[List[str]]
    Re2Expression: NotRequired[str]
    MaxItems: NotRequired[int]
    ExpressionDescription: NotRequired[str]

class TargetTypeDef(TypedDict):
    AccountId: NotRequired[str]
    OrganizationalUnitId: NotRequired[str]
    RootId: NotRequired[str]

class ConfigurationPolicySummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    UpdatedAt: NotRequired[datetime]
    ServiceEnabled: NotRequired[bool]

class VolumeMountTypeDef(TypedDict):
    Name: NotRequired[str]
    MountPath: NotRequired[str]

class CreateActionTargetRequestTypeDef(TypedDict):
    Name: str
    Description: str
    Id: str

class CreateFindingAggregatorRequestTypeDef(TypedDict):
    RegionLinkingMode: str
    Regions: NotRequired[Sequence[str]]

class ResultTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ProcessingResult: NotRequired[str]

class DateRangeTypeDef(TypedDict):
    Value: NotRequired[int]
    Unit: NotRequired[Literal["DAYS"]]

class DeclineInvitationsRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class DeleteActionTargetRequestTypeDef(TypedDict):
    ActionTargetArn: str

class DeleteConfigurationPolicyRequestTypeDef(TypedDict):
    Identifier: str

class DeleteFindingAggregatorRequestTypeDef(TypedDict):
    FindingAggregatorArn: str

class DeleteInsightRequestTypeDef(TypedDict):
    InsightArn: str

class DeleteInvitationsRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class DeleteMembersRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeActionTargetsRequestTypeDef(TypedDict):
    ActionTargetArns: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeHubRequestTypeDef(TypedDict):
    HubArn: NotRequired[str]

class OrganizationConfigurationTypeDef(TypedDict):
    ConfigurationType: NotRequired[OrganizationConfigurationConfigurationTypeType]
    Status: NotRequired[OrganizationConfigurationStatusType]
    StatusMessage: NotRequired[str]

class DescribeProductsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ProductArn: NotRequired[str]

class ProductTypeDef(TypedDict):
    ProductArn: str
    ProductName: NotRequired[str]
    CompanyName: NotRequired[str]
    Description: NotRequired[str]
    Categories: NotRequired[List[str]]
    IntegrationTypes: NotRequired[List[IntegrationTypeType]]
    MarketplaceUrl: NotRequired[str]
    ActivationUrl: NotRequired[str]
    ProductSubscriptionResourcePolicy: NotRequired[str]

class DescribeStandardsControlsRequestTypeDef(TypedDict):
    StandardsSubscriptionArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class StandardsControlTypeDef(TypedDict):
    StandardsControlArn: NotRequired[str]
    ControlStatus: NotRequired[ControlStatusType]
    DisabledReason: NotRequired[str]
    ControlStatusUpdatedAt: NotRequired[datetime]
    ControlId: NotRequired[str]
    Title: NotRequired[str]
    Description: NotRequired[str]
    RemediationUrl: NotRequired[str]
    SeverityRating: NotRequired[SeverityRatingType]
    RelatedRequirements: NotRequired[List[str]]

class DescribeStandardsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DisableImportFindingsForProductRequestTypeDef(TypedDict):
    ProductSubscriptionArn: str

class DisableOrganizationAdminAccountRequestTypeDef(TypedDict):
    AdminAccountId: str

class DisassociateMembersRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class EnableImportFindingsForProductRequestTypeDef(TypedDict):
    ProductArn: str

class EnableOrganizationAdminAccountRequestTypeDef(TypedDict):
    AdminAccountId: str

class EnableSecurityHubRequestTypeDef(TypedDict):
    Tags: NotRequired[Mapping[str, str]]
    EnableDefaultStandards: NotRequired[bool]
    ControlFindingGenerator: NotRequired[ControlFindingGeneratorType]

class FilePathsTypeDef(TypedDict):
    FilePath: NotRequired[str]
    FileName: NotRequired[str]
    ResourceId: NotRequired[str]
    Hash: NotRequired[str]

class FindingAggregatorTypeDef(TypedDict):
    FindingAggregatorArn: NotRequired[str]

FindingHistoryUpdateSourceTypeDef = TypedDict(
    "FindingHistoryUpdateSourceTypeDef",
    {
        "Type": NotRequired[FindingHistoryUpdateSourceTypeType],
        "Identity": NotRequired[str],
    },
)

class FindingHistoryUpdateTypeDef(TypedDict):
    UpdatedField: NotRequired[str]
    OldValue: NotRequired[str]
    NewValue: NotRequired[str]

class FindingProviderSeverityTypeDef(TypedDict):
    Label: NotRequired[SeverityLabelType]
    Original: NotRequired[str]

class FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef(TypedDict):
    Priority: NotRequired[int]
    ResourceArn: NotRequired[str]

class GeneratorDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Labels: NotRequired[Sequence[str]]

class InvitationTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InvitationId: NotRequired[str]
    InvitedAt: NotRequired[datetime]
    MemberStatus: NotRequired[str]

class GetConfigurationPolicyRequestTypeDef(TypedDict):
    Identifier: str

class GetEnabledStandardsRequestTypeDef(TypedDict):
    StandardsSubscriptionArns: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetFindingAggregatorRequestTypeDef(TypedDict):
    FindingAggregatorArn: str

TimestampTypeDef = Union[datetime, str]

class SortCriterionTypeDef(TypedDict):
    Field: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]

class GetInsightResultsRequestTypeDef(TypedDict):
    InsightArn: str

class GetInsightsRequestTypeDef(TypedDict):
    InsightArns: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetMembersRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class MemberTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Email: NotRequired[str]
    MasterId: NotRequired[str]
    AdministratorId: NotRequired[str]
    MemberStatus: NotRequired[str]
    InvitedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class GetSecurityControlDefinitionRequestTypeDef(TypedDict):
    SecurityControlId: str

IndicatorOutputTypeDef = TypedDict(
    "IndicatorOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
        "Title": NotRequired[str],
        "Type": NotRequired[str],
    },
)
IndicatorTypeDef = TypedDict(
    "IndicatorTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "Title": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class InsightResultValueTypeDef(TypedDict):
    GroupByAttributeValue: str
    Count: int

class InviteMembersRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class ListAutomationRulesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListConfigurationPoliciesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEnabledProductsForImportRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListFindingAggregatorsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListInvitationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListMembersRequestTypeDef(TypedDict):
    OnlyAssociated: NotRequired[bool]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListOrganizationAdminAccountsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSecurityControlDefinitionsRequestTypeDef(TypedDict):
    StandardsArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListStandardsControlAssociationsRequestTypeDef(TypedDict):
    SecurityControlId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class StandardsControlAssociationSummaryTypeDef(TypedDict):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: NotRequired[List[str]]
    UpdatedAt: NotRequired[datetime]
    UpdatedReason: NotRequired[str]
    StandardsControlTitle: NotRequired[str]
    StandardsControlDescription: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class NetworkAutonomousSystemTypeDef(TypedDict):
    Name: NotRequired[str]
    Number: NotRequired[int]

class NetworkConnectionTypeDef(TypedDict):
    Direction: NotRequired[ConnectionDirectionType]

class NetworkGeoLocationTypeDef(TypedDict):
    City: NotRequired[str]
    Country: NotRequired[str]
    Lat: NotRequired[float]
    Lon: NotRequired[float]

class PortRangeTypeDef(TypedDict):
    Begin: NotRequired[int]
    End: NotRequired[int]

class RangeTypeDef(TypedDict):
    Start: NotRequired[int]
    End: NotRequired[int]
    StartColumn: NotRequired[int]

class RecordTypeDef(TypedDict):
    JsonPath: NotRequired[str]
    RecordIndex: NotRequired[int]

class ParameterValueOutputTypeDef(TypedDict):
    Integer: NotRequired[int]
    IntegerList: NotRequired[List[int]]
    Double: NotRequired[float]
    String: NotRequired[str]
    StringList: NotRequired[List[str]]
    Boolean: NotRequired[bool]
    Enum: NotRequired[str]
    EnumList: NotRequired[List[str]]

class ParameterValueTypeDef(TypedDict):
    Integer: NotRequired[int]
    IntegerList: NotRequired[Sequence[int]]
    Double: NotRequired[float]
    String: NotRequired[str]
    StringList: NotRequired[Sequence[str]]
    Boolean: NotRequired[bool]
    Enum: NotRequired[str]
    EnumList: NotRequired[Sequence[str]]

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": NotRequired[str],
        "Url": NotRequired[str],
    },
)

class RuleGroupSourceListDetailsOutputTypeDef(TypedDict):
    GeneratedRulesType: NotRequired[str]
    TargetTypes: NotRequired[List[str]]
    Targets: NotRequired[List[str]]

class RuleGroupSourceListDetailsTypeDef(TypedDict):
    GeneratedRulesType: NotRequired[str]
    TargetTypes: NotRequired[Sequence[str]]
    Targets: NotRequired[Sequence[str]]

RuleGroupSourceStatefulRulesHeaderDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    {
        "Destination": NotRequired[str],
        "DestinationPort": NotRequired[str],
        "Direction": NotRequired[str],
        "Protocol": NotRequired[str],
        "Source": NotRequired[str],
        "SourcePort": NotRequired[str],
    },
)

class RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef(TypedDict):
    Keyword: NotRequired[str]
    Settings: NotRequired[List[str]]

class RuleGroupSourceStatefulRulesOptionsDetailsTypeDef(TypedDict):
    Keyword: NotRequired[str]
    Settings: NotRequired[Sequence[str]]

class RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef(TypedDict):
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]

class RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef(TypedDict):
    AddressDefinition: NotRequired[str]

class RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef(TypedDict):
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]

class RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef(TypedDict):
    AddressDefinition: NotRequired[str]

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef(TypedDict):
    Flags: NotRequired[List[str]]
    Masks: NotRequired[List[str]]

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef(TypedDict):
    Flags: NotRequired[Sequence[str]]
    Masks: NotRequired[Sequence[str]]

class RuleGroupVariablesIpSetsDetailsOutputTypeDef(TypedDict):
    Definition: NotRequired[List[str]]

class RuleGroupVariablesIpSetsDetailsTypeDef(TypedDict):
    Definition: NotRequired[Sequence[str]]

class RuleGroupVariablesPortSetsDetailsOutputTypeDef(TypedDict):
    Definition: NotRequired[List[str]]

class RuleGroupVariablesPortSetsDetailsTypeDef(TypedDict):
    Definition: NotRequired[Sequence[str]]

class SecurityControlParameterTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[Sequence[str]]

class SoftwarePackageTypeDef(TypedDict):
    Name: NotRequired[str]
    Version: NotRequired[str]
    Epoch: NotRequired[str]
    Release: NotRequired[str]
    Architecture: NotRequired[str]
    PackageManager: NotRequired[str]
    FilePath: NotRequired[str]
    FixedInVersion: NotRequired[str]
    Remediation: NotRequired[str]
    SourceLayerHash: NotRequired[str]
    SourceLayerArn: NotRequired[str]

class StandardsManagedByTypeDef(TypedDict):
    Company: NotRequired[str]
    Product: NotRequired[str]

class StandardsStatusReasonTypeDef(TypedDict):
    StatusReasonCode: StatusReasonCodeType

class StatelessCustomPublishMetricActionDimensionTypeDef(TypedDict):
    Value: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateActionTargetRequestTypeDef(TypedDict):
    ActionTargetArn: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateFindingAggregatorRequestTypeDef(TypedDict):
    FindingAggregatorArn: str
    RegionLinkingMode: str
    Regions: NotRequired[Sequence[str]]

class UpdateSecurityHubConfigurationRequestTypeDef(TypedDict):
    AutoEnableControls: NotRequired[bool]
    ControlFindingGenerator: NotRequired[ControlFindingGeneratorType]

class UpdateStandardsControlRequestTypeDef(TypedDict):
    StandardsControlArn: str
    ControlStatus: NotRequired[ControlStatusType]
    DisabledReason: NotRequired[str]

class VulnerabilityVendorTypeDef(TypedDict):
    Name: str
    Url: NotRequired[str]
    VendorSeverity: NotRequired[str]
    VendorCreatedAt: NotRequired[str]
    VendorUpdatedAt: NotRequired[str]

class CreateMembersRequestTypeDef(TypedDict):
    AccountDetails: Sequence[AccountDetailsTypeDef]

class ActionRemoteIpDetailsTypeDef(TypedDict):
    IpAddressV4: NotRequired[str]
    Organization: NotRequired[IpOrganizationDetailsTypeDef]
    Country: NotRequired[CountryTypeDef]
    City: NotRequired[CityTypeDef]
    GeoLocation: NotRequired[GeoLocationTypeDef]

ActorUserTypeDef = TypedDict(
    "ActorUserTypeDef",
    {
        "Name": NotRequired[str],
        "Uid": NotRequired[str],
        "Type": NotRequired[str],
        "CredentialUid": NotRequired[str],
        "Account": NotRequired[UserAccountTypeDef],
    },
)

class CvssOutputTypeDef(TypedDict):
    Version: NotRequired[str]
    BaseScore: NotRequired[float]
    BaseVector: NotRequired[str]
    Source: NotRequired[str]
    Adjustments: NotRequired[List[AdjustmentTypeDef]]

class CvssTypeDef(TypedDict):
    Version: NotRequired[str]
    BaseScore: NotRequired[float]
    BaseVector: NotRequired[str]
    Source: NotRequired[str]
    Adjustments: NotRequired[Sequence[AdjustmentTypeDef]]

class ListConfigurationPolicyAssociationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[AssociationFiltersTypeDef]

class AssociationSetDetailsTypeDef(TypedDict):
    AssociationState: NotRequired[AssociationStateDetailsTypeDef]
    GatewayId: NotRequired[str]
    Main: NotRequired[bool]
    RouteTableAssociationId: NotRequired[str]
    RouteTableId: NotRequired[str]
    SubnetId: NotRequired[str]

class AutomationRulesFindingFieldsUpdateOutputTypeDef(TypedDict):
    Note: NotRequired[NoteUpdateTypeDef]
    Severity: NotRequired[SeverityUpdateTypeDef]
    VerificationState: NotRequired[VerificationStateType]
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    Types: NotRequired[List[str]]
    UserDefinedFields: NotRequired[Dict[str, str]]
    Workflow: NotRequired[WorkflowUpdateTypeDef]
    RelatedFindings: NotRequired[List[RelatedFindingTypeDef]]

class AutomationRulesFindingFieldsUpdateTypeDef(TypedDict):
    Note: NotRequired[NoteUpdateTypeDef]
    Severity: NotRequired[SeverityUpdateTypeDef]
    VerificationState: NotRequired[VerificationStateType]
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    Types: NotRequired[Sequence[str]]
    UserDefinedFields: NotRequired[Mapping[str, str]]
    Workflow: NotRequired[WorkflowUpdateTypeDef]
    RelatedFindings: NotRequired[Sequence[RelatedFindingTypeDef]]

AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef = Union[
    AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef,
    AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef,
]

class AwsAmazonMqBrokerLogsDetailsTypeDef(TypedDict):
    Audit: NotRequired[bool]
    General: NotRequired[bool]
    AuditLogGroup: NotRequired[str]
    GeneralLogGroup: NotRequired[str]
    Pending: NotRequired[AwsAmazonMqBrokerLogsPendingDetailsTypeDef]

AwsApiGatewayCanarySettingsUnionTypeDef = Union[
    AwsApiGatewayCanarySettingsTypeDef, AwsApiGatewayCanarySettingsOutputTypeDef
]

class AwsApiGatewayRestApiDetailsOutputTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedDate: NotRequired[str]
    Version: NotRequired[str]
    BinaryMediaTypes: NotRequired[List[str]]
    MinimumCompressionSize: NotRequired[int]
    ApiKeySource: NotRequired[str]
    EndpointConfiguration: NotRequired[AwsApiGatewayEndpointConfigurationOutputTypeDef]

AwsApiGatewayEndpointConfigurationUnionTypeDef = Union[
    AwsApiGatewayEndpointConfigurationTypeDef, AwsApiGatewayEndpointConfigurationOutputTypeDef
]

class AwsApiGatewayStageDetailsOutputTypeDef(TypedDict):
    DeploymentId: NotRequired[str]
    ClientCertificateId: NotRequired[str]
    StageName: NotRequired[str]
    Description: NotRequired[str]
    CacheClusterEnabled: NotRequired[bool]
    CacheClusterSize: NotRequired[str]
    CacheClusterStatus: NotRequired[str]
    MethodSettings: NotRequired[List[AwsApiGatewayMethodSettingsTypeDef]]
    Variables: NotRequired[Dict[str, str]]
    DocumentationVersion: NotRequired[str]
    AccessLogSettings: NotRequired[AwsApiGatewayAccessLogSettingsTypeDef]
    CanarySettings: NotRequired[AwsApiGatewayCanarySettingsOutputTypeDef]
    TracingEnabled: NotRequired[bool]
    CreatedDate: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    WebAclArn: NotRequired[str]

class AwsApiGatewayV2ApiDetailsOutputTypeDef(TypedDict):
    ApiEndpoint: NotRequired[str]
    ApiId: NotRequired[str]
    ApiKeySelectionExpression: NotRequired[str]
    CreatedDate: NotRequired[str]
    Description: NotRequired[str]
    Version: NotRequired[str]
    Name: NotRequired[str]
    ProtocolType: NotRequired[str]
    RouteSelectionExpression: NotRequired[str]
    CorsConfiguration: NotRequired[AwsCorsConfigurationOutputTypeDef]

class AwsApiGatewayV2StageDetailsOutputTypeDef(TypedDict):
    ClientCertificateId: NotRequired[str]
    CreatedDate: NotRequired[str]
    Description: NotRequired[str]
    DefaultRouteSettings: NotRequired[AwsApiGatewayV2RouteSettingsTypeDef]
    DeploymentId: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    RouteSettings: NotRequired[AwsApiGatewayV2RouteSettingsTypeDef]
    StageName: NotRequired[str]
    StageVariables: NotRequired[Dict[str, str]]
    AccessLogSettings: NotRequired[AwsApiGatewayAccessLogSettingsTypeDef]
    AutoDeploy: NotRequired[bool]
    LastDeploymentStatusMessage: NotRequired[str]
    ApiGatewayManaged: NotRequired[bool]

class AwsApiGatewayV2StageDetailsTypeDef(TypedDict):
    ClientCertificateId: NotRequired[str]
    CreatedDate: NotRequired[str]
    Description: NotRequired[str]
    DefaultRouteSettings: NotRequired[AwsApiGatewayV2RouteSettingsTypeDef]
    DeploymentId: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    RouteSettings: NotRequired[AwsApiGatewayV2RouteSettingsTypeDef]
    StageName: NotRequired[str]
    StageVariables: NotRequired[Mapping[str, str]]
    AccessLogSettings: NotRequired[AwsApiGatewayAccessLogSettingsTypeDef]
    AutoDeploy: NotRequired[bool]
    LastDeploymentStatusMessage: NotRequired[str]
    ApiGatewayManaged: NotRequired[bool]

class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef(TypedDict):
    AuthenticationType: NotRequired[str]
    LambdaAuthorizerConfig: NotRequired[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]
    OpenIdConnectConfig: NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]
    UserPoolConfig: NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]

class AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef(TypedDict):
    EncryptionConfiguration: NotRequired[
        AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef
    ]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef(
    TypedDict
):
    LaunchTemplateSpecification: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
    ]
    Overrides: NotRequired[
        List[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
        ]
    ]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef(TypedDict):
    LaunchTemplateSpecification: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
    ]
    Overrides: NotRequired[
        Sequence[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
        ]
    ]

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef(TypedDict):
    DeviceName: NotRequired[str]
    Ebs: NotRequired[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef]
    NoDevice: NotRequired[bool]
    VirtualName: NotRequired[str]

AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef,
    AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef,
]

class AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef(TypedDict):
    DestinationBackupVaultArn: NotRequired[str]
    Lifecycle: NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef]

class AwsBackupBackupVaultDetailsOutputTypeDef(TypedDict):
    BackupVaultArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    Notifications: NotRequired[AwsBackupBackupVaultNotificationsDetailsOutputTypeDef]
    AccessPolicy: NotRequired[str]

AwsBackupBackupVaultNotificationsDetailsUnionTypeDef = Union[
    AwsBackupBackupVaultNotificationsDetailsTypeDef,
    AwsBackupBackupVaultNotificationsDetailsOutputTypeDef,
]

class AwsBackupRecoveryPointDetailsTypeDef(TypedDict):
    BackupSizeInBytes: NotRequired[int]
    BackupVaultArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    CalculatedLifecycle: NotRequired[AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef]
    CompletionDate: NotRequired[str]
    CreatedBy: NotRequired[AwsBackupRecoveryPointCreatedByDetailsTypeDef]
    CreationDate: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    IamRoleArn: NotRequired[str]
    IsEncrypted: NotRequired[bool]
    LastRestoreTime: NotRequired[str]
    Lifecycle: NotRequired[AwsBackupRecoveryPointLifecycleDetailsTypeDef]
    RecoveryPointArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    SourceBackupVaultArn: NotRequired[str]
    Status: NotRequired[str]
    StatusMessage: NotRequired[str]
    StorageClass: NotRequired[str]

class AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef(TypedDict):
    DomainName: NotRequired[str]
    ResourceRecord: NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef]
    ValidationDomain: NotRequired[str]
    ValidationEmails: NotRequired[List[str]]
    ValidationMethod: NotRequired[str]
    ValidationStatus: NotRequired[str]

class AwsCertificateManagerCertificateDomainValidationOptionTypeDef(TypedDict):
    DomainName: NotRequired[str]
    ResourceRecord: NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef]
    ValidationDomain: NotRequired[str]
    ValidationEmails: NotRequired[Sequence[str]]
    ValidationMethod: NotRequired[str]
    ValidationStatus: NotRequired[str]

class AwsCloudFormationStackDetailsOutputTypeDef(TypedDict):
    Capabilities: NotRequired[List[str]]
    CreationTime: NotRequired[str]
    Description: NotRequired[str]
    DisableRollback: NotRequired[bool]
    DriftInformation: NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef]
    EnableTerminationProtection: NotRequired[bool]
    LastUpdatedTime: NotRequired[str]
    NotificationArns: NotRequired[List[str]]
    Outputs: NotRequired[List[AwsCloudFormationStackOutputsDetailsTypeDef]]
    RoleArn: NotRequired[str]
    StackId: NotRequired[str]
    StackName: NotRequired[str]
    StackStatus: NotRequired[str]
    StackStatusReason: NotRequired[str]
    TimeoutInMinutes: NotRequired[int]

class AwsCloudFormationStackDetailsTypeDef(TypedDict):
    Capabilities: NotRequired[Sequence[str]]
    CreationTime: NotRequired[str]
    Description: NotRequired[str]
    DisableRollback: NotRequired[bool]
    DriftInformation: NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef]
    EnableTerminationProtection: NotRequired[bool]
    LastUpdatedTime: NotRequired[str]
    NotificationArns: NotRequired[Sequence[str]]
    Outputs: NotRequired[Sequence[AwsCloudFormationStackOutputsDetailsTypeDef]]
    RoleArn: NotRequired[str]
    StackId: NotRequired[str]
    StackName: NotRequired[str]
    StackStatus: NotRequired[str]
    StackStatusReason: NotRequired[str]
    TimeoutInMinutes: NotRequired[int]

class AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef(TypedDict):
    Items: NotRequired[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]]

class AwsCloudFrontDistributionCacheBehaviorsTypeDef(TypedDict):
    Items: NotRequired[Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef]]

class AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef(TypedDict):
    HttpPort: NotRequired[int]
    HttpsPort: NotRequired[int]
    OriginKeepaliveTimeout: NotRequired[int]
    OriginProtocolPolicy: NotRequired[str]
    OriginReadTimeout: NotRequired[int]
    OriginSslProtocols: NotRequired[AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef]

class AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef(TypedDict):
    StatusCodes: NotRequired[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef]

AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef,
    AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef,
]
AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginSslProtocolsTypeDef,
    AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef,
]

class AwsCloudWatchAlarmDetailsOutputTypeDef(TypedDict):
    ActionsEnabled: NotRequired[bool]
    AlarmActions: NotRequired[List[str]]
    AlarmArn: NotRequired[str]
    AlarmConfigurationUpdatedTimestamp: NotRequired[str]
    AlarmDescription: NotRequired[str]
    AlarmName: NotRequired[str]
    ComparisonOperator: NotRequired[str]
    DatapointsToAlarm: NotRequired[int]
    Dimensions: NotRequired[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]]
    EvaluateLowSampleCountPercentile: NotRequired[str]
    EvaluationPeriods: NotRequired[int]
    ExtendedStatistic: NotRequired[str]
    InsufficientDataActions: NotRequired[List[str]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    OkActions: NotRequired[List[str]]
    Period: NotRequired[int]
    Statistic: NotRequired[str]
    Threshold: NotRequired[float]
    ThresholdMetricId: NotRequired[str]
    TreatMissingData: NotRequired[str]
    Unit: NotRequired[str]

class AwsCloudWatchAlarmDetailsTypeDef(TypedDict):
    ActionsEnabled: NotRequired[bool]
    AlarmActions: NotRequired[Sequence[str]]
    AlarmArn: NotRequired[str]
    AlarmConfigurationUpdatedTimestamp: NotRequired[str]
    AlarmDescription: NotRequired[str]
    AlarmName: NotRequired[str]
    ComparisonOperator: NotRequired[str]
    DatapointsToAlarm: NotRequired[int]
    Dimensions: NotRequired[Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef]]
    EvaluateLowSampleCountPercentile: NotRequired[str]
    EvaluationPeriods: NotRequired[int]
    ExtendedStatistic: NotRequired[str]
    InsufficientDataActions: NotRequired[Sequence[str]]
    MetricName: NotRequired[str]
    Namespace: NotRequired[str]
    OkActions: NotRequired[Sequence[str]]
    Period: NotRequired[int]
    Statistic: NotRequired[str]
    Threshold: NotRequired[float]
    ThresholdMetricId: NotRequired[str]
    TreatMissingData: NotRequired[str]
    Unit: NotRequired[str]

AwsCodeBuildProjectEnvironmentOutputTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentOutputTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)

class AwsCodeBuildProjectLogsConfigDetailsTypeDef(TypedDict):
    CloudWatchLogs: NotRequired[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef]
    S3Logs: NotRequired[AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef]

AwsCodeBuildProjectVpcConfigUnionTypeDef = Union[
    AwsCodeBuildProjectVpcConfigTypeDef, AwsCodeBuildProjectVpcConfigOutputTypeDef
]
AwsCorsConfigurationUnionTypeDef = Union[
    AwsCorsConfigurationTypeDef, AwsCorsConfigurationOutputTypeDef
]

class AwsDmsReplicationInstanceDetailsOutputTypeDef(TypedDict):
    AllocatedStorage: NotRequired[int]
    AutoMinorVersionUpgrade: NotRequired[bool]
    AvailabilityZone: NotRequired[str]
    EngineVersion: NotRequired[str]
    KmsKeyId: NotRequired[str]
    MultiAZ: NotRequired[bool]
    PreferredMaintenanceWindow: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    ReplicationInstanceClass: NotRequired[str]
    ReplicationInstanceIdentifier: NotRequired[str]
    ReplicationSubnetGroup: NotRequired[
        AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
    ]
    VpcSecurityGroups: NotRequired[List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]]

class AwsDmsReplicationInstanceDetailsTypeDef(TypedDict):
    AllocatedStorage: NotRequired[int]
    AutoMinorVersionUpgrade: NotRequired[bool]
    AvailabilityZone: NotRequired[str]
    EngineVersion: NotRequired[str]
    KmsKeyId: NotRequired[str]
    MultiAZ: NotRequired[bool]
    PreferredMaintenanceWindow: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    ReplicationInstanceClass: NotRequired[str]
    ReplicationInstanceIdentifier: NotRequired[str]
    ReplicationSubnetGroup: NotRequired[
        AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
    ]
    VpcSecurityGroups: NotRequired[
        Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]
    ]

class AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef(TypedDict):
    Backfilling: NotRequired[bool]
    IndexArn: NotRequired[str]
    IndexName: NotRequired[str]
    IndexSizeBytes: NotRequired[int]
    IndexStatus: NotRequired[str]
    ItemCount: NotRequired[int]
    KeySchema: NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]]
    Projection: NotRequired[AwsDynamoDbTableProjectionOutputTypeDef]
    ProvisionedThroughput: NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef]

class AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef(TypedDict):
    IndexArn: NotRequired[str]
    IndexName: NotRequired[str]
    KeySchema: NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]]
    Projection: NotRequired[AwsDynamoDbTableProjectionOutputTypeDef]

AwsDynamoDbTableProjectionUnionTypeDef = Union[
    AwsDynamoDbTableProjectionTypeDef, AwsDynamoDbTableProjectionOutputTypeDef
]

class AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef(TypedDict):
    IndexName: NotRequired[str]
    ProvisionedThroughputOverride: NotRequired[AwsDynamoDbTableProvisionedThroughputOverrideTypeDef]

AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ActiveDirectory": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef
        ],
        "MutualAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef
        ],
        "FederatedAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef
        ],
    },
)

class AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    LambdaFunctionArn: NotRequired[str]
    Status: NotRequired[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef]

AwsEc2InstanceDetailsOutputTypeDef = TypedDict(
    "AwsEc2InstanceDetailsOutputTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[List[str]],
        "IpV6Addresses": NotRequired[List[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[Sequence[str]],
        "IpV6Addresses": NotRequired[Sequence[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef(TypedDict):
    DeviceName: NotRequired[str]
    Ebs: NotRequired[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef]
    NoDevice: NotRequired[str]
    VirtualName: NotRequired[str]

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef(TypedDict):
    CapacityReservationPreference: NotRequired[str]
    CapacityReservationTarget: NotRequired[
        AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef
    ]

class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef(TypedDict):
    MarketType: NotRequired[str]
    SpotOptions: NotRequired[AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef]

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef(TypedDict):
    AcceleratorCount: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
    ]
    AcceleratorManufacturers: NotRequired[List[str]]
    AcceleratorNames: NotRequired[List[str]]
    AcceleratorTotalMemoryMiB: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
    ]
    AcceleratorTypes: NotRequired[List[str]]
    BareMetal: NotRequired[str]
    BaselineEbsBandwidthMbps: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
    ]
    BurstablePerformance: NotRequired[str]
    CpuManufacturers: NotRequired[List[str]]
    ExcludedInstanceTypes: NotRequired[List[str]]
    InstanceGenerations: NotRequired[List[str]]
    LocalStorage: NotRequired[str]
    LocalStorageTypes: NotRequired[List[str]]
    MemoryGiBPerVCpu: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
    ]
    MemoryMiB: NotRequired[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef]
    NetworkInterfaceCount: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
    ]
    OnDemandMaxPricePercentageOverLowestPrice: NotRequired[int]
    RequireHibernateSupport: NotRequired[bool]
    SpotMaxPricePercentageOverLowestPrice: NotRequired[int]
    TotalLocalStorageGB: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
    ]
    VCpuCount: NotRequired[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef]

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef(TypedDict):
    AcceleratorCount: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
    ]
    AcceleratorManufacturers: NotRequired[Sequence[str]]
    AcceleratorNames: NotRequired[Sequence[str]]
    AcceleratorTotalMemoryMiB: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
    ]
    AcceleratorTypes: NotRequired[Sequence[str]]
    BareMetal: NotRequired[str]
    BaselineEbsBandwidthMbps: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
    ]
    BurstablePerformance: NotRequired[str]
    CpuManufacturers: NotRequired[Sequence[str]]
    ExcludedInstanceTypes: NotRequired[Sequence[str]]
    InstanceGenerations: NotRequired[Sequence[str]]
    LocalStorage: NotRequired[str]
    LocalStorageTypes: NotRequired[Sequence[str]]
    MemoryGiBPerVCpu: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
    ]
    MemoryMiB: NotRequired[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef]
    NetworkInterfaceCount: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
    ]
    OnDemandMaxPricePercentageOverLowestPrice: NotRequired[int]
    RequireHibernateSupport: NotRequired[bool]
    SpotMaxPricePercentageOverLowestPrice: NotRequired[int]
    TotalLocalStorageGB: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
    ]
    VCpuCount: NotRequired[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef(TypedDict):
    AssociateCarrierIpAddress: NotRequired[bool]
    AssociatePublicIpAddress: NotRequired[bool]
    DeleteOnTermination: NotRequired[bool]
    Description: NotRequired[str]
    DeviceIndex: NotRequired[int]
    Groups: NotRequired[List[str]]
    InterfaceType: NotRequired[str]
    Ipv4PrefixCount: NotRequired[int]
    Ipv4Prefixes: NotRequired[
        List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
    ]
    Ipv6AddressCount: NotRequired[int]
    Ipv6Addresses: NotRequired[
        List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
    ]
    Ipv6PrefixCount: NotRequired[int]
    Ipv6Prefixes: NotRequired[
        List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
    ]
    NetworkCardIndex: NotRequired[int]
    NetworkInterfaceId: NotRequired[str]
    PrivateIpAddress: NotRequired[str]
    PrivateIpAddresses: NotRequired[
        List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
    ]
    SecondaryPrivateIpAddressCount: NotRequired[int]
    SubnetId: NotRequired[str]

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef(TypedDict):
    AssociateCarrierIpAddress: NotRequired[bool]
    AssociatePublicIpAddress: NotRequired[bool]
    DeleteOnTermination: NotRequired[bool]
    Description: NotRequired[str]
    DeviceIndex: NotRequired[int]
    Groups: NotRequired[Sequence[str]]
    InterfaceType: NotRequired[str]
    Ipv4PrefixCount: NotRequired[int]
    Ipv4Prefixes: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
    ]
    Ipv6AddressCount: NotRequired[int]
    Ipv6Addresses: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
    ]
    Ipv6PrefixCount: NotRequired[int]
    Ipv6Prefixes: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
    ]
    NetworkCardIndex: NotRequired[int]
    NetworkInterfaceId: NotRequired[str]
    PrivateIpAddress: NotRequired[str]
    PrivateIpAddresses: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
    ]
    SecondaryPrivateIpAddressCount: NotRequired[int]
    SubnetId: NotRequired[str]

AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeFromToTypeDef],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)

class AwsEc2NetworkInterfaceDetailsOutputTypeDef(TypedDict):
    Attachment: NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef]
    NetworkInterfaceId: NotRequired[str]
    SecurityGroups: NotRequired[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]]
    SourceDestCheck: NotRequired[bool]
    IpV6Addresses: NotRequired[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]]
    PrivateIpAddresses: NotRequired[List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]]
    PublicDnsName: NotRequired[str]
    PublicIp: NotRequired[str]

class AwsEc2NetworkInterfaceDetailsTypeDef(TypedDict):
    Attachment: NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef]
    NetworkInterfaceId: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef]]
    SourceDestCheck: NotRequired[bool]
    IpV6Addresses: NotRequired[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]]
    PrivateIpAddresses: NotRequired[Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]]
    PublicDnsName: NotRequired[str]
    PublicIp: NotRequired[str]

class AwsEc2SecurityGroupIpPermissionOutputTypeDef(TypedDict):
    IpProtocol: NotRequired[str]
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]
    UserIdGroupPairs: NotRequired[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]]
    IpRanges: NotRequired[List[AwsEc2SecurityGroupIpRangeTypeDef]]
    Ipv6Ranges: NotRequired[List[AwsEc2SecurityGroupIpv6RangeTypeDef]]
    PrefixListIds: NotRequired[List[AwsEc2SecurityGroupPrefixListIdTypeDef]]

class AwsEc2SecurityGroupIpPermissionTypeDef(TypedDict):
    IpProtocol: NotRequired[str]
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]
    UserIdGroupPairs: NotRequired[Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef]]
    IpRanges: NotRequired[Sequence[AwsEc2SecurityGroupIpRangeTypeDef]]
    Ipv6Ranges: NotRequired[Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef]]
    PrefixListIds: NotRequired[Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef]]

class AwsEc2SubnetDetailsOutputTypeDef(TypedDict):
    AssignIpv6AddressOnCreation: NotRequired[bool]
    AvailabilityZone: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    AvailableIpAddressCount: NotRequired[int]
    CidrBlock: NotRequired[str]
    DefaultForAz: NotRequired[bool]
    MapPublicIpOnLaunch: NotRequired[bool]
    OwnerId: NotRequired[str]
    State: NotRequired[str]
    SubnetArn: NotRequired[str]
    SubnetId: NotRequired[str]
    VpcId: NotRequired[str]
    Ipv6CidrBlockAssociationSet: NotRequired[List[Ipv6CidrBlockAssociationTypeDef]]

class AwsEc2SubnetDetailsTypeDef(TypedDict):
    AssignIpv6AddressOnCreation: NotRequired[bool]
    AvailabilityZone: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    AvailableIpAddressCount: NotRequired[int]
    CidrBlock: NotRequired[str]
    DefaultForAz: NotRequired[bool]
    MapPublicIpOnLaunch: NotRequired[bool]
    OwnerId: NotRequired[str]
    State: NotRequired[str]
    SubnetArn: NotRequired[str]
    SubnetId: NotRequired[str]
    VpcId: NotRequired[str]
    Ipv6CidrBlockAssociationSet: NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]]

AwsEc2TransitGatewayDetailsUnionTypeDef = Union[
    AwsEc2TransitGatewayDetailsTypeDef, AwsEc2TransitGatewayDetailsOutputTypeDef
]

class AwsEc2VolumeDetailsOutputTypeDef(TypedDict):
    CreateTime: NotRequired[str]
    DeviceName: NotRequired[str]
    Encrypted: NotRequired[bool]
    Size: NotRequired[int]
    SnapshotId: NotRequired[str]
    Status: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Attachments: NotRequired[List[AwsEc2VolumeAttachmentTypeDef]]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[str]
    VolumeScanStatus: NotRequired[str]

class AwsEc2VolumeDetailsTypeDef(TypedDict):
    CreateTime: NotRequired[str]
    DeviceName: NotRequired[str]
    Encrypted: NotRequired[bool]
    Size: NotRequired[int]
    SnapshotId: NotRequired[str]
    Status: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Attachments: NotRequired[Sequence[AwsEc2VolumeAttachmentTypeDef]]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[str]
    VolumeScanStatus: NotRequired[str]

class AwsEc2VpcDetailsOutputTypeDef(TypedDict):
    CidrBlockAssociationSet: NotRequired[List[CidrBlockAssociationTypeDef]]
    Ipv6CidrBlockAssociationSet: NotRequired[List[Ipv6CidrBlockAssociationTypeDef]]
    DhcpOptionsId: NotRequired[str]
    State: NotRequired[str]

class AwsEc2VpcDetailsTypeDef(TypedDict):
    CidrBlockAssociationSet: NotRequired[Sequence[CidrBlockAssociationTypeDef]]
    Ipv6CidrBlockAssociationSet: NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]]
    DhcpOptionsId: NotRequired[str]
    State: NotRequired[str]

AwsEc2VpcEndpointServiceDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsOutputTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[List[str]],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)
AwsEc2VpcEndpointServiceDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BaseEndpointDnsNames": NotRequired[Sequence[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)

class AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef(TypedDict):
    CidrBlock: NotRequired[str]
    CidrBlockSet: NotRequired[List[VpcInfoCidrBlockSetDetailsTypeDef]]
    Ipv6CidrBlockSet: NotRequired[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]]
    OwnerId: NotRequired[str]
    PeeringOptions: NotRequired[VpcInfoPeeringOptionsDetailsTypeDef]
    Region: NotRequired[str]
    VpcId: NotRequired[str]

class AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef(TypedDict):
    CidrBlock: NotRequired[str]
    CidrBlockSet: NotRequired[Sequence[VpcInfoCidrBlockSetDetailsTypeDef]]
    Ipv6CidrBlockSet: NotRequired[Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef]]
    OwnerId: NotRequired[str]
    PeeringOptions: NotRequired[VpcInfoPeeringOptionsDetailsTypeDef]
    Region: NotRequired[str]
    VpcId: NotRequired[str]

class AwsEc2VpnConnectionOptionsDetailsOutputTypeDef(TypedDict):
    StaticRoutesOnly: NotRequired[bool]
    TunnelOptions: NotRequired[List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef]]

AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef,
    AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef,
]
AwsEcrContainerImageDetailsUnionTypeDef = Union[
    AwsEcrContainerImageDetailsTypeDef, AwsEcrContainerImageDetailsOutputTypeDef
]

class AwsEcrRepositoryDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    ImageScanningConfiguration: NotRequired[
        AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef
    ]
    ImageTagMutability: NotRequired[str]
    LifecyclePolicy: NotRequired[AwsEcrRepositoryLifecyclePolicyDetailsTypeDef]
    RepositoryName: NotRequired[str]
    RepositoryPolicyText: NotRequired[str]

class AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef(TypedDict):
    KmsKeyId: NotRequired[str]
    LogConfiguration: NotRequired[
        AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef
    ]
    Logging: NotRequired[str]

class AwsEcsContainerDetailsOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Image: NotRequired[str]
    MountPoints: NotRequired[List[AwsMountPointTypeDef]]
    Privileged: NotRequired[bool]

class AwsEcsContainerDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Image: NotRequired[str]
    MountPoints: NotRequired[Sequence[AwsMountPointTypeDef]]
    Privileged: NotRequired[bool]

class AwsEcsServiceDeploymentConfigurationDetailsTypeDef(TypedDict):
    DeploymentCircuitBreaker: NotRequired[
        AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef
    ]
    MaximumPercent: NotRequired[int]
    MinimumHealthyPercent: NotRequired[int]

class AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef(TypedDict):
    AwsVpcConfiguration: NotRequired[
        AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef
    ]

AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef = Union[
    AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef,
    AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef,
]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef(TypedDict):
    Capabilities: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef
    ]
    Devices: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef]
    ]
    InitProcessEnabled: NotRequired[bool]
    MaxSwap: NotRequired[int]
    SharedMemorySize: NotRequired[int]
    Swappiness: NotRequired[int]
    Tmpfs: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef]
    ]

AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef,
]

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef(TypedDict):
    LogDriver: NotRequired[str]
    Options: NotRequired[Dict[str, str]]
    SecretOptions: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef]
    ]

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef(TypedDict):
    LogDriver: NotRequired[str]
    Options: NotRequired[Mapping[str, str]]
    SecretOptions: NotRequired[
        Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
        ]
    ]

AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef
            ]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef,
]

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef(TypedDict):
    AuthorizationConfig: NotRequired[
        AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef
    ]
    FilesystemId: NotRequired[str]
    RootDirectory: NotRequired[str]
    TransitEncryption: NotRequired[str]
    TransitEncryptionPort: NotRequired[int]

class AwsEcsTaskVolumeDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Host: NotRequired[AwsEcsTaskVolumeHostDetailsTypeDef]

AwsEfsAccessPointPosixUserDetailsUnionTypeDef = Union[
    AwsEfsAccessPointPosixUserDetailsTypeDef, AwsEfsAccessPointPosixUserDetailsOutputTypeDef
]

class AwsEfsAccessPointRootDirectoryDetailsTypeDef(TypedDict):
    CreationInfo: NotRequired[AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef]
    Path: NotRequired[str]

class AwsEksClusterLoggingDetailsOutputTypeDef(TypedDict):
    ClusterLogging: NotRequired[List[AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef]]

AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef = Union[
    AwsEksClusterLoggingClusterLoggingDetailsTypeDef,
    AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef,
]
AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef = Union[
    AwsEksClusterResourcesVpcConfigDetailsTypeDef,
    AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef,
]

class AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    Cname: NotRequired[str]
    DateCreated: NotRequired[str]
    DateUpdated: NotRequired[str]
    Description: NotRequired[str]
    EndpointUrl: NotRequired[str]
    EnvironmentArn: NotRequired[str]
    EnvironmentId: NotRequired[str]
    EnvironmentLinks: NotRequired[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]]
    EnvironmentName: NotRequired[str]
    OptionSettings: NotRequired[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]]
    PlatformArn: NotRequired[str]
    SolutionStackName: NotRequired[str]
    Status: NotRequired[str]
    Tier: NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef]
    VersionLabel: NotRequired[str]

class AwsElasticBeanstalkEnvironmentDetailsTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    Cname: NotRequired[str]
    DateCreated: NotRequired[str]
    DateUpdated: NotRequired[str]
    Description: NotRequired[str]
    EndpointUrl: NotRequired[str]
    EnvironmentArn: NotRequired[str]
    EnvironmentId: NotRequired[str]
    EnvironmentLinks: NotRequired[Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]]
    EnvironmentName: NotRequired[str]
    OptionSettings: NotRequired[Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]]
    PlatformArn: NotRequired[str]
    SolutionStackName: NotRequired[str]
    Status: NotRequired[str]
    Tier: NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef]
    VersionLabel: NotRequired[str]

class AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef(TypedDict):
    DedicatedMasterCount: NotRequired[int]
    DedicatedMasterEnabled: NotRequired[bool]
    DedicatedMasterType: NotRequired[str]
    InstanceCount: NotRequired[int]
    InstanceType: NotRequired[str]
    ZoneAwarenessConfig: NotRequired[
        AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef
    ]
    ZoneAwarenessEnabled: NotRequired[bool]

class AwsElasticsearchDomainLogPublishingOptionsTypeDef(TypedDict):
    IndexSlowLogs: NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]
    SearchSlowLogs: NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]
    AuditLogs: NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]

AwsElasticsearchDomainVPCOptionsUnionTypeDef = Union[
    AwsElasticsearchDomainVPCOptionsTypeDef, AwsElasticsearchDomainVPCOptionsOutputTypeDef
]

class AwsElbLoadBalancerPoliciesOutputTypeDef(TypedDict):
    AppCookieStickinessPolicies: NotRequired[List[AwsElbAppCookieStickinessPolicyTypeDef]]
    LbCookieStickinessPolicies: NotRequired[List[AwsElbLbCookieStickinessPolicyTypeDef]]
    OtherPolicies: NotRequired[List[str]]

class AwsElbLoadBalancerPoliciesTypeDef(TypedDict):
    AppCookieStickinessPolicies: NotRequired[Sequence[AwsElbAppCookieStickinessPolicyTypeDef]]
    LbCookieStickinessPolicies: NotRequired[Sequence[AwsElbLbCookieStickinessPolicyTypeDef]]
    OtherPolicies: NotRequired[Sequence[str]]

class AwsElbLoadBalancerAttributesOutputTypeDef(TypedDict):
    AccessLog: NotRequired[AwsElbLoadBalancerAccessLogTypeDef]
    ConnectionDraining: NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef]
    ConnectionSettings: NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef]
    CrossZoneLoadBalancing: NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef]
    AdditionalAttributes: NotRequired[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]]

class AwsElbLoadBalancerAttributesTypeDef(TypedDict):
    AccessLog: NotRequired[AwsElbLoadBalancerAccessLogTypeDef]
    ConnectionDraining: NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef]
    ConnectionSettings: NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef]
    CrossZoneLoadBalancing: NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef]
    AdditionalAttributes: NotRequired[Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef]]

AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef = Union[
    AwsElbLoadBalancerBackendServerDescriptionTypeDef,
    AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef,
]

class AwsElbLoadBalancerListenerDescriptionOutputTypeDef(TypedDict):
    Listener: NotRequired[AwsElbLoadBalancerListenerTypeDef]
    PolicyNames: NotRequired[List[str]]

class AwsElbLoadBalancerListenerDescriptionTypeDef(TypedDict):
    Listener: NotRequired[AwsElbLoadBalancerListenerTypeDef]
    PolicyNames: NotRequired[Sequence[str]]

AwsElbv2LoadBalancerDetailsOutputTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsOutputTypeDef",
    {
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[List[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)
AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[Sequence[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)

class AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef(TypedDict):
    Primary: NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef]
    Secondary: NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef]

class AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef(TypedDict):
    AuditLogs: NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef]

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef(
    TypedDict
):
    EbsVolumes: NotRequired[
        AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef
    ]

class AwsIamAccessKeySessionContextTypeDef(TypedDict):
    Attributes: NotRequired[AwsIamAccessKeySessionContextAttributesTypeDef]
    SessionIssuer: NotRequired[AwsIamAccessKeySessionContextSessionIssuerTypeDef]

class AwsIamGroupDetailsOutputTypeDef(TypedDict):
    AttachedManagedPolicies: NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]
    GroupPolicyList: NotRequired[List[AwsIamGroupPolicyTypeDef]]
    Path: NotRequired[str]

class AwsIamGroupDetailsTypeDef(TypedDict):
    AttachedManagedPolicies: NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]
    GroupPolicyList: NotRequired[Sequence[AwsIamGroupPolicyTypeDef]]
    Path: NotRequired[str]

class AwsIamInstanceProfileOutputTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreateDate: NotRequired[str]
    InstanceProfileId: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    Path: NotRequired[str]
    Roles: NotRequired[List[AwsIamInstanceProfileRoleTypeDef]]

class AwsIamInstanceProfileTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreateDate: NotRequired[str]
    InstanceProfileId: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    Path: NotRequired[str]
    Roles: NotRequired[Sequence[AwsIamInstanceProfileRoleTypeDef]]

class AwsIamPolicyDetailsOutputTypeDef(TypedDict):
    AttachmentCount: NotRequired[int]
    CreateDate: NotRequired[str]
    DefaultVersionId: NotRequired[str]
    Description: NotRequired[str]
    IsAttachable: NotRequired[bool]
    Path: NotRequired[str]
    PermissionsBoundaryUsageCount: NotRequired[int]
    PolicyId: NotRequired[str]
    PolicyName: NotRequired[str]
    PolicyVersionList: NotRequired[List[AwsIamPolicyVersionTypeDef]]
    UpdateDate: NotRequired[str]

class AwsIamPolicyDetailsTypeDef(TypedDict):
    AttachmentCount: NotRequired[int]
    CreateDate: NotRequired[str]
    DefaultVersionId: NotRequired[str]
    Description: NotRequired[str]
    IsAttachable: NotRequired[bool]
    Path: NotRequired[str]
    PermissionsBoundaryUsageCount: NotRequired[int]
    PolicyId: NotRequired[str]
    PolicyName: NotRequired[str]
    PolicyVersionList: NotRequired[Sequence[AwsIamPolicyVersionTypeDef]]
    UpdateDate: NotRequired[str]

class AwsIamUserDetailsOutputTypeDef(TypedDict):
    AttachedManagedPolicies: NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    GroupList: NotRequired[List[str]]
    Path: NotRequired[str]
    PermissionsBoundary: NotRequired[AwsIamPermissionsBoundaryTypeDef]
    UserId: NotRequired[str]
    UserName: NotRequired[str]
    UserPolicyList: NotRequired[List[AwsIamUserPolicyTypeDef]]

class AwsIamUserDetailsTypeDef(TypedDict):
    AttachedManagedPolicies: NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    GroupList: NotRequired[Sequence[str]]
    Path: NotRequired[str]
    PermissionsBoundary: NotRequired[AwsIamPermissionsBoundaryTypeDef]
    UserId: NotRequired[str]
    UserName: NotRequired[str]
    UserPolicyList: NotRequired[Sequence[AwsIamUserPolicyTypeDef]]

class AwsKinesisStreamDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    StreamEncryption: NotRequired[AwsKinesisStreamStreamEncryptionDetailsTypeDef]
    ShardCount: NotRequired[int]
    RetentionPeriodHours: NotRequired[int]

class AwsLambdaFunctionEnvironmentOutputTypeDef(TypedDict):
    Variables: NotRequired[Dict[str, str]]
    Error: NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef]

class AwsLambdaFunctionEnvironmentTypeDef(TypedDict):
    Variables: NotRequired[Mapping[str, str]]
    Error: NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef]

AwsLambdaFunctionVpcConfigUnionTypeDef = Union[
    AwsLambdaFunctionVpcConfigTypeDef, AwsLambdaFunctionVpcConfigOutputTypeDef
]
AwsLambdaLayerVersionDetailsUnionTypeDef = Union[
    AwsLambdaLayerVersionDetailsTypeDef, AwsLambdaLayerVersionDetailsOutputTypeDef
]

class AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef(TypedDict):
    Iam: NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef]
    Scram: NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef]

AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef,
    AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef,
]

class AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef(TypedDict):
    EncryptionInTransit: NotRequired[
        AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef
    ]
    EncryptionAtRest: NotRequired[
        AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef
    ]

class AwsNetworkFirewallFirewallDetailsOutputTypeDef(TypedDict):
    DeleteProtection: NotRequired[bool]
    Description: NotRequired[str]
    FirewallArn: NotRequired[str]
    FirewallId: NotRequired[str]
    FirewallName: NotRequired[str]
    FirewallPolicyArn: NotRequired[str]
    FirewallPolicyChangeProtection: NotRequired[bool]
    SubnetChangeProtection: NotRequired[bool]
    SubnetMappings: NotRequired[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]]
    VpcId: NotRequired[str]

class AwsNetworkFirewallFirewallDetailsTypeDef(TypedDict):
    DeleteProtection: NotRequired[bool]
    Description: NotRequired[str]
    FirewallArn: NotRequired[str]
    FirewallId: NotRequired[str]
    FirewallName: NotRequired[str]
    FirewallPolicyArn: NotRequired[str]
    FirewallPolicyChangeProtection: NotRequired[bool]
    SubnetChangeProtection: NotRequired[bool]
    SubnetMappings: NotRequired[Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]]
    VpcId: NotRequired[str]

class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    InternalUserDatabaseEnabled: NotRequired[bool]
    MasterUserOptions: NotRequired[AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef]

class AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef(TypedDict):
    InstanceCount: NotRequired[int]
    WarmEnabled: NotRequired[bool]
    WarmCount: NotRequired[int]
    DedicatedMasterEnabled: NotRequired[bool]
    ZoneAwarenessConfig: NotRequired[
        AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef
    ]
    DedicatedMasterCount: NotRequired[int]
    InstanceType: NotRequired[str]
    WarmType: NotRequired[str]
    ZoneAwarenessEnabled: NotRequired[bool]
    DedicatedMasterType: NotRequired[str]

class AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef(TypedDict):
    IndexSlowLogs: NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]
    SearchSlowLogs: NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]
    AuditLogs: NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]

AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef = Union[
    AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef,
    AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef,
]

class AwsRdsDbClusterDetailsOutputTypeDef(TypedDict):
    AllocatedStorage: NotRequired[int]
    AvailabilityZones: NotRequired[List[str]]
    BackupRetentionPeriod: NotRequired[int]
    DatabaseName: NotRequired[str]
    Status: NotRequired[str]
    Endpoint: NotRequired[str]
    ReaderEndpoint: NotRequired[str]
    CustomEndpoints: NotRequired[List[str]]
    MultiAz: NotRequired[bool]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    MasterUsername: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    ReadReplicaIdentifiers: NotRequired[List[str]]
    VpcSecurityGroups: NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]]
    HostedZoneId: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbClusterResourceId: NotRequired[str]
    AssociatedRoles: NotRequired[List[AwsRdsDbClusterAssociatedRoleTypeDef]]
    ClusterCreateTime: NotRequired[str]
    EnabledCloudWatchLogsExports: NotRequired[List[str]]
    EngineMode: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    HttpEndpointEnabled: NotRequired[bool]
    ActivityStreamStatus: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    CrossAccountClone: NotRequired[bool]
    DomainMemberships: NotRequired[List[AwsRdsDbDomainMembershipTypeDef]]
    DbClusterParameterGroup: NotRequired[str]
    DbSubnetGroup: NotRequired[str]
    DbClusterOptionGroupMemberships: NotRequired[List[AwsRdsDbClusterOptionGroupMembershipTypeDef]]
    DbClusterIdentifier: NotRequired[str]
    DbClusterMembers: NotRequired[List[AwsRdsDbClusterMemberTypeDef]]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    AutoMinorVersionUpgrade: NotRequired[bool]

class AwsRdsDbClusterDetailsTypeDef(TypedDict):
    AllocatedStorage: NotRequired[int]
    AvailabilityZones: NotRequired[Sequence[str]]
    BackupRetentionPeriod: NotRequired[int]
    DatabaseName: NotRequired[str]
    Status: NotRequired[str]
    Endpoint: NotRequired[str]
    ReaderEndpoint: NotRequired[str]
    CustomEndpoints: NotRequired[Sequence[str]]
    MultiAz: NotRequired[bool]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    Port: NotRequired[int]
    MasterUsername: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    ReadReplicaIdentifiers: NotRequired[Sequence[str]]
    VpcSecurityGroups: NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]]
    HostedZoneId: NotRequired[str]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbClusterResourceId: NotRequired[str]
    AssociatedRoles: NotRequired[Sequence[AwsRdsDbClusterAssociatedRoleTypeDef]]
    ClusterCreateTime: NotRequired[str]
    EnabledCloudWatchLogsExports: NotRequired[Sequence[str]]
    EngineMode: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    HttpEndpointEnabled: NotRequired[bool]
    ActivityStreamStatus: NotRequired[str]
    CopyTagsToSnapshot: NotRequired[bool]
    CrossAccountClone: NotRequired[bool]
    DomainMemberships: NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]]
    DbClusterParameterGroup: NotRequired[str]
    DbSubnetGroup: NotRequired[str]
    DbClusterOptionGroupMemberships: NotRequired[
        Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef]
    ]
    DbClusterIdentifier: NotRequired[str]
    DbClusterMembers: NotRequired[Sequence[AwsRdsDbClusterMemberTypeDef]]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    AutoMinorVersionUpgrade: NotRequired[bool]

class AwsRdsDbClusterSnapshotDetailsOutputTypeDef(TypedDict):
    AvailabilityZones: NotRequired[List[str]]
    SnapshotCreateTime: NotRequired[str]
    Engine: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    Status: NotRequired[str]
    Port: NotRequired[int]
    VpcId: NotRequired[str]
    ClusterCreateTime: NotRequired[str]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    SnapshotType: NotRequired[str]
    PercentProgress: NotRequired[int]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbClusterIdentifier: NotRequired[str]
    DbClusterSnapshotIdentifier: NotRequired[str]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    DbClusterSnapshotAttributes: NotRequired[
        List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef]
    ]

AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef = Union[
    AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef,
    AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef,
]

class AwsRdsDbSnapshotDetailsOutputTypeDef(TypedDict):
    DbSnapshotIdentifier: NotRequired[str]
    DbInstanceIdentifier: NotRequired[str]
    SnapshotCreateTime: NotRequired[str]
    Engine: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    Status: NotRequired[str]
    Port: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    VpcId: NotRequired[str]
    InstanceCreateTime: NotRequired[str]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    SnapshotType: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupName: NotRequired[str]
    PercentProgress: NotRequired[int]
    SourceRegion: NotRequired[str]
    SourceDbSnapshotIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    TdeCredentialArn: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    Timezone: NotRequired[str]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    ProcessorFeatures: NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]]
    DbiResourceId: NotRequired[str]

class AwsRdsDbSnapshotDetailsTypeDef(TypedDict):
    DbSnapshotIdentifier: NotRequired[str]
    DbInstanceIdentifier: NotRequired[str]
    SnapshotCreateTime: NotRequired[str]
    Engine: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    Status: NotRequired[str]
    Port: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    VpcId: NotRequired[str]
    InstanceCreateTime: NotRequired[str]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    SnapshotType: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupName: NotRequired[str]
    PercentProgress: NotRequired[int]
    SourceRegion: NotRequired[str]
    SourceDbSnapshotIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    TdeCredentialArn: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    Timezone: NotRequired[str]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    ProcessorFeatures: NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]]
    DbiResourceId: NotRequired[str]

class AwsRdsDbPendingModifiedValuesOutputTypeDef(TypedDict):
    DbInstanceClass: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    MasterUserPassword: NotRequired[str]
    Port: NotRequired[int]
    BackupRetentionPeriod: NotRequired[int]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    DbInstanceIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    CaCertificateIdentifier: NotRequired[str]
    DbSubnetGroupName: NotRequired[str]
    PendingCloudWatchLogsExports: NotRequired[AwsRdsPendingCloudWatchLogsExportsOutputTypeDef]
    ProcessorFeatures: NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]]

class AwsRdsDbSecurityGroupDetailsOutputTypeDef(TypedDict):
    DbSecurityGroupArn: NotRequired[str]
    DbSecurityGroupDescription: NotRequired[str]
    DbSecurityGroupName: NotRequired[str]
    Ec2SecurityGroups: NotRequired[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]]
    IpRanges: NotRequired[List[AwsRdsDbSecurityGroupIpRangeTypeDef]]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]

class AwsRdsDbSecurityGroupDetailsTypeDef(TypedDict):
    DbSecurityGroupArn: NotRequired[str]
    DbSecurityGroupDescription: NotRequired[str]
    DbSecurityGroupName: NotRequired[str]
    Ec2SecurityGroups: NotRequired[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]]
    IpRanges: NotRequired[Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef]]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]

class AwsRdsDbSubnetGroupSubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef]
    SubnetStatus: NotRequired[str]

AwsRdsEventSubscriptionDetailsUnionTypeDef = Union[
    AwsRdsEventSubscriptionDetailsTypeDef, AwsRdsEventSubscriptionDetailsOutputTypeDef
]
AwsRdsPendingCloudWatchLogsExportsUnionTypeDef = Union[
    AwsRdsPendingCloudWatchLogsExportsTypeDef, AwsRdsPendingCloudWatchLogsExportsOutputTypeDef
]

class AwsRedshiftClusterClusterParameterGroupOutputTypeDef(TypedDict):
    ClusterParameterStatusList: NotRequired[List[AwsRedshiftClusterClusterParameterStatusTypeDef]]
    ParameterApplyStatus: NotRequired[str]
    ParameterGroupName: NotRequired[str]

class AwsRedshiftClusterClusterParameterGroupTypeDef(TypedDict):
    ClusterParameterStatusList: NotRequired[
        Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef]
    ]
    ParameterApplyStatus: NotRequired[str]
    ParameterGroupName: NotRequired[str]

class AwsRoute53HostedZoneObjectDetailsTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Config: NotRequired[AwsRoute53HostedZoneConfigDetailsTypeDef]

class AwsRoute53QueryLoggingConfigDetailsTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[CloudWatchLogsLogGroupArnConfigDetailsTypeDef]

class AwsS3AccessPointDetailsTypeDef(TypedDict):
    AccessPointArn: NotRequired[str]
    Alias: NotRequired[str]
    Bucket: NotRequired[str]
    BucketAccountId: NotRequired[str]
    Name: NotRequired[str]
    NetworkOrigin: NotRequired[str]
    PublicAccessBlockConfiguration: NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef]
    VpcConfiguration: NotRequired[AwsS3AccessPointVpcConfigurationDetailsTypeDef]

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)

class AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef(TypedDict):
    FilterRules: NotRequired[List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]]

class AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef(TypedDict):
    FilterRules: NotRequired[Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]]

class AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef(TypedDict):
    DefaultRetention: NotRequired[
        AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef
    ]

class AwsS3BucketServerSideEncryptionRuleTypeDef(TypedDict):
    ApplyServerSideEncryptionByDefault: NotRequired[AwsS3BucketServerSideEncryptionByDefaultTypeDef]

class AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef(TypedDict):
    Condition: NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef]
    Redirect: NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef]

class AwsSageMakerNotebookInstanceDetailsOutputTypeDef(TypedDict):
    AcceleratorTypes: NotRequired[List[str]]
    AdditionalCodeRepositories: NotRequired[List[str]]
    DefaultCodeRepository: NotRequired[str]
    DirectInternetAccess: NotRequired[str]
    FailureReason: NotRequired[str]
    InstanceMetadataServiceConfiguration: NotRequired[
        AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
    ]
    InstanceType: NotRequired[str]
    KmsKeyId: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    NotebookInstanceArn: NotRequired[str]
    NotebookInstanceLifecycleConfigName: NotRequired[str]
    NotebookInstanceName: NotRequired[str]
    NotebookInstanceStatus: NotRequired[str]
    PlatformIdentifier: NotRequired[str]
    RoleArn: NotRequired[str]
    RootAccess: NotRequired[str]
    SecurityGroups: NotRequired[List[str]]
    SubnetId: NotRequired[str]
    Url: NotRequired[str]
    VolumeSizeInGB: NotRequired[int]

class AwsSageMakerNotebookInstanceDetailsTypeDef(TypedDict):
    AcceleratorTypes: NotRequired[Sequence[str]]
    AdditionalCodeRepositories: NotRequired[Sequence[str]]
    DefaultCodeRepository: NotRequired[str]
    DirectInternetAccess: NotRequired[str]
    FailureReason: NotRequired[str]
    InstanceMetadataServiceConfiguration: NotRequired[
        AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
    ]
    InstanceType: NotRequired[str]
    KmsKeyId: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    NotebookInstanceArn: NotRequired[str]
    NotebookInstanceLifecycleConfigName: NotRequired[str]
    NotebookInstanceName: NotRequired[str]
    NotebookInstanceStatus: NotRequired[str]
    PlatformIdentifier: NotRequired[str]
    RoleArn: NotRequired[str]
    RootAccess: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]
    SubnetId: NotRequired[str]
    Url: NotRequired[str]
    VolumeSizeInGB: NotRequired[int]

class AwsSecretsManagerSecretDetailsTypeDef(TypedDict):
    RotationRules: NotRequired[AwsSecretsManagerSecretRotationRulesTypeDef]
    RotationOccurredWithinFrequency: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    RotationEnabled: NotRequired[bool]
    RotationLambdaArn: NotRequired[str]
    Deleted: NotRequired[bool]
    Name: NotRequired[str]
    Description: NotRequired[str]

class BatchUpdateFindingsRequestTypeDef(TypedDict):
    FindingIdentifiers: Sequence[AwsSecurityFindingIdentifierTypeDef]
    Note: NotRequired[NoteUpdateTypeDef]
    Severity: NotRequired[SeverityUpdateTypeDef]
    VerificationState: NotRequired[VerificationStateType]
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    Types: NotRequired[Sequence[str]]
    UserDefinedFields: NotRequired[Mapping[str, str]]
    Workflow: NotRequired[WorkflowUpdateTypeDef]
    RelatedFindings: NotRequired[Sequence[RelatedFindingTypeDef]]

class BatchUpdateFindingsUnprocessedFindingTypeDef(TypedDict):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    ErrorCode: str
    ErrorMessage: str

class AwsSnsTopicDetailsOutputTypeDef(TypedDict):
    KmsMasterKeyId: NotRequired[str]
    Subscription: NotRequired[List[AwsSnsTopicSubscriptionTypeDef]]
    TopicName: NotRequired[str]
    Owner: NotRequired[str]
    SqsSuccessFeedbackRoleArn: NotRequired[str]
    SqsFailureFeedbackRoleArn: NotRequired[str]
    ApplicationSuccessFeedbackRoleArn: NotRequired[str]
    FirehoseSuccessFeedbackRoleArn: NotRequired[str]
    FirehoseFailureFeedbackRoleArn: NotRequired[str]
    HttpSuccessFeedbackRoleArn: NotRequired[str]
    HttpFailureFeedbackRoleArn: NotRequired[str]

class AwsSnsTopicDetailsTypeDef(TypedDict):
    KmsMasterKeyId: NotRequired[str]
    Subscription: NotRequired[Sequence[AwsSnsTopicSubscriptionTypeDef]]
    TopicName: NotRequired[str]
    Owner: NotRequired[str]
    SqsSuccessFeedbackRoleArn: NotRequired[str]
    SqsFailureFeedbackRoleArn: NotRequired[str]
    ApplicationSuccessFeedbackRoleArn: NotRequired[str]
    FirehoseSuccessFeedbackRoleArn: NotRequired[str]
    FirehoseFailureFeedbackRoleArn: NotRequired[str]
    HttpSuccessFeedbackRoleArn: NotRequired[str]
    HttpFailureFeedbackRoleArn: NotRequired[str]

class AwsSsmPatchTypeDef(TypedDict):
    ComplianceSummary: NotRequired[AwsSsmComplianceSummaryTypeDef]

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef(TypedDict):
    CloudWatchLogsLogGroup: NotRequired[
        AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef
    ]

class AwsWafRateBasedRuleDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RateKey: NotRequired[str]
    RateLimit: NotRequired[int]
    RuleId: NotRequired[str]
    MatchPredicates: NotRequired[List[AwsWafRateBasedRuleMatchPredicateTypeDef]]

class AwsWafRateBasedRuleDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RateKey: NotRequired[str]
    RateLimit: NotRequired[int]
    RuleId: NotRequired[str]
    MatchPredicates: NotRequired[Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef]]

class AwsWafRegionalRateBasedRuleDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RateKey: NotRequired[str]
    RateLimit: NotRequired[int]
    RuleId: NotRequired[str]
    MatchPredicates: NotRequired[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]]

class AwsWafRegionalRateBasedRuleDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RateKey: NotRequired[str]
    RateLimit: NotRequired[int]
    RuleId: NotRequired[str]
    MatchPredicates: NotRequired[Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]]

class AwsWafRegionalRuleDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    PredicateList: NotRequired[List[AwsWafRegionalRulePredicateListDetailsTypeDef]]
    RuleId: NotRequired[str]

class AwsWafRegionalRuleDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    PredicateList: NotRequired[Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef]]
    RuleId: NotRequired[str]

AwsWafRegionalRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalWebAclRulesListActionDetailsTypeDef],
        "OverrideAction": NotRequired[AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AwsWafRuleDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    PredicateList: NotRequired[List[AwsWafRulePredicateListDetailsTypeDef]]
    RuleId: NotRequired[str]

class AwsWafRuleDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    PredicateList: NotRequired[Sequence[AwsWafRulePredicateListDetailsTypeDef]]
    RuleId: NotRequired[str]

AwsWafRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRuleOutputTypeDef = TypedDict(
    "AwsWafWebAclRuleOutputTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[List[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[Sequence[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AwsWafv2CustomRequestHandlingDetailsOutputTypeDef(TypedDict):
    InsertHeaders: NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]]

class AwsWafv2CustomRequestHandlingDetailsTypeDef(TypedDict):
    InsertHeaders: NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]]

class AwsWafv2CustomResponseDetailsOutputTypeDef(TypedDict):
    CustomResponseBodyKey: NotRequired[str]
    ResponseCode: NotRequired[int]
    ResponseHeaders: NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]]

class AwsWafv2CustomResponseDetailsTypeDef(TypedDict):
    CustomResponseBodyKey: NotRequired[str]
    ResponseCode: NotRequired[int]
    ResponseHeaders: NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]]

class AwsWafv2WebAclCaptchaConfigDetailsTypeDef(TypedDict):
    ImmunityTimeProperty: NotRequired[AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef]

class CreateActionTargetResponseTypeDef(TypedDict):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutomationRuleResponseTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingAggregatorResponseTypeDef(TypedDict):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInsightResponseTypeDef(TypedDict):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteActionTargetResponseTypeDef(TypedDict):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInsightResponseTypeDef(TypedDict):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActionTargetsResponseTypeDef(TypedDict):
    ActionTargets: List[ActionTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeHubResponseTypeDef(TypedDict):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool
    ControlFindingGenerator: ControlFindingGeneratorType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImportFindingsForProductResponseTypeDef(TypedDict):
    ProductSubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyAssociationResponseTypeDef(TypedDict):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingAggregatorResponseTypeDef(TypedDict):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(TypedDict):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomationRulesResponseTypeDef(TypedDict):
    AutomationRulesMetadata: List[AutomationRulesMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEnabledProductsForImportResponseTypeDef(TypedDict):
    ProductSubscriptions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListOrganizationAdminAccountsResponseTypeDef(TypedDict):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartConfigurationPolicyAssociationResponseTypeDef(TypedDict):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFindingAggregatorResponseTypeDef(TypedDict):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteAutomationRulesResponseTypeDef(TypedDict):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomationRulesResponseTypeDef(TypedDict):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsRequestTypeDef(TypedDict):
    StandardsSubscriptionRequests: Sequence[StandardsSubscriptionRequestTypeDef]

class ListConfigurationPolicyAssociationsResponseTypeDef(TypedDict):
    ConfigurationPolicyAssociationSummaries: List[ConfigurationPolicyAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetStandardsControlAssociationsRequestTypeDef(TypedDict):
    StandardsControlAssociationIds: Sequence[StandardsControlAssociationIdTypeDef]

class UnprocessedStandardsControlAssociationTypeDef(TypedDict):
    StandardsControlAssociationId: StandardsControlAssociationIdTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: NotRequired[str]

class BatchImportFindingsResponseTypeDef(TypedDict):
    FailedCount: int
    SuccessCount: int
    FailedFindings: List[ImportFindingsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsRequestTypeDef(TypedDict):
    StandardsControlAssociationUpdates: Sequence[StandardsControlAssociationUpdateTypeDef]

class UnprocessedStandardsControlAssociationUpdateTypeDef(TypedDict):
    StandardsControlAssociationUpdate: StandardsControlAssociationUpdateTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: NotRequired[str]

class VulnerabilityCodeVulnerabilitiesOutputTypeDef(TypedDict):
    Cwes: NotRequired[List[str]]
    FilePath: NotRequired[CodeVulnerabilitiesFilePathTypeDef]
    SourceArn: NotRequired[str]

class VulnerabilityCodeVulnerabilitiesTypeDef(TypedDict):
    Cwes: NotRequired[Sequence[str]]
    FilePath: NotRequired[CodeVulnerabilitiesFilePathTypeDef]
    SourceArn: NotRequired[str]

class ComplianceOutputTypeDef(TypedDict):
    Status: NotRequired[ComplianceStatusType]
    RelatedRequirements: NotRequired[List[str]]
    StatusReasons: NotRequired[List[StatusReasonTypeDef]]
    SecurityControlId: NotRequired[str]
    AssociatedStandards: NotRequired[List[AssociatedStandardTypeDef]]
    SecurityControlParameters: NotRequired[List[SecurityControlParameterOutputTypeDef]]

class ConfigurationOptionsTypeDef(TypedDict):
    Integer: NotRequired[IntegerConfigurationOptionsTypeDef]
    IntegerList: NotRequired[IntegerListConfigurationOptionsTypeDef]
    Double: NotRequired[DoubleConfigurationOptionsTypeDef]
    String: NotRequired[StringConfigurationOptionsTypeDef]
    StringList: NotRequired[StringListConfigurationOptionsTypeDef]
    Boolean: NotRequired[BooleanConfigurationOptionsTypeDef]
    Enum: NotRequired[EnumConfigurationOptionsTypeDef]
    EnumList: NotRequired[EnumListConfigurationOptionsTypeDef]

class ConfigurationPolicyAssociationTypeDef(TypedDict):
    Target: NotRequired[TargetTypeDef]

class GetConfigurationPolicyAssociationRequestTypeDef(TypedDict):
    Target: TargetTypeDef

class StartConfigurationPolicyAssociationRequestTypeDef(TypedDict):
    ConfigurationPolicyIdentifier: str
    Target: TargetTypeDef

class StartConfigurationPolicyDisassociationRequestTypeDef(TypedDict):
    ConfigurationPolicyIdentifier: str
    Target: NotRequired[TargetTypeDef]

class ListConfigurationPoliciesResponseTypeDef(TypedDict):
    ConfigurationPolicySummaries: List[ConfigurationPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ContainerDetailsOutputTypeDef(TypedDict):
    ContainerRuntime: NotRequired[str]
    Name: NotRequired[str]
    ImageId: NotRequired[str]
    ImageName: NotRequired[str]
    LaunchedAt: NotRequired[str]
    VolumeMounts: NotRequired[List[VolumeMountTypeDef]]
    Privileged: NotRequired[bool]

class ContainerDetailsTypeDef(TypedDict):
    ContainerRuntime: NotRequired[str]
    Name: NotRequired[str]
    ImageId: NotRequired[str]
    ImageName: NotRequired[str]
    LaunchedAt: NotRequired[str]
    VolumeMounts: NotRequired[Sequence[VolumeMountTypeDef]]
    Privileged: NotRequired[bool]

class CreateMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InviteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DateFilterTypeDef(TypedDict):
    Start: NotRequired[str]
    End: NotRequired[str]
    DateRange: NotRequired[DateRangeTypeDef]

class DescribeActionTargetsRequestPaginateTypeDef(TypedDict):
    ActionTargetArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeProductsRequestPaginateTypeDef(TypedDict):
    ProductArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStandardsControlsRequestPaginateTypeDef(TypedDict):
    StandardsSubscriptionArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStandardsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetEnabledStandardsRequestPaginateTypeDef(TypedDict):
    StandardsSubscriptionArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetInsightsRequestPaginateTypeDef(TypedDict):
    InsightArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfigurationPoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfigurationPolicyAssociationsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[AssociationFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnabledProductsForImportRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFindingAggregatorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvitationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMembersRequestPaginateTypeDef(TypedDict):
    OnlyAssociated: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrganizationAdminAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityControlDefinitionsRequestPaginateTypeDef(TypedDict):
    StandardsArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStandardsControlAssociationsRequestPaginateTypeDef(TypedDict):
    SecurityControlId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrganizationConfigurationResponseTypeDef(TypedDict):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    AutoEnableStandards: AutoEnableStandardsType
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOrganizationConfigurationRequestTypeDef(TypedDict):
    AutoEnable: bool
    AutoEnableStandards: NotRequired[AutoEnableStandardsType]
    OrganizationConfiguration: NotRequired[OrganizationConfigurationTypeDef]

class DescribeProductsResponseTypeDef(TypedDict):
    Products: List[ProductTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeStandardsControlsResponseTypeDef(TypedDict):
    Controls: List[StandardsControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ThreatOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Severity: NotRequired[str]
    ItemCount: NotRequired[int]
    FilePaths: NotRequired[List[FilePathsTypeDef]]

class ThreatTypeDef(TypedDict):
    Name: NotRequired[str]
    Severity: NotRequired[str]
    ItemCount: NotRequired[int]
    FilePaths: NotRequired[Sequence[FilePathsTypeDef]]

class ListFindingAggregatorsResponseTypeDef(TypedDict):
    FindingAggregators: List[FindingAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FindingHistoryRecordTypeDef(TypedDict):
    FindingIdentifier: NotRequired[AwsSecurityFindingIdentifierTypeDef]
    UpdateTime: NotRequired[datetime]
    FindingCreated: NotRequired[bool]
    UpdateSource: NotRequired[FindingHistoryUpdateSourceTypeDef]
    Updates: NotRequired[List[FindingHistoryUpdateTypeDef]]
    NextToken: NotRequired[str]

class FindingProviderFieldsOutputTypeDef(TypedDict):
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    RelatedFindings: NotRequired[List[RelatedFindingTypeDef]]
    Severity: NotRequired[FindingProviderSeverityTypeDef]
    Types: NotRequired[List[str]]

class FindingProviderFieldsTypeDef(TypedDict):
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    RelatedFindings: NotRequired[Sequence[RelatedFindingTypeDef]]
    Severity: NotRequired[FindingProviderSeverityTypeDef]
    Types: NotRequired[Sequence[str]]

GeneratorDetailsUnionTypeDef = Union[GeneratorDetailsTypeDef, GeneratorDetailsOutputTypeDef]

class GetAdministratorAccountResponseTypeDef(TypedDict):
    Administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(TypedDict):
    Master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(TypedDict):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetFindingHistoryRequestPaginateTypeDef(TypedDict):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetFindingHistoryRequestTypeDef(TypedDict):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetMembersResponseTypeDef(TypedDict):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(TypedDict):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

SignalOutputTypeDef = TypedDict(
    "SignalOutputTypeDef",
    {
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "ProductArn": NotRequired[str],
        "ResourceIds": NotRequired[List[str]],
        "SignalIndicators": NotRequired[List[IndicatorOutputTypeDef]],
        "Name": NotRequired[str],
        "CreatedAt": NotRequired[int],
        "UpdatedAt": NotRequired[int],
        "FirstSeenAt": NotRequired[int],
        "LastSeenAt": NotRequired[int],
        "Severity": NotRequired[float],
        "Count": NotRequired[int],
        "ActorIds": NotRequired[List[str]],
        "EndpointIds": NotRequired[List[str]],
    },
)
IndicatorUnionTypeDef = Union[IndicatorTypeDef, IndicatorOutputTypeDef]
SignalTypeDef = TypedDict(
    "SignalTypeDef",
    {
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "ProductArn": NotRequired[str],
        "ResourceIds": NotRequired[Sequence[str]],
        "SignalIndicators": NotRequired[Sequence[IndicatorTypeDef]],
        "Name": NotRequired[str],
        "CreatedAt": NotRequired[int],
        "UpdatedAt": NotRequired[int],
        "FirstSeenAt": NotRequired[int],
        "LastSeenAt": NotRequired[int],
        "Severity": NotRequired[float],
        "Count": NotRequired[int],
        "ActorIds": NotRequired[Sequence[str]],
        "EndpointIds": NotRequired[Sequence[str]],
    },
)

class InsightResultsTypeDef(TypedDict):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List[InsightResultValueTypeDef]

class ListStandardsControlAssociationsResponseTypeDef(TypedDict):
    StandardsControlAssociationSummaries: List[StandardsControlAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class NetworkEndpointTypeDef(TypedDict):
    Id: NotRequired[str]
    Ip: NotRequired[str]
    Domain: NotRequired[str]
    Port: NotRequired[int]
    Location: NotRequired[NetworkGeoLocationTypeDef]
    AutonomousSystem: NotRequired[NetworkAutonomousSystemTypeDef]
    Connection: NotRequired[NetworkConnectionTypeDef]

class NetworkPathComponentDetailsOutputTypeDef(TypedDict):
    Address: NotRequired[List[str]]
    PortRanges: NotRequired[List[PortRangeTypeDef]]

class NetworkPathComponentDetailsTypeDef(TypedDict):
    Address: NotRequired[Sequence[str]]
    PortRanges: NotRequired[Sequence[PortRangeTypeDef]]

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NotRequired[NetworkDirectionType],
        "Protocol": NotRequired[str],
        "OpenPortRange": NotRequired[PortRangeTypeDef],
        "SourceIpV4": NotRequired[str],
        "SourceIpV6": NotRequired[str],
        "SourcePort": NotRequired[int],
        "SourceDomain": NotRequired[str],
        "SourceMac": NotRequired[str],
        "DestinationIpV4": NotRequired[str],
        "DestinationIpV6": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "DestinationDomain": NotRequired[str],
    },
)

class PageTypeDef(TypedDict):
    PageNumber: NotRequired[int]
    LineRange: NotRequired[RangeTypeDef]
    OffsetRange: NotRequired[RangeTypeDef]

class ParameterConfigurationOutputTypeDef(TypedDict):
    ValueType: ParameterValueTypeType
    Value: NotRequired[ParameterValueOutputTypeDef]

ParameterValueUnionTypeDef = Union[ParameterValueTypeDef, ParameterValueOutputTypeDef]

class RemediationTypeDef(TypedDict):
    Recommendation: NotRequired[RecommendationTypeDef]

RuleGroupSourceListDetailsUnionTypeDef = Union[
    RuleGroupSourceListDetailsTypeDef, RuleGroupSourceListDetailsOutputTypeDef
]

class RuleGroupSourceStatefulRulesDetailsOutputTypeDef(TypedDict):
    Action: NotRequired[str]
    Header: NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef]
    RuleOptions: NotRequired[List[RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef]]

RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef = Union[
    RuleGroupSourceStatefulRulesOptionsDetailsTypeDef,
    RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef,
]

class RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef(TypedDict):
    DestinationPorts: NotRequired[
        List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
    ]
    Destinations: NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]]
    Protocols: NotRequired[List[int]]
    SourcePorts: NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]]
    Sources: NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]]
    TcpFlags: NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef]]

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef,
    RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef,
]
RuleGroupVariablesIpSetsDetailsUnionTypeDef = Union[
    RuleGroupVariablesIpSetsDetailsTypeDef, RuleGroupVariablesIpSetsDetailsOutputTypeDef
]

class RuleGroupVariablesOutputTypeDef(TypedDict):
    IpSets: NotRequired[RuleGroupVariablesIpSetsDetailsOutputTypeDef]
    PortSets: NotRequired[RuleGroupVariablesPortSetsDetailsOutputTypeDef]

RuleGroupVariablesPortSetsDetailsUnionTypeDef = Union[
    RuleGroupVariablesPortSetsDetailsTypeDef, RuleGroupVariablesPortSetsDetailsOutputTypeDef
]
SecurityControlParameterUnionTypeDef = Union[
    SecurityControlParameterTypeDef, SecurityControlParameterOutputTypeDef
]

class StandardTypeDef(TypedDict):
    StandardsArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    EnabledByDefault: NotRequired[bool]
    StandardsManagedBy: NotRequired[StandardsManagedByTypeDef]

class StandardsSubscriptionTypeDef(TypedDict):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatusType
    StandardsControlsUpdatable: NotRequired[StandardsControlsUpdatableType]
    StandardsStatusReason: NotRequired[StandardsStatusReasonTypeDef]

class StatelessCustomPublishMetricActionOutputTypeDef(TypedDict):
    Dimensions: NotRequired[List[StatelessCustomPublishMetricActionDimensionTypeDef]]

class StatelessCustomPublishMetricActionTypeDef(TypedDict):
    Dimensions: NotRequired[Sequence[StatelessCustomPublishMetricActionDimensionTypeDef]]

AwsApiCallActionOutputTypeDef = TypedDict(
    "AwsApiCallActionOutputTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Dict[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Mapping[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "RemotePortDetails": NotRequired[ActionRemotePortDetailsTypeDef],
        "LocalPortDetails": NotRequired[ActionLocalPortDetailsTypeDef],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)

class PortProbeDetailTypeDef(TypedDict):
    LocalPortDetails: NotRequired[ActionLocalPortDetailsTypeDef]
    LocalIpDetails: NotRequired[ActionLocalIpDetailsTypeDef]
    RemoteIpDetails: NotRequired[ActionRemoteIpDetailsTypeDef]

class ActorTypeDef(TypedDict):
    Id: NotRequired[str]
    User: NotRequired[ActorUserTypeDef]
    Session: NotRequired[ActorSessionTypeDef]

CvssUnionTypeDef = Union[CvssTypeDef, CvssOutputTypeDef]

class AwsEc2RouteTableDetailsOutputTypeDef(TypedDict):
    AssociationSet: NotRequired[List[AssociationSetDetailsTypeDef]]
    OwnerId: NotRequired[str]
    PropagatingVgwSet: NotRequired[List[PropagatingVgwSetDetailsTypeDef]]
    RouteTableId: NotRequired[str]
    RouteSet: NotRequired[List[RouteSetDetailsTypeDef]]
    VpcId: NotRequired[str]

class AwsEc2RouteTableDetailsTypeDef(TypedDict):
    AssociationSet: NotRequired[Sequence[AssociationSetDetailsTypeDef]]
    OwnerId: NotRequired[str]
    PropagatingVgwSet: NotRequired[Sequence[PropagatingVgwSetDetailsTypeDef]]
    RouteTableId: NotRequired[str]
    RouteSet: NotRequired[Sequence[RouteSetDetailsTypeDef]]
    VpcId: NotRequired[str]

AutomationRulesActionOutputTypeDef = TypedDict(
    "AutomationRulesActionOutputTypeDef",
    {
        "Type": NotRequired[Literal["FINDING_FIELDS_UPDATE"]],
        "FindingFieldsUpdate": NotRequired[AutomationRulesFindingFieldsUpdateOutputTypeDef],
    },
)
AutomationRulesFindingFieldsUpdateUnionTypeDef = Union[
    AutomationRulesFindingFieldsUpdateTypeDef, AutomationRulesFindingFieldsUpdateOutputTypeDef
]

class AwsAmazonMqBrokerDetailsOutputTypeDef(TypedDict):
    AuthenticationStrategy: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    BrokerArn: NotRequired[str]
    BrokerName: NotRequired[str]
    DeploymentMode: NotRequired[str]
    EncryptionOptions: NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef]
    EngineType: NotRequired[str]
    EngineVersion: NotRequired[str]
    HostInstanceType: NotRequired[str]
    BrokerId: NotRequired[str]
    LdapServerMetadata: NotRequired[AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef]
    Logs: NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef]
    MaintenanceWindowStartTime: NotRequired[
        AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
    ]
    PubliclyAccessible: NotRequired[bool]
    SecurityGroups: NotRequired[List[str]]
    StorageType: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    Users: NotRequired[List[AwsAmazonMqBrokerUsersDetailsTypeDef]]

class AwsAmazonMqBrokerDetailsTypeDef(TypedDict):
    AuthenticationStrategy: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    BrokerArn: NotRequired[str]
    BrokerName: NotRequired[str]
    DeploymentMode: NotRequired[str]
    EncryptionOptions: NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef]
    EngineType: NotRequired[str]
    EngineVersion: NotRequired[str]
    HostInstanceType: NotRequired[str]
    BrokerId: NotRequired[str]
    LdapServerMetadata: NotRequired[AwsAmazonMqBrokerLdapServerMetadataDetailsUnionTypeDef]
    Logs: NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef]
    MaintenanceWindowStartTime: NotRequired[
        AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
    ]
    PubliclyAccessible: NotRequired[bool]
    SecurityGroups: NotRequired[Sequence[str]]
    StorageType: NotRequired[str]
    SubnetIds: NotRequired[Sequence[str]]
    Users: NotRequired[Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef]]

class AwsApiGatewayStageDetailsTypeDef(TypedDict):
    DeploymentId: NotRequired[str]
    ClientCertificateId: NotRequired[str]
    StageName: NotRequired[str]
    Description: NotRequired[str]
    CacheClusterEnabled: NotRequired[bool]
    CacheClusterSize: NotRequired[str]
    CacheClusterStatus: NotRequired[str]
    MethodSettings: NotRequired[Sequence[AwsApiGatewayMethodSettingsTypeDef]]
    Variables: NotRequired[Mapping[str, str]]
    DocumentationVersion: NotRequired[str]
    AccessLogSettings: NotRequired[AwsApiGatewayAccessLogSettingsTypeDef]
    CanarySettings: NotRequired[AwsApiGatewayCanarySettingsUnionTypeDef]
    TracingEnabled: NotRequired[bool]
    CreatedDate: NotRequired[str]
    LastUpdatedDate: NotRequired[str]
    WebAclArn: NotRequired[str]

class AwsApiGatewayRestApiDetailsTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedDate: NotRequired[str]
    Version: NotRequired[str]
    BinaryMediaTypes: NotRequired[Sequence[str]]
    MinimumCompressionSize: NotRequired[int]
    ApiKeySource: NotRequired[str]
    EndpointConfiguration: NotRequired[AwsApiGatewayEndpointConfigurationUnionTypeDef]

AwsApiGatewayV2StageDetailsUnionTypeDef = Union[
    AwsApiGatewayV2StageDetailsTypeDef, AwsApiGatewayV2StageDetailsOutputTypeDef
]

class AwsAppSyncGraphQlApiDetailsOutputTypeDef(TypedDict):
    ApiId: NotRequired[str]
    Id: NotRequired[str]
    OpenIdConnectConfig: NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]
    Name: NotRequired[str]
    LambdaAuthorizerConfig: NotRequired[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]
    XrayEnabled: NotRequired[bool]
    Arn: NotRequired[str]
    UserPoolConfig: NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]
    AuthenticationType: NotRequired[str]
    LogConfig: NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef]
    AdditionalAuthenticationProviders: NotRequired[
        List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
    ]
    WafWebAclArn: NotRequired[str]

class AwsAppSyncGraphQlApiDetailsTypeDef(TypedDict):
    ApiId: NotRequired[str]
    Id: NotRequired[str]
    OpenIdConnectConfig: NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]
    Name: NotRequired[str]
    LambdaAuthorizerConfig: NotRequired[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]
    XrayEnabled: NotRequired[bool]
    Arn: NotRequired[str]
    UserPoolConfig: NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]
    AuthenticationType: NotRequired[str]
    LogConfig: NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef]
    AdditionalAuthenticationProviders: NotRequired[
        Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
    ]
    WafWebAclArn: NotRequired[str]

class AwsAthenaWorkGroupConfigurationDetailsTypeDef(TypedDict):
    ResultConfiguration: NotRequired[
        AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef
    ]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef(TypedDict):
    InstancesDistribution: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
    ]
    LaunchTemplate: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef
    ]

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef,
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef,
]

class AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef(TypedDict):
    AssociatePublicIpAddress: NotRequired[bool]
    BlockDeviceMappings: NotRequired[
        List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
    ]
    ClassicLinkVpcId: NotRequired[str]
    ClassicLinkVpcSecurityGroups: NotRequired[List[str]]
    CreatedTime: NotRequired[str]
    EbsOptimized: NotRequired[bool]
    IamInstanceProfile: NotRequired[str]
    ImageId: NotRequired[str]
    InstanceMonitoring: NotRequired[
        AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
    ]
    InstanceType: NotRequired[str]
    KernelId: NotRequired[str]
    KeyName: NotRequired[str]
    LaunchConfigurationName: NotRequired[str]
    PlacementTenancy: NotRequired[str]
    RamdiskId: NotRequired[str]
    SecurityGroups: NotRequired[List[str]]
    SpotPrice: NotRequired[str]
    UserData: NotRequired[str]
    MetadataOptions: NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef]

class AwsAutoScalingLaunchConfigurationDetailsTypeDef(TypedDict):
    AssociatePublicIpAddress: NotRequired[bool]
    BlockDeviceMappings: NotRequired[
        Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
    ]
    ClassicLinkVpcId: NotRequired[str]
    ClassicLinkVpcSecurityGroups: NotRequired[Sequence[str]]
    CreatedTime: NotRequired[str]
    EbsOptimized: NotRequired[bool]
    IamInstanceProfile: NotRequired[str]
    ImageId: NotRequired[str]
    InstanceMonitoring: NotRequired[
        AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
    ]
    InstanceType: NotRequired[str]
    KernelId: NotRequired[str]
    KeyName: NotRequired[str]
    LaunchConfigurationName: NotRequired[str]
    PlacementTenancy: NotRequired[str]
    RamdiskId: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]
    SpotPrice: NotRequired[str]
    UserData: NotRequired[str]
    MetadataOptions: NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef]

class AwsBackupBackupPlanRuleDetailsOutputTypeDef(TypedDict):
    TargetBackupVault: NotRequired[str]
    StartWindowMinutes: NotRequired[int]
    ScheduleExpression: NotRequired[str]
    RuleName: NotRequired[str]
    RuleId: NotRequired[str]
    EnableContinuousBackup: NotRequired[bool]
    CompletionWindowMinutes: NotRequired[int]
    CopyActions: NotRequired[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]]
    Lifecycle: NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef]

class AwsBackupBackupPlanRuleDetailsTypeDef(TypedDict):
    TargetBackupVault: NotRequired[str]
    StartWindowMinutes: NotRequired[int]
    ScheduleExpression: NotRequired[str]
    RuleName: NotRequired[str]
    RuleId: NotRequired[str]
    EnableContinuousBackup: NotRequired[bool]
    CompletionWindowMinutes: NotRequired[int]
    CopyActions: NotRequired[Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]]
    Lifecycle: NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef]

class AwsBackupBackupVaultDetailsTypeDef(TypedDict):
    BackupVaultArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    Notifications: NotRequired[AwsBackupBackupVaultNotificationsDetailsUnionTypeDef]
    AccessPolicy: NotRequired[str]

class AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef(TypedDict):
    DomainValidationOptions: NotRequired[
        List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]
    ]
    RenewalStatus: NotRequired[str]
    RenewalStatusReason: NotRequired[str]
    UpdatedAt: NotRequired[str]

AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef = Union[
    AwsCertificateManagerCertificateDomainValidationOptionTypeDef,
    AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef,
]

class AwsCertificateManagerCertificateRenewalSummaryTypeDef(TypedDict):
    DomainValidationOptions: NotRequired[
        Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]
    ]
    RenewalStatus: NotRequired[str]
    RenewalStatusReason: NotRequired[str]
    UpdatedAt: NotRequired[str]

AwsCloudFormationStackDetailsUnionTypeDef = Union[
    AwsCloudFormationStackDetailsTypeDef, AwsCloudFormationStackDetailsOutputTypeDef
]
AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef = Union[
    AwsCloudFrontDistributionCacheBehaviorsTypeDef,
    AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef,
]

class AwsCloudFrontDistributionOriginItemOutputTypeDef(TypedDict):
    DomainName: NotRequired[str]
    Id: NotRequired[str]
    OriginPath: NotRequired[str]
    S3OriginConfig: NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef]
    CustomOriginConfig: NotRequired[AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef]

class AwsCloudFrontDistributionOriginGroupOutputTypeDef(TypedDict):
    FailoverCriteria: NotRequired[AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef]

class AwsCloudFrontDistributionOriginGroupFailoverTypeDef(TypedDict):
    StatusCodes: NotRequired[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnionTypeDef]

class AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef(TypedDict):
    HttpPort: NotRequired[int]
    HttpsPort: NotRequired[int]
    OriginKeepaliveTimeout: NotRequired[int]
    OriginProtocolPolicy: NotRequired[str]
    OriginReadTimeout: NotRequired[int]
    OriginSslProtocols: NotRequired[AwsCloudFrontDistributionOriginSslProtocolsUnionTypeDef]

AwsCloudWatchAlarmDetailsUnionTypeDef = Union[
    AwsCloudWatchAlarmDetailsTypeDef, AwsCloudWatchAlarmDetailsOutputTypeDef
]
AwsCodeBuildProjectEnvironmentUnionTypeDef = Union[
    AwsCodeBuildProjectEnvironmentTypeDef, AwsCodeBuildProjectEnvironmentOutputTypeDef
]

class AwsCodeBuildProjectDetailsOutputTypeDef(TypedDict):
    EncryptionKey: NotRequired[str]
    Artifacts: NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]]
    Environment: NotRequired[AwsCodeBuildProjectEnvironmentOutputTypeDef]
    Name: NotRequired[str]
    Source: NotRequired[AwsCodeBuildProjectSourceTypeDef]
    ServiceRole: NotRequired[str]
    LogsConfig: NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef]
    VpcConfig: NotRequired[AwsCodeBuildProjectVpcConfigOutputTypeDef]
    SecondaryArtifacts: NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]]

class AwsApiGatewayV2ApiDetailsTypeDef(TypedDict):
    ApiEndpoint: NotRequired[str]
    ApiId: NotRequired[str]
    ApiKeySelectionExpression: NotRequired[str]
    CreatedDate: NotRequired[str]
    Description: NotRequired[str]
    Version: NotRequired[str]
    Name: NotRequired[str]
    ProtocolType: NotRequired[str]
    RouteSelectionExpression: NotRequired[str]
    CorsConfiguration: NotRequired[AwsCorsConfigurationUnionTypeDef]

AwsDmsReplicationInstanceDetailsUnionTypeDef = Union[
    AwsDmsReplicationInstanceDetailsTypeDef, AwsDmsReplicationInstanceDetailsOutputTypeDef
]

class AwsDynamoDbTableGlobalSecondaryIndexTypeDef(TypedDict):
    Backfilling: NotRequired[bool]
    IndexArn: NotRequired[str]
    IndexName: NotRequired[str]
    IndexSizeBytes: NotRequired[int]
    IndexStatus: NotRequired[str]
    ItemCount: NotRequired[int]
    KeySchema: NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]]
    Projection: NotRequired[AwsDynamoDbTableProjectionUnionTypeDef]
    ProvisionedThroughput: NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef]

class AwsDynamoDbTableLocalSecondaryIndexTypeDef(TypedDict):
    IndexArn: NotRequired[str]
    IndexName: NotRequired[str]
    KeySchema: NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]]
    Projection: NotRequired[AwsDynamoDbTableProjectionUnionTypeDef]

AwsDynamoDbTableReplicaOutputTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaOutputTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)
AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)

class AwsEc2ClientVpnEndpointDetailsOutputTypeDef(TypedDict):
    ClientVpnEndpointId: NotRequired[str]
    Description: NotRequired[str]
    ClientCidrBlock: NotRequired[str]
    DnsServer: NotRequired[List[str]]
    SplitTunnel: NotRequired[bool]
    TransportProtocol: NotRequired[str]
    VpnPort: NotRequired[int]
    ServerCertificateArn: NotRequired[str]
    AuthenticationOptions: NotRequired[
        List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
    ]
    ConnectionLogOptions: NotRequired[AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef]
    SecurityGroupIdSet: NotRequired[List[str]]
    VpcId: NotRequired[str]
    SelfServicePortalUrl: NotRequired[str]
    ClientConnectOptions: NotRequired[AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef]
    SessionTimeoutHours: NotRequired[int]
    ClientLoginBannerOptions: NotRequired[
        AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
    ]

class AwsEc2ClientVpnEndpointDetailsTypeDef(TypedDict):
    ClientVpnEndpointId: NotRequired[str]
    Description: NotRequired[str]
    ClientCidrBlock: NotRequired[str]
    DnsServer: NotRequired[Sequence[str]]
    SplitTunnel: NotRequired[bool]
    TransportProtocol: NotRequired[str]
    VpnPort: NotRequired[int]
    ServerCertificateArn: NotRequired[str]
    AuthenticationOptions: NotRequired[
        Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
    ]
    ConnectionLogOptions: NotRequired[AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef]
    SecurityGroupIdSet: NotRequired[Sequence[str]]
    VpcId: NotRequired[str]
    SelfServicePortalUrl: NotRequired[str]
    ClientConnectOptions: NotRequired[AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef]
    SessionTimeoutHours: NotRequired[int]
    ClientLoginBannerOptions: NotRequired[
        AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
    ]

AwsEc2InstanceDetailsUnionTypeDef = Union[
    AwsEc2InstanceDetailsTypeDef, AwsEc2InstanceDetailsOutputTypeDef
]
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef,
    AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef,
]

class AwsEc2LaunchTemplateDataDetailsOutputTypeDef(TypedDict):
    BlockDeviceMappingSet: NotRequired[
        List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
    ]
    CapacityReservationSpecification: NotRequired[
        AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
    ]
    CpuOptions: NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef]
    CreditSpecification: NotRequired[AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef]
    DisableApiStop: NotRequired[bool]
    DisableApiTermination: NotRequired[bool]
    EbsOptimized: NotRequired[bool]
    ElasticGpuSpecificationSet: NotRequired[
        List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
    ]
    ElasticInferenceAcceleratorSet: NotRequired[
        List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
    ]
    EnclaveOptions: NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef]
    HibernationOptions: NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef]
    IamInstanceProfile: NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef]
    ImageId: NotRequired[str]
    InstanceInitiatedShutdownBehavior: NotRequired[str]
    InstanceMarketOptions: NotRequired[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef]
    InstanceRequirements: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef
    ]
    InstanceType: NotRequired[str]
    KernelId: NotRequired[str]
    KeyName: NotRequired[str]
    LicenseSet: NotRequired[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]]
    MaintenanceOptions: NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef]
    MetadataOptions: NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef]
    Monitoring: NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef]
    NetworkInterfaceSet: NotRequired[
        List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef]
    ]
    Placement: NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef]
    PrivateDnsNameOptions: NotRequired[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef]
    RamDiskId: NotRequired[str]
    SecurityGroupIdSet: NotRequired[List[str]]
    SecurityGroupSet: NotRequired[List[str]]
    UserData: NotRequired[str]

AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef,
    AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef,
]

class AwsEc2NetworkAclDetailsOutputTypeDef(TypedDict):
    IsDefault: NotRequired[bool]
    NetworkAclId: NotRequired[str]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]
    Associations: NotRequired[List[AwsEc2NetworkAclAssociationTypeDef]]
    Entries: NotRequired[List[AwsEc2NetworkAclEntryTypeDef]]

class AwsEc2NetworkAclDetailsTypeDef(TypedDict):
    IsDefault: NotRequired[bool]
    NetworkAclId: NotRequired[str]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]
    Associations: NotRequired[Sequence[AwsEc2NetworkAclAssociationTypeDef]]
    Entries: NotRequired[Sequence[AwsEc2NetworkAclEntryTypeDef]]

AwsEc2NetworkInterfaceDetailsUnionTypeDef = Union[
    AwsEc2NetworkInterfaceDetailsTypeDef, AwsEc2NetworkInterfaceDetailsOutputTypeDef
]

class AwsEc2SecurityGroupDetailsOutputTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupId: NotRequired[str]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]
    IpPermissions: NotRequired[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]]
    IpPermissionsEgress: NotRequired[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]]

AwsEc2SecurityGroupIpPermissionUnionTypeDef = Union[
    AwsEc2SecurityGroupIpPermissionTypeDef, AwsEc2SecurityGroupIpPermissionOutputTypeDef
]
AwsEc2SubnetDetailsUnionTypeDef = Union[
    AwsEc2SubnetDetailsTypeDef, AwsEc2SubnetDetailsOutputTypeDef
]
AwsEc2VolumeDetailsUnionTypeDef = Union[
    AwsEc2VolumeDetailsTypeDef, AwsEc2VolumeDetailsOutputTypeDef
]
AwsEc2VpcDetailsUnionTypeDef = Union[AwsEc2VpcDetailsTypeDef, AwsEc2VpcDetailsOutputTypeDef]
AwsEc2VpcEndpointServiceDetailsUnionTypeDef = Union[
    AwsEc2VpcEndpointServiceDetailsTypeDef, AwsEc2VpcEndpointServiceDetailsOutputTypeDef
]

class AwsEc2VpcPeeringConnectionDetailsOutputTypeDef(TypedDict):
    AccepterVpcInfo: NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef]
    ExpirationTime: NotRequired[str]
    RequesterVpcInfo: NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef]
    Status: NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef]
    VpcPeeringConnectionId: NotRequired[str]

AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef = Union[
    AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef,
    AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef,
]
AwsEc2VpnConnectionDetailsOutputTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsOutputTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsOutputTypeDef],
        "Routes": NotRequired[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)

class AwsEc2VpnConnectionOptionsDetailsTypeDef(TypedDict):
    StaticRoutesOnly: NotRequired[bool]
    TunnelOptions: NotRequired[Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnionTypeDef]]

class AwsEcsClusterConfigurationDetailsTypeDef(TypedDict):
    ExecuteCommandConfiguration: NotRequired[
        AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef
    ]

AwsEcsContainerDetailsUnionTypeDef = Union[
    AwsEcsContainerDetailsTypeDef, AwsEcsContainerDetailsOutputTypeDef
]
AwsEcsServiceDetailsOutputTypeDef = TypedDict(
    "AwsEcsServiceDetailsOutputTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[List[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef],
        "PlacementConstraints": NotRequired[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]],
        "PlacementStrategies": NotRequired[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)

class AwsEcsServiceNetworkConfigurationDetailsTypeDef(TypedDict):
    AwsVpcConfiguration: NotRequired[
        AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnionTypeDef
    ]

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef(TypedDict):
    Capabilities: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnionTypeDef
    ]
    Devices: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnionTypeDef]
    ]
    InitProcessEnabled: NotRequired[bool]
    MaxSwap: NotRequired[int]
    SharedMemorySize: NotRequired[int]
    Swappiness: NotRequired[int]
    Tmpfs: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnionTypeDef]
    ]

class AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef(TypedDict):
    Command: NotRequired[List[str]]
    Cpu: NotRequired[int]
    DependsOn: NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]]
    DisableNetworking: NotRequired[bool]
    DnsSearchDomains: NotRequired[List[str]]
    DnsServers: NotRequired[List[str]]
    DockerLabels: NotRequired[Dict[str, str]]
    DockerSecurityOptions: NotRequired[List[str]]
    EntryPoint: NotRequired[List[str]]
    Environment: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
    ]
    EnvironmentFiles: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
    ]
    Essential: NotRequired[bool]
    ExtraHosts: NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]]
    FirelensConfiguration: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef
    ]
    HealthCheck: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef
    ]
    Hostname: NotRequired[str]
    Image: NotRequired[str]
    Interactive: NotRequired[bool]
    Links: NotRequired[List[str]]
    LinuxParameters: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef
    ]
    LogConfiguration: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef
    ]
    Memory: NotRequired[int]
    MemoryReservation: NotRequired[int]
    MountPoints: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
    ]
    Name: NotRequired[str]
    PortMappings: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
    ]
    Privileged: NotRequired[bool]
    PseudoTerminal: NotRequired[bool]
    ReadonlyRootFilesystem: NotRequired[bool]
    RepositoryCredentials: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
    ]
    ResourceRequirements: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
    ]
    Secrets: NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]]
    StartTimeout: NotRequired[int]
    StopTimeout: NotRequired[int]
    SystemControls: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
    ]
    Ulimits: NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]]
    User: NotRequired[str]
    VolumesFrom: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
    ]
    WorkingDirectory: NotRequired[str]

AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef,
    AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef,
]

class AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef(TypedDict):
    DockerVolumeConfiguration: NotRequired[
        AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef
    ]
    EfsVolumeConfiguration: NotRequired[
        AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
    ]
    Host: NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef]
    Name: NotRequired[str]

class AwsEcsTaskDefinitionVolumesDetailsTypeDef(TypedDict):
    DockerVolumeConfiguration: NotRequired[
        AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnionTypeDef
    ]
    EfsVolumeConfiguration: NotRequired[
        AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
    ]
    Host: NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef]
    Name: NotRequired[str]

class AwsEcsTaskDetailsOutputTypeDef(TypedDict):
    ClusterArn: NotRequired[str]
    TaskDefinitionArn: NotRequired[str]
    Version: NotRequired[str]
    CreatedAt: NotRequired[str]
    StartedAt: NotRequired[str]
    StartedBy: NotRequired[str]
    Group: NotRequired[str]
    Volumes: NotRequired[List[AwsEcsTaskVolumeDetailsTypeDef]]
    Containers: NotRequired[List[AwsEcsContainerDetailsOutputTypeDef]]

class AwsEfsAccessPointDetailsOutputTypeDef(TypedDict):
    AccessPointId: NotRequired[str]
    Arn: NotRequired[str]
    ClientToken: NotRequired[str]
    FileSystemId: NotRequired[str]
    PosixUser: NotRequired[AwsEfsAccessPointPosixUserDetailsOutputTypeDef]
    RootDirectory: NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef]

class AwsEfsAccessPointDetailsTypeDef(TypedDict):
    AccessPointId: NotRequired[str]
    Arn: NotRequired[str]
    ClientToken: NotRequired[str]
    FileSystemId: NotRequired[str]
    PosixUser: NotRequired[AwsEfsAccessPointPosixUserDetailsUnionTypeDef]
    RootDirectory: NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef]

class AwsEksClusterDetailsOutputTypeDef(TypedDict):
    Arn: NotRequired[str]
    CertificateAuthorityData: NotRequired[str]
    ClusterStatus: NotRequired[str]
    Endpoint: NotRequired[str]
    Name: NotRequired[str]
    ResourcesVpcConfig: NotRequired[AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef]
    RoleArn: NotRequired[str]
    Version: NotRequired[str]
    Logging: NotRequired[AwsEksClusterLoggingDetailsOutputTypeDef]

class AwsEksClusterLoggingDetailsTypeDef(TypedDict):
    ClusterLogging: NotRequired[Sequence[AwsEksClusterLoggingClusterLoggingDetailsUnionTypeDef]]

AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef = Union[
    AwsElasticBeanstalkEnvironmentDetailsTypeDef, AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef
]

class AwsElasticsearchDomainDetailsOutputTypeDef(TypedDict):
    AccessPolicies: NotRequired[str]
    DomainEndpointOptions: NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef]
    DomainId: NotRequired[str]
    DomainName: NotRequired[str]
    Endpoint: NotRequired[str]
    Endpoints: NotRequired[Dict[str, str]]
    ElasticsearchVersion: NotRequired[str]
    ElasticsearchClusterConfig: NotRequired[
        AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
    ]
    EncryptionAtRestOptions: NotRequired[AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef]
    LogPublishingOptions: NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[
        AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
    ]
    ServiceSoftwareOptions: NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef]
    VPCOptions: NotRequired[AwsElasticsearchDomainVPCOptionsOutputTypeDef]

class AwsElasticsearchDomainDetailsTypeDef(TypedDict):
    AccessPolicies: NotRequired[str]
    DomainEndpointOptions: NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef]
    DomainId: NotRequired[str]
    DomainName: NotRequired[str]
    Endpoint: NotRequired[str]
    Endpoints: NotRequired[Mapping[str, str]]
    ElasticsearchVersion: NotRequired[str]
    ElasticsearchClusterConfig: NotRequired[
        AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
    ]
    EncryptionAtRestOptions: NotRequired[AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef]
    LogPublishingOptions: NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[
        AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
    ]
    ServiceSoftwareOptions: NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef]
    VPCOptions: NotRequired[AwsElasticsearchDomainVPCOptionsUnionTypeDef]

AwsElbLoadBalancerPoliciesUnionTypeDef = Union[
    AwsElbLoadBalancerPoliciesTypeDef, AwsElbLoadBalancerPoliciesOutputTypeDef
]
AwsElbLoadBalancerAttributesUnionTypeDef = Union[
    AwsElbLoadBalancerAttributesTypeDef, AwsElbLoadBalancerAttributesOutputTypeDef
]

class AwsElbLoadBalancerDetailsOutputTypeDef(TypedDict):
    AvailabilityZones: NotRequired[List[str]]
    BackendServerDescriptions: NotRequired[
        List[AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef]
    ]
    CanonicalHostedZoneName: NotRequired[str]
    CanonicalHostedZoneNameID: NotRequired[str]
    CreatedTime: NotRequired[str]
    DnsName: NotRequired[str]
    HealthCheck: NotRequired[AwsElbLoadBalancerHealthCheckTypeDef]
    Instances: NotRequired[List[AwsElbLoadBalancerInstanceTypeDef]]
    ListenerDescriptions: NotRequired[List[AwsElbLoadBalancerListenerDescriptionOutputTypeDef]]
    LoadBalancerAttributes: NotRequired[AwsElbLoadBalancerAttributesOutputTypeDef]
    LoadBalancerName: NotRequired[str]
    Policies: NotRequired[AwsElbLoadBalancerPoliciesOutputTypeDef]
    Scheme: NotRequired[str]
    SecurityGroups: NotRequired[List[str]]
    SourceSecurityGroup: NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef]
    Subnets: NotRequired[List[str]]
    VpcId: NotRequired[str]

AwsElbLoadBalancerListenerDescriptionUnionTypeDef = Union[
    AwsElbLoadBalancerListenerDescriptionTypeDef, AwsElbLoadBalancerListenerDescriptionOutputTypeDef
]
AwsElbv2LoadBalancerDetailsUnionTypeDef = Union[
    AwsElbv2LoadBalancerDetailsTypeDef, AwsElbv2LoadBalancerDetailsOutputTypeDef
]

class AwsEventsEndpointRoutingConfigDetailsTypeDef(TypedDict):
    FailoverConfig: NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef]

class AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef(TypedDict):
    ScanEc2InstanceWithFindings: NotRequired[
        AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef
    ]
    ServiceRole: NotRequired[str]

class AwsIamAccessKeyDetailsTypeDef(TypedDict):
    UserName: NotRequired[str]
    Status: NotRequired[AwsIamAccessKeyStatusType]
    CreatedAt: NotRequired[str]
    PrincipalId: NotRequired[str]
    PrincipalType: NotRequired[str]
    PrincipalName: NotRequired[str]
    AccountId: NotRequired[str]
    AccessKeyId: NotRequired[str]
    SessionContext: NotRequired[AwsIamAccessKeySessionContextTypeDef]

AwsIamGroupDetailsUnionTypeDef = Union[AwsIamGroupDetailsTypeDef, AwsIamGroupDetailsOutputTypeDef]

class AwsIamRoleDetailsOutputTypeDef(TypedDict):
    AssumeRolePolicyDocument: NotRequired[str]
    AttachedManagedPolicies: NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    InstanceProfileList: NotRequired[List[AwsIamInstanceProfileOutputTypeDef]]
    PermissionsBoundary: NotRequired[AwsIamPermissionsBoundaryTypeDef]
    RoleId: NotRequired[str]
    RoleName: NotRequired[str]
    RolePolicyList: NotRequired[List[AwsIamRolePolicyTypeDef]]
    MaxSessionDuration: NotRequired[int]
    Path: NotRequired[str]

AwsIamInstanceProfileUnionTypeDef = Union[
    AwsIamInstanceProfileTypeDef, AwsIamInstanceProfileOutputTypeDef
]
AwsIamPolicyDetailsUnionTypeDef = Union[
    AwsIamPolicyDetailsTypeDef, AwsIamPolicyDetailsOutputTypeDef
]
AwsIamUserDetailsUnionTypeDef = Union[AwsIamUserDetailsTypeDef, AwsIamUserDetailsOutputTypeDef]

class AwsLambdaFunctionDetailsOutputTypeDef(TypedDict):
    Code: NotRequired[AwsLambdaFunctionCodeTypeDef]
    CodeSha256: NotRequired[str]
    DeadLetterConfig: NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef]
    Environment: NotRequired[AwsLambdaFunctionEnvironmentOutputTypeDef]
    FunctionName: NotRequired[str]
    Handler: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    LastModified: NotRequired[str]
    Layers: NotRequired[List[AwsLambdaFunctionLayerTypeDef]]
    MasterArn: NotRequired[str]
    MemorySize: NotRequired[int]
    RevisionId: NotRequired[str]
    Role: NotRequired[str]
    Runtime: NotRequired[str]
    Timeout: NotRequired[int]
    TracingConfig: NotRequired[AwsLambdaFunctionTracingConfigTypeDef]
    VpcConfig: NotRequired[AwsLambdaFunctionVpcConfigOutputTypeDef]
    Version: NotRequired[str]
    Architectures: NotRequired[List[str]]
    PackageType: NotRequired[str]

AwsLambdaFunctionEnvironmentUnionTypeDef = Union[
    AwsLambdaFunctionEnvironmentTypeDef, AwsLambdaFunctionEnvironmentOutputTypeDef
]

class AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef(TypedDict):
    Sasl: NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef]
    Unauthenticated: NotRequired[
        AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
    ]
    Tls: NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef]

class AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef(TypedDict):
    Sasl: NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef]
    Unauthenticated: NotRequired[
        AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
    ]
    Tls: NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnionTypeDef]

AwsNetworkFirewallFirewallDetailsUnionTypeDef = Union[
    AwsNetworkFirewallFirewallDetailsTypeDef, AwsNetworkFirewallFirewallDetailsOutputTypeDef
]

class AwsOpenSearchServiceDomainDetailsOutputTypeDef(TypedDict):
    Arn: NotRequired[str]
    AccessPolicies: NotRequired[str]
    DomainName: NotRequired[str]
    Id: NotRequired[str]
    DomainEndpoint: NotRequired[str]
    EngineVersion: NotRequired[str]
    EncryptionAtRestOptions: NotRequired[
        AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
    ]
    NodeToNodeEncryptionOptions: NotRequired[
        AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
    ]
    ServiceSoftwareOptions: NotRequired[
        AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
    ]
    ClusterConfig: NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef]
    DomainEndpointOptions: NotRequired[
        AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
    ]
    VpcOptions: NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef]
    LogPublishingOptions: NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef]
    DomainEndpoints: NotRequired[Dict[str, str]]
    AdvancedSecurityOptions: NotRequired[
        AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
    ]

class AwsOpenSearchServiceDomainDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    AccessPolicies: NotRequired[str]
    DomainName: NotRequired[str]
    Id: NotRequired[str]
    DomainEndpoint: NotRequired[str]
    EngineVersion: NotRequired[str]
    EncryptionAtRestOptions: NotRequired[
        AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
    ]
    NodeToNodeEncryptionOptions: NotRequired[
        AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
    ]
    ServiceSoftwareOptions: NotRequired[
        AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
    ]
    ClusterConfig: NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef]
    DomainEndpointOptions: NotRequired[
        AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
    ]
    VpcOptions: NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsUnionTypeDef]
    LogPublishingOptions: NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef]
    DomainEndpoints: NotRequired[Mapping[str, str]]
    AdvancedSecurityOptions: NotRequired[
        AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
    ]

AwsRdsDbClusterDetailsUnionTypeDef = Union[
    AwsRdsDbClusterDetailsTypeDef, AwsRdsDbClusterDetailsOutputTypeDef
]

class AwsRdsDbClusterSnapshotDetailsTypeDef(TypedDict):
    AvailabilityZones: NotRequired[Sequence[str]]
    SnapshotCreateTime: NotRequired[str]
    Engine: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    Status: NotRequired[str]
    Port: NotRequired[int]
    VpcId: NotRequired[str]
    ClusterCreateTime: NotRequired[str]
    MasterUsername: NotRequired[str]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    SnapshotType: NotRequired[str]
    PercentProgress: NotRequired[int]
    StorageEncrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    DbClusterIdentifier: NotRequired[str]
    DbClusterSnapshotIdentifier: NotRequired[str]
    IamDatabaseAuthenticationEnabled: NotRequired[bool]
    DbClusterSnapshotAttributes: NotRequired[
        Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnionTypeDef]
    ]

AwsRdsDbSnapshotDetailsUnionTypeDef = Union[
    AwsRdsDbSnapshotDetailsTypeDef, AwsRdsDbSnapshotDetailsOutputTypeDef
]
AwsRdsDbSecurityGroupDetailsUnionTypeDef = Union[
    AwsRdsDbSecurityGroupDetailsTypeDef, AwsRdsDbSecurityGroupDetailsOutputTypeDef
]

class AwsRdsDbSubnetGroupOutputTypeDef(TypedDict):
    DbSubnetGroupName: NotRequired[str]
    DbSubnetGroupDescription: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetGroupStatus: NotRequired[str]
    Subnets: NotRequired[List[AwsRdsDbSubnetGroupSubnetTypeDef]]
    DbSubnetGroupArn: NotRequired[str]

class AwsRdsDbSubnetGroupTypeDef(TypedDict):
    DbSubnetGroupName: NotRequired[str]
    DbSubnetGroupDescription: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetGroupStatus: NotRequired[str]
    Subnets: NotRequired[Sequence[AwsRdsDbSubnetGroupSubnetTypeDef]]
    DbSubnetGroupArn: NotRequired[str]

class AwsRdsDbPendingModifiedValuesTypeDef(TypedDict):
    DbInstanceClass: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    MasterUserPassword: NotRequired[str]
    Port: NotRequired[int]
    BackupRetentionPeriod: NotRequired[int]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    DbInstanceIdentifier: NotRequired[str]
    StorageType: NotRequired[str]
    CaCertificateIdentifier: NotRequired[str]
    DbSubnetGroupName: NotRequired[str]
    PendingCloudWatchLogsExports: NotRequired[AwsRdsPendingCloudWatchLogsExportsUnionTypeDef]
    ProcessorFeatures: NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]]

class AwsRedshiftClusterDetailsOutputTypeDef(TypedDict):
    AllowVersionUpgrade: NotRequired[bool]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    ClusterAvailabilityStatus: NotRequired[str]
    ClusterCreateTime: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    ClusterNodes: NotRequired[List[AwsRedshiftClusterClusterNodeTypeDef]]
    ClusterParameterGroups: NotRequired[List[AwsRedshiftClusterClusterParameterGroupOutputTypeDef]]
    ClusterPublicKey: NotRequired[str]
    ClusterRevisionNumber: NotRequired[str]
    ClusterSecurityGroups: NotRequired[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]]
    ClusterSnapshotCopyStatus: NotRequired[AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef]
    ClusterStatus: NotRequired[str]
    ClusterSubnetGroupName: NotRequired[str]
    ClusterVersion: NotRequired[str]
    DBName: NotRequired[str]
    DeferredMaintenanceWindows: NotRequired[
        List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
    ]
    ElasticIpStatus: NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef]
    ElasticResizeNumberOfNodeOptions: NotRequired[str]
    Encrypted: NotRequired[bool]
    Endpoint: NotRequired[AwsRedshiftClusterEndpointTypeDef]
    EnhancedVpcRouting: NotRequired[bool]
    ExpectedNextSnapshotScheduleTime: NotRequired[str]
    ExpectedNextSnapshotScheduleTimeStatus: NotRequired[str]
    HsmStatus: NotRequired[AwsRedshiftClusterHsmStatusTypeDef]
    IamRoles: NotRequired[List[AwsRedshiftClusterIamRoleTypeDef]]
    KmsKeyId: NotRequired[str]
    MaintenanceTrackName: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    MasterUsername: NotRequired[str]
    NextMaintenanceWindowStartTime: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    PendingActions: NotRequired[List[str]]
    PendingModifiedValues: NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    ResizeInfo: NotRequired[AwsRedshiftClusterResizeInfoTypeDef]
    RestoreStatus: NotRequired[AwsRedshiftClusterRestoreStatusTypeDef]
    SnapshotScheduleIdentifier: NotRequired[str]
    SnapshotScheduleState: NotRequired[str]
    VpcId: NotRequired[str]
    VpcSecurityGroups: NotRequired[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]]
    LoggingStatus: NotRequired[AwsRedshiftClusterLoggingStatusTypeDef]

AwsRedshiftClusterClusterParameterGroupUnionTypeDef = Union[
    AwsRedshiftClusterClusterParameterGroupTypeDef,
    AwsRedshiftClusterClusterParameterGroupOutputTypeDef,
]

class AwsRoute53HostedZoneDetailsOutputTypeDef(TypedDict):
    HostedZone: NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef]
    Vpcs: NotRequired[List[AwsRoute53HostedZoneVpcDetailsTypeDef]]
    NameServers: NotRequired[List[str]]
    QueryLoggingConfig: NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef]

class AwsRoute53HostedZoneDetailsTypeDef(TypedDict):
    HostedZone: NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef]
    Vpcs: NotRequired[Sequence[AwsRoute53HostedZoneVpcDetailsTypeDef]]
    NameServers: NotRequired[Sequence[str]]
    QueryLoggingConfig: NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef]

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef",
    {
        "Operands": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": NotRequired[
            Sequence[
                AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)

class AwsS3BucketNotificationConfigurationFilterOutputTypeDef(TypedDict):
    S3KeyFilter: NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef]

AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef,
    AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef,
]

class AwsS3BucketObjectLockConfigurationTypeDef(TypedDict):
    ObjectLockEnabled: NotRequired[str]
    Rule: NotRequired[AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef]

class AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef(TypedDict):
    Rules: NotRequired[List[AwsS3BucketServerSideEncryptionRuleTypeDef]]

class AwsS3BucketServerSideEncryptionConfigurationTypeDef(TypedDict):
    Rules: NotRequired[Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef]]

class AwsS3BucketWebsiteConfigurationOutputTypeDef(TypedDict):
    ErrorDocument: NotRequired[str]
    IndexDocumentSuffix: NotRequired[str]
    RedirectAllRequestsTo: NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef]
    RoutingRules: NotRequired[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]]

class AwsS3BucketWebsiteConfigurationTypeDef(TypedDict):
    ErrorDocument: NotRequired[str]
    IndexDocumentSuffix: NotRequired[str]
    RedirectAllRequestsTo: NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef]
    RoutingRules: NotRequired[Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]]

AwsSageMakerNotebookInstanceDetailsUnionTypeDef = Union[
    AwsSageMakerNotebookInstanceDetailsTypeDef, AwsSageMakerNotebookInstanceDetailsOutputTypeDef
]

class BatchUpdateFindingsResponseTypeDef(TypedDict):
    ProcessedFindings: List[AwsSecurityFindingIdentifierTypeDef]
    UnprocessedFindings: List[BatchUpdateFindingsUnprocessedFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

AwsSnsTopicDetailsUnionTypeDef = Union[AwsSnsTopicDetailsTypeDef, AwsSnsTopicDetailsOutputTypeDef]

class AwsSsmPatchComplianceDetailsTypeDef(TypedDict):
    Patch: NotRequired[AwsSsmPatchTypeDef]

class AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef(TypedDict):
    Destinations: NotRequired[
        List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
    ]
    IncludeExecutionData: NotRequired[bool]
    Level: NotRequired[str]

class AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef(TypedDict):
    Destinations: NotRequired[
        Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
    ]
    IncludeExecutionData: NotRequired[bool]
    Level: NotRequired[str]

AwsWafRateBasedRuleDetailsUnionTypeDef = Union[
    AwsWafRateBasedRuleDetailsTypeDef, AwsWafRateBasedRuleDetailsOutputTypeDef
]
AwsWafRegionalRateBasedRuleDetailsUnionTypeDef = Union[
    AwsWafRegionalRateBasedRuleDetailsTypeDef, AwsWafRegionalRateBasedRuleDetailsOutputTypeDef
]
AwsWafRegionalRuleDetailsUnionTypeDef = Union[
    AwsWafRegionalRuleDetailsTypeDef, AwsWafRegionalRuleDetailsOutputTypeDef
]

class AwsWafRegionalRuleGroupDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RuleGroupId: NotRequired[str]
    Rules: NotRequired[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]]

class AwsWafRegionalRuleGroupDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RuleGroupId: NotRequired[str]
    Rules: NotRequired[Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef]]

class AwsWafRegionalWebAclDetailsOutputTypeDef(TypedDict):
    DefaultAction: NotRequired[str]
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RulesList: NotRequired[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]]
    WebAclId: NotRequired[str]

class AwsWafRegionalWebAclDetailsTypeDef(TypedDict):
    DefaultAction: NotRequired[str]
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RulesList: NotRequired[Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef]]
    WebAclId: NotRequired[str]

AwsWafRuleDetailsUnionTypeDef = Union[AwsWafRuleDetailsTypeDef, AwsWafRuleDetailsOutputTypeDef]

class AwsWafRuleGroupDetailsOutputTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RuleGroupId: NotRequired[str]
    Rules: NotRequired[List[AwsWafRuleGroupRulesDetailsTypeDef]]

class AwsWafRuleGroupDetailsTypeDef(TypedDict):
    MetricName: NotRequired[str]
    Name: NotRequired[str]
    RuleGroupId: NotRequired[str]
    Rules: NotRequired[Sequence[AwsWafRuleGroupRulesDetailsTypeDef]]

class AwsWafWebAclDetailsOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    DefaultAction: NotRequired[str]
    Rules: NotRequired[List[AwsWafWebAclRuleOutputTypeDef]]
    WebAclId: NotRequired[str]

AwsWafWebAclRuleUnionTypeDef = Union[AwsWafWebAclRuleTypeDef, AwsWafWebAclRuleOutputTypeDef]

class AwsWafv2ActionAllowDetailsOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]

class AwsWafv2RulesActionCaptchaDetailsOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]

class AwsWafv2RulesActionCountDetailsOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]

AwsWafv2CustomRequestHandlingDetailsUnionTypeDef = Union[
    AwsWafv2CustomRequestHandlingDetailsTypeDef, AwsWafv2CustomRequestHandlingDetailsOutputTypeDef
]

class AwsWafv2ActionBlockDetailsOutputTypeDef(TypedDict):
    CustomResponse: NotRequired[AwsWafv2CustomResponseDetailsOutputTypeDef]

AwsWafv2CustomResponseDetailsUnionTypeDef = Union[
    AwsWafv2CustomResponseDetailsTypeDef, AwsWafv2CustomResponseDetailsOutputTypeDef
]

class BatchGetStandardsControlAssociationsResponseTypeDef(TypedDict):
    StandardsControlAssociationDetails: List[StandardsControlAssociationDetailTypeDef]
    UnprocessedAssociations: List[UnprocessedStandardsControlAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsResponseTypeDef(TypedDict):
    UnprocessedAssociationUpdates: List[UnprocessedStandardsControlAssociationUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VulnerabilityOutputTypeDef(TypedDict):
    Id: str
    VulnerablePackages: NotRequired[List[SoftwarePackageTypeDef]]
    Cvss: NotRequired[List[CvssOutputTypeDef]]
    RelatedVulnerabilities: NotRequired[List[str]]
    Vendor: NotRequired[VulnerabilityVendorTypeDef]
    ReferenceUrls: NotRequired[List[str]]
    FixAvailable: NotRequired[VulnerabilityFixAvailableType]
    EpssScore: NotRequired[float]
    ExploitAvailable: NotRequired[VulnerabilityExploitAvailableType]
    LastKnownExploitAt: NotRequired[str]
    CodeVulnerabilities: NotRequired[List[VulnerabilityCodeVulnerabilitiesOutputTypeDef]]

VulnerabilityCodeVulnerabilitiesUnionTypeDef = Union[
    VulnerabilityCodeVulnerabilitiesTypeDef, VulnerabilityCodeVulnerabilitiesOutputTypeDef
]

class ParameterDefinitionTypeDef(TypedDict):
    Description: str
    ConfigurationOptions: ConfigurationOptionsTypeDef

class BatchGetConfigurationPolicyAssociationsRequestTypeDef(TypedDict):
    ConfigurationPolicyAssociationIdentifiers: Sequence[ConfigurationPolicyAssociationTypeDef]

class UnprocessedConfigurationPolicyAssociationTypeDef(TypedDict):
    ConfigurationPolicyAssociationIdentifiers: NotRequired[ConfigurationPolicyAssociationTypeDef]
    ErrorCode: NotRequired[str]
    ErrorReason: NotRequired[str]

ContainerDetailsUnionTypeDef = Union[ContainerDetailsTypeDef, ContainerDetailsOutputTypeDef]
AutomationRulesFindingFiltersOutputTypeDef = TypedDict(
    "AutomationRulesFindingFiltersOutputTypeDef",
    {
        "ProductArn": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[List[StringFilterTypeDef]],
        "Id": NotRequired[List[StringFilterTypeDef]],
        "GeneratorId": NotRequired[List[StringFilterTypeDef]],
        "Type": NotRequired[List[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[List[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "CreatedAt": NotRequired[List[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "Confidence": NotRequired[List[NumberFilterTypeDef]],
        "Criticality": NotRequired[List[NumberFilterTypeDef]],
        "Title": NotRequired[List[StringFilterTypeDef]],
        "Description": NotRequired[List[StringFilterTypeDef]],
        "SourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ProductName": NotRequired[List[StringFilterTypeDef]],
        "CompanyName": NotRequired[List[StringFilterTypeDef]],
        "SeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "ResourceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceId": NotRequired[List[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[List[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[List[StringFilterTypeDef]],
        "ResourceTags": NotRequired[List[MapFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[List[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[List[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[List[StringFilterTypeDef]],
        "VerificationState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[List[StringFilterTypeDef]],
        "RecordState": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "NoteText": NotRequired[List[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[List[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[List[MapFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[List[StringFilterTypeDef]],
    },
)
AutomationRulesFindingFiltersTypeDef = TypedDict(
    "AutomationRulesFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "Id": NotRequired[Sequence[StringFilterTypeDef]],
        "GeneratorId": NotRequired[Sequence[StringFilterTypeDef]],
        "Type": NotRequired[Sequence[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "CreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "Confidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "Criticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "Title": NotRequired[Sequence[StringFilterTypeDef]],
        "Description": NotRequired[Sequence[StringFilterTypeDef]],
        "SourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ProductName": NotRequired[Sequence[StringFilterTypeDef]],
        "CompanyName": NotRequired[Sequence[StringFilterTypeDef]],
        "SeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[Sequence[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[Sequence[StringFilterTypeDef]],
        "VerificationState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "RecordState": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteText": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[Sequence[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
AwsSecurityFindingFiltersOutputTypeDef = TypedDict(
    "AwsSecurityFindingFiltersOutputTypeDef",
    {
        "ProductArn": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[List[StringFilterTypeDef]],
        "Id": NotRequired[List[StringFilterTypeDef]],
        "GeneratorId": NotRequired[List[StringFilterTypeDef]],
        "Region": NotRequired[List[StringFilterTypeDef]],
        "Type": NotRequired[List[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[List[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "CreatedAt": NotRequired[List[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "SeverityProduct": NotRequired[List[NumberFilterTypeDef]],
        "SeverityNormalized": NotRequired[List[NumberFilterTypeDef]],
        "SeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "Confidence": NotRequired[List[NumberFilterTypeDef]],
        "Criticality": NotRequired[List[NumberFilterTypeDef]],
        "Title": NotRequired[List[StringFilterTypeDef]],
        "Description": NotRequired[List[StringFilterTypeDef]],
        "RecommendationText": NotRequired[List[StringFilterTypeDef]],
        "SourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ProductFields": NotRequired[List[MapFilterTypeDef]],
        "ProductName": NotRequired[List[StringFilterTypeDef]],
        "CompanyName": NotRequired[List[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[List[MapFilterTypeDef]],
        "MalwareName": NotRequired[List[StringFilterTypeDef]],
        "MalwareType": NotRequired[List[StringFilterTypeDef]],
        "MalwarePath": NotRequired[List[StringFilterTypeDef]],
        "MalwareState": NotRequired[List[StringFilterTypeDef]],
        "NetworkDirection": NotRequired[List[StringFilterTypeDef]],
        "NetworkProtocol": NotRequired[List[StringFilterTypeDef]],
        "NetworkSourceIpV4": NotRequired[List[IpFilterTypeDef]],
        "NetworkSourceIpV6": NotRequired[List[IpFilterTypeDef]],
        "NetworkSourcePort": NotRequired[List[NumberFilterTypeDef]],
        "NetworkSourceDomain": NotRequired[List[StringFilterTypeDef]],
        "NetworkSourceMac": NotRequired[List[StringFilterTypeDef]],
        "NetworkDestinationIpV4": NotRequired[List[IpFilterTypeDef]],
        "NetworkDestinationIpV6": NotRequired[List[IpFilterTypeDef]],
        "NetworkDestinationPort": NotRequired[List[NumberFilterTypeDef]],
        "NetworkDestinationDomain": NotRequired[List[StringFilterTypeDef]],
        "ProcessName": NotRequired[List[StringFilterTypeDef]],
        "ProcessPath": NotRequired[List[StringFilterTypeDef]],
        "ProcessPid": NotRequired[List[NumberFilterTypeDef]],
        "ProcessParentPid": NotRequired[List[NumberFilterTypeDef]],
        "ProcessLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ProcessTerminatedAt": NotRequired[List[DateFilterTypeDef]],
        "ThreatIntelIndicatorType": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorValue": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorCategory": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "ThreatIntelIndicatorSource": NotRequired[List[StringFilterTypeDef]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ResourceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceId": NotRequired[List[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[List[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[List[StringFilterTypeDef]],
        "ResourceTags": NotRequired[List[MapFilterTypeDef]],
        "ResourceAwsEc2InstanceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceImageId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[List[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[List[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceAwsS3BucketOwnerId": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsS3BucketOwnerName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[List[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceAwsIamUserUserName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerImageId": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerImageName": NotRequired[List[StringFilterTypeDef]],
        "ResourceContainerLaunchedAt": NotRequired[List[DateFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[List[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[List[StringFilterTypeDef]],
        "VerificationState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[List[StringFilterTypeDef]],
        "RecordState": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "NoteText": NotRequired[List[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[List[StringFilterTypeDef]],
        "Keyword": NotRequired[List[KeywordFilterTypeDef]],
        "FindingProviderFieldsConfidence": NotRequired[List[NumberFilterTypeDef]],
        "FindingProviderFieldsCriticality": NotRequired[List[NumberFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[List[StringFilterTypeDef]],
        "FindingProviderFieldsTypes": NotRequired[List[StringFilterTypeDef]],
        "Sample": NotRequired[List[BooleanFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[List[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[List[StringFilterTypeDef]],
        "VulnerabilitiesExploitAvailable": NotRequired[List[StringFilterTypeDef]],
        "VulnerabilitiesFixAvailable": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersName": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersValue": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[List[StringFilterTypeDef]],
    },
)
AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "Id": NotRequired[Sequence[StringFilterTypeDef]],
        "GeneratorId": NotRequired[Sequence[StringFilterTypeDef]],
        "Region": NotRequired[Sequence[StringFilterTypeDef]],
        "Type": NotRequired[Sequence[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "CreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "SeverityProduct": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityNormalized": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "Confidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "Criticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "Title": NotRequired[Sequence[StringFilterTypeDef]],
        "Description": NotRequired[Sequence[StringFilterTypeDef]],
        "RecommendationText": NotRequired[Sequence[StringFilterTypeDef]],
        "SourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ProductFields": NotRequired[Sequence[MapFilterTypeDef]],
        "ProductName": NotRequired[Sequence[StringFilterTypeDef]],
        "CompanyName": NotRequired[Sequence[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[Sequence[MapFilterTypeDef]],
        "MalwareName": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareType": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwarePath": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareState": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDirection": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkProtocol": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourceIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourcePort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkSourceDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceMac": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDestinationIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationPort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkDestinationDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessName": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPath": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessParentPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ProcessTerminatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorType": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorValue": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorCategory": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorSource": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceAwsEc2InstanceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsS3BucketOwnerId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsS3BucketOwnerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsIamUserUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[Sequence[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "VerificationState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "RecordState": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteText": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[Sequence[StringFilterTypeDef]],
        "Keyword": NotRequired[Sequence[KeywordFilterTypeDef]],
        "FindingProviderFieldsConfidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsCriticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[
            Sequence[StringFilterTypeDef]
        ],
        "FindingProviderFieldsSeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsTypes": NotRequired[Sequence[StringFilterTypeDef]],
        "Sample": NotRequired[Sequence[BooleanFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesExploitAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesFixAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersName": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersValue": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
ThreatUnionTypeDef = Union[ThreatTypeDef, ThreatOutputTypeDef]

class GetFindingHistoryResponseTypeDef(TypedDict):
    Records: List[FindingHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

FindingProviderFieldsUnionTypeDef = Union[
    FindingProviderFieldsTypeDef, FindingProviderFieldsOutputTypeDef
]
SignalUnionTypeDef = Union[SignalTypeDef, SignalOutputTypeDef]

class GetInsightResultsResponseTypeDef(TypedDict):
    InsightResults: InsightResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

NetworkHeaderOutputTypeDef = TypedDict(
    "NetworkHeaderOutputTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsOutputTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsOutputTypeDef],
    },
)
NetworkPathComponentDetailsUnionTypeDef = Union[
    NetworkPathComponentDetailsTypeDef, NetworkPathComponentDetailsOutputTypeDef
]

class OccurrencesOutputTypeDef(TypedDict):
    LineRanges: NotRequired[List[RangeTypeDef]]
    OffsetRanges: NotRequired[List[RangeTypeDef]]
    Pages: NotRequired[List[PageTypeDef]]
    Records: NotRequired[List[RecordTypeDef]]
    Cells: NotRequired[List[CellTypeDef]]

class OccurrencesTypeDef(TypedDict):
    LineRanges: NotRequired[Sequence[RangeTypeDef]]
    OffsetRanges: NotRequired[Sequence[RangeTypeDef]]
    Pages: NotRequired[Sequence[PageTypeDef]]
    Records: NotRequired[Sequence[RecordTypeDef]]
    Cells: NotRequired[Sequence[CellTypeDef]]

class SecurityControlCustomParameterOutputTypeDef(TypedDict):
    SecurityControlId: NotRequired[str]
    Parameters: NotRequired[Dict[str, ParameterConfigurationOutputTypeDef]]

class SecurityControlTypeDef(TypedDict):
    SecurityControlId: str
    SecurityControlArn: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    SecurityControlStatus: ControlStatusType
    UpdateStatus: NotRequired[UpdateStatusType]
    Parameters: NotRequired[Dict[str, ParameterConfigurationOutputTypeDef]]
    LastUpdateReason: NotRequired[str]

class ParameterConfigurationTypeDef(TypedDict):
    ValueType: ParameterValueTypeType
    Value: NotRequired[ParameterValueUnionTypeDef]

class RuleGroupSourceStatefulRulesDetailsTypeDef(TypedDict):
    Action: NotRequired[str]
    Header: NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef]
    RuleOptions: NotRequired[Sequence[RuleGroupSourceStatefulRulesOptionsDetailsUnionTypeDef]]

class RuleGroupSourceStatelessRuleDefinitionOutputTypeDef(TypedDict):
    Actions: NotRequired[List[str]]
    MatchAttributes: NotRequired[RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef]

class RuleGroupSourceStatelessRuleMatchAttributesTypeDef(TypedDict):
    DestinationPorts: NotRequired[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
    ]
    Destinations: NotRequired[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]
    ]
    Protocols: NotRequired[Sequence[int]]
    SourcePorts: NotRequired[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]
    ]
    Sources: NotRequired[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]]
    TcpFlags: NotRequired[Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnionTypeDef]]

class RuleGroupVariablesTypeDef(TypedDict):
    IpSets: NotRequired[RuleGroupVariablesIpSetsDetailsUnionTypeDef]
    PortSets: NotRequired[RuleGroupVariablesPortSetsDetailsUnionTypeDef]

class ComplianceTypeDef(TypedDict):
    Status: NotRequired[ComplianceStatusType]
    RelatedRequirements: NotRequired[Sequence[str]]
    StatusReasons: NotRequired[Sequence[StatusReasonTypeDef]]
    SecurityControlId: NotRequired[str]
    AssociatedStandards: NotRequired[Sequence[AssociatedStandardTypeDef]]
    SecurityControlParameters: NotRequired[Sequence[SecurityControlParameterUnionTypeDef]]

class DescribeStandardsResponseTypeDef(TypedDict):
    Standards: List[StandardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDisableStandardsResponseTypeDef(TypedDict):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsResponseTypeDef(TypedDict):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnabledStandardsResponseTypeDef(TypedDict):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StatelessCustomActionDefinitionOutputTypeDef(TypedDict):
    PublishMetricAction: NotRequired[StatelessCustomPublishMetricActionOutputTypeDef]

StatelessCustomPublishMetricActionUnionTypeDef = Union[
    StatelessCustomPublishMetricActionTypeDef, StatelessCustomPublishMetricActionOutputTypeDef
]
AwsApiCallActionUnionTypeDef = Union[AwsApiCallActionTypeDef, AwsApiCallActionOutputTypeDef]

class PortProbeActionOutputTypeDef(TypedDict):
    PortProbeDetails: NotRequired[List[PortProbeDetailTypeDef]]
    Blocked: NotRequired[bool]

class PortProbeActionTypeDef(TypedDict):
    PortProbeDetails: NotRequired[Sequence[PortProbeDetailTypeDef]]
    Blocked: NotRequired[bool]

class SequenceOutputTypeDef(TypedDict):
    Uid: NotRequired[str]
    Actors: NotRequired[List[ActorTypeDef]]
    Endpoints: NotRequired[List[NetworkEndpointTypeDef]]
    Signals: NotRequired[List[SignalOutputTypeDef]]
    SequenceIndicators: NotRequired[List[IndicatorOutputTypeDef]]

AwsEc2RouteTableDetailsUnionTypeDef = Union[
    AwsEc2RouteTableDetailsTypeDef, AwsEc2RouteTableDetailsOutputTypeDef
]
AutomationRulesActionTypeDef = TypedDict(
    "AutomationRulesActionTypeDef",
    {
        "Type": NotRequired[Literal["FINDING_FIELDS_UPDATE"]],
        "FindingFieldsUpdate": NotRequired[AutomationRulesFindingFieldsUpdateUnionTypeDef],
    },
)
AwsAmazonMqBrokerDetailsUnionTypeDef = Union[
    AwsAmazonMqBrokerDetailsTypeDef, AwsAmazonMqBrokerDetailsOutputTypeDef
]
AwsApiGatewayStageDetailsUnionTypeDef = Union[
    AwsApiGatewayStageDetailsTypeDef, AwsApiGatewayStageDetailsOutputTypeDef
]
AwsApiGatewayRestApiDetailsUnionTypeDef = Union[
    AwsApiGatewayRestApiDetailsTypeDef, AwsApiGatewayRestApiDetailsOutputTypeDef
]
AwsAppSyncGraphQlApiDetailsUnionTypeDef = Union[
    AwsAppSyncGraphQlApiDetailsTypeDef, AwsAppSyncGraphQlApiDetailsOutputTypeDef
]

class AwsAthenaWorkGroupDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[str]
    Configuration: NotRequired[AwsAthenaWorkGroupConfigurationDetailsTypeDef]

class AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef(TypedDict):
    LaunchConfigurationName: NotRequired[str]
    LoadBalancerNames: NotRequired[List[str]]
    HealthCheckType: NotRequired[str]
    HealthCheckGracePeriod: NotRequired[int]
    CreatedTime: NotRequired[str]
    MixedInstancesPolicy: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef
    ]
    AvailabilityZones: NotRequired[
        List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
    ]
    LaunchTemplate: NotRequired[
        AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
    ]
    CapacityRebalance: NotRequired[bool]

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef(TypedDict):
    InstancesDistribution: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
    ]
    LaunchTemplate: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnionTypeDef
    ]

AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef = Union[
    AwsAutoScalingLaunchConfigurationDetailsTypeDef,
    AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef,
]

class AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef(TypedDict):
    BackupPlanName: NotRequired[str]
    AdvancedBackupSettings: NotRequired[
        List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef]
    ]
    BackupPlanRule: NotRequired[List[AwsBackupBackupPlanRuleDetailsOutputTypeDef]]

AwsBackupBackupPlanRuleDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanRuleDetailsTypeDef, AwsBackupBackupPlanRuleDetailsOutputTypeDef
]
AwsBackupBackupVaultDetailsUnionTypeDef = Union[
    AwsBackupBackupVaultDetailsTypeDef, AwsBackupBackupVaultDetailsOutputTypeDef
]
AwsCertificateManagerCertificateDetailsOutputTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsOutputTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[List[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)
AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef = Union[
    AwsCertificateManagerCertificateRenewalSummaryTypeDef,
    AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef,
]

class AwsCloudFrontDistributionOriginsOutputTypeDef(TypedDict):
    Items: NotRequired[List[AwsCloudFrontDistributionOriginItemOutputTypeDef]]

class AwsCloudFrontDistributionOriginGroupsOutputTypeDef(TypedDict):
    Items: NotRequired[List[AwsCloudFrontDistributionOriginGroupOutputTypeDef]]

AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupFailoverTypeDef,
    AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef,
]
AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef,
    AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef,
]

class AwsCodeBuildProjectDetailsTypeDef(TypedDict):
    EncryptionKey: NotRequired[str]
    Artifacts: NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]]
    Environment: NotRequired[AwsCodeBuildProjectEnvironmentUnionTypeDef]
    Name: NotRequired[str]
    Source: NotRequired[AwsCodeBuildProjectSourceTypeDef]
    ServiceRole: NotRequired[str]
    LogsConfig: NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef]
    VpcConfig: NotRequired[AwsCodeBuildProjectVpcConfigUnionTypeDef]
    SecondaryArtifacts: NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]]

AwsApiGatewayV2ApiDetailsUnionTypeDef = Union[
    AwsApiGatewayV2ApiDetailsTypeDef, AwsApiGatewayV2ApiDetailsOutputTypeDef
]
AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef = Union[
    AwsDynamoDbTableGlobalSecondaryIndexTypeDef, AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef
]
AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef = Union[
    AwsDynamoDbTableLocalSecondaryIndexTypeDef, AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef
]

class AwsDynamoDbTableDetailsOutputTypeDef(TypedDict):
    AttributeDefinitions: NotRequired[List[AwsDynamoDbTableAttributeDefinitionTypeDef]]
    BillingModeSummary: NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef]
    CreationDateTime: NotRequired[str]
    GlobalSecondaryIndexes: NotRequired[List[AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef]]
    GlobalTableVersion: NotRequired[str]
    ItemCount: NotRequired[int]
    KeySchema: NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]]
    LatestStreamArn: NotRequired[str]
    LatestStreamLabel: NotRequired[str]
    LocalSecondaryIndexes: NotRequired[List[AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef]]
    ProvisionedThroughput: NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef]
    Replicas: NotRequired[List[AwsDynamoDbTableReplicaOutputTypeDef]]
    RestoreSummary: NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef]
    SseDescription: NotRequired[AwsDynamoDbTableSseDescriptionTypeDef]
    StreamSpecification: NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef]
    TableId: NotRequired[str]
    TableName: NotRequired[str]
    TableSizeBytes: NotRequired[int]
    TableStatus: NotRequired[str]
    DeletionProtectionEnabled: NotRequired[bool]

AwsDynamoDbTableReplicaUnionTypeDef = Union[
    AwsDynamoDbTableReplicaTypeDef, AwsDynamoDbTableReplicaOutputTypeDef
]
AwsEc2ClientVpnEndpointDetailsUnionTypeDef = Union[
    AwsEc2ClientVpnEndpointDetailsTypeDef, AwsEc2ClientVpnEndpointDetailsOutputTypeDef
]

class AwsEc2LaunchTemplateDetailsOutputTypeDef(TypedDict):
    LaunchTemplateName: NotRequired[str]
    Id: NotRequired[str]
    LaunchTemplateData: NotRequired[AwsEc2LaunchTemplateDataDetailsOutputTypeDef]
    DefaultVersionNumber: NotRequired[int]
    LatestVersionNumber: NotRequired[int]

class AwsEc2LaunchTemplateDataDetailsTypeDef(TypedDict):
    BlockDeviceMappingSet: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
    ]
    CapacityReservationSpecification: NotRequired[
        AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
    ]
    CpuOptions: NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef]
    CreditSpecification: NotRequired[AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef]
    DisableApiStop: NotRequired[bool]
    DisableApiTermination: NotRequired[bool]
    EbsOptimized: NotRequired[bool]
    ElasticGpuSpecificationSet: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
    ]
    ElasticInferenceAcceleratorSet: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
    ]
    EnclaveOptions: NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef]
    HibernationOptions: NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef]
    IamInstanceProfile: NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef]
    ImageId: NotRequired[str]
    InstanceInitiatedShutdownBehavior: NotRequired[str]
    InstanceMarketOptions: NotRequired[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef]
    InstanceRequirements: NotRequired[
        AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnionTypeDef
    ]
    InstanceType: NotRequired[str]
    KernelId: NotRequired[str]
    KeyName: NotRequired[str]
    LicenseSet: NotRequired[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]]
    MaintenanceOptions: NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef]
    MetadataOptions: NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef]
    Monitoring: NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef]
    NetworkInterfaceSet: NotRequired[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnionTypeDef]
    ]
    Placement: NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef]
    PrivateDnsNameOptions: NotRequired[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef]
    RamDiskId: NotRequired[str]
    SecurityGroupIdSet: NotRequired[Sequence[str]]
    SecurityGroupSet: NotRequired[Sequence[str]]
    UserData: NotRequired[str]

AwsEc2NetworkAclDetailsUnionTypeDef = Union[
    AwsEc2NetworkAclDetailsTypeDef, AwsEc2NetworkAclDetailsOutputTypeDef
]

class AwsEc2SecurityGroupDetailsTypeDef(TypedDict):
    GroupName: NotRequired[str]
    GroupId: NotRequired[str]
    OwnerId: NotRequired[str]
    VpcId: NotRequired[str]
    IpPermissions: NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionUnionTypeDef]]
    IpPermissionsEgress: NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]]

class AwsEc2VpcPeeringConnectionDetailsTypeDef(TypedDict):
    AccepterVpcInfo: NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef]
    ExpirationTime: NotRequired[str]
    RequesterVpcInfo: NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnionTypeDef]
    Status: NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef]
    VpcPeeringConnectionId: NotRequired[str]

AwsEc2VpnConnectionOptionsDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionOptionsDetailsTypeDef, AwsEc2VpnConnectionOptionsDetailsOutputTypeDef
]

class AwsEcsClusterDetailsOutputTypeDef(TypedDict):
    ClusterArn: NotRequired[str]
    ActiveServicesCount: NotRequired[int]
    CapacityProviders: NotRequired[List[str]]
    ClusterSettings: NotRequired[List[AwsEcsClusterClusterSettingsDetailsTypeDef]]
    Configuration: NotRequired[AwsEcsClusterConfigurationDetailsTypeDef]
    DefaultCapacityProviderStrategy: NotRequired[
        List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
    ]
    ClusterName: NotRequired[str]
    RegisteredContainerInstancesCount: NotRequired[int]
    RunningTasksCount: NotRequired[int]
    Status: NotRequired[str]

class AwsEcsClusterDetailsTypeDef(TypedDict):
    ClusterArn: NotRequired[str]
    ActiveServicesCount: NotRequired[int]
    CapacityProviders: NotRequired[Sequence[str]]
    ClusterSettings: NotRequired[Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef]]
    Configuration: NotRequired[AwsEcsClusterConfigurationDetailsTypeDef]
    DefaultCapacityProviderStrategy: NotRequired[
        Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
    ]
    ClusterName: NotRequired[str]
    RegisteredContainerInstancesCount: NotRequired[int]
    RunningTasksCount: NotRequired[int]
    Status: NotRequired[str]

class AwsEcsTaskDetailsTypeDef(TypedDict):
    ClusterArn: NotRequired[str]
    TaskDefinitionArn: NotRequired[str]
    Version: NotRequired[str]
    CreatedAt: NotRequired[str]
    StartedAt: NotRequired[str]
    StartedBy: NotRequired[str]
    Group: NotRequired[str]
    Volumes: NotRequired[Sequence[AwsEcsTaskVolumeDetailsTypeDef]]
    Containers: NotRequired[Sequence[AwsEcsContainerDetailsUnionTypeDef]]

AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef = Union[
    AwsEcsServiceNetworkConfigurationDetailsTypeDef,
    AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef,
]
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef,
]

class AwsEcsTaskDefinitionDetailsOutputTypeDef(TypedDict):
    ContainerDefinitions: NotRequired[
        List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef]
    ]
    Cpu: NotRequired[str]
    ExecutionRoleArn: NotRequired[str]
    Family: NotRequired[str]
    InferenceAccelerators: NotRequired[
        List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
    ]
    IpcMode: NotRequired[str]
    Memory: NotRequired[str]
    NetworkMode: NotRequired[str]
    PidMode: NotRequired[str]
    PlacementConstraints: NotRequired[List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]]
    ProxyConfiguration: NotRequired[AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef]
    RequiresCompatibilities: NotRequired[List[str]]
    TaskRoleArn: NotRequired[str]
    Volumes: NotRequired[List[AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef]]
    Status: NotRequired[str]

AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionVolumesDetailsTypeDef, AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef
]
AwsEfsAccessPointDetailsUnionTypeDef = Union[
    AwsEfsAccessPointDetailsTypeDef, AwsEfsAccessPointDetailsOutputTypeDef
]
AwsEksClusterLoggingDetailsUnionTypeDef = Union[
    AwsEksClusterLoggingDetailsTypeDef, AwsEksClusterLoggingDetailsOutputTypeDef
]
AwsElasticsearchDomainDetailsUnionTypeDef = Union[
    AwsElasticsearchDomainDetailsTypeDef, AwsElasticsearchDomainDetailsOutputTypeDef
]

class AwsElbLoadBalancerDetailsTypeDef(TypedDict):
    AvailabilityZones: NotRequired[Sequence[str]]
    BackendServerDescriptions: NotRequired[
        Sequence[AwsElbLoadBalancerBackendServerDescriptionUnionTypeDef]
    ]
    CanonicalHostedZoneName: NotRequired[str]
    CanonicalHostedZoneNameID: NotRequired[str]
    CreatedTime: NotRequired[str]
    DnsName: NotRequired[str]
    HealthCheck: NotRequired[AwsElbLoadBalancerHealthCheckTypeDef]
    Instances: NotRequired[Sequence[AwsElbLoadBalancerInstanceTypeDef]]
    ListenerDescriptions: NotRequired[Sequence[AwsElbLoadBalancerListenerDescriptionUnionTypeDef]]
    LoadBalancerAttributes: NotRequired[AwsElbLoadBalancerAttributesUnionTypeDef]
    LoadBalancerName: NotRequired[str]
    Policies: NotRequired[AwsElbLoadBalancerPoliciesUnionTypeDef]
    Scheme: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]
    SourceSecurityGroup: NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef]
    Subnets: NotRequired[Sequence[str]]
    VpcId: NotRequired[str]

class AwsEventsEndpointDetailsOutputTypeDef(TypedDict):
    Arn: NotRequired[str]
    Description: NotRequired[str]
    EndpointId: NotRequired[str]
    EndpointUrl: NotRequired[str]
    EventBuses: NotRequired[List[AwsEventsEndpointEventBusesDetailsTypeDef]]
    Name: NotRequired[str]
    ReplicationConfig: NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef]
    RoleArn: NotRequired[str]
    RoutingConfig: NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class AwsEventsEndpointDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    Description: NotRequired[str]
    EndpointId: NotRequired[str]
    EndpointUrl: NotRequired[str]
    EventBuses: NotRequired[Sequence[AwsEventsEndpointEventBusesDetailsTypeDef]]
    Name: NotRequired[str]
    ReplicationConfig: NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef]
    RoleArn: NotRequired[str]
    RoutingConfig: NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class AwsGuardDutyDetectorDataSourcesDetailsTypeDef(TypedDict):
    CloudTrail: NotRequired[AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef]
    DnsLogs: NotRequired[AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef]
    FlowLogs: NotRequired[AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef]
    Kubernetes: NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef]
    MalwareProtection: NotRequired[AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef]
    S3Logs: NotRequired[AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef]

class AwsIamRoleDetailsTypeDef(TypedDict):
    AssumeRolePolicyDocument: NotRequired[str]
    AttachedManagedPolicies: NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]]
    CreateDate: NotRequired[str]
    InstanceProfileList: NotRequired[Sequence[AwsIamInstanceProfileUnionTypeDef]]
    PermissionsBoundary: NotRequired[AwsIamPermissionsBoundaryTypeDef]
    RoleId: NotRequired[str]
    RoleName: NotRequired[str]
    RolePolicyList: NotRequired[Sequence[AwsIamRolePolicyTypeDef]]
    MaxSessionDuration: NotRequired[int]
    Path: NotRequired[str]

class AwsLambdaFunctionDetailsTypeDef(TypedDict):
    Code: NotRequired[AwsLambdaFunctionCodeTypeDef]
    CodeSha256: NotRequired[str]
    DeadLetterConfig: NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef]
    Environment: NotRequired[AwsLambdaFunctionEnvironmentUnionTypeDef]
    FunctionName: NotRequired[str]
    Handler: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    LastModified: NotRequired[str]
    Layers: NotRequired[Sequence[AwsLambdaFunctionLayerTypeDef]]
    MasterArn: NotRequired[str]
    MemorySize: NotRequired[int]
    RevisionId: NotRequired[str]
    Role: NotRequired[str]
    Runtime: NotRequired[str]
    Timeout: NotRequired[int]
    TracingConfig: NotRequired[AwsLambdaFunctionTracingConfigTypeDef]
    VpcConfig: NotRequired[AwsLambdaFunctionVpcConfigUnionTypeDef]
    Version: NotRequired[str]
    Architectures: NotRequired[Sequence[str]]
    PackageType: NotRequired[str]

class AwsMskClusterClusterInfoDetailsOutputTypeDef(TypedDict):
    EncryptionInfo: NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef]
    CurrentVersion: NotRequired[str]
    NumberOfBrokerNodes: NotRequired[int]
    ClusterName: NotRequired[str]
    ClientAuthentication: NotRequired[
        AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef
    ]
    EnhancedMonitoring: NotRequired[str]

AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef,
    AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef,
]
AwsOpenSearchServiceDomainDetailsUnionTypeDef = Union[
    AwsOpenSearchServiceDomainDetailsTypeDef, AwsOpenSearchServiceDomainDetailsOutputTypeDef
]
AwsRdsDbClusterSnapshotDetailsUnionTypeDef = Union[
    AwsRdsDbClusterSnapshotDetailsTypeDef, AwsRdsDbClusterSnapshotDetailsOutputTypeDef
]

class AwsRdsDbInstanceDetailsOutputTypeDef(TypedDict):
    AssociatedRoles: NotRequired[List[AwsRdsDbInstanceAssociatedRoleTypeDef]]
    CACertificateIdentifier: NotRequired[str]
    DBClusterIdentifier: NotRequired[str]
    DBInstanceIdentifier: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    DbInstancePort: NotRequired[int]
    DbiResourceId: NotRequired[str]
    DBName: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    Endpoint: NotRequired[AwsRdsDbInstanceEndpointTypeDef]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    InstanceCreateTime: NotRequired[str]
    KmsKeyId: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    StorageEncrypted: NotRequired[bool]
    TdeCredentialArn: NotRequired[str]
    VpcSecurityGroups: NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]]
    MultiAz: NotRequired[bool]
    EnhancedMonitoringResourceArn: NotRequired[str]
    DbInstanceStatus: NotRequired[str]
    MasterUsername: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    PreferredBackupWindow: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    DbSecurityGroups: NotRequired[List[str]]
    DbParameterGroups: NotRequired[List[AwsRdsDbParameterGroupTypeDef]]
    AvailabilityZone: NotRequired[str]
    DbSubnetGroup: NotRequired[AwsRdsDbSubnetGroupOutputTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[AwsRdsDbPendingModifiedValuesOutputTypeDef]
    LatestRestorableTime: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    ReadReplicaSourceDBInstanceIdentifier: NotRequired[str]
    ReadReplicaDBInstanceIdentifiers: NotRequired[List[str]]
    ReadReplicaDBClusterIdentifiers: NotRequired[List[str]]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupMemberships: NotRequired[List[AwsRdsDbOptionGroupMembershipTypeDef]]
    CharacterSetName: NotRequired[str]
    SecondaryAvailabilityZone: NotRequired[str]
    StatusInfos: NotRequired[List[AwsRdsDbStatusInfoTypeDef]]
    StorageType: NotRequired[str]
    DomainMemberships: NotRequired[List[AwsRdsDbDomainMembershipTypeDef]]
    CopyTagsToSnapshot: NotRequired[bool]
    MonitoringInterval: NotRequired[int]
    MonitoringRoleArn: NotRequired[str]
    PromotionTier: NotRequired[int]
    Timezone: NotRequired[str]
    PerformanceInsightsEnabled: NotRequired[bool]
    PerformanceInsightsKmsKeyId: NotRequired[str]
    PerformanceInsightsRetentionPeriod: NotRequired[int]
    EnabledCloudWatchLogsExports: NotRequired[List[str]]
    ProcessorFeatures: NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]]
    ListenerEndpoint: NotRequired[AwsRdsDbInstanceEndpointTypeDef]
    MaxAllocatedStorage: NotRequired[int]

AwsRdsDbSubnetGroupUnionTypeDef = Union[
    AwsRdsDbSubnetGroupTypeDef, AwsRdsDbSubnetGroupOutputTypeDef
]
AwsRdsDbPendingModifiedValuesUnionTypeDef = Union[
    AwsRdsDbPendingModifiedValuesTypeDef, AwsRdsDbPendingModifiedValuesOutputTypeDef
]

class AwsRedshiftClusterDetailsTypeDef(TypedDict):
    AllowVersionUpgrade: NotRequired[bool]
    AutomatedSnapshotRetentionPeriod: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    ClusterAvailabilityStatus: NotRequired[str]
    ClusterCreateTime: NotRequired[str]
    ClusterIdentifier: NotRequired[str]
    ClusterNodes: NotRequired[Sequence[AwsRedshiftClusterClusterNodeTypeDef]]
    ClusterParameterGroups: NotRequired[
        Sequence[AwsRedshiftClusterClusterParameterGroupUnionTypeDef]
    ]
    ClusterPublicKey: NotRequired[str]
    ClusterRevisionNumber: NotRequired[str]
    ClusterSecurityGroups: NotRequired[Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef]]
    ClusterSnapshotCopyStatus: NotRequired[AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef]
    ClusterStatus: NotRequired[str]
    ClusterSubnetGroupName: NotRequired[str]
    ClusterVersion: NotRequired[str]
    DBName: NotRequired[str]
    DeferredMaintenanceWindows: NotRequired[
        Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
    ]
    ElasticIpStatus: NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef]
    ElasticResizeNumberOfNodeOptions: NotRequired[str]
    Encrypted: NotRequired[bool]
    Endpoint: NotRequired[AwsRedshiftClusterEndpointTypeDef]
    EnhancedVpcRouting: NotRequired[bool]
    ExpectedNextSnapshotScheduleTime: NotRequired[str]
    ExpectedNextSnapshotScheduleTimeStatus: NotRequired[str]
    HsmStatus: NotRequired[AwsRedshiftClusterHsmStatusTypeDef]
    IamRoles: NotRequired[Sequence[AwsRedshiftClusterIamRoleTypeDef]]
    KmsKeyId: NotRequired[str]
    MaintenanceTrackName: NotRequired[str]
    ManualSnapshotRetentionPeriod: NotRequired[int]
    MasterUsername: NotRequired[str]
    NextMaintenanceWindowStartTime: NotRequired[str]
    NodeType: NotRequired[str]
    NumberOfNodes: NotRequired[int]
    PendingActions: NotRequired[Sequence[str]]
    PendingModifiedValues: NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    ResizeInfo: NotRequired[AwsRedshiftClusterResizeInfoTypeDef]
    RestoreStatus: NotRequired[AwsRedshiftClusterRestoreStatusTypeDef]
    SnapshotScheduleIdentifier: NotRequired[str]
    SnapshotScheduleState: NotRequired[str]
    VpcId: NotRequired[str]
    VpcSecurityGroups: NotRequired[Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef]]
    LoggingStatus: NotRequired[AwsRedshiftClusterLoggingStatusTypeDef]

AwsRoute53HostedZoneDetailsUnionTypeDef = Union[
    AwsRoute53HostedZoneDetailsTypeDef, AwsRoute53HostedZoneDetailsOutputTypeDef
]

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef(TypedDict):
    Predicate: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef
    ]

AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef,
]
AwsS3BucketNotificationConfigurationDetailOutputTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailOutputTypeDef",
    {
        "Events": NotRequired[List[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterOutputTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class AwsS3BucketNotificationConfigurationFilterTypeDef(TypedDict):
    S3KeyFilter: NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterUnionTypeDef]

AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef = Union[
    AwsS3BucketServerSideEncryptionConfigurationTypeDef,
    AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef,
]
AwsS3BucketWebsiteConfigurationUnionTypeDef = Union[
    AwsS3BucketWebsiteConfigurationTypeDef, AwsS3BucketWebsiteConfigurationOutputTypeDef
]
AwsStepFunctionStateMachineDetailsOutputTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsOutputTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef = Union[
    AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef,
    AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef,
]
AwsWafRegionalRuleGroupDetailsUnionTypeDef = Union[
    AwsWafRegionalRuleGroupDetailsTypeDef, AwsWafRegionalRuleGroupDetailsOutputTypeDef
]
AwsWafRegionalWebAclDetailsUnionTypeDef = Union[
    AwsWafRegionalWebAclDetailsTypeDef, AwsWafRegionalWebAclDetailsOutputTypeDef
]
AwsWafRuleGroupDetailsUnionTypeDef = Union[
    AwsWafRuleGroupDetailsTypeDef, AwsWafRuleGroupDetailsOutputTypeDef
]

class AwsWafWebAclDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    DefaultAction: NotRequired[str]
    Rules: NotRequired[Sequence[AwsWafWebAclRuleUnionTypeDef]]
    WebAclId: NotRequired[str]

class AwsWafv2ActionAllowDetailsTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef]

class AwsWafv2RulesActionCaptchaDetailsTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef]

class AwsWafv2RulesActionCountDetailsTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[AwsWafv2CustomRequestHandlingDetailsUnionTypeDef]

class AwsWafv2RulesActionDetailsOutputTypeDef(TypedDict):
    Allow: NotRequired[AwsWafv2ActionAllowDetailsOutputTypeDef]
    Block: NotRequired[AwsWafv2ActionBlockDetailsOutputTypeDef]
    Captcha: NotRequired[AwsWafv2RulesActionCaptchaDetailsOutputTypeDef]
    Count: NotRequired[AwsWafv2RulesActionCountDetailsOutputTypeDef]

class AwsWafv2WebAclActionDetailsOutputTypeDef(TypedDict):
    Allow: NotRequired[AwsWafv2ActionAllowDetailsOutputTypeDef]
    Block: NotRequired[AwsWafv2ActionBlockDetailsOutputTypeDef]

class AwsWafv2ActionBlockDetailsTypeDef(TypedDict):
    CustomResponse: NotRequired[AwsWafv2CustomResponseDetailsUnionTypeDef]

class VulnerabilityTypeDef(TypedDict):
    Id: str
    VulnerablePackages: NotRequired[Sequence[SoftwarePackageTypeDef]]
    Cvss: NotRequired[Sequence[CvssUnionTypeDef]]
    RelatedVulnerabilities: NotRequired[Sequence[str]]
    Vendor: NotRequired[VulnerabilityVendorTypeDef]
    ReferenceUrls: NotRequired[Sequence[str]]
    FixAvailable: NotRequired[VulnerabilityFixAvailableType]
    EpssScore: NotRequired[float]
    ExploitAvailable: NotRequired[VulnerabilityExploitAvailableType]
    LastKnownExploitAt: NotRequired[str]
    CodeVulnerabilities: NotRequired[Sequence[VulnerabilityCodeVulnerabilitiesUnionTypeDef]]

class SecurityControlDefinitionTypeDef(TypedDict):
    SecurityControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    CurrentRegionAvailability: RegionAvailabilityStatusType
    CustomizableProperties: NotRequired[List[Literal["Parameters"]]]
    ParameterDefinitions: NotRequired[Dict[str, ParameterDefinitionTypeDef]]

class BatchGetConfigurationPolicyAssociationsResponseTypeDef(TypedDict):
    ConfigurationPolicyAssociations: List[ConfigurationPolicyAssociationSummaryTypeDef]
    UnprocessedConfigurationPolicyAssociations: List[
        UnprocessedConfigurationPolicyAssociationTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef

class AutomationRulesConfigTypeDef(TypedDict):
    RuleArn: NotRequired[str]
    RuleStatus: NotRequired[RuleStatusType]
    RuleOrder: NotRequired[int]
    RuleName: NotRequired[str]
    Description: NotRequired[str]
    IsTerminal: NotRequired[bool]
    Criteria: NotRequired[AutomationRulesFindingFiltersOutputTypeDef]
    Actions: NotRequired[List[AutomationRulesActionOutputTypeDef]]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    CreatedBy: NotRequired[str]

AutomationRulesFindingFiltersUnionTypeDef = Union[
    AutomationRulesFindingFiltersTypeDef, AutomationRulesFindingFiltersOutputTypeDef
]

class InsightTypeDef(TypedDict):
    InsightArn: str
    Name: str
    Filters: AwsSecurityFindingFiltersOutputTypeDef
    GroupByAttribute: str

AwsSecurityFindingFiltersUnionTypeDef = Union[
    AwsSecurityFindingFiltersTypeDef, AwsSecurityFindingFiltersOutputTypeDef
]

class SequenceTypeDef(TypedDict):
    Uid: NotRequired[str]
    Actors: NotRequired[Sequence[ActorTypeDef]]
    Endpoints: NotRequired[Sequence[NetworkEndpointTypeDef]]
    Signals: NotRequired[Sequence[SignalUnionTypeDef]]
    SequenceIndicators: NotRequired[Sequence[IndicatorUnionTypeDef]]

class NetworkPathComponentOutputTypeDef(TypedDict):
    ComponentId: NotRequired[str]
    ComponentType: NotRequired[str]
    Egress: NotRequired[NetworkHeaderOutputTypeDef]
    Ingress: NotRequired[NetworkHeaderOutputTypeDef]

NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsUnionTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsUnionTypeDef],
    },
)

class CustomDataIdentifiersDetectionsOutputTypeDef(TypedDict):
    Count: NotRequired[int]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Occurrences: NotRequired[OccurrencesOutputTypeDef]

SensitiveDataDetectionsOutputTypeDef = TypedDict(
    "SensitiveDataDetectionsOutputTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesOutputTypeDef],
    },
)
OccurrencesUnionTypeDef = Union[OccurrencesTypeDef, OccurrencesOutputTypeDef]

class SecurityControlsConfigurationOutputTypeDef(TypedDict):
    EnabledSecurityControlIdentifiers: NotRequired[List[str]]
    DisabledSecurityControlIdentifiers: NotRequired[List[str]]
    SecurityControlCustomParameters: NotRequired[List[SecurityControlCustomParameterOutputTypeDef]]

class BatchGetSecurityControlsResponseTypeDef(TypedDict):
    SecurityControls: List[SecurityControlTypeDef]
    UnprocessedIds: List[UnprocessedSecurityControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ParameterConfigurationUnionTypeDef = Union[
    ParameterConfigurationTypeDef, ParameterConfigurationOutputTypeDef
]

class SecurityControlCustomParameterTypeDef(TypedDict):
    SecurityControlId: NotRequired[str]
    Parameters: NotRequired[Mapping[str, ParameterConfigurationTypeDef]]

RuleGroupSourceStatefulRulesDetailsUnionTypeDef = Union[
    RuleGroupSourceStatefulRulesDetailsTypeDef, RuleGroupSourceStatefulRulesDetailsOutputTypeDef
]

class RuleGroupSourceStatelessRulesDetailsOutputTypeDef(TypedDict):
    Priority: NotRequired[int]
    RuleDefinition: NotRequired[RuleGroupSourceStatelessRuleDefinitionOutputTypeDef]

RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleMatchAttributesTypeDef,
    RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef,
]
RuleGroupVariablesUnionTypeDef = Union[RuleGroupVariablesTypeDef, RuleGroupVariablesOutputTypeDef]
ComplianceUnionTypeDef = Union[ComplianceTypeDef, ComplianceOutputTypeDef]

class FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef(TypedDict):
    ActionDefinition: NotRequired[StatelessCustomActionDefinitionOutputTypeDef]
    ActionName: NotRequired[str]

class RuleGroupSourceCustomActionsDetailsOutputTypeDef(TypedDict):
    ActionDefinition: NotRequired[StatelessCustomActionDefinitionOutputTypeDef]
    ActionName: NotRequired[str]

class StatelessCustomActionDefinitionTypeDef(TypedDict):
    PublishMetricAction: NotRequired[StatelessCustomPublishMetricActionUnionTypeDef]

class ActionOutputTypeDef(TypedDict):
    ActionType: NotRequired[str]
    NetworkConnectionAction: NotRequired[NetworkConnectionActionTypeDef]
    AwsApiCallAction: NotRequired[AwsApiCallActionOutputTypeDef]
    DnsRequestAction: NotRequired[DnsRequestActionTypeDef]
    PortProbeAction: NotRequired[PortProbeActionOutputTypeDef]

PortProbeActionUnionTypeDef = Union[PortProbeActionTypeDef, PortProbeActionOutputTypeDef]
DetectionOutputTypeDef = TypedDict(
    "DetectionOutputTypeDef",
    {
        "Sequence": NotRequired[SequenceOutputTypeDef],
    },
)
AutomationRulesActionUnionTypeDef = Union[
    AutomationRulesActionTypeDef, AutomationRulesActionOutputTypeDef
]
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef,
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef,
]

class AwsBackupBackupPlanDetailsOutputTypeDef(TypedDict):
    BackupPlan: NotRequired[AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef]
    BackupPlanArn: NotRequired[str]
    BackupPlanId: NotRequired[str]
    VersionId: NotRequired[str]

class AwsBackupBackupPlanBackupPlanDetailsTypeDef(TypedDict):
    BackupPlanName: NotRequired[str]
    AdvancedBackupSettings: NotRequired[
        Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnionTypeDef]
    ]
    BackupPlanRule: NotRequired[Sequence[AwsBackupBackupPlanRuleDetailsUnionTypeDef]]

AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            Sequence[AwsCertificateManagerCertificateDomainValidationOptionUnionTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[Sequence[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[AwsCertificateManagerCertificateRenewalSummaryUnionTypeDef],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "Type": NotRequired[str],
    },
)

class AwsCloudFrontDistributionDetailsOutputTypeDef(TypedDict):
    CacheBehaviors: NotRequired[AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef]
    DefaultCacheBehavior: NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef]
    DefaultRootObject: NotRequired[str]
    DomainName: NotRequired[str]
    ETag: NotRequired[str]
    LastModifiedTime: NotRequired[str]
    Logging: NotRequired[AwsCloudFrontDistributionLoggingTypeDef]
    Origins: NotRequired[AwsCloudFrontDistributionOriginsOutputTypeDef]
    OriginGroups: NotRequired[AwsCloudFrontDistributionOriginGroupsOutputTypeDef]
    ViewerCertificate: NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef]
    Status: NotRequired[str]
    WebAclId: NotRequired[str]

class AwsCloudFrontDistributionOriginGroupTypeDef(TypedDict):
    FailoverCriteria: NotRequired[AwsCloudFrontDistributionOriginGroupFailoverUnionTypeDef]

class AwsCloudFrontDistributionOriginItemTypeDef(TypedDict):
    DomainName: NotRequired[str]
    Id: NotRequired[str]
    OriginPath: NotRequired[str]
    S3OriginConfig: NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef]
    CustomOriginConfig: NotRequired[AwsCloudFrontDistributionOriginCustomOriginConfigUnionTypeDef]

AwsCodeBuildProjectDetailsUnionTypeDef = Union[
    AwsCodeBuildProjectDetailsTypeDef, AwsCodeBuildProjectDetailsOutputTypeDef
]

class AwsDynamoDbTableDetailsTypeDef(TypedDict):
    AttributeDefinitions: NotRequired[Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef]]
    BillingModeSummary: NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef]
    CreationDateTime: NotRequired[str]
    GlobalSecondaryIndexes: NotRequired[Sequence[AwsDynamoDbTableGlobalSecondaryIndexUnionTypeDef]]
    GlobalTableVersion: NotRequired[str]
    ItemCount: NotRequired[int]
    KeySchema: NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]]
    LatestStreamArn: NotRequired[str]
    LatestStreamLabel: NotRequired[str]
    LocalSecondaryIndexes: NotRequired[Sequence[AwsDynamoDbTableLocalSecondaryIndexUnionTypeDef]]
    ProvisionedThroughput: NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef]
    Replicas: NotRequired[Sequence[AwsDynamoDbTableReplicaUnionTypeDef]]
    RestoreSummary: NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef]
    SseDescription: NotRequired[AwsDynamoDbTableSseDescriptionTypeDef]
    StreamSpecification: NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef]
    TableId: NotRequired[str]
    TableName: NotRequired[str]
    TableSizeBytes: NotRequired[int]
    TableStatus: NotRequired[str]
    DeletionProtectionEnabled: NotRequired[bool]

AwsEc2LaunchTemplateDataDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDataDetailsTypeDef, AwsEc2LaunchTemplateDataDetailsOutputTypeDef
]
AwsEc2SecurityGroupDetailsUnionTypeDef = Union[
    AwsEc2SecurityGroupDetailsTypeDef, AwsEc2SecurityGroupDetailsOutputTypeDef
]
AwsEc2VpcPeeringConnectionDetailsUnionTypeDef = Union[
    AwsEc2VpcPeeringConnectionDetailsTypeDef, AwsEc2VpcPeeringConnectionDetailsOutputTypeDef
]
AwsEc2VpnConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsUnionTypeDef],
        "Routes": NotRequired[Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)
AwsEcsClusterDetailsUnionTypeDef = Union[
    AwsEcsClusterDetailsTypeDef, AwsEcsClusterDetailsOutputTypeDef
]
AwsEcsTaskDetailsUnionTypeDef = Union[AwsEcsTaskDetailsTypeDef, AwsEcsTaskDetailsOutputTypeDef]
AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[AwsEcsServiceNetworkConfigurationDetailsUnionTypeDef],
        "PlacementConstraints": NotRequired[
            Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef]
        ],
        "PlacementStrategies": NotRequired[
            Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef]
        ],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)

class AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef(TypedDict):
    Command: NotRequired[Sequence[str]]
    Cpu: NotRequired[int]
    DependsOn: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]
    ]
    DisableNetworking: NotRequired[bool]
    DnsSearchDomains: NotRequired[Sequence[str]]
    DnsServers: NotRequired[Sequence[str]]
    DockerLabels: NotRequired[Mapping[str, str]]
    DockerSecurityOptions: NotRequired[Sequence[str]]
    EntryPoint: NotRequired[Sequence[str]]
    Environment: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
    ]
    EnvironmentFiles: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
    ]
    Essential: NotRequired[bool]
    ExtraHosts: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]
    ]
    FirelensConfiguration: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnionTypeDef
    ]
    HealthCheck: NotRequired[AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnionTypeDef]
    Hostname: NotRequired[str]
    Image: NotRequired[str]
    Interactive: NotRequired[bool]
    Links: NotRequired[Sequence[str]]
    LinuxParameters: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnionTypeDef
    ]
    LogConfiguration: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnionTypeDef
    ]
    Memory: NotRequired[int]
    MemoryReservation: NotRequired[int]
    MountPoints: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
    ]
    Name: NotRequired[str]
    PortMappings: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
    ]
    Privileged: NotRequired[bool]
    PseudoTerminal: NotRequired[bool]
    ReadonlyRootFilesystem: NotRequired[bool]
    RepositoryCredentials: NotRequired[
        AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
    ]
    ResourceRequirements: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
    ]
    Secrets: NotRequired[Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]]
    StartTimeout: NotRequired[int]
    StopTimeout: NotRequired[int]
    SystemControls: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
    ]
    Ulimits: NotRequired[Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]]
    User: NotRequired[str]
    VolumesFrom: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
    ]
    WorkingDirectory: NotRequired[str]

class AwsEksClusterDetailsTypeDef(TypedDict):
    Arn: NotRequired[str]
    CertificateAuthorityData: NotRequired[str]
    ClusterStatus: NotRequired[str]
    Endpoint: NotRequired[str]
    Name: NotRequired[str]
    ResourcesVpcConfig: NotRequired[AwsEksClusterResourcesVpcConfigDetailsUnionTypeDef]
    RoleArn: NotRequired[str]
    Version: NotRequired[str]
    Logging: NotRequired[AwsEksClusterLoggingDetailsUnionTypeDef]

AwsElbLoadBalancerDetailsUnionTypeDef = Union[
    AwsElbLoadBalancerDetailsTypeDef, AwsElbLoadBalancerDetailsOutputTypeDef
]
AwsEventsEndpointDetailsUnionTypeDef = Union[
    AwsEventsEndpointDetailsTypeDef, AwsEventsEndpointDetailsOutputTypeDef
]

class AwsGuardDutyDetectorDetailsOutputTypeDef(TypedDict):
    DataSources: NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef]
    Features: NotRequired[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]]
    FindingPublishingFrequency: NotRequired[str]
    ServiceRole: NotRequired[str]
    Status: NotRequired[str]

class AwsGuardDutyDetectorDetailsTypeDef(TypedDict):
    DataSources: NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef]
    Features: NotRequired[Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef]]
    FindingPublishingFrequency: NotRequired[str]
    ServiceRole: NotRequired[str]
    Status: NotRequired[str]

AwsIamRoleDetailsUnionTypeDef = Union[AwsIamRoleDetailsTypeDef, AwsIamRoleDetailsOutputTypeDef]
AwsLambdaFunctionDetailsUnionTypeDef = Union[
    AwsLambdaFunctionDetailsTypeDef, AwsLambdaFunctionDetailsOutputTypeDef
]

class AwsMskClusterDetailsOutputTypeDef(TypedDict):
    ClusterInfo: NotRequired[AwsMskClusterClusterInfoDetailsOutputTypeDef]

class AwsMskClusterClusterInfoDetailsTypeDef(TypedDict):
    EncryptionInfo: NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef]
    CurrentVersion: NotRequired[str]
    NumberOfBrokerNodes: NotRequired[int]
    ClusterName: NotRequired[str]
    ClientAuthentication: NotRequired[
        AwsMskClusterClusterInfoClientAuthenticationDetailsUnionTypeDef
    ]
    EnhancedMonitoring: NotRequired[str]

class AwsRdsDbInstanceDetailsTypeDef(TypedDict):
    AssociatedRoles: NotRequired[Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef]]
    CACertificateIdentifier: NotRequired[str]
    DBClusterIdentifier: NotRequired[str]
    DBInstanceIdentifier: NotRequired[str]
    DBInstanceClass: NotRequired[str]
    DbInstancePort: NotRequired[int]
    DbiResourceId: NotRequired[str]
    DBName: NotRequired[str]
    DeletionProtection: NotRequired[bool]
    Endpoint: NotRequired[AwsRdsDbInstanceEndpointTypeDef]
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    IAMDatabaseAuthenticationEnabled: NotRequired[bool]
    InstanceCreateTime: NotRequired[str]
    KmsKeyId: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    StorageEncrypted: NotRequired[bool]
    TdeCredentialArn: NotRequired[str]
    VpcSecurityGroups: NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]]
    MultiAz: NotRequired[bool]
    EnhancedMonitoringResourceArn: NotRequired[str]
    DbInstanceStatus: NotRequired[str]
    MasterUsername: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    PreferredBackupWindow: NotRequired[str]
    BackupRetentionPeriod: NotRequired[int]
    DbSecurityGroups: NotRequired[Sequence[str]]
    DbParameterGroups: NotRequired[Sequence[AwsRdsDbParameterGroupTypeDef]]
    AvailabilityZone: NotRequired[str]
    DbSubnetGroup: NotRequired[AwsRdsDbSubnetGroupUnionTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[AwsRdsDbPendingModifiedValuesUnionTypeDef]
    LatestRestorableTime: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    ReadReplicaSourceDBInstanceIdentifier: NotRequired[str]
    ReadReplicaDBInstanceIdentifiers: NotRequired[Sequence[str]]
    ReadReplicaDBClusterIdentifiers: NotRequired[Sequence[str]]
    LicenseModel: NotRequired[str]
    Iops: NotRequired[int]
    OptionGroupMemberships: NotRequired[Sequence[AwsRdsDbOptionGroupMembershipTypeDef]]
    CharacterSetName: NotRequired[str]
    SecondaryAvailabilityZone: NotRequired[str]
    StatusInfos: NotRequired[Sequence[AwsRdsDbStatusInfoTypeDef]]
    StorageType: NotRequired[str]
    DomainMemberships: NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]]
    CopyTagsToSnapshot: NotRequired[bool]
    MonitoringInterval: NotRequired[int]
    MonitoringRoleArn: NotRequired[str]
    PromotionTier: NotRequired[int]
    Timezone: NotRequired[str]
    PerformanceInsightsEnabled: NotRequired[bool]
    PerformanceInsightsKmsKeyId: NotRequired[str]
    PerformanceInsightsRetentionPeriod: NotRequired[int]
    EnabledCloudWatchLogsExports: NotRequired[Sequence[str]]
    ProcessorFeatures: NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]]
    ListenerEndpoint: NotRequired[AwsRdsDbInstanceEndpointTypeDef]
    MaxAllocatedStorage: NotRequired[int]

AwsRedshiftClusterDetailsUnionTypeDef = Union[
    AwsRedshiftClusterDetailsTypeDef, AwsRedshiftClusterDetailsOutputTypeDef
]

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef(TypedDict):
    AbortIncompleteMultipartUpload: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
    ]
    ExpirationDate: NotRequired[str]
    ExpirationInDays: NotRequired[int]
    ExpiredObjectDeleteMarker: NotRequired[bool]
    Filter: NotRequired[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef]
    ID: NotRequired[str]
    NoncurrentVersionExpirationInDays: NotRequired[int]
    NoncurrentVersionTransitions: NotRequired[
        List[AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef]
    ]
    Prefix: NotRequired[str]
    Status: NotRequired[str]
    Transitions: NotRequired[
        List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
    ]

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef(TypedDict):
    Predicate: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnionTypeDef
    ]

class AwsS3BucketNotificationConfigurationOutputTypeDef(TypedDict):
    Configurations: NotRequired[List[AwsS3BucketNotificationConfigurationDetailOutputTypeDef]]

AwsS3BucketNotificationConfigurationFilterUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationFilterTypeDef,
    AwsS3BucketNotificationConfigurationFilterOutputTypeDef,
]
AwsStepFunctionStateMachineDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsUnionTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclDetailsUnionTypeDef = Union[
    AwsWafWebAclDetailsTypeDef, AwsWafWebAclDetailsOutputTypeDef
]
AwsWafv2ActionAllowDetailsUnionTypeDef = Union[
    AwsWafv2ActionAllowDetailsTypeDef, AwsWafv2ActionAllowDetailsOutputTypeDef
]
AwsWafv2RulesActionCaptchaDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionCaptchaDetailsTypeDef, AwsWafv2RulesActionCaptchaDetailsOutputTypeDef
]
AwsWafv2RulesActionCountDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionCountDetailsTypeDef, AwsWafv2RulesActionCountDetailsOutputTypeDef
]

class AwsWafv2RulesDetailsOutputTypeDef(TypedDict):
    Action: NotRequired[AwsWafv2RulesActionDetailsOutputTypeDef]
    Name: NotRequired[str]
    OverrideAction: NotRequired[str]
    Priority: NotRequired[int]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

AwsWafv2ActionBlockDetailsUnionTypeDef = Union[
    AwsWafv2ActionBlockDetailsTypeDef, AwsWafv2ActionBlockDetailsOutputTypeDef
]
VulnerabilityUnionTypeDef = Union[VulnerabilityTypeDef, VulnerabilityOutputTypeDef]

class GetSecurityControlDefinitionResponseTypeDef(TypedDict):
    SecurityControlDefinition: SecurityControlDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityControlDefinitionsResponseTypeDef(TypedDict):
    SecurityControlDefinitions: List[SecurityControlDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetAutomationRulesResponseTypeDef(TypedDict):
    Rules: List[AutomationRulesConfigTypeDef]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsResponseTypeDef(TypedDict):
    Insights: List[InsightTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateInsightRequestTypeDef(TypedDict):
    Name: str
    Filters: AwsSecurityFindingFiltersUnionTypeDef
    GroupByAttribute: str

class GetFindingsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[AwsSecurityFindingFiltersUnionTypeDef]
    SortCriteria: NotRequired[Sequence[SortCriterionTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetFindingsRequestTypeDef(TypedDict):
    Filters: NotRequired[AwsSecurityFindingFiltersUnionTypeDef]
    SortCriteria: NotRequired[Sequence[SortCriterionTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class UpdateFindingsRequestTypeDef(TypedDict):
    Filters: AwsSecurityFindingFiltersUnionTypeDef
    Note: NotRequired[NoteUpdateTypeDef]
    RecordState: NotRequired[RecordStateType]

class UpdateInsightRequestTypeDef(TypedDict):
    InsightArn: str
    Name: NotRequired[str]
    Filters: NotRequired[AwsSecurityFindingFiltersUnionTypeDef]
    GroupByAttribute: NotRequired[str]

SequenceUnionTypeDef = Union[SequenceTypeDef, SequenceOutputTypeDef]
NetworkHeaderUnionTypeDef = Union[NetworkHeaderTypeDef, NetworkHeaderOutputTypeDef]

class CustomDataIdentifiersResultOutputTypeDef(TypedDict):
    Detections: NotRequired[List[CustomDataIdentifiersDetectionsOutputTypeDef]]
    TotalCount: NotRequired[int]

class SensitiveDataResultOutputTypeDef(TypedDict):
    Category: NotRequired[str]
    Detections: NotRequired[List[SensitiveDataDetectionsOutputTypeDef]]
    TotalCount: NotRequired[int]

class CustomDataIdentifiersDetectionsTypeDef(TypedDict):
    Count: NotRequired[int]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Occurrences: NotRequired[OccurrencesUnionTypeDef]

SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesUnionTypeDef],
    },
)

class SecurityHubPolicyOutputTypeDef(TypedDict):
    ServiceEnabled: NotRequired[bool]
    EnabledStandardIdentifiers: NotRequired[List[str]]
    SecurityControlsConfiguration: NotRequired[SecurityControlsConfigurationOutputTypeDef]

class UpdateSecurityControlRequestTypeDef(TypedDict):
    SecurityControlId: str
    Parameters: Mapping[str, ParameterConfigurationUnionTypeDef]
    LastUpdateReason: NotRequired[str]

class SecurityControlsConfigurationTypeDef(TypedDict):
    EnabledSecurityControlIdentifiers: NotRequired[Sequence[str]]
    DisabledSecurityControlIdentifiers: NotRequired[Sequence[str]]
    SecurityControlCustomParameters: NotRequired[Sequence[SecurityControlCustomParameterTypeDef]]

class RuleGroupSourceStatelessRuleDefinitionTypeDef(TypedDict):
    Actions: NotRequired[Sequence[str]]
    MatchAttributes: NotRequired[RuleGroupSourceStatelessRuleMatchAttributesUnionTypeDef]

class FirewallPolicyDetailsOutputTypeDef(TypedDict):
    StatefulRuleGroupReferences: NotRequired[
        List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
    ]
    StatelessCustomActions: NotRequired[
        List[FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef]
    ]
    StatelessDefaultActions: NotRequired[List[str]]
    StatelessFragmentDefaultActions: NotRequired[List[str]]
    StatelessRuleGroupReferences: NotRequired[
        List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
    ]

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef(TypedDict):
    CustomActions: NotRequired[List[RuleGroupSourceCustomActionsDetailsOutputTypeDef]]
    StatelessRules: NotRequired[List[RuleGroupSourceStatelessRulesDetailsOutputTypeDef]]

StatelessCustomActionDefinitionUnionTypeDef = Union[
    StatelessCustomActionDefinitionTypeDef, StatelessCustomActionDefinitionOutputTypeDef
]

class ActionTypeDef(TypedDict):
    ActionType: NotRequired[str]
    NetworkConnectionAction: NotRequired[NetworkConnectionActionTypeDef]
    AwsApiCallAction: NotRequired[AwsApiCallActionUnionTypeDef]
    DnsRequestAction: NotRequired[DnsRequestActionTypeDef]
    PortProbeAction: NotRequired[PortProbeActionUnionTypeDef]

class CreateAutomationRuleRequestTypeDef(TypedDict):
    RuleOrder: int
    RuleName: str
    Description: str
    Criteria: AutomationRulesFindingFiltersUnionTypeDef
    Actions: Sequence[AutomationRulesActionUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    RuleStatus: NotRequired[RuleStatusType]
    IsTerminal: NotRequired[bool]

class UpdateAutomationRulesRequestItemTypeDef(TypedDict):
    RuleArn: str
    RuleStatus: NotRequired[RuleStatusType]
    RuleOrder: NotRequired[int]
    Description: NotRequired[str]
    RuleName: NotRequired[str]
    IsTerminal: NotRequired[bool]
    Criteria: NotRequired[AutomationRulesFindingFiltersUnionTypeDef]
    Actions: NotRequired[Sequence[AutomationRulesActionUnionTypeDef]]

class AwsAutoScalingAutoScalingGroupDetailsTypeDef(TypedDict):
    LaunchConfigurationName: NotRequired[str]
    LoadBalancerNames: NotRequired[Sequence[str]]
    HealthCheckType: NotRequired[str]
    HealthCheckGracePeriod: NotRequired[int]
    CreatedTime: NotRequired[str]
    MixedInstancesPolicy: NotRequired[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnionTypeDef
    ]
    AvailabilityZones: NotRequired[
        Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
    ]
    LaunchTemplate: NotRequired[
        AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
    ]
    CapacityRebalance: NotRequired[bool]

AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanBackupPlanDetailsTypeDef, AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef
]
AwsCertificateManagerCertificateDetailsUnionTypeDef = Union[
    AwsCertificateManagerCertificateDetailsTypeDef,
    AwsCertificateManagerCertificateDetailsOutputTypeDef,
]
AwsCloudFrontDistributionOriginGroupUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupTypeDef, AwsCloudFrontDistributionOriginGroupOutputTypeDef
]
AwsCloudFrontDistributionOriginItemUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginItemTypeDef, AwsCloudFrontDistributionOriginItemOutputTypeDef
]
AwsDynamoDbTableDetailsUnionTypeDef = Union[
    AwsDynamoDbTableDetailsTypeDef, AwsDynamoDbTableDetailsOutputTypeDef
]

class AwsEc2LaunchTemplateDetailsTypeDef(TypedDict):
    LaunchTemplateName: NotRequired[str]
    Id: NotRequired[str]
    LaunchTemplateData: NotRequired[AwsEc2LaunchTemplateDataDetailsUnionTypeDef]
    DefaultVersionNumber: NotRequired[int]
    LatestVersionNumber: NotRequired[int]

AwsEc2VpnConnectionDetailsUnionTypeDef = Union[
    AwsEc2VpnConnectionDetailsTypeDef, AwsEc2VpnConnectionDetailsOutputTypeDef
]
AwsEcsServiceDetailsUnionTypeDef = Union[
    AwsEcsServiceDetailsTypeDef, AwsEcsServiceDetailsOutputTypeDef
]
AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef,
    AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef,
]
AwsEksClusterDetailsUnionTypeDef = Union[
    AwsEksClusterDetailsTypeDef, AwsEksClusterDetailsOutputTypeDef
]
AwsGuardDutyDetectorDetailsUnionTypeDef = Union[
    AwsGuardDutyDetectorDetailsTypeDef, AwsGuardDutyDetectorDetailsOutputTypeDef
]
AwsMskClusterClusterInfoDetailsUnionTypeDef = Union[
    AwsMskClusterClusterInfoDetailsTypeDef, AwsMskClusterClusterInfoDetailsOutputTypeDef
]
AwsRdsDbInstanceDetailsUnionTypeDef = Union[
    AwsRdsDbInstanceDetailsTypeDef, AwsRdsDbInstanceDetailsOutputTypeDef
]

class AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef(TypedDict):
    Rules: NotRequired[List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef]]

AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef,
]
AwsS3BucketNotificationConfigurationDetailTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    {
        "Events": NotRequired[Sequence[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterUnionTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineDetailsUnionTypeDef = Union[
    AwsStepFunctionStateMachineDetailsTypeDef, AwsStepFunctionStateMachineDetailsOutputTypeDef
]

class AwsWafv2RuleGroupDetailsOutputTypeDef(TypedDict):
    Capacity: NotRequired[int]
    Description: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Rules: NotRequired[List[AwsWafv2RulesDetailsOutputTypeDef]]
    Scope: NotRequired[str]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

class AwsWafv2WebAclDetailsOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    ManagedbyFirewallManager: NotRequired[bool]
    Id: NotRequired[str]
    Capacity: NotRequired[int]
    CaptchaConfig: NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef]
    DefaultAction: NotRequired[AwsWafv2WebAclActionDetailsOutputTypeDef]
    Description: NotRequired[str]
    Rules: NotRequired[List[AwsWafv2RulesDetailsOutputTypeDef]]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

class AwsWafv2RulesActionDetailsTypeDef(TypedDict):
    Allow: NotRequired[AwsWafv2ActionAllowDetailsUnionTypeDef]
    Block: NotRequired[AwsWafv2ActionBlockDetailsUnionTypeDef]
    Captcha: NotRequired[AwsWafv2RulesActionCaptchaDetailsUnionTypeDef]
    Count: NotRequired[AwsWafv2RulesActionCountDetailsUnionTypeDef]

class AwsWafv2WebAclActionDetailsTypeDef(TypedDict):
    Allow: NotRequired[AwsWafv2ActionAllowDetailsUnionTypeDef]
    Block: NotRequired[AwsWafv2ActionBlockDetailsUnionTypeDef]

DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "Sequence": NotRequired[SequenceUnionTypeDef],
    },
)

class NetworkPathComponentTypeDef(TypedDict):
    ComponentId: NotRequired[str]
    ComponentType: NotRequired[str]
    Egress: NotRequired[NetworkHeaderUnionTypeDef]
    Ingress: NotRequired[NetworkHeaderUnionTypeDef]

class ClassificationResultOutputTypeDef(TypedDict):
    MimeType: NotRequired[str]
    SizeClassified: NotRequired[int]
    AdditionalOccurrences: NotRequired[bool]
    Status: NotRequired[ClassificationStatusTypeDef]
    SensitiveData: NotRequired[List[SensitiveDataResultOutputTypeDef]]
    CustomDataIdentifiers: NotRequired[CustomDataIdentifiersResultOutputTypeDef]

CustomDataIdentifiersDetectionsUnionTypeDef = Union[
    CustomDataIdentifiersDetectionsTypeDef, CustomDataIdentifiersDetectionsOutputTypeDef
]
SensitiveDataDetectionsUnionTypeDef = Union[
    SensitiveDataDetectionsTypeDef, SensitiveDataDetectionsOutputTypeDef
]

class PolicyOutputTypeDef(TypedDict):
    SecurityHub: NotRequired[SecurityHubPolicyOutputTypeDef]

class SecurityHubPolicyTypeDef(TypedDict):
    ServiceEnabled: NotRequired[bool]
    EnabledStandardIdentifiers: NotRequired[Sequence[str]]
    SecurityControlsConfiguration: NotRequired[SecurityControlsConfigurationTypeDef]

RuleGroupSourceStatelessRuleDefinitionUnionTypeDef = Union[
    RuleGroupSourceStatelessRuleDefinitionTypeDef,
    RuleGroupSourceStatelessRuleDefinitionOutputTypeDef,
]

class AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef(TypedDict):
    FirewallPolicy: NotRequired[FirewallPolicyDetailsOutputTypeDef]
    FirewallPolicyArn: NotRequired[str]
    FirewallPolicyId: NotRequired[str]
    FirewallPolicyName: NotRequired[str]
    Description: NotRequired[str]

class RuleGroupSourceOutputTypeDef(TypedDict):
    RulesSourceList: NotRequired[RuleGroupSourceListDetailsOutputTypeDef]
    RulesString: NotRequired[str]
    StatefulRules: NotRequired[List[RuleGroupSourceStatefulRulesDetailsOutputTypeDef]]
    StatelessRulesAndCustomActions: NotRequired[
        RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef
    ]

class FirewallPolicyStatelessCustomActionsDetailsTypeDef(TypedDict):
    ActionDefinition: NotRequired[StatelessCustomActionDefinitionUnionTypeDef]
    ActionName: NotRequired[str]

class RuleGroupSourceCustomActionsDetailsTypeDef(TypedDict):
    ActionDefinition: NotRequired[StatelessCustomActionDefinitionUnionTypeDef]
    ActionName: NotRequired[str]

ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]

class BatchUpdateAutomationRulesRequestTypeDef(TypedDict):
    UpdateAutomationRulesRequestItems: Sequence[UpdateAutomationRulesRequestItemTypeDef]

AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef = Union[
    AwsAutoScalingAutoScalingGroupDetailsTypeDef, AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef
]

class AwsBackupBackupPlanDetailsTypeDef(TypedDict):
    BackupPlan: NotRequired[AwsBackupBackupPlanBackupPlanDetailsUnionTypeDef]
    BackupPlanArn: NotRequired[str]
    BackupPlanId: NotRequired[str]
    VersionId: NotRequired[str]

class AwsCloudFrontDistributionOriginGroupsTypeDef(TypedDict):
    Items: NotRequired[Sequence[AwsCloudFrontDistributionOriginGroupUnionTypeDef]]

class AwsCloudFrontDistributionOriginsTypeDef(TypedDict):
    Items: NotRequired[Sequence[AwsCloudFrontDistributionOriginItemUnionTypeDef]]

AwsEc2LaunchTemplateDetailsUnionTypeDef = Union[
    AwsEc2LaunchTemplateDetailsTypeDef, AwsEc2LaunchTemplateDetailsOutputTypeDef
]

class AwsEcsTaskDefinitionDetailsTypeDef(TypedDict):
    ContainerDefinitions: NotRequired[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsUnionTypeDef]
    ]
    Cpu: NotRequired[str]
    ExecutionRoleArn: NotRequired[str]
    Family: NotRequired[str]
    InferenceAccelerators: NotRequired[
        Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
    ]
    IpcMode: NotRequired[str]
    Memory: NotRequired[str]
    NetworkMode: NotRequired[str]
    PidMode: NotRequired[str]
    PlacementConstraints: NotRequired[
        Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]
    ]
    ProxyConfiguration: NotRequired[AwsEcsTaskDefinitionProxyConfigurationDetailsUnionTypeDef]
    RequiresCompatibilities: NotRequired[Sequence[str]]
    TaskRoleArn: NotRequired[str]
    Volumes: NotRequired[Sequence[AwsEcsTaskDefinitionVolumesDetailsUnionTypeDef]]
    Status: NotRequired[str]

class AwsMskClusterDetailsTypeDef(TypedDict):
    ClusterInfo: NotRequired[AwsMskClusterClusterInfoDetailsUnionTypeDef]

class AwsS3BucketDetailsOutputTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    OwnerName: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    CreatedAt: NotRequired[str]
    ServerSideEncryptionConfiguration: NotRequired[
        AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef
    ]
    BucketLifecycleConfiguration: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef
    ]
    PublicAccessBlockConfiguration: NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef]
    AccessControlList: NotRequired[str]
    BucketLoggingConfiguration: NotRequired[AwsS3BucketLoggingConfigurationTypeDef]
    BucketWebsiteConfiguration: NotRequired[AwsS3BucketWebsiteConfigurationOutputTypeDef]
    BucketNotificationConfiguration: NotRequired[AwsS3BucketNotificationConfigurationOutputTypeDef]
    BucketVersioningConfiguration: NotRequired[AwsS3BucketBucketVersioningConfigurationTypeDef]
    ObjectLockConfiguration: NotRequired[AwsS3BucketObjectLockConfigurationTypeDef]
    Name: NotRequired[str]

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef(TypedDict):
    AbortIncompleteMultipartUpload: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
    ]
    ExpirationDate: NotRequired[str]
    ExpirationInDays: NotRequired[int]
    ExpiredObjectDeleteMarker: NotRequired[bool]
    Filter: NotRequired[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnionTypeDef]
    ID: NotRequired[str]
    NoncurrentVersionExpirationInDays: NotRequired[int]
    NoncurrentVersionTransitions: NotRequired[
        Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
        ]
    ]
    Prefix: NotRequired[str]
    Status: NotRequired[str]
    Transitions: NotRequired[
        Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
    ]

AwsS3BucketNotificationConfigurationDetailUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationDetailTypeDef,
    AwsS3BucketNotificationConfigurationDetailOutputTypeDef,
]
AwsWafv2RulesActionDetailsUnionTypeDef = Union[
    AwsWafv2RulesActionDetailsTypeDef, AwsWafv2RulesActionDetailsOutputTypeDef
]
AwsWafv2WebAclActionDetailsUnionTypeDef = Union[
    AwsWafv2WebAclActionDetailsTypeDef, AwsWafv2WebAclActionDetailsOutputTypeDef
]
DetectionUnionTypeDef = Union[DetectionTypeDef, DetectionOutputTypeDef]
NetworkPathComponentUnionTypeDef = Union[
    NetworkPathComponentTypeDef, NetworkPathComponentOutputTypeDef
]

class DataClassificationDetailsOutputTypeDef(TypedDict):
    DetailedResultsLocation: NotRequired[str]
    Result: NotRequired[ClassificationResultOutputTypeDef]

class CustomDataIdentifiersResultTypeDef(TypedDict):
    Detections: NotRequired[Sequence[CustomDataIdentifiersDetectionsUnionTypeDef]]
    TotalCount: NotRequired[int]

class SensitiveDataResultTypeDef(TypedDict):
    Category: NotRequired[str]
    Detections: NotRequired[Sequence[SensitiveDataDetectionsUnionTypeDef]]
    TotalCount: NotRequired[int]

class CreateConfigurationPolicyResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigurationPolicyResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyTypeDef(TypedDict):
    SecurityHub: NotRequired[SecurityHubPolicyTypeDef]

class RuleGroupSourceStatelessRulesDetailsTypeDef(TypedDict):
    Priority: NotRequired[int]
    RuleDefinition: NotRequired[RuleGroupSourceStatelessRuleDefinitionUnionTypeDef]

class RuleGroupDetailsOutputTypeDef(TypedDict):
    RuleVariables: NotRequired[RuleGroupVariablesOutputTypeDef]
    RulesSource: NotRequired[RuleGroupSourceOutputTypeDef]

FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef = Union[
    FirewallPolicyStatelessCustomActionsDetailsTypeDef,
    FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef,
]
RuleGroupSourceCustomActionsDetailsUnionTypeDef = Union[
    RuleGroupSourceCustomActionsDetailsTypeDef, RuleGroupSourceCustomActionsDetailsOutputTypeDef
]
AwsBackupBackupPlanDetailsUnionTypeDef = Union[
    AwsBackupBackupPlanDetailsTypeDef, AwsBackupBackupPlanDetailsOutputTypeDef
]
AwsCloudFrontDistributionOriginGroupsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginGroupsTypeDef, AwsCloudFrontDistributionOriginGroupsOutputTypeDef
]
AwsCloudFrontDistributionOriginsUnionTypeDef = Union[
    AwsCloudFrontDistributionOriginsTypeDef, AwsCloudFrontDistributionOriginsOutputTypeDef
]
AwsEcsTaskDefinitionDetailsUnionTypeDef = Union[
    AwsEcsTaskDefinitionDetailsTypeDef, AwsEcsTaskDefinitionDetailsOutputTypeDef
]
AwsMskClusterDetailsUnionTypeDef = Union[
    AwsMskClusterDetailsTypeDef, AwsMskClusterDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef,
]

class AwsS3BucketNotificationConfigurationTypeDef(TypedDict):
    Configurations: NotRequired[Sequence[AwsS3BucketNotificationConfigurationDetailUnionTypeDef]]

class AwsWafv2RulesDetailsTypeDef(TypedDict):
    Action: NotRequired[AwsWafv2RulesActionDetailsUnionTypeDef]
    Name: NotRequired[str]
    OverrideAction: NotRequired[str]
    Priority: NotRequired[int]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

CustomDataIdentifiersResultUnionTypeDef = Union[
    CustomDataIdentifiersResultTypeDef, CustomDataIdentifiersResultOutputTypeDef
]
SensitiveDataResultUnionTypeDef = Union[
    SensitiveDataResultTypeDef, SensitiveDataResultOutputTypeDef
]
PolicyUnionTypeDef = Union[PolicyTypeDef, PolicyOutputTypeDef]
RuleGroupSourceStatelessRulesDetailsUnionTypeDef = Union[
    RuleGroupSourceStatelessRulesDetailsTypeDef, RuleGroupSourceStatelessRulesDetailsOutputTypeDef
]
AwsNetworkFirewallRuleGroupDetailsOutputTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsOutputTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsOutputTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class FirewallPolicyDetailsTypeDef(TypedDict):
    StatefulRuleGroupReferences: NotRequired[
        Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
    ]
    StatelessCustomActions: NotRequired[
        Sequence[FirewallPolicyStatelessCustomActionsDetailsUnionTypeDef]
    ]
    StatelessDefaultActions: NotRequired[Sequence[str]]
    StatelessFragmentDefaultActions: NotRequired[Sequence[str]]
    StatelessRuleGroupReferences: NotRequired[
        Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
    ]

class AwsCloudFrontDistributionDetailsTypeDef(TypedDict):
    CacheBehaviors: NotRequired[AwsCloudFrontDistributionCacheBehaviorsUnionTypeDef]
    DefaultCacheBehavior: NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef]
    DefaultRootObject: NotRequired[str]
    DomainName: NotRequired[str]
    ETag: NotRequired[str]
    LastModifiedTime: NotRequired[str]
    Logging: NotRequired[AwsCloudFrontDistributionLoggingTypeDef]
    Origins: NotRequired[AwsCloudFrontDistributionOriginsUnionTypeDef]
    OriginGroups: NotRequired[AwsCloudFrontDistributionOriginGroupsUnionTypeDef]
    ViewerCertificate: NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef]
    Status: NotRequired[str]
    WebAclId: NotRequired[str]

class AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef(TypedDict):
    Rules: NotRequired[Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnionTypeDef]]

AwsS3BucketNotificationConfigurationUnionTypeDef = Union[
    AwsS3BucketNotificationConfigurationTypeDef, AwsS3BucketNotificationConfigurationOutputTypeDef
]
AwsWafv2RulesDetailsUnionTypeDef = Union[
    AwsWafv2RulesDetailsTypeDef, AwsWafv2RulesDetailsOutputTypeDef
]

class AwsWafv2WebAclDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    ManagedbyFirewallManager: NotRequired[bool]
    Id: NotRequired[str]
    Capacity: NotRequired[int]
    CaptchaConfig: NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef]
    DefaultAction: NotRequired[AwsWafv2WebAclActionDetailsUnionTypeDef]
    Description: NotRequired[str]
    Rules: NotRequired[Sequence[AwsWafv2RulesDetailsTypeDef]]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

class ClassificationResultTypeDef(TypedDict):
    MimeType: NotRequired[str]
    SizeClassified: NotRequired[int]
    AdditionalOccurrences: NotRequired[bool]
    Status: NotRequired[ClassificationStatusTypeDef]
    SensitiveData: NotRequired[Sequence[SensitiveDataResultUnionTypeDef]]
    CustomDataIdentifiers: NotRequired[CustomDataIdentifiersResultUnionTypeDef]

class CreateConfigurationPolicyRequestTypeDef(TypedDict):
    Name: str
    ConfigurationPolicy: PolicyUnionTypeDef
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateConfigurationPolicyRequestTypeDef(TypedDict):
    Identifier: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    UpdatedReason: NotRequired[str]
    ConfigurationPolicy: NotRequired[PolicyUnionTypeDef]

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef(TypedDict):
    CustomActions: NotRequired[Sequence[RuleGroupSourceCustomActionsDetailsUnionTypeDef]]
    StatelessRules: NotRequired[Sequence[RuleGroupSourceStatelessRulesDetailsUnionTypeDef]]

ResourceDetailsOutputTypeDef = TypedDict(
    "ResourceDetailsOutputTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef
        ],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsOutputTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsOutputTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsOutputTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsOutputTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsOutputTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsOutputTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsOutputTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsOutputTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsOutputTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsOutputTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef
        ],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsOutputTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsOutputTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsOutputTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsOutputTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsOutputTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsOutputTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsOutputTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsOutputTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsOutputTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsOutputTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsOutputTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsOutputTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsOutputTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsOutputTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsOutputTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsOutputTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsOutputTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsOutputTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsOutputTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsOutputTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsOutputTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsOutputTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsOutputTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsOutputTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsOutputTypeDef],
        "Container": NotRequired[ContainerDetailsOutputTypeDef],
        "Other": NotRequired[Dict[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsOutputTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsOutputTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsOutputTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsOutputTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[AwsOpenSearchServiceDomainDetailsOutputTypeDef],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsOutputTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsOutputTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[AwsWafRegionalRateBasedRuleDetailsOutputTypeDef],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsOutputTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[AwsNetworkFirewallFirewallDetailsOutputTypeDef],
        "AwsNetworkFirewallRuleGroup": NotRequired[AwsNetworkFirewallRuleGroupDetailsOutputTypeDef],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsOutputTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsOutputTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsOutputTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsOutputTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsOutputTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[AwsEc2VpcPeeringConnectionDetailsOutputTypeDef],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsOutputTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsOutputTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsOutputTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsOutputTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsOutputTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsOutputTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsOutputTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsOutputTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsOutputTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[
            AwsSageMakerNotebookInstanceDetailsOutputTypeDef
        ],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsOutputTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsOutputTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsOutputTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsOutputTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsOutputTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsOutputTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[AwsStepFunctionStateMachineDetailsOutputTypeDef],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsOutputTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsOutputTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsOutputTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsOutputTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsOutputTypeDef],
    },
)
FirewallPolicyDetailsUnionTypeDef = Union[
    FirewallPolicyDetailsTypeDef, FirewallPolicyDetailsOutputTypeDef
]
AwsCloudFrontDistributionDetailsUnionTypeDef = Union[
    AwsCloudFrontDistributionDetailsTypeDef, AwsCloudFrontDistributionDetailsOutputTypeDef
]
AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef = Union[
    AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef,
    AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef,
]

class AwsWafv2RuleGroupDetailsTypeDef(TypedDict):
    Capacity: NotRequired[int]
    Description: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Rules: NotRequired[Sequence[AwsWafv2RulesDetailsUnionTypeDef]]
    Scope: NotRequired[str]
    VisibilityConfig: NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef]

AwsWafv2WebAclDetailsUnionTypeDef = Union[
    AwsWafv2WebAclDetailsTypeDef, AwsWafv2WebAclDetailsOutputTypeDef
]
ClassificationResultUnionTypeDef = Union[
    ClassificationResultTypeDef, ClassificationResultOutputTypeDef
]
RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef = Union[
    RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef,
    RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef,
]
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsOutputTypeDef],
        "Details": NotRequired[ResourceDetailsOutputTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)

class AwsNetworkFirewallFirewallPolicyDetailsTypeDef(TypedDict):
    FirewallPolicy: NotRequired[FirewallPolicyDetailsUnionTypeDef]
    FirewallPolicyArn: NotRequired[str]
    FirewallPolicyId: NotRequired[str]
    FirewallPolicyName: NotRequired[str]
    Description: NotRequired[str]

class AwsS3BucketDetailsTypeDef(TypedDict):
    OwnerId: NotRequired[str]
    OwnerName: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    CreatedAt: NotRequired[str]
    ServerSideEncryptionConfiguration: NotRequired[
        AwsS3BucketServerSideEncryptionConfigurationUnionTypeDef
    ]
    BucketLifecycleConfiguration: NotRequired[
        AwsS3BucketBucketLifecycleConfigurationDetailsUnionTypeDef
    ]
    PublicAccessBlockConfiguration: NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef]
    AccessControlList: NotRequired[str]
    BucketLoggingConfiguration: NotRequired[AwsS3BucketLoggingConfigurationTypeDef]
    BucketWebsiteConfiguration: NotRequired[AwsS3BucketWebsiteConfigurationUnionTypeDef]
    BucketNotificationConfiguration: NotRequired[AwsS3BucketNotificationConfigurationUnionTypeDef]
    BucketVersioningConfiguration: NotRequired[AwsS3BucketBucketVersioningConfigurationTypeDef]
    ObjectLockConfiguration: NotRequired[AwsS3BucketObjectLockConfigurationTypeDef]
    Name: NotRequired[str]

AwsWafv2RuleGroupDetailsUnionTypeDef = Union[
    AwsWafv2RuleGroupDetailsTypeDef, AwsWafv2RuleGroupDetailsOutputTypeDef
]

class DataClassificationDetailsTypeDef(TypedDict):
    DetailedResultsLocation: NotRequired[str]
    Result: NotRequired[ClassificationResultUnionTypeDef]

class RuleGroupSourceTypeDef(TypedDict):
    RulesSourceList: NotRequired[RuleGroupSourceListDetailsUnionTypeDef]
    RulesString: NotRequired[str]
    StatefulRules: NotRequired[Sequence[RuleGroupSourceStatefulRulesDetailsUnionTypeDef]]
    StatelessRulesAndCustomActions: NotRequired[
        RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnionTypeDef
    ]

class AwsSecurityFindingOutputTypeDef(TypedDict):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceOutputTypeDef]
    ProductName: NotRequired[str]
    CompanyName: NotRequired[str]
    Region: NotRequired[str]
    Types: NotRequired[List[str]]
    FirstObservedAt: NotRequired[str]
    LastObservedAt: NotRequired[str]
    Severity: NotRequired[SeverityTypeDef]
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    Remediation: NotRequired[RemediationTypeDef]
    SourceUrl: NotRequired[str]
    ProductFields: NotRequired[Dict[str, str]]
    UserDefinedFields: NotRequired[Dict[str, str]]
    Malware: NotRequired[List[MalwareTypeDef]]
    Network: NotRequired[NetworkTypeDef]
    NetworkPath: NotRequired[List[NetworkPathComponentOutputTypeDef]]
    Process: NotRequired[ProcessDetailsTypeDef]
    Threats: NotRequired[List[ThreatOutputTypeDef]]
    ThreatIntelIndicators: NotRequired[List[ThreatIntelIndicatorTypeDef]]
    Compliance: NotRequired[ComplianceOutputTypeDef]
    VerificationState: NotRequired[VerificationStateType]
    WorkflowState: NotRequired[WorkflowStateType]
    Workflow: NotRequired[WorkflowTypeDef]
    RecordState: NotRequired[RecordStateType]
    RelatedFindings: NotRequired[List[RelatedFindingTypeDef]]
    Note: NotRequired[NoteTypeDef]
    Vulnerabilities: NotRequired[List[VulnerabilityOutputTypeDef]]
    PatchSummary: NotRequired[PatchSummaryTypeDef]
    Action: NotRequired[ActionOutputTypeDef]
    FindingProviderFields: NotRequired[FindingProviderFieldsOutputTypeDef]
    Sample: NotRequired[bool]
    GeneratorDetails: NotRequired[GeneratorDetailsOutputTypeDef]
    ProcessedAt: NotRequired[str]
    AwsAccountName: NotRequired[str]
    Detection: NotRequired[DetectionOutputTypeDef]

AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef = Union[
    AwsNetworkFirewallFirewallPolicyDetailsTypeDef,
    AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef,
]
AwsS3BucketDetailsUnionTypeDef = Union[AwsS3BucketDetailsTypeDef, AwsS3BucketDetailsOutputTypeDef]
DataClassificationDetailsUnionTypeDef = Union[
    DataClassificationDetailsTypeDef, DataClassificationDetailsOutputTypeDef
]
RuleGroupSourceUnionTypeDef = Union[RuleGroupSourceTypeDef, RuleGroupSourceOutputTypeDef]

class GetFindingsResponseTypeDef(TypedDict):
    Findings: List[AwsSecurityFindingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RuleGroupDetailsTypeDef(TypedDict):
    RuleVariables: NotRequired[RuleGroupVariablesUnionTypeDef]
    RulesSource: NotRequired[RuleGroupSourceUnionTypeDef]

RuleGroupDetailsUnionTypeDef = Union[RuleGroupDetailsTypeDef, RuleGroupDetailsOutputTypeDef]
AwsNetworkFirewallRuleGroupDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsUnionTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsNetworkFirewallRuleGroupDetailsUnionTypeDef = Union[
    AwsNetworkFirewallRuleGroupDetailsTypeDef, AwsNetworkFirewallRuleGroupDetailsOutputTypeDef
]
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            AwsAutoScalingAutoScalingGroupDetailsUnionTypeDef
        ],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsUnionTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsUnionTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsUnionTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsUnionTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsUnionTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsUnionTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsUnionTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsUnionTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsUnionTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsUnionTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            AwsElasticBeanstalkEnvironmentDetailsUnionTypeDef
        ],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsUnionTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsUnionTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsUnionTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsUnionTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsUnionTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsUnionTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsUnionTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsUnionTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsUnionTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsUnionTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsUnionTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsUnionTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsUnionTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsUnionTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsUnionTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsUnionTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsUnionTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsUnionTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsUnionTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsUnionTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsUnionTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsUnionTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsUnionTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsUnionTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsUnionTypeDef],
        "Container": NotRequired[ContainerDetailsUnionTypeDef],
        "Other": NotRequired[Mapping[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsUnionTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsUnionTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsUnionTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsUnionTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsUnionTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[AwsOpenSearchServiceDomainDetailsUnionTypeDef],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsUnionTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsUnionTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[AwsWafRegionalRateBasedRuleDetailsUnionTypeDef],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsUnionTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsUnionTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[AwsNetworkFirewallFirewallDetailsUnionTypeDef],
        "AwsNetworkFirewallRuleGroup": NotRequired[AwsNetworkFirewallRuleGroupDetailsUnionTypeDef],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsUnionTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsUnionTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsUnionTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsUnionTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsUnionTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[AwsEc2VpcPeeringConnectionDetailsUnionTypeDef],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsUnionTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsUnionTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsUnionTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsUnionTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsUnionTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsUnionTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsUnionTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsUnionTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsUnionTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[
            AwsSageMakerNotebookInstanceDetailsUnionTypeDef
        ],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsUnionTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsUnionTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsUnionTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsUnionTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsUnionTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsUnionTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[AwsStepFunctionStateMachineDetailsUnionTypeDef],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsUnionTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsUnionTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsUnionTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsUnionTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsUnionTypeDef],
    },
)
ResourceDetailsUnionTypeDef = Union[ResourceDetailsTypeDef, ResourceDetailsOutputTypeDef]
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsUnionTypeDef],
        "Details": NotRequired[ResourceDetailsUnionTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]

class AwsSecurityFindingTypeDef(TypedDict):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: Sequence[ResourceUnionTypeDef]
    ProductName: NotRequired[str]
    CompanyName: NotRequired[str]
    Region: NotRequired[str]
    Types: NotRequired[Sequence[str]]
    FirstObservedAt: NotRequired[str]
    LastObservedAt: NotRequired[str]
    Severity: NotRequired[SeverityTypeDef]
    Confidence: NotRequired[int]
    Criticality: NotRequired[int]
    Remediation: NotRequired[RemediationTypeDef]
    SourceUrl: NotRequired[str]
    ProductFields: NotRequired[Mapping[str, str]]
    UserDefinedFields: NotRequired[Mapping[str, str]]
    Malware: NotRequired[Sequence[MalwareTypeDef]]
    Network: NotRequired[NetworkTypeDef]
    NetworkPath: NotRequired[Sequence[NetworkPathComponentUnionTypeDef]]
    Process: NotRequired[ProcessDetailsTypeDef]
    Threats: NotRequired[Sequence[ThreatUnionTypeDef]]
    ThreatIntelIndicators: NotRequired[Sequence[ThreatIntelIndicatorTypeDef]]
    Compliance: NotRequired[ComplianceUnionTypeDef]
    VerificationState: NotRequired[VerificationStateType]
    WorkflowState: NotRequired[WorkflowStateType]
    Workflow: NotRequired[WorkflowTypeDef]
    RecordState: NotRequired[RecordStateType]
    RelatedFindings: NotRequired[Sequence[RelatedFindingTypeDef]]
    Note: NotRequired[NoteTypeDef]
    Vulnerabilities: NotRequired[Sequence[VulnerabilityUnionTypeDef]]
    PatchSummary: NotRequired[PatchSummaryTypeDef]
    Action: NotRequired[ActionUnionTypeDef]
    FindingProviderFields: NotRequired[FindingProviderFieldsUnionTypeDef]
    Sample: NotRequired[bool]
    GeneratorDetails: NotRequired[GeneratorDetailsUnionTypeDef]
    ProcessedAt: NotRequired[str]
    AwsAccountName: NotRequired[str]
    Detection: NotRequired[DetectionUnionTypeDef]

AwsSecurityFindingUnionTypeDef = Union[AwsSecurityFindingTypeDef, AwsSecurityFindingOutputTypeDef]

class BatchImportFindingsRequestTypeDef(TypedDict):
    Findings: Sequence[AwsSecurityFindingUnionTypeDef]
